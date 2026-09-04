# TASK-SL039: Write corpus completion report and stamp feature freshness

## Context

This is the last task in the run and the one the operator actually reads. Everything before it produces notebooks and index rows; this produces the single document that says what exists, whether it meets the bar, what was verified and how, and what was deliberately left undone. It also closes the roadmap: every feature stamped fresh, every story fulfilled or explicitly not, so the PGPS state matches the corpus state.

## Acceptance Criteria

- [ ] `CONSCIOUSNESS/artifacts/CORPUS-REPORT.md` written, containing: a one-paragraph statement of what the corpus now is; a table of every notebook with its lesson, type, LaTeX spans, size, execution status and verifier result, generated from `reports/verify/summary.json` rather than typed; the reading order for a newcomer; and a short section on what the run changed versus what it inherited
- [ ] A "Verification" section stating exactly how each claim was checked — the verifier's thresholds, the numerical gradient checks, the library cross-checks — and naming the commands a reader can re-run
- [ ] A "Known gaps and deliberate omissions" section: the unsupervised and reinforcement-learning repos are out of scope (REINFORCEMENT_LEARNING_PLAN.md remains a plan), the X-series is deliberately not restored per the roadmap, and any acceptance criterion that closed as not-applicable during the run with the reason
- [ ] A "Run record" section: which tasks ran, in what order, on which model, total wall-clock, and any task that needed a retry — read from `reports/run/`
- [ ] Every FEAT card has a fresh `last_tested` stamp: `record-feature-verification-cli <FEAT-ID> --pass --notes "corpus sweep <sha>"` for FEAT-SL1 through FEAT-SL9
- [ ] Every feature that has met its acceptance criteria carries an `agent-approved` verdict via `append-verdict-cli` and sits in `FEATURE-MAINTAINED-DONE-INDEX.md` with status `maintained`
- [ ] STORY-SL4, SL5, SL6, SL7, SL8, SL9, SL10, SL11 and SL12 are each moved to `STORY-FULFILLED-REJECTED-INDEX.md` with status `fulfilled`, or left active with a one-line reason recorded on the story card
- [ ] DIRECT-SL1's card and index row are updated: success criteria ticked with evidence, or the remaining scope named (the directive spans three repositories, so it plausibly stays in_progress with supervised-learning complete — say which)
- [ ] `CURRICULUM_ROADMAP.md` updated so its "Current State" and per-lesson status reflect the finished corpus, with the measured benchmark figures corrected
- [ ] PGPS `--headless` reports 52/52 with zero errors, and `/consciousness:pgps` shows no orphaned in_progress work
- [ ] The report's final line states plainly whether the corpus meets the bar the roadmap publishes, with the evidence, and does not overstate — a partial result is reported as N of M

## Verification

```bash
.venv/bin/python scripts/verify_notebook.py --all ; echo "verify exit=$?"
PLUGIN_ROOT=... ; node "$PLUGIN_ROOT/dist/packages/core/pgps/main.js" --headless | grep -A5 "^Validation:"
grep -c "last_tested" CONSCIOUSNESS/features/FEATURE-MAINTAINED-DONE-INDEX.md
```
Paste all three into the closing note, plus the report's final line.

## Dispatch

model: sonnet
effort: high
max_turns: 120
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7
- Blocked by: TASK-SL038 (Regenerate README as the corpus index), TASK-SL029 (Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes)

## Pre-mortem

### Failure modes

- Writing the report from memory of the run rather than from `reports/` — every figure in the table must come from the JSON, or it is an assertion dressed as evidence
- Declaring stories fulfilled whose features are not actually maintained — check the indexes, not the intent
- Claiming the corpus meets the bar when one notebook is short of it; the honest form is "21 of 22 pass; 2c is at 18 spans and is tracked as ..."

### Weak assumptions

- Every story's acceptance criteria are satisfiable by this run; STORY-SL9's card mentions "All six notebooks completely rewritten", which by the end will be true for 9a–9f, but the story also inherits older criteria — read them individually
