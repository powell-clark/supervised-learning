# TASK-SL044: Audit lessons 0, 3-9 against the 1a/1b/2a/2b/2c style bar

## Context

First audit task under STORY-SL13 (Style conformance). Read 1a, 1b, 2a, 2b, 2c as the reference bar (Feynman voice, first-principles derivation, runnable end to end by a reader with A-level-not-further-maths), write the rubric down, then score every other lesson (0a, 0b, 3a, 3b, 4a, 4b, 5a, 5b, 6a, 6b, 7a, 7b, 8a, 8b, 9a-9f) against it. File one named refinement task per lesson that falls short, citing the specific rubric criterion and location. Record loop-on/loop-off per STORY-SL16.

## Acceptance criteria

- [ ] A written rubric exists (in this card's Notes or STORY-SL13.md) naming the concrete, checkable properties that make 1a/1b/2a/2b/2c work — not a restatement of CURRICULUM_ROADMAP.md's mechanical checklist, which already has its own verifier
- [ ] Every one of 0a, 0b, 3a, 3b, 4a, 4b, 5a, 5b, 6a, 6b, 7a, 7b, 8a, 8b, 9a, 9b, 9c, 9d, 9e, 9f is read against the rubric and scored pass or fall-short, with the score and reasoning recorded
- [ ] Every lesson scored fall-short gets its own named follow-up task (title, cell/section reference, which rubric criterion it fails), filed via append-task-cli under STORY-SL13
- [ ] This card's closing note states whether the audit ran with `/consciousness:on` active or in interactive mode (STORY-SL16)
- [ ] No notebook is edited by this task itself — it audits and files; refinement is the follow-up tasks' job

## Dependencies

- Directive: DIRECT-SL2
- Story: STORY-SL13

## Pre-mortem

### Failure modes

- Scoring by vibes rather than the written rubric produces an audit that can't be defended or repeated — write the rubric down and cite it per lesson, not just an overall impression
- 20 lessons is a lot of reading; a shortcut that skims rather than reads risks missing exactly the voice/level problems this task exists to catch — budget for genuinely reading each one
- Filing 15+ follow-up tasks in one pass risks id-broker churn (each append-task-cli call reserves against origin/main) — batch-read first, then file, rather than interleaving

### Weak assumptions

- 1a/1b/2a/2b/2c are uniformly good exemplars throughout — if one of them turns out to fall short of its own standard in places, say so rather than treating the reference set as beyond audit
- "A-level maths, not further maths" has a stable, checkable meaning — if it's ambiguous in practice, state the working definition used rather than leaving it to individual judgement per lesson
