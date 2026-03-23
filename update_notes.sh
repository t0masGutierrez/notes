#!/bin/bash
cd "$(dirname "$0")"
python3 update_notes.py
git add .
git commit -m "update notes"
git push
