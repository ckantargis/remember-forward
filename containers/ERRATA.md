# Container Documents — Errata

**Opened 2026-08-20.** These documents are published: they sit in a public
GitHub repo, on archive.org and behind a Zenodo DOI. Anyone who downloaded them
before this date has the uncorrected version. That is what an errata list is
for — the project's own governance material says to keep the reversals in, and
a public correction is cheaper than a quiet edit.

---

## Corrected 2026-08-20

| Document | Was | Now | Why |
|---|---|---|---|
| `gd_09_flyer_pvc` | "laser-engraved **nickel** plates" | titanium | Substrate reversed Aug 2026 |
| `gd_10_flyer_titanium` | Viton O-rings "maintain the seal" over millennia | Seal rated 100–300 yrs; weld it if it must outlast that | Sealing analysis, 2026-08-08 |
| `gd_11_flyer_ocean` | "**Gold-plated nickel plates are mandatory**" | Titanium, inert in seawater, no plating; vitrified stoneware also viable | Substrate reversal + shipwreck-porcelain precedent |
| `container_and_tiering_v2` | Viton described as an upgrade that solves sealing | Ranked seal table: welded metal > cast lead ≈ pitch on ceramic > glass-to-metal > C-ring > elastomer | Sealing analysis |
| `container_and_tiering_v2` | "full 206-plate stack fits in standard 6-inch sphere" | **Does not fit.** 1.85 L sphere vs ~3.4 L and 15 kg of plates. Real capacity ~100–120 thin plates | Geometry, 2026-08-20 |
| `container_and_tiering_v2` | "standard nickel plate thickness of 1.5 mm" | Titanium runs 0.5–0.8 mm; check volume, not just stack height | Substrate reversal |

**Why the substrate changed.** Nickel's archival reputation rests on the Long
Now Rosetta Disk, whose credential is electroforming fidelity at micron scale —
irrelevant at this project's 0.1 mm feature size. Nickel also costs about twice
titanium per plate, is vulnerable to sulfide attack in anoxic burial soils,
cannot be colour-anodised, and is the world's most common contact allergen.

**Why the seal claim changed.** No elastomer has a validated multi-century life.
A 10,000-year vessel with a 100-year seal is a 100-year vessel. The deeper point
from that analysis: *every re-openable seal is a permanent liability bought to
serve a one-time event that will be destructive anyway.* The finder cuts it
open. Sweden's KBS-3 nuclear canisters, designed for 100,000 years, use
friction-stir-welded copper lids and no seal at all.

---

## Still wrong, not yet corrected

These need a rewrite rather than a sentence swap, and several are blocked on
decisions that are still open.

1. **Every plate cost in `container_and_tiering_v2` §2 is stale.** The tables
   price plates at $15–30 each and the complete 206-plate set at $3,090–6,780.
   Those were nickel figures and they did not include engraving setup, which is
   charged per unique design ($50–75 each) and was never modelled. Current
   titanium figures are $21.70–48.30 per plate — and pressed ceramic is
   $0.20–0.62. **The whole section needs rebuilding once the engraving quote
   matrix lands.**

2. **The three-tier framing in `gd_12_flyer_network` predates the material
   split.** Tier assignment now follows freight, not prestige: ceramic is a
   make-it-where-it-goes material, titanium is a ship-it-anywhere material.

3. **The 6-inch sphere is used as the reference vessel in several places.**
   Only the one instance above is corrected. Every other capacity claim in the
   set needs the same arithmetic done to it.

4. **`gd_11` claims the ocean capsule is self-righting.** That is a buoyancy
   and centre-of-mass calculation, and no calculation is in the record.

5. **`gd_11`'s zinc anode specification is unsourced.** A sacrificial anode is a
   consumable: it is used up, and after that the protection is gone. Same
   structural defect as the desiccant packets — a component with a decades-long
   life inside a vessel rated for millennia.

6. **Audio disc costs and the nickel disc option** in §3 carry the same stale
   substrate assumption as the plates.

---

## Applying the staged correction

`container_and_tiering_v2.docx` was locked by another process (Word, or a sync
client) when the corrections ran, so the corrected copy is staged beside it:

```
cd containers
mv container_and_tiering_v2.docx container_and_tiering_v2.PRE-2026-08-20.docx
mv container_and_tiering_v2.CORRECTED.docx container_and_tiering_v2.docx
```

The other three flyers were edited in place; each has a `.bak` of the version
that shipped before this date.

---

## Two malformed plate files found the same day

Not container documents, but found by the same pass and published in the same
places:

- **`plates/knowledge/plate10_electrical_phenomena.svg`** — a bare `&` in the
  text "`& motor`" made the file invalid XML. **Fixed** (`&amp;`). Strict SVG
  parsers reject the published copy; browsers happen to be forgiving.
