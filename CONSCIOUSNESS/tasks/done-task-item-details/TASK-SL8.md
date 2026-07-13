# TASK-SL8: Lesson 7b: Ensemble Methods practical — XGBoost, LightGBM, hyperparameter tuning

## Context

Create the practical notebook for Ensemble Methods. Apply XGBoost and LightGBM to real datasets, demonstrate hyperparameter tuning strategies, feature importance analysis, and comparison to from-scratch AdaBoost.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/7b_ensemble_methods_practical.ipynb`
- [x] Dataset: Tabular data suitable for tree-based methods — breast cancer dataset, same split as 7a for direct comparability
- [x] XGBoost implementation: Basic setup, training, and hyperparameter tuning (learning_rate, max_depth, subsample)
- [x] LightGBM implementation: Comparison to XGBoost, speed/accuracy trade-offs — measured directly (matched hyperparameters, same accuracy, LightGBM faster)
- [x] Hyperparameter tuning: Grid search or Bayesian optimization (e.g., Optuna) — both: grid search (27 combos) and Optuna TPE (40 trials, 98.24% CV accuracy)
- [x] Learning curves: Plot training vs validation error over iterations
- [x] Feature importance: Extract and visualize feature contributions to model — both XGBoost (gain-based) and LightGBM (split-count based)
- [x] Bagging vs Boosting comparison: Show different ensemble approaches on same data
- [x] Comparison: From-scratch AdaBoost (from 7a) vs XGBoost/LightGBM — 7a's from-scratch AdaBoost (97.4%) matches Optuna-tuned XGBoost (97.4%) and beats untuned baselines
- [x] Early stopping: Show how to prevent overfitting during training — measured best_iteration=197 of 500 requested rounds
- [x] Performance analysis: Cross-validation, metrics relevant to problem (classification/regression) — 5-fold CV, confusion matrix, classification report
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: XGBoost paper, LightGBM documentation, ESL
- [x] Notebook length: 50 hours effort — 27.7KB rendered, 29 cells

## Technical Notes

XGBoost adds regularization and uses column subsampling. LightGBM uses leaf-wise tree growth vs level-wise (faster).

Show practical impact: LightGBM trains faster than XGBoost with comparable accuracy.

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] Hyperparameter tuning strategy is systematic and reproducible
- [x] Feature importance analysis provides actionable insights
- [x] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL7 (requires understanding from theory notebook)
