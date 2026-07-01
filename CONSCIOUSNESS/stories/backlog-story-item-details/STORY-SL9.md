# STORY-SL9: Deep Learning — CNNs, RNNs, Transformers

## User Story

I want comprehensive coverage of modern deep learning architectures so that I can understand convolutional neural networks, recurrent networks, transformers, and their applications to computer vision and sequence modeling.

## Context

This story is a major effort covering three fundamental deep learning architectures. Each requires mathematical rigor (backpropagation through specialized layers, attention mechanisms, positional encodings) and practical implementation. Current notebooks are PyTorch tutorials with emojis and marketing language—they require complete rewrites to meet academic standards.

## Acceptance Criteria

### Lesson 9a: Convolutional Neural Networks

- [ ] Theory notebook (9a-theory) covers discrete convolution mathematics, backpropagation through conv layers, pooling layer gradients, weight sharing with >100 LaTeX symbols
- [ ] Theory notebook includes from-scratch CNN implementation in NumPy with forward and backward pass
- [ ] Theory notebook demonstrates convergence analysis and proves weight sharing reduces parameters
- [ ] Practical notebook (9a-practical) applies CNNs to image classification (CIFAR-10 or similar)
- [ ] Practical notebook covers transfer learning mathematics and feature reuse across models
- [ ] Both 9a notebooks follow academic standards: 60-80 hours, >20 math symbols
- [ ] References Stanford CS231n lectures and Goodfellow's Deep Learning Book Chapter 9

### Lesson 9b: Recurrent Neural Networks

- [ ] Theory notebook (9b-theory) derives Backpropagation Through Time (BPTT), vanishing/exploding gradient mathematics, LSTM gate equations with >100 LaTeX symbols
- [ ] Theory notebook covers GRU simplification and performance trade-offs
- [ ] Theory notebook includes from-scratch RNN and LSTM implementation in NumPy with full gradient derivation
- [ ] Practical notebook (9b-practical) applies to sequence modeling and time series forecasting
- [ ] Practical notebook demonstrates vanishing gradient problem and LSTM solutions empirically
- [ ] Both 9b notebooks follow academic standards: 60-80 hours, >20 math symbols
- [ ] References Goodfellow Chapter 10 and Hochreiter & Schmidhuber LSTM paper

### Lesson 9c: Transformers & Attention

- [ ] Theory notebook (9c-theory) derives scaled dot-product attention, multi-head attention, positional encoding with >100 LaTeX symbols
- [ ] Theory notebook covers self-attention vs cross-attention mathematics and encoder-decoder architecture
- [ ] Theory notebook includes from-scratch attention mechanism in NumPy showing scaled dot-product computation
- [ ] Practical notebook (9c-practical) applies transformers to sequence-to-sequence tasks
- [ ] Practical notebook explains pre-trained model mathematics and transfer learning for language models
- [ ] Both 9c notebooks follow academic standards: 60-80 hours, >20 math symbols
- [ ] References "Attention Is All You Need" paper and Harvard NLP Annotated Transformer

### Overall Acceptance

- [ ] All six notebooks completely rewritten from current stubs/tutorials
- [ ] No emojis, marketing language, or corporate buzzwords in any notebook
- [ ] All from-scratch implementations are production-quality and educationally clear
- [ ] Total effort: ~180 hours across all three sub-stories
- [ ] All notebooks ready for publication

## Definition of Done

- [ ] All six deep learning notebooks (9a, 9b, 9c each with theory and practical) are complete
- [ ] Mathematical rigor matches or exceeds lessons 1-2 quality benchmarks
- [ ] From-scratch implementations are clear enough for a student to understand and extend
- [ ] All notebooks pass academic quality review
- [ ] Notebooks ready for publication

## Story Points

56 (total of 14 per lesson sub-task × 4 lesson-sub-tasks, divided by 2 for parallelization potential)

## Technical Notes

These are the most complex lessons and require complete rewrites. The current stubs exist at commit 366684d in git history but contain only PyTorch tutorials with marketing language. They must be rebuilt from first principles.
