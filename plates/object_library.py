"""
Remember Forward - OBJECT LIBRARY
The drawn primitives the 89 plates are composed from.

WHY THIS FILE EXISTS
  Building A01 showed that five object types (figure, hand, stone, vessel, flame)
  consumed nearly all the effort, and that those same five recur across dozens of
  plates. Drawing them once per plate would mean redrawing the pot six times.
  Library first, plates second: 89 drawing problems become N draw-once problems
  plus 89 COMPOSITION problems.

THE FINDING THAT SHAPES THE WHOLE LIBRARY
  Word reuse is NOT object reuse. The most-repeated words across the 89 plates are
  dry, cut, mark, carry, cool, turn, before, after, hot - actions and properties,
  not things. So the library is not a library of nouns. It splits four ways:

    GRAMMAR   marks that carry the reading system itself. Tiny set, every plate.
    FIGURE    one base body in many poses. Carries every ACTION word.
    PARTS     body parts and anatomy.
    NATURE    the non-made world.
    LIVING    body plans and plant forms - never species.
    MADE      the long tail of human things. Biggest set, thinnest reuse.

  PROPERTIES COST NOTHING. big/small, hot/cold, wet/dry, near/far, good/bad need
  no primitive at all - they are ARRAY grammar, the same object drawn twice with
  one thing changed. That is why they top the reuse table and yet add zero to this
  file. Roughly a fifth of the lexicon is free for this reason.

STATUS: inventory only. Nothing here is drawn yet except what A01 already built,
marked DONE below.
"""

KINDS = {
    "GRAMMAR": "Marks that carry the reading system. Drawn once, used on every plate.",
    "FIGURE":  "One base body, many poses. Every action word resolves to a pose.",
    "PARTS":   "Body parts and internal anatomy.",
    "NATURE":  "The non-made world: water, fire, earth, sky, stone, weather.",
    "LIVING":  "Body plans and plant forms. Never species - distributions shift.",
    "MADE":    "Human things. The long tail: biggest set, thinnest reuse.",
}

