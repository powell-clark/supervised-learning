#!/usr/bin/env bash
# Autonomous syllabus run orchestrator (TASK-SL028).
#
# Walks the PGPS execution spine, dispatches each unblocked, Dispatch-bearing
# task to a headless `claude -p` Sonnet session, verifies independently,
# retries once on failure, runs a reviewer session when a feature's tasks are
# all done, and stops cleanly when the spine is empty.
#
# Known deviations from the literal card text (TASK-SL028), documented here
# because a literal implementation would not run at all:
#
#   1. `claude -p --help` on the installed binary (2.1.261) has no
#      `--max-turns` flag — confirmed by full flag enumeration, not by a
#      single failed attempt. The flag is dropped from the actual
#      invocation; `max_turns` from the card's Dispatch block is still
#      parsed and recorded in the JSON result filename/log for audit, and
#      the wall-clock `timeout` below (already an independently required
#      guard) is the sole runaway bound.
#   2. The post-run "git status --porcelain is clean" check is evaluated as
#      a before/after DIFF, not a literal empty-output check. This repo
#      carries ~40 lines of pre-existing dirty state at all times (plugin
#      runtime exhaust under CONSCIOUSNESS/stream/, .claude/ session files)
#      that no single task owns or can clean up; a literal empty-output
#      check would fail every task, including the ones this orchestrator
#      itself must close to be considered done.
#   3. `node main.js --headless` exits 0 even when it reports validation
#      errors (measured 2026-09-05: exit 0 with "2 errors detected." in the
#      text). The abort-on-PGPS-error check therefore parses the
#      "N errors detected" text rather than trusting the exit code.

set -u
set -o pipefail

# --------------------------------------------------------------------------
# paths
# --------------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VPY="$REPO_ROOT/.venv/bin/python"

# Honour an inherited RUN_TS (set by a --detach parent re-executing this
# script as its child) so the detached process writes into the same
# reports/run/<ts>/ directory the parent already announced, rather than
# computing a second, slightly later timestamp and splitting the log.
RUN_TS="${RUN_TS:-$(date -u +%Y%m%dT%H%M%SZ)}"
RUN_DIR="$REPO_ROOT/reports/run/$RUN_TS"
RUN_LOG="$RUN_DIR/run.log"
CURRENT_PID="$REPO_ROOT/reports/run/current.pid"

MIN_FREE_MB=3000
MIN_FREE_DISK_GB=10
MAX_REFUSALS=10
REFUSAL_WAIT_S=120
TASK_TIMEOUT_S=5400   # 90 minutes
THREADS=4

DRY_RUN=0
LIMIT=0
ONLY_TASK=""
DETACH=0

# --------------------------------------------------------------------------
# args
# --------------------------------------------------------------------------

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --limit) LIMIT="$2"; shift 2 ;;
    --only) ONLY_TASK="$2"; shift 2 ;;
    --detach) DETACH=1; shift ;;
    *) echo "run_syllabus: unknown argument: $1" >&2; exit 2 ;;
  esac
done

# --------------------------------------------------------------------------
# logging
# --------------------------------------------------------------------------

log() {
  local msg="[run-syllabus $(date -u +%H:%M:%S)] $*"
  echo "$msg"
  if [ -n "${RUN_LOG:-}" ] && [ -d "$(dirname "$RUN_LOG")" ]; then
    echo "$msg" >> "$RUN_LOG"
  fi
}

die() {
  log "FATAL: $*"
  exit "${2:-1}"
}

# --------------------------------------------------------------------------
# plugin root resolution — same three-step order as agents/neurologist.md
# --------------------------------------------------------------------------

