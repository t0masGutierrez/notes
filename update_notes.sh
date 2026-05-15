#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

git pull --rebase --quiet
python3 update_notes.py

# Include untracked markdown files in the diff summary without staging content yet.
git add --intent-to-add -- '*.md'

if git diff --quiet -- '*.md'; then
    echo "Already up to date."
    exit 0
fi

git diff --numstat -- '*.md' | awk -F '\t' '{
    added = ($1 == "-" ? 0 : $1)
    deleted = ($2 == "-" ? 0 : $2)
    print $3 " (+" added " -" deleted ")"
}'

git add '*.md'
git commit --quiet -m "update notes"
git push --quiet

echo "Everything up-to-date"
