# TASK-SL15: Lesson 9c: Transformer theory — scaled dot-product attention, multi-head attention, positional encoding, self/cross-attention

## Context

Create the theory notebook for Transformers and Attention Mechanisms. This is the most complex deep learning lesson and requires complete rewrite from the current marketing-language stub. Cover attention mathematics, multi-head mechanisms, positional encodings, and transformer architecture. Include from-scratch attention implementation.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/9e_transformer_theory.ipynb` (complete rewrite from stub)
- [ ] Scaled dot-product attention: Q, K, V matrices, softmax, scale factor 1/sqrt(d_k) (>100 LaTeX symbols)
- [ ] Attention mathematics: Attention(Q, K, V) = softmax(QK^T/sqrt(d_k))V with full derivation
- [ ] Multi-head attention: Separate attention heads in parallel, concatenation, motivation
- [ ] Positional encoding mathematics: Sinusoidal vs learned encodings, why needed for permutation invariance
- [ ] Self-attention vs cross-attention: Different use cases, mathematical difference
- [ ] Transformer encoder architecture: Stack of attention and feed-forward layers with residual connections
- [ ] Transformer decoder architecture: Masked self-attention, encoder-decoder attention, causal masking
- [ ] From-scratch scaled dot-product attention in NumPy
- [ ] From-scratch multi-head attention demonstrating separate heads and concatenation
- [ ] Demonstration on simple sequence task or synthetic data
- [ ] No emojis, marketing language ("revolutionary", "most important"), or tool tutorials
- [ ] References cited: "Attention Is All You Need" paper, Harvard NLP Annotated Transformer, Goodfellow Chapter
- [ ] Notebook length: 80 hours effort

## Technical Notes

Attention: softmax(QK^T) learns which positions attend to which. Scaled by 1/sqrt(d_k) for stable gradients.

Multi-head: Allows different representations. h = Concat(head_1, ..., head_h)W^O where head_i = Attention(QW^Q, KW^K, VW^V).

Positional encoding: PE(pos, 2i) = sin(pos/10000^{2i/d}), PE(pos, 2i+1) = cos(pos/10000^{2i/d}). Allows model to use position information.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch implementation is correct and educational
- [ ] Mathematical derivations are complete and rigorous
- [ ] No marketing language or PyTorch tutorials
- [ ] Ready for peer review and publication

## Story Points

16 (80 hours estimated effort)

## Blocked By

TASK-SL14 (lesson sequencing)
