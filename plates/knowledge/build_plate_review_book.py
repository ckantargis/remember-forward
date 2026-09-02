#!/usr/bin/env python3
"""
build_plate_review_book.py  --  Remember Forward

Compiles every CANONICAL knowledge plate into ONE printable document
(knowledge_plates_review.html) for hand review / recreation.

Why HTML instead of a rendered PDF:
  - The browser renders SVG natively and perfectly (pattern fills, live
    text, beziers) -- svglib silently drops plate02's sand/gravel/charcoal
    pattern fills and choked on plate06's path, so a PDF pipeline would
    misrepresent the very plates you're reviewing.
  - Matches the project's build pattern: script -> writes file ->
    os.startfile() auto-opens in the browser. Then File > Print > Save as
    PDF (or print to paper) for the physical review copy.

STANDARD USAGE for all future knowledge plates:
  Add/replace the plate's entry in CANONICAL below (newest version wins),
  then re-run this script. It always emits the full, current review book.

    python plates/knowledge/build_plate_review_book.py

Grid: an on-screen checkbox overlays a 40-unit (12 x 17) grid on every
plate. On the real 12 x 17 cm plate each cell is ~1 cm -- copy cell by
cell. Whatever state is showing when you print is what prints.
"""

import os
import re
import datetime
import html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "..", "review")
OUT_FILE = os.path.join(OUT_DIR, "knowledge_plates_review.html")

# The canonical knowledge set: (svg filename, short label, topic).
# Newest accepted version of each plate only. Edit this list as the
# single source of truth for what belongs in the review book.
CANONICAL = [
    ("plate01_v3_rosetta.svg",             "Plate 1",   "Index / Master Key (Rosetta)"),
    ("plate02_v9_water_filter.svg",        "Plate 2",   "Clean Water · Charcoal Filter"),
    ("plate02a_charcoal_retort.svg",       "Plate 2A",  "Making Charcoal · Retort / Clay-Vessel Method"),
    ("plate03_v2_agriculture_seeds.svg",   "Plate 3",   "Agriculture & Seeds"),
    ("plate04_v2_technology.svg",          "Plate 4",   "Technology Re-foundation"),
    ("plate05_v2_governance.svg",          "Plate 5",   "Governance & Ethics"),
    ("plate06_v2_concords_stars.svg",      "Plate 6",   "The Concords & The Stars"),
    ("plate07_encoding_communication.svg", "Plate 7",   "Encoding & Communication"),
    ("plate08_physics_of_sound_v2.svg",    "Plate 8",   "Physics of Sound"),
    ("plate09_audio_playback_guide.svg",   "Plate 9",   "Audio Playback Guide"),
    ("plate10_electrical_phenomena.svg",   "Plate 10",  "Electrical Phenomena"),
    ("plate11_energy_generation.svg",      "Plate 11",  "Energy Generation"),
]

XML_DECL = re.compile(r"<\?xml[^>]*\?>\s*", re.IGNORECASE)
SVG_OPEN = re.compile(r"<svg\b[^>]*>", re.IGNORECASE)


