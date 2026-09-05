# TASK-SL034: Uplift practicals 1b, 2b, 2c, 3b: purge emojis, add mathematical explanations

## Context

Measured 2026-09-04 against the practical bar (20+ LaTeX spans, zero emojis): `1b_logistic_regression_practical` 12 spans; `2b_decision_trees_practical` 24 spans but carries emojis; `2c_decision_trees_ATLAS_model_comparison` 0 spans and emojis; `3b_neural_networks_practical` 0 spans. These are otherwise substantial notebooks (170 KB, 279 KB, 251 KB, 92 KB) — the gap is mathematical explanation of what the library calls are doing, and decoration that the style rules forbid.

## Acceptance Criteria

- [x] All four notebooks reach at least 20 LaTeX spans and zero emojis, with zero marketing words — measured: 1b 24 spans, 2b 23 spans, 2c 22 spans, 3b 21 spans; all 0 emoji, all 0 marketing hits
- [x] `1b`: the PyTorch training loop's mathematics made explicit — binary cross-entropy $J = -\frac{1}{m}\sum [y\log\hat y + (1-y)\log(1-\hat y)]$, the logistic gradient, what the optimiser's learning rate and momentum terms do, and a cross-check of the fitted coefficients against 1a's from-scratch solution — done in the "why PyTorch" and "hyperparameter optimisation" sections; the cross-check is a from-scratch NumPy gradient-descent logistic regression fit on the same features (1a's own implementation is too different in structure to import directly), agreeing with the PyTorch/Adam model on 98.25% of test predictions
- [x] `2b`: emojis removed; the splitting criteria stated in LaTeX — Gini $1-\sum_k p_k^2$, entropy $-\sum_k p_k \log_2 p_k$, information gain, and the regression variance-reduction criterion; plus what `max_depth` and `min_samples_leaf` do to the bias-variance trade-off, tied to the results already in the notebook — all four criteria stated in the "Understanding overfitting" section, tied to the notebook's own unrestricted (R²=1.0/0.786)/controlled (0.777/0.787)/grid-search-optimal (0.805) measurements; 7 emoji stripped
- [x] `2c`: emojis removed; ATLAS's comparison metrics defined mathematically (precision, recall, $F_1$, ROC-AUC as the probability a random positive outranks a random negative) and the feature-engineering transformations it applies stated as formulae — **defect found and documented, not fabricated**: ATLAS actually compares regression models on log-price ($R^2$, MAE), not classification; documented accurately in cell 13's markdown per this card's own pre-mortem instruction, follow-up TASK-SL041 filed to correct the assumption at the card level; feature-engineering (log-price target, one-hot, smoothed out-of-fold target encoding) stated as formulae in cell 9; 2 emoji stripped
- [x] `3b`: the network's forward and backward mathematics stated (referring back to 3a rather than re-deriving), the loss and optimiser written out, and the library results compared numerically to 3a's from-scratch implementation — done in "Building our first neural network"/"Training our first network"/"Comprehensive evaluation"; numerical comparison cites 3A's measured 94.74% test accuracy against `comparison_df`'s figures for `SimpleNeuralNetwork`/`ModernNeuralNetwork`
- [x] Every notebook still executes end to end with stored outputs; no cell is deleted merely to raise a metric — all four `executed: true`, `error_outputs: 0`; 3b needed four genuine pre-existing bugs fixed to reach this (see closing note), none of which deleted a cell — one fix (a markdown fragment stranded inside a code cell) added a cell instead
- [x] Each notebook has a Further Reading section — 1b/2c: added; 2b/3b: already present, confirmed via `has_references`

## Verification

```bash
for nb in 1b_logistic_regression_practical 2b_decision_trees_practical 2c_decision_trees_ATLAS_model_comparison 3b_neural_networks_practical; do
  .venv/bin/python scripts/verify_notebook.py "notebooks/$nb.ipynb" --type practical --execute || echo "FAILED $nb"
done
```
All four must exit 0. Paste the summary lines into the closing note.

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

