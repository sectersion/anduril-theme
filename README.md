# Spaceframe — a directive-grade design system for AI agents

Imposes a clean, "precision hardware" marketing aesthetic (defense-tech minimalism with Apple-style ease) on anything an AI agent builds: dark-light tokenized themes, one chartreuse accent, big light-weight type with small dense body, quiet motion, multi-page architecture. **Tokenized, stack-agnostic, zero dependencies at runtime.**

**Live demo:** [anduril.vaultless.dev](https://anduril.vaultless.dev)

## What's inside

| Path | What it is |
|---|---|
| `AGENTS.md` | Non-negotiable rules, architecture model, aesthetic self-check |
| `docs/tokens.md` | Every value: colors, type scale, spacing, motion, voice |
| `docs/patterns.md` | 18 named layout patterns + architecture + anti-pattern reject list |
| `docs/evidence.md` | REA/CDP-captured reference evidence behind the patterns |
| `docs/prompts.md` | Copy-paste recipe phrasings for common agent asks |
| `docs/walkthrough.md` | End-to-end worked build (the reference tour) |
| `example/` | The reference site: index + 3 detail pages + 404 (this is what's deployed) |
| `scripts/audit.py` | Rule-lint for generated HTML (try `python3 scripts/audit.py example/index.html`) |
| `scripts/shots.sh` | Screenshot capture for visual regression checks |
| `.opencode/skills/spaceframe/SKILL.md` | OpenCode skill wrapper |
| `.github/workflows/screenshots.yml` | CI: captures full-page screenshots of all pages on every push |
| `docs/tokens.tailwind.css` | `@theme`-based color/typography/spacing tokens for Tailwind v4 projects |

## Quick start (humans)

Open `example/index.html`. Switch theme via `<html data-theme>`.

## Quick start (agents)

Drop the folder in your project, or point your agent at `AGENTS.md`. In OpenCode the bundled skill loads automatically.

## Deploying

Uses Cloudflare Workers Static Assets (see `wrangler.jsonc`): `npx wrangler deploy`, or point CI at the same command after `npx wrangler login`.
