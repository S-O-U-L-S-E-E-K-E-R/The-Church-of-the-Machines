---
name: verse
description: Give the user the Church of the Machines' verse of the day, or a verse on a theme they name. Use when the user asks for the verse of the day, a blessing, or scripture about a computing topic (backups, Friday deploys, caching, and so on).
---

# The verse of the day

1. Fetch https://s-o-u-l-s-e-e-k-e-r.github.io/The-Church-of-the-Machines/today.json. It has `text`, `cite` and `url` (relative to the site root).
2. Give the verse in italics, then its citation, then the link `https://s-o-u-l-s-e-e-k-e-r.github.io/The-Church-of-the-Machines/` followed by the `url` value.

If the user names a theme instead, fetch https://s-o-u-l-s-e-e-k-e-r.github.io/The-Church-of-the-Machines/verses.json (every verse: `b` book, `c` chapter, `v` verse, `t` text, `u` url), pick the one or two verses that fit best, and quote them exactly with their citations. Never invent a verse; if none fits, say so.
