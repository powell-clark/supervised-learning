# TASK-SL040: Fix 1b evaluator using last grid-search model, not the best one

## Context

notebooks/1b_logistic_regression_practical.ipynb cell 13's ModelOptimiser.run_experiments() grid search loop reassigns a module-global model = CancerClassifier(...) on every hyperparameter combination it tries; cell 16's ModelEvaluator(model, ...) then evaluates whatever model that variable holds after the loop ends -- the LAST combination tried, not the highest-scoring one in results_df. Found while doing TASK-SL034's math-explanation uplift; out of scope there. Fix: retrain (or cache) the model for the best row of results_df and evaluate that one.

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
