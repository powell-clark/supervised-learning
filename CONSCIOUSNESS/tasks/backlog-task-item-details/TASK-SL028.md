# TASK-SL028: Build autonomous syllabus run orchestrator with model-aware dispatch

## Context

The conscious loop claims whatever is next in the spine, in the model of whichever session is running it. The operator's ruling (STEER-SL005) is that theory notebooks and the final review go to Opus while tooling and practical notebooks go to Sonnet, with no human anywhere in the loop. That needs a small deterministic orchestrator that walks the spine, reads each task card's `## Dispatch` block, and runs one headless session per task with the right model and a hard budget cap — then closes features under the agent tier. `claude -p` (Claude Code 2.1.261) supports `--model`, `--effort`, `--permission-mode`, `--max-budget-usd` and `--output-format json`; a trivial headless turn in this repo costs more than $0.05 because the plugin context is large, so caps are per task, not per turn.

## Acceptance Criteria

- [ ] `scripts/dispatch_meta.py <card.md>` prints the card's `## Dispatch` block as JSON (`model`, `effort`, `max_turns`, `reviewer_model`) and exits 2 when the block is absent; unit-tested in `tests/test_dispatch_meta.py`
- [ ] `scripts/run_syllabus.sh` selects the next task as: the first row of the PGPS execution spine's Layer 0 (`node "$PLUGIN_ROOT/dist/packages/core/pgps/main.js" --sequence`) whose card carries a `## Dispatch` block and whose `blocked_by` ids are all in `TASK-DONE-INDEX.md`; tasks without a Dispatch block (TASK-SL017, SL018, SL019, SL023) are skipped and listed once in the log
- [ ] For each selected task it runs, synchronously: `claude -p --model <model> --effort <effort> --max-turns <max_turns> --permission-mode bypassPermissions --output-format json "<prompt>"` where the prompt is read from `scripts/prompts/task.md` with `{TASK_ID}` substituted, and that prompt instructs the session to: claim with `update-task-status-cli --to in_progress`, read the task card and its story card, implement, run the card's `## Verification` commands until they pass, commit and push with `Authored-By: Emmanuel Powell-Clark <emmanuel@powellclark.com>` and no AI attribution, then close via `--to in_review` and `--to done --verdict bypass-approved`, relocating the card to `done-task-item-details/` and correcting the DONE row's `doc`, `expected_duration` and `story_points` columns (powell-clark/consciousness#2229)
- [ ] **This is a subscription, not API billing:** no `--max-budget-usd` anywhere (it caps API spend and is inert here); the bound on a runaway session is `--max_turns` from the card plus the per-task wall-clock cap below. `total_cost_usd` in the JSON result is recorded for information only and never used as a control
- [ ] **Every dispatched session is Sonnet** (operator ruling, STEER-SL007). The orchestrator refuses to start and exits 2 if any card's `## Dispatch` block names a model other than `sonnet`
- [ ] **Host protection (measured 2026-09-05: 16 cores, ~6 GB free of 31 GB, disk 85% full):** strictly one dispatched session at a time — never background a task session, never fan out; before dispatching, require `MemAvailable` ≥ 3 GB and free disk ≥ 10 GB, otherwise wait 120 s and re-check, aborting with exit 4 after ten consecutive refusals; wrap each session in `timeout 5400` so no task can run beyond 90 minutes; and export `OMP_NUM_THREADS=4`, `MKL_NUM_THREADS=4`, `OPENBLAS_NUM_THREADS=4` into every session's environment so a notebook cannot claim all 16 cores
- [ ] After each session it verifies independently: the task id is in `TASK-DONE-INDEX.md`, `git status --porcelain` is clean, and the card's `## Verification` commands exit 0 when re-run; on any failure it re-runs the task once with the failure output appended to the prompt; on a second failure it records the failure in the log, notes it on the card under `## Run log`, and continues with the next task
- [ ] When every task of a feature is in the DONE index, it runs a review session with `--model <reviewer_model>` from `scripts/prompts/review.md`: the reviewer reads the feature card and each task's verifier report, re-runs `scripts/verify_notebook.py` on the feature's `code_paths`, records `append-verdict-cli --target FEAT-ID --verdict agent-approved|agent-rejected --evidence <HEAD sha> --note "<one sentence>"`, and on approval moves the feature to `FEATURE-MAINTAINED-DONE-INDEX.md` with status `maintained` and its card to `maintained-done-feature-item-details/`, then commits and pushes
- [ ] Between tasks it runs the neurologist's self-healing CLI with `--apply --session syllabus-run` and PGPS `--headless`, and aborts the run (exit 3) if PGPS validation reports errors, so a broken index never propagates
- [ ] Flags: `--dry-run` prints the ordered plan (task id, title, model, budget, blocked_by state) and dispatches nothing; `--limit N` stops after N tasks; `--only TASK-ID` runs one task; `--detach` re-executes itself under `setsid nohup` writing to `reports/run/<UTC-timestamp>/run.log` and `reports/run/current.pid`
- [ ] Every session's JSON result (`total_cost_usd`, `num_turns`, `duration_ms`, `is_error`, `result` tail) is saved to `reports/run/<ts>/<TASK-ID>.<attempt>.json`; the run log carries a running cost total and the log is committed at the end of the run
- [ ] The run exits 0 when no dispatchable, unblocked task remains and exits 1 if any task ended in the failed state, printing a final table of task → status → cost
- [ ] `--dry-run` output for the current backlog shows TASK-SL029 (Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes) first, since TASK-SL026–SL028 will be done by then, and shows `sonnet` for every row
- [ ] `--limit 1` real run closes TASK-SL029 end to end (DONE row present, clean tree, verifier green) — this is the orchestrator's own acceptance test, and its cost is recorded in the log
- [ ] On successful `--limit 1`, the closing session starts the full run with `scripts/run_syllabus.sh --detach` and records the pid and log path in this card's `## Run log`

## Verification

```bash
.venv/bin/python -m pytest -q tests/test_dispatch_meta.py
scripts/run_syllabus.sh --dry-run
scripts/run_syllabus.sh --limit 1 ; echo "exit=$?"
cat reports/run/current.pid && tail -5 "$(dirname "$(readlink -f reports/run/current.pid)")/run.log"
```
Paste all outputs into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 100
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7
- Blocked by: TASK-SL027 (Build notebook quality verifier with executable thresholds)

## Pre-mortem

### Failure modes

- `CLAUDE_PLUGIN_ROOT` does not reach subprocesses reliably — resolve the plugin root inside the script exactly as `agents/neurologist.md` documents, never assume the env var
- Two sessions writing the same index concurrently — the orchestrator is strictly sequential; never launch a task session while another is live
- Exhausting host memory and taking the desktop down — the machine had ~6 GB free when this was planned; the memory/disk precheck and the 4-thread cap are load-bearing, not advisory
- A session that "finishes" without closing the task — the post-run check reads the DONE index, not the session's own claim
- `approve/cli.js` cannot run in this install (js-yaml unresolvable) — use `append-verdict-cli.js`, which works

### Weak assumptions

- The spine's Layer 0 is the right claim order; if PGPS `--sequence` output changes shape, fall back to parsing `TASK-BACKLOG-INDEX.md` directly
- Budget caps are generous enough for a full notebook; a budget-exhausted session shows `is_error` or a truncated result and is handled by the retry path, not silently accepted
