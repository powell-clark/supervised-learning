# TASK-SL022: Add ensemble combination strategies (voting, averaging, stacking) to Lesson 7

## Context

Discovered while closing TASK-SL8 (Lesson 7b: Ensemble Methods practical).
FEAT-SL4's frontmatter acceptance_criteria requires "decision tree analysis and
ensemble combination strategies (voting, averaging, stacking)", but neither
7a (theory) nor 7b (practical) covers stacking or an explicit voting classifier
— both notebooks focus on bagging (Random Forest), boosting (AdaBoost,
XGBoost, LightGBM), which are distinct techniques from stacking's meta-learner
approach.

## Acceptance Criteria

- [ ] Explain voting (hard/soft) and simple averaging as combination strategies, with the math for how soft voting aggregates predicted probabilities
- [ ] Explain stacking: base learners trained on the full training set, a meta-learner trained on out-of-fold base-model predictions to avoid leakage
- [ ] Demonstrate stacking empirically (e.g. `StackingClassifier` or a from-scratch out-of-fold implementation) on the same breast cancer split used in 7a/7b
- [ ] Compare stacking's performance to the individual base learners and to bagging/boosting from 7a/7b
- [ ] Update FEAT-SL4's acceptance criteria checkbox once verified

## References

- FEAT-SL4 (Lesson 7 — Ensemble Methods theory and practice)
- notebooks/7a_ensemble_methods_theory.ipynb
- notebooks/7b_ensemble_methods_practical.ipynb

## Blocked By

TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/7b_ensemble_methods_practical.ipynb --type practical --execute
```
Must exit 0 after the additions; the new stacking section must be executed with stored outputs.

## Dispatch

model: sonnet
effort: medium
max_turns: 60
reviewer_model: sonnet
