# STORY-SL14: Currency — a bounded refresh cadence so the corpus keeps updating itself instead of quietly rotting

## User Story

I want the corpus to refresh itself on a stated cadence so library versions, datasets, and execution outputs stay current without me having to notice they've gone stale.

## Context

TASK-SL037 proved the corpus can be verified end to end in one sweep
(`scripts/verify_notebook.py --all --execute`), and that a missing
`--max-mem-mb` flag or a library version drift is exactly the kind of thing
that silently breaks a notebook between runs (found twice in that task:
`--max-mem-mb 6144` being required, and 9b's unbatched ResNet inference
allocating more than a default kernel budget). Left alone, the same classes
of drift (torch/sklearn/torchvision releases, a dataset URL going stale, a
deprecated API) will recur. A living portfolio needs a repeatable check, not
a one-off sweep.

## Acceptance Criteria

- [ ] A stated cadence exists (e.g. a scheduled or operator-triggered interval) for re-running `scripts/verify_notebook.py --all --execute`
- [ ] Each refresh run's outcome is recorded (pass / fixed / task filed), not silently absorbed into a green checkmark
- [ ] requirements.txt / .venv pinning strategy is documented so a refresh can tell a genuine break from a routine version bump
- [ ] A refresh that finds a break files a task rather than being hand-patched inline and forgotten
- [ ] The cadence is bounded — explicit about how often, not "whenever someone remembers"

## References

- scripts/verify_notebook.py
- requirements.txt, .venv
- CONSCIOUSNESS/tasks/done-task-item-details/TASK-SL037.md (the sweep this story keeps repeatable)
