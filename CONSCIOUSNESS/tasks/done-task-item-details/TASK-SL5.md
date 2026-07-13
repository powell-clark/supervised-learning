# TASK-SL5: Lesson 6a: Naive Bayes theory — Bayes theorem, conditional independence, Gaussian/Multinomial/Bernoulli variants

## Context

Create the theory notebook for Naive Bayes. Build from first principles covering Bayes' theorem, the conditional independence assumption, and three major variants. Include from-scratch implementation of Gaussian Naive Bayes.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/6a_naive_bayes_theory.ipynb`
- [x] Bayes' theorem derived and explained with clear notation (>100 LaTeX symbols) — 250 dollar-delimited math spans
- [x] Conditional independence assumption explained and its implications
- [x] Gaussian Naive Bayes: Derivation assuming normally distributed features
- [x] Multinomial Naive Bayes: Application to document/text data
- [x] Bernoulli Naive Bayes: Application to binary feature data
- [x] From-scratch Gaussian NB implementation using MLE for parameter estimation (NumPy)
- [x] Derivation of parameter estimation: mean and variance from training data
- [x] Comparison to scikit-learn Naive Bayes — exact match (0.00e+00 parameter difference, 100% prediction agreement)
- [x] Theoretical analysis: When conditional independence assumption holds/breaks
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: Murphy's "Machine Learning: A Probabilistic Perspective" Chapter 3, Bishop PRML
- [x] Notebook length: 40-50 hours effort — 42.8KB rendered, 40 cells

## Technical Notes

Gaussian NB parameters: μ_j and σ_j estimated from training data using MLE. P(y) estimated as class frequency. P(x_i|y) = N(x_i; μ_{i,y}, σ²_{i,y}).

Show that despite conditional independence assumption being violated in practice, NB often works well due to parameter robustness.

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] From-scratch implementation is clear and matches scikit-learn results
- [x] Mathematical foundations are rigorous and well-explained
- [x] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL4 (lesson sequencing)
