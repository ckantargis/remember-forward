"""
apply_profile.py — re-render an existing plate SVG under a different profile.

Lets you test the ceramic constraint against plates already built, without
touching their build scripts.

    python apply_profile.py plates/knowledge/plate01_v3_rosetta.svg ceramic
    python apply_profile.py <in.svg> ceramic -o <out.svg>

What it does:
  * scales stroke widths and floors them at the profile minimum
  * floors font sizes at the profile minimum
  * reports geometry that falls below the profile's minimum feature size

What it does NOT do:
  * analyze <path> d= geometry. Detecting a too-narrow gap between two curves
    needs real geometric analysis. Path-heavy plates MUST still be printed at
    120 x 170 mm and checked by eye.
  * add color. Colorizing needs to know what each shape depicts, which only the
    build script knows. Import CERAMIC_PALETTE in the build script instead.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plate_profiles import PROFILES, MM_PER_UNIT, describe  # noqa: E402

NUM = r"([0-9]*\.?[0-9]+)"


def _scale_stroke(value, p):
    return round(max(p["min_stroke"], value * p["stroke_scale"]), 3)


def apply(svg, profile_name):
    p = PROFILES[profile_name]
    report = {"strokes": 0, "fonts": 0, "small": []}

    def stroke_attr(m):
        old = float(m.group(1))
        new = _scale_stroke(old, p)
        if new != old:
            report["strokes"] += 1
        return f'stroke-width="{new}"'

    def stroke_css(m):
        old = float(m.group(1))
        new = _scale_stroke(old, p)
        if new != old:
            report["strokes"] += 1
        return f"stroke-width:{new}"

    def font_css(m):
        old = float(m.group(1))
        new = round(max(p["min_font"], old), 3)
        if new != old:
            report["fonts"] += 1
        return f"font-size:{new}px"

    def font_attr(m):
        old = float(m.group(1))
        new = round(max(p["min_font"], old), 3)
        if new != old:
            report["fonts"] += 1
        return f'font-size="{new}"'

    svg = re.sub(rf'stroke-width="{NUM}"', stroke_attr, svg)
    svg = re.sub(rf"stroke-width:\s*{NUM}", stroke_css, svg)
    svg = re.sub(rf"font-size:\s*{NUM}px", font_css, svg)
    svg = re.sub(rf'font-size="{NUM}"', font_attr, svg)

    # Flag primitives smaller than the profile can hold.
    floor = p["min_feature_mm"] / MM_PER_UNIT
    for tag, attrs in (("rect", ("width", "height")),
                       ("circle", ("r",)),
                       ("ellipse", ("rx", "ry"))):
        for el in re.findall(rf"<{tag}\b[^>]*>", svg):
            for a in attrs:
                m = re.search(rf'{a}="{NUM}"', el)
                if not m:
                    continue
                v = float(m.group(1))
                v = v * 2 if a in ("r", "rx", "ry") else v
                if v < floor:
                    report["small"].append(f"{tag} {a}={m.group(1)} ({v * MM_PER_UNIT:.3f} mm)")
    return svg, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("profile", choices=sorted(PROFILES))
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    with open(args.svg, encoding="utf-8") as fh:
        src = fh.read()

    out_svg, rep = apply(src, args.profile)

    out = args.out
    if not out:
        base, ext = os.path.splitext(args.svg)
        out = f"{base}__{args.profile}{ext}"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(out_svg)

    p = PROFILES[args.profile]
    print(describe(args.profile))
    print()
    print(f"in   {args.svg}")
    print(f"out  {out}")
    print(f"     {rep['strokes']} stroke widths scaled, {rep['fonts']} font sizes raised")

    if rep["small"]:
        uniq = sorted(set(rep["small"]))
        print(f"\n  {len(rep['small'])} primitives below {p['min_feature_mm']} mm "
              f"({len(uniq)} distinct) — these will close up when fired:")
        for s in uniq[:12]:
            print(f"    {s}")
        if len(uniq) > 12:
            print(f"    ... and {len(uniq) - 12} more")
    else:
        print(f"\n  no primitives below {p['min_feature_mm']} mm")

    print("\n  path geometry NOT checked — print at 120 x 170 mm and inspect.")


if __name__ == "__main__":
    main()
