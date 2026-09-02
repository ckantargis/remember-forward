"""
PLATE A01 - HOW TO READ THESE PLATES
The bootstrap plate. Replaces plate00 as the master key.

THE PROBLEM THIS PLATE SOLVES
  It must teach the callout grammar without being able to use the callout grammar.
  Everything on it has to be recoverable by a finder who shares no language, no
  culture and no convention with us.

THE THREE ESCAPES FROM THE BOOTSTRAP TRAP
  1. THE BODY. The only referent every human finder is holding while they read.
     Callouts land on a person's own parts, so the number-to-thing mapping is
     inferable without knowing what a callout is.
  2. GRAVITY. Reading order is taught by a falling stone. Read the panels the
     wrong way and the stone rises off the ground, which is absurd. The sequence
     teaches its own direction - we never have to assert "left to right".
  3. COUNTING. Dot-bar numerals are taught by direct correspondence against
     counted objects. Counting is pre-linguistic, so this is non-circular.

CONSEQUENCE IS SHOWN, NEVER SYMBOLISED. No tick, no cross, no circle-slash,
no skull. Two rows start the same, diverge at one action, and end differently.
The outcome IS the judgement.

Output: plateA01_how_to_read.svg   (480x680 viewBox = 120x170 mm)
"""

W, H = 480, 680
MIN_SW = 0.4          # metal engraving floor: 0.4 SVG units = 0.10 mm at 120x170
out = []
a = out.append


