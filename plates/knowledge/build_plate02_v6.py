#!/usr/bin/env python3
"""
build_plate02_v6.py — Plate 02 v6: Water — Filter and Purify
Comprehensive redesign. Every figure placement is deliberate.

Narrative structure:
  A. WHY:     dirty water → sick | filtered+boiled water → healthy drinking
  B. BUILD:   cross-section of filter (charcoal/sand/gravel layers)
  C. COLLECT: gravel from streambed, sand from bank, charcoal from fire
  D. USE:     5-step sequence — pour, wait, collect, boil, drink
  E. KEY:     material symbols reference

Figures used:
  lying_sick      — horizontal, clearly incapacitated (Section A left)
  drinking_clean  — kneeling, pot raised to lips (Section A right + D step 5)
  kneeling        — reaching forward/down (Section C panels + D step 3)
  pouring_filter  — standing, pot tilted downward (D step 1)
  seated          — cross-legged, waiting (D step 2)
  tending_fire    — crouching beside fire (D step 4 + C charcoal)
  clay_pot        — standalone vessel (material reference)
"""

import os, json, random

OUTDIR  = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02_v6_water_filter.svg')
FIGDATA = r'C:\Users\kanta\Documents\remember-forward\reference_images\figures\figure_paths.json'

with open(FIGDATA, encoding='utf-8') as f:
    FIGS = json.load(f)

lines = []
def out(s): lines.append(s)

# ── FIGURE PLACEMENT ──────────────────────────────────────────────────────────

def fig(name, cx, cy, target_h, anchor='bottom'):
    """Place a traced figure. anchor: bottom/center/top."""
    f   = FIGS[name]
    bb  = f['bbox']
    s   = target_h / bb['h']
    fw  = bb['w'] * s
    fh  = target_h
    if   anchor == 'bottom': ty = cy - fh
    elif anchor == 'center': ty = cy - fh/2
    else:                    ty = cy
    tx  = cx - fw/2
    out(f'<g transform="translate({tx:.1f},{ty:.1f}) scale({s:.4f}) translate({-bb["x"]:.1f},{-bb["y"]:.1f})">')
    for d in f['paths']:
        out(f'  <path d="{d}" fill="black" fill-rule="evenodd"/>')
    out('</g>')

def fig_width(name, target_h):
    """Return scaled width of a figure at given height."""
    bb = FIGS[name]['bbox']
    return bb['w'] * (target_h / bb['h'])

# ── UTILITIES ─────────────────────────────────────────────────────────────────

def wavy(x1, x2, y, n=6, amp=3, sw=1.2, color="black"):
    seg = (x2-x1)/n
    d = f"M {x1:.1f} {y:.1f}"
    for i in range(n):
        sx = x1+i*seg
        ey = y-amp if i%2==0 else y+amp
        d += f" Q {sx+seg/2:.1f} {ey:.1f} {sx+seg:.1f} {y:.1f}"
    out(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw:.1f}"/>')

def drop(cx, ty, h=9):
    out(f'<path d="M {cx:.1f} {ty:.1f} Q {cx-2.5:.1f} {ty+h*0.7:.1f} {cx:.1f} {ty+h:.1f} Q {cx+2.5:.1f} {ty+h*0.7:.1f} {cx:.1f} {ty:.1f}" fill="black"/>')

def flame(cx, by, w=14, h=18):
    """Simple black flame silhouette."""
    hw = w/2
    out(f'<path d="M {cx:.1f} {by:.1f} Q {cx-hw:.1f} {by-h*0.4:.1f} {cx-hw*0.5:.1f} {by-h*0.7:.1f} Q {cx-hw*0.3:.1f} {by-h*0.5:.1f} {cx:.1f} {by-h:.1f} Q {cx+hw*0.3:.1f} {by-h*0.5:.1f} {cx+hw*0.5:.1f} {by-h*0.7:.1f} Q {cx+hw:.1f} {by-h*0.4:.1f} {cx:.1f} {by:.1f} Z" fill="black"/>')

def clay_pot_svg(cx, cy, w=18, h=22):
    """Hand-drawn clay pot silhouette (round belly, narrow neck)."""
    hw = w/2
    nh = h*0.25  # neck height
    bh = h*0.75  # belly height
    # belly (ellipse-ish rounded rect)
    out(f'<ellipse cx="{cx:.1f}" cy="{cy+nh+bh*0.5:.1f}" rx="{hw:.1f}" ry="{bh*0.5:.1f}" fill="black"/>')
    # neck
    nw = hw*0.55
    out(f'<rect x="{cx-nw:.1f}" y="{cy:.1f}" width="{nw*2:.1f}" height="{nh+2:.1f}" rx="{nw*0.4:.1f}" fill="black"/>')

