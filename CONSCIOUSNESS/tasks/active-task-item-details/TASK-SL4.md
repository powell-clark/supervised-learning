# TASK-SL4: Lesson 5b: KNN practical — optimal K selection, weighted voting, KD-tree implementation

## Context

Create the practical notebook for K-Nearest Neighbors. Apply KNN to real datasets, showing hyperparameter selection, weighted voting schemes, and the efficiency benefits of KD-tree from 5a.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/5b_knn_practical.ipynb`
- [ ] Optimal K selection: Cross-validation grid search, plot error vs K to show optimal choice
- [ ] Weighted KNN: Implement distance-weighted voting (weights = 1/distance)
- [ ] Dataset: Non-trivial classification problem with varied dimensionality
- [ ] Performance analysis: Confusion matrix, precision, recall, F1-score
- [ ] Efficiency comparison: Brute-force vs KD-tree search times on datasets of varying size
- [ ] Comparison to scikit-learn KNN
- [ ] Curse of dimensionality demonstration: Show KNN performance degrades with high dimensions
- [ ] Visualization: Confusion matrices, K vs error, search time comparison
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: Scikit-learn documentation, ESL Chapter 13
- [ ] Notebook length: 40-50 hours effort

## Technical Notes

Show that brute-force is O(n) search, KD-tree is O(log n) on average, important for large n. Demonstrate when KNN becomes impractical (high-dimensional data, large n).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Efficiency analysis is thorough and data-driven
- [ ] Practical limitations are clearly explained
- [ ] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL3 (requires understanding from theory notebook)
