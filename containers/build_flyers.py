"""
Reissue the two container flyers corrected by AUDIT_2026-09-01.

  gd_09_flyer_pvc  ->  gd_09_flyer_hdpe   (material replaced)
  gd_15_tiere_granite                     (lead removed, rewritten)

CONTENT IS DEFINED ONCE, RENDERED TWICE. Every document in this project ships as
both .docx and .pdf, and hand-maintaining two copies is precisely how the
nickel/Viton/lead claims survived three weeks of corrections. The block list
below is the single source; render_docx() and render_pdf() both read from it.

Each reissue opens with a "What Changed In This Edition" block rather than being
edited silently — the project's own governance material says to keep the
reversals in, and a public correction is cheaper than a quiet edit.

    python containers/build_flyers.py
"""
import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH as A
from docx.shared import Pt, RGBColor
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (ListFlowable, ListItem, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
ACCENT_HEX = "1F3B53"
ACCENT_DOCX = RGBColor(0x1F, 0x3B, 0x53)
ACCENT_PDF = colors.HexColor("#" + ACCENT_HEX)
DOCX_FONT = "Arial"
PDF_FONT = "Helvetica"          # metrically the same family as Arial

STALE_COST = ("Plate-set prices are STALE and under revision. They were calculated for nickel, "
              "and never included engraving setup, which is charged per unique design. Treat "
              "them as an order of magnitude only. See the errata.")


# ═════════════════════════════════════════════════════════════════ RENDERERS
def render_docx(blocks, path):
    d = Document()
    for s in d.sections:
        s.left_margin = s.right_margin = Pt(54)
        s.top_margin = s.bottom_margin = Pt(54)

    def para(text, size=10.5, bold=False, align=None, italic=False, after=6, color=None):
        p = d.add_paragraph()
        if align is not None:
            p.alignment = align
        r = p.add_run(text)
        r.font.name, r.font.size, r.font.bold, r.font.italic = DOCX_FONT, Pt(size), bold, italic
        if color:
            r.font.color.rgb = color
        p.paragraph_format.space_after = Pt(after)

    for kind, val in blocks:
        if kind == "masthead":
            para(val[0], 26, True, A.CENTER, after=2)
            para(val[1], 17, True, A.CENTER, after=4)
            para(val[2], 11, False, A.CENTER, italic=True, after=6)
            para(val[3], 11, True, A.CENTER, after=10, color=ACCENT_DOCX)
        elif kind == "h1":
            p = d.add_paragraph()
            r = p.add_run(val)
            r.font.name, r.font.size, r.font.bold = DOCX_FONT, Pt(13), True
            r.font.color.rgb = ACCENT_DOCX
            p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(14), Pt(5)
        elif kind == "h2":
            p = d.add_paragraph()
            r = p.add_run(val)
            r.font.name, r.font.size, r.font.bold = DOCX_FONT, Pt(11), True
            p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(9), Pt(3)
        elif kind == "p":
            para(val)
        elif kind == "note":
            para(val, 9, italic=True)
        elif kind == "changed":
            for ln in val:
                para(ln, 10, italic=True, after=4)
        elif kind == "bullets":
            for it in val:
                p = d.add_paragraph(style="List Bullet")
                r = p.add_run(it)
                r.font.name, r.font.size = DOCX_FONT, Pt(10.5)
                p.paragraph_format.space_after = Pt(2)
        elif kind == "table":
            t = d.add_table(rows=len(val), cols=len(val[0]))
            t.style = "Table Grid"
            for i, row in enumerate(val):
                for j, cell in enumerate(row):
                    c = t.cell(i, j)
                    c.text = ""
                    p = c.paragraphs[0]
                    r = p.add_run(cell)
                    r.font.name, r.font.size, r.font.bold = DOCX_FONT, Pt(9), (i == 0)
                    p.paragraph_format.space_after = Pt(1)
        elif kind == "footer":
            para("", 8, after=8)
            para("Remember Forward · The Patient Message", 11, True, A.CENTER, after=2)
            para("Buy it. Build it. Bury it. For someone you will never meet.",
                 10, False, A.CENTER, italic=True, after=2)
            para("CC BY-SA 4.0 · All materials free to use, share, and adapt · rememberforward.org",
                 9, False, A.CENTER, after=0)
    d.save(path)


def render_pdf(blocks, path):
    S = {
        "t1":  ParagraphStyle("t1", fontName=PDF_FONT + "-Bold", fontSize=26, leading=30,
                              alignment=TA_CENTER, spaceAfter=2),
        "t2":  ParagraphStyle("t2", fontName=PDF_FONT + "-Bold", fontSize=17, leading=21,
                              alignment=TA_CENTER, spaceAfter=4),
        "t3":  ParagraphStyle("t3", fontName=PDF_FONT + "-Oblique", fontSize=11, leading=14,
                              alignment=TA_CENTER, spaceAfter=6),
        "t4":  ParagraphStyle("t4", fontName=PDF_FONT + "-Bold", fontSize=11, leading=14,
                              alignment=TA_CENTER, spaceAfter=12, textColor=ACCENT_PDF),
        "h1":  ParagraphStyle("h1", fontName=PDF_FONT + "-Bold", fontSize=13, leading=16,
                              spaceBefore=14, spaceAfter=5, textColor=ACCENT_PDF),
        "h2":  ParagraphStyle("h2", fontName=PDF_FONT + "-Bold", fontSize=11, leading=14,
                              spaceBefore=9, spaceAfter=3),
        "p":   ParagraphStyle("p", fontName=PDF_FONT, fontSize=10.5, leading=14, spaceAfter=6),
        "it":  ParagraphStyle("it", fontName=PDF_FONT + "-Oblique", fontSize=10, leading=13.5,
                              spaceAfter=4),
        "sm":  ParagraphStyle("sm", fontName=PDF_FONT + "-Oblique", fontSize=9, leading=12,
                              spaceAfter=6),
        "li":  ParagraphStyle("li", fontName=PDF_FONT, fontSize=10.5, leading=13.5, spaceAfter=2),
        "cel": ParagraphStyle("cel", fontName=PDF_FONT, fontSize=8.5, leading=11),
        "hd":  ParagraphStyle("hd", fontName=PDF_FONT + "-Bold", fontSize=8.5, leading=11),
        "f1":  ParagraphStyle("f1", fontName=PDF_FONT + "-Bold", fontSize=11, leading=14,
                              alignment=TA_CENTER, spaceAfter=2),
        "f2":  ParagraphStyle("f2", fontName=PDF_FONT + "-Oblique", fontSize=10, leading=13,
                              alignment=TA_CENTER, spaceAfter=2),
        "f3":  ParagraphStyle("f3", fontName=PDF_FONT, fontSize=9, leading=12,
                              alignment=TA_CENTER),
    }
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    story = []
    for kind, val in blocks:
        if kind == "masthead":
            for txt, st in zip(val, ("t1", "t2", "t3", "t4")):
                story.append(Paragraph(esc(txt), S[st]))
        elif kind in ("h1", "h2", "p"):
            story.append(Paragraph(esc(val), S[kind]))
        elif kind == "note":
            story.append(Paragraph(esc(val), S["sm"]))
        elif kind == "changed":
            for ln in val:
                story.append(Paragraph(esc(ln), S["it"]))
        elif kind == "bullets":
            story.append(ListFlowable(
                [ListItem(Paragraph(esc(i), S["li"]), leftIndent=14) for i in val],
                bulletType="bullet", start="•", leftIndent=14, bulletFontSize=8))
            story.append(Spacer(1, 4))
        elif kind == "table":
            ncol = len(val[0])
            avail = LETTER[0] - 2 * 54
            widths = ([avail * w for w in (.22, .13, .30, .35)] if ncol == 4
                      else [avail * w for w in (.46, .16, .38)] if ncol == 3
                      else [avail / ncol] * ncol)
            data = [[Paragraph(esc(c), S["hd"] if i == 0 else S["cel"]) for c in row]
                    for i, row in enumerate(val)]
            t = Table(data, colWidths=widths, repeatRows=1)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#999999")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EDF2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story += [t, Spacer(1, 6)]
        elif kind == "footer":
            story.append(Spacer(1, 14))
            story.append(Paragraph("Remember Forward · The Patient Message", S["f1"]))
            story.append(Paragraph("Buy it. Build it. Bury it. For someone you will never meet.", S["f2"]))
            story.append(Paragraph(
                "CC BY-SA 4.0 · All materials free to use, share, and adapt · rememberforward.org", S["f3"]))
    SimpleDocTemplate(path, pagesize=LETTER, leftMargin=54, rightMargin=54,
                      topMargin=54, bottomMargin=54,
                      title=os.path.basename(path)).build(story)


# ═════════════════════════════════════════════════════════════════ CONTENT
HDPE = [
 ("masthead", ("REMEMBER FORWARD", "BUILD A TIME CAPSULE FOR CIVILIZATION",
               "Not for a school project. For the actual future of humanity.",
               "THE STANDARD HOUSEHOLD CAPSULE · $75–$150 · HDPE PIPE")),
 ("h1", "What Changed In This Edition"),
 ("changed", [
   "This edition replaces the Schedule 80 PVC design issued through August 2026. PVC has been "
   "withdrawn from the project.",
   "PVC degrades by dehydrochlorination: it releases hydrogen chloride gas, the released acid "
   "accelerates further degradation, and inside a sealed capsule there is nowhere for that acid "
   "to go except onto your contents. PVC has also only existed since the 1930s, so the "
   "500–1,000 year figure previously printed here had no evidence behind it at all.",
   "HDPE is a plain hydrocarbon — carbon and hydrogen, no chlorine, nothing acidic to release. "
   "The closure method changes with it, because HDPE does not solvent-weld the way PVC does. "
   "See 'Closing The Capsule'."]),
 ("h1", "What Is This?"),
 ("p", "A time capsule containing laser-engraved titanium plates carrying what a surviving "
       "community would need to rebuild: how to make water safe, how to make fire and charcoal, "
       "how to grow food, how to organise fairly, and how to read the languages we wrote in. It "
       "is designed to be found by someone who shares no language and no culture with us."),
 ("p", "The project is called Remember Forward. The plates are called The Patient Message. "
       "Everything is free to download, copy, engrave and bury. No permission needed."),
 ("h1", "Why HDPE"),
 ("bullets", [
   "No chlorine. Nothing in the polymer can turn into acid and attack the contents.",
   "Buy the BLACK pipe. The carbon black is not cosmetic — it is the antioxidant and UV "
   "stabiliser, and black pipe is the standard buried grade.",
   "DR-11 or thicker wall. Under soil pressure over centuries, wall thickness is what resists "
   "slow deformation.",
   "Honest expectation: a design target of 100+ years, far shorter than the titanium tiers. "
   "That is the point of this tier. Its job is to be cheap enough that there are thousands of "
   "them, not to be the one that lasts longest."]),
 ("h1", "Materials"),
 ("table", [
   ["Item", "Cost", "Where to Find"],
   ["4\" black HDPE pipe, DR-11, 18–24\" section", "$20–$35", "Irrigation or plumbing supplier"],
   ["4\" HDPE socket-fusion end caps (2)", "$15–$25", "Same supplier"],
   ["Socket fusion iron — rent, borrow, or supplier-fused", "$0–$60",
    "Tool rental; many irrigation suppliers fuse on site"],
   ["Silica gel desiccant packets (8–10)", "$5–$10", "Online or hardware store"],
   ["Oxygen absorbers (4–6 packets)", "$4–$8", "Online or hardware store"],
   ["Mylar vacuum-seal bags", "$5–$10", "Online"],
   ["Plate set — see note below", "see errata", "Free to download at rememberforward.org"]]),
 ("note", STALE_COST),
 ("h1", "Closing The Capsule"),
 ("p", "There is no thread, no gasket, no tape and no epoxy in this design. HDPE is welded to "
       "itself, and the capsule is closed permanently."),
 ("p", "That is deliberate. Every re-openable seal is a permanent liability bought to serve a "
       "single event that will be destructive anyway — the finder will cut it open. A capsule "
       "with a 100-year gasket is a 100-year capsule no matter what it is made of. Sweden's "
       "KBS-3 nuclear canisters, designed for 100,000 years, use welded lids and no seal at all."),
 ("h2", "Method A — socket fusion (preferred)"),
 ("bullets", [
   "Heat the pipe end and the cap socket on the fusion iron until both surfaces are glossy — "
   "typically 200–220 °C, 8–12 seconds for 4\" pipe.",
   "Push together to the stop in one movement. Do not twist.",
   "Hold 60 seconds without moving. Leave undisturbed 30 minutes to cool fully.",
   "Do not exceed about 250 °C. Above that HDPE degrades rather than welds."]),
 ("h2", "Method B — hot plate"),
 ("bullets", [
   "Face both parts flat on a clean steel plate heated to 200–220 °C until a bead of melt "
   "appears around the edge.",
   "Press together squarely and hold until cool. A misaligned joint is a weak joint."]),
 ("h2", "Test before you load it"),
 ("bullets", [
   "Fuse one cap. Fill the tube with water, stand it upright 24 hours, check for weeping at "
   "the joint.",
   "Dry the inside completely. Load. Then fuse the second cap.",
   "Better: submerge the finished capsule and press gently. Any bubble is a failed weld."]),
 ("h1", "Burial Instructions"),
 ("bullets", [
   "Minimum depth 4 feet; 5 to 6 feet is better, and below the local frost line. Deeper than "
   "plough depth — cultivation reaches 8 to 12 inches.",
   "Orientation horizontal — this distributes soil pressure along the length rather than onto "
   "the welded ends.",
   "Surround with clean gravel before backfilling, for drainage.",
   "Mark with a COPPER or BRONZE stake driven 12 inches above the capsule. Earlier editions "
   "said \"non-ferrous (copper or stainless steel)\" — stainless steel is an iron alloy and is "
   "not non-ferrous. It will corrode and stain over this timescale.",
   "Trade-off worth knowing: a steel stake is far easier to find with a metal detector, but "
   "will not last. If findability matters more than the marker's own lifespan, set a steel "
   "plate ABOVE the capsule and accept that it is a century-scale marker, not a permanent one.",
   "Record GPS coordinates and a description by landmarks — distances from two prominent "
   "natural features — and store both in several places."]),
 ("h1", "Free Downloads"),
 ("p", "All SVG plate files, build guides, and this document are free at rememberforward.org — "
       "CC BY-SA 4.0, no permission needed."),
 ("footer", None),
]

GRANITE = [
 ("masthead", ("REMEMBER FORWARD", "TIER E · GRANITE VAULT",
               "The permanent institutional archive.",
               "$500–$1,500 · DESIGN TARGET 10,000+ YEARS · FIXED LOCATION")),
 ("h1", "What Changed In This Edition"),
 ("changed", [
   "This edition removes the lead lining and the poured lead seal specified through August 2026, "
   "and withdraws the claim of \"100,000+ years, the nuclear industry standard.\"",
   "That claim was wrong. The nuclear industry does not use lead-lined stone for archival "
   "containment. Sweden and Finland's KBS-3 design uses a copper canister over a cast-iron "
   "insert, surrounded by a bentonite clay buffer, in granitic bedrock. Lead appears in that "
   "industry only as radiation shielding in transport casks. And the 100,000-year figure is "
   "claimed for repository GEOLOGY behind a formal safety case — never for a container, and "
   "never by us.",
   "Lead is withdrawn on its own merits too: it creeps under sustained load so it cannot carry "
   "structure, it is toxic to cast and handle, and in the presence of moisture it forms a "
   "galvanic couple with titanium in which the lead is consumed. The molten-lead pouring step "
   "in earlier editions was also the most hazardous instruction in this entire project.",
   "What replaces it is better and cheaper: a bentonite clay buffer and a sealed inner vessel."]),
 ("h1", "Historical Precedent"),
 ("table", [
   ["Civilization", "Application", "Age", "Survival Status"],
   ["Ancient Egypt", "Granite sarcophagi and canopic jars", "3,000–5,000 years",
    "Contents intact in many cases"],
   ["Ancient Rome", "Stone sarcophagi", "2,000 years", "Many survive intact with contents"],
   ["Medieval Europe", "Stone church crypts", "500–1,000 years",
    "Most survive structurally intact"],
   ["Modern nuclear industry", "Copper canister in a bentonite buffer, in granitic bedrock (KBS-3)",
    "Designed for 100,000 years",
    "Engineering standard, not time-tested. Their safety case, not ours."],
   ["This project", "Civilizational knowledge archive", "Design target: 10,000 years",
    "Granite body, bentonite buffer, sealed inner vessel"]]),
 ("h1", "Why Granite"),
 ("h2", "Chemical properties"),
 ("p", "Granite is an igneous rock of quartz, feldspar and mica. It is chemically inert to "
       "virtually everything it will meet underground, it does not dissolve in groundwater on "
       "any timescale that matters here, and it is the host rock class that real deep "
       "repositories are actually built in."),
 ("h2", "Mechanical properties"),
 ("p", "Compressive strength of roughly 100 to 300 MPa. It will not be crushed by soil load, it "
       "will not deform, and unlike lead it does not creep. Granite carries the structure; "
       "nothing else in this design has to."),
 ("h1", "The Containment System — Three Layers"),
 ("h2", "Layer 1 — the granite body"),
 ("p", "Structural and inert. It resists load, roots, burrowing animals and casual disturbance. "
       "It is not, by itself, a seal — stone joints are never hermetic."),
 ("h2", "Layer 2 — bentonite clay buffer"),
 ("p", "This is the layer that does the work the lead was imagined to do, and it does it better. "
       "Sodium bentonite swells roughly ten to fifteen times its dry volume when it meets water, "
       "which means any crack, gap or void it can reach becomes self-sealing. It buffers the "
       "chemistry around the inner vessel and slows water movement to a crawl. It is the "
       "engineered barrier in every serious geological repository."),
 ("p", "Sourcing: sold as pond sealer, as drilling mud, and as unscented clumping cat litter. If "
       "you use cat litter, confirm it is sodium bentonite with no added fragrance, deodoriser "
       "or clumping agents."),
 ("h2", "Layer 3 — the sealed inner vessel"),
 ("p", "The only real barrier. Everything else buys it time."),
 ("bullets", [
   "BUILD IT YOURSELF: a fired ceramic vessel sealed with hot pine pitch. In this project's own "
   "ranking of seals, pitch on ceramic rates equal to cast lead — and it is non-toxic, needs no "
   "crucible, and is the same method as the Tier 0 capsule.",
   "COMMISSION IT: a welded titanium vessel, if an institution can have one made. No gasket, no "
   "joint compound, nothing to fail. Titanium welding needs argon shielding and back-purge; "
   "this is a fabrication-shop operation, not a workshop one. Do not attempt it with a "
   "hardware-store welder.",
   "DO NOT USE any gasket, O-ring or elastomer, whatever the datasheet claims. No elastomer has "
   "a validated multi-century life. A 10,000-year vault with a 100-year seal is a 100-year vault."]),
 ("h1", "Construction"),
 ("h2", "Step 1 — obtain or cut the granite"),
 ("p", "Six slabs: base, four sides, lid. Minimum 5 cm thick, ideally 8 to 10 cm. Monument yards "
       "and stone fabricators sell offcuts cheaply. Alternatively carve a cavity into a single "
       "block — slower, and the traditional method, with no joints to fail."),
 ("h2", "Step 2 — assemble the box"),
 ("p", "Dry-fit all six slabs and grind any gaps with a diamond disc. Bed the joints in lime "
       "mortar. Geopolymer — local clay or metakaolin with an alkali activator, cured at low "
       "temperature — is an alternative worth considering: durable, low-permeability, and "
       "makeable from local materials by anyone who finds this later."),
 ("h2", "Step 3 — prepare and seal the inner vessel"),
 ("bullets", [
   "Dry the plates and any other contents thoroughly. Moisture sealed in is moisture that stays in.",
   "Load the vessel with desiccant and oxygen absorbers. Oxygen is the main agent of decay once "
   "water is excluded.",
   "Seal it: pitch on ceramic, or a welded titanium lid. Seal it permanently. The finder will "
   "cut it open."]),
 ("h2", "Step 4 — pack with bentonite"),
 ("p", "Set the sealed vessel centrally in the granite cavity and pack dry sodium bentonite "
       "firmly all around it — a minimum of 5 cm on every face, including beneath. Leave no "
       "voids. Pack it dry: it is meant to swell later, when and if water ever arrives."),
 ("h2", "Step 5 — close and coat"),
 ("p", "Bed the lid on lime mortar and point the perimeter joint. When cured, coat the whole "
       "exterior in three or four layers of hot pine pitch or bitumen. This is a water-shedding "
       "layer, not a seal — it buys the mortar joints decades they would not otherwise have."),
 ("h1", "Burial and Placement"),
 ("p", "A vault of these dimensions weighs roughly 60 to 90 kg before contents. Plan the lift "
       "and the route before you build it, not after."),
 ("table", [
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
    "Self-sealing, dry, low oxygen. Requires an institutional agreement."]]),
 ("h1", "The Community Commitment"),
 ("p", "A granite vault is not just a container. It is heavy enough that it will not be moved "
       "casually, and permanent enough that it outlives whoever sites it. That makes siting it a "
       "decision about a place and the people in it, not a decision about a box."),
 ("p", "Consider inscribing on the exterior: the year of burial, a brief plain description of the "
       "contents, and the bridge phrase — \"This was made for you, freely, by people who "
       "remembered forward.\" Cut it deep. Raised letters abrade away first; a cut groove fills "
       "with dirt and gets easier to read, not harder."),
 ("footer", None),
]

DOCS = [("gd_09_flyer_hdpe", HDPE), ("gd_15_tiere_granite", GRANITE)]

if __name__ == "__main__":
    print("Reissuing flyers per AUDIT_2026-09-01 (docx + pdf from one source):")
    for name, blocks in DOCS:
        for ext, fn in ((".docx", render_docx), (".pdf", render_pdf)):
            p = os.path.join(HERE, name + ext)
            fn(blocks, p)
            print(f"  {os.path.getsize(p):>7,} B  containers/{name}{ext}")
