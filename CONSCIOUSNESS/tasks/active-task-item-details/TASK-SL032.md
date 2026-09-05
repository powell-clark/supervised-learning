# TASK-SL032: Uplift Lesson 3a neural networks theory to the curriculum bar

## Context

`notebooks/3a_neural_networks_theory.ipynb` is 85 KB across 45 cells but carries only 9 LaTeX spans and emojis — it explains neural networks largely in prose where the curriculum's own benchmark (1a at 97 spans, 2a at 65, 9a at 91, 9c at 153) derives them. Lesson 3 is also load-bearing: 9a's convolution backpropagation and 9c's BPTT both assume the reader has already seen the chain rule applied layer by layer here. The roadmap lists 3a as complete with "120 math symbols", which the measurement contradicts; that claim should be corrected as part of this task.

## Acceptance Criteria

- [ ] `notebooks/3a_neural_networks_theory.ipynb` reaches at least 100 LaTeX spans with zero emojis, keeping its existing structure and prose where sound and converting its mathematics from text to LaTeX
- [ ] Forward pass written out for a multi-layer perceptron: $z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}$, $a^{(l)} = \sigma(z^{(l)})$, with layer shapes stated
- [ ] Activation functions derived with their gradients: sigmoid $\sigma'(z) = \sigma(z)(1-\sigma(z))$, tanh $1 - \tanh^2(z)$, ReLU and its subgradient at zero, plus why saturating activations cause vanishing gradients (forward-referencing 9c)
- [ ] Backpropagation derived in full: the output-layer error $\delta^{(L)} = \nabla_a J \odot \sigma'(z^{(L)})$, the recursion $\delta^{(l)} = ((W^{(l+1)})^\top \delta^{(l+1)}) \odot \sigma'(z^{(l)})$, and the parameter gradients $\partial J/\partial W^{(l)} = \delta^{(l)} (a^{(l-1)})^\top$ and $\partial J/\partial b^{(l)} = \delta^{(l)}$ — each step justified by the chain rule, no jumps
- [ ] Loss functions stated: squared error for regression and cross-entropy for classification, with the softmax-plus-cross-entropy gradient simplifying to $\hat y - y$ derived rather than asserted
- [ ] Weight initialisation covered: why zeros break symmetry, and the variance argument behind Xavier and He initialisation
- [ ] From-scratch NumPy MLP with forward and backward passes, verified by numerical gradient checking to at least 1e-6 on every parameter tensor, with the check's output printed in the notebook (the pattern used in 9a and 9c)
- [ ] The from-scratch network trained on a real dataset (MNIST subset or breast cancer) with a loss curve and test accuracy reported, plus a scikit-learn `MLPClassifier` baseline for comparison
- [ ] CURRICULUM_ROADMAP.md's benchmark line for 3a is corrected to the measured span count
- [ ] References: Goodfellow Chapters 6 and 8, CS231n backpropagation notes, Nielsen's *Neural Networks and Deep Learning*

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/3a_neural_networks_theory.ipynb --type theory --execute
```
Must exit 0 with `latex_spans >= 100`, `emoji_count == 0`. Paste the output and JSON report into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 140
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- 3b already trains an MLP; duplicating it here wastes the reader's time — 3a's implementation must be from scratch in NumPy with gradient checking, 3b keeps the library work
- Gradient checking a full MLP is slow; keep the checked network tiny (2 layers, a handful of units) as 9c does

### Weak assumptions

- The existing 45 cells are worth keeping structurally; if the notebook is mostly narrative with little to build on, a rewrite in the 9c shape is acceptable and should be said in the commit
