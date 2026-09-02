#!/usr/bin/env python3
"""
build_plate02_v8.py — Plate 02 v8: Water — Filter and Purify

What changed from v7:
  BAND A: thick border on left panel = danger signal; taller figures (h=82 panels);
          bolder causal arrow; "OR" divider replaces math ≠
  BAND B: right column annotates each filter layer with its material symbol;
          drain holes get explicit downward arrows; dirty-water input label larger
  BAND C: collect panels reordered to match filter layer numbering (①CHARCOAL
          ②SAND ③GRAVEL = top→bottom); each panel note now shows layer reference
          ("from fire → LAYER ①"); charcoal burn sequence enlarged
  BAND D: panels widened to 80px with 11px gaps (was 86/3px); icons moved to
          right zone (cx=px+60), figures moved to left zone (cx=px+20); inter-step
          arrows 8px sw=2 (were 7px sw=1.2); subtitle text 6px
  BAND E: clay_pot h=20; description text 6px
"""

import os, json, random

OUTDIR  = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02_v8_water_filter.svg')
FIGDATA = r'C:\Users\kanta\Documents\remember-forward\reference_images\figures\figure_paths.json'

with open(FIGDATA, encoding='utf-8') as f:
    FIGS = json.load(f)

lines = []
def out(s): lines.append(s)

# ── FIGURE PLACEMENT ──────────────────────────────────────────────────────────

def fig(name, cx, cy, target_h, anchor='bottom'):
    f  = FIGS[name]
    bb = f['bbox']
    s  = target_h / bb['h']
    fw = bb['w'] * s
    fh = target_h
    if   anchor == 'bottom': ty = cy - fh
    elif anchor == 'center': ty = cy - fh / 2
    else:                    ty = cy
    tx = cx - fw / 2
    out(f'<g transform="translate({tx:.1f},{ty:.1f}) scale({s:.4f}) translate({-bb["x"]:.1f},{-bb["y"]:.1f})">')
    for d in f['paths']:
        out(f'  <path d="{d}" fill="black" fill-rule="nonzero"/>')
    out('</g>')

# ── DRAWING UTILITIES ─────────────────────────────────────────────────────────

def wavy(x1, x2, y, n=6, amp=3, sw=1.2):
    seg = (x2 - x1) / n
    d = f"M {x1:.1f} {y:.1f}"
    for i in range(n):
        sx = x1 + i * seg
        ey = y - amp if i % 2 == 0 else y + amp
        d += f" Q {sx+seg/2:.1f} {ey:.1f} {sx+seg:.1f} {y:.1f}"
    out(f'<path d="{d}" fill="none" stroke="black" stroke-width="{sw:.1f}"/>')

def drop(cx, ty, h=8):
    out(f'<path d="M {cx:.1f} {ty:.1f} Q {cx-2.2:.1f} {ty+h*0.7:.1f} {cx:.1f} {ty+h:.1f} Q {cx+2.2:.1f} {ty+h*0.7:.1f} {cx:.1f} {ty:.1f}" fill="black"/>')

def flame(cx, by, w=14, h=18):
    # 3-peak silhouette: left tip (55% h), center tip (100% h), right tip (72% h)
    # valleys at ~35% h between peaks — unmistakably fire at small scale
    hw = w / 2
    pts = [
        (cx - hw,        by),               # bottom-left
        (cx - hw*0.65,   by - h*0.32),      # left rise
        (cx - hw*0.38,   by - h*0.55),      # left peak
        (cx - hw*0.12,   by - h*0.33),      # left valley
        (cx,             by - h),            # center peak (tallest)
        (cx + hw*0.15,   by - h*0.33),      # right valley
        (cx + hw*0.42,   by - h*0.72),      # right peak
        (cx + hw*0.68,   by - h*0.30),      # right fall
        (cx + hw,        by),               # bottom-right
    ]
    pts_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    out(f'<polygon points="{pts_str}" fill="black"/>')

def coal_symbol(x, y):
    """Two jagged charcoal chunks centered near (x, y)."""
    out(f'<polygon points="{x-12},{y-4} {x-2},{y-7} {x+2},{y+1} {x-2},{y+8} {x-11},{y+9} {x-13},{y+2}" fill="black"/>')
    out(f'<polygon points="{x+1},{y-6} {x+12},{y-8} {x+14},{y+3} {x+9},{y+9} {x+2},{y+7} {x},{y+0}" fill="black"/>')