- 2b and 2c are large and load the London housing data; execution needs the data files present and the memory guard respected — run them one at a time
- Adding formulae that do not match what the code actually does is worse than no formulae — read each cell's code before writing its mathematics
- Emoji removal that also strips legitimate mathematical unicode (≤, ∑) would be a regression; the verifier's emoji class excludes those, follow it

### Weak assumptions

- 2c's ATLAS system is stable enough to document as-is; if its behaviour and its description disagree, document the behaviour and file a task for the discrepancy — the disagreement materialised exactly as anticipated (ATLAS is regression, not classification); documented the real behaviour and filed TASK-SL041 (Correct STORY-SL12/TASK-SL034 assumption that ATLAS uses classification metrics)

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit 510dde5, worked
directly in-session per the operator's pivot on TASK-SL028 (Build
autonomous syllabus run orchestrator with model-aware dispatch)
(self-dispatch dropped in favour of continuing in this session).

### A genuine defect found outside this task's own scope (filed ahead)

While reading 1b's grid-search code to write its optimiser-mathematics
section, found that cell 16's `ModelEvaluator(model, ...)` evaluates
whatever the module-global `model` variable holds after cell 13's grid
search loop finishes -- the *last* hyperparameter combination tried, not
the highest-scoring row in `results_df`. Out of scope for a
math-explanation task; filed TASK-SL040 (Fix 1b evaluator using last
grid-search model, not the best one) rather than silently leaving it or
silently fixing training-loop logic outside this task's claim.

### Four genuine pre-existing bugs found and fixed in 3b (required by "executes end to end")

1. A demo loop passed `dropout=` in a kwargs dict to `ModernNeuralNetwork`,
   whose constructor parameter is `dropout_rate` -- `TypeError`.
2. `ReduceLROnPlateau(..., verbose=True)` -- `verbose` was removed from
   this torch version's signature (checked directly:
   `inspect.signature(ReduceLROnPlateau.__init__)`, torch 2.14.0+cpu).
3. A markdown fragment (`<a name="running-experiments">` + heading) was
   stranded inside a code cell, immediately after a Python list literal --
   a genuine `SyntaxError`. Split into its own markdown cell (increasing
   cell count by one, never decreasing it), preserving the Table of
   Contents' `#running-experiments` anchor target.
4. `analyze_activation_patterns` tried `np.array(sample_activations)` over
   activation vectors from layers of different widths (30→64→32→1), which
   raises `ValueError: inhomogeneous shape`. Fixed by NaN-padding every
   vector to the widest layer's size before stacking.

### Verification command output

```
$ for nb in 1b_logistic_regression_practical 2b_decision_trees_practical 2c_decision_trees_ATLAS_model_comparison 3b_neural_networks_practical; do
    .venv/bin/python scripts/verify_notebook.py "notebooks/$nb.ipynb" --type practical --execute --max-mem-mb 6144 || echo "FAILED $nb"
  done
PASS 1b_logistic_regression_practical.ipynb [practical]
verify: 1 passed, 0 failed
PASS 2b_decision_trees_practical.ipynb [practical]
verify: 1 passed, 0 failed
PASS 2c_decision_trees_ATLAS_model_comparison.ipynb [practical]
verify: 1 passed, 0 failed
PASS 3b_neural_networks_practical.ipynb [practical]
verify: 1 passed, 0 failed
```

All four notebooks required `--max-mem-mb 6144` (not the verifier's 2048
default) -- their grid/architecture searches retain more per-combination
state (histories, per-run metrics) than the default guard budgets for;
`DeadKernelError: Kernel died` was the failure mode at the default cap.
This is worth carrying forward into TASK-SL035/036/037's own verification
commands rather than rediscovering per notebook.

### Final metrics (JSON reports)

| notebook | spans | emoji | marketing | executed | errors |
|---|---:|---:|---:|---|---:|
| 1b | 24 | 0 | 0 | true | 0 |
| 2b | 23 (6 display) | 0 | 0 | true | 0 |
| 2c | 22 | 0 | 0 | true | 0 |
| 3b | 21 | 0 | 0 | true | 0 |
