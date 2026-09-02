"""
plate_profiles.py — render profiles for the two plate media.

One SVG source, three outputs:
  METAL           monochrome, laser-engraved, fine detail   (Ti Gr2 / 316L)
  CERAMIC         color underglaze decal, fired, coarser    (stoneware / enamel-on-steel)
  CERAMIC_RELIEF  impressed from a plaster press mould      (stoneware, no printing)

CERAMIC and CERAMIC_RELIEF are NOT the same medium and do not share limits.
A decal is printed onto a fired surface and can hold 0.3 mm. A relief is
pressed into wet clay from a mould and must survive mould release, drying
shrinkage and firing shrinkage -- it holds about 1 mm. Relief is the cheap,
self-manufactured medium (see the 2026-08-20 affordability analysis); decal is
the colour medium.

Content is IDENTICAL between profiles. Only rendering changes. Color is an
overlay that carries no meaning — every plate must remain fully legible in
monochrome. See project/governance_series_scope.md and
project/symbol_universality_research.md.

Geometry reference (unchanged across profiles):
    viewBox 0 0 480 680  ->  120 x 170 mm  ->  1 unit = 0.25 mm
"""

MM_PER_UNIT = 0.25
UNITS_PER_MM = 1.0 / MM_PER_UNIT   # 4.0


def mm(v):
    """Millimetres -> SVG units."""
    return v * UNITS_PER_MM


PROFILES = {
    "metal": {
        "name": "metal",
        "label": "METAL — laser-engraved, monochrome",
        # Smallest reliably engraved feature. ~0.1 mm real-world.
        "min_feature_mm": 0.10,
        "min_stroke": 0.4,          # units (0.10 mm)
        "stroke_scale": 1.0,
        "min_font": 5.5,            # units (1.38 mm)
        "strokes": {"main": 1.5, "detail": 0.8, "texture": 0.5},
        "color": False,
        "notes": "Baseline. Matches all plates built to date.",
    },
    "ceramic_relief": {
        "name": "ceramic_relief",
        "label": "CERAMIC RELIEF -- impressed from a plaster press mould",
        # A line pressed into wet clay has to survive four insults: mould
        # release, the clay's own slump, ~12% shrinkage, and the glaze or wash
        # that lands in it. Below ~1 mm the walls close up and the line reads
        # as a smudge. Cuneiform wedges run 1-3 mm for exactly this reason.
        "min_feature_mm": 1.00,
        "min_stroke": 4.0,          # units (1.00 mm)
        "stroke_scale": 3.0,
        "min_font": 16.0,           # units (4.00 mm cap height)
        "strokes": {"main": 6.0, "detail": 4.5, "texture": 4.0},
        "color": False,             # oxide wash in the recesses, not printing
        # Relief-only parameters. Nothing else in the pipeline reads these yet;
        # they are here so the master-builder and the mould shop agree.
        "relief_depth_mm": 0.80,    # impressed depth; below 0.5 mm a wash won't hold
        "draft_angle_deg": 5.0,     # wall taper, or the tile tears on release
        "shrink_total": 0.12,       # drying + cone 6 firing, stoneware
        "min_tile_thickness_mm": 8.0,
        "notes": (
            "IMPRESSED, not raised: a recessed line is protected by the surface "
            "around it, which is why worn coins lose their relief before their "
            "counters fill. Master is a POSITIVE (raised) -> plaster negative "
            "-> pressed tile reads impressed. Master must be scaled up by "
            "1/(1-shrink) = 1.136x. No printing, no decal, no colour: legibility "
            "comes from shadow plus an iron or manganese oxide wash rubbed into "
            "the recesses and sponged off the surface."
        ),
    },

    "ceramic": {
        "name": "ceramic",
        "label": "CERAMIC — underglaze, fired, color",
        # Screen-printed underglaze decal holds ~0.2-0.3 mm. Below that,
        # pigment bleeds into the glaze during firing and lines close up.
        "min_feature_mm": 0.30,
        "min_stroke": 1.2,          # units (0.30 mm)
        "stroke_scale": 1.6,
        "min_font": 8.0,            # units (2.00 mm)
        "strokes": {"main": 2.5, "detail": 1.5, "texture": 1.2},
        "color": True,
        "notes": (
            "Cone 6 was chosen over cone 10 on 2026-08-06: near-equivalent "
            "vitrification, far cheaper kiln, longer element life, WIDER palette. "
            "Stoneware shrinks ~12% total at cone 6, so greenware must be "
            "oversized. Tiles under ~8 mm thick warp at this plate size."
        ),
    },
}