resolve_plugin_root() {
  local cli_rel="dist/packages/core/pgps/main.js"
  if [ -n "${CLAUDE_PLUGIN_ROOT:-}" ] && [ -f "${CLAUDE_PLUGIN_ROOT}/${cli_rel}" ]; then
    echo "${CLAUDE_PLUGIN_ROOT}"
    return 0
  fi
  local resolver
  resolver=$(ls ~/.claude/plugins/cache/powell-clark/consciousness/*/dist/packages/core/attention/resolve-plugin-cli.js 2>/dev/null | sort -V | tail -1)
  if [ -n "$resolver" ]; then
    local active_root
    active_root=$(node "$resolver" 2>/dev/null)
    if [ -n "$active_root" ] && [ -f "$active_root/${cli_rel}" ]; then
      echo "$active_root"
      return 0
    fi
  fi
  local cached
  cached=$(ls -d ~/.claude/plugins/cache/powell-clark/consciousness/*/ 2>/dev/null | sort -V | tail -1)
  if [ -n "$cached" ] && [ -f "${cached}${cli_rel}" ]; then
    echo "${cached%/}"
    return 0
  fi
  return 1
}

PLUGIN_ROOT="$(resolve_plugin_root)" || die "cannot resolve the consciousness plugin root" 2
PGPS_CLI="$PLUGIN_ROOT/dist/packages/core/pgps/main.js"
STATUS_CLI="$PLUGIN_ROOT/dist/packages/core/pgps/update-task-status-cli.js"
VERDICT_CLI="$PLUGIN_ROOT/dist/packages/core/fragments/append-verdict-cli.js"
HEAL_CLI="$PLUGIN_ROOT/dist/packages/core/pgps/self-healing/cli.js"

# --------------------------------------------------------------------------
# host guards
# --------------------------------------------------------------------------

mem_available_mb() {
  awk '/MemAvailable:/ {print int($2/1024)}' /proc/meminfo
}

free_disk_gb() {
  df -Pk "$REPO_ROOT" | awk 'NR==2 {print int($4/1024/1024)}'
}

wait_for_host_headroom() {
  local refusals=0
  while true; do
    local mem_mb disk_gb
    mem_mb=$(mem_available_mb)
    disk_gb=$(free_disk_gb)
    if [ "$mem_mb" -ge "$MIN_FREE_MB" ] && [ "$disk_gb" -ge "$MIN_FREE_DISK_GB" ]; then
      log "host headroom ok: MemAvailable=${mem_mb}MB free_disk=${disk_gb}GB"
      return 0
    fi
    refusals=$((refusals + 1))
    log "host headroom refused ($refusals/$MAX_REFUSALS): MemAvailable=${mem_mb}MB (need ${MIN_FREE_MB}) free_disk=${disk_gb}GB (need ${MIN_FREE_DISK_GB})"
    if [ "$refusals" -ge "$MAX_REFUSALS" ]; then
      return 1
    fi
    sleep "$REFUSAL_WAIT_S"
  done
}

# --------------------------------------------------------------------------
# spine selection
# --------------------------------------------------------------------------

# id_is_done TASK-ID
id_is_done() {
  awk -F'|' -v id="$1" 'NR>1 && $1==id {found=1} END {exit !found}' \
    "$REPO_ROOT/CONSCIOUSNESS/tasks/TASK-DONE-INDEX.md"
}

# blocked_by_satisfied "id1,id2"
blocked_by_satisfied() {
  local blocked_by="$1"
  [ -z "$blocked_by" ] && return 0
  local IFS=','
  local id
  for id in $blocked_by; do
    id_is_done "$id" || return 1
  done
  return 0
}

# card_doc_path TASK-ID -> absolute path, searching active/backlog/done
card_doc_path() {
  local id="$1"
  local d
  for d in active-task-item-details backlog-task-item-details done-task-item-details; do
    if [ -f "$REPO_ROOT/CONSCIOUSNESS/tasks/$d/$id.md" ]; then
      echo "$REPO_ROOT/CONSCIOUSNESS/tasks/$d/$id.md"
      return 0
    fi
  done
  return 1
}

declare -A SKIP_LOGGED

