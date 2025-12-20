#!/bin/bash

# Directory for weeknotes
WEEKNOTE_DIR="content/weeknotes"

# Get current year
CURRENT_YEAR=$(date +%Y)

# Get today's date
TODAY=$(date +%Y-%m-%d)

# Find the highest weeknote number so far
LAST_NUM=$(ls -1 "${WEEKNOTE_DIR}/${CURRENT_YEAR}"/*-weeknote-*.md 2>/dev/null \
  | grep -oE 'weeknote-[0-9]+' \
  | grep -oE '[0-9]+' \
  | sort -n \
  | tail -n 1)

if [ -z "$LAST_NUM" ]; then
  NEXT_NUM=1
else
  NEXT_NUM=$((LAST_NUM + 1))
fi

# Always calculate the previous week's Monday and Friday
MONDAY=$(date -v -1w -v +1d +%d-%b-%Y)
FRIDAY=$(date -v -1w -v +5d +%d-%b-%Y)

# Filename format: YYYY-MM-DD-weeknote-NN.md
FILENAME="${WEEKNOTE_DIR}/${CURRENT_YEAR}/${TODAY}-weeknote-${NEXT_NUM}.md"

# Create the markdown file with frontmatter
cat > "$FILENAME" <<EOF
---
author: "liamjbennett"
title: "Week Note ${NEXT_NUM}"
date: "${TODAY}"
description: "${MONDAY} - ${FRIDAY}"
series: ["weeknotes"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
draft: true
---

XXX
<p/>

* -
<p/>
 
* -
<p/>

* -
<p/>

* -
<p/>

📈 - This weeks stats:
* XX minutes of podcasts
* XX average weekly steps
* XX book pages read
<p/>

📺 - This weeks background entertainment:
*
*

EOF

echo "✅ Created new weeknote: $FILENAME"

