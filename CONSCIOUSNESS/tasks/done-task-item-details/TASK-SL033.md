# TASK-SL033: Convert Lesson 5a KNN theory mathematics to LaTeX and re-verify FEAT-SL2

## Context

`notebooks/5a_k_nearest_neighbors_theory.ipynb` is 291 KB with 77 KB of markdown across 44 cells — substantial content — but exactly 2 dollar signs in the whole notebook. Its mathematics is written as plain text and unicode (`✓`, `✗`, `⟺`), so nothing renders as mathematics and the notebook reads as prose about equations rather than equations. FEAT-SL2 (Lesson 5 — K-Nearest Neighbors theory and practice) currently carries `agent-rejected` (REVIEW-CCC049) and is the only rejected feature in the corpus. This is a conversion task, not a rewrite: the content is there, the notation is not.

## Acceptance Criteria

- [x] `notebooks/5a_k_nearest_neighbors_theory.ipynb` reaches at least 100 LaTeX spans with zero emoji-class characters (the mathematical `⟺` may stay if it is inside LaTeX as `\iff`, but `✓`/`✗` decorations go) — verifier measured 197 spans (>= 100); all 60 `✓`/`✗` occurrences stripped (cells 24, 30, 41, 43), every retained `⟺` converted to `\iff` inside a LaTeX span
- [x] Every distance metric expressed in LaTeX: Euclidean $d(x,y) = \sqrt{\sum_i (x_i-y_i)^2}$, Manhattan $\sum_i |x_i - y_i|$, Minkowski $(\sum_i |x_i-y_i|^p)^{1/p}$, and Mahalanobis $\sqrt{(x-y)^\top \Sigma^{-1} (x-y)}$ with the role of $\Sigma^{-1}$ explained — Cell 18 ("Mathematical Foundations of Distance") states all four with $\Sigma^{-1}$'s whitening role explained in prose; Cell 40's "Mahalanobis Distance Deep Dive" and Cell 41's "Detailed Reference: Distance Metrics" (Euclidean/Manhattan/Chebyshev/Minkowski/Cosine/Hamming/Correlation) also converted
- [x] The curse of dimensionality stated quantitatively, not just described: the concentration result that the ratio of nearest to farthest distance tends to 1 as $d \to \infty$, with the existing empirical demonstration kept and its axes tied to the formula — Cell 8's header now states $d_{min}/d_{max} \to 1$ and explicitly ties it to Cell 9's unchanged empirical demo, which plots the reciprocal ratio $d_{max}/d_{min} \to \infty$; Cells 26 and 40's duplicate "detailed analysis" sections converted and cross-referenced to the same result
- [x] KD-tree construction and search written with complexity bounds in LaTeX — $O(n \log n)$ build, $O(\log n)$ average query, $O(n)$ worst case — and the pruning condition for a branch stated as an inequality — Cell 10's header states all three bounds and derives the pruning inequality $\lvert x_{axis}-v \rvert < d_k$ directly from Cell 11's (unchanged) code, which implements exactly that condition
- [x] The bias-variance behaviour of $k$ expressed with formulae, not only the existing decision-boundary plots — Cell 14 (previously two lines of prose, no formula anywhere in the notebook) now derives $\mathrm{Var}(\hat f_k(x)) = \sigma^2/k$ and $\mathrm{Bias}(\hat f_k(x)) = \frac{1}{k}\sum_{x_i \in N_k(x)} f(x_i) - f(x)$ from the k-NN averaging estimator
- [x] No content is lost: the cell count does not fall, and any prose replaced by a formula keeps its explanatory sentence — 44 cells before and after (10 code, 34 markdown, unchanged split); every substitution was verified byte-exact against the pre-edit source before being applied, so no cell was touched by accident
- [x] The notebook executes end to end with stored outputs — verify_notebook.py --execute: `executed: true`, `error_outputs: 0`
- [ ] After conversion, FEAT-SL2 is re-verified: `record-feature-verification-cli FEAT-SL2 --pass` is recorded, and an `append-verdict-cli --target FEAT-SL2 --verdict agent-approved --evidence <HEAD sha>` verdict is written citing the verifier report — superseding REVIEW-CCC049 — **[deferred — see Handover below]** `5b_knn_practical.ipynb` measured 0 latex spans (checked directly, `verify_notebook.py notebooks/5b_knn_practical.ipynb --type practical`), still pending TASK-SL035 (Uplift practicals 5b/6b/7b/8b to the practical bar)'s uplift; per this card's own Verification section, the feature verdict goes to whichever of TASK-SL033/TASK-SL035 closes second
- [ ] FEAT-SL2's card acceptance criteria are ticked with evidence, and the feature moves to `FEATURE-MAINTAINED-DONE-INDEX.md` with status `maintained` — **[deferred — see Handover below]**, same reason

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

- The 2026-07-13 markdown-corruption repair (TASK-SL024) left 5a clean; verify no stripped-newline damage remains before adding to it — confirmed clean: max line length across the entire dumped notebook text was 275 characters, no evidence of the stripped-newline pattern (which would show as single lines of thousands of characters)

## Handover: FEAT-SL2 close deferred to TASK-SL035

`notebooks/5a_k_nearest_neighbors_theory.ipynb` now passes
`verify_notebook.py --type theory --execute` (197 spans, 0 emoji). But
`notebooks/5b_knn_practical.ipynb` still measures 0 LaTeX spans, well
below the 20-span practical bar, pending TASK-SL035 (Uplift practicals
5b/6b/7b/8b to the practical bar). Per this card's own Verification
section instruction, whichever of TASK-SL033/TASK-SL035 closes second
should: run both verify commands, and if both pass, do the FEAT-SL2
re-verification and close (`record-feature-verification-cli FEAT-SL2
--pass`, `append-verdict-cli --target FEAT-SL2 --verdict agent-approved
--evidence <HEAD sha>`, tick FEAT-SL2's card, move it to
`FEATURE-MAINTAINED-DONE-INDEX.md`). This closing note is the "noting
the handover on this card" the verification section asked for.

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit a95cb49, worked
directly in-session per the operator's pivot on TASK-SL028 (Build
autonomous syllabus run orchestrator with model-aware dispatch)
(self-dispatch dropped in favour of continuing in this session).

### REVIEW-CCC049 (the pre-mortem's "read before starting" instruction)

REVIEW-CCC049 rejected two defects: markdown-cell newline corruption in
5a/5b, and 5b's cell 17 printing an unconditional checkmark without
running the comparison it claimed. Both were already fixed prior to this
task per FEAT-SL2's own card Notes (verified there, not re-verified
independently here since they are 5b/prior-task concerns outside this
card's scope) — the remaining reason FEAT-SL2 has not closed is purely
5a/5b's LaTeX density, which is exactly what TASK-SL033/TASK-SL035 exist
to fix.

### Verification command output

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/5a_k_nearest_neighbors_theory.ipynb --type theory --execute
PASS 5a_k_nearest_neighbors_theory.ipynb [theory]
verify: 1 passed, 0 failed
```

### JSON report (`reports/verify/5a_k_nearest_neighbors_theory.json`)

```json
{
  "notebook": "5a_k_nearest_neighbors_theory.ipynb",
  "type": "theory",
  "metrics": {
    "latex_spans": 197,
    "display_dollar_blocks": 0,
    "code_cells": 10,
    "markdown_cells": 34,
    "bytes": 302888,
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