# ----------------------------------------------------------------- primitives
def t(x, y, s, anchor="middle", cls="L"):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    a(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{s}</text>')


def rect(x, y, w, h, sw=0.8, fill="none"):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#000" stroke-width="{max(sw, MIN_SW)}"/>')


def line(x1, y1, x2, y2, sw=0.8):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="{max(sw, MIN_SW)}"/>')


def circle(cx, cy, r, sw=0.8, fill="none"):
    st = f' stroke="#000" stroke-width="{max(sw, MIN_SW)}"' if sw else ""
    a(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>')


def poly(pts, fill="#000", sw=0):
    p = " ".join(f"{x},{y}" for x, y in pts)
    st = f' stroke="#000" stroke-width="{max(sw, MIN_SW)}"' if sw else ""
    a(f'<polygon points="{p}" fill="{fill}"{st}/>')


def sh(y, txt):
    """Section header: em-dash bullet em-dash, per house style."""
    t(W / 2, y, f"— {txt} —", cls="H")


def arrow(x0, x1, y, sw=1.2, head=4.5):
    """Horizontal arrow, x0 -> x1."""
    line(x0, y, x1, y, sw)
    d = 1 if x1 > x0 else -1
    poly([(x1, y), (x1 - d * head, y - head * 0.55), (x1 - d * head, y + head * 0.55)])


# ----------------------------------------------------------------- mayan number
def numeral(cx, cy, n, s=3.0):
    """Mayan dot-bar numeral 0-19, centred on (cx, cy). s = unit scale."""
    if n == 0:                                    # shell glyph for zero
        a(f'<ellipse cx="{cx}" cy="{cy}" rx="{s*2.1}" ry="{s*1.3}" fill="none" stroke="#000" stroke-width="0.8"/>')
        line(cx - s * 1.1, cy + s * .2, cx - s * .4, cy + s * .2, 0.6)
        line(cx + s * .4, cy + s * .2, cx + s * 1.1, cy + s * .2, 0.6)
        return
    bars, dots = divmod(n, 5)
    rows = bars + (1 if dots else 0)
    total_h = rows * s * 1.9 - s * 0.5
    y = cy - total_h / 2 + s * 0.5
    if dots:                                      # dots sit above the bars
        span = (dots - 1) * s * 2.2
        for i in range(dots):
            a(f'<circle cx="{cx - span/2 + i*s*2.2}" cy="{y}" r="{s*0.75}" fill="#000"/>')
        y += s * 1.9
    for _ in range(bars):
        a(f'<rect x="{cx - s*3.1}" y="{y - s*0.42}" width="{s*6.2}" height="{s*0.84}" fill="#000"/>')
        y += s * 1.9


def callout(cx, cy, n, r=7.2):
    """A numbered callout bubble - the convention this whole plate exists to teach."""
    circle(cx, cy, r, 1.0, fill="#fff")
    numeral(cx, cy, n, s=1.75)


def leader(x0, y0, x1, y1, r=7.2):
    """Leader line stopping at the callout bubble's edge."""
    import math
    d = math.hypot(x1 - x0, y1 - y0) or 1
    line(x0, y0, x1 - (x1 - x0) / d * r, y1 - (y1 - y0) / d * r, 0.55)


# ----------------------------------------------------------------- isotype body
def figure(cx, top, h, pose="stand"):
    """ISOTYPE silhouette. Must read as an unambiguous black blob."""
    hr = h * 0.098
    circle(cx, top + hr, hr, 0, fill="#000")
    sy = top + hr * 2.35                                  # shoulder line
    hy = sy + h * 0.30                                    # hip line
    sw_, hw = h * 0.135, h * 0.105                        # shoulder / hip half-width
    poly([(cx - sw_, sy), (cx + sw_, sy), (cx + hw, hy), (cx - hw, hy)])

    aw = h * 0.042
    if pose == "drink":                                   # forearm up to the mouth
        poly([(cx + sw_ - aw, sy), (cx + sw_, sy), (cx + h * .17, top + hr * 1.55),
              (cx + h * .13, top + hr * 2.15)])
        poly([(cx - sw_, sy), (cx - sw_ + aw, sy), (cx - sw_ + aw * 1.4, hy + h * .10),
              (cx - sw_ + aw * .3, hy + h * .10)])
    elif pose == "point":                                 # one arm out, pointing
        poly([(cx + sw_ - aw, sy + h * .01), (cx + sw_, sy),
              (cx + sw_ + h * .17, sy + h * .01), (cx + sw_ + h * .17, sy + h * .05)])
        poly([(cx - sw_, sy), (cx - sw_ + aw, sy), (cx - sw_ + aw * 1.4, hy + h * .10),
              (cx - sw_ + aw * .3, hy + h * .10)])
    else:                                                 # arms at sides
        for s in (-1, 1):
            poly([(cx + s * sw_, sy), (cx + s * (sw_ - aw), sy),
                  (cx + s * (sw_ - aw * .4), hy + h * .10), (cx + s * (sw_ + aw * .6), hy + h * .10)])

    lw = h * 0.052
    for s in (-1, 1):                                     # legs
        poly([(cx + s * hw * .92, hy), (cx + s * (hw * .92 - lw), hy),
              (cx + s * (hw * .55 - lw), top + h), (cx + s * hw * .62, top + h)])


def figure_lying(cx, ground_y, h):
    """A body on the ground. Drawn HORIZONTAL because a collapsed vertical figure
    fails the silhouette test - it reads as a standing person in a skirt."""
    L = h * 0.95
    hr = h * 0.115
    line(cx - L * .62, ground_y, cx + L * .62, ground_y, 1.0)       # the ground
    circle(cx - L * .40, ground_y - hr, hr, 0, fill="#000")          # head
    poly([(cx - L * .28, ground_y - hr * 1.7), (cx + L * .10, ground_y - hr * 1.35),
          (cx + L * .10, ground_y - hr * .15), (cx - L * .28, ground_y - hr * .15)])
    poly([(cx + L * .06, ground_y - hr * 1.15), (cx + L * .44, ground_y - hr * .95),
          (cx + L * .44, ground_y - hr * .15), (cx + L * .06, ground_y - hr * .15)])
    poly([(cx - L * .24, ground_y - hr * 1.6), (cx - L * .02, ground_y - hr * 2.5),
          (cx + L * .04, ground_y - hr * 2.1), (cx - L * .18, ground_y - hr * 1.25)])


def hand(cx, cy, s=1.0, flip=False):
    """Open hand, palm out. Fingers must stay separate at 0.1 mm feature size."""
    f = -1 if flip else 1
    poly([(cx - 9 * s * f, cy + 2 * s), (cx - 9 * s * f, cy + 11 * s),
          (cx + 9 * s * f, cy + 11 * s), (cx + 9 * s * f, cy + 2 * s)])
    for i, (dx, ln) in enumerate([(-6.6, 10.5), (-2.2, 12.5), (2.2, 12.0), (6.6, 9.5)]):
        poly([(cx + (dx - 1.6) * s * f, cy + 3 * s), (cx + (dx - 1.6) * s * f, cy + 3 * s - ln * s),
              (cx + (dx + 1.6) * s * f, cy + 3 * s - ln * s), (cx + (dx + 1.6) * s * f, cy + 3 * s)])
    poly([(cx + 9 * s * f, cy + 4 * s), (cx + 15.5 * s * f, cy - 1 * s),
          (cx + 17.5 * s * f, cy + 2.5 * s), (cx + 11 * s * f, cy + 8 * s)])


def water(cx, cy, w, rows=3, gap=3.2):
    """Wavy horizontal lines. Highest cross-cultural reliability - never a teardrop."""
    for r in range(rows):
        y = cy + r * gap
        seg, d = w / 6, ""
        x = cx - w / 2
        d += f"M {x} {y}"
        for i in range(6):
            d += f" q {seg/2} {-2.2 if i%2==0 else 2.2} {seg} 0"
        a(f'<path d="{d}" fill="none" stroke="#000" stroke-width="0.75"/>')


def vessel(cx, cy, w, h_, dirty=False):
    """Open pot in side elevation. Water clipped inside the rim, dirt as bold specks -
    at 1.5mm the earlier 0.9u specks vanished entirely."""
    poly([(cx - w / 2, cy), (cx + w / 2, cy), (cx + w * .40, cy + h_), (cx - w * .40, cy + h_)],
         fill="none", sw=1.1)
    line(cx - w / 2, cy, cx + w / 2, cy, 1.1)
    water(cx, cy + h_ * .42, w * .60, rows=2, gap=3.0)
    if dirty:
        for dx, dy in [(-6.5, -1), (0.5, 2), (6.0, 0), (-3.0, 5), (3.5, 6), (-7.5, 4), (7.0, 5)]:
            a(f'<circle cx="{cx+dx}" cy="{cy+h_*.42+dy}" r="1.5" fill="#000"/>')


def hearth(cx, top_y, w):
    """Pot supported over flames. The support stones matter - without them the pot
    floats and the picture stops meaning 'heat this'."""
    for s_ in (-1, 1):
        poly([(cx + s_ * w * .46, top_y), (cx + s_ * w * .60, top_y),
              (cx + s_ * w * .56, top_y + 15), (cx + s_ * w * .40, top_y + 15)],
             fill="none", sw=0.9)
    for i, dx in enumerate((-7, 0, 7)):
        flame(cx + dx, top_y + 15, 1.0 if i == 1 else 0.75)
    line(cx - w * .62, top_y + 15, cx + w * .62, top_y + 15, 1.0)


def flame(cx, cy, s=1.0):
    a(f'<path d="M {cx} {cy} C {cx-4*s} {cy-4*s} {cx-3*s} {cy-9*s} {cx} {cy-13*s} '
      f'C {cx+3.4*s} {cy-9*s} {cx+4*s} {cy-4*s} {cx} {cy} Z" fill="#000"/>')
    a(f'<path d="M {cx} {cy-1*s} C {cx-2*s} {cy-3.4*s} {cx-1.5*s} {cy-6*s} {cx} {cy-8.4*s} '
      f'C {cx+1.7*s} {cy-6*s} {cx+2*s} {cy-3.4*s} {cx} {cy-1*s} Z" fill="#fff"/>')


# ================================================================= DOCUMENT
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="120mm" height="170mm">')
a('<rect width="100%" height="100%" fill="#fff"/>')
a("""<style>
.L{font:7px Georgia,serif}.Ls{font:6px Georgia,serif}.Lx{font:5.5px Georgia,serif}
.H{font:bold 6.5px Georgia,serif;letter-spacing:2.5px}
.T{font:bold 12px Georgia,serif;letter-spacing:2px}
.S{font:7px Georgia,serif;letter-spacing:1.5px}
.M{font:6px Georgia,serif}.F{font:italic 7px Georgia,serif}.Fb{font:bold 7.5px Georgia,serif}
.K{font:bold 7px Georgia,serif}.Ka{font:6.5px Georgia,serif}
text{fill:#000}
</style>""")

# borders (house spec)
rect(6, 6, 468, 668, 3)
rect(12, 12, 456, 656, 0.75)

t(W / 2, 32, "HOW TO READ THESE PLATES", cls="T")
t(W / 2, 50, "A01  ·  THE KEY TO EVERY OTHER PLATE", cls="S")

# ----------------------------------------------------------------- 1 CALLOUT
sh(66, "A NUMBER MARKS A THING")
figure(96, 76, 82, pose="point")
for n, (px, py), (bx, by) in [
    (1, (96, 84), (52, 82)),      # head
    (2, (96, 112), (52, 108)),    # body
    (3, (124, 100), (152, 92)),   # hand
    (4, (86, 152), (52, 150)),    # foot
]:
    leader(px, py, bx, by)
    callout(bx, by, n)

# the margin strip - this is the part that gets re-etched per language
rect(176, 74, 118, 86, 0.8)
t(235, 84, "WORDS", cls="K")
line(182, 88, 288, 88, 0.4)
for i, (n, word) in enumerate([(1, "HEAD"), (2, "BODY"), (3, "HAND"), (4, "FOOT")]):
    y = 100 + i * 15
    callout(190, y - 2.5, n, r=6.0)
    t(203, y, word, anchor="start", cls="L")
    line(203, y + 2.5, 288, y + 2.5, 0.25)
t(235, 155, "[ SECOND LANGUAGE STRIP ]", cls="Lx")

rect(302, 74, 160, 86, 0.8)
t(382, 86, "The mark on the picture", cls="Ls")
t(382, 95, "and the mark beside the word", cls="Ls")
t(382, 104, "are the same mark.", cls="Ls")
line(316, 111, 448, 111, 0.4)
t(382, 122, "You are holding the thing", cls="Ls")
t(382, 131, "each of these four words", cls="Ls")
t(382, 140, "names. Look at your own", cls="Ls")
t(382, 149, "body and the words follow.", cls="Ls")

# ----------------------------------------------------------------- 2 NUMBER
sh(178, "HOW THE NUMBERS ARE WRITTEN")
for i, n in enumerate([1, 2, 3, 4, 5]):
    x = 44 + i * 52
    numeral(x, 196, n, s=2.6)
    for k in range(n):                                    # counted stones beneath
        a(f'<circle cx="{x - (n-1)*3.4 + k*6.8}" cy="212" r="2.2" fill="none" stroke="#000" stroke-width="0.7"/>')
for i, n in enumerate([10, 19, 0]):
    x = 322 + i * 56
    numeral(x, 194, n, s=2.6)
    for k in range(n):                                    # stones, in rows of five
        row, col = divmod(k, 5)
        a(f'<circle cx="{x - 13.6 + col*6.8}" cy="{210 + row*6.2}" r="2.2" '
          f'fill="none" stroke="#000" stroke-width="0.7"/>')
t(W / 2, 232, "Count the marks against the stones. A line is five. A shell is none.", cls="Ls")
t(W / 2, 242, "Every plate repeats this key in its lower margin.", cls="Lx")

# ----------------------------------------------------------------- 3 SEQUENCE
sh(256, "PICTURES IN A ROW ARE TIME PASSING")
for i in range(3):
    rect(40 + i * 134, 264, 122, 68, 0.9)
# panel 1: stone held high
hand(74, 274, 0.62)
circle(74, 288, 5.0, 0, fill="#000")
# panel 2: mid-fall, motion ticks above
hand(208, 271, 0.62)
for k in range(3):
    line(208, 288 + k * 6, 208, 292 + k * 6, 0.6)
circle(208, 314, 5.0, 0, fill="#000")
# panel 3: on the ground, dust
line(306, 322, 390, 322, 1.0)
circle(348, 316.5, 5.0, 0, fill="#000")
for dx in (-14, -9, 9, 14):
    line(348 + dx, 314, 348 + dx * 1.35, 309, 0.45)
arrow(168, 178, 298)
arrow(302, 312, 298)
t(W / 2, 344, "The stone falls. It cannot fall upward — so you already know which way to read.", cls="Ls")

# ----------------------------------------------------------------- 4 ARROW
sh(362, "AN ARROW MEANS FROM ONE THING TO ANOTHER")
figure(64, 372, 44)
arrow(92, 150, 392, 1.4, 5.5)
figure(178, 372, 44)
t(121, 384, "moves", cls="Lx")
line(240, 370, 240, 414, 0.4)
hand(286, 378, 0.6)
arrow(310, 352, 390, 1.4, 5.5)
circle(410, 390, 8, 1.0)
t(371, 380, "acts on", cls="Lx")
t(W / 2, 420, "A hand shown doing a thing means: this is the thing to do.", cls="Ls")

# ----------------------------------------------------------------- 5 CONSEQUENCE
sh(440, "WHAT FOLLOWS FROM WHAT YOU DO")

# --- row one: drink it as found
for i in range(3):
    rect(40 + i * 134, 448, 122, 72, 0.9)
vessel(101, 466, 42, 30, dirty=True)
t(101, 512, "water as found", cls="Lx")
figure(206, 456, 54, pose="drink")
vessel(224, 462, 22, 15, dirty=True)
t(235, 512, "drink it", cls="Lx")
figure_lying(348, 500, 48)
t(348, 512, "sick", cls="Lx")
arrow(168, 178, 484)
arrow(302, 312, 484)

# --- row two: put it on the fire first
for i in range(3):
    rect(40 + i * 134, 526, 122, 72, 0.9)
vessel(101, 538, 42, 30, dirty=True)
hearth(101, 568, 42)
t(101, 594, "put it on the fire", cls="Lx")
figure(206, 534, 54, pose="drink")
vessel(224, 540, 22, 15, dirty=False)
t(235, 594, "then drink it", cls="Lx")
figure(348, 534, 54)
t(348, 594, "well", cls="Lx")
arrow(168, 178, 562)
arrow(302, 312, 562)

line(24, 606, 456, 606, 0.5)
t(W / 2, 613, "Both rows begin with the same water. They differ at one act, and they end differently.", cls="Ls")

# ----------------------------------------------------------------- footer
t(W / 2, 630, "REMEMBER FORWARD  ·  A01  ·  CC BY-SA 4.0  ·  rememberforward.org", cls="M")
t(W / 2, 648, "THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, "
              "BY PEOPLE WHO REMEMBERED FORWARD.", cls="Fb")
t(W / 2, 663, "BUY IT · BUILD IT · BURY IT · FOR SOMEONE YOU WILL NEVER MEET", cls="F")
a("</svg>")

open("plateA01_how_to_read.svg", "w", encoding="utf-8").write("\n".join(out))
print("wrote plateA01_how_to_read.svg")
