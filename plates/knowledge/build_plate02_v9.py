#!/usr/bin/env python3
"""
build_plate02_v9.py — Plate 02 v9: Water — Filter and Purify

What changed from v8:
  Fire icon replaced: hand-coded flame() polygon removed; Bootstrap Icons fire
  (MIT license, viewBox 0 0 16 16) added to figure_paths.json as "fire" and
  rendered via fig() in Band C charcoal panel and Band D BOIL step.
"""

import os, json, random

OUTDIR  = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02_v9_water_filter.svg')
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

def sand_pile(cx, cy):
    """Mound outline + 3-size stipple — FGDC sand standard as standalone icon."""
    out(f'<path d="M {cx-14} {cy} Q {cx-8} {cy-13} {cx} {cy-14} Q {cx+8} {cy-13} {cx+14} {cy} Z"'
        f' fill="none" stroke="black" stroke-width="0.8"/>')
    for ox, oy in [(-7,-3),(0,-4),(6,-5)]:                          # large r=1.6
        out(f'<circle cx="{cx+ox}" cy="{cy+oy}" r="1.6" fill="black"/>')
    for ox, oy in [(-10,-2),(11,-2),(-4,-7),(4,-8),(-1,-11)]:       # medium r=1.2
        out(f'<circle cx="{cx+ox}" cy="{cy+oy}" r="1.2" fill="black"/>')
    for ox, oy in [(-12,-1),(12,-1),(8,-4),(-6,-7),(1,-12)]:        # small r=0.8
        out(f'<circle cx="{cx+ox}" cy="{cy+oy}" r="0.8" fill="black"/>')

def gravel_stones(cx, cy):
    """3 organic stone shapes with white highlight — natural water-worn stones."""
    # Stone A: large, elongated horizontal
    out(f'<path d="M {cx-15} {cy-4} Q {cx-14} {cy-10} {cx-7} {cy-10}'
        f' Q {cx-1} {cy-10} {cx+1} {cy-5} Q {cx} {cy+1} {cx-5} {cy}'
        f' Q {cx-13} {cy+1} {cx-15} {cy-4} Z" fill="black"/>')
    out(f'<circle cx="{cx-12}" cy="{cy-8}" r="1.1" fill="white"/>')
    # Stone B: medium, rounder, slightly offset right
    out(f'<path d="M {cx-1} {cy-4} Q {cx} {cy-9} {cx+5} {cy-8}'
        f' Q {cx+9} {cy-7} {cx+10} {cy-2} Q {cx+9} {cy+2} {cx+4} {cy+2}'
        f' Q {cx-1} {cy+1} {cx-1} {cy-4} Z" fill="black"/>')
    out(f'<circle cx="{cx+3}" cy="{cy-7}" r="0.85" fill="white"/>')
    # Stone C: small, compact, nestled above A and B
    out(f'<path d="M {cx-5} {cy-9} Q {cx-5} {cy-14} {cx-1} {cy-13}'
        f' Q {cx+2} {cy-12} {cx+2} {cy-8} Q {cx+1} {cy-6} {cx-4} {cy-7}'
        f' Q {cx-6} {cy-8} {cx-5} {cy-9} Z" fill="black"/>')
    out(f'<circle cx="{cx-3}" cy="{cy-12}" r="0.6" fill="white"/>')

# ── SVG HEADER + BORDERS ──────────────────────────────────────────────────────

out('<?xml version="1.0" encoding="UTF-8"?>')
out('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="120mm" height="170mm">')
out('<rect width="480" height="680" fill="white"/>')
_cc     = FIGS['charcoal_chunks']
_cc_sc  = round(14 / _cc['bbox']['h'], 4)   # 14px tile height → ~2× more tiles = denser chunks
# Dump-bucket charcoal: large/medium/small chunks at random rotation + position
# → no tiling artifact; cross-section side-view appearance
_big_tw, _big_th = 200, 100
_cx_path = _cc['bbox']['w'] / 2    # rotate each chunk around its own centre
_cy_path = _cc['bbox']['h'] / 2
_rng = random.Random(13)           # fixed seed → reproducible

def _place(tx, ty, sc_mult, angle):
    sc = round(_cc_sc * sc_mult, 4)
    return (f'<g transform="translate({tx:.1f},{ty:.1f}) rotate({angle:.0f})'
            f' scale({sc}) translate({-_cx_path:.2f},{-_cy_path:.2f})">'
            f'<path d="{_cc["paths"][0]}" fill="black" fill-rule="nonzero"/></g>')

_chunk_gs = []
for _ in range(12):   # large backbone chunks
    _chunk_gs.append(_place(_rng.uniform(0,_big_tw), _rng.uniform(0,_big_th),
                            _rng.uniform(1.6, 2.3), _rng.uniform(0,360)))
for _ in range(20):   # medium filler chunks
    _chunk_gs.append(_place(_rng.uniform(0,_big_tw), _rng.uniform(0,_big_th),
                            _rng.uniform(0.9, 1.4), _rng.uniform(0,360)))
for _ in range(16):   # small gap fillers
    _chunk_gs.append(_place(_rng.uniform(0,_big_tw), _rng.uniform(0,_big_th),
                            _rng.uniform(0.4, 0.75), _rng.uniform(0,360)))

