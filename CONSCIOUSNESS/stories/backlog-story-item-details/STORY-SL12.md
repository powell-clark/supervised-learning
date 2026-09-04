# STORY-SL12: Uniform quality uplift across lessons 0-9 so every notebook meets the published curriculum bar

## User Story

I want every existing notebook brought to the bar CURRICULUM_ROADMAP.md publishes so that a reader working through the corpus meets the same rigour in Lesson 0 as in Lesson 9, and no notebook still carries emojis, plain-text mathematics or unexecuted cells.

## Context

Measured 2026-09-04 over all 22 notebooks (dollar-delimited LaTeX spans in
markdown; roadmap bar is 100+ for theory, 20+ for practical; zero emojis):

| notebook | spans | emoji | note |
|---|---|---|---|
| 0a_linear_regression_theory | 18 | yes | 20 KB, far below the theory bar |
| 1b_logistic_regression_practical | 12 | no | below practical bar |
| 2b_decision_trees_practical | 24 | yes | |
| 2c_decision_trees_ATLAS | 0 | yes | |
| 3a_neural_networks_theory | 9 | yes | far below the theory bar |
| 3b_neural_networks_practical | 0 | no | |
| 5a_k_nearest_neighbors_theory | 1 | yes | 77 KB of markdown with mathematics as plain text and unicode (✓ ✗ ⟺); FEAT-SL2 agent-rejected |
| 5b_knn_practical | 0 | no | |
| 6b_naive_bayes_practical | 18 | no | |
| 7b_ensemble_methods_practical | 3 | no | |
| 8b_anomaly_detection_practical | 5 | no | |
| 9b_cnn_practical | 10 | no | |
| 9d_rnn_practical | 9 | no | |

Only 5 of 22 notebooks store executed outputs; the rest are unexecuted code
a reader has to trust. Lessons 1a, 2a, 4a, 6a, 7a, 8a, 9a, 9c already meet
the theory bar.

## Acceptance Criteria

- [ ] 0a, 3a and 5a each reach 100+ LaTeX spans with a numerically-checked from-scratch implementation and zero emojis
- [ ] Every practical notebook reaches 20+ LaTeX spans of mathematical explanation and zero emojis or marketing language
- [ ] Every notebook in `notebooks/` executes end to end in the verification environment with outputs stored and zero error outputs
- [ ] FEAT-SL2 (Lesson 5 — K-Nearest Neighbors theory and practice) is re-verified and agent-approved after the 5a conversion
- [ ] `scripts/verify_notebook.py --all` passes for the whole corpus

## References

- CURRICULUM_ROADMAP.md (Quality Checklist for New Lessons)
- CONSCIOUSNESS/reviews/REVIEW-INDEX.md REVIEW-CCC049 (FEAT-SL2 agent-rejected)
