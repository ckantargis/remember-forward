"""
sign_lang_helpers.py
Shared SVG helpers for sign language plates (series 62–66).
Includes hand-shape drawing functions for manual alphabet grids.
"""

import math

# ── Standard SVG boilerplate ─────────────────────────────────────────────────

STYLE_SIGN = """<style>
  .T  { font: bold 12px/1 Georgia,serif; letter-spacing: 2px; }
  .S  { font: 7px/1 Georgia,serif; letter-spacing: 1.5px; }
  .H  { font: bold 6.5px/1 Georgia,serif; letter-spacing: 2.5px; }
  .L  { font: 7px/1.35 Georgia,serif; }
  .Ls { font: 6px/1.35 Georgia,serif; }
  .Lx { font: 5.5px/1.35 Georgia,serif; }
  .Lg { font: italic 8px/1.2 Georgia,serif; }
  .M  { font: 6px/1 Georgia,serif; letter-spacing: 0.5px; }
  .F  { font: italic 7px/1 Georgia,serif; }
  .Fb { font: bold 7.5px/1 Georgia,serif; }
</style>"""

def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def open_svg():
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 480 680" width="480" height="680">\n'
        + STYLE_SIGN + '\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="#111" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="#111" stroke-width="0.75"/>\n'
    )

def close_svg():
    return '</svg>\n'

