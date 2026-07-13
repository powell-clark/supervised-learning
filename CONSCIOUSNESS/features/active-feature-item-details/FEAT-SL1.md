---
id: FEAT-SL1
status: backlog
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
- [ ] Theory notebook complete with maximum margin problem formulation and geometric interpretation
- [ ] Lagrangian dual formulation with KKT conditions and complementary slackness
- [ ] Kernel trick explanation with polynomial, RBF, and linear kernel derivations
- [ ] Soft margin formulation (C parameter) with geometric interpretation
- [ ] Practical notebook with comparison of kernel types on binary classification
- [ ] Hyperparameter tuning via grid search with cross-validation
- [ ] Multi-class extension (one-vs-rest, one-vs-one) explained
- [ ] Both notebooks run top-to-bottom in Google Colab with no local setup
- [ ] NumPy implementation of linear SVM; Scikit-learn comparison

## Notes
TASK-SL1 and TASK-SL2 are complete. This feature card documents the acceptance bar
that was met by those tasks.
