# TASK-SL041: Correct STORY-SL12/TASK-SL034 assumption that ATLAS uses classification metrics

## Context

TASK-SL034's own card assumed notebooks/2c_decision_trees_ATLAS_model_comparison.ipynb's CrossValidator computes classification metrics (precision, recall, F1, ROC-AUC as probability a random positive outranks a random negative). Verified false: ATLAS compares DecisionTreeRegressor/RandomForestRegressor/XGBRegressor on a continuous log-price target, so it actually reports R^2 and MAE throughout. TASK-SL034 documented the real behaviour in the notebook (2c cell 13's markdown) per its own pre-mortem instruction rather than inventing fictional classification metrics. This follow-up is just editorial: correct the STORY-SL12/TASK-SL034 card text itself so future readers of those cards are not misled about what 2c measures. No code or notebook change needed.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
