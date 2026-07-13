---
id: FEAT-SL4
status: backlog
priority: p2
kano: performance
title: Lesson 7 — Ensemble Methods theory and practice
description: Complete ensemble learning lesson with mathematical theory (bias-variance tradeoff, bagging, AdaBoost, gradient boosting) and practical implementation (XGBoost, LightGBM, hyperparameter tuning)
acceptance_criteria:
  - Theory notebook complete with bias-variance decomposition, bagging mathematics, AdaBoost algorithm derivation, and gradient boosting framework
  - Practical notebook complete with XGBoost and LightGBM implementations and hyperparameter tuning via Bayesian optimization
  - Both notebooks runnable end-to-end in Google Colab with dependencies installed in first cell
  - Includes decision tree analysis and ensemble combination strategies (voting, averaging, stacking)
  - Markdown cells document learning objectives, key formulas, and interpretation of results
stories: [STORY-SL7]
tasks: [TASK-SL7,TASK-SL8]
---

# FEAT-SL4: Lesson 7 — Ensemble Methods

## Context
Ensemble methods combine multiple weak learners to create a strong predictor.
This lesson covers the theoretical foundations (bias-variance, boosting, bagging)
and state-of-the-art implementations (gradient boosting, XGBoost). Ensemble methods
are among the most effective techniques in practical machine learning.

## Acceptance Criteria
- [x] Theory notebook complete with bias-variance decomposition and geometric interpretation
- [x] Bagging algorithm explained with bootstrap sampling analysis
- [x] Random Forest feature importance and decorrelation strategy
- [x] AdaBoost algorithm derivation with exponential loss minimization
- [x] Gradient Boosting framework and residual fitting intuition
- [ ] Stochastic gradient boosting variants explained
- [ ] Practical notebook with XGBoost implementation and hyperparameter interpretation
- [ ] LightGBM vs XGBoost trade-offs and when to use each
- [ ] Hyperparameter tuning via grid search and Bayesian optimization
- [ ] Both notebooks run top-to-bottom in Google Colab with no local setup

## Notes
TASK-SL7 (theory, verified 2026-07-13): notebooks/7a_ensemble_methods_theory.ipynb
covers the bias-variance decomposition (with an empirical repeated-resampling
demo), bagging's variance-of-average formula, Random Forest decorrelation and
feature importance, AdaBoost's exponential-loss derivation, and the gradient
boosting residual-fitting framework. From-scratch AdaBoost matches/exceeds
scikit-learn's AdaBoostClassifier.

"Stochastic gradient boosting variants" is left for TASK-SL8 (practical) —
XGBoost/LightGBM's subsample and colsample_bytree hyperparameters are the
natural place to cover row/column subsampling empirically, rather than
duplicating that ground in the theory notebook. TASK-SL8 remains in the
backlog; feature stays in_progress until it lands.