# ── DEFS & HEADER ─────────────────────────────────────────────────────────────

out('<?xml version="1.0" encoding="UTF-8"?>')
out('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">')
out('<rect width="480" height="680" fill="white"/>')
out('''<defs>
  <pattern id="coal" x="0" y="0" width="28" height="22" patternUnits="userSpaceOnUse">
    <rect width="28" height="22" fill="white"/>
    <polygon points="1,3 13,1 17,8 13,17 2,18 0,9" fill="black"/>
    <polygon points="16,2 27,0 28,11 23,19 16,16 14,8" fill="black"/>
  </pattern>
  <pattern id="sand" x="0" y="0" width="8" height="7" patternUnits="userSpaceOnUse">
    <circle cx="4" cy="3.5" r="1.8" fill="#111"/>
    <circle cx="0" cy="7" r="1.8" fill="#111"/>
    <circle cx="8" cy="7" r="1.8" fill="#111"/>
  </pattern>
  <pattern id="grav" x="0" y="0" width="36" height="28" patternUnits="userSpaceOnUse">
    <rect width="36" height="28" fill="white"/>
    <ellipse cx="9"  cy="8"  rx="7"   ry="5"   fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="26" cy="7"  rx="7.5" ry="4.5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="7"  cy="21" rx="5"   ry="3.5" fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="24" cy="21" rx="8"   ry="5"   fill="none" stroke="black" stroke-width="1.3"/>
    <ellipse cx="34" cy="19" rx="3.5" ry="2.8" fill="none" stroke="black" stroke-width="1.1"/>
  </pattern>
  <clipPath id="c-coal"><polygon points="154,116 326,116 319,172 161,172"/></clipPath>
  <clipPath id="c-sand"><polygon points="161,172 319,172 312,230 168,230"/></clipPath>
  <clipPath id="c-grav"><polygon points="168,230 312,230 302,348 178,348"/></clipPath>
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

# ══ A — WHY ═══════════════════════════════════════════════════════════════════
out('<text x="240" y="68" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2.5">&#8212; WHY THIS MATTERS &#8212;</text>')

# Left: contaminated water → sick
out('<rect x="20" y="72" width="200" height="68" fill="none" stroke="black" stroke-width="0.8"/>')
# Heavy dark waves = contaminated
for i in range(7):
    wx, wy = 26+i*16, (84 if i%2==0 else 88)
    out(f'<path d="M {wx} {wy} Q {wx+5} {wy-5} {wx+10} {wy} Q {wx+16} {wy+4} {wx+22} {wy}" fill="none" stroke="black" stroke-width="2.5"/>')
out('<text x="68" y="100" font-size="7" font-weight="bold" text-anchor="middle">CONTAMINATED WATER</text>')
# Arrow to sick figure
out('<line x1="130" y1="105" x2="148" y2="105" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')
# Lying sick figure: fits in right portion of left panel
fig('lying_sick', cx=178, cy=138, target_h=36, anchor='bottom')
out('<text x="180" y="134" font-size="6.5" font-weight="bold" text-anchor="middle">ILLNESS / DEATH</text>')

# Arrow between panels
out('<text x="229" y="109" font-size="18" text-anchor="middle" font-weight="bold">&#8800;</text>')
out('<line x1="18" y1="142" x2="462" y2="142" stroke="black" stroke-width="0.75"/>')

# Right: filtered+boiled → drinking healthy
out('<rect x="260" y="72" width="200" height="68" fill="none" stroke="black" stroke-width="0.8"/>')
# Light clean waves
for yi in [82, 90, 98]:
    wavy(268, 370, yi, n=5, amp=2, sw=1.0)
out('<text x="310" y="80" font-size="7" font-weight="bold" text-anchor="middle">FILTERED + BOILED</text>')
out('<line x1="310" y1="103" x2="328" y2="103" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')
# Drinking clean figure (kneeling, pot raised to lips)
fig('drinking_clean', cx=415, cy=138, target_h=56, anchor='bottom')
out('<text x="415" y="134" font-size="6.5" font-weight="bold" text-anchor="middle">SAFE TO DRINK</text>')

# ══ B — BUILD THE FILTER ══════════════════════════════════════════════════════
out('<text x="155" y="154" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; BUILD THE FILTER &#8212;</text>')
out('<text x="155" y="163" font-size="5.5" font-style="italic" text-anchor="middle">cross-section &#183; layer order is critical</text>')
out('<text x="240" y="108" font-size="6.5" font-style="italic" text-anchor="middle">dirty water &#8595;</text>')

# Container
out('<polygon points="154,112 326,112 302,350 178,350" fill="none" stroke="black" stroke-width="3.5"/>')
out('<ellipse cx="240" cy="112" rx="86" ry="7" fill="white" stroke="black" stroke-width="2.2"/>')
for xi in [200, 220, 240, 260, 280]:
    out(f'<line x1="{xi}" y1="108" x2="{xi}" y2="116" stroke="black" stroke-width="1.0" marker-end="url(#arrsm)"/>')

# Drain gaps at base
out('<line x1="178" y1="350" x2="198" y2="350" stroke="black" stroke-width="3.5"/>')
out('<line x1="220" y1="350" x2="260" y2="350" stroke="black" stroke-width="3.5"/>')
out('<line x1="282" y1="350" x2="302" y2="350" stroke="black" stroke-width="3.5"/>')

# Material layers
out('<rect x="0" y="0" width="480" height="680" fill="url(#coal)" clip-path="url(#c-coal)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#sand)" clip-path="url(#c-sand)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#grav)" clip-path="url(#c-grav)"/>')
out('<line x1="161" y1="172" x2="319" y2="172" stroke="black" stroke-width="1.8"/>')
out('<line x1="168" y1="230" x2="312" y2="230" stroke="black" stroke-width="1.8"/>')

# Layer badges
for num, yp, label in [('1',144,'CHARCOAL'),('2',201,'SAND'),('3',290,'GRAVEL')]:
    out(f'<circle cx="130" cy="{yp}" r="9" fill="black"/>')
    out(f'<text x="130" y="{yp+3.5}" font-size="9" font-weight="bold" text-anchor="middle" fill="white">{num}</text>')
    out(f'<line x1="139" y1="{yp}" x2="152" y2="{yp}" stroke="black" stroke-width="0.8" marker-end="url(#arrsm)"/>')
    out(f'<text x="128" y="{yp-12}" font-size="7.5" font-weight="bold" text-anchor="middle">{label}</text>')

# Filter output: clean wavy lines
out('<line x1="240" y1="350" x2="240" y2="362" stroke="black" stroke-width="1.3"/>')
out('<line x1="222" y1="350" x2="222" y2="357" stroke="black" stroke-width="1.1"/>')
out('<line x1="258" y1="350" x2="258" y2="357" stroke="black" stroke-width="1.1"/>')
for yi in [363, 370, 377]:
    wavy(218, 262, yi, n=4, amp=2, sw=1.0)
out('<text x="240" y="392" font-size="7" font-weight="bold" text-anchor="middle">&#8595; BOIL BEFORE DRINKING &#8595;</text>')
out('<text x="240" y="402" font-size="5.5" font-style="italic" text-anchor="middle">filtering alone does not make water safe</text>')

out('<line x1="348" y1="142" x2="348" y2="408" stroke="black" stroke-width="0.6"/>')

# ══ C — COLLECT MATERIALS ═════════════════════════════════════════════════════
out('<text x="405" y="154" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; COLLECT &#8212;</text>')

# Panel 1: GRAVEL — kneeling at streambed
out('<rect x="352" y="162" width="106" height="56" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="172" font-size="6.5" font-weight="bold" text-anchor="middle">&#9312; GRAVEL</text>')
fig('kneeling', cx=382, cy=215, target_h=36, anchor='bottom')
out('<path d="M 354 213 Q 366 210 378 213 Q 390 216 402 213 Q 414 210 426 213 Q 440 216 452 213" fill="none" stroke="black" stroke-width="1.0"/>')
for ex,ey,erx,ery in [(363,210,4.5,2.8),(376,211,4,2.5),(390,210,5,3),(403,211,3.8,2.5),(416,210,4.5,2.8)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.1"/>')
out('<text x="432" y="212" font-size="5" font-style="italic">stream</text>')

# Panel 2: SAND — kneeling at sandy bank
out('<rect x="352" y="222" width="106" height="56" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="232" font-size="6.5" font-weight="bold" text-anchor="middle">&#9313; SAND</text>')
fig('kneeling', cx=382, cy=275, target_h=36, anchor='bottom')
for sx in range(356,450,7):
    for sy in [260,265,270]:
        random.seed(sx*100+sy)
        jx = random.uniform(-2,2)
        out(f'<circle cx="{sx+jx:.1f}" cy="{sy}" r="1.1" fill="black"/>')
out('<text x="432" y="272" font-size="5" font-style="italic">bank</text>')

# Panel 3: CHARCOAL — tending_fire figure + burn→cover→collect
out('<rect x="352" y="282" width="106" height="68" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="292" font-size="6.5" font-weight="bold" text-anchor="middle">&#9314; CHARCOAL</text>')
# Use tending_fire for the burn step
fig('tending_fire', cx=372, cy=346, target_h=40, anchor='bottom')
# Fire symbol beside figure
flame(390, 342, w=10, h=14)
# Arrow + cover mound + arrow + chunks
out('<text x="404" y="326" font-size="7" text-anchor="middle">&#8594;</text>')
mx = 416
out(f'<ellipse cx="{mx}" cy="336" rx="8" ry="4" fill="black"/>')
out(f'<path d="M {mx-8} 336 Q {mx} 326 {mx+8} 336" fill="none" stroke="black" stroke-width="1.8"/>')
out('<text x="431" y="326" font-size="7" text-anchor="middle">&#8594;</text>')
cx2 = 442
out(f'<polygon points="{cx2-5},332 {cx2},328 {cx2+3},335 {cx2-1},341 {cx2-6},340" fill="black"/>')
out(f'<polygon points="{cx2+1},330 {cx2+6},328 {cx2+8},336 {cx2+5},341 {cx2+1},340" fill="black"/>')
out('<text x="372" y="350" font-size="5" font-style="italic" text-anchor="middle">burn</text>')
out('<text x="416" y="350" font-size="5" font-style="italic" text-anchor="middle">cover</text>')
out('<text x="442" y="350" font-size="5" font-style="italic" text-anchor="middle">collect</text>')

out('<line x1="18" y1="408" x2="462" y2="408" stroke="black" stroke-width="0.75"/>')

# ══ D — HOW TO USE (5 steps) ══════════════════════════════════════════════════
out('<text x="240" y="420" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; HOW TO USE THE FILTER &#8212;</text>')

py, ph = 426, 62
pw  = 82
pxs = [20, 110, 200, 290, 380]

steps = [
    ('pouring_filter', 'POUR',    'dirty water\ninto top'),
    ('seated',         'WAIT',    'water passes\nthrough layers'),
    ('kneeling',       'COLLECT', 'filtered water\nat bottom'),
    ('tending_fire',   'BOIL',    'before\ndrinking'),
    ('drinking_clean', 'DRINK',   'only after\nboiling'),
]

for i, (fname, title, subtitle) in enumerate(steps):
    px  = pxs[i]
    mid = px + pw/2

    out(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="none" stroke="black" stroke-width="0.7"/>')
    out(f'<circle cx="{px+10}" cy="{py+10}" r="7" fill="black"/>')
    out(f'<text x="{px+10}" y="{py+14}" font-size="8" font-weight="bold" text-anchor="middle" fill="white">{i+1}</text>')

    # Figure on left of panel
    fig(fname, cx=px+22, cy=py+ph-3, target_h=46, anchor='bottom')

    # Icon on right of panel
    icon_cx = px + pw - 20
    icon_mid = px + pw - 22

    if i == 0:   # POUR: drops falling into filter funnel
        for dx in [icon_mid-5, icon_mid, icon_mid+5]:
            drop(dx, py+12, 8)
        out(f'<polygon points="{icon_mid-12:.0f},{py+26} {icon_mid+12:.0f},{py+26} {icon_mid+9:.0f},{py+44} {icon_mid-9:.0f},{py+44}" fill="none" stroke="black" stroke-width="1.2"/>')

    elif i == 1: # WAIT: filter with dashed arrow
        out(f'<polygon points="{icon_mid-10:.0f},{py+14} {icon_mid+10:.0f},{py+14} {icon_mid+7:.0f},{py+42} {icon_mid-7:.0f},{py+42}" fill="none" stroke="black" stroke-width="1.2"/>')
        out(f'<line x1="{icon_mid:.0f}" y1="{py+16}" x2="{icon_mid:.0f}" y2="{py+40}" stroke="black" stroke-width="0.8" stroke-dasharray="2.5,2" marker-end="url(#arrsm)"/>')

    elif i == 2: # COLLECT: clay pot below filter drips
        for dx in [icon_mid-5, icon_mid, icon_mid+5]:
            drop(dx, py+14, 8)
        clay_pot_svg(icon_mid, py+34, w=20, h=20)

    elif i == 3: # BOIL: clay pot over flames
        clay_pot_svg(icon_mid, py+22, w=18, h=18)
        flame(icon_mid-4, py+44, w=8, h=12)
        flame(icon_mid+4, py+44, w=8, h=12)
        # steam dots above pot
        for bxo, byo in [(-3, 18),(3,15),(0,12)]:
            out(f'<circle cx="{icon_mid+bxo:.0f}" cy="{py+byo}" r="1.5" fill="none" stroke="black" stroke-width="0.8"/>')

    elif i == 4: # DRINK: figure tells the whole story, no extra icon needed
        pass

    # Labels
    out(f'<text x="{mid:.0f}" y="{py+ph+9:.0f}" font-size="6.5" font-weight="bold" text-anchor="middle">{title}</text>')
    for li, ll in enumerate(subtitle.split('\n')):
        out(f'<text x="{mid:.0f}" y="{py+ph+17+li*8:.0f}" font-size="5.5" font-style="italic" text-anchor="middle">{ll}</text>')

    # Arrow to next step
    if i < 4:
        ax = px + pw + 2
        out(f'<line x1="{ax}" y1="{py+ph/2:.0f}" x2="{ax+8}" y2="{py+ph/2:.0f}" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')

out('<line x1="18" y1="516" x2="462" y2="516" stroke="black" stroke-width="0.75"/>')

# ══ E — MATERIAL KEY ══════════════════════════════════════════════════════════
out('<text x="240" y="527" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">&#8212; MATERIAL SYMBOLS &#8212;</text>')

# Charcoal
out('<polygon points="26,535 40,531 44,542 38,552 25,552" fill="black"/>')
out('<polygon points="46,532 62,529 65,541 59,551 46,549" fill="black"/>')
out('<text x="72" y="539" font-size="8" font-weight="bold">CHARCOAL</text>')
out('<text x="72" y="549" font-size="6" font-style="italic">angular &#183; jagged &#183; from burnt wood &#183; used in layer 1</text>')

# Sand
for xi,yi in [(26,563),(33,560),(40,563),(47,560),(54,563),(61,560),(68,563)]:
    out(f'<circle cx="{xi}" cy="{yi}" r="2" fill="#111"/>')
out('<text x="78" y="563" font-size="8" font-weight="bold">SAND</text>')
out('<text x="78" y="573" font-size="6" font-style="italic">fine uniform grains &#183; from riverbank or dry bed &#183; layer 2</text>')

# Gravel
for ex,ey,erx,ery in [(34,588,9,6),(58,587,8,5.5),(76,588,6.5,4.5)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.5"/>')
out('<text x="90" y="587" font-size="8" font-weight="bold">GRAVEL</text>')
out('<text x="90" y="597" font-size="6" font-style="italic">smooth rounded stones &#183; from streambed &#183; layer 3 (bottom)</text>')

# Clay pot reference
clay_pot_svg(32, 604, w=22, h=26)
out('<text x="50" y="610" font-size="8" font-weight="bold">VESSEL</text>')
out('<text x="50" y="620" font-size="6" font-style="italic">any clay pot or container that can hold water and withstand fire</text>')

# ── FOOTER ───────────────────────────────────────────────────────────────────
out('<line x1="6" y1="630" x2="474" y2="630" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="640" font-size="6" text-anchor="middle" letter-spacing="0.8">PLATE 02 V6 &#183; CC BY-SA 4.0 &#183; REMEMBER FORWARD &#183; rememberforward.org &#183; DOI 10.5281/zenodo.19545922</text>')
out('<line x1="6" y1="646" x2="474" y2="646" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="661" font-size="7.5" font-weight="bold" font-style="italic" text-anchor="middle">THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.</text>')
out('<text x="240" y="673" font-size="7" font-style="italic" text-anchor="middle">BUY IT &#183; BUILD IT &#183; BURY IT &#183; FOR SOMEONE YOU WILL NEVER MEET</text>')

out('</svg>')

os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {OUTFILE}')

try:
    import os as _os; _os.startfile(OUTFILE)
except Exception:
    pass
