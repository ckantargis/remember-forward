"""
Plate 09 — Audio Playback Guide
Needle construction, groove anatomy, tone arm, minimal playback build.
"""
import os, math

OUT = os.path.dirname(os.path.abspath(__file__))

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return (
        '<svg viewBox="0 0 480 680" xmlns="http://www.w3.org/2000/svg">\n'
        '<defs><style>\n'
        '  text{font-family:Georgia,serif;fill:#000;}\n'
        '  .T{font-size:13px;font-weight:bold;letter-spacing:2px;}\n'
        '  .S{font-size:7.5px;letter-spacing:1.5px;}\n'
        '  .H{font-size:7px;font-weight:bold;letter-spacing:2.5px;}\n'
        '  .L{font-size:7px;}\n'
        '  .Ls{font-size:6px;}\n'
        '  .Lx{font-size:5.5px;}\n'
        '  .M{font-size:6px;letter-spacing:1px;}\n'
        '  .F{font-size:7px;font-style:italic;}\n'
        '  .Fb{font-size:7px;font-weight:bold;}\n'
        '</style></defs>\n'
        '<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="#000" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="#000" stroke-width="0.75"/>\n'
    )

def close_svg():
    return (
        '<line x1="18" y1="615" x2="462" y2="615" stroke="#000" stroke-width="0.5"/>\n'
        '<text x="240" y="624" text-anchor="middle" class="M">REMEMBER FORWARD · THE PATIENT MESSAGE · CC BY-SA 4.0 · rememberforward.org</text>\n'
        '<line x1="18" y1="630" x2="462" y2="630" stroke="#000" stroke-width="1"/>\n'
        '<text x="240" y="648" text-anchor="middle" class="Fb">THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.</text>\n'
        '<text x="240" y="663" text-anchor="middle" class="F">UNDERSTAND IT · BUILD WITH IT · LEAVE MORE CAPSULES FOR OTHERS</text>\n'
        '</svg>\n'
    )

