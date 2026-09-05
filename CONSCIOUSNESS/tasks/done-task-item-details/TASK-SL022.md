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

- [x] Explain voting (hard/soft) and simple averaging as combination strategies, with the math for how soft voting aggregates predicted probabilities — $\hat y = \arg\max_c \frac{1}{M}\sum_m P_m(y=c\mid x)$ derived alongside hard voting's mode formula
- [x] Explain stacking: base learners trained on the full training set, a meta-learner trained on out-of-fold base-model predictions to avoid leakage — the 4-step out-of-fold procedure stated explicitly, explaining why training the meta-learner on in-sample predictions would leak each base model's own overfitting into the meta-learner
- [x] Demonstrate stacking empirically (e.g. `StackingClassifier` or a from-scratch out-of-fold implementation) on the same breast cancer split used in 7a/7b — `VotingClassifier` (hard and soft) and `StackingClassifier` (logistic meta-learner, cv=5) on the identical `X_train`/`X_test` split, same 4 base learners (bagging, random forest, matched-hyperparameter XGBoost/LightGBM) already fitted elsewhere in the notebook
- [x] Compare stacking's performance to the individual base learners and to bagging/boosting from 7a/7b — printed comparison table includes all 4 base learners, both voting variants, stacking, and the Optuna-tuned XGBoost; measured run: stacking (0.9561) slightly below the best single base learner (Random Forest, 0.9649) and well below the Optuna-tuned XGBoost (0.9737) — stated honestly rather than presented as a win
- [x] Update FEAT-SL4's acceptance criteria checkbox once verified — added AC-11, commit e5ccf0d

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

## Closing note

Closed 2026-09-05 by session sl-07bdf165 on commit 71e6aa9, worked
directly in-session per the operator's pivot on TASK-SL028 (Build
autonomous syllabus run orchestrator with model-aware dispatch)
(self-dispatch dropped in favour of continuing in this session).

### Verification command output

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/7b_ensemble_methods_practical.ipynb --type practical --execute
PASS 7b_ensemble_methods_practical.ipynb [practical]
verify: 1 passed, 0 failed
```

### JSON report (`reports/verify/7b_ensemble_methods_practical.json`)

```json
{
  "notebook": "7b_ensemble_methods_practical.ipynb",
  "type": "practical",
  "metrics": {
    "latex_spans": 35,
    "display_dollar_blocks": 2,
    "code_cells": 13,
    "markdown_cells": 18,
    "bytes": 311939,
    "emoji_count": 0,
    "marketing_hits": 0,
    "error_outputs": 0,
    "has_title": true,
    "has_references": true,
    "executed": true
  },
  "passed": true
}
```
