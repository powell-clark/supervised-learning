# STORY-SL7: Ensemble Methods theory and practice

## User Story

I want comprehensive understanding of ensemble methods so that I can build powerful composite models, understand bias-variance trade-offs, and apply AdaBoost and gradient boosting effectively.

## Context

Ensemble methods are among the most powerful algorithms in machine learning. This story covers the mathematical theory (bias-variance decomposition, bagging, AdaBoost, gradient boosting) and practical application with modern libraries like XGBoost and LightGBM.

## Acceptance Criteria

- [x] Theory notebook (7a) covers bias-variance decomposition, bagging mathematics, AdaBoost derivation, and gradient boosting theory with >100 LaTeX symbols — 176 dollar-delimited spans
- [x] Theory notebook includes from-scratch AdaBoost implementation with derivation of weight updates (NumPy only)
- [x] Theory notebook demonstrates convergence analysis and theoretical properties on standard datasets — empirical bias-variance repeated-resampling demo, training-error-vs-round curve
- [x] Practical notebook (7b) shows XGBoost and LightGBM with hyperparameter tuning strategies
- [x] Practical notebook demonstrates feature importance analysis and model interpretation
- [ ] Practical notebook includes comparison of bagging, boosting, and stacking approaches — bagging vs boosting compared directly; stacking deferred to TASK-SL022 (see FEAT-SL4 notes)
- [x] Both notebooks follow CURRICULUM_ROADMAP quality standards: >20 math symbols, 50 hours effort
- [x] No emojis, no hype language, no corporate buzzwords
- [x] References ESL Chapter 10 and Friedman's gradient boosting papers

## Definition of Done

- [x] Both notebooks are mathematically rigorous and implementation-ready
- [x] From-scratch AdaBoost implementation shows clear understanding of algorithm mechanics
- [x] Practical examples demonstrate hyperparameter impact and model behavior
- [x] Notebooks ready for publication

## Story Points

20 (10 per task: 7a theory, 7b practical)
