# TASK-SL031: Rewrite Lesson 0a linear regression theory to the curriculum bar

## Context

`notebooks/0a_linear_regression_theory.ipynb` is the corpus's opening notebook and its weakest: 20 KB, 20 cells, 18 LaTeX spans and emojis in the markdown, against a published theory bar of 100+ spans with a from-scratch implementation and convergence analysis. The benchmark notebooks are 1a (97 spans, 143 KB) and 2a (65 spans, 147 KB); the recent 9c (153 spans) shows the shape this run expects. A reader meeting the curriculum for the first time meets this notebook first, so it sets the standard the rest is judged against.

## Acceptance Criteria

- [ ] `notebooks/0a_linear_regression_theory.ipynb` rewritten with at least 100 LaTeX spans and zero emojis, following the 9c structure: H1 title, anchored table of contents, derivation sections each followed by a small verification cell, a from-scratch implementation section, a real-data section, then Conclusion → Key Insights → Further Reading
- [ ] The model and loss derived from first principles: $\hat y = X\beta$, squared-error loss $J(\beta) = \frac{1}{2m}\lVert X\beta - y\rVert^2$, and why squared error rather than absolute error (differentiability, and the Gaussian-noise maximum-likelihood argument stated explicitly)
- [ ] Normal equation derived by setting $\nabla_\beta J = 0$, giving $\hat\beta = (X^\top X)^{-1}X^\top y$, with the invertibility condition stated and what collinearity does to it
- [ ] Gradient descent derived: the update $\beta \leftarrow \beta - \alpha \nabla_\beta J$, the gradient $\frac{1}{m}X^\top(X\beta - y)$ written out, and a convergence argument — the loss is convex, its Hessian is $\frac{1}{m}X^\top X$, and the step size must satisfy $\alpha < 2/\lambda_{\max}$
- [ ] Feature scaling motivated by the condition number $\kappa(X^\top X)$, with an empirical demonstration that an ill-conditioned design converges slowly and a scaled one does not
- [ ] From-scratch NumPy implementation of both solvers, with a numerical check that gradient descent converges to the normal-equation solution to at least 1e-6, printed in the notebook
- [ ] Applied to a real dataset (the California housing set from `sklearn.datasets`, or the London housing CSV already in the repo) with a train/test split and reported RMSE and $R^2$
- [ ] A short section on the bias-variance decomposition of squared error, since later lessons refer back to it
- [ ] References: ESL Chapter 3, Andrew Ng's CS229 notes on linear regression and the normal equation

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

- The reader has met derivatives but not linear algebra notation; introduce $X^\top X$ rather than assuming it
