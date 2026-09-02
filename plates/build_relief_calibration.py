"""
build_relief_calibration.py — the tile to press before pressing anything else.

The ceramic relief plan has one load-bearing unknown: the smallest mark that
survives mould release, 12% shrinkage, and a cone 6 firing. Every downstream
number depends on it. At a 2.0 mm minimum cap height the 13 knowledge plates
become 22 tiles; at 4.0 mm they become 77. Nobody can settle that by reasoning
about it. Press this, fire it, and read it.

    python build_relief_calibration.py

Writes knowledge/plate_relief_calibration.svg, sized as a MASTER: the physical
width/height are scaled up by 1/(1-shrink) so the fired tile lands at
120 x 170 mm. The coordinate system is unchanged from every other plate
(viewBox 480 x 680, 1 unit = 0.25 mm of FIRED tile), so every number printed on
the tile is a FIRED dimension.

Six ladders, each labelled on the tile in its own units, so the fired object is
self-documenting and still readable in a photograph two years from now:

    A  text        1.5 / 2.0 / 2.5 / 3.0 / 4.0 mm cap height
    B  line width  0.4 / 0.6 / 0.8 / 1.0 / 1.5 / 2.0 mm
    C  line gap    0.5 / 0.75 / 1.0 / 1.5 mm
    D  dot         0.5 / 0.75 / 1.0 / 1.5 / 2.0 mm diameter
    E  hatching    0.75 / 1.0 / 1.5 / 2.0 mm spacing — what replaces a pattern fill
    F  real work   a vessel, a seed and a flame at 100 / 70 / 50%

To turn this into a mould: open in Inkscape, Select All, Path > Object to Path
(converts the text), then Path > Stroke to Path (converts the lines), save as
plain SVG, extrude. Print or cut THREE masters at 0.4, 0.8 and 1.2 mm relief
depth — depth cannot be tested from one tile, and it is the second unknown.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plate_profiles import PROFILES, MM_PER_UNIT  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "knowledge", "plate_relief_calibration.svg")

W, H = 480, 680                      # units; 120 x 170 mm fired
P = PROFILES["ceramic_relief"]
SHRINK = P["shrink_total"]
SCALE = 1.0 / (1.0 - SHRINK)         # 1.136

CAP_RATIO = 0.70                     # Georgia cap height as a fraction of em
MARGIN = 6.0                         # mm

TEXT_MM = [1.5, 2.0, 2.5, 3.0, 4.0]
LINE_MM = [0.4, 0.6, 0.8, 1.0, 1.5]
GAP_MM = [0.5, 0.75, 1.0, 1.5]
DOT_MM = [0.5, 0.75, 1.0, 1.5, 2.0]
HATCH_MM = [0.75, 1.0, 1.5, 2.0]

# Long enough to judge word shapes, short enough that 4 mm caps still fit the
# tile width. Georgia averages ~0.55 em advance.
SPECIMEN = "REMEMBER FORWARD 1234"
SPECIMEN_SHORT = "RF 1234 abc"


def u(mm_):
    """Millimetres of FIRED tile -> SVG units."""
    return mm_ / MM_PER_UNIT


def font_for_cap(mm_):
    """Font-size in units yielding a given cap height in fired mm."""
    return u(mm_) / CAP_RATIO


class Tile:
    """A vertical cursor. Rows claim the space they need and no more."""

    def __init__(self):
        self.o = []
        self.y = MARGIN                      # mm

    def text(self, x_mm, y_mm, cap_mm, s, anchor="start", bold=False):
        w = ' font-weight="bold"' if bold else ""
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        self.o.append(
            f'  <text x="{u(x_mm):.1f}" y="{u(y_mm):.1f}" '
            f'font-size="{font_for_cap(cap_mm):.2f}"{w}{a} fill="#000" stroke="none">{s}</text>'
        )

    def line(self, x1, y1, x2, y2, w_mm):
        self.o.append(
            f'  <line x1="{u(x1):.1f}" y1="{u(y1):.1f}" x2="{u(x2):.1f}" '
            f'y2="{u(y2):.1f}" stroke-width="{u(w_mm):.2f}"/>'
        )

    def rule(self, y_mm):
        self.line(MARGIN, y_mm, 120 - MARGIN, y_mm, 0.8)

    def head(self, letter, title, note, tx=6.0):
        self.y += 5.0
        self.text(MARGIN, self.y, 3.0, letter, bold=True)
        self.text(MARGIN + tx, self.y, 2.6, title)
        self.text(120 - MARGIN, self.y, 1.8, note, anchor="end")
        self.y += 1.5

    def svg(self):
        return "\n".join(self.o)


def build():
    t = Tile()

    # ---- header ----------------------------------------------------------
    t.y = 10.0
    t.text(MARGIN, t.y, 5.0, "RELIEF CALIBRATION", bold=True)
    t.y += 5.5
    t.text(MARGIN, t.y, 2.2,
           f"Fired tile 120 x 170 mm. Every dimension shown is FIRED, "
           f"after {SHRINK * 100:.0f}% shrinkage.")
    t.y += 4.0
    t.text(MARGIN, t.y, 2.2,
           "Record on the back: clay body · cone · relief depth · mould material · date.")
    t.y += 2.5
    t.rule(t.y)

    # ---- A. text ---------------------------------------------------------
    t.head("A", "TEXT — cap height", "smallest you can still read = min_font")
    for mm_ in TEXT_MM:
        t.y += max(mm_ * 1.25, 3.0)
        s = SPECIMEN if mm_ <= 3.0 else SPECIMEN_SHORT
        t.text(MARGIN, t.y, mm_, s)
        t.text(120 - MARGIN, t.y, 1.8, f"{mm_} mm", anchor="end")
    t.y += 2.0

    # ---- B. line width ---------------------------------------------------
    t.head("B", "LINE WIDTH", "does it hold, or close up?")
    for mm_ in LINE_MM:
        t.y += 3.3
        t.line(MARGIN, t.y, 82, t.y, mm_)
        t.text(86, t.y + 0.8, 1.8, f"{mm_} mm")
    t.y += 2.0

    # ---- C. gap ----------------------------------------------------------
    t.head("C", "GAP BETWEEN LINES", "the gap fails before the line does")
    for mm_ in GAP_MM:
        t.y += 4.0
        t.line(MARGIN, t.y, 82, t.y, 0.8)
        t.line(MARGIN, t.y + mm_, 82, t.y + mm_, 0.8)
        t.text(86, t.y + 1.4, 1.8, f"{mm_} mm")
        t.y += mm_
    t.y += 2.0

    # ---- D + E side by side ---------------------------------------------
    t.head("D/E", "DOTS and HATCH SPACING", "smallest discrete mark · texture", tx=10.0)
    t.y += 6.5
    row_y = t.y
    x = MARGIN + 4
    for mm_ in DOT_MM:
        t.o.append(f'  <circle cx="{u(x):.1f}" cy="{u(row_y):.1f}" r="{u(mm_) / 2:.2f}" '
                   f'fill="#000" stroke="none"/>')
        t.text(x, row_y + 5.0, 1.8, f"{mm_}", anchor="middle")
        x += 9.5
    x = 66
    box = 11.0
    for mm_ in HATCH_MM:
        t.o.append(f'  <rect x="{u(x):.1f}" y="{u(row_y - box / 2):.1f}" '
                   f'width="{u(box):.1f}" height="{u(box):.1f}" stroke-width="{u(0.8):.2f}"/>')
        n = int(box / mm_)
        for i in range(1, n):
            xx = x + i * mm_
            t.line(xx, row_y - box / 2, xx, row_y + box / 2, 0.4)
        t.text(x + box / 2, row_y + 5.0 + box / 2 - 1.0, 1.8, f"{mm_}", anchor="middle")
        x += box + 1.5
    t.y = row_y + box / 2 + 6.0

    # ---- F. real geometry ------------------------------------------------
    t.head("F", "REAL GEOMETRY", "vessel · seed · flame, at 100 / 70 / 50%")
    t.y += 3.0
    base = t.y
    x = MARGIN + 2
    for frac in (1.0, 0.70, 0.50):
        s = frac
        t.o.append(f'  <g transform="translate({u(x):.1f},{u(base):.1f}) scale({s:.2f})" '
                   f'stroke-width="{u(0.8) / s:.2f}">')
        # vessel in section, water line, three settling layers
        t.o.append(f'    <path d="M {u(0):.1f} {u(0):.1f} L {u(1.6):.1f} {u(17):.1f} '
                   f'L {u(13.4):.1f} {u(17):.1f} L {u(15):.1f} {u(0):.1f}"/>')
        t.o.append(f'    <line x1="{u(0.9):.1f}" y1="{u(5):.1f}" x2="{u(14.1):.1f}" '
                   f'y2="{u(5):.1f}"/>')
        for dy in (9.5, 12.0, 14.5):
            t.o.append(f'    <line x1="{u(1.3):.1f}" y1="{u(dy):.1f}" x2="{u(13.7):.1f}" '
                       f'y2="{u(dy):.1f}"/>')
        # seed with radicle
        t.o.append(f'    <ellipse cx="{u(24):.1f}" cy="{u(7):.1f}" rx="{u(3.4):.1f}" '
                   f'ry="{u(4.8):.1f}"/>')
        t.o.append(f'    <path d="M {u(24):.1f} {u(11.8):.1f} q {u(1.4):.1f} {u(3.4):.1f} '
                   f'{u(4.2):.1f} {u(4.8):.1f}"/>')
        # flame: asymmetric outer silhouette with an inner tongue, because a
        # symmetric teardrop reads as a leaf and we already have a seed
        t.o.append(f'    <path d="M {u(33.2):.1f} {u(17):.1f} '
                   f'C {u(29.6):.1f} {u(12.6):.1f} {u(33.6):.1f} {u(9.4):.1f} '
                   f'{u(34.4):.1f} {u(4.6):.1f} '
                   f'C {u(36.4):.1f} {u(7.4):.1f} {u(36.0):.1f} {u(8.6):.1f} '
                   f'{u(38.0):.1f} {u(7.0):.1f} '
                   f'C {u(38.6):.1f} {u(11.4):.1f} {u(41.2):.1f} {u(12.2):.1f} '
                   f'{u(38.6):.1f} {u(17):.1f} Z"/>')
        t.o.append(f'    <path d="M {u(35.0):.1f} {u(17):.1f} '
                   f'C {u(33.8):.1f} {u(14.4):.1f} {u(35.6):.1f} {u(12.8):.1f} '
                   f'{u(36.2):.1f} {u(10.6):.1f} '
                   f'C {u(37.4):.1f} {u(13.2):.1f} {u(37.6):.1f} {u(14.6):.1f} '
                   f'{u(36.8):.1f} {u(17):.1f} Z"/>')
        t.o.append(f'    <line x1="{u(31.6):.1f}" y1="{u(17):.1f}" '
                   f'x2="{u(40.4):.1f}" y2="{u(17):.1f}"/>')
        t.o.append('  </g>')
        t.text(x + 20 * frac, base + 21.0, 1.8, f"{int(frac * 100)}%", anchor="middle")
        x += 40 * frac + 4
    t.y = base + 17 + 4

    # ---- footer ----------------------------------------------------------
    t.rule(170 - 11)
    t.text(MARGIN, 170 - 6, 2.2,
           "REMEMBER FORWARD · the smallest mark you can still read is the whole answer")

    body = t.svg()
    header = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<!-- RELIEF CALIBRATION MASTER — Remember Forward.\n'
        f'     viewBox {W}x{H}; 1 unit = {MM_PER_UNIT} mm of FIRED tile.\n'
        f'     Physical size below is the GREENWARE master: scaled {SCALE:.3f}x for\n'
        f'     {SHRINK * 100:.0f}% total shrinkage (drying + cone 6), so the fired tile lands\n'
        f'     at 120 x 170 mm. Do not rescale on export.\n'
        f'     Inkscape: Object to Path, then Stroke to Path, before extruding. -->\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{W * MM_PER_UNIT * SCALE:.1f}mm" height="{H * MM_PER_UNIT * SCALE:.1f}mm" '
        f'viewBox="0 0 {W} {H}">\n'
        '<rect width="480" height="680" fill="white"/>\n'
        '<g fill="none" stroke="#000" stroke-linecap="butt">\n'
    )
    return header + body + "\n</g>\n</svg>\n", t.y


if __name__ == "__main__":
    svg, used = build()
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"wrote {OUT}")
    print(f"  master {W * MM_PER_UNIT * SCALE:.1f} x {H * MM_PER_UNIT * SCALE:.1f} mm "
          f"-> fires to {W * MM_PER_UNIT:.0f} x {H * MM_PER_UNIT:.0f} mm "
          f"({SHRINK * 100:.0f}% shrinkage)")
    print(f"  content ends at {used:.1f} mm of {H * MM_PER_UNIT:.0f} mm "
          f"({'FITS' if used < 158 else 'OVERFLOW'})")
    print(f"  text {TEXT_MM} · line {LINE_MM} · gap {GAP_MM} · dot {DOT_MM} · hatch {HATCH_MM}")
    print("  print three masters at 0.4 / 0.8 / 1.2 mm relief depth")
