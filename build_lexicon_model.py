"""
Remember Forward - Lexicon Area & Cost Model
Builds lexicon_model.xlsx : a live, formula-driven model for the card-deck lexicon.

Change anything on the INPUTS sheet; every other sheet recalculates.
Density anchored on Memory of Mankind's published figures (see NOTES sheet).
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HDR = PatternFill("solid", fgColor="1F3864")
SUB = PatternFill("solid", fgColor="D9E2F3")
INP = PatternFill("solid", fgColor="FFF2CC")   # yellow = user-editable
GOOD = PatternFill("solid", fgColor="E2EFDA")
WHITE = Font(color="FFFFFF", bold=True, size=11)
B = Font(bold=True)
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()


def sheet(name, widths):
    ws = wb.create_sheet(name)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    return ws


def title(ws, row, text, span):
    ws.cell(row, 1, text).font = WHITE
    for c in range(1, span + 1):
        ws.cell(row, c).fill = HDR
    return row + 1


def hdrrow(ws, row, vals):
    for i, v in enumerate(vals, 1):
        c = ws.cell(row, i, v)
        c.font = B
        c.fill = SUB
        c.border = BOX
        c.alignment = Alignment(wrap_text=True, vertical="center")
    return row + 1


# ---------------------------------------------------------------- INPUTS
ws = wb.active
ws.title = "INPUTS"
for i, w in enumerate([38, 14, 12, 66], 1):
    ws.column_dimensions[get_column_letter(i)].width = w
r = title(ws, 1, "REMEMBER FORWARD - LEXICON MODEL  |  yellow cells are inputs, everything else is formula", 4)
r = hdrrow(ws, r, ["Parameter", "Value", "Unit", "Note"])


def inp(label, val, unit, note):
    global r
    ws.cell(r, 1, label).border = BOX
    c = ws.cell(r, 2, val)
    c.fill = INP
    c.border = BOX
    c.font = B
    ws.cell(r, 3, unit).border = BOX
    n = ws.cell(r, 4, note)
    n.border = BOX
    n.alignment = Alignment(wrap_text=True)
    ref = "INPUTS!$B$%d" % r
    r += 1
    return ref


def sect(text):
    global r
    ws.cell(r, 1, text).font = B
    for c in range(1, 5):
        ws.cell(r, c).fill = SUB
    r += 1


sect("LEXICON STRUCTURE")
T0 = inp("Tier 0 - semantic primes", 65, "words", "NSM primes (Wierzbicka). Fully pictogrammed, issued in every language.")
T1 = inp("Tier 1 - core vocabulary", 935, "words", "To ~1000 total: Ogden Basic English 850 + Swadesh 207, merged and deduped.")
T2 = inp("Tier 2 - long tail", 4000, "words", "To 5000 total. Defined strictly in Tier 1 vocabulary.")
HEADCH = inp("Chars per headword block", 22, "chars", "Headword + part of speech + the paired second-language headword (Arabic).")
DEFCH = inp("Chars per definition", 108, "chars", "~18 words. Restricted-vocabulary definitions run long; a 12-word def would be ~72.")
PICT0 = inp("Tier 0 pictogram coverage", 1.00, "fraction", "Every prime gets a pictogram.")
PICT1 = inp("Tier 1 pictogram coverage", 0.70, "fraction", "Most of Basic English is picturable.")
PICT2 = inp("Tier 2 pictogram coverage", 0.25, "fraction", "Abstract vocabulary resists depiction - this is the realistic ceiling.")
PICTMM = inp("Pictogram size (square edge)", 12, "mm", "12x12mm reads well unaided. Drives total area more than the text does.")
OVER = inp("Layout overhead", 0.40, "fraction", "Margins, rules, gutters, card edges, index furniture, holes.")

sect("DENSITY  (anchored on Memory of Mankind published specs)")
ANCHPT = inp("Anchor type size", 4, "pt", "MOM individual-design spec: text at least 4pt Arial.")
ANCHDEN = inp("Anchor density at that size", 1.25, "chars/mm2", "MOM: 50,000 chars per 20x20cm tablet = 50000/40000.")
MICRODEN = inp("Microfilm density", 125, "chars/mm2", "MOM ceramic microfilm: 5,000,000 chars per 20x20cm tablet. 5 lines/mm, needs 10x magnifier.")
PT_UN = inp("UNAIDED tier type size", 8, "pt", "~2mm cap height. Readable by aging eyes in poor light, no tools.")
PT_FINE = inp("FINE tier type size", 4, "pt", "Dictionary fine print. Young eye, or a cheap +3 reading lens.")

sect("PANELS")
TI_W = inp("Titanium panel width", 300, "mm", "Typical PCM panel; 600x300 is a standard tray size.")
TI_H = inp("Titanium panel height", 600, "mm", "")
TI_SIDES = inp("Titanium sides used", 2, "1 or 2", "PCM etches both sides in one pass - use 2.")
CE_W = inp("Ceramic tile width", 300, "mm", "NOT a ceramic limit. 20x20cm is MOM's ARCHIVE format. Large-format stoneware runs to 300x600.")
CE_H = inp("Ceramic tile height", 600, "mm", "Set 200/200 to model MOM archive tablets specifically.")
CE_SIDES = inp("Ceramic sides used", 2, "1 or 2", "MOM print one face because they stack tablets. Edge-set on stilts and you can fire both.")

sect("COST")
TI_THK = inp("Titanium thickness", 0.3, "mm", "0.2-0.5mm for cards. Thicker = stiffer but heavier deck.")
TI_KG = inp("Titanium Grade 2 price", 40, "$/kg", "Range $30-50/kg for sheet.")
TI_DEN = inp("Titanium density", 4.51, "g/cm3", "Grade 2. Fixed physical constant - do not edit.")
TI_ETCH = inp("PCM etch cost per panel", 28, "$/panel", "Qty 100. Ti needs HF/nitric - fewer vendors, 1.5-2.5x stainless. Cost is per AREA, not per mark.")
TI_TOOL = inp("PCM phototool per design", 250, "$/design", "One-time per unique panel artwork.")
sect("CERAMIC - MAKE IN HOUSE (cost built up from components, not a placeholder)")
CL_THK = inp("Tile thickness", 6, "mm", "6mm resists warping at large format. Thicker = heavier, more clay, slower firing.")
CL_DEN = inp("Clay density (fired stoneware)", 2.3, "g/cm3", "Physical constant - do not edit.")
CL_KG = inp("Clay price", 1.00, "$/kg", "Stoneware body in quantity. Cheap; never the driver.")
GLAZE = inp("Glaze per tile", 0.30, "$/tile", "Thin roller coat, MOM style.")
KWH = inp("Kiln energy per firing", 70, "kWh", "~7 cu ft kiln to cone 6.")
ELEC = inp("Electricity", 0.20, "$/kWh", "")
PERFIRE = inp("Tiles per firing", 30, "tiles", "Large-format tiles need shelf space; 20x20 tablets would fit far more.")
KILNMULT = inp("Kiln wear multiplier", 2.0, "x", "Doubles energy cost to cover elements, furniture, vent, maintenance.")
SCRAP = inp("Ceramic scrap / breakage", 0.12, "fraction", "Warping, cracking, glaze faults. Brittle medium - budget for it.")
CE_TOOL = inp("Ceramic setup per design", 150, "$/design", "Decal film or laser file prep.")

sect("MARKING - the real cost driver")
CHRATE = inp("Laser marking rate", 50, "chars/sec", "Galvo fiber laser, quality vector engraving. THIS IS PER-MARK, so it scales with CHARACTER COUNT, not area.")
SHOPRATE = inp("Machine + operator rate", 60, "$/hr", "Loaded shop rate.")
DECAL_M2 = inp("Ceramic decal print", 45, "$/m2", "Screen or laser-toner ceramic decal. PER-AREA - detail is free. This is how ceramic gets cheap at volume.")
QTY = inp("Kits in the run", 100, "kits", "Tooling amortizes over this. Drives $/word more than anything else.")

sect("CERAMIC - BUY FROM MOM (archival service, NOT a manufacturing cost)")
EURUSD = inp("EUR to USD", 1.08, "rate", "")
MOM11 = inp("MOM 1/1 tablet", 195, "EUR", "Buys a SLOT IN THE HALLSTATT ARCHIVE + certificate + token. Not a way to source tablets.")
MOM11D = inp("MOM 1/1 + duplicate", 455, "EUR", "The interesting one: archived tablet AND a physical duplicate back to you, + token.")
MOM14 = inp("MOM 1/4 tablet", 78, "EUR", "Cheapest way in, and it still includes a token.")

sect("MOM COLLABORATION")
TOKQTY = inp("MOM tokens per capsule", 2, "tokens", "One extractable and carryable, one stays with the capsule.")
TOKCOST = inp("Token cost", 25, "$/token", "PLACEHOLDER - ask Kunze about bulk supply.")

# ---------------------------------------------------------------- DENSITY
ws = sheet("DENSITY", [32, 14, 16, 16, 16, 56])
r = title(ws, 1, "CHARACTER DENSITY vs TYPE SIZE   (area scales as pt^2, calibrated to the MOM anchor)", 6)
r = hdrrow(ws, r, ["Mode", "Type size (pt)", "Cap height (mm)", "Chars / mm2", "mm2 / char", "Reality check"])
modes = [
    ("Large / Tier 0 display", 12, "Headline scale. Used for primes and card titles."),
    ("Unaided (poor light, old eyes)", "=" + PT_UN, "The floor for 'no tools required'. ~2mm cap height."),
    ("Compact unaided", 6, "Newspaper body text. Most adults, decent light."),
    ("Fine / MOM standard", "=" + PT_FINE, "MOM's own minimum for direct-read tablets. 50,000 chars per 20x20cm."),
    ("Very fine (Ti PCM limit)", 2, "PCM min feature 0.1mm allows this. Needs a lens."),
]
first_data = r
for name, pt, note in modes:
    ws.cell(r, 1, name).border = BOX
    ws.cell(r, 2, pt).border = BOX
    ws.cell(r, 3, "=ROUND(B%d*0.3528*0.7,2)" % r).border = BOX
    c = ws.cell(r, 4, "=ROUND(%s*(%s/B%d)^2,3)" % (ANCHDEN, ANCHPT, r))
    c.border = BOX
    c.font = B
    ws.cell(r, 5, "=ROUND(1/D%d,3)" % r).border = BOX
    n = ws.cell(r, 6, note)
    n.border = BOX
    n.alignment = Alignment(wrap_text=True)
    r += 1
ws.cell(r, 1, "CERAMIC MICROFILM").border = BOX
ws.cell(r, 1).font = B
ws.cell(r, 2, "~0.5").border = BOX
ws.cell(r, 3, "5 lines/mm").border = BOX
c = ws.cell(r, 4, "=" + MICRODEN)
c.border = BOX
c.font = B
c.fill = GOOD
ws.cell(r, 5, "=ROUND(1/D%d,4)" % r).border = BOX
n = ws.cell(r, 6, "MOM ceramic microfilm. 5,000,000 chars per 20x20cm tablet. REQUIRES a 10x magnifier - hard dependency, see NOTES.")
n.border = BOX
n.alignment = Alignment(wrap_text=True)
MICRO_ROW = r
UNAIDED_ROW = first_data + 1
FINE_ROW = first_data + 3
r += 2
ws.cell(r, 1, "Density gap between FINE and MICROFILM is ~100x. That gap is the whole ceramic argument.").font = Font(italic=True)

# ---------------------------------------------------------------- LEXICON
ws = sheet("LEXICON", [24, 12, 14, 14, 18, 18, 16, 14])
r = title(ws, 1, "LEXICON CONTENT -> AREA REQUIRED", 8)
r = hdrrow(ws, r, ["Tier", "Words", "Chars/entry", "Total chars", "Text area @UNAIDED (mm2)",
                   "Text area @FINE (mm2)", "Pictogram area (mm2)", "Pictograms"])
tiers = [("Tier 0 - primes", T0, PICT0), ("Tier 1 - core", T1, PICT1), ("Tier 2 - long tail", T2, PICT2)]
tr0 = r
for label, cnt, pf in tiers:
    ws.cell(r, 1, label).border = BOX
    ws.cell(r, 2, "=" + cnt).border = BOX
    ws.cell(r, 3, "=%s+%s" % (HEADCH, DEFCH)).border = BOX
    ws.cell(r, 4, "=B%d*C%d" % (r, r)).border = BOX
    ws.cell(r, 5, "=D%d*DENSITY!$E$%d" % (r, UNAIDED_ROW)).border = BOX
    ws.cell(r, 6, "=D%d*DENSITY!$E$%d" % (r, FINE_ROW)).border = BOX
    ws.cell(r, 8, "=ROUND(B%d*%s,0)" % (r, pf)).border = BOX
    ws.cell(r, 7, "=H%d*%s^2" % (r, PICTMM)).border = BOX
    r += 1
tr1 = r - 1
ws.cell(r, 1, "TOTAL").font = B
for col in [2, 4, 5, 6, 7, 8]:
    L = get_column_letter(col)
    c = ws.cell(r, col, "=SUM(%s%d:%s%d)" % (L, tr0, L, tr1))
    c.font = B
    c.fill = SUB
    c.border = BOX
TOT_ROW = r
r += 2
ws.cell(r, 1, "AREA ROLL-UP (includes overhead)").font = B
r += 1
r = hdrrow(ws, r, ["Build", "Raw area mm2", "With overhead mm2", "m2", "", "", "", ""])
ws.cell(r, 1, "UNAIDED everywhere").border = BOX
ws.cell(r, 2, "=E%d+G%d" % (TOT_ROW, TOT_ROW)).border = BOX
ws.cell(r, 3, "=B%d*(1+%s)" % (r, OVER)).border = BOX
ws.cell(r, 4, "=ROUND(C%d/1000000,3)" % r).border = BOX
A_UN = r
r += 1
ws.cell(r, 1, "FINE text + pictograms").border = BOX
ws.cell(r, 2, "=F%d+G%d" % (TOT_ROW, TOT_ROW)).border = BOX
ws.cell(r, 3, "=B%d*(1+%s)" % (r, OVER)).border = BOX
ws.cell(r, 4, "=ROUND(C%d/1000000,3)" % r).border = BOX
A_FINE = r
r += 1
ws.cell(r, 1, "MICROFILM text only").border = BOX
ws.cell(r, 2, "=D%d*DENSITY!$E$%d" % (TOT_ROW, MICRO_ROW)).border = BOX
ws.cell(r, 3, "=B%d*(1+%s)" % (r, OVER)).border = BOX
ws.cell(r, 4, "=ROUND(C%d/1000000,4)" % r).border = BOX
for c in range(1, 5):
    ws.cell(r, c).fill = GOOD
A_MICRO = r

# ---------------------------------------------------------------- MEDIA
ws = sheet("MEDIA", [34, 13, 15, 11, 12, 12, 13, 13, 40])
r = title(ws, 1, "MEDIA COMPARISON - substrate cost and marking cost kept SEPARATE, because they scale differently", 9)
r += 1
ws.cell(r, 1, "KEY: substrate cost scales with AREA. Marking cost scales with AREA (etch/decal) or CHARACTER COUNT (laser). "
              "That difference, not the material, is what decides the price.").font = Font(italic=True, bold=True)
r += 2
r = hdrrow(ws, r, ["Build", "Area (m2)", "Usable/sheet (mm2)", "Sheets",
                   "Substrate $", "Marking $", "Tooling $", "TOTAL $/set", "Note"])

# component cost strings
TI_MAT = "(%s*%s*%s/1000*%s/1000*%s)" % (TI_W, TI_H, TI_THK, TI_DEN, TI_KG)
CE_MAT = ("(%s*%s*%s/1000*%s/1000*%s+%s)*(1+%s)" %
          (CE_W, CE_H, CL_THK, CL_DEN, CL_KG, GLAZE, SCRAP))
CE_FIRE = "(%s*%s/%s*%s)" % (KWH, ELEC, PERFIRE, KILNMULT)
LASER_SET = "(LEXICON!D%d/%s/3600*%s)" % (TOT_ROW, CHRATE, SHOPRATE)  # whole-set laser time


def media(label, area_row, pw, ph, sides, sub_per_sheet, marking, tool, note, hi=False):
    global r
    ws.cell(r, 1, label).border = BOX
    ws.cell(r, 2, "=LEXICON!D%d" % area_row).border = BOX
    ws.cell(r, 3, "=%s*%s*%s" % (pw, ph, sides)).border = BOX
    c = ws.cell(r, 4, "=ROUNDUP(B%d*1000000/C%d,0)" % (r, r))
    c.border = BOX
    c.font = B
    ws.cell(r, 5, "=ROUND(D%d*%s,2)" % (r, sub_per_sheet)).border = BOX
    ws.cell(r, 6, "=ROUND(%s,2)" % marking).border = BOX
    ws.cell(r, 7, "=ROUND(D%d*%s/%s,2)" % (r, tool, QTY)).border = BOX
    t = ws.cell(r, 8, "=ROUND(E%d+F%d+G%d,2)" % (r, r, r))
    t.border = BOX
    t.font = B
    n = ws.cell(r, 9, note)
    n.border = BOX
    n.alignment = Alignment(wrap_text=True)
    if hi:
        for col in [1, 4, 8]:
            ws.cell(r, col).fill = GOOD
    row = r
    r += 1
    return row


m_ti_un = media("TITANIUM PCM - unaided 8pt", A_UN, TI_W, TI_H, TI_SIDES, TI_MAT,
                "D%d*%s" % (r, TI_ETCH), TI_TOOL,
                "No tools needed anywhere. Most robust, most panels.")
m_ti_fine = media("TITANIUM PCM - fine 4pt", A_FINE, TI_W, TI_H, TI_SIDES, TI_MAT,
                  "D%d*%s" % (r, TI_ETCH), TI_TOOL,
                  "PCM min feature 0.1mm, so 4pt is easy. NO LASER AT ALL - the whole panel etches at once in a bath. "
                  "This is why titanium is cheap: marking is per-area.", hi=True)
m_ce_dec = media("CERAMIC + DECAL - fine 4pt", A_FINE, CE_W, CE_H, CE_SIDES, "(%s+%s)" % (CE_MAT, CE_FIRE),
                 "B%d*%s" % (r, DECAL_M2), CE_TOOL,
                 "Screen / laser-toner ceramic decal, then fire. PER-AREA like PCM. 300dpi COLOUR, which titanium "
                 "cannot do. This is the ceramic build for any real quantity.", hi=True)
m_ce_las = media("CERAMIC + LASER - fine 4pt", A_FINE, CE_W, CE_H, CE_SIDES, "(%s+%s)" % (CE_MAT, CE_FIRE),
                 LASER_SET, CE_TOOL,
                 "MOM's own method (engrave, then roller-glaze). Marking is PER-MARK: see MARKING TIME below. "
                 "Fine for one-offs, brutal at qty 100.")
m_ce_mic = media("CERAMIC MICROFILM + LASER", A_MICRO, CE_W, CE_H, CE_SIDES, "(%s+%s)" % (CE_MAT, CE_FIRE),
                 LASER_SET, CE_TOOL,
                 "Substrate cost collapses to almost nothing - but marking does NOT, because laser time tracks "
                 "character count, not area. Microfilm saves material, never machine time.")

r += 1
ws.cell(r, 1, "MARKING TIME (laser paths only) - the number that actually decides buy vs build").font = B
r += 1
r = hdrrow(ws, r, ["Metric", "Value", "", "", "", "", "", "", ""])
for lbl, f in [("Characters in the lexicon", "=LEXICON!D%d" % TOT_ROW),
               ("Laser hours per SET", "=ROUND(LEXICON!D%d/%s/3600,2)" % (TOT_ROW, CHRATE)),
               ("Laser hours for the whole RUN", "=ROUND(LEXICON!D%d/%s/3600*%s,0)" % (TOT_ROW, CHRATE, QTY)),
               ("Laser $ per set", "=ROUND(%s,2)" % LASER_SET)]:
    ws.cell(r, 1, lbl).border = BOX
    c = ws.cell(r, 2, f)
    c.border = BOX
    c.font = B
    r += 1
ws.cell(r, 1, "MOM absorb this only because Workshop of Photonics built them a purpose-made laser system, and because "
              "they make ONE-OFF tablets, not runs of 100.").font = Font(italic=True)
r += 2

ws.cell(r, 1, "COST PER WORD").font = B
r += 1
r = hdrrow(ws, r, ["Build", "$ / word", "", "", "", "", "", "", ""])
for lbl, row in [("Titanium PCM fine", m_ti_fine), ("Ceramic + decal fine", m_ce_dec),
                 ("Ceramic + laser fine", m_ce_las), ("Ceramic microfilm + laser", m_ce_mic)]:
    ws.cell(r, 1, lbl).border = BOX
    ws.cell(r, 2, "=ROUND(H%d/LEXICON!B%d,4)" % (row, TOT_ROW)).border = BOX
    r += 1

r += 1
ws.cell(r, 1, "BUYING FROM MOM - an archival SERVICE, not a way to source tablets").font = B
r += 1
r = hdrrow(ws, r, ["Product", "EUR", "USD", "What it actually buys", "", "", "", "", ""])
for lbl, eur, what in [
    ("MOM 1/4 tablet", MOM14, "Cheapest entry. Slot in the Hallstatt salt mine + certificate + TOKEN."),
    ("MOM 1/1 tablet", MOM11, "Full tablet archived at Hallstatt + certificate + token."),
    ("MOM 1/1 + duplicate", MOM11D, "THE ONE TO WANT: archived at Hallstatt AND a physical duplicate mailed back "
                                    "for your own capsule. Pointer runs both directions."),
]:
    ws.cell(r, 1, lbl).border = BOX
    ws.cell(r, 2, "=" + eur).border = BOX
    ws.cell(r, 3, "=ROUND(%s*%s,2)" % (eur, EURUSD)).border = BOX
    n = ws.cell(r, 4, what)
    n.border = BOX
    n.alignment = Alignment(wrap_text=True)
    r += 1
ws.cell(r, 1, "You buy 1-2 of these as a COLLABORATION. You never buy 27 to source substrate - that would be paying "
              "MOM to archive 27 tablets in Austria, which is not the goal.").font = Font(italic=True)

r += 1
ws.cell(r, 1, "RECOMMENDED BUILD - all three layers, deliberately").font = B
r += 1
r = hdrrow(ws, r, ["Layer", "Medium", "Sheets", "", "", "Why"])
rec = [
    ("Unaided core (Tier 0+1)", "Ceramic, colour",
     "=ROUNDUP((SUM(LEXICON!E%d:E%d)+SUM(LEXICON!G%d:G%d))*(1+%s)/(%s*%s*%s),0)"
     % (tr0, tr0 + 1, tr0, tr0 + 1, OVER, CE_W, CE_H, CE_SIDES),
     "300dpi colour pictograms, no tools needed, MOM-proven in a salt mine. This layer is the expensive one - unaided legibility, not vocabulary size, is what costs area."),
    ("Full lexicon, carried", "Titanium PCM 4pt", "=D%d" % m_ti_fine,
     "Unbreakable, thin, snap-out cards, half-etch relief doubles as a printing plate."),
    ("Full lexicon, archived", "Ceramic microfilm", "=D%d" % m_ce_mic,
     "~100x denser. Full redundancy at near-zero marginal area."),
    ("Magnifier", "Glass / fused silica", 1,
     "Converts the microfilm dependency from a gamble into a supplied tool."),
    ("MOM tokens", "Ceramic", "=" + TOKQTY,
     "Points the finder at a second archive. Network topology, not an isolated deposit."),
]
for lbl, med, sh, why in rec:
    ws.cell(r, 1, lbl).border = BOX
    ws.cell(r, 2, med).border = BOX
    ws.cell(r, 3, sh).border = BOX
    n = ws.cell(r, 6, why)
    n.border = BOX
    n.alignment = Alignment(wrap_text=True)
    r += 1

# ---------------------------------------------------------------- CARDS
ws = sheet("CARDS", [34, 18, 16, 18, 56])
r = title(ws, 1, "CARD FORMAT - how the lexicon divides into carryable cards", 5)
r = hdrrow(ws, r, ["Card format", "Area both sides (mm2)", "Entries per card", "Cards for whole lexicon", "Note"])
cards = [
    ("ID-1 / membership card 85.6x54", 85.6, 54, "ISO 7810 ID-1. RECOMMENDED - the carrying unit is a topic, not a word."),
    ("Key tag ~54x30", 54, 30, "Too few entries per card; 450+ cards is unsortable and loss-prone."),
    ("Large card 105x74 (A7)", 105, 74, "Fewer cards, less pocketable. Good for the Tier 0 pictogram set."),
    ("One word per card", 85.6, 54, "5000 loose objects, 30-40% of area lost to edges and holes. Rejected."),
]
cr0 = r
for lbl, w, h, note in cards:
    ws.cell(r, 1, lbl).border = BOX
    ws.cell(r, 2, "=%s*%s*2" % (w, h)).border = BOX
    if lbl.startswith("One word"):
        ws.cell(r, 3, 1).border = BOX
        ws.cell(r, 4, "=LEXICON!B%d" % TOT_ROW).border = BOX
    else:
        ws.cell(r, 3, "=ROUNDDOWN(B%d/(LEXICON!C%d/LEXICON!B%d),0)" % (r, A_FINE, TOT_ROW)).border = BOX
        ws.cell(r, 4, "=ROUNDUP(LEXICON!B%d/C%d,0)" % (TOT_ROW, r)).border = BOX
    n = ws.cell(r, 5, note)
    n.border = BOX
    n.alignment = Alignment(wrap_text=True)
    r += 1
ID1 = cr0
r += 1
ws.cell(r, 1, "DECK PHYSICALS (ID-1 in titanium)").font = B
r += 1
mass_row = r
ws.cell(r, 1, "Mass per card (g)").border = BOX
ws.cell(r, 2, "=ROUND(85.6*54*%s/1000*%s,2)" % (TI_THK, TI_DEN)).border = BOX
ws.cell(r, 2).font = B
r += 1
ws.cell(r, 1, "Whole-deck mass (g)").border = BOX
ws.cell(r, 2, "=ROUND(B%d*D%d,0)" % (mass_row, ID1)).border = BOX
ws.cell(r, 2).font = B
r += 1
ws.cell(r, 1, "Whole-deck thickness (mm)").border = BOX
ws.cell(r, 2, "=ROUND(%s*D%d,0)" % (TI_THK, ID1)).border = BOX
ws.cell(r, 2).font = B
r += 1
ws.cell(r, 1, "Cards you actually carry (20%)").border = BOX
ws.cell(r, 2, "=ROUNDUP(D%d*0.2,0)" % ID1).border = BOX
ws.cell(r, 2).font = B
r += 2
ws.cell(r, 1, "You never carry the whole deck - that is the point of cards. Carry the Tier 0 set plus today's topic.").font = Font(italic=True)

# ---------------------------------------------------------------- NOTES
ws = sheet("NOTES", [4, 120])
r = title(ws, 1, "FINDINGS, CAVEATS, SOURCES", 2)
notes = [
    ("H", "CORRECTION - ceramic CAN carry the full 5000 words, and pictograms belong on both media"),
    ("", "The 0.30mm minimum-feature figure in plates/plate_profiles.py is a property of an assumed PROCESS"),
    ("", "(hand carving / underglaze brush / coarse decal), not of ceramic itself. MOM laser-engrave the tablet and"),
    ("", "then roller-apply glaze over it, so the mark sits in a recess under glass: no pigment bleed, no abrasion path."),
    ("", "That is how they reach 5 lines/mm. ACTION: split the CERAMIC profile into CERAMIC_HAND (0.30mm) and"),
    ("", "CERAMIC_LASER (~0.05mm) in plate_profiles.py, and stop treating 0.30mm as a material constant."),
    ("", "Ceramic also does 300dpi colour, which titanium cannot - anodising gives interference colour, not halftone."),
    ("", "So ceramic should carry the RICHER pictograms and titanium the monochrome line versions. Both get pictograms."),
    ("", ""),
    ("H", "The real trade is the magnification dependency, not resolution"),
    ("", "Microfilm mode needs a 10x lens. For a project whose premise is 'no presumed viewer', that is a hard dependency."),
    ("", "Three mitigations, use all of them: (1) ship a glass or fused-silica lens in the capsule - glass itself lasts"),
    ("", "millennia; (2) borrow the Long Now Rosetta Disk trick - a visible ramp of decreasing type that announces"),
    ("", "'this needs magnification' and demonstrates the scale; (3) never let microfilm be load-bearing. It is"),
    ("", "redundancy. The unaided tier stays complete on its own - the same rule already set for colour:"),
    ("", "may differentiate, never signify."),
    ("", ""),
    ("H", "Per-area vs per-mark still holds"),
    ("", "PCM and ceramic decal cost by area - once tooling exists, extra detail is free. Fibre-laser marking costs by"),
    ("", "mark: ~1.6 m2 of dense filled text is 7-13 machine-hours per set. MOM absorb this only because Workshop of"),
    ("", "Photonics built them a purpose-made laser system - their capital cost, not ours."),
    ("", "=> BUYING ceramic capacity from MOM may beat the $2,200-7,500 in-house kiln estimate until volume justifies it."),
    ("", ""),
    ("H", "NO STEEL - standing constraint as of 2026-09-01"),
    ("", "Kills the 316L card-stock option AND the enamel-on-steel fast-prototype route in the materials notes."),
    ("", "Prototype substitute: anodised aluminium. Cheap, laser-markable, and a valve metal, so it is a true analogue"),
    ("", "for titanium anodising trials. Not archival - prototypes only. Anything that ships is titanium or ceramic."),
    ("", ""),
    ("H", "MOM collaboration - tokens in every capsule"),
    ("", "Two tokens per capsule is correct design: one extractable and carryable, one that stays with the capsule."),
    ("", "Turns each deposit into a node pointing at another archive - network topology instead of isolated caches."),
    ("", "Reciprocity: submit a Remember Forward tablet into the MOM archive so the pointer runs both directions."),
    ("", "Tokens ship bundled with MOM tablet purchases, so buying ceramic capacity also sources tokens."),
    ("", "Ask Kunze about bulk token supply and about a reciprocal deposit."),
    ("", "CAVEAT: a pointer to Hallstatt only helps if Hallstatt survives and the finder can travel. Additive, never load-bearing."),
    ("", ""),
    ("H", "What is actually hard"),
    ("", "Not the manufacturing. Writing 5000 non-circular definitions inside a ~1000-word controlled vocabulary is"),
    ("", "600,000+ characters of tightly constrained prose, and circularity is easy to introduce and hard to detect."),
    ("", "Needs a dependency checker: parse every definition, verify every token exists in a strictly lower tier."),
    ("", "Months, not weeks."),
    ("", ""),
    ("H", "SOURCES"),
    ("", "MOM specs: memory-of-mankind.com/how-is-information-kept-legible-for-1-million-years/"),
    ("", "  - 20x20cm tablet, up to 5,000,000 chars (ceramic microfilm, 5 lines/mm, 10x magnifier)"),
    ("", "  - individual-design option: min 4pt Arial, up to 50,000 chars (~20 A4 pages), photos 300dpi"),
    ("", "  - laser engraved, then alkali/acid/temperature-resistant glaze roller-applied, stable to 1300C"),
    ("", "MOM tablet + token product: memory-of-mankind.com/product/1-1-tablet-in-the-mom-archiv-plus-token-by-mail/"),
    ("", "American Ceramic Society: ceramics.org/ceramic-tech-today/ceramic-tablets-may-help-preserve-the-worlds-knowledge-for-future-generations/"),
    ("", "Laser system: wophotonics.com/news/wop-developed-laser-system-for-memory-of-mankind-project-delivered-to-vienna/"),
    ("", "Defining vocabularies: NSM primes ~65 (Wierzbicka); Ogden Basic English 850; Swadesh 207; Longman Defining Vocabulary ~2000."),
    ("", ""),
    ("H", "OPEN - not decided"),
    ("", "1. Buy ceramic from MOM, or build in-house kiln capability?"),
    ("", "2. Titanium thickness for the card deck (0.2 / 0.3 / 0.5mm) - stiffness vs deck mass."),
    ("", "3. Half-etch relief (printing plate) vs recessed and oxide-filled (contrast). Can one panel do both?"),
    ("", "4. Build 500 as a proof first, or go straight to 5000?"),
    ("", "5. Which lens ships in the capsule, and does it need its own instruction plate?"),
]
for kind, text in notes:
    c = ws.cell(r, 2, text)
    if kind == "H":
        c.font = B
        c.fill = SUB
    r += 1

wb.save(r"C:\Users\kanta\Documents\remember-forward\lexicon_model.xlsx")
print("wrote lexicon_model.xlsx")
