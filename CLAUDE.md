# REMEMBER FORWARD — PROJECT BRIEF FOR CLAUDE CODE

## PROJECT IDENTITY
- Brand: Remember Forward (movement/call to action)
- IP Name: The Patient Message (the capsule contents)
- LLC: Remember Forward LLC (pending formation, NH)
- Tagline: Buy it. Build it. Bury it. For someone you will never meet.
- Domain: rememberforward.org (live)
- GitHub: github.com/ckantargis/remember-forward
- License: CC BY-SA 4.0

## PLATE DESIGN SPECIFICATIONS
- Format: SVG, viewBox="0 0 480 680"
- Borders: outer rect 6,6 468x668 stroke-width 3 / inner rect 12,12 456x656 stroke-width 0.75
- Font: Georgia, serif — all text
- Section headers: centered, em-dash bullet em-dash format, class H (6.5px bold letter-spacing 2.5px)
- Title bar: 12px bold letter-spacing 2px, y=32
- Subtitle: 7px letter-spacing 1.5px, y=50
- Body text classes: L=7px, Ls=6px, Lx=5.5px
- Script/large text: Lt=14px (Tamil), Ld=13px (Devanagari), La=14px (Arabic), Lh=13px (Hebrew)
- Footer line 1 (y=615-630): metadata strip, class M 6px
- Footer line 2 (y=648): "THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD." class Fb 7.5px bold
- Footer line 3 (y=663): "BUY IT · BUILD IT · BURY IT · FOR SOMEONE YOU WILL NEVER MEET" class F 7px italic
- All plates built as Python scripts that generate SVG strings and write to file
- Output goes to: plates/languages/{language}/ or plates/knowledge/

## FOLDER STRUCTURE
    plates/
      knowledge/         <- plates 01-11 (survival/knowledge)
      languages/
        hebrew/          <- plates 09A-12D (16 plates, complete)
        arabic/          <- plates 13A-13D (complete)
        tamil/           <- plates 14A-14D (complete)
        sanskrit/        <- plates 15A-15D (complete)
        bengali/         <- plates 16A-16D (NEXT)
    guides/              <- Word documents gd_00 through gd_08
    containers/          <- gd_09 through gd_16
    project/             <- master_handoff.docx, inner_ark_operational_structure.docx

## COMPLETED KNOWLEDGE PLATES
- plate01_v3_rosetta.svg — Rosetta Index, Mayan number system
- plate02_v2_water_fire_shelter.svg
- plate03_v2_agriculture_seeds.svg
- plate04_v2_technology.svg
- plate05_v2_governance.svg
- plate06_v2_concords_stars.svg
- plate07_encoding_communication.svg
- plate08_physics_of_sound_v2.svg
- plate10_electrical_phenomena.svg
- plate11_energy_generation.svg
- plate09_audio_playback_guide.svg — BUILT (needle construction, tone arm, groove)
- plate02a_charcoal_retort.svg — BUILT (clay-vessel charcoal, 12–24 h method)
- PENDING: plate00 master key · plate02b/02c/02d charcoal series · plate05a–05h governance series

## COMPLETED LANGUAGE SERIES (28 plates total)

### Hebrew — plates/languages/hebrew/ (16 plates)
- plate09a_biblical_hebrew_script.svg
- plate09b_biblical_hebrew_phonology.svg
- plate09c_biblical_hebrew_grammar.svg
- plate09d_biblical_hebrew_text.svg
- plate10a_mishnaic_hebrew_script.svg
- plate10b_mishnaic_hebrew_phonology.svg
- plate10c_mishnaic_hebrew_grammar.svg
- plate10d_mishnaic_hebrew_text.svg
- plate11a_yemenite_hebrew_script.svg
- plate11b_yemenite_hebrew_phonology.svg
- plate11c_yemenite_hebrew_grammar.svg
- plate11d_yemenite_hebrew_text.svg
- plate12a_modern_hebrew_script.svg
- plate12b_modern_hebrew_phonology.svg
- plate12c_modern_hebrew_grammar.svg
- plate12d_modern_hebrew_text.svg