def t(x, y, s, a='middle', c='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'

def hr(y, w=0.3):
    return f'<line x1="24" y1="{y}" x2="456" y2="{y}" stroke="#111" stroke-width="{w}"/>\n'

def sh(y, txt):
    return (
        f'<line x1="30" y1="{y}" x2="118" y2="{y}" stroke="#111" stroke-width="0.3"/>\n'
        f'<text x="240" y="{y+4}" text-anchor="middle" class="H">— {esc(txt)} —</text>\n'
        f'<line x1="362" y1="{y}" x2="450" y2="{y}" stroke="#111" stroke-width="0.3"/>\n'
    )

def bx(x, y, w, h, sw=0.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#555" stroke-width="{sw}"/>\n'

def footer(pid, series, lang_full, note, doi='10.5281/zenodo.19433177'):
    return (
        '<line x1="24" y1="607" x2="456" y2="607" stroke="#111" stroke-width="0.3"/>\n'
        f'<text x="240" y="616" text-anchor="middle" class="M">'
        f'{pid}  \u00b7  SERIES {series}  \u00b7  {lang_full}  \u00b7  {note}'
        f'</text>\n'
        '<line x1="24" y1="622" x2="456" y2="622" stroke="#111" stroke-width="0.3"/>\n'
        f'<text x="240" y="631" text-anchor="middle" class="M">'
        f'CC BY-SA 4.0  \u00b7  rememberforward.org  \u00b7  DOI {doi}'
        f'</text>\n'
        '<line x1="24" y1="638" x2="456" y2="638" stroke="#111" stroke-width="0.5"/>\n'
        '<text x="240" y="649" text-anchor="middle" class="Fb">'
        'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.'
        '</text>\n'
        '<text x="240" y="663" text-anchor="middle" class="F">'
        'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET'
        '</text>\n'
    )

# ── Hand-shape drawing ────────────────────────────────────────────────────────
# Each hand is drawn in a ~32×42 cell.
# cx, cy = center of palm area within the cell.
# Fingers extend UPWARD from palm top.
# Configuration: finger_h = [idx, mid, rng, pnk] heights 0–11px
#                thumb: 'side'|'across'|'up'|'between'|'over'|'none'

COL = '#111'
SW  = 0.75

def _rect(x, y, w, h, r=1.5):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="none" stroke="{COL}" stroke-width="{SW}"/>'

def _line(x1, y1, x2, y2):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COL}" stroke-width="{SW}"/>'

def _circ(x, y, r):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" stroke="{COL}" stroke-width="{SW}"/>'

def _arc(cx, cy, r, a_start, a_end):
    """Arc from a_start to a_end degrees (0=right, 90=down). Counterclockwise sweep."""
    sx = cx + r * math.cos(math.radians(a_start))
    sy = cy + r * math.sin(math.radians(a_start))
    ex = cx + r * math.cos(math.radians(a_end))
    ey = cy + r * math.sin(math.radians(a_end))
    diff = (a_end - a_start) % 360
    laf = 1 if diff > 180 else 0
    return f'<path d="M{sx:.1f},{sy:.1f} A{r},{r} 0 {laf},0 {ex:.1f},{ey:.1f}" fill="none" stroke="{COL}" stroke-width="{SW}"/>'


def hand_asl(cx, cy, ltr):
    """
    Draw simplified ASL handshape for letter `ltr` centered at (cx, cy_palm).
    Returns SVG string. Palm center at (cx, cy).
    """
    PW, PH = 15, 11   # palm width, height
    FW = 2.6          # finger width
    px = cx - PW / 2  # palm left
    py = cy - PH / 2  # palm top

    # Finger x-centers spaced across palm interior
    fxc = [px + 2 + i * (PW - 4) / 3 for i in range(4)]

    def finger(i, h):
        if h <= 0: return ''
        return _rect(fxc[i] - FW/2, py - h, FW, h)

    def palm():
        return _rect(px, py, PW, PH, r=2.5)

    def thumb_side(h=7, toward='left'):
        if toward == 'left':
            return _rect(px - h, cy - 2, h, 5)
        return _rect(px + PW, cy - 2, h, 5)

    def thumb_across():
        return _line(px + 1, cy + 2, px + PW - 1, cy + 2)

    def thumb_up(h=8):
        return _rect(px - 4, py - h, 4, h)

    parts = []

    if ltr == 'A':
        parts += [palm(), thumb_side(6)]
    elif ltr == 'B':
        parts += [palm(), finger(0,11), finger(1,11), finger(2,11), finger(3,11), thumb_across()]
    elif ltr == 'C':
        # Open C curve, facing right
        r = 9
        parts += [_arc(cx, cy - 4, r, -40, 220)]
    elif ltr == 'D':
        parts += [palm(), finger(0, 11), finger(1, 4), finger(2, 4), finger(3, 4), thumb_up(7)]
    elif ltr == 'E':
        parts += [palm(), finger(0, 2), finger(1, 2), finger(2, 2), finger(3, 2), thumb_across()]
    elif ltr == 'F':
        # Index+thumb form circle; middle/ring/pinky up
        parts += [palm(), finger(1, 10), finger(2, 10), finger(3, 10)]
        parts += [_circ(cx - PW/4, py - 3, 3)]
    elif ltr == 'G':
        # Hand rotated: index + thumb point right
        parts += [_rect(cx - 10, cy - 3, 10, 10, r=2)]    # palm (rotated)
        parts += [_rect(cx, cy, 9, 3, r=1)]                # index sideways
        parts += [_rect(cx - 10, cy - 7, 3.5, 5, r=1)]    # thumb up
    elif ltr == 'H':
        parts += [_rect(cx - 10, cy - 5, 10, 12, r=2)]
        parts += [_rect(cx, cy - 4, 9, 3, r=1)]
        parts += [_rect(cx, cy + 1, 9, 3, r=1)]
    elif ltr == 'I':
        parts += [palm(), finger(3, 11), thumb_side(6)]
    elif ltr == 'J':
        parts += [palm(), finger(3, 11), thumb_side(6)]
        # Motion dots (J trace)
        parts += [_circ(cx + 8, cy - 8, 1.2), _circ(cx + 11, cy - 4, 1.2)]
    elif ltr == 'K':
        parts += [palm(), finger(0, 11), finger(1, 9), thumb_up(7)]
    elif ltr == 'L':
        # L shape: index up, thumb out left at 90°
        parts += [palm(), finger(0, 11), thumb_side(8)]
    elif ltr == 'M':
        parts += [palm(), finger(0, 3), finger(1, 3), finger(2, 3), thumb_across()]
    elif ltr == 'N':
        parts += [palm(), finger(0, 3), finger(1, 3), thumb_across()]
    elif ltr == 'O':
        parts += [_circ(cx, cy - 4, 9)]
    elif ltr == 'P':
        # Like K but pointing down/forward
        parts += [_rect(cx - 5, cy - 4, 10, 11, r=2)]
        parts += [_rect(cx - 9, cy - 4, 8, 3, r=1)]
        parts += [_rect(cx - 9, cy + 1, 8, 3, r=1)]
        parts += [_rect(cx + 5, cy - 8, 3.5, 6, r=1)]
    elif ltr == 'Q':
        # Like G but pointing down
        parts += [_rect(cx - 5, cy - 8, 10, 10, r=2)]
        parts += [_rect(cx - 1, cy + 2, 3, 8, r=1)]
        parts += [_rect(cx + 5, cy - 4, 6, 3, r=1)]
    elif ltr == 'R':
        # Index + middle crossed
        parts += [palm()]
        parts += [_rect(fxc[0]-FW/2 - 1, py - 10, FW, 10)]
        parts += [_rect(fxc[1]-FW/2 + 1, py - 10, FW, 10)]
        parts += [_line(fxc[0]+FW/2, py - 6, fxc[1]-FW/2, py - 10)]
        parts += [thumb_side(6)]
    elif ltr == 'S':
        # Closed fist, thumb over fingers
        parts += [palm()]
        parts += [_line(px + 1, py + 2, px + PW - 1, py + 2)]  # thumb over
        parts += [thumb_across()]
    elif ltr == 'T':
        # Fist, thumb between index + middle
        parts += [palm()]
        parts += [finger(0, 4), finger(1, 4)]
        parts += [_rect(fxc[0] + FW/2, py - 6, fxc[1] - fxc[0] - FW, 5, r=1)]  # thumb tip
    elif ltr == 'U':
        parts += [palm(), finger(0, 11), finger(1, 11), thumb_side(6)]
    elif ltr == 'V':
        # Peace / V: index + middle spread
        parts += [palm()]
        parts += [_rect(fxc[0] - FW/2 - 1.5, py - 11, FW, 11)]
        parts += [_rect(fxc[1] - FW/2 + 1.5, py - 11, FW, 11)]
        parts += [thumb_side(6)]
    elif ltr == 'W':
        parts += [palm(), finger(0, 11), finger(1, 11), finger(2, 11), thumb_side(6)]
    elif ltr == 'X':
        # Index hooked
        parts += [palm(), _rect(fxc[0]-FW/2, py - 7, FW, 7)]
        parts += [_line(fxc[0]+FW/2, py - 7, fxc[0]+FW/2+3, py-10)]
        parts += [thumb_side(6)]
    elif ltr == 'Y':
        # Shaka: pinky + thumb
        parts += [palm(), finger(3, 11), thumb_side(8)]
    elif ltr == 'Z':
        # Index up (Z is a movement letter)
        parts += [palm(), finger(0, 11), thumb_side(6)]
        parts += [_circ(cx + 8, cy - 9, 1.2), _circ(cx + 10, cy - 6, 1.2)]

    # Letter label below palm
    parts.append(
        f'<text x="{cx}" y="{cy + PH/2 + 9:.1f}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="7.5" fill="{COL}">{ltr}</text>'
    )
    return '\n'.join(p for p in parts if p)


def draw_asl_alphabet(x0, y0, cell_w=33, cell_h=42, letters=None):
    """Draw the full ASL manual alphabet in a grid.
    x0, y0 = top-left of first cell.
    Returns (svg_string, next_y after last row).
    """
    if letters is None:
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    per_row = 13
    out = ''
    for i, ltr in enumerate(letters):
        col = i % per_row
        row = i // per_row
        cx = x0 + col * cell_w + cell_w // 2
        # palm center: leave room for fingers above
        cy = y0 + row * cell_h + cell_h - 14
        out += hand_asl(cx, cy, ltr) + '\n'
    rows = (len(letters) + per_row - 1) // per_row
    next_y = y0 + rows * cell_h + 4
    return out, next_y


def param_diagram(x, y, w, h, label, sub, items):
    """Draw a parameter box with label, sub-label, and bullet items."""
    out = bx(x, y, w, h)
    out += t(x + w//2, y + 11, label, 'middle', 'H')
    out += t(x + w//2, y + 21, sub,   'middle', 'Lx')
    out += hr(y + 24, 0.3).replace('x1="24"', f'x1="{x+4}"').replace('x2="456"', f'x2="{x+w-4}"')
    iy = y + 32
    for item in items:
        out += t(x + 8, iy, '\u2022 ' + item, 'start', 'Lx')
        iy += 8
    return out


def grammar_box(x, y, w, h, title, lines):
    out = bx(x, y, w, h)
    out += t(x + w//2, y + 10, title, 'middle', 'H')
    out += hr(y+13, 0.3).replace('x1="24"', f'x1="{x+3}"').replace('x2="456"', f'x2="{x+w-3}"')
    iy = y + 22
    for line in lines:
        out += t(x + 6, iy, line, 'start', 'Lx')
        iy += 8
    return out
