# TASK-SL10: Lesson 8b: Anomaly Detection practical — fraud detection case study, ROC curve analysis for imbalanced data

## Context

Create the practical notebook for Anomaly Detection. Apply anomaly detection methods to a fraud detection case study, demonstrating ROC curve analysis, threshold selection, and handling imbalanced datasets.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/8b_anomaly_detection_practical.ipynb`
- [ ] Dataset: Fraud detection dataset (e.g., credit card transactions) with strong class imbalance
- [ ] Gaussian anomaly detection: Apply from 8a theory to fraud data
- [ ] Isolation Forest: Scikit-learn implementation and hyperparameter tuning
- [ ] One-Class SVM: Application to same dataset
- [ ] ROC curve analysis: Critical for imbalanced data (use PR curve, not standard ROC)
- [ ] Precision-Recall curves: Show why better than ROC for imbalanced problems
- [ ] Threshold selection: Discuss trade-offs (False Positive Rate vs False Negative Rate for fraud)
- [ ] Performance comparison: Gaussian vs Isolation Forest vs One-Class SVM
- [ ] Comparison to supervised approach: Show anomaly detection advantages when labels unavailable
- [ ] Visualization: ROC/PR curves, confusion matrix, threshold vs metrics
- [ ] No emojis, no corporate buzzwords, no tool tutorials
- [ ] References cited: Scikit-learn documentation, Davis & Goadrich PR curves paper
- [ ] Notebook length: 50 hours effort

## Technical Notes

Imbalanced data: Accuracy is misleading. Use precision, recall, F1-score, PR-AUC.

Fraud detection: Cost asymmetry—missing a fraud (False Negative) is more expensive than false alarm (False Positive).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Imbalanced data handling is thorough and practical
- [ ] Threshold selection trade-offs are clearly explained
- [ ] Ready for peer review and publication

## Story Points

10 (50 hours estimated effort)

## Blocked By

TASK-SL9 (requires understanding from theory notebook)
