# TASK-SL020: Add multi-class extension (one-vs-rest, one-vs-one) coverage to 4b SVM practical notebook

## Context

Discovered while closing TASK-SL1 (Lesson 4a: SVM theory). FEAT-SL1's acceptance
criteria require the SVM lesson to explain the multi-class extension (one-vs-rest,
one-vs-one), but `notebooks/4b_support_vector_machines_practical.ipynb` (tracked as
TASK-SL2, currently marked done) contains no such coverage — confirmed by keyword
search (`multi-class`, `multiclass`, `one-vs-rest`, `one-vs-one` all absent).

## Acceptance Criteria

- [ ] Add a section to the 4b practical notebook explaining one-vs-rest (OvR) and one-vs-one (OvO) multi-class strategies
- [ ] Demonstrate both strategies on a multi-class dataset (e.g. Iris or Digits) with scikit-learn's `SVC(decision_function_shape=...)` or `OneVsRestClassifier`/`OneVsOneClassifier`
- [ ] Compare training cost and prediction behaviour between OvR and OvO
- [ ] Update FEAT-SL1's acceptance criteria checkbox once verified

## References

- FEAT-SL1 (Lesson 4 — Support Vector Machines theory and practice)
- notebooks/4b_support_vector_machines_practical.ipynb
