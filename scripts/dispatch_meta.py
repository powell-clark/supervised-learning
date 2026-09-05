#!/usr/bin/env python3
"""Print a task card's ``## Dispatch`` block as JSON.

Usage: dispatch_meta.py <card.md>

Exits 2 when the card carries no ``## Dispatch`` block (TASK-SL017, SL018,
SL019, SL023 are deliberately skipped this way — consciousness-plugin
observations, not curriculum work).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_SECTION_RE = re.compile(r"^##\s+Dispatch\s*$", re.MULTILINE)
_NEXT_HEADING_RE = re.compile(r"^##\s+\S", re.MULTILINE)
_FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_ ]*):\s*(.+?)\s*$", re.MULTILINE)

INT_FIELDS = {"max_turns"}


def parse_dispatch_block(text: str) -> dict | None:
    m = _SECTION_RE.search(text)
    if not m:
        return None
    start = m.end()
    rest = text[start:]
    nxt = _NEXT_HEADING_RE.search(rest)
    block = rest[: nxt.start()] if nxt else rest

    fields: dict = {}
    for fm in _FIELD_RE.finditer(block):
        key = fm.group(1).strip().lower().replace(" ", "_")
        value = fm.group(2).strip()
        if key in INT_FIELDS:
            try:
                value = int(value)
            except ValueError:
                pass
        fields[key] = value
    return fields


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) != 1:
        print("usage: dispatch_meta.py <card.md>", file=sys.stderr)
        return 2

    path = Path(argv[0])
    if not path.is_file():
        print(f"dispatch_meta: no such card: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    fields = parse_dispatch_block(text)
    if fields is None:
        print(f"dispatch_meta: no ## Dispatch block in {path}", file=sys.stderr)
        return 2

    required = ("model", "effort", "max_turns", "reviewer_model")
    missing = [f for f in required if f not in fields]
    if missing:
        print(f"dispatch_meta: Dispatch block missing {missing} in {path}", file=sys.stderr)
        return 2

    print(json.dumps({k: fields[k] for k in required}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
