# STORY-SL15: Lockstep — this repo and its three siblings converge on one README shape and one status line

## User Story

I want supervised-learning, unsupervised-learning, reinforcement-learning, and deep-learning to present the same way so a reader (or me, coming back to any one of them) recognises the family at a glance, instead of four repos that happened to start from the same idea and drifted.

## Context

The eagle-peak kernel measured this directly during the 2026-09-05/06
overnight run: the four ML repos do not share a README shape or a status
line today (unsupervised-learning's README states "17 of 17 complete",
deep-learning's states "20/20", this repo's completion is tracked in
CONSCIOUSNESS/ rather than surfaced in README.md at all). FEAT-SL7 already
scopes "README.md regenerated from the notebooks" for this repo alone; this
story is the cross-repo half — agreeing a shared shape, then applying it
here and confirming the siblings match, not redesigning each repo's README
from scratch independently.

## Acceptance Criteria

- [ ] A shared README shape (sections, ordering, and a one-line status format) is agreed and documented somewhere all four repos can reference
- [ ] This repo's README matches the shared shape, generated from live notebook metadata (per FEAT-SL7), not hand-written
- [ ] A status line here matches the pattern the other three repos use for theirs (e.g. "N of M lessons complete")
- [ ] Conformance is verified by diffing structure against the sibling repos, not by eye
- [ ] Divergence found in a sibling repo is filed as a task there, not silently fixed by reaching into another repo's checkout

## References

- README.md (this repo)
- FEAT-SL7 (Curriculum verification and autonomous run tooling — owns this repo's README regeneration)
- /home/powell-clark/projects/auxiliary/unsupervised-learning, reinforcement-learning, deep-learning (sibling repos, read-only reference — this story does not edit them)
