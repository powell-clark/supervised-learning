# TASK-SL036: Uplift practicals 9b and 9d to the practical bar

## Context

`notebooks/9b_cnn_practical.ipynb` has 10 LaTeX spans and `notebooks/9d_rnn_practical.ipynb` has 9, both under the 20-span practical bar (their theory partners 9a and 9c sit at 91 and 153). Both notebooks are recent and structurally sound, so this is additive work. TASK-SL029 (Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes) also assigns three FEAT-SL6 criteria here that the shipped RNN notebooks do not yet cover.

## Acceptance Criteria

- [ ] `9b` and `9d` each reach at least 20 LaTeX spans, zero emojis, zero marketing words
- [ ] `9b`: transfer-learning mathematics stated — why freezing a backbone means $\partial L/\partial W_{\text{frozen}}$ is never computed and what that does to optimiser state and step cost; the softmax cross-entropy objective; and the parameter-count arithmetic for the fine-tuned head versus the full network
- [ ] `9d`: the sliding-window construction written as a mapping from series to $(X, y)$ pairs; the normalisation transform and its inverse for reporting errors on the original scale; MAE and RMSE defined; and the free-running decoder's error-accumulation argument stated as a recurrence
- [ ] **Bidirectional RNNs** covered in 9d (carried over from FEAT-SL6): the forward and backward hidden states $\overrightarrow{h}_t, \overleftarrow{h}_t$, their concatenation, why this is available for classification over a complete sequence but not for causal forecasting — with a worked example or a clearly-argued explanation of why it is inapplicable to the forecasting task at hand
- [ ] **Character-level sequence modelling** added to 9d (carried over from FEAT-SL6): a small character-level LSTM trained on a short public-domain text, with sampled output shown; keep it small enough to execute within the verifier's time and memory limits
- [ ] **LSTM vs GRU comparison** added to 9d (carried over from FEAT-SL6): both trained on the same task with matched hidden size, reporting parameter counts, wall-clock training time and final loss, with the 25% parameter difference from 9c confirmed empirically
- [ ] Both notebooks still execute end to end with stored outputs
- [ ] FEAT-SL6's three previously-unticked criteria are ticked with evidence once this lands

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/9b_cnn_practical.ipynb --type practical --execute
.venv/bin/python scripts/verify_notebook.py notebooks/9d_rnn_practical.ipynb --type practical --execute
```
Both must exit 0. Paste the outputs into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 140
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9 (and completes FEAT-SL6 criteria)
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- 9b fetches CIFAR-10 via `fetch_openml` and fine-tunes a ResNet-18 — that is the heaviest execution in the corpus on a host with ~6 GB free; keep the existing small subsets, do not enlarge them, and let the verifier's memory guard refuse rather than swapping the machine
- The three added 9d sections could double the notebook's execution time; keep the character model tiny (one layer, short sequences, few epochs) and the GRU comparison at the same scale as the existing LSTM run

### Weak assumptions

- A suitable short public-domain text is available offline; if not, generate a synthetic character sequence with structure (repeating motifs) and say so
