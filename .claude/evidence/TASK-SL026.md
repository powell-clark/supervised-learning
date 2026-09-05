# TASK-SL026 — evidence for rebuilding `.venv`

## Diagnosis

The checked-in `.venv` is non-functional. It was created 2024-12-09 against
`pyenv 3.10.16`, which is no longer installed on this host, so both its
interpreter symlink and the `home` it points at are dangling. Nothing in the
repository can execute a notebook until it is rebuilt.

## Falsifying command and raw output

Run before any destructive action, 2026-09-05:

```
$ .venv/bin/python --version
/bin/bash: line 13: /home/powell-clark/projects/auxiliary/supervised-learning/.venv/bin/python: No such file or directory

$ test -e .venv/bin/python && echo "TARGET EXISTS" || echo "TARGET MISSING"
TARGET MISSING — venv is broken

$ grep home .venv/pyvenv.cfg
home = /home/powell-clark/.pyenv/versions/3.10.16/bin

$ test -d /home/powell-clark/.pyenv/versions/3.10.16/bin && echo EXISTS || echo MISSING
HOME MISSING — interpreter gone

$ ls ~/.pyenv/versions/
3.12.8
emissionscalculator
```

The diagnosis is confirmed: the venv cannot be repaired in place because the
interpreter it was built from does not exist.

## Rollback

None needed, and none possible to lose:

- `.venv` is git-ignored (`.gitignore:59`), so it is not tracked and its removal
  changes no committed state
- It is already non-functional, so there is no working state to preserve
- `scripts/setup_env.sh`, written by this task, reconstructs it from
  `requirements.txt` in one command — the rebuild *is* the rollback

## Action authorised

Remove `.venv` and recreate it from the newest available interpreter
(pyenv 3.12.8), then install `requirements.txt` and register the
`supervised-learning` kernel.