def sand_dots(cx, cy, spread=12):
    """Cluster of sand dots centered at (cx, cy)."""
    for ox, oy in [(-9,1),(-5,-2),(0,0),(5,-1),(9,1),(-7,5),(0,4),(7,5),(-3,-5),(4,-4)]:
        out(f'<circle cx="{cx+ox}" cy="{cy+oy}" r="1.5" fill="black"/>')

def gravel_stones(cx, cy):
    """Three rounded stones centered near (cx, cy)."""
    for ex, ey, rx, ry in [(cx-12,cy-1,7,4),(cx+1,cy,7,4.5),(cx+14,cy-2,5.5,3.5)]:
        out(f'<ellipse cx="{ex}" cy="{ey}" rx="{rx}" ry="{ry}" fill="none" stroke="black" stroke-width="1.4"/>')

# ── SVG HEADER + BORDERS ──────────────────────────────────────────────────────

out('<?xml version="1.0" encoding="UTF-8"?>')
out('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="120mm" height="170mm">')
out('<rect width="480" height="680" fill="white"/>')
out('''<defs>
  <pattern id="coal" x="0" y="0" width="28" height="22" patternUnits="userSpaceOnUse">
    <rect width="28" height="22" fill="white"/>
    <polygon points="1,3 13,1 17,8 13,17 2,18 0,9" fill="black"/>
    <polygon points="16,2 27,0 28,11 23,19 16,16 14,8" fill="black"/>
  </pattern>
  <pattern id="sand" x="0" y="0" width="8" height="7" patternUnits="userSpaceOnUse">
    <circle cx="4" cy="3.5" r="1.8" fill="#111"/>
    <circle cx="0" cy="7"   r="1.8" fill="#111"/>
    <circle cx="8" cy="7"   r="1.8" fill="#111"/>
  </pattern>
  <pattern id="grav" x="0" y="0" width="36" height="28" patternUnits="userSpaceOnUse">
    <rect width="36" height="28" fill="white"/>
    <ellipse cx="9"  cy="8"  rx="7"   ry="5"   fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="26" cy="7"  rx="7.5" ry="4.5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="7"  cy="21" rx="5"   ry="3.5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="24" cy="21" rx="8"   ry="5"   fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="34" cy="19" rx="3.5" ry="2.8" fill="none" stroke="black" stroke-width="1.1"/>
  </pattern>
  <!-- Filter y-coords: top=202, charcoal/sand=254, sand/gravel=306, bottom=376 -->
  <clipPath id="c-coal"><polygon points="154,202 326,202 319,254 161,254"/></clipPath>
  <clipPath id="c-sand"><polygon points="161,254 319,254 312,306 168,306"/></clipPath>
  <clipPath id="c-grav"><polygon points="168,306 312,306 302,376 178,376"/></clipPath>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
  <marker id="arrsm" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
  <marker id="arrlg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="2"/>
  </marker>
</defs>''')
out('<style>text { font-family: Georgia, serif; fill: black; }</style>')
out('<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="black" stroke-width="3"/>')
out('<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="black" stroke-width="0.75"/>')

out('<text x="240" y="32" font-size="11" font-weight="bold" text-anchor="middle" letter-spacing="2">WATER &#8212; FILTER AND PURIFY</text>')
out('<line x1="18" y1="38" x2="462" y2="38" stroke="black" stroke-width="1"/>')
out('<text x="240" y="50" font-size="7" text-anchor="middle" letter-spacing="1.5">PLATE 02 &#183; SURVIVAL KNOWLEDGE &#183; CLEAN WATER PREVENTS ILLNESS AND DEATH</text>')
out('<line x1="18" y1="56" x2="462" y2="56" stroke="black" stroke-width="0.5"/>')

# ══ BAND A — WHY (y=57-165) ═══════════════════════════════════════════════════
# Panels h=82. Left panel has thick danger border (sw=3). Right is normal (sw=0.8).
# Causal arrow is bold (sw=2.5). "OR" replaces ≠.

out('<text x="240" y="68" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2.5">&#8212; WHY THIS MATTERS &#8212;</text>')

# ── Left panel: DANGER ────────────────────────────────────────────────────────
# thick border signals danger without requiring cultural knowledge of any symbol
out('<rect x="18" y="74" width="210" height="82" fill="none" stroke="black" stroke-width="3"/>')

# Heavy contaminated waves — bold stroke fills top of panel
for i in range(7):
    wx = 22 + i * 16
    wy = 82 if i % 2 == 0 else 86
    out(f'<path d="M {wx} {wy} Q {wx+5} {wy-5} {wx+10} {wy} Q {wx+16} {wy+4} {wx+22} {wy}" fill="none" stroke="black" stroke-width="3"/>')
