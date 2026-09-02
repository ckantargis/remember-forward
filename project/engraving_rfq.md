# Engraving RFQ — Remember Forward / The Patient Message

**Send to 3–5 shops. Engraving is ~55% of COGS and the only real unknown in the
kit price. Everything else in the Founder's Kit is costed; this quote decides
whether the kit is a $905 product or something else.**

Attach: `plate_coupon_b_engraving.dxf` (and `.svg`, `.pdf`) as the specimen.
Face B *is* the RFQ specimen — it was drawn so a quote comes back against real
geometry rather than a description.

---

## 1. What we're making

Engraved titanium plates for a buried archive. Long-life legibility is the whole
product, so process choices are driven by permanence, not appearance.

| | |
|---|---|
| Material | **Titanium Grade 2 (CP)**, not Grade 5 |
| Thickness | **0.8 mm** (also quote 0.5 mm — we may drop to it on the large plate) |
| Standard plate | **120 × 170 mm, engraved BOTH FACES** |
| Large plate | **297 × 420 mm (A3), engraved both faces** — see §4, this one has a catch |
| Disc | **68 mm diameter, both faces** |
| Marking | **Ablated grooves — NOT laser-annealed oxide marks.** See §3. |
| Minimum feature | **0.10 mm** |
| Finish | Mill finish acceptable. No coating, no anodising. |

---

## 2. Quantities — please price the ladder

One kit = **14 engraved faces**: 4 plates × 2 faces (120 × 170) + 1 A3 × 2 faces
+ 1 plate × 2 faces (120 × 170) + 1 disc × 2 faces.

| Order | Purpose |
|---|---|
| **Coupons: 3 pieces** | The attached specimen, both faces. Needed FIRST and separately. |
| 10 kits | 140 faces |
| 25 kits | 350 faces |
| 50 kits | 700 faces |

**Please break out separately:**
- **Per-face run cost** at each quantity
- **Setup / programming charge per unique design** — we have 14 unique faces, and
  this is charged per design, not per part. It has never been modelled on our
  side and may dominate at low volume.
- Minimum order value
- Lead time at each quantity

---

## 3. Ablated grooves, not annealed marks — this matters

We need a **topographic groove**, not a colour change.

A laser-annealed mark is an oxide film. It is destroyed by the **480–540 °C
stress-relief** we run after rolling the plates, and it abrades away in soil. An
ablated groove survives both.

- Please confirm you can ablate to a measurable depth in Ti Gr2 and state the
  depth you would target.
- If you would normally anneal for this application, tell us — we would rather
  hear the objection than receive annealed parts.

---

## 4. Two things we expect to be problems

**a) Two-sided registration.** Both faces carry content that must align. Face B
of the specimen has registration crosshairs at four corners and centre.
- What front-to-back registration tolerance can you hold? We have assumed
  **±0.15 mm** and have never verified it.
- How do you fixture for the second side?

**b) The A3 plate and your galvo field.** Our own note on field size:
175 mm field → ~0.07 mm floor · 200 mm → ~0.10 mm · 300 mm → ~0.15 mm.
A 297 × 420 mm plate is far outside a single field.
- Do you stitch fields, or move the part? What is the stitching error?
- **Does the 0.10 mm minimum feature survive on the A3 plate, or does it degrade?**
  If it degrades, say by how much — we would rather re-plan the plate than
  discover it after the run.

---

## 5. Files

- **DXF preferred**, text converted to outline paths, no live text.
- SVG and PDF also available.
- All geometry is **stroked lines, not filled outlines**. If you need
  closed-contour geometry instead, tell us and we will re-export.
- Units are millimetres. The specimen is 120 × 170 mm — please confirm the size
  your software reads, as a check that nothing rescaled in transit.

---

## 6. Questions we'd like answered in the quote

1. Per-face cost at 10 / 25 / 50 kits, and setup per unique design.
2. Can you hold 0.10 mm minimum feature on Ti Gr2 at 0.8 mm thickness?
3. Front-to-back registration tolerance, and how you fixture for it.
4. Groove depth you would target, and whether you can hold it consistently.
5. Whether the A3 plate degrades the minimum feature, and by how much.
6. Do you stress-relieve, or should we arrange 480–540 °C separately?
7. Lead time for 3 coupons, and lead time for a 25-kit run.
8. Do you supply the titanium, or should we?

---

## 7. Context you may find useful

The plates are an open-source archive intended to stay legible for a very long
time — the files are CC BY-SA 4.0 and published at rememberforward.org, on
archive.org, and under a Zenodo DOI. We are not asking for anything exotic; we
are asking for ordinary industrial marking held to a stated minimum feature and
a stated depth, and we would rather be told early that something is not
achievable than find out at first article.

---

### Internal notes — not for the shop

- **The coupon must be ordered before the run.** Face A settles the
  diminished-figure vocabulary that has blocked 05A–05H since 2026-04-17; Face B
  settles the process. One part, two blockers.
- **Sizing defect caught 2026-09-01:** every plate SVG in this repo declares
  `width="480" height="680"` with no units. Unitless is CSS pixels, which any
  tool reads at 96 dpi = **127 × 180 mm, 5.83% oversize.** The coupon is fixed
  (`width="120mm" height="170mm"`, viewBox unchanged so the drawing is
  untouched). **FIXED 2026-09-01 across the fleet**: 491 SVGs + 112 generator scripts, one
  attribute each, viewBox untouched. Verified by re-exporting a production plate
  to DXF: 170.00 mm on a 680-unit canvas = exactly 0.2500 mm/unit. The 14 ceramic
  relief masters are deliberately 1.136x oversize for 12% firing shrinkage and
  were correctly skipped.
- **Two plates carry geometry ~2.5 mm past the right edge** — `plate21c_greek_grammar`
  and `plate20a_swahili_script`. Both are paused language plates, neither is in the
  kit, but they must be trimmed before they are ever sent out.
- Price context: kit rebuilt 2026-08-30 to $594–1,215, mid ~$905, break-even
  ~$930 — riding on an unquoted $15–35/face. This RFQ is what replaces that guess.
- Cap of 25 was deferred pending this quote.
