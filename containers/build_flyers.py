"""
Reissue the two container flyers corrected by AUDIT_2026-09-01.

  gd_09_flyer_pvc.docx  ->  gd_09_flyer_hdpe.docx   (material replaced)
  gd_15_tiere_granite.docx                          (lead removed, rewritten)

Both originals are published on GitHub, archive.org and under the Zenodo DOI.
Each reissue opens with a "What changed in this edition" block rather than
editing silently — the project's own governance material says to keep the
reversals in, and a public correction is cheaper than a quiet edit.

    python containers/build_flyers.py
"""
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH as A
from docx.shared import Pt, RGBColor

FONT = "Arial"          # matches the existing flyers
ACCENT = RGBColor(0x1F, 0x3B, 0x53)


def doc():
    d = Document()
    for s in d.sections:
        s.left_margin = s.right_margin = Pt(54)
        s.top_margin = s.bottom_margin = Pt(54)
    return d


def para(d, text, size=10.5, bold=False, align=None, italic=False, space_after=6, color=None):
    p = d.add_paragraph()
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    r.font.name, r.font.size, r.font.bold, r.font.italic = FONT, Pt(size), bold, italic
    if color:
        r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(space_after)
    return p


def h1(d, text):
    p = d.add_paragraph()
    r = p.add_run(text)
    r.font.name, r.font.size, r.font.bold = FONT, Pt(13), True
    r.font.color.rgb = ACCENT
    p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(14), Pt(5)


def h2(d, text):
    p = d.add_paragraph()
    r = p.add_run(text)
    r.font.name, r.font.size, r.font.bold = FONT, Pt(11), True
    p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(9), Pt(3)


def bullets(d, items):
    for it in items:
        p = d.add_paragraph(style="List Bullet")
        r = p.add_run(it)
        r.font.name, r.font.size = FONT, Pt(10.5)
        p.paragraph_format.space_after = Pt(2)


def table(d, rows):
    t = d.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.cell(i, j)
            cell.text = ""
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name, r.font.size, r.font.bold = FONT, Pt(9), (i == 0)
            p.paragraph_format.space_after = Pt(1)
    return t


def masthead(d, line2, line3, strip):
    para(d, "REMEMBER FORWARD", 26, True, A.CENTER, space_after=2)
    para(d, line2, 17, True, A.CENTER, space_after=4)
    para(d, line3, 11, False, A.CENTER, italic=True, space_after=6)
    para(d, strip, 11, True, A.CENTER, space_after=10, color=ACCENT)


def changed_block(d, lines):
    h1(d, "What Changed In This Edition")
    for ln in lines:
        para(d, ln, 10, italic=True, space_after=4)


def footer(d):
    para(d, "", 8, space_after=8)
    para(d, "Remember Forward · The Patient Message", 11, True, A.CENTER, space_after=2)
    para(d, "Buy it. Build it. Bury it. For someone you will never meet.",
         10, False, A.CENTER, italic=True, space_after=2)
    para(d, "CC BY-SA 4.0 · All materials free to use, share, and adapt · rememberforward.org",
         9, False, A.CENTER, space_after=0)


STALE_COST = ("Plate-set prices below are STALE and under revision. They were calculated for "
              "nickel, and they never included engraving setup, which is charged per unique "
              "design. Treat them as an order of magnitude only. See the errata.")


