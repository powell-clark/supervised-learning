---
id: FEAT-SL6
status: backlog
priority: p2
kano: performance
title: Lesson 9 — Deep Learning theory and practice
description: Complete deep learning lesson covering CNNs, RNNs, and Transformers with mathematical theory (backpropagation through architectures, attention mechanisms, positional encoding) and practical implementations (image classification, sequence modeling, NumPy implementations)
acceptance_criteria:
  - CNN theory notebook complete with discrete convolution derivation, backprop through conv/pooling layers, and weight sharing explanation
  - RNN theory notebook complete with BPTT derivation, vanishing/exploding gradient analysis, LSTM/GRU gate mathematics
  - Transformer theory notebook complete with scaled dot-product attention, multi-head attention, and positional encoding mathematics
  - Practical notebooks complete with image classification, sequence modeling, and time series forecasting case studies
  - All notebooks runnable end-to-end in Google Colab with dependencies installed in first cell
  - Includes NumPy implementations of attention mechanisms and core layers plus PyTorch comparison
  - Markdown cells document learning objectives, key formulas, and interpretation of results
stories: [STORY-SL9]
tasks: [TASK-SL11,TASK-SL12,TASK-SL13,TASK-SL14,TASK-SL15,TASK-SL16]
code_paths:
  - notebooks/9a_cnn_theory.ipynb
  - notebooks/9b_cnn_practical.ipynb
  - notebooks/9c_rnn_theory.ipynb
  - notebooks/9d_rnn_practical.ipynb
  - notebooks/9e_transformer_theory.ipynb
  - notebooks/9f_transformer_practical.ipynb
---

# FEAT-SL6: Lesson 9 — Deep Learning

## Context
Deep learning has transformed machine learning, achieving state-of-the-art results
across computer vision, natural language processing, and speech recognition. This
lesson covers the three major architectures (CNNs, RNNs, Transformers) from both
mathematical and implementation perspectives.

## Theory Acceptance Criteria

### Convolutional Neural Networks (TASK-SL11)
- [x] Discrete convolution derivation with mathematical notation and examples
- [x] Backpropagation through convolutional layers (gradient flow) — gradient-checked to 2.3e-10
- [x] Pooling layer gradients (max pooling, average pooling)
- [x] Weight sharing intuition and sparse connectivity
- [x] Receptive field and feature map size calculations
- [x] Modern architectures (ResNets, skip connections) motivation — derived why the additive identity term keeps the gradient from vanishing

### Recurrent Neural Networks (TASK-SL13)
- [x] Unrolled RNN computation graph and backpropagation through time (BPTT) — chain-rule BPTT derived and cross-checked against finite-difference on a 3-step example
- [x] Vanishing gradient problem with empirical demonstration — measured gradient shrinking ~1e36x over 120 steps on an untrained network
- [x] Long Short-Term Memory (LSTM) gate derivations and intuition — full input/forget/output gate equations derived, "constant error carousel" explained
- [x] Gated Recurrent Unit (GRU) as LSTM simplification — full equations derived; parameter-count check confirms GRU uses exactly 75.0% of LSTM's parameters at matching D,H
- [x] Exploding gradient problem and gradient clipping solution — spectral-radius>1 case measured, clip-by-norm implemented and demonstrated
- [ ] Bidirectional RNNs explained

### Transformers (TASK-SL15)
- [ ] Scaled dot-product attention derivation (query, key, value)
- [ ] Multi-head attention mechanism and parallel computation
- [ ] Positional encoding (sinusoidal, learned) for sequence ordering
- [ ] Self-attention vs cross-attention explained
- [ ] Encoder-decoder architecture for sequence-to-sequence tasks
- [ ] Layer normalization and residual connections motivation

## Practice Acceptance Criteria

### CNN Practical (TASK-SL12)
- [x] Image classification on CIFAR-10 or similar dataset
- [x] Transfer learning using pre-trained models (ResNet, VGG)
- [x] Feature visualization techniques (filters, activation maps)
- [x] Model architecture comparison (SimpleNet, AlexNet concepts)
- [x] NumPy CNN implementation of core layers
- [x] PyTorch comparison for reproducibility

