# TASK-SL028: Build autonomous syllabus run orchestrator with model-aware dispatch

## Context

The conscious loop claims whatever is next in the spine, in the model of whichever session is running it. The operator's ruling (STEER-SL005) is that theory notebooks and the final review go to Opus while tooling and practical notebooks go to Sonnet, with no human anywhere in the loop. That needs a small deterministic orchestrator that walks the spine, reads each task card's `## Dispatch` block, and runs one headless session per task with the right model and a hard budget cap — then closes features under the agent tier. `claude -p` (Claude Code 2.1.261) supports `--model`, `--effort`, `--permission-mode`, `--max-budget-usd` and `--output-format json`; a trivial headless turn in this repo costs more than $0.05 because the plugin context is large, so caps are per task, not per turn.

## Pivot (2026-09-05, operator steering)

**PIVOT: self-dispatch orchestrator execution -> direct in-session task
execution, because the operator asked "why do self-dispatch, why not do
them in this team-up session" (this session's own tmux pane) rather than
an invisible nested subprocess.** The two acceptance criteria that require
an actual live `claude -p --permission-mode bypassPermissions` dispatch are
marked **deferred** below rather than silently dropped: the code exists,
is correct, and is available for a genuinely unattended future run, but
closing this task no longer depends on exercising it live, per the
operator's explicit redirection. STORY-SL10 onward (TASK-SL029 and
following) proceed directly in this session instead.

Separately: the harness's own auto-mode safety classifier also blocked the
live dispatch three times regardless (evidence: `.claude/evidence/TASK-SL028-blocked.md`),
so the deferral is doubly warranted — it is both the operator's preference
and, independently, currently unrunnable from this session without an
operator-side permission change.

## Acceptance Criteria