### Arabic — plates/languages/arabic/ (4 plates)
- plate13a_arabic_script.svg
- plate13b_arabic_phonology.svg
- plate13c_arabic_grammar.svg
- plate13d_arabic_text.svg

### Tamil — plates/languages/tamil/ (4 plates)
- plate14a_tamil_script.svg
- plate14b_tamil_phonology.svg
- plate14c_tamil_grammar.svg
- plate14d_tamil_text.svg

### Sanskrit — plates/languages/sanskrit/ (4 plates)
- plate15a_sanskrit_script.svg
- plate15b_sanskrit_phonology.svg
- plate15c_sanskrit_grammar.svg
- plate15d_sanskrit_text.svg

## LANGUAGE SERIES PLAN (50 total languages)
- Series 16: Bengali (NEXT)
- Series 17: Mandarin Chinese
- Series 18: Japanese
- Series 19: Malay/Indonesian
- Series 20: Swahili
- Series 21: Greek
- Series 22: Latin
- Series 23: Persian/Farsi
- Series 24: Russian
- Series 25: Hindi
- Series 26-50: continuing to 50 languages total

## NAMING CONVENTION
plateXXy_language_descriptor.svg
where XX = series number, y = A/B/C/D

Examples:
  plate16a_bengali_script.svg
  plate16b_bengali_phonology.svg
  plate16c_bengali_grammar.svg
  plate16d_bengali_text.svg

## EACH LANGUAGE SERIES — 4-PLATE STRUCTURE
- Plate A: Script (alphabet/writing system, letter forms, numerals, script history)
- Plate B: Phonology (distinctive sounds, vowel system, key contrasts, IPA)
- Plate C: Grammar and Vocabulary (sentence structure, verb system, 20-30 core words)
- Plate D: Running Text (4-5 passages interlinear, bridge phrase in that language)

## THE BRIDGE PHRASE
Every Plate D ends with this phrase rendered in the target language:
"This was made for you, freely, by people who remembered forward."
Always add a note explaining how the language expresses the concept of
"forward" or "future" in the phrase — the translation is never mechanical,
always idiomatic.

## SVG PYTHON BUILD PATTERN
Every plate is built by a Python script using this structure:

    def bx(x,y,w,h,sw=0.8):  # draw box
    def t(x,y,s,a="middle",c="L"):  # draw text (escapes & < >)
    def hr(y,w=0.3):  # horizontal rule
    def sh(y,txt):  # section header with em-dash bullets
    def arh(x0,x1,y,s=4):  # horizontal arrow

Standard STYLE block (Georgia serif, named classes L Ls Lx H S T M F Fb
plus script-specific classes Lt Ld La Lh etc.)

Standard BORDERS block (double border rect)

Standard FOOTER block (three lines at y=615, 648, 663)

All four plates per language built in one Python script.
Files written to local plates/languages/{language}/ folder.
After build: git add, git commit, git push.

## GITHUB WORKFLOW
- Repository: github.com/ckantargis/remember-forward
- Branch: main
- After completing a language series:
    git add plates/languages/{language}/
    git commit -m "Add {language} series plates {XX}A-{XX}D"
    git push
- Commit message format: "Add Bengali series plates 16A-16D"

## KEY DESIGN DECISIONS
- Mayan dot-bar-shell (base 20) as universal number system on knowledge plates
- All plates: CC BY-SA 4.0, rememberforward.org in footer
- Language labels in English by default
- Arabic labels to be added to knowledge plates 02-06 AFTER all 50 languages done
- Interlinear translation on all Plate D texts (word-for-word, then full meaning)
- Arabic and Hebrew: read right-to-left (noted on every plate)
- Tamil, Sanskrit, Bengali, and most others: read left-to-right
- No voiced/aspirated distinction in pure Tamil — positional allophones only
- Yemenite Hebrew: phonology plates are the most important, not script

