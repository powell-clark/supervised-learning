# TASK-SL033: Convert Lesson 5a KNN theory mathematics to LaTeX and re-verify FEAT-SL2

## Context

`notebooks/5a_k_nearest_neighbors_theory.ipynb` is 291 KB with 77 KB of markdown across 44 cells — substantial content — but exactly 2 dollar signs in the whole notebook. Its mathematics is written as plain text and unicode (`✓`, `✗`, `⟺`), so nothing renders as mathematics and the notebook reads as prose about equations rather than equations. FEAT-SL2 (Lesson 5 — K-Nearest Neighbors theory and practice) currently carries `agent-rejected` (REVIEW-CCC049) and is the only rejected feature in the corpus. This is a conversion task, not a rewrite: the content is there, the notation is not.

## Acceptance Criteria

- [ ] `notebooks/5a_k_nearest_neighbors_theory.ipynb` reaches at least 100 LaTeX spans with zero emoji-class characters (the mathematical `⟺` may stay if it is inside LaTeX as `\iff`, but `✓`/`✗` decorations go)
- [ ] Every distance metric expressed in LaTeX: Euclidean $d(x,y) = \sqrt{\sum_i (x_i-y_i)^2}$, Manhattan $\sum_i |x_i - y_i|$, Minkowski $(\sum_i |x_i-y_i|^p)^{1/p}$, and Mahalanobis $\sqrt{(x-y)^\top \Sigma^{-1} (x-y)}$ with the role of $\Sigma^{-1}$ explained
- [ ] The curse of dimensionality stated quantitatively, not just described: the concentration result that the ratio of nearest to farthest distance tends to 1 as $d \to \infty$, with the existing empirical demonstration kept and its axes tied to the formula
- [ ] KD-tree construction and search written with complexity bounds in LaTeX — $O(n \log n)$ build, $O(\log n)$ average query, $O(n)$ worst case — and the pruning condition for a branch stated as an inequality
- [ ] The bias-variance behaviour of $k$ expressed with formulae, not only the existing decision-boundary plots
- [ ] No content is lost: the cell count does not fall, and any prose replaced by a formula keeps its explanatory sentence
- [ ] The notebook executes end to end with stored outputs
- [ ] After conversion, FEAT-SL2 is re-verified: `record-feature-verification-cli FEAT-SL2 --pass` is recorded, and an `append-verdict-cli --target FEAT-SL2 --verdict agent-approved --evidence <HEAD sha>` verdict is written citing the verifier report — superseding REVIEW-CCC049
- [ ] FEAT-SL2's card acceptance criteria are ticked with evidence, and the feature moves to `FEATURE-MAINTAINED-DONE-INDEX.md` with status `maintained`

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py notebooks/5a_k_nearest_neighbors_theory.ipynb --type theory --execute
.venv/bin/python scripts/verify_notebook.py notebooks/5b_knn_practical.ipynb --type practical --execute
```
Both must exit 0 before the FEAT-SL2 verdict is recorded (5b is uplifted by TASK-SL035; if that has not landed yet, record the 5a result and leave the feature verdict to whichever of the two tasks closes second, noting the handover on this card).

## Dispatch

model: sonnet
effort: high
max_turns: 120
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL12
- Features: FEAT-SL9 (and re-verifies FEAT-SL2)
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- A bulk find-and-replace mangles code cells or markdown tables — convert cell by cell, and re-run the verifier's span count after each batch
- The notebook is 291 KB with stored outputs; a careless rewrite drops the outputs and turns a passing notebook into an unexecuted one — re-execute at the end
- REVIEW-CCC049's rejection may cite defects beyond the notation; read it before starting and address what it actually says

### Weak assumptions

- The 2026-07-13 markdown-corruption repair (TASK-SL024) left 5a clean; verify no stripped-newline damage remains before adding to it