# ══════════════════════════════════════════════════════════ gd_09 — HDPE
def build_hdpe():
    d = doc()
    masthead(d, "BUILD A TIME CAPSULE FOR CIVILIZATION",
             "Not for a school project. For the actual future of humanity.",
             "THE STANDARD HOUSEHOLD CAPSULE · $75–$150 · HDPE PIPE")

    changed_block(d, [
        "This edition replaces the Schedule 80 PVC design issued through August 2026. "
        "PVC has been withdrawn from the project.",
        "PVC degrades by dehydrochlorination: it releases hydrogen chloride gas, the released "
        "acid accelerates further degradation, and inside a sealed capsule there is nowhere "
        "for that acid to go except onto your contents. PVC has also only existed since the "
        "1930s, so the 500–1,000 year figure previously printed here had no evidence behind "
        "it at all.",
        "HDPE is a plain hydrocarbon — carbon and hydrogen, no chlorine, nothing acidic to "
        "release. The closure method changes with it, because HDPE does not solvent-weld the "
        "way PVC does. See 'Closing The Capsule'.",
    ])

    h1(d, "What Is This?")
    para(d, "A time capsule containing laser-engraved titanium plates carrying what a surviving "
            "community would need to rebuild: how to make water safe, how to make fire and "
            "charcoal, how to grow food, how to organise fairly, and how to read the languages "
            "we wrote in. It is designed to be found by someone who shares no language and no "
            "culture with us.")
    para(d, "The project is called Remember Forward. The plates are called The Patient Message. "
            "Everything is free to download, copy, engrave and bury. No permission needed.")

    h1(d, "Why HDPE")
    bullets(d, [
        "No chlorine. Nothing in the polymer can turn into acid and attack the contents.",
        "Buy the BLACK pipe. The carbon black is not cosmetic — it is the antioxidant and UV "
        "stabiliser, and black pipe is the standard buried grade.",
        "DR-11 or thicker wall. Under soil pressure over centuries, wall thickness is what "
        "resists slow deformation.",
        "Honest expectation: a design target of 100+ years, which is far shorter than the "
        "titanium tiers. That is the point of this tier. Its job is to be cheap enough that "
        "there are thousands of them, not to be the one that lasts longest.",
    ])

    h1(d, "Materials")
    table(d, [
        ["Item", "Cost", "Where to Find"],
        ["4\" black HDPE pipe, DR-11, 18–24\" section", "$20–$35", "Irrigation or plumbing supplier"],
        ["4\" HDPE socket-fusion end caps (2)", "$15–$25", "Same supplier"],
        ["Socket fusion iron — rent, borrow, or supplier-fused", "$0–$60", "Tool rental; many irrigation suppliers fuse on site"],
        ["Silica gel desiccant packets (8–10)", "$5–$10", "Online or hardware store"],
        ["Oxygen absorbers (4–6 packets)", "$4–$8", "Online or hardware store"],
        ["Mylar vacuum-seal bags", "$5–$10", "Online"],
        ["Plate set — see note below", "see errata", "Free to download at rememberforward.org"],
    ])
    para(d, "", 6, space_after=2)
    para(d, STALE_COST, 9, italic=True)

    h1(d, "Closing The Capsule")
    para(d, "There is no thread, no gasket, no tape and no epoxy in this design. HDPE is welded "
            "to itself, and the capsule is closed permanently.")
    para(d, "That is deliberate. Every re-openable seal is a permanent liability bought to serve "
            "a single event that will be destructive anyway — the finder will cut it open. A "
            "capsule with a 100-year gasket is a 100-year capsule no matter what it is made of. "
            "Sweden's KBS-3 nuclear canisters, designed for 100,000 years, use welded lids and "
            "no seal at all.")
    h2(d, "Method A — socket fusion (preferred)")
    bullets(d, [
        "Heat the pipe end and the cap socket on the fusion iron until both surfaces are glossy — "
        "typically 200–220 °C, 8–12 seconds for 4\" pipe.",
        "Push together to the stop in one movement. Do not twist.",
        "Hold 60 seconds without moving. Leave undisturbed 30 minutes to cool fully.",
        "Do not exceed about 250 °C. Above that HDPE degrades rather than welds.",
    ])
    h2(d, "Method B — hot plate")
    bullets(d, [
        "Face both parts flat on a clean steel plate heated to 200–220 °C until a bead of melt "
        "appears around the edge.",
        "Press together squarely and hold until cool. A misaligned joint is a weak joint.",
    ])
    h2(d, "Test before you load it")
    bullets(d, [
        "Fuse one cap. Fill the tube with water, stand it upright 24 hours, check for weeping "
        "at the joint.",
        "Dry the inside completely. Load. Then fuse the second cap.",
        "Better: submerge the finished capsule and press gently. Any bubble is a failed weld.",
    ])

    h1(d, "Burial Instructions")
    bullets(d, [
        "Minimum depth 4 feet; 5 to 6 feet is better, and below the local frost line. Deeper "
        "than plough depth — cultivation reaches 8 to 12 inches.",
        "Orientation horizontal — this distributes soil pressure along the length rather than "
        "onto the welded ends.",
        "Surround with clean gravel before backfilling, for drainage.",
        "Mark with a COPPER or BRONZE stake driven 12 inches above the capsule. Earlier editions "
        "said \"non-ferrous (copper or stainless steel)\" — stainless steel is an iron alloy and "
        "is not non-ferrous. It will corrode and stain over this timescale.",
        "Trade-off worth knowing: a steel stake is far easier to find with a metal detector, but "
        "will not last. If findability matters more than the marker's own lifespan, set a steel "
        "plate ABOVE the capsule and accept that it is a century-scale marker, not a permanent one.",
        "Record GPS coordinates and a description by landmarks — distances from two prominent "
        "natural features — and store both in several places.",
    ])

    h1(d, "Free Downloads")
    para(d, "All SVG plate files, build guides, and this document are free at "
            "rememberforward.org — CC BY-SA 4.0, no permission needed.")
    footer(d)
    d.save("containers/gd_09_flyer_hdpe.docx")
    print("  wrote containers/gd_09_flyer_hdpe.docx")