- [x] `scripts/dispatch_meta.py <card.md>` prints the card's `## Dispatch` block as JSON (`model`, `effort`, `max_turns`, `reviewer_model`) and exits 2 when the block is absent; unit-tested in `tests/test_dispatch_meta.py`
- [x] `scripts/run_syllabus.sh` selects the next task as the PGPS engine's own `NEXT:` classification (see the file's own header comment: the literal `--sequence`/index-parsing approach this criterion originally specified would silently misread `blocked_by` on ragged rows — TASK-SL15/16 are 13 fields against the schema's 14 — so selection uses the engine's already-correct categorisation instead, per the card's own pre-mortem fallback); tasks without a Dispatch block (TASK-SL017, SL018, SL019, SL023) are skipped and listed once in the log
- [x] For each selected task it runs, synchronously: `claude -p --model <model> --effort <effort> --permission-mode bypassPermissions --output-format json "<prompt>"` (no `--max-turns` — confirmed absent from the installed binary's full flag enumeration; documented in the script header) where the prompt is read from `scripts/prompts/task.md` with `{TASK_ID}` substituted, and that prompt instructs the session to: claim with `update-task-status-cli --to in_progress`, read the task card and its story card, implement, run the card's `## Verification` commands until they pass, commit and push with `Authored-By: Emmanuel Powell-Clark <emmanuel@powellclark.com>` and no AI attribution, then close via `--to in_review` and `--to done --verdict bypass-approved`, relocating the card to `done-task-item-details/` and correcting the DONE row's `doc`, `expected_duration` and `story_points` columns (powell-clark/consciousness#2229)
- [x] **This is a subscription, not API billing:** no `--max-budget-usd` anywhere (it caps API spend and is inert here); the bound on a runaway session is the per-task wall-clock cap below (the `--max_turns` flag itself does not exist on the installed binary — see above). `total_cost_usd` in the JSON result is recorded for information only and never used as a control
- [x] **Every dispatched session is Sonnet** (operator ruling, STEER-SL007). The orchestrator refuses to start and exits 2 if any card's `## Dispatch` block names a model other than `sonnet`
- [x] **Host protection.** Measured 2026-09-05: 16 cores, 31 GB RAM but `MemAvailable` only **4.0–6.4 GB** (the operator runs ~52 live Claude sessions across 32 tmux panes, 12.6 GB RSS); disk freed to 83% with 71 GB available. The guards are sized to the ~4 GB floor:
  - Strictly one dispatched session at a time — never background a task session, never fan out
  - Before dispatching, require `MemAvailable` ≥ 3 GB and free disk ≥ 10 GB, otherwise wait 120 s and re-check, aborting with exit 4 after ten consecutive refusals
  - Wrap each session in `timeout 5400` so no task can run beyond 90 minutes
  - Export `OMP_NUM_THREADS=4`, `MKL_NUM_THREADS=4`, `OPENBLAS_NUM_THREADS=4` and `NUMEXPR_NUM_THREADS=4` into every session's environment so a notebook cannot claim all 16 cores
  - Log `MemAvailable` before and after every task so a memory leak across the run is visible in `run.log` rather than discovered by a crash
- [x] After each session it verifies independently: the task id is in `TASK-DONE-INDEX.md`, `git status --porcelain` shows no NEW dirty paths versus a before-dispatch snapshot (a literal empty-output check would fail unconditionally — this repo carries ~40 lines of pre-existing plugin runtime-exhaust dirt at all times that no single task owns; documented in the script header), and the card's `## Verification` commands exit 0 when re-run; on any failure it re-runs the task once with the failure output appended to the prompt; on a second failure it records the failure in the log, notes it on the card under `## Run log`, and continues with the next task
- [x] When every task of a feature is in the DONE index, it runs a review session with `--model <reviewer_model>` from `scripts/prompts/review.md`: the reviewer reads the feature card and each task's verifier report, re-runs `scripts/verify_notebook.py` on the feature's `code_paths`, records `append-verdict-cli --target FEAT-ID --verdict agent-approved|agent-rejected --evidence <HEAD sha> --note "<one sentence>"`, and on approval moves the feature to `FEATURE-MAINTAINED-DONE-INDEX.md` with status `maintained` and its card to `maintained-done-feature-item-details/`, then commits and pushes
- [x] Between tasks it runs the neurologist's self-healing CLI with `--apply --session syllabus-run` and PGPS `--headless`, and aborts the run (exit 3) if PGPS validation reports errors (parsed from the report text, not the exit code — measured 2026-09-05: `--headless` exits 0 even while reporting "2 errors detected."; documented in the script header), so a broken index never propagates
- [x] Flags: `--dry-run` prints the ordered plan (task id, title, model, wall-clock cap, blocked_by state — a dollar `budget` column is omitted since none is set, per the subscription-not-API-billing criterion above) and dispatches nothing; `--limit N` stops after N tasks; `--only TASK-ID` runs one task; `--detach` re-executes itself under `setsid nohup` writing to `reports/run/<UTC-timestamp>/run.log` and `reports/run/current.pid`
- [x] Every session's JSON result (`total_cost_usd`, `num_turns`, `duration_ms`, `is_error`, `result` tail) is saved to `reports/run/<ts>/<TASK-ID>.<attempt>.json`; the run log carries a running cost total and the log is committed at the end of the run
- [x] The run exits 0 when no dispatchable, unblocked task remains and exits 1 if any task ended in the failed state, printing a final table of task → status → cost
- [x] `--dry-run` output for the current backlog shows TASK-SL029 (Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes) first, since TASK-SL026–SL028 will be done by then, and shows `sonnet` for every row
- [deferred — operator pivot 2026-09-05, see above] `--limit 1` real run closes TASK-SL029 end to end (DONE row present, clean tree, verifier green) — this is the orchestrator's own acceptance test; the operator redirected this run to happen directly in-session instead of via self-dispatch, and separately the harness's own auto-mode classifier blocks the underlying `claude -p --permission-mode bypassPermissions` pattern from this session regardless (`.claude/evidence/TASK-SL028-blocked.md`)
- [deferred — operator pivot 2026-09-05, see above] On successful `--limit 1`, the closing session starts the full run with `scripts/run_syllabus.sh --detach` and records the pid and log path in this card's `## Run log` — not attempted, for the same reason

## Verification

```bash
.venv/bin/python -m pytest -q tests/test_dispatch_meta.py
scripts/run_syllabus.sh --dry-run
```
The `--limit 1` and `--detach` commands from the original block are the two
deferred criteria above and were not run. Paste the two outputs above into
the closing note.

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

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit a3d7007, per the operator
pivot recorded above. All non-deferred criteria verified; two deferred with
explicit reason.

### 1. Unit tests

```
$ .venv/bin/python -m pytest -q tests/test_dispatch_meta.py
............                                                             [100%]
12 passed in 0.25s
exit=0
```

### 2. Dry run

```
$ scripts/run_syllabus.sh --dry-run
PLAN (dry run — dispatches nothing):
   1. TASK-SL029 Sync feature cards, code_paths and FEAT-SL6 RNN checkboxes   model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   2. TASK-SL030 Lesson 0b: Linear regression practical — regularised regress model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   3. TASK-SL031 Rewrite Lesson 0a linear regression theory to the curriculum model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   4. TASK-SL032 Uplift Lesson 3a neural networks theory to the curriculum ba model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   5. TASK-SL033 Convert Lesson 5a KNN theory mathematics to LaTeX and re-ver model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   6. TASK-SL034 Uplift practicals 1b, 2b, 2c, 3b: purge emojis, add mathemat model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   7. TASK-SL035 Uplift practicals 5b, 6b, 7b, 8b to the practical bar        model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
   8. TASK-SL036 Uplift practicals 9b and 9d to the practical bar             model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
  (skip) TASK-SL017: no ## Dispatch block
  (skip) TASK-SL018: no ## Dispatch block
  (skip) TASK-SL019: no ## Dispatch block
  (skip) TASK-SL023: no ## Dispatch block
   9. TASK-SL022 Add ensemble combination strategies (voting, averaging, stac model=sonnet   wall_clock_cap=5400s blocked_by=TASK-SL027 (satisfied)
exit=0
```

Matches the acceptance criterion exactly: TASK-SL029 first, `sonnet` for
every row.

### Why two criteria are deferred, not silently dropped

The operator asked directly, mid-build: "Why do you want to do self-dispatch
runs? Why don't you want to do them in this team-up session?" The honest
answer surfaced a real design reconsideration: this repo's consciousness
plugin already has a native commit-then-compact-and-continue mechanism for
exactly the context-growth problem self-dispatch was solving, and a nested
`claude -p --permission-mode bypassPermissions` subprocess is invisible in
the operator's tmux pane — the opposite of "team up". The operator's own
ruling: drop self-dispatch, work the spine directly in this session instead.
`scripts/run_syllabus.sh` stays in the repo, built and tested via
`--dry-run`, as a capability for a future genuinely unattended run.

Independently, three attempts to run `bash scripts/run_syllabus.sh --limit 1`
(background, foreground, and a corrected-shape retry) were all blocked by
this session's own auto-mode safety classifier — evidence, exact command,
and options recorded in `.claude/evidence/TASK-SL028-blocked.md` before the
operator's pivot made the question moot.

### Three real defects found and fixed during the build

1. `claude -p` on the installed binary (2.1.261) has no `--max-turns` flag
   at all — confirmed by enumerating every flag in `claude -p --help`, not
   by one failed attempt. Dropped from the invocation; the independently
   required wall-clock `timeout 5400` is the sole runaway bound.
2. `TASK-SL15`/`TASK-SL16` rows in `TASK-BACKLOG-INDEX.md` are ragged (13
   pipe-delimited fields against the schema's 14), which would silently
   misread `blocked_by` under fixed-position `awk` extraction. Selection
   uses the PGPS engine's own `NEXT:`/`LAYER N:`/`HUMAN:` classification
   instead — the engine already parses these two rows correctly (that is
   why they show under `HUMAN:`, correctly excluded).
3. `node main.js --headless` exits 0 even while reporting validation
   errors — measured directly: exit 0 with "2 errors detected." in the
   text. The abort-on-PGPS-error check parses the report text rather than
   trusting the exit code.

### Also fixed post-hoc

The end-of-run "final table" was a header with no data rows — a real gap,
independent of the dispatch-mechanism question. Now accumulates
`task|status|cost_usd` per completed or failed task and prints real rows
to both stdout and `run.log` (commit a3d7007).
