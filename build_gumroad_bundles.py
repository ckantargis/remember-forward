"""
build_gumroad_bundles.py
Builds two Gumroad product ZIP files:

  downloads/gumroad-plate-set.zip          — plates only (PWYW, suggested $8)
  downloads/gumroad-complete-archive.zip   — plates + all guides + docs (suggested $20)

Run from repo root: python build_gumroad_bundles.py
"""

import os, zipfile

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'downloads')
os.makedirs(OUT, exist_ok=True)

# ── Helpers ───────────────────────────────────────────────────────────────────

def add_dir(zf, local_dir, arc_prefix):
    """Recursively add a local directory into the zip under arc_prefix."""
    for root, dirs, files in os.walk(local_dir):
        dirs.sort()
        for f in sorted(files):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, local_dir).replace(os.sep, '/')
            zf.write(full, f'{arc_prefix}/{rel}')

def svg_count(local_dir):
    n = 0
    for root, dirs, files in os.walk(local_dir):
        n += sum(1 for f in files if f.endswith('.svg'))
    return n

# ── README texts ─────────────────────────────────────────────────────────────

README_PLATES = """\
REMEMBER FORWARD — THE PATIENT MESSAGE
Plate Set · CC BY-SA 4.0 · rememberforward.org
================================================

WHAT'S IN THIS ARCHIVE
  plates/knowledge/       11 knowledge plates
  plates/languages/       49 language series, 4 plates each (208 plates)
  remember-forward-plates.pdf   All plates as a single print-ready PDF

PLATE TYPES (each language)
  A  Script & writing system — alphabet, syllabary, or abugida
  B  Phonology — sound inventory, tones, vowel systems, IPA
  C  Grammar & vocabulary — word order, verb system, ~30 core words
  D  Running text & bridge phrase — real passages with interlinear gloss

THE BRIDGE PHRASE
Every Plate D ends with this phrase in the target language:
"This was made for you, freely, by people who remembered forward."

LANGUAGES COVERED
  Hebrew (Biblical · Mishnaic · Yemenite · Modern), Arabic, Tamil, Sanskrit,
  Bengali, Mandarin, Japanese, Malay/Indonesian, Swahili, Greek, Latin,
  Persian, Russian, Hindi, Spanish, Portuguese, French, Hausa, Yoruba,
  Amharic, Somali, Lingala, Tigrinya, Igbo, Shona, Zulu, Vietnamese, Thai,
  Burmese, Lao, Tagalog, Javanese, Sinhala, Tok Pisin, Quechua, Nahuatl,
  English, Dutch, Korean, Turkish, German, Punjabi, Urdu, Pashto, Tibetan,
  Mongolian, Khmer, Hawaiian, Egyptian Arabic

FORMAT
  SVG · 480x680 pt · black strokes only · no fills · no color
  Laser-engraver ready · scales to any material size
  Recommended material: nickel, stainless steel, or anodized aluminum

PRINTING
  The included PDF prints at 5"x7" on standard paper.
  For metal engraving, open SVGs in LightBurn, RDWorks, or Inkscape.

LICENSE
  CC BY-SA 4.0 — copy, adapt, distribute, even commercially,
  as long as you credit and share alike.
  https://creativecommons.org/licenses/by-sa/4.0/

SUPPORT
  If this was useful, consider buying a copy for someone else.
  rememberforward.org
"""

README_COMPLETE = """\
REMEMBER FORWARD — THE PATIENT MESSAGE
Complete Archive · CC BY-SA 4.0 · rememberforward.org
=======================================================

WHAT'S IN THIS ARCHIVE

  plates/               All 219 SVG plates + print-ready PDF
    knowledge/          11 knowledge plates (survival to metaphysics)
    languages/          49 language series, 4 plates each

  guides/               Build and context guides
    gd_00  Main guide — how to use this system
    gd_01  IP manufacturing — making the plates
    gd_02  Founder's letter — why this exists
    gd_03  Tier 1 — Survival knowledge
    gd_04  Tier 2 — Agriculture
    gd_05  Tier 3 — Technology re-foundation
    gd_06  Tier 4 — Governance and ethics
    gd_07  Tier 5 — Advanced science
    gd_08  Tier 6 — Metaphysics and meaning

  containers/           Container design and burial guides
    Tier 0   Fired ceramic + pitch ($10-30 · 500-2000 yrs)
    Tier A   Schedule 80 PVC ($75-150 · 100-300 yrs)
    Tier B   Titanium tube ($300-600 · 1000-5000 yrs)
    Tier C   Ocean deployment
    Tier D   Network distribution
    Tier E   Hastelloy alloy ($2000+ · 5000+ yrs)
    Tier F   Granite vault ($10,000+ · indefinite)
    Location strategies guide

  project/              Project documentation
    master_handoff.docx
    inner_ark_operational_structure.docx

THE BRIDGE PHRASE
"This was made for you, freely, by people who remembered forward."
Engraved on every Plate D in every language.

LICENSE
  CC BY-SA 4.0 — copy, adapt, distribute freely.
  The knowledge belongs to whoever finds it.
  https://creativecommons.org/licenses/by-sa/4.0/

rememberforward.org
"""

# ── Build Plate Set bundle ────────────────────────────────────────────────────

def build_plate_set():
    path = os.path.join(OUT, 'gumroad-plate-set.zip')
    plates_dir = os.path.join(BASE, 'plates')
    pdf_path = os.path.join(OUT, 'remember-forward-plates.pdf')
    n = svg_count(plates_dir)
    print(f'Building Plate Set bundle ({n} SVGs)...')
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('README.txt', README_PLATES)
        add_dir(zf, plates_dir, 'plates')
        if os.path.exists(pdf_path):
            zf.write(pdf_path, 'remember-forward-plates.pdf')
    mb = os.path.getsize(path) / 1_048_576
    print(f'  -> {path}  ({mb:.1f} MB)')
    return path

# ── Build Complete Archive bundle ─────────────────────────────────────────────

def build_complete_archive():
    path = os.path.join(OUT, 'gumroad-complete-archive.zip')
    plates_dir  = os.path.join(BASE, 'plates')
    guides_dir  = os.path.join(BASE, 'guides')
    containers_dir = os.path.join(BASE, 'containers')
    project_dir = os.path.join(BASE, 'project')
    pdf_path    = os.path.join(OUT, 'remember-forward-plates.pdf')
    n = svg_count(plates_dir)
    print(f'Building Complete Archive bundle ({n} SVGs + guides + docs)...')
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('README.txt', README_COMPLETE)
        add_dir(zf, plates_dir, 'plates')
        if os.path.exists(pdf_path):
            zf.write(pdf_path, 'remember-forward-plates.pdf')
        if os.path.exists(guides_dir):
            add_dir(zf, guides_dir, 'guides')
        if os.path.exists(containers_dir):
            add_dir(zf, containers_dir, 'containers')
        if os.path.exists(project_dir):
            add_dir(zf, project_dir, 'project')
    mb = os.path.getsize(path) / 1_048_576
    print(f'  -> {path}  ({mb:.1f} MB)')
    return path

# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    build_plate_set()
    print()
    build_complete_archive()
    print('\nDone. Upload these to Gumroad:')
    print('  Product 1: gumroad-plate-set.zip        PWYW, suggested $8')
    print('  Product 2: gumroad-complete-archive.zip  suggested $20')
