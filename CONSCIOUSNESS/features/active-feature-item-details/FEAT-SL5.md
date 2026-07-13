---
id: FEAT-SL5
status: backlog
priority: p2
kano: performance
title: Lesson 8 — Anomaly Detection theory and practice
description: Complete anomaly detection lesson with mathematical theory (Gaussian modeling, Mahalanobis distance, Isolation Forest, One-Class SVM) and practical implementation (fraud detection case study, ROC curve analysis for imbalanced data)
acceptance_criteria:
  - Theory notebook complete with Gaussian distribution-based anomaly detection, Mahalanobis distance derivation, Isolation Forest algorithm, and One-Class SVM formulation
  - Practical notebook complete with fraud detection case study and ROC/AUC analysis for imbalanced data
  - Both notebooks runnable end-to-end in Google Colab with dependencies installed in first cell
  - Includes NumPy implementation of anomaly detection algorithms plus Scikit-learn comparison
  - Markdown cells document learning objectives, key formulas, and interpretation of results
stories: [STORY-SL8]
tasks: [TASK-SL9,TASK-SL10]
---

# FEAT-SL5: Lesson 8 — Anomaly Detection

## Context
Anomaly detection (outlier detection) is crucial for fraud detection, system monitoring,
and data quality control. This lesson covers both statistical methods (Gaussian-based)
and isolation-based approaches (random forests, kernel methods). Special attention is
paid to handling imbalanced datasets where anomalies are rare.

## Acceptance Criteria
- [x] Theory notebook complete with Gaussian anomaly detection and probability threshold selection
- [x] Mahalanobis distance derivation for multivariate Gaussian modeling
- [x] Isolation Forest algorithm explained with tree construction strategy
- [x] One-Class SVM formulation and kernel methods for anomaly detection
- [ ] Imbalanced data problem explained with precision-recall tradeoffs
- [ ] Practical notebook with fraud detection case study (e.g., credit card data)
- [ ] Threshold selection via ROC curve and precision-recall analysis
- [ ] Performance metrics: TPR, FPR, ROC-AUC, PR-AUC for imbalanced data
- [ ] Both notebooks run top-to-bottom in Google Colab with no local setup
- [x] NumPy implementations and Scikit-learn comparison for reproducibility

## Notes
TASK-SL9 (theory, verified 2026-07-13): notebooks/8a_anomaly_detection_theory.ipynb
covers Gaussian anomaly detection with threshold selection, the Mahalanobis
distance derivation (with a worked example showing it catches correlation
violations a per-feature check misses), Isolation Forest's path-length
mechanism, One-Class SVM's boundary-fitting formulation, a from-scratch
multivariate Gaussian detector matching scikit-learn's EmpiricalCovariance,
and a four-way comparison against IsolationForest/OneClassSVM.

"Imbalanced data problem explained with precision-recall tradeoffs" is left
for TASK-SL10 (practical) — this is squarely a real-fraud-data topic (extreme
class imbalance, ROC/PR-AUC on a genuinely skewed dataset), not something a
synthetic theory-notebook example can demonstrate honestly. TASK-SL10 remains
in the backlog; feature stays in_progress until it lands.
