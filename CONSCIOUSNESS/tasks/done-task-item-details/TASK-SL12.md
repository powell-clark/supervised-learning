# TASK-SL12: Lesson 9a: CNN practical — image classification, transfer learning mathematics, NumPy CNN implementation

## Context

Create the practical notebook for Convolutional Neural Networks. Apply CNNs to image classification, demonstrate transfer learning principles, and show the NumPy CNN from theory in practice. Use PyTorch/TensorFlow as modern comparison.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/9b_cnn_practical.ipynb`
- [x] Image classification dataset: CIFAR-10 or STL-10 (non-trivial dataset) — `fetch_openml('CIFAR_10_small', ...)`
- [x] CNN architecture design: Explain choice of kernel sizes, number of filters, pooling strategies
- [x] Training from scratch: Implement using PyTorch or TensorFlow with learning curves — `CIFAR_CNN`, 156,074 params, 15 epochs on 4000 images
- [x] Transfer learning mathematics: Explain feature reuse, fine-tuning, frozen layers mathematics
- [x] Pre-trained model application: Use ResNet/VGG from PyTorch and fine-tune on dataset — frozen-backbone ResNet-18, 1200 images, 5 epochs
- [x] Feature visualization: Show learned filters and activations to build intuition
- [x] From-scratch NumPy CNN: Demonstrate simpler CNN from 9a theory on subset of data — Conv2D/MaxPool2D reproduced inline, 500/150-image CIFAR-10 subset
- [x] Comparison: NumPy CNN vs PyTorch (correctness, runtime)
- [x] Performance analysis: Training/validation curves, per-class accuracy, confusion matrix
- [x] Visualization: Learned filters, activation maps, misclassified examples
- [x] No emojis, no corporate buzzwords, no "state-of-the-art" language
- [x] References cited: PyTorch documentation, Goodfellow Chapter 9, Stanford CS231n assignments
- [x] Notebook length: 70 hours effort

## Technical Notes

Transfer learning: Early layers learn general features (edges, textures), later layers task-specific. Fine-tuning allows reuse.

Visualize filters: Show what patterns early layers detect (oriented edges, colors).

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] Transfer learning approach is well-motivated and shows clear benefits
- [x] NumPy and PyTorch implementations match in results
- [x] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL11 (requires understanding from theory notebook)
