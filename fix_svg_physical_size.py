"""
Declare physical size on every plate SVG, and on the scripts that generate them.

THE DEFECT
  Plate SVGs declared width="480" height="680" with no units. Unitless is CSS
  pixels, so every tool reads them at 96 dpi = 127 x 180 mm against a specified
  120 x 170 mm - 5.83% oversize. It is invisible on screen and only appears when
  a file is converted for manufacture. Caught 2026-09-01 when an Inkscape DXF
  export of the test coupon came back the wrong size.

  Files with no width/height at all are the same defect: a consumer falls back
  to the viewBox as pixels and lands in the same place.

THE FIX
  Add width/height in millimetres. viewBox is NEVER touched, so the drawing is
  bit-identical and only the declared physical size changes. The project scale
  is 1 unit = 0.25 mm (480 x 680 units = 120 x 170 mm).

BOTH LAYERS OR NEITHER
  The .svg files are build artefacts. Fixing them without fixing the generators
  means the defect returns on the next rebuild - the same drift that let the
  nickel and Viton claims survive three weeks of corrections. This patches the
  scripts too.

    python fix_svg_physical_size.py            # dry run
    python fix_svg_physical_size.py --apply
"""
import argparse
import pathlib
import re

MM_PER_UNIT = 0.25


def mm(v):
    s = f"{v * MM_PER_UNIT:g}"
    return s


def fix_svg_text(s):
    """Return (new_text, note) or (None, reason) if nothing to do."""
    m = re.search(r"<svg\b[^>]*>", s)
    if not m:
        return None, "no <svg> tag"
    tag = m.group(0)
    vb = re.search(r'viewBox="\s*0\s+0\s+([\d.]+)\s+([\d.]+)\s*"', tag)
    if not vb:
        return None, "no parseable viewBox"
    w_u, h_u = float(vb.group(1)), float(vb.group(2))
    w_mm, h_mm = mm(w_u), mm(h_u)

    cur_w = re.search(r'\swidth="([^"]*)"', tag)
    if cur_w and not re.fullmatch(r"[\d.]+", cur_w.group(1)):
        return None, f"already physical ({cur_w.group(1)})"

    new = tag
    if cur_w:
        new = re.sub(r'\swidth="[^"]*"', f' width="{w_mm}mm"', new, count=1)
        new = re.sub(r'\sheight="[^"]*"', f' height="{h_mm}mm"', new, count=1)
    else:
        new = new[:-1].rstrip() + f' width="{w_mm}mm" height="{h_mm}mm">'
    if new == tag:
        return None, "unchanged"
    return s[:m.start()] + new + s[m.end():], f'{w_mm}x{h_mm} mm'


# generator patterns: (regex, replacement) - only the width/height pair changes
GEN_SUBS = [
    (re.compile(r'(viewBox="0 0 480 680")\s+width="480"\s+height="680"'),
     r'\1 width="120mm" height="170mm"'),
    (re.compile(r'(viewBox="0 0 480 330")\s+width="480"\s+height="330"'),
     r'\1 width="120mm" height="82.5mm"'),
    (re.compile(r'(viewBox="0 0 \{W\} \{H\}")\s+width="\{W\}"\s+height="\{H\}"'),
     r'\1 width="120mm" height="170mm"'),
    # headers that declare no size at all
    (re.compile(r'(<svg xmlns="http://www\.w3\.org/2000/svg" viewBox="0 0 480 680")>'),
     r'\1 width="120mm" height="170mm">'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    print("APPLYING" if a.apply else "DRY RUN — nothing written")
    print("=" * 60)

    fixed = skipped = 0
    reasons = {}
    for p in sorted(pathlib.Path("plates").rglob("*.svg")):
        s = p.read_text(encoding="utf-8", errors="replace", newline="")
        new, note = fix_svg_text(s)
        if new is None:
            skipped += 1
            reasons[note] = reasons.get(note, 0) + 1
            continue
        fixed += 1
        if a.apply:
            p.write_text(new, encoding="utf-8", newline="")
    print(f"\nSVG files:  {fixed} to fix, {skipped} skipped")
    for r, n in sorted(reasons.items(), key=lambda kv: -kv[1]):
        print(f"    skipped: {n:>3}  {r}")

    gfixed = 0
    for p in sorted(pathlib.Path("plates").rglob("*.py")):
        s = p.read_text(encoding="utf-8", errors="replace", newline="")
        new = s
        for rx, rep in GEN_SUBS:
            new = rx.sub(rep, new)
        if new != s:
            gfixed += 1
            if a.apply:
                p.write_text(new, encoding="utf-8", newline="")
    print(f"\nGenerator scripts: {gfixed} to fix")

    if not a.apply:
        print("\nRe-run with --apply.")


if __name__ == "__main__":
    main()
