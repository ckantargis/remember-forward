"""
build_downloads.py
Generates two download packages:
  downloads/remember-forward-all-plates.zip   — all SVGs, folder structure preserved
  downloads/remember-forward-plates.pdf       — all plates as a single PDF

Run from the repo root:
  python build_downloads.py
"""

import os, zipfile, io, glob, sys

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, 'downloads')
os.makedirs(OUT_DIR, exist_ok=True)

# ── Plate ordering ────────────────────────────────────────────────────────────
# Knowledge plates first (sorted by filename), then language plates sorted by
# series number (extracted from filename pattern plateNN[a-d]_...).

def plate_sort_key(rel_path):
    fname = os.path.basename(rel_path)
    # Knowledge plates: plate01..plate11
    if 'knowledge' in rel_path:
        return (0, fname)
    # Language plates: plateNNx_...  NN = series number, x = a/b/c/d
    import re
    m = re.search(r'plate(\d+)([a-d])', fname)
    if m:
        return (1, int(m.group(1)), m.group(2))
    return (2, fname)

def collect_svgs():
    svgs = []
    for root, dirs, files in os.walk(os.path.join(BASE, 'plates')):
        for f in files:
            if f.endswith('.svg'):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, BASE).replace(os.sep, '/')
                svgs.append((rel, full))
    svgs.sort(key=lambda x: plate_sort_key(x[0]))
    return svgs

# ── ZIP ───────────────────────────────────────────────────────────────────────
def build_zip(svgs):
    zip_path = os.path.join(OUT_DIR, 'remember-forward-all-plates.zip')
    print(f'Building ZIP ({len(svgs)} files)...')
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        # Add a README at the root
        readme = (
            'REMEMBER FORWARD — THE PATIENT MESSAGE\n'
            'CC BY-SA 4.0 · rememberforward.org\n'
            '========================================\n\n'
            f'This archive contains {len(svgs)} SVG plate files.\n\n'
            'STRUCTURE\n'
            '  plates/knowledge/       11 knowledge plates (survival -> metaphysics)\n'
            '  plates/languages/{lang} 4 plates per language (60 languages)\n\n'
            'PLATE TYPES (per language)\n'
            '  A = Script & writing system\n'
            '  B = Phonology\n'
            '  C = Grammar & vocabulary\n'
            '  D = Running text & bridge phrase\n\n'
            'BRIDGE PHRASE (on every Plate D)\n'
            '"This was made for you, freely, by people who remembered forward."\n\n'
            'FORMAT\n'
            '  SVG · 480×680px · black strokes only · laser-engraver ready\n'
            '  Designed for nickel or stainless steel plate engraving\n\n'
            'LICENSE\n'
            '  Creative Commons Attribution-ShareAlike 4.0 International\n'
            '  Copy · Translate · Improve · Distribute freely\n'
        )
        zf.writestr('README.txt', readme)
        for rel, full in svgs:
            zf.write(full, rel)
    size_mb = os.path.getsize(zip_path) / 1_048_576
    print(f'  -> {zip_path}  ({size_mb:.1f} MB)')
    return zip_path

# ── PDF ───────────────────────────────────────────────────────────────────────
def build_pdf(svgs):
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF

    pdf_path = os.path.join(OUT_DIR, 'remember-forward-plates.pdf')
    print(f'Building PDF ({len(svgs)} pages)...')

    # Page size matches SVG viewBox: 480x680 pt
    PAGE_W, PAGE_H = 480, 680

    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.graphics import renderPDF as rpdf

    c = rl_canvas.Canvas(pdf_path, pagesize=(PAGE_W, PAGE_H))
    c.setTitle('Remember Forward — The Patient Message')
    c.setAuthor('Remember Forward · rememberforward.org')
    c.setSubject('Complete plate set — CC BY-SA 4.0')

    errors = []
    for i, (rel, full) in enumerate(svgs):
        if (i + 1) % 25 == 0 or i == 0:
            print(f'  page {i+1}/{len(svgs)}  {rel}')
        try:
            drawing = svg2rlg(full)
            if drawing is None:
                errors.append(rel)
                c.showPage()
                continue
            # Scale drawing to fit page exactly
            sx = PAGE_W / drawing.width if drawing.width else 1
            sy = PAGE_H / drawing.height if drawing.height else 1
            drawing.width = PAGE_W
            drawing.height = PAGE_H
            drawing.transform = (sx, 0, 0, sy, 0, 0)
            rpdf.draw(drawing, c, 0, 0)
        except Exception as e:
            errors.append(f'{rel}: {e}')
            c.showPage()
            continue
        c.showPage()

    c.save()
    size_mb = os.path.getsize(pdf_path) / 1_048_576
    print(f'  -> {pdf_path}  ({size_mb:.1f} MB)')
    if errors:
        print(f'  Errors ({len(errors)}):')
        for e in errors:
            print(f'    {e}')
    return pdf_path

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    svgs = collect_svgs()
    print(f'Found {len(svgs)} SVG plates.\n')

    build_zip(svgs)
    print()
    build_pdf(svgs)
    print('\nDone.')
