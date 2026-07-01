# TASK-SL11: Lesson 9a: CNN theory — discrete convolution, backprop through conv layers, pooling gradients, weight sharing

## Context

Create the theory notebook for Convolutional Neural Networks. This requires a complete rewrite from the current PyTorch tutorial stub. Cover discrete convolution mathematics, backpropagation through specialized layers, and the weight sharing principle. Include from-scratch CNN implementation in NumPy.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/9a_cnn_theory.ipynb` (complete rewrite from stub)
- [ ] Discrete convolution mathematical definition with clear notation (>100 LaTeX symbols)
- [ ] Forward pass: Derivation of convolution output size, padding, stride mathematics
- [ ] Backpropagation through convolutional layers: Full chain rule derivation for ∂L/∂w, ∂L/∂x
- [ ] Pooling layer mathematics: Max pooling and average pooling, gradient computation
- [ ] Weight sharing principle: Show how parameters are shared across spatial locations
- [ ] Parameter reduction mathematics: Compare fully-connected vs convolutional layers
- [ ] From-scratch CNN implementation in NumPy with both forward and backward pass
- [ ] Demonstration on standard dataset (MNIST or CIFAR-10)
- [ ] Convergence analysis and training dynamics
- [ ] No emojis, marketing language ("cutting edge", "revolutionary"), or PyTorch tutorials
- [ ] References cited: Stanford CS231n, Goodfellow Chapter 9, LeCun foundational papers
- [ ] Notebook length: 70 hours effort

## Technical Notes

Discrete 2D convolution: y[i,j] = Σ_k Σ_l w[k,l] * x[i+k, j+l]

Backprop: ∂L/∂w[k,l] = Σ_{i,j} δ[i,j] * x[i+k, j+l] where δ is upstream gradient.

Weight sharing reduces parameters from O(spatial_size × filter_size) to O(filter_size) per filter.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch implementation is correct, efficient, and educational
- [ ] Mathematical derivations are step-by-step with no jumps
- [ ] No marketing language, no emojis, no tool tutorials
- [ ] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL10 (lesson sequencing, builds on previous deep learning foundation)
