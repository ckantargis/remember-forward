"""
FOUNDER'S KIT — TEST COUPON, two faces on one 120x170 mm part.

One physical part, two jobs, one engraving order:

  FACE A — resolves governance_series_scope.md §6, the diminished-figure
           vocabulary, which has blocked 05A-05H since 2026-04-17. Three
           candidate ways of saying "this sequence ended badly", tested blind
           on someone who has never seen the system.

  FACE B — proves the process before the run: minimum feature size, minimum
           gap, stroke ladder, type ladder, the five §4 grammar devices at
           actual size, and front-to-back registration.

Face B is also the RFQ specimen, so the engraving quote comes back against real
geometry instead of a description. Engraving is ~55% of COGS and the whole
$905 midpoint rides on an unquoted $15-35/face.

WHY THE TEST IS BLIND
  The 2026-04-17 review found the sick figure read as "stretching" and the
  crouching figure read as "a hand". A test that tells the tester what to look
  for cannot detect that failure. So Face A carries no labels, no captions and
  no answer key, and the good sequence is not always the top row.

  THE VESSEL IS HELD CONSTANT ON PURPOSE.
  In v1 the vessel emptied in every "bad" row, which meant it carried the signal
  in parallel with the figures. A tester scoring 3/3 would have proved only that
  they can see a vessel empty. Section 6 asks whether the FIGURE vocabulary
  reads, so the vessel is now full in every panel of every block and the figures
  are the only thing that varies. The full/empty vessel is a separate section-4
  device and is not what is in question here.

  ANSWER KEY (printed by this script; NOT engraved on the part):
      Block 1  bad = BOTTOM row
      Block 2  bad = TOP row
      Block 3  bad = BOTTOM row

Geometry: viewBox 480x680 = 120x170 mm. 1 unit = 0.25 mm.
"""
W, H = 480, 680
MIN_SW = 0.4                      # 0.10 mm engraving floor
U = 0.25                          # mm per unit

out = []
a = out.append


# ----------------------------------------------------------------- primitives
def t(x, y, s, anchor="middle", cls="L"):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    a(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{s}</text>')


def rect(x, y, w, h, sw=0.8, fill="none"):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
      f'stroke="#000" stroke-width="{max(sw, MIN_SW)}"/>')


def line(x1, y1, x2, y2, sw=0.8):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" '
      f'stroke-width="{max(sw, MIN_SW)}"/>')


