# RFQ covering email

Send to 3–5 shops. Search terms that find the right kind of vendor: *fiber laser
marking service*, *laser engraving titanium*, *photochemical etching titanium*.
Ask for the estimating or sales engineer, not general enquiries.

**Do not send `engraving_rfq.md`.** That is the master and it ends with an
internal section carrying the kit's cost model. Send `engraving_rfq_TO_SEND.md`,
which is generated from it by `build_rfq_send.py` with that section stripped.

---

## Subject

`RFQ — two-sided laser engraving, titanium Gr2, 120×170 mm — specimen attached`

## Body

> Hello,
>
> I'm looking for a quote on two-sided laser engraving in titanium Grade 2, and
> I'd like to start with three test coupons before committing to any run.
>
> The short version: 120 × 170 mm plates, 0.8 mm Ti Gr2, engraved on both faces,
> 0.10 mm minimum feature, ablated grooves rather than annealed marks. A
> production kit is 14 unique engraved faces; I'd like pricing at 10, 25 and 50
> kits, with the per-design setup charge broken out separately from the per-face
> run cost.
>
> I've attached the actual specimen part rather than describing it — DXF with
> text converted to outline paths, plus PDF and SVG of the same geometry. The
> file carries a stroke ladder from 0.10 mm, a gap ladder, a dot ladder and
> registration crosshairs, so you can quote against real geometry and tell me
> where the process actually stops.
>
> Full spec is below. Three things I'd particularly like your view on:
>
> 1. Whether you can hold 0.10 mm minimum feature on 0.8 mm Ti Gr2, and what
>    groove depth you'd target.
> 2. What front-to-back registration tolerance you can hold, and how you fixture
>    for the second side.
> 3. One plate in the set is A3 (297 × 420 mm), which is well outside a single
>    galvo field. Whether you stitch or move the part, and whether the 0.10 mm
>    minimum feature survives on that plate.
>
> If any of this is not something you'd take on, I'd genuinely rather know now
> than at first article — and a pointer to someone who would is welcome.
>
> Thanks,
> Cormac Kantargis
> Remember Forward LLC
> rememberforward.org

Then paste the contents of `engraving_rfq_TO_SEND.md` below the signature, or
attach it as a PDF.

## Attachments

| File | Why |
|---|---|
| `plate_coupon_b_engraving.dxf` | The specimen. DXF is what shops want, text already outlined. |
| `plate_coupon_b_engraving.pdf` | So they can see it without a CAD seat. |
| `plate_coupon_a_vocabulary.dxf` | The reverse face of the same part — both faces must be quoted. |
| `plate_coupon_a_vocabulary.pdf` | As above. |
| `engraving_rfq_TO_SEND.md` | Only if not pasting into the body. |

SVG on request. Do not attach the master `engraving_rfq.md`.

---

## Before you press send

- [ ] Sending `engraving_rfq_TO_SEND.md`, **not** `engraving_rfq.md`
- [ ] Both coupon faces attached, not just Face B
- [ ] Files are the post-2026-09-01 versions — the earlier ones were 5.83%
      oversize and would have produced 127 × 180 mm parts

## What to do with the replies

The quote decides the kit price, so capture it in a form you can compare:

| Shop | Per-face @10 | @25 | @50 | Setup per design | Min feature held | Registration | A3 verdict | Lead time |
|---|---|---|---|---|---|---|---|---|

**Watch the setup charge more than the per-face cost.** With 14 unique designs,
a $75 setup per design is $1,050 before a single plate is marked — which at a
25-kit run is more than the entire per-face cost. If setup dominates, the answer
may be fewer unique faces rather than a different shop.

**A shop that says the A3 plate degrades the minimum feature is doing you a
favour.** That would be a reason to re-plan 05I, not a reason to discount them.