- **`plates/languages/hausa/plate29d_hausa_text.svg`** — contains raw control
  characters (U+0006, U+0007) inside the Hausa running text, where hooked
  letters (ɓ ɗ ƙ) almost certainly belong. **Not fixed:** guessing at a letter
  in a language-preservation plate is worse than leaving a flagged bug. Needs a
  verified source or a Hausa speaker.
- 489 of 491 plate SVGs parse cleanly. Re-check with
  `python plates/relief_report.py` and the scan in the same session's notes.

---

## Corrected 2026-09-01 — website tier table

Full sweep in `AUDIT_2026-09-01.md`. All applied to `build_site.py` and
regenerated into `index.html` across all five languages.

| Tier | Was | Now | Why |
|---|---|---|---|
| A | Schedule 80 PVC, "500 – 1,000 years" | **HDPE Pipe, "100+ years"** | PVC outgasses HCl autocatalytically and the acid attacks the contents. PVC dates to the 1930s — there was never an empirical basis for a 500-year figure. HDPE has no chlorine. |
| B | "Grade 5 Ti-6Al-4V" | **Grade 2 CP titanium** | Grade 5 is the strength alloy; Grade 2 has better corrosion resistance for burial, and is what the plates use. |
| B | "Viton O-rings, aerogel insulation" | **"Welded closure — no elastomer to fail"** | Contradicted this errata's own 2026-08-20 seal ranking. Aerogel served no archival function. |
| B | **"Pyramid cavity at Giza angle"** | deleted | No engineering basis. Pseudo-archaeology in a product spec. |
| C | "HDPE hull + zinc sacrificial anodes" | **"HDPE outer hull, titanium pressure vessel"** | Zinc anodes cannot protect a plastic hull — galvanic protection needs metal in electrical continuity. |
| C | "Gold-plated plates only" | **"Titanium is inert in seawater — no plating needed"** | The `gd_11` correction of 2026-08-20 had never reached the website. |
| C | **"Unreachable, unjurisdictable"** | **"Check maritime law before any deposition"** | Legally false. UNCLOS governs the high seas; the London Convention and Protocol regulate seabed dumping. |
| D | "Outperforms titanium in corrosive zones" | **"Beats titanium in reducing acids; titanium wins in oxidising chlorides"** | Overstated. The advantage is conditional and reverses in oxidising conditions. |
| E | "Lead-Lined Granite · 100,000+ years · nuclear industry permanence standard" | **"Granite Vault · 10,000+ years · granite body, bentonite clay buffer, welded titanium vessel"** | The citation was false — the industry uses copper canisters in bentonite (KBS-3), and lead only for shielding in transport casks. 100,000 years is claimed for repository *geology*, never for a container. |
| F | "Geological timescale" | **"As long as the site holds"** | Unsupportable as written. |
| all | bare lifespan figures | **labelled "Design target"** + a note that these are intended service lives, not tested or warranted performance | Every figure on the page was unsourced — the same class of claim that failed on Tier E. |

### Still to do — downstream documents

These are **published** (GitHub, archive.org, Zenodo DOI) and now disagree with
the website. Both need a rewrite, not a sentence swap:

1. **`gd_09_flyer_pvc.docx`** — the entire flyer is about a material the site no
   longer recommends. Needs reissuing as an HDPE flyer, including a new closure
   method: PVC was chosen partly because it solvent-welds with hardware-store
   cement, and HDPE does not. Threaded fitting or fusion weld instead.
2. **`gd_15_tiere_granite.docx`** — carries the lead-lined spec and the
   100,000-year claim corrected above.

---

## Reissued 2026-09-01 — gd_09 and gd_15

Both rebuilt by `containers/build_flyers.py`. Each opens with a
"What Changed In This Edition" block rather than being edited silently.

**`gd_09_flyer_pvc.docx` → `gd_09_flyer_hdpe.docx`** — the material changed, so
the filename did. Schedule 80 PVC is withdrawn: it degrades by
dehydrochlorination, the released acid is autocatalytic, and inside a sealed
capsule there is nowhere for it to go but onto the contents. The 500–1,000 year
figure had no evidence behind it — PVC has only existed since the 1930s.
Replaced with black DR-11 HDPE, design target 100+ years, stated honestly as
the short tier whose job is to be cheap enough that there are thousands of them.

The closure had to be redesigned, not renamed: HDPE does not solvent-weld.
Socket fusion or hot-plate welding, no thread, no gasket, no tape — closed
permanently, on the same reasoning as the seal analysis of 2026-08-08. Added a
leak test before loading.

