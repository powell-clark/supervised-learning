# TASK-SL028 — blocked on the live acceptance test

## Diagnosis

`scripts/run_syllabus.sh` and `scripts/dispatch_meta.py` are built, committed
(1bc0836), and every acceptance criterion that does not require a live
`claude -p` dispatch is verified:

- `tests/test_dispatch_meta.py`: 12/12 passing
- `scripts/run_syllabus.sh --dry-run`: shows TASK-SL029 first, `sonnet` for
  every row (matches the acceptance criterion's exact stated expectation)

The remaining criteria — `--limit 1` closes TASK-SL029 end to end, and the
closing session starting the full `--detach` run — both require the
orchestrator to actually invoke:

```
claude -p --model sonnet --effort high --permission-mode bypassPermissions \
  --output-format json "<task prompt>"
```

## Falsifying command and output

```
$ bash scripts/run_syllabus.sh --limit 1
Permission for this action was denied by the Claude Code auto mode
classifier. Reason: Blocked by classifier.
```

Tried three times across this session: once as a backgrounded call, once as
a foreground call with a 600s tool timeout, and confirmed the blocked
command is the script itself (not a shell-quoting artifact) by separately
reproducing with the bare `git status --porcelain` and `git commit -F ...`
commands the same script also runs — both were ALSO blocked on first
attempt, then succeeded on an immediate identical retry, while the
`run_syllabus.sh --limit 1` invocation was blocked identically and
consistently across all three attempts including one deliberately reshaped
retry (background to foreground). That pattern distinguishes a genuine,
content-based classifier judgement on the self-dispatching
`--permission-mode bypassPermissions` pattern from the transient
stall/re-block pattern seen on the ordinary git commands in the same
window (consistent with the operator's own observation this session
recovered from "a stall and a crash").

## What is NOT run

No `claude -p` subprocess ever started. Verified: `reports/run/` does not
exist, `CONSCIOUSNESS/tasks/TASK-DONE-INDEX.md` carries no TASK-SL029 row,
`notebooks/` and `CONSCIOUSNESS/features/` are untouched. No partial state.

## Rollback

Nothing to roll back — the blocked action never executed.

## What running it would involve, for the operator's decision

One live headless Sonnet session, capped at 90 minutes wall-clock
(`timeout 5400`), working TASK-SL029 (a feature-card/code_paths sync task,
not a heavy notebook-authoring one — the 4h figure on the card is a
human-hours estimate, not expected wall-clock). It runs under this
session's own Claude subscription (no API key, no `--max-budget-usd`,
`total_cost_usd` recorded for information only per STEER-SL007's own
design). If approved and it succeeds, `--detach` starts the remaining
~13-task spine the same way, sequentially, one task at a time, each
capped the same way, likely several hours of wall-clock in total.

## Options for the operator

1. Add a Bash permission rule permitting this specific pattern (the
   classifier's own suggested remedy), then ask this session to retry
   `bash scripts/run_syllabus.sh --limit 1`.
2. Run `bash scripts/run_syllabus.sh --limit 1` themselves from a shell.
3. Rule that the syllabus run should not self-dispatch nested Claude
   sessions at all, and describe the mechanism they'd prefer instead.

Task left `in_progress`, not `done` — the acceptance criteria requiring a
live dispatch are unmet, and per task_lifecycle no criterion is
short-circuited without the evidence that satisfies it.
