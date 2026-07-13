# TASK-SL11: Lesson 9a: CNN theory — discrete convolution, backprop through conv layers, pooling gradients, weight sharing

## Context

Create the theory notebook for Convolutional Neural Networks. This requires a complete rewrite from the current PyTorch tutorial stub. Cover discrete convolution mathematics, backpropagation through specialized layers, and the weight sharing principle. Include from-scratch CNN implementation in NumPy.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/9a_cnn_theory.ipynb` (complete rewrite from stub) — no stub was found in the repo; built new
- [x] Discrete convolution mathematical definition with clear notation (>100 LaTeX symbols) — 182 dollar-delimited spans
- [x] Forward pass: Derivation of convolution output size, padding, stride mathematics — formula verified against a direct convolution implementation across 4 padding/stride combinations
- [x] Backpropagation through convolutional layers: Full chain rule derivation for ∂L/∂w, ∂L/∂x — implementation verified by numerical gradient checking to 2.3e-10
- [x] Pooling layer mathematics: Max pooling and average pooling, gradient computation — both derived; max pooling also implemented and gradient-checked to 4.3e-11
- [x] Weight sharing principle: Show how parameters are shared across spatial locations
- [x] Parameter reduction mathematics: Compare fully-connected vs convolutional layers — concrete parameter counts computed (up to ~78x reduction) plus a receptive-field growth derivation
- [x] From-scratch CNN implementation in NumPy with both forward and backward pass
- [x] Demonstration on standard dataset (MNIST or CIFAR-10) — real MNIST (2000 train / 500 test subset via fetch_openml, for pure-NumPy training-time tractability)
- [x] Convergence analysis and training dynamics — 8-epoch training curve, monotonic loss decrease, final test accuracy 89.2% (vs 88.8% for an sklearn MLP baseline on the same split)
- [x] No emojis, marketing language ("cutting edge", "revolutionary"), or PyTorch tutorials
- [x] References cited: Stanford CS231n, Goodfellow Chapter 9, LeCun foundational papers
- [x] Notebook length: 70 hours effort — 45.1KB rendered, 31 cells

## Technical Notes

Discrete 2D convolution: y[i,j] = Σ_k Σ_l w[k,l] * x[i+k, j+l]

Backprop: ∂L/∂w[k,l] = Σ_{i,j} δ[i,j] * x[i+k, j+l] where δ is upstream gradient.

Weight sharing reduces parameters from O(spatial_size × filter_size) to O(filter_size) per filter.

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] From-scratch implementation is correct, efficient, and educational — gradient-checked to floating-point precision
- [x] Mathematical derivations are step-by-step with no jumps
- [x] No marketing language, no emojis, no tool tutorials
- [x] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL10 (lesson sequencing, builds on previous deep learning foundation)
