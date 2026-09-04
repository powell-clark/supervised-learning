---
id: FEAT-SL9
status: backlog
priority: p1
kano: performance
title: Lessons 0-9 quality uplift to the curriculum bar
description: Bring every existing notebook to the CURRICULUM_ROADMAP.md bar — theory notebooks 0a, 3a and 5a rewritten or converted to 100+ LaTeX spans with numerically-checked from-scratch implementations; every practical notebook to 20+ LaTeX spans with zero emojis or marketing language; every notebook executed end to end with outputs stored — so the corpus reads uniformly from Lesson 0 to Lesson 9.
acceptance_criteria:
  - 0a, 3a and 5a each reach 100+ LaTeX spans, zero emojis, and include a numerically-checked from-scratch implementation
  - 1b, 2b, 2c, 3b, 5b, 6b, 7b, 8b, 9b and 9d each reach 20+ LaTeX spans with zero emojis and zero marketing words
  - Every notebook in notebooks/ executes end to end in .venv with outputs stored and zero error outputs
  - FEAT-SL2 re-verified and agent-approved after the 5a conversion
  - scripts/verify_notebook.py --all exits 0 across the whole corpus
stories: [STORY-SL12]
tasks: []
code_paths:
  - notebooks/
---

# FEAT-SL9: Lessons 0-9 quality uplift to the curriculum bar

## Context

Measured 2026-09-04: 13 of 22 notebooks miss the roadmap's own checklist on
LaTeX density or emoji presence, and 17 of 22 store no executed outputs. The
detail is tabulated on STORY-SL12. This feature closes when the verifier
passes the whole corpus, not when the edits land.

## Acceptance Criteria

- [ ] Theory rewrites: 0a (Opus), 3a (Opus), 5a LaTeX conversion (Opus)
- [ ] Practical uplifts in three bounded sessions: lessons 1-3, lessons 5-8, lesson 9 (Sonnet)
- [ ] Execute-all sweep with stored outputs (Sonnet) after every content task lands
- [ ] FEAT-SL2 freshness stamped and agent-approved
