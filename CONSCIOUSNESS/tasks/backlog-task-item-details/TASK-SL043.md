# TASK-SL043: Sync .gitignore stream-exhaust patterns with eglpk601 distribution

## Context

2026-09-05: found CONSCIOUSNESS/stream/active-sessions.json, sessions.jsonl, sessions-history.json, cursors/, evaluations/, daily.jsonl, command-usage.jsonl, hooks.jsonl, framing-checks.jsonl, protect-events.jsonl, subagent-spawns.jsonl, and CONSCIOUSNESS/pgps-snapshots/ all untracked and un-ignored, tripping the Stop hook's uncommitted-file safety threshold. Added a local-additions block to .gitignore as a stopgap (commit follows); the distributed block from eagle-peak TASK-EGLPK601 (2026-08-05) is stale relative to what the plugin now writes and still names the pre-migration CONSCIOUSNESS/active-sessions.json root path instead of stream/active-sessions.json. Root fix belongs in the eglpk601 distribution, not a per-repo patch.

## Acceptance criteria

- [ ] _(to be filled in)_

## Dependencies

- _(to be filled in)_

## Pre-mortem

### Failure modes

- _(to be filled in)_

### Weak assumptions

- _(to be filled in)_
