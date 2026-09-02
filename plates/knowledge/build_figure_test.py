"""
build_figure_test.py
ISOTYPE-style silhouette figure test plate.
Solid black segments, clear horizontal torso / vertical legs contrast.
"""
import os

W, H = 480, 680

# ── Core drawing helpers ──────────────────────────────────────────────────────

def seg(x1, y1, x2, y2, sw, cap="round"):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="black" stroke-width="{sw}" stroke-linecap="{cap}" fill="none"/>')

def arc(d, sw, cap="round"):
    return (f'<path d="{d}" fill="none" stroke="black" '
            f'stroke-width="{sw}" stroke-linecap="{cap}" stroke-linejoin="round"/>')

def circ(cx, cy, r, fill="black"):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="none"/>'

def ellip(cx, cy, rx, ry, fill="black", stroke="none", sw=1.5):
    if stroke == "none":
        return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"/>'
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def txt(x, y, s, anchor="middle", size=7.5, weight="normal", style="normal", spacing=0):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="Georgia,serif" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}" '
            f'fill="black"{sp}>{s}</text>')

def hr(y, x0=18, x1=462, sw=0.5):
    return f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="black" stroke-width="{sw}"/>'

def wavy(y, x0=28, x1=228, sw=1.2):
    pts, x, up = [], x0, True
    pts.append(f'M {x} {y}')
    while x < x1:
        nx = min(x + 15, x1)
        cy2 = y - 3 if up else y + 3
        pts.append(f'Q {x+7} {cy2} {nx} {y}')
        x = nx; up = not up
    return f'<path d="{" ".join(pts)}" fill="none" stroke="black" stroke-width="{sw}"/>'

# ── FIGURE: bent-forward collecting posture ───────────────────────────────────
#
# Design principles (from Opus research):
#   - Solid black silhouette, ISOTYPE tradition
#   - Clear horizontal torso vs vertical legs = immediately reads as "bent forward"
#   - Large distinct head (r ≈ 10% of total height), clear neck gap
#   - Profile, facing right
#
def figure_collecting(ox, ground_y, sc=1.0):
    """
    ox        : horizontal centre of figure footprint
    ground_y  : y of ground / water surface
    sc        : scale factor (1.0 = ~65 px tall)
    Returns list of SVG element strings + (hand_x, hand_y) + (foot_x, foot_y)
    """
    g = ground_y
    s = sc

    # ── Joint positions (absolute SVG coords) ────────────────────────────────
    # Torso: nearly horizontal bar going forward (right)
    hip_x  = ox;            hip_y  = g - 36*s   # left/back end of torso
    sho_x  = ox + 33*s;     sho_y  = g - 39*s   # right/front end (shoulder)

    # Head: circle above shoulder, with clear neck gap
    nk_x   = sho_x + 4*s;  nk_y   = sho_y - 9*s   # neck top
    hd_x   = nk_x  + 2*s;  hd_y   = nk_y  - 11*s  # head centre

    # Legs: hanging nearly vertically from hip end
    kn1_x  = hip_x - 3*s;  kn1_y  = g - 19*s   # near knee
    an1_x  = hip_x - 1*s;  an1_y  = g           # near ankle (ground)
    ft1_x  = hip_x - 11*s  # near foot tip (extends backward)

    kn2_x  = hip_x + 5*s;  kn2_y  = g - 18*s   # far knee
    an2_x  = hip_x + 7*s;  an2_y  = g           # far ankle (ground)
    ft2_x  = hip_x + 15*s  # far foot tip (extends forward)

    # Arms: reaching forward-down from shoulder
    el1_x  = sho_x + 16*s; el1_y  = sho_y + 17*s  # near elbow
    ha1_x  = sho_x + 22*s; ha1_y  = g - 8*s        # near hand (near water)

    el2_x  = sho_x + 11*s; el2_y  = sho_y + 18*s  # far elbow
    ha2_x  = sho_x + 16*s; ha2_y  = g - 6*s        # far hand

    # ── Stroke widths ────────────────────────────────────────────────────────
    sw_torso = 16*s
    sw_uleg  = 10*s
    sw_lleg  =  8*s
    sw_foot  =  6*s
    sw_uarm  =  7*s
    sw_larm  =  5*s
    sw_neck  =  6*s
    r_head   = 10*s

    els = []

    # Far leg (draw behind near leg)
    els.append(seg(hip_x+3*s, hip_y, kn2_x, kn2_y, sw_uleg*0.9))
    els.append(seg(kn2_x, kn2_y, an2_x, an2_y, sw_lleg*0.9))
    els.append(seg(an2_x, an2_y, ft2_x, an2_y+2*s, sw_foot*0.85, "butt"))

    # Torso (thick horizontal bar — the key shape that reads "bent over")
    els.append(seg(hip_x, hip_y, sho_x, sho_y, sw_torso))

    # Near leg (on top)
    els.append(seg(hip_x, hip_y, kn1_x, kn1_y, sw_uleg))
    els.append(seg(kn1_x, kn1_y, an1_x, an1_y, sw_lleg))
    els.append(seg(an1_x, an1_y, ft1_x, an1_y+2*s, sw_foot, "butt"))

    # Neck (clear gap between shoulder mass and head)
    els.append(seg(sho_x, sho_y, nk_x, nk_y, sw_neck))

    # Head (large circle, must not touch torso stroke)
    els.append(circ(hd_x, hd_y, r_head))

    # Far arm
    els.append(seg(sho_x-3*s, sho_y, el2_x, el2_y, sw_uarm*0.9))
    els.append(seg(el2_x, el2_y, ha2_x, ha2_y, sw_larm*0.9))

    # Near arm
    els.append(seg(sho_x, sho_y, el1_x, el1_y, sw_uarm))
    els.append(seg(el1_x, el1_y, ha1_x, ha1_y, sw_larm))

    return els, (ha1_x, ha1_y), (an1_x, an1_y)


