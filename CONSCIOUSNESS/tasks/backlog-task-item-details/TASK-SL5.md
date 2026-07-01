# TASK-SL5: Lesson 6a: Naive Bayes theory — Bayes theorem, conditional independence, Gaussian/Multinomial/Bernoulli variants

## Context

Create the theory notebook for Naive Bayes. Build from first principles covering Bayes' theorem, the conditional independence assumption, and three major variants. Include from-scratch implementation of Gaussian Naive Bayes.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/6a_naive_bayes_theory.ipynb`
- [ ] Bayes' theorem derived and explained with clear notation (>100 LaTeX symbols)
- [ ] Conditional independence assumption explained and its implications
- [ ] Gaussian Naive Bayes: Derivation assuming normally distributed features
- [ ] Multinomial Naive Bayes: Application to document/text data
- [ ] Bernoulli Naive Bayes: Application to binary feature data
- [ ] From-scratch Gaussian NB implementation using MLE for parameter estimation (NumPy)
- [ ] Derivation of parameter estimation: mean and variance from training data
- [ ] Comparison to scikit-learn Naive Bayes
- [ ] Theoretical analysis: When conditional independence assumption holds/breaks
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: Murphy's "Machine Learning: A Probabilistic Perspective" Chapter 3, Bishop PRML
- [ ] Notebook length: 40-50 hours effort

## Technical Notes

Gaussian NB parameters: μ_j and σ_j estimated from training data using MLE. P(y) estimated as class frequency. P(x_i|y) = N(x_i; μ_{i,y}, σ²_{i,y}).

Show that despite conditional independence assumption being violated in practice, NB often works well due to parameter robustness.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch implementation is clear and matches scikit-learn results
- [ ] Mathematical foundations are rigorous and well-explained
- [ ] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL4 (lesson sequencing)
