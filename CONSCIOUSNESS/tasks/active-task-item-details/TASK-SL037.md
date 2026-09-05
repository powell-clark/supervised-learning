# TASK-SL037: Execute every notebook end-to-end and store outputs

## Context

Measured 2026-09-04: only 5 of 22 notebooks store executed outputs (4b, 5a, 5b, 9c, 9d). The other 17 ship code a reader has to trust, and the Colab badges in the README promise "Run all" works. This is the corpus-wide execution sweep, run after every content task has landed, and it is the last gate before the README and the completion report.

## Acceptance Criteria

- [ ] `scripts/verify_notebook.py --all --execute` exits 0 across every notebook in `notebooks/`
- [ ] Every notebook in `notebooks/` has stored outputs — every code cell carries an `execution_count` and cells that produce figures carry image outputs
- [ ] Any notebook that cannot execute is fixed rather than skipped: missing data files fetched or the fetch made conditional, deprecated library calls updated, non-deterministic cells seeded
- [ ] Any fix that changes a notebook's reported numbers updates the prose quoting those numbers in the same commit
- [ ] Execution is sequential, one notebook at a time, respecting the verifier's memory guard — a `skipped: insufficient memory` result is retried, never accepted as a pass
- [ ] `reports/verify/summary.md` is committed showing every notebook green
- [ ] `record-verification-run-cli --pass` is recorded so feature freshness stamps populate from the sweep

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py --all --execute --timeout 1800 ; echo "exit=$?"
cat reports/verify/summary.md
git status --porcelain notebooks/ | head
```
First command must exit 0; the summary must show every notebook passing; the third confirms the executed notebooks are committed (empty output after committing).

## Dispatch

model: sonnet
effort: high
max_turns: 160
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9
- Blocked by: TASK-SL030, TASK-SL031, TASK-SL032, TASK-SL033, TASK-SL034, TASK-SL035, TASK-SL036, TASK-SL15, TASK-SL16, TASK-SL022

## Pre-mortem

### Failure modes

- This is the longest-running task in the plan: 22 notebooks including a CIFAR fetch, a ResNet fine-tune and a transformer fine-tune, on a host with ~6 GB free. It must run sequentially with the memory guard on, and the 90-minute per-task cap in the orchestrator may not be enough — if the sweep is cut short, it resumes by re-running, since already-executed notebooks pass quickly
- Executing notebooks that fetch from the network (OpenML, seaborn datasets, Hugging Face) fails offline — record which notebooks have a network dependency in the summary so the operator knows what a fresh clone needs
- Storing outputs inflates the repo: 4b is already 1.5 MB and 9d 647 KB; check the total added size and report it, and strip base64 images only if a notebook exceeds ~5 MB

### Weak assumptions

- Every notebook is executable at all; one may turn out to depend on a data file that was never committed, in which case file a task rather than fabricating the data
