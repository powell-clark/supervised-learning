# TASK-SL1: Lesson 4a: SVM theory — maximum margin, Lagrangian dual, kernel trick

## Context

Create the theory notebook for Support Vector Machines. This is a foundational algorithm and the notebook must build from first principles, deriving the maximum margin classifier, the Lagrangian dual formulation, and the kernel trick. Include from-scratch NumPy implementation of SVM with hinge loss optimization.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/4a_svm_theory.ipynb`
- [ ] Mathematical derivation of maximum margin classifier from optimization perspective (minimize ||w||, subject to y_i(w·x_i + b) ≥ 1)
- [ ] Lagrangian dual formulation derived step-by-step using KKT conditions
- [ ] Kernel trick explained mathematically with kernel functions (linear, polynomial, RBF)
- [ ] From-scratch SVM implementation using gradient descent on hinge loss (NumPy only, no scikit-learn/PyTorch)
- [ ] Implementation achieves >100 LaTeX math symbols in total (target: 120+)
- [ ] Code demonstrates SVM on standard dataset (MNIST or similar)
- [ ] Convergence analysis included: show training loss decreasing over iterations
- [ ] Compare from-scratch implementation output to scikit-learn baseline
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: MIT 6.034 SVM notes, Stanford CS229 lectures, ESL Chapter 12
- [ ] Notebook length: 40-50 hours effort (approximately 50-60KB when rendered)

## Technical Notes

Quality benchmark: 1a_logistic_regression_theory has 194 math symbols, 7 implementations, 133KB. Aim for similar depth.

Use Lagrangian formulation: L(w, b, α) = (1/2)||w||² - Σ α_i[y_i(w·x_i + b) - 1]. Derive dual: maximise Σα_i - (1/2)Σα_i α_j y_i y_j x_i·x_j subject to Σα_i y_i = 0, 0 ≤ α_i ≤ C.

Implement gradient descent on hinge loss: L(y, ŷ) = max(0, 1 - y·ŷ).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Code is clean, well-commented, and educationally clear
- [ ] Mathematical derivations are step-by-step with no jumps in logic
- [ ] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)
