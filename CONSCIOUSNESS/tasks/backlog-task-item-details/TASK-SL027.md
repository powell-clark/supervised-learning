# TASK-SL027: Build notebook quality verifier with executable thresholds

## Context

CURRICULUM_ROADMAP.md publishes a quality checklist (theory: 100+ LaTeX symbols, from-scratch NumPy implementation, no emojis or hype; practical: 20+ math symbols, library-vs-from-scratch comparison), but the only checker in the repo, `test_notebooks.py`, validates JSON and Python syntax and hard-codes an absolute path. Nothing executes notebooks, nothing measures the bar, so "verified" has meant "a session said so". This task turns the checklist into a program every later task closes against.

## Acceptance Criteria

- [ ] `scripts/verify_notebook.py` exists with the CLI: `verify_notebook.py <notebook.ipynb>... [--all] [--type theory|practical|auto] [--execute] [--timeout SECONDS] [--report-dir reports/verify] [--record-feature FEAT-ID] [--json]`
- [ ] `--type auto` classifies by filename: `<N>a_*` is theory; `<N>b_*`, `<N>c_*`, `<N>d_*`, `<N>e_*`, `<N>f_*` are practical unless the filename contains `theory`, in which case theory
- [ ] Metrics computed per notebook and written to `<report-dir>/<notebook-stem>.json`: `latex_spans` (count of `$...$`, `$$...$$`, `\(...\)`, `\[...\]` and `\begin{equation|align|aligned|gather}` blocks in markdown cells), `code_cells`, `markdown_cells`, `bytes`, `emoji_count` (codepoints in U+1F000–U+1FAFF, U+2600–U+27BF, U+FE0F, U+200D; the mathematical unicode ⟺ ⟹ ≤ ≥ ≠ ∈ ∑ ∏ ∂ ∇ is not counted), `marketing_hits` (case-insensitive whole-word matches for: breakthrough, revolutionary, game-changing, cutting-edge, industry-standard, state of the art, awesome, amazing, most important, unlock, supercharge), `error_outputs`, `has_title` (first cell is an H1 starting `# Lesson`), `has_references` (a heading matching `further reading` or `references`), `executed` (every code cell has an `execution_count`)
- [ ] Thresholds, applied per type and reported as pass/fail per check: theory `latex_spans >= 100`; practical `latex_spans >= 20`; both: `emoji_count == 0`, `marketing_hits == 0`, `has_title`, `has_references`, and when `--execute` was given `error_outputs == 0` and `executed`
- [ ] `--execute` runs the notebook with `nbclient` using the `supervised-learning` kernel from `.venv`, then writes the executed notebook back to its own path atomically (write to a temp file in the same directory, then rename) so outputs are stored; the original is left untouched on any execution error
- [ ] **Resource guards (host has 16 cores and, measured 2026-09-05, ~6 GB free of 31 GB with the disk 85% full — an unbounded execution can take the machine down):** before each execution the verifier reads `MemAvailable` from `/proc/meminfo` and refuses to start, reporting `skipped: insufficient memory`, when it is below `--min-free-mb` (default 3000); the kernel is launched with `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS` and `NUMEXPR_NUM_THREADS` all set to `--threads` (default 4, never more than half of `nproc`); `--timeout` defaults to 900 s per notebook and is enforced by `nbclient`; and the kernel process is started under `resource.setrlimit(RLIMIT_AS, --max-mem-mb * 1024**2)` (default 6000) so a runaway allocation raises `MemoryError` inside the notebook instead of triggering the OOM killer
- [ ] A memory-refusal or timeout is a reported failure with its own reason string, never a silent pass, and never leaves a partially-executed notebook on disk
- [ ] Exit code 0 only when every checked notebook passes every check; 1 otherwise; the last line of stdout is a one-line summary `verify: N passed, M failed`
- [ ] `--all` verifies every `notebooks/*.ipynb` and additionally writes `<report-dir>/summary.json` (list of per-notebook results) and `<report-dir>/summary.md` (a table)
- [ ] `--record-feature FEAT-ID` calls `record-feature-verification-cli.js` with `--pass` or `--fail` according to the overall result, resolving the plugin root the same way `agents/neurologist.md` does (validate `CLAUDE_PLUGIN_ROOT`, else `resolve-plugin-cli.js`, else highest cached version)
- [ ] `tests/test_verify_notebook.py` covers: span counting across all four delimiter styles, emoji vs mathematical-unicode discrimination, marketing-word matching, type classification, and an end-to-end pass/fail on two tiny fixture notebooks under `tests/fixtures/`; `.venv/bin/python -m pytest -q tests/` is green
- [ ] Running `scripts/verify_notebook.py --all` (without `--execute`) over the current corpus reproduces the STORY-SL12 measurement table within ±3 spans on the dollar-delimited notebooks and flags exactly the emoji notebooks listed there (0a, 2b, 2c, 3a, 5a)
- [ ] `test_notebooks.py` is deleted; its only surviving behaviour (syntax check) is a `--syntax-only` flag on the new verifier
- [ ] `reports/` is git-ignored except `reports/verify/summary.md`, which is committed as the running scoreboard

## Verification

```bash
.venv/bin/python -m pytest -q tests/
.venv/bin/python scripts/verify_notebook.py --all ; echo "exit=$?"
.venv/bin/python scripts/verify_notebook.py notebooks/9c_rnn_theory.ipynb --type theory --execute --timeout 900 ; echo "exit=$?"
```
The second command is expected to exit 1 today (the corpus is below the bar); the third must exit 0. Paste all three outputs and `reports/verify/summary.md` into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 100
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7
- Blocked by: TASK-SL026 (Rebuild reproducible verification environment for the curriculum)

## Pre-mortem

### Failure modes

- Counting `$` naively double-counts `$$` blocks or catches currency in prose — tokenise, do not count characters
- Executing 4b (1.5 MB) or the CIFAR fetch in 9b takes minutes and needs network — `--timeout` must be per notebook and a timeout must be a reported failure, not a hang
- Writing the executed notebook over the source loses work if execution half-fails — hence the atomic rename and untouched-on-error rule

### Weak assumptions

- Every notebook opens with an H1 `# Lesson ...`; older ones may not — the check is still right, the fix belongs to the uplift tasks
