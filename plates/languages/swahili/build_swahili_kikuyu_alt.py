"""
Batch 10 — Swahili + Kikuyu alt plates (Series 20, plates 20a–20d)
Secondary language: Kikuyu/Gikuyu (~8M speakers, Bantu, Kenya)
Geographic link: Nairobi (Kikuyu center) to Mombasa (Swahili coast) ~300mi
Both Bantu languages; Kikuyu is Kenya's largest ethnic group; Swahili is the national language
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

# ── PLATE 20a  SCRIPT ────────────────────────────────────────────────────────
def plate20a():
    s = open_svg()
    s += t(240, 28, 'SWAHILI', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEMS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SWAHILI SCRIPT HISTORY')
    s += t(240, 68, 'Swahili = "sawaahili" (Arabic: "of the coast")', 'middle', 'L')
    s += t(240, 79, 'Arabic script (Ajami) used for 700+ years before Latin', 'middle', 'L')
    s += t(240, 90, 'Utendi wa Tambuka (1728): oldest known Swahili manuscript in Ajami', 'middle', 'Ls')
    s += t(240, 101, '19th c.: Latin alphabet introduced by European missionaries', 'middle', 'Ls')
    s += t(240, 112, '1930: Standard Swahili Latin orthography adopted', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'SWAHILI LATIN ALPHABET')
    s += t(240, 139, '24 letters; no Q or X in native words', 'middle', 'L')
    s += t(240, 150, 'Digraphs: ch /t\u0283/ \u2022 gh /\u0263/ \u2022 ng\u2019 /\u014b/ \u2022 sh /\u0283/ \u2022 dh /\u00f0/', 'middle', 'L')
    s += t(240, 161, 'th = /\u03b8/ (dental fricative, from Arabic loanwords)', 'middle', 'L')
    s += t(240, 172, 'Tone: not marked — Swahili is traditionally described as non-tonal', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'SAMPLE TEXT')
    s += t(240, 200, 'Habari yako?  "How are you?"  (lit. "Your news?")', 'middle', 'L')
    s += t(240, 211, 'Nzuri sana.  "Very good."', 'middle', 'L')
    s += t(240, 222, 'Hakuna matata.  "No problem."  (lit. "no worries")', 'middle', 'L')
    s += hr(230)
    # Divider
    s += sec_divider(237, 'KIKUYU / GIKUYU  \u00b7  G\u012aK\u0168Y\u0168  \u00b7  SECONDARY LANGUAGE')
    s += sh(262, 'KIKUYU LATIN ALPHABET')
    s += t(240, 273, 'Latin alphabet; standardized by missionaries and linguists', 'middle', 'L')
    s += t(240, 284, 'Kikuyu phonemic features in orthography:', 'middle', 'H')
    s += t(240, 295, 'ng\u2019 = /\u014b/ (velar nasal)  \u2022  th = /\u03b4/ or /\u03b8/', 'middle', 'L')
    s += t(240, 306, 'Long vowels marked by doubling: aa ii uu ee oo', 'middle', 'L')
    s += t(240, 317, 'Tone: HIGH marked by acute accent (a\u0301, e\u0301, i\u0301, o\u0301, u\u0301)', 'middle', 'L')
    s += hr(325)
    s += sh(333, 'KIKUYU SAMPLE')
    s += t(240, 345, 'N\u012b w\u0113ga  "I am fine"  (response to greeting)', 'middle', 'L')
    s += t(240, 356, 'N\u012b \u0169r\u0169  "It is good"', 'middle', 'L')
    s += t(240, 367, 'Gikuyu = self-name  \u2022  Kikuyu = name used by non-Kikuyu', 'middle', 'Ls')
    s += hr(375)
    s += sh(383, 'SCRIPT COMPARISON')
    s += t(240, 394, 'Both: Latin alphabet  \u2022  both: digraphs for Bantu sounds', 'middle', 'L')
    s += t(240, 405, 'Swahili: no tone marking  \u2022  Kikuyu: tone marked with accents', 'middle', 'L')
    s += t(240, 416, 'Swahili: Arabic loan layer  \u2022  Kikuyu: minimal Arabic influence', 'middle', 'Ls')
    s += t(240, 427, 'Both: ng\u2019 digraph for /\u014b/ (shared Bantu feature)', 'middle', 'Ls')
    s += footer('20', 'SWAHILI', 'KIKUYU', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 20b  PHONOLOGY ─────────────────────────────────────────────────────
def plate20b():
    s = open_svg()
    s += t(240, 28, 'SWAHILI', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SWAHILI CONSONANT SYSTEM')
    s += t(240, 68, 'Stops: p b \u2022 t d \u2022 k g (no aspiration contrast)', 'middle', 'L')
    s += t(240, 79, 'Fricatives: f v \u2022 s z \u2022 sh /\u0283/ \u2022 gh /\u0263/ \u2022 h', 'middle', 'L')
    s += t(240, 90, 'Affricates: ch /t\u0283/ \u2022 dh /\u00f0/ \u2022 th /\u03b8/ (Arabic loans)', 'middle', 'L')
    s += t(240, 101, 'Nasals: m n ng\u2019 /\u014b/ \u2022 Prenasalized: mb nd ng nj', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'SWAHILI VOWELS')
    s += t(240, 128, 'Five pure vowels: a e i o u (no long/short distinction)', 'middle', 'L')
    s += t(240, 139, 'No vowel reduction (every vowel pronounced fully)', 'middle', 'L')
    s += t(240, 150, 'Penultimate stress: almost always on second-to-last syllable', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'SYLLABLE STRUCTURE')
    s += t(240, 177, 'Preferred: CV (consonant + vowel) \u2022 V also possible', 'middle', 'L')
    s += t(240, 188, 'Syllabic nasals: m-tu "person" \u2022 n-chi "country"', 'middle', 'L')
    s += t(240, 199, 'No final consonants in native words (all end in vowel)', 'middle', 'Ls')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'KIKUYU PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'KIKUYU TONAL SYSTEM')
    s += t(240, 250, 'Kikuyu is a TONAL language (Swahili traditionally is not)', 'middle', 'L')
    s += t(240, 261, 'High (H) and Low (L) tones distinguish meaning and grammar:', 'middle', 'L')
    s += t(240, 272, 'tHaat\u00e9 "three" \u2022 thaate "to walk" (tone distinguishes)', 'middle', 'L')
    s += t(240, 283, 'Tone also marks tense in verbs: perfective vs. imperfective', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'KIKUYU CONSONANTS')
    s += t(240, 310, 'Similar inventory to Swahili with key additions:', 'middle', 'L')
    s += t(240, 321, '\u0263 /\u0263/ (voiced velar fricative)  \u2022  \u03b4 /\u00f0/ (voiced dental fricative)', 'middle', 'L')
    s += t(240, 332, 'Prenasalized stops: mb nd ng (same as Swahili Bantu heritage)', 'middle', 'L')
    s += hr(340)
    s += sh(348, 'KIKUYU VOWELS')
    s += t(240, 359, 'Five vowels with phonemic length distinction: a/aa i/ii u/uu e/ee o/oo', 'middle', 'L')
    s += t(240, 370, 'Unlike Swahili: long vowels are phonemic in Kikuyu', 'middle', 'L')
    s += t(240, 381, 'm\u016bk\u0129 "woman" \u2022 m\u016bkii "old woman" (length distinction)', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'SHARED BANTU FEATURES')
    s += t(240, 408, 'Both: 5 vowels  \u2022  prenasalized stops  \u2022  syllabic nasals', 'middle', 'L')
    s += t(240, 419, 'Both: CV syllable preference  \u2022  open syllable words', 'middle', 'L')
    s += t(240, 430, 'Kikuyu: adds tone + vowel length  \u2022  Swahili: simpler phonology', 'middle', 'Ls')
    s += t(240, 441, 'Swahili simplicity: why it spread as a trade language', 'middle', 'Ls')
    s += footer('20', 'SWAHILI', 'KIKUYU', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 20c  GRAMMAR ───────────────────────────────────────────────────────
def plate20c():
    s = open_svg()
    s += t(240, 28, 'SWAHILI', 'middle', 'T')
    s += t(240, 40, 'NOUN CLASS GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SWAHILI NOUN CLASSES (15+)')
    s += t(240, 68, 'M/WA (1/2): people \u2022 mtu/watu "person/people"', 'middle', 'L')
    s += t(240, 79, 'M/MI (3/4): plants/objects \u2022 mti/miti "tree/trees"', 'middle', 'L')
    s += t(240, 90, 'N/N (9/10): animals/borrowings \u2022 ndege/ndege "bird/birds"', 'middle', 'L')
    s += t(240, 101, 'KI/VI (7/8): things \u2022 kitu/vitu "thing/things"', 'middle', 'L')
    s += t(240, 112, 'JI/MA (5/6): fruits, augmentatives \u2022 jicho/macho "eye/eyes"', 'middle', 'L')
    s += t(240, 123, 'U/N (11/10): abstract, long things \u2022 uso "face" (no plural)', 'middle', 'L')
    s += hr(131)
    s += sh(139, 'SWAHILI AGREEMENT CHAIN')
    s += t(240, 150, 'Every modifier matches noun class prefix:', 'middle', 'L')
    s += t(240, 161, 'mtoto mmoja mzuri anakimbia', 'middle', 'L')
    s += t(240, 172, '"one good child runs" — m- on all 4 words (class 1)', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'SWAHILI VERB TEMPLATE')
    s += t(240, 199, 'SP-TNS-OP-ROOT-FV: ninakupenda "I love you"', 'middle', 'L')
    s += t(240, 210, 'ni-na-ku-pend-a = I-PRES-you-love-FV', 'middle', 'L')
    s += t(240, 221, 'wa-li-ni-ona = they-PAST-me-see = "they saw me"', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'KIKUYU GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'KIKUYU NOUN CLASSES (18)')
    s += t(240, 272, 'More noun classes than Swahili (archaic Proto-Bantu preserved)', 'middle', 'L')
    s += t(240, 283, 'Class 1/2 (m\u0169-/a-): people \u2022 m\u0169nd\u0169/and\u0169 "person/people"', 'middle', 'L')
    s += t(240, 294, 'Class 3/4 (m\u0169-/m\u012b-): trees \u2022 m\u0169t\u012b/m\u012bt\u012b "tree/trees"', 'middle', 'L')
    s += t(240, 305, 'Class 7/8 (k\u012b-/\u012by\u0169-): things \u2022 k\u012b\u00fat\u0169/\u012by\u0169\u00fat\u0169 "thing/things"', 'middle', 'L')
    s += t(240, 316, 'Abstract class (o\u0169-): concepts unique to Kikuyu system', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'KIKUYU VERB SYSTEM')
    s += t(240, 343, 'Same SP-TNS-OP-ROOT template as Swahili', 'middle', 'L')
    s += t(240, 354, 'Tone marks tense/aspect: rising tone = perfective', 'middle', 'L')
    s += t(240, 365, 'Verb extensions: -ir- (applicative), -an- (reciprocal)', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'BANTU GRAMMAR PARALLELS')
    s += t(240, 392, 'Both: noun class system controlling all agreement', 'middle', 'L')
    s += t(240, 403, 'Both: SP-TNS-OP-ROOT-FV verb template', 'middle', 'L')
    s += t(240, 414, 'Both: verb extensions (applicative, causative, reciprocal)', 'middle', 'L')
    s += t(240, 425, 'Swahili: fewer classes, simpler agreement chains', 'middle', 'Ls')
    s += t(240, 436, 'Kikuyu: more classes, tonal grammar layer on top', 'middle', 'Ls')
    s += footer('20', 'SWAHILI', 'KIKUYU', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 20d  HISTORY ───────────────────────────────────────────────────────
def plate20d():
    s = open_svg()
    s += t(240, 28, 'SWAHILI', 'middle', 'T')
    s += t(240, 40, 'HISTORY & EAST AFRICAN COAST', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SWAHILI ORIGINS')
    s += t(240, 68, 'Bantu speakers reach East African coast ~100-300 CE', 'middle', 'L')
    s += t(240, 79, 'Arab traders: contacts from ~700 CE; Arabic loanwords pour in', 'middle', 'L')
    s += t(240, 90, 'City-states: Mombasa, Malindi, Kilwa, Zanzibar, Sofala (900-1500 CE)', 'middle', 'Ls')
    s += t(240, 101, 'Swahili culture: uniquely African-Arab-Indian Ocean fusion', 'middle', 'Ls')
    s += t(240, 112, '16th c.: Portuguese disrupt Indian Ocean trade networks', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'SWAHILI AS LINGUA FRANCA')
    s += t(240, 139, '19th c.: Arab-Swahili traders spread Swahili into interior', 'middle', 'L')
    s += t(240, 150, 'Slave and ivory trade routes: Swahili follows caravan paths', 'middle', 'Ls')
    s += t(240, 161, 'German East Africa, British East Africa: colonizers adopt Swahili', 'middle', 'Ls')
    s += t(240, 172, 'Today: 200M+ speakers across 14 countries (L1 + L2)', 'middle', 'L')
    s += t(240, 183, 'UN African Union, East African Community: Swahili is official', 'middle', 'L')
    s += hr(191)
    # Divider
    s += sec_divider(198, 'KIKUYU HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(223, 'GIKUYU ORIGIN TRADITION')
    s += t(240, 234, 'Gikuyu tradition: Ngai (God) gave first man and woman Mount Kenya', 'middle', 'Ls')
    s += t(240, 245, 'Kikuyu heartland: Central Kenya highlands around Mount Kenya', 'middle', 'L')
    s += t(240, 256, 'Settled agriculturalists: fig tree (mugomo) central to culture', 'middle', 'Ls')
    s += t(240, 267, 'Nine clans (mbari): traced to nine daughters of founder couple', 'middle', 'Ls')
    s += hr(275)
    s += sh(283, 'COLONIAL PERIOD & MAU MAU')
    s += t(240, 294, 'British colonists seized Kikuyu highlands (White Highlands)', 'middle', 'L')
    s += t(240, 305, '1952-1960: Mau Mau uprising — Kikuyu-led anti-colonial revolt', 'middle', 'L')
    s += t(240, 316, 'Jomo Kenyatta: Kikuyu; first president of Kenya (1964-1978)', 'middle', 'L')
    s += t(240, 327, 'Ngugi wa Thiongo: world-renowned Kikuyu novelist and playwright', 'middle', 'Ls')
    s += hr(335)
    s += sh(343, 'KIKUYU TODAY')
    s += t(240, 354, '~8M speakers; Kenya\'s largest ethnic group (~17% of population)', 'middle', 'L')
    s += t(240, 365, 'Nairobi surrounds traditional Kikuyu territory', 'middle', 'Ls')
    s += t(240, 376, 'Kikuyu economic dominance: nicknamed "the Jews of Africa" by some', 'middle', 'Ls')
    s += hr(384)
    s += sh(392, 'SWAHILI-KIKUYU KENYA')
    s += t(240, 403, 'Kenya: Swahili (national) + English (official) + Kikuyu (largest L1)', 'middle', 'Ls')
    s += t(240, 414, 'Nairobi: Swahili as urban lingua franca among all Kikuyu', 'middle', 'Ls')
    s += t(240, 425, 'Kikuyu learning Swahili: both within 300mi, both Bantu', 'middle', 'Ls')
    s += t(240, 436, 'Shared Bantu grammar gives Kikuyu speakers advantage with Swahili', 'middle', 'Ls')
    s += t(240, 447, 'Ngugi wa Thiongo: writes in Kikuyu as political act of decolonization', 'middle', 'Ls')
    s += footer('20', 'SWAHILI', 'KIKUYU', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate20a_swahili_kikuyu_script_alt.svg', plate20a()),
                  ('plate20b_swahili_kikuyu_phonology_alt.svg', plate20b()),
                  ('plate20c_swahili_kikuyu_grammar_alt.svg', plate20c()),
                  ('plate20d_swahili_kikuyu_history_alt.svg', plate20d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
