# TASK-SL9: Lesson 8a: Anomaly Detection theory — Gaussian modeling, Mahalanobis distance, Isolation Forest, One-Class SVM

## Context

Create the theory notebook for Anomaly Detection. Cover statistical approaches (Gaussian models, Mahalanobis distance), isolation-based methods, and one-class SVM. Include from-scratch Gaussian anomaly detection implementation.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/8a_anomaly_detection_theory.ipynb`
- [x] Gaussian distribution modeling: Assume normal distribution for normal data (>100 LaTeX symbols) — 136 dollar-delimited spans
- [x] Mahalanobis distance: Derivation and intuition for accounting for covariance — includes a worked example where a point is individually normal per-feature but jointly anomalous (Euclidean 2.82 vs Mahalanobis 7.55)
- [x] Anomaly threshold selection: Statistical approach (fit Gaussian, flag low-probability points)
- [x] Isolation Forest mathematics: Why isolation forests work without explicit distance metrics — path-length/anomaly-score formula derived and verified numerically
- [x] One-Class SVM: Theory of support vector approach to outlier detection
- [x] From-scratch Gaussian anomaly detection with covariance matrix estimation (NumPy)
- [x] Parameter estimation: Mean and covariance matrix from training data
- [x] Comparison to scikit-learn approaches — from-scratch Gaussian, sklearn EmpiricalCovariance/Mahalanobis, IsolationForest, and OneClassSVM compared side by side
- [x] Theoretical analysis: Assumptions and limitations of each approach
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: Chandola et al. "Anomaly Detection: A Survey", Schölkopf One-Class SVM paper
- [x] Notebook length: 50 hours effort — 37.4KB rendered, 27 cells

## Technical Notes

Gaussian anomaly: Flag point x as anomalous if p(x) < ε, where ε is chosen threshold.

Mahalanobis distance: d(x) = sqrt((x-μ)^T Σ^{-1} (x-μ)). Accounts for feature correlations.

Isolation Forest: Random trees partition space; anomalies isolated faster (shorter paths).

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] From-scratch Gaussian implementation is correct
- [x] Mathematical foundations are rigorous
- [x] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL8 (lesson sequencing)