# ══════════════════════════════════════════════════════════ gd_15 — GRANITE
def build_granite():
    d = doc()
    masthead(d, "TIER E · GRANITE VAULT",
             "The permanent institutional archive.",
             "$500–$1,500 · DESIGN TARGET 10,000+ YEARS · FIXED LOCATION")

    changed_block(d, [
        "This edition removes the lead lining and the poured lead seal specified through "
        "August 2026, and withdraws the claim of \"100,000+ years, the nuclear industry "
        "standard.\"",
        "That claim was wrong. The nuclear industry does not use lead-lined stone for archival "
        "containment. Sweden and Finland's KBS-3 design uses a copper canister over a cast-iron "
        "insert, surrounded by a bentonite clay buffer, in granitic bedrock. Lead appears in "
        "that industry only as radiation shielding in transport casks. And the 100,000-year "
        "figure is claimed for repository GEOLOGY behind a formal safety case — never for a "
        "container, and never by us.",
        "Lead is withdrawn on its own merits too: it creeps under sustained load so it cannot "
        "carry structure, it is toxic to cast and handle, and in the presence of moisture it "
        "forms a galvanic couple with titanium in which the lead is consumed. The molten-lead "
        "pouring step in earlier editions was also the most hazardous instruction in this "
        "entire project.",
        "What replaces it is better and cheaper: a bentonite clay buffer and a sealed inner "
        "vessel.",
    ])

    h1(d, "Historical Precedent")
    table(d, [
        ["Civilization", "Application", "Age", "Survival Status"],
        ["Ancient Egypt", "Granite sarcophagi and canopic jars", "3,000–5,000 years",
         "Contents intact in many cases"],
        ["Ancient Rome", "Stone sarcophagi", "2,000 years", "Many survive intact with contents"],
        ["Medieval Europe", "Stone church crypts", "500–1,000 years",
         "Most survive structurally intact"],
        ["Modern nuclear industry", "Copper canister in a bentonite buffer, in granitic bedrock (KBS-3)",
         "Designed for 100,000 years", "Engineering standard, not time-tested. Their safety case, not ours."],
        ["This project", "Civilizational knowledge archive", "Design target: 10,000 years",
         "Granite body, bentonite buffer, sealed inner vessel"],
    ])

    h1(d, "Why Granite")
    h2(d, "Chemical properties")
    para(d, "Granite is an igneous rock of quartz, feldspar and mica. It is chemically inert to "
            "virtually everything it will meet underground, it does not dissolve in groundwater "
            "on any timescale that matters here, and it is the host rock class that real deep "
            "repositories are actually built in.")
    h2(d, "Mechanical properties")
    para(d, "Compressive strength of roughly 100 to 300 MPa. It will not be crushed by soil load, "
            "it will not deform, and unlike lead it does not creep. Granite carries the structure; "
            "nothing else in this design has to.")

    h1(d, "The Containment System — Three Layers")
    h2(d, "Layer 1 — the granite body")
    para(d, "Structural and inert. It resists load, roots, burrowing animals and casual disturbance. "
            "It is not, by itself, a seal — stone joints are never hermetic.")
    h2(d, "Layer 2 — bentonite clay buffer")
    para(d, "This is the layer that does the work the lead was imagined to do, and it does it "
            "better. Sodium bentonite swells roughly ten to fifteen times its dry volume when it "
            "meets water, which means any crack, gap or void it can reach becomes self-sealing. "
            "It buffers the chemistry around the inner vessel and slows water movement to a crawl. "
            "It is the engineered barrier in every serious geological repository.")
    para(d, "Sourcing: sold as pond sealer, as drilling mud, and as unscented clumping cat litter. "
            "If you use cat litter, confirm it is sodium bentonite with no added fragrance, "
            "deodoriser or clumping agents.")
    h2(d, "Layer 3 — the sealed inner vessel")
    para(d, "The only real barrier. Everything else buys it time.")
    bullets(d, [
        "BUILD IT YOURSELF: a fired ceramic vessel sealed with hot pine pitch. In this project's "
        "own ranking of seals, pitch on ceramic rates equal to cast lead — and it is non-toxic, "
        "needs no crucible, and is the same method as the Tier 0 capsule.",
        "COMMISSION IT: a welded titanium vessel, if an institution can have one made. No gasket, "
        "no joint compound, nothing to fail. Titanium welding needs argon shielding and back-purge; "
        "this is a fabrication-shop operation, not a workshop one. Do not attempt it with a "
        "hardware-store welder.",
        "DO NOT USE any gasket, O-ring or elastomer, whatever the datasheet claims. No elastomer "
        "has a validated multi-century life. A 10,000-year vault with a 100-year seal is a "
        "100-year vault.",
    ])

    h1(d, "Construction")
    h2(d, "Step 1 — obtain or cut the granite")
    para(d, "Six slabs: base, four sides, lid. Minimum 5 cm thick, ideally 8 to 10 cm. Monument "
            "yards and stone fabricators sell offcuts cheaply. Alternatively carve a cavity into "
            "a single block — slower, and the traditional method, with no joints to fail.")
    h2(d, "Step 2 — assemble the box")
    para(d, "Dry-fit all six slabs and grind any gaps with a diamond disc. Bed the joints in lime "
            "mortar. Geopolymer — local clay or metakaolin with an alkali activator, cured at "
            "low temperature — is an alternative worth considering: it is durable, low-permeability, "
            "and makeable from local materials by anyone who finds this later.")
    h2(d, "Step 3 — prepare and seal the inner vessel")
    bullets(d, [
        "Dry the plates and any other contents thoroughly. Moisture sealed in is moisture that "
        "stays in.",
        "Load the vessel with desiccant and oxygen absorbers. Oxygen is the main agent of decay "
        "once water is excluded.",
        "Seal it: pitch on ceramic, or a welded titanium lid. Seal it permanently. The finder "
        "will cut it open.",
    ])
    h2(d, "Step 4 — pack with bentonite")
    para(d, "Set the sealed vessel centrally in the granite cavity and pack dry sodium bentonite "
            "firmly all around it — a minimum of 5 cm on every face, including beneath. Leave no "
            "voids. Pack it dry: it is meant to swell later, when and if water ever arrives.")
    h2(d, "Step 5 — close and coat")
    para(d, "Bed the lid on lime mortar and point the perimeter joint. When cured, coat the whole "
            "exterior in three or four layers of hot pine pitch or bitumen. This is a water "
            "shedding layer, not a seal — it buys the mortar joints decades they would not "
            "otherwise have.")

    h1(d, "Burial and Placement")
    para(d, "A vault of these dimensions weighs roughly 60 to 90 kg before contents. Plan the "
            "lift and the route before you build it, not after.")
    table(d, [
        ["Placement", "Depth / Location", "Best For", "Notes"],
        ["Deep burial", "Minimum 6 feet, ideally 8–10", "Permanent hidden archive",
         "Store GPS coordinates separately, in more than one place"],
        ["Cave or rock shelter", "On a raised shelf above floor level", "Long-term accessible archive",
         "Dry caves are the best preservation record we have"],
        ["Foundation burial", "Within a stone or concrete foundation", "Community institutional archive",
         "Protected by the structure above; the most accessible option"],
        ["Arctic / permafrost", "8–10 feet in a permafrost region", "NO LONGER RECOMMENDED ALONE",
         "Permafrost is not a permanent assumption. Svalbard's seed vault took meltwater into its "
         "access tunnel within nine years of opening. Treat frozen ground as a bonus, never as the barrier."],
        ["Salt mine", "On a raised platform above the mine floor", "Excellent long-term archive",
         "Self-sealing, dry, low oxygen. Requires an institutional agreement."],
    ])

    h1(d, "The Community Commitment")
    para(d, "A granite vault is not just a container. It is heavy enough that it will not be moved "
            "casually, and permanent enough that it outlives whoever sites it. That makes siting "
            "it a decision about a place and the people in it, not a decision about a box.")
    para(d, "Consider inscribing on the exterior: the year of burial, a brief plain description of "
            "the contents, and the bridge phrase — \"This was made for you, freely, by people who "
            "remembered forward.\" Cut it deep. Raised letters abrade away first; a cut groove "
            "fills with dirt and gets easier to read, not harder.")
    footer(d)
    d.save("containers/gd_15_tiere_granite.docx")
    print("  wrote containers/gd_15_tiere_granite.docx (rewritten)")


if __name__ == "__main__":
    print("Reissuing flyers per AUDIT_2026-09-01:")
    build_hdpe()
    build_granite()
