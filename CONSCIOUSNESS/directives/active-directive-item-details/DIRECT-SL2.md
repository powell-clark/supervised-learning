# DIRECT-SL2 — Maintain the curriculum as a living Feynman-style corpus

**Status:** in_progress
**Priority:** p2
**Expected:** ongoing — no closing date, this directive does not complete
**Filed from:** operator charge 2026-09-06 14:48 bst, relayed by eagle-peak kernel (MSG-EGLPK005)

---

## Vision

DIRECT-SL1's scope (Lessons 0-9, a university-grade supervised learning
curriculum) is content-complete and verified end to end (TASK-SL037). That
closes DIRECT-SL1's build phase; it does not close the project. Operator,
verbatim: "make me a nice portfolio piece that later on I can use as my
syllabus to learn and update over time — the corpus is always updating
itself — it is also an excellent test bed for consciousness on and off, and
it will forever need to be maintained." This directive is the standing home
for that ongoing maintenance — a separate, permanent directive rather than a
scope creep onto DIRECT-SL1, because DIRECT-SL1 is allowed to actually
finish.

## Scope

Four maintenance dimensions, one story each:

- **Style conformance** (STORY-SL13) — every lesson held against the
  operator's own reference notebooks (1a, 1b, 2a, 2b, 2c) for voice, level,
  and runnability; lessons that fall short get a named refinement task
- **Currency** (STORY-SL14) — a bounded, repeatable refresh cadence so
  library versions, datasets, and the execution sweep do not silently rot
- **Lockstep** (STORY-SL15) — this repo and its three siblings
  (unsupervised-learning, reinforcement-learning, deep-learning) converge on
  one README shape and one status line, measured, not assumed
- **Consciousness test bed** (STORY-SL16) — every task filed under this
  directive records whether it ran with the conscious loop on or off, so the
  maintenance cadence itself is a standing on/off comparison

## Success criteria

- Every lesson in the corpus is auditable against a written style bar, not
  tribal knowledge — the audit and its refinement tasks are the evidence
- A refresh runs on a stated cadence and each run's outcome (pass, fixed,
  filed) is recorded, not silently absorbed
- README shape and status line match across all four ML repos, verified by
  diff, not by eye
- Every task under this directive states loop-on or loop-off in its closing
  evidence

## Dependencies

- DIRECT-SL1 (ML/AI education — Andrew Ng Machine Learning Course and foundations) — this directive begins only once DIRECT-SL1's content is built and verified; it starts from TASK-SL037's closing state
