# TASK-SL020: Add multi-class extension (one-vs-rest, one-vs-one) coverage to 4b SVM practical notebook

## Context

Discovered while closing TASK-SL1 (Lesson 4a: SVM theory). FEAT-SL1's acceptance
criteria require the SVM lesson to explain the multi-class extension (one-vs-rest,
one-vs-one), but `notebooks/4b_support_vector_machines_practical.ipynb` (tracked as
TASK-SL2, currently marked done) contains no such coverage — confirmed by keyword
search (`multi-class`, `multiclass`, `one-vs-rest`, `one-vs-one` all absent).

## Acceptance Criteria

- [x] Add a section to the 4b practical notebook explaining one-vs-rest (OvR) and one-vs-one (OvO) multi-class strategies
- [x] Demonstrate both strategies on a multi-class dataset (e.g. Iris or Digits) with scikit-learn's `SVC(decision_function_shape=...)` or `OneVsRestClassifier`/`OneVsOneClassifier`
- [x] Compare training cost and prediction behaviour between OvR and OvO
- [x] Update FEAT-SL1's acceptance criteria checkbox once verified

## Verification Notes (2026-07-13)

Added a new "Multi-Class Extension" section to `notebooks/4b_support_vector_machines_practical.ipynb`
(3 new cells: markdown explanation, demo, training-cost comparison), inserted before the summary
section (renumbered 9 -> 10). Uses the Digits dataset (10 classes) rather than Iris (3 classes) —
Iris's K=3 makes K and K(K-1)/2 coincidentally equal (both 3), which would have hidden the O(K) vs
O(K(K-1)/2) scaling difference the task exists to demonstrate. With Digits: OvR trains 10 classifiers
(K), OvO trains 45 (K(K-1)/2, 4.5x more), each on ~20% of the training data. Explicitly notes that
scikit-learn's `SVC` already reduces multi-class to one-vs-one internally at the libsvm level
regardless of `decision_function_shape` (verified: `decision_function` shape is (n,10) for `'ovr'`
vs (n,45) for `'ovo'` — the parameter only reshapes output, and OneVsRestClassifier/OneVsOneClassifier
wrappers are used to compare the reductions as genuinely distinct strategies. Also fixed two
pre-existing bugs discovered while re-executing the notebook end-to-end: (1) cell 23 was stored as
a markdown cell containing an unexecuted f-string/`.format()` call instead of a code cell, rendering
literal Python source instead of the formatted summary; converted to a code cell using
`IPython.display.Markdown`. (2) a numpy-array format-string `TypeError` in the preprocessing cell
(`f"{array:.6f}"` is invalid on an array) blocking execution; fixed with `np.array2string`. Full
notebook (27 cells) executes end-to-end with zero error outputs.

## References

- FEAT-SL1 (Lesson 4 — Support Vector Machines theory and practice)
- notebooks/4b_support_vector_machines_practical.ipynb
