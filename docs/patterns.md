# patterns.md

Named, reusable layout patterns. Each gives structure only — all values come from `docs/tokens.md`.
ASCII sketches show desktop; mobile collapses everything to a single column with reduced section
padding. Build pages as: `Nav → Hero → 1–2 content patterns → Data section → Closing band → Footer`.

## P1 — Hero: `<FullBleedHero>`

One screen (100svh). **The hero viewport must be set in material** (AGENTS.md rule 3): pick ONE of
(a) full-bleed media — photo or muted looping video under `--overlay`, or (b) the **instrument
field** — layered `--wash` on `--grid`, masked by `--field-mask` so the hairlines catch light near
the top and dissolve before the content zone. A flat single-color hero is a violation. The
field carries a second depth layer only if needed (a single faint radial *sheen point* at the
`--grid` horizon, never glow-colored). Bottom-left anchored composition.

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

## P14 — `<ProductCard>` (homepage gallery item; evidence.md §3.3)

The trailer for a product-level detail page. Full-width media photograph, then a caption row:
title (`.label` in `--fg`), one-line descriptor (`.lead muted`), and a top-anchored arrow
(`Explore →`-class link). Media may be depressingly static (still frame) or a muted loop; text
never sits on the image — the caption row is on `--bg` beneath. Height ≈ 70svh; consecutive cards
are separated only by hairlines, no card borders. Used only on gallery-style index pages.

## P15 — `<MegaNav>` (evidence.md §2)
Two-pane overlay menu: left column = **domains** (`--type-h2`, light weight), right column =
**all links revealed at once** for the active domain — never hover-toggled partial menus.
Keyboard: tab reaches panes in order; Esc closes. Overlay uses `--bg` at 100%, `--dur-slow`
staggered link entrance; closes to a hairline top nav.

## P16 — `<NewsRow>` (evidence.md §3.5)
One lead story (image + label + `--type-h2` title + date in `--type-data`) plus a compact index
list of further headlines with hairlines and dates. **Forbidden to reshape into a card carousel**
— the pattern is: 1 lead + text-only list. Ends with `All stories →` if more exist.

## Site architecture (AGENTS.md rule 11)

Homepage is an INDEX: hero + 3–4 section trailers (01/02/03 numbered labels matching detail
pages) + closing band. Each trailer's only job is to route you to its detail page.

### P9 — DetailPage: `<Article>`
DetailHeader (P13) → full-width `--measure` prose column (lead + 2–3 body paras) → one
`<ImageBreak>`-caliber media → prose → footer. Ratio: text-most. One link per paragraph block.

### P10 — DetailPage: `<Gallery>`
DetailHeader → 2–3 full-width media blocks stacked with `--space-9` between, each captioned
`--type-label`. Negligible text beyond captions. Ends in a 3-stat `<StatRow>`.

### P11 — DetailPage: `<SpecSheet>`
DetailHeader → large `<SpecTable>` (8–12 rows) → short application prose → CTA band.

### P12 — DetailPage: `<Log>`
DetailHeader → dated rows (date `--type-data` mono, event sentence), hairline-separated. Reads
like a mission log. Ends in CTA band.

### P13 — `<DetailHeader>` + section trail
Top-of-page block on all detail pages: eyebrow `.label` naming its homepage section ("01 —
Systems"), `--type-h1` title, lead. Below the headline, a horizontal trail of section links
(01 02 03, current one `--fg`, others `--fg-faint`, hairline above and below) — wayfinding
between sibling detail pages without a back-button.

## P17 — `<ProductDetail>` (evidence.md §5)
The hardware detail page. Fix order: **Header** (display title + one CTA, no paragraph above the
fold) → **Variants** (2–5 cards: name, characteristic label/value rows in mono values, CTA
bottom-right) → **Qualities** (one list of capability statements, hairline apart) → optional
SpecSheet (P4) → closing band. Variant cards: `--bg-raised` field, NO border — raised *value* is
the separator. Values with heavy tracking tension use the `.data` role lowercase.

## P18 — `<ThemeInvert>` (evidence.md §6)
A whole section that flips to the opposite palette (use for long-form/wordy artifacts inside a
dark page). Add `.theme-invert` on the section; it re-maps `--bg`/`--fg` locally. Maximum one per
page, minimum 60svh, always ends with a regular section — never adjacent to another invert or the
closing band. (All values stay tokens — the flip is re-mapping, not new colors.)