# name, kind, status, note
PRIMITIVES = [
 # ---------------------------------------------------------------- GRAMMAR (14)
 ("callout bubble",      "GRAMMAR", "DONE", "Numbered circle. The single most important mark in the system."),
 ("leader line",         "GRAMMAR", "DONE", "Stops at the bubble edge, never touches it."),
 ("panel border",        "GRAMMAR", "DONE", "One panel = one moment."),
 ("sequence arrow",      "GRAMMAR", "DONE", "Between panels. Time passing."),
 ("motion arrow",        "GRAMMAR", "DONE", "Inside a panel. From one thing to another."),
 ("mayan numeral 0-19",  "GRAMMAR", "DONE", "Dot, bar, shell. Taught by counted stones on A01."),
 ("motion ticks",        "GRAMMAR", "DONE", "Short marks trailing a moving thing."),
 ("ground line",         "GRAMMAR", "DONE", "Establishes down. Load-bearing for the gravity argument."),
 ("hand-sign 'do this'", "GRAMMAR", "DONE", "A hand performing the act = an instruction, not a description."),
 ("thought enclosure",   "GRAMMAR", "",     "Contains a picture of the thing thought about. Needed by A04, K01."),
 ("speech mark",         "GRAMMAR", "",     "From the mouth. Needed by A04, J05, J06, K01."),
 ("cutaway hatch",       "GRAMMAR", "",     "Marks a cut face. Needed by every cross-section: B02, C06, F01, G08."),
 ("scale reference bar", "GRAMMAR", "",     "Engraved on the plate edge. I01 makes the plate itself the standard."),
 ("enlargement frame",   "GRAMMAR", "",     "Detail blown up, tied back to its place on the whole."),

 # ---------------------------------------------------------------- FIGURE (46)
 ("figure: stand",       "FIGURE", "DONE", "The base silhouette everything else is a variant of."),
 ("figure: lying",       "FIGURE", "DONE", "Horizontal on a ground line. A collapsed VERTICAL figure reads as a skirt."),
 ("figure: drink",       "FIGURE", "WEAK", "Failed three passes on A01. Vessel must meet the mouth. Needs an artist."),
 ("figure: point",       "FIGURE", "DONE", "Arm out. Used for naming and for indicating."),
 ("figure: walk",        "FIGURE", "", ""),
 ("figure: run",         "FIGURE", "", ""),
 ("figure: sit",         "FIGURE", "", ""),
 ("figure: squat",       "FIGURE", "", "Working posture. Very common across C, E, F, G."),
 ("figure: kneel",       "FIGURE", "", ""),
 ("figure: bend over",   "FIGURE", "", ""),
 ("figure: sleep",       "FIGURE", "", ""),
 ("figure: carry on back",     "FIGURE", "", ""),
 ("figure: carry on head",     "FIGURE", "", ""),
 ("figure: carry on shoulder", "FIGURE", "", ""),
 ("figure: two carrying",      "FIGURE", "", "Cooperation shown as a mechanical fact. J01."),
 ("figure: lift",        "FIGURE", "", ""),
 ("figure: push",        "FIGURE", "", ""),
 ("figure: pull",        "FIGURE", "", ""),
 ("figure: drag",        "FIGURE", "", ""),
 ("figure: strike down", "FIGURE", "", "Hammer, axe, adze, knapping. Very high reuse across G and H."),
 ("figure: chop",        "FIGURE", "", ""),
 ("figure: dig",         "FIGURE", "", "Appears in C01, D04, F01, F03, F05, G07."),
 ("figure: throw",       "FIGURE", "", ""),
 ("figure: reach up",    "FIGURE", "", ""),
 ("figure: hold out",    "FIGURE", "", ""),
 ("figure: give",        "FIGURE", "", "J02 trade, J08 strangers."),
 ("figure: take",        "FIGURE", "", ""),
 ("figure: eat",         "FIGURE", "", ""),
 ("figure: cut with knife", "FIGURE", "", ""),
 ("figure: grind",       "FIGURE", "", ""),
 ("figure: stir",        "FIGURE", "", ""),
 ("figure: pour",        "FIGURE", "", ""),
 ("figure: tie",         "FIGURE", "", ""),
 ("figure: weave",       "FIGURE", "", ""),
 ("figure: spin thread", "FIGURE", "", ""),
 ("figure: paddle",      "FIGURE", "", "H07 boats."),
 ("figure: climb",       "FIGURE", "", ""),
 ("figure: speaking",    "FIGURE", "", "With speech mark. A04, J05, J06, K01, K03."),
 ("figure: listening",   "FIGURE", "", ""),
 ("figure: sick",        "FIGURE", "", "Distinct from lying - upright but bent, sweating."),
 ("figure: child",       "FIGURE", "", "Proportion, not size: bigger head ratio."),
 ("figure: elder",       "FIGURE", "", "Stooped, staff."),
 ("figure: pregnant",    "FIGURE", "", "B05."),
 ("figure: infant",      "FIGURE", "", ""),
 ("group: two",          "FIGURE", "", "Group-COUNT is the agreed grammar for governance, not diminished posture."),
 ("group: many",         "FIGURE", "", "J03, J06, J07. Unblocks the diminished-figure problem."),

 # ---------------------------------------------------------------- PARTS (17)
 ("hand: open",          "PARTS", "DONE", "Fingers must stay separate at 0.10 mm."),
 ("hand: gripping",      "PARTS", "", "Every tool-use plate needs this."),
 ("hand: pinching",      "PARTS", "", "Fine work: needle, seed, spark."),
 ("hand: pointing",      "PARTS", "", ""),
 ("two hands working",   "PARTS", "", "Cordage reverse-wrap, tying, weaving. G01 depends on it."),
 ("foot",                "PARTS", "", ""),
 ("eye",                 "PARTS", "", ""),
 ("ear",                 "PARTS", "", ""),
 ("mouth",               "PARTS", "", ""),
 ("head profile",        "PARTS", "", ""),
 ("tooth",               "PARTS", "", ""),
 ("skeleton",            "PARTS", "", "B02."),
 ("heart and lungs",     "PARTS", "", ""),
 ("gut",                 "PARTS", "", ""),
 ("skin cross-section",  "PARTS", "", "Wounds, burns, frostbite. D01, D02."),
 ("muscle / sinew",      "PARTS", "", "Also a MATERIAL - E05 butchering feeds G01."),
 ("blood",               "PARTS", "", ""),

 # ---------------------------------------------------------------- NATURE (29)
 ("water: wavy lines",   "NATURE", "DONE", "Highest cross-cultural reliability. NEVER a teardrop."),
 ("water: body/pool",    "NATURE", "", ""),
 ("water: flowing",      "NATURE", "", ""),
 ("rain",                "NATURE", "", ""),
 ("snow",                "NATURE", "", ""),
 ("ice",                 "NATURE", "", ""),
 ("flame",               "NATURE", "DONE", "Built for A01."),
 ("ember / coal",        "NATURE", "", ""),
 ("smoke",               "NATURE", "", "Appears on 4+ plates."),
 ("ash",                 "NATURE", "", "Appears on 4+ plates."),
 ("charcoal",            "NATURE", "", "Taught by INDEX - burn, cover, black chunks - never by texture alone."),
 ("sun",                 "NATURE", "", ""),
 ("sun path arc",        "NATURE", "", "I02, I03, F04."),
 ("moon",                "NATURE", "", ""),
 ("star",                "NATURE", "", ""),
 ("cloud",               "NATURE", "", ""),
 ("wind",                "NATURE", "", ""),
 ("shadow",              "NATURE", "", "A06, I02. Carries the whole of time-telling."),
 ("stone / rock",        "NATURE", "DONE", "Built for A01."),
 ("sand",                "NATURE", "", ""),
 ("gravel",              "NATURE", "", "C02 filter. Cross-section material symbol already drafted."),
 ("clay",                "NATURE", "", ""),
 ("mud",                 "NATURE", "", ""),
 ("soil profile",        "NATURE", "", "F01. Cutaway."),
 ("hill / horizon",      "NATURE", "", ""),
 ("valley",              "NATURE", "", ""),
 ("cave / overhang",     "NATURE", "", ""),
 ("ore in rock",         "NATURE", "", "G09."),
 ("salt",                "NATURE", "", ""),

 # ---------------------------------------------------------------- LIVING (25)
 ("tree",                "LIVING", "", ""),
 ("shrub",               "LIVING", "", ""),
 ("grass",               "LIVING", "", ""),
 ("vine",                "LIVING", "", ""),
 ("moss",                "LIVING", "", ""),
 ("fungus",              "LIVING", "", ""),
 ("leaf forms",          "LIVING", "", "Shape, edge, arrangement - the DESCRIPTIVE vocabulary, not a field guide."),
 ("root / tuber",        "LIVING", "", ""),
 ("flower",              "LIVING", "", ""),
 ("fruit",               "LIVING", "", ""),
 ("nut",                 "LIVING", "", ""),
 ("seed",                "LIVING", "", ""),
 ("grain head",          "LIVING", "", ""),
 ("quadruped: large",    "LIVING", "", "Body plan, not species. E03, E05, F07."),
 ("quadruped: small",    "LIVING", "", ""),
 ("bird",                "LIVING", "", ""),
 ("fish",                "LIVING", "", ""),
 ("insect",              "LIVING", "", ""),
 ("snake",               "LIVING", "", ""),
 ("worm",                "LIVING", "", ""),
 ("egg",                 "LIVING", "", ""),
 ("track / footprint",   "LIVING", "", "E03. Reading sign is the transferable skill."),
 ("fur / feather / scale", "LIVING", "", ""),
 ("horn / claw",         "LIVING", "", ""),
 ("vermin set",          "LIVING", "", "D06. Rat, louse, flea, fly, mosquito - the disease vectors."),

 # ---------------------------------------------------------------- MADE (96)
 ("vessel: pot",         "MADE", "DONE", "Built for A01. Recurs in C02, D05, E06, E07, G07, G10."),
 ("vessel: jar sealed",  "MADE", "", ""),
 ("vessel: gourd",       "MADE", "", ""),
 ("vessel: basket",      "MADE", "", ""),
 ("vessel: sack",        "MADE", "", ""),
 ("vessel: skin bag",    "MADE", "", ""),
 ("vessel: box",         "MADE", "", ""),
 ("vessel: barrel",      "MADE", "", ""),
 ("lid / stopper",       "MADE", "", ""),
 ("knife",               "MADE", "", ""),
 ("axe",                 "MADE", "", ""),
 ("adze",                "MADE", "", ""),
 ("saw",                 "MADE", "", ""),
 ("hammer / maul",       "MADE", "", ""),
 ("chisel",              "MADE", "", ""),
 ("wedge",               "MADE", "", ""),
 ("drill / bow drill",   "MADE", "", "C03 fire, H03 turning."),
 ("awl",                 "MADE", "", ""),
 ("needle",              "MADE", "", ""),
 ("file / rasp",         "MADE", "", ""),
 ("tongs",               "MADE", "", ""),
 ("anvil",               "MADE", "", ""),
 ("bellows",             "MADE", "", "G08. Cutaway to show the air path."),
 ("spindle",             "MADE", "", ""),
 ("loom",                "MADE", "", ""),
 ("quern",               "MADE", "", ""),
 ("lathe / pole lathe",  "MADE", "", ""),
 ("potter's wheel",      "MADE", "", ""),
 ("spade / digging stick", "MADE", "", ""),
 ("hoe",                 "MADE", "", ""),
 ("plough",              "MADE", "", ""),
 ("sickle",              "MADE", "", ""),
 ("flail",               "MADE", "", ""),
 ("winnowing basket",    "MADE", "", ""),
 ("cord / rope",         "MADE", "", ""),
 ("knot set",            "MADE", "", "Drawn mid-tie AND finished. Overlaps H07 rigging."),
 ("net",                 "MADE", "", ""),
 ("snare",               "MADE", "", ""),
 ("deadfall trap",       "MADE", "", ""),
 ("fish trap / weir",    "MADE", "", ""),
 ("hook and line",       "MADE", "", ""),
 ("spear",               "MADE", "", ""),
 ("bow and arrow",       "MADE", "", ""),
 ("cloth / weave detail","MADE", "", ""),
 ("hide on frame",       "MADE", "", ""),
 ("garment",             "MADE", "", ""),
 ("shoe",                "MADE", "", ""),
 ("belt / strap",        "MADE", "", ""),
 ("hearth",              "MADE", "DONE", "Pot on support stones over flame. Built for A01."),
 ("drying rack",         "MADE", "", ""),
 ("smoke house",         "MADE", "", ""),
 ("earth oven",          "MADE", "", ""),
 ("kiln",                "MADE", "", ""),
 ("bloomery furnace",    "MADE", "", ""),
 ("charcoal retort",     "MADE", "", "plate02a already exists - port it."),
 ("filter column",       "MADE", "", "plate02 exists - port it. Sand/charcoal/gravel cross-section."),
 ("post and beam frame", "MADE", "", ""),
 ("wattle and daub wall","MADE", "", ""),
 ("thatch roof",         "MADE", "", ""),
 ("shingle roof",        "MADE", "", ""),
 ("door",                "MADE", "", ""),
 ("chimney / smoke hole","MADE", "", ""),
 ("lean-to shelter",     "MADE", "", ""),
 ("debris hut",          "MADE", "", ""),
 ("snow trench",         "MADE", "", ""),
 ("granary raised",      "MADE", "", ""),
 ("storage pit",         "MADE", "", ""),
 ("latrine",             "MADE", "", "D04. Highest-mortality-value object in the set."),
 ("well",                "MADE", "", ""),
 ("ditch / channel",     "MADE", "", ""),
 ("check dam",           "MADE", "", ""),
 ("fence / pen",         "MADE", "", ""),
 ("dry-stone wall",      "MADE", "", ""),
 ("raft",                "MADE", "", ""),
 ("dugout hull",         "MADE", "", ""),
 ("plank hull",          "MADE", "", "H07. Cutaway."),
 ("paddle / oar",        "MADE", "", ""),
 ("sail and mast",       "MADE", "", ""),
 ("anchor",              "MADE", "", ""),
 ("cart and axle",       "MADE", "", ""),
 ("sled",                "MADE", "", ""),
 ("travois",             "MADE", "", ""),
 ("pack frame",          "MADE", "", ""),
 ("yoke / harness",      "MADE", "", ""),
 ("roller / skid",       "MADE", "", ""),
 ("lever and fulcrum",   "MADE", "", ""),
 ("pulley",              "MADE", "", ""),
 ("screw",               "MADE", "", ""),
 ("wheel and axle",      "MADE", "", ""),
 ("water wheel",         "MADE", "", ""),
 ("windmill sail",       "MADE", "", ""),
 ("gear / drive train",  "MADE", "", ""),
 ("lens",                "MADE", "", "H05. Ray path drawn through it."),
 ("pen and ink",         "MADE", "", ""),
 ("carved printing block","MADE", "", "H06. The plate that makes the set propagate."),
 ("balance beam",        "MADE", "", ""),
 ("gnomon",              "MADE", "", ""),
 ("drum / string / pipe","MADE", "", "K06."),
 ("token / tally",       "MADE", "", "J02 trade, J04 record."),
 ("boundary marker",     "MADE", "", "J03, J08. Also ties to the surface-marker thread."),
 ("grave marker",        "MADE", "", ""),
 ("splint and sling",    "MADE", "", "D02."),
 ("bandage",             "MADE", "", ""),
]


