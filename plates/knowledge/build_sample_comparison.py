#!/usr/bin/env python3
"""
build_sample_comparison.py — Sand & gravel final designs for review.
Sand: mound outline + 3-size stipple (FGDC standard in icon form)
Gravel: 3 organic bezier stone shapes with white highlights
"""

import os
OUTDIR  = r'C:\Users\kanta\Documents\remember-forward\plates\knowledge'
OUTFILE = os.path.join(OUTDIR, 'sample_sand_gravel.svg')

lines = []
def out(s): lines.append(s)

# ─── Designs (s = scale factor) ───────────────────────────────────────────────

def sand_icon(cx, cy, s=1):
    """Mound outline + 3-size stipple — FGDC sand standard as standalone icon."""
    sw = 0.8 * s
    out(f'<path d="M {cx-14*s} {cy} Q {cx-8*s} {cy-13*s} {cx} {cy-14*s}'
        f' Q {cx+8*s} {cy-13*s} {cx+14*s} {cy} Z"'
        f' fill="none" stroke="black" stroke-width="{sw}"/>')
    for ox, oy in [(-7,-3),(0,-4),(6,-5)]:
        out(f'<circle cx="{cx+ox*s}" cy="{cy+oy*s}" r="{1.6*s}" fill="black"/>')
    for ox, oy in [(-10,-2),(11,-2),(-4,-7),(4,-8),(-1,-11)]:
        out(f'<circle cx="{cx+ox*s}" cy="{cy+oy*s}" r="{1.2*s}" fill="black"/>')
    for ox, oy in [(-12,-1),(12,-1),(8,-4),(-6,-7),(1,-12)]:
        out(f'<circle cx="{cx+ox*s}" cy="{cy+oy*s}" r="{0.8*s}" fill="black"/>')

def gravel_icon(cx, cy, s=1):
    """3 organic stone shapes with white highlights — natural water-worn stones."""
    # Stone A: large, elongated horizontal
    out(f'<path d="M {cx-15*s} {cy-4*s} Q {cx-14*s} {cy-10*s} {cx-7*s} {cy-10*s}'
        f' Q {cx-1*s} {cy-10*s} {cx+1*s} {cy-5*s} Q {cx} {cy+1*s} {cx-5*s} {cy}'
        f' Q {cx-13*s} {cy+1*s} {cx-15*s} {cy-4*s} Z" fill="black"/>')
    out(f'<circle cx="{cx-12*s}" cy="{cy-8*s}" r="{1.1*s}" fill="white"/>')
    # Stone B: medium, rounder
    out(f'<path d="M {cx-1*s} {cy-4*s} Q {cx} {cy-9*s} {cx+5*s} {cy-8*s}'
        f' Q {cx+9*s} {cy-7*s} {cx+10*s} {cy-2*s} Q {cx+9*s} {cy+2*s} {cx+4*s} {cy+2*s}'
        f' Q {cx-1*s} {cy+1*s} {cx-1*s} {cy-4*s} Z" fill="black"/>')
    out(f'<circle cx="{cx+3*s}" cy="{cy-7*s}" r="{0.85*s}" fill="white"/>')
    # Stone C: small, compact, nestled above
    out(f'<path d="M {cx-5*s} {cy-9*s} Q {cx-5*s} {cy-14*s} {cx-1*s} {cy-13*s}'
        f' Q {cx+2*s} {cy-12*s} {cx+2*s} {cy-8*s} Q {cx+1*s} {cy-6*s} {cx-4*s} {cy-7*s}'
        f' Q {cx-6*s} {cy-8*s} {cx-5*s} {cy-9*s} Z" fill="black"/>')
    out(f'<circle cx="{cx-3*s}" cy="{cy-12*s}" r="{0.6*s}" fill="white"/>')

# ─── SVG ─────────────────────────────────────────────────────────────────────

out('<?xml version="1.0" encoding="UTF-8"?>')
out('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 330" width="120mm" height="82.5mm">')
out('<rect width="480" height="330" fill="white"/>')
out('<style>text { font-family: Georgia, serif; fill: black; }</style>')
out('<rect x="2" y="2" width="476" height="326" fill="none" stroke="black" stroke-width="1"/>')

out('<text x="240" y="17" font-size="9" font-weight="bold" text-anchor="middle" letter-spacing="1.5">MATERIAL SYMBOLS — FINAL DESIGNS</text>')
out('<text x="240" y="27" font-size="6.5" text-anchor="middle" fill="#555">FGDC/USGS standard · sand = stipple · gravel = circles</text>')
out('<line x1="8" y1="31" x2="472" y2="31" stroke="black" stroke-width="0.8"/>')

out('<rect x="8" y="32" width="232" height="14" fill="#f0f0f0"/>')
out('<rect x="242" y="32" width="230" height="14" fill="#f0f0f0"/>')
out('<text x="124" y="42" font-size="8" font-weight="bold" text-anchor="middle">SAND</text>')
out('<text x="357" y="42" font-size="8" font-weight="bold" text-anchor="middle">GRAVEL</text>')
out('<line x1="240" y1="31" x2="240" y2="328" stroke="black" stroke-width="0.5" stroke-dasharray="4,3"/>')

out('<text x="124" y="56" font-size="6.5" text-anchor="middle" fill="#444">mound outline + 3-size stipple (large / medium / small)</text>')
out('<text x="357" y="56" font-size="6.5" text-anchor="middle" fill="#444">3 organic bezier stones · white highlight = 3D roundness</text>')
out('<line x1="8" y1="61" x2="472" y2="61" stroke="#ddd" stroke-width="0.5"/>')

# ── 3× enlarged ───────────────────────────────────────────────────────────────
out('<text x="14" y="71" font-size="6" fill="#888">3× scale</text>')

sand_icon(124, 190, s=3)
gravel_icon(357, 190, s=3)

out('<line x1="8" y1="236" x2="472" y2="236" stroke="#ddd" stroke-width="0.5"/>')

# ── 2× scale ─────────────────────────────────────────────────────────────────
out('<text x="14" y="244" font-size="6" fill="#888">2× scale</text>')

sand_icon(124, 278, s=2)
gravel_icon(357, 278, s=2)

out('<line x1="8" y1="294" x2="472" y2="294" stroke="black" stroke-width="0.7"/>')

# ── 1× plate scale in context ─────────────────────────────────────────────────
out('<text x="14" y="302" font-size="6.5" fill="#555" font-weight="bold">actual plate scale — Band E layout</text>')
out('<line x1="8" y1="305" x2="472" y2="305" stroke="#ddd" stroke-width="0.4"/>')

sand_icon(36, 322, s=1)
out('<text x="54" y="317" font-size="7.5" font-weight="bold">&#9313; SAND</text>')
out('<text x="54" y="326" font-size="6" font-style="italic">fine grains &#183; middle layer</text>')

gravel_icon(270, 322, s=1)
out('<text x="288" y="317" font-size="7.5" font-weight="bold">&#9314; GRAVEL</text>')
out('<text x="288" y="326" font-size="6" font-style="italic">rounded stones &#183; bottom layer</text>')

out('</svg>')

os.makedirs(OUTDIR, exist_ok=True)
with open(OUTFILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {OUTFILE}')
try:
    import os as _os; _os.startfile(OUTFILE)
except Exception:
    pass