out('<text x="113" y="102" font-size="7" font-weight="bold" text-anchor="middle">CONTAMINATED WATER</text>')

# Bold causal arrow — thick, clearly pointing from water label to sick figure
out('<line x1="92" y1="111" x2="122" y2="111" stroke="black" stroke-width="2.5" marker-end="url(#arrlg)"/>')

# lying_sick: cx=161 keeps right edge at 228 (fits 210px panel starting x=18)
# target_h=40 → fw = 936*(40/280) = 133.7px, spans x=94–228
fig('lying_sick', cx=161, cy=154, target_h=40, anchor='bottom')
out('<text x="161" y="161" font-size="6.5" font-weight="bold" text-anchor="middle">ILLNESS / DEATH</text>')

# ── Divider ────────────────────────────────────────────────────────────────────
out('<text x="240" y="119" font-size="9" font-weight="bold" text-anchor="middle">OR</text>')

# ── Right panel: SAFE ─────────────────────────────────────────────────────────
out('<rect x="252" y="74" width="210" height="82" fill="none" stroke="black" stroke-width="0.8"/>')

# Light clean waves — thin stroke, calm
for yi in [82, 90, 98]:
    wavy(256, 400, yi, n=6, amp=2, sw=1.0)
out('<text x="328" y="80" font-size="7" font-weight="bold" text-anchor="middle">FILTERED + BOILED</text>')

# Arrow to drinking figure — thinner than danger panel
out('<line x1="334" y1="111" x2="360" y2="111" stroke="black" stroke-width="1.5" marker-end="url(#arr)"/>')

# drinking_clean: large figure fills right side. target_h=80 → fw=46.4px, spans 439–509... wait
# cx=435, fw=431*(80/743)=46.4, spans 435-23.2=411.8 to 435+23.2=458.2. Panel right=462. ✓
fig('drinking_clean', cx=435, cy=154, target_h=80, anchor='bottom')
out('<text x="435" y="161" font-size="6.5" font-weight="bold" text-anchor="middle">SAFE TO DRINK</text>')

out('<line x1="18" y1="165" x2="462" y2="165" stroke="black" stroke-width="0.75"/>')

# ══ BAND B — BUILD THE FILTER (y=166-407) ════════════════════════════════════
# Filter polygon: top=202, layers at 254/306, bottom=376.
# NEW: right column (x=332-462) annotates each layer with its material symbol.
# NEW: drain holes have explicit ↓ arrows. Dirty-water label larger/bolder.

out('<text x="155" y="177" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; BUILD THE FILTER &#8212;</text>')
out('<text x="155" y="186" font-size="5.5" font-style="italic" text-anchor="middle">cross-section &#183; layer order is critical</text>')
out('<text x="155" y="196" font-size="8" font-weight="bold" text-anchor="middle">DIRTY WATER &#8595;</text>')

for xi in [200, 220, 240, 260, 280]:
    out(f'<line x1="{xi}" y1="196" x2="{xi}" y2="202" stroke="black" stroke-width="1.2" marker-end="url(#arrsm)"/>')

# Filter container
out('<polygon points="154,202 326,202 302,376 178,376" fill="none" stroke="black" stroke-width="3.5"/>')
out('<ellipse cx="240" cy="202" rx="86" ry="7" fill="white" stroke="black" stroke-width="2.2"/>')

# Drain: broken bottom + explicit ↓ arrows at each gap
out('<line x1="178" y1="376" x2="196" y2="376" stroke="black" stroke-width="3.5"/>')
out('<line x1="220" y1="376" x2="260" y2="376" stroke="black" stroke-width="3.5"/>')
out('<line x1="284" y1="376" x2="302" y2="376" stroke="black" stroke-width="3.5"/>')
# ↓ arrows at each gap center
for gx in [208, 272]:
    out(f'<line x1="{gx}" y1="376" x2="{gx}" y2="384" stroke="black" stroke-width="1.5" marker-end="url(#arrsm)"/>')

# Material fills
out('<rect x="0" y="0" width="480" height="680" fill="url(#coal)" clip-path="url(#c-coal)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#sand)" clip-path="url(#c-sand)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#grav)" clip-path="url(#c-grav)"/>')
out('<line x1="161" y1="254" x2="319" y2="254" stroke="black" stroke-width="1.8"/>')
out('<line x1="168" y1="306" x2="312" y2="306" stroke="black" stroke-width="1.8"/>')

