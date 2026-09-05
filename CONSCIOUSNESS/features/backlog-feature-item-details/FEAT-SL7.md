---
id: FEAT-SL7
status: backlog
priority: p1
kano: performance
title: Curriculum verification and autonomous run tooling
description: Reproducible execution environment, a mechanical notebook quality verifier that enforces the CURRICULUM_ROADMAP.md checklist, a model-aware orchestrator that dispatches each task to Sonnet or Opus and records agent verdicts, regenerated README as corpus index, and a final corpus completion report — so the curriculum builds and verifies itself with no human gate.
acceptance_criteria:
  - scripts/setup_env.sh builds .venv idempotently from an installed interpreter and requirements.txt, and every notebook import resolves inside it
  - scripts/verify_notebook.py executes a notebook, stores outputs, computes LaTeX-span/emoji/marketing/error metrics, applies theory or practical thresholds, writes reports/verify/<name>.json and exits non-zero on failure
  - scripts/run_syllabus.sh dispatches each unblocked task to the model in its Dispatch block via claude -p with a budget cap, runs the verifier, records verdicts with append-verdict-cli, retries once, and exits when the spine is empty
  - Every FEAT card carries code_paths so record-verification-run resolves features and stamps last_tested
  - README.md regenerated from the notebooks with no emojis and no stale entries
  - CONSCIOUSNESS/artifacts/CORPUS-REPORT.md summarises every notebook's metrics and execution status, and every feature is fresh
stories: [STORY-SL10]
tasks: []
code_paths:
  - scripts/
  - test_notebooks.py
  - README.md
  - requirements.txt
---

# FEAT-SL7: Curriculum verification and autonomous run tooling

## Context

The run described in STEER-SL005 has no human in it. That is only honest if
verification is mechanical and the dispatch is deterministic. This feature is
the tooling layer the rest of the syllabus depends on; its tasks run first in
the execution spine.

## Acceptance Criteria

- [ ] **AC-1** — Environment: `.venv` rebuilt (the checked-in one points at pyenv 3.10.16, which is not installed); `.python-version` updated to the interpreter actually used; `transformers` and `datasets` added for Lesson 9f
- [ ] **AC-2** — Verifier: thresholds encode the roadmap bar exactly (theory 100+ LaTeX spans, practical 20+, zero emojis, zero marketing words, zero error outputs, references section present); `--all` mode; `--record-feature FEAT-x` calls `record-feature-verification-cli`
- [ ] **AC-3** — Orchestrator: model, effort and budget read from each task card's `## Dispatch` block; reviewer session uses the other model; logs to `reports/run/`; `--dry-run` prints the plan without dispatching
- [ ] **AC-4** — README and corpus report generated from live notebook metadata, not hand-written

## Notes

`approve/cli.js` cannot run in the current plugin install (powell-clark/consciousness#2229 — js-yaml unresolvable), so agent verdicts go through `dist/packages/core/fragments/append-verdict-cli.js`, which works.
