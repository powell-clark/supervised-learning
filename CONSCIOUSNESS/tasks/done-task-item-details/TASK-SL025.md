# TASK-SL025: Remove duplicated inline advisor discipline

## Context

Dispatched from EGLPK TASK-EGLPK331. Delete the repo-local advisor block from CLAUDE.md so this repo inherits the canonical machine-wide model/advisor router and ~/.claude/advisor-lanes only. Preserve all non-advisor repo instructions, verify no duplicate remains, commit and report.

## Acceptance criteria

- [ ] _(to be filled in)_

## Closed 2026-08-05 (eagle-peak cockpit, eglpk-661c8eec, under TASK-EGLPK412)

CLAUDE.md deleted: the whole file was the 19-line duplicated advisor block (byte-identical
across SL/UL/RL; no repo-specific instructions existed in it and no AGENTS.md exists here).
The machine-wide posture router (~/.llm-global/AGENTS.md -> ~/.claude/advisor-lanes/) still
loads for every session in this repo, so advisor guidance is inherited, not lost. Executed
cockpit-side after the owning repo sat dormant three weeks with this task at p1.

## Closed without contract

This task reached a terminal state while its acceptance criteria still read
`_(to be filled in)_`. No criteria have been authored retrospectively: the contract
that would have governed this work was never written, and this marker records that
honestly rather than manufacturing one after the fact.
