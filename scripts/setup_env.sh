#!/usr/bin/env bash
# Build the reproducible verification environment for the curriculum.
#
# Idempotent: a second run against a healthy .venv makes no changes and exits 0.
# Freshness is keyed on the interpreter version plus a hash of requirements.txt,
# recorded in .venv/.setup-stamp; either changing forces a reinstall.
#
# Interpreter selection, in order:
#   1. $PYTHON, if set and executable
#   2. the newest pyenv 3.1x installed
#   3. the newest python3.1x on PATH, provided it is >= 3.10
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$REPO/.venv"
REQ="$REPO/requirements.txt"
STAMP="$VENV/.setup-stamp"
KERNEL_NAME="supervised-learning"
KERNEL_DISPLAY="Supervised Learning (.venv)"

log() { printf '[setup-env] %s\n' "$*"; }
die() { printf '[setup-env] ERROR: %s\n' "$*" >&2; exit 1; }

# --- 1. choose an interpreter -------------------------------------------------
pick_interpreter() {
  if [ -n "${PYTHON:-}" ]; then
    [ -x "$PYTHON" ] || die "\$PYTHON is set to '$PYTHON' but that is not executable"
    printf '%s' "$PYTHON"; return
  fi
  local candidate
  candidate="$(ls -d "$HOME"/.pyenv/versions/3.1*/bin/python3 2>/dev/null | sort -V | tail -1 || true)"
  if [ -n "$candidate" ] && [ -x "$candidate" ]; then
    printf '%s' "$candidate"; return
  fi
  for v in 3.13 3.12 3.11 3.10; do
    if command -v "python3.$v" >/dev/null 2>&1; then
      command -v "python3.$v"; return
    fi
  done
  die "no python3.10+ interpreter found; install one or set \$PYTHON"
}

PY="$(pick_interpreter)"
PY_VERSION="$("$PY" -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])')"
PY_MAJOR_MINOR="$("$PY" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
log "interpreter: $PY ($PY_VERSION)"

"$PY" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3,10) else 1)' \
  || die "interpreter $PY is $PY_VERSION; 3.10 or newer is required"

# --- 2. is the existing venv healthy and current? -----------------------------
[ -f "$REQ" ] || die "requirements.txt not found at $REQ"
REQ_HASH="$("$PY" -c 'import hashlib,sys; print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest()[:16])' "$REQ")"
WANT_STAMP="python=$PY_VERSION requirements=$REQ_HASH"

if [ -x "$VENV/bin/python" ] && [ -f "$STAMP" ] && [ "$(cat "$STAMP")" = "$WANT_STAMP" ]; then
  if "$VENV/bin/python" -c 'import sys' 2>/dev/null; then
    log "environment already current ($WANT_STAMP) — nothing to do"
    exit 0
  fi
fi

# --- 3. (re)create the venv ---------------------------------------------------
if [ -e "$VENV" ] && ! "$VENV/bin/python" -c 'import sys' 2>/dev/null; then
  log "existing .venv is broken (interpreter missing) — recreating"
  rm -rf "$VENV"
elif [ -e "$VENV" ]; then
  log "existing .venv is stale (interpreter or requirements changed) — recreating"
  rm -rf "$VENV"
fi

log "creating $VENV"
"$PY" -m venv "$VENV"

VPY="$VENV/bin/python"
"$VPY" -m pip install --quiet --upgrade pip setuptools wheel

# --- 4. install requirements --------------------------------------------------
# torch is pulled from the CPU index: the default index serves CUDA-linked
# wheels that are several GB larger, and nothing in this curriculum needs a GPU.
#
# --timeout/--retries are not optional niceties. Measured 2026-09-05: a run
# without them wedged for 21 minutes on an idle socket to the PyTorch index —
# 19s of CPU across 1295s elapsed, zero files added to the pip cache in the
# last 10 minutes of it. pip's default socket timeout is long enough that a
# dead index looks identical to a slow download, so an unattended run cannot
# tell a stall from progress. Bound it, and let the outer PIP_MAX_SECONDS cap
# kill a hang outright rather than burning the task's whole wall clock.
PIP_MAX_SECONDS="${PIP_MAX_SECONDS:-1800}"
log "installing requirements (CPU-only torch, ${PIP_MAX_SECONDS}s ceiling)"
if ! timeout "$PIP_MAX_SECONDS" "$VPY" -m pip install \
      --progress-bar off \
      --timeout 30 --retries 3 \
      --extra-index-url https://download.pytorch.org/whl/cpu \
      -r "$REQ"; then
  rc=$?
  if [ "$rc" -eq 124 ]; then
    die "pip exceeded ${PIP_MAX_SECONDS}s — likely a hung index. Re-run; \
consider PIP_MAX_SECONDS=3600 or dropping the --extra-index-url to use PyPI's \
default torch build."
  fi
  die "pip install failed with exit $rc"
fi

# --- 5. register the kernel ---------------------------------------------------
log "registering ipykernel '$KERNEL_NAME'"
"$VPY" -m ipykernel install --user --name "$KERNEL_NAME" --display-name "$KERNEL_DISPLAY" >/dev/null

# --- 6. verify ----------------------------------------------------------------
log "verifying imports"
"$VPY" - <<'PYCHECK'
import importlib, sys
required = [
    "numpy", "pandas", "matplotlib", "seaborn", "sklearn",
    "xgboost", "lightgbm", "torch", "torchvision",
    "category_encoders", "optuna", "imblearn", "tqdm",
    "transformers", "datasets",
    "nbconvert", "nbclient", "ipykernel", "pytest",
]
missing = []
for name in required:
    try:
        importlib.import_module(name)
    except Exception as exc:
        missing.append(f"{name}: {type(exc).__name__}: {exc}")
if missing:
    print("MISSING OR BROKEN:", file=sys.stderr)
    for m in missing:
        print("  " + m, file=sys.stderr)
    raise SystemExit(1)
print("all required imports resolve")
PYCHECK

printf '%s' "$WANT_STAMP" > "$STAMP"

# --- 7. keep .python-version honest ------------------------------------------
if [ -f "$REPO/.python-version" ] && [ "$(cat "$REPO/.python-version")" != "$PY_VERSION" ]; then
  log "updating .python-version: $(cat "$REPO/.python-version") -> $PY_VERSION"
  printf '%s\n' "$PY_VERSION" > "$REPO/.python-version"
fi

log "done — $VENV ready on python $PY_VERSION"
log "kernel: $KERNEL_NAME    activate with: source .venv/bin/activate"
