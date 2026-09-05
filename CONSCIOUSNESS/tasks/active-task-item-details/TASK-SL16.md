# TASK-SL16: Lesson 9c: Transformer practical — sequence-to-sequence, pre-trained model mathematics, NumPy attention mechanism

## Context

Create the practical notebook for Transformers. Apply transformers to sequence-to-sequence tasks (machine translation, summarization). Explain pre-trained model mathematics and demonstrate from-scratch attention from theory. Compare to modern implementations.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/9f_transformer_practical.ipynb`
- [ ] Sequence-to-sequence task: Machine translation, text summarization, or question answering
- [ ] Dataset preparation: Tokenization, padding, vocabulary construction, train/test split
- [ ] Transformer encoder-decoder implementation: Build using PyTorch with attention modules
- [ ] Training loop: Loss function, optimizer, gradient updates, validation monitoring
- [ ] From-scratch attention mechanism in NumPy: Demonstrate scaled dot-product from 9c theory
- [ ] From-scratch multi-head attention in NumPy showing separate heads and concatenation
- [ ] Pre-trained model mathematics: Explain what pre-training learns, why transfer effective
- [ ] Fine-tuning demonstration: Use pre-trained (BERT/GPT) model and fine-tune on downstream task
- [ ] Beam search decoding: Generate sequences greedily and with beam search comparison
- [ ] Attention visualization: Show which positions attend to which (attention weights)
- [ ] Performance analysis: BLEU score (for translation) or appropriate metrics for task
- [ ] Visualization: Attention heatmaps, generated sequences, loss curves
- [ ] No emojis, no corporate buzzwords
- [ ] References cited: PyTorch documentation, "Attention Is All You Need", Hugging Face tutorials
- [ ] Notebook length: 80 hours effort

## Technical Notes

Sequence-to-sequence: Encoder reads input, decoder generates output one token at a time.

Beam search: Keep k best hypotheses, decode iteratively, select most likely full sequence.

Pre-trained models: Transformer trained on massive text corpus (language model), then fine-tuned on specific task.

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] From-scratch implementation matches PyTorch in results
- [ ] Attention visualizations provide clear understanding of model behavior
- [ ] Pre-trained model transfer learning approach is well-demonstrated
- [ ] Ready for peer review and publication

## Story Points

16 (80 hours estimated effort)

## Blocked By

TASK-SL15 (requires understanding from theory notebook)

## Environment note

`transformers`, `datasets` and `sentencepiece` are installed into `.venv` by TASK-SL026 (Rebuild reproducible verification environment for the curriculum). Use a small pre-trained model (`distilbert-base-uncased` or `t5-small`) and a short fine-tune so the notebook executes in under 30 minutes on CPU. If the model or dataset download is unavailable, fall back to a from-scratch encoder-decoder on a synthetic reverse/copy task and state the substitution in the notebook — do not fake a fine-tune.

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/9f_transformer_practical.ipynb --type practical --execute
```
Must exit 0: 20+ LaTeX spans, zero emojis, zero marketing words, zero error outputs, references present. Match the structure of `notebooks/9d_rnn_practical.ipynb`.

## Dispatch

model: sonnet
effort: high
max_turns: 120
reviewer_model: sonnet
