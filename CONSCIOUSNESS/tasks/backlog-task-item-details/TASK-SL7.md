# TASK-SL7: Lesson 7a: Ensemble Methods theory — bias-variance, bagging, AdaBoost, gradient boosting

## Context

Create the theory notebook for Ensemble Methods. Cover bias-variance decomposition, bagging for variance reduction, AdaBoost for boosting weak learners, and gradient boosting. Include from-scratch AdaBoost implementation.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/7a_ensemble_methods_theory.ipynb`
- [ ] Bias-variance decomposition: Mathematical derivation with clear interpretation (>100 LaTeX symbols)
- [ ] Bagging: Theory of parallel ensemble construction and variance reduction
- [ ] Bootstrap aggregating mathematics: Why averaging reduces variance
- [ ] AdaBoost: Step-by-step derivation of weight update rules and weak learner focus
- [ ] AdaBoost algorithm with full mathematical development: Weight update formula, error bound
- [ ] Gradient boosting framework: Explain as iterative residual fitting
- [ ] From-scratch AdaBoost implementation using decision stumps as weak learners (NumPy)
- [ ] Derivation of exponential loss and its connection to classification error
- [ ] Comparison of different ensemble approaches on standard datasets
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: ESL Chapter 10, Friedman's gradient boosting papers, Schapire AdaBoost
- [ ] Notebook length: 50 hours effort

## Technical Notes

AdaBoost weight update: α_m = (1/2) * ln((1-err_m)/err_m), sample weight w_{i,m+1} = w_{i,m} * exp(-α_m * y_i * h_m(x_i))

Gradient boosting: F_m(x) = F_{m-1}(x) + γ_m * h_m(x) where h_m fits residuals y_i - F_{m-1}(x_i).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch AdaBoost is correct and shows clear algorithm steps
- [ ] Mathematical derivations are rigorous and well-explained
- [ ] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL6 (lesson sequencing)