Also corrected in that flyer: the burial instruction said to mark the site with
a "non-ferrous (copper or stainless steel)" stake. **Stainless steel is an iron
alloy and is not non-ferrous.** Now copper or bronze, with the findability
trade-off stated — a steel marker is much easier to detect and much shorter-lived.

The stale plate-set cost table was removed rather than reprinted. Those figures
were nickel-era and excluded engraving setup; they now point here.

**`gd_15_tiere_granite.docx`** — rewritten. Removes the lead lining, the poured
lead seal, and the claim of "100,000+ years, the nuclear industry standard."
That claim was false: KBS-3 uses a copper canister over cast iron in a bentonite
buffer, and lead appears in that industry only as cask shielding. The
100,000-year figure belongs to repository geology behind a formal safety case.
The document also contradicted itself — its own precedent table already said the
nuclear standard was "designed for 10,000 years."

Replaced with a three-layer system: granite body for structure, **bentonite clay
buffer** as the engineered barrier, and a sealed inner vessel as the only real
seal — pitch-sealed fired ceramic for a self-builder (equal to cast lead in this
project's own ranking, and non-toxic), or a commissioned welded titanium vessel
for an institution. Explicitly rules out gaskets and O-rings.

Removing lead also removes the molten-lead pouring step, which was the most
hazardous instruction anywhere in this project's documents.

The placement table's arctic/permafrost row is no longer recommended on its own:
Svalbard's seed vault took meltwater into its access tunnel within nine years of
opening. Frozen ground is a bonus, never the barrier.

### Archive.org synced 2026-09-01

`sync_archive_files.py` touches named files only, unlike `upload_to_archive.py`
which re-uploads the whole plate set.

- **Uploaded:** `gd_09_flyer_hdpe.docx` / `.pdf` (new), `gd_15_tiere_granite.docx`
  / `.pdf` (replaced), and `containers/ERRATA.md` + `AUDIT_2026-09-01.md` so the
  correction log travels with the documents it corrects.
- **Deleted:** `gd_09_flyer_pvc.docx` and `.pdf`. A build guide that tells people
  to seal acid-generating plastic around their contents is not the kind of
  stale document that should stand as a historical artefact. The reversal is
  preserved here instead, which is what this file is for.

`build_flyers.py` now renders **both** formats from a single block list. Every
document in this project ships as .docx and .pdf, and hand-maintaining two
copies is exactly how the nickel, Viton and lead claims survived three weeks of
corrections.

### Corrected 2026-09-01 — the 2026-08-20 corrections were only half applied

Checked by downloading the live archive.org copies and testing them. The finding
was worse than "not propagated": **the prose was corrected and the specification
tables were not**, so each document contradicted itself.

| Document | Prose said | Table still said |
|---|---|---|
| `gd_10_flyer_titanium` | seal rated 100–300 yrs, weld it if longer | `O-rings · Viton (FKM) — not Buna-N · "Superior chemical resistance for long-term sealing"` |
| `gd_11_flyer_ocean` | "titanium is inert in seawater and needs no plating" | `Gold-plated nickel only` |
| `gd_11_flyer_ocean` | — | `Self-righting — capsule always returns to upright` (still no calculation on record) |
| `container_and_tiering_v2` | substrate reversed throughout | the **audio section** was missed entirely: "Option A: Laser-engraved nickel" |

All now fixed in the tables as well as the prose, each with a dated note saying
why. `gd_10` also moves Grade 5 Ti-6Al-4V to Grade 2 CP, matching the plates and
the website. `container_and_tiering_v2.CORRECTED.docx` has been promoted to be
`container_and_tiering_v2.docx` and the duplicate removed.

**PDFs were the silent half of this problem.** The August edits touched .docx
only, so archive.org carried corrected Word files beside stale PDFs of the same
document. `docx_to_pdf.py` now regenerates a PDF from any .docx in this repo, so
the pair can never drift again. All six files re-uploaded.

---

## PROPAGATION CHECKLIST — added 2026-09-01

The 2026-08-06 substrate reversal was errata'd here on 2026-08-20 and still had
not reached a single published surface three weeks later. An errata entry is not
finished until it has been checked against all seven:

- [ ] `build_site.py` (then rerun it — `index.html` is generated, never edit it directly)
- [ ] `README.md`
- [ ] `upload_to_zenodo.py` — **hardens into a permanent DOI, do this one first**
- [ ] `upload_to_archive.py`
- [ ] `prior_art_submission_template.txt` — body **and** keywords; this is IP scope
- [ ] `build_downloads.py`
- [ ] `build_gumroad_bundles.py`
- [ ] `outreach/` drafts — a stale spec in a partner letter misrepresents the project

See `AUDIT_2026-09-01.md` for the full sweep that found this.
