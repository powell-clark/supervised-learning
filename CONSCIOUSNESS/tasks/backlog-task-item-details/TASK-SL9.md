# TASK-SL9: Lesson 8a: Anomaly Detection theory — Gaussian modeling, Mahalanobis distance, Isolation Forest, One-Class SVM

## Context

Create the theory notebook for Anomaly Detection. Cover statistical approaches (Gaussian models, Mahalanobis distance), isolation-based methods, and one-class SVM. Include from-scratch Gaussian anomaly detection implementation.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/8a_anomaly_detection_theory.ipynb`
- [ ] Gaussian distribution modeling: Assume normal distribution for normal data (>100 LaTeX symbols)
- [ ] Mahalanobis distance: Derivation and intuition for accounting for covariance
- [ ] Anomaly threshold selection: Statistical approach (fit Gaussian, flag low-probability points)
- [ ] Isolation Forest mathematics: Why isolation forests work without explicit distance metrics
- [ ] One-Class SVM: Theory of support vector approach to outlier detection
- [ ] From-scratch Gaussian anomaly detection with covariance matrix estimation (NumPy)
- [ ] Parameter estimation: Mean and covariance matrix from training data
- [ ] Comparison to scikit-learn approaches
- [ ] Theoretical analysis: Assumptions and limitations of each approach
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: Chandola et al. "Anomaly Detection: A Survey", Schölkopf One-Class SVM paper
- [ ] Notebook length: 50 hours effort

## Technical Notes

Gaussian anomaly: Flag point x as anomalous if p(x) < ε, where ε is chosen threshold.

Mahalanobis distance: d(x) = sqrt((x-μ)^T Σ^{-1} (x-μ)). Accounts for feature correlations.

Isolation Forest: Random trees partition space; anomalies isolated faster (shorter paths).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch Gaussian implementation is correct
- [ ] Mathematical foundations are rigorous
- [ ] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL8 (lesson sequencing)
