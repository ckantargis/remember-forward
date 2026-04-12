"""
Batch 10 — Thai + Karen alt plates (Series 39, plates 39a–39d)
Secondary language: Karen (~5-7M speakers, Sino-Tibetan/Karenic, Myanmar/Thailand)
Geographic link: Bangkok (Thai) to Karen state border ~300-400mi; Karen live in western Thailand
Both mainland SE Asian languages; Karen is the largest indigenous minority in Thailand
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

# ── PLATE 39a  SCRIPT ────────────────────────────────────────────────────────
def plate39a():
    s = open_svg()
    s += t(240, 28, 'THAI', 'middle', 'T')
    s += t(240, 40, 'THAI SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'THAI ALPHABET — AN ABUGIDA')
    s += t(240, 68, 'Created 1283 CE by King Ramkhamhaeng; derived from Khmer', 'middle', 'L')
    s += t(240, 79, 'Khmer script derived from ancient Pallava (South Indian)', 'middle', 'Ls')
    s += t(240, 90, '44 consonants \u2022 15 vowel forms \u2022 4 tone marks \u2022 numerals', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'THREE CONSONANT CLASSES')
    s += t(240, 117, 'Mid class (\u0e01 \u0e08 \u0e10 \u0e15 \u0e1b \u0e2d): default tone rules', 'middle', 'L')
    s += t(240, 128, 'High class (\u0e09 \u0e16 \u0e1c \u0e1d \u0e2b): shift tones up', 'middle', 'L')
    s += t(240, 139, 'Low class (\u0e07 \u0e0a \u0e0b \u0e0d \u0e0e \u0e0f \u0e10 ...): shift tones down', 'middle', 'L')
    s += t(240, 150, 'Class + tone mark + vowel type together determine the tone', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'VOWELS')
    s += t(240, 177, 'Short: \u0e30 \u0e34 \u0e38 \u0e40\u0e30 \u0e41\u0e30 \u0e42\u0e30 \u0e43 \u0e44', 'middle', 'L')
    s += t(240, 188, 'Long: \u0e32 \u0e35 \u0e39 \u0e40 \u0e41 \u0e42 \u0e40\u0e2d \u0e40\u0e32 \u0e40\u0e37\u0e2d \u0e2d \u0e27', 'middle', 'L')
    s += t(240, 199, 'Vowels appear above, below, before or after consonants', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'SAMPLE TEXT')
    s += t(240, 227, '\u0e2a\u0e27\u0e31\u0e2a\u0e14\u0e35  Sawatdee "Hello/Goodbye"', 'middle', 'L')
    s += t(240, 238, '\u0e44\u0e17\u0e22  Thai = "Thai language/Thai people"', 'middle', 'L')
    s += hr(246)
    # Divider
    s += sec_divider(253, 'KAREN  \u00b7  PKO / S\u2019GAW  \u00b7  SECONDARY LANGUAGE')
    s += sh(278, 'KAREN WRITING SYSTEMS')
    s += t(240, 289, 'S\'gaw Karen: largest Karen variety (~3M speakers)', 'middle', 'L')
    s += t(240, 300, 'Pwo Karen: second variety (~1M speakers)', 'middle', 'L')
    s += t(240, 311, '1832: American Baptist missionaries create S\'gaw Karen script', 'middle', 'L')
    s += t(240, 322, 'S\'gaw script: derived from Burmese Mon script (rounded letters)', 'middle', 'L')
    s += t(240, 333, 'Abugida: consonant + inherent vowel, modified by diacritics', 'middle', 'Ls')
    s += hr(341)
    s += sh(349, 'S\'GAW KAREN SAMPLE')
    s += t(240, 361, '\u1000\u1019\u102c (Karen word in Burmese-derived script)', 'middle', 'L')
    s += t(240, 372, 'Karen written script resembles Burmese (circular forms)', 'middle', 'Ls')
    s += hr(380)
    s += sh(388, 'SCRIPT COMPARISON')
    s += t(240, 399, 'Thai: derived from Khmer/Pallava (angular forms)', 'middle', 'L')
    s += t(240, 410, 'Karen: derived from Mon/Burmese (rounded circular forms)', 'middle', 'L')
    s += t(240, 421, 'Both: abugida structure  \u2022  both: tone marking system', 'middle', 'L')
    s += t(240, 432, 'Both scripts used in Thailand; Karen schools use Karen script', 'middle', 'Ls')
    s += footer('39', 'THAI', 'KAREN', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 39b  PHONOLOGY ─────────────────────────────────────────────────────
def plate39b():
    s = open_svg()
    s += t(240, 28, 'THAI', 'middle', 'T')
    s += t(240, 40, 'TONAL PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'FIVE TONES OF THAI')
    s += t(240, 68, 'Mid (level): m\u0101a "come" (no mark)', 'middle', 'L')
    s += t(240, 79, 'Low (falling): m\u00e0a "horse" (\u0e48 mark)', 'middle', 'L')
    s += t(240, 90, 'Falling: m\u00e2a "dog" (\u0e49 mark)', 'middle', 'L')
    s += t(240, 101, 'High (rising): m\u00e1a "value" (high class consonant)', 'middle', 'L')
    s += t(240, 112, 'Rising: m\u01cda "not" (\u0e4b mark)', 'middle', 'L')
    s += t(240, 123, 'Same syllable: 5 different meanings based on tone alone', 'middle', 'Ls')
    s += hr(131)
    s += sh(139, 'CONSONANT SYSTEM')
    s += t(240, 150, 'Stops: p ph b \u2022 t th d \u2022 k kh \u2022 glottal \u0294', 'middle', 'L')
    s += t(240, 161, 'Three-way contrast: plain / aspirated / voiced (for some)', 'middle', 'L')
    s += t(240, 172, 'Final position: only unreleased stops + nasals + /w j/', 'middle', 'L')
    s += t(240, 183, 'No final fricatives or affricates (unlike English)', 'middle', 'Ls')
    s += hr(191)
    s += sh(199, 'VOWEL SYSTEM')
    s += t(240, 210, '9 short + 9 long + diphthongs: 21 total vowel contrasts', 'middle', 'L')
    s += t(240, 221, 'Central vowel /\u0268/ (no English equivalent)', 'middle', 'L')
    s += t(240, 232, 'Vowel length is phonemic: /m\u0101a/ vs /ma/ different words', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'KAREN PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'S\'GAW KAREN TONES')
    s += t(240, 283, 'S\'gaw Karen: 6 tones (more than Thai!)', 'middle', 'L')
    s += t(240, 294, 'Tones interact with consonant class and vowel length', 'middle', 'L')
    s += t(240, 305, 'Karen tonal system similar to neighboring Tibeto-Burman languages', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'KAREN CONSONANT SYSTEM')
    s += t(240, 332, 'Aspirated / unaspirated stop distinction (like Thai)', 'middle', 'L')
    s += t(240, 343, 'p ph \u2022 t th \u2022 k kh (parallel to Thai)', 'middle', 'L')
    s += t(240, 354, 'Uvular stop /q/ present in some Karen dialects', 'middle', 'Ls')
    s += t(240, 365, 'Rhotic /r/ absent (like Thai, unlike English)', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'SHARED SE ASIAN PHONOLOGICAL FEATURES')
    s += t(240, 392, 'Both: tonal languages (Thai 5 tones, Karen 6 tones)', 'middle', 'L')
    s += t(240, 403, 'Both: aspirated vs. unaspirated stop contrast', 'middle', 'L')
    s += t(240, 414, 'Both: no consonant clusters at syllable onset', 'middle', 'L')
    s += t(240, 425, 'Both: monosyllabic roots (Mainland SE Asia areal feature)', 'middle', 'L')
    s += t(240, 436, 'Both: vowel length phonemically contrastive', 'middle', 'Ls')
    s += footer('39', 'THAI', 'KAREN', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 39c  GRAMMAR ───────────────────────────────────────────────────────
def plate39c():
    s = open_svg()
    s += t(240, 28, 'THAI', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'THAI WORD ORDER: SVO')
    s += t(240, 68, 'Subject  Verb  Object (like English, unlike most Asian languages)', 'middle', 'L')
    s += t(240, 79, 'Chan gin khao.  "I eat rice." (I eat rice)', 'middle', 'L')
    s += t(240, 90, 'Modifiers follow head: khao dam "rice black" = "black rice"', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'ISOLATING MORPHOLOGY')
    s += t(240, 117, 'No inflection: no case, gender, number, tense marking on nouns/verbs', 'middle', 'L')
    s += t(240, 128, 'Tense: indicated by time words and aspect markers', 'middle', 'L')
    s += t(240, 139, 'cha (future) \u2022 kamlang (progressive) \u2022 laeo (perfect)', 'middle', 'L')
    s += t(240, 150, 'chan gin khao laeo  "I have eaten rice" (laeo = already)', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'CLASSIFIERS')
    s += t(240, 177, 'Classifiers: nouns need a classifier when counted', 'middle', 'L')
    s += t(240, 188, 'maew s\u0101am tua "cat three CL:animal" = "three cats"', 'middle', 'L')
    s += t(240, 199, 'nangsu\u0113 s\u0101am lem "book three CL:bound" = "three books"', 'middle', 'L')
    s += t(240, 210, 'Different classifier for every semantic category', 'middle', 'Ls')
    s += hr(218)
    s += sh(226, 'POLITENESS PARTICLES')
    s += t(240, 237, 'Kha (FEM speaker) / Khrap (MASC speaker): sentence-final respect', 'middle', 'L')
    s += t(240, 248, 'Sawatdii khrap  (male: "hello")  \u2022  Sawatdii kha  (female: "hello")', 'middle', 'L')
    s += hr(256)
    # Divider
    s += sec_divider(263, 'KAREN GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(288, 'KAREN WORD ORDER: SOV')
    s += t(240, 299, 'Karen is SOV (Subject Object Verb) — opposite of Thai!', 'middle', 'L')
    s += t(240, 310, 'Postpositions (not prepositions): locative suffix after noun', 'middle', 'L')
    s += t(240, 321, 'Object before verb: more typical Tibeto-Burman pattern', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'KAREN MORPHOLOGY')
    s += t(240, 348, 'Karen: also mostly isolating (like Thai)', 'middle', 'L')
    s += t(240, 359, 'Reduplication: common grammatical and semantic device', 'middle', 'L')
    s += t(240, 370, 'Verbs: can be serialized (verb-verb compounds)', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'KAREN CLASSIFIERS')
    s += t(240, 397, 'Karen also uses classifiers when counting nouns!', 'middle', 'L')
    s += t(240, 408, 'Similar classifier categories to Thai (animate, flat, round...)', 'middle', 'Ls')
    s += t(240, 419, 'This areal feature shared across mainland SE Asia', 'middle', 'Ls')
    s += hr(427)
    s += sh(435, 'GRAMMATICAL COMPARISON')
    s += t(240, 446, 'Thai: SVO  \u2022  Karen: SOV  (different word orders!)', 'middle', 'L')
    s += t(240, 457, 'Both: isolating  \u2022  both: classifiers  \u2022  both: tonal', 'middle', 'L')
    s += t(240, 468, 'Thai: premodifiers  \u2022  Karen: postpositions', 'middle', 'Ls')
    s += footer('39', 'THAI', 'KAREN', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 39d  HISTORY ───────────────────────────────────────────────────────
def plate39d():
    s = open_svg()
    s += t(240, 28, 'THAI', 'middle', 'T')
    s += t(240, 40, 'HISTORY & MAINLAND SE ASIA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'THAI ORIGINS')
    s += t(240, 68, 'Proto-Tai: originated in southern China/northern Vietnam', 'middle', 'L')
    s += t(240, 79, 'Southward migration into SE Asia ~1000 CE', 'middle', 'Ls')
    s += t(240, 90, '1238: Sukhothai Kingdom — first Thai state; Ramkhamhaeng creates alphabet', 'middle', 'L')
    s += t(240, 101, '1350: Ayutthaya Kingdom; major power of mainland SE Asia', 'middle', 'L')
    s += t(240, 112, '1782: Chakri dynasty; Bangkok founded as new capital', 'middle', 'Ls')
    s += t(240, 123, 'Thailand never colonized: buffer state between British and French', 'middle', 'L')
    s += hr(131)
    s += sh(139, 'THAI TODAY')
    s += t(240, 150, '~60M speakers; sole official language of Thailand', 'middle', 'L')
    s += t(240, 161, 'Buddhism deeply embedded in language: many Buddhist vocabulary', 'middle', 'Ls')
    s += t(240, 172, 'Royal vocabulary: separate formal terms for royalty vs. commoners', 'middle', 'Ls')
    s += t(240, 183, 'Wai: gesture of respect; language of respect encoded in pronouns', 'middle', 'Ls')
    s += hr(191)
    # Divider
    s += sec_divider(198, 'KAREN HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(223, 'KAREN ORIGINS')
    s += t(240, 234, 'Karen people: migrated from Tibet-China plateau ~2000 years ago', 'middle', 'L')
    s += t(240, 245, 'Settled in Irrawaddy delta and Tenasserim hills (Myanmar/Thailand)', 'middle', 'Ls')
    s += t(240, 256, 'Multiple Karen groups: S\'gaw \u2022 Pwo \u2022 Pa\'O \u2022 Kayah \u2022 Kayan', 'middle', 'L')
    s += t(240, 267, 'Karen do not form a single political or linguistic entity', 'middle', 'Ls')
    s += hr(275)
    s += sh(283, 'KAREN UNDER BURMESE RULE')
    s += t(240, 294, '1824-1885: British colonize Burma; Karen ally with British', 'middle', 'L')
    s += t(240, 305, '1947: Burma independence; Karen excluded from Panglong Agreement', 'middle', 'L')
    s += t(240, 316, '1949: Karen National Union begins armed struggle — world\'s longest civil war', 'middle', 'L')
    s += t(240, 327, 'Karen conflict continues: displacement into Thailand ongoing', 'middle', 'Ls')
    s += hr(335)
    s += sh(343, 'KAREN IN THAILAND')
    s += t(240, 354, '~500,000 Karen in Thailand; largest ethnic minority', 'middle', 'L')
    s += t(240, 365, 'Refugees from Myanmar war: 90,000+ in Thai border camps', 'middle', 'L')
    s += t(240, 376, 'Karen hill tribe (Doi Inthanon area): famous for traditional weaving', 'middle', 'Ls')
    s += t(240, 387, 'Long-neck Karen (Kayan Lahwi): cultural tourism controversy', 'middle', 'Ls')
    s += hr(395)
    s += sh(403, 'SHARED MAINLAND SE ASIA')
    s += t(240, 414, 'Both peoples: shaped by rice agriculture, rivers, forest', 'middle', 'Ls')
    s += t(240, 425, 'Karen: minority in Thailand; Thai is their administrative language', 'middle', 'Ls')
    s += t(240, 436, 'Buddhist monks in both communities: shared spiritual tradition', 'middle', 'Ls')
    s += t(240, 447, 'Karen teach Thai children traditional forest knowledge; vital exchange', 'middle', 'Ls')
    s += footer('39', 'THAI', 'KAREN', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate39a_thai_karen_script_alt.svg', plate39a()),
                  ('plate39b_thai_karen_phonology_alt.svg', plate39b()),
                  ('plate39c_thai_karen_grammar_alt.svg', plate39c()),
                  ('plate39d_thai_karen_history_alt.svg', plate39d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
