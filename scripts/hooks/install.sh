#!/usr/bin/env bash
# Install the hooks from scripts/hooks/ into the repository's hooks directory.
# Run once per fresh clone, from the main checkout or any linked worktree.
# Idempotent: overwrites existing hooks.

set -e
cd "$(git rev-parse --show-toplevel)"

HOOKS_SRC="scripts/hooks"
# The common git directory, absolute: a linked worktree's .git is a file, and a
# relative hooks path would resolve inside that worktree and find no hooks.
HOOKS_DST="$(git rev-parse --path-format=absolute --git-common-dir)/hooks"

if [ ! -d "$HOOKS_DST" ]; then
    echo "ERROR: $HOOKS_DST does not exist — is this a git repo?"
    exit 1
fi

GLOBAL_HOOKS_PATH=$(git config --global --get core.hooksPath || true)
LOCAL_HOOKS_PATH=$(git config --local --get core.hooksPath || true)

# pii-gate.sh is not a git hook name; pre-push calls it from beside itself.
for hook in pre-push pii-gate.sh; do
    src="$HOOKS_SRC/$hook"
    dst="$HOOKS_DST/$hook"
    if [ ! -f "$src" ]; then
        echo "skip: $src does not exist"
        continue
    fi
    cp "$src" "$dst"
    chmod +x "$dst"
    echo "installed: $dst"
done

# A global hooksPath would bypass the hooks just installed; point this repo at
# them so the install takes effect in every worktree. The global setting stays
# untouched for every other repo on the machine.
if [ "$LOCAL_HOOKS_PATH" = ".git/hooks" ] || { [ -n "$GLOBAL_HOOKS_PATH" ] \
    && [ "$GLOBAL_HOOKS_PATH" != "$HOOKS_DST" ] && [ "$LOCAL_HOOKS_PATH" != "$HOOKS_DST" ]; }; then
    [ -n "$GLOBAL_HOOKS_PATH" ] && echo "NOTE: detected global 'core.hooksPath = $GLOBAL_HOOKS_PATH'."
    echo "NOTE: setting 'core.hooksPath = $HOOKS_DST' for this repo only."
    git config --local core.hooksPath "$HOOKS_DST"
fi

echo ""
echo "Hooks installed. The gate reads an optional local replacement list: set it with"
echo "  git config pii.listPath <path>   (or the PII_LIST environment variable)"
