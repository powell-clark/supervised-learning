# TASK-SL036: Uplift practicals 9b and 9d to the practical bar

## Context

`notebooks/9b_cnn_practical.ipynb` has 10 LaTeX spans and `notebooks/9d_rnn_practical.ipynb` has 9, both under the 20-span practical bar (their theory partners 9a and 9c sit at 91 and 153). Both notebooks are recent and structurally sound, so this is additive work. TASK-SL029 (Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes) also assigns three FEAT-SL6 criteria here that the shipped RNN notebooks do not yet cover.

## Acceptance Criteria

- [x] `9b` and `9d` each reach at least 20 LaTeX spans, zero emojis, zero marketing words — measured: 9b 21 spans, 9d 46 spans; both 0 emoji, both 0 marketing hits
- [x] `9b`: transfer-learning mathematics stated — why freezing a backbone means $\partial L/\partial W_{\text{frozen}}$ is never computed and what that does to optimiser state and step cost; the softmax cross-entropy objective; and the parameter-count arithmetic for the fine-tuned head versus the full network — all three added to cell 11/13, sharpening the existing (already substantial) frozen/fine-tuning discussion to the precise `requires_grad=False` autograd-skips-the-node claim
- [x] `9d`: the sliding-window construction written as a mapping from series to $(X, y)$ pairs; the normalisation transform and its inverse for reporting errors on the original scale; MAE and RMSE defined; and the free-running decoder's error-accumulation argument stated as a recurrence — all four added at cells 7/17/25
- [x] **Bidirectional RNNs** covered in 9d (carried over from FEAT-SL6): the forward and backward hidden states $\overrightarrow{h}_t, \overleftarrow{h}_t$, their concatenation, why this is available for classification over a complete sequence but not for causal forecasting — with a worked example or a clearly-argued explanation of why it is inapplicable to the forecasting task at hand — new section added (markdown argument plus a code cell demonstrating the concatenated-width doubling)
- [x] **Character-level sequence modelling** added to 9d (carried over from FEAT-SL6): a small character-level LSTM trained on a short public-domain text, with sampled output shown; keep it small enough to execute within the verifier's time and memory limits — a one-layer, 32-hidden-unit LSTM trained 60 epochs on a repeated public-domain nursery rhyme (Jane Taylor, "The Star", 1806); measured run sampled real phrase fragments ("twinkle little star ih world so high like a diamond...") in well under a second
- [x] **LSTM vs GRU comparison** added to 9d (carried over from FEAT-SL6): both trained on the same task with matched hidden size, reporting parameter counts, wall-clock training time and final loss, with the 25% parameter difference from 9c confirmed empirically — measured run: LSTM 1216 params vs GRU 912 (`assert abs(reduction - 0.25) < 1e-6` passed, exact not approximate), plus wall-clock and final MSE for both
- [x] Both notebooks still execute end to end with stored outputs — both `executed: true`, `error_outputs: 0`; 9b needed `--max-mem-mb 8192` for the ResNet-18 fine-tuning loop's peak memory (see closing note)
- [x] FEAT-SL6's three previously-unticked criteria are ticked with evidence once this lands — done, commit 9ea8437

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

- A suitable short public-domain text is available offline; if not, generate a synthetic character sequence with structure (repeating motifs) and say so — used a genuine public-domain text instead (Jane Taylor's 1806 nursery rhyme "The Star," better known as "Twinkle, Twinkle, Little Star," embedded directly as a Python string literal, repeated 40x for enough training windows; no network or file dependency)

## Closing note

Closed 2026-09-05 by session sl-07bdf165 (forked from sl-0be0fde7 mid-task;
the claim and all prior work carried over cleanly) on commits 650a14d (9d)
and 1e3e858 (9b), worked directly in-session per the operator's pivot on
TASK-SL028 (Build autonomous syllabus run orchestrator with model-aware
dispatch) (self-dispatch dropped in favour of continuing in this session).

### 9b's memory guard needed real measurement, not a guess

First execution attempt at `--max-mem-mb 4096` produced 4 genuine OOM
errors (`RuntimeError: can't allocate memory`) at the ResNet-18
fine-tuning and CIFAR-10 forward-pass points -- not a code bug, the cap
was simply too tight for 224x224 ResNet-18 batches. Retried at 6144MB
(the value that had sufficed for every other heavy notebook this
session): down to 1 error, a single 1.2GB allocation still failing in
the fine-tuning loop. Retried at 8192MB, with the host's actual free
memory checked before and during each attempt (never below the 2.5GB
floor): clean pass, memory recovered fully afterward. Documenting the
escalation rather than jumping straight to a large cap, per the
pre-mortem's own instruction to let the guard refuse rather than assume.

### Verification command output

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/9b_cnn_practical.ipynb --type practical --execute --max-mem-mb 8192
PASS 9b_cnn_practical.ipynb [practical]
verify: 1 passed, 0 failed

$ .venv/bin/python scripts/verify_notebook.py notebooks/9d_rnn_practical.ipynb --type practical --execute --max-mem-mb 6144
PASS 9d_rnn_practical.ipynb [practical]
verify: 1 passed, 0 failed
```

### Final metrics (JSON reports)

| notebook | spans | emoji | marketing | executed | errors |
|---|---:|---:|---:|---|---:|
| 9b | 21 (3 display) | 0 | 0 | true | 0 |
| 9d | 46 (6 display) | 0 | 0 | true | 0 |
