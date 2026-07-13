# TASK-SL10: Lesson 8b: Anomaly Detection practical — fraud detection case study, ROC curve analysis for imbalanced data

## Context

Create the practical notebook for Anomaly Detection. Apply anomaly detection methods to a fraud detection case study, demonstrating ROC curve analysis, threshold selection, and handling imbalanced datasets.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/8b_anomaly_detection_practical.ipynb`
- [x] Dataset: Fraud detection dataset (e.g., credit card transactions) with strong class imbalance — real credit card fraud dataset (284,807 transactions, 0.172% fraud)
- [x] Gaussian anomaly detection: Apply from 8a theory to fraud data
- [x] Isolation Forest: Scikit-learn implementation and hyperparameter tuning
- [x] One-Class SVM: Application to same dataset — fit on a stated subsample (5,000 normal transactions) for tractability, explicitly disclosed
- [x] ROC curve analysis: Critical for imbalanced data (use PR curve, not standard ROC) — ROC-AUC vs PR-AUC gap measured directly for every method (0.46-0.70 gap)
- [x] Precision-Recall curves: Show why better than ROC for imbalanced problems
- [x] Threshold selection: Discuss trade-offs (False Positive Rate vs False Negative Rate for fraud) — cost-weighted threshold optimization (FN 100x costlier than FP)
- [x] Performance comparison: Gaussian vs Isolation Forest vs One-Class SVM
- [x] Comparison to supervised approach: Show anomaly detection advantages when labels unavailable — RandomForest (PR-AUC 0.82) vs unsupervised methods (PR-AUC 0.24-0.49), with discussion of when unsupervised still applies
- [x] Visualization: ROC/PR curves, confusion matrix, threshold vs metrics
- [x] No emojis, no corporate buzzwords, no tool tutorials
- [x] References cited: Scikit-learn documentation, Davis & Goadrich PR curves paper
- [x] Notebook length: 50 hours effort — 27.4KB rendered, 27 cells

## Technical Notes

Imbalanced data: Accuracy is misleading. Use precision, recall, F1-score, PR-AUC.

Fraud detection: Cost asymmetry—missing a fraud (False Negative) is more expensive than false alarm (False Positive).

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] Imbalanced data handling is thorough and practical
- [x] Threshold selection trade-offs are clearly explained
- [x] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL9 (requires understanding from theory notebook)
