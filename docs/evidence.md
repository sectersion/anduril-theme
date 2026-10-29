# evidence.md — observed reference behavior (CDP captures, 2026-10-29)

Facts below are **observed** from passive Chrome DevTools captures of anduril.com (scroll timing,
JS inventory, resource files) plus its shipped CSS. They ground the patterns in `docs/patterns.md`.
Values used by Spaceframe are *derived abstractions*, not copies: no assets, copy, or imagery.

## 1. Confirmed motion stack

| Component | Evidence | What it does | Spaceframe analog |
|---|---|---|---|
| **Lenis** (~18 KB) | shipped `lib/lenis.min.js` | Inertia smooth-scrolling; anchors glide, not jump | `--scroll-lerp` spec (tokens.md §4); Lenis-class scroller |
| **Theatre.js** (~98 KB) | shipped `lib/theatrejs.js` | Keyframed scroll-linked choreography (hero media parallax, sequence timing) | Replace with IntersectionObserver reveals + CSS transforms; scroll-scrub only when media demands it |
| **WebGL scene** (~1.5 MB app + shaders + Draco/Basis decoders) | `shaders/compiled.vs`, `geometry/*` Draco bins | 3D product turntables + particle globe on hero | Recreate as: full-bleed VIDEO or the instrument field (`--wash`+`--grid`) — two sanctioned paths, nothing else |
| **Load bar** | inline boot script | 3px top progress strip, accent `#DFF140`, ease `1000ms`, glow tip | Permitted: thin accent progress bar is the only moving chrome |
| **Algolia** | `lib/algolia.esm.js` | command palette search | Optional; keep keyboard-first, monospace results |

## 2. Confirmed interaction vocabulary (copy these)

- Scroll `stage` instead of scroll `state`: the page behaves like one continuous sequence, not
  independent sections. Sections hand off via hairline breaks while the media layer persists.
- Product/gallery cards navigate with a **top-right-arrow sprite** (their visual idiom for
  "goes to a real page") — Spaceframe's `Explore →` march.
- Nav is a **mega-menu with two panes**: left = domains (Air/Sea/Land/Space/Subterranean),
  right = related product links that match the hovered domain. Reproduced as P15.
- Fonts preloaded in two drops only: display regular + mono. Total self-hosted weights per page
  stay at ≤ 3 files (manifest has many, pages preload 2).

## 3. Confirmed structure facts (homepage, in order)

1. Boot bar + zero-JS shell paints instantly (`#010101` body before CSS loads).
2. Hero = full-viewport video with poster; single display-size claim set bottom-left.
3. Product gallery: 7 full-width media cards, each = image → one-line title → arrow link.
4. Platform band (Arsenal OS): wide media + paragraph + arrow.
5. News row: one lead story + prev/next chevrons (not a carousel of cards).
6. Two book banners ("Rebooting/Rebuild the Arsenal"): single media + arrow links.
7. Footer: four-column directory incl. domain/product cascades; hairline legal rows.

Distribution: > 50% viewport height is media; text blocks never exceed ~45% of any band.

## 4. Media policy

All imagery/video/3D comes from their CDN (Sanity + local assets) — **never assumed**. When
rebuilding: licensed media, generated footage, or the instrument field. Copy/imagery from the
reference site is not used; only structural facts above are.

## 5. Product detail pages (P6 capture, /steelfin, 2026-10-29)

Slice anatomy: `ProductHeaderSlice` (display title + CTA) → `ProductVariationsSlice`
(variant cards: characteristic container = label + value, CTA pinned bottom-right of card) →
`ProductQualitiesSlice` (single qualities list). Long-form specs load client-side (Sanity CMS);
the SSG shell ships the skeleton only — worth copying: strict slice registry, CMS-shaped sections.

## 6. Micro-features observed

| Mechanism | Behavior | Spaceframe stance |
|---|---|---|
| `.redacted` value treatment | classified-look **streamed text**: light-styled value characters with tightened tracking (`-.05em` to `-.1em`) | Wonderful for live/slowly-revealing data (mission telemetry, counters). **Banned for static content** — fake-redacting marketing copy is role-play slop. |
| `.Roller` odometer | digit-by-digit roller odometer (6-digit) with scale multiplier | Load once as a live counter for flight hours/stats in `<StatRow>`; number changes matter, not the roller |
| `.theme-light` blocks | whole sections flip palette on a dark page (their docs/book bands) | Use `.theme-invert` section wrappers only for printable/long-form artifacts — ≤ 1 per page |
| `--theme-color-background` | the meta theme-color flips (`#000` in light UI, `#fff` in dark UI context) | Per-theme `meta theme-color` in generated pages |