# Restricted on purpose: these five are metal-oxide colorants stable through a
# cone 6 firing (all are stable at cone 10 too, so the set survives a kiln
# change), and every one has a pre-industrial precedent a finder could in
# principle re-derive. Cone 6 permits a wider palette than this -- the
# restriction is a legibility and re-derivability choice, not a kiln limit.
#
# USE FOR DIFFERENTIATION AND MATERIAL DEPICTION ONLY, NEVER FOR MEANING.
# Color coding is a learned cultural convention and does not survive
# translation across cultures or centuries.
CERAMIC_PALETTE = {
    "manganese_black": {"hex": "#1b1a18", "oxide": "MnO2",  "use": "line work, charcoal, carbon"},
    "cobalt_blue":     {"hex": "#2a4a7c", "oxide": "CoO",   "use": "water, differentiation"},
    "iron_ochre":      {"hex": "#a8672e", "oxide": "Fe2O3", "use": "earth, clay, fired material"},
    "chrome_green":    {"hex": "#4a6b45", "oxide": "Cr2O3", "use": "living plants, growth"},
    "bone_white":      {"hex": "#efe9dd", "oxide": "ZrSiO4","use": "ground, negative space"},
}


def style_block(profile_name):
    """
    Emit the <style> CSS for a profile. Font sizes are floored at the
    profile minimum; classes keep the names used by every existing build
    script (L Ls Lx H S T M F Fb).
    """
    p = PROFILES[profile_name]
    f = lambda v: max(v, p["min_font"])
    return f"""<style>
    text {{ font-family: Georgia, serif; fill: #000; }}
    .L  {{ font-size: {f(7.0)}px; }}
    .Ls {{ font-size: {f(6.0)}px; }}
    .Lx {{ font-size: {f(5.5)}px; }}
    .H  {{ font-size: {f(6.5)}px; font-weight: bold; letter-spacing: 2.5px; }}
    .T  {{ font-size: {f(12.0)}px; font-weight: bold; letter-spacing: 2px; }}
    .S  {{ font-size: {f(7.0)}px; letter-spacing: 1.5px; }}
    .M  {{ font-size: {f(6.0)}px; }}
    .F  {{ font-size: {f(7.0)}px; font-style: italic; }}
    .Fb {{ font-size: {f(7.5)}px; font-weight: bold; }}
    .main {{ stroke-width: {p['strokes']['main']}; }}
    .detail {{ stroke-width: {p['strokes']['detail']}; }}
    .texture {{ stroke-width: {p['strokes']['texture']}; }}
  </style>"""


def describe(profile_name):
    p = PROFILES[profile_name]
    return (
        f"{p['label']}\n"
        f"  min feature   {p['min_feature_mm']:.2f} mm  ({mm(p['min_feature_mm']):.2f} units)\n"
        f"  min stroke    {p['min_stroke']} units\n"
        f"  min font      {p['min_font']} units ({p['min_font'] * MM_PER_UNIT:.2f} mm)\n"
        f"  strokes       main {p['strokes']['main']} / detail {p['strokes']['detail']}"
        f" / texture {p['strokes']['texture']}\n"
        f"  color         {'yes' if p['color'] else 'no'}\n"
        f"  {p['notes']}"
    )


if __name__ == "__main__":
    for name in PROFILES:
        print(describe(name))
        print()
    print("Cone 6 palette:")
    for k, v in CERAMIC_PALETTE.items():
        print(f"  {k:18s} {v['hex']}  {v['oxide']:8s} {v['use']}")
