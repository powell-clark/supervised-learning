# TASK-SL3: Lesson 5a: KNN theory — distance metrics, KD-tree mathematics, curse of dimensionality

## Context

Create the theory notebook for K-Nearest Neighbors. Build from first principles covering distance metrics, the KD-tree data structure for efficient search, and the curse of dimensionality. Include from-scratch implementation with KD-tree.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/5a_knn_theory.ipynb`
- [ ] Distance metrics covered: Euclidean, Manhattan, Minkowski with mathematical definitions (>100 LaTeX symbols)
- [ ] KD-tree data structure: Mathematical foundations, construction algorithm, search algorithm, time complexity analysis
- [ ] From-scratch KNN implementation using brute-force search (NumPy)
- [ ] From-scratch KD-tree implementation showing efficiency improvements
- [ ] Curse of dimensionality: Mathematical explanation of why Euclidean distance breaks down in high dimensions
- [ ] Convergence analysis: Show KNN asymptotic properties and generalization bounds
- [ ] Compare from-scratch implementation to scikit-learn baseline
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: ESL Chapter 13, Hastie et al., Bentley KD-tree paper
- [ ] Notebook length: 40-50 hours effort

## Technical Notes

KD-tree construction: O(n log n) with median-of-medians. Search: O(log n) average, O(n) worst-case. Show the efficiency difference empirically.

Implement KD-tree from scratch to demonstrate: node structure, recursive partitioning, nearest-neighbor search with pruning.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] KD-tree implementation is correct and efficient
- [ ] Mathematical explanations are clear and step-by-step
- [ ] Curse of dimensionality is demonstrated with empirical examples
- [ ] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL2 (lesson sequencing)