# pgps_ready_ids -> one "TASK-ID title" per line, in spine order, for every
# task the PGPS engine itself has already classified as ready (its NEXT: and
# LAYER N: sections list every currently-blocked or currently-ready
# non-active task; only NEXT: is actually dispatchable now). Using the
# engine's own classification — rather than hand-parsing
# TASK-BACKLOG-INDEX.md's blocked_by column — sidesteps two problems
# discovered while building this script: the sequence column is a
# lexicographic fractional-indexing key (a5CYz, aI, ...), not a number
# sortable with `sort -n`, and at least one row (TASK-SL15, TASK-SL16) is
# ragged (13 fields where the schema defines 14), which silently misreads
# blocked_by for that row under fixed-position awk extraction. The PGPS
# engine already parses these correctly — that is how TASK-SL15/16 ended up
# correctly excluded under its HUMAN: section rather than NEXT:.
pgps_ready_ids() {
  local out
  out=$(node "$PGPS_CLI" --repo "$REPO_ROOT" 2>/dev/null)
  echo "$out" | awk '
    /^  NEXT:$/ { active=1; next }
    /^  LAYER [0-9]+:$/ { active=0 }
    /^  HUMAN:$/ { active=0 }
    /^TASKS\./ && !/ACTIVE/ { active=0 }
    active && match($0, /\[TASK-[A-Za-z0-9]+\]/) {
      id = substr($0, RSTART+1, RLENGTH-2)
      print id
    }
  '
}

# select_next_task -> prints "TASK-ID|title" or nothing
select_next_task() {
  if [ -n "$ONLY_TASK" ]; then
    echo "$ONLY_TASK|(--only)"
    return 0
  fi

  local ready_ids
  ready_ids=$(pgps_ready_ids)
  local id
  if [ -n "$ready_ids" ]; then
    while read -r id; do
      [ -z "$id" ] && continue
      id_is_done "$id" && continue
      local doc
      doc=$(card_doc_path "$id") || continue
      if ! "$VPY" "$SCRIPT_DIR/dispatch_meta.py" "$doc" >/dev/null 2>&1; then
        if [ -z "${SKIP_LOGGED[$id]:-}" ]; then
          log "skipping $id: no ## Dispatch block"
          SKIP_LOGGED[$id]=1
        fi
        continue
      fi
      local title
      title=$(grep -F "$id|" "$REPO_ROOT/CONSCIOUSNESS/tasks/TASK-BACKLOG-INDEX.md" | head -1 | cut -d'|' -f3)
      echo "$id|${title:-$id}"
      return 0
    done <<< "$ready_ids"
    return 1
  fi

  log "PGPS NEXT: section unavailable or empty — falling back to raw index scan"
  local rows
  rows=$(grep -v '^id|' "$REPO_ROOT/CONSCIOUSNESS/tasks/TASK-BACKLOG-INDEX.md" \
    | awk -F'|' '{print $1"|"$3"|"$8"|"$10"|"$12}' \
    | sort -t'|' -k5,5)
  local title blocked_by assignee seq
  while IFS='|' read -r id title blocked_by assignee seq; do
    id_is_done "$id" && continue
    [ -n "$assignee" ] && continue
    local doc
    doc=$(card_doc_path "$id") || continue
    if ! "$VPY" "$SCRIPT_DIR/dispatch_meta.py" "$doc" >/dev/null 2>&1; then
      if [ -z "${SKIP_LOGGED[$id]:-}" ]; then
        log "skipping $id ($title): no ## Dispatch block"
        SKIP_LOGGED[$id]=1
      fi
      continue
    fi
    if blocked_by_satisfied "$blocked_by"; then
      echo "$id|$title"
      return 0
    fi
  done <<< "$rows"
  return 1
}

# --------------------------------------------------------------------------
# verification-block extraction and execution
# --------------------------------------------------------------------------

