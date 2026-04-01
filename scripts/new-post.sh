#!/bin/bash

# Directory for posts
POST_DIR="content/posts"

# Get today's date
TODAY=$(date +%Y-%m-%d)

# Check if title was provided
if [ -z "$1" ]; then
  echo "❌ Error: No title provided."
  echo "Usage: $0 \"Post Title Here\""
  exit 1
fi

# Use first argument as the title
TITLE="$1"

# Slugify the title (lowercase, replace spaces with hyphens, remove special chars)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-+|-+$//g')


# Filename format: YYYY-MM-DD-title.md
FILENAME="${POST_DIR}/${TODAY}-${SLUG}.md"

# Create the markdown file with frontmatter
cat > "$FILENAME" <<EOF
---
author: "liamjbennett"
title: "${TITLE}"
date: "${TODAY}"
description: ""
tags: [""]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: ""
audio_length: ""
audio_bytes: ""
draft: true
---

XXX

EOF

echo "✅ Created new post: $FILENAME"

