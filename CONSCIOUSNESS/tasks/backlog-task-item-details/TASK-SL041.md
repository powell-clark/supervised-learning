# TASK-SL041: Correct STORY-SL12/TASK-SL034 assumption that ATLAS uses classification metrics

## Context

TASK-SL034's own card assumed notebooks/2c_decision_trees_ATLAS_model_comparison.ipynb's CrossValidator computes classification metrics (precision, recall, F1, ROC-AUC as probability a random positive outranks a random negative). Verified false: ATLAS compares DecisionTreeRegressor/RandomForestRegressor/XGBRegressor on a continuous log-price target, so it actually reports R^2 and MAE throughout. TASK-SL034 documented the real behaviour in the notebook (2c cell 13's markdown) per its own pre-mortem instruction rather than inventing fictional classification metrics. This follow-up is just editorial: correct the STORY-SL12/TASK-SL034 card text itself so future readers of those cards are not misled about what 2c measures. No code or notebook change needed.

## Acceptance criteria

- [x] STORY-SL12/TASK-SL034 card text does not mislead a future reader about what 2c measures — already satisfied: TASK-SL034.md's own 2c bullet states the original classification-metric assumption alongside a bolded **defect found and documented, not fabricated** correction naming the real R^2/MAE regression metrics, in the same sentence; 2c's own cell 13 markdown carries the identical correction ("Correction to this notebook's own description below..."). No further edit needed.

> **2026-09-05, sl-4afb8881:** verified both texts directly; this task's remaining scope is already met by TASK-SL034's own closing work. Not formally closed here — TASK-SL037 is this session's one claimed in_progress task and this needs no further work, only the lifecycle paperwork (in_review, verdict, done) a future session or the operator can do in one step citing this note.

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