### RNN Practical (TASK-SL14)
- [x] Time series forecasting (e.g., stock prices, temperature) — Box & Jenkins airline passengers (1949-1960), one-month-ahead and 6-month-ahead encoder-decoder forecasts
- [ ] Text sequence modeling (character or word level)
- [ ] LSTM vs GRU performance comparison
- [x] Sequence length impact on training and prediction — window length (6/12/24), hidden size (8/32) and learning rate (0.005/0.02) all swept with trained results
- [x] NumPy LSTM implementation — reused 9c's gradient-checked `LSTMCell`, trained with its own BPTT (test MAE=68.35, RMSE=78.85)
- [x] PyTorch sequence model comparison — weight-copied NumPy/PyTorch equivalence check, max abs difference 2.8e-17 on identical input

### Transformer Practical (TASK-SL16)
- [ ] Sequence-to-sequence task (e.g., machine translation, summarization)
- [ ] Pre-trained model usage and fine-tuning mathematics
- [ ] Attention visualization and interpretability
- [ ] Position encoding impact analysis
- [ ] NumPy attention mechanism implementation
- [ ] PyTorch Transformer comparison

## General Acceptance Criteria
- [ ] All notebooks run top-to-bottom in Google Colab with no local setup
- [ ] Markdown cells explain learning objectives, key formulas, and result interpretation
- [ ] Visualizations of learned features, activations, and attention weights
- [ ] Performance metrics and training curves documented
- [ ] Hyperparameter sensitivity analysis included

## Notes
Six tasks: TASK-SL11-SL16 (three theory, three practical). This feature card documents
the comprehensive acceptance bar all tasks must collectively meet.

TASK-SL11 (CNN theory, verified 2026-07-13): notebooks/9a_cnn_theory.ipynb covers
discrete convolution, weight sharing/parameter reduction, receptive field growth,
backprop through conv and pooling layers (gradient-checked to floating-point
precision), a from-scratch CNN trained on real MNIST (89.2% test accuracy vs
88.8% for an sklearn MLP baseline on the same split), and ResNet/skip-connection
motivation.

TASK-SL12 (CNN practical, verified 2026-07-13): notebooks/9b_cnn_practical.ipynb
(30 cells) trains a CIFAR_CNN PyTorch model (156,074 params, 15 epochs on 4000
CIFAR-10 images fetched via fetch_openml('CIFAR_10_small', ...)), fine-tunes a
frozen-backbone ResNet-18 (1200 images, 5 epochs), visualizes learned filters and
activations, and reproduces 9a's Conv2D/MaxPool2D inline for a NumPy-vs-PyTorch
correctness comparison on a 500/150-image CIFAR-10 subset. Executed end-to-end
without errors (1m52s). Remaining two tasks (SL15-SL16, Transformer
theory/practical) pending; feature stays in_progress.

TASK-SL13/TASK-SL14 (RNN theory and practical, verified and ticked
2026-09-05, TASK-SL029): three criteria — Bidirectional RNNs explained, Text
sequence modeling (character or word level), and LSTM vs GRU performance
comparison — are left unticked because notebooks/9c_rnn_theory.ipynb and
notebooks/9d_rnn_practical.ipynb as shipped do not cover them (9c covers
vanilla RNN/LSTM/GRU derivations and gradient behaviour but not
bidirectionality; 9d compares RNN vs LSTM on numeric time series only, no
text and no LSTM-vs-GRU run). TASK-SL036 (Uplift practicals 9b and 9d to
the practical bar) already carries all three as its own acceptance
criteria, so nothing here is silently dropped — see that card.

TASK-SL15/TASK-SL16 (Transformer theory and practical) remain pending;
`code_paths` above forward-references their intended filenames
(9e_transformer_theory.ipynb, 9f_transformer_practical.ipynb), which do
not exist yet.
