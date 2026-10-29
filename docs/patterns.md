# patterns.md

Named, reusable layout patterns. Each gives structure only — all values come from `docs/tokens.md`.
ASCII sketches show desktop; mobile collapses everything to a single column with reduced section
padding. Build pages as: `Nav → Hero → 1–2 content patterns → Data section → Closing band → Footer`.

## P1 — Hero: `<FullBleedHero>`

One screen (100svh). Full-bleed media (photo or muted looping video) with `--overlay` scrim, or
pure `--bg` field. Bottom-left anchored composition.

    ┌──────────────────────────────────────────────┐
    │ NAV                                          │
    │                                              │
    │                 (full-bleed media + scrim)   │
    │                                              │
    │ LABEL — eyebrow (uppercase, muted)           │
    │ THIS IS THE ONE CLAIM YOU MAKE{{ type-display }}  │
    │ short lead paragraph, --measure; accent rule │
    └──────────────────────────────────────────────┘

- Label sits directly on top of display with `--space-5` between; lead below with `--space-4`.
- Optional scroll cue: 1px vertical accent line, animated height pulse, bottom-right.
- Headline max ~10 words. This is the only `--type-display` on the page.

## P2 — `<SplitSection>`

The workhorse. Text block and media block, asymmetric spans (5/7 or 7/5) on the 12-col grid,
aligned to baseline top. Given id section anchors a headline in `--type-h1`.

    ├────────┬───────────────────────┤
    │ LABEL  │                       │
    │ H1     │     media (media      │
    │ lead   │     media (may        │
    │ body   │                       │

- Alternate sides between consecutive P2s (media right, then media left).
- Eyebrow label above headline, `--space-3` gap.
- Media is one image or video — never a collage, never a card with a border.

## P3 — `<StatRow>`

Data as aesthetic. 3–4 stats on one flex row, divided by hairlines, numbers in mono/display.

    8 × 24HR     │ 150 × M    │ 40,000 × FT
    ENDURANCE    │ PAYLOAD    │ CEILING

- Number: `--type-h1` at weight 300; unit: `--type-data` in `--fg-muted`; caption:
  `--type-label` uppercase below.
- Values left-aligned; vertical hairline separators (`--border`).
- Optionally animate numbers counting up once on reveal (mono, no easing wobble).

## P4 — `<SpecTable>`

The credibility block: a dense rows-of-facts table. Full content width, hairline row rules,
no stripes, no rounded corners, no backgrounds.

    LENGTH .......... 9.1 M
    MTOW ............ 1,814 KG
    CRUISE .......... 120 KT

- Left column `--type-label` uppercase muted; right column `--type-data` (mono) `--fg`.
- Leaders/dotted fill optional; row padding `--space-3` vertical.
- Header row optional: fields in `--type-label` with `--border` bottom, weight 500.

## P5 — `<QuietNav>`

Fixed top bar, height `--space-7`, no background on load. On scroll past 40px: `--bg` at 90%
opacity + 1px bottom hairline (frosted: `backdrop-filter: blur(8px)` is the only permitted blur).

    WORDMARK        CAPABILITIES  PRODUCTS  NEWS        [ CTA → ]

- Wordmark left (text is fine); links center-right; text link CTA uses uppercase `--type-label`
  with an arrow that translates 4px right on hover.
- Mobile: wordmark + menu button; open state is a full-screen `--bg` sheet with oversized
  `--type-h1` links, staggered `--dur` entrances.

## P6 — `<ImageBreak>`

Full-viewport-width media with a single short caption line in `--type-label` bottom-left over the
`--overlay`. No headline on media unless scrims guarantee ≥4.5:1. Alternates the rhythm between
text-dense sections.

## P7 — `<ClosingBand>`

Final content section before footer. `--bg` (or inverted theme via a `.theme-invert` wrapper).
Big `--type-h1` question/statement + one link-button. Nothing else.

    TWO WORDS MAX.
    CONTACT →

## P8 — `<QuietFooter>`

No dark card, no columns of marketing. Top row, four zones: wordmark; link groups
(`--type-body`, muted, hover → `--fg`); legal row in `--type-label` at `--fg-faint` with year +
bottom hairline. Total height modest — the footer is the quietest block on the page.

## Anti-patterns (auto-reject)

- Icon-in-rounded-square feature grids ("SaaS cards" with shadows). Use `<SpecTable>` or copy blocks.
- Center-aligned everything. Centers only inside `<StatRow>` and `<ClosingBand>` (and even there, prefer left).
- Button gradients, pill buttons >2px radius, glowing CTAs, pastel blobs.
- Carousel/slider testimonials. Use one quote block, large `--type-h2`, hairline above.
- Stock smiley-people photos. Use hardware, environments, sensors, data.
 - Decorative divider imagery (wave/curve SVG fillers). Dividers are hairlines or open space.
