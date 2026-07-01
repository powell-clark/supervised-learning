# STORY-SL4: Support Vector Machines theory and practice

## User Story

I want comprehensive coverage of Support Vector Machines so that I can understand maximum margin classification, kernel methods, and their practical application to real datasets.

## Context

Support Vector Machines are a cornerstone supervised learning algorithm. This story delivers theory-first treatment (mathematical derivations, from-scratch implementation) and practical notebooks (kernel comparison, hyperparameter tuning, real-world datasets).

## Acceptance Criteria

- [ ] Theory notebook (4a) covers maximum margin derivation, Lagrangian dual formulation, and kernel trick mathematics with >100 LaTeX symbols
- [ ] Theory notebook includes from-scratch SVM implementation with gradient descent on hinge loss (NumPy only)
- [ ] Theory notebook demonstrates convergence analysis and theoretical properties on standard datasets
- [ ] Practical notebook (4b) compares kernel methods (linear, RBF, polynomial) with empirical benchmarks
- [ ] Practical notebook shows hyperparameter tuning (C, gamma) via cross-validation
- [ ] Practical notebook includes code comparing to scikit-learn SVM
- [ ] Both notebooks follow CURRICULUM_ROADMAP quality standards: >20 math symbols, 40-50 hours effort
- [ ] No emojis, no hype language, no corporate buzzwords in either notebook
- [ ] References ESL Chapter 12, Stanford CS229 SVM lectures

## Definition of Done

- [ ] Both notebooks (4a and 4b) are academically rigorous, mathematically complete, and production-ready
- [ ] From-scratch implementation is clear enough for a student to understand and extend
- [ ] Notebooks are integrated into the lesson sequence and ready for publication

## Technical Notes

Quality benchmark: 1a_logistic_regression_theory has 194 math symbols, 7 implementations, 133KB. 4a should achieve similar depth.

## Story Points

18 (9 per task: 4a theory, 4b practical)
