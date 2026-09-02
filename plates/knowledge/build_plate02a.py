#!/usr/bin/env python3
"""
build_plate02a.py — Plate 02A: Making Charcoal — Retort / Clay Vessel Method

Six panels (2 cols × 3 rows):
  ① Gather dry wood — cut short, sun = dry
  ② Fill pot with wood — pack tightly
  ③ Seal top with clay — leave one vent hole
  ④ Heat in external fire — 12–24 hours, smoke from vent = working
  ⑤ Watch smoke — thick smoke = cooking; smoke stops = done
  ⑥ Cool completely — then open and harvest charcoal
"""

import os, json, math

OUTDIR  = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'plate02a_charcoal_retort.svg')
FIGDATA = r'C:\Users\kanta\Documents\remember-forward\reference_images\figures\figure_paths.json'

with open(FIGDATA, encoding='utf-8') as f:
    FIGS = json.load(f)

lines = []
def out(s): lines.append(s)

# ── figure placement ──────────────────────────────────────────────────────────
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
    out(f'<g transform="translate({tx:.1f},{ty:.1f}) scale({s:.4f})'
        f' translate({-bb["x"]:.1f},{-bb["y"]:.1f})">')
    for d in f['paths']:
        out(f'  <path d="{d}" fill="black" fill-rule="nonzero"/>')
    out('</g>')

# ── drawing primitives ────────────────────────────────────────────────────────
def smoke_wisps(cx, y_base, count=3, height=28, sw=1.2):
    offsets = [-5, 0, 5, -3, 3][:count]
    for i, ox in enumerate(offsets):
        x0 = cx + ox
        ctrl_flip = 1 if i % 2 == 0 else -1
        y1 = y_base - height * 0.4
        y2 = y_base - height * 0.7
        y3 = y_base - height
        out(f'<path d="M {x0:.1f} {y_base:.1f} C {x0-5*ctrl_flip:.1f} {y1:.1f}'
            f' {x0+5*ctrl_flip:.1f} {y2:.1f} {x0-3*ctrl_flip:.1f} {y3:.1f}"'
            f' fill="none" stroke="black" stroke-width="{sw}"/>')

def log_shape(cx, cy, w=44, h=12):
    x, y = cx - w/2, cy - h/2
    out(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="4"'
        f' fill="none" stroke="black" stroke-width="1.3"/>')
    for gx in [cx - w*0.3, cx, cx + w*0.3]:
        out(f'<line x1="{gx:.1f}" y1="{y+2:.1f}" x2="{gx:.1f}" y2="{y+h-2:.1f}"'
            f' stroke="black" stroke-width="0.4"/>')
    out(f'<circle cx="{x+3:.1f}" cy="{cy:.1f}" r="2.5"'
        f' fill="none" stroke="black" stroke-width="0.8"/>')
    out(f'<circle cx="{x+w-3:.1f}" cy="{cy:.1f}" r="2.5"'
        f' fill="none" stroke="black" stroke-width="0.8"/>')

def sun_symbol(cx, cy, r=8):
    out(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}"'
        f' fill="none" stroke="black" stroke-width="1.3"/>')
    for i in range(8):
        a = i * math.pi / 4
        x1 = cx + (r+2) * math.cos(a)
        y1 = cy + (r+2) * math.sin(a)
        x2 = cx + (r+5) * math.cos(a)
        y2 = cy + (r+5) * math.sin(a)
        out(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"'
            f' stroke="black" stroke-width="1"/>')

# ── charcoal fill pattern ─────────────────────────────────────────────────────
import random as _r
_cc   = FIGS['charcoal_chunks']
_sc   = 10 / _cc['bbox']['h']
_rng  = _r.Random(77)
_tw, _th = 140, 70
_cpx, _cpy = _cc['bbox']['w']/2, _cc['bbox']['h']/2

