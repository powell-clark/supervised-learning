# TASK-SL029: Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes

## Context

Three linkage gaps found on 2026-09-04. FEAT-SL6's card still shows every RNN theory and practical checkbox unticked although TASK-SL13 and TASK-SL14 closed with verified evidence. FEAT-SL1 to FEAT-SL6 carry no `code_paths:` frontmatter, so `record-verification-run-cli` cannot resolve a notebook diff back to a feature and `last_tested` never populates from a run. FEAT-SL4's card lists TASK-SL7 and TASK-SL8 but not TASK-SL022, which the index already links. This is also the orchestrator's acceptance test (TASK-SL028 `--limit 1`), so it must be small and mechanically checkable.

## Acceptance Criteria

- [x] In `CONSCIOUSNESS/features/active-feature-item-details/FEAT-SL6.md`, every checkbox under "Recurrent Neural Networks (TASK-SL13)" and "RNN Practical (TASK-SL14)" is ticked with a one-clause evidence note drawn from the two done task cards (gradient-check tolerances, adding-problem result, 2.8e-17 NumPy/PyTorch match), except "Bidirectional RNNs explained" and "Text sequence modeling (character or word level)" and "LSTM vs GRU performance comparison", which the shipped notebooks do not cover — leave those unticked and add a `Notes` line saying so, referencing TASK-SL036 (Uplift practicals 9b and 9d to the practical bar) as the place they will be covered
- [x] The card for TASK-SL036 gains those three items as acceptance criteria (so nothing is silently dropped)
- [x] `code_paths:` is added to the frontmatter of FEAT-SL1 through FEAT-SL6 listing each lesson's notebooks (`notebooks/4a_svm_theory.ipynb`, `notebooks/4b_support_vector_machines_practical.ipynb`, and so on; FEAT-SL6 lists 9a–9f)
- [x] FEAT-SL4's frontmatter `tasks:` and body list include TASK-SL022
- [x] PGPS `--headless` reports 52/52 with zero fk-asymmetry warnings after the edits

## Verification

```bash
PLUGIN_ROOT=... # resolve as in agents/neurologist.md
node "$PLUGIN_ROOT/dist/packages/core/pgps/main.js" --headless | grep -A3 "^Validation:"
grep -c "code_paths" CONSCIOUSNESS/features/*/FEAT-SL[1-6].md
```
Paste both outputs into the closing note.

## Dispatch

model: sonnet
effort: medium
max_turns: 40
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- Ticking criteria the notebooks do not actually satisfy — read the two done cards' evidence lines first; anything without evidence stays unticked

### Weak assumptions

- Feature card frontmatter tolerates a `code_paths` list — FEAT-SL7 to FEAT-SL9 already carry one and pass validation

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit bfe8446, worked directly
in-session per the operator's pivot on TASK-SL028 (self-dispatch dropped in
favour of continuing here).

### 1. PGPS headless validation

```
$ node "$PLUGIN_ROOT/dist/packages/core/pgps/main.js" --headless | grep -A3 "^Validation:"
Validation: 52/52 passed. PGPS output is valid.

Warnings: 3, 472 checks passed
  - Fulfilment-ready: STORY-SL8 (Thorough anomaly detection understanding so fraud-detection and outlier-identification models can be built) — all features are ready, story could be fulfilled
  - Warning 16: Priority inversion - active work at p3 while backlog has p1
  - FEAT-SL2 is review-eligible (all tasks done, awaiting review)
```

### 2. code_paths coverage

```
$ grep -c "code_paths" CONSCIOUSNESS/features/*/FEAT-SL[1-6].md
CONSCIOUSNESS/features/maintained-done-feature-item-details/FEAT-SL1.md:1
CONSCIOUSNESS/features/active-feature-item-details/FEAT-SL2.md:1
CONSCIOUSNESS/features/maintained-done-feature-item-details/FEAT-SL3.md:1
CONSCIOUSNESS/features/maintained-done-feature-item-details/FEAT-SL4.md:1
CONSCIOUSNESS/features/maintained-done-feature-item-details/FEAT-SL5.md:1
CONSCIOUSNESS/features/active-feature-item-details/FEAT-SL6.md:2
```

All six carry `code_paths` (FEAT-SL6 shows 2 — the frontmatter field plus a
prose mention in the Notes section explaining the 9e/9f forward reference).

### What was actually found and fixed

- FEAT-SL6: 5 of 6 RNN theory criteria and 4 of 6 RNN practical criteria
  ticked with one-clause evidence drawn from TASK-SL13/TASK-SL14's own
  closing evidence (BPTT cross-check, gradient-decay measurement, GRU
  parameter ratio, forecasting result, NumPy/PyTorch equivalence). The
  three genuinely uncovered items (Bidirectional RNNs, text sequence
  modeling, LSTM-vs-GRU) stay unticked with a Notes line pointing to
  TASK-SL036.
- TASK-SL036's card already carried all three carried-over criteria as its
  own acceptance criteria (Fable's planning session had already anticipated
  this) — verified via diff, no edit needed, no double-booking.
- FEAT-SL4: `tasks:` frontmatter was missing TASK-SL022, which
  FEATURE-MAINTAINED-DONE-INDEX.md already linked — a genuine card/index
  drift, now resolved in the card's favour of the index (the index is what
  the review-gates precept treats as canonical for task linkage).
- code_paths added to all of FEAT-SL1 through FEAT-SL6, forward-referencing
  FEAT-SL6's not-yet-built 9e/9f (TASK-SL15/16 pending), documented as such
  in the card's own Notes rather than left unexplained.
