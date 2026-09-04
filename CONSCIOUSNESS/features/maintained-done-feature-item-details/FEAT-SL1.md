---
id: FEAT-SL1
status: maintained
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
tasks: [TASK-SL1,TASK-SL2,TASK-SL020]
---

# FEAT-SL1: Lesson 4 — Support Vector Machines

## Context
Support Vector Machines form the bridge between linear and non-linear classification.
The lesson covers both the mathematical foundations (optimization, duality, kernels)
and practical engineering (kernel selection, soft margins, hyperparameter tuning).

This feature ensures comprehensive theory coverage, practical implementation details,
and the NumPy derivation that exposes the algorithm's internal mechanics.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook complete with maximum margin problem formulation and geometric interpretation
- [x] **AC-2** — Lagrangian dual formulation with KKT conditions and complementary slackness
- [x] **AC-3** — Kernel trick explanation with polynomial, RBF, and linear kernel derivations
- [x] **AC-4** — Soft margin formulation (C parameter) with geometric interpretation
- [x] **AC-5** — Practical notebook with comparison of kernel types on binary classification
- [x] **AC-6** — Hyperparameter tuning via grid search with cross-validation
- [x] **AC-7** — Multi-class extension (one-vs-rest, one-vs-one) explained
- [x] **AC-8** — Both notebooks run top-to-bottom in Google Colab with no local setup
- [x] **AC-9** — NumPy implementation of linear SVM; Scikit-learn comparison

## Notes
TASK-SL1 (theory) and TASK-SL2 (practical) are complete. TASK-SL020 (verified 2026-07-13)
closed the remaining gap: notebooks/4b_support_vector_machines_practical.ipynb now
covers the multi-class extension (one-vs-rest, one-vs-one) with a Digits-dataset
demonstration (K=10) showing OvR's 10 classifiers vs OvO's 45, and confirms
scikit-learn's SVC reduces multi-class to one-vs-one internally regardless of
decision_function_shape. Independent review (REVIEW-CCC046, blind to implementer
summary) confirmed both notebooks execute end-to-end with zero errors and
independently re-verified the multi-class demonstration's classifier counts and
decision_function shapes via a standalone script. Verdict: APPROVE. Feature moved
to maintained 2026-07-13 (performance kano, agent-tier gate).
