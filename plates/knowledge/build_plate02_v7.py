#!/usr/bin/env python3
"""
build_plate02_v7.py — Plate 02 v7: Water — Filter and Purify

Layout: true horizontal bands — each section has its own y-range, zero overlap.
  Band A (WHY):     y=57-155
  Band B (FILTER):  y=156-397
  Band C (COLLECT): y=398-476
  Band D (USE):     y=477-577
  Band E (KEY):     y=578-628
  Footer:           y=629-668

Fixes from v6:
  - lying_sick no longer overflows left panel boundary (cx adjusted, target_h reduced)
  - arrows no longer placed inside figures (arrow ends at x=112, figure starts at x=116)
  - collect panels now full-width with room to breathe (3×145px vs cramped 106px)
  - traced clay_pot from JSON used in D step icons (no more hand-coded geometry)
  - angular polygon flame reads better at small scale than v6 Bezier flame
  - tending_fire still used but NOTE: needs re-trace at higher simplification
    (17 paths → visual noise at small scale; re-run trace_figures.py with threshold=8)
"""

import os, json, random

OUTDIR  = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02_v7_water_filter.svg')
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
        out(f'  <path d="{d}" fill="black" fill-rule="evenodd"/>')
    out('</g>')

def fig_w(name, target_h):
    bb = FIGS[name]['bbox']
    return bb['w'] * (target_h / bb['h'])

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
    """Angular three-peak flame polygon — sharp tips read better than rounded Bezier at small scale."""
    hw = w / 2
    pts = " ".join([
        f"{cx-hw:.1f},{by:.1f}",
        f"{cx-hw*0.55:.1f},{by-h*0.62:.1f}",
        f"{cx-hw*0.18:.1f},{by-h*0.56:.1f}",
        f"{cx:.1f},{by-h:.1f}",
        f"{cx+hw*0.18:.1f},{by-h*0.56:.1f}",
        f"{cx+hw*0.55:.1f},{by-h*0.62:.1f}",
        f"{cx+hw:.1f},{by:.1f}",
    ])
    out(f'<polygon points="{pts}" fill="black"/>')

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
  <!-- Clip paths updated for new filter y-coordinates: top=192, coal/sand=244, sand/grav=296, bottom=366 -->
  <clipPath id="c-coal"><polygon points="154,192 326,192 319,244 161,244"/></clipPath>
  <clipPath id="c-sand"><polygon points="161,244 319,244 312,296 168,296"/></clipPath>
  <clipPath id="c-grav"><polygon points="168,296 312,296 302,366 178,366"/></clipPath>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
  <marker id="arrsm" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
