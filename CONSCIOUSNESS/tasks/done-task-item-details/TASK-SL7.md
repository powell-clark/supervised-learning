# TASK-SL7: Lesson 7a: Ensemble Methods theory — bias-variance, bagging, AdaBoost, gradient boosting

## Context

Create the theory notebook for Ensemble Methods. Cover bias-variance decomposition, bagging for variance reduction, AdaBoost for boosting weak learners, and gradient boosting. Include from-scratch AdaBoost implementation.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/7a_ensemble_methods_theory.ipynb`
- [x] Bias-variance decomposition: Mathematical derivation with clear interpretation (>100 LaTeX symbols) — 176 dollar-delimited spans, plus an empirical repeated-resampling demo confirming the decomposition
- [x] Bagging: Theory of parallel ensemble construction and variance reduction
- [x] Bootstrap aggregating mathematics: Why averaging reduces variance — variance-of-average formula derived and verified numerically against synthetic correlated predictors
- [x] AdaBoost: Step-by-step derivation of weight update rules and weak learner focus
- [x] AdaBoost algorithm with full mathematical development: Weight update formula, error bound
- [x] Gradient boosting framework: Explain as iterative residual fitting
- [x] From-scratch AdaBoost implementation using decision stumps as weak learners (NumPy) — matches/exceeds scikit-learn's AdaBoostClassifier (97.4% vs 96.5% test accuracy)
- [x] Derivation of exponential loss and its connection to classification error
- [x] Comparison of different ensemble approaches on standard datasets — single tree, bagging, Random Forest, sklearn AdaBoost, and from-scratch AdaBoost compared on breast cancer
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: ESL Chapter 10, Friedman's gradient boosting papers, Schapire AdaBoost
- [x] Notebook length: 50 hours effort — 43.1KB rendered, 30 cells

## Technical Notes

AdaBoost weight update: α_m = (1/2) * ln((1-err_m)/err_m), sample weight w_{i,m+1} = w_{i,m} * exp(-α_m * y_i * h_m(x_i))

Gradient boosting: F_m(x) = F_{m-1}(x) + γ_m * h_m(x) where h_m fits residuals y_i - F_{m-1}(x_i).

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] From-scratch AdaBoost is correct and shows clear algorithm steps
- [x] Mathematical derivations are rigorous and well-explained
- [x] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL6 (lesson sequencing)
