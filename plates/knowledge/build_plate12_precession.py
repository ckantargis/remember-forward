"""Plate 12 — The Precession Clock.

A polar-projection chart centred on the pole of the Earth's ORBIT (the north
ecliptic pole), which does not move. Around it the pole of the Earth's SPIN
travels a 23.44-degree circle once every ~25,772 years.

That circle is a clock. The plate marks where the spin pole stood when the
plate was made; a finder who measures where it stands for them reads the
elapsed time straight off the rim. No shared calendar, no lab, no instrument
beyond a sighting stick.

Coordinates are J2000. Proper motion is ignored: over the 500-2000 year
design window even Arcturus moves ~1.3 deg and the polar stars far less,
which is below the engraved dot size.

Output: plate12_precession_clock.svg
"""
import math
import os

# --- astronomy ----------------------------------------------------------

OBLIQ = 23.4393                    # obliquity of the ecliptic, deg (J2000)
PREC_RATE = 50.2877 / 3600.0       # general precession in longitude, deg/yr
PREC_PERIOD = 360.0 / PREC_RATE    # ~25,772 yr
EPOCH = 2026                       # year the plate is made

# Rate at which the celestial pole moves ACROSS THE SKY. This is the
# precession rate reduced by sin(obliquity), because the pole travels a small
# circle of angular radius = obliquity, not a great circle.
POLE_ARC_RATE = PREC_RATE * math.sin(math.radians(OBLIQ))   # deg/yr


def eq_to_ecl(ra_h, dec_d):
    """Equatorial (RA hours, Dec deg) -> ecliptic (lon deg, lat deg)."""
    a, d = math.radians(ra_h * 15.0), math.radians(dec_d)
    e = math.radians(OBLIQ)
    sb = math.sin(d) * math.cos(e) - math.cos(d) * math.sin(e) * math.sin(a)
    lat = math.asin(sb)
    y = math.sin(d) * math.sin(e) + math.cos(d) * math.cos(e) * math.sin(a)
    x = math.cos(d) * math.cos(a)
    return math.degrees(math.atan2(y, x)) % 360.0, math.degrees(lat)


def ncp_lon(year):
    """Ecliptic longitude of the north CELESTIAL pole at `year`.

    At J2000 the celestial pole sits at ecliptic longitude 90 deg; precession
    carries it backwards through longitude at PREC_RATE.
    """
    return (90.0 - PREC_RATE * (year - 2000.0)) % 360.0


def sep(l1, b1, l2, b2):
    """Angular separation between two ecliptic positions, degrees."""
    l1, b1, l2, b2 = map(math.radians, (l1, b1, l2, b2))
    c = (math.sin(b1) * math.sin(b2) +
         math.cos(b1) * math.cos(b2) * math.cos(l1 - l2))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


# --- stars --------------------------------------------------------------
# name, RA hours, Dec deg, magnitude, label anchor hint, label dy
# dy nudges labels apart where stars sit closer than their names are wide;
# Rastaban and Eltanin are 0.9 deg apart in Draco's head and need it.
STARS = [
    ("POLARIS",   2.5303, 89.2641, 1.98, "e", 0.0),
    ("KOCHAB",   14.8451, 74.1555, 2.08, "e", 0.0),
    ("PHERKAD",  15.3455, 71.8340, 3.00, "e", 0.0),
    ("THUBAN",   14.0731, 64.3758, 3.65, "e", 0.0),
    ("EDASICH",  15.4155, 58.9648, 3.29, "e", 0.0),
    ("GIAUSAR",  11.5311, 69.3312, 3.85, "w", 0.0),
    ("RASTABAN", 17.5072, 52.3014, 2.79, "e", -4.5),
    ("ELTANIN",  17.9435, 51.4889, 2.23, "e", 5.0),
    ("ALDERAMIN", 21.3097, 62.5856, 2.45, "w", 0.0),
    ("ALFIRK",   21.4776, 70.5607, 3.23, "w", 0.0),
    ("ERRAI",    23.6558, 77.6323, 3.21, "w", 0.0),
    ("IOTA CEP", 22.8281, 66.2005, 3.52, "w", 0.0),
    ("DENEB",    20.6906, 45.2803, 1.25, "w", 0.0),
    ("VEGA",     18.6156, 38.7837, 0.03, "e", 0.0),
    ("DUBHE",    11.0622, 61.7511, 1.79, "w", 0.0),
    ("MERAK",    11.0307, 56.3824, 2.37, "w", 0.0),
    ("ALIOTH",   12.9005, 55.9598, 1.77, "w", 0.0),
    ("MIZAR",    13.3988, 54.9254, 2.23, "w", 0.0),
    ("ALKAID",   13.7923, 49.3133, 1.86, "w", 0.0),
    ("SCHEDAR",   0.6751, 56.5373, 2.24, "e", 0.0),
    ("CAPH",      0.1529, 59.1498, 2.28, "e", 0.0),
    ("RUCHBAH",   1.4304, 60.2353, 2.68, "e", 0.0),
    ("SEGIN",     1.9065, 63.6701, 3.38, "e", 0.0),
    ("TAU HER",  16.3325, 46.3131, 3.89, "e", 0.0),
]

