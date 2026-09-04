# TASK-SL029: Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes

## Context

Three linkage gaps found on 2026-09-04. FEAT-SL6's card still shows every RNN theory and practical checkbox unticked although TASK-SL13 and TASK-SL14 closed with verified evidence. FEAT-SL1 to FEAT-SL6 carry no `code_paths:` frontmatter, so `record-verification-run-cli` cannot resolve a notebook diff back to a feature and `last_tested` never populates from a run. FEAT-SL4's card lists TASK-SL7 and TASK-SL8 but not TASK-SL022, which the index already links. This is also the orchestrator's acceptance test (TASK-SL028 `--limit 1`), so it must be small and mechanically checkable.

## Acceptance Criteria

- [ ] In `CONSCIOUSNESS/features/active-feature-item-details/FEAT-SL6.md`, every checkbox under "Recurrent Neural Networks (TASK-SL13)" and "RNN Practical (TASK-SL14)" is ticked with a one-clause evidence note drawn from the two done task cards (gradient-check tolerances, adding-problem result, 2.8e-17 NumPy/PyTorch match), except "Bidirectional RNNs explained" and "Text sequence modeling (character or word level)" and "LSTM vs GRU performance comparison", which the shipped notebooks do not cover — leave those unticked and add a `Notes` line saying so, referencing TASK-SL036 (Uplift practicals 9b and 9d to the practical bar) as the place they will be covered
- [ ] The card for TASK-SL036 gains those three items as acceptance criteria (so nothing is silently dropped)
- [ ] `code_paths:` is added to the frontmatter of FEAT-SL1 through FEAT-SL6 listing each lesson's notebooks (`notebooks/4a_svm_theory.ipynb`, `notebooks/4b_support_vector_machines_practical.ipynb`, and so on; FEAT-SL6 lists 9a–9f)
- [ ] FEAT-SL4's frontmatter `tasks:` and body list include TASK-SL022
- [ ] PGPS `--headless` reports 52/52 with zero fk-asymmetry warnings after the edits

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
