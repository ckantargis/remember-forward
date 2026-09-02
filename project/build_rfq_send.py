"""
Generate the shop-facing RFQ from the master, stripping the internal section.

engraving_rfq.md carries an "Internal notes - not for the shop" block with the
kit's cost model in it: the $594-1,215 range, the ~$905 midpoint and the ~$930
break-even. A shop that can see your break-even is quoting against it. This
strips everything from that heading down, so the send version cannot drift from
the master and cannot leak it either.

    python project/build_rfq_send.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "engraving_rfq.md")
DST = os.path.join(HERE, "engraving_rfq_TO_SEND.md")

MARKER = "### Internal notes"

src = open(SRC, encoding="utf-8").read()
if MARKER not in src:
    raise SystemExit("ERROR: internal-notes marker not found. Refusing to guess "
                     "where the shop-facing content ends.")

body = src.split(MARKER)[0]
body = re.sub(r"\n---\s*\n\s*$", "\n", body)

# The lead paragraph is an internal instruction, not something a shop should read.
body = re.sub(r"\*\*Send to 3–5 shops.*?\*\*\n\n", "", body, flags=re.S)
# "never been modelled on our side" tells a shop you cannot price-check their
# setup charge. Keep the request, drop the tell. (The registration line in 4a is
# left as-is - admitting an unverified assumption there invites a correction,
# which is what we want.)
body = body.replace(
    "this is charged per design, not per part. It has never been modelled on our\n"
    "  side and may dominate at low volume.",
    "this is charged per design rather than per part, so we need to see it as its\n"
    "  own line at each quantity.")

body = body.replace(
    "Attach: `plate_coupon_b_engraving.dxf` (and `.svg`, `.pdf`) as the specimen.\n"
    "Face B *is* the RFQ specimen — it was drawn so a quote comes back against real\n"
    "geometry rather than a description.",
    "A specimen part is attached — `plate_coupon_b_engraving` in DXF, PDF and SVG. "
    "It was drawn specifically so you can quote against real geometry rather than a\n"
    "description. `plate_coupon_a_vocabulary` is the reverse face of the same part.")

open(DST, "w", encoding="utf-8").write(body.rstrip() + "\n")

leaks = [w for w in ("905", "930", "594", "1,215", "break-even", "COGS", "blocked",
                     "05A", "diminished") if w in body]
print(f"wrote {os.path.relpath(DST, os.path.dirname(HERE))}  ({len(body):,} chars)")
print("leak check:", "CLEAN" if not leaks else f"*** FOUND {leaks} ***")
