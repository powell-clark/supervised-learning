# TASK-SL038: Regenerate README as the corpus index

## Context

`README.md` lists lessons 1 and 2 only, says "Neural Networks (Coming Soon)" when 3a, 3b, 9a–9d all exist, carries emojis the style rules forbid elsewhere, and points its Colab badges at `powell-clark/supervised-machine-learning` while the git remote is `powell-clark/supervised-learning`. It is the first thing a reader sees and it is the least accurate document in the repo. Generating it from the notebooks makes it impossible to go stale again.

## Acceptance Criteria

- [ ] `scripts/build_readme.py` generates `README.md` from a template plus live notebook metadata: for each notebook in lexical order, its H1 title, a one-line description taken from the notebook's Introduction section, a Colab badge with the correct repository path, and a source link
- [ ] The Colab badge URL is derived from `git remote get-url origin` rather than hard-coded, so it cannot drift from the actual repository again
- [ ] The generated README carries no emojis and no marketing language, matching the standard the notebooks are held to
- [ ] Sections preserved from the current README: local setup, datasets, licence and copyright, contributing, citation, contact — updated where they are wrong (the clone URL, the Python version from `.python-version`)
- [ ] A short "How this corpus is built" section describing the theory/practical pairing, the quality bar, and how to run the verifier — so a reader can check the claims themselves
- [ ] The datasets section lists every dataset actually used across the corpus, derived from the notebooks rather than hand-listed
- [ ] Running `scripts/build_readme.py --check` exits non-zero if the committed README differs from what the generator would produce, so drift is detectable in future
- [ ] `README.md` regenerated and committed

## Verification

```bash
.venv/bin/python scripts/build_readme.py && git diff --stat README.md
.venv/bin/python scripts/build_readme.py --check ; echo "exit=$?"
grep -c "supervised-machine-learning" README.md   # must be 0
```
`--check` must exit 0 after committing; the stale-slug grep must return 0.

## Dispatch

model: sonnet
effort: medium
max_turns: 80
reviewer_model: sonnet

## Dependencies

- Directive: DIRECT-SL1
- Story: STORY-SL10
- Features: FEAT-SL7
- Blocked by: TASK-SL037 (Execute every notebook end-to-end and store outputs)

## Pre-mortem

### Failure modes

- Extracting a one-line description from each notebook's Introduction is fragile across 22 differently-shaped notebooks — fall back to the H1 subtitle and flag notebooks needing a hand-written line rather than emitting something wrong
- Overwriting the README loses the hand-written contributing and citation prose — template those sections, do not generate them

### Weak assumptions

- The public repository slug is `supervised-learning`; confirm from the remote before writing badges, since the README's current slug suggests it may once have been different and the Colab links may need to keep working for existing readers
