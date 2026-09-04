# TASK-SL035: Uplift practicals 5b, 6b, 7b, 8b to the practical bar

## Context

Measured 2026-09-04 against the practical bar (20+ LaTeX spans, zero emojis): `5b_knn_practical` 0 spans (263 KB, 55 cells), `6b_naive_bayes_practical` 18 spans, `7b_ensemble_methods_practical` 3 spans, `8b_anomaly_detection_practical` 5 spans. Their theory partners are all at or above the bar (6a at 125 spans, 7a at 88, 8a at 68), so the mathematics exists in the lesson — it is the practical half that states results without stating what is being computed.

## Acceptance Criteria

- [ ] All four notebooks reach at least 20 LaTeX spans, zero emojis, zero marketing words
- [ ] `5b`: distance-weighted voting written as $\hat y = \arg\max_c \sum_{i \in N_k(x)} w_i \mathbb{1}[y_i = c]$ with $w_i = 1/d(x,x_i)$; the cross-validation objective for choosing $k$; and the time-complexity comparison between brute force and KD-tree tied to the timings the notebook already measures
- [ ] `6b`: TF-IDF written out — term frequency, inverse document frequency $\log(N/df_t)$, and the product — plus multinomial Naive Bayes' posterior $\propto P(c)\prod_i P(w_i|c)^{x_i}$ in log space, and Laplace smoothing $\frac{count + \alpha}{total + \alpha V}$ with what $\alpha$ does to unseen words
- [ ] `7b`: the boosting objective made explicit — AdaBoost's exponential loss and weight update, gradient boosting as stagewise fitting of $-\partial L/\partial F$, XGBoost's regularised objective with its $\gamma$ and $\lambda$ terms — mapped onto the hyperparameters the notebook tunes
- [ ] `8b`: the anomaly score for the Gaussian model $-\log p(x)$ with the multivariate density written out; Mahalanobis distance; the precision/recall trade-off under class imbalance, and why ROC-AUC can flatter a detector on imbalanced data while precision-recall AUC does not
- [ ] Every notebook still executes end to end with stored outputs
- [ ] Each notebook has a Further Reading section
- [ ] If 5b's uplift completes after TASK-SL033, this task records the FEAT-SL2 verdict per that card's handover clause

## Verification

```bash
for nb in 5b_knn_practical 6b_naive_bayes_practical 7b_ensemble_methods_practical 8b_anomaly_detection_practical; do
  .venv/bin/python scripts/verify_notebook.py "notebooks/$nb.ipynb" --type practical --execute || echo "FAILED $nb"
done
```
All four must exit 0. Paste the summary lines into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 140
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- 7b imports xgboost and lightgbm; if TASK-SL026 could not install lightgbm on this host, the notebook will not execute — report that as an environment failure against TASK-SL026 rather than deleting the LightGBM section
- 5b is 263 KB with stored outputs from a previous run; re-executing may change timings quoted in prose — quote them from the fresh run

### Weak assumptions

- TASK-SL022 (stacking) may land in 7b around the same time; check the file's state before editing to avoid clobbering that work
