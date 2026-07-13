# TASK-SL1: Lesson 4a: SVM theory — maximum margin, Lagrangian dual, kernel trick

## Context

Create the theory notebook for Support Vector Machines. This is a foundational algorithm and the notebook must build from first principles, deriving the maximum margin classifier, the Lagrangian dual formulation, and the kernel trick. Include from-scratch NumPy implementation of SVM with hinge loss optimization.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/4a_svm_theory.ipynb`
- [x] Mathematical derivation of maximum margin classifier from optimization perspective (minimize ||w||, subject to y_i(w·x_i + b) ≥ 1)
- [x] Lagrangian dual formulation derived step-by-step using KKT conditions
- [x] Kernel trick explained mathematically with kernel functions (linear, polynomial, RBF)
- [x] From-scratch SVM implementation using gradient descent on hinge loss (NumPy only, no scikit-learn/PyTorch)
- [x] Implementation achieves >100 LaTeX math symbols in total (target: 120+) — 128 dollar-delimited math spans across the derivation
- [x] Code demonstrates SVM on standard dataset (breast cancer dataset, consistent with 4b's practical notebook)
- [x] Convergence analysis included: show training loss decreasing over iterations
- [x] Compare from-scratch implementation output to scikit-learn baseline
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: MIT 6.034 SVM notes, Stanford CS229 lectures, ESL Chapter 12
- [x] Notebook length: 40-50 hours effort (approximately 50-60KB when rendered) — 57.7KB rendered

## Technical Notes

Quality benchmark: 1a_logistic_regression_theory has 194 math symbols, 7 implementations, 133KB. Aim for similar depth.

Use Lagrangian formulation: L(w, b, α) = (1/2)||w||² - Σ α_i[y_i(w·x_i + b) - 1]. Derive dual: maximise Σα_i - (1/2)Σα_i α_j y_i y_j x_i·x_j subject to Σα_i y_i = 0, 0 ≤ α_i ≤ C.

Implement gradient descent on hinge loss: L(y, ŷ) = max(0, 1 - y·ŷ).

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] Code is clean, well-commented, and educationally clear
- [x] Mathematical derivations are step-by-step with no jumps in logic
- [x] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)
