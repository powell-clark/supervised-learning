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
- [ ] Theory notebook complete with distance metric derivations (Euclidean, Manhattan, Minkowski, cosine similarity)
- [ ] KD-tree construction and nearest-neighbor search algorithm with pseudocode
- [ ] Curse of dimensionality analysis with empirical demonstrations
- [ ] Practical notebook with optimal K selection via k-fold cross-validation
- [ ] Weighted voting schemes (inverse distance, kernel-based) with comparative analysis
- [ ] Benchmarks: KD-tree vs brute force vs ball-tree retrieval performance
- [ ] Both notebooks run top-to-bottom in Google Colab with no local setup
- [ ] NumPy implementation of KD-tree search; Scikit-learn comparison
- [ ] Markdown cells explain learning objectives, algorithm intuition, and result interpretation

## Notes
Work is in progress under TASK-SL3 (theory) and TASK-SL4 (practical). This feature
card documents the acceptance bar that both tasks must satisfy when complete.
