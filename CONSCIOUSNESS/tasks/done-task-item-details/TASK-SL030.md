# TASK-SL030: Lesson 0b: Linear regression practical — regularised regression, diagnostics, London housing

## Context

Lesson 0 is the only lesson in the curriculum with a theory notebook and no practical one; every other lesson from 1 to 9 ships an `a`/`b` pair. `datasets/London_Housing_Data.csv` (3,479 rows × 9 features) and `data/df_with_outcode.csv` are already in the repo and are the same data 2b uses, so the reader meets a familiar dataset in a regression setting before meeting it in a tree setting. This notebook is also where regularisation belongs: the roadmap's "Better approach" section puts hyperparameter tuning and model evaluation inside practical notebooks rather than in separate meta-lessons.

## Acceptance Criteria

- [x] `notebooks/0b_linear_regression_practical.ipynb` created, following the structure of `notebooks/9d_rnn_practical.ipynb`: H1 title `# Lesson 0B: Linear Regression Practical`, anchored table of contents, required-libraries cell, then the sections below, closing with Conclusion → Key Insights → Further Reading — 30 cells (11 code, 19 markdown), title cell verified by `has_title`, TOC anchors match the seven numbered `##` sections plus Conclusion
- [x] Objectives stated mathematically with at least 20 LaTeX spans in total: OLS $\min_\beta \lVert y - X\beta \rVert_2^2$ with the closed form $\hat\beta = (X^\top X)^{-1} X^\top y$; ridge $+\lambda\lVert\beta\rVert_2^2$ with its closed form $(X^\top X + \lambda I)^{-1}X^\top y$; lasso $+\lambda\lVert\beta\rVert_1$; elastic net as the convex combination — including why the L1 ball's corners produce exact zeros while the L2 ball's smoothness does not — Section 1 covers all four objectives/closed forms plus the L1-corner/L2-ball geometric argument; verifier measured 48 total LaTeX spans (>= 20)
- [x] Data preparation: load the London housing CSV, state and handle missing values, encode the categorical outcode, standardise features (fit the scaler on train only), and split train/test with a fixed seed — the leakage risk of scaling before splitting is stated explicitly — Section 2 loads `data/df_with_outcode.csv`, states and handles missing values (drops `Location`/`City/County`/`Postal Code`, confirms zero missing in the four modelling columns), smoothed-target-encodes the 154-value `Outcode` fit on train only, standardises continuous features fit on train only, splits with `random_state=42`, and states the leakage risk explicitly before the split
- [x] `LinearRegression`, `Ridge`, `Lasso` and `ElasticNet` fitted with scikit-learn; regularisation strength selected by `RidgeCV`/`LassoCV` or an explicit `GridSearchCV` over a log-spaced grid with k-fold cross-validation, and the chosen $\lambda$ reported — Section 3 fits all four via `RidgeCV`/`LassoCV`/`ElasticNetCV` over `np.logspace(-3, 3, 50)` with 5-fold `KFold`; printed run: `ridge lambda*=0.28118`, `lasso lambda*=6.25055`, `elastic lambda*=0.00133, l1_ratio*=0.90`
- [x] A coefficient-path plot over $\lambda$ for ridge and lasso, showing lasso coefficients reaching exactly zero and ridge coefficients shrinking without doing so — Section 4 plots both paths over `np.logspace(-2, 4, 60)`; printed run showed lasso coefficients hitting exact `0.0` at the largest tested $\lambda$ and zero ridge coefficients doing so
- [x] Residual diagnostics on the test set: residuals vs fitted, a Q-Q plot, and a comment on heteroscedasticity — each interpreted in one or two sentences, not just plotted — Section 5 plots both on the OLS test-set residuals and interprets the fan-shaped spread (heteroscedasticity) and the Q-Q tail bow (skew) in two sentences each
- [x] Cross-check against Lesson 0a: the scikit-learn OLS coefficients match the normal-equation solution computed with NumPy on the same design matrix to at least 1e-8, and the printed comparison is in the notebook — Section 6 solves the centred normal equation via `np.linalg.lstsq` (explicit $X_c^\top X_c$ inversion alone measured 1.68e-8, over budget, because forming it squares the condition number; documented in the notebook and fixed by not forming it); measured run: `max |normal-equation beta - sklearn OLS beta| = 0.000e+00`, well under 1e-8
- [x] Performance table: train and test RMSE, MAE and $R^2$ for all four models — Section 7 builds a `pandas.DataFrame` with train/test RMSE, MAE, $R^2$ for all four models (test $R^2$ range 0.5436–0.5436, train 0.6139 — regularisation makes little difference on this feature set, stated in the Conclusion)
- [x] No emojis, no marketing language, no tool tutorial framing — verifier measured `emoji_count: 0`, `marketing_hits: 0`
- [x] References: ESL Chapter 3, scikit-learn linear-model documentation, and Lesson 0a — Further Reading cites all three

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/0b_linear_regression_practical.ipynb --type practical --execute
```
Must exit 0. Paste the command output and the JSON report into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 120
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL11
- Features: FEAT-SL8
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- The London housing CSV has missing values and a categorical outcode; a naive `read_csv` then `fit` will throw — inspect the frame first and state the cleaning decisions in markdown
- Lasso on unstandardised features penalises large-scale columns unfairly and the coefficient path becomes meaningless — standardise, and say why in the notebook

### Weak assumptions

- 0a's from-scratch solution is recoverable for the cross-check; if 0a's implementation is too thin to reuse, recompute the normal equation inline in 0b and note that TASK-SL031 will align them — assumption resolved as predicted: 0a is itself slated for a full rewrite under TASK-SL031, so 0b recomputes the normal equation inline (Section 6) rather than depending on 0a's current code, with that alignment plan noted directly in the notebook

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit c0ca84f, worked directly
in-session per the operator's pivot on TASK-SL028 (self-dispatch dropped in
favour of continuing in this session).

### Design decisions worth recording

- **Data source**: used `data/df_with_outcode.csv` (already has `Outcode`
  extracted, already drops `No. of Bathrooms`/`No. of Receptions`) loaded
  locally, rather than mirroring `2b_decision_trees_practical.ipynb`'s
  `!wget` GitHub-fetch pattern — no network dependency for a local dataset
  already in the repo.
- **Outcode encoding**: `Outcode` has 154 unique values. One-hot encoding
  all of them would add 150+ sparse columns and, combined with the
  intercept, would reintroduce dummy-variable-trap collinearity. Used
  smoothed target (mean) encoding instead, fit on train only, with unseen
  test-set outcodes falling back to the training global mean.
- **Normal-equation numerical stability (a genuine finding, not a
  shortcut)**: forming $X_c^\top X_c$ explicitly and inverting it gave
  `max_abs_diff = 1.68e-8` — over the 1e-8 bar this criterion needs,
  because explicit normal-equation formation squares the design matrix's
  condition number ($\kappa \approx 7234$ here). Solving the same centred
  system via `np.linalg.lstsq` (SVD-based, no squared conditioning, the
  same algorithm scikit-learn's own solver uses internally) gave an exact
  `0.0` difference. This is documented in the notebook itself as a real
  numerical-linear-algebra lesson rather than hidden.

### 1. Verification command output

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/0b_linear_regression_practical.ipynb --type practical --execute
PASS 0b_linear_regression_practical.ipynb [practical]
verify: 1 passed, 0 failed
```

### 2. JSON report (`reports/verify/0b_linear_regression_practical.json`)

```json
{
  "notebook": "0b_linear_regression_practical.ipynb",
  "type": "practical",
  "metrics": {
    "latex_spans": 48,
    "display_dollar_blocks": 0,
    "code_cells": 11,
    "markdown_cells": 19,
    "bytes": 253312,
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

### 3. Dispatch block note

`max_turns: 120` in the Dispatch block above is unusable: TASK-SL028's
falsification work established that `claude -p` (Claude Code 2.1.261) has
no `--max-turns` flag at all (confirmed by full `claude -p --help`
enumeration). The operator's TASK-SL028 pivot also dropped self-dispatch
entirely in favour of working the syllabus spine directly in this session,
so the Dispatch block's `model`/`effort`/`reviewer_model` fields were not
invoked as a `claude -p` call either — noted here rather than silently
ignored.
