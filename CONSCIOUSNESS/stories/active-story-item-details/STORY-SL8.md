# STORY-SL8: Anomaly Detection theory and practice

## User Story

I want thorough understanding of anomaly detection so that I can build unsupervised learning models for fraud detection, outlier identification, and understand the mathematical foundations of anomaly detection methods.

## Context

Anomaly detection is critical for real-world applications like fraud detection and system monitoring. This story covers statistical approaches (Gaussian models, Mahalanobis distance), isolation-based methods, and one-class SVM from first principles.

## Acceptance Criteria

- [x] Theory notebook (8a) covers Gaussian distribution modeling, Mahalanobis distance, Isolation Forest mathematics, and One-Class SVM theory with >100 LaTeX symbols — 136 dollar-delimited spans
- [x] Theory notebook includes from-scratch Gaussian anomaly detection with MLE parameter estimation (NumPy only)
- [x] Theory notebook demonstrates convergence analysis and theoretical properties on standard datasets — assumptions/limitations section plus the Mahalanobis-vs-Euclidean worked example
- [x] Practical notebook (8b) applies anomaly detection to fraud detection case study
- [x] Practical notebook demonstrates ROC curve analysis and threshold selection for imbalanced data
- [ ] Practical notebook compares multiple anomaly detection methods (statistical, isolation, neural network-based) — statistical/isolation/boundary methods compared; neural-network-based (e.g. autoencoder) anomaly detection not covered, arguably belongs to the unsupervised-learning/deep-learning curriculum rather than this repo's Lesson 8
- [x] Both notebooks follow CURRICULUM_ROADMAP quality standards: >20 math symbols, 50 hours effort
- [x] No emojis, no hype language, no corporate buzzwords
- [x] References Chandola et al. "Anomaly Detection: A Survey" and foundational papers

## Definition of Done

- [x] Both notebooks are mathematically complete and implementation-ready
- [x] From-scratch implementation demonstrates clear understanding of Gaussian approach
- [x] Practical examples show real-world challenges with imbalanced data
- [x] Notebooks ready for publication

## Story Points

20 (10 per task: 8a theory, 8b practical)
