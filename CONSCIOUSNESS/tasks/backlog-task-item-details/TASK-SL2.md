# TASK-SL2: Lesson 4b: SVM practical — kernel comparison and hyperparameter tuning

## Context

Create the practical notebook for Support Vector Machines. Apply SVMs to real datasets, demonstrating kernel methods in practice, hyperparameter tuning strategies, and comparison to from-scratch implementation from 4a.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/4b_svm_practical.ipynb`
- [ ] Dataset selection: Use a non-trivial classification problem (CIFAR-10 subset or similar)
- [ ] Kernel comparison: Linear, polynomial (degree 2-3), and RBF kernels with empirical results
- [ ] Hyperparameter tuning: Grid search over C (regularization) and kernel parameters (gamma for RBF)
- [ ] Cross-validation: 5-fold or 10-fold cross-validation for model selection
- [ ] Performance analysis: Confusion matrix, precision, recall, F1-score, ROC curve
- [ ] Comparison code: Show from-scratch implementation (from 4a) vs scikit-learn SVM side-by-side
- [ ] Visualization: Plot decision boundaries for 2D projections, learning curves, kernel comparison charts
- [ ] Mathematical explanation of why different kernels suit different data distributions
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: Scikit-learn documentation, ESL Chapter 12
- [ ] Notebook length: 40-50 hours effort (approximately 50-60KB when rendered)

## Technical Notes

Use scikit-learn.svm.SVC with different kernels. Show that kernel selection impacts runtime and accuracy. Explain time complexity: SVM is O(n²) to O(n³) depending on solver and kernel.

Demonstrate on a dataset with non-linearly separable classes to justify kernel trick effectiveness.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Code is production-quality with clear explanations
- [ ] Hyperparameter tuning is systematic and reproducible
- [ ] Results are analyzed and interpreted in context of theory from 4a
- [ ] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL1 (requires understanding from theory notebook)
