# TASK-SL6: Lesson 6b: Naive Bayes practical — text classification, TF-IDF, Laplace smoothing

## Context

Create the practical notebook for Naive Bayes. Apply NB to text classification, demonstrating TF-IDF vectorization, Laplace smoothing for sparse data handling, and comparison to from-scratch implementation.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/6b_naive_bayes_practical.ipynb`
- [ ] Dataset: Text classification problem (e.g., sentiment analysis or spam detection)
- [ ] TF-IDF vectorization: Explain mathematics and implement with scikit-learn
- [ ] Laplace smoothing: Show why necessary for text (zero counts), demonstrate effect on performance
- [ ] Multinomial NB for text: Apply to TF-IDF vectors
- [ ] Gaussian NB comparison: Show why less suitable for text data
- [ ] Performance analysis: Precision, recall, F1-score, confusion matrix
- [ ] Comparison: From-scratch implementation (from 6a) vs scikit-learn
- [ ] Error analysis: Show failure cases and discuss why
- [ ] Visualization: Confusion matrix, most informative features per class, per-class performance
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: Scikit-learn documentation, Bishop PRML
- [ ] Notebook length: 40-50 hours effort

## Technical Notes

Laplace smoothing: Add 1 to all counts to avoid zero probabilities. This is a form of regularization.

TF-IDF: term frequency × inverse document frequency. Show the mathematics and why it emphasizes discriminative terms.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Text classification results are meaningful and analyzed
- [ ] Laplace smoothing impact is demonstrated empirically
- [ ] Ready for peer review and publication

## Story Points

9 (45 hours estimated effort)

## Blocked By

TASK-SL5 (requires understanding from theory notebook)
