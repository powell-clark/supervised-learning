Work {TASK_ID} to completion, autonomously, with no operator gate.

Sequence, exactly:

1. Read `CONSCIOUSNESS/tasks/backlog-task-item-details/{TASK_ID}.md` (or wherever
   the DONE/ACTIVE/BACKLOG index currently points its `doc` column) in full,
   and read its parent story card.
2. Claim it: `update-task-status-cli --task {TASK_ID} --to in_progress --repo .`
3. Implement every acceptance criterion on the card.
4. Run every command in the card's `## Verification` block until each exits 0.
   Do not claim success on a command you have not actually run this session.
5. Commit with explicit pathspec (never a bare `git add -A` or bare
   `git commit`), authored as:
   `Authored-By: Emmanuel Powell-Clark <emmanuel@powellclark.com>`
   with no AI/bot attribution of any kind (no Co-Authored-By, no
   Claude-Session, no Generated-With line). Push to origin main.
6. Close it: `update-task-status-cli --task {TASK_ID} --to in_review --repo .`,
   then `append-verdict-cli --target {TASK_ID} --verdict bypass-approved
   --type task --evidence <commit-sha> --note "<one sentence>" --repo .`,
   then `update-task-status-cli --task {TASK_ID} --to done --repo .`.
7. Relocate the card to `CONSCIOUSNESS/tasks/done-task-item-details/{TASK_ID}.md`
   and correct the DONE row's `doc`, `expected_duration` and `story_points`
   columns if the status-transition CLI left them wrong (a known plugin gap,
   powell-clark/consciousness#2229) — check the row after every transition
   rather than assuming it is correct.
8. Tick every acceptance criterion `- [x]` on the card and append a closing
   note under a `## Closing note` heading pasting the verbatim, unmodified
   output of every `## Verification` command.
9. Commit and push the PGPS state changes (card move, index rows, verdict
   fragment) with explicit pathspec, same authorship rule as step 5.

If a card acceptance criterion or Verification command is factually wrong for
this repo (a flag that does not exist, a path that does not exist, a pin with
no wheel for the interpreter in use) — diagnose it, fix it in scope, document
the deviation plainly in the closing note and the commit message, and continue.
Do not halt silently and do not ask the operator; there is no operator in this
loop. If you are genuinely blocked (the fix requires a decision only a human
can make, or touches infrastructure outside the sandbox), stop, leave the task
in_progress, write exactly what is blocking to a file named
`.claude/evidence/{TASK_ID}-blocked.md`, and end the session — do not mark the
task done or in_review from a blocked state.

Never run more than one task. Never claim a second task. Never touch
CONSCIOUSNESS/reviews/REVIEW-INDEX.md by hand — verdicts are fragment writes
only, the compactor mints the canonical row.