def _chunk(tx, ty, sm, ang):
    s = round(_sc * sm, 4)
    return (f'<g transform="translate({tx:.1f},{ty:.1f}) rotate({ang:.0f})'
            f' scale({s}) translate({-_cpx:.2f},{-_cpy:.2f})">'
            f'<path d="{_cc["paths"][0]}" fill="black" fill-rule="nonzero"/></g>')

_chunks = (
    [_chunk(_rng.uniform(0,_tw), _rng.uniform(0,_th), _rng.uniform(1.5,2.2), _rng.uniform(0,360)) for _ in range(9)]
  + [_chunk(_rng.uniform(0,_tw), _rng.uniform(0,_th), _rng.uniform(0.9,1.4), _rng.uniform(0,360)) for _ in range(14)]
  + [_chunk(_rng.uniform(0,_tw), _rng.uniform(0,_th), _rng.uniform(0.35,0.75), _rng.uniform(0,360)) for _ in range(12)]
)

# ── SVG header + defs ─────────────────────────────────────────────────────────
out('<?xml version="1.0" encoding="UTF-8"?>')
out('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="120mm" height="170mm">')
out('<rect width="480" height="680" fill="white"/>')

out(f'''<defs>
  <pattern id="coal" x="0" y="0" width="{_tw}" height="{_th}" patternUnits="userSpaceOnUse">
    <rect width="{_tw}" height="{_th}" fill="white"/>
    {''.join(_chunks)}
  </pattern>
  <clipPath id="c-pot">
    <polygon points="382,498 432,498 422,571 392,571"/>
  </clipPath>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
  <marker id="arrsm" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="4" markerHeight="4" orient="auto">
    <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="black" stroke-width="1.5"/>
  </marker>
</defs>''')

out('<style>text { font-family: Georgia, serif; fill: black; }</style>')
out('<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="black" stroke-width="3"/>')
out('<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="black" stroke-width="0.75"/>')

# ── title ─────────────────────────────────────────────────────────────────────
out('<text x="240" y="32" font-size="11" font-weight="bold" text-anchor="middle"'
    ' letter-spacing="2">CHARCOAL &#8212; HOW TO MAKE IT</text>')
out('<line x1="18" y1="38" x2="462" y2="38" stroke="black" stroke-width="1"/>')
out('<text x="240" y="50" font-size="7" text-anchor="middle" letter-spacing="1.5">'
    'PLATE 02A &#183; SURVIVAL KNOWLEDGE &#183; RETORT / CLAY VESSEL METHOD</text>')
out('<line x1="18" y1="56" x2="462" y2="56" stroke="black" stroke-width="0.5"/>')
out('<text x="240" y="68" font-size="6.5" font-weight="bold" text-anchor="middle"'
    ' letter-spacing="2">&#8212; SEAL WOOD IN CLAY POT &#183; EXTERNAL FIRE &#183; OXYGEN RESTRICTED &#8212;</text>')
out('<text x="240" y="80" font-size="5.5" font-style="italic" text-anchor="middle">'
    'charcoal forms inside because oxygen cannot reach the wood</text>')

# ── layout constants ──────────────────────────────────────────────────────────
COL = [18, 244]   # panel left-x
ROW = [88, 265, 442]  # panel top-y
PW  = 218         # panel width
PH  = 144         # panel height

def mid(col): return COL[col] + PW // 2  # center-x of column

# grid lines (dashed)
out('<line x1="240" y1="88" x2="240" y2="586" stroke="black" stroke-width="0.4" stroke-dasharray="4,3"/>')
out('<line x1="18" y1="256" x2="462" y2="256" stroke="black" stroke-width="0.4" stroke-dasharray="4,3"/>')
out('<line x1="18" y1="433" x2="462" y2="433" stroke="black" stroke-width="0.4" stroke-dasharray="4,3"/>')

def box(col, row, sw=0.8):
    x, y = COL[col], ROW[row]
    out(f'<rect x="{x}" y="{y}" width="{PW}" height="{PH}"'
        f' fill="none" stroke="black" stroke-width="{sw}"/>')

