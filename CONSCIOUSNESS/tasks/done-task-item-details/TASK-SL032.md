# TASK-SL032: Uplift Lesson 3a neural networks theory to the curriculum bar

## Context

`notebooks/3a_neural_networks_theory.ipynb` is 85 KB across 45 cells but carries only 9 LaTeX spans and emojis — it explains neural networks largely in prose where the curriculum's own benchmark (1a at 97 spans, 2a at 65, 9a at 91, 9c at 153) derives them. Lesson 3 is also load-bearing: 9a's convolution backpropagation and 9c's BPTT both assume the reader has already seen the chain rule applied layer by layer here. The roadmap lists 3a as complete with "120 math symbols", which the measurement contradicts; that claim should be corrected as part of this task.

## Acceptance Criteria

- [x] `notebooks/3a_neural_networks_theory.ipynb` reaches at least 100 LaTeX spans with zero emojis, keeping its existing structure and prose where sound and converting its mathematics from text to LaTeX — full rewrite in the 9c shape per the pre-mortem's stated fallback (the existing 45 cells were visualisation-driven prose with 9 spans, not derivations worth keeping structurally); 24 cells (10 code, 14 markdown); verifier measured 122 spans (>= 100), 0 emoji
- [x] Forward pass written out for a multi-layer perceptron: $z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}$, $a^{(l)} = \sigma(z^{(l)})$, with layer shapes stated — Section 2, with a code cell verifying the shape bookkeeping on a toy 3-layer network
- [x] Activation functions derived with their gradients: sigmoid $\sigma'(z) = \sigma(z)(1-\sigma(z))$, tanh $1 - \tanh^2(z)$, ReLU and its subgradient at zero, plus why saturating activations cause vanishing gradients (forward-referencing 9c) — Section 3 derives all three and the vanishing-gradient mechanism (explicitly linked to 9c's BPTT); measured run: all three gradients match finite differences to ~1e-10
- [x] Backpropagation derived in full: the output-layer error $\delta^{(L)} = \nabla_a J \odot \sigma'(z^{(L)})$, the recursion $\delta^{(l)} = ((W^{(l+1)})^\top \delta^{(l+1)}) \odot \sigma'(z^{(l)})$, and the parameter gradients $\partial J/\partial W^{(l)} = \delta^{(l)} (a^{(l-1)})^\top$ and $\partial J/\partial b^{(l)} = \delta^{(l)}$ — each step justified by the chain rule, no jumps — Section 5 derives all four formulas from the chain rule; measured run: the recursion matches finite differences to 9.9e-11
- [x] Loss functions stated: squared error for regression and cross-entropy for classification, with the softmax-plus-cross-entropy gradient simplifying to $\hat y - y$ derived rather than asserted — Section 4 derives the simplification via $\log\hat y_k = z_k - \log\sum_j e^{z_j}$; measured run confirms `y_hat - y` matches finite differences to 1.86e-10
- [x] Weight initialisation covered: why zeros break symmetry, and the variance argument behind Xavier and He initialisation — Section 6; the symmetry demo initially zeroed only one layer (a genuine bug — the next layer's distinct weights re-broke the symmetry on the backward pass) and was fixed to zero the whole network, documented below
- [x] From-scratch NumPy MLP with forward and backward passes, verified by numerical gradient checking to at least 1e-6 on every parameter tensor, with the check's output printed in the notebook (the pattern used in 9a and 9c) — Section 8; measured run: max difference 2.38e-11 across every parameter tensor, well under 1e-6
- [x] The from-scratch network trained on a real dataset (MNIST subset or breast cancer) with a loss curve and test accuracy reported, plus a scikit-learn `MLPClassifier` baseline for comparison — Section 9 uses `load_breast_cancer` (ships with scikit-learn, no network fetch needed); measured run: from-scratch test accuracy 94.74%, `MLPClassifier` baseline 96.49%
- [x] CURRICULUM_ROADMAP.md's benchmark line for 3a is corrected to the measured span count — corrected "120 math symbols, 5 implementations, 55KB" to "122 LaTeX spans ... 1 from-scratch implementation with numerical gradient checking, 73KB"
- [x] References: Goodfellow Chapters 6 and 8, CS231n backpropagation notes, Nielsen's *Neural Networks and Deep Learning* — Further Reading cites all three

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

- The existing 45 cells are worth keeping structurally; if the notebook is mostly narrative with little to build on, a rewrite in the 9c shape is acceptable and should be said in the commit — assumption failed as flagged: the 45 cells were almost entirely `visualise_*`/`plot_*`/`demonstrate_*` helper functions producing pictures, with no derivation of backprop, no gradient checking, and no real dataset; rewrote in the 9c shape, stated in the commit message

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit 569a106, worked directly
in-session per the operator's pivot on TASK-SL028 (Build autonomous
syllabus run orchestrator with model-aware dispatch) (self-dispatch dropped
in favour of continuing in this session).

### A genuine mid-build defect, found and fixed before closing

The first execution attempt passed every verifier check but its Section 6
symmetry-breaking demonstration was silently wrong: it zeroed only the
first layer's weights (`W1`) while leaving the second layer (`W2`) at
independent random values, then reported `every row of dJ/dW1 is
identical: False` — the opposite of the intended demonstration. The bug
was conceptual, not a typo: two units in a layer are only interchangeable
if *both* their incoming weights (so their forward activations match) and
their outgoing weights (so the backward recursion's `(W^(l+1))^T delta`
term treats them identically) are the same. Zeroing one layer while the
other stays random still differentiates the gradient on the backward
pass. Fixed by zeroing the whole network for the "broken symmetry" case
(confirmed `True`, with all gradients exactly zero — a further real
observation now noted in the code comments) and using independent
Xavier-scaled weights throughout for the "not broken" case. The markdown
derivation was rewritten to state the both-directions condition
precisely rather than the looser, incorrect "one layer's weights" framing
the first draft used.

### Verification command output

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/3a_neural_networks_theory.ipynb --type theory --execute
PASS 3a_neural_networks_theory.ipynb [theory]
verify: 1 passed, 0 failed
```

### JSON report (`reports/verify/3a_neural_networks_theory.json`)

```json
{
  "notebook": "3a_neural_networks_theory.ipynb",
  "type": "theory",
  "metrics": {
    "latex_spans": 122,
    "display_dollar_blocks": 0,
    "code_cells": 10,
    "markdown_cells": 14,
    "bytes": 75129,
    "emoji_count": 0,
    "marketing_hits": 0,
    "error_outputs": 0,
    "has_title": true,
    "has_references": true,
    "executed": true
  },
  "passed": true
}
```
