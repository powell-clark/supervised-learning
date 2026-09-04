# TASK-SL030: Lesson 0b: Linear regression practical — regularised regression, diagnostics, London housing

## Context

Lesson 0 is the only lesson in the curriculum with a theory notebook and no practical one; every other lesson from 1 to 9 ships an `a`/`b` pair. `datasets/London_Housing_Data.csv` (3,479 rows × 9 features) and `data/df_with_outcode.csv` are already in the repo and are the same data 2b uses, so the reader meets a familiar dataset in a regression setting before meeting it in a tree setting. This notebook is also where regularisation belongs: the roadmap's "Better approach" section puts hyperparameter tuning and model evaluation inside practical notebooks rather than in separate meta-lessons.

## Acceptance Criteria

- [ ] `notebooks/0b_linear_regression_practical.ipynb` created, following the structure of `notebooks/9d_rnn_practical.ipynb`: H1 title `# Lesson 0B: Linear Regression Practical`, anchored table of contents, required-libraries cell, then the sections below, closing with Conclusion → Key Insights → Further Reading
- [ ] Objectives stated mathematically with at least 20 LaTeX spans in total: OLS $\min_\beta \lVert y - X\beta \rVert_2^2$ with the closed form $\hat\beta = (X^\top X)^{-1} X^\top y$; ridge $+\lambda\lVert\beta\rVert_2^2$ with its closed form $(X^\top X + \lambda I)^{-1}X^\top y$; lasso $+\lambda\lVert\beta\rVert_1$; elastic net as the convex combination — including why the L1 ball's corners produce exact zeros while the L2 ball's smoothness does not
- [ ] Data preparation: load the London housing CSV, state and handle missing values, encode the categorical outcode, standardise features (fit the scaler on train only), and split train/test with a fixed seed — the leakage risk of scaling before splitting is stated explicitly
- [ ] `LinearRegression`, `Ridge`, `Lasso` and `ElasticNet` fitted with scikit-learn; regularisation strength selected by `RidgeCV`/`LassoCV` or an explicit `GridSearchCV` over a log-spaced grid with k-fold cross-validation, and the chosen $\lambda$ reported
- [ ] A coefficient-path plot over $\lambda$ for ridge and lasso, showing lasso coefficients reaching exactly zero and ridge coefficients shrinking without doing so
- [ ] Residual diagnostics on the test set: residuals vs fitted, a Q-Q plot, and a comment on heteroscedasticity — each interpreted in one or two sentences, not just plotted
- [ ] Cross-check against Lesson 0a: the scikit-learn OLS coefficients match the normal-equation solution computed with NumPy on the same design matrix to at least 1e-8, and the printed comparison is in the notebook
- [ ] Performance table: train and test RMSE, MAE and $R^2$ for all four models
- [ ] No emojis, no marketing language, no tool tutorial framing
- [ ] References: ESL Chapter 3, scikit-learn linear-model documentation, and Lesson 0a

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

- 0a's from-scratch solution is recoverable for the cross-check; if 0a's implementation is too thin to reuse, recompute the normal equation inline in 0b and note that TASK-SL031 will align them
