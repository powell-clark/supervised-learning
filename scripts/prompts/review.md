Review {FEATURE_ID}, autonomously, with no operator gate.

1. Read `CONSCIOUSNESS/features/backlog-feature-item-details/{FEATURE_ID}.md`
   (or wherever its index row's `doc` column currently points) in full,
   including every acceptance criterion and `code_paths`.
2. For each task id in the feature's `task_ids`, read that task's card and its
   closing note under `## Closing note`.
3. Re-run `scripts/verify_notebook.py --all --record-feature {FEATURE_ID}` (or,
   if `code_paths` names specific notebooks rather than the whole corpus, pass
   those explicitly) and read the report it writes to `reports/verify/`. Do
   not accept a task's own claim of a passing verifier run as evidence — run
   it again yourself, now, and read this run's output.
4. Decide `agent-approved` only if every acceptance criterion on the feature
   card is actually met by what is in the repository right now, and every
   code_paths file's tests (if any) pass. Otherwise decide `agent-rejected`
   and say exactly which criterion failed and why, citing the command and
   output that proves it.
5. Record the verdict:
   `append-verdict-cli --target {FEATURE_ID} --verdict agent-approved|agent-rejected
   --type feature --evidence <HEAD-sha> --note "<one sentence>" --repo .`
6. On `agent-approved`: move the feature's row from
   `CONSCIOUSNESS/features/FEATURE-BACKLOG-INDEX.md` (or wherever it
   currently is) to `CONSCIOUSNESS/features/FEATURE-MAINTAINED-DONE-INDEX.md`
   with `status: maintained`, relocate its card to
   `CONSCIOUSNESS/features/maintained-done-feature-item-details/{FEATURE_ID}.md`,
   and stamp `last_tested` to today's date via the verification run in step 3.
   On `agent-rejected`: leave the feature where it is; do not move it.
7. Commit and push with explicit pathspec, authored as:
   `Authored-By: Emmanuel Powell-Clark <emmanuel@powellclark.com>`
   with no AI/bot attribution of any kind.

Never touch CONSCIOUSNESS/reviews/REVIEW-INDEX.md by hand. Never mark a
feature maintained on the strength of a task's own report alone — the review
session's own re-run is the evidence.