# pole stars worth naming on the rim: (star name, label)
RIM_MARKS = ["THUBAN", "POLARIS", "ERRAI", "ALDERAMIN", "DENEB", "VEGA"]

# --- projection ---------------------------------------------------------

CX, CY = 240.0, 262.0     # chart centre = north ecliptic pole
LIMIT = 32.0              # deg from ecliptic pole shown
RAD = 150.0               # SVG units for LIMIT
SCALE = RAD / LIMIT       # units per degree


def project(lon, lat):
    """Ecliptic (lon, lat) -> SVG (x, y), azimuthal equidistant about the NEP.

    Longitude increases anticlockwise on the page: this is the standard
    north-polar convention, so the chart matches the sky when held overhead
    and looked up at.
    """
    r = (90.0 - lat) * SCALE
    th = math.radians(lon - 90.0)
    return CX - r * math.sin(th), CY - r * math.cos(th)


def project_polar(dist_deg, lon):
    """Point at `dist_deg` from the ecliptic pole, at ecliptic longitude."""
    return project(lon, 90.0 - dist_deg)


def mag_radius(m):
    """Engraved dot radius from magnitude. Floor respects 0.4u min feature."""
    return max(0.55, 2.6 - 0.42 * m)


# --- svg helpers (project standard) -------------------------------------

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, a="middle", c="L"):
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{a}" class="{c}">{esc(s)}</text>'


def hr(y, w=0.45, x0=30, x1=450):
    return f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#000" stroke-width="{w}"/>'


def sh(y, txt):
    return t(240, y, f"— {txt} —", "middle", "H")