# ── Symbol vocabulary helpers ─────────────────────────────────────────────────

def sym_fire(cx, cy, h=20):
    """Flame silhouette: solid filled path."""
    b = cy + h//2
    return (f'<path d="M {cx} {b} Q {cx-7} {b-8} {cx-4} {b-14} '
            f'Q {cx-6} {b-8} {cx} {b-18} '
            f'Q {cx+3} {b-10} {cx+7} {b-16} '
            f'Q {cx+5} {b-6} {cx+9} {b-12} '
            f'Q {cx+8} {b-4} {cx+5} {b} Z" fill="black"/>')

def sym_steam(cx, cy):
    """Three wavy steam lines rising."""
    els = []
    for i, dx in enumerate([-6, 0, 6]):
        x = cx + dx
        els.append(f'<path d="M {x} {cy} Q {x+3} {cy-5} {x} {cy-10} '
                   f'Q {x-3} {cy-15} {x} {cy-20}" '
                   f'fill="none" stroke="black" stroke-width="1.2"/>')
    return "\n".join(els)

def sym_bubble(cx, cy, r=3):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="black" stroke-width="1.2"/>'


# ── Build SVG ─────────────────────────────────────────────────────────────────

lines = []
lines.append('<?xml version="1.0" encoding="UTF-8"?>')
lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="120mm" height="170mm">')
lines.append(f'<rect width="{W}" height="{H}" fill="white"/>')
lines.append('<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="black" stroke-width="3"/>')
lines.append('<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="black" stroke-width="0.75"/>')

# Header
lines.append(txt(240, 33, "PICTOGRAM FIGURE TEST — WATER FILTER SEQUENCE", size=11, weight="bold", spacing=2))
lines.append(hr(39, sw=1))
lines.append(txt(240, 51, "SILHOUETTE SYSTEM · ISOTYPE-STYLE · DESIGN REVIEW", size=7, spacing=1))
lines.append(hr(56, sw=0.5))

# ── A: Symbol vocabulary key ──────────────────────────────────────────────────
lines.append(txt(240, 69, "— SYMBOL VOCABULARY —", size=8, weight="bold", spacing=2))
lines.append(hr(74, sw=0.3))

ky = 100  # key row y (baseline of symbols)

# Clean water
lines.append(wavy(ky-4, x0=22, x1=82, sw=1.5))
lines.append(wavy(ky+2, x0=22, x1=82, sw=1.5))
lines.append(txt(52, ky+16, "CLEAN WATER", size=6.5))

# Dirty water
lines.append(wavy(ky-4, x0=98, x1=158, sw=1.5))
lines.append(wavy(ky+2, x0=98, x1=158, sw=1.5))
for ddx, ddy in [(104,ky-6),(114,ky-2),(124,ky-7),(135,ky-1),(146,ky-5),(107,ky+2),(130,ky+4)]:
    lines.append(circ(ddx, ddy, 1.8))
lines.append(txt(128, ky+16, "DIRTY WATER", size=6.5))

