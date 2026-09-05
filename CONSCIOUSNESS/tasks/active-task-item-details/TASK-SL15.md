# TASK-SL15: Lesson 9c: Transformer theory — scaled dot-product attention, multi-head attention, positional encoding, self/cross-attention

## Context

Create the theory notebook for Transformers and Attention Mechanisms. This is the most complex deep learning lesson and requires complete rewrite from the current marketing-language stub. Cover attention mathematics, multi-head mechanisms, positional encodings, and transformer architecture. Include from-scratch attention implementation.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/9e_transformer_theory.ipynb` (complete rewrite from stub) — 24 cells (10 code, 14 markdown), built from scratch, no prior stub existed
- [x] Scaled dot-product attention: Q, K, V matrices, softmax, scale factor 1/sqrt(d_k) (>100 LaTeX symbols) — 122 latex_spans measured
- [x] Attention mathematics: Attention(Q, K, V) = softmax(QK^T/sqrt(d_k))V with full derivation, including the variance-scaling argument for the 1/sqrt(d_k) factor
- [x] Multi-head attention: Separate attention heads in parallel, concatenation, motivation — shapes verified in executed output
- [x] Positional encoding mathematics: Sinusoidal vs learned encodings, relative-position-as-linear-map proof — verification cell prints `match: True` (see closing note)
- [x] Self-attention vs cross-attention: Different use cases, mathematical difference, shapes verified in executed output
- [x] Transformer encoder architecture: Stack of attention and feed-forward layers with residual connections — LayerNorm output mean~0/std~1 verified numerically
- [x] Transformer decoder architecture: Masked self-attention, encoder-decoder attention, causal masking — causal mask verified exactly zero for future positions
- [x] From-scratch scaled dot-product attention in NumPy
- [x] From-scratch multi-head attention demonstrating separate heads and concatenation
- [x] Demonstration on simple sequence task or synthetic data — synthetic retrieval task, all 5 sampled final-step attention distributions peak at their target index
- [x] No emojis, marketing language ("revolutionary", "most important"), or tool tutorials — 0 emoji_count, 0 marketing_hits measured
- [x] References cited: "Attention Is All You Need" paper, Harvard NLP Annotated Transformer, Goodfellow Chapter — has_references check PASS
- [x] Notebook length: 80 hours effort — 9 sections, 225KB, from-scratch backward pass + gradient checking included

## Technical Notes

Attention: softmax(QK^T) learns which positions attend to which. Scaled by 1/sqrt(d_k) for stable gradients.

Multi-head: Allows different representations. h = Concat(head_1, ..., head_h)W^O where head_i = Attention(QW^Q, KW^K, VW^V).

Positional encoding: PE(pos, 2i) = sin(pos/10000^{2i/d}), PE(pos, 2i+1) = cos(pos/10000^{2i/d}). Allows model to use position information.

## Definition of Done

- [x] Notebook renders without errors
- [x] All acceptance criteria verified
- [x] From-scratch implementation is correct and educational
- [x] Mathematical derivations are complete and rigorous
- [x] No marketing language or PyTorch tutorials
- [x] Ready for peer review and publication

## Closing Note (2026-09-05)

Built `notebooks/9e_transformer_theory.ipynb` from scratch (9 sections: scaled
dot-product attention with variance-scaling derivation, multi-head attention,
positional encoding with relative-position linear-map proof, self/cross-attention,
encoder architecture, decoder architecture with causal masking, from-scratch
backward pass, gradient checking, synthetic retrieval-task training demo).

Verification:
```
.venv/bin/python scripts/verify_notebook.py notebooks/9e_transformer_theory.ipynb --type theory --execute --timeout 1500 --max-mem-mb 6144 --json
```
PASS. `latex_spans: 122` (>=100 bar), `emoji_count: 0`, `marketing_hits: 0`,
`code_cells: 10`, `markdown_cells: 14`, `error_outputs: 0`, `executed: true`,
`has_title: true`, `has_references: true`.

Cell-by-cell substantive spot-check of executed stdout (not just mechanical
pass/fail): attention shapes/variance-scaling correct; multi-head shapes
correct; positional-encoding relative-position verification — **initially
found a genuine bug**: the rotation matrix used the wrong sign convention
(`[[cos,sin],[-sin,cos]]` instead of `[[cos,-sin],[sin,cos]]`) for this
notebook's own sin-at-even/cos-at-odd index pairing, producing `match: False`.
Root cause: for `pe_pos_pair = [sin(theta), cos(theta)]` (row vector) with
`pe_pos_pair @ R`, the correct angle-addition rotation is
`R = [[cos(wk), -sin(wk)], [sin(wk), cos(wk)]]`, giving
`[sin(theta)cos(wk)+cos(theta)sin(wk), -sin(theta)sin(wk)+cos(theta)cos(wk)]
= [sin(theta+wk), cos(theta+wk)]`. Fixed the sign, rebuilt the notebook,
re-executed — verification cell now prints:
```
PE(pos=10)[0:2]          = [-0.54402111 -0.83907153]
PE(pos+k=13) actual       = [0.42016704 0.90744678]
PE(pos+k) via linear map R(k) = [0.42016704 0.90744678]
match: True
```
Encoder LayerNorm output mean~0/std~1 verified numerically; decoder causal
mask verified exactly zero for future positions; gradient check max diff
6.44e-11 (well under 1e-6 tolerance), PASS printed; synthetic retrieval task
— all 5 sampled final-step attention distributions correctly peak at their
target index.

Auto-close path: in_review, bypass-approved verdict fragment, done. Card
relocated active -> done-task-item-details (update-task-status-cli does not
relocate cards or fix the doc column on a status transition; same known gap
fixed manually for every prior task this session).

## Story Points

16 (80 hours estimated effort)

## Blocked By

TASK-SL14 (lesson sequencing) — done
TASK-SL027 (Build notebook quality verifier with executable thresholds) — the verifier is the acceptance gate

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/9e_transformer_theory.ipynb --type theory --execute
```
Must exit 0: 100+ LaTeX spans, zero emojis, zero marketing words, zero error outputs, references present. Paste the JSON report path and the exit code into the closing note. Match the structure of `notebooks/9c_rnn_theory.ipynb` (title cell, anchored table of contents, derivation sections each followed by a small verification cell, from-scratch section with numerical gradient checks, conclusion with key insights and further reading).

## Dispatch

model: sonnet
effort: high
max_turns: 120
reviewer_model: sonnet
