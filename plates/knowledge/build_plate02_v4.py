#!/usr/bin/env python3
"""
build_plate02_v4.py  —  Plate 02 v4: Water Filter and Purify

Changes from v3:
- fig_sick  → fig_lying_sick: horizontal side-profile (ISOTYPE 00183 principle)
- fig_crouching → fig_kneeling: one knee down, torso forward (ISOTYPE 00386)
- fig_standing → fig_standing_profile: true side profile
- How-to-use panels: human figures added to all 4 panels
- Clean water: wavy lines instead of teardrops
- Vessel: rounded bowl instead of rectangle
- White cut-lines within torso to separate arm from body
"""

import os, random

OUTDIR = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02_v4_water_filter.svg')

lines = []
def out(s): lines.append(s)

# ── FIGURES ──────────────────────────────────────────────────────────────────

def fig_standing_profile(cx, cy, s=1.0):
    """Side-profile standing figure. cy = top of head."""
    r = 5*s
    out(f'<circle cx="{cx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    tx, ty, tw, th = cx-4*s, cy+2*r+0.5*s, 8*s, 14*s
    out(f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{tw:.1f}" height="{th:.1f}" rx="{2*s:.1f}" fill="black"/>')
    fy = ty+th
    out(f'<rect x="{cx-1*s:.1f}" y="{fy:.1f}" width="{3.5*s:.1f}" height="{13*s:.1f}" rx="{1.5*s:.1f}" fill="black" transform="rotate(6,{cx:.1f},{fy:.1f})"/>')
    out(f'<rect x="{cx-5*s:.1f}" y="{fy:.1f}" width="{3.5*s:.1f}" height="{12*s:.1f}" rx="{1.5*s:.1f}" fill="black" transform="rotate(-4,{cx-3*s:.1f},{fy:.1f})"/>')

def fig_lying_sick(lx, cy, s=1.0):
    """Horizontal side-profile figure lying down. lx=left edge, cy=center."""
    r = 5*s
    out(f'<circle cx="{lx+r:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="black"/>')
    tx, th, tw = lx+2*r+0.5*s, 8*s, 18*s
    ty = cy - th/2
    out(f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{tw:.1f}" height="{th:.1f}" rx="{2*s:.1f}" fill="black"/>')
    # white cut-line: separates arm from torso
    cut_x = tx + 5*s
    out(f'<line x1="{cut_x:.1f}" y1="{ty:.1f}" x2="{cut_x+0.5*s:.1f}" y2="{ty+th:.1f}" stroke="white" stroke-width="{1.5*s:.1f}"/>')
    # arm bent slightly upward (weakness — can't hold it up fully)
    out(f'<line x1="{cut_x+0.5*s:.1f}" y1="{ty+2*s:.1f}" x2="{cut_x+5*s:.1f}" y2="{ty-6*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')
    hpx = tx + tw
    # back leg: upper thigh, then knee bends back
    out(f'<line x1="{hpx:.1f}" y1="{cy-1*s:.1f}" x2="{hpx+12*s:.1f}" y2="{cy+2*s:.1f}" stroke="black" stroke-width="{5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hpx+12*s:.1f}" y1="{cy+2*s:.1f}" x2="{hpx+9*s:.1f}" y2="{cy-5*s:.1f}" stroke="black" stroke-width="{4*s:.1f}" stroke-linecap="round"/>')
    # front leg: offset down, also bends
    out(f'<line x1="{hpx:.1f}" y1="{cy+2*s:.1f}" x2="{hpx+13*s:.1f}" y2="{cy+5*s:.1f}" stroke="black" stroke-width="{4.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hpx+13*s:.1f}" y1="{cy+5*s:.1f}" x2="{hpx+11*s:.1f}" y2="{cy-2*s:.1f}" stroke="black" stroke-width="{3.5*s:.1f}" stroke-linecap="round"/>')

def fig_kneeling(cx, cy, s=1.0):
    """Side-profile kneeling figure: one knee down, torso forward, arm reaching.
    Based on ISOTYPE 00386. cx=center, cy=top of head."""
    r = 5*s
    hx = cx - 2*s
    out(f'<circle cx="{hx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    sh_x, sh_y = hx, cy+2*r+1*s
    hip_x, hip_y = cx+5*s, sh_y+14*s
    # torso diagonal
    out(f'<line x1="{sh_x:.1f}" y1="{sh_y:.1f}" x2="{hip_x:.1f}" y2="{hip_y:.1f}" stroke="black" stroke-width="{9*s:.1f}" stroke-linecap="round"/>')
    # front arm reaching forward-down
    out(f'<line x1="{sh_x-1*s:.1f}" y1="{sh_y+3*s:.1f}" x2="{sh_x-9*s:.1f}" y2="{hip_y+4*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')
    # back leg: knee goes to ground, lower leg lies back
    out(f'<line x1="{hip_x:.1f}" y1="{hip_y:.1f}" x2="{hip_x+9*s:.1f}" y2="{hip_y+13*s:.1f}" stroke="black" stroke-width="{4.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x+9*s:.1f}" y1="{hip_y+13*s:.1f}" x2="{hip_x+18*s:.1f}" y2="{hip_y+12*s:.1f}" stroke="black" stroke-width="{3.5*s:.1f}" stroke-linecap="round"/>')
    # front leg: thigh forward, shin down
    out(f'<line x1="{hip_x:.1f}" y1="{hip_y:.1f}" x2="{hip_x-8*s:.1f}" y2="{hip_y+13*s:.1f}" stroke="black" stroke-width="{4*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x-8*s:.1f}" y1="{hip_y+13*s:.1f}" x2="{hip_x-12*s:.1f}" y2="{hip_y+9*s:.1f}" stroke="black" stroke-width="{3.5*s:.1f}" stroke-linecap="round"/>')

# ── SMALL PANEL FIGURES (s≈0.50) ──────────────────────────────────────────

def fig_sm_pouring(cx, cy, s=0.50):
    r = 4*s
    out(f'<circle cx="{cx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    tx, ty, tw, th = cx-3*s, cy+2*r+0.5*s, 6*s, 11*s
    out(f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{tw:.1f}" height="{th:.1f}" rx="{1.5*s:.1f}" fill="black"/>')
    ay = ty+2*s
    # arms raised holding container
    out(f'<line x1="{tx+tw:.1f}" y1="{ay:.1f}" x2="{tx+tw+8*s:.1f}" y2="{ay-5*s:.1f}" stroke="black" stroke-width="{2.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{tx:.1f}" y1="{ay:.1f}" x2="{tx+tw+5*s:.1f}" y2="{ay-7*s:.1f}" stroke="black" stroke-width="{2*s:.1f}" stroke-linecap="round"/>')
    # tilted container
    bx, by = tx+tw+8*s, ay-5*s
    out(f'<rect x="{bx-2*s:.1f}" y="{by-7*s:.1f}" width="{6*s:.1f}" height="{8*s:.1f}" rx="{s:.1f}" fill="none" stroke="black" stroke-width="{1.5*s:.1f}" transform="rotate(28,{bx:.1f},{by:.1f})"/>')
    fy = ty+th
    out(f'<rect x="{cx-1*s:.1f}" y="{fy:.1f}" width="{2.5*s:.1f}" height="{9*s:.1f}" rx="{s:.1f}" fill="black"/>')
    out(f'<rect x="{cx-4*s:.1f}" y="{fy:.1f}" width="{2.5*s:.1f}" height="{8*s:.1f}" rx="{s:.1f}" fill="black"/>')

def fig_sm_seated(cx, cy, s=0.50):
    r = 4*s
    out(f'<circle cx="{cx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    sh_y = cy+2*r+0.5*s
    out(f'<line x1="{cx:.1f}" y1="{sh_y:.1f}" x2="{cx+1*s:.1f}" y2="{sh_y+11*s:.1f}" stroke="black" stroke-width="{6*s:.1f}" stroke-linecap="round"/>')
    hip_y = sh_y+11*s
    out(f'<line x1="{cx+1*s:.1f}" y1="{hip_y:.1f}" x2="{cx+12*s:.1f}" y2="{hip_y:.1f}" stroke="black" stroke-width="{4.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{cx+12*s:.1f}" y1="{hip_y:.1f}" x2="{cx+12*s:.1f}" y2="{hip_y+10*s:.1f}" stroke="black" stroke-width="{3.5*s:.1f}" stroke-linecap="round"/>')

def fig_sm_kneeling(cx, cy, s=0.50):
    r = 4*s
    hx = cx-1*s
    out(f'<circle cx="{hx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    sh_x, sh_y = hx, cy+2*r+0.5*s
    hip_x, hip_y = cx+3*s, sh_y+11*s
    out(f'<line x1="{sh_x:.1f}" y1="{sh_y:.1f}" x2="{hip_x:.1f}" y2="{hip_y:.1f}" stroke="black" stroke-width="{7*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{sh_x:.1f}" y1="{sh_y+2*s:.1f}" x2="{sh_x-6*s:.1f}" y2="{hip_y+3*s:.1f}" stroke="black" stroke-width="{2.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x:.1f}" y1="{hip_y:.1f}" x2="{hip_x+7*s:.1f}" y2="{hip_y+10*s:.1f}" stroke="black" stroke-width="{3.5*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x+7*s:.1f}" y1="{hip_y+10*s:.1f}" x2="{hip_x+14*s:.1f}" y2="{hip_y+9*s:.1f}" stroke="black" stroke-width="{3*s:.1f}" stroke-linecap="round"/>')
    out(f'<line x1="{hip_x:.1f}" y1="{hip_y:.1f}" x2="{hip_x-6*s:.1f}" y2="{hip_y+10*s:.1f}" stroke="black" stroke-width="{3.5*s:.1f}" stroke-linecap="round"/>')

def fig_sm_standing(cx, cy, s=0.50):
    r = 4*s
    out(f'<circle cx="{cx:.1f}" cy="{cy+r:.1f}" r="{r:.1f}" fill="black"/>')
    tx, ty, tw, th = cx-3*s, cy+2*r+0.5*s, 6*s, 11*s
    out(f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{tw:.1f}" height="{th:.1f}" rx="{1.5*s:.1f}" fill="black"/>')
    fy = ty+th
    out(f'<rect x="{cx-0.5*s:.1f}" y="{fy:.1f}" width="{2.5*s:.1f}" height="{9*s:.1f}" rx="{s:.1f}" fill="black" transform="rotate(5,{cx:.1f},{fy:.1f})"/>')
    out(f'<rect x="{cx-4*s:.1f}" y="{fy:.1f}" width="{2.5*s:.1f}" height="{8*s:.1f}" rx="{s:.1f}" fill="black" transform="rotate(-3,{cx-2*s:.1f},{fy:.1f})"/>')

# ── UTILITIES ────────────────────────────────────────────────────────────────

def wavy(x1, x2, y, n=6, amp=3, sw=1.2, color="black"):
    seg = (x2-x1)/n
    d = f"M {x1:.1f} {y:.1f}"
    for i in range(n):
        sx = x1+i*seg
        ey = y-amp if i%2==0 else y+amp
        d += f" Q {sx+seg/2:.1f} {ey:.1f} {sx+seg:.1f} {y:.1f}"
    out(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw:.1f}"/>')

def bowl(cx, by, w, h, sw=1.5):
    hw = w/2
    out(f'<path d="M {cx-hw:.1f} {by:.1f} L {cx-hw:.1f} {by+h*0.4:.1f} Q {cx-hw:.1f} {by+h:.1f} {cx:.1f} {by+h:.1f} Q {cx+hw:.1f} {by+h:.1f} {cx+hw:.1f} {by+h*0.4:.1f} L {cx+hw:.1f} {by:.1f}" fill="none" stroke="black" stroke-width="{sw:.1f}"/>')
    out(f'<line x1="{cx-hw-2:.1f}" y1="{by:.1f}" x2="{cx+hw+2:.1f}" y2="{by:.1f}" stroke="black" stroke-width="{sw:.1f}"/>')

def drop(cx, ty, h, fill="black"):
    out(f'<path d="M {cx:.1f} {ty:.1f} Q {cx-3:.1f} {ty+h*0.7:.1f} {cx:.1f} {ty+h:.1f} Q {cx+3:.1f} {ty+h*0.7:.1f} {cx:.1f} {ty:.1f}" fill="{fill}"/>')

# ── DEFS ─────────────────────────────────────────────────────────────────────

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

# BORDERS
out('<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="black" stroke-width="3"/>')
out('<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="black" stroke-width="0.75"/>')

# ── HEADER ───────────────────────────────────────────────────────────────────
out('<text x="240" y="32" font-size="11" font-weight="bold" text-anchor="middle" letter-spacing="2">WATER — FILTER AND PURIFY</text>')
out('<line x1="18" y1="38" x2="462" y2="38" stroke="black" stroke-width="1"/>')
out('<text x="240" y="50" font-size="7" text-anchor="middle" letter-spacing="1.5">PLATE 02 · SURVIVAL KNOWLEDGE · CLEAN WATER PREVENTS ILLNESS AND DEATH</text>')
out('<line x1="18" y1="56" x2="462" y2="56" stroke="black" stroke-width="0.5"/>')

# ══ A — WHY ══════════════════════════════════════════════════════════════════
out('<text x="240" y="68" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2.5">— WHY THIS MATTERS —</text>')

# Left panel: dirty water + lying sick figure
out('<rect x="20" y="72" width="200" height="66" fill="none" stroke="black" stroke-width="0.8"/>')
for i in range(7):
    wx = 26 + i*16
    wy = 84 if i%2==0 else 87
    out(f'<path d="M {wx} {wy} Q {wx+5} {wy-5} {wx+10} {wy} Q {wx+16} {wy+4} {wx+22} {wy}" fill="none" stroke="black" stroke-width="2.5"/>')
out('<text x="68" y="100" font-size="7.5" font-weight="bold" text-anchor="middle">CONTAMINATED</text>')
out('<text x="68" y="110" font-size="6" font-style="italic" text-anchor="middle">murky · smells · standing</text>')
fig_lying_sick(118, 108, s=0.72)
out('<text x="175" y="132" font-size="7" font-weight="bold" text-anchor="middle">ILLNESS</text>')

out('<text x="229" y="108" font-size="14" text-anchor="middle">→</text>')

# Right panel: clean water + standing profile figure
out('<rect x="260" y="72" width="200" height="66" fill="none" stroke="black" stroke-width="0.8"/>')
for yi in [83, 91, 99]:
    wavy(268, 390, yi, n=5, amp=2.5, sw=1.2)
out('<text x="320" y="111" font-size="7.5" font-weight="bold" text-anchor="middle">FILTERED + BOILED</text>')
out('<text x="320" y="121" font-size="6" font-style="italic" text-anchor="middle">clear · no smell · safe</text>')
fig_standing_profile(432, 74, s=0.85)
out('<text x="432" y="133" font-size="7" font-weight="bold" text-anchor="middle">HEALTHY</text>')

out('<line x1="18" y1="142" x2="462" y2="142" stroke="black" stroke-width="0.75"/>')

# ══ B — BUILD THE FILTER ═════════════════════════════════════════════════════
out('<text x="155" y="154" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— BUILD THE FILTER —</text>')
out('<text x="155" y="164" font-size="6" font-style="italic" text-anchor="middle">cross-section view · layer order critical</text>')
out('<text x="240" y="107" font-size="7" font-style="italic" text-anchor="middle">dirty water ↓</text>')

out('<polygon points="154,112 326,112 302,350 178,350" fill="none" stroke="black" stroke-width="3.5"/>')
out('<ellipse cx="240" cy="112" rx="86" ry="7" fill="white" stroke="black" stroke-width="2.2"/>')
for xi in [200, 220, 240, 260, 280]:
    out(f'<line x1="{xi}" y1="108" x2="{xi}" y2="116" stroke="black" stroke-width="1.0" marker-end="url(#arrsm)"/>')

out('<line x1="178" y1="350" x2="198" y2="350" stroke="black" stroke-width="3.5"/>')
out('<line x1="220" y1="350" x2="260" y2="350" stroke="black" stroke-width="3.5"/>')
out('<line x1="282" y1="350" x2="302" y2="350" stroke="black" stroke-width="3.5"/>')

out('<rect x="0" y="0" width="480" height="680" fill="url(#coal)" clip-path="url(#c-coal)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#sand)" clip-path="url(#c-sand)"/>')
out('<rect x="0" y="0" width="480" height="680" fill="url(#grav)" clip-path="url(#c-grav)"/>')
out('<line x1="161" y1="172" x2="319" y2="172" stroke="black" stroke-width="1.8"/>')
out('<line x1="168" y1="230" x2="312" y2="230" stroke="black" stroke-width="1.8"/>')

for num, yp, label in [('1',144,'CHARCOAL'),('2',201,'SAND'),('3',290,'GRAVEL')]:
    out(f'<circle cx="130" cy="{yp}" r="9" fill="black"/>')
    out(f'<text x="130" y="{yp+3.5}" font-size="9" font-weight="bold" text-anchor="middle" fill="white">{num}</text>')
    out(f'<line x1="139" y1="{yp}" x2="152" y2="{yp}" stroke="black" stroke-width="0.8" marker-end="url(#arrsm)"/>')
    out(f'<text x="128" y="{yp-12}" font-size="7.5" font-weight="bold" text-anchor="middle">{label}</text>')

# filter output: wavy clean water
out('<line x1="240" y1="350" x2="240" y2="362" stroke="black" stroke-width="1.3"/>')
out('<line x1="222" y1="350" x2="222" y2="358" stroke="black" stroke-width="1.1"/>')
out('<line x1="258" y1="350" x2="258" y2="358" stroke="black" stroke-width="1.1"/>')
for yi in [364, 371, 378]:
    wavy(220, 260, yi, n=4, amp=2, sw=1.0)
out('<text x="240" y="393" font-size="7.5" font-weight="bold" text-anchor="middle">THEN BOIL</text>')
out('<text x="240" y="403" font-size="6" font-style="italic" text-anchor="middle">filtered water is not yet safe — boil before drinking</text>')

out('<line x1="348" y1="142" x2="348" y2="408" stroke="black" stroke-width="0.6"/>')

# ══ C — COLLECT ══════════════════════════════════════════════════════════════
out('<text x="405" y="154" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— COLLECT —</text>')

# Panel 1: GRAVEL
out('<rect x="352" y="160" width="106" height="58" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="172" font-size="7" font-weight="bold" text-anchor="middle">① GRAVEL</text>')
fig_kneeling(388, 173, s=0.56)
out('<path d="M 354 213 Q 366 210 378 213 Q 390 216 402 213 Q 414 210 426 213 Q 438 216 452 213" fill="none" stroke="black" stroke-width="1.0"/>')
for ex,ey,erx,ery in [(362,209,5,3),(375,210,4.5,3),(389,209,5.5,3.5),(402,210,4,3),(415,209,5,3)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.1"/>')

# Panel 2: SAND
out('<rect x="352" y="222" width="106" height="58" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="234" font-size="7" font-weight="bold" text-anchor="middle">② SAND</text>')
fig_kneeling(388, 235, s=0.56)
for sx in range(354,452,8):
    for sy in [260,265,270]:
        random.seed(sx*100+sy)
        jx = random.uniform(-2,2)
        out(f'<circle cx="{sx+jx:.1f}" cy="{sy}" r="1.2" fill="black"/>')

# Panel 3: CHARCOAL
out('<rect x="352" y="284" width="106" height="66" fill="none" stroke="black" stroke-width="0.7"/>')
out('<text x="405" y="296" font-size="7" font-weight="bold" text-anchor="middle">③ CHARCOAL</text>')
fx = 368
out(f'<ellipse cx="{fx}" cy="336" rx="10" ry="5" fill="black"/>')
out(f'<path d="M {fx} 334 Q {fx-4} 324 {fx} 318 Q {fx+2} 324 {fx+6} 320 Q {fx+4} 326 {fx+8} 322 Q {fx+6} 330 {fx+5} 334" fill="black"/>')
out('<text x="390" y="330" font-size="9" text-anchor="middle">→</text>')
mx = 408
out(f'<ellipse cx="{mx}" cy="336" rx="10" ry="5" fill="black"/>')
out(f'<path d="M {mx-10} 336 Q {mx} 324 {mx+10} 336" fill="none" stroke="black" stroke-width="2"/>')
out('<text x="428" y="330" font-size="9" text-anchor="middle">→</text>')
cx2 = 443
out(f'<polygon points="{cx2-7},334 {cx2-1},330 {cx2+2},337 {cx2-2},344 {cx2-8},343" fill="black"/>')
out(f'<polygon points="{cx2+1},332 {cx2+8},330 {cx2+10},339 {cx2+6},344 {cx2},342" fill="black"/>')
out('<text x="368" y="348" font-size="5.5" font-style="italic" text-anchor="middle">burn</text>')
out('<text x="408" y="348" font-size="5.5" font-style="italic" text-anchor="middle">cover</text>')
out('<text x="443" y="348" font-size="5.5" font-style="italic" text-anchor="middle">collect</text>')

out('<line x1="18" y1="408" x2="462" y2="408" stroke="black" stroke-width="0.75"/>')

# ══ D — HOW TO USE ═══════════════════════════════════════════════════════════
out('<text x="240" y="420" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— HOW TO USE THE FILTER —</text>')

py, ph, pw = 426, 62, 100
pxs = [20, 128, 236, 344]
labels = ['POUR\ndirty water\ninto top','WAIT\nwater passes\nthrough layers','COLLECT\nfiltered water\nat bottom','BOIL\nbefore\ndrinking']

for i, (px, label) in enumerate(zip(pxs, labels)):
    mid = px + pw/2
    out(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="none" stroke="black" stroke-width="0.7"/>')
    out(f'<circle cx="{px+10}" cy="{py+10}" r="7" fill="black"/>')
    out(f'<text x="{px+10}" y="{py+14}" font-size="8" font-weight="bold" text-anchor="middle" fill="white">{i+1}</text>')

    if i == 0:  # POUR
        fig_sm_pouring(px+22, py+10, s=0.50)
        for dx in [mid+12, mid+19, mid+26]:
            drop(dx, py+14, 10)
        out(f'<polygon points="{mid+5:.1f},{py+30:.1f} {mid+33:.1f},{py+30:.1f} {mid+29:.1f},{py+46:.1f} {mid+9:.1f},{py+46:.1f}" fill="none" stroke="black" stroke-width="1.2"/>')

    elif i == 1:  # WAIT
        fig_sm_seated(px+18, py+10, s=0.50)
        out(f'<polygon points="{mid+4:.1f},{py+16:.1f} {mid+24:.1f},{py+16:.1f} {mid+20:.1f},{py+40:.1f} {mid+8:.1f},{py+40:.1f}" fill="none" stroke="black" stroke-width="1.2"/>')
        out(f'<line x1="{mid+14:.1f}" y1="{py+18:.1f}" x2="{mid+14:.1f}" y2="{py+38:.1f}" stroke="black" stroke-width="0.8" stroke-dasharray="2.5,2" marker-end="url(#arrsm)"/>')

    elif i == 2:  # COLLECT
        fig_sm_kneeling(px+22, py+10, s=0.50)
        bowl(mid+24, py+36, 22, 14, sw=1.4)
        for dx in [mid+18, mid+24, mid+30]:
            drop(dx, py+18, 10)

    elif i == 3:  # BOIL
        fig_sm_standing(px+18, py+12, s=0.50)
        # vessel
        out(f'<path d="M {mid+4:.1f} {py+36:.1f} L {mid+2:.1f} {py+52:.1f} L {mid+22:.1f} {py+52:.1f} L {mid+20:.1f} {py+36:.1f} Z" fill="none" stroke="black" stroke-width="1.3"/>')
        # steam bubbles
        for bxo, byo in [(-2,26),(3,23),(0,20)]:
            out(f'<circle cx="{mid+12+bxo:.1f}" cy="{py+byo:.1f}" r="2" fill="none" stroke="black" stroke-width="0.8"/>')
        # fire
        out(f'<path d="M {mid+4:.1f} {py+56:.1f} Q {mid+8:.1f} {py+48:.1f} {mid+12:.1f} {py+52:.1f} Q {mid+16:.1f} {py+48:.1f} {mid+20:.1f} {py+56:.1f}" fill="none" stroke="black" stroke-width="1.0"/>')
        out(f'<path d="M {mid+7:.1f} {py+56:.1f} Q {mid+10:.1f} {py+50:.1f} {mid+12:.1f} {py+52:.1f} Q {mid+14:.1f} {py+50:.1f} {mid+17:.1f} {py+56:.1f}" fill="black"/>')

    for li, ll in enumerate(label.split('\n')):
        lfs = 6.5 if li==0 else 5.5
        lfw = 'bold' if li==0 else 'normal'
        lst = 'normal' if li==0 else 'italic'
        out(f'<text x="{mid:.1f}" y="{py+ph+9+li*8:.1f}" font-size="{lfs}" font-weight="{lfw}" font-style="{lst}" text-anchor="middle">{ll}</text>')

    if i < 3:
        ax = px+pw+4
        out(f'<line x1="{ax}" y1="{py+ph/2:.1f}" x2="{ax+12}" y2="{py+ph/2:.1f}" stroke="black" stroke-width="1.2" marker-end="url(#arr)"/>')

out('<line x1="18" y1="514" x2="462" y2="514" stroke="black" stroke-width="0.75"/>')

# ══ E — MATERIAL SYMBOLS ══════════════════════════════════════════════════════
out('<text x="240" y="526" font-size="6.5" font-weight="bold" text-anchor="middle" letter-spacing="2">— MATERIAL SYMBOLS —</text>')
out('<polygon points="26,534 40,530 44,541 38,551 25,551" fill="black"/>')
out('<polygon points="46,531 62,528 65,540 59,550 46,548" fill="black"/>')
out('<text x="72" y="538" font-size="8" font-weight="bold">CHARCOAL</text>')
out('<text x="72" y="548" font-size="6.5" font-style="italic">angular · jagged · solid black · from burnt wood</text>')
for xi,yi in [(26,562),(33,559),(40,562),(47,559),(54,562),(61,559),(68,562)]:
    out(f'<circle cx="{xi}" cy="{yi}" r="2" fill="#111"/>')
out('<text x="78" y="562" font-size="8" font-weight="bold">SAND</text>')
out('<text x="78" y="572" font-size="6.5" font-style="italic">tiny uniform dots · fine-grained · riverbank or beach</text>')
for ex,ey,erx,ery in [(34,587,9,6),(58,586,8,5.5),(76,587,6.5,4.5)]:
    out(f'<ellipse cx="{ex}" cy="{ey}" rx="{erx}" ry="{ery}" fill="none" stroke="black" stroke-width="1.5"/>')
out('<text x="90" y="586" font-size="8" font-weight="bold">GRAVEL</text>')
out('<text x="90" y="596" font-size="6.5" font-style="italic">rounded ovals · smooth stones · from streambed</text>')

# ── FOOTER ───────────────────────────────────────────────────────────────────
out('<line x1="6" y1="610" x2="474" y2="610" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="620" font-size="6" text-anchor="middle" letter-spacing="0.8">PLATE 02 V4 · CC BY-SA 4.0 · REMEMBER FORWARD · rememberforward.org · DOI 10.5281/zenodo.19545922</text>')
out('<line x1="6" y1="626" x2="474" y2="626" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="646" font-size="7.5" font-weight="bold" font-style="italic" text-anchor="middle">THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.</text>')
out('<text x="240" y="661" font-size="7" font-style="italic" text-anchor="middle">BUY IT · BUILD IT · BURY IT · FOR SOMEONE YOU WILL NEVER MEET</text>')

out('</svg>')

os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f"Written: {OUTFILE}")

try:
    import os as _os; _os.startfile(OUTFILE)
except Exception:
    pass
