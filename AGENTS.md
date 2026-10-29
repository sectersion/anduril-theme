# Spaceframe — Directive-Grade Web Design System

A design system for AI agents building clean, authoritative, "precision hardware" marketing
websites in the engineering-defense aesthetic. The vibe: an engineered instrument, not a template.
Authority through restraint. Every element must earn its place.

File map:

- `AGENTS.md` — non-negotiable rules (highest priority)
- `docs/tokens.md` — design tokens (colors, type, spacing, motion)
- `docs/patterns.md` — named layout/component patterns
- `example/` — reference implementation (`index.html` + `tokens.css`); use as canonical baseline

Resolution order when guidance seems ambiguous or conflicting:

1. `AGENTS.md` hard rules win over everything.
2. `docs/tokens.md` for any concrete value (never invent values — pick nearest token).
3. `docs/patterns.md` for layout structure.
4. `example/` for verbatim baselines to adapt.

## Hard rules (never violate)

1. **Tokens only.** Every color, size, duration, and easing comes from `docs/tokens.md` or
   `example/tokens.css`. Never write ad-hoc values (no `#3af`, no `font-size: 17px`, no `7px` gaps).
   Snap any requested odd value to the nearest token.
2. **One accent.** `--accent` is used for emphasis, interactive affordances, and data highlights
   only. Never as a background wash for large areas. Never compete with photography.
3. **Whitespace is a feature.** Section padding is generous (see `--space-section`). If a section
   feels empty, that is correct. Do not fill it with decoration — fewer, larger elements.
4. **One idea per section.** A section states one claim in one headline, optionally with one
   supporting block (image, table, or paragraph group). Never combine three pitches in one band.
5. **No decoration without information.** No soft rounded cards with drop shadows, no stock
   illustration, no random gradients. The only permitted "surface treatments" come from tokens:
   hairline borders (`--border`), frosted glass (`--glass` on the nav), and *deliberate* sheen
   gradients that imitate how light falls on metal/glass — defined in tokens.md, applied only to
   display typography or media scrims, never as decorative blobs. Corners are square or barely
   rounded (`--radius: 0–2px`). Drop shadows are forbidden except on the nav/floating glass layer.
6. **Motion is quiet and continuous.** Pages scroll smoothly (heavier inertia than native-default;
   see tokens.md §4), entries are fade + 16–24px rise with a single defined easing, hovers are
   state-only (nothing moves more than 4px). Durations 300–900ms. Nothing bounces, nothing
   parallax-jitters, no autoplaying sound.
7. **Typography carries hierarchy.** Bigger/lighter for display, smaller/denser for body,
   uppercase micro-labels for wayfinding. Never use color or size alone when weight + tracking can
   do it; never use more than 4 text sizes in one viewport.
8. **Communication-first.** If requirements are missing (brand name, tone, audience, accent
   color), ask up to 3 pointed questions before generating. Never invent logo imagery or copy
   trademarked names.
9. **Respect `prefers-reduced-motion`** and `prefers-color-scheme` (see example) in every build.
10. **Semantic, accessible HTML.** Landmarks (`header/main/footer/nav`), real headings in order,
   alt text, ≥4.5:1 text contrast, visible focus states, keyboard-operable nav. Attachment is not
    an excuse for `<div>` soup.

## Aesthetic self-check (run before finishing)

- [ ] Can I delete anything without losing information? If yes — delete it.
- [ ] Is there exactly one accent color, used ≤ 5 times per page?
- [ ] Is the largest piece of text at least 8× the size of the smallest?
- [ ] Do all sections alternate media/text sides or density? (no wall of sameness)
- [ ] Would a screenshot read as "engineered" at 20% zoom (strong grid, strong contrast)?
- [ ] Zero gradients? Zero border-radius above token? Zero shadows above frosted overlay?
- [ ] All values from tokens?

## Generation workflow

1. Read `docs/tokens.md`, `docs/patterns.md` fully before writing code.
2. Copy `example/tokens.css` verbatim as the base (including both `data-theme`s).
3. Build page from `docs/patterns.md` sections in order: nav → hero → one or two content
   patterns → data section → closing band → footer.
4. Write copy in the house voice: declarative, dry, specific, no exclamation marks, no
   "revolutionary/disruptive/game-changing". Numbers beat adjectives.
5. Run the aesthetic self-check, then fix violations.
6. Ship — never ask for permission to remove something; removal is the default.