# Fire
lines.append(sym_fire(192, ky-2, h=22))
lines.append(txt(192, ky+16, "FIRE / HEAT", size=6.5))

# Charcoal lumps (solid irregular shapes)
for clx, cly, crx, cry in [(220,ky,10,6),(234,ky-4,8,5.5),(246,ky+1,9,6),(258,ky-3,7,5)]:
    lines.append(ellip(clx, cly, crx, cry))
lines.append(txt(239, ky+16, "CHARCOAL", size=6.5))

# Sand dots
for sdx, sdy in [(278,ky-3),(286,ky+1),(294,ky-4),(302,ky+2),(310,ky-2),(318,ky+1),(279,ky+5),(295,ky+4),(311,ky+5)]:
    lines.append(circ(sdx, sdy, 2.2))
lines.append(txt(298, ky+16, "SAND", size=6.5))

# Gravel (outline ovals)
for glx, gly, grx, gry in [(332,ky,10,6.5),(348,ky-2,9,6),(362,ky+1,8,5.5),(374,ky-1,7,5)]:
    lines.append(ellip(glx, gly, grx, gry, fill="none", stroke="black", sw=1.8))
lines.append(txt(353, ky+16, "GRAVEL", size=6.5))

# Boiling pot (cross-section + bubbles + steam)
bpx = 418; bpy = ky + 4
# pot walls
lines.append(f'<path d="M {bpx-18} {bpy} L {bpx-20} {bpy+14} Q {bpx} {bpy+22} {bpx+20} {bpy+14} L {bpx+18} {bpy}" '
             f'fill="none" stroke="black" stroke-width="1.8"/>')
lines.append(seg(bpx-18, bpy, bpx+18, bpy, 1.8))  # rim
# bubbles
for bbx, bby in [(bpx-8,bpy+10),(bpx,bpy+8),(bpx+8,bpy+10)]:
    lines.append(sym_bubble(bbx, bby, 2.8))
# steam
lines.append(sym_steam(bpx, bpy-2))
lines.append(txt(bpx, ky+16, "BOILING", size=6.5))

lines.append(hr(126, sw=0.4))

# Cross-section convention explainer
lines.append(txt(240, 138, "CROSS-SECTION CONVENTION  (teaches viewer that cutaway = shows inside)", size=6.5, style="italic"))
cx_y = 148
# solid box
lines.append(f'<rect x="30" y="{cx_y}" width="44" height="30" rx="2" fill="none" stroke="black" stroke-width="1.5"/>')
lines.append(txt(52, cx_y+20, "SOLID", size=6))
lines.append(txt(52, cx_y+30, "(opaque)", size=5.5, style="italic"))
lines.append(txt(105, cx_y+18, "=", size=14))
# cutaway box (open top, dashed)
lines.append(f'<line x1="122" y1="{cx_y+30}" x2="166" y2="{cx_y+30}" stroke="black" stroke-width="1.5"/>') # bottom
lines.append(f'<line x1="122" y1="{cx_y}" x2="122" y2="{cx_y+30}" stroke="black" stroke-width="1.5"/>')  # left
lines.append(f'<line x1="166" y1="{cx_y}" x2="166" y2="{cx_y+30}" stroke="black" stroke-width="1.5"/>')  # right
lines.append(f'<line x1="122" y1="{cx_y}" x2="166" y2="{cx_y}" stroke="black" stroke-width="1" stroke-dasharray="4,3"/>') # open top
lines.append(txt(144, cx_y+20, "CUTAWAY", size=6))
lines.append(txt(144, cx_y+30, "(shows inside)", size=5.5, style="italic"))