# Light hatch for any hairline gaps that remain
_tw, _th, _hstep = _big_tw, _big_th, 4.0
_hl, _c = [], _hstep
while _c < _tw + _th:
    _x1 = min(_c, _tw);  _y1 = max(0.0, _c - _tw)
    _x2 = max(0.0, _c - _th);  _y2 = min(_c, _th)
    if not (abs(_x1 - _x2) < 0.1 and abs(_y1 - _y2) < 0.1):
        _hl.append(f'<line x1="{_x1:.1f}" y1="{_y1:.1f}" x2="{_x2:.1f}" y2="{_y2:.1f}" stroke="black" stroke-width="0.3"/>')
    _c += _hstep
_cc_pat = (
    f'<pattern id="coal" x="0" y="0" width="{_big_tw}" height="{_big_th}" patternUnits="userSpaceOnUse">'
    f'<rect width="{_big_tw}" height="{_big_th}" fill="white"/>'
    + ''.join(_hl)
    + ''.join(_chunk_gs)
    + '</pattern>'
)

out(f'''<defs>
  {_cc_pat}
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
# Charcoal: dense chunk pattern + fine hatch — shows what to pack, not just "fill with black"
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
fig('charcoal_chunks', cx=350, cy=228, target_h=16, anchor='center')
out('<text x="366" y="224" font-size="7" font-weight="bold">&#9312; CHARCOAL</text>')
out('<text x="366" y="233" font-size="5.5" font-style="italic">angular burnt chunks</text>')

# ② SAND annotation (layer midpoint y=280)
sand_pile(350, 287)
out('<text x="366" y="276" font-size="7" font-weight="bold">&#9313; SAND</text>')
out('<text x="366" y="285" font-size="5.5" font-style="italic">fine uniform grains</text>')

# ③ GRAVEL annotation (layer midpoint y=341)
gravel_stones(354, 348)
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
fig('fire', cx=px+98, cy=PY_C+56, target_h=32, anchor='bottom')
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

    elif i == 3: # BOIL — firepit with pot + bubbles + steam above it
        fpx = px + 52          # firepit/pot center x (right side of panel)
        fpy = PY_D + PH_D - 4  # stone base y
        # Stones at base
        for sx, sy in [(fpx-7,fpy+1),(fpx-3,fpy+2),(fpx+1,fpy+2),(fpx+5,fpy+1),(fpx+9,fpy)]:
            out(f'<ellipse cx="{sx}" cy="{sy}" rx="2.8" ry="1.6" fill="black"/>')
        # Fire rising from within stones
        fig('fire', cx=fpx, cy=fpy+1, target_h=14, anchor='bottom')
        # Pot sitting in fire (bottom 2px into fire top)
        fig('clay_pot', cx=fpx, cy=fpy-14, target_h=20, anchor='bottom')
        # Bubbles inside pot near opening
        for bx, by in [(fpx-4, fpy-30), (fpx+1, fpy-33), (fpx+5, fpy-29)]:
            out(f'<circle cx="{bx}" cy="{by}" r="2.0" fill="none" stroke="black" stroke-width="0.9"/>')
        # Steam wisps above pot
        for scx, syo in [(fpx-5, 0), (fpx, -2), (fpx+5, 0)]:
            y0 = fpy - 41 + syo
            y1 = y0 - 11
            out(f'<path d="M {scx} {y0} C {scx-3} {y0-3} {scx+3} {y0-6} {scx} {y1}" fill="none" stroke="black" stroke-width="1.1"/>')

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

# 3-column layout — col x: 18, 166, 314
# Row 1 (y=614): CHARCOAL · SAND · GRAVEL
# Row 2 (y=635): VESSEL · FIREPIT

# ① CHARCOAL — col 1
fig('charcoal_chunks', cx=36, cy=614, target_h=16, anchor='center')
out('<text x="54" y="611" font-size="7.5" font-weight="bold">&#9312; CHARCOAL</text>')
out('<text x="54" y="620" font-size="6" font-style="italic">burnt wood &#183; top layer</text>')

# ② SAND — col 2
sand_pile(184, 621)
out('<text x="202" y="611" font-size="7.5" font-weight="bold">&#9313; SAND</text>')
out('<text x="202" y="620" font-size="6" font-style="italic">fine grains &#183; middle layer</text>')

# ③ GRAVEL — col 3
gravel_stones(336, 621)
out('<text x="352" y="611" font-size="7.5" font-weight="bold">&#9314; GRAVEL</text>')
out('<text x="352" y="620" font-size="6" font-style="italic">rounded stones &#183; bottom layer</text>')

# VESSEL — col 1, row 2
fig('clay_pot', cx=36, cy=643, target_h=18, anchor='bottom')
out('<text x="54" y="632" font-size="7.5" font-weight="bold">VESSEL</text>')
out('<text x="54" y="641" font-size="6" font-style="italic">clay pot &#183; withstands fire</text>')

# FIREPIT — col 2, row 2
for sx, sy in [(175,639),(179,640),(184,640),(189,639),(193,638)]:
    out(f'<ellipse cx="{sx}" cy="{sy}" rx="2.8" ry="1.6" fill="black"/>')
fig('fire', cx=184, cy=639, target_h=10, anchor='bottom')
out('<text x="202" y="632" font-size="7.5" font-weight="bold">FIREPIT</text>')
out('<text x="202" y="641" font-size="6" font-style="italic">stones &#183; open fire &#183; boil water</text>')

# ── FOOTER ────────────────────────────────────────────────────────────────────
out('<line x1="6" y1="644" x2="474" y2="644" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="653" font-size="6" text-anchor="middle" letter-spacing="0.8">PLATE 02 V9 &#183; CC BY-SA 4.0 &#183; REMEMBER FORWARD &#183; rememberforward.org &#183; DOI 10.5281/zenodo.19545922</text>')
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