def report():
    from collections import Counter, defaultdict
    import os
    import re
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from lexicon_domains import PLATES

    words = sum(p[4] for p in PLATES)
    by_kind = Counter(p[1] for p in PRIMITIVES)
    done = [p for p in PRIMITIVES if p[2] == "DONE"]
    weak = [p for p in PRIMITIVES if p[2] == "WEAK"]

    print("OBJECT LIBRARY: %d primitives for %s words across %d plates"
          % (len(PRIMITIVES), format(words, ","), len(PLATES)))
    print("  %.1f words carried per primitive\n" % (words / len(PRIMITIVES)))
    for k, desc in KINDS.items():
        print("  %-8s %3d   %s" % (k, by_kind[k], desc))
    print("\n  built already (A01): %d    weak / needs an artist: %d" % (len(done), len(weak)))
    print("  remaining to draw:   %d" % (len(PRIMITIVES) - len(done)))

    # Coverage. Word-boundary matching: plain substring had "rain" hitting grain
    # and drain, "well" hitting swell and dwell, which inflated every count.
    text = {p[0]: (p[6] + " " + " ".join(p[7])).lower() for p in PLATES}
    ALIAS = {
        "figure: stand": ["person", "people", "figure", "figures", "someone", "attendant"],
        "figure: dig": ["dig", "digging", "dug"],
        "figure: strike down": ["strike", "striking", "struck", "hammer"],
        "water: wavy lines": ["water"],
        "water: body/pool": ["pool", "river", "stream", "spring", "seep"],
        "hand: open": ["hand", "hands"],
        "cutaway hatch": ["cutaway", "cross-section", "section", "sliced"],
        "group: many": ["group", "groups", "assembly", "several"],
        "vessel: pot": ["pot", "vessel", "crock", "jar"],
        "cord / rope": ["cord", "rope", "cordage", "twist"],
        "flame": ["fire", "flame", "flames", "burning"],
        "panel border": ["panel", "panels"],
        "sequence arrow": ["sequence", "numbered panels"],
        "callout bubble": ["callout", "callouts"],
        "ground line": ["ground", "floor"],
        "tree": ["tree", "trees", "timber"],
    }
    hits = defaultdict(set)
    for name, kind, status, _note in PRIMITIVES:
        terms = ALIAS.get(name) or [name.split(":")[-1].split("/")[0].strip()]
        terms = [t for t in terms if len(t) >= 3]
        if not terms:
            continue
        rx = re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b")
        for pid, blob in text.items():
            if rx.search(blob):
                hits[name].add(pid)
    ranked = sorted(hits.items(), key=lambda kv: -len(kv[1]))

    print("\n  CUMULATIVE PLATE COVERAGE")
    for n in (10, 20, 40, 60):
        covered = set()
        for _nm, ps in ranked[:n]:
            covered |= ps
        print("    top %2d primitives  ->  %2d of %d plates  (%.0f%%)"
              % (n, len(covered), len(PLATES), 100 * len(covered) / len(PLATES)))

    print("\n  HIGHEST-LEVERAGE PRIMITIVES — draw these first")
    for name, ps in ranked[:16]:
        print("    %2d plates  %s" % (len(ps), name))

    never = [p[0] for p in PRIMITIVES if p[0] not in hits]
    print("\n  %d primitives are named by no plate description — these are the long tail"
          % len(never))
    print("  (they still carry words; the descriptions are summaries, not inventories)")


if __name__ == "__main__":
    report()
