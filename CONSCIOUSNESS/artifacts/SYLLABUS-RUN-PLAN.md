# Autonomous syllabus run — plan

Authored 2026-09-05 by the planning session (Fable 5.1, then Opus 5) under operator
rulings STEER-SL005, STEER-SL006 and STEER-SL007. Every dispatched session is
Sonnet. No human gate exists anywhere in this run.

## What the operator gets at the end

A finished, executed corpus: 24 notebooks (lessons 0–9, theory and practical
paired throughout), every one meeting the bar CURRICULUM_ROADMAP.md publishes,
every one executed with stored outputs, indexed by a generated README, and
summarised in `CONSCIOUSNESS/artifacts/CORPUS-REPORT.md`. The operator reads the
report and the notebooks; nothing waits on them.

## Why the run needs tooling before it needs content

Three of the twenty-two existing notebooks claim in their feature cards to be
verified. The corpus-wide measurement taken on 2026-09-04 disagrees: 13 of 22
notebooks miss the roadmap's own checklist on LaTeX density or emoji presence,
and 17 of 22 store no executed outputs. "Verified" has meant "a session said
so". So the first three tasks build an environment, a verifier that turns the
checklist into an exit code, and an orchestrator that dispatches and closes
work against that exit code. Every content task afterwards closes on the
verifier, not on an assertion.

## The spine

Fourteen new tasks plus three inherited ones, in dependency order. Layer 0 is
whatever is unblocked; the orchestrator walks it one task at a time.

| # | Task | What it produces | Model |
|---|---|---|---|
| 1 | TASK-SL026 | `scripts/setup_env.sh`, a working `.venv` | sonnet |
| 2 | TASK-SL027 | `scripts/verify_notebook.py` — the acceptance gate | sonnet |
| 3 | TASK-SL028 | `scripts/run_syllabus.sh` — the orchestrator | sonnet |
| 4 | TASK-SL029 | Feature-card linkage, `code_paths`, FEAT-SL6 checkboxes | sonnet |
| 5 | TASK-SL031 | Lesson 0a rewritten to the theory bar | sonnet |
| 6 | TASK-SL030 | Lesson 0b — the missing practical | sonnet |
| 7 | TASK-SL032 | Lesson 3a uplifted to the theory bar | sonnet |
| 8 | TASK-SL033 | Lesson 5a converted to LaTeX; FEAT-SL2 re-verified | sonnet |
| 9 | TASK-SL034 | Practicals 1b, 2b, 2c, 3b uplifted | sonnet |
| 10 | TASK-SL035 | Practicals 5b, 6b, 7b, 8b uplifted | sonnet |
| 11 | TASK-SL022 | Stacking added to Lesson 7 (inherited) | sonnet |
| 12 | TASK-SL15 | Lesson 9e — Transformer theory (inherited) | sonnet |
| 13 | TASK-SL16 | Lesson 9f — Transformer practical (inherited) | sonnet |
| 14 | TASK-SL036 | Practicals 9b, 9d uplifted; FEAT-SL6 completed | sonnet |
| 15 | TASK-SL037 | Every notebook executed, outputs stored | sonnet |
| 16 | TASK-SL038 | README regenerated as the corpus index | sonnet |
| 17 | TASK-SL039 | Corpus report; features stamped; stories fulfilled | sonnet |

Tasks 5–14 are mutually independent once the verifier exists — they are ordered
by value, not necessity, and the orchestrator may take them in any spine order.
TASK-SL037 blocks on all of them. TASK-SL017, SL018, SL019 and SL023 carry no
`## Dispatch` block and are deliberately skipped: they are consciousness-plugin
observations, not curriculum work.

## How a task closes

Each card carries a `## Verification` block naming the exact commands and a
`## Dispatch` block naming model, effort, turn cap and reviewer model. The
dispatched session claims the task, implements it, runs the verification
commands until they exit 0, commits and pushes, then closes through
`update-task-status-cli` (`in_progress` → `in_review` → `done` with a
`bypass-approved` verdict). The orchestrator then re-runs the verification
commands itself; a session's own claim of success is never the evidence.

When every task of a feature is done, a separate Sonnet reviewer session reads
the feature card and the verifier reports, re-runs the checks, and records
`agent-approved` or `agent-rejected` with `append-verdict-cli`. Features resolve
to the **agent** tier (config.json `review_gates.entity_overrides`), so approval
closes them without the operator.

## Billing and models

This is a **subscription**, not API billing. `--max-budget-usd` is an API cap and
is inert here; the bound on a runaway session is `--max-turns` from the card plus
a 90-minute wall-clock cap per task. `total_cost_usd` from each session's JSON
result is logged for information only and never used as a control.

Every dispatched session is Sonnet. The orchestrator refuses to start if any card
names another model. Planning and this document are Opus; Opus dispatches
nothing.

## Host protection

Measured on this host, 2026-09-05: 16 cores, 31 GB RAM with ~6 GB available, disk
85% full, 15-minute load average 10.4. The run is capable of taking the machine
down if it executes deep-learning notebooks without limits, so three guards are
load-bearing rather than advisory:

- **Sequential only.** One dispatched session at a time; no fan-out, no
  backgrounded task sessions. Per-task wall clock capped at 90 minutes.
- **Memory and disk precheck.** Before dispatching and before every notebook
  execution: `MemAvailable` ≥ 3 GB and ≥ 10 GB free disk, otherwise wait and
  re-check, aborting after ten refusals. The kernel runs under an address-space
  rlimit so a runaway allocation raises `MemoryError` instead of inviting the OOM
  killer.
- **Thread caps.** `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS`
  and `NUMEXPR_NUM_THREADS` pinned to 4 of the 16 cores in every session and
  every kernel, so torch cannot claim the machine.

The heaviest executions are 9b (CIFAR-10 fetch plus a ResNet-18 fine-tune) and
9f (a small transformer fine-tune). Both keep the small subsets already in use;
neither is to be enlarged.

## Known plugin defects this run works around

Filed as powell-clark/consciousness#2229:

- `update-task-status-cli --to done` writes the DONE row with `story_points` in
  the `expected_duration` column, drops the duration, and leaves the `doc` path
  pointing at `active-task-item-details/`. Every dispatched session corrects the
  row it writes; the neurologist's `misplaced-cards` healer relocates the card.
- The cached plugin install has no `node_modules`, so any CLI importing
  `review-gates-config.js` — notably `review/approve/cli.js` — dies with
  `ERR_MODULE_NOT_FOUND: js-yaml`. Verdicts therefore go through
  `fragments/append-verdict-cli.js`, which works.

## Starting the run

From a fresh session in this repository:

```bash
/consciousness:on
```

then let the loop take TASK-SL026. Once TASK-SL028 has landed, the orchestrator
takes over and the loop is no longer needed:

```bash
scripts/run_syllabus.sh --dry-run     # inspect the plan
scripts/run_syllabus.sh --detach      # run it unattended
tail -f reports/run/current/run.log   # watch
```

## Stopping it

`scripts/run_syllabus.sh` writes its pid to `reports/run/current.pid`; killing
that pid stops the run between tasks, never mid-commit. Every completed task is
already committed and pushed, so a stopped run resumes by re-running the same
command.
