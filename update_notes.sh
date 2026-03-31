#!/bin/bash
cd "$(dirname "$0")"
git pull --rebase
python3 update_notes.py
git add "*.md"
git diff --cached --quiet || git commit -m "update notes"
git push
