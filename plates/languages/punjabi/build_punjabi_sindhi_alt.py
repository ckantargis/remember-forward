"""
Batch 8 — Punjabi + Sindhi alt plates (Series 53, plates 53a–53d)
Secondary language: Sindhi (~33M speakers, Indo-Aryan, Pakistan/India)
Geographic link: Lahore (Punjabi center) to Hyderabad (Sindhi center) ~500mi
Both Indo-Aryan; shared history in the Indus-Ganges corridor
"""
from pathlib import Path

OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">
<rect x="0" y="0" width="480" height="680" fill="#fffff8"/>
<rect x="6" y="6" width="468" height="668" fill="none" stroke="#222" stroke-width="1.5"/>
<rect x="10" y="10" width="460" height="660" fill="none" stroke="#222" stroke-width="0.5"/>
<style>
text{font-family:Georgia,serif;fill:#111;}
.T{font-size:11px;font-weight:bold;}
.S{font-size:6.5px;}
.H{font-size:6.5px;font-weight:bold;}
.Hb{font-size:7px;font-weight:bold;fill:#fff;}
.L{font-size:7px;}
.Ls{font-size:6px;}
.Lx{font-size:5.5px;}
.M{font-size:6px;}
.F{font-size:7px;font-style:italic;}
.Fb{font-size:7.5px;font-weight:bold;}
</style>
'''

def close_svg(): return '</svg>\n'

def t(x, y, text, anchor='middle', cls='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.5):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#555" stroke-width="{sw}"/>\n'

def sh(y, label, cls='H'):
    return t(240, y, label, 'middle', cls)

def sec_divider(y, label):
    return (f'<rect x="10" y="{y}" width="460" height="13" fill="#111"/>\n'
            + f'<text x="240" y="{y+9.5}" text-anchor="middle" class="Hb">{esc(label)}</text>\n')

def footer(num, lang1, lang2, letter, desc):
    return (hr(634) +
            t(240, 643, f'PLATE {num}{letter} ALT  \u00b7  {lang1} / {lang2}  \u00b7  {desc}', 'middle', 'M') +
            t(240, 652, 'CC BY-SA 4.0  \u00b7  REMEMBERFORWARD.ORG', 'middle', 'M'))

# ── PLATE 53a  SCRIPT ────────────────────────────────────────────────────────
def plate53a():
    s = open_svg()
    s += t(240, 28, 'PUNJABI', 'middle', 'T')
    s += t(240, 40, 'GURMUKHI & SHAHMUKHI SCRIPTS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'GURMUKHI SCRIPT (INDIA)')
    s += t(240, 68, 'Gurmukhi (\u0a17\u0a41\u0a30\u0a2e\u0a41\u0a16\u0a40) — "from the mouth of the Guru"', 'middle', 'L')
    s += t(240, 78, 'Created by Guru Angad Dev Ji, 2nd Sikh Guru (1539 CE)', 'middle', 'Ls')
    s += t(240, 89, 'Abugida: 35 consonants, inherent /a/ vowel (muted with virama)', 'middle', 'Ls')
    s += t(240, 99, 'Consonants:', 'middle', 'H')
    s += t(240, 110, '\u0a38 /s/   \u0a39 /h/   \u0a15 /k/   \u0a16 /kh/   \u0a17 /g/   \u0a18 /gh/   \u0a19 /\u014b/', 'middle', 'L')
    s += t(240, 122, '\u0a1a /ch/  \u0a1b /chh/  \u0a1c /j/   \u0a1d /jh/   \u0a1e /\u00f1/', 'middle', 'L')
    s += t(240, 134, '\u0a24 /t/   \u0a25 /th/   \u0a26 /d/   \u0a27 /dh/   \u0a28 /n/', 'middle', 'L')
    s += t(240, 146, '\u0a2a /p/   \u0a2b /ph/   \u0a2c /b/   \u0a2d /bh/   \u0a2e /m/', 'middle', 'L')
    s += t(240, 157, 'Vowel diacritics attach above, below or beside consonants', 'middle', 'Ls')
    s += t(240, 168, '\u0a07 i   \u0a08 \u012b   \u0a09 u   \u0a0a \u016b   \u0a0f e   \u0a10 ai   \u0a13 o   \u0a14 au', 'middle', 'L')
    s += t(240, 178, 'Tonal markers: \u0a71 udaat (rising) \u0a70 tippi (nasal)', 'middle', 'Ls')
    s += hr(185)
    s += sh(193, 'PUNJABI WORD IN GURMUKHI')
    s += t(240, 206, '\u0a38\u0a24\u0a3f \u0a38\u0a4d\u0a30\u0a40 \u0a35\u0a3e\u0a39\u0a3f\u0a17\u0a41\u0a30\u0a42', 'middle', 'Fb')
    s += t(240, 217, '"Sat Sri Akal" — timeless truth (Sikh greeting)', 'middle', 'Ls')
    s += hr(225)
    s += sh(233, 'SHAHMUKHI SCRIPT (PAKISTAN)')
    s += t(240, 244, 'Shahmukhi (\u0634\u0627\u06c1\u0645\u06a9\u06be\u06cc) — "from the mouth of the King"', 'middle', 'L')
    s += t(240, 254, 'Perso-Arabic script, written right-to-left, 38+ letters', 'middle', 'Ls')
    s += t(240, 265, 'Same language, two completely different writing systems', 'middle', 'Ls')
    s += t(240, 275, 'Additional letters for Punjabi sounds:', 'middle', 'H')
    s += t(240, 286, '\u06ba \u00b7 \u06c1 \u00b7 \u06be \u00b7 \u067e \u00b7 \u0679 \u00b7 \u06b9  (nasal and retroflex markers)', 'middle', 'L')
    s += hr(295)
    # Divider
    s += sec_divider(302, 'SINDHI  \u00b7  \u0633\u0646\u068c\u064a  \u00b7  \u0938\u093f\u0928\u094d\u0927\u0940  \u00b7  SECONDARY LANGUAGE')
    s += sh(327, 'SINDHI SCRIPT — 52 LETTERS')
    s += t(240, 338, 'Largest Perso-Arabic alphabet of any language (52 letters)', 'middle', 'L')
    s += t(240, 348, 'Added letters represent sounds absent in Arabic/Urdu:', 'middle', 'Ls')
    s += t(240, 359, '\u06ba \u062c \u0621 \u06b3 \u06ad \u06b1 \u06bb (retroflex + implosive markers)', 'middle', 'L')
    s += t(240, 370, 'Four implosive consonants (unique in Indo-Aryan):', 'middle', 'H')
    s += t(240, 381, '\u0628\u0657 /\u0253/   \u062f\u0657 /\u0257/   \u062c\u0657 /\u0284/   \u06af\u0657 /\u0260/', 'middle', 'L')
    s += t(240, 392, 'Implosives: air pulled inward during closure', 'middle', 'Ls')
    s += t(240, 403, 'Devanagari used in India (Sindhi community post-partition)', 'middle', 'Ls')
    s += hr(411)
    s += sh(419, 'SCRIPT COMPARISON')
    s += t(240, 430, 'Punjabi (Shahmukhi):  \u067e\u0646\u062c\u0627\u0628\u06cc  (right-to-left)', 'middle', 'L')
    s += t(240, 441, 'Punjabi (Gurmukhi):  \u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40  (left-to-right)', 'middle', 'L')
    s += t(240, 452, 'Sindhi: \u0633\u0646\u068c\u064a (Arabic-based, right-to-left)', 'middle', 'L')
    s += t(240, 463, 'All three scripts coexist in the Punjab-Sindh corridor', 'middle', 'Ls')
    s += hr(471)
    s += sh(479, 'SHARED INDO-ARYAN HERITAGE')
    s += t(240, 490, 'Both descended from Sanskrit via Prakrits and Apabhramsas', 'middle', 'Ls')
    s += t(240, 500, 'Punjab (\u067e\u0646\u062c\u0627\u0628): "five rivers" — Indus + five tributaries', 'middle', 'Ls')
    s += t(240, 510, 'Sindh (\u0633\u0646\u062f\u06be): ancient name of the Indus River itself', 'middle', 'Ls')
    s += footer('53', 'PUNJABI', 'SINDHI', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 53b  PHONOLOGY ─────────────────────────────────────────────────────
def plate53b():
    s = open_svg()
    s += t(240, 28, 'PUNJABI', 'middle', 'T')
    s += t(240, 40, 'TONAL PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'THREE TONES OF PUNJABI')
    s += t(240, 68, 'Punjabi is the only tonal Indo-Aryan language', 'middle', 'L')
    s += t(240, 78, 'Tones arise from historical voiced aspirates losing aspiration:', 'middle', 'Ls')
    s += t(240, 89, 'Level tone (no mark):  k\u0101l \u00b7 \u0a15\u0a3e\u0a32  "time/black"', 'middle', 'L')
    s += t(240, 100, 'Rising tone (\u0301):  k\u00e1l \u00b7 \u0a15\u0a71\u0a32  "tomorrow/yesterday"', 'middle', 'L')
    s += t(240, 111, 'Falling tone (\u0300):  k\u00e0l \u00b7 \u0a15\u0a72\u0a32  "cheek"', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'CONSONANT INVENTORY')
    s += t(240, 139, 'Three-way contrast: voiceless / voiced / aspirated', 'middle', 'Ls')
    s += t(240, 149, 'Stops: p b bh  /  t d dh  /  \u0288 \u0256 \u0256h  /  k g gh', 'middle', 'L')
    s += t(240, 160, 'Retroflex set: \u0288 \u0256 \u0273 \u027d (tongue curled back to palate)', 'middle', 'L')
    s += t(240, 170, 'Approximants: v \u028b (labiodental) — rare cross-linguistically', 'middle', 'Ls')
    s += hr(178)
    s += sh(186, 'VOWEL SYSTEM')
    s += t(240, 197, 'Ten vowels: a \u0101 i \u012b u \u016b e \u025b o \u0254', 'middle', 'L')
    s += t(240, 207, 'Nasalization: \u0101\u0303 \u012b\u0303 \u016b\u0303 (like French nasals)', 'middle', 'L')
    s += t(240, 218, 'No diphthongs — all pure monophthongs', 'middle', 'Ls')
    s += hr(226)
    s += sh(234, 'TONE MINIMAL PAIRS')
    s += t(240, 245, 'kor (level) "leprosy"  \u2022  k\u00f3r (rising) "does"  \u2022  k\u00f2r (falling) "work"', 'middle', 'Ls')
    s += t(240, 256, 'ghar (level) "horse"  \u2022  gh\u00e1r (rising) "home"', 'middle', 'Ls')
    s += hr(264)
    # Divider
    s += sec_divider(271, 'SINDHI PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(296, 'FOUR IMPLOSIVE CONSONANTS')
    s += t(240, 307, 'Sindhi has four implosive (ingressive) consonants:', 'middle', 'L')
    s += t(240, 318, '/\u0253/ bilabial  \u2022  /\u0257/ dental  \u2022  /\u0284/ palatal  \u2022  /\u0260/ velar', 'middle', 'L')
    s += t(240, 329, 'Extremely rare: only Sindhi, Saraiki, and a few African languages', 'middle', 'Ls')
    s += t(240, 340, 'Produced by pulling larynx down while making closure', 'middle', 'Ls')
    s += hr(348)
    s += sh(356, 'SINDHI TONES & VOWELS')
    s += t(240, 367, 'No lexical tone (unlike Punjabi)', 'middle', 'L')
    s += t(240, 378, 'Ten oral vowels + nasalized counterparts', 'middle', 'L')
    s += t(240, 389, 'Preserves Sanskrit /v/ as /v/ (Hindi turned to /b/)', 'middle', 'Ls')
    s += t(240, 400, 'Retroflex stops: \u0288 \u0256 \u0273 (shared with Punjabi)', 'middle', 'L')
    s += hr(408)
    s += sh(416, 'PHONOLOGICAL BRIDGE')
    s += t(240, 427, 'Both languages share retroflex consonant set from Sanskrit', 'middle', 'Ls')
    s += t(240, 438, 'Punjabi tone  \u2260  Sindhi implosive — complementary features', 'middle', 'Ls')
    s += t(240, 449, 'Shared aspirate contrasts: p/ph  t/th  k/kh  b/bh  d/dh', 'middle', 'Ls')
    s += t(240, 460, 'Sindhi: "pitu" (father)  /  Punjabi: "pita" (\u0a2a\u0a3f\u0a24\u0a3e)', 'middle', 'L')
    s += t(240, 471, 'Sanskrit pitri \u2192 both descended via Prakrit prakrits', 'middle', 'Ls')
    s += hr(479)
    s += sh(487, 'REGIONAL SOUND DIFFERENCES')
    s += t(240, 498, 'Sindhi preserves ancient Sanskrit sounds better than Hindi', 'middle', 'Ls')
    s += t(240, 509, 'Punjabi: voiced aspirates shifted to tone (unique innovation)', 'middle', 'Ls')
    s += t(240, 520, 'Both languages spoken in adjacent Indus basin territory', 'middle', 'Ls')
    s += footer('53', 'PUNJABI', 'SINDHI', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 53c  GRAMMAR ───────────────────────────────────────────────────────
def plate53c():
    s = open_svg()
    s += t(240, 28, 'PUNJABI', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'WORD ORDER & BASIC STRUCTURE')
    s += t(240, 68, 'SOV: Subject  \u2192  Object  \u2192  Verb', 'middle', 'L')
    s += t(240, 78, 'Postpositions (not prepositions): ne/nu/de/to/vich', 'middle', 'L')
    s += t(240, 89, 'Main \u0a28\u0a47  \u00b7  \u0a28\u0a47  \u2192  ergative marker', 'middle', 'Ls')
    s += hr(97)
    s += sh(105, 'GENDER & AGREEMENT')
    s += t(240, 116, 'Two genders: masculine / feminine (no neuter)', 'middle', 'L')
    s += t(240, 126, 'Adjectives and verbs agree with subject gender/number', 'middle', 'Ls')
    s += t(240, 137, 'Munda \u0a2e\u0a41\u0a70\u0a21\u0a3e "boy"  \u2022  Kuri \u0a15\u0a41\u0a5c\u0a40 "girl"', 'middle', 'L')
    s += hr(145)
    s += sh(153, 'ERGATIVE ALIGNMENT')
    s += t(240, 164, 'Punjabi is split ergative: past tense uses ergative case', 'middle', 'L')
    s += t(240, 175, 'Mai\u0304 kitab padhi — I (ERG) book-FEM read-FEM', 'middle', 'Ls')
    s += t(240, 185, 'Subject of past transitive takes -ne; verb agrees with object', 'middle', 'Ls')
    s += hr(193)
    s += sh(201, 'ASPECT & TENSE')
    s += t(240, 212, 'Three aspects: simple / continuous / perfective', 'middle', 'L')
    s += t(240, 222, 'Future: main verb + gaa/gee/ge (masculine/feminine/plural)', 'middle', 'Ls')
    s += t(240, 233, 'No passive voice — use intransitive or impersonal constructions', 'middle', 'Ls')
    s += hr(241)
    # Divider
    s += sec_divider(248, 'SINDHI GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(273, 'SINDHI WORD ORDER')
    s += t(240, 284, 'SOV (same as Punjabi) with postpositions', 'middle', 'L')
    s += t(240, 295, 'Three genders: masculine / feminine / neuter (unlike Punjabi!)', 'middle', 'L')
    s += t(240, 306, 'Neuter gender for inanimates in many dialects', 'middle', 'Ls')
    s += hr(314)
    s += sh(322, 'SINDHI CASE SYSTEM')
    s += t(240, 333, 'Four cases: nominative / oblique / ablative / vocative', 'middle', 'L')
    s += t(240, 344, 'Agglutinative postpositions attach to oblique stem', 'middle', 'Ls')
    s += t(240, 355, 'Ergative split: past transitive uses oblique agent', 'middle', 'Ls')
    s += hr(363)
    s += sh(371, 'SINDHI VERB SYSTEM')
    s += t(240, 382, 'Rich verbal morphology: marks tense/aspect/mood/gender/number', 'middle', 'Ls')
    s += t(240, 393, 'Causative: aanu (come) \u2192 aayaraanu (cause to come)', 'middle', 'L')
    s += t(240, 404, 'Compound verbs common: karo "do" as vector verb', 'middle', 'Ls')
    s += hr(412)
    s += sh(420, 'GRAMMATICAL PARALLELS')
    s += t(240, 431, 'Both: SOV  \u2022  postpositions  \u2022  split ergativity', 'middle', 'L')
    s += t(240, 442, 'Both: rich aspect system inherited from Sanskrit', 'middle', 'Ls')
    s += t(240, 453, 'Punjabi: 2 genders  vs.  Sindhi: 3 genders (more archaic)', 'middle', 'Ls')
    s += t(240, 464, '"House" patterning: Punjabi ghar  \u2022  Sindhi ghar', 'middle', 'L')
    s += t(240, 475, '"Water": Punjabi pani  \u2022  Sindhi pani (identical!)', 'middle', 'L')
    s += footer('53', 'PUNJABI', 'SINDHI', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 53d  HISTORY ───────────────────────────────────────────────────────
def plate53d():
    s = open_svg()
    s += t(240, 28, 'PUNJABI', 'middle', 'T')
    s += t(240, 40, 'HISTORY & CULTURAL CONTEXT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'PUNJABI ORIGINS')
    s += t(240, 68, 'Descended from Sanskrit via Shauraseni Prakrit and Apabhramsha', 'middle', 'Ls')
    s += t(240, 79, 'Punjab = "Panj" (five) + "Ab" (water) — Land of Five Rivers', 'middle', 'L')
    s += t(240, 90, 'Five rivers: Jhelum, Chenab, Ravi, Beas, Sutlej', 'middle', 'Ls')
    s += t(240, 100, '~800 CE: Early Punjabi emerges from Apabhramsha dialects', 'middle', 'Ls')
    s += t(240, 111, 'Guru Granth Sahib (1604): Sacred scripture in Gurmukhi', 'middle', 'L')
    s += t(240, 122, 'Sikh tradition: language, script and religion intertwined', 'middle', 'Ls')
    s += t(240, 133, 'Waris Shah (1766): Heer Ranjha — masterwork of Punjabi literature', 'middle', 'Ls')
    s += hr(141)
    s += sh(149, 'PARTITION & DIVERGENCE (1947)')
    s += t(240, 160, 'India-Pakistan partition split the Punjabi region in two', 'middle', 'L')
    s += t(240, 171, 'Pakistani Punjab: Shahmukhi script (Arabic-based), Urdu official', 'middle', 'Ls')
    s += t(240, 182, 'Indian Punjab: Gurmukhi script, state language since 1966', 'middle', 'Ls')
    s += t(240, 193, 'Same spoken language; two writing systems; political border', 'middle', 'Ls')
    s += hr(201)
    s += sh(209, 'PUNJABI TODAY')
    s += t(240, 220, '~125M speakers; 10th most spoken language in the world', 'middle', 'L')
    s += t(240, 231, 'Diaspora: UK, Canada, USA — major communities worldwide', 'middle', 'Ls')
    s += t(240, 241, 'Bhangra music brings Punjabi language globally', 'middle', 'Ls')
    s += hr(249)
    # Divider
    s += sec_divider(256, 'SINDHI HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(281, 'SINDH: CRADLE OF CIVILIZATION')
    s += t(240, 292, 'Indus Valley Civilization (3300-1300 BCE): Mohenjo-daro in Sindh', 'middle', 'Ls')
    s += t(240, 303, 'Sindhi script = undeciphered Indus script (4000+ inscriptions)', 'middle', 'Ls')
    s += t(240, 314, '711 CE: Arab conquest of Sindh — Arabic influence on vocabulary', 'middle', 'Ls')
    s += t(240, 325, 'Shah Abdul Latif Bhittai (1689-1752): greatest Sindhi poet', 'middle', 'L')
    s += t(240, 336, 'Shah Jo Risalo: 30 surs (musical chapters) — Sindhi soul', 'middle', 'Ls')
    s += hr(344)
    s += sh(352, 'PARTITION & DIASPORA')
    s += t(240, 363, '1947: Hindu Sindhis fled to India; Muslim Sindhis remained', 'middle', 'L')
    s += t(240, 374, 'Indian Sindhi: adopted Devanagari; scattered across cities', 'middle', 'Ls')
    s += t(240, 385, 'Pakistani Sindhi: Perso-Arabic script; centered in Sindh province', 'middle', 'Ls')
    s += t(240, 396, 'Unique: Sindhi Hindu diaspora maintained identity without homeland', 'middle', 'Ls')
    s += hr(404)
    s += sh(412, 'SHARED RIVER HERITAGE')
    s += t(240, 423, '"Sindh" = ancient name of the Indus River (Sanskrit: Sindhu)', 'middle', 'L')
    s += t(240, 434, '"Punjab" = land of the five rivers that feed the Indus', 'middle', 'L')
    s += t(240, 445, 'Both civilizations built on the same Indus watershed', 'middle', 'Ls')
    s += t(240, 456, 'Lahore to Hyderabad: the Indus corridor connecting both peoples', 'middle', 'Ls')
    s += t(240, 467, 'Sanskrit \u2192 Prakrits \u2192 Apabhramshas \u2192 Punjabi + Sindhi', 'middle', 'Ls')
    s += footer('53', 'PUNJABI', 'SINDHI', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate53a_punjabi_sindhi_script_alt.svg', plate53a()),
                  ('plate53b_punjabi_sindhi_phonology_alt.svg', plate53b()),
                  ('plate53c_punjabi_sindhi_grammar_alt.svg', plate53c()),
                  ('plate53d_punjabi_sindhi_history_alt.svg', plate53d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
