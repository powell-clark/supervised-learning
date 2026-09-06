# STORY-SL16: Consciousness test bed — every task under this directive records whether it ran with the loop on or off

## User Story

I want this maintenance directive to double as a standing consciousness on/off comparison, so the ongoing work itself produces evidence about autonomous operation rather than that evidence having to be manufactured separately.

## Context

Operator, verbatim: "it is also an excellent test bed for consciousness on
and off." Lessons 0-9 (DIRECT-SL1) were themselves built under a mix of
interactive and conscious-loop sessions without that distinction being
tracked as data; this story makes the tracking deliberate for everything
under DIRECT-SL2 going forward, so a later comparison (turnaround time,
correction rate, quality) has something to compare against.

## Acceptance Criteria

- [ ] Every task filed under DIRECT-SL2 states, in its closing evidence, whether the work ran with `/consciousness:on` active or in plain interactive mode for the bulk of its execution
- [ ] The loop-on/loop-off split is queryable across this directive's tasks without re-reading every transcript (a note in the task card or task-events is sufficient; a dedicated log is not required unless the split becomes hard to read otherwise)
- [ ] No task is blocked or gated on which mode it ran under — this is observational, not a constraint on how work gets done
- [ ] Any pattern worth reporting (one mode consistently faster, more accurate, more prone to stalls) is written up as a finding, not left implicit in the data

## References

- .claude/rules/consciousness.md (the loop this story observes)
- CONSCIOUSNESS/stream/commentary.jsonl, task-events.jsonl (existing loop-activity logs this story can read rather than duplicate)