# Layer badges (left margin) — numbered top→bottom = ①CHARCOAL ②SAND ③GRAVEL
for num, yp, label in [('1', 228, 'CHARCOAL'), ('2', 280, 'SAND'), ('3', 341, 'GRAVEL')]:
    out(f'<circle cx="112" cy="{yp}" r="9" fill="none" stroke="black" stroke-width="1.5"/>')
    out(f'<text x="112" y="{yp+3.5:.1f}" font-size="9" font-weight="bold" text-anchor="middle">{num}</text>')
    out(f'<line x1="121" y1="{yp}" x2="134" y2="{yp}" stroke="black" stroke-width="0.8" marker-end="url(#arrsm)"/>')
    out(f'<text x="110" y="{yp-12}" font-size="7.5" font-weight="bold" text-anchor="middle">{label}</text>')

# ── Right-column annotations: material symbol aligned to each layer ───────────
# Thin separator between filter zone and annotation column
out('<line x1="334" y1="202" x2="334" y2="376" stroke="black" stroke-width="0.5"/>')
out('<text x="398" y="209" font-size="6" font-weight="bold" text-anchor="middle" letter-spacing="1">MATERIALS</text>')

# ① CHARCOAL annotation (layer midpoint y=228)
coal_symbol(350, 228)
out('<text x="366" y="224" font-size="7" font-weight="bold">&#9312; CHARCOAL</text>')
out('<text x="366" y="233" font-size="5.5" font-style="italic">angular burnt chunks</text>')

# ② SAND annotation (layer midpoint y=280)
sand_dots(350, 280)
out('<text x="366" y="276" font-size="7" font-weight="bold">&#9313; SAND</text>')
out('<text x="366" y="285" font-size="5.5" font-style="italic">fine uniform grains</text>')

# ③ GRAVEL annotation (layer midpoint y=341)
gravel_stones(354, 341)
out('<text x="372" y="337" font-size="7" font-weight="bold">&#9314; GRAVEL</text>')
out('<text x="372" y="346" font-size="5.5" font-style="italic">smooth rounded stones</text>')

# ── Filter output ─────────────────────────────────────────────────────────────
out('<line x1="240" y1="384" x2="240" y2="396" stroke="black" stroke-width="2.5" marker-end="url(#arrlg)"/>')
wavy(218, 262, 399, n=4, amp=2, sw=1.0)
out('<text x="240" y="396" font-size="7.5" font-weight="bold" text-anchor="middle">&#8595; BOIL BEFORE DRINKING &#8595;</text>')
out('<text x="240" y="405" font-size="5.5" font-style="italic" text-anchor="middle">filtering alone does not kill pathogens</text>')

out('<line x1="18" y1="407" x2="462" y2="407" stroke="black" stroke-width="0.75"/>')

# ══ BAND C — COLLECT MATERIALS (y=408-490) ════════════════════════════════════
# Reordered ①CHARCOAL ②SAND ③GRAVEL (top→bottom filter order = collect order).
# Each panel note: "from X → LAYER ①/②/③". Charcoal burn sequence enlarged.

out('<text x="240" y="419" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; COLLECT MATERIALS &#8212;</text>')

PW_C = 145
PH_C = 60
PY_C = 424
C_XS = [18, 167, 316]

# ①CHARCOAL ②SAND ③GRAVEL — matches filter layer numbering top→bottom
collect_panels = [
    ('&#9312; CHARCOAL', 'tending_fire', 'from fire &#8594; LAYER &#9312;'),
    ('&#9313; SAND',     'kneeling',     'sandy bank &#8594; LAYER &#9313;'),
    ('&#9314; GRAVEL',   'kneeling',     'streambed &#8594; LAYER &#9314;'),
]

for pi, (label, fname, note) in enumerate(collect_panels):
    px = C_XS[pi]
    out(f'<rect x="{px}" y="{PY_C}" width="{PW_C}" height="{PH_C}" fill="none" stroke="black" stroke-width="0.7"/>')
    out(f'<text x="{px+PW_C//2}" y="{PY_C+10}" font-size="6.5" font-weight="bold" text-anchor="middle">{label}</text>')
    fig(fname, cx=px+40, cy=PY_C+PH_C-3, target_h=46, anchor='bottom')
    out(f'<text x="{px+PW_C//2}" y="{PY_C+PH_C+10}" font-size="6" font-style="italic" text-anchor="middle">{note}</text>')