def circle(cx, cy, r, sw=0.8, fill="none"):
    st = f' stroke="#000" stroke-width="{max(sw, MIN_SW)}"' if sw else ""
    a(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>')


def poly(pts, fill="#000", sw=0):
    p = " ".join(f"{x},{y}" for x, y in pts)
    st = f' stroke="#000" stroke-width="{max(sw, MIN_SW)}"' if sw else ""
    a(f'<polygon points="{p}" fill="{fill}"{st}/>')


def arrow(x0, x1, y, sw=1.0, head=3.6):
    line(x0, y, x1, y, sw)
    d = 1 if x1 > x0 else -1
    poly([(x1, y), (x1 - d * head, y - head * .55), (x1 - d * head, y + head * .55)])


def head(y, txt):
    t(W / 2, y, f"— {txt} —", cls="H")


def borders_and_style(subtitle):
    # Physical size MUST be declared in mm. Unitless width/height are CSS pixels,
    # which any tool reads at 96 dpi = 127 x 180 mm, not the 120 x 170 mm this
    # project specifies. Caught 2026-09-01 when the DXF came back 5.83% oversize.
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="120mm" height="170mm">')
    a('<rect width="100%" height="100%" fill="#fff"/>')
    a("""<style>
.L{font:7px Georgia,serif}.Ls{font:6px Georgia,serif}.Lx{font:5.5px Georgia,serif}
.Lm{font:5px Georgia,serif}.H{font:bold 6.5px Georgia,serif;letter-spacing:2.5px}
.T{font:bold 12px Georgia,serif;letter-spacing:2px}.S{font:7px Georgia,serif;letter-spacing:1.5px}
.M{font:6px Georgia,serif}.F{font:italic 7px Georgia,serif}.Fb{font:bold 7.5px Georgia,serif}
.B{font:bold 7px Georgia,serif}
text{fill:#000}</style>""")
    rect(6, 6, 468, 668, 3)
    rect(12, 12, 456, 656, 0.75)
    t(W / 2, 32, "REMEMBER FORWARD — TEST COUPON", cls="T")
    t(W / 2, 50, subtitle, cls="S")


def footer(line1):
    t(W / 2, 630, line1, cls="M")
    t(W / 2, 648, "NOT A KNOWLEDGE PLATE. THIS IS A TEST INSTRUMENT.", cls="Fb")
    t(W / 2, 663, "REMEMBER FORWARD · rememberforward.org · CC BY-SA 4.0", cls="F")
    a("</svg>")


# ----------------------------------------------------------------- figures
def fig(cx, top, h, state="up"):
    """Small ISOTYPE figure. state: up | stoop."""
    hr = h * .105
    circle(cx, top + hr, hr, 0, fill="#000")
    sy = top + hr * 2.3
    hy = sy + h * .30
    sw_, hw = h * .14, h * .11
    if state == "stoop":
        # Bent at the waist, head dropped to roughly chest height, knees flexed.
        # Must fail the silhouette test as an UPRIGHT figure - the whole outline
        # has to change, not a face or a detail. Posture gets a fair trial here;
        # if it still loses to group-count, that result means something.
        hr2 = h * .115
        circle(cx + h * .17, top + h * .30, hr2, 0, fill="#000")          # head, forward + low
        poly([(cx + h * .20, top + h * .27), (cx + h * .24, top + h * .40),
              (cx - h * .06, top + h * .56), (cx - h * .13, top + h * .44)])   # pitched torso
        poly([(cx + h * .19, top + h * .40), (cx + h * .25, top + h * .43),
              (cx + h * .20, top + h * .70), (cx + h * .13, top + h * .68)])   # hanging arm
        for s in (-1, 1):                                                  # flexed legs
            poly([(cx - h * .12 + s * h * .05, top + h * .52),
                  (cx - h * .04 + s * h * .05, top + h * .55),
                  (cx + h * .02 + s * h * .05, top + h * .80),
                  (cx - h * .05 + s * h * .05, top + h * .80)])
            poly([(cx - h * .05 + s * h * .05, top + h * .78),
                  (cx + h * .02 + s * h * .05, top + h * .78),
                  (cx + h * .01 + s * h * .05, top + h),
                  (cx - h * .07 + s * h * .05, top + h)])
        return
    poly([(cx - sw_, sy), (cx + sw_, sy), (cx + hw, hy), (cx - hw, hy)])
    for s in (-1, 1):
        poly([(cx + s * sw_, sy), (cx + s * (sw_ - h * .045), sy),
              (cx + s * (sw_ - h * .02), hy + h * .09), (cx + s * (sw_ + h * .05), hy + h * .09)])
    for s in (-1, 1):
        poly([(cx + s * hw * .9, hy), (cx + s * (hw * .9 - h * .055), hy),
              (cx + s * (hw * .5 - h * .055), top + h), (cx + s * hw * .58, top + h)])


def row_of_figures(cx, cy, n, h=19, state="up", span=86):
    """n figures evenly spaced, centred on cx."""
    if n <= 0:
        return
    step = span / max(n - 1, 1) if n > 1 else 0
    x0 = cx - (span / 2 if n > 1 else 0)
    for i in range(n):
        fig(x0 + i * step, cy, h, state)


def vessel(cx, cy, w, h_, full=True):
    poly([(cx - w / 2, cy), (cx + w / 2, cy), (cx + w * .40, cy + h_), (cx - w * .40, cy + h_)],
         fill="none", sw=1.0)
    line(cx - w / 2, cy, cx + w / 2, cy, 1.0)
    if full:
        for r in range(2):
            y = cy + h_ * .32 + r * 3.0
            seg, d = w * .58 / 6, ""
            x = cx - w * .29
            d += f"M {x} {y}"
            for i in range(6):
                d += f" q {seg/2} {-1.8 if i%2==0 else 1.8} {seg} 0"
            a(f'<path d="{d}" fill="none" stroke="#000" stroke-width="0.7"/>')


# ═══════════════════════════════════════════════════════ FACE A — VOCABULARY
def face_a():
    out.clear()
    borders_and_style("FACE A  ·  WHICH SEQUENCE ENDED BADLY?")

    t(W / 2, 70, "Each block below has two rows. Read each row left to right.",
      cls="Ls")
    t(W / 2, 80, "In every block, ONE row ends well and ONE ends badly.", cls="Ls")
    t(W / 2, 90, "Mark the box beside the row you think ended BADLY. Do not ask questions.",
      cls="Ls")
    line(60, 96, 420, 96, 0.5)

    # each block: (label, y, good_row, mode)  good_row 0=top 1=bottom
    blocks = [("1", 114, 0, "count"),
              ("2", 258, 1, "posture"),
              ("3", 402, 0, "both")]

    for label, y0, good_row, mode in blocks:
        t(34, y0 - 4, f"BLOCK {label}", anchor="start", cls="B")
        for r in (0, 1):
            ry = y0 + r * 62
            good = (r == good_row)
            # response box on the LEFT, clear of the panels. It sat at x=440 in v1,
            # which is inside the third panel - it overlapped the artwork.
            rect(28, ry + 21, 12, 12, 0.8)
            for p in range(3):
                px = 50 + p * 130
                rect(px, ry, 118, 54, 0.8)
                if p < 2:
                    arrow(px + 120, px + 128, ry + 27)
                if mode == "count":
                    n = 9 if (good or p == 0) else (9 if p == 0 else 6 if p == 1 else 4)
                    row_of_figures(px + 59, ry + 8, n, h=17, span=88)
                    vessel(px + 59, ry + 34, 26, 15, full=True)   # held constant - see note
                elif mode == "posture":
                    st = "up" if (good or p == 0) else ("up" if p == 0 else "stoop")
                    row_of_figures(px + 59, ry + 8, 6, h=19, span=74, state=st)
                    vessel(px + 59, ry + 34, 26, 15, full=True)   # held constant - see note
                else:
                    n = 9 if (good or p == 0) else (9 if p == 0 else 6 if p == 1 else 4)
                    st = "up" if (good or p < 2) else "stoop"
                    row_of_figures(px + 59, ry + 8, n, h=17, span=88, state=st)
                    vessel(px + 59, ry + 34, 26, 15, full=True)   # held constant - see note
        line(28, y0 + 128, 440, y0 + 128, 0.3)

    t(W / 2, 545, "Tester: ____________________   Date: __________   "
                  "Has seen these plates before?  Y / N", cls="Lx")
    t(W / 2, 558, "If a block is unreadable either way, mark BOTH boxes. That is a valid result "
                  "and the most useful one.", cls="Lm")
    t(W / 2, 572, "Blocks differ only in HOW the ending is shown. Do not tell the tester that.",
      cls="Lm")

    footer("COUPON FACE A · governance_series_scope.md §6 · 120×170 mm · v1")
    open("plate_coupon_a_vocabulary.svg", "w", encoding="utf-8").write("\n".join(out))
    print("  wrote plate_coupon_a_vocabulary.svg")


# ═══════════════════════════════════════════════════════ FACE B — ENGRAVING
def face_b():
    out.clear()
    borders_and_style("FACE B  ·  PROCESS PROOF & RFQ SPECIMEN")

    # ---- registration: corners + centre
    for cx, cy in [(34, 74), (446, 74), (34, 600), (446, 600), (240, 337)]:
        line(cx - 9, cy, cx + 9, cy, 0.6)
        line(cx, cy - 9, cx, cy + 9, 0.6)
        circle(cx, cy, 6, 0.6)
    t(240, 352, "REGISTRATION — front and back marks must coincide within 0.15 mm",
      cls="Lm")

    # ---- 1 stroke-width ladder
    head(96, "MINIMUM STROKE")
    widths = [0.4, 0.5, 0.6, 0.8, 1.0, 1.4, 2.0]
    for i, sw in enumerate(widths):
        y = 108 + i * 11
        line(60, y, 300, y, sw)
        t(310, y + 2, f"{sw:.1f} u = {sw*U:.3f} mm", anchor="start", cls="Lm")
    t(240, 194, "Report the finest line that engraves cleanly and consistently.", cls="Lm")

    # ---- 2 gap / clearance ladder
    head(212, "MINIMUM GAP BETWEEN FEATURES")
    for i, gap in enumerate([0.4, 0.6, 0.8, 1.2, 1.6, 2.4]):
        x = 62 + i * 66
        for k in range(4):
            line(x + k * (gap + 0.8), 224, x + k * (gap + 0.8), 258, 0.8)
        t(x + 10, 268, f"{gap*U:.2f} mm", cls="Lm")
    t(240, 280, "Report the smallest gap that does not bridge or burn through.", cls="Lm")

    # ---- 3 dot ladder
    head(292, "SMALLEST RESOLVED DOT")
    for i, r in enumerate([0.2, 0.3, 0.4, 0.6, 0.8, 1.2, 1.6]):
        x = 70 + i * 55
        circle(x, 304, r, 0, fill="#000")
        t(x, 317, f"{r*2*U:.2f}", cls="Lm")

    # ---- 4 type ladder
    head(378, "TYPE LADDER — smallest legible size")
    samples = [("Lm", 5, "1.25"), ("Lx", 5.5, "1.38"), ("Ls", 6, "1.50"),
               ("L", 7, "1.75"), ("B", 7, "1.75 bold")]
    for i, (cls, px, mm) in enumerate(samples):
        y = 392 + i * 13
        t(60, y, "The quick brown fox jumps over the lazy dog 0123456789",
          anchor="start", cls=cls)
        t(420, y, f"{px}px = {mm} mm", anchor="end", cls="Lm")

    # ---- 5 the five §4 grammar devices at actual size
    head(470, "§4 GRAMMAR DEVICES AT ACTUAL SIZE")
    # circle of equal figures
    import math
    for i in range(8):
        ang = -math.pi / 2 + i * math.pi / 4
        fig(80 + 34 * math.cos(ang), 496 + 26 * math.sin(ang) - 9, 15)
    t(78, 542, "circle of equals", cls="Lm")
    # raised figure
    line(150, 522, 200, 522, 0.8)
    rect(166, 508, 18, 14, 0.8)
    fig(175, 486, 20)
    fig(157, 506, 16); fig(193, 506, 16)
    t(175, 542, "raised figure", cls="Lm")
    # passed staff
    for i in range(5):
        fig(228 + i * 15, 492, 16)
    line(228, 484, 228, 500, 1.0)
    line(273, 484, 273, 500, 1.0)
    t(250, 542, "passed staff", cls="Lm")
    # radiating head-lines
    fig(330, 492, 20)
    for k in range(5):
        ang = -math.pi / 2 + (k - 2) * 0.42
        line(330 + 5 * math.cos(ang), 494 + 5 * math.sin(ang),
             330 + 13 * math.cos(ang), 494 + 13 * math.sin(ang), 0.6)
    t(330, 542, "is heard", cls="Lm")
    # full vs empty
    vessel(398, 490, 26, 16, full=True)
    vessel(432, 490, 26, 16, full=False)
    t(415, 542, "full / empty", cls="Lm")

    # ---- 6 solid fill + hatch
    head(560, "FILL & HATCH")
    rect(62, 570, 40, 22, 0, fill="#000")
    t(82, 600, "solid", cls="Lm")
    for i, pitch in enumerate([1.2, 1.8, 2.6, 4.0]):
        x0 = 122 + i * 62
        n = int(38 / pitch)
        for k in range(n):
            line(x0 + k * pitch, 570, x0 + k * pitch, 592, 0.4)
        t(x0 + 19, 600, f"{pitch*U:.2f} mm", cls="Lm")

    footer("COUPON FACE B · process proof · Ti Gr2 0.8 mm · ablated grooves · v1")
    open("plate_coupon_b_engraving.svg", "w", encoding="utf-8").write("\n".join(out))
    print("  wrote plate_coupon_b_engraving.svg")


if __name__ == "__main__":
    face_a()
    face_b()
    print("\n  ANSWER KEY (do NOT show the tester, not engraved on the part):")
    print("    Block 1 (group-count only) : bad = BOTTOM row")
    print("    Block 2 (posture only)     : bad = TOP row")
    print("    Block 3 (count + posture)  : bad = BOTTOM row")
