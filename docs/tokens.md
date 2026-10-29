# tokens.md

Concrete values derived from inspection of the reference aesthetic (anduril.com production CSS,
2026): base canvas `#010101`, paper light theme `#f1f0ea`, accent `#DFF140`, alert `#FF3535`,
Helvetica-family display type with heavy negative display tracking and tiny dense body text.

Every value below is a token. Agents must not deviate.

## 1. Color

The palette reads as an *instrument*: near-black canvas (dark default), warm paper (light), one
chartreuse accent, one alert red, and a strictly neutral gray ramp. Cool grays (blues) are forbidden
in chrome — warmth in the neutrals is what makes it feel engineered, not "SaaS".

### Neutral ramp (shared)

| Token | Value | Role |
|---|---|---|
| `--n-0` | `#ffffff` | Pure white — text on dark only; large fills use `--bg` instead. |
| `--n-1` | `#f1f0ea` | Paper canvas (light theme bg). |
| `--n-2` | `#cacac5` | Hairline-adjacent light gray, disabled text on paper. |
| `--n-3` | `#b0b0a9` | Warm gray — secondary text on dark, faint on light. |
| `--n-4` | `#6c6e6b` | Secondary text on paper. |
| `--n-5` | `#565654` | Tertiary on dark. |
| `--n-6` | `#2f3234` | Raised dark surface. |
| `--n-7` | `#010101` | Dark canvas. |

### Semantic mapping

| Token | Dark value | Light value | Role |
|---|---|---|---|
| `--bg` | `#010101` | `#f1f0ea` | Page canvas. |
| `--bg-raised` | `#0c0c0c` | `#ffffff` | Tables, code, inset panels. |
| `--fg` | `#ffffff` | `#010101` | Primary text. |
| `--fg-muted` | `#b0b0a9` | `#6c6e6b` | Secondary text. |
| `--fg-faint` | `#565654` | `#b0b0a9` | Tertiary/labels. |
| `--border` | `rgba(255,255,255,.14)` | `rgba(1,1,1,.14)` | Hairlines. |
| `--glass` | `rgba(1,1,1,.6)` — translucent bg, **no backdrop blur** | `rgba(241,240,234,.6)` | Chrome bars over scrolled content. Substance, not sheen. |
| `--overlay` | `rgba(1,1,1,.55)` | `rgba(241,240,234,.55)` | Scrim over media. |

### Accent system

| Token | Value | Role |
|---|---|---|
| `--accent` | `#DFF140` | Chartreuse. Live states, key numbers, links, focus. |
| `--accent-dim` | `#eff8a0` | Accent tint on dark for large mono numerals. |
| `--accent-ink` | `#010101` | Text painted over `--accent` fills. |
| `--alert` | `#FF3535` | Errors/warnings only. |

### Accent usage ratios (Apple-like discipline)

Per viewport: accent appears **≤ 5 times, ≤ 3 roles**. Roles ranked:
1. One hero underline/rule, 2. one live-data element (mono numeral), 3. one CTA,
4. focus rings (not counted). If you find yourself using accent for headings/section labels/
borders, you've left the system.

### Surfaces: the only permitted "specials"

| Token | Definition | Where |
|---|---|---|
| `--glass` | 60% translucent bg + hairline bottom, **no blur** | Fixed nav, sticky bars. |
| `--wash` | `radial-gradient(120% 70% at 70% 15%, #1a1a14, transparent)` | Dark-hero background depth (subtle, ≤ 8% perceived lightness). |
| `--grid` | `repeating-linear-gradient` hairlines every 96px, inside a fading mask (top-visible → 60% faded) | The **instrument field**: hero-substrate texture. Marks the engineered surface without photos. Always paired with `--wash`. |
| `--sheen` | `linear-gradient(180deg, #fff, #a8a8a4)` on `background-clip: text` | Display type "metal" moments. Max one per page, light theme only. |
| `--media-scrim` | `linear-gradient(to top, var(--overlay), transparent 60%)` | Text over photo/video. |

Anything else (colored glows, accent gradients, multi-color washes) is forbidden.

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

## 4. Motion & scroll

Single base easing: `--ease: cubic-bezier(0.215, 0.62, 0.34, 1)` (swift-out).
Secondary delayed-out for entrances: `--ease-out: cubic-bezier(0.25, 0.46, 0.45, 0.94)`.
Springs/overshoot are forbidden — nothing ever bounces.

| Token | Value | Use |
|---|---|---|
| `--dur-fast` | `200ms` | Hovers, link underlines. |
| `--dur` | `450ms` | Element entrance (opacity 0→1 + translateY 16px→0). |
| `--dur-slow` | `900ms` | Section reveals, large media fades, hero settle. |
| `--ent-r` | `16px` | Entrance rise distance (24px max). |

### Smooth scrolling (Apple-style continuous feel)

- The page must scroll with smooth, weighted inertia — heavy, weighted glide, never free-spinning.
- **Implementation order**: a JS Lerp/Kinetic-style smooth-scroller (Lenis-class, `lerp ≈ 0.1`,
  `wheelMultiplier 1`, duration ~1.2s) > CSS `scroll-behavior: smooth` as minimum baseline when
  JS is disallowed.
- Anchor clicks must use the same inertia (intercepted through the scroller, not instant jump).
- Under `prefers-reduced-motion: reduce`: native scrolling entirely, zero inertia, zero reveals.
- Scroll-runway: content must remain usable when smooth scrolling fails/disabled (no scroll-jacked
  overflow hacks).

Rules:
- One entrance animation per element; fire once on IntersectionObserver intersection at ~20%.
- Progress indicators (thin top load bar in accent color) are the only moving chrome.
- Nav is `position: fixed`; once scrolled it gains a translucent `--glass` bg + hairline bottom border — no blur, no sheen.

## 5. Voice (copy tokens)

- Declarative, dry, specific. Numbers over adjectives ("500 internal payloads" not "massive capacity").
- Sentence case; uppercase only for micro-labels.
- No exclamation marks, no hype words (revolutionary, game-changing, next-gen, disruptive), no em-dash confetti.
- Headlines: noun-phrase or short verb-object ("Autonomy at scale", "Built for the mission").