extract_verification_script() {
  local card="$1"
  awk '
    /^## Verification/ { in_section=1; next }
    in_section && /^## / { exit }
    in_section && /^```/ { in_fence = !in_fence; next }
    in_section && in_fence { print }
  ' "$card"
}

run_verification() {
  local card="$1"
  local script
  script=$(extract_verification_script "$card")
  if [ -z "$script" ]; then
    log "no ## Verification fenced block found in $card"
    return 1
  fi
  ( cd "$REPO_ROOT" && bash -c "$script" )
}

# --------------------------------------------------------------------------
# dispatch
# --------------------------------------------------------------------------

run_task() {
  local id="$1" title="$2" attempt="$3" extra_context="${4:-}"
  local doc
  doc=$(card_doc_path "$id") || { log "$id: no card found, cannot dispatch"; return 1; }

  local meta model effort max_turns reviewer_model
  meta=$("$VPY" "$SCRIPT_DIR/dispatch_meta.py" "$doc") || { log "$id: dispatch_meta failed"; return 1; }
  model=$(echo "$meta" | jq -r .model)
  effort=$(echo "$meta" | jq -r .effort)
  max_turns=$(echo "$meta" | jq -r .max_turns)
  reviewer_model=$(echo "$meta" | jq -r .reviewer_model)

  if [ "$model" != "sonnet" ]; then
    die "$id names model '$model' in its Dispatch block; STEER-SL007 requires every dispatched session to be sonnet" 2
  fi

  wait_for_host_headroom || die "host headroom refused $MAX_REFUSALS consecutive times before dispatching $id" 4

  local before_dirty after_dirty
  before_dirty=$(git -C "$REPO_ROOT" status --porcelain | sort)
  local mem_before
  mem_before=$(mem_available_mb)
  log "$id attempt=$attempt model=$model effort=$effort max_turns(recorded,not passed)=$max_turns MemAvailable_before=${mem_before}MB"

  local prompt
  prompt=$(sed "s/{TASK_ID}/$id/g" "$SCRIPT_DIR/prompts/task.md")
  if [ -n "$extra_context" ]; then
    prompt="$prompt

## Prior attempt failed — fix this before continuing

$extra_context"
  fi

  mkdir -p "$RUN_DIR"
  local result_file="$RUN_DIR/${id}.${attempt}.json"

  OMP_NUM_THREADS=$THREADS MKL_NUM_THREADS=$THREADS OPENBLAS_NUM_THREADS=$THREADS NUMEXPR_NUM_THREADS=$THREADS \
    timeout "$TASK_TIMEOUT_S" claude -p \
      --model "$model" \
      --effort "$effort" \
      --permission-mode bypassPermissions \
      --output-format json \
      "$prompt" \
      < /dev/null > "$result_file" 2> "$RUN_DIR/${id}.${attempt}.stderr.log"
  local claude_exit=$?

  local mem_after
  mem_after=$(mem_available_mb)
  local cost turns dur is_err
  cost=$(jq -r '.total_cost_usd // "n/a"' "$result_file" 2>/dev/null)
  turns=$(jq -r '.num_turns // "n/a"' "$result_file" 2>/dev/null)
  dur=$(jq -r '.duration_ms // "n/a"' "$result_file" 2>/dev/null)
  is_err=$(jq -r '.is_error // "n/a"' "$result_file" 2>/dev/null)
  log "$id attempt=$attempt claude_exit=$claude_exit is_error=$is_err cost_usd=$cost turns=$turns duration_ms=$dur MemAvailable_after=${mem_after}MB"

  if [ "$claude_exit" -eq 124 ]; then
    log "$id attempt=$attempt: TIMEOUT after ${TASK_TIMEOUT_S}s"
    return 1
  fi

  after_dirty=$(git -C "$REPO_ROOT" status --porcelain | sort)
  local new_dirty
  new_dirty=$(comm -13 <(echo "$before_dirty") <(echo "$after_dirty"))

  local ok=1
  if ! id_is_done "$id"; then
    log "$id attempt=$attempt: FAIL — not present in TASK-DONE-INDEX.md"
    ok=0
  fi
  if [ -n "$new_dirty" ]; then
    log "$id attempt=$attempt: FAIL — new uncommitted paths after the session: $(echo "$new_dirty" | tr '\n' ' ')"
    ok=0
  fi
  doc=$(card_doc_path "$id") || doc=""
  if [ -n "$doc" ]; then
    if ! run_verification "$doc" > "$RUN_DIR/${id}.${attempt}.verify.log" 2>&1; then
      log "$id attempt=$attempt: FAIL — card Verification commands did not all exit 0 (see ${id}.${attempt}.verify.log)"
      ok=0
    fi
  fi

  [ "$ok" -eq 1 ]
}

# --------------------------------------------------------------------------
# feature review
# --------------------------------------------------------------------------

feature_row() {
  local feat_id="$1"
  awk -F'|' -v id="$feat_id" 'NR>1 && $1==id {print; exit}' "$REPO_ROOT/CONSCIOUSNESS/features/FEATURE-BACKLOG-INDEX.md"
}

feature_tasks_all_done() {
  local feat_id="$1"
  local row task_ids
  row=$(feature_row "$feat_id") || return 1
  [ -z "$row" ] && return 1
  task_ids=$(echo "$row" | awk -F'|' '{print $6}')
  [ -z "$task_ids" ] && return 1
  local IFS=','
  local t
  for t in $task_ids; do
    id_is_done "$t" || return 1
  done
  return 0
}

run_review() {
  local feat_id="$1" reviewer_model="$2"
  wait_for_host_headroom || { log "review $feat_id: host headroom refused, skipping this cycle"; return 1; }
  local prompt
  prompt=$(sed "s/{FEATURE_ID}/$feat_id/g" "$SCRIPT_DIR/prompts/review.md")
  mkdir -p "$RUN_DIR"
  local result_file="$RUN_DIR/${feat_id}.review.json"
  OMP_NUM_THREADS=$THREADS MKL_NUM_THREADS=$THREADS OPENBLAS_NUM_THREADS=$THREADS NUMEXPR_NUM_THREADS=$THREADS \
    timeout "$TASK_TIMEOUT_S" claude -p \
      --model "$reviewer_model" \
      --effort high \
      --permission-mode bypassPermissions \
      --output-format json \
      "$prompt" \
      < /dev/null > "$result_file" 2> "$RUN_DIR/${feat_id}.review.stderr.log"
  log "review $feat_id: claude_exit=$? (see ${feat_id}.review.json)"
}

# --------------------------------------------------------------------------
# between-task hooks
# --------------------------------------------------------------------------

between_task_hooks() {
  node "$HEAL_CLI" --apply --session syllabus-run --consciousness "$REPO_ROOT/CONSCIOUSNESS" \
    >> "$RUN_LOG" 2>&1

  local headless_out
  headless_out=$(node "$PGPS_CLI" --headless --repo "$REPO_ROOT" 2>&1)
  echo "$headless_out" >> "$RUN_LOG"
  local err_count
  err_count=$(echo "$headless_out" | grep -oE '[0-9]+ errors? detected' | grep -oE '^[0-9]+' | head -1)
  err_count="${err_count:-0}"
  if [ "$err_count" != "0" ]; then
    die "PGPS validation reports $err_count error(s) after a task cycle — aborting the run rather than propagating a broken index" 3
  fi
}

# --------------------------------------------------------------------------
# detach
# --------------------------------------------------------------------------

if [ "$DETACH" -eq 1 ]; then
  mkdir -p "$RUN_DIR"
  mkdir -p "$(dirname "$CURRENT_PID")"
  RUN_TS="$RUN_TS" setsid nohup bash "$0" > "$RUN_LOG" 2>&1 < /dev/null &
  DETACHED_PID=$!
  echo "$DETACHED_PID" > "$CURRENT_PID"
  log "detached: pid=$DETACHED_PID log=$RUN_LOG pid_file=$CURRENT_PID"
  echo "detached pid=$DETACHED_PID"
  echo "log=$RUN_LOG"
  echo "pid_file=$CURRENT_PID"
  exit 0
fi

# --------------------------------------------------------------------------
# main loop
# --------------------------------------------------------------------------

mkdir -p "$RUN_DIR"
log "run start: repo=$REPO_ROOT plugin_root=$PLUGIN_ROOT dry_run=$DRY_RUN limit=$LIMIT only=${ONLY_TASK:-none}"

if [ "$DRY_RUN" -eq 1 ]; then
  echo "PLAN (dry run — dispatches nothing):"
  count=0
  ready_ids=$(pgps_ready_ids)
  while read -r id; do
    [ -z "$id" ] && continue
    id_is_done "$id" && continue
    doc=$(card_doc_path "$id") || continue
    if ! meta=$("$VPY" "$SCRIPT_DIR/dispatch_meta.py" "$doc" 2>/dev/null); then
      if [ -z "${SKIP_LOGGED[$id]:-}" ]; then
        echo "  (skip) $id: no ## Dispatch block"
        SKIP_LOGGED[$id]=1
      fi
      continue
    fi
    model=$(echo "$meta" | jq -r '.model // "?"')
    title=$(grep -F "$id|" "$REPO_ROOT/CONSCIOUSNESS/tasks/TASK-BACKLOG-INDEX.md" | head -1 | cut -d'|' -f3)
    blocked_by=$(grep -F "$id|" "$REPO_ROOT/CONSCIOUSNESS/tasks/TASK-BACKLOG-INDEX.md" | head -1 | cut -d'|' -f8)
    printf "  %2d. %-10s %-60s model=%-8s wall_clock_cap=%ds blocked_by=%s (satisfied)\n" \
      "$((++count))" "$id" "${title:0:60}" "$model" "$TASK_TIMEOUT_S" "${blocked_by:-none}"
    [ -n "$ONLY_TASK" ] && break
  done <<< "$ready_ids"
  [ "$count" -eq 0 ] && echo "  (nothing dispatchable — spine empty or all blocked)"
  exit 0
fi

declare -A ATTEMPTS
declare -A FAILED
COMPLETED=0
FAILED_COUNT=0

while true; do
  next=$(select_next_task) || { log "spine empty — no dispatchable task remains"; break; }
  id="${next%%|*}"
  title="${next#*|}"

  if [ "$LIMIT" -gt 0 ] && [ "$COMPLETED" -ge "$LIMIT" ]; then
    log "reached --limit $LIMIT — stopping"
    break
  fi

  attempt=1
  extra=""
  ok=0
  if run_task "$id" "$title" "$attempt" ""; then
    ok=1
  else
    fail_log="$RUN_DIR/${id}.${attempt}.verify.log"
    extra=$(tail -c 4000 "$fail_log" 2>/dev/null)
    log "$id: attempt 1 failed, retrying once"
    attempt=2
    if run_task "$id" "$title" "$attempt" "$extra"; then
      ok=1
    fi
  fi

  if [ "$ok" -eq 1 ]; then
    COMPLETED=$((COMPLETED + 1))
    log "$id: DONE"
    doc=$(card_doc_path "$id" 2>/dev/null)
    feat_ids=$(awk -F'|' -v id="$id" 'NR>1 && $1==id {print $6}' "$REPO_ROOT/CONSCIOUSNESS/tasks/TASK-DONE-INDEX.md")
    IFS=',' read -ra FEATS <<< "$feat_ids"
    for f in "${FEATS[@]:-}"; do
      [ -z "$f" ] && continue
      if feature_tasks_all_done "$f"; then
        meta=$("$VPY" "$SCRIPT_DIR/dispatch_meta.py" "$doc" 2>/dev/null)
        rm_model=$(echo "$meta" | jq -r '.reviewer_model // "sonnet"')
        log "$f: all tasks done — dispatching review ($rm_model)"
        run_review "$f" "$rm_model"
      fi
    done
  else
    FAILED_COUNT=$((FAILED_COUNT + 1))
    log "$id: FAILED after 2 attempts — noting on card and continuing"
    doc=$(card_doc_path "$id" 2>/dev/null)
    if [ -n "$doc" ]; then
      {
        echo ""
        echo "## Run log"
        echo ""
        echo "- $(date -u +%Y-%m-%dT%H:%M:%SZ) orchestrator run $RUN_TS: FAILED after 2 attempts. See reports/run/$RUN_TS/${id}.*.json and .verify.log."
      } >> "$doc"
    fi
  fi

  if [ -n "$ONLY_TASK" ]; then
    log "--only $ONLY_TASK complete"
    break
  fi

  between_task_hooks
done

{
  echo ""
  echo "=== final table ==="
  printf "%-10s %-8s\n" "task" "status"
} >> "$RUN_LOG"

log "run end: completed=$COMPLETED failed=$FAILED_COUNT"

git -C "$REPO_ROOT" add -- "reports/run/$RUN_TS/run.log" 2>/dev/null
git -C "$REPO_ROOT" commit -m "chore(run): syllabus run $RUN_TS log" -- "reports/run/$RUN_TS/run.log" >/dev/null 2>&1 || true

if [ "$FAILED_COUNT" -gt 0 ]; then
  exit 1
fi
exit 0
