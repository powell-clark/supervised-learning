# STORY-SL10: Autonomous verification and run tooling so the curriculum builds, checks and closes itself without a human in the loop

## User Story

I want the remaining curriculum to be built, verified and closed by agents alone so that I can walk away from the run and come back to a finished, executed corpus with an index and a report, rather than reviewing notebooks one by one.

## Context

Operator ruling 2026-09-04 (STEER-SL005): no human gates. Fable authors the
plan and cards; Sonnet builds tooling and practical notebooks; Opus builds
theory notebooks and the final review. That only works if three things exist
that do not today: a reproducible execution environment (the checked-in
`.venv` points at a Python that is no longer installed), a mechanical quality
verifier that turns CURRICULUM_ROADMAP.md's checklist into pass/fail with
evidence (`test_notebooks.py` only checks syntax), and an orchestrator that
dispatches each task to the right model and records agent verdicts so features
close under the agent tier.

## Acceptance Criteria

- [ ] `scripts/setup_env.sh` creates `.venv` from an installed interpreter and `requirements.txt`, is idempotent, and every notebook's imports resolve inside it
- [ ] `scripts/verify_notebook.py` executes a notebook, stores its outputs, computes the roadmap metrics, applies the theory/practical thresholds, writes a JSON report, and exits non-zero on any failure
- [ ] `scripts/run_syllabus.sh` walks the execution spine, dispatches each unblocked task to the model named in its card, verifies, records verdicts, retries once, and stops cleanly when the spine is empty
- [ ] Every feature card carries `code_paths:` so verification runs resolve to features and stamp `last_tested`
- [ ] README.md is regenerated from the notebooks as the corpus index, with no emojis and no stale entries
- [ ] A corpus completion report exists with per-notebook metrics, execution status and links, and every feature is fresh and every story fulfilled or explicitly not

## References

- CURRICULUM_ROADMAP.md (quality checklist and benchmarks)
- CONSCIOUSNESS/stream/steering.jsonl STEER-SL005, STEER-SL006
- CONSCIOUSNESS/artifacts/SYLLABUS-RUN-PLAN.md
