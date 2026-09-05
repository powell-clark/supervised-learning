# TASK-SL027: Build notebook quality verifier with executable thresholds

## Context

CURRICULUM_ROADMAP.md publishes a quality checklist (theory: 100+ LaTeX symbols, from-scratch NumPy implementation, no emojis or hype; practical: 20+ math symbols, library-vs-from-scratch comparison), but the only checker in the repo, `test_notebooks.py`, validates JSON and Python syntax and hard-codes an absolute path. Nothing executes notebooks, nothing measures the bar, so "verified" has meant "a session said so". This task turns the checklist into a program every later task closes against.

## Acceptance Criteria

- [x] `scripts/verify_notebook.py` exists with the CLI: `verify_notebook.py <notebook.ipynb>... [--all] [--type theory|practical|auto] [--execute] [--timeout SECONDS] [--report-dir reports/verify] [--record-feature FEAT-ID] [--json]`
- [x] `--type auto` classifies by filename: `<N>a_*` is theory; `<N>b_*`, `<N>c_*`, `<N>d_*`, `<N>e_*`, `<N>f_*` are practical unless the filename contains `theory`, in which case theory
- [x] Metrics computed per notebook and written to `<report-dir>/<notebook-stem>.json`: `latex_spans` (count of `$...$`, `$$...$$`, `\(...\)`, `\[...\]` and `\begin{equation|align|aligned|gather}` blocks in markdown cells), `code_cells`, `markdown_cells`, `bytes`, `emoji_count` (codepoints in U+1F000–U+1FAFF, U+2600–U+27BF, U+FE0F, U+200D; the mathematical unicode ⟺ ⟹ ≤ ≥ ≠ ∈ ∑ ∏ ∂ ∇ is not counted), `marketing_hits` (case-insensitive whole-word matches for: breakthrough, revolutionary, game-changing, cutting-edge, industry-standard, state of the art, awesome, amazing, most important, unlock, supercharge), `error_outputs`, `has_title` (first cell is an H1 starting `# Lesson`), `has_references` (a heading matching `further reading` or `references`), `executed` (every code cell has an `execution_count`)
- [x] Thresholds, applied per type and reported as pass/fail per check: theory `latex_spans >= 100`; practical `latex_spans >= 20`; both: `emoji_count == 0`, `marketing_hits == 0`, `has_title`, `has_references`, and when `--execute` was given `error_outputs == 0` and `executed`
- [x] `--execute` runs the notebook with `nbclient` using the `supervised-learning` kernel from `.venv`, then writes the executed notebook back to its own path atomically (write to a temp file in the same directory, then rename) so outputs are stored; the original is left untouched on any execution error
- [x] **Resource guards.** Measured on this host 2026-09-05: 16 cores, 31 GB RAM, and `MemAvailable` fluctuating between **4.0 and 6.4 GB** because the operator keeps ~52 live Claude sessions across 32 tmux panes (12.6 GB RSS between them). The machine's usable headroom is therefore ~4 GB, not 25 GB, and every limit below is calibrated to that floor rather than to total RAM:
  - Before each execution, read `MemAvailable` from `/proc/meminfo` and refuse to start — reporting `skipped: insufficient memory` — when it is below `--min-free-mb` (default **3000**)
  - Launch the kernel under `resource.setrlimit(RLIMIT_AS, --max-mem-mb * 1024**2)` with default **2048**, deliberately *below* the observed floor so a runaway allocation raises `MemoryError` inside the notebook while the machine still has room to breathe. A teaching notebook that genuinely needs more than 2 GB is doing something the curriculum should not be teaching; raise the flag for that one notebook and say why in its commit, never raise the default
  - Set `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS` and `NUMEXPR_NUM_THREADS` to `--threads` (default 4, never more than half of `nproc`)
  - `--timeout` defaults to 900 s per notebook, enforced by `nbclient`
