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
- PENDING: plate09_audio_playback_guide.svg (needle construction, tone arm, groove)

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

## PENDING TASKS (priority order)
1.  Build Bengali series (16A-16D) — IMMEDIATE NEXT
2.  Build Mandarin series (17A-17D)
3.  Continue through all 50 languages
4.  Build plate09 Audio Playback Guide (knowledge plate, pending)
5.  Add Arabic labels to knowledge plates 02-06 after all 50 languages done
6.  Upload plates 12B-15D to archive.org
7.  Reorganize GitHub plates folder into subfolders if not done
8.  Form Remember Forward LLC at nhquickstart.nh.gov
9.  Get EIN at irs.gov (free, after LLC)
10. Open business bank account under new LLC
11. File trademark: Remember Forward + The Patient Message
12. Submit to priorartarchive.org
13. Register copyright at copyright.gov

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
