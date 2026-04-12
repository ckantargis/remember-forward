"""
Batch 11 — Turkish + Kurdish alt plates (Series 51, plates 51a–51d)
Secondary language: Kurdish (~30M speakers, Northwestern Iranian, Turkey/Iraq/Syria/Iran)
Geographic link: Ankara (Turkish center) to Diyarbakir (Kurdish heartland) ~400mi
Kurdish is the largest minority language in Turkey; ~20M Kurds live in Turkey
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

# ── PLATE 51a  SCRIPT ────────────────────────────────────────────────────────
def plate51a():
    s = open_svg()
    s += t(240, 28, 'TURKISH', 'middle', 'T')
    s += t(240, 40, 'LATIN SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'OTTOMAN TO MODERN TURKISH')
    s += t(240, 68, 'Ottoman Turkish: Persian-Arabic script for 600+ years', 'middle', 'L')
    s += t(240, 79, '1928: Atat\u00fcrk replaces Arabic script with Latin alphabet', 'middle', 'L')
    s += t(240, 90, 'Motivation: phonemic transparency + break from Ottoman past', 'middle', 'Ls')
    s += t(240, 101, 'Turkish Latin alphabet: 29 letters (6 modified from basic Latin)', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'TURKISH SPECIAL LETTERS')
    s += t(240, 128, '\u00e7 = /t\u0283/ (ch in "church")', 'middle', 'L')
    s += t(240, 139, '\u011f = "soft g" \u2014 lengthens preceding vowel or is silent', 'middle', 'L')
    s += t(240, 150, '\u0131 = /\u0268/ (close back unrounded — not in English)', 'middle', 'L')
    s += t(240, 161, '\u00f6 = /\u00f8/ (German \u00f6, French eu)', 'middle', 'L')
    s += t(240, 172, '\u015f = /\u0283/ (sh in "shoe")', 'middle', 'L')
    s += t(240, 183, '\u00fc = /y/ (German \u00fc, French u)', 'middle', 'L')
    s += hr(191)
    s += sh(199, 'SAMPLE TEXT')
    s += t(240, 211, 'Merhaba!  "Hello!"', 'middle', 'L')
    s += t(240, 222, 'T\u00fcrkiye  "Turkey" (the country)', 'middle', 'L')
    s += t(240, 233, 'G\u00fczel dil T\u00fcrk\u00e7e.  "Turkish is a beautiful language."', 'middle', 'L')
    s += hr(241)
    # Divider
    s += sec_divider(248, 'KURDISH  \u00b7  KURD\u00ce  \u00b7  SECONDARY LANGUAGE')
    s += sh(273, 'TWO SCRIPTS FOR KURDISH')
    s += t(240, 284, 'Kurmanji (Northern Kurdish): Latin-based Hawar alphabet (1932)', 'middle', 'L')
    s += t(240, 295, 'Sorani (Central Kurdish): Arabic/Perso-Arabic script', 'middle', 'L')
    s += t(240, 306, 'Two dialects \u2014 two scripts \u2014 limited mutual intelligibility', 'middle', 'Ls')
    s += hr(314)
    s += sh(322, 'HAWAR LATIN ALPHABET (KURMANJI)')
    s += t(240, 333, 'Bedirxan brothers created Hawar alphabet 1932 (in exile)', 'middle', 'L')
    s += t(240, 344, 'Special letters: \u00ea /e:/ \u2022 \u00ee /i:/ \u2022 \u00fb /u:/ (circumflexed long vowels)', 'middle', 'L')
    s += t(240, 355, 'w: retained (absent from modern Turkish Latin)', 'middle', 'L')
    s += t(240, 366, 'x = /x/ (velar fricative)  \u2022  q = /q/ (uvular stop)', 'middle', 'L')
    s += hr(374)
    s += sh(382, 'SCRIPT COMPARISON')
    s += t(240, 393, 'Turkish: 29 Latin letters  \u2022  Kurmanji: 31 Latin letters', 'middle', 'L')
    s += t(240, 404, 'Turkish: \u00e7 \u011f \u0131 \u00f6 \u015f \u00fc  \u2022  Kurmanji adds: \u00ea \u00ee \u00fb q w x', 'middle', 'L')
    s += t(240, 415, 'Sorani: Arabic-based (right-to-left) vs. Turkish Latin (left-to-right)', 'middle', 'Ls')
    s += t(240, 426, 'Both Turkish and Kurmanji: Latin scripts with phonemic spelling', 'middle', 'Ls')
    s += footer('51', 'TURKISH', 'KURDISH', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 51b  PHONOLOGY ─────────────────────────────────────────────────────
def plate51b():
    s = open_svg()
    s += t(240, 28, 'TURKISH', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY & VOWEL HARMONY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TURKISH VOWEL HARMONY')
    s += t(240, 68, 'Vowels must agree in backness and rounding within a word:', 'middle', 'L')
    s += t(240, 79, 'Back vowels: a \u0131 o u  \u2022  Front vowels: e i \u00f6 \u00fc', 'middle', 'L')
    s += t(240, 90, 'Suffix vowels change to match root vowel:', 'middle', 'L')
    s += t(240, 101, 'g\u00f6z-\u00fc (eye-his/her) \u2022 el-i (hand-his/her) \u2014 \u00fc matches \u00f6; i matches e', 'middle', 'L')
    s += t(240, 112, 'k\u00f6y-den (from village) \u2022 \u015fehir-den (from city) — den vs. den', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'TURKISH CONSONANTS')
    s += t(240, 139, 'Stops: p b  t d  k g  (+ \u00e7 and \u011f)', 'middle', 'L')
    s += t(240, 150, 'Fricatives: f v  s z  \u015f /\u0283/  h', 'middle', 'L')
    s += t(240, 161, 'Final devoicing: b\u2192p d\u2192t g\u2192k at word end', 'middle', 'L')
    s += t(240, 172, 'kitab "book" (Arabic) \u2192 Turkish: kitap (final devoicing)', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'TURKISH VOWELS (8)')
    s += t(240, 199, 'a /a/  e /e/  \u0131 /\u0268/  i /i/  o /o/  \u00f6 /\u00f8/  u /u/  \u00fc /y/', 'middle', 'L')
    s += t(240, 210, '/\u0268/ (dotless i): unique — absent from most European languages', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'KURDISH PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'KURMANJI CONSONANTS')
    s += t(240, 261, 'Additional consonants not in Turkish:', 'middle', 'L')
    s += t(240, 272, '/q/ uvular stop  \u2022  /x/ velar fricative  \u2022  /w/ bilabial approximant', 'middle', 'L')
    s += t(240, 283, '/\u0295/ voiced pharyngeal (from Iranian heritage)', 'middle', 'L')
    s += t(240, 294, 'These are Iranian-origin sounds not in Turkic', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'Kurdish VOWELS')
    s += t(240, 321, 'Kurmanji: a e \u00ea i \u00ee o u \u00fb (long vowels with circumflex)', 'middle', 'L')
    s += t(240, 332, 'NO vowel harmony (unlike Turkish) — Iranian language feature', 'middle', 'L')
    s += t(240, 343, 'Sorani: similar vowel inventory, Arabic-script based', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'PHONOLOGICAL CONTRAST')
    s += t(240, 370, 'Turkish: 8 vowels with vowel harmony system', 'middle', 'L')
    s += t(240, 381, 'Kurdish: vowels no harmony (different family entirely)', 'middle', 'L')
    s += t(240, 392, 'Both: /t\u0283/ "ch" sound  \u2022  both: final devoicing tendency', 'middle', 'L')
    s += t(240, 403, 'Kurdish: uvular /q/ and /x/ (Turkic lacks native /q/)', 'middle', 'Ls')
    s += t(240, 414, 'Contact: Turkish borrowed some Kurdish sounds; Kurdish Turkish words', 'middle', 'Ls')
    s += footer('51', 'TURKISH', 'KURDISH', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 51c  GRAMMAR ───────────────────────────────────────────────────────
def plate51c():
    s = open_svg()
    s += t(240, 28, 'TURKISH', 'middle', 'T')
    s += t(240, 40, 'AGGLUTINATIVE GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TURKISH SUFFIX STACKING')
    s += t(240, 68, 'Turkish adds suffixes in strict order to express complex meaning:', 'middle', 'L')
    s += t(240, 79, 'ev = house', 'middle', 'L')
    s += t(240, 90, 'evler = houses (plural)', 'middle', 'L')
    s += t(240, 101, 'evlerim = my houses', 'middle', 'L')
    s += t(240, 112, 'evlerimde = in my houses', 'middle', 'L')
    s += t(240, 123, 'evlerimden = from my houses', 'middle', 'L')
    s += t(240, 134, 'evlerimizi = our houses (accusative)', 'middle', 'L')
    s += hr(142)
    s += sh(150, 'TURKISH SOV WORD ORDER')
    s += t(240, 161, 'Ben kitab\u0131 okuyorum.  "I the-book am-reading."', 'middle', 'L')
    s += t(240, 172, 'Object comes before verb; verb is always final', 'middle', 'Ls')
    s += t(240, 183, 'Postpositions: ile "with" \u2022 i\u00e7in "for" \u2022 g\u00f6re "according to"', 'middle', 'L')
    s += hr(191)
    s += sh(199, 'TURKISH CASES (6)')
    s += t(240, 210, 'Nominative (subject)  \u2022  Accusative (definite object)', 'middle', 'L')
    s += t(240, 221, 'Dative (to/for)  \u2022  Locative (in/at)  \u2022  Ablative (from)  \u2022  Genitive (of)', 'middle', 'L')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'KURDISH GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'KURDISH SPLIT ERGATIVITY')
    s += t(240, 272, 'Kurdish has SPLIT ERGATIVITY (Turkish does not!)', 'middle', 'L')
    s += t(240, 283, 'Present: nominative-accusative alignment (like Turkish)', 'middle', 'L')
    s += t(240, 294, 'Past transitive: ergative alignment (agent takes oblique)', 'middle', 'L')
    s += t(240, 305, 'Min kitab xwend. "I-ERG book read." (past: min = oblique agent)', 'middle', 'L')
    s += hr(313)
    s += sh(321, 'KURDISH WORD ORDER')
    s += t(240, 332, 'SOV (same as Turkish) with postpositions', 'middle', 'L')
    s += t(240, 343, 'Kurmanji: extensive use of Ezafe construction (from Persian)', 'middle', 'L')
    s += t(240, 354, 'Ezafe -\u00ea: links noun to modifier: kitab-\u00ea bafl "good book"', 'middle', 'L')
    s += hr(362)
    s += sh(370, 'GRAMMATICAL PARALLELS')
    s += t(240, 381, 'Both: SOV word order  \u2022  postpositions  \u2022  agglutinative morphology', 'middle', 'L')
    s += t(240, 392, 'Both: no grammatical gender  \u2022  no articles (in Kurmanji)', 'middle', 'L')
    s += t(240, 403, 'Turkish: no ergativity  \u2022  Kurdish: split ergativity', 'middle', 'L')
    s += t(240, 414, 'Turkish: vowel harmony  \u2022  Kurdish: no vowel harmony', 'middle', 'Ls')
    s += t(240, 425, 'Both languages spoken in same mountain territory for millennia', 'middle', 'Ls')
    s += footer('51', 'TURKISH', 'KURDISH', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 51d  HISTORY ───────────────────────────────────────────────────────
def plate51d():
    s = open_svg()
    s += t(240, 28, 'TURKISH', 'middle', 'T')
    s += t(240, 40, 'HISTORY & ANATOLIA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TURKISH ORIGINS')
    s += t(240, 68, 'Turkic languages: origin in Central Asian steppes ~500 BCE', 'middle', 'L')
    s += t(240, 79, '1071 CE: Battle of Manzikert — Seljuk Turks enter Anatolia', 'middle', 'L')
    s += t(240, 90, '1299: Ottoman Sultanate founded by Osman I', 'middle', 'L')
    s += t(240, 101, '1453: Ottoman conquest of Constantinople (now Istanbul)', 'middle', 'L')
    s += t(240, 112, '1517: Ottoman control of Arab world; Arabic loanwords pour into Turkish', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'REPUBLIC OF TURKEY & LANGUAGE REFORM')
    s += t(240, 139, '1923: Turkish Republic founded by Mustafa Kemal Atat\u00fcrk', 'middle', 'L')
    s += t(240, 150, '1928: Latin alphabet replaces Ottoman Arabic script', 'middle', 'L')
    s += t(240, 161, '1932: Turkish Language Association purges Arabic/Persian loanwords', 'middle', 'Ls')
    s += t(240, 172, '~80M speakers; official in Turkey and Northern Cyprus', 'middle', 'L')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'KURDISH HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'KURDISH ORIGINS')
    s += t(240, 223, 'Kurdish: descended from Old Iranian (same root as Persian)', 'middle', 'L')
    s += t(240, 234, 'Medes (ancient Iran): possible ancestors of Kurdish people', 'middle', 'Ls')
    s += t(240, 245, 'Kurdistan: "Land of the Kurds" — no independent state exists', 'middle', 'L')
    s += t(240, 256, 'Kurdish territory spans Turkey, Iraq, Syria, Iran', 'middle', 'L')
    s += hr(264)
    s += sh(272, 'OTTOMAN KURDISH RELATIONS')
    s += t(240, 283, 'Kurdish emirs: semi-autonomous under Ottoman system', 'middle', 'Ls')
    s += t(240, 294, '1514: Ottomans ally with Kurds against Safavid Persia', 'middle', 'Ls')
    s += t(240, 305, '1880: Sheikh Ubeydullah revolt: first modern Kurdish nationalist uprising', 'middle', 'Ls')
    s += t(240, 316, '1920: Treaty of S\u00e8vres promised Kurdish autonomy (never implemented)', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'KURDISH IN TURKEY')
    s += t(240, 343, '~20M Kurds in Turkey: largest ethnic minority (~25% of population)', 'middle', 'L')
    s += t(240, 354, '1924-1991: Kurdish language banned in Turkey', 'middle', 'L')
    s += t(240, 365, '1984: PKK insurgency begins; language debate intensifies', 'middle', 'Ls')
    s += t(240, 376, '1991: Kurdish language restrictions eased; 2003: private Kurdish TV allowed', 'middle', 'Ls')
    s += hr(384)
    s += sh(392, 'TWO LANGUAGES, ONE MOUNTAIN')
    s += t(240, 403, 'Both peoples: built by the same Anatolian/Mesopotamian landscape', 'middle', 'Ls')
    s += t(240, 414, 'Turkish: Altaic steppe language transplanted to ancient crossroads', 'middle', 'Ls')
    s += t(240, 425, 'Kurdish: Iranian mountain language of the ancient Near East', 'middle', 'Ls')
    s += t(240, 436, 'Anatolia has been home to both for nearly a thousand years', 'middle', 'L')
    s += footer('51', 'TURKISH', 'KURDISH', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate51a_turkish_kurdish_script_alt.svg', plate51a()),
                  ('plate51b_turkish_kurdish_phonology_alt.svg', plate51b()),
                  ('plate51c_turkish_kurdish_grammar_alt.svg', plate51c()),
                  ('plate51d_turkish_kurdish_history_alt.svg', plate51d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
