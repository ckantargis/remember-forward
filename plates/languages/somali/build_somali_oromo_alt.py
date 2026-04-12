"""
Batch 9 — Somali + Oromo alt plates (Series 32, plates 32a–32d)
Secondary language: Oromo (~40M speakers, Cushitic, Ethiopia/Kenya)
Geographic link: Mogadishu (Somali) to Addis Ababa (Oromo) ~400mi
Both Cushitic languages (Afroasiatic family); share Horn of Africa geography
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

# ── PLATE 32a  SCRIPT ────────────────────────────────────────────────────────
def plate32a():
    s = open_svg()
    s += t(240, 28, 'SOMALI', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEMS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SOMALI SCRIPT HISTORY')
    s += t(240, 68, 'Somali had NO official writing system until 1972!', 'middle', 'L')
    s += t(240, 79, 'For centuries: Arabic script used for religious texts', 'middle', 'Ls')
    s += t(240, 90, '1922: Osmaniya script invented by Osman Yusuf Keenadiid', 'middle', 'L')
    s += t(240, 101, 'Osmaniya: unique script designed specifically for Somali sounds', 'middle', 'Ls')
    s += t(240, 112, '1972: Latin alphabet officially adopted by Somali government', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'MODERN SOMALI LATIN ALPHABET')
    s += t(240, 139, '26 letters; no Q, P, V, Z from English (added x, dh, kh, sh)', 'middle', 'L')
    s += t(240, 150, 'x = /\u0127/ (pharyngeal fricative — like Hebrew chet)', 'middle', 'L')
    s += t(240, 161, 'dh = /\u00f0/ (dental fricative) or retroflex /\u0256/', 'middle', 'L')
    s += t(240, 172, 'sh = /\u0283/ \u2022 kh = /x/ (velar fricative)', 'middle', 'L')
    s += t(240, 183, 'c = /\u0295/ (voiced pharyngeal fricative — Arabic ayin)', 'middle', 'L')
    s += hr(191)
    s += sh(199, 'SAMPLE TEXT')
    s += t(240, 211, 'Nabad gelyo!  "Peace upon you!" (Somali greeting)', 'middle', 'L')
    s += t(240, 222, 'Magacaygu waa...  "My name is..."', 'middle', 'L')
    s += t(240, 233, 'Af Soomaali ayaan ku hadlaa.  "I speak Somali."', 'middle', 'L')
    s += hr(241)
    # Divider
    s += sec_divider(248, 'OROMO  \u00b7  AFAAN OROMOO  \u00b7  SECONDARY LANGUAGE')
    s += sh(273, 'OROMO WRITING HISTORY')
    s += t(240, 284, 'Oromo was suppressed during Amhara-dominated Ethiopian empire', 'middle', 'Ls')
    s += t(240, 295, 'Ethiopic (Ge\'ez) script: never adopted for Oromo', 'middle', 'Ls')
    s += t(240, 306, '1970s-1991: Oromo Liberation Front develops Qubee (Latin)', 'middle', 'L')
    s += t(240, 317, '1991: Qubee Latin alphabet officially adopted after Derg falls', 'middle', 'L')
    s += hr(325)
    s += sh(333, 'QUBEE — OROMO LATIN ALPHABET')
    s += t(240, 344, '26 basic letters + diacritics for long vowels and pharyngeals', 'middle', 'L')
    s += t(240, 355, 'aa ii uu ee oo: double letters = long vowels', 'middle', 'L')
    s += t(240, 366, "ph = /\u0294/ (glottal stop)  \u2022  x = /\u0127/ (pharyngeal)", 'middle', 'L')
    s += t(240, 377, "'a = /'a/ (glottalized)  \u2022  'i 'u 'e 'o (ejective vowels)", 'middle', 'Ls')
    s += hr(385)
    s += sh(393, 'SCRIPT PARALLEL')
    s += t(240, 404, 'Both Somali and Oromo: Latin alphabets adopted after 1970', 'middle', 'L')
    s += t(240, 415, 'Both: represent Cushitic pharyngeal consonants in Latin', 'middle', 'L')
    s += t(240, 426, 'Both: long vowel distinction written with double letters', 'middle', 'L')
    s += t(240, 437, 'Both: previously used Arabic script for religious purposes', 'middle', 'Ls')
    s += t(240, 448, 'Shared challenge: writing pharyngeals /\u0127/ /\u0295/ in Latin', 'middle', 'Ls')
    s += footer('32', 'SOMALI', 'OROMO', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 32b  PHONOLOGY ─────────────────────────────────────────────────────
def plate32b():
    s = open_svg()
    s += t(240, 28, 'SOMALI', 'middle', 'T')
    s += t(240, 40, 'CUSHITIC PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SOMALI CONSONANT SYSTEM')
    s += t(240, 68, 'Pharyngeal consonants (from Proto-Semitic/Cushitic):', 'middle', 'L')
    s += t(240, 79, '/\u0127/ voiceless pharyngeal fricative (x in Somali)', 'middle', 'L')
    s += t(240, 90, '/\u0295/ voiced pharyngeal fricative (c in Somali)', 'middle', 'L')
    s += t(240, 101, 'These sounds exist in Arabic, Hebrew, Amharic — not in Indo-European', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'SOMALI EJECTIVES')
    s += t(240, 128, 'Ejective stops: consonants released with upward larynx push', 'middle', 'L')
    s += t(240, 139, "q = /q\u02bc/ uvular ejective  \u2022  dh = retroflex ejective", 'middle', 'L')
    s += t(240, 150, 'Ejectives shared with Amharic, Tigrinya, Oromo (areal feature)', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'SOMALI TONE/PITCH ACCENT')
    s += t(240, 177, 'Somali uses pitch accent (high vs. low tone on syllable)', 'middle', 'L')
    s += t(240, 188, 'Tone distinguishes gender: naag "woman" vs. naag\u00ed "the woman"', 'middle', 'L')
    s += t(240, 199, 'High tone marks definite article in some environments', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'SOMALI VOWELS')
    s += t(240, 226, 'Five short + five long vowels: a aa \u2022 i ii \u2022 u uu \u2022 e ee \u2022 o oo', 'middle', 'L')
    s += t(240, 237, 'Length distinction is phonemic: war vs. waar (different meanings)', 'middle', 'Ls')
    s += hr(245)
    # Divider
    s += sec_divider(252, 'OROMO PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(277, 'OROMO CONSONANT SYSTEM')
    s += t(240, 288, 'Pharyngeal consonants same as Somali:', 'middle', 'L')
    s += t(240, 299, '/\u0127/ (x) and /\u0295/ (voiced pharyngeal) both present', 'middle', 'L')
    s += t(240, 310, 'Ejective consonants: t\u02bc ch\u02bc k\u02bc (glottalized releases)', 'middle', 'L')
    s += t(240, 321, 'Geminate consonants: tt kk pp mm (doubled = long)', 'middle', 'L')
    s += hr(329)
    s += sh(337, 'OROMO VOWELS')
    s += t(240, 348, 'Five short + five long: a aa \u2022 i ii \u2022 u uu \u2022 e ee \u2022 o oo', 'middle', 'L')
    s += t(240, 359, 'IDENTICAL vowel system to Somali (shared Cushitic heritage)', 'middle', 'L')
    s += t(240, 370, 'Oromo has NO lexical tone (unlike Somali)', 'middle', 'L')
    s += hr(378)
    s += sh(386, 'SHARED CUSHITIC FEATURES')
    s += t(240, 397, 'Both: pharyngeal fricatives /\u0127/ and /\u0295/', 'middle', 'L')
    s += t(240, 408, 'Both: ejective consonants (glottalized stops)', 'middle', 'L')
    s += t(240, 419, 'Both: 5+5 short/long vowel system', 'middle', 'L')
    s += t(240, 430, 'Both: geminate consonant phonemic contrast', 'middle', 'L')
    s += t(240, 441, 'Somali adds: pitch accent \u2022 Oromo adds: more ejective series', 'middle', 'Ls')
    s += footer('32', 'SOMALI', 'OROMO', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 32c  GRAMMAR ───────────────────────────────────────────────────────
def plate32c():
    s = open_svg()
    s += t(240, 28, 'SOMALI', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & CUSHITIC STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SOMALI WORD ORDER: SOV')
    s += t(240, 68, 'SOV: Ninkii baaquli wuu soo qaatay.', 'middle', 'L')
    s += t(240, 79, '"The man the bucket brought." (S + O + V)', 'middle', 'Ls')
    s += t(240, 90, 'Focus system: moved element takes verb agreement', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'GENDER SYSTEM')
    s += t(240, 117, 'Two genders: masculine and feminine', 'middle', 'L')
    s += t(240, 128, 'Definite article: -ka (masc.) / -ta (fem.) / -ga / -da', 'middle', 'L')
    s += t(240, 139, 'Gender shift: some words change gender in plural', 'middle', 'Ls')
    s += t(240, 150, 'naag (woman, FEM) \u2192 naago (women, MASC!) — gender switch', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'SOMALI CASE & FOCUS')
    s += t(240, 177, 'Absolutive: unmarked citation form', 'middle', 'L')
    s += t(240, 188, 'Nominative: subject of sentence (with focus marker)', 'middle', 'L')
    s += t(240, 199, 'Genitive: possession \u2022 Oblique: indirect object/postpositions', 'middle', 'L')
    s += t(240, 210, 'Somali focus particles: waa (declarative) \u2022 baa/ayaa (focus)', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'OROMO GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'OROMO WORD ORDER: SOV')
    s += t(240, 261, 'Abbaan manaa dhufan. "Father home came."', 'middle', 'L')
    s += t(240, 272, 'Same SOV order as Somali — shared Cushitic feature', 'middle', 'L')
    s += t(240, 283, 'Postpositions: irratti "on" \u2022 keessatti "in" \u2022 irraa "from"', 'middle', 'L')
    s += hr(291)
    s += sh(299, 'OROMO GENDER & NUMBER')
    s += t(240, 310, 'Two genders: masculine (-a final) / feminine (-tuu/-too final)', 'middle', 'L')
    s += t(240, 321, 'hiriyaa "friend" (masc.) \u2022 hiriyyoo "friend" (fem.)', 'middle', 'L')
    s += t(240, 332, 'Plural: -oota / -ooli / -lee suffixes (varying by dialect)', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'OROMO VERB AGREEMENT')
    s += t(240, 359, 'Verbs agree with subject in person, number, and gender', 'middle', 'L')
    s += t(240, 370, 'Dhufan = "he came" \u2022 Dhufte = "she came" \u2022 Dhufan = "they came"', 'middle', 'L')
    s += t(240, 381, 'Converbs: subordinate verb forms for chaining clauses', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'SHARED CUSHITIC GRAMMAR')
    s += t(240, 408, 'Both: SOV word order  \u2022  postpositions  \u2022  two genders', 'middle', 'L')
    s += t(240, 419, 'Both: definite articles suffixed to nouns (not prefixed)', 'middle', 'L')
    s += t(240, 430, 'Both: complex focus/information structure systems', 'middle', 'L')
    s += t(240, 441, 'Both: verb-final position maintained across clause types', 'middle', 'Ls')
    s += t(240, 452, 'Parallel structure from Proto-Cushitic ancestor', 'middle', 'Ls')
    s += footer('32', 'SOMALI', 'OROMO', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 32d  HISTORY ───────────────────────────────────────────────────────
def plate32d():
    s = open_svg()
    s += t(240, 28, 'SOMALI', 'middle', 'T')
    s += t(240, 40, 'HISTORY & HORN OF AFRICA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SOMALI HISTORY')
    s += t(240, 68, 'Ancient Land of Punt: Egypt traded with Somalia ~2500 BCE', 'middle', 'L')
    s += t(240, 79, '7th-10th c. CE: Arab traders arrive; Islam adopted', 'middle', 'Ls')
    s += t(240, 90, 'Ajuran Sultanate (13th-17th c.): hydraulic engineering, resistance', 'middle', 'Ls')
    s += t(240, 101, 'Sultanate of the Geledi \u2022 Majeerteen Sultanate (19th c.)', 'middle', 'Ls')
    s += t(240, 112, '1960: Independence from Britain + Italy; unified Somali Republic', 'middle', 'L')
    s += t(240, 123, '1972: Latin script adopted for Somali — mass literacy campaign', 'middle', 'L')
    s += hr(131)
    s += sh(139, 'SOMALI TODAY')
    s += t(240, 150, '~20M speakers; official in Somalia and Somaliland', 'middle', 'L')
    s += t(240, 161, 'Somali diaspora: largest in UK, USA, Scandinavia, Gulf states', 'middle', 'Ls')
    s += t(240, 172, 'Ancient oral poetry tradition: gabay (long odes) — living art form', 'middle', 'Ls')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'OROMO HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'GADAA SYSTEM — OROMO DEMOCRACY')
    s += t(240, 223, 'Gadaa: indigenous Oromo democratic governance system', 'middle', 'L')
    s += t(240, 234, 'Grade-based government: men advance through 8-year grades', 'middle', 'Ls')
    s += t(240, 245, 'Irreecha: thanksgiving festival — largest Oromo annual gathering', 'middle', 'Ls')
    s += t(240, 256, 'UNESCO: Gadaa recognized as Intangible Cultural Heritage (2016)', 'middle', 'L')
    s += hr(264)
    s += sh(272, 'OROMO EXPANSION & SUPPRESSION')
    s += t(240, 283, '16th c. Oromo migration expanded across Ethiopian highlands', 'middle', 'L')
    s += t(240, 294, 'Abyssinian empire: Oromo language suppressed for centuries', 'middle', 'Ls')
    s += t(240, 305, 'Menelik II conquest: Oromo lands absorbed into Ethiopia (1880s)', 'middle', 'Ls')
    s += t(240, 316, '1974-1991: Derg regime bans Oromo language in schools', 'middle', 'Ls')
    s += t(240, 327, '1991: EPRDF victory; Oromo gains federal regional recognition', 'middle', 'L')
    s += hr(335)
    s += sh(343, 'OROMO TODAY')
    s += t(240, 354, '~40M speakers — largest ethnic group in Ethiopia', 'middle', 'L')
    s += t(240, 365, 'Oromia region: official language in largest Ethiopian state', 'middle', 'L')
    s += t(240, 376, 'Qubee Latin script: politically charged symbol of Oromo identity', 'middle', 'Ls')
    s += hr(384)
    s += sh(392, 'CUSHITIC PEOPLES OF THE HORN')
    s += t(240, 403, 'Somali and Oromo: the two largest Cushitic-speaking peoples', 'middle', 'L')
    s += t(240, 414, 'Proto-Cushitic homeland: Horn of Africa ~3000 BCE', 'middle', 'Ls')
    s += t(240, 425, 'Shared geography: both shaped by Rift Valley ecology', 'middle', 'Ls')
    s += t(240, 436, 'Both: pastoral nomadic tradition \u2022 cattle = wealth in both cultures', 'middle', 'Ls')
    s += t(240, 447, 'Both: Islam as majority religion (different arrival paths)', 'middle', 'Ls')
    s += t(240, 458, 'Two great Cushitic civilizations of the same ancient horn', 'middle', 'L')
    s += footer('32', 'SOMALI', 'OROMO', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate32a_somali_oromo_script_alt.svg', plate32a()),
                  ('plate32b_somali_oromo_phonology_alt.svg', plate32b()),
                  ('plate32c_somali_oromo_grammar_alt.svg', plate32c()),
                  ('plate32d_somali_oromo_history_alt.svg', plate32d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
