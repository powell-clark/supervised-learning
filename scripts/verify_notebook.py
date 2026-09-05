#!/usr/bin/env python3
"""Mechanical quality verifier for the curriculum notebooks.

Turns the CURRICULUM_ROADMAP.md quality checklist into a program: it measures
each notebook, applies the theory/practical thresholds, optionally executes the
notebook under memory and thread guards, writes a JSON report per notebook and
exits non-zero when anything is below the bar.

Usage:
    verify_notebook.py <notebook.ipynb>... [--all] [--type theory|practical|auto]
                       [--execute] [--timeout SECONDS] [--report-dir reports/verify]
                       [--record-feature FEAT-ID] [--json] [--syntax-only]
                       [--min-free-mb MB] [--max-mem-mb MB] [--threads N]

Exit code is 0 only when every checked notebook passes every check.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

THEORY_MIN_SPANS = 100
PRACTICAL_MIN_SPANS = 20

DEFAULT_TIMEOUT = 900
DEFAULT_REPORT_DIR = "reports/verify"
DEFAULT_MIN_FREE_MB = 3000
DEFAULT_MAX_MEM_MB = 2048
DEFAULT_THREADS = 4
KERNEL_NAME = "supervised-learning"

THREAD_ENV_VARS = (
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
)


# --------------------------------------------------------------------------
# metrics
# --------------------------------------------------------------------------

_ENV_RE = re.compile(r"\\begin\{(equation|align|aligned|gather)\*?\}")

# Codepoint ranges that count as decoration. The mathematical operators the
# curriculum legitimately uses (see _MATH_EXEMPT) sit outside these ranges by
# construction, and are excluded explicitly so a future range widening cannot
# silently start penalising mathematics.
_EMOJI_RANGES = ((0x1F000, 0x1FAFF), (0x2600, 0x27BF))
_EMOJI_SINGLES = frozenset({0xFE0F, 0x200D})
_MATH_EXEMPT = frozenset("⟺⟹≤≥≠∈∑∏∂∇")

_MARKETING_TERMS = (
    "breakthrough",
    "revolutionary",
    "game-changing",
    "cutting-edge",
    "industry-standard",
    "state of the art",
    "awesome",
    "amazing",
    "most important",
    "unlock",
    "supercharge",
)
_MARKETING_RE = re.compile(
    "|".join(r"\b" + t.replace(" ", r"\s+").replace("-", r"[-\s]") + r"\b" for t in _MARKETING_TERMS),
    re.IGNORECASE,
)

_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s*(.+?)\s*$", re.MULTILINE)
_REFERENCES_RE = re.compile(r"further\s+reading|references", re.IGNORECASE)


def _find_unescaped_dollar(text: str, start: int) -> int:
    i = start
    n = len(text)
    while i < n:
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "$":
            return i
        i += 1
    return -1


def scan_latex(text: str) -> tuple:
    """Tokenise mathematical spans. Returns (total_spans, display_dollar_blocks).

    ``$$...$$`` is one span, not two ``$...$`` spans; ``\\$`` is currency, not
    mathematics; an unterminated delimiter opens no span. The second figure is
    reported separately because a naive ``text.count('$') // 2`` — the method
    that produced the STORY-SL12 measurement table — counts each ``$$`` block
    twice, so ``naive == total_spans + display_dollar_blocks`` for a purely
    dollar-delimited notebook.
    """
    count = 0
    display = 0
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == "\\":
            m = _ENV_RE.match(text, i)
            if m:
                env = m.group(1)
                end = text.find("\\end{" + env, m.end())
                count += 1
                i = (end + 1) if end != -1 else m.end()
                continue
            if text.startswith("\\(", i):
                end = text.find("\\)", i + 2)
                if end != -1:
                    count += 1
                    i = end + 2
                    continue
                i += 2
                continue
            if text.startswith("\\[", i):
                end = text.find("\\]", i + 2)
                if end != -1:
                    count += 1
                    i = end + 2
                    continue
                i += 2
                continue
            i += 2
            continue
        if ch == "$":
            if text.startswith("$$", i):
                end = text.find("$$", i + 2)
                if end != -1:
                    count += 1
                    display += 1
                    i = end + 2
                    continue
                i += 2
                continue
            end = _find_unescaped_dollar(text, i + 1)
            if end != -1:
                count += 1
                i = end + 1
                continue
            i += 1
            continue
        i += 1
    return count, display


def count_latex_spans(text: str) -> int:
    return scan_latex(text)[0]


def count_emoji(text: str) -> int:
    total = 0
    for ch in text:
        if ch in _MATH_EXEMPT:
            continue
        cp = ord(ch)
        if cp in _EMOJI_SINGLES:
            total += 1
            continue
        for lo, hi in _EMOJI_RANGES:
            if lo <= cp <= hi:
                total += 1
                break
    return total


def count_marketing(text: str) -> int:
    return len(_MARKETING_RE.findall(text))


def cell_source(cell: dict) -> str:
    src = cell.get("source", "")
    if isinstance(src, list):
        return "".join(src)
    return src or ""


def classify(path: Path, forced: str = "auto") -> str:
    """theory for ``<N>a_*``; practical for ``<N>b_``..``<N>f_`` unless the
    filename says theory."""
    if forced in ("theory", "practical"):
        return forced
    name = path.name
    if "theory" in name.lower():
        return "theory"
    m = re.match(r"^\d+([a-f])_", name)
    if m and m.group(1) == "a":
        return "theory"
    if m:
        return "practical"
    return "practical"


def read_notebook(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def compute_metrics(nb: dict, path: Path) -> dict:
    cells = nb.get("cells", [])
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]

    markdown_text = "\n".join(cell_source(c) for c in markdown_cells)
    code_text = "\n".join(cell_source(c) for c in code_cells)
    all_text = markdown_text + "\n" + code_text

    error_outputs = 0
    for cell in code_cells:
        for out in cell.get("outputs", []) or []:
            if out.get("output_type") == "error":
                error_outputs += 1

    has_title = False
    if cells:
        first = cells[0]
        if first.get("cell_type") == "markdown":
            first_line = cell_source(first).lstrip().splitlines()[0] if cell_source(first).strip() else ""
            has_title = bool(re.match(r"^#\s+Lesson\b", first_line))

    has_references = any(
        _REFERENCES_RE.search(heading) for heading in _HEADING_RE.findall(markdown_text)
    )

    executed = bool(code_cells) and all(
        c.get("execution_count") is not None for c in code_cells
    )

    total_spans, display_blocks = scan_latex(markdown_text)

    return {
        "latex_spans": total_spans,
        "display_dollar_blocks": display_blocks,
        "code_cells": len(code_cells),
        "markdown_cells": len(markdown_cells),
        "bytes": path.stat().st_size,
        "emoji_count": count_emoji(all_text),
        "marketing_hits": count_marketing(all_text),
        "error_outputs": error_outputs,
        "has_title": has_title,
        "has_references": has_references,
        "executed": executed,
    }


def syntax_errors(nb: dict) -> list:
    """The only surviving behaviour of the retired test_notebooks.py."""
    problems = []
    for idx, cell in enumerate(c for c in nb.get("cells", []) if c.get("cell_type") == "code"):
        code = cell_source(cell)
        stripped = code.strip()
        if not stripped or stripped.startswith("%") or stripped.startswith("!"):
            continue
        try:
            ast.parse(code)
        except SyntaxError as exc:
            problems.append(f"code cell {idx}: {exc.msg} at line {exc.lineno}")
        except Exception:  # noqa: BLE001 - non-standalone fragments are not our business
            pass
    return problems


def apply_thresholds(metrics: dict, ntype: str, executed_requested: bool) -> list:
    min_spans = THEORY_MIN_SPANS if ntype == "theory" else PRACTICAL_MIN_SPANS
    checks = [
        {
            "name": "latex_spans",
            "ok": metrics["latex_spans"] >= min_spans,
            "detail": f"{metrics['latex_spans']} spans (>= {min_spans} for {ntype})",
        },
        {
            "name": "emoji_count",
            "ok": metrics["emoji_count"] == 0,
            "detail": f"{metrics['emoji_count']} emoji codepoints (== 0)",
        },
        {
            "name": "marketing_hits",
            "ok": metrics["marketing_hits"] == 0,
            "detail": f"{metrics['marketing_hits']} marketing matches (== 0)",
        },
        {
            "name": "has_title",
            "ok": metrics["has_title"],
            "detail": "first cell is an H1 starting '# Lesson'",
        },
        {
            "name": "has_references",
            "ok": metrics["has_references"],
            "detail": "a 'Further reading' or 'References' heading exists",
        },
    ]
    if executed_requested:
        checks.append(
            {
                "name": "error_outputs",
                "ok": metrics["error_outputs"] == 0,
                "detail": f"{metrics['error_outputs']} error outputs (== 0)",
            }
        )
        checks.append(
            {
                "name": "executed",
                "ok": metrics["executed"],
                "detail": "every code cell carries an execution_count",
            }
        )
    return checks


# --------------------------------------------------------------------------
# execution, under host resource guards
# --------------------------------------------------------------------------


def mem_available_mb() -> int:
    with open("/proc/meminfo", "r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) // 1024
    raise RuntimeError("MemAvailable missing from /proc/meminfo")


class limited_address_space:
    """Cap RLIMIT_AS for this process and everything it launches.

    The kernel is a child of this process, so it inherits the cap at fork; a
    runaway allocation inside the notebook raises MemoryError there while the
    machine still has room to breathe.
    """

    def __init__(self, max_bytes: int):
        self.max_bytes = max_bytes
        self.previous = None

    def __enter__(self):
        self.previous = resource.getrlimit(resource.RLIMIT_AS)
        soft, hard = self.previous
        if hard != resource.RLIM_INFINITY and self.max_bytes > hard:
            raise RuntimeError(f"--max-mem-mb exceeds the inherited hard RLIMIT_AS ({hard} bytes)")
        resource.setrlimit(resource.RLIMIT_AS, (self.max_bytes, hard))
        return self

    def __exit__(self, *exc):
        if self.previous is not None:
            resource.setrlimit(resource.RLIMIT_AS, self.previous)
        return False


def execute_notebook(path: Path, args) -> tuple:
    """Execute in place, atomically. Returns (ok, reason).

    On any execution error the original notebook on disk is left untouched.
    """
    free_mb = mem_available_mb()
    if free_mb < args.min_free_mb:
        return False, f"skipped: insufficient memory ({free_mb} MB available, need {args.min_free_mb} MB)"

    threads = max(1, min(args.threads, max(1, (os.cpu_count() or 2) // 2)))
    for var in THREAD_ENV_VARS:
        os.environ[var] = str(threads)

    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError as exc:
        return False, f"execution unavailable: {exc}"

    nb = nbformat.read(str(path), as_version=4)
    client = NotebookClient(
        nb,
        timeout=args.timeout,
        kernel_name=KERNEL_NAME,
        allow_errors=True,
        resources={"metadata": {"path": str(path.parent)}},
    )

    try:
        with limited_address_space(args.max_mem_mb * 1024 * 1024):
            client.execute()
    except Exception as exc:  # noqa: BLE001 - every failure shape is a reported failure
        name = type(exc).__name__
        if "Timeout" in name:
            return False, f"timeout: no cell completed within {args.timeout}s ({name})"
        if isinstance(exc, MemoryError) or "Memory" in name:
            return False, f"memory refusal: {name}: {exc}"
        return False, f"execution failed: {name}: {exc}"

    tmp_fd, tmp_name = tempfile.mkstemp(
        prefix=path.stem + ".", suffix=".ipynb.tmp", dir=str(path.parent)
    )
    os.close(tmp_fd)
    tmp_path = Path(tmp_name)
    try:
        nbformat.write(nb, str(tmp_path))
        shutil.copymode(str(path), str(tmp_path))
        os.replace(str(tmp_path), str(path))
    except Exception as exc:  # noqa: BLE001
        tmp_path.unlink(missing_ok=True)
        return False, f"write-back failed: {type(exc).__name__}: {exc}"
    return True, ""


# --------------------------------------------------------------------------
# feature verification recording
# --------------------------------------------------------------------------


def resolve_plugin_root() -> str:
    root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    if root and Path(root, "dist/packages/core/review/record-feature-verification-cli.js").is_file():
        return root
    cache = Path.home() / ".claude/plugins/cache/powell-clark/consciousness"
    resolvers = sorted(cache.glob("*/dist/packages/core/attention/resolve-plugin-cli.js"))
    if resolvers:
        try:
            out = subprocess.run(
                ["node", str(resolvers[-1])], capture_output=True, text=True, timeout=30
            ).stdout.strip()
            if out and Path(out, "dist/packages/core/review/record-feature-verification-cli.js").is_file():
                return out
        except Exception:  # noqa: BLE001
            pass
    candidates = sorted(cache.glob("*/dist/packages/core/review/record-feature-verification-cli.js"))
    if candidates:
        return str(candidates[-1].parents[4])
    return ""


def record_feature(feat_id: str, passed: bool, notes: str) -> str:
    root = resolve_plugin_root()
    if not root:
        return "record-feature: plugin root unresolvable; verdict not recorded"
    cli = Path(root, "dist/packages/core/review/record-feature-verification-cli.js")
    cmd = ["node", str(cli), feat_id, "--pass" if passed else "--fail", "--notes", notes]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except Exception as exc:  # noqa: BLE001
        return f"record-feature: failed to run ({type(exc).__name__}: {exc})"
    return (proc.stdout or proc.stderr or "").strip() or f"record-feature: exit {proc.returncode}"


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------


def write_summary_md(results: list, dest: Path) -> None:
    lines = [
        "# Notebook verification scoreboard",
        "",
        "| notebook | type | spans | emoji | marketing | code | md | executed | errors | result |",
        "|---|---|---:|---:|---:|---:|---:|---|---:|---|",
    ]
    for r in results:
        m = r["metrics"]
        lines.append(
            "| {nb} | {t} | {s} | {e} | {mk} | {cc} | {mc} | {ex} | {eo} | {res} |".format(
                nb=r["notebook"],
                t=r["type"],
                s=m["latex_spans"],
                e=m["emoji_count"],
                mk=m["marketing_hits"],
                cc=m["code_cells"],
                mc=m["markdown_cells"],
                ex="yes" if m["executed"] else "no",
                eo=m["error_outputs"],
                res="pass" if r["passed"] else "FAIL",
            )
        )
    passed = sum(1 for r in results if r["passed"])
    lines += ["", f"verify: {passed} passed, {len(results) - passed} failed", ""]
    dest.write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="verify_notebook.py",
        description="Measure curriculum notebooks against the published quality bar.",
    )
    p.add_argument("notebooks", nargs="*", type=Path, help="notebook paths")
    p.add_argument("--all", action="store_true", help="verify every notebooks/*.ipynb")
    p.add_argument("--type", choices=("theory", "practical", "auto"), default="auto")
    p.add_argument("--execute", action="store_true", help="execute and store outputs")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    p.add_argument("--report-dir", default=DEFAULT_REPORT_DIR)
    p.add_argument("--record-feature", default="", metavar="FEAT-ID")
    p.add_argument("--json", action="store_true", help="print the full result list as JSON")
    p.add_argument("--syntax-only", action="store_true", help="JSON and Python syntax check only")
    p.add_argument("--min-free-mb", type=int, default=DEFAULT_MIN_FREE_MB)
    p.add_argument("--max-mem-mb", type=int, default=DEFAULT_MAX_MEM_MB)
    p.add_argument("--threads", type=int, default=DEFAULT_THREADS)
    return p


def resolve_targets(args) -> list:
    targets = list(args.notebooks)
    if args.all:
        targets += sorted((REPO_ROOT / "notebooks").glob("*.ipynb"))
    seen = []
    for t in targets:
        t = Path(t)
        if t not in seen:
            seen.append(t)
    return seen


def verify_one(path: Path, args, report_dir: Path) -> dict:
    result = {
        "notebook": path.name,
        "path": str(path),
        "type": None,
        "metrics": {},
        "checks": [],
        "passed": False,
        "reason": "",
    }
    if not path.is_file():
        result["reason"] = "missing: no such notebook"
        return result

    try:
        nb = read_notebook(path)
    except Exception as exc:  # noqa: BLE001
        result["reason"] = f"unreadable: {type(exc).__name__}: {exc}"
        return result

    ntype = classify(path, args.type)
    result["type"] = ntype

    if args.syntax_only:
        problems = syntax_errors(nb)
        result["checks"] = [
            {"name": "syntax", "ok": not problems, "detail": "; ".join(problems) or "no syntax errors"}
        ]
        result["metrics"] = {
            "latex_spans": 0,
            "display_dollar_blocks": 0,
            "code_cells": sum(1 for c in nb.get("cells", []) if c.get("cell_type") == "code"),
            "markdown_cells": sum(1 for c in nb.get("cells", []) if c.get("cell_type") == "markdown"),
            "bytes": path.stat().st_size,
            "emoji_count": 0,
            "marketing_hits": 0,
            "error_outputs": 0,
            "has_title": False,
            "has_references": False,
            "executed": False,
        }
        result["passed"] = not problems
        return result

    exec_ok = True
    if args.execute:
        exec_ok, reason = execute_notebook(path, args)
        if not exec_ok:
            result["reason"] = reason
        nb = read_notebook(path)

    metrics = compute_metrics(nb, path)
    checks = apply_thresholds(metrics, ntype, args.execute)
    if args.execute:
        checks.insert(0, {"name": "execution", "ok": exec_ok, "detail": result["reason"] or "executed cleanly"})

    result["metrics"] = metrics
    result["checks"] = checks
    result["passed"] = all(c["ok"] for c in checks)
    return result


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    targets = resolve_targets(args)
    if not targets:
        print("verify: no notebooks given (pass paths or --all)", file=sys.stderr)
        print("verify: 0 passed, 0 failed")
        return 1

    report_dir = Path(args.report_dir)
    if not report_dir.is_absolute():
        report_dir = REPO_ROOT / report_dir
    report_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for path in targets:
        result = verify_one(Path(path), args, report_dir)
        results.append(result)
        (report_dir / (Path(path).stem + ".json")).write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8"
        )

    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"{status} {r['notebook']} [{r['type'] or 'unknown'}]")
        if r["reason"]:
            print(f"     reason: {r['reason']}")
        for c in r["checks"]:
            if not c["ok"]:
                print(f"     - {c['name']}: {c['detail']}")

    if args.all:
        (report_dir / "summary.json").write_text(
            json.dumps(results, indent=2) + "\n", encoding="utf-8"
        )
        write_summary_md(results, report_dir / "summary.md")

    if args.json:
        print(json.dumps(results, indent=2))

    passed = sum(1 for r in results if r["passed"])
    failed = len(results) - passed

    if args.record_feature:
        note = f"verify_notebook.py: {passed} passed, {failed} failed"
        print(record_feature(args.record_feature, failed == 0, note))

    print(f"verify: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
