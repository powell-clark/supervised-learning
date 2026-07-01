---
id: FEAT-SL3
status: backlog
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
---

# FEAT-SL3: Lesson 6 — Naive Bayes

## Context
Naive Bayes is a probabilistic classifier grounded in Bayes theorem with a strong
conditional independence assumption. Despite its simplicity, it performs remarkably
well on text and high-dimensional data. The lesson covers the mathematical foundation
and practical applications in text classification.

## Acceptance Criteria
- [ ] Theory notebook complete with Bayes theorem derivation and geometric interpretation
- [ ] Conditional independence assumption explained with worked examples
- [ ] Gaussian Naive Bayes for continuous features with derivation
- [ ] Multinomial Naive Bayes for text classification (bag-of-words)
- [ ] Bernoulli Naive Bayes variant explained
- [ ] Laplace smoothing problem and solution documented
- [ ] Practical notebook with text classification case study (e.g., spam detection)
- [ ] TF-IDF vectorization with NumPy and Scikit-learn comparison
- [ ] Both notebooks run top-to-bottom in Google Colab with no local setup
- [ ] Accuracy, precision, recall, F1 analysis on classification results

## Notes
TASK-SL5 (theory) and TASK-SL6 (practical) pending. This feature card documents
the acceptance bar both tasks must meet when complete.
