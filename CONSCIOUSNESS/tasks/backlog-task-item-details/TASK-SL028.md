# TASK-SL028: Build autonomous syllabus run orchestrator with model-aware dispatch

## Context

scripts/run_syllabus.sh: walk the execution spine, dispatch each unblocked task to the model in its card's Dispatch block via claude -p with a budget cap, verify, record agent verdicts with append-verdict-cli, retry once, log, exit when the spine is empty.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
