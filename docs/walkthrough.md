# walkthrough.md — full build, end to end

Worked example of a complete Spaceframe build (commits on main are this example's output).
Copy the decision sequence, not the copy itself.

## Brief
"Marketing site for Atlas Dynamics, an autonomy/perception software company for unmanned aerial
vehicles. Dry tone; audience: defense operators and program managers."

## Step 1 — clarify (3 questions max)
Ask only what tokens can't deliver: brand name ✓ (given), accent color, real media? For an
illustrative build: placeholder charts + Unsplash hardware imagery. Confirm answer in one line
in the PR/commit message.

## Step 2 — decide architecture before pixels
One page or five? This brief has 4 distinct claims (perception, provenance, datasheet, contact) →
homepage = FullBleedHero + 4 section trailers + ClosingBand; 3 trailers become detail pages
(systems→P9 Article, reliability→P10 Gallery, specs→P11 SpecSheet). Homepage never exceeds 5
sections (AGENTS.md architecture rule).

## Step 3 — tokens first, page later
Copy example/tokens.css verbatim. Page CSS = layout only, all values via `var(--…)`. Verify both
themes switch (`data-theme="light"` up front) before writing the first section.

## Step 4 — write the homepage bottom-up
1. Hero: eyebrow `.label` + one display line (~10 words) + 1-sentence lead. Confirm ratio: display
   ≥ 8× label.
2. Each trailer: label → `--type-h1` → 2-sentence lead → Explore link. Numbered labels, and
   **even trailers flip media side** (P2 pattern rule).
3. StatRow as trailer support for numeric claims (stats.html links).
4. ClosingBand: one statement + one CTA. Accent count ≤ 5.

## Step 5 — detail pages
Each starts with P13 DetailHeader + section trail (01 02 03 wayfinding). Archetype dictates body:
Article = prose column max `--measure`; Gallery = big media, captions only; SpecSheet = full table
then 2 application paragraphs. Every page foots with Continue → next page (site is a loop).

## Step 6 — motion pass
Add `.ent` reveals (IO threshold .2, once). Smooth scrolling per tokens.md §4 (Lenis-class if
allowed, CSS baseline otherwise). Then prefers-reduced-motion pass — verify frozen.

## Step 7 — gates
1. `python3 scripts/audit.py example/*.html` — every finding fixed, not waived.
2. AGENTS.md aesthetic self-check, honestly. If the page feels busy, remove the weakest element —
   deletions are free, additions are not.

## Step 8 — ship note
Commit per file-group (theme / homepage / detail pages), push, watch the deploy URL, then
capture before/after screenshots with scripts/shots.sh for the PR.
