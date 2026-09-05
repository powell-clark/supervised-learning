# TASK-SL026: Rebuild reproducible verification environment for the curriculum

## Context

The checked-in `.venv` was built in December 2024 against pyenv 3.10.16, which is no longer installed (`.venv/bin/python` is a dead symlink; `.python-version` still pins 3.10.16). Every later task in this run executes notebooks, so a working, reproducible environment is the first thing the run needs. pyenv 3.12.8 is installed and already runs every existing notebook's stack (numpy, matplotlib, seaborn, scikit-learn, torch 2.13, nbconvert). Lesson 9f (TASK-SL16) additionally needs `transformers`, `datasets` and `sentencepiece`; the ensemble and tree practicals need `xgboost`, `lightgbm`, `category_encoders`, `optuna`, `imblearn`.

## Acceptance Criteria

- [x] `scripts/setup_env.sh` exists, is executable, and: selects the interpreter (`PYTHON` env var if set, else pyenv 3.12.x if present, else the newest `python3` ≥ 3.10 on PATH); creates or reuses `.venv` at the repo root; installs `requirements.txt`; registers an ipykernel named `supervised-learning`
- [x] Re-running `scripts/setup_env.sh` on a healthy `.venv` makes no changes and exits 0 (idempotent)
- [x] `requirements.txt` gains, pinned: `nbconvert`, `nbclient`, `ipykernel`, `jupyter`, `transformers`, `datasets`, `sentencepiece`, `pytest`; existing pins are kept unless a pin has no wheel for the selected interpreter, in which case the change and the reason are recorded in the commit message
- [x] `.python-version` is updated to the interpreter version actually used
- [x] `.venv/bin/python -c "import numpy, pandas, matplotlib, seaborn, sklearn, xgboost, lightgbm, torch, torchvision, category_encoders, optuna, imblearn, tqdm, transformers, datasets, nbconvert, nbclient, ipykernel"` exits 0
- [x] `.venv/bin/jupyter kernelspec list` shows `supervised-learning`
- [x] `.venv/` is ignored by git (check `.gitignore`; add it if missing) so the environment is rebuilt from the script, never committed

## Verification

```bash
bash scripts/setup_env.sh && bash scripts/setup_env.sh   # second run must be a no-op
.venv/bin/python -c "import numpy, pandas, matplotlib, seaborn, sklearn, xgboost, lightgbm, torch, torchvision, category_encoders, optuna, imblearn, tqdm, transformers, datasets, nbconvert, nbclient, ipykernel; print('env ok')"
.venv/bin/jupyter kernelspec list | grep supervised-learning
```
Paste all three outputs into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 60
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7

## Pre-mortem

### Failure modes

- `lightgbm` wheel needs `libgomp` on the host — check with `ldconfig -p | grep gomp` and record the fix in the script, not by hand
- `numpy==2.2.0` and `torch` pins may conflict with `transformers` — resolve by loosening the newest pin only, and say so in the commit
- CUDA-enabled torch wheels are large and unnecessary; install the CPU wheel index if the default pulls CUDA

### Weak assumptions

- pyenv 3.12.8 stays installed on this host for the duration of the run; the script must not hard-code that path

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit cb9d7b2. All three commands
from the Verification block, run verbatim, with their unmodified output.

### 1. Idempotency — two consecutive runs

```
$ bash scripts/setup_env.sh && bash scripts/setup_env.sh
[setup-env] interpreter: /home/powell-clark/.pyenv/versions/3.12.8/bin/python3 (3.12.8)
[setup-env] environment already current (python=3.12.8 requirements=947964ed17a4711f) — nothing to do
[setup-env] interpreter: /home/powell-clark/.pyenv/versions/3.12.8/bin/python3 (3.12.8)
[setup-env] environment already current (python=3.12.8 requirements=947964ed17a4711f) — nothing to do
EXIT1=0
```

### 2. Import check — nineteen modules

```
$ .venv/bin/python -c "import numpy, pandas, matplotlib, seaborn, sklearn, xgboost, lightgbm, torch, torchvision, category_encoders, optuna, imblearn, tqdm, transformers, datasets, nbconvert, nbclient, ipykernel; print('env ok')"
env ok
EXIT2=0
```

### 3. Kernel registration

```
$ .venv/bin/jupyter kernelspec list | grep supervised-learning
  supervised-learning    /home/powell-clark/.local/share/jupyter/kernels/supervised-learning
EXIT3=0
```

### Supporting state

```
$ cat .python-version
3.12.8

$ cat .venv/.setup-stamp
python=3.12.8 requirements=947964ed17a4711f
```

### What the environment resolved to

python 3.12.8, torch 2.14.0+cpu, torchvision 0.29.0+cpu, numpy 2.2.0,
pandas 2.2.3, scikit-learn 1.5.2, xgboost 2.1.4, lightgbm 4.7.0,
transformers 5.16.1, datasets 5.0.1, nbconvert 7.17.1, nbclient 0.11.0.
Total 2.8 GB on disk, rebuildable from `scripts/setup_env.sh` alone.

### Deviations from the plan, and why

- **`xgboost==1.7.6` -> `xgboost>=2.0.3,<3.0`.** The card permits a pin change
  where a pin has no wheel for the selected interpreter, and requires the
  reason in the commit message. 1.7.6 predates Python 3.12 and publishes no
  cp312 wheel; pip fell back to a source build that does not complete. This is
  the only pin altered.
- **The `numpy`/`torch`/`transformers` conflict in the pre-mortem did not
  occur.** The resolver took numpy 2.2.0 and transformers 5.16.1 together with
  no loosening required.
- **The `libgomp` failure mode did not occur.** `ldconfig -p | grep gomp`
  returns `libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1`, so lightgbm's
  OpenMP dependency was already satisfied and the script needed no fix for it.

### One defect found and fixed during the task

The first install wedged for 21 minutes: 19 s of CPU across 1295 s elapsed,
zero files added to the pip cache in the last 10 minutes, five idle sockets.
Both indexes were reachable when probed directly. The cause was in this task's
own script — `--quiet` with no socket timeout, so an unattended run cannot
distinguish a stall from a slow download. The install now carries
`--timeout 30 --retries 3`, `--progress-bar off`, and an outer
`PIP_MAX_SECONDS` ceiling that fails with a diagnostic naming the likely
cause. The successful run then took roughly 21 minutes of genuine work,
most of it downloading the 196 MB CPU torch wheel at about 260 KB/s.
