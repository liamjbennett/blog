#!/bin/bash

# Set the content directory (adjust if yours is different)
CONTENT_DIR="content"

# Find all .md files and check for 'draft: true' in frontmatter
find "$CONTENT_DIR" -type f -name "*.md" | while read -r file; do
    if grep -qE '^draft:\s*true' "$file"; then
        echo "$file"
    fi
done

