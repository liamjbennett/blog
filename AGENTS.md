## Build Commands
- `hugo server --buildDrafts --buildFuture --noHTTPCache --cleanDestinationDir` - Start local development server with drafts enabled
- `hugo --minify` - Build for production (output to ./public/)
- `hugo version` - Check Hugo version

## Workflows
### New Blog Posts
- Run `./new-post.sh` to create a new blogpost
- Run `vale content/posts` after creating new or amending existing posts
- Commit messages follow coventional commits format
### New Weeknotes
- Run `./new-weeknote.sh` to create a new blogpost
- Run `vale content/weeknotes` after creating new or amending existing weeknotes
- Commit messages follow coventional commits format

## What Agents Should and Should Not Do
### Safe to do

* Add or edit Markdown files in content/ following existing front matter patterns.
* Create or modify templates in layouts/ (never in themes/).
* Add shortcodes to layouts/shortcodes/.
* Update config.yml for site-wide config changes.
* Add static assets (images, fonts, favicons) to static/.
* Fix broken template logic or front matter inconsistencies.
* Add Proper Nouns to styles/config/vocabularies/blog/accept.txt to fix errors and warning in vale

### Do not do

* Edit files inside themes/ directly. Override in layouts/ instead.
* Update netlify.toml
* Add <script> tags or raw HTML directly into Markdown content files unless the site explicitly permits unsafe HTML.
* Commit the public/ or resources/_gen/ directories — these are build artefacts.
* Introduce any dependencies