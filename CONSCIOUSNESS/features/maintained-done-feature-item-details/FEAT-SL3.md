---
id: FEAT-SL3
status: maintained
priority: p2
kano: performance
title: Lesson 6 — Naive Bayes theory and practice
description: Complete Naive Bayes lesson with mathematical theory (Bayes theorem, conditional independence assumption) and practical implementation (text classification, TF-IDF, Laplace smoothing)
acceptance_criteria:
  - Theory notebook complete with Bayes theorem derivation, conditional independence explanation, and Gaussian/Multinomial/Bernoulli variant math
  - Practical notebook complete with text classification case study and TF-IDF analysis
  - Both notebooks runnable end-to-end in Google Colab with dependencies installed in first cell
  - Includes NumPy implementation of Naive Bayes from scratch plus Scikit-learn comparison
  - Markdown cells document learning objectives, key formulas, and interpretation of results
stories: [STORY-SL6]
tasks: [TASK-SL5,TASK-SL6]
code_paths:
  - notebooks/6a_naive_bayes_theory.ipynb
  - notebooks/6b_naive_bayes_practical.ipynb
---

# FEAT-SL3: Lesson 6 — Naive Bayes

## Context
Naive Bayes is a probabilistic classifier grounded in Bayes theorem with a strong
conditional independence assumption. Despite its simplicity, it performs remarkably
well on text and high-dimensional data. The lesson covers the mathematical foundation
and practical applications in text classification.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook complete with Bayes theorem derivation and geometric interpretation
- [x] **AC-2** — Conditional independence assumption explained with worked examples
- [x] **AC-3** — Gaussian Naive Bayes for continuous features with derivation
- [x] **AC-4** — Multinomial Naive Bayes for text classification (bag-of-words)
- [x] **AC-5** — Bernoulli Naive Bayes variant explained
- [x] **AC-6** — Laplace smoothing problem and solution documented
- [x] **AC-7** — Practical notebook with text classification case study (20 Newsgroups subset, 4-class)
- [x] **AC-8** — TF-IDF vectorization with NumPy and Scikit-learn comparison — from-scratch NumPy TF-IDF matches scikit-learn to 2.22e-16
- [x] **AC-9** — Both notebooks run top-to-bottom in Google Colab with no local setup
- [x] **AC-10** — Accuracy, precision, recall, F1 analysis on classification results

## Notes
TASK-SL5 (theory, verified 2026-07-13): notebooks/6a_naive_bayes_theory.ipynb covers
Bayes' theorem, conditional independence, all three variants, Laplace smoothing, and
a from-scratch Gaussian NB matching scikit-learn exactly.

TASK-SL6 (practical, verified 2026-07-13): notebooks/6b_naive_bayes_practical.ipynb
covers TF-IDF (with a from-scratch NumPy implementation matching scikit-learn),
a from-scratch MultinomialNB matching scikit-learn, an empirical Laplace-smoothing
sweep, a GaussianNB-on-text comparison showing why it underperforms, confusion
matrix, most-informative-features, and error analysis on the 20 Newsgroups subset.

All acceptance criteria met. An independent agent review (blind to this
session's summary) re-executed the from-scratch implementations against live
scikit-learn and verdicted APPROVE — see REVIEW-CCC018. Feature moves to
maintained per the agent-tier gate (performance kano).