def line(x1, y1, x2, y2, w=0.8):
    return (f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="#000" stroke-width="{w}"/>')


def circle(cx, cy, r, w=0.8, fill="none", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" '
            f'stroke="#000" stroke-width="{w}"{d}/>')


def dot(cx, cy, r):
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="#000"/>'


# --- build --------------------------------------------------------------

def build():
    o = []
    o.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" '
             'width="480" height="680">')
    o.append("""<style>
text{font-family:Georgia,serif;fill:#000}
.T{font-size:12px;font-weight:bold;letter-spacing:2px}
.S{font-size:7px;letter-spacing:1.5px}
.H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}
.L{font-size:7px}
.Ls{font-size:6px}
.Lx{font-size:5.5px}
.Lb{font-size:6px;font-weight:bold;letter-spacing:1px}
.M{font-size:6px}
.F{font-size:7px;font-style:italic}
.Fb{font-size:7.5px;font-weight:bold}
</style>""")
    o.append('<rect x="6" y="6" width="468" height="668" fill="none" '
             'stroke="#000" stroke-width="3"/>')
    o.append('<rect x="12" y="12" width="456" height="656" fill="none" '
             'stroke="#000" stroke-width="0.75"/>')

    o.append(t(240, 32, "PLATE 12 — THE PRECESSION CLOCK", "middle", "T"))
    o.append(t(240, 50, "HOW LONG AGO THIS WAS BURIED · READ IT FROM THE SKY",
               "middle", "S"))
    o.append(hr(56, 0.5))

    # ---- section 1: the chart ----
    o.append(sh(70, "THE PATH OF THE POLE"))

    # degree rings
    for d in (10, 20, 30):
        o.append(circle(CX, CY, d * SCALE, 0.45, dash="2 3"))
        o.append(t(CX + d * SCALE - 1, CY - 2.5, f"{d}°", "end", "Lx"))
    o.append(circle(CX, CY, LIMIT * SCALE, 0.8))

    # the precession circle: path of the spin pole
    prec_r = OBLIQ * SCALE
    o.append(circle(CX, CY, prec_r, 1.5))

    # ecliptic pole marker (fixed point)
    o.append(line(CX - 5, CY, CX + 5, CY, 1.0))
    o.append(line(CX, CY - 5, CX, CY + 5, 1.0))
    o.append(circle(CX, CY, 2.6, 0.8))
    o.append(t(CX, CY + 13, "THIS POINT DOES NOT MOVE", "middle", "Lx"))

    # rim ticks: 500 yr minor, 2500 yr major, running the full cycle
    n = int(round(PREC_PERIOD / 500.0))
    for i in range(n):
        yr = EPOCH + i * 500.0
        lon = ncp_lon(yr)
        major = (i % 5 == 0)
        r0 = prec_r - (5.0 if major else 2.6)
        r1 = prec_r + (5.0 if major else 2.6)
        ax, ay = project(lon, 90.0 - OBLIQ)
        # radial tick: interpolate along the radius through that point
        ux, uy = (ax - CX) / prec_r, (ay - CY) / prec_r
        o.append(line(CX + ux * r0, CY + uy * r0,
                      CX + ux * r1, CY + uy * r1, 1.0 if major else 0.5))

    # named pole stars on the rim
    lookup = {s[0]: s for s in STARS}
    for name in RIM_MARKS:
        _, ra, dec, _, _, _ = lookup[name]
        lon, lat = eq_to_ecl(ra, dec)
        px, py = project(lon, lat)
        o.append(circle(px, py, 5.0, 0.6, dash="1.5 1.5"))

    # the epoch mark: where the spin pole stood when this plate was made
    elon = ncp_lon(EPOCH)
    ex, ey = project(elon, 90.0 - OBLIQ)
    o.append(circle(ex, ey, 6.5, 1.5))
    o.append(circle(ex, ey, 3.0, 1.0))
    o.append(dot(ex, ey, 1.2))
    ux, uy = (ex - CX) / prec_r, (ey - CY) / prec_r
    o.append(t(ex + ux * 22, ey + uy * 22 - 4,
               "THE POLE STOOD HERE", "middle", "Lb"))
    o.append(t(ex + ux * 22, ey + uy * 22 + 4,
               "WHEN THIS WAS MADE", "middle", "Lb"))

    # direction-of-travel arrow, 900 yr ahead of epoch
    a1 = ncp_lon(EPOCH + 700)
    a2 = ncp_lon(EPOCH + 1100)
    x1, y1 = project(a1, 90.0 - OBLIQ)
    x2, y2 = project(a2, 90.0 - OBLIQ)
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (2.6, -2.6):
        o.append(line(x2, y2,
                      x2 - 6 * math.cos(ang) + s * math.sin(ang),
                      y2 - 6 * math.sin(ang) - s * math.cos(ang), 1.0))
    o.append(line(x1, y1, x2, y2, 1.4))

    # stars
    for name, ra, dec, mag, anchor, dy in STARS:
        lon, lat = eq_to_ecl(ra, dec)
        if (90.0 - lat) > LIMIT:
            continue
        px, py = project(lon, lat)
        o.append(dot(px, py, mag_radius(mag)))
        dx = 5.0 if anchor == "e" else -5.0
        o.append(t(px + dx, py + 2.0 + dy, name,
                   "start" if anchor == "e" else "end", "Lx"))

    # ---- section 2: the fine scale ----
    o.append(sh(432, "THE FINE SCALE — ONE MARK IS ONE HUNDRED YEARS"))

    sx0, sx1, sy = 60.0, 420.0, 458.0
    span_yr = 3000.0
    o.append(line(sx0, sy, sx1, sy, 1.2))
    for i in range(int(span_yr // 100) + 1):
        x = sx0 + (sx1 - sx0) * (i * 100.0) / span_yr
        major = (i % 5 == 0)
        o.append(line(x, sy, x, sy + (7.0 if major else 3.5),
                      1.0 if major else 0.5))
        if major:
            arc = i * 100.0 * POLE_ARC_RATE
            o.append(t(x, sy + 15, f"{arc:.1f}°", "middle", "Lx"))
    o.append(circle(sx0, sy, 4.5, 1.2))
    o.append(t(sx0, sy - 9, "MADE", "middle", "Lb"))
    o.append(t(sx1, sy - 9, "3000 YEARS LATER", "end", "Lb"))
    o.append(t(240, sy + 26,
               "MEASURE THE GAP BETWEEN THE RING-AND-DOT MARK AND THE POLE "
               "YOU SEE. READ THE YEARS BELOW IT.", "middle", "Ls"))

    # ---- section 3: procedure ----
    o.append(sh(500, "HOW TO READ IT"))
    steps = [
        "1.  AT NIGHT, FIND THE POINT THE STARS TURN AROUND. THAT IS YOUR POLE. "
        "IT DOES NOT RISE OR SET.",
        "2.  FIND THE RING-AND-DOT MARK ON THE CIRCLE ABOVE. THAT IS WHERE YOUR "
        "POLE STOOD WHEN THIS PLATE WAS MADE.",
        "3.  MEASURE THE ANGLE BETWEEN THE TWO. A STICK HELD AT ARM'S LENGTH, A "
        "HAND'S BREADTH, ANY FIXED MEASURE WILL DO.",
        "4.  THE POLE TRAVELS THIS CIRCLE AT ONE PART IN 25,772 EACH YEAR. THE "
        "SCALE ABOVE CONVERTS YOUR ANGLE TO YEARS.",
        "5.  IF THE MARK AND YOUR POLE AGREE, LITTLE TIME HAS PASSED. IF THEY "
        "STAND FAR APART, MUCH HAS.",
    ]
    y = 514
    for s in steps:
        o.append(t(30, y, s, "start", "Ls"))
        y += 11.5
    o.append(t(30, y + 2,
               "A YEAR IS ONE RETURN OF THE SUN TO THE SAME PLACE AMONG THE "
               "STARS. THE CIRCLE CLOSES AND BEGINS AGAIN — IF THE STARS "
               "DISAGREE WITH THE MARK BY", "start", "Lx"))
    o.append(t(30, y + 10,
               "MORE THAN THE WHOLE SCALE, ONE FULL TURN OF 25,772 YEARS MAY "
               "HAVE PASSED. THE NAMED STARS ON THE RIM TELL YOU WHICH TURN.",
               "start", "Lx"))

    # ---- footer ----
    o.append(hr(606, 0.5))
    o.append(t(240, 616,
               "NORTH ECLIPTIC POLE AT CENTRE · AZIMUTHAL EQUIDISTANT · "
               "STAR POSITIONS J2000 · OBLIQUITY 23.4393° · "
               f"PRECESSION 50.2877\"/YR · EPOCH {EPOCH}", "middle", "M"))
    o.append(t(240, 626,
               "TITANIUM GRADE 2 · STAR DOTS ENGRAVED AS PITS, DEPTH BY "
               "BRIGHTNESS · CC BY-SA 4.0 · REMEMBERFORWARD.ORG",
               "middle", "M"))
    o.append(t(240, 648,
               "THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY "
               "PEOPLE WHO REMEMBERED FORWARD.", "middle", "Fb"))
    o.append(t(240, 663,
               "BUY IT · BUILD IT · BURY IT · FOR SOMEONE YOU WILL NEVER MEET",
               "middle", "F"))
    o.append("</svg>")
    return "\n".join(o)


def verify():
    """Self-check the astronomy against known facts before trusting the chart."""
    print("--- verification ---")
    print(f"precession period      {PREC_PERIOD:,.0f} yr   (expect ~25,772)")
    print(f"pole motion across sky {POLE_ARC_RATE*100:.3f} deg/century "
          f"(expect ~0.556)")

    def pole_gap(name, year):
        _, ra, dec, _, _, _ = {s[0]: s for s in STARS}[name]
        sl, sb = eq_to_ecl(ra, dec)
        return sep(sl, sb, ncp_lon(year), 90.0 - OBLIQ)

    print(f"Polaris to pole, {EPOCH}   {pole_gap('POLARIS', EPOCH):.2f} deg "
          f"(expect ~0.65)")
    print(f"Polaris to pole, 2100  {pole_gap('POLARIS', 2100):.2f} deg "
          f"(expect ~0.45, closest)")
    print(f"Polaris to pole, 3000  {pole_gap('POLARIS', 3000):.2f} deg "
          f"(expect ~5.2)")
    print(f"Polaris to pole, 4026  {pole_gap('POLARIS', 4026):.2f} deg "
          f"(expect ~10.8)")
    print(f"Thuban  to pole, -2700 {pole_gap('THUBAN', -2700):.2f} deg "
          f"(expect ~1, pole star of the pyramids)")
    print(f"Vega    to pole, 13700 {pole_gap('VEGA', 13700):.2f} deg "
          f"(expect ~4.8, never closer)")
    print(f"Errai   to pole, 4000  {pole_gap('ERRAI', 4000):.2f} deg "
          f"(expect ~3, takes over from Polaris)")

    print("\n--- dating resolution ---")
    for err in (0.2, 0.5, 1.0, 2.0):
        print(f"  measure pole to +/-{err:>4.1f} deg  ->  "
              f"+/-{err/POLE_ARC_RATE:>5.0f} years")

    print("\n--- latitude error from trusting Polaris as the pole ---")
    for yr in (2026, 2200, 2500, 3000, 4026):
        g = pole_gap("POLARIS", yr)
        print(f"  {yr:>5}   {g:>5.2f} deg   {g*111:>6.0f} km")


if __name__ == "__main__":
    verify()
    svg = build()
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "plate12_precession_clock.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"\nwrote {path}  ({len(svg):,} bytes)")
