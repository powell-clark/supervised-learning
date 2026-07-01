# TASK-SL13: Lesson 9b: RNN theory — BPTT derivation, vanishing/exploding gradients, LSTM gates, GRU trade-offs

## Context

Create the theory notebook for Recurrent Neural Networks. This requires complete rewrite from PyTorch tutorial. Cover sequence modeling, Backpropagation Through Time (BPTT), gradient flow problems, and LSTM/GRU architectures. Include from-scratch RNN and LSTM implementation.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/9c_rnn_theory.ipynb` (complete rewrite from stub)
- [ ] Recurrent neuron mathematics: h_t = tanh(W_h * h_{t-1} + W_x * x_t + b) (>100 LaTeX symbols)
- [ ] Backpropagation Through Time (BPTT): Full chain rule derivation for sequence gradients
- [ ] Vanishing gradient problem: Mathematical derivation showing ∂h_T/∂h_0 → 0 with depth
- [ ] Exploding gradient problem: Show gradient growth and clipping solutions
- [ ] LSTM gates: Input, forget, output gates with mathematical definitions
- [ ] LSTM cell state dynamics: c_t = f_t ⊙ c_{t-1} + i_t ⊙ tanh(...), explains gradient flow
- [ ] Gated Recurrent Unit (GRU): Simplification of LSTM with fewer parameters
- [ ] From-scratch RNN implementation in NumPy with BPTT
- [ ] From-scratch LSTM implementation in NumPy with full forward/backward pass
- [ ] Demonstration on sequence data (synthetic or real time series)
- [ ] No emojis, marketing language ("breakthrough", "revolutionary"), or tool tutorials
- [ ] References cited: Goodfellow Chapter 10, Hochreiter & Schmidhuber LSTM paper, Cho GRU paper
- [ ] Notebook length: 70 hours effort

## Technical Notes

BPTT: Unfold RNN over time, compute gradients, sum contributions from each time step.

LSTM: Cell state c_t acts as "memory" that gradients can flow through due to additive updates.

Gradient clipping: Clip ||∇|| to threshold to prevent explosions.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch implementations are correct and educational
- [ ] Mathematical derivations are complete with no jumps
- [ ] Vanishing/exploding gradient problem is clearly demonstrated
- [ ] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL12 (lesson sequencing)
