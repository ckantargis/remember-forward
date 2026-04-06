"""
build_outreach_images.py
Generates all preview images for outreach posts using Inkscape.

Images produced (in outreach/images/):
  individual plates:
    plate01_rosetta.png             — knowledge scope
    plate09_audio.png               — most diagram-heavy knowledge plate
    plate56a_tibetan_script.png     — visually striking non-Latin script
    plate50a_korean_script.png      — Hangul (recognizable, clean)
    plate53a_punjabi_script.png     — Gurmukhi (visually rich)
    plate60a_egyptian_script.png    — Arabic script (familiar)
    plate59a_hawaiian_script.png    — smallest alphabet, striking contrast
    plate47c_nahuatl_grammar.png    — polysynthetic grammar plate

  composites (SVG collages rendered to PNG):
    hero_grid.png          — 3x3 grid of varied plates, 1200x675 (OG/Twitter)
    hero_scripts.png       — 2x4 grid of script plates only, 1200x675
    hero_knowledge.png     — all 11 knowledge plates in two rows, 1200x500

Run from repo root: python build_outreach_images.py
Requires Inkscape installed at C:/Program Files/Inkscape/bin/inkscape.exe
"""

import os, subprocess, textwrap

BASE = os.path.dirname(os.path.abspath(__file__))
IMG_OUT = os.path.join(BASE, 'outreach', 'images')
os.makedirs(IMG_OUT, exist_ok=True)

INKSCAPE = r'C:\Program Files\Inkscape\bin\inkscape.exe'

def export_png(svg_path, out_path, width=960):
    result = subprocess.run(
        [INKSCAPE, f'--export-filename={out_path}', f'--export-width={width}', svg_path],
        capture_output=True, text=True
    )
    if os.path.exists(out_path):
        kb = os.path.getsize(out_path) // 1024
        print(f'  OK  {os.path.basename(out_path)}  ({kb} KB)')
    else:
        print(f'  FAIL  {out_path}')
        if result.stderr:
            print(f'    {result.stderr[:200]}')

def make_composite_svg(cells, canvas_w, canvas_h, cell_w, cell_h, cols, padding=8):
    """
    Build an SVG that embeds other SVGs as <image> elements in a grid.
    cells: list of (svg_path, label_text)  — left-to-right, top-to-bottom
    """
    rows = (len(cells) + cols - 1) // cols
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" '
                 f'xmlns:xlink="http://www.w3.org/1999/xlink" '
                 f'viewBox="0 0 {canvas_w} {canvas_h}" '
                 f'width="{canvas_w}" height="{canvas_h}">')
    # Background
    parts.append(f'<rect width="{canvas_w}" height="{canvas_h}" fill="#0d0d14"/>')

    for i, (svg_path, label) in enumerate(cells):
        col = i % cols
        row = i // cols
        x = padding + col * (cell_w + padding)
        y = padding + row * (cell_h + padding)
        # Embed SVG as image
        rel = os.path.relpath(svg_path, BASE).replace(os.sep, '/')
        parts.append(
            f'<image href="{rel}" x="{x}" y="{y}" '
            f'width="{cell_w}" height="{cell_h}" '
            f'preserveAspectRatio="xMidYMid meet"/>'
        )
        # Thin border
        parts.append(
            f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" '
            f'fill="none" stroke="#2a2a40" stroke-width="1"/>'
        )
        if label:
            lx = x + cell_w // 2
            ly = y + cell_h + 12
            parts.append(
                f'<text x="{lx}" y="{ly}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="9" fill="#5a5a7a">{label}</text>'
            )

    parts.append('</svg>')
    return '\n'.join(parts)

