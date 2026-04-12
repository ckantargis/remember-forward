"""
Batch 10 — Tamil + Telugu alt plates (Series 14, plates 14a–14d)
Secondary language: Telugu (~85M speakers, Dravidian, Andhra Pradesh/Telangana)
Geographic link: Chennai (Tamil center) to Hyderabad (Telugu center) ~400mi
Both major Dravidian languages of South India; longest continuous literary traditions
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

# ── PLATE 14a  SCRIPT ────────────────────────────────────────────────────────
def plate14a():
    s = open_svg()
    s += t(240, 28, 'TAMIL', 'middle', 'T')
    s += t(240, 40, 'TAMIL SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TAMIL SCRIPT — AN ABUGIDA')
    s += t(240, 68, 'Derived from Brahmi via Tamil-Brahmi (3rd c. BCE)', 'middle', 'L')
    s += t(240, 79, 'Oldest literary tradition in India: 2000+ years continuous', 'middle', 'L')
    s += t(240, 90, '18 consonants + 12 vowels = 247 total characters (with combinations)', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'TAMIL CONSONANTS')
    s += t(240, 117, '\u0b95 k  \u0b99 ng  \u0b9a c  \u0b9e ny  \u0b9f T  \u0ba3 N  \u0ba4 t  \u0ba8 n  \u0baa p  \u0bae m', 'middle', 'L')
    s += t(240, 128, '\u0baf y  \u0bb0 r  \u0bb2 l  \u0bb5 v  \u0bb4 zh  \u0bb3 L  \u0bb1 rr  \u0ba9 n (alveolar)', 'middle', 'L')
    s += t(240, 139, 'No aspiration contrast: single series of stops', 'middle', 'Ls')
    s += t(240, 150, 'zh /\u0292/ retroflex approximant: unique to Tamil-Malayalam', 'middle', 'L')
    s += t(240, 161, 'L /\u026d/ retroflex lateral: distinct from l', 'middle', 'L')
    s += hr(169)
    s += sh(177, 'TAMIL VOWELS')
    s += t(240, 188, '\u0b85 a  \u0b86 \u0101  \u0b87 i  \u0b88 \u012b  \u0b89 u  \u0b8a \u016b  \u0b8e e  \u0b8f \u0113  \u0b90 ai  \u0b92 o  \u0b93 \u014d  \u0b94 au', 'middle', 'L')
    s += t(240, 199, 'Vowel sign (matra) written around consonant base', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'SAMPLE TEXT')
    s += t(240, 227, '\u0bb5\u0bbe\u0bb4\u0bcd\u0b95  — Vaazha "May you prosper" (greeting)', 'middle', 'L')
    s += t(240, 238, '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd  — Tamil "Tamil language"', 'middle', 'L')
    s += hr(246)
    # Divider
    s += sec_divider(253, 'TELUGU  \u00b7  \u0c24\u0c46\u0c32\u0c41\u0c17\u0c41  \u00b7  SECONDARY LANGUAGE')
    s += sh(278, 'TELUGU SCRIPT')
    s += t(240, 289, 'Also from Brahmi; shares Kadamba/Vengi calligraphic tradition', 'middle', 'Ls')
    s += t(240, 300, 'Telugu script: rounded forms with consistent circular elements', 'middle', 'Ls')
    s += t(240, 311, '~52 letters including Sanskrit-borrowed aspirates and sibilants', 'middle', 'L')
    s += hr(319)
    s += sh(327, 'TELUGU CONSONANTS')
    s += t(240, 338, '\u0c15 k  \u0c16 kh  \u0c17 g  \u0c18 gh  \u0c19 ng', 'middle', 'L')
    s += t(240, 349, '\u0c1a c  \u0c1b ch  \u0c1c j  \u0c1d jh  \u0c1e ny', 'middle', 'L')
    s += t(240, 360, 'Telugu has ASPIRATED stops (Tamil does NOT!)', 'middle', 'L')
    s += t(240, 371, 'Telugu: borrowed Sanskrit aspirate set kh gh chh jh etc.', 'middle', 'Ls')
    s += hr(379)
    s += sh(387, 'SCRIPT DIVERGENCE')
    s += t(240, 398, 'Tamil: no aspirates in native words  \u2022  Telugu: has aspirates', 'middle', 'L')
    s += t(240, 409, 'Tamil: 18 consonants  \u2022  Telugu: ~36 consonants (with aspirates)', 'middle', 'L')
    s += t(240, 420, 'Both: abugida structure  \u2022  both: Brahmi ancestry', 'middle', 'L')
    s += t(240, 431, 'Both: rounded letterforms from palm-leaf scribing tradition', 'middle', 'Ls')
    s += footer('14', 'TAMIL', 'TELUGU', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 14b  PHONOLOGY ─────────────────────────────────────────────────────
def plate14b():
    s = open_svg()
    s += t(240, 28, 'TAMIL', 'middle', 'T')
    s += t(240, 40, 'DRAVIDIAN PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TAMIL CONSONANT FEATURES')
    s += t(240, 68, 'No aspiration contrast (unlike Sanskrit, Telugu, Hindi)', 'middle', 'L')
    s += t(240, 79, 'Five places of articulation with full retroflexes:', 'middle', 'L')
    s += t(240, 90, 'Velar k \u2022 Palatal c \u2022 Retroflex T \u2022 Dental t \u2022 Labial p', 'middle', 'L')
    s += t(240, 101, 'zh /\u0292/ retroflex approximant: ONLY in Tamil and Malayalam', 'middle', 'L')
    s += t(240, 112, 'Distinguishes: l /l/  \u2022  L /\u026d/ (retroflex lateral)  \u2022  zh /\u0292/', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'CONTEXT-DEPENDENT ALLOPHONES')
    s += t(240, 139, 'Tamil consonants change sound by position in word:', 'middle', 'L')
    s += t(240, 150, 'k = /k/ at start of word  \u2022  /\u0261/ between vowels', 'middle', 'L')
    s += t(240, 161, 't = /t/ at start  \u2022  /\u00f0/ or /d/ between vowels', 'middle', 'Ls')
    s += t(240, 172, 'p = /p/ initially  \u2022  /b/ or /\u03b2/ medially', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'TAMIL VOWELS')
    s += t(240, 199, '5 short + 5 long: a/\u0101  i/\u012b  u/\u016b  e/\u0113  o/\u014d  + ai au', 'middle', 'L')
    s += t(240, 210, 'Length is phonemic: paal "milk"  \u2022  pal "tooth"', 'middle', 'L')
    s += t(240, 221, 'No nasal vowels (unlike Sanskrit)', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'TELUGU PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'TELUGU CONSONANT SYSTEM')
    s += t(240, 272, 'Four-way stop contrast (more than Tamil):', 'middle', 'L')
    s += t(240, 283, 'voiceless plain / voiceless aspirate / voiced plain / voiced aspirate', 'middle', 'Ls')
    s += t(240, 294, 'p  ph  b  bh  /  t  th  d  dh  /  k  kh  g  gh', 'middle', 'L')
    s += t(240, 305, 'Borrowed from Sanskrit; Telugu integrated full Sanskrit phonology', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'TELUGU VOWELS')
    s += t(240, 332, 'Similar 5+5 short/long vowel system: a/\u0101 i/\u012b u/\u016b e/\u0113 o/\u014d', 'middle', 'L')
    s += t(240, 343, 'No vowel reduction; all vowels pronounced fully', 'middle', 'Ls')
    s += t(240, 354, 'Telugu: no zh /\u0292/ (that retroflex approximant is Tamil-specific)', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'DRAVIDIAN PHONOLOGICAL PARALLELS')
    s += t(240, 381, 'Both: retroflex series T D N L (Dravidian hallmark)', 'middle', 'L')
    s += t(240, 392, 'Both: 5+5 short/long vowels  \u2022  both: no tone', 'middle', 'L')
    s += t(240, 403, 'Both: SOV word order  \u2022  both: agglutinative morphology', 'middle', 'L')
    s += t(240, 414, 'Tamil: no aspiration, zh present  \u2022  Telugu: aspiration, no zh', 'middle', 'Ls')
    s += t(240, 425, 'Telugu more Sanskrit-influenced phonologically than Tamil', 'middle', 'Ls')
    s += footer('14', 'TAMIL', 'TELUGU', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 14c  GRAMMAR ───────────────────────────────────────────────────────
def plate14c():
    s = open_svg()
    s += t(240, 28, 'TAMIL', 'middle', 'T')
    s += t(240, 40, 'DRAVIDIAN GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TAMIL CASE SYSTEM (8 CASES)')
    s += t(240, 68, 'Nominative (subject)  \u2022  Accusative (object)  \u2022  Dative', 'middle', 'L')
    s += t(240, 79, 'Sociative  \u2022  Instrumental  \u2022  Ablative  \u2022  Genitive  \u2022  Locative', 'middle', 'L')
    s += t(240, 90, 'Cases are suffixed (agglutinative): maram "tree"', 'middle', 'Ls')
    s += t(240, 101, 'marattu (gen.) \u2022 marattukkku (dat.) \u2022 marattil (loc.)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'TAMIL NOUN CLASSES')
    s += t(240, 128, 'Nouns divided: High class (rational) vs. Low class (non-rational)', 'middle', 'L')
    s += t(240, 139, 'High class: humans + deities (grammatically "rational")', 'middle', 'L')
    s += t(240, 150, 'Low class: animals, plants, objects (grammatically "irrational")', 'middle', 'L')
    s += t(240, 161, 'Gender within high class: masculine (avan) / feminine (aval)', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'TAMIL VERB SYSTEM')
    s += t(240, 188, 'Verbs conjugate for: person \u2022 number \u2022 gender \u2022 tense', 'middle', 'L')
    s += t(240, 199, 'Three tenses: past / present / future', 'middle', 'L')
    s += t(240, 210, 'Negative verb forms: separate paradigm (not just "not + verb")', 'middle', 'L')
    s += t(240, 221, 'Diglossia: literary Tamil \u2260 spoken Tamil (different verb forms)', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'TELUGU GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'TELUGU CASE SYSTEM (7 CASES)')
    s += t(240, 272, 'Nominative \u2022 Accusative \u2022 Instrumental \u2022 Dative', 'middle', 'L')
    s += t(240, 283, 'Ablative \u2022 Genitive \u2022 Locative', 'middle', 'L')
    s += t(240, 294, 'Same agglutinative case system: il\u016bdu "house"', 'middle', 'Ls')
    s += t(240, 305, 'il\u016bniki (dat.) \u2022 il\u016blo (loc.) \u2022 il\u016bnu (acc.)', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'TELUGU NOUN CLASSES')
    s += t(240, 332, 'Similar rational/irrational distinction as Tamil', 'middle', 'L')
    s += t(240, 343, 'Masculine / feminine / neuter for rational nouns', 'middle', 'L')
    s += t(240, 354, 'Telugu neuter class broader than Tamil (includes many animals)', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'TELUGU VERB SYSTEM')
    s += t(240, 381, 'Same SOV structure; verbs mark person/number/gender/tense', 'middle', 'L')
    s += t(240, 392, 'Participial construction: elaborate non-finite verb forms', 'middle', 'Ls')
    s += t(240, 403, 'Telugu diglossia: grantham (literary) vs. vyavaharikam (spoken)', 'middle', 'Ls')
    s += hr(411)
    s += sh(419, 'SHARED DRAVIDIAN GRAMMAR')
    s += t(240, 430, 'Both: SOV  \u2022  agglutinative  \u2022  postpositions  \u2022  rational/irrational', 'middle', 'L')
    s += t(240, 441, 'Both: no articles  \u2022  relative clauses BEFORE noun (unlike English)', 'middle', 'L')
    s += t(240, 452, 'Both: diglossia  \u2022  both: ancient literary traditions', 'middle', 'L')
    s += footer('14', 'TAMIL', 'TELUGU', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 14d  HISTORY ───────────────────────────────────────────────────────
def plate14d():
    s = open_svg()
    s += t(240, 28, 'TAMIL', 'middle', 'T')
    s += t(240, 40, 'HISTORY & DRAVIDIAN CIVILIZATIONS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TAMIL ORIGINS')
    s += t(240, 68, '~300 BCE: Tamil-Brahmi inscriptions — oldest Dravidian writing', 'middle', 'L')
    s += t(240, 79, 'Sangam literature (300 BCE-300 CE): world-class ancient poetry', 'middle', 'L')
    s += t(240, 90, 'Sangam = "assembly of poets" at Madurai — 8 anthologies survive', 'middle', 'Ls')
    s += t(240, 101, 'Tolkappiyam (~1st c. BCE): grammar text; first comprehensive Indian grammar', 'middle', 'Ls')
    s += t(240, 112, 'Chola, Pandya, Chera kingdoms: three ancient Tamil dynasties', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'TAMIL EMPIRES')
    s += t(240, 139, 'Pallava dynasty (275-897 CE): Tamil cultural peak; spread to SE Asia', 'middle', 'Ls')
    s += t(240, 150, 'Chola Empire (848-1279 CE): naval power; temples across India and SE Asia', 'middle', 'L')
    s += t(240, 161, 'Thiruvalluvar: Kural (1-2 CE?): 1330 couplets on life, ethics, love', 'middle', 'L')
    s += t(240, 172, 'Kural translated into 80+ languages — Tamil philosophic peak', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'TAMIL TODAY')
    s += t(240, 199, '~80M speakers; official in Tamil Nadu, Sri Lanka, Singapore, Malaysia', 'middle', 'L')
    s += t(240, 210, 'One of 22 scheduled languages of India; classical language status', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'TELUGU HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'TELUGU ORIGINS')
    s += t(240, 261, '~400-500 CE: earliest Telugu inscriptions (later than Tamil)', 'middle', 'L')
    s += t(240, 272, 'Proto-Dravidian: common ancestor of Tamil and Telugu ~3000 BCE', 'middle', 'Ls')
    s += t(240, 283, 'Telugu and Tamil diverged earlier than Romance languages diverged', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'TELUGU LITERARY GOLDEN AGE')
    s += t(240, 310, 'Nannaya (11th c.): translated Mahabharata into Telugu — first great work', 'middle', 'L')
    s += t(240, 321, 'Tikkana (13th c.) + Errana (14th c.): completed Mahabharata translation', 'middle', 'Ls')
    s += t(240, 332, 'Vijayanagara Empire (14th-17th c.): Telugu language and culture peak', 'middle', 'L')
    s += t(240, 343, 'Tenali Ramakrishna: court poet; "Telugu Birbal" for wit and wisdom', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'TELUGU TODAY')
    s += t(240, 370, '~85M speakers; largest Dravidian language by speakers', 'middle', 'L')
    s += t(240, 381, 'Official: Andhra Pradesh + Telangana (two separate states since 2014)', 'middle', 'L')
    s += t(240, 392, 'Telugu film (Tollywood): 2nd largest film industry in India', 'middle', 'L')
    s += hr(400)
    s += sh(408, 'DRAVIDIAN CIVILIZATIONS')
    s += t(240, 419, 'Tamil and Telugu: two of four classical Dravidian languages', 'middle', 'L')
    s += t(240, 430, 'Indus Valley (~3300 BCE): possibly Dravidian (not yet deciphered)', 'middle', 'Ls')
    s += t(240, 441, 'Both languages: resisted Sanskrit dominance while absorbing it', 'middle', 'Ls')
    s += t(240, 452, 'Both: built temple civilizations across South and SE Asia', 'middle', 'Ls')
    s += t(240, 463, 'Two great Dravidian river civilizations: Kaveri (Tamil) \u2022 Krishna (Telugu)', 'middle', 'Ls')
    s += footer('14', 'TAMIL', 'TELUGU', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate14a_tamil_telugu_script_alt.svg', plate14a()),
                  ('plate14b_tamil_telugu_phonology_alt.svg', plate14b()),
                  ('plate14c_tamil_telugu_grammar_alt.svg', plate14c()),
                  ('plate14d_tamil_telugu_history_alt.svg', plate14d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
