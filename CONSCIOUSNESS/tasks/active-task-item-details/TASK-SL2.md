---
id: TASK-SL2
status: in_progress
priority: p2
title: Lesson 4b - SVM Practical Implementation
story_id: STORY-SL4
directive_id: DIRECT-SL1
blocked_by: TASK-SL1
expected_duration: 45h
story_points: 9
---

# Lesson 4b: SVM Practical Implementation

## Description

Create a comprehensive Jupyter notebook demonstrating practical SVM usage with scikit-learn, kernel comparison, and hyperparameter tuning. Build on the theory from Lesson 4a with real-world applications and original implementations that compare from-scratch results with library implementations.

## Acceptance Criteria

- [ ] Notebook loads without errors and all cells execute successfully
- [ ] Implement SVM with scikit-learn using at least 3 different kernels (linear, RBF, polynomial)
- [ ] Compare performance across kernels on breast cancer dataset (from Lesson 4a)
- [ ] Implement hyperparameter tuning for C and gamma using GridSearchCV or RandomizedSearchCV
- [ ] Visualization: decision boundaries for 2D projections showing margin and support vectors
- [ ] Visualization: kernel comparison heatmaps and performance metrics
- [ ] Include decision boundary visualization with margin and support vectors
- [ ] Demonstrate effect of regularization parameter C on margin and misclassification
- [ ] Code demonstrates understanding of kernel trick mathematics (no reimplementation required)
- [ ] Apply to real dataset with train/test split and cross-validation
- [ ] Performance metrics: accuracy, precision, recall, F1, confusion matrix
- [ ] Compare scikit-learn performance to from-scratch implementation from 4a
- [ ] ~20+ mathematical explanations (LaTeX symbols) for hyperparameter choices
- [ ] No emojis, no corporate language, academic rigor maintained
- [ ] Minimum file size: 120KB (comparable to 1b_logistic_regression_practical.ipynb at 171KB)

## Technical Scope

- Load breast cancer dataset (from sklearn.datasets or lesson 4a)
- Implement kernel comparison: linear, RBF, polynomial, sigmoid
- Hyperparameter grid: C in [0.1, 1, 10, 100], gamma in [0.001, 0.01, 0.1, 1, 'scale']
- Visualization of decision boundaries for best kernel
- Cross-validation: 5-fold or stratified k-fold
- Class imbalance handling: class_weight='balanced' or resampling discussion

## References

- Lesson 4a: Support Vector Machines Theory (maximum margin, kernel trick, Lagrangian duality)
- Scikit-learn SVM documentation
- Elements of Statistical Learning, Chapter 12
- Stanford CS229 lecture on SVMs (Andrew Ng)