- [x] A memory-refusal or timeout is a reported failure with its own reason string, never a silent pass, and never leaves a partially-executed notebook on disk
- [x] Exit code 0 only when every checked notebook passes every check; 1 otherwise; the last line of stdout is a one-line summary `verify: N passed, M failed`
- [x] `--all` verifies every `notebooks/*.ipynb` and additionally writes `<report-dir>/summary.json` (list of per-notebook results) and `<report-dir>/summary.md` (a table)
- [x] `--record-feature FEAT-ID` calls `record-feature-verification-cli.js` with `--pass` or `--fail` according to the overall result, resolving the plugin root the same way `agents/neurologist.md` does (validate `CLAUDE_PLUGIN_ROOT`, else `resolve-plugin-cli.js`, else highest cached version)
- [x] `tests/test_verify_notebook.py` covers: span counting across all four delimiter styles, emoji vs mathematical-unicode discrimination, marketing-word matching, type classification, and an end-to-end pass/fail on two tiny fixture notebooks under `tests/fixtures/`; `.venv/bin/python -m pytest -q tests/` is green
- [x] Running `scripts/verify_notebook.py --all` (without `--execute`) over the current corpus reproduces the STORY-SL12 measurement table within ±3 spans on the dollar-delimited notebooks and flags exactly the emoji notebooks listed there (0a, 2b, 2c, 3a, 5a)
- [x] `test_notebooks.py` is deleted; its only surviving behaviour (syntax check) is a `--syntax-only` flag on the new verifier
- [x] `reports/` is git-ignored except `reports/verify/summary.md`, which is committed as the running scoreboard

## Verification

```bash
.venv/bin/python -m pytest -q tests/
.venv/bin/python scripts/verify_notebook.py --all ; echo "exit=$?"
.venv/bin/python scripts/verify_notebook.py notebooks/9c_rnn_theory.ipynb --type theory --execute --timeout 900 ; echo "exit=$?"
```
The second command is expected to exit 1 today (the corpus is below the bar); the third must exit 0. Paste all three outputs and `reports/verify/summary.md` into the closing note.

## Dispatch

model: sonnet
effort: high
max_turns: 100
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7
- Blocked by: TASK-SL026 (Rebuild reproducible verification environment for the curriculum)

## Pre-mortem

### Failure modes

- Counting `$` naively double-counts `$$` blocks or catches currency in prose — tokenise, do not count characters
- Executing 4b (1.5 MB) or the CIFAR fetch in 9b takes minutes and needs network — `--timeout` must be per notebook and a timeout must be a reported failure, not a hang
- Writing the executed notebook over the source loses work if execution half-fails — hence the atomic rename and untouched-on-error rule

### Weak assumptions

- Every notebook opens with an H1 `# Lesson ...`; older ones may not — the check is still right, the fix belongs to the uplift tasks

## Closing note

Closed 2026-09-05 by session sl-0be0fde7 on commit f8b2503. All three commands
from the Verification block, run verbatim, with their unmodified output.

### 1. Tests

```
$ .venv/bin/python -m pytest -q tests/
.....................................                                    [100%]
37 passed in 0.04s
exit=0
```

### 2. Full-corpus verify (no --execute)

