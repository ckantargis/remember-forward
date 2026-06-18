#!/usr/bin/env python3
"""
build_plate02_v3.py
Plate 02 v3 — Water: Filter and Purify
Proof-of-concept for the role-based pictogram style system.

Style rules demonstrated:
  - ISOTYPE silhouettes       → consequence strip figures (healthy / sick)
  - Cross-section cutaway     → filter layer diagram
  - Sequence panels           → collection steps + use steps
  - Side elevation            → collection figures (person at riverbank)
"""

import os, sys

OUTDIR = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02_v3_water_filter.svg')

lines = []

def out(s): lines.append(s)

# ─── ISOTYPE FIGURE HELPERS ──────────────────────────────────────────────────

def fig_standing(cx, cy, s=1.0):
    """Standing healthy figure, filled black, top of head at cy."""
    r = 5.5*s
    bw, bh = 9*s, 15*s
    bx2 = cx - bw/2
    by2 = cy + 2*r + 1*s
    out(f'<circle cx="{cx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    out(f'<rect x="{bx2:.1f}" y="{by2:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{2.5*s:.1f}" fill="black"/>')
    out(f'<rect x="{cx+bw/2:.1f}" y="{by2+2*s:.1f}" width="{3*s:.1f}" height="{10*s:.1f}" rx="{1.5*s:.1f}" fill="black" transform="rotate(20,{cx+bw/2:.1f},{by2+2*s:.1f})"/>')
    out(f'<rect x="{cx-bw/2-3*s:.1f}" y="{by2+2*s:.1f}" width="{3*s:.1f}" height="{10*s:.1f}" rx="{1.5*s:.1f}" fill="black" transform="rotate(-20,{cx-bw/2:.1f},{by2+2*s:.1f})"/>')
    out(f'<rect x="{cx+1*s:.1f}" y="{by2+bh:.1f}" width="{3*s:.1f}" height="{13*s:.1f}" rx="{1.5*s:.1f}" fill="black" transform="rotate(5,{cx+1*s:.1f},{by2+bh:.1f})"/>')
    out(f'<rect x="{cx-4*s:.1f}" y="{by2+bh:.1f}" width="{3*s:.1f}" height="{13*s:.1f}" rx="{1.5*s:.1f}" fill="black" transform="rotate(-5,{cx-1*s:.1f},{by2+bh:.1f})"/>')

def fig_sick(cx, cy, s=1.0):
    """Bent-over sick figure."""
    r = 5*s
    # head drooped forward
    hx, hy = cx + 9*s, cy + 14*s
    out(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{r:.1f}" fill="black"/>')
    # torso: thick diagonal line (back bent forward)
    out(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{hx:.1f}" y2="{hy-r:.1f}" stroke="black" stroke-width="{5*s:.1f}" stroke-linecap="round"/>')
    # legs straight down from hip
    out(f'<line x1="{cx+2*s:.1f}" y1="{cy:.1f}" x2="{cx+3*s:.1f}" y2="{cy+20*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{cx-2*s:.1f}" y1="{cy:.1f}" x2="{cx-3*s:.1f}" y2="{cy+20*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')

def fig_crouching(cx, cy, s=1.0):
    """Crouching figure reaching toward ground."""
    r = 5*s
    # head: slightly forward
    hx, hy = cx + 5*s, cy + r
    out(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{r:.1f}" fill="black"/>')
    # back: thick horizontal stroke
    hip_x, hip_y = cx - 5*s, cy + r*2 + 9*s
    shl_x, shl_y = cx + 12*s, cy + r*2 + 2*s
    out(f'<line x1="{hip_x:.1f}" y1="{hip_y:.1f}" x2="{shl_x:.1f}" y2="{shl_y:.1f}" stroke="black" stroke-width="{5*s:.1f}" stroke-linecap="round"/>')
    # arm reaching down
    out(f'<line x1="{shl_x:.1f}" y1="{shl_y+3*s:.1f}" x2="{shl_x+5*s:.1f}" y2="{hip_y+8*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')
    # legs bent
    out(f'<line x1="{hip_x:.1f}" y1="{hip_y:.1f}" x2="{hip_x-4*s:.1f}" y2="{hip_y+12*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x-4*s:.1f}" y1="{hip_y+12*s:.1f}" x2="{hip_x+4*s:.1f}" y2="{hip_y+14*s:.1f}" stroke="black" stroke-width="{2.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x+4*s:.1f}" y1="{hip_y:.1f}" x2="{hip_x+2*s:.1f}" y2="{hip_y+15*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')

# ─── MATERIAL PATTERNS (reused from review) ──────────────────────────────────

def defs_and_patterns():
    out('''<defs>
  <!-- Charcoal: angular black chunks -->
  <pattern id="coal" x="0" y="0" width="28" height="22" patternUnits="userSpaceOnUse">
    <rect width="28" height="22" fill="white"/>
    <polygon points="1,3 13,1 17,8 13,17 2,18 0,9" fill="black"/>
    <polygon points="16,2 27,0 28,11 23,19 16,16 14,8" fill="black"/>
  </pattern>
  <!-- Sand: stipple dots -->
  <pattern id="sand" x="0" y="0" width="8" height="7" patternUnits="userSpaceOnUse">
    <circle cx="4" cy="3.5" r="1.8" fill="#111"/>
    <circle cx="0" cy="7" r="1.8" fill="#111"/>
    <circle cx="8" cy="7" r="1.8" fill="#111"/>
  </pattern>
  <!-- Gravel: rounded ovals -->
  <pattern id="grav" x="0" y="0" width="36" height="28" patternUnits="userSpaceOnUse">
    <rect width="36" height="28" fill="white"/>
    <ellipse cx="9"  cy="8"  rx="7" ry="5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="26" cy="7"  rx="7.5" ry="4.5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="7"  cy="21" rx="5" ry="3.5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="24" cy="21" rx="8" ry="5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="34" cy="19" rx="3.5" ry="2.8" fill="none" stroke="black" stroke-width="1.1"/>
  </pattern>
  <!-- Filter clip paths -->
  <clipPath id="c-coal"><polygon points="154,116 326,116 319,172 161,172"/></clipPath>
  <clipPath id="c-sand"><polygon points="161,172 319,172 312,230 168,230"/></clipPath>
  <clipPath id="c-grav"><polygon points="168,230 312,230 302,348 178,348"/></clipPath>
  <!-- Arrow marker -->
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
  <marker id="arrsm" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="4" markerHeight="4" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
</defs>''')

# ─── GENERATE SVG ────────────────────────────────────────────────────────────

out('<?xml version="1.0" encoding="UTF-8"?>')
out('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">')
out('<rect width="480" height="680" fill="white"/>')

defs_and_patterns()

# STYLE
out('''<style>
text { font-family: Georgia, serif; fill: black; }
</style>''')

# BORDERS
out('<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="black" stroke-width="3"/>')
out('<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="black" stroke-width="0.75"/>')

# ── HEADER ────────────────────────────────────────────────────────────────────
out('<text x="240" y="32" font-size="11" font-weight="bold" text-anchor="middle" letter-spacing="2">WATER — FILTER AND PURIFY</text>')
out('<line x1="18" y1="38" x2="462" y2="38" stroke="black" stroke-width="1"/>')
out('<text x="240" y="50" font-size="7" text-anchor="middle" letter-spacing="1.5">PLATE 02 · SURVIVAL KNOWLEDGE · CLEAN WATER PREVENTS ILLNESS AND DEATH</text>')
out('<line x1="18" y1="56" x2="462" y2="56" stroke="black" stroke-width="0.5"/>')

# ══ SECTION A — CONSEQUENCE STRIP (WHY) ══════════════════════════════════════
# Two panels: CONTAMINATED → SAFE, showing figures
out('<text x="240" y="68" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2.5">— WHY THIS MATTERS —</text>')

# Left panel: dirty water + sick person
out('<rect x="20" y="72" width="200" height="64" fill="none" stroke="black" stroke-width="0.8"/>')
# Dirty wavy water symbol (dark, thick waves)
for i, xi in enumerate([30, 48, 66, 84, 102, 120, 138, 156, 174, 192, 210]):
    if xi < 215:
        y1 = 82 + (4 if i % 2 == 0 else 0)
        out(f'<path d="M {xi} {y1} Q {xi+5} {y1-5} {xi+9} {y1}" fill="none" stroke="black" stroke-width="2.2"/>')
out('<text x="60" y="99" font-size="7.5" font-weight="bold" text-anchor="middle">CONTAMINATED</text>')
out('<text x="60" y="109" font-size="6.5" font-style="italic" text-anchor="middle">murky · smells · standing</text>')

# Sick figure (right side of left panel, small scale)
fig_sick(170, 78, s=0.85)
out('<text x="170" y="132" font-size="7" font-weight="bold" text-anchor="middle">ILLNESS</text>')

# Arrow between panels
out('<text x="229" y="108" font-size="14" text-anchor="middle">→</text>')

# Right panel: clean drops + healthy person
out('<rect x="260" y="72" width="200" height="64" fill="none" stroke="black" stroke-width="0.8"/>')
# Clean water drops
for dx in [280, 295, 310]:
    out(f'<path d="M {dx} 82 Q {dx-4} 92 {dx} 96 Q {dx+4} 92 {dx} 82" fill="black"/>')
out('<text x="320" y="99" font-size="7.5" font-weight="bold" text-anchor="middle">FILTERED + BOILED</text>')
out('<text x="320" y="109" font-size="6.5" font-style="italic" text-anchor="middle">clear · no smell · safe to drink</text>')

# Healthy standing figure (right side of right panel)
fig_standing(420, 74, s=0.85)
out('<text x="420" y="132" font-size="7" font-weight="bold" text-anchor="middle">HEALTHY</text>')

out('<line x1="18" y1="140" x2="462" y2="140" stroke="black" stroke-width="0.75"/>')

# ══ SECTION B — FILTER CROSS-SECTION (left column) ═══════════════════════════
out('<text x="122" y="152" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— BUILD THE FILTER —</text>')
out('<text x="122" y="162" font-size="6" font-style="italic" text-anchor="middle">cross-section view · layer order critical</text>')

# Dirty water arrows in
for xi in [190, 210, 230]:
    out(f'<line x1="{xi}" y1="108" x2="{xi}" y2="112" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')

# Container outline (trapezoid, slightly smaller than review)
out('<polygon points="154,112 326,112 302,350 178,350" fill="none" stroke="black" stroke-width="3.5"/>')
out('<ellipse cx="240" cy="112" rx="86" ry="7" fill="white" stroke="black" stroke-width="2.2"/>')

# Dirty water arrows (inside container top)
for xi in [200, 220, 240, 260, 280]:
    out(f'<line x1="{xi}" y1="108" x2="{xi}" y2="116" stroke="black" stroke-width="1.0" marker-end="url(#arrsm)"/>')
out('<text x="240" y="106" font-size="7" font-style="italic" text-anchor="middle">dirty water ↓</text>')

# Drain gaps at bottom
out('<line x1="178" y1="350" x2="198" y2="350" stroke="black" stroke-width="3.5"/>')
out('<line x1="220" y1="350" x2="260" y2="350" stroke="black" stroke-width="3.5"/>')
out('<line x1="282" y1="350" x2="302" y2="350" stroke="black" stroke-width="3.5"/>')

# Material fills
out('<rect x="0" y="0" width="480" height="680" fill="url(#coal)" clip-path="url(#c-coal)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#sand)" clip-path="url(#c-sand)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#grav)" clip-path="url(#c-grav)"/>')

# Layer dividers
out('<line x1="161" y1="172" x2="319" y2="172" stroke="black" stroke-width="1.8"/>')
out('<line x1="168" y1="230" x2="312" y2="230" stroke="black" stroke-width="1.8"/>')

# Layer number badges (left side)
for num, y_pos, label in [('1', 144, 'CHARCOAL'), ('2', 201, 'SAND'), ('3', 290, 'GRAVEL')]:
    out(f'<circle cx="137" cy="{y_pos}" r="9" fill="black"/>')
    out(f'<text x="137" y="{y_pos+3.5}" font-size="9" font-weight="bold" text-anchor="middle" fill="white">{num}</text>')
    out(f'<line x1="146" y1="{y_pos}" x2="155" y2="{y_pos}" stroke="black" stroke-width="0.8" marker-end="url(#arrsm)"/>')
    out(f'<text x="135" y="{y_pos-12}" font-size="7.5" font-weight="bold" text-anchor="middle">{label}</text>')

# Filter output
out('<line x1="240" y1="350" x2="240" y2="362" stroke="black" stroke-width="1.3"/>')
out('<line x1="222" y1="350" x2="222" y2="358" stroke="black" stroke-width="1.2"/>')
out('<line x1="258" y1="350" x2="258" y2="358" stroke="black" stroke-width="1.2"/>')
for dx, dy in [(222,363),(240,368),(258,363)]:
    out(f'<path d="M {dx} {dy-5} Q {dx-3} {dy+4} {dx} {dy+7} Q {dx+3} {dy+4} {dx} {dy-5}" fill="none" stroke="black" stroke-width="1.2"/>')
out('<text x="240" y="384" font-size="7.5" font-weight="bold" text-anchor="middle">THEN BOIL</text>')
out('<text x="240" y="395" font-size="6.5" font-style="italic" text-anchor="middle">filtered water is not yet safe — boil before drinking</text>')

# Vertical divider between columns
out('<line x1="348" y1="140" x2="348" y2="404" stroke="black" stroke-width="0.6"/>')

# ══ SECTION C — COLLECT MATERIALS (right column) ════════════════════════════
out('<text x="405" y="152" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— COLLECT —</text>')

# Panel 1: GRAVEL (y=160–218)
out('<rect x="352" y="158" width="106" height="58" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="170" font-size="7" font-weight="bold" text-anchor="middle">① GRAVEL</text>')
# Side elevation: figure crouching at river
fig_crouching(385, 175, s=0.62)
# Riverbed wavy line
out('<path d="M 356 215 Q 368 212 380 215 Q 392 218 404 215 Q 416 212 428 215 Q 440 218 452 215" fill="none" stroke="black" stroke-width="1.0"/>')
# Gravel stones at river bottom
for ex, ey, erx, ery in [(365,210,5,3.5),(378,211,4.5,3),(390,210,5.5,3.5),(402,211,4,3),(414,210,5,3.5)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.1"/>')
out('<text x="405" y="212" font-size="5.5" font-style="italic" text-anchor="middle">streambed</text>')

# Panel 2: SAND (y=222–280)
out('<rect x="352" y="220" width="106" height="58" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="232" font-size="7" font-weight="bold" text-anchor="middle">② SAND</text>')
fig_crouching(385, 238, s=0.62)
# Sandy bank (dots)
for sx in range(356, 452, 7):
    for sy in [260, 265, 270]:
        import random
        random.seed(sx*100+sy)
        jx = random.uniform(-2, 2)
        out(f'<circle cx="{sx+jx:.1f}" cy="{sy}" r="1.2" fill="black"/>')
out('<text x="405" y="274" font-size="5.5" font-style="italic" text-anchor="middle">riverbank or dry bed</text>')

# Panel 3: CHARCOAL (y=284–350) — 3-step sequence
out('<rect x="352" y="282" width="106" height="68" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="294" font-size="7" font-weight="bold" text-anchor="middle">③ CHARCOAL</text>')

# Step A: fire symbol (simple flames over log)
fx = 368
out(f'<ellipse cx="{fx}" cy="334" rx="10" ry="5" fill="black"/>') # log
out(f'<path d="M {fx} 332 Q {fx-4} 322 {fx} 316 Q {fx+2} 322 {fx+6} 318 Q {fx+4} 324 {fx+8} 320 Q {fx+6} 328 {fx+5} 332" fill="black"/>') # flames

# Arrow
out('<text x="390" y="328" font-size="9" text-anchor="middle">→</text>')

# Step B: mound covered (earth over coals — restricted oxygen = charcoal not ash)
mx = 408
out(f'<ellipse cx="{mx}" cy="334" rx="10" ry="5" fill="black"/>') # mound
out(f'<path d="M {mx-10} 334 Q {mx} 322 {mx+10} 334" fill="none" stroke="black" stroke-width="2"/>')

# Arrow
out('<text x="428" y="328" font-size="9" text-anchor="middle">→</text>')

# Step C: black chunks (charcoal symbol)
cx2 = 443
out(f'<polygon points="{cx2-7},332 {cx2-1},328 {cx2+2},335 {cx2-2},342 {cx2-8},341" fill="black"/>')
out(f'<polygon points="{cx2+1},330 {cx2+8},328 {cx2+10},337 {cx2+6},342 {cx2},340" fill="black"/>')

out('<text x="368" y="345" font-size="5.5" font-style="italic" text-anchor="middle">burn</text>')
out('<text x="408" y="345" font-size="5.5" font-style="italic" text-anchor="middle">cover</text>')
out('<text x="443" y="345" font-size="5.5" font-style="italic" text-anchor="middle">collect</text>')
out('<text x="405" y="344" font-size="5.5" text-anchor="middle"></text>')
out('<text x="405" y="346" font-size="6" font-style="italic" text-anchor="middle">cool fully before collecting</text>')

out('<line x1="18" y1="404" x2="462" y2="404" stroke="black" stroke-width="0.75"/>')

# ══ SECTION D — HOW TO USE SEQUENCE (full width) ════════════════════════════
out('<text x="240" y="416" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— HOW TO USE THE FILTER —</text>')

panel_y = 422
panel_h = 60
panel_labels = ['POUR\ndirty water\ninto top', 'WAIT\nwater passes\nthrough layers', 'COLLECT\nfiltered water\nat bottom', 'BOIL\nbefore\ndrinking']
panel_x_starts = [20, 128, 236, 344]
pw = 100

for i, (px, label) in enumerate(zip(panel_x_starts, panel_labels)):
    # Panel box
    out(f'<rect x="{px}" y="{panel_y}" width="{pw}" height="{panel_h}" fill="none" stroke="black" stroke-width="0.7"/>')
    # Step number circle
    out(f'<circle cx="{px+10}" cy="{panel_y+10}" r="7" fill="black"/>')
    out(f'<text x="{px+10}" y="{panel_y+14}" font-size="8" font-weight="bold" text-anchor="middle" fill="white">{i+1}</text>')

    # Icons
    mid = px + pw/2
    if i == 0:
        # Pour: container tilting, drops
        out(f'<rect x="{mid-8}" y="{panel_y+16}" width="16" height="22" rx="2" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-20,{mid},{panel_y+27})"/>')
        for di, (dx, dy) in enumerate([(mid-5, panel_y+36),(mid, panel_y+40),(mid+5, panel_y+36)]):
            out(f'<path d="M {dx} {dy} Q {dx-2} {dy+5} {dx} {dy+8} Q {dx+2} {dy+5} {dx} {dy}" fill="black"/>')
    elif i == 1:
        # Wait: filter silhouette (trapezoid) with down arrow
        out(f'<polygon points="{mid-12},{panel_y+16} {mid+12},{panel_y+16} {mid+8},{panel_y+42} {mid-8},{panel_y+42}" fill="none" stroke="black" stroke-width="1.5"/>')
        out(f'<line x1="{mid}" y1="{panel_y+18}" x2="{mid}" y2="{panel_y+40}" stroke="black" stroke-width="1" stroke-dasharray="3,2" marker-end="url(#arrsm)"/>')
    elif i == 2:
        # Collect: container below, drops falling into it
        out(f'<rect x="{mid-10}" y="{panel_y+38}" width="20" height="16" rx="2" fill="none" stroke="black" stroke-width="1.5"/>')
        for dx in [mid-4, mid, mid+4]:
            out(f'<path d="M {dx} {panel_y+18} Q {dx-2} {panel_y+27} {dx} {panel_y+30} Q {dx+2} {panel_y+27} {dx} {panel_y+18}" fill="black"/>')
    elif i == 3:
        # Boil: fire under vessel
        # Vessel
        out(f'<path d="M {mid-10} {panel_y+40} L {mid-12} {panel_y+52} L {mid+12} {panel_y+52} L {mid+10} {panel_y+40} Z" fill="none" stroke="black" stroke-width="1.5"/>')
        # Steam/boil bubbles
        out(f'<circle cx="{mid-4}" cy="{panel_y+36}" r="2.5" fill="none" stroke="black" stroke-width="1"/>')
        out(f'<circle cx="{mid+4}" cy="{panel_y+34}" r="2.5" fill="none" stroke="black" stroke-width="1"/>')
        out(f'<circle cx="{mid}" cy="{panel_y+32}" r="2.5" fill="none" stroke="black" stroke-width="1"/>')
        # Fire
        out(f'<path d="M {mid-8} {panel_y+56} Q {mid-5} {panel_y+50} {mid} {panel_y+52} Q {mid+5} {panel_y+50} {mid+8} {panel_y+56}" fill="none" stroke="black" stroke-width="1.2"/>')
        out(f'<path d="M {mid-4} {panel_y+56} Q {mid-2} {panel_y+48} {mid} {panel_y+52} Q {mid+2} {panel_y+48} {mid+4} {panel_y+56}" fill="black"/>')

    # Label (multi-line)
    label_lines = label.split('\n')
    for li, ll in enumerate(label_lines):
        lfs = 6.5 if li == 0 else 5.5
        lfw = 'bold' if li == 0 else 'normal'
        lst = 'normal' if li == 0 else 'italic'
        out(f'<text x="{mid}" y="{panel_y+panel_h+9+li*8}" font-size="{lfs}" font-weight="{lfw}" font-style="{lst}" text-anchor="middle">{ll}</text>')

    # Arrow to next panel
    if i < 3:
        ax = px + pw + 4
        out(f'<line x1="{ax}" y1="{panel_y+panel_h/2}" x2="{ax+12}" y2="{panel_y+panel_h/2}" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')

out('<line x1="18" y1="506" x2="462" y2="506" stroke="black" stroke-width="0.75"/>')

# ══ SECTION E — MATERIAL SYMBOL KEY ══════════════════════════════════════════
out('<text x="240" y="518" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— MATERIAL SYMBOLS —</text>')

# Charcoal
out('<polygon points="26,526 40,522 44,533 38,543 25,543" fill="black"/>')
out('<polygon points="46,523 62,520 65,532 59,542 46,540" fill="black"/>')
out('<text x="72" y="530" font-size="8" font-weight="bold">CHARCOAL</text>')
out('<text x="72" y="540" font-size="6.5" font-style="italic">angular · jagged · solid black · from burnt wood</text>')

# Sand
for xi, yi in [(26,554),(33,551),(40,554),(47,551),(54,554),(61,551),(68,554)]:
    out(f'<circle cx="{xi}" cy="{yi}" r="2" fill="#111"/>')
out('<text x="78" y="554" font-size="8" font-weight="bold">SAND</text>')
out('<text x="78" y="564" font-size="6.5" font-style="italic">tiny uniform dots · fine-grained · riverbank or beach</text>')

# Gravel
for ex, ey, erx, ery in [(34,579,9,6),(58,578,8,5.5),(76,579,6.5,4.5)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.5"/>')
out('<text x="90" y="578" font-size="8" font-weight="bold">GRAVEL</text>')
out('<text x="90" y="588" font-size="6.5" font-style="italic">rounded ovals · smooth stones · from streambed</text>')

# ── FOOTER ─────────────────────────────────────────────────────────────────
out('<line x1="6" y1="604" x2="474" y2="604" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="614" font-size="6" text-anchor="middle" letter-spacing="0.8">PLATE 02 V3 · CC BY-SA 4.0 · REMEMBER FORWARD · rememberforward.org · DOI 10.5281/zenodo.19545922</text>')
out('<line x1="6" y1="620" x2="474" y2="620" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="640" font-size="7.5" font-weight="bold" font-style="italic" text-anchor="middle">THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.</text>')
out('<text x="240" y="655" font-size="7" font-style="italic" text-anchor="middle">BUY IT · BUILD IT · BURY IT · FOR SOMEONE YOU WILL NEVER MEET</text>')

out('</svg>')

# Write file
svg = '\n'.join(lines)
os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"Written: {OUTFILE}")

import os as _os
try:
    _os.startfile(OUTFILE)
except Exception:
    pass
