"""
Batch 9 — Shona + Nyanja alt plates (Series 36, plates 36a–36d)
Secondary language: Nyanja/Chichewa (~15M speakers, Bantu, Malawi/Zambia/Mozambique)
Geographic link: Harare (Shona center) to Lilongwe (Nyanja heartland) ~430mi
Both Southern Bantu languages sharing Bantu noun class system
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

# ── PLATE 36a  SCRIPT ────────────────────────────────────────────────────────
def plate36a():
    s = open_svg()
    s += t(240, 28, 'SHONA', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SHONA LATIN ALPHABET')
    s += t(240, 68, 'Shona uses the Latin alphabet with digraphs for Bantu sounds', 'middle', 'L')
    s += t(240, 79, 'Standardized 1931 by Clement Doke (Union Shona orthography)', 'middle', 'Ls')
    s += t(240, 90, 'No pre-colonial writing system; oral tradition dominant', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'DISTINCTIVE SHONA LETTERS')
    s += t(240, 117, 'zh /\u0292/ — like measure, vision (rare phoneme in African languages)', 'middle', 'L')
    s += t(240, 128, 'sv /s\u028b/ — labiodental fricative cluster', 'middle', 'L')
    s += t(240, 139, 'zv /z\u028b/ — voiced labiodental fricative cluster', 'middle', 'L')
    s += t(240, 150, 'bv /b\u028b/ — bilabial+labiodental cluster', 'middle', 'L')
    s += t(240, 161, 'ng\u2019 /\u014b/ — velar nasal (syllable-final or as syllable)', 'middle', 'L')
    s += hr(169)
    s += sh(177, 'SHONA DIALECTS (UNION SHONA)')
    s += t(240, 188, 'Five major dialect clusters combined in standardization:', 'middle', 'L')
    s += t(240, 199, 'Karanga \u2022 Zezuru \u2022 Korekore \u2022 Manyika \u2022 Ndau', 'middle', 'L')
    s += t(240, 210, 'Unified written standard; spoken dialects vary considerably', 'middle', 'Ls')
    s += hr(218)
    s += sh(226, 'SAMPLE TEXT')
    s += t(240, 238, 'Mhoro! Zita rangu ndi... "Hello! My name is..."', 'middle', 'L')
    s += t(240, 249, 'Unobva kupi? "Where do you come from?"', 'middle', 'L')
    s += t(240, 260, 'Maita basa. "Thank you." (lit. "You have done work")', 'middle', 'L')
    s += hr(268)
    # Divider
    s += sec_divider(275, 'NYANJA / CHICHEWA  \u00b7  SECONDARY LANGUAGE')
    s += sh(300, 'NYANJA LATIN ALPHABET')
    s += t(240, 311, 'Latin alphabet standardized during British colonial period', 'middle', 'L')
    s += t(240, 322, 'Nyanja = "lake" (people of the lake — Lake Malawi/Nyasa)', 'middle', 'L')
    s += t(240, 333, 'Chichewa = name used in Malawi; Nyanja = name used in Zambia', 'middle', 'Ls')
    s += t(240, 344, '~15M speakers: Malawi, Zambia, Mozambique, Zimbabwe', 'middle', 'Ls')
    s += hr(352)
    s += sh(360, 'DISTINCTIVE NYANJA LETTERS')
    s += t(240, 371, 'nj /\u0272/ — palatal nasal (banja "family")', 'middle', 'L')
    s += t(240, 382, 'ny /\u0272/ — "nyumba" (house)', 'middle', 'L')
    s += t(240, 393, 'ng\u2019 /\u014b/ — syllabic nasal (same as Shona)', 'middle', 'L')
    s += t(240, 404, 'mw /m\u02b7/ — labialized nasal cluster', 'middle', 'L')
    s += hr(412)
    s += sh(420, 'SCRIPT COMPARISON')
    s += t(240, 431, 'Shona:  mhoro (hello)  \u2022  Nyanja:  moni (hello)', 'middle', 'L')
    s += t(240, 442, 'Shona:  nyika (country/world)  \u2022  Nyanja:  dziko (country)', 'middle', 'L')
    s += t(240, 453, 'Shona:  muti (tree)  \u2022  Nyanja:  mtengo (tree)', 'middle', 'L')
    s += t(240, 464, 'Both use Latin; different digraphs for similar Bantu phonemes', 'middle', 'Ls')
    s += footer('36', 'SHONA', 'NYANJA', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 36b  PHONOLOGY ─────────────────────────────────────────────────────
def plate36b():
    s = open_svg()
    s += t(240, 28, 'SHONA', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY & TONE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SHONA TONE SYSTEM')
    s += t(240, 68, 'Shona is a tonal language: High (H) and Low (L) tones', 'middle', 'L')
    s += t(240, 79, 'Tone distinguishes meaning: bveni "baboon" vs. bveni "watch"', 'middle', 'L')
    s += t(240, 90, 'Downstep: H tone after L is slightly lower than previous H', 'middle', 'Ls')
    s += t(240, 101, 'Tones not marked in standard orthography — context required', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'CONSONANT CLUSTERS')
    s += t(240, 128, 'Shona allows complex onsets rare in other languages:', 'middle', 'L')
    s += t(240, 139, 'sv- \u2022 zv- \u2022 bv- \u2022 mb- \u2022 nd- \u2022 ng- \u2022 nzv-', 'middle', 'L')
    s += t(240, 150, 'Syllabic nasals: m\u0329 n\u0329 function as syllable peaks', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'VOWEL SYSTEM')
    s += t(240, 177, 'Five vowels: a e i o u (pure, no diphthongs in standard)', 'middle', 'L')
    s += t(240, 188, 'Vowel length is not phonemic in standard Shona', 'middle', 'Ls')
    s += t(240, 199, 'Open syllable preference: most syllables end in vowel', 'middle', 'Ls')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'NYANJA PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'NYANJA TONE SYSTEM')
    s += t(240, 250, 'Nyanja also has lexical tone (High/Low distinction)', 'middle', 'L')
    s += t(240, 261, 'Tones grammatically significant: mark tense and focus', 'middle', 'L')
    s += t(240, 272, 'Tone affects verb tenses: H-stem vs. L-stem verbs', 'middle', 'Ls')
    s += hr(280)
    s += sh(288, 'NYANJA CONSONANTS')
    s += t(240, 299, 'Prenasalized stops: mb nd ng\u2019 mj mv nzw (Bantu feature)', 'middle', 'L')
    s += t(240, 310, 'These count as SINGLE consonants (not clusters)', 'middle', 'Ls')
    s += t(240, 321, 'No labiodental fricative clusters (unlike Shona sv/zv/bv)', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'SHARED BANTU PHONOLOGICAL FEATURES')
    s += t(240, 348, 'Both: 5 vowel system (a e i o u)', 'middle', 'L')
    s += t(240, 359, 'Both: lexical High/Low tone distinction', 'middle', 'L')
    s += t(240, 370, 'Both: open syllable preference (CV structure)', 'middle', 'L')
    s += t(240, 381, 'Both: prenasalized stops (mb nd ng)', 'middle', 'L')
    s += t(240, 392, 'Both: syllabic nasals as syllable peaks', 'middle', 'L')
    s += hr(400)
    s += sh(408, 'KEY PHONOLOGICAL DIFFERENCES')
    s += t(240, 419, 'Shona: labiodental clusters sv/zv/bv (unique in Bantu)', 'middle', 'Ls')
    s += t(240, 430, 'Nyanja: alveolar affricate /\u02a4/ (ch sound) prominent', 'middle', 'Ls')
    s += t(240, 441, 'Shona: zh /\u0292/ phoneme  \u2022  Nyanja: no /\u0292/ phoneme', 'middle', 'Ls')
    s += t(240, 452, 'Both: Proto-Bantu phonological system well-preserved', 'middle', 'Ls')
    s += footer('36', 'SHONA', 'NYANJA', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 36c  GRAMMAR ───────────────────────────────────────────────────────
def plate36c():
    s = open_svg()
    s += t(240, 28, 'SHONA', 'middle', 'T')
    s += t(240, 40, 'NOUN CLASS GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SHONA NOUN CLASSES (15)')
    s += t(240, 68, 'Bantu noun classes replace gender: prefix determines agreement', 'middle', 'L')
    s += t(240, 79, 'Class 1/2 (mu-/va-): people  \u2022  muntu/vanhu "person/people"', 'middle', 'L')
    s += t(240, 90, 'Class 3/4 (mu-/mi-): trees, nature  \u2022  muti/miti "tree/trees"', 'middle', 'L')
    s += t(240, 101, 'Class 5/6 (ri-/ma-): augmentatives  \u2022  banga/mabanga "knife/knives"', 'middle', 'L')
    s += t(240, 112, 'Class 7/8 (chi-/zvi-): things  \u2022  chibage/zvibage "mealie/mealies"', 'middle', 'L')
    s += t(240, 123, 'Class 9/10 (n-): animals  \u2022  nzou/nzou "elephant/elephants"', 'middle', 'L')
    s += hr(131)
    s += sh(139, 'AGREEMENT SYSTEM')
    s += t(240, 150, 'Every modifier agrees with noun class prefix:', 'middle', 'L')
    s += t(240, 161, 'muntu musha "good person" (class 1)', 'middle', 'L')
    s += t(240, 172, 'vanhu vakanaka "good people" (class 2)', 'middle', 'L')
    s += t(240, 183, 'Adjective, verb, pronoun all carry the class prefix', 'middle', 'Ls')
    s += hr(191)
    s += sh(199, 'VERB STRUCTURE')
    s += t(240, 210, 'Subject prefix + Tense marker + Object prefix + Root + Final', 'middle', 'L')
    s += t(240, 221, 'a-no-bata = "he/she catches" (SP + PRES + root + FV)', 'middle', 'L')
    s += t(240, 232, 'va-ka-bata = "they caught" (SP + PAST + root + FV)', 'middle', 'L')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'NYANJA GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'NYANJA NOUN CLASSES (16)')
    s += t(240, 283, 'Class 1/2 (mu-/a-): people  \u2022  munthu/anthu "person/people"', 'middle', 'L')
    s += t(240, 294, 'Class 3/4 (mu-/mi-): trees  \u2022  mtengo/mitengo "tree/trees"', 'middle', 'L')
    s += t(240, 305, 'Class 5/6 (li-/ma-): paired/mass  \u2022  bale/mabale "relative/s"', 'middle', 'L')
    s += t(240, 316, 'Class 7/8 (chi-/zi-): things  \u2022  chinthu/zinthu "thing/things"', 'middle', 'L')
    s += t(240, 327, 'Class 9/10 (n-/n-): animals  \u2022  njovu/njovu "elephant/s"', 'middle', 'L')
    s += hr(335)
    s += sh(343, 'NYANJA VERB SYSTEM')
    s += t(240, 354, 'Subject prefix + Tense + Object + Root + Final vowel', 'middle', 'L')
    s += t(240, 365, 'a-ku-samba = "he/she is washing" (SP + PROG + root + FV)', 'middle', 'L')
    s += t(240, 376, 'a-na-samba = "he/she washed" (SP + PAST + root + FV)', 'middle', 'L')
    s += hr(384)
    s += sh(392, 'PARALLEL BANTU GRAMMAR')
    s += t(240, 403, 'Both: noun class prefix system controlling all agreement', 'middle', 'L')
    s += t(240, 414, 'Both: verb template with SP-TNS-OP-ROOT-FV structure', 'middle', 'L')
    s += t(240, 425, 'Both: SOV tendency with flexible word order', 'middle', 'L')
    s += t(240, 436, 'Shona chi- class  \u2248  Nyanja chi- class (same Proto-Bantu class 7)', 'middle', 'Ls')
    s += t(240, 447, 'Chirungu/Chingerezi both mean "English language" in both languages', 'middle', 'Ls')
    s += footer('36', 'SHONA', 'NYANJA', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 36d  HISTORY ───────────────────────────────────────────────────────
def plate36d():
    s = open_svg()
    s += t(240, 28, 'SHONA', 'middle', 'T')
    s += t(240, 40, 'HISTORY & SOUTHERN AFRICA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SHONA ORIGINS')
    s += t(240, 68, 'Shona peoples: descended from Iron Age Bantu migrations (~300 CE)', 'middle', 'Ls')
    s += t(240, 79, '~1100-1450 CE: Great Zimbabwe — Shona-built stone city complex', 'middle', 'L')
    s += t(240, 90, 'Great Zimbabwe: 11m walls without mortar; largest in sub-Saharan Africa', 'middle', 'Ls')
    s += t(240, 101, '~1430-1760: Mutapa Kingdom (Monomotapa) — gold trade with coast', 'middle', 'Ls')
    s += t(240, 112, '~1690-1900: Rozvi Empire — successor Shona state', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'COLONIAL PERIOD')
    s += t(240, 139, '1890: British South Africa Company (Rhodes) colonizes Zimbabwe', 'middle', 'L')
    s += t(240, 150, '1931: Clement Doke standardizes Shona (Union Shona) from dialects', 'middle', 'Ls')
    s += t(240, 161, '1965: Rhodesia UDI; Shona speakers join liberation movement', 'middle', 'Ls')
    s += t(240, 172, '1980: Zimbabwe independence; Shona becomes official language', 'middle', 'L')
    s += t(240, 183, '~15M speakers; 70-75% of Zimbabwe\'s population speaks Shona', 'middle', 'Ls')
    s += hr(191)
    # Divider
    s += sec_divider(198, 'NYANJA HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(223, 'MARAVI KINGDOM & LAKE NYASA')
    s += t(240, 234, 'Lake Nyasa = Lake Malawi: "nyasa" = lake in Nyanja', 'middle', 'L')
    s += t(240, 245, '~1480-1700: Maravi Kingdom — Chewa/Nyanja people confederation', 'middle', 'L')
    s += t(240, 256, 'Maravi traded ivory and slaves to Swahili coast merchants', 'middle', 'Ls')
    s += t(240, 267, 'David Livingstone: called it "Lake Nyasa" (1859) from local name', 'middle', 'Ls')
    s += hr(275)
    s += sh(283, 'COLONIAL STANDARDIZATION')
    s += t(240, 294, '1875: Scottish missionaries create first Nyanja written texts', 'middle', 'L')
    s += t(240, 305, 'Nyanja Bible translation 1922 — major literary milestone', 'middle', 'Ls')
    s += t(240, 316, 'Malawi independence 1964: Chichewa (Nyanja) becomes national language', 'middle', 'L')
    s += t(240, 327, 'Zambia: Nyanja is one of 7 official regional languages', 'middle', 'Ls')
    s += hr(335)
    s += sh(343, 'NYANJA TODAY')
    s += t(240, 354, '~15M speakers across Malawi, Zambia, Mozambique, Zimbabwe', 'middle', 'L')
    s += t(240, 365, 'Malawi: Chichewa is ONE of two official languages (with English)', 'middle', 'Ls')
    s += t(240, 376, 'Lusaka (Zambia capital): Nyanja is primary street language', 'middle', 'Ls')
    s += hr(384)
    s += sh(392, 'SHARED SOUTHERN BANTU HERITAGE')
    s += t(240, 403, 'Both: descended from Bantu migrations into southern Africa', 'middle', 'Ls')
    s += t(240, 414, 'Both: Great Zimbabwe was within reach of both peoples', 'middle', 'Ls')
    s += t(240, 425, 'Both: sophisticated pre-colonial kingdoms (Mutapa, Maravi)', 'middle', 'Ls')
    s += t(240, 436, 'Shared word: "nyika" (Shona) / "dziko" (Nyanja) both mean "land"', 'middle', 'Ls')
    s += t(240, 447, 'Zimbabwe-Malawi shared border: Shona and Nyanja speakers meet', 'middle', 'Ls')
    s += footer('36', 'SHONA', 'NYANJA', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate36a_shona_nyanja_script_alt.svg', plate36a()),
                  ('plate36b_shona_nyanja_phonology_alt.svg', plate36b()),
                  ('plate36c_shona_nyanja_grammar_alt.svg', plate36c()),
                  ('plate36d_shona_nyanja_history_alt.svg', plate36d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
