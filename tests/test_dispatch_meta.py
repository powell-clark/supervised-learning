"""Tests for scripts/dispatch_meta.py."""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "dispatch_meta.py"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import dispatch_meta as dm  # noqa: E402


CARD_WITH_DISPATCH = """# TASK-XX001: Example

## Context

Some context.

## Dispatch

model: sonnet
effort: high
max_turns: 100
reviewer_model: sonnet

## Dependencies

- Blocked by: nothing
"""

CARD_WITHOUT_DISPATCH = """# TASK-XX002: No dispatch block

## Context

Nothing to see here.
"""

CARD_DISPATCH_AT_EOF = """# TASK-XX003: Dispatch last

## Dispatch

model: sonnet
effort: medium
max_turns: 40
reviewer_model: sonnet
"""

CARD_DISPATCH_INCOMPLETE = """# TASK-XX004: Missing a field

## Dispatch

model: sonnet
effort: high

## Dependencies
"""


class TestParseDispatchBlock:
    def test_parses_full_block(self):
        fields = dm.parse_dispatch_block(CARD_WITH_DISPATCH)
        assert fields == {
            "model": "sonnet",
            "effort": "high",
            "max_turns": 100,
            "reviewer_model": "sonnet",
        }

    def test_absent_block_returns_none(self):
        assert dm.parse_dispatch_block(CARD_WITHOUT_DISPATCH) is None

    def test_block_at_end_of_file(self):
        fields = dm.parse_dispatch_block(CARD_DISPATCH_AT_EOF)
        assert fields["model"] == "sonnet"
        assert fields["max_turns"] == 40

    def test_max_turns_is_int(self):
        fields = dm.parse_dispatch_block(CARD_WITH_DISPATCH)
        assert isinstance(fields["max_turns"], int)

    def test_stops_at_next_heading(self):
        fields = dm.parse_dispatch_block(CARD_WITH_DISPATCH)
        assert "blocked_by" not in fields


class TestMainCli:
    def test_exit_2_when_no_dispatch_block(self, tmp_path):
        card = tmp_path / "TASK-XX002.md"
        card.write_text(CARD_WITHOUT_DISPATCH, encoding="utf-8")
        assert dm.main([str(card)]) == 2

    def test_exit_2_when_missing_field(self, tmp_path):
        card = tmp_path / "TASK-XX004.md"
        card.write_text(CARD_DISPATCH_INCOMPLETE, encoding="utf-8")
        assert dm.main([str(card)]) == 2

    def test_exit_2_when_file_missing(self, tmp_path):
        assert dm.main([str(tmp_path / "nope.md")]) == 2

    def test_exit_2_wrong_argc(self):
        assert dm.main([]) == 2
        assert dm.main(["a", "b"]) == 2

    def test_prints_json_and_exits_0(self, tmp_path, capsys):
        card = tmp_path / "TASK-XX001.md"
        card.write_text(CARD_WITH_DISPATCH, encoding="utf-8")
        code = dm.main([str(card)])
        assert code == 0
        out = json.loads(capsys.readouterr().out)
        assert out == {
            "model": "sonnet",
            "effort": "high",
            "max_turns": 100,
            "reviewer_model": "sonnet",
        }

    def test_subprocess_end_to_end(self, tmp_path):
        card = tmp_path / "TASK-XX001.md"
        card.write_text(CARD_WITH_DISPATCH, encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), str(card)], capture_output=True, text=True
        )
        assert proc.returncode == 0
        assert json.loads(proc.stdout) == {
            "model": "sonnet",
            "effort": "high",
            "max_turns": 100,
            "reviewer_model": "sonnet",
        }

    def test_subprocess_exit_2_on_real_skipped_card(self):
        # TASK-SL017 is one of the cards deliberately skipped for carrying no
        # Dispatch block (consciousness-plugin observation, not curriculum work).
        candidates = list(
            (REPO_ROOT / "CONSCIOUSNESS" / "tasks").glob("*/TASK-SL017.md")
        )
        if not candidates:
            return  # card relocated or not present in this checkout; nothing to assert
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), str(candidates[0])], capture_output=True, text=True
        )
        assert proc.returncode == 2
