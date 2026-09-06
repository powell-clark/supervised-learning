# STORY-SL13: Style conformance — every lesson held against the operator's own reference notebooks for Feynman voice, first-principles depth, and runnability by a rusty 18-year-old with A-level (not further) maths

## User Story

I want every lesson audited against the standard my own reference notebooks (1a, 1b, 2a, 2b, 2c) already set, so a lesson that reads like a library tutorial instead of a Feynman explanation gets caught and fixed, not left to drift.

## Context

The existing CURRICULUM_ROADMAP.md quality checklist governs mechanical
properties — LaTeX span counts, emoji, execution, references — and
scripts/verify_notebook.py enforces exactly those. It does not check voice
or pedagogical level, and a notebook can pass every mechanical check while
still reading like documentation rather than teaching. The operator named
1a, 1b, 2a, 2b, and 2c as the reference bar for what "right" looks like:
Richard Feynman voice (explain the idea before the formalism, use concrete
numbers, admit what's hard), first-principles grounding (derive, don't
assert), and a level a reader with good A-level maths — not further maths,
not a maths degree — can actually follow and run end to end.

This is a genuinely new audit dimension, not a re-run of the existing
mechanical verifier. It needs a human or agent reading pass against the
reference lessons, not a script.

## Acceptance Criteria

- [ ] A written style rubric exists, derived from reading 1a/1b/2a/2b/2c and naming the concrete properties that make them work (not a restatement of the mechanical checklist)
- [ ] Every lesson (0-9, all a/b/c notebooks) is read against the rubric and scored pass/fall-short
- [ ] Every lesson scored fall-short gets its own named refinement task, citing the specific rubric criterion it fails and where
- [ ] The audit's findings are recorded on this story's card, not lost to a session transcript
- [ ] Passes the existing mechanical bar throughout — style conformance never regresses execution, span counts, or the from-scratch/library pairing

## References

- notebooks/1a_logistic_regression_theory.ipynb, 1b_logistic_regression_practical.ipynb
- notebooks/2a_decision_trees_theory.ipynb, 2b_decision_trees_practical.ipynb, 2c_decision_trees_ATLAS_model_comparison.ipynb
- CURRICULUM_ROADMAP.md (existing mechanical checklist, which this story extends rather than replaces)
