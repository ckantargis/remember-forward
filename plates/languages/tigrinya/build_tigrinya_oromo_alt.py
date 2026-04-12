"""
Batch 11 — Tigrinya + Oromo alt plates (Series 34, plates 34a–34d)
Secondary language: Oromo (~40M speakers, Cushitic, Ethiopia/Kenya)
Geographic link: Asmara (Tigrinya center) to Addis Ababa (Oromo) ~200mi
Tigrinya (Semitic) and Oromo (Cushitic) meet in the Horn of Africa; both in Ethiopia/Eritrea
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

# ── PLATE 34a  SCRIPT ────────────────────────────────────────────────────────
def plate34a():
    s = open_svg()
    s += t(240, 28, 'TIGRINYA', 'middle', 'T')
    s += t(240, 40, 'GE\'EZ / ETHIOPIC SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, "GE'EZ SCRIPT — WORLD'S OLDEST ALPHABETS")
    s += t(240, 68, "Ge'ez (Ethiopic) script: derived from ancient South Arabian", 'middle', 'L')
    s += t(240, 79, '~4th c. CE: adopted for ancient Ethiopian language Ge\'ez', 'middle', 'Ls')
    s += t(240, 90, 'Left-to-right abugida: each symbol = consonant + vowel combination', 'middle', 'L')
    s += t(240, 101, '7 vowel orders per consonant = 7 forms of each letter', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'TIGRINYA IN GE\'EZ SCRIPT')
    s += t(240, 128, 'First order (inherent /\u0259/): \u1200 \u1208 \u1218 \u1228 \u1230 \u1240 \u1260 \u1270 \u1278 \u1290', 'middle', 'L')
    s += t(240, 139, 'Second order (/u/): \u1201 \u1209 \u1219 \u1229 \u1231 \u1241 \u1261 \u1271 \u1279 \u1291', 'middle', 'L')
    s += t(240, 150, 'Third order (/i/): \u1202 \u120a \u121a \u122a \u1232 \u1242 \u1262 \u1272 \u127a \u1292', 'middle', 'L')
    s += t(240, 161, '245 total syllabic characters in standard Tigrinya set', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'SPECIAL TIGRINYA LETTERS')
    s += t(240, 188, 'Pharyngeal consonants: \u12d0 /\u0295a/ \u12d1 /\u0295u/ ... (voiced pharyngeal)', 'middle', 'L')
    s += t(240, 199, 'Ejective consonants: \u1338 /p\u02bc/ \u1338 \u1338 (unique to Ethiopic languages)', 'middle', 'L')
    s += t(240, 210, 'No punctuation system in classical Ge\'ez (four dots = full stop)', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'OROMO  \u00b7  AFAAN OROMOO  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, "QUBEE — OROMO'S LATIN ALPHABET")
    s += t(240, 261, "Oromo uses Latin script (Qubee) adopted 1991 after Derg falls", 'middle', 'L')
    s += t(240, 272, 'Political script choice: rejected Ethiopic/Ge\'ez as Amhara symbol', 'middle', 'L')
    s += t(240, 283, 'Long vowels: doubled letters aa ii uu ee oo', 'middle', 'L')
    s += t(240, 294, "Pharyngeals in Qubee: x = /\u0127/  '(apostrophe) for glottals", 'middle', 'L')
    s += hr(302)
    s += sh(310, 'SCRIPT CONTRAST: MAXIMUM DIVERGENCE')
    s += t(240, 321, "Tigrinya: Ge'ez syllabary (245 characters)", 'middle', 'L')
    s += t(240, 332, 'Oromo: Latin alphabet (26 + doubled vowels)', 'middle', 'L')
    s += t(240, 343, 'Both in Ethiopia: Oromo rejected Ge\'ez as political statement', 'middle', 'Ls')
    s += t(240, 354, "Eritrea: Ge'ez used for Tigrinya \u2022 Ethiopia: Latin for Oromo", 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'SHARED HORN OF AFRICA CONTEXT')
    s += t(240, 381, 'Tigrinya speakers: Eritrea + Tigray (northern Ethiopia)', 'middle', 'Ls')
    s += t(240, 392, 'Oromo speakers: central/southern Ethiopia + northern Kenya', 'middle', 'Ls')
    s += t(240, 403, 'Addis Ababa sits in Oromo territory; Tigrinya ~200mi north', 'middle', 'Ls')
    s += t(240, 414, 'Two writing systems; one Horn of Africa history', 'middle', 'L')
    s += footer('34', 'TIGRINYA', 'OROMO', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 34b  PHONOLOGY ─────────────────────────────────────────────────────
def plate34b():
    s = open_svg()
    s += t(240, 28, 'TIGRINYA', 'middle', 'T')
    s += t(240, 40, 'SEMITIC PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TIGRINYA PHARYNGEAL CONSONANTS')
    s += t(240, 68, '/\u0127/ voiceless pharyngeal fricative (\u1210 in Ge\'ez)', 'middle', 'L')
    s += t(240, 79, '/\u0295/ voiced pharyngeal fricative (\u12d0 in Ge\'ez)', 'middle', 'L')
    s += t(240, 90, 'Both from ancient Semitic root (shared with Arabic, Hebrew)', 'middle', 'Ls')
    s += t(240, 101, 'Pharyngeals produced deep in throat — difficult for non-Semitic speakers', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'EJECTIVE CONSONANTS')
    s += t(240, 128, 'Six ejective stops: p\u02bc t\u02bc k\u02bc s\u02bc ts\u02bc t\u0283\u02bc', 'middle', 'L')
    s += t(240, 139, 'Ejectives: simultaneous glottal + oral closure, then explosive release', 'middle', 'L')
    s += t(240, 150, 'Feature shared with Oromo, Amharic, Somali — areal Horn of Africa', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'TIGRINYA VOWELS')
    s += t(240, 177, 'Seven vowels: \u0259 u i a e o \u026a (the seven Ge\'ez vowel orders)', 'middle', 'L')
    s += t(240, 188, 'Geminate consonants phonemic: sala "peace" \u2022 salla "he prayed"', 'middle', 'L')
    s += t(240, 199, 'No tones; stress generally penultimate', 'middle', 'Ls')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'OROMO PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'OROMO CUSHITIC PHONOLOGY')
    s += t(240, 250, 'Pharyngeal consonants also present in Oromo:', 'middle', 'L')
    s += t(240, 261, '/\u0127/ (x in Qubee) and voiced pharyngeal \u2014 same as Tigrinya!', 'middle', 'L')
    s += t(240, 272, 'Ejective consonants: k\u02bc t\u02bc ch\u02bc (shared Horn of Africa feature)', 'middle', 'L')
    s += hr(280)
    s += sh(288, 'SHARED AREAL FEATURES')
    s += t(240, 299, 'Both: pharyngeal fricatives /\u0127/ /\u0295/ (uncommon globally)', 'middle', 'L')
    s += t(240, 310, 'Both: ejective consonants (glottalized stops)', 'middle', 'L')
    s += t(240, 321, 'Both: 5+ vowel system with long/short distinction', 'middle', 'L')
    s += t(240, 332, 'Both: geminate consonants phonemically significant', 'middle', 'L')
    s += t(240, 343, 'Different families: Tigrinya (Semitic) vs. Oromo (Cushitic)', 'middle', 'Ls')
    s += t(240, 354, 'Same phonological features: convergence across millennia of contact', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'PHONOLOGICAL DIVERGENCE')
    s += t(240, 381, 'Tigrinya: no tones  \u2022  Oromo: no tones (both unlike SE Asian Cushitic)', 'middle', 'Ls')
    s += t(240, 392, 'Tigrinya: Semitic root system (trilateral roots)', 'middle', 'Ls')
    s += t(240, 403, 'Oromo: Cushitic longer roots (typically 2-3 consonants, not trilateral)', 'middle', 'Ls')
    s += t(240, 414, 'Ethiopian highlands: shared phonological space across language families', 'middle', 'Ls')
    s += footer('34', 'TIGRINYA', 'OROMO', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 34c  GRAMMAR ───────────────────────────────────────────────────────
def plate34c():
    s = open_svg()
    s += t(240, 28, 'TIGRINYA', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TIGRINYA WORD ORDER: SOV')
    s += t(240, 68, 'Verb-final: Subject + Object + Verb', 'middle', 'L')
    s += t(240, 79, 'Tigrinya shares SOV order with Amharic (unusual for Semitic)', 'middle', 'L')
    s += t(240, 90, 'Arabic and Hebrew are VSO; Tigrinya SOV from contact with Cushitic', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'SEMITIC ROOT SYSTEM')
    s += t(240, 117, 'Trilateral roots: three consonants carry basic meaning', 'middle', 'L')
    s += t(240, 128, 'sb\u02bc = root for "Saturday" / "Sabbath" concept', 'middle', 'Ls')
    s += t(240, 139, 'Vowel patterns inserted into roots to derive forms:', 'middle', 'Ls')
    s += t(240, 150, 'ktb = write-root: kataba "he wrote" \u2022 kaatib "writer"', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'GENDER IN TIGRINYA')
    s += t(240, 177, 'Two genders: masculine and feminine', 'middle', 'L')
    s += t(240, 188, 'Feminine marked with -ti suffix: neger "thing" (M) \u2022 negerti (F)', 'middle', 'L')
    s += t(240, 199, 'Verbs agree in gender: masculine vs. feminine 3rd person forms', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'TIGRINYA DEFINITENESS')
    s += t(240, 226, 'Definite article: -ti (F) / -u (M) suffixed to noun', 'middle', 'L')
    s += t(240, 237, 'Indefinite: no article (like Semitic languages generally)', 'middle', 'Ls')
    s += hr(245)
    # Divider
    s += sec_divider(252, 'OROMO GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(277, 'OROMO WORD ORDER: SOV')
    s += t(240, 288, 'Oromo is also SOV (same as Tigrinya!)', 'middle', 'L')
    s += t(240, 299, 'Abbaan mana dhufan. "Father house came." = "Father came home."', 'middle', 'L')
    s += t(240, 310, 'Postpositions: irratti "on" \u2022 keessa "in" \u2022 irraa "from"', 'middle', 'L')
    s += hr(318)
    s += sh(326, 'OROMO GENDER')
    s += t(240, 337, 'Two genders: masculine and feminine (same as Tigrinya)', 'middle', 'L')
    s += t(240, 348, 'Masculine: -a final  \u2022  Feminine: -tuu / -oo final', 'middle', 'L')
    s += t(240, 359, 'Oromo gender not based on Semitic root (different system, same concept)', 'middle', 'Ls')
    s += hr(367)
    s += sh(375, 'OROMO DEFINITENESS')
    s += t(240, 386, 'Definite: suffixed -icha (M) / -ittii (F): mana "house" \u2192 manicha "the house"', 'middle', 'Ls')
    s += t(240, 397, 'Parallel to Tigrinya: both suffix definiteness (not prefix)', 'middle', 'Ls')
    s += hr(405)
    s += sh(413, 'ETHIOPIAN LINGUISTIC AREA')
    s += t(240, 424, 'SOV word order shared by Tigrinya + Oromo + Amharic + Somali', 'middle', 'L')
    s += t(240, 435, 'Unusual for Semitic (Tigrinya); typical for Cushitic (Oromo)', 'middle', 'Ls')
    s += t(240, 446, 'Suffixed definiteness: shared across Ethiopian language families', 'middle', 'Ls')
    s += t(240, 457, 'Ethiopian Linguistic Area: convergence across Semitic+Cushitic boundary', 'middle', 'Ls')
    s += footer('34', 'TIGRINYA', 'OROMO', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 34d  HISTORY ───────────────────────────────────────────────────────
def plate34d():
    s = open_svg()
    s += t(240, 28, 'TIGRINYA', 'middle', 'T')
    s += t(240, 40, 'HISTORY & HORN OF AFRICA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TIGRINYA ORIGINS')
    s += t(240, 68, 'Tigrinya descended from Ge\'ez (ancient Aksumite language)', 'middle', 'L')
    s += t(240, 79, 'Aksum Empire (~100-940 CE): one of ancient world\'s great powers', 'middle', 'L')
    s += t(240, 90, 'Aksum: first empire to mint gold coins in sub-Saharan Africa', 'middle', 'Ls')
    s += t(240, 101, '~4th c. CE: Emperor Ezana converts to Christianity (first African empire)', 'middle', 'Ls')
    s += t(240, 112, 'Ge\'ez: liturgical language of Ethiopian Orthodox Church; still used today', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'TIGRINYA TODAY')
    s += t(240, 139, '~8M speakers; official language of Eritrea (with Arabic)', 'middle', 'L')
    s += t(240, 150, 'Also spoken in Ethiopia\'s Tigray region (~4M more speakers)', 'middle', 'L')
    s += t(240, 161, '2020-2022: Tigray War; devastating conflict in Tigrinya-speaking region', 'middle', 'Ls')
    s += hr(169)
    # Divider
    s += sec_divider(176, 'OROMO HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(201, 'OROMO ORIGINS')
    s += t(240, 212, 'Oromo: indigenous to Ethiopian highlands and Great Rift Valley', 'middle', 'L')
    s += t(240, 223, 'Gadaa democratic system: age-grade governance predates modern democracy', 'middle', 'L')
    s += t(240, 234, '16th c.: Oromo migration expanded across Ethiopian highlands', 'middle', 'Ls')
    s += t(240, 245, 'Menelik II (1889-1913): conquered Oromo lands for Amhara empire', 'middle', 'Ls')
    s += hr(253)
    s += sh(261, 'OROMO SUPPRESSION & RESISTANCE')
    s += t(240, 272, 'Amhara-dominated Ethiopia: Oromo culture and language marginalized', 'middle', 'L')
    s += t(240, 283, 'Oromo Liberation Front (OLF): founded 1973; decades of resistance', 'middle', 'L')
    s += t(240, 294, '1991: Oromo gains recognition after Derg regime falls', 'middle', 'L')
    s += t(240, 305, 'Qubee Latin script: adopted as symbol of Oromo identity, not Amhara', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'OROMO TODAY')
    s += t(240, 332, '~40M speakers; largest ethnic group in Ethiopia', 'middle', 'L')
    s += t(240, 343, 'Oromia: largest regional state; surrounds Addis Ababa', 'middle', 'L')
    s += t(240, 354, 'Abiy Ahmed: Oromo-descended prime minister; Nobel Peace Prize 2019', 'middle', 'L')
    s += hr(362)
    s += sh(370, 'SEMITIC + CUSHITIC: ONE HIGHLAND')
    s += t(240, 381, 'Tigrinya (Semitic) and Oromo (Cushitic): neighboring peoples of Ethiopia', 'middle', 'Ls')
    s += t(240, 392, 'Both in Ethiopian highlands: shared geography, shared ecological pressures', 'middle', 'Ls')
    s += t(240, 403, 'Ethiopian Linguistic Area: languages converged across family lines', 'middle', 'Ls')
    s += t(240, 414, 'Both: Christian / Muslim communities within each language group', 'middle', 'Ls')
    s += t(240, 425, 'Addis Ababa: built between Tigrinya north and Oromo south', 'middle', 'L')
    s += footer('34', 'TIGRINYA', 'OROMO', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate34a_tigrinya_oromo_script_alt.svg', plate34a()),
                  ('plate34b_tigrinya_oromo_phonology_alt.svg', plate34b()),
                  ('plate34c_tigrinya_oromo_grammar_alt.svg', plate34c()),
                  ('plate34d_tigrinya_oromo_history_alt.svg', plate34d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