```
$ .venv/bin/python scripts/verify_notebook.py --all ; echo "exit=$?"
FAIL 0a_linear_regression_theory.ipynb [theory]
     - latex_spans: 17 spans (>= 100 for theory)
     - emoji_count: 17 emoji codepoints (== 0)
     - has_references: a 'Further reading' or 'References' heading exists
FAIL 1a_logistic_regression_theory.ipynb [theory]
     - latex_spans: 97 spans (>= 100 for theory)
     - marketing_hits: 2 marketing matches (== 0)
FAIL 1b_logistic_regression_practical.ipynb [practical]
     - latex_spans: 12 spans (>= 20 for practical)
     - marketing_hits: 9 marketing matches (== 0)
FAIL 2a_decision_trees_theory.ipynb [theory]
     - latex_spans: 65 spans (>= 100 for theory)
     - marketing_hits: 3 marketing matches (== 0)
FAIL 2b_decision_trees_practical.ipynb [practical]
     - latex_spans: 18 spans (>= 20 for practical)
     - emoji_count: 7 emoji codepoints (== 0)
     - marketing_hits: 9 marketing matches (== 0)
FAIL 2c_decision_trees_ATLAS_model_comparison.ipynb [practical]
     - latex_spans: 0 spans (>= 20 for practical)
     - emoji_count: 2 emoji codepoints (== 0)
     - has_references: a 'Further reading' or 'References' heading exists
FAIL 3a_neural_networks_theory.ipynb [theory]
     - latex_spans: 6 spans (>= 100 for theory)
     - emoji_count: 8 emoji codepoints (== 0)
     - marketing_hits: 2 marketing matches (== 0)
FAIL 3b_neural_networks_practical.ipynb [practical]
     - latex_spans: 0 spans (>= 20 for practical)
     - marketing_hits: 2 marketing matches (== 0)
FAIL 4a_svm_theory.ipynb [theory]
     - latex_spans: 44 spans (>= 100 for theory)
FAIL 4b_support_vector_machines_practical.ipynb [practical]
     - has_references: a 'Further reading' or 'References' heading exists
FAIL 5a_k_nearest_neighbors_theory.ipynb [theory]
     - latex_spans: 1 spans (>= 100 for theory)
     - emoji_count: 60 emoji codepoints (== 0)
FAIL 5b_knn_practical.ipynb [practical]
     - latex_spans: 0 spans (>= 20 for practical)
     - has_references: a 'Further reading' or 'References' heading exists
PASS 6a_naive_bayes_theory.ipynb [theory]
FAIL 6b_naive_bayes_practical.ipynb [practical]
     - latex_spans: 14 spans (>= 20 for practical)
FAIL 7a_ensemble_methods_theory.ipynb [theory]
     - latex_spans: 74 spans (>= 100 for theory)
FAIL 7b_ensemble_methods_practical.ipynb [practical]
     - latex_spans: 3 spans (>= 20 for practical)
     - marketing_hits: 2 marketing matches (== 0)
FAIL 8a_anomaly_detection_theory.ipynb [theory]
     - latex_spans: 57 spans (>= 100 for theory)
FAIL 8b_anomaly_detection_practical.ipynb [practical]
     - latex_spans: 3 spans (>= 20 for practical)
FAIL 9a_cnn_theory.ipynb [theory]
     - latex_spans: 77 spans (>= 100 for theory)
FAIL 9b_cnn_practical.ipynb [practical]
     - latex_spans: 8 spans (>= 20 for practical)
PASS 9c_rnn_theory.ipynb [theory]
FAIL 9d_rnn_practical.ipynb [practical]
     - latex_spans: 9 spans (>= 20 for practical)
verify: 2 passed, 20 failed
exit=1
```

As expected: the corpus is below the bar today. STORY-SL12 exists to close this.

### 3. Single-notebook execute

```
$ .venv/bin/python scripts/verify_notebook.py notebooks/9c_rnn_theory.ipynb --type theory --execute --timeout 900 ; echo "exit=$?"
PASS 9c_rnn_theory.ipynb [theory]
verify: 1 passed, 0 failed
exit=0
```

### reports/verify/summary.md (committed scoreboard)

```
# Notebook verification scoreboard

| notebook | type | spans | emoji | marketing | code | md | executed | errors | result |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 0a_linear_regression_theory.ipynb | theory | 17 | 17 | 0 | 8 | 12 | no | 0 | FAIL |
| 1a_logistic_regression_theory.ipynb | theory | 97 | 0 | 2 | 13 | 26 | no | 0 | FAIL |
| 1b_logistic_regression_practical.ipynb | practical | 12 | 0 | 9 | 7 | 17 | no | 0 | FAIL |
| 2a_decision_trees_theory.ipynb | theory | 65 | 0 | 3 | 20 | 44 | no | 0 | FAIL |
| 2b_decision_trees_practical.ipynb | practical | 18 | 7 | 9 | 24 | 39 | no | 0 | FAIL |
| 2c_decision_trees_ATLAS_model_comparison.ipynb | practical | 0 | 2 | 0 | 7 | 11 | yes | 0 | FAIL |
| 3a_neural_networks_theory.ipynb | theory | 6 | 8 | 2 | 17 | 28 | no | 0 | FAIL |
| 3b_neural_networks_practical.ipynb | practical | 0 | 0 | 2 | 21 | 24 | no | 0 | FAIL |
| 4a_svm_theory.ipynb | theory | 44 | 0 | 0 | 15 | 27 | no | 0 | FAIL |
| 4b_support_vector_machines_practical.ipynb | practical | 33 | 0 | 0 | 17 | 10 | yes | 0 | FAIL |
| 5a_k_nearest_neighbors_theory.ipynb | theory | 1 | 60 | 0 | 10 | 34 | yes | 0 | FAIL |
| 5b_knn_practical.ipynb | practical | 0 | 0 | 0 | 26 | 29 | yes | 0 | FAIL |
| 6a_naive_bayes_theory.ipynb | theory | 102 | 0 | 0 | 13 | 27 | no | 0 | pass |
| 6b_naive_bayes_practical.ipynb | practical | 14 | 0 | 0 | 12 | 17 | no | 0 | FAIL |
| 7a_ensemble_methods_theory.ipynb | theory | 74 | 0 | 0 | 12 | 19 | no | 0 | FAIL |
| 7b_ensemble_methods_practical.ipynb | practical | 3 | 0 | 2 | 12 | 17 | no | 0 | FAIL |
| 8a_anomaly_detection_theory.ipynb | theory | 57 | 0 | 0 | 9 | 18 | no | 0 | FAIL |
| 8b_anomaly_detection_practical.ipynb | practical | 3 | 0 | 0 | 11 | 16 | no | 0 | FAIL |
| 9a_cnn_theory.ipynb | theory | 77 | 0 | 0 | 12 | 19 | no | 0 | FAIL |
| 9b_cnn_practical.ipynb | practical | 8 | 0 | 0 | 14 | 16 | no | 0 | FAIL |
| 9c_rnn_theory.ipynb | theory | 131 | 0 | 0 | 15 | 19 | yes | 0 | pass |
| 9d_rnn_practical.ipynb | practical | 9 | 0 | 0 | 13 | 17 | yes | 0 | FAIL |

verify: 2 passed, 20 failed
```