def t(x, y, s, a='middle', c='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'

def hr(y, x1=22, x2=458, sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#000" stroke-width="{sw}"/>\n'

def sh(y, txt):
    return hr(y-4) + t(240, y+5, f'— · —  {txt}  — · —', 'middle', 'H') + hr(y+10)

def line(x1, y1, x2, y2, sw=0.8):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="{sw}"/>\n'

def rect(x, y, w, h, sw=0.9, fill='none'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>\n'

def circle(cx, cy, r, sw=0.8, fill='none'):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>\n'

def poly(pts, sw=1.0, fill='none'):
    ps = ' '.join(f'{x},{y}' for x,y in pts)
    return f'<polyline points="{ps}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>\n'

def polygon(pts, sw=0.8, fill='#000'):
    ps = ' '.join(f'{x},{y}' for x,y in pts)
    return f'<polygon points="{ps}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>\n'

def arrow_r(x1, y1, x2, y2, sw=0.7):
    out = line(x1, y1, x2, y2, sw)
    out += polygon([(x2-4, y2-2), (x2, y2), (x2-4, y2+2)], fill='#000', sw=0.5)
    return out

def build():
    out = open_svg()

    # ── TITLE ────────────────────────────────────────────────────────────
    out += t(240, 34, 'PLATE 9  ·  AUDIO PLAYBACK', 'middle', 'T')
    out += hr(40, sw=0.75)
    out += t(240, 51, 'how a groove stores sound  ·  how a needle reads it  ·  how to build a player with found materials', 'middle', 'S')
    out += hr(57, sw=0.5)

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 1 — THE GROOVE  (y 58–145)
    # ══════════════════════════════════════════════════════════════════════
    out += sh(60, 'THE GROOVE')

    # Left: cross-section diagram of groove
    # Ground surface
    out += line(22, 100, 175, 100, 1.0)
    # V-groove walls — 45° each side, tip at y=125, x=98
    out += line(65, 100, 98, 125, 1.0)   # left wall
    out += line(131, 100, 98, 125, 1.0)  # right wall
    # Needle tip circle
    out += circle(98, 122, 4, sw=0.8, fill='none')
    # Labels
    out += t(98, 95, 'GROOVE CROSS-SECTION', 'middle', 'Lx')
    out += t(30, 105, 'wall', 'middle', 'Lx')
    out += t(165, 105, 'wall', 'middle', 'Lx')
    out += t(98, 136, 'stylus tip', 'middle', 'Lx')
    out += t(98, 143, '(radius ~0.5–2.5 mil)', 'middle', 'Lx')

    # Right: groove plan view — sinusoidal wiggle
    out += t(320, 77, 'GROOVE FROM ABOVE', 'middle', 'Lx')
    # Center line
    out += line(200, 110, 450, 110, 0.3)
    # Sine wave groove path
    pts = []
    for i in range(251):
        x = 200 + i
        y = 110 + 10 * math.sin(i * 2 * math.pi / 50)
        pts.append((x, y))
    out += poly(pts, sw=1.0)
    out += t(200, 125, 'silence', 'start', 'Lx')
    out += t(320, 125, 'louder / higher freq', 'middle', 'Lx')

    # Speed table
    out += hr(130, sw=0.3)
    speeds = [('78 RPM', 'shellac · pre-1950 · 3–5 min/side · wide groove'),
              ('33⅓ RPM', 'vinyl LP · from 1948 · 20–30 min/side'),
              ('45 RPM', 'vinyl single · from 1949 · 4–6 min/side')]
    y = 139
    for spd, note in speeds:
        out += t(50, y, spd, 'start', 'Ls')
        out += t(115, y, note, 'start', 'Lx')
        y += 8

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 2 — THE STYLUS  (y 158–255)
    # ══════════════════════════════════════════════════════════════════════
    out += sh(158, 'THE STYLUS  (NEEDLE)')

    # Needle anatomy diagram — left side
    # Shank
    out += poly([(60, 170), (60, 205)], sw=1.5)
    # Cantilever (angled arm, 15° from vertical)
    out += line(60, 205, 75, 230, 1.2)
    # Tip (small filled circle)
    out += circle(75, 233, 2.5, sw=0.6, fill='#000')
    # Labels
    out += t(45, 176, 'shank', 'end', 'Lx')
    out += t(35, 210, 'cantilever', 'end', 'Lx')
    out += t(85, 235, 'tip', 'start', 'Lx')
    out += t(60, 245, 'NEEDLE ANATOMY', 'middle', 'Lx')

    # Tip geometry detail — center
    # Two profile outlines: conical and elliptical
    out += t(175, 173, 'CONICAL TIP', 'middle', 'Lx')
    out += poly([(155, 175), (175, 210), (195, 175)], sw=0.8)
    out += circle(175, 210, 3, sw=0.7, fill='none')
    out += t(175, 220, 'side wear', 'middle', 'Lx')
    out += t(175, 226, '(wider contact)', 'middle', 'Lx')

    out += t(265, 173, 'ELLIPTICAL TIP', 'middle', 'Lx')
    out += poly([(245, 175), (255, 215), (265, 175)], sw=0.8)
    out += poly([(265, 175), (275, 215), (285, 175)], sw=0.8)
    out += circle(265, 215, 2, sw=0.7, fill='none')
    out += t(265, 224, 'better HF tracking', 'middle', 'Lx')

    # Materials table — right
    out += t(390, 173, 'MATERIALS', 'middle', 'Lx')
    mats = [('steel pin', 'works · wears fast'),
            ('cactus spine', 'traditional 78 RPM use'),
            ('thorn (hardwood)', 'file to point, ~2 per side'),
            ('bone splinter', 'file and polish tip'),
            ('sapphire/diamond', 'commercial · 500+ hrs')]
    y = 182
    for mat, note in mats:
        out += t(340, y, mat, 'start', 'Ls')
        out += t(340, y+7, f'  {note}', 'start', 'Lx')
        y += 17

    out += hr(253, sw=0.3)
    out += t(240, 259, 'tip must be smooth · sharp point · radius matched to groove width · clean before each side', 'middle', 'Lx')

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 3 — TONE ARM  (y 262–330)
    # ══════════════════════════════════════════════════════════════════════
    out += sh(262, 'THE TONE ARM')

    # Simple diagram: pivot point, arm, cartridge head
    px, py = 60, 300   # pivot
    ex, ey = 200, 295  # headshell end
    out += circle(px, py, 4, sw=1.0, fill='none')
    out += line(px, py, ex, ey, 1.5)
    out += rect(ex-4, ey-6, 12, 12, sw=0.8)  # cartridge
    out += circle(ex+2, ey+7, 2.5, sw=0.6, fill='#000')  # stylus
    # Counterweight (other end)
    cx2, cy2 = 38, 303
    out += rect(cx2-8, cy2-5, 16, 10, sw=0.8, fill='none')
    out += t(30, 315, 'counterweight', 'middle', 'Lx')
    out += t(px, 312, 'pivot', 'middle', 'Lx')
    out += t(ex+4, 314, 'cartridge', 'start', 'Lx')
    # Downforce arrow
    out += arrow_r(ex+2, ey+12, ex+2, ey+20, sw=0.6)
    out += t(ex+14, ey+20, '1–3 g', 'start', 'Lx')

    # Tone arm notes
    notes = [
        'pivot must swing freely in horizontal AND vertical plane',
        'tracking force: 1–3 g for vinyl · 3–7 g for shellac 78s',
        'too heavy → groove damage  ·  too light → skipping',
        'anti-skate force balances inward groove drag (can skip for basic use)',
        'arm length: longer = less tracking error across record radius',
    ]
    y = 273
    for n in notes:
        out += t(230, y, n, 'start', 'Lx')
        y += 9

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 4 — SIGNAL PATH  (y 333–385)
    # ══════════════════════════════════════════════════════════════════════
    out += sh(333, 'SIGNAL PATH')

    # Flow boxes
    boxes = ['GROOVE\nWIGGLE', 'STYLUS\nVIBRATES', 'CANTILEVER\nBENDS', 'MAGNET\nMOVES', 'COIL\nVOLTAGE', 'AMP', 'SPEAKER\nCONE']
    bx = 22
    for i, label in enumerate(boxes):
        lines = label.split('\n')
        bw = 52 if i < 6 else 52
        bh = 22
        by = 348
        out += rect(bx, by, bw, bh, sw=0.8)
        if len(lines) == 1:
            out += t(bx + bw/2, by + 14, lines[0], 'middle', 'Lx')
        else:
            out += t(bx + bw/2, by + 9, lines[0], 'middle', 'Lx')
            out += t(bx + bw/2, by + 18, lines[1], 'middle', 'Lx')
        if i < len(boxes) - 1:
            ax = bx + bw
            out += arrow_r(ax, by+11, ax+5, by+11, sw=0.6)
        bx += bw + 5

    out += hr(374, sw=0.3)
    out += t(240, 381, 'moving magnet (MM): magnet on cantilever · coil fixed · output ~5mV', 'middle', 'Lx')
    out += t(240, 388, 'moving coil (MC): coil on cantilever · magnet fixed · output ~0.2mV · needs more amplification', 'middle', 'Lx')

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 5 — MINIMAL BUILD  (y 392–500)
    # ══════════════════════════════════════════════════════════════════════
    out += sh(392, 'MINIMAL BUILD  —  NO ELECTRICITY REQUIRED')

    # Diagram: pin through paper cone riding on record
    # Record circle (partial arc)
    pts_arc = []
    cx_r, cy_r = 120, 470
    for deg in range(150, 390, 2):
        r = 70
        x = cx_r + r * math.cos(math.radians(deg))
        y = cy_r + r * math.sin(math.radians(deg))
        pts_arc.append((x, y))
    out += poly(pts_arc, sw=0.8)
    # Groove rings
    for rr in [50, 55, 60, 65]:
        pts_g = []
        for deg in range(150, 390, 3):
            x = cx_r + rr * math.cos(math.radians(deg))
            y = cy_r + rr * math.sin(math.radians(deg))
            pts_g.append((x, y))
        out += poly(pts_g, sw=0.3)
    # Label record
    out += t(cx_r, cy_r+75, 'RECORD', 'middle', 'Lx')
    out += t(cx_r, cy_r+83, '(spinning)', 'middle', 'Lx')

    # Paper cone — triangle shape above-right of needle contact
    needle_x = cx_r + 65 * math.cos(math.radians(210))
    needle_y = cy_r + 65 * math.sin(math.radians(210))
    cone_tip_x = needle_x
    cone_tip_y = needle_y
    cone_base_x1 = needle_x - 35
    cone_base_y1 = needle_y - 55
    cone_base_x2 = needle_x + 35
    cone_base_y2 = needle_y - 60
    out += poly([(cone_base_x1, cone_base_y1), (cone_tip_x, cone_tip_y), (cone_base_x2, cone_base_y2)], sw=0.9)
    out += line(cone_base_x1, cone_base_y1, cone_base_x2, cone_base_y2, 0.9)
    # Pin through cone tip
    out += circle(cone_tip_x, cone_tip_y, 2, sw=0.7, fill='#000')
    out += t(cone_tip_x - 15, cone_tip_y + 12, 'pin/thorn', 'middle', 'Lx')
    out += t(cone_tip_x, cone_base_y1 - 8, 'paper/card', 'middle', 'Lx')
    out += t(cone_tip_x, cone_base_y1 - 1, 'cone (horn)', 'middle', 'Lx')

    # Instructions — right side
    steps = [
        '1. Cut stiff paper into a cone, ~15 cm wide opening.',
        '2. Push a steel pin or thorn through the tip.',
        '3. Build a spindle: rotate record at correct RPM.',
        '   78 RPM ≈ 1.3 rev/sec  ·  33⅓ RPM ≈ 0.56 rev/sec',
        '4. Lower pin gently into outer groove, ~1-2 g pressure.',
        '5. Cone amplifies stylus vibration acoustically.',
        '6. Move arm inward at same rate groove spirals (~0.5mm/rev).',
        '',
        'Expected volume: low (like a whisper) but intelligible.',
        'One play wears a thorn tip — resharpen or replace.',
        'Steel pins last longer but may damage soft vinyl.',
        'Shellac 78s are more tolerant of improvised needles.',
    ]
    y = 405
    for s in steps:
        out += t(230, y, s, 'start', 'Lx')
        y += 8

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 6 — STEREO GROOVE  (y 503–520)
    # ══════════════════════════════════════════════════════════════════════
    out += hr(503, sw=0.3)
    out += t(240, 510, 'STEREO: left channel = 45° inner wall modulation  ·  right channel = 45° outer wall  ·  mono = equal lateral', 'middle', 'Lx')
    out += t(240, 518, 'a mono cartridge plays stereo records safely  ·  a stereo cartridge plays mono records safely', 'middle', 'Lx')

    # ══════════════════════════════════════════════════════════════════════
    # SECTION 7 — CARE  (y 523–545)
    # ══════════════════════════════════════════════════════════════════════
    out += hr(523, sw=0.3)
    out += t(240, 530, 'RECORD CARE: keep dry · brush before play · store vertically · never stack flat · inner sleeve protects', 'middle', 'Lx')
    out += t(240, 538, 'PLAYBACK LIMIT: vinyl ~300–1000 plays at correct force  ·  shellac ~100–300 plays  ·  thorn: 1 play', 'middle', 'Lx')
    out += t(240, 546, 'see Plate 8 for wave physics  ·  see Plate 10 for electrical generation  ·  amplifier from Plate 4', 'middle', 'Lx')

    out += close_svg()
    return out

def main():
    content = build()
    path = os.path.join(OUT, 'plate09_audio_playback_guide.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {path}')

if __name__ == '__main__':
    main()
