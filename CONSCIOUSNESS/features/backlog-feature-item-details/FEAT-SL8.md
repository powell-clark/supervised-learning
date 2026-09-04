---
id: FEAT-SL8
status: backlog
priority: p2
kano: performance
title: Lesson 0 — Linear Regression theory and practice
description: Pair the existing Lesson 0 theory notebook with a practical notebook covering ordinary least squares, ridge, lasso and elastic net on a real regression dataset, with cross-validated regularisation, residual diagnostics and a numerical cross-check against the from-scratch solutions from 0a.
acceptance_criteria:
  - notebooks/0b_linear_regression_practical.ipynb executes end to end with stored outputs and zero errors
  - OLS, ridge, lasso and elastic net stated mathematically with 20+ LaTeX spans in total, including why the L1 penalty induces sparsity
  - Fitted with scikit-learn on datasets/London_Housing_Data.csv with a proper train/test split and cross-validated regularisation strength
  - Residual diagnostics shown and interpreted
  - scikit-learn OLS matches the 0a normal-equation and gradient-descent solutions to numerical precision
  - Passes scripts/verify_notebook.py --type practical
stories: [STORY-SL11]
tasks: []
code_paths:
  - notebooks/0a_linear_regression_theory.ipynb
  - notebooks/0b_linear_regression_practical.ipynb
---

# FEAT-SL8: Lesson 0 — Linear Regression theory and practice

## Context

Lesson 0 is the only lesson without a practical notebook. Its theory notebook
is also below the bar (18 LaTeX spans, emojis); the rewrite of 0a is tracked
under FEAT-SL9 (quality uplift), and 0b is tracked here, so the pair is
complete and consistent when both features close.

## Acceptance Criteria

- [ ] 0b exists and passes the practical verifier
- [ ] Regularisation mathematics stated and demonstrated on real data
- [ ] From-scratch cross-check against 0a to numerical precision
