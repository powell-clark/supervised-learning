# TASK-SL034: Uplift practicals 1b, 2b, 2c, 3b: purge emojis, add mathematical explanations

## Context

Measured 2026-09-04 against the practical bar (20+ LaTeX spans, zero emojis): `1b_logistic_regression_practical` 12 spans; `2b_decision_trees_practical` 24 spans but carries emojis; `2c_decision_trees_ATLAS_model_comparison` 0 spans and emojis; `3b_neural_networks_practical` 0 spans. These are otherwise substantial notebooks (170 KB, 279 KB, 251 KB, 92 KB) — the gap is mathematical explanation of what the library calls are doing, and decoration that the style rules forbid.

## Acceptance Criteria

- [ ] All four notebooks reach at least 20 LaTeX spans and zero emojis, with zero marketing words
- [ ] `1b`: the PyTorch training loop's mathematics made explicit — binary cross-entropy $J = -\frac{1}{m}\sum [y\log\hat y + (1-y)\log(1-\hat y)]$, the logistic gradient, what the optimiser's learning rate and momentum terms do, and a cross-check of the fitted coefficients against 1a's from-scratch solution
- [ ] `2b`: emojis removed; the splitting criteria stated in LaTeX — Gini $1-\sum_k p_k^2$, entropy $-\sum_k p_k \log_2 p_k$, information gain, and the regression variance-reduction criterion; plus what `max_depth` and `min_samples_leaf` do to the bias-variance trade-off, tied to the results already in the notebook
- [ ] `2c`: emojis removed; ATLAS's comparison metrics defined mathematically (precision, recall, $F_1$, ROC-AUC as the probability a random positive outranks a random negative) and the feature-engineering transformations it applies stated as formulae
- [ ] `3b`: the network's forward and backward mathematics stated (referring back to 3a rather than re-deriving), the loss and optimiser written out, and the library results compared numerically to 3a's from-scratch implementation
- [ ] Every notebook still executes end to end with stored outputs; no cell is deleted merely to raise a metric
- [ ] Each notebook has a Further Reading section

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

- 2c's ATLAS system is stable enough to document as-is; if its behaviour and its description disagree, document the behaviour and file a task for the discrepancy
