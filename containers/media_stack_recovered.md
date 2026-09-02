# The Media Stack — recovered 2026-08-20

**Cormac was right and the record was searched badly.** The microfilm-plus-lens
idea is real, it is his, and it is documented — in the **24–25 March 2026**
conversation, preserved in `claude_export_2026-05-29/conversations.json` under
*"Remember Forward LLC — The Patient Message."* It is not in any container
document, any guide, or any memory file, which is why two searches missed it.

More importantly: **the March design was a six-layer media stack, and five of
those six layers are absent from every current document.** Nothing in the record
records a decision to drop them. This looks like drift between March and the
May `container_and_tiering_v2` rewrite, not a choice.

---

## What the March design actually specified

A 4″ PVC capsule holding media ordered by durability, *most to least*:

| # | Layer | Life | Cost | Status today |
|---|---|---|---|---|
| 1 | Nickel / stainless engraved plates | 10,000 yr | $15–20 each | **Kept** (now titanium) |
| 2 | Anodized aluminium tiles — maps, star charts, crop calendars | millennia | $30–40 for dozens | **Gone** |
| 3 | **35 mm B&W archival microfilm + magnifying glass** | **500+ yr dry** | **$50–80/roll** | **Gone** |
| 4 | Acid-free laminated paper — the finder's letter | 100–300 yr | $10–20 | **Gone** |
| 5 | Heirloom seeds in Mylar | rotate 5–10 yr | $20–40 | **Gone** |
| 6 | SD cards in cast epoxy — the bridge medium | 50–100 yr | $12–18 | **Gone** |

Original bill of materials: **$165–271**, with a stated **budget build under
$80** that dropped the microfilm and professional engraving.

### The line that matters

> *"A single roll holds 1,000+ pages of text and diagrams. Include a magnifying
> glass (a simple glass lens survives as long as anything) sealed separately.
> **The lens IS the reader — no power needed.**"*

Named suppliers: Crowley Micrographics, Archive Systems, Backstage Library
Works. Quoted at $60–120 per roll in small batches, **$20–40 at volume**.

---

## Why this matters to the affordability problem

The whole 264-plate archive is roughly 264 images. **A single microfilm roll
holds 1,000+ pages.** So:

| Complete archive, one capsule | Cost | Mass | Life |
|---|---|---|---|
| Titanium plates | $5,729–12,751 | 19 kg | 10,000 yr (modelled) |
| Pressed ceramic tiles | $159–657 + a $6k–74k mould library | 39 kg | 2,000 yr (observed) |
| **35 mm microfilm + lens** | **$25–95** | **under 150 g** | **500 yr, dry** |

That is the low price point that still contains *all* the knowledge — and it was
designed in March, before anyone asked the affordability question.

It does not replace ceramic or metal. It is 500 years against 2,000+, and it is
conditional on staying dry, which makes it hostage to a desiccant that is itself
a consumable. **Microfilm buys completeness; ceramic and metal buy permanence.**
A capsule wants both, and they are cheap together.

---

## The idea underneath, which is better than any single layer

The March stack has a property nobody named at the time: **each layer is aimed
at a different finder-era.**

    50–100 yr    SD card      a finder with a computer
    100–300 yr   paper        a finder who reads a modern language
    500 yr       microfilm    a finder with a lens and patience
    2,000 yr+    ceramic      a finder with nothing but eyes
    10,000 yr    metal        a finder after everything else is gone

A capsule is not one message to one future. **It is a relay**, and it should
degrade gracefully — each layer handing off to the next as it fails. That
principle sits directly alongside *every capsule must be independently
sufficient*: sufficiency across **time**, not only across language.

It also fixes a real weakness in the current plate-only architecture. As it
stands, a finder in 2075 gets an object designed for a finder in 4000 and
nothing pitched at them — even though they are overwhelmingly the most likely
person to open it, and the only one who could copy and redistribute it.

---

## Open questions this reopens

1. **Can microfilm be shot in-house?** Photographing plates onto B&W polyester
   film with a copy stand is not hard; archival *processing* — full fixing and
   washing — is what determines whether it lasts 500 years or 50. Worth pricing
   both ways before assuming the service route. **Unverified.**
2. **Does the lens go in every capsule?** It is cheap, it never fails, and it is
   also the thing that makes ceramic microfilm viable later. Probably yes, with
   a plate showing how to grind another.
3. **Do seeds come back?** They are consumables needing rotation every 5–10
   years, which conflicts with a sealed capsule — but "seeds are civilization"
   is the strongest single line in the March design, and a burial-day seed
   packet is a very different product from a 2,000-year one.
4. **What else did the March–May rewrite drop?** This surfaced by accident while
   chasing one question. The export holds twelve conversations and has never
   been systematically compared against the current documents.

---

## Filing note

The March conversation predates the repo's document set. **The export is a
primary source and should be treated as one** — it is currently a zip file in
the repo root with no index and nothing pointing at it.
