# Supervised Machine Learning

A university-grade curriculum for supervised machine learning, from linear regression through
convolutional networks, recurrent networks and transformers. Every method is derived from first
principles, implemented from scratch in NumPy, then reproduced with scikit-learn, XGBoost or PyTorch.
All notebooks run in Google Colab with no local setup.

## The series

Four repositories, one curriculum. The first three are *how* a model learns; the fourth is *what*
it is built from, and cuts across all three.

- **[Supervised learning](https://github.com/powell-clark/supervised-learning)** — learning from labelled examples (you are here)
- [Unsupervised learning](https://github.com/powell-clark/unsupervised-learning) — finding structure with no labels
- [Reinforcement learning](https://github.com/powell-clark/reinforcement-learning) — learning from reward
- [Deep learning & transformers](https://github.com/powell-clark/deep-learning) — the architecture the other three can each be built on

**Status:** 10 of 10 lessons complete (25 notebooks)

## Overview

- **From First Principles**: every algorithm derived from foundations, not quoted
- **Dual Structure**: theory (a) + practical (b) notebooks for each lesson
- **Story-Driven**: a real-world motivation before the mathematics
- **Complete Implementations**: from-scratch NumPy, then production libraries
- **Google Colab Compatible**: runs in the browser, no local setup
- **Machine-Verified**: `scripts/verify_notebook.py` measures every notebook against the curriculum's
  quality bar and executes it top to bottom; the latest scoreboard is in
  [reports/verify/summary.md](reports/verify/summary.md)

## Lesson catalog

#### Foundations

- **Lesson 0**: Linear Regression
  - [`0a_linear_regression_theory.ipynb`](notebooks/0a_linear_regression_theory.ipynb) — the model and its loss, the normal equation, gradient descent, feature scaling and the bias-variance decomposition, implemented from scratch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/0a_linear_regression_theory.ipynb)
  - [`0b_linear_regression_practical.ipynb`](notebooks/0b_linear_regression_practical.ipynb) — fitting, coefficient paths and residual diagnostics, cross-checked against the from-scratch model [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/0b_linear_regression_practical.ipynb)
- **Lesson 1**: Logistic Regression
  - [`1a_logistic_regression_theory.ipynb`](notebooks/1a_logistic_regression_theory.ipynb) — the sigmoid, cross-entropy and gradient descent, built from scratch on the Wisconsin breast cancer dataset [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/1a_logistic_regression_theory.ipynb)
  - [`1b_logistic_regression_practical.ipynb`](notebooks/1b_logistic_regression_practical.ipynb) — the same classifier in PyTorch, with a full data pipeline and evaluation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/1b_logistic_regression_practical.ipynb)
- **Lesson 2**: Decision Trees
  - [`2a_decision_trees_theory.ipynb`](notebooks/2a_decision_trees_theory.ipynb) — splitting criteria, interpretability, and tree depth against the bias-variance trade-off, with a from-scratch tree [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/2a_decision_trees_theory.ipynb)
  - [`2b_decision_trees_practical.ipynb`](notebooks/2b_decision_trees_practical.ipynb) — predicting London house prices with scikit-learn, random forests and XGBoost, from data cleaning to feature encoding [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/2b_decision_trees_practical.ipynb)
  - [`2c_decision_trees_ATLAS_model_comparison.ipynb`](notebooks/2c_decision_trees_ATLAS_model_comparison.ipynb) — ATLAS, an automated tree-learning analysis system for comparing configurations and features [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/2c_decision_trees_ATLAS_model_comparison.ipynb)
- **Lesson 3**: Neural Networks
  - [`3a_neural_networks_theory.ipynb`](notebooks/3a_neural_networks_theory.ipynb) — forward pass, activations, losses, backpropagation and initialisation, with gradient checking [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/3a_neural_networks_theory.ipynb)
  - [`3b_neural_networks_practical.ipynb`](notebooks/3b_neural_networks_practical.ipynb) — PyTorch networks, training techniques, architecture search and evaluation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/3b_neural_networks_practical.ipynb)

#### Classical Methods

- **Lesson 4**: Support Vector Machines
  - [`4a_svm_theory.ipynb`](notebooks/4a_svm_theory.ipynb) — the maximum-margin principle, Lagrangian duality, the kernel trick and soft margins, derived and implemented [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/4a_svm_theory.ipynb)
  - [`4b_support_vector_machines_practical.ipynb`](notebooks/4b_support_vector_machines_practical.ipynb) — kernels, tuning C and γ, decision boundaries, and from-scratch against scikit-learn [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/4b_support_vector_machines_practical.ipynb)
- **Lesson 5**: K-Nearest Neighbours
  - [`5a_k_nearest_neighbors_theory.ipynb`](notebooks/5a_k_nearest_neighbors_theory.ipynb) — distance metrics, the curse of dimensionality and KD-trees, with a from-scratch classifier [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/5a_k_nearest_neighbors_theory.ipynb)
  - [`5b_knn_practical.ipynb`](notebooks/5b_knn_practical.ipynb) — choosing K by cross-validation, weighted K-NN, and brute force against KD-trees [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/5b_knn_practical.ipynb)
- **Lesson 6**: Naive Bayes
  - [`6a_naive_bayes_theory.ipynb`](notebooks/6a_naive_bayes_theory.ipynb) — Bayes' theorem, the conditional independence assumption, and the Gaussian, multinomial and Bernoulli variants [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/6a_naive_bayes_theory.ipynb)
  - [`6b_naive_bayes_practical.ipynb`](notebooks/6b_naive_bayes_practical.ipynb) — text classification on 20 Newsgroups with TF-IDF and a from-scratch multinomial model [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/6b_naive_bayes_practical.ipynb)
- **Lesson 7**: Ensemble Methods
  - [`7a_ensemble_methods_theory.ipynb`](notebooks/7a_ensemble_methods_theory.ipynb) — bagging, random forests, AdaBoost and gradient boosting, derived from the bias-variance decomposition [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/7a_ensemble_methods_theory.ipynb)
  - [`7b_ensemble_methods_practical.ipynb`](notebooks/7b_ensemble_methods_practical.ipynb) — XGBoost and LightGBM, early stopping, tuning, and stacking [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/7b_ensemble_methods_practical.ipynb)
- **Lesson 8**: Anomaly Detection
  - [`8a_anomaly_detection_theory.ipynb`](notebooks/8a_anomaly_detection_theory.ipynb) — Gaussian models, Mahalanobis distance, Isolation Forest, one-class SVM and LOF [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/8a_anomaly_detection_theory.ipynb)
  - [`8b_anomaly_detection_practical.ipynb`](notebooks/8b_anomaly_detection_practical.ipynb) — credit-card fraud detection, precision-recall curves and threshold selection on imbalanced data [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/8b_anomaly_detection_practical.ipynb)

#### Deep Architectures

- **Lesson 9**: Convolutional, Recurrent and Transformer Networks
  - [`9a_cnn_theory.ipynb`](notebooks/9a_cnn_theory.ipynb) — discrete convolution, weight sharing, backpropagation through conv and pooling, and a from-scratch CNN on MNIST [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/9a_cnn_theory.ipynb)
  - [`9b_cnn_practical.ipynb`](notebooks/9b_cnn_practical.ipynb) — CIFAR-10 in PyTorch, transfer learning with a pretrained ResNet-18, and filter visualisation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/9b_cnn_practical.ipynb)
  - [`9c_rnn_theory.ipynb`](notebooks/9c_rnn_theory.ipynb) — the recurrent neuron, backpropagation through time, vanishing gradients, LSTM and GRU [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/9c_rnn_theory.ipynb)
  - [`9d_rnn_practical.ipynb`](notebooks/9d_rnn_practical.ipynb) — time-series forecasting with RNNs and LSTMs in PyTorch, against a from-scratch NumPy LSTM [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/9d_rnn_practical.ipynb)
  - [`9e_transformer_theory.ipynb`](notebooks/9e_transformer_theory.ipynb) — scaled dot-product and multi-head attention, positional encoding, and the encoder and decoder, with gradient checking [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/9e_transformer_theory.ipynb)
  - [`9f_transformer_practical.ipynb`](notebooks/9f_transformer_practical.ipynb) — a PyTorch encoder-decoder, greedy and beam-search decoding, and fine-tuning DistilBERT [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/powell-clark/supervised-learning/blob/main/notebooks/9f_transformer_practical.ipynb)

## Datasets

- [Wisconsin Breast Cancer (1995)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) — binary classification, 569 samples × 30 features
- [London Housing Prices (2020)](https://www.kaggle.com/datasets/arnavkulkarni/housing-prices-in-london) — regression, 3,479 samples × 9 features; a copy is in `datasets/`
- Standard library datasets loaded in the notebooks: Iris, 20 Newsgroups, MNIST, CIFAR-10 and others

## Local use

```bash
git clone https://github.com/powell-clark/supervised-learning.git
cd supervised-learning
scripts/setup_env.sh                                   # build .venv from requirements.txt
.venv/bin/python scripts/verify_notebook.py notebooks/0a_linear_regression_theory.ipynb --execute
```

## How this repository is built

The curriculum was developed with Claude Code: later lessons were drafted by autonomous sessions
against a written syllabus, executed top to bottom and reviewed before they were accepted. The
agents' working state is kept out of this repository.

## Contributing

Spotted a typo, an unclear explanation or a bug? Open an issue or a pull request.

## Licence

Copyright © 2025 Powell-Clark Limited. Licensed under the Apache License, Version 2.0; see
[LICENSE.md](LICENSE.md).
