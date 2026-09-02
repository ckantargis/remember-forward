"""
relief_report.py — how much of each plate survives being pressed into clay?

The metal plates were drawn to a 0.10 mm feature limit. A tile pressed from a
plaster mould holds about 1.00 mm. That is a 10x coarsening, and the question
this answers is not "does it still look right" (it does not) but "how many
ceramic tiles does one metal plate become".

Method: text is what fails first and what is easiest to measure honestly. Every
<text> element is measured at its metal font size and again at the relief
minimum, using a 0.55em average advance width for Georgia. The ratio of total
text area is the tile multiplier — how many tiles of the same size are needed to
hold the same words at a size that survives firing.

    python relief_report.py                 # every knowledge plate
    python relief_report.py plate03_v2_agriculture_seeds.svg

Caveats, stated because they change the answer:
  * ignores diagrams entirely. A drawing coarsens differently from text — some
    survive untouched, some lose the distinction they were carrying.
  * pattern fills (sand, gravel, charcoal texture) do not press at all and are
    counted separately. They need redrawing as discrete impressed marks.
  * assumes the tile stays 120 x 170 mm. Making the tile bigger is usually the
    cheaper fix than splitting a plate.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plate_profiles import PROFILES, MM_PER_UNIT  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE = os.path.join(HERE, "knowledge")

# Georgia's average advance across mixed-case text, in em. Measured rather than
# assumed would be better; this is close enough to rank plates against usable.
AVG_ADVANCE_EM = 0.55
LINE_HEIGHT_EM = 1.30

CLASS_SIZES = {  # from style_block() in plate_profiles.py, metal profile
    "L": 7.0, "Ls": 6.0, "Lx": 5.5, "H": 6.5, "T": 12.0,
    "S": 7.0, "M": 6.0, "F": 7.0, "Fb": 7.5,
}
DEFAULT_SIZE = 7.0

TEXT_RE = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)
TSPAN_RE = re.compile(r"<tspan\b[^>]*>(.*?)</tspan>", re.S)


def _font_size(attrs, svg_defaults):
    m = re.search(r'font-size="([0-9.]+)"', attrs)
    if m:
        return float(m.group(1))
    m = re.search(r'font-size:\s*([0-9.]+)', attrs)
    if m:
        return float(m.group(1))
    m = re.search(r'class="([^"]+)"', attrs)
    if m:
        for cls in m.group(1).split():
            if cls in svg_defaults:
                return svg_defaults[cls]
    return DEFAULT_SIZE


def _plain(inner):
    parts = TSPAN_RE.findall(inner)
    text = " ".join(parts) if parts else inner
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def analyse(path):
    svg = open(path, encoding="utf-8").read()

    sizes = dict(CLASS_SIZES)
    for cls, val in re.findall(r"\.(\w+)\s*\{[^}]*font-size:\s*([0-9.]+)px", svg):
        sizes[cls] = float(val)

    relief = PROFILES["ceramic_relief"]
    min_font = relief["min_font"]
    min_stroke = relief["min_stroke"]
    floor_units = relief["min_feature_mm"] / MM_PER_UNIT

    metal_area = relief_area = 0.0
    chars = raised = 0
    smallest = 99.0

    for attrs, inner in TEXT_RE.findall(svg):
        s = _plain(inner)
        if not s:
            continue
        n = len(s)
        size = _font_size(attrs, sizes)
        smallest = min(smallest, size)
        chars += n
        metal_area += n * size * AVG_ADVANCE_EM * size * LINE_HEIGHT_EM
        new = max(size, min_font)
        if new > size:
            raised += 1
        relief_area += n * new * AVG_ADVANCE_EM * new * LINE_HEIGHT_EM

    strokes = [float(v) for v in re.findall(r'stroke-width="([0-9.]+)"', svg)]
    strokes += [float(v) for v in re.findall(r"stroke-width:\s*([0-9.]+)", svg)]
    thin = sum(1 for v in strokes if v < min_stroke)

    tiny = 0
    for tag, attrs_ in (("rect", ("width", "height")), ("circle", ("r",)),
                        ("ellipse", ("rx", "ry"))):
        for el in re.findall(rf"<{tag}\b[^>]*>", svg):
            for a in attrs_:
                m = re.search(rf'{a}="([0-9.]+)"', el)
                if not m:
                    continue
                v = float(m.group(1)) * (2 if a in ("r", "rx", "ry") else 1)
                if v < floor_units:
                    tiny += 1

    return {
        "plate": os.path.basename(path),
        "chars": chars,
        "raised": raised,
        "smallest_mm": smallest * MM_PER_UNIT,
        "mult": (relief_area / metal_area) if metal_area else 0.0,
        "thin": thin,
        "strokes": len(strokes),
        "tiny": tiny,
        "patterns": len(re.findall(r"<pattern\b", svg)),
    }


def main():
    args = sys.argv[1:]
    if args:
        files = [a if os.path.isabs(a) else os.path.join(KNOWLEDGE, a) for a in args]
    else:
        skip = ("figure_test", "filter_review", "sample_", "__")
        files = sorted(
            os.path.join(KNOWLEDGE, f)
            for f in os.listdir(KNOWLEDGE)
            if f.endswith(".svg") and not any(k in f for k in skip)
            and not re.search(r"plate02_v[2-8]_", f)
        )

    rows = [analyse(f) for f in files]

    print("RELIEF READINESS — metal plates measured against the ceramic_relief profile")
    print(f"  min feature 1.00 mm · min stroke 1.00 mm · min text 4.00 mm cap height\n")
    hdr = f"{'plate':<34}{'chars':>7}{'min mm':>8}{'text x':>8}{'tiles':>7}{'thin':>12}{'tiny':>7}{'patt':>6}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        name = r["plate"].replace(".svg", "").replace("_v2", "").replace("_v3", "")
        tiles = max(1, round(r["mult"] + 0.35))
        thin = f"{r['thin']}/{r['strokes']}"
        print(f"{name:<34}{r['chars']:>7}{r['smallest_mm']:>8.2f}{r['mult']:>8.1f}"
              f"{tiles:>7}{thin:>12}{r['tiny']:>7}{r['patterns']:>6}")

    tot_mult = sum(r["mult"] for r in rows) / len(rows)
    tiles = sum(max(1, round(r["mult"] + 0.35)) for r in rows)
    print("-" * len(hdr))
    print(f"{len(rows)} plates · mean text multiplier {tot_mult:.1f}x · "
          f"{tiles} tiles at 120x170 mm")
    print(f"\nthin  = strokes below 1.00 mm / total strokes")
    print(f"tiny  = rects/circles/ellipses below 1.00 mm")
    print(f"patt  = pattern fills; these do not press and must be redrawn as "
          f"discrete marks")


if __name__ == "__main__":
    main()