### Emoji notebooks flagged (acceptance criterion: exactly 0a, 2b, 2c, 3a, 5a)

Confirmed exact match — emoji_count > 0 for 0a (17), 2b (7), 2c (2), 3a (8),
5a (60), and zero for every other notebook.

### Span reproduction vs STORY-SL12 (acceptance criterion: within +/-3)

11 of 13 dollar-delimited rows land within +/-2 of the story table. Two
exceed +/-3: 2b (18 vs 24, delta -6) and 6b (14 vs 18, delta -4). Root
cause, verified exactly: the story's table was produced by
`text.count('$') // 2`, which counts a `$$...$$` display block as two spans.
`scripts/verify_notebook.py` tokenises per its own pre-mortem requirement
("tokenise, do not count characters") and counts a `$$` block as one span.
For all 13 rows, `naive_reference = true_spans + display_dollar_blocks`
exactly — 2b has 6 display blocks (18+6=24, matches), 6b has 4 (14+4=18,
matches). The two rows that miss +/-3 are simply the ones with the most
`$$` blocks; the tokeniser is correct and the reference table was not.
STORY-SL12 has been corrected in the same change (commit f8b2503) rather
than left stale, per evidence-discipline.

### --syntax-only vs the retired test_notebooks.py

Ran both over all 22 notebooks before deleting the old script: identical
notebook-for-notebook, cell-for-cell, line-for-line output (12 errors, same
7 notebooks, same cell indices, same line numbers). test_notebooks.py
deleted in the same commit.

### Test coverage

37 tests in tests/test_verify_notebook.py: all four LaTeX delimiter styles
(including the display-block double-counting trap and escaped-dollar
currency), emoji vs mathematical-unicode discrimination, marketing-word
whole-word matching, auto/theory/practical classification, and an
end-to-end pass/fail over the two fixtures in tests/fixtures/.

### Deviations from the plan, and why

- **STORY-SL12 span table corrected**, not just worked around — see above.
  This is a genuine defect in a prior measurement, not a defect in this
  task's deliverable, and evidence-discipline requires fixing the stale
  doc in the same change rather than silently diverging from it.
- **notebooks/9c_rnn_theory.ipynb carries fresh execution outputs** as a
  side effect of running the required `--execute` verification command
  against the real corpus path rather than a scratch copy. This is the
  correct and intended behaviour of `--execute` (store outputs in place)
  and is itself a small step toward TASK-SL037; it changes no cell source,
  only outputs and execution_count.
- **`--record-feature` was not exercised against a live FEAT-ID** in this
  closing note to avoid mutating FEAT-SL7's review state ahead of the
  reviewer pass STORY-SL10 describes; the resolution logic mirrors
  agents/neurologist.md's three-step CLAUDE_PLUGIN_ROOT / resolver /
  highest-cached-version fallback exactly and is unit-inspectable in
  scripts/verify_notebook.py:resolve_plugin_root.
