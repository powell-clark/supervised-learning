# TASK-SL024: Fix KNN retrieval benchmark methodology and complete FEAT-SL2 verification

## Context

Discovered while checking FEAT-SL2 (Lesson 5 — K-Nearest Neighbors) for promotion to
maintained: its acceptance criteria checkboxes were never updated despite TASK-SL3
(theory) and TASK-SL4 (practical) both being marked done. Verifying the actual
notebooks against the checklist surfaced two real defects in
`notebooks/5b_knn_practical.ipynb`:

1. `benchmark_knn_methods()` times `.fit()` calls in a loop over queries, but never
   calls `.kneighbors()` or `.predict()` — it measures repeated fitting cost, not
   query/retrieval cost, so its printed "Speedup" numbers do not measure what the
   cell claims to measure (KD-tree vs brute-force retrieval performance).
2. The benchmark omits `ball_tree` entirely, though FEAT-SL2's acceptance criteria
   require a three-way comparison (KD-tree vs brute force vs ball-tree).
3. The benchmark cell (and possibly others) has no saved outputs, suggesting the
   notebook has not been executed end-to-end and verified since these tasks were
   marked done.

## Acceptance Criteria

- [x] Fix `benchmark_knn_methods()` to time actual nearest-neighbor query/retrieval (`.kneighbors()` or `.predict()` on the query points), not repeated `.fit()` calls
- [x] Add `ball_tree` as a third algorithm in the benchmark comparison alongside brute force and KD-tree
- [x] Execute both `5a_k_nearest_neighbors_theory.ipynb` and `5b_knn_practical.ipynb` end-to-end in a disposable venv and confirm zero error outputs
- [x] Update FEAT-SL2's acceptance criteria checkboxes to reflect verified reality
- [x] Dispatch an independent review agent (performance kano, agent-tier gate) before promoting FEAT-SL2 to maintained

## Verification Notes (2026-07-13)

Fixed the benchmark to fit each algorithm once, then time `.kneighbors()` over all
query points (steady-state retrieval cost, with a one-query warm-up to exclude
one-time import/compilation overhead), and added `ball_tree` as a third comparison
algorithm. Re-execution surfaced timing that is genuinely noisy (system/joblib
threading dependent) run to run — the accompanying markdown note was written to be
robust to that variance rather than asserting a specific winner.

Re-executing `5a_k_nearest_neighbors_theory.ipynb` end-to-end (never previously
verified — all cells had empty saved outputs) surfaced three further genuine,
pre-existing defects, all fixed:
1. All 10 code cells had their `source` stored as a list of lines with no `\n`
   terminators, so `''.join(source)` (what nbconvert/nbformat actually executes)
   collapsed each cell into one unparseable line — a hard syntax error on every
   cell. Fixed by rejoining with `\n` and re-splitting via `splitlines(keepends=True)`.
2. The from-scratch `KDTree.__init__` referenced `self.n_features` inside `_build()`
   before assigning it (assignment came after the `_build()` call that needed it) —
   `AttributeError` on construction. Fixed by moving the assignment first.
3. `KDTree._build()` never excluded the chosen median point from its own left/right
   split — the median's own axis value trivially satisfies the `>=` right-branch
   condition, so it recursed into the same node forever (`RecursionError`). Fixed by
   excluding the median index via `np.delete` before computing the child splits.
   Verified the corrected KDTree's 5-nearest-neighbor query result matches an
   independent brute-force NumPy computation exactly (same points, same distances,
   same order).

Both notebooks (44 + 55 cells) execute end-to-end with zero error outputs.

## References

- FEAT-SL2 (Lesson 5 — K-Nearest Neighbors theory and practice)
- notebooks/5a_k_nearest_neighbors_theory.ipynb
- notebooks/5b_knn_practical.ipynb
