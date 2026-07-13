---
id: FEAT-SL1
status: in_progress
priority: p2
kano: performance
title: Lesson 4 — Support Vector Machines theory and practice
description: Complete SVM lesson with mathematical theory (maximum margin, Lagrangian dual, kernel trick) and practical implementation (kernel comparison, hyperparameter tuning, soft margins)
acceptance_criteria:
  - Theory notebook complete with maximum margin derivation, Lagrangian dual formulation, and kernel trick explanation
  - Practical notebook complete with kernel comparison study and hyperparameter tuning via grid search
  - Both notebooks runnable end-to-end in Google Colab with dependencies installed in first cell
  - Includes NumPy implementation of linear SVM plus Scikit-learn comparison
  - Markdown cells document learning objectives, key formulas, and interpretation of results
stories: [STORY-SL4]
tasks: [TASK-SL1,TASK-SL2]
---

# FEAT-SL1: Lesson 4 — Support Vector Machines

## Context
Support Vector Machines form the bridge between linear and non-linear classification.
The lesson covers both the mathematical foundations (optimization, duality, kernels)
and practical engineering (kernel selection, soft margins, hyperparameter tuning).

This feature ensures comprehensive theory coverage, practical implementation details,
and the NumPy derivation that exposes the algorithm's internal mechanics.

## Acceptance Criteria
- [x] Theory notebook complete with maximum margin problem formulation and geometric interpretation
- [x] Lagrangian dual formulation with KKT conditions and complementary slackness
- [x] Kernel trick explanation with polynomial, RBF, and linear kernel derivations
- [x] Soft margin formulation (C parameter) with geometric interpretation
- [x] Practical notebook with comparison of kernel types on binary classification
- [x] Hyperparameter tuning via grid search with cross-validation
- [ ] Multi-class extension (one-vs-rest, one-vs-one) explained
- [x] Both notebooks run top-to-bottom in Google Colab with no local setup
- [x] NumPy implementation of linear SVM; Scikit-learn comparison

## Notes
TASK-SL1 is complete (theory notebook, verified 2026-07-13). TASK-SL2 (practical
notebook) is marked done in the index but does not cover the multi-class extension
(one-vs-rest, one-vs-one) acceptance criterion — see TASK-SL020 for the follow-up.
Feature stays in_progress until that gap closes.