## ARK / JERICHO HYPOTHESIS (in Founder's Letter v3)
- Gold + acacia wood + charcoal layers = supercapacitor construction
- Beryl discs = optical/acoustic reflectors
- Helmholtz resonant cavity producing voice-like plasma arc sound
- Jericho walls = resonant fatigue fracture from 7 shofarot detuned 1-3Hz apart
  producing 1-15Hz infrasound matching stone wall resonance
  cumulative 7-day fatigue, final shout as trigger
- Documented in gd_02_founders_letter.docx v3

## BUSINESS / IP STATUS
- Remember Forward LLC: PENDING formation at nhquickstart.nh.gov ($102, NAICS 511130)
- Old LLC (The Inner Ark Project LLC): lapsing naturally
- Trademarks: pending LLC formation before filing
  - "Remember Forward" — Classes 41+16, Intent to Use, ~$500
  - "The Patient Message" — same, ~$500
- Prior Art Archive: pending submission at priorartarchive.org (free, gets DOI)
- Copyright registration: pending at copyright.gov ($45-65, can file as individual now)
- Archive.org: plates 01-12A uploaded, plates 12B-15D not yet uploaded

## WEBSITE
- `build_site.py` generates `index.html` — run `python build_site.py` from project root after any structural change
- Auto-detects language series from folder names — new folders don't require LANG_META entries (only needed for custom display names/badges)
- Language switcher built in: EN / 中文 / हिंदी / Español / العربية
- "Alternate Language Pairings" section lists all 58 alt series
- Plate count/language count must be manually updated in LANG_META when adding series

## DISTRIBUTION / ARCHIVE STATUS
- **archive.org:** `archive.org/details/remember-forward-patient-message-plates` — 475 files uploaded (all main + alt plates). Credentials in `.env`, auto-loaded by `upload_to_archive.py`.
- **Zenodo:** Published DOI `10.5281/zenodo.19545922` — citable, permanent. Use this for prior art filings, trademark applications, academic citations.
- **Gumroad:** Integration on website exists, but product URLs are PLACEHOLDERS. Must create products at gumroad.com first, upload `downloads/gumroad-plate-set.zip` and `downloads/gumroad-complete-archive.zip`, then update the two slug placeholders in `index.html`.
- **Downloads:** `build_downloads.py` generates `remember-forward-all-plates.zip` and PDF. `build_gumroad_bundles.py` generates Gumroad bundles. Run both after adding new plates.

## OUTREACH
- Draft posts in `outreach/posts_draft.md` — 6 posts for different communities (HN, Reddit, Long Now, etc.)
- 16 preview PNGs in `outreach/images/` generated by `build_outreach_images.py`
- **ALL POSTS ON HOLD** until LLC formation, trademarks, copyright registration, and business bank account are complete

## PICTOGRAM STYLE RULES (settled — apply to all knowledge plates)

### Role-based style system
Each style is used only for what it uniquely does well. Never mix styles within a single panel.

| Content type | Style | Rule |
|---|---|---|
| Person performing an action | ISOTYPE silhouette | Flat filled shape, no outlines, no internal lines |
| Construction / assembly | Isometric line drawing | 30° equal angles, no vanishing point, no shading — just lines |
| Layers / what's inside | Cross-section cutaway | Show interior as if sliced — the only view that reveals hidden structure |
| How to hold / use a tool | Side elevation | Clear side view showing hand-tool relationship; NOT hand's-eye (too foreshortened) |
| Cause and effect / steps | Sequence panels | Numbered left-to-right or top-to-bottom; action → consequence pairs |

### What NOT to use
- **Hand's-eye / first-person view** — foreshortened, complex, engraves poorly
- **One-point perspective** — requires consistent horizon/vanishing point across all plates, too hard to maintain
- **Photorealistic or shaded renders** — shading is destroyed by engraving
- **Checkmarks, circle-slash, thumbs up, skulls in isolation** — not cross-cultural (see symbol_universality_research.md)

