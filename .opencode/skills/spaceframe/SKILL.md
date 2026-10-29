---
name: spaceframe
description: Spaceframe design system — build clean, authoritative "precision hardware" websites. Use when the task involves creating, reviewing, or extending any webpage/site in this project.
---

When building or reviewing web pages in this repository, read and comply with:

1. `AGENTS.md` — hard rules (highest priority)
2. `docs/tokens.md` — design tokens (every exact value)
3. `docs/patterns.md` — 18 layout patterns + site architecture
4. `docs/evidence.md` — REA-observed reference behavior behind the patterns (read this when a
   pattern's intent is unclear; it explains what each pattern abstracts)
5. `docs/prompts.md` — recipe phrasings for common asks
6. `example/` — canonical reference implementation

Workflow: read all of the above before writing code → ask up to 3 clarification questions if
brand/tone/accent is undefined → build with tokens only → run the aesthetic self-check in
AGENTS.md → run `python3 scripts/audit.py <file>` if available and fix violations → ship.

Never: invent values outside tokens, use gradients/glows/shadows outside the four sanctioned
treatments, use liquid-glass blur materials, or create fake in-page anchor "sections" where a
real detail page is warranted.