def write_and_export(svg_content, name, width=1200):
    tmp_svg = os.path.join(IMG_OUT, f'_tmp_{name}.svg')
    out_png = os.path.join(IMG_OUT, f'{name}.png')
    with open(tmp_svg, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    export_png(tmp_svg, out_png, width=width)
    os.remove(tmp_svg)

P = os.path.join(BASE, 'plates')  # shorthand

# ── Individual plates ─────────────────────────────────────────────────────────
print('Individual plates...')
individuals = [
    (f'{P}/knowledge/plate01_v3_rosetta.svg',              'plate01_rosetta.png',          960),
    (f'{P}/knowledge/plate09_audio_playback_guide.svg',    'plate09_audio.png',            960),
    (f'{P}/languages/tibetan/plate56a_tibetan_script.svg', 'plate56a_tibetan_script.png',  960),
    (f'{P}/languages/korean/plate50a_korean_script.svg',   'plate50a_korean_script.png',   960),
    (f'{P}/languages/punjabi/plate53a_punjabi_script.svg', 'plate53a_punjabi_script.png',  960),
    (f'{P}/languages/egyptian-arabic/plate60a_egyptian_arabic_script.svg',
                                                            'plate60a_egyptian_script.png', 960),
    (f'{P}/languages/hawaiian/plate59a_hawaiian_script.svg','plate59a_hawaiian_script.png',960),
    (f'{P}/languages/nahuatl/plate47c_nahuatl_grammar.svg','plate47c_nahuatl_grammar.png', 960),
    (f'{P}/languages/tibetan/plate56c_tibetan_grammar.svg','plate56c_tibetan_grammar.png', 960),
    (f'{P}/languages/mongolian/plate57a_mongolian_script.svg','plate57a_mongolian_script.png',960),
    (f'{P}/languages/hebrew/plate09a_biblical_hebrew.svg', 'plate09a_biblical_hebrew.png', 960),
    (f'{P}/languages/thai/plate39a_thai_script.svg',       'plate39a_thai_script.png',     960),
]
for svg, out, w in individuals:
    export_png(svg, os.path.join(IMG_OUT, out), width=w)

# ── Composite: Hero grid 3x3 (1200x675 — OG/Twitter/Reddit) ──────────────────
print('\nHero grid (3x3)...')
# 3 cols, 3 rows: 9 diverse plates
# canvas 1200x675, padding 10
# cell = (1200 - 10*4) / 3  x  (675 - 10*4) / 3  = 386 x 211 (too wide for portrait)
# Better: use cell sized to portrait ratio 480:680 = 0.706
# With padding 8: cols=4, canvas 1200x700
# cell_w = (1200 - 8*5)/4 = 280   cell_h = 280/0.706 = 396  → too tall
# Let's just do 4 cols, rows as needed, render at 1200 wide

hero_cells = [
    (f'{P}/knowledge/plate01_v3_rosetta.svg',               'Plate 01 — Rosetta Index'),
    (f'{P}/languages/tibetan/plate56a_tibetan_script.svg',   '56A — Tibetan Script'),
    (f'{P}/languages/arabic/plate13a_arabic_script.svg',     '13A — Arabic Script'),
    (f'{P}/languages/korean/plate50a_korean_script.svg',     '50A — Korean Hangul'),
    (f'{P}/knowledge/plate09_audio_playback_guide.svg',      'Plate 09 — Audio Playback'),
    (f'{P}/languages/mongolian/plate57a_mongolian_script.svg','57A — Mongolian'),
    (f'{P}/languages/punjabi/plate53a_punjabi_script.svg',   '53A — Punjabi Gurmukhi'),
    (f'{P}/languages/nahuatl/plate47c_nahuatl_grammar.svg',  '47C — Nahuatl Grammar'),
    (f'{P}/languages/hawaiian/plate59a_hawaiian_script.svg', '59A — Hawaiian'),
    (f'{P}/languages/thai/plate39a_thai_script.svg',         '39A — Thai Script'),
    (f'{P}/languages/hebrew/plate09a_biblical_hebrew.svg',   '09A — Biblical Hebrew'),
    (f'{P}/languages/egyptian-arabic/plate60a_egyptian_arabic_script.svg','60A — Egyptian Arabic'),
]
# 4 cols × 3 rows, canvas 1200 wide
# cell_w = (1200 - 8*5)/4 = 280,  cell_h = 280*(680/480) = 397
COLS = 4
CW, CH = 280, 397
PAD = 8
canvas_w = PAD + COLS*(CW+PAD)
canvas_h = PAD + 3*(CH+PAD) + 20  # +20 for labels
svg = make_composite_svg(hero_cells, canvas_w, canvas_h, CW, CH, COLS, PAD)
write_and_export(svg, 'hero_grid', width=1200)

# ── Composite: Script diversity — 6 visually distinct scripts ─────────────────
print('\nScript diversity composite...')
script_cells = [
    (f'{P}/languages/tibetan/plate56a_tibetan_script.svg',        'Tibetan — Uchen'),
    (f'{P}/languages/arabic/plate13a_arabic_script.svg',          'Arabic — Naskh'),
    (f'{P}/languages/hebrew/plate09a_biblical_hebrew.svg',         'Biblical Hebrew'),
    (f'{P}/languages/mongolian/plate57a_mongolian_script.svg',     'Mongolian — Cyrillic + Traditional'),
    (f'{P}/languages/punjabi/plate53a_punjabi_script.svg',         'Punjabi — Gurmukhi'),
    (f'{P}/languages/thai/plate39a_thai_script.svg',               'Thai — Abugida'),
    (f'{P}/languages/korean/plate50a_korean_script.svg',           'Korean — Hangul'),
    (f'{P}/languages/egyptian-arabic/plate60a_egyptian_arabic_script.svg','Egyptian Arabic'),
]
COLS2 = 4
canvas_w2 = PAD + COLS2*(CW+PAD)
canvas_h2 = PAD + 2*(CH+PAD) + 20
svg2 = make_composite_svg(script_cells, canvas_w2, canvas_h2, CW, CH, COLS2, PAD)
write_and_export(svg2, 'hero_scripts', width=1200)

# ── Composite: Knowledge plates — all 11 in two rows ─────────────────────────
print('\nKnowledge plates composite...')
k_dir = f'{P}/knowledge'
k_plates = [
    (f'{k_dir}/plate01_v3_rosetta.svg',            '01 Rosetta Index'),
    (f'{k_dir}/plate02_v2_water_fire_shelter.svg',  '02 Water · Fire · Shelter'),
    (f'{k_dir}/plate03_v2_agriculture_seeds.svg',   '03 Agriculture'),
    (f'{k_dir}/plate04_v2_technology.svg',          '04 Technology'),
    (f'{k_dir}/plate05_v2_governance.svg',          '05 Governance'),
    (f'{k_dir}/plate06_v2_concords_stars.svg',      '06 Stars · Concords'),
    (f'{k_dir}/plate07_encoding_communication.svg', '07 Encoding'),
    (f'{k_dir}/plate08_physics_of_sound_v2.svg',    '08 Sound'),
    (f'{k_dir}/plate09_audio_playback_guide.svg',   '09 Audio Playback'),
    (f'{k_dir}/plate10_electrical_phenomena.svg',   '10 Electricity'),
    (f'{k_dir}/plate11_energy_generation.svg',      '11 Energy'),
]
COLS3 = 6
CW3, CH3 = 180, 255  # tighter for 11 plates
canvas_w3 = PAD + COLS3*(CW3+PAD)
canvas_h3 = PAD + 2*(CH3+PAD) + 20
svg3 = make_composite_svg(k_plates, canvas_w3, canvas_h3, CW3, CH3, COLS3, PAD)
write_and_export(svg3, 'hero_knowledge', width=1200)

# ── Composite: Laser engraving focus — knowledge + close detail ───────────────
print('\nLaser focus composite...')
laser_cells = [
    (f'{k_dir}/plate09_audio_playback_guide.svg',            '09 Audio — needle diagram'),
    (f'{k_dir}/plate08_physics_of_sound_v2.svg',             '08 Sound — wave diagrams'),
    (f'{k_dir}/plate04_v2_technology.svg',                   '04 Technology — circuits'),
    (f'{k_dir}/plate02_v2_water_fire_shelter.svg',           '02 Water · Fire · Shelter'),
    (f'{P}/languages/tibetan/plate56a_tibetan_script.svg',   '56A Tibetan — stacked glyphs'),
    (f'{P}/languages/hebrew/plate09a_biblical_hebrew.svg',   '09A Biblical Hebrew'),
]
COLS4 = 3
canvas_w4 = PAD + COLS4*(CW+PAD)
canvas_h4 = PAD + 2*(CH+PAD) + 20
svg4 = make_composite_svg(laser_cells, canvas_w4, canvas_h4, CW, CH, COLS4, PAD)
write_and_export(svg4, 'hero_laser', width=1200)

print(f'\nAll images written to: {IMG_OUT}')
print('Files:')
for f in sorted(os.listdir(IMG_OUT)):
    if f.endswith('.png'):
        kb = os.path.getsize(os.path.join(IMG_OUT, f)) // 1024
        print(f'  {f}  ({kb} KB)')
