# STORY-SL6: Naive Bayes theory and practice

## User Story

I want deep understanding of Naive Bayes so that I can build probabilistic classifiers, understand the conditional independence assumption, and know when and why it works.

## Context

Naive Bayes is foundational for probabilistic modeling and remains highly practical for text classification. This story covers Bayes' theorem from first principles, conditional independence, and multiple variants (Gaussian, Multinomial, Bernoulli).

## Acceptance Criteria

- [ ] Theory notebook (6a) derives Bayes' theorem, conditional independence assumption, and probabilistic interpretation with >100 LaTeX symbols
- [ ] Theory notebook covers Gaussian, Multinomial, and Bernoulli variants with mathematical foundations
- [ ] Theory notebook includes from-scratch Gaussian NB with MLE parameter estimation (NumPy only)
- [ ] Theory notebook demonstrates convergence analysis and theoretical properties on standard datasets
- [ ] Practical notebook (6b) applies NB to text classification with TF-IDF vectorization
- [ ] Practical notebook shows Laplace smoothing and its effect on sparse data
- [ ] Practical notebook compares from-scratch implementation to scikit-learn NB
- [ ] Both notebooks follow CURRICULUM_ROADMAP quality standards: >20 math symbols, 40-50 hours effort
- [ ] No emojis, no hype language, no corporate buzzwords
- [ ] References Murphy's "Machine Learning: A Probabilistic Perspective" Chapter 3

## Definition of Done

- [ ] Both notebooks are mathematically complete and implementation-ready
- [ ] From-scratch implementation is clear and extensible to other variants
- [ ] Notebooks ready for publication

## Story Points

18 (9 per task: 6a theory, 6b practical)
