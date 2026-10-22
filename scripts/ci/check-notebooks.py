#!/usr/bin/env python3
"""Repository checks for the curriculum, run by CI (.github/workflows/notebooks.yml) and the pre-push hook.

1. Every tracked notebook is valid nbformat-4 JSON: a cells list whose cells carry a known cell_type and a source.
2. No tracked text file holds an absolute home-directory path for a real user. Placeholders such as /home/user,
   /home/runner and /Users/user are allowed.
3. No tracked file is an AI-session transcript (a JSONL record carrying both "sessionId" and "parentUuid").

Prints file names and counts only, never the matched text. Standard library only.
"""
import json
import re
import subprocess
import sys

PLACEHOLDER_USERS = {
    'user', 'username', 'runner', 'you', 'yourname', 'your-name', 'me', 'name', 'someone', 'somebody',
    'example', 'ubuntu', 'linuxbrew', 'shared', 'public', 'default', 'guest', 'jovyan', 'codespace', 'vscode',
}
HOME = re.compile(rb'(?<![A-Za-z0-9._~-])(?:/home[/]|/Users[/]|[A-Za-z]:\\\\?Users\\\\?)([A-Za-z0-9._-]+)')
TRANSCRIPT = (re.compile(rb'"sessionId"\s*:'), re.compile(rb'"parentUuid"\s*:'))


def tracked():
    out = subprocess.run(['git', 'ls-files', '-z'], check=True, stdout=subprocess.PIPE).stdout
    return [p.decode() for p in out.split(b'\0') if p]


def main():
    failures = 0
    files = tracked()
    notebooks = [f for f in files if f.endswith('.ipynb')]
    for nb in notebooks:
        try:
            with open(nb, encoding='utf-8') as fh:
                doc = json.load(fh)
            ok = doc.get('nbformat') == 4 and isinstance(doc.get('cells'), list) and all(
                isinstance(c, dict) and c.get('cell_type') in ('code', 'markdown', 'raw')
                and isinstance(c.get('source'), (str, list)) for c in doc['cells'])
        except (OSError, ValueError, UnicodeDecodeError) as exc:
            print(f'::error file={nb}::notebook does not parse ({type(exc).__name__})')
            failures += 1
            continue
        if not ok:
            print(f'::error file={nb}::not a valid nbformat-4 notebook')
            failures += 1
    home_hits, transcripts = 0, 0
    for f in files:
        try:
            with open(f, 'rb') as fh:
                data = fh.read()
        except OSError:
            continue
        if b'\0' in data[:8192]:
            continue
        n = sum(1 for m in HOME.finditer(data) if m.group(1).decode().lower() not in PLACEHOLDER_USERS)
        if n:
            print(f'::error file={f}::{n} absolute home-directory path(s) for a real user; use a relative path or /home/user')
            home_hits += n
            failures += 1
        if f.endswith(('.jsonl', '.json')) and all(rx.search(data) for rx in TRANSCRIPT):
            print(f'::error file={f}::looks like an AI-session transcript; transcripts stay local')
            transcripts += 1
            failures += 1
    print(f'[check-notebooks] notebooks checked: {len(notebooks)}; files scanned: {len(files)}; '
          f'home-path hits: {home_hits}; transcripts: {transcripts}; failures: {failures}')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
