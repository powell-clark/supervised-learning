# TASK-SL031: Rewrite Lesson 0a linear regression theory to the curriculum bar

## Context

`notebooks/0a_linear_regression_theory.ipynb` is the corpus's opening notebook and its weakest: 20 KB, 20 cells, 18 LaTeX spans and emojis in the markdown, against a published theory bar of 100+ spans with a from-scratch implementation and convergence analysis. The benchmark notebooks are 1a (97 spans, 143 KB) and 2a (65 spans, 147 KB); the recent 9c (153 spans) shows the shape this run expects. A reader meeting the curriculum for the first time meets this notebook first, so it sets the standard the rest is judged against.

## Acceptance Criteria

- [x] `notebooks/0a_linear_regression_theory.ipynb` rewritten with at least 100 LaTeX spans and zero emojis, following the 9c structure: H1 title, anchored table of contents, derivation sections each followed by a small verification cell, a from-scratch implementation section, a real-data section, then Conclusion → Key Insights → Further Reading — 23 cells (10 code, 13 markdown), verifier measured 101 spans (>= 100), 0 emoji
- [x] The model and loss derived from first principles: $\hat y = X\beta$, squared-error loss $J(\beta) = \frac{1}{2m}\lVert X\beta - y\rVert^2$, and why squared error rather than absolute error (differentiability, and the Gaussian-noise maximum-likelihood argument stated explicitly) — Section 1 derives both, with a code cell contrasting the smooth $2e$ derivative against absolute error's undefined derivative at $e=0$
- [x] Normal equation derived by setting $\nabla_\beta J = 0$, giving $\hat\beta = (X^\top X)^{-1}X^\top y$, with the invertibility condition stated and what collinearity does to it — Section 2 derives it via full expansion, states the full-column-rank condition, and a code cell constructs a collinear design showing `rank=3 of 4` and a singular $X^\top X$ (`cond ≈ 1.47e16`, determinant ≈ 0) against a full-rank control (`cond ≈ 2.4`)
- [x] Gradient descent derived: the update $\beta \leftarrow \beta - \alpha \nabla_\beta J$, the gradient $\frac{1}{m}X^\top(X\beta - y)$ written out, and a convergence argument — the loss is convex, its Hessian is $\frac{1}{m}X^\top X$, and the step size must satisfy $\alpha < 2/\lambda_{\max}$ — Section 3 derives all of this and a code cell verifies the bound directly: `alpha < bound` converges (loss 1.25 -> 0.002), `alpha > bound` diverges (loss 6.18 -> 2.6e5)
- [x] Feature scaling motivated by the condition number $\kappa(X^\top X)$, with an empirical demonstration that an ill-conditioned design converges slowly and a scaled one does not — Section 4 gives each design its own stability-respecting step size ($1/\lambda_{\max}$) to isolate conditioning from the stability bound in Section 3; measured run: ill-conditioned ($\kappa$=2.95e5) loss barely moves (3.08 -> 3.08 over 200 steps) while standardised ($\kappa$=1.18) converges (0.016 -> 0.0026)
- [x] From-scratch NumPy implementation of both solvers, with a numerical check that gradient descent converges to the normal-equation solution to at least 1e-6, printed in the notebook — Section 5 implements `NormalEquationRegressor`/`GradientDescentRegressor`; Section 6's measured run: `max |normal_eq_beta - gd_beta| = 6.550e-15`, well under 1e-6
- [x] Applied to a real dataset (the California housing set from `sklearn.datasets`, or the London housing CSV already in the repo) with a train/test split and reported RMSE and $R^2$ — used the London housing CSV (per the pre-mortem's stated fallback) rather than fetching California housing over the network, so 0A and 0B are built on identical, already-local data; Section 7 reports train/test RMSE and $R^2$ for both solvers (test $R^2$≈0.5436, matching 0B's OLS result on the same split/features, which is an independent cross-check the two notebooks agree)
- [x] A short section on the bias-variance decomposition of squared error, since later lessons refer back to it — Section 8 derives the three-term decomposition and estimates Bias² and Variance empirically via 200 bootstrap refits
- [x] References: ESL Chapter 3, Andrew Ng's CS229 notes on linear regression and the normal equation — Further Reading cites both, plus Lesson 0B

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/0a_linear_regression_theory.ipynb --type theory --execute
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

- Rewriting destroys explanations worth keeping — read the existing notebook first and carry forward any prose that is already good; this is a rewrite of the mathematics, not a deletion of the pedagogy
- Fetching California housing needs network; if unavailable, use `datasets/London_Housing_Data.csv` and say so

### Weak assumptions

- The reader has met derivatives but not linear algebra notation; introduce $X^\top X$ rather than assuming it — done: Section 1 introduces $X^\top X$ and matrix-calculus identities ($\nabla_\beta(\beta^\top A\beta)=2A\beta$) inline at the point they are first used, rather than assuming prior familiarity

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit a13e48a, worked directly
in-session per the operator's pivot on TASK-SL028 (self-dispatch dropped in
favour of continuing in this session).

### A genuine mid-build defect, found and fixed before closing

The first execution attempt hit a real bug, not a cosmetic one:
`NormalEquationRegressor` originally solved the explicit normal equation
(`np.linalg.solve(X^T X, X^T y)`), and Section 8's bootstrap resampling of
the training design matrix occasionally produced a resampled `House Type`
dummy column that was all-zero (a rare category, e.g. `Duplex`/`Mews`,
absent from that particular bootstrap draw), making `X^T X` exactly
singular and raising `LinAlgError: Singular matrix`. Fixed by switching
`NormalEquationRegressor` to `np.linalg.lstsq` on the design matrix
directly (the Moore-Penrose pseudoinverse solution), which degrades
gracefully to the minimum-norm solution instead of raising — consistent
with, and explicitly cross-referencing, Lesson 0B's own finding that
forming $X^\top X$ explicitly squares the design matrix's condition
number. A second defect (Section 4's original conditioning demo used one
shared step size for both designs, which was stable for the well-scaled
design but far past the ill-conditioned design's own stability bound, so
gradient descent diverged to `NaN` with overflow warnings) was fixed by
giving each design its own stability-respecting step size ($1/\lambda_{\max}$),
which isolates the conditioning effect cleanly and matches the acceptance
criterion's "converges slowly" framing rather than producing an unrelated
divergence.

### Verification command output

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/0a_linear_regression_theory.ipynb --type theory --execute
PASS 0a_linear_regression_theory.ipynb [theory]
verify: 1 passed, 0 failed
```

### JSON report (`reports/verify/0a_linear_regression_theory.json`)

```json
{
  "notebook": "0a_linear_regression_theory.ipynb",
  "type": "theory",
  "metrics": {
    "latex_spans": 101,
    "display_dollar_blocks": 0,
    "code_cells": 10,
    "markdown_cells": 13,
    "bytes": 110495,
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