</defs>''')
out('<style>text { font-family: Georgia, serif; fill: black; }</style>')
out('<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="black" stroke-width="3"/>')
out('<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="black" stroke-width="0.75"/>')

out('<text x="240" y="32" font-size="11" font-weight="bold" text-anchor="middle" letter-spacing="2">WATER &#8212; FILTER AND PURIFY</text>')
out('<line x1="18" y1="38" x2="462" y2="38" stroke="black" stroke-width="1"/>')
out('<text x="240" y="50" font-size="7" text-anchor="middle" letter-spacing="1.5">PLATE 02 &#183; SURVIVAL KNOWLEDGE &#183; CLEAN WATER PREVENTS ILLNESS AND DEATH</text>')
out('<line x1="18" y1="56" x2="462" y2="56" stroke="black" stroke-width="0.5"/>')

# ══ BAND A — WHY (y=57-155) ═══════════════════════════════════════════════════
out('<text x="240" y="68" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2.5">&#8212; WHY THIS MATTERS &#8212;</text>')

# Left panel: contaminated → sick
# Panel: x=18-230, y=74-146. lying_sick at cx=173 → right edge ≈230 (fits exactly).
out('<rect x="18" y="74" width="212" height="72" fill="none" stroke="black" stroke-width="0.8"/>')
for i in range(7):
    wx = 22 + i * 16
    wy = 82 if i % 2 == 0 else 86
    out(f'<path d="M {wx} {wy} Q {wx+5} {wy-5} {wx+10} {wy} Q {wx+16} {wy+4} {wx+22} {wy}" fill="none" stroke="black" stroke-width="2.5"/>')
out('<text x="75" y="100" font-size="7" font-weight="bold" text-anchor="middle">CONTAMINATED WATER</text>')
# Arrow ends at x=112; lying_sick figure starts at cx-fw/2 = 173-56.8 = 116.2 → 4px gap
out('<line x1="88" y1="113" x2="112" y2="113" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')
fig('lying_sick', cx=173, cy=146, target_h=34, anchor='bottom')
out('<text x="173" y="152" font-size="6" font-weight="bold" text-anchor="middle">ILLNESS / DEATH</text>')

# Divider
out('<text x="240" y="116" font-size="17" text-anchor="middle" font-weight="bold">&#8800;</text>')

# Right panel: filtered+boiled → healthy
# Panel: x=250-462, y=74-146
out('<rect x="250" y="74" width="212" height="72" fill="none" stroke="black" stroke-width="0.8"/>')
for yi in [83, 91, 99]:
    wavy(254, 378, yi, n=5, amp=2, sw=1.0)
out('<text x="316" y="80" font-size="7" font-weight="bold" text-anchor="middle">FILTERED + BOILED</text>')
out('<line x1="330" y1="113" x2="354" y2="113" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')
# drinking_clean: tall figure, right side. fw at h=70 = 431*(70/743) = 40.6px, fits well
fig('drinking_clean', cx=432, cy=146, target_h=70, anchor='bottom')
out('<text x="432" y="152" font-size="6" font-weight="bold" text-anchor="middle">SAFE TO DRINK</text>')

out('<line x1="18" y1="155" x2="462" y2="155" stroke="black" stroke-width="0.75"/>')

# ══ BAND B — BUILD THE FILTER (y=156-397) ════════════════════════════════════
out('<text x="240" y="167" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; BUILD THE FILTER &#8212;</text>')
out('<text x="240" y="176" font-size="5.5" font-style="italic" text-anchor="middle">cross-section &#183; layer order is critical</text>')
out('<text x="240" y="184" font-size="6.5" font-style="italic" text-anchor="middle">dirty water &#8595;</text>')

for xi in [200, 220, 240, 260, 280]:
    out(f'<line x1="{xi}" y1="182" x2="{xi}" y2="190" stroke="black" stroke-width="1.0" marker-end="url(#arrsm)"/>')

# Filter container: top y=192, bottom y=366, height=174px
out('<polygon points="154,192 326,192 302,366 178,366" fill="none" stroke="black" stroke-width="3.5"/>')
out('<ellipse cx="240" cy="192" rx="86" ry="7" fill="white" stroke="black" stroke-width="2.2"/>')

# Drain: broken bottom line (gaps = drain holes)
out('<line x1="178" y1="366" x2="196" y2="366" stroke="black" stroke-width="3.5"/>')
out('<line x1="220" y1="366" x2="260" y2="366" stroke="black" stroke-width="3.5"/>')
out('<line x1="284" y1="366" x2="302" y2="366" stroke="black" stroke-width="3.5"/>')

# Material fills
out('<rect x="0" y="0" width="480" height="680" fill="url(#coal)" clip-path="url(#c-coal)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#sand)" clip-path="url(#c-sand)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#grav)" clip-path="url(#c-grav)"/>')
out('<line x1="161" y1="244" x2="319" y2="244" stroke="black" stroke-width="1.8"/>')
out('<line x1="168" y1="296" x2="312" y2="296" stroke="black" stroke-width="1.8"/>')

# Layer badges (left margin)
for num, yp, label in [('1', 218, 'CHARCOAL'), ('2', 270, 'SAND'), ('3', 331, 'GRAVEL')]:
    out(f'<circle cx="112" cy="{yp}" r="9" fill="none" stroke="black" stroke-width="1.5"/>')
    out(f'<text x="112" y="{yp+3.5:.1f}" font-size="9" font-weight="bold" text-anchor="middle">{num}</text>')
    out(f'<line x1="121" y1="{yp}" x2="134" y2="{yp}" stroke="black" stroke-width="0.8" marker-end="url(#arrsm)"/>')
    out(f'<text x="110" y="{yp-12}" font-size="7.5" font-weight="bold" text-anchor="middle">{label}</text>')

# Filter output: drip lines + boil warning
out('<line x1="240" y1="366" x2="240" y2="376" stroke="black" stroke-width="1.3"/>')
out('<line x1="222" y1="366" x2="222" y2="373" stroke="black" stroke-width="1.1"/>')
out('<line x1="258" y1="366" x2="258" y2="373" stroke="black" stroke-width="1.1"/>')
wavy(218, 262, 374, n=4, amp=2, sw=1.0)
out('<text x="240" y="384" font-size="7" font-weight="bold" text-anchor="middle">&#8595; BOIL BEFORE DRINKING &#8595;</text>')
out('<text x="240" y="393" font-size="5.5" font-style="italic" text-anchor="middle">filtering alone does not kill pathogens</text>')

out('<line x1="18" y1="397" x2="462" y2="397" stroke="black" stroke-width="0.75"/>')

# ══ BAND C — COLLECT MATERIALS (y=398-476) ═══════════════════════════════════
out('<text x="240" y="408" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; COLLECT MATERIALS &#8212;</text>')

PW_C = 145
PH_C = 58
PY_C = 413
C_XS = [18, 167, 316]  # 3 panels each 145px, 4px gaps

collect_panels = [
    ('&#9312; GRAVEL',   'kneeling',     'streambed'),
    ('&#9313; SAND',     'kneeling',     'sandy bank'),
    ('&#9314; CHARCOAL', 'tending_fire', 'from fire'),
]

for pi, (label, fname, note) in enumerate(collect_panels):
    px = C_XS[pi]
    out(f'<rect x="{px}" y="{PY_C}" width="{PW_C}" height="{PH_C}" fill="none" stroke="black" stroke-width="0.7"/>')
    out(f'<text x="{px + PW_C//2}" y="{PY_C+10}" font-size="6.5" font-weight="bold" text-anchor="middle">{label}</text>')
    fig(fname, cx=px+40, cy=PY_C+PH_C-3, target_h=44, anchor='bottom')
    out(f'<text x="{px + PW_C//2}" y="{PY_C+PH_C+8}" font-size="5" font-style="italic" text-anchor="middle">{note}</text>')

# Gravel panel — stream line + stones (right side of panel 1)
px = C_XS[0]
out(f'<path d="M {px+88} {PY_C+40} Q {px+101} {PY_C+37} {px+114} {PY_C+40} Q {px+127} {PY_C+43} {px+140} {PY_C+40}" fill="none" stroke="black" stroke-width="1.0"/>')
for ex, ey, erx, ery in [
    (px+93, PY_C+37, 5.5, 3.2), (px+107, PY_C+38, 5, 2.8),
    (px+121, PY_C+37, 6,   3.4), (px+135, PY_C+38, 4.5, 2.5),
]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.1"/>')

# Sand panel — dot field (right side of panel 2)
px = C_XS[1]
for sx in range(px+88, px+143, 7):
    for sy_off in [34, 39, 44]:
        sy = PY_C + sy_off
        random.seed(sx * 100 + sy)
        jx = random.uniform(-2, 2)
        out(f'<circle cx="{sx+jx:.1f}" cy="{sy}" r="1.1" fill="black"/>')

# Charcoal panel — burn → cover mini-sequence (right side of panel 3)
px = C_XS[2]
bx = px + 90
flame(bx, PY_C + 48, w=11, h=14)
out(f'<text x="{bx}" y="{PY_C+PH_C+8}" font-size="4.5" font-style="italic" text-anchor="middle">burn wood</text>')
out(f'<text x="{bx+20}" y="{PY_C+40}" font-size="7" text-anchor="middle">&#8594;</text>')
mx = bx + 38
out(f'<ellipse cx="{mx}" cy="{PY_C+42}" rx="9" ry="4.5" fill="black"/>')
out(f'<path d="M {mx-9} {PY_C+42} Q {mx} {PY_C+33} {mx+9} {PY_C+42}" fill="none" stroke="black" stroke-width="1.8"/>')
out(f'<text x="{mx}" y="{PY_C+PH_C+8}" font-size="4.5" font-style="italic" text-anchor="middle">cover ash</text>')

out('<line x1="18" y1="476" x2="462" y2="476" stroke="black" stroke-width="0.75"/>')

# ══ BAND D — HOW TO USE (y=477-577) ══════════════════════════════════════════
out('<text x="240" y="487" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; HOW TO USE THE FILTER &#8212;</text>')

PY_D = 492
PH_D = 62
PW_D = 86
D_XS = [18, 107, 196, 285, 374]

steps = [
    ('pouring_filter', 'POUR',    'dirty water into top'),
    ('seated',         'WAIT',    'water passes through'),
    ('kneeling',       'COLLECT', 'filtered water at bottom'),
    ('tending_fire',   'BOIL',    'before drinking'),
    ('drinking_clean', 'DRINK',   'only after boiling'),
]

for i, (fname, title, subtitle) in enumerate(steps):
    px  = D_XS[i]
    mid = px + PW_D // 2

    out(f'<rect x="{px}" y="{PY_D}" width="{PW_D}" height="{PH_D}" fill="none" stroke="black" stroke-width="0.7"/>')
    # No in-panel badge — step number lives in the label below (Unicode circled numeral)

    # Figure: left side of panel
    fig(fname, cx=px+25, cy=PY_D+PH_D-3, target_h=48, anchor='bottom')

    # Icon: right side
    icx = px + PW_D - 17

    if i == 0:   # POUR — drops into funnel
        for dx in [icx-4, icx, icx+4]:
            drop(dx, PY_D+14, 7)
        out(f'<polygon points="{icx-10},{PY_D+27} {icx+10},{PY_D+27} {icx+8},{PY_D+44} {icx-8},{PY_D+44}" fill="none" stroke="black" stroke-width="1.2"/>')
    elif i == 1: # WAIT — filter with dashed through-arrow
        out(f'<polygon points="{icx-9},{PY_D+16} {icx+9},{PY_D+16} {icx+7},{PY_D+44} {icx-7},{PY_D+44}" fill="none" stroke="black" stroke-width="1.2"/>')
        out(f'<line x1="{icx}" y1="{PY_D+18}" x2="{icx}" y2="{PY_D+42}" stroke="black" stroke-width="0.8" stroke-dasharray="2.5,2" marker-end="url(#arrsm)"/>')
    elif i == 2: # COLLECT — drops into traced clay_pot
        for dx in [icx-4, icx, icx+4]:
            drop(dx, PY_D+16, 7)
        fig('clay_pot', cx=icx, cy=PY_D+PH_D-7, target_h=22, anchor='bottom')
    elif i == 3: # BOIL — traced clay_pot over angular flames
        fig('clay_pot', cx=icx, cy=PY_D+PH_D-18, target_h=22, anchor='bottom')
        flame(icx-5, PY_D+PH_D-3, w=9, h=12)
        flame(icx+5, PY_D+PH_D-3, w=9, h=12)
        for bxo, byo in [(-3, 17), (3, 14), (0, 11)]:
            out(f'<circle cx="{icx+bxo}" cy="{PY_D+byo}" r="1.5" fill="none" stroke="black" stroke-width="0.8"/>')
    # i==4 DRINK: figure alone tells the story

    circled = ['&#9312;', '&#9313;', '&#9314;', '&#9315;', '&#9316;'][i]
    out(f'<text x="{mid}" y="{PY_D+PH_D+11}" font-size="7" font-weight="bold" text-anchor="middle">{circled} {title}</text>')
    out(f'<text x="{mid}" y="{PY_D+PH_D+20}" font-size="5" font-style="italic" text-anchor="middle">{subtitle}</text>')

    if i < 4:
        ax = px + PW_D + 2
        out(f'<line x1="{ax}" y1="{PY_D+PH_D//2}" x2="{ax+7}" y2="{PY_D+PH_D//2}" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')

out('<line x1="18" y1="577" x2="462" y2="577" stroke="black" stroke-width="0.75"/>')

# ══ BAND E — MATERIAL SYMBOLS (y=578-628) ════════════════════════════════════
out('<text x="240" y="588" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; MATERIAL SYMBOLS &#8212;</text>')

# Two-column, two-row layout (4 entries in 40px — tight but fits)
# Row 1 y≈597, Row 2 y≈614

# CHARCOAL (left col, row 1)
out('<polygon points="20,592 33,589 37,598 31,607 20,607" fill="black"/>')
out('<polygon points="39,590 52,587 55,598 49,607 39,605" fill="black"/>')
out('<text x="60" y="597" font-size="7.5" font-weight="bold">CHARCOAL</text>')
out('<text x="60" y="605" font-size="5" font-style="italic">angular &#183; burnt wood &#183; top layer</text>')

# SAND (right col, row 1)
for xi, yi in [(246,596),(252,593),(258,596),(264,593),(270,596),(276,593),(282,596)]:
    out(f'<circle cx="{xi}" cy="{yi}" r="1.8" fill="#111"/>')
out('<text x="290" y="597" font-size="7.5" font-weight="bold">SAND</text>')
out('<text x="290" y="605" font-size="5" font-style="italic">fine grains &#183; riverbank &#183; middle layer</text>')

# GRAVEL (left col, row 2)
for ex, ey, erx, ery in [(28,616,8,5.5),(46,615,7,4.5),(60,616,5.5,3.8)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.5"/>')
out('<text x="72" y="616" font-size="7.5" font-weight="bold">GRAVEL</text>')
out('<text x="72" y="624" font-size="5" font-style="italic">rounded stones &#183; streambed &#183; bottom layer</text>')

# VESSEL (right col, row 2) — traced clay_pot at small scale
fig('clay_pot', cx=252, cy=626, target_h=14, anchor='bottom')
out('<text x="268" y="616" font-size="7.5" font-weight="bold">VESSEL</text>')
out('<text x="268" y="624" font-size="5" font-style="italic">any clay pot that holds water and survives fire</text>')

# ── FOOTER ────────────────────────────────────────────────────────────────────
out('<line x1="6" y1="629" x2="474" y2="629" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="639" font-size="6" text-anchor="middle" letter-spacing="0.8">PLATE 02 V7 &#183; CC BY-SA 4.0 &#183; REMEMBER FORWARD &#183; rememberforward.org &#183; DOI 10.5281/zenodo.19545922</text>')
out('<line x1="6" y1="645" x2="474" y2="645" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="660" font-size="7.5" font-weight="bold" font-style="italic" text-anchor="middle">THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.</text>')
out('<text x="240" y="672" font-size="7" font-style="italic" text-anchor="middle">BUY IT &#183; BUILD IT &#183; BURY IT &#183; FOR SOMEONE YOU WILL NEVER MEET</text>')

out('</svg>')

os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {OUTFILE}')

try:
    import os as _os; _os.startfile(OUTFILE)
except Exception:
    pass
