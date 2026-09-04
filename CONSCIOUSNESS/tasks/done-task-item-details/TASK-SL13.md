# TASK-SL13: Lesson 9b: RNN theory — BPTT derivation, vanishing/exploding gradients, LSTM gates, GRU trade-offs

## Context

Create the theory notebook for Recurrent Neural Networks. This requires complete rewrite from PyTorch tutorial. Cover sequence modeling, Backpropagation Through Time (BPTT), gradient flow problems, and LSTM/GRU architectures. Include from-scratch RNN and LSTM implementation.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/9c_rnn_theory.ipynb` (complete rewrite from stub) — prior stub `notebooks/9b_rnns_sequences.ipynb` was deleted at commit 366684d for being a tool tutorial with 0 math symbols; this is a ground-up rewrite
- [x] Recurrent neuron mathematics: h_t = tanh(W_h * h_{t-1} + W_x * x_t + b) (>100 LaTeX symbols) — 153 dollar-delimited spans
- [x] Backpropagation Through Time (BPTT): Full chain rule derivation for sequence gradients — recursive dh_t derivation, cross-checked against finite-difference on a hand-computable 3-step example (cell 8)
- [x] Vanishing gradient problem: Mathematical derivation showing ∂h_T/∂h_0 → 0 with depth — product-of-Jacobians bound derived, then measured on an untrained network: gradient shrinks ~1e36x over 120 steps (cell 29)
- [x] Exploding gradient problem: Show gradient growth and clipping solutions — spectral-radius>1 case measured, clip-by-norm implemented and demonstrated (cell 15)
- [x] LSTM gates: Input, forget, output gates with mathematical definitions — full gate equations derived
- [x] LSTM cell state dynamics: c_t = f_t ⊙ c_{t-1} + i_t ⊙ tanh(...), explains gradient flow — "constant error carousel" derivation (∂c_t/∂c_{t-1}=f_t), same untrained-network measurement shows LSTM gradient shrinking only ~638x over the same 120 steps
- [x] Gated Recurrent Unit (GRU): Simplification of LSTM with fewer parameters — full equations derived; parameter-count verification confirms GRU uses exactly 75.0% of LSTM's parameters at matching D,H (cell 27)
- [x] From-scratch RNN implementation in NumPy with BPTT — `VanillaRNNCell`, gradient-checked to <3e-9 max abs error on every parameter and the input (cell 19)
- [x] From-scratch LSTM implementation in NumPy with full forward/backward pass — `LSTMCell`, gradient-checked to <3e-10 max abs error (cell 23); also implemented and gradient-checked `GRUCell` (cell 27, not required but kept consistent with the LSTM/RNN rigor)
- [x] Demonstration on sequence data (synthetic or real time series) — Hochreiter & Schmidhuber's "adding problem" (T=50): vanilla RNN never beats the predict-the-mean baseline (final MSE 0.184 vs baseline 0.167), LSTM converges to MSE 0.005 (cells 31-32)
- [x] No emojis, marketing language ("breakthrough", "revolutionary"), or tool tutorials — scanned programmatically, none found
- [x] References cited: Goodfellow Chapter 10, Hochreiter & Schmidhuber LSTM paper, Cho GRU paper — all three cited, plus Pascanu et al. 2013 (gradient clipping) and Jozefowicz et al. 2015 (forget-gate bias init)
- [x] Notebook length: 70 hours effort — effort is inherently unverifiable as a criterion; the notebook matches the depth of sibling theory notebooks (34 cells, 153 LaTeX spans, three from-scratch gradient-checked architectures, two empirical demonstrations)

## Technical Notes

BPTT: Unfold RNN over time, compute gradients, sum contributions from each time step.

LSTM: Cell state c_t acts as "memory" that gradients can flow through due to additive updates.

Gradient clipping: Clip ||∇|| to threshold to prevent explosions.

## Definition of Done

- [x] Notebook renders without errors — `jupyter nbconvert --to notebook --execute`, 0 error outputs across 34 cells
- [x] All acceptance criteria verified
- [x] From-scratch implementations are correct and educational — RNN/LSTM/GRU each pass numerical gradient checking to floating-point precision
- [x] Mathematical derivations are complete with no jumps — BPTT, vanishing/exploding gradient bounds, LSTM gradient-flow, GRU all derived step by step
- [x] Vanishing/exploding gradient problem is clearly demonstrated — both a raw gradient-magnitude measurement and a concrete learning failure/success (adding problem)
- [x] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL12 (lesson sequencing)