### Engraving constraints (all pictograms must pass these)
- Binary only: no gradients, no shading, no fills other than solid black
- Minimum feature size: ~0.1mm real-world (~0.4 SVG units at 12×17cm)
- Stroke weights: 1.5px for main forms, 0.8px for interior detail lines, 0.5px for texture (stipple/cross-hatch)
- Test at actual plate scale before committing — what reads at 1000px may blob at 12cm

### Style consistency rule
Every plate in the set must feel like it belongs to the same visual grammar. Before drawing anything new, check:
1. Does an open-licensed equivalent already exist? (OCHA, ISO 7010, WHO WASH — check first)
2. Which role-based style applies?
3. Does it match the visual weight of other plates already built?

### OCHA / ISO 7010 audit status
- **OCHA Humanitarian Icons** (github.com/UN-OCHA/humanitarian-icons, 295+ icons): covers water containers, hygiene, sanitation, shelter, relief categories. Good for SYMBOLS (representing a concept). NOT instructional — won't show how to build a filter.
- **ISO 7010** (commons.wikimedia.org/wiki/Category:ISO_7010_safety_signs, 352 SVGs): safety/warning signs. Useful for danger indicators, fire extinguisher, emergency exit. Not instructional.
- **WHO WASH pictograms**: useful for water safety concepts. Access via WHO website directly.
- **Bottom line**: Use OCHA/ISO for concept symbols (clean water icon, shelter icon, danger icon). All instructional content (how to build, step sequences) must be custom drawn using the role-based system above.

