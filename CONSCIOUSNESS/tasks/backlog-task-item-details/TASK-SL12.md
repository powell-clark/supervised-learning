# TASK-SL12: Lesson 9a: CNN practical — image classification, transfer learning mathematics, NumPy CNN implementation

## Context

Create the practical notebook for Convolutional Neural Networks. Apply CNNs to image classification, demonstrate transfer learning principles, and show the NumPy CNN from theory in practice. Use PyTorch/TensorFlow as modern comparison.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/9b_cnn_practical.ipynb`
- [ ] Image classification dataset: CIFAR-10 or STL-10 (non-trivial dataset)
- [ ] CNN architecture design: Explain choice of kernel sizes, number of filters, pooling strategies
- [ ] Training from scratch: Implement using PyTorch or TensorFlow with learning curves
- [ ] Transfer learning mathematics: Explain feature reuse, fine-tuning, frozen layers mathematics
- [ ] Pre-trained model application: Use ResNet/VGG from PyTorch and fine-tune on dataset
- [ ] Feature visualization: Show learned filters and activations to build intuition
- [ ] From-scratch NumPy CNN: Demonstrate simpler CNN from 9a theory on subset of data
- [ ] Comparison: NumPy CNN vs PyTorch (correctness, runtime)
- [ ] Performance analysis: Training/validation curves, per-class accuracy, confusion matrix
- [ ] Visualization: Learned filters, activation maps, misclassified examples
- [ ] No emojis, no corporate buzzwords, no "state-of-the-art" language
- [ ] References cited: PyTorch documentation, Goodfellow Chapter 9, Stanford CS231n assignments
- [ ] Notebook length: 70 hours effort

## Technical Notes

Transfer learning: Early layers learn general features (edges, textures), later layers task-specific. Fine-tuning allows reuse.

Visualize filters: Show what patterns early layers detect (oriented edges, colors).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] Transfer learning approach is well-motivated and shows clear benefits
- [ ] NumPy and PyTorch implementations match in results
- [ ] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL11 (requires understanding from theory notebook)
