# prompts.md — tested recipe phrasings

Copy these when asking agents for common tasks; adapt the BRACKETED parts. Each recipe cites the
system files so the agent doesn't guess its way back to generic output.

## Build a new homepage

    Using docs/tokens.md, docs/patterns.md and AGENTS.md in this repo, build <BRAND NAME>'s
    homepage. Copy: <one-paragraph brief>. Build exactly: FullBleedHero + 3–4 section trailers
    (01/02/03 labels) + ClosingBand + QuietFooter. Each trailer routes to a page named
    <kebab>.html using the stated detail archetype. Output files in example/. Use
    example/tokens.css as the stylesheet, page CSS = tokens only.

## Build a new detail page

    Following docs/patterns.md, add detail page <name>.html for homepage section <N> using
    archetype P<PX> (<Article|Gallery|SpecSheet|Log>). Start with DetailHeader (P13) + section
    trail, end with "Continue →" to <next page>. Extend example/ only.

## Convert an existing site to Spaceframe

    Audit <file> against AGENTS.md and docs/tokens.md, then rebuild it in place preserving all
    copy and URLs. Snap every color/size/duration to the nearest token. Run
    scripts/audit.py on the result and fix all findings before reporting back.

## Add one section to an existing page

    Add a <PatternName> section to <file> for claim "<CLAIM>". It must remain a trailer (label +
    headline + lead + one supporting element + Explore link) — max 5 trailers total on the
    homepage; if over, propose converting one into its own detail page instead.

## Audit pass (no rebuild)

    Run the aesthetic self-check and scripts/audit.py on <file>. Report violations as a table
    (rule | location | fix), then apply fixes. Do not redesign; only remove and snap to tokens.

## Copy rewrite

    Rewrite <file>'s copy in house voice (tokens.md §5): declarative, dry, specific, numbers over
    adjectives, sentence case, no exclamation marks, no hype words. Keep landmarks/labels.

## New accent for a different brand

    Derive a recolor: keep the structure, swap --accent (and --accent-dim/-ink) to
    <HEX or HUE>; verify all pairings keep ≥4.5:1 text contrast per rule 10; keep neutral ramp
    unchanged. Update tokens.css and tokens.md §1 value tables only — no other file changes.