## PICTOGRAM WORK IN PROGRESS
- `plates/knowledge/plate02_filter_review.svg` — redesign draft of plate02. NOT the final plate. Has cross-section material symbols (charcoal/sand/gravel) and a traced Canva figure for Scene 1 (gravel collection). Scene 2 (charcoal making) still placeholder.
- `plates/knowledge/figure_test.svg` and `build_figure_test.py` — ISOTYPE silhouette figure tests. Figure still needs refinement before use in plates.
- `symbol_universality_research.md` — Opus research document on cross-cultural symbol validity. KEY FINDING: only narrative pictographic sequences (action→consequence) are truly cross-cultural. Checkmarks, circle-slash, thumbs up, skull in isolation — all fail.
- **Image gen workflow:** Canva Magic Media (text-to-image) → export as PNG to `reference_images/` → hand-trace into SVG. ComfyUI (installed at `C:\Users\kanta\ComfyUI_windows_portable\`, DreamShaper 8) was set up but replaced by Canva for better results.

## PICTOGRAPH PERSPECTIVE DISCUSSION (deferred, not resolved)
- The "3D pictographs" discussion from session b0077064 was about **perspective-appropriate views**, not photorealistic 3D renders
- Core idea: show scenes from the survivalist's actual viewpoint (crouching over fire, looking down into filter being built, hands at the angle of striking flint)
- Perspective styles that work for engraving (line art, no shading): isometric, one-point perspective, hand's-eye view, cross-section cutaways
- These are complementary to ISOTYPE, not competing: ISOTYPE for figures/simple objects, perspective line drawings for construction sequences and spatial assembly
- This discussion was deferred — not yet acted on

## PENDING TASKS (priority order)

> **RE-PRIORITISED 2026-08-27.** The Governance & Commons series is now the **sole plate build
> focus**. Language series are PAUSED. The 15-plate Founder's Edition kit is SUSPENDED.
> See `project/governance_series_scope.md` and `project/plate_format_consolidation.md`.

1.  **Resolve the diminished-figure vocabulary** — BLOCKING the whole governance series (governance_series_scope.md §6). Prefer group-count over individual posture.
2.  **Build 05C first** (circle / raised-figure grammar), print at 12×17 cm, functional-test it on someone unfamiliar. If they can't tell which sequence ended well, stop and redesign.
3.  Then 05A → 05B, 05D, 05E, 05F → 05G, 05H. Revise 05I last (EN face A / ES face B).
4.  Build the **master-key disc** (68 mm, flat, two-sided) — replaces plate00 in the kit.
5.  **Get engraving quotes** — two-sided, 120×170, 0.1 mm feature, setup quoted separately (launch_plan_2027.md §8).
6.  Prove **two-sided engraving + registration** on a coupon before committing the run.
7.  Issue correction notices for `gd_09` and `gd_10` — both make false container-capacity claims.
8.  Form Remember Forward LLC at nhquickstart.nh.gov
9.  Get EIN at irs.gov (free, after LLC)
10. Open business bank account under new LLC
11. File trademark: Remember Forward + The Patient Message
12. Submit to priorartarchive.org
13. Register copyright at copyright.gov

**PAUSED (not cancelled):** Bengali 16A-16D · Mandarin 17A-17D · the remaining 50-language plan · Arabic labels on knowledge plates 02-06 · upload 12B-15D to archive.org · GitHub folder reorganisation.

## PLATE FORMAT — SETTLED 2026-08-27
- **120 × 170 mm** stays. Pictographic plates are governed by the 0.1 mm engraving floor, not point size.
- **Engrave BOTH FACES.** Nine content faces on five plates. Untested — prove on a coupon.
- **Ablated grooves, NOT laser-annealed marks.** An annealed mark is an oxide colour and is destroyed by the 540 °C stress relief; an ablated groove is topographic and survives heat treat and abrasion. (The 2026-04-13 audit's "laser-annealed" note was about 316L stainless — do not carry it to titanium.)
- **Rolled, not stacked** — 20 mm core, 50 mm bundle, 3" Sch 80 pipe. Flat 120 mm plates do NOT fit the 4" pipe in gd_09 or the 6" sphere in gd_10.
- **Stress-relieve after rolling**, 480–540 °C, 1–2 h. Stay below 600 °C or you get alpha case. Batch process — $8–16/kit, or ~free in a ceramics kiln.
- **Anodizing is optional** — the galling concern that motivated it does not survive scrutiny; static Ti at ambient does not diffusion-bond.
- Galvo field limits: 175 mm → 0.07 mm floor · 200 mm → 0.10 · 300 mm → 0.15. A 171×243 plate on a 300 mm lens engraves WORSE than 120×170 on a 175 mm lens.

## PICTOGRAM / IMAGE GENERATION STRATEGY

### Ruled out approaches
- **Hand-coded SVG paths for complex figures:** Too labor-intensive, poor results for organic shapes
- **3D rendered images:** Engraving destroys shading and depth cues — 3D renders collapse to illegible noise after B&W conversion. Also carry cultural/temporal specificity (clothing, props, architecture) that works against long-term legibility. The silhouette is what survives engraving regardless, so start there.
- **Photorealistic AI images:** Same problem as 3D — culture-specific, shading-dependent, poor vector tracing results

### Chosen approach: ISOTYPE-style flat silhouettes
- No outlines, no internal lines, no gradients — filled shapes only
- Check OCHA Humanitarian Icons, ISO 7010 (Wikimedia Commons), WHO WASH pictograms BEFORE drawing anything new — these cover ~30–60% of knowledge plate concepts and are open-licensed
- Workflow: AI image gen (Canva) → reference sketch → Inkscape Trace Bitmap (Potrace) or VTracer → manual path cleanup → SVG rebuild
- VTracer (github.com/visioncortex/vtracer) is a scriptable Python alternative to Potrace

### AI image generation notes
- Prompt that works: `flat black silhouette, single color, no outlines, no internal lines, no gradients, no shadows, white background, simple geometric shapes only, vector icon style`
- Style drift across sessions is a real risk — use a reference image (--sref in Midjourney, or image-to-image) to keep plates visually consistent
- Voting on AI outputs filters aesthetics only — also run a functional filter: print at actual plate size, show to someone unfamiliar (no caption), ask what they see
- AI alone is NOT sufficient for bridge phrase translations — contact Translators Without Borders (translatorswithoutborders.org)

## OPUS AUDIT FINDINGS (2026-04-13)

### Language plate accuracy risks
- ~30 of 50 languages likely have AI errors
- Extreme risk: Ancient Egyptian, Zapotec, Karen, Tamazight, Tibetan, Classical Sanskrit
- High risk: Quechua, Aymara, Nahuatl, Tok Pisin, Tigrinya, Oromo, Zhuang, Maithili
- Unicode verification: add uharfbuzz + Noto pipeline to build scripts to catch encoding errors

### Biggest structural gap
- No parallel text — Plate D running text is undecodable without cross-language alignment
- Fix: add UDHR (Universal Declaration of Human Rights, OHCHR, 500+ languages, open license) as parallel text thread on every Plate D
- Use Leipzig Glossing Rules (eva.mpg.de/lingua/resources/glossing-rules.php) for interlinear glossing on Plate D
- Add Swadesh 100-word vocabulary panel (fixed order) to every Plate C for cross-language triangulation

### Missing knowledge topics
- First aid / medical triage (ICRC already has pictographic materials)
- Food safety — what not to eat, spoilage identification
- Toolmaking from basic materials
- Self-location (sun/stars/landscape)
- Time reckoning / sun calendar
- Consider splitting into "Survival" series (immediate) and "Civilization rebuild" series (long-term)

### Structural improvements needed
- Plate 0: master key plate that teaches a finder the pictographic vocabulary
- Distribution: mail sets to ~200 institutional libraries as permanent deposit (redundancy beats monumentality)
- DXF export via ezdxf Python library for laser engraving handoff
- Convert all SVG text to outline paths before export (laser shops need paths, not live text)
- Add version numbers to plates + maintain public errata list
- Consider CC0 instead of CC BY-SA 4.0 to maximize reproduction with no legal friction

### Metal / engraving specs
- ~~Best alloy for burial: 316L stainless steel (laser-annealed, not ablated)~~ **SUPERSEDED.** Titanium Grade 2, ablated grooves. Substrate reversed 2026-08-06; **no steel at all** as of 2026-09-01. The laser-annealed finding applied to 316L only and must NOT be carried to titanium.
- Shop format: DXF preferred over SVG
- Minimum feature size: ~0.1mm real-world (~0.4 SVG units at 12×17cm plate)
- ~~Sealed stainless canister with desiccant~~ **SUPERSEDED — no steel.** Welded titanium vessel, desiccant + oxygen absorber.
- AI-generated image provenance should be documented given uncertain copyright status

### Strategic outreach (high priority)
- Email Long Now Foundation / Rosetta Project (rosettaproject.org) — they've solved the same problems; ask for methodology, parallel-text source recommendations, metadata schema

## PRIMARY SOURCES — SEARCH THESE BEFORE SAYING "NOT IN THE RECORD"

`claude_export_2026-05-29/conversations.json` holds **12 conversations,
2.8 million characters, March-May 2026** — including the 362-message main
thread. **It contains design decisions that never reached any document in this
repo.** Two searches of the repo and the memory files both wrongly concluded the
microfilm-and-lens idea had never been discussed; it is in the 24-25 March
conversation.

Searchable with:

    python -c "import json;d=json.load(open('claude_export_2026-05-29/conversations.json',encoding='utf-8'))..."

- `project/export_audit_2026-08-20.md` — what the audit found missing
- `containers/media_stack_recovered.md` — the six-layer media stack, recovered

Known gaps the audit surfaced: PVC may be archivally disqualified (HCl
outgassing); the brother partnership agreement was drafted twice and never
saved; the fibre-laser purchase research (vendors and prices) is not in the
repo; gd_17 and gd_18 were built in-chat and lost.

## NOTES FOR CLAUDE CODE SESSIONS
- When starting a new language series, always web search for script + phonology
  specifics before building — do not rely on training data alone for Unicode
  character ranges and IPA values
- Build all 4 plates in one Python script when possible
- Verify each SVG with: grep -c "<svg" file.svg and grep -c "</svg>" file.svg
  Both should return 1
- After each series: commit and push before moving to the next language
- If a script-specific font class is needed, add it to the STYLE block
  (e.g., class="Lb" for Bengali script at appropriate font size)
