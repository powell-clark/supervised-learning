# TASK-SL021: Repair duplicate/stale TASK-SL2 detail cards and missing done-task-item-details file

## Context

Discovered while closing TASK-SL1. TASK-DONE-INDEX.md points TASK-SL2's doc at
`done-task-item-details/TASK-SL2.md`, but that file does not exist. Instead two
different, inconsistent detail cards exist for TASK-SL2:
`backlog-task-item-details/TASK-SL2.md` (matches the original spec-driven-development
card shape) and `active-task-item-details/TASK-SL2.md` (a different frontmatter shape
and different acceptance criteria wording). This is a structural integrity gap — the
INDEX references a file that was never created, and two stale duplicates were left
behind from an earlier card revision.

## Acceptance Criteria

- [ ] Reconcile the two TASK-SL2.md variants into one canonical detail card reflecting what was actually built in `notebooks/4b_support_vector_machines_practical.ipynb`
- [ ] Move the reconciled card to `done-task-item-details/TASK-SL2.md` matching TASK-DONE-INDEX.md's doc column
- [ ] Delete the stale backlog and active copies
- [ ] Run the neurologist diagnostic (or equivalent PGPS validation) to confirm no other task/feature doc references are dangling

## References

- CONSCIOUSNESS/tasks/TASK-DONE-INDEX.md
- CONSCIOUSNESS/tasks/backlog-task-item-details/TASK-SL2.md
- CONSCIOUSNESS/tasks/active-task-item-details/TASK-SL2.md