def prepare_svg(raw: str) -> str:
    """Drop the XML declaration and strip width/height from the root <svg>
    so CSS controls sizing while the viewBox preserves aspect ratio."""
    raw = XML_DECL.sub("", raw).lstrip()
    m = SVG_OPEN.search(raw)
    if m:
        tag = m.group(0)
        tag = re.sub(r'\s+width="[^"]*"', "", tag, flags=re.IGNORECASE)
        tag = re.sub(r'\s+height="[^"]*"', "", tag, flags=re.IGNORECASE)
        raw = raw[:m.start()] + tag + raw[m.end():]
    return raw


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    today = datetime.date.today().isoformat()

    plates, missing = [], []
    for fname, label, topic in CANONICAL:
        path = os.path.join(HERE, fname)
        if not os.path.exists(path):
            missing.append(fname)
            continue
        with open(path, "r", encoding="utf-8") as fh:
            plates.append((label, topic, fname, prepare_svg(fh.read())))

    # --- cover / index page ------------------------------------------------
    index_rows = "\n".join(
        f'<tr><td class="ix-lbl">{_html.escape(l)}</td>'
        f'<td class="ix-top">{_html.escape(t)}</td>'
        f'<td class="ix-file">{_html.escape(f)}</td></tr>'
        for l, t, f in [(p[0], p[1], p[2]) for p in plates]
    )

    pages = []
    pages.append(f"""
    <section class="page cover">
      <h1>Remember Forward</h1>
      <h2>Knowledge Plates &mdash; Review &amp; Hand-Recreation Book</h2>
      <p class="meta">Compiled {today} &middot; {len(plates)} canonical plates &middot; CC BY-SA 4.0</p>
      <table class="index">
        <thead><tr><th>Plate</th><th>Topic</th><th>Source file</th></tr></thead>
        <tbody>{index_rows}</tbody>
      </table>
      <div class="howto">
        <h3>How to use this book</h3>
        <ul>
          <li>One plate per page. Print to paper, or File &rarr; Print &rarr; Save as PDF.</li>
          <li>Tick <strong>Show 1&nbsp;cm grid</strong> (top of screen) before printing to
              overlay a 12&times;17 grid. Each cell is ~1&nbsp;cm on the finished
              12&times;17&nbsp;cm plate &mdash; copy cell by cell.</li>
          <li>Design law for every plate: <em>show every step, assume no viewer,
              pictograph first, text only as Rosetta evidence.</em></li>
        </ul>
      </div>
      {('<p class="warn">Missing (skipped): ' + ', '.join(map(_html.escape, missing)) + '</p>') if missing else ''}
    </section>""")

    GRID_CELL = 40  # 480/12 = 40, 680/17 = 40  ->  12 x 17 cells
    grid_lines = []
    for x in range(0, 481, GRID_CELL):
        grid_lines.append(f'<line x1="{x}" y1="0" x2="{x}" y2="680"/>')
    for y in range(0, 681, GRID_CELL):
        grid_lines.append(f'<line x1="0" y1="{y}" x2="480" y2="{y}"/>')
    grid_svg = (
        '<svg class="grid" viewBox="0 0 480 680" preserveAspectRatio="xMidYMid meet">'
        + "".join(grid_lines) + "</svg>"
    )

    for label, topic, fname, svg in plates:
        pages.append(f"""
    <section class="page plate">
      <header class="plate-head">
        <span class="ph-label">{_html.escape(label)}</span>
        <span class="ph-topic">{_html.escape(topic)}</span>
      </header>
      <div class="stage">
        {svg}
        {grid_svg}
      </div>
      <footer class="plate-foot">{_html.escape(fname)} &middot; Remember Forward &middot; CC BY-SA 4.0</footer>
    </section>""")

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Remember Forward &mdash; Knowledge Plates Review Book</title>
<style>
  :root {{ --ink:#111; }}
  * {{ box-sizing: border-box; }}
  html,body {{ margin:0; background:#555; color:var(--ink); font-family:Georgia,serif; }}
  .toolbar {{
    position:sticky; top:0; z-index:50; background:#222; color:#fff;
    padding:10px 16px; font:14px/1.3 system-ui,sans-serif; display:flex;
    gap:18px; align-items:center;
  }}
  .toolbar label {{ cursor:pointer; user-select:none; }}
  .toolbar .hint {{ opacity:.7; }}

  .page {{
    width:8.5in; min-height:11in; background:#fff; margin:18px auto;
    padding:0.5in; box-shadow:0 2px 14px rgba(0,0,0,.4);
    display:flex; flex-direction:column;
  }}

  /* cover */
  .cover h1 {{ margin:0; font-size:34px; letter-spacing:1px; }}
  .cover h2 {{ margin:.2em 0 0; font-size:17px; font-weight:normal; color:#333; }}
  .cover .meta {{ color:#666; font-size:12px; margin:.4em 0 1.4em; }}
  table.index {{ width:100%; border-collapse:collapse; font-size:12.5px; }}
  table.index th {{ text-align:left; border-bottom:2px solid #111; padding:5px 6px; }}
  table.index td {{ padding:4px 6px; border-bottom:1px solid #ddd; vertical-align:top; }}
  .ix-lbl {{ font-weight:bold; white-space:nowrap; width:16%; }}
  .ix-file {{ font-family:ui-monospace,Consolas,monospace; font-size:10.5px; color:#777; }}
  .howto {{ margin-top:1.6em; border-top:1px solid #ccc; padding-top:1em; font-size:12.5px; }}
  .howto h3 {{ margin:0 0 .5em; font-size:14px; }}
  .howto ul {{ margin:0; padding-left:1.2em; }}
  .howto li {{ margin:.3em 0; }}
  .warn {{ color:#a00; font-size:12px; margin-top:1em; }}

  /* plate pages */
  .plate-head {{
    display:flex; justify-content:space-between; align-items:baseline;
    border-bottom:2px solid #111; padding-bottom:6px; margin-bottom:8px;
    font-family:system-ui,sans-serif;
  }}
  .ph-label {{ font-weight:700; font-size:15px; letter-spacing:.5px; }}
  .ph-topic {{ font-size:13px; color:#333; }}
  .stage {{
    position:relative; flex:1 1 auto; display:flex;
    align-items:center; justify-content:center; min-height:0;
  }}
  .stage > svg:not(.grid) {{
    max-width:100%; max-height:9.1in; height:auto; width:auto;
    border:1px solid #000;
  }}
  .stage .grid {{
    position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    max-width:100%; max-height:9.1in; height:auto; width:auto;
    pointer-events:none; display:none;
    stroke:#0a63d6; stroke-width:0.5; opacity:.45;
  }}
  body.grid-on .stage .grid {{ display:block; }}
  .plate-foot {{
    margin-top:8px; padding-top:5px; border-top:1px solid #ccc;
    font-family:ui-monospace,Consolas,monospace; font-size:9.5px; color:#888;
    text-align:center;
  }}

  @media print {{
    html,body {{ background:#fff; }}
    .toolbar {{ display:none; }}
    .page {{ margin:0; box-shadow:none; width:auto; min-height:auto;
             page-break-after:always; padding:0.35in; }}
    .page:last-child {{ page-break-after:auto; }}
    @page {{ size:letter portrait; margin:0.35in; }}
  }}
</style>
</head>
<body>
  <div class="toolbar">
    <strong>Knowledge Plates Review Book</strong>
    <label><input type="checkbox" id="gridToggle"> Show 1&nbsp;cm grid</label>
    <span class="hint">Then use your browser's Print &rarr; Save as PDF (or print to paper).</span>
  </div>
  {''.join(pages)}
  <script>
    document.getElementById('gridToggle').addEventListener('change', function(e) {{
      document.body.classList.toggle('grid-on', e.target.checked);
    }});
  </script>
</body>
</html>"""

    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(doc)

    print(f"Wrote {os.path.abspath(OUT_FILE)}")
    print(f"  {len(plates)} plates embedded" + (f", {len(missing)} missing" if missing else ""))
    try:
        os.startfile(os.path.abspath(OUT_FILE))  # Windows: open in browser
    except AttributeError:
        pass


if __name__ == "__main__":
    main()