# Charcoal panel (①, leftmost) — larger burn→cover sequence
px = C_XS[0]
# Bigger flame (right side of panel)
flame(px+98, PY_C+56, w=26, h=32)
out(f'<text x="{px+98}" y="{PY_C+60}" font-size="5.5" font-style="italic" text-anchor="middle">burn</text>')
out(f'<text x="{px+118}" y="{PY_C+42}" font-size="8" text-anchor="middle">&#8594;</text>')
# Mound / cover symbol (larger)
mx = px + 132
out(f'<ellipse cx="{mx}" cy="{PY_C+46}" rx="10" ry="5" fill="black"/>')
out(f'<path d="M {mx-10} {PY_C+46} Q {mx} {PY_C+35} {mx+10} {PY_C+46}" fill="none" stroke="black" stroke-width="2"/>')
out(f'<text x="{mx}" y="{PY_C+56}" font-size="5.5" font-style="italic" text-anchor="middle">cover</text>')

# Sand panel (②) — dot field
px = C_XS[1]
for sx in range(px+88, px+143, 7):
    for sy_off in [32, 38, 44]:
        sy = PY_C + sy_off
        random.seed(sx * 100 + sy)
        jx = random.uniform(-2, 2)
        out(f'<circle cx="{sx+jx:.1f}" cy="{sy}" r="1.3" fill="black"/>')

# Gravel panel (③) — stream + stones
px = C_XS[2]
out(f'<path d="M {px+86} {PY_C+42} Q {px+100} {PY_C+38} {px+114} {PY_C+42} Q {px+128} {PY_C+46} {px+142} {PY_C+42}" fill="none" stroke="black" stroke-width="1.0"/>')
for ex, ey, erx, ery in [
    (px+92, PY_C+38, 6, 3.5), (px+107, PY_C+39, 5.5, 3),
    (px+122, PY_C+38, 6.5, 3.8), (px+137, PY_C+39, 5, 2.8),
]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.2"/>')

out('<line x1="18" y1="490" x2="462" y2="490" stroke="black" stroke-width="0.75"/>')

# ══ BAND D — HOW TO USE (y=491-591) ══════════════════════════════════════════
# 80px panels with 11px gaps. LEFT zone (cx=px+20): person figure at h=36.
# RIGHT zone (cx=px+60): dominant icon at 28-36px tall.
# Inter-step arrows: 8px, stroke-width=2 (was 7px / sw=1.2).

out('<text x="240" y="501" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; HOW TO USE THE FILTER &#8212;</text>')

PY_D = 507
PH_D = 62
PW_D = 80
D_XS = [18, 109, 200, 291, 382]   # 80px panels, 11px gaps

steps = [
    ('pouring_filter', 'POUR',    'dirty water into top'),
    ('seated',         'WAIT',    'water passes through'),
    ('kneeling',       'COLLECT', 'filtered water in pot'),
    ('tending_fire',   'BOIL',    'before drinking'),
    ('drinking_clean', 'DRINK',   'only after boiling'),
]

