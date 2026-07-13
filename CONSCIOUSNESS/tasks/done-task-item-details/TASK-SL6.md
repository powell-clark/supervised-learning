# TASK-SL6: Lesson 6b: Naive Bayes practical — text classification, TF-IDF, Laplace smoothing

## Context

Create the practical notebook for Naive Bayes. Apply NB to text classification, demonstrating TF-IDF vectorization, Laplace smoothing for sparse data handling, and comparison to from-scratch implementation.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/6b_naive_bayes_practical.ipynb`
- [x] Dataset: Text classification problem (20 Newsgroups subset, 4 categories, multi-class)
- [x] TF-IDF vectorization: Explain mathematics and implement with scikit-learn
- [x] Laplace smoothing: Show why necessary for text (zero counts), demonstrate effect on performance — measured 70-82% of test docs per class hit an unseen word; alpha sweep shows the accuracy trade-off
- [x] Multinomial NB for text: Apply to TF-IDF vectors
- [x] Gaussian NB comparison: Show why less suitable for text data — GaussianNB scores 81.1% vs MultinomialNB's 87.3% on identical features, tied to feature sparsity (99.6% zeros)
- [x] Performance analysis: Precision, recall, F1-score, confusion matrix
- [x] Comparison: From-scratch implementation (from 6a) vs scikit-learn — built a from-scratch MultinomialNaiveBayes extending 6a's derivation, matches sklearn to 1.78e-15
- [x] Error analysis: Show failure cases and discuss why
- [x] Visualization: Confusion matrix, most informative features per class, per-class performance
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: Scikit-learn documentation, Bishop PRML
- [x] Notebook length: 40-50 hours effort — 27.8KB rendered, 27 cells

## Technical Notes

Laplace smoothing: Add 1 to all counts to avoid zero probabilities. This is a form of regularization.

TF-IDF: term frequency × inverse document frequency. Show the mathematics and why it emphasizes discriminative terms.

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] Text classification results are meaningful and analyzed
- [x] Laplace smoothing impact is demonstrated empirically
- [x] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL5 (requires understanding from theory notebook)
