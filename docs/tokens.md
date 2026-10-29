# tokens.md

Concrete values derived from inspection of the reference aesthetic (anduril.com production CSS,
2026): base canvas `#010101`, paper light theme `#f1f0ea`, accent `#DFF140`, alert `#FF3535`,
Helvetica-family display type with heavy negative display tracking and tiny dense body text.

Every value below is a token. Agents must not deviate.

## 1. Color

### Dark theme (`data-theme="dark"` — default)

| Token | Value | Role |
|---|---|---|
| `--bg` | `#010101` | Page canvas. True near-black, never `#000` for surfaces with type. |
| `--bg-raised` | `#0c0c0c` | Tables, code blocks, inset panels. |
| `--fg` | `#ffffff` | Primary text, icons. |
| `--fg-muted` | `#b0b0a9` | Secondary text (warm gray — never pure `#888`). |
| `--fg-faint` | `#565654` | Tertiary/labels on dark, inactive. |
| `--accent` | `#DFF140` | Chartreuse accent. Links, live data, key numbers, focus rings. |
| `--accent-dim` | `#eff8a0` | Accent tint for large data strokes on dark. |
| `--alert` | `#FF3535` | Errors, warning badges. |
| `--border` | `rgba(255,255,255,.14)` | Hairlines, dividers, table rules. |
| `--overlay` | `rgba(1,1,1,.55)` | Scrim over media for text contrast. |

### Light theme (`data-theme="light"`)

| Token | Value | Role |
|---|---|---|
| `--bg` | `#f1f0ea` | Warm paper, never pure white. |
| `--bg-raised` | `#ffffff` | Tables, panels. |
| `--fg` | `#010101` | Primary text. |
| `--fg-muted` | `#6c6e6b` | Secondary text. |
| `--fg-faint` | `#b0b0a9` | Tertiary. |
| `--accent` | `#010101` | On paper, the accent *withdraws* — accent usage becomes black underlines/marks. |
| `--alert` | `#FF3535` | Same. |
| `--border` | `rgba(1,1,1,.14)` | Hairlines. |

Rules:
- Never use more than one accent hue per page. `--alert` only when semantically required.
- Media (photo/video) is allowed to carry any colors; UI chrome around it stays in the palette.

## 2. Typography

Family stack: `"Helvetica Now Display", "Neue Haas Grotesk", Inter, Helvetica, Arial, sans-serif`.
If loading a webfont, target weights 300/400/500 only. A secondary mono ("Elios"-like: use
`"Berkeley Mono", "JetBrains Mono", ui-monospace`) is reserved for data, units, IDs, and micro-labels.

| Token | Size (desktop → mobile via clamp) | Weight | Tracking | Line-height | Use |
|---|---|---|---|---|---|
| `--type-display` | `clamp(3rem, 8vw, 14rem)` | 300 (light) | `-0.04em` | 0.95 | Page heros, one per viewport max |
| `--type-h1` | `clamp(2rem, 4vw, 4rem)` | 300–400 | `-0.03em` | 1.02 | Section headlines |
| `--type-h2` | `clamp(1.25rem, 2vw, 2rem)` | 400 | `-0.02em` | 1.15 | Sub-headlines |
| `--type-body` | `0.9375rem` | 400 | `-0.011em` | 1.55 | Paragraphs (deliberately small & dense) |
| `--type-lead` | `1.125rem` | 400 | `-0.015em` | 1.5 | First paragraph after a headline |
| `--type-label` | `0.75rem` | 500 | `+0.06em` | 1.3 | Uppercase micro-labels, eyebrow (nav, section tags) |
| `--type-data` | `0.9375rem` | 400 | `0` | 1.4 | Mono, tables, stats |

Rules:
- **Display is light and enormous; body is small and dense.** The tension between the two is the
  signature of the style. Never set body copy large.
- Eyebrow labels are `uppercase`, `--fg-muted`, always paired with a headline.
- Max measure: body 68ch; headlines 12 words.
- Headline rhythm: display → lead → body → label. That's the standard unit; reuse it.

## 3. Spacing & layout

Base-8 scale: `--space-1: 4px; --space-2: 8px; --space-3: 16px; --space-4: 24px;
--space-5: 32px; --space-6: 48px; --space-7: 64px; --space-8: 96px; --space-9: 128px;`

| Token | Value | Use |
|---|---|---|
| `--gutter` | `clamp(24px, 6vw, 96px)` | Page side padding. Content never touches edges. |
| `--max-w` | `1440px` | Content max width (media may bleed to viewport edge). |
| `--measure` | `68ch` | Body copy max. |
| `--space-section` | `clamp(96px, 14vw, 192px)` | Vertical padding per section — generous by design. |
| `--gap-grid` | `--space-5` | Gap between grid columns. |
| `--border-hair` | `1px` | All borders. Never thicker. |
| `--radius` | `0` | Default. `2px` max for interactive states. |

Grid: 12-column, but *use asymmetric placements* — text spans 5 cols offset opposite a media
span of 7. Full symmetry is forbidden between a text block and its media block.

## 4. Motion

Single easing everywhere: `--ease: cubic-bezier(.215,.62,.34,1)`.

| Token | Value | Use |
|---|---|---|
| `--dur-fast` | `200ms` | Hovers, link underlines. |
| `--dur` | `450ms` | Element entrance (opacity 0→1 + translateY 16px→0). |
| `--dur-slow` | `700ms` | Section reveals, large media fades. |
| `--ent-r` | `16px` | Entrance rise distance. |

Rules:
- One entrance animation per element; fire once on IntersectionObserver intersection at ~20%.
- Reference uses smooth scrolling (Lenis); acceptable, but only behind `prefers-reduced-motion` guards.
- Progress indicators (thin top load bar in accent color) are the only moving chrome.
- All motion suppressed under `@media (prefers-reduced-motion: reduce)`.

## 5. Voice (copy tokens)

- Declarative, dry, specific. Numbers over adjectives ("500 internal payloads" not "massive capacity").
- Sentence case; uppercase only for micro-labels.
- No exclamation marks, no hype words (revolutionary, game-changing, next-gen, disruptive), no em-dash confetti.
- Headlines: noun-phrase or short verb-object ("Autonomy at scale", "Built for the mission").
