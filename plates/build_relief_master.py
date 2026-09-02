"""
build_relief_master.py — turn a metal plate into a press-mould master.

    python build_relief_master.py plate03_v2_agriculture_seeds.svg
    python build_relief_master.py plate03_v2_agriculture_seeds.svg --cap-mm 2.5
    python build_relief_master.py --all --cap-mm 2.5

Three things happen:

  1. Strokes and font sizes are floored at the relief minimum. A 0.4 mm line
     that a laser cuts happily closes up in clay.
  2. The physical width/height are scaled by 1/(1-shrink) so the FIRED tile
     lands at 120 x 170 mm. The viewBox is untouched, so every coordinate in
     the file still means what it meant — 1 unit = 0.25 mm of fired tile.
  3. A spec header is written into the file for whoever cuts the mould.

--cap-mm overrides the profile's minimum text size, because that number is the
single largest unknown in the ceramic plan and it is not settled by argument.
Fire plate_relief_calibration.svg, read the smallest text you can still read,
and pass it here. Everything downstream — plate count, mould library cost, jars
per capsule — follows from it.

The output is a DIAGNOSTIC, not a finished plate. Flooring the type does not
re-lay-out the page: text will overrun its boxes and collide. That overrun is
the measurement — it is telling you how much content has to come off this tile
and onto another one.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apply_profile import apply  # noqa: E402
from plate_profiles import PROFILES, MM_PER_UNIT  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE = os.path.join(HERE, "knowledge")
OUTDIR = os.path.join(KNOWLEDGE, "relief")

W_UNITS, H_UNITS = 480, 680
CAP_RATIO = 0.70


def convert(path, cap_mm=None, outdir=OUTDIR):
    p = dict(PROFILES["ceramic_relief"])
    if cap_mm is not None:
        p["min_font"] = (cap_mm / MM_PER_UNIT) / CAP_RATIO
        cap_used = cap_mm
    else:
        cap_used = p["min_font"] * MM_PER_UNIT * CAP_RATIO

    PROFILES["_relief_run"] = p
    src = open(path, encoding="utf-8").read()
    out, rep = apply(src, "_relief_run")
    del PROFILES["_relief_run"]

    shrink = p["shrink_total"]
    scale = 1.0 / (1.0 - shrink)
    w_mm = W_UNITS * MM_PER_UNIT * scale
    h_mm = H_UNITS * MM_PER_UNIT * scale

    # Physical size -> greenware. viewBox is deliberately left alone.
    # Existing width/height must be REMOVED first: duplicate attributes are a
    # fatal XML error, and these files carry width/height after the viewBox.
    m = re.search(r"<svg\b[^>]*>", out)
    if not m:
        raise ValueError(f"no <svg> tag in {path}")
    tag = m.group(0)
    stripped = re.sub(r'\s(?:width|height)="[^"]*"', "", tag)
    stripped = stripped.replace(
        "<svg", f'<svg width="{w_mm:.1f}mm" height="{h_mm:.1f}mm"', 1)
    out = out[:m.start()] + stripped + out[m.end():]

    header = (
        f"<!-- CERAMIC RELIEF MASTER — {os.path.basename(path)}\n"
        f"     Fired tile      120 x 170 mm\n"
        f"     Greenware/master {w_mm:.1f} x {h_mm:.1f} mm "
        f"(scaled {scale:.3f}x for {shrink * 100:.0f}% shrinkage)\n"
        f"     Min text        {cap_used:.2f} mm cap height\n"
        f"     Min line        {p['min_stroke'] * MM_PER_UNIT:.2f} mm\n"
        f"     Relief depth    {p['relief_depth_mm']:.2f} mm impressed\n"
        f"     Draft angle     {p['draft_angle_deg']:.0f} deg (or the tile tears on release)\n"
        f"     Tile thickness  {p['min_tile_thickness_mm']:.0f} mm minimum\n"
        f"\n"
        f"     MASTER IS A POSITIVE. Plaster negative is taken from it; the\n"
        f"     pressed tile reads IMPRESSED. Before extruding: Inkscape >\n"
        f"     Object to Path, then Stroke to Path, then save as plain SVG.\n"
        f"\n"
        f"     DIAGNOSTIC, NOT FINAL ART. Type was floored, not re-laid-out.\n"
        f"     Overrunning text is the measurement, not a bug. -->\n"
    )
    out = out.replace("<svg", header + "<svg", 1)

    os.makedirs(outdir, exist_ok=True)
    base = os.path.basename(path).replace(".svg", "")
    dest = os.path.join(outdir, f"{base}__relief.svg")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(out)

    return dest, rep, cap_used, (w_mm, h_mm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svg", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--cap-mm", type=float, default=None,
                    help="minimum text cap height in mm of FIRED tile "
                         "(default: the profile's 4.0, which is a guess)")
    args = ap.parse_args()

    if args.all:
        skip = ("figure_test", "filter_review", "sample_", "__", "calibration")
        files = sorted(os.path.join(KNOWLEDGE, f) for f in os.listdir(KNOWLEDGE)
                       if f.endswith(".svg") and not any(k in f for k in skip)
                       and not re.search(r"plate02_v[2-8]_", f))
    elif args.svg:
        files = [args.svg if os.path.isabs(args.svg)
                 else os.path.join(KNOWLEDGE, args.svg)]
    else:
        ap.error("give a plate filename or --all")

    print("CERAMIC RELIEF MASTERS")
    for f in files:
        dest, rep, cap, (w, h) = convert(f, args.cap_mm)
        print(f"\n  {os.path.basename(f)}")
        print(f"    -> {os.path.relpath(dest, HERE)}")
        print(f"       {w:.1f} x {h:.1f} mm greenware, {cap:.2f} mm min text")
        print(f"       {rep['strokes']} strokes widened, {rep['fonts']} type sizes raised")
        if rep["small"]:
            print(f"       {len(rep['small'])} primitives below the relief floor "
                  f"— these need redrawing, not rescaling")


if __name__ == "__main__":
    main()
