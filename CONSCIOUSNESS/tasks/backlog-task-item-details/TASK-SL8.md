# TASK-SL8: Lesson 7b: Ensemble Methods practical — XGBoost, LightGBM, hyperparameter tuning

## Context

Create the practical notebook for Ensemble Methods. Apply XGBoost and LightGBM to real datasets, demonstrate hyperparameter tuning strategies, feature importance analysis, and comparison to from-scratch AdaBoost.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/7b_ensemble_methods_practical.ipynb`
- [ ] Dataset: Tabular data suitable for tree-based methods
- [ ] XGBoost implementation: Basic setup, training, and hyperparameter tuning (learning_rate, max_depth, subsample)
- [ ] LightGBM implementation: Comparison to XGBoost, speed/accuracy trade-offs
- [ ] Hyperparameter tuning: Grid search or Bayesian optimization (e.g., Optuna)
- [ ] Learning curves: Plot training vs validation error over iterations
- [ ] Feature importance: Extract and visualize feature contributions to model
- [ ] Bagging vs Boosting comparison: Show different ensemble approaches on same data
- [ ] Comparison: From-scratch AdaBoost (from 7a) vs XGBoost/LightGBM
- [ ] Early stopping: Show how to prevent overfitting during training
- [ ] Performance analysis: Cross-validation, metrics relevant to problem (classification/regression)
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: XGBoost paper, LightGBM documentation, ESL
- [ ] Notebook length: 50 hours effort

## Technical Notes

XGBoost adds regularization and uses column subsampling. LightGBM uses leaf-wise tree growth vs level-wise (faster).

Show practical impact: LightGBM trains faster than XGBoost with comparable accuracy.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Hyperparameter tuning strategy is systematic and reproducible
- [ ] Feature importance analysis provides actionable insights
- [ ] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL7 (requires understanding from theory notebook)
