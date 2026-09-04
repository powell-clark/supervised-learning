# STORY-SL11: Lesson 0 linear regression practical so the foundational lesson has the same theory-plus-practice pair as every other lesson

## User Story

I want Lesson 0 to have a practical notebook so that the corpus opens with the same theory-then-practice shape every later lesson uses, and regularised regression (ridge, lasso, elastic net) is taught in context rather than left to a footnote.

## Context

Every lesson from 1 to 9 has an `a` (theory) and `b` (practical) notebook;
Lesson 0 has only `0a_linear_regression_theory.ipynb`. The roadmap's "Better
approach" section says feature engineering, model evaluation and
hyperparameter tuning belong inside practical notebooks — 0b is the natural
home for regularisation, cross-validated model selection and residual
diagnostics on a real regression dataset (the London housing data already in
`datasets/`).

## Acceptance Criteria

- [ ] `notebooks/0b_linear_regression_practical.ipynb` exists, executes end to end with stored outputs and zero errors
- [ ] Ordinary least squares, ridge, lasso and elastic net are each stated mathematically (objective, closed form where one exists, why L1 induces sparsity) with 20+ LaTeX spans in total
- [ ] Models are fitted with scikit-learn on the London housing dataset with a chronological or stratified train/test split and cross-validated regularisation strength
- [ ] Residual diagnostics (residuals vs fitted, Q-Q, heteroscedasticity check) are shown and interpreted
- [ ] The scikit-learn OLS fit is cross-checked against the from-scratch normal-equation and gradient-descent solutions from 0a to numerical precision
- [ ] Passes `scripts/verify_notebook.py --type practical`

## References

- notebooks/0a_linear_regression_theory.ipynb
- datasets/London_Housing_Data.csv
- ESL Chapter 3 (Linear Methods for Regression)