def lbl(col, row, num, title, sub=''):
    mx = mid(col)
    by = ROW[row] + PH + 13
    out(f'<text x="{mx}" y="{by}" font-size="7" font-weight="bold"'
        f' text-anchor="middle">{num} {title}</text>')
    if sub:
        out(f'<text x="{mx}" y="{by+10}" font-size="5.5" font-style="italic"'
            f' text-anchor="middle">{sub}</text>')

# inter-column sequence arrows on divider
for ry in [ROW[0]+PH//2, ROW[1]+PH//2, ROW[2]+PH//2]:
    out(f'<line x1="232" y1="{ry}" x2="248" y2="{ry}"'
        f' stroke="black" stroke-width="1.8" marker-end="url(#arr)"/>')

# ══ PANEL ① — GATHER DRY WOOD ════════════════════════════════════════════════
box(0, 0)

# sun = dry indicator (top-right corner)
sun_symbol(cx=COL[0]+PW-22, cy=ROW[0]+20, r=8)
out(f'<text x="{COL[0]+PW-22}" y="{ROW[0]+36}" font-size="5.5"'
    f' text-anchor="middle">DRY</text>')

# 3 wood logs stacked (left-centre area)
log_shape(cx=COL[0]+80, cy=ROW[0]+100, w=52, h=13)
log_shape(cx=COL[0]+85, cy=ROW[0]+117, w=52, h=13)
log_shape(cx=COL[0]+78, cy=ROW[0]+134, w=52, h=13)

# clay pot icon for size reference (right side, smaller)
fig('clay_pot', cx=COL[0]+178, cy=ROW[0]+PH-6, target_h=68, anchor='bottom')

# standing figure (far left)
fig('standing', cx=COL[0]+30, cy=ROW[0]+PH-6, target_h=85, anchor='bottom')

lbl(0, 0, '&#9312;', 'GATHER DRY WOOD', 'cut short — must fit inside pot')

# ══ PANEL ② — FILL POT WITH WOOD ═════════════════════════════════════════════
box(1, 0)

# large pot centered
pot2_cx = mid(1)
pot2_cy = ROW[0] + PH - 8
fig('clay_pot', cx=pot2_cx, cy=pot2_cy, target_h=90, anchor='bottom')

# approximate pot opening y (top 12% of pot height from top of figure)
pot2_top = pot2_cy - 90
open2_y  = pot2_top + 12

# wood sticks visible in/above pot mouth
for ox in [-14, -6, 2, 10]:
    out(f'<line x1="{pot2_cx+ox}" y1="{open2_y-8:.0f}"'
        f' x2="{pot2_cx+ox}" y2="{open2_y+14:.0f}"'
        f' stroke="black" stroke-width="2.5" stroke-linecap="round"/>')

# down arrow + label above pot
out(f'<line x1="{pot2_cx}" y1="{ROW[0]+16}" x2="{pot2_cx}" y2="{open2_y-12:.0f}"'
    f' stroke="black" stroke-width="1.5" marker-end="url(#arr)"/>')
out(f'<text x="{pot2_cx}" y="{ROW[0]+14}" font-size="5.5"'
    f' font-weight="bold" text-anchor="middle">WOOD ONLY &#8595;</text>')

lbl(1, 0, '&#9313;', 'FILL POT WITH WOOD', 'pack tightly · wood only — no soil, no wet leaves')

# ══ PANEL ③ — SEAL TOP / VENT HOLE ═══════════════════════════════════════════
box(0, 1)

# pot (slightly right of centre to leave room for standing figure)
pot3_cx = COL[0] + 140
pot3_cy = ROW[1] + PH - 8
fig('clay_pot', cx=pot3_cx, cy=pot3_cy, target_h=80, anchor='bottom')

pot3_top = pot3_cy - 80
open3_y  = pot3_top + 10  # approx opening y
seal_w   = 42

# clay seal band at top of pot (filled rect with white hatch = clay texture)
out(f'<rect x="{pot3_cx-seal_w//2}" y="{open3_y:.0f}" width="{seal_w}" height="10"'
    f' fill="black" rx="2"/>')
for hx in range(int(pot3_cx-seal_w//2)+4, int(pot3_cx+seal_w//2)-2, 6):
    out(f'<line x1="{hx}" y1="{open3_y:.0f}" x2="{hx}" y2="{open3_y+10:.0f}"'
        f' stroke="white" stroke-width="0.9"/>')

# vent hole — white circle in the seal
vent_x = pot3_cx
vent_y = open3_y + 5
out(f'<circle cx="{vent_x:.0f}" cy="{vent_y:.0f}" r="3.5"'
    f' fill="white" stroke="black" stroke-width="0.8"/>')

# arrow + callout pointing to vent hole
ax1, ay1 = pot3_cx - 32, ROW[1] + 18
out(f'<line x1="{ax1}" y1="{ay1}" x2="{vent_x-4:.0f}" y2="{vent_y:.0f}"'
    f' stroke="black" stroke-width="0.9" marker-end="url(#arrsm)"/>')
out(f'<text x="{ax1-2}" y="{ay1-4}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">VENT</text>')
out(f'<text x="{ax1-2}" y="{ay1+4}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">HOLE</text>')

# standing figure applying clay (left side)
fig('standing', cx=COL[0]+30, cy=pot3_cy, target_h=75, anchor='bottom')

lbl(0, 1, '&#9314;', 'SEAL TOP WITH CLAY', 'leave ONE small vent hole — do not seal it')

# ══ PANEL ④ — HEAT IN FIRE ═══════════════════════════════════════════════════
box(1, 1)

pot4_cx = mid(1)
pot4_cy = ROW[1] + PH - 22
fig('clay_pot', cx=pot4_cx, cy=pot4_cy, target_h=72, anchor='bottom')

pot4_top  = pot4_cy - 72
pot4_base = pot4_cy

# fire icons across base of pot
for fx in [pot4_cx-24, pot4_cx-12, pot4_cx, pot4_cx+12, pot4_cx+24]:
    fig('fire', cx=fx, cy=pot4_base, target_h=20, anchor='bottom')

# ground stones under fire
for gx, gr in [(pot4_cx-28,5), (pot4_cx-16,4), (pot4_cx-4,5),
               (pot4_cx+8,4), (pot4_cx+20,5), (pot4_cx+30,4)]:
    out(f'<ellipse cx="{gx}" cy="{pot4_base+2}" rx="{gr}" ry="3" fill="black"/>')

# smoke wisps from vent
vent4_y = pot4_top + 10
smoke_wisps(cx=pot4_cx, y_base=vent4_y, count=4, height=28, sw=1.5)

# time arc: sun crossing arc in upper-right of panel
arc_cx = COL[1] + PW - 30
arc_cy = ROW[1] + 60
arc_r  = 20
out(f'<path d="M {arc_cx-arc_r:.1f} {arc_cy:.1f}'
    f' A {arc_r} {arc_r} 0 0 1 {arc_cx+arc_r:.1f} {arc_cy:.1f}"'
    f' fill="none" stroke="black" stroke-width="0.8" stroke-dasharray="2,2"/>')
sun_symbol(cx=arc_cx, cy=arc_cy - arc_r, r=6)
out(f'<text x="{arc_cx}" y="{arc_cy+12}" font-size="6" font-weight="bold"'
    f' text-anchor="middle">12&#8211;24h</text>')

lbl(1, 1, '&#9315;', 'HEAT IN EXTERNAL FIRE', 'keep fire burning · smoke from vent = still working')

# ══ PANEL ⑤ — SMOKE STOPS = DONE ════════════════════════════════════════════
box(0, 2)

# split panel at mid-x of col 0
split_x = COL[0] + PW // 2  # x=127

# dashed divider in panel
out(f'<line x1="{split_x}" y1="{ROW[2]+8}" x2="{split_x}" y2="{ROW[2]+PH-8}"'
    f' stroke="black" stroke-width="0.5" stroke-dasharray="3,2"/>')

# LEFT: thick smoke = still cooking
lp_cx  = COL[0] + 55
lp_cy  = ROW[2] + PH - 12
fig('clay_pot', cx=lp_cx, cy=lp_cy, target_h=55, anchor='bottom')
lp_top = lp_cy - 55
smoke_wisps(cx=lp_cx, y_base=lp_top+8, count=5, height=35, sw=2.2)
out(f'<text x="{lp_cx}" y="{ROW[2]+15}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">THICK</text>')
out(f'<text x="{lp_cx}" y="{ROW[2]+23}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">SMOKE</text>')
out(f'<text x="{lp_cx}" y="{ROW[2]+31}" font-size="5" font-style="italic"'
    f' text-anchor="middle">= still cooking</text>')

# arrow from left to right
out(f'<line x1="{split_x-8}" y1="{ROW[2]+PH//2}"'
    f' x2="{split_x+8}" y2="{ROW[2]+PH//2}"'
    f' stroke="black" stroke-width="2" marker-end="url(#arr)"/>')

# RIGHT: no smoke = done
rp_cx = split_x + 55
rp_cy = lp_cy
fig('clay_pot', cx=rp_cx, cy=rp_cy, target_h=55, anchor='bottom')
rp_top = rp_cy - 55
# single very thin wisp (almost nothing)
smoke_wisps(cx=rp_cx, y_base=rp_top+8, count=1, height=10, sw=0.6)
out(f'<text x="{rp_cx}" y="{ROW[2]+15}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">NO</text>')
out(f'<text x="{rp_cx}" y="{ROW[2]+23}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">SMOKE</text>')
out(f'<text x="{rp_cx}" y="{ROW[2]+31}" font-size="5" font-style="italic"'
    f' text-anchor="middle">= done</text>')

lbl(0, 2, '&#9316;', 'SMOKE STOPS = DONE', 'seal the vent hole · do not open yet · let cool sealed')

# ══ PANEL ⑥ — COOL COMPLETELY THEN OPEN ════════════════════════════════════
box(1, 2)

split6_x = COL[1] + PW // 2  # x=353

# dashed divider
out(f'<line x1="{split6_x}" y1="{ROW[2]+8}" x2="{split6_x}" y2="{ROW[2]+PH-8}"'
    f' stroke="black" stroke-width="0.5" stroke-dasharray="3,2"/>')

# LEFT: pot off fire, cooling
cool_cx  = COL[1] + 55
cool_cy  = ROW[2] + PH - 12
fig('clay_pot', cx=cool_cx, cy=cool_cy, target_h=55, anchor='bottom')

# crossed-out fire (X over small fire icon above pot)
fx_cx  = cool_cx
fx_cy  = cool_cy - 55 - 10
fig('fire', cx=fx_cx, cy=fx_cy, target_h=12, anchor='bottom')
out(f'<line x1="{fx_cx-7}" y1="{fx_cy-12}" x2="{fx_cx+7}" y2="{fx_cy}"'
    f' stroke="black" stroke-width="2"/>')
out(f'<line x1="{fx_cx+7}" y1="{fx_cy-12}" x2="{fx_cx-7}" y2="{fx_cy}"'
    f' stroke="black" stroke-width="2"/>')

# heat radiating lines from pot sides
pot_mid_y = cool_cy - 28
for deg in [150, 160, 170, 200, 210, 220]:
    rad = deg * math.pi / 180
    x1  = cool_cx + 28 * math.cos(rad)
    y1  = pot_mid_y + 28 * math.sin(rad)
    x2  = cool_cx + 38 * math.cos(rad)
    y2  = pot_mid_y + 38 * math.sin(rad)
    out(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"'
        f' stroke="black" stroke-width="0.9"/>')

out(f'<text x="{cool_cx}" y="{ROW[2]+15}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">WAIT</text>')
out(f'<text x="{cool_cx}" y="{ROW[2]+23}" font-size="5.5" text-anchor="middle">'
    f'until cool</text>')

# arrow
out(f'<line x1="{split6_x-8}" y1="{ROW[2]+PH//2}"'
    f' x2="{split6_x+8}" y2="{ROW[2]+PH//2}"'
    f' stroke="black" stroke-width="2" marker-end="url(#arr)"/>')

# RIGHT: open pot showing charcoal cross-section
hrv_cx = split6_x + 55
# trapezoid cross-section of open pot
trap_ty = ROW[2] + 42
trap_by = ROW[2] + PH - 12
trap_thw = 26   # half-width at top
trap_bhw = 16   # half-width at bottom

# fill interior with coal pattern (clipped to trapezoid)
out(f'<defs><clipPath id="c-harv">'
    f'<polygon points="{hrv_cx-trap_thw},{trap_ty} {hrv_cx+trap_thw},{trap_ty}'
    f' {hrv_cx+trap_bhw},{trap_by} {hrv_cx-trap_bhw},{trap_by}"/>'
    f'</clipPath></defs>')
out(f'<rect x="{hrv_cx-trap_thw}" y="{trap_ty}" width="{trap_thw*2}" height="{trap_by-trap_ty}"'
    f' fill="url(#coal)" clip-path="url(#c-harv)"/>')
# trapezoid outline
out(f'<polygon points="{hrv_cx-trap_thw},{trap_ty} {hrv_cx+trap_thw},{trap_ty}'
    f' {hrv_cx+trap_bhw},{trap_by} {hrv_cx-trap_bhw},{trap_by}"'
    f' fill="none" stroke="black" stroke-width="2.2"/>')
# lid open: two halves tilted away
lid_y = trap_ty - 3
out(f'<line x1="{hrv_cx-trap_thw-6}" y1="{lid_y+3}" x2="{hrv_cx-trap_thw+12}" y2="{lid_y}"'
    f' stroke="black" stroke-width="2.5" stroke-linecap="round"/>')
out(f'<line x1="{hrv_cx+trap_thw+6}" y1="{lid_y+3}" x2="{hrv_cx+trap_thw-12}" y2="{lid_y}"'
    f' stroke="black" stroke-width="2.5" stroke-linecap="round"/>')

out(f'<text x="{hrv_cx}" y="{ROW[2]+15}" font-size="5.5" font-weight="bold"'
    f' text-anchor="middle">OPEN</text>')
out(f'<text x="{hrv_cx}" y="{ROW[2]+23}" font-size="5.5" text-anchor="middle">'
    f'black chunks</text>')
out(f'<text x="{hrv_cx}" y="{ROW[2]+31}" font-size="5" font-style="italic"'
    f' text-anchor="middle">= charcoal &#10003;</text>')

lbl(1, 2, '&#9317;', 'COOL FULLY · OPEN · HARVEST', 'jet black · lightweight · metallic clink = good charcoal')

# ── footer ────────────────────────────────────────────────────────────────────
out('<line x1="18" y1="602" x2="462" y2="602" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="612" font-size="6" text-anchor="middle" letter-spacing="0.8">'
    'PLATE 02A &#183; CC BY-SA 4.0 &#183; REMEMBER FORWARD &#183; rememberforward.org'
    ' &#183; DOI 10.5281/zenodo.19545922</text>')
out('<line x1="6" y1="622" x2="474" y2="622" stroke="black" stroke-width="0.75"/>')
out('<text x="240" y="636" font-size="7.5" font-weight="bold" font-style="italic"'
    ' text-anchor="middle">'
    'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.'
    '</text>')
out('<text x="240" y="650" font-size="7" font-style="italic" text-anchor="middle">'
    'BUY IT &#183; BUILD IT &#183; BURY IT &#183; FOR SOMEONE YOU WILL NEVER MEET</text>')

out('</svg>')

os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {OUTFILE}')

try:
    import os as _os; _os.startfile(OUTFILE)
except Exception:
    pass
