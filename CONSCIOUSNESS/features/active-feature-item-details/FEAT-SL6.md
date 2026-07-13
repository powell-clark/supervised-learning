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
- [ ] Unrolled RNN computation graph and backpropagation through time (BPTT)
- [ ] Vanishing gradient problem with empirical demonstration
- [ ] Long Short-Term Memory (LSTM) gate derivations and intuition
- [ ] Gated Recurrent Unit (GRU) as LSTM simplification
- [ ] Exploding gradient problem and gradient clipping solution
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
- [ ] Time series forecasting (e.g., stock prices, temperature)
- [ ] Text sequence modeling (character or word level)
- [ ] LSTM vs GRU performance comparison
- [ ] Sequence length impact on training and prediction
- [ ] NumPy LSTM implementation
- [ ] PyTorch sequence model comparison

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
without errors (1m52s). Remaining four tasks (SL13-SL16, RNN and Transformer
theory/practical) pending; feature stays in_progress.