# Sequence numbering
lines.append(txt(310, cx_y+6, "SEQUENCE NUMBERING:", size=6.5, weight="bold", anchor="start"))
for n, tally in [(1,"I"),(2,"II"),(3,"III"),(4,"IIII"),(5,"IIIII"),(6,"IIIII·I")]:
    col = 310 + ((n-1) % 3) * 55
    row = cx_y + 16 + ((n-1) // 3) * 14
    lines.append(txt(col, row, f"{n}  ·  {tally}", size=6.5, anchor="start"))

lines.append(hr(190, sw=0.75))

# ── B: Figure test — large scale ─────────────────────────────────────────────
lines.append(txt(240, 203, "— FIGURE POSTURE: COLLECTING (PROFILE, FACING RIGHT) —", size=8, weight="bold", spacing=2))
lines.append(txt(240, 215, "horizontal torso + vertical legs = bent-forward posture reads instantly", size=6.5, style="italic"))

ground_A = 370
fig_els, (ha_x, ha_y), (ft_x, ft_y) = figure_collecting(110, ground_A, sc=1.0)
for el in fig_els:
    lines.append(el)

# Ground / water
lines.append(wavy(ground_A, x0=30, x1=220))
# Rocks at streambed
for rx, ry, rrx, rry in [(75,ground_A+9,9,6),(92,ground_A+10,7.5,5.5),(108,ground_A+9,9,5.5),
                          (124,ground_A+10,8,5),(140,ground_A+9,9,6),(158,ground_A+10,7,4.5)]:
    lines.append(ellip(rx, ry, rrx, rry))

# Bucket near hand
bkt_x = int(ha_x) + 6; bkt_y = int(ha_y) - 2
lines.append(f'<polygon points="{bkt_x},{bkt_y} {bkt_x-2},{bkt_y+16} {bkt_x+18},{bkt_y+16} {bkt_x+16},{bkt_y}" '
             f'fill="white" stroke="black" stroke-width="1.8"/>')
lines.append(ellip(bkt_x+6, bkt_y+11, 4.5, 3))
lines.append(ellip(bkt_x+12, bkt_y+10, 4, 3))

# Annotation callouts (right side)
ann_x = 270
lines.append(txt(ann_x, 240, "← head: large, distinct", size=6.5, style="italic", anchor="start"))
lines.append(txt(ann_x, 280, "← torso: horizontal bar", size=6.5, style="italic", anchor="start"))
lines.append(txt(ann_x, 320, "← arms reach to water", size=6.5, style="italic", anchor="start"))
lines.append(txt(ann_x, 355, "← legs: vertical, clear", size=6.5, style="italic", anchor="start"))
lines.append(txt(ann_x, 375, "← bucket at ground level", size=6.5, style="italic", anchor="start"))

lines.append(hr(392, sw=0.5))

# ── C: Same figure at 3 actual panel scales ───────────────────────────────────
lines.append(txt(240, 404, "— SAME FIGURE AT ACTUAL PANEL SCALE —", size=8, weight="bold", spacing=2))

ground_C = 468
panel_centers = [75, 210, 345]
for i, fx in enumerate(panel_centers):
    fig_els2, _, _ = figure_collecting(fx, ground_C, sc=0.85)
    for el in fig_els2:
        lines.append(el)
    lines.append(wavy(ground_C, x0=fx-48, x1=fx+65, sw=1.0))
    for rx, ry, rrx, rry in [(fx+8,ground_C+8,8,5),(fx+22,ground_C+9,6.5,4.5),
                              (fx+36,ground_C+8,7.5,5),(fx+48,ground_C+9,6,4)]:
        lines.append(ellip(rx, ry, rrx, rry))
    # panel number
    lines.append(txt(fx - 40, ground_C + 22, f"{i+1}  ·  {'I'*(i+1)}", size=6.5, weight="bold", anchor="start"))

lines.append(hr(495, sw=0.4))

# ── D: Stroke weight reference ────────────────────────────────────────────────
lines.append(txt(240, 507, "— STROKE WEIGHT REFERENCE —", size=8, weight="bold", spacing=2))
sw_demo_y = 555
for i, (lbl, sw_val) in enumerate([("torso  16", 16), ("leg  10", 10), ("arm  7", 7), ("lower  5", 5), ("min  1.5", 1.5)]):
    lx = 52 + i * 82
    lines.append(seg(lx, sw_demo_y-26, lx, sw_demo_y+26, sw_val))
    lines.append(txt(lx, sw_demo_y+38, lbl, size=6.2))

lines.append(hr(600, sw=0.5))

# Footer
lines.append(hr(616, sw=0.75))
lines.append(txt(240, 626, "CC BY-SA 4.0 · DESIGN REVIEW · REMEMBER FORWARD · rememberforward.org", size=6.5, spacing=0.8))
lines.append(hr(630, sw=0.75))
lines.append(txt(240, 649, "THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.", size=11, weight="bold", style="italic"))
lines.append(txt(240, 664, "BUY IT · BUILD IT · BURY IT · FOR SOMEONE YOU WILL NEVER MEET", size=8.5))
lines.append('</svg>')

svg = "\n".join(lines)
out = r"C:\Users\kanta\Documents\remember-forward\plates\knowledge\figure_test.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Written: {out}")
print(f"SVG open/close tags: {svg.count('<svg')}/{svg.count('</svg>')}")
os.startfile(out)
