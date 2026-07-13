# TASK-SL023: getFeatureKano() only reads FEATURE-ACTIVE-INDEX.md, causing review-gate kano-tier resolution to silently fall back to human gate when a feature's row is removed from active before its verdict is recorded

> **Needs review:** the agent created this task during real-time validation and is uncertain about scope or priority. Operator should review and re-tier as appropriate.


## Context

Auto-created from /consciousness:issue (issue:ZOk0wNucoIQ94BGSzzSe9).

Report context:
Bug found in packages/core/review/readiness.js:getFeatureKano(). It only reads CONSCIOUSNESS/features/FEATURE-ACTIVE-INDEX.md to resolve a feature's kano tier. resolveGateConfig (reviews/gates.js) uses this to pick the kano_overrides tier (e.g. performance -> requires: agent) vs the base feature default (requires: human, gate: hard). If a feature's row is removed from FEATURE-ACTIVE-INDEX.md before its review verdict is recorded -- which naturally happens when closing a feature, since the row moves out of active as part of the maintained/done transition -- the kano lookup returns null and resolveGateConfig silently falls back to the human-gated default, even for a performance-kano feature that should only need one agent-tier review.

Reproduced on FEAT-SL4 (supervised-learning repo): after removing its row from FEATURE-ACTIVE-INDEX.md and recording an agent-approved review, 'node approve/cli.js FEAT-SL4 --machine-reviewed=1' reported 'its per-entity gate requires a human verdict -- not auto-transitioning to done' despite FEAT-SL4 being kano: performance (agent-tier per DEFAULT_GATES). Restoring the row in FEATURE-ACTIVE-INDEX.md, then re-running the same command, correctly resolved the agent tier and the checkReviewGates hook then permitted the write to FEATURE-MAINTAINED-DONE-INDEX.md.

Workaround used: temporarily restore the feature's row in FEATURE-ACTIVE-INDEX.md before recording the review verdict, run the transition, then remove it.

Suggested fix: getFeatureKano should fall back to reading the feature's own detail-card frontmatter (the kano: field, which is always present per feature card schema) when the ID is not found in FEATURE-ACTIVE-INDEX.md, rather than only checking the one index file. This would make the kano lookup robust to whichever index the feature currently lives in during a transition.

## Acceptance criteria

- [ ] _(to be filled in)_
