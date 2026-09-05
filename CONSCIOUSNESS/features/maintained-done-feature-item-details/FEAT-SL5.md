---
id: FEAT-SL5
status: maintained
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
code_paths:
  - notebooks/8a_anomaly_detection_theory.ipynb
  - notebooks/8b_anomaly_detection_practical.ipynb
---

# FEAT-SL5: Lesson 8 — Anomaly Detection

## Context
Anomaly detection (outlier detection) is crucial for fraud detection, system monitoring,
and data quality control. This lesson covers both statistical methods (Gaussian-based)
and isolation-based approaches (random forests, kernel methods). Special attention is
paid to handling imbalanced datasets where anomalies are rare.

## Acceptance Criteria
- [x] **AC-1** — Theory notebook complete with Gaussian anomaly detection and probability threshold selection
- [x] **AC-2** — Mahalanobis distance derivation for multivariate Gaussian modeling
- [x] **AC-3** — Isolation Forest algorithm explained with tree construction strategy
- [x] **AC-4** — One-Class SVM formulation and kernel methods for anomaly detection
- [x] **AC-5** — Imbalanced data problem explained with precision-recall tradeoffs
- [x] **AC-6** — Practical notebook with fraud detection case study (e.g., credit card data)
- [x] **AC-7** — Threshold selection via ROC curve and precision-recall analysis
- [x] **AC-8** — Performance metrics: TPR, FPR, ROC-AUC, PR-AUC for imbalanced data
- [x] **AC-9** — Both notebooks run top-to-bottom in Google Colab with no local setup
- [x] **AC-10** — NumPy implementations and Scikit-learn comparison for reproducibility

## Notes
TASK-SL9 (theory, verified 2026-07-13): notebooks/8a_anomaly_detection_theory.ipynb
covers Gaussian anomaly detection with threshold selection, the Mahalanobis
distance derivation (with a worked example showing it catches correlation
violations a per-feature check misses), Isolation Forest's path-length
mechanism, One-Class SVM's boundary-fitting formulation, a from-scratch
multivariate Gaussian detector matching scikit-learn's EmpiricalCovariance,
and a four-way comparison against IsolationForest/OneClassSVM.

TASK-SL10 (practical, verified 2026-07-13): notebooks/8b_anomaly_detection_practical.ipynb
applies all three methods to the real credit card fraud dataset (284,807
transactions, 0.172% fraud), demonstrates the ROC-AUC vs PR-AUC gap directly
(every method's ROC-AUC is 0.46-0.70 higher than its PR-AUC), performs
cost-weighted threshold selection (fraud misses assumed 100x costlier than
false alarms), and compares against a supervised RandomForest baseline —
including the finding that ROC-AUC barely distinguishes supervised from
unsupervised (0.947 vs 0.950) while PR-AUC shows an enormous gap (0.82 vs
0.49), reinforcing the lesson's central point empirically rather than just
asserting it.

Both tasks complete; all acceptance criteria met. First-pass independent review
(REVIEW-CCC034) found a genuine StandardScaler leakage bug and an Isolation
Forest labeled-data inconsistency in 8b; both fixed and confirmed by a second
independent review (REVIEW-CCC035, blind, separate agent). Feature moves to
maintained per the agent-tier gate (performance kano).
