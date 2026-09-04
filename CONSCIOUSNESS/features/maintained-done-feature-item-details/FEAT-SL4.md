---
id: FEAT-SL4
status: maintained
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
- [x] **AC-1** — Theory notebook complete with bias-variance decomposition and geometric interpretation
- [x] **AC-2** — Bagging algorithm explained with bootstrap sampling analysis
- [x] **AC-3** — Random Forest feature importance and decorrelation strategy
- [x] **AC-4** — AdaBoost algorithm derivation with exponential loss minimization
- [x] **AC-5** — Gradient Boosting framework and residual fitting intuition
- [x] **AC-6** — Stochastic gradient boosting variants explained — TASK-SL8's XGBoost `subsample`/`colsample_bytree` (row/column subsampling per Friedman's 1999 stochastic gradient boosting) explained and tuned via Optuna
- [x] **AC-7** — Practical notebook with XGBoost implementation and hyperparameter interpretation
- [x] **AC-8** — LightGBM vs XGBoost trade-offs and when to use each
- [x] **AC-9** — Hyperparameter tuning via grid search and Bayesian optimization
- [x] **AC-10** — Both notebooks run top-to-bottom in Google Colab with no local setup

## Notes
TASK-SL7 (theory, verified 2026-07-13): notebooks/7a_ensemble_methods_theory.ipynb
covers the bias-variance decomposition (with an empirical repeated-resampling
demo), bagging's variance-of-average formula, Random Forest decorrelation and
feature importance, AdaBoost's exponential-loss derivation, and the gradient
boosting residual-fitting framework. From-scratch AdaBoost matches/exceeds
scikit-learn's AdaBoostClassifier.

TASK-SL8 (practical, verified 2026-07-13): notebooks/7b_ensemble_methods_practical.ipynb
covers XGBoost/LightGBM with learning curves, early stopping, grid search and
Optuna Bayesian optimization, feature importance, bagging-vs-boosting, and a
direct comparison to 7a's from-scratch AdaBoost.

Gap found during closure: the frontmatter acceptance_criteria also lists
"ensemble combination strategies (voting, averaging, stacking)" — neither
notebook covers stacking or an explicit VotingClassifier, since it is
conceptually distinct from bagging/boosting (a meta-learner trained on
out-of-fold base-model predictions) and was not in either task's own detail
card. Filed TASK-SL022 for this rather than retrofitting it into an
already-substantial pair of notebooks.

An independent agent review (blind to this session's summary) re-executed the
from-scratch AdaBoost standalone, confirmed the 97.4% accuracy claim exactly,
confirmed 7a/7b share an identical split, and verdicted APPROVE — see
REVIEW-CCC025. Feature moves to maintained per the agent-tier gate (performance
kano).