for i, (fname, title, subtitle) in enumerate(steps):
    px  = D_XS[i]
    mid = px + PW_D // 2

    out(f'<rect x="{px}" y="{PY_D}" width="{PW_D}" height="{PH_D}" fill="none" stroke="black" stroke-width="0.7"/>')

    # LEFT zone: person figure (cx=px+20, target_h=36)
    # DRINK step: figure spans full panel (no separate icon)
    if i < 4:
        fig(fname, cx=px+20, cy=PY_D+PH_D-3, target_h=36, anchor='bottom')
    else:  # DRINK: tall figure centered
        fig(fname, cx=px+40, cy=PY_D+PH_D-3, target_h=56, anchor='bottom')

    # RIGHT zone: dominant icon (cx=px+60)
    icx = px + 60

    if i == 0:   # POUR — drops + funnel (large)
        for dx in [icx-7, icx, icx+7]:
            drop(dx, PY_D+10, 9)
        out(f'<polygon points="{icx-14},{PY_D+25} {icx+14},{PY_D+25} {icx+10},{PY_D+50} {icx-10},{PY_D+50}" fill="none" stroke="black" stroke-width="1.5"/>')

    elif i == 1: # WAIT — filter outline + dashed through-arrow (large)
        out(f'<polygon points="{icx-13},{PY_D+12} {icx+13},{PY_D+12} {icx+10},{PY_D+52} {icx-10},{PY_D+52}" fill="none" stroke="black" stroke-width="1.5"/>')
        out(f'<line x1="{icx}" y1="{PY_D+14}" x2="{icx}" y2="{PY_D+50}" stroke="black" stroke-width="1.2" stroke-dasharray="3,2.5" marker-end="url(#arrsm)"/>')

    elif i == 2: # COLLECT — drops into large pot
        for dx in [icx-7, icx, icx+7]:
            drop(dx, PY_D+10, 9)
        fig('clay_pot', cx=icx, cy=PY_D+PH_D-5, target_h=28, anchor='bottom')

    elif i == 3: # BOIL — pot over prominent flames
        fig('clay_pot', cx=icx, cy=PY_D+40, target_h=26, anchor='bottom')
        flame(icx-9, PY_D+PH_D-2, w=16, h=22)
        flame(icx+9, PY_D+PH_D-2, w=16, h=22)
        for bxo, byo in [(-4, 18), (4, 15), (0, 12)]:
            out(f'<circle cx="{icx+bxo}" cy="{PY_D+byo}" r="1.8" fill="none" stroke="black" stroke-width="0.9"/>')

    # i==4 DRINK: figure covers whole panel, no icon needed

    # Labels below panel
    circled = ['&#9312;', '&#9313;', '&#9314;', '&#9315;', '&#9316;'][i]
    out(f'<text x="{mid}" y="{PY_D+PH_D+11}" font-size="7" font-weight="bold" text-anchor="middle">{circled} {title}</text>')
    out(f'<text x="{mid}" y="{PY_D+PH_D+20}" font-size="6" font-style="italic" text-anchor="middle">{subtitle}</text>')

    # Inter-step arrows: 8px, sw=2 in the 11px gap
    if i < 4:
        ax = px + PW_D + 2
        out(f'<line x1="{ax}" y1="{PY_D+PH_D//2}" x2="{ax+7}" y2="{PY_D+PH_D//2}" stroke="black" stroke-width="2" marker-end="url(#arrlg)"/>')

out('<line x1="18" y1="591" x2="462" y2="591" stroke="black" stroke-width="0.75"/>')

# ══ BAND E — MATERIAL SYMBOLS (y=592-634) ════════════════════════════════════
out('<text x="240" y="602" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; MATERIAL SYMBOLS &#8212;</text>')

# Two-column layout
# ① CHARCOAL (left, row 1)
coal_symbol(36, 614)
out('<text x="54" y="612" font-size="7.5" font-weight="bold">&#9312; CHARCOAL</text>')
out('<text x="54" y="621" font-size="6" font-style="italic">angular &#183; burnt wood &#183; top layer</text>')

# ② SAND (right, row 1)
sand_dots(258, 614)
out('<text x="272" y="612" font-size="7.5" font-weight="bold">&#9313; SAND</text>')
out('<text x="272" y="621" font-size="6" font-style="italic">fine grains &#183; riverbank &#183; middle layer</text>')

# ③ GRAVEL (left, row 2)
gravel_stones(40, 632)
out('<text x="54" y="630" font-size="7.5" font-weight="bold">&#9314; GRAVEL</text>')
out('<text x="54" y="639" font-size="6" font-style="italic">rounded stones &#183; streambed &#183; bottom layer</text>')

# VESSEL (right, row 2) — traced clay_pot, larger (h=20)
fig('clay_pot', cx=258, cy=640, target_h=20, anchor='bottom')
out('<text x="272" y="630" font-size="7.5" font-weight="bold">VESSEL</text>')
out('<text x="272" y="639" font-size="6" font-style="italic">clay pot &#183; holds water &#183; survives fire</text>')

# ── FOOTER ────────────────────────────────────────────────────────────────────
out('<line x1="6" y1="644" x2="474" y2="644" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="653" font-size="6" text-anchor="middle" letter-spacing="0.8">PLATE 02 V8 &#183; CC BY-SA 4.0 &#183; REMEMBER FORWARD &#183; rememberforward.org &#183; DOI 10.5281/zenodo.19545922</text>')
out('<line x1="6" y1="659" x2="474" y2="659" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="664" font-size="7.5" font-weight="bold" font-style="italic" text-anchor="middle">THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.</text>')
out('<text x="240" y="674" font-size="7" font-style="italic" text-anchor="middle">BUY IT &#183; BUILD IT &#183; BURY IT &#183; FOR SOMEONE YOU WILL NEVER MEET</text>')

out('</svg>')

os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {OUTFILE}')

try:
    import os as _os; _os.startfile(OUTFILE)
except Exception:
    pass
