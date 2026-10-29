#!/usr/bin/env python3
"""Spaceframe rule-lint: flag violations of AGENTS.md in generated HTML.
Usage: python3 scripts/audit.py example/index.html example/systems.html
Exit 1 if findings exist."""
import re, sys
from pathlib import Path

ALLOWED_HEX = {"#010101", "#f1f0ea", "#ffffff", "#b0b0a9", "#565654", "#dff140",
               "#eff8a0", "#ff3535", "#cacac5", "#6c6e6b", "#2f3234", "#0c0c0c", "#1a1a14", "#a8a8a4"}
CSS_VAR = re.compile(r"var\(--[a-z0-9-]+\)|rgba?\(|let\(|\b[0-9.]+(px|rem|em|ms|s|vw|ch)\b", re.I)
STYLE_BLOCK = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)
INLINE_STYLE = re.compile(r'style="([^"]*)"')
HEX = re.compile(r"#[0-9A-Fa-f]{3,8}\b")
ACCENT = re.compile(r"(--accent(?!-)|btn--accent|accent-dim|accent-ink)")

def audits(path):
    s = Path(path).read_text()
    css = "".join(m.group(1) for m in STYLE_BLOCK.finditer(s)) + "".join(m.group(1) for m in INLINE_STYLE.finditer(s))
    out = []
    for h in {x.group(0).lower() for x in HEX.finditer(css)}:
        if h not in ALLOWED_HEX:
            out.append(("tokens-only (rule 1)", f"non-token color {h}"))
    for m in re.finditer(r"border-radius:\s*([0-9.]+)px", css):
        if float(m.group(1)) > 2:
            out.append(("radius ≤ 2px (rule 5)", m.group(0)))
    if re.search(r"box-shadow:", css):
        out.append(("no drop shadows (rule 5)", "box-shadow found"))
    if re.search(r"backdrop-filter:[^;]*(blur|(s)aturate?)", css, re.I):
        out.append(("no liquid glass (rule 5)", "backdrop-filter blur/saturate"))
    for m in re.finditer(r"(?:animation|transition)-duration:\s*([0-9.]+)ms", css):
        if float(m.group(1)) > 900:
            out.append(("durations ≤ 900ms (rule 6)", m.group(0)))
    n = len(ACCENT.findall(css))
    if n > 12:
        out.append(("accent restraint (rule 2)", f"{n} accent references"))
    if "<img" not in s and "--type-display" not in css and "display" not in css:
        out.append(("hierarchy", "no display type found"))
    for i, tag in enumerate(re.findall(r"<h([1-6])", s)):
        if int(tag) - i > 1:
            out.append(("heading order (rule 10)", f"h{tag} out of order"))
            break
    for img in re.finditer(r"<img[^>]*>", s):
        if "alt=" not in img.group(0):
            out.append(("alt text (rule 10)", img.group(0)[:60]))
    if 'footer' not in s.lower():
        out.append(("landmarks (rule 10)", "missing <footer>"))
    return out

def main(paths):
    bad = 0
    for p in paths:
        fs = audits(p)
        print(f"\n== {p} ({len(fs)} findings)")
        for rule, where in fs:
            print(f"  ✗ [{rule}] {where}")
        bad += bool(fs)
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
