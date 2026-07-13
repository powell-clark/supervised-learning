---
id: FEAT-SL2
status: in_progress
priority: p2
kano: performance
title: Lesson 5 — K-Nearest Neighbors theory and practice
description: Complete KNN lesson with mathematical theory (distance metrics, KD-trees, curse of dimensionality) and practical implementation (optimal K, weighted voting, efficient search)
acceptance_criteria:
  - Theory notebook complete with distance metric derivations, KD-tree construction and traversal, and curse of dimensionality analysis
  - Practical notebook complete with optimal K selection via cross-validation, weighted voting schemes, and KD-tree vs brute force benchmarks
  - Both notebooks runnable end-to-end in Google Colab with dependencies installed in first cell
  - Includes NumPy implementation from scratch plus Scikit-learn comparison
  - Markdown cells document learning objectives, key formulas, and interpretation of results
stories: [STORY-SL5]
tasks: [TASK-SL3,TASK-SL4]
---

# FEAT-SL2: Lesson 5 — K-Nearest Neighbors

## Context
K-Nearest Neighbors is a foundational instance-based learning algorithm that forms
the bridge between parametric and non-parametric methods. The lesson covers both the
mathematical foundations (distance metrics, spatial indexing, asymptotic complexity)
and practical engineering (optimal hyperparameters, efficient retrieval, edge cases).

This feature ensures the lesson achieves comprehensive coverage, practical runnable
code, and the from-scratch NumPy derivation that makes the algorithm's mechanics
transparent.

## Acceptance Criteria
- [x] Theory notebook complete with distance metric derivations (Euclidean, Manhattan, Minkowski, cosine similarity)
- [x] KD-tree construction and nearest-neighbor search algorithm with pseudocode
- [x] Curse of dimensionality analysis with empirical demonstrations
- [x] Practical notebook with optimal K selection via k-fold cross-validation
- [x] Weighted voting schemes (inverse distance, kernel-based) with comparative analysis
- [x] Benchmarks: KD-tree vs brute force vs ball-tree retrieval performance
- [x] Both notebooks run top-to-bottom in Google Colab with no local setup
- [x] NumPy implementation of KD-tree search; Scikit-learn comparison
- [x] Markdown cells explain learning objectives, algorithm intuition, and result interpretation

## Notes
TASK-SL3 (theory) and TASK-SL4 (practical) were marked done, but the checkboxes
above were never verified against the actual notebooks. TASK-SL024 (verified
2026-07-13) did that verification and found three genuine defects, all fixed:
`notebooks/5a_k_nearest_neighbors_theory.ipynb` had never been executed end-to-end
(newline-stripped cell sources causing hard syntax errors, plus two real bugs in
the from-scratch KDTree — an attribute-order bug and an infinite-recursion bug from
not excluding the split median from its own subtree); `notebooks/5b_knn_practical.ipynb`'s
KD-tree-vs-brute-force benchmark measured `.fit()` time instead of retrieval time and
omitted ball-tree entirely. Both notebooks now execute end-to-end with zero errors
(44 + 55 cells). All acceptance criteria genuinely met; feature ready to move to
maintained (performance kano, agent-tier gate).
