# TASK-SL026: Rebuild reproducible verification environment for the curriculum

## Context

The checked-in `.venv` was built in December 2024 against pyenv 3.10.16, which is no longer installed (`.venv/bin/python` is a dead symlink; `.python-version` still pins 3.10.16). Every later task in this run executes notebooks, so a working, reproducible environment is the first thing the run needs. pyenv 3.12.8 is installed and already runs every existing notebook's stack (numpy, matplotlib, seaborn, scikit-learn, torch 2.13, nbconvert). Lesson 9f (TASK-SL16) additionally needs `transformers`, `datasets` and `sentencepiece`; the ensemble and tree practicals need `xgboost`, `lightgbm`, `category_encoders`, `optuna`, `imblearn`.

## Acceptance Criteria

- [ ] `scripts/setup_env.sh` exists, is executable, and: selects the interpreter (`PYTHON` env var if set, else pyenv 3.12.x if present, else the newest `python3` ≥ 3.10 on PATH); creates or reuses `.venv` at the repo root; installs `requirements.txt`; registers an ipykernel named `supervised-learning`
- [ ] Re-running `scripts/setup_env.sh` on a healthy `.venv` makes no changes and exits 0 (idempotent)
- [ ] `requirements.txt` gains, pinned: `nbconvert`, `nbclient`, `ipykernel`, `jupyter`, `transformers`, `datasets`, `sentencepiece`, `pytest`; existing pins are kept unless a pin has no wheel for the selected interpreter, in which case the change and the reason are recorded in the commit message
- [ ] `.python-version` is updated to the interpreter version actually used
- [ ] `.venv/bin/python -c "import numpy, pandas, matplotlib, seaborn, sklearn, xgboost, lightgbm, torch, torchvision, category_encoders, optuna, imblearn, tqdm, transformers, datasets, nbconvert, nbclient, ipykernel"` exits 0
- [ ] `.venv/bin/jupyter kernelspec list` shows `supervised-learning`
- [ ] `.venv/` is ignored by git (check `.gitignore`; add it if missing) so the environment is rebuilt from the script, never committed

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
