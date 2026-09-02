"""Layout check for plate12 — label collisions, overflow, min feature size.

Stands in for a visual proof when no rasteriser is available. Georgia advance
width averages ~0.50 em over uppercase text; that is the estimate used here,
so reported box widths are approximate but conservative enough to catch real
overlaps.
"""
import re
import xml.etree.ElementTree as ET

SVG = "plate12_precession_clock.svg"
NS = "{http://www.w3.org/2000/svg}"

SIZES = {"T": 12, "S": 7, "H": 6.5, "L": 7, "Ls": 6, "Lx": 5.5,
         "Lb": 6, "M": 6, "F": 7, "Fb": 7.5}
AVG_ADV = 0.50          # em per char, uppercase Georgia
INNER = (12, 12, 468, 656)   # inner border rect: x, y, w, h
MIN_FEATURE = 0.4       # SVG units, per project engraving spec

tree = ET.parse(SVG)
root = tree.getroot()

boxes = []
for el in root.iter(f"{NS}text"):
    txt = "".join(el.itertext())
    cls = el.get("class", "L")
    size = SIZES.get(cls, 7)
    x, y = float(el.get("x")), float(el.get("y"))
    w = len(txt) * size * AVG_ADV
    anchor = el.get("text-anchor", "start")
    x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
    boxes.append({"t": txt, "x0": x0, "x1": x0 + w,
                  "y0": y - size * 0.78, "y1": y + size * 0.24,
                  "cls": cls, "size": size})

print(f"text elements: {len(boxes)}")

# --- overflow past the inner border ---
bx0, by0 = INNER[0], INNER[1]
bx1, by1 = INNER[0] + INNER[2], INNER[1] + INNER[3]
over = [b for b in boxes if b["x0"] < bx0 + 3 or b["x1"] > bx1 - 3
        or b["y0"] < by0 + 3 or b["y1"] > by1 - 3]
print(f"\noverflowing inner border: {len(over)}")
for b in over:
    print(f"  [{b['cls']}] x {b['x0']:7.1f}..{b['x1']:7.1f}  "
          f"y {b['y0']:6.1f}  {b['t'][:58]}")

# --- label collisions ---
def hit(a, b):
    return not (a["x1"] <= b["x0"] or b["x1"] <= a["x0"]
                or a["y1"] <= b["y0"] or b["y1"] <= a["y0"])

coll = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        if hit(boxes[i], boxes[j]):
            coll.append((boxes[i], boxes[j]))

print(f"\noverlapping label pairs: {len(coll)}")
for a, b in coll:
    print(f"  {a['t'][:30]!r:34} <-> {b['t'][:30]!r}")

# --- engraved feature sizes ---
radii = [float(m) for m in re.findall(r'<circle[^>]*r="([\d.]+)"',
                                      open(SVG, encoding="utf-8").read())]
widths = [float(m) for m in re.findall(r'stroke-width="([\d.]+)"',
                                       open(SVG, encoding="utf-8").read())]
small_r = [r for r in radii if r < MIN_FEATURE]
small_w = [w for w in widths if w < MIN_FEATURE]
print(f"\nsmallest circle radius: {min(radii):.2f}u  "
      f"({len(small_r)} below {MIN_FEATURE}u minimum)")
print(f"thinnest stroke:        {min(widths):.2f}u  "
      f"({len(small_w)} below {MIN_FEATURE}u minimum)")

# --- real-world scale ---
plate_w_cm = 12.0
u_to_mm = plate_w_cm * 10 / 480
print(f"\nat {plate_w_cm:.0f}cm plate width, 1 unit = {u_to_mm:.3f} mm")
print(f"  faintest star dot  {min(radii)*2*u_to_mm:.3f} mm diameter")
print(f"  thinnest line      {min(widths)*u_to_mm:.3f} mm")
print(f"  smallest text (Lx) {5.5*u_to_mm:.2f} mm cap height")
