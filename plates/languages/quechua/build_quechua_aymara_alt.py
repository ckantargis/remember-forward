"""
Batch 8 — Quechua + Aymara alt plates (Series 46, plates 46a–46d)
Secondary language: Aymara (~2M speakers, Aymaran family, Bolivia/Peru/Chile)
Geographic link: Cusco (Quechua center) to Lake Titicaca (Aymara heartland) ~200mi
Both Andean languages sharing the Inca highland cultural complex
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

# ── PLATE 46a  SCRIPT ────────────────────────────────────────────────────────
def plate46a():
    s = open_svg()
    s += t(240, 28, 'QUECHUA', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEMS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'PRE-CONTACT: THE QUIPU')
    s += t(240, 68, 'No alphabetic writing before Spanish contact', 'middle', 'L')
    s += t(240, 78, 'Quipu (khipu): knotted string recording system', 'middle', 'L')
    s += t(240, 89, 'Knots encoded numbers, records, narratives', 'middle', 'Ls')
    s += t(240, 99, 'Positional decimal system: knot position = place value', 'middle', 'Ls')
    s += t(240, 110, 'Khipu kamayuq: specialized knot-reader officials', 'middle', 'Ls')
    s += hr(118)
    s += sh(126, 'COLONIAL LATIN ALPHABET')
    s += t(240, 137, 'Spanish missionaries transcribed Quechua in 1560 CE', 'middle', 'L')
    s += t(240, 148, 'Fray Domingo de Santo Thomas: first Quechua grammar (1560)', 'middle', 'Ls')
    s += t(240, 159, 'Modern alphabet: 3 vowels a i u (no e, o in Classical)', 'middle', 'L')
    s += t(240, 170, 'Consonants with three-way stop contrast:', 'middle', 'H')
    s += t(240, 181, 'plain  \u2022  aspirate  \u2022  ejective (unique feature)', 'middle', 'L')
    s += t(240, 192, 'p  ph  p\'  /  t  th  t\'  /  k  kh  k\'  /  q  qh  q\'', 'middle', 'L')
    s += t(240, 203, 'Uvular /q/ absent from most other Amerindian families', 'middle', 'Ls')
    s += hr(211)
    s += sh(219, 'QUECHUA SAMPLE TEXT')
    s += t(240, 231, 'Ima sutiki?  "What is your name?"', 'middle', 'L')
    s += t(240, 242, 'Nuqa-m kay llaqta-manta-m.  "I am from this town."', 'middle', 'L')
    s += t(240, 253, 'Pachamama  "Mother Earth" (pacha=earth/time, mama=mother)', 'middle', 'Ls')
    s += hr(261)
    # Divider
    s += sec_divider(268, 'AYMARA  \u00b7  AYMAR ARU  \u00b7  SECONDARY LANGUAGE')
    s += sh(293, 'AYMARA ALPHABET')
    s += t(240, 304, 'Latin alphabet since colonial era, standardized 1984', 'middle', 'L')
    s += t(240, 315, 'Aymara also has 3-way stop contrast:', 'middle', 'H')
    s += t(240, 326, 'p  ph  p\'  /  t  th  t\'  /  k  kh  k\'  /  q  qh  q\'', 'middle', 'L')
    s += t(240, 337, 'Ejective consonants: t\' ch\' k\' q\' (glottalized releases)', 'middle', 'L')
    s += t(240, 348, 'Three-vowel system: a i u (exactly like Classical Quechua!)', 'middle', 'L')
    s += hr(356)
    s += sh(364, 'PARALLEL STRUCTURE')
    s += t(240, 375, 'Both Quechua and Aymara share the same consonant framework', 'middle', 'Ls')
    s += t(240, 386, 'Long contact may explain parallel phonological evolution', 'middle', 'Ls')
    s += t(240, 397, 'Quechua: ~8-10M speakers  \u2022  Aymara: ~2M speakers', 'middle', 'L')
    s += t(240, 408, 'Aymara: Bolivia (official), Peru, Chile', 'middle', 'Ls')
    s += t(240, 419, 'Quechua: Peru (official), Bolivia, Ecuador, Colombia, Argentina', 'middle', 'Ls')
    s += hr(427)
    s += sh(435, 'ANDEAN LANGUAGE CONTACT AREA')
    s += t(240, 446, 'Two families, NOT related — convergence through contact', 'middle', 'L')
    s += t(240, 457, 'Sprachbund: shared features through geographic proximity', 'middle', 'Ls')
    s += t(240, 468, 'Lake Titicaca basin: heartland of both language communities', 'middle', 'Ls')
    s += t(240, 479, 'Tiwanaku (500-1000 CE): precursor civilization spoke Aymara', 'middle', 'Ls')
    s += footer('46', 'QUECHUA', 'AYMARA', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 46b  PHONOLOGY ─────────────────────────────────────────────────────
def plate46b():
    s = open_svg()
    s += t(240, 28, 'QUECHUA', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'QUECHUA CONSONANT SYSTEM')
    s += t(240, 68, 'Three-way contrast at 6 places of articulation:', 'middle', 'L')
    s += t(240, 79, 'Bilabial:  p  ph  p\u02bc', 'middle', 'L')
    s += t(240, 90, 'Alveolar:  t  th  t\u02bc   ch  chh  ch\u02bc', 'middle', 'L')
    s += t(240, 101, 'Palatal:  ll /\u028e/ lateral   y /j/', 'middle', 'L')
    s += t(240, 112, 'Velar:  k  kh  k\u02bc', 'middle', 'L')
    s += t(240, 123, 'Uvular:  q  qh  q\u02bc  (back-of-throat, no European equivalent)', 'middle', 'L')
    s += t(240, 134, 'Ejectives: air plosion with closed glottis — explosive release', 'middle', 'Ls')
    s += hr(142)
    s += sh(150, 'THREE VOWELS ONLY')
    s += t(240, 161, 'a  i  u  (no e or o in classical Quechua)', 'middle', 'L')
    s += t(240, 172, 'Near uvular /q/: i and u lower to [e] and [o]', 'middle', 'Ls')
    s += t(240, 182, 'Vowel length contrast: mama "mother" vs. maama "aunt"', 'middle', 'L')
    s += hr(190)
    s += sh(198, 'STRESS & SYLLABLE STRUCTURE')
    s += t(240, 209, 'Fixed penultimate stress: pach\u00e1mama, \u00e1llin', 'middle', 'L')
    s += t(240, 219, 'No consonant clusters at syllable onset', 'middle', 'Ls')
    s += t(240, 229, 'Suffix-heavy: words can be very long (see grammar plate)', 'middle', 'Ls')
    s += hr(237)
    # Divider
    s += sec_divider(244, 'AYMARA PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(269, 'AYMARA CONSONANT SYSTEM')
    s += t(240, 280, 'Same three-way contrast as Quechua:', 'middle', 'L')
    s += t(240, 291, 'plain / aspirate / ejective at 6 places of articulation', 'middle', 'L')
    s += t(240, 302, 'Additional: retroflex series \u0288 \u0288h \u0288\u02bc (Quechua lacks this)', 'middle', 'L')
    s += t(240, 313, 'Uvular /q/ present (same as Quechua)', 'middle', 'Ls')
    s += hr(321)
    s += sh(329, 'AYMARA VOWELS')
    s += t(240, 340, 'Three vowels: a i u (same inventory as Quechua)', 'middle', 'L')
    s += t(240, 351, 'Stressed and unstressed vowels may differ in quality', 'middle', 'Ls')
    s += t(240, 362, 'Vowel harmony: suffix vowels harmonize with root', 'middle', 'Ls')
    s += hr(370)
    s += sh(378, 'PARALLEL PHONOLOGY — CONVERGENCE')
    s += t(240, 389, 'Both languages: 3 vowels  \u2022  uvular /q/  \u2022  ejectives', 'middle', 'L')
    s += t(240, 400, 'Both languages: aspirate stops  \u2022  SOV word order', 'middle', 'L')
    s += t(240, 411, 'Linguists debate: shared ancestry vs. areal diffusion?', 'middle', 'Ls')
    s += t(240, 422, 'Current consensus: separate families, convergent contact', 'middle', 'Ls')
    s += hr(430)
    s += sh(438, 'MINIMAL PAIRS ACROSS LANGUAGES')
    s += t(240, 449, 'Quechua: wasi "house"  \u2022  Aymara: uta "house"', 'middle', 'L')
    s += t(240, 460, 'Quechua: punchaw "day"  \u2022  Aymara: uru "day"', 'middle', 'L')
    s += t(240, 471, 'Core vocabulary DIFFERENT despite shared phonology', 'middle', 'Ls')
    s += t(240, 482, 'Confirms: contact area, not shared genetic ancestry', 'middle', 'Ls')
    s += footer('46', 'QUECHUA', 'AYMARA', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 46c  GRAMMAR ───────────────────────────────────────────────────────
def plate46c():
    s = open_svg()
    s += t(240, 28, 'QUECHUA', 'middle', 'T')
    s += t(240, 40, 'AGGLUTINATIVE GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'AGGLUTINATION — SUFFIX STACKING')
    s += t(240, 68, 'Quechua adds multiple suffixes to a single root:', 'middle', 'L')
    s += t(240, 79, 'wasi = house', 'middle', 'L')
    s += t(240, 90, 'wasiy = my house', 'middle', 'L')
    s += t(240, 101, 'wasiykipi = in your house', 'middle', 'L')
    s += t(240, 112, 'wasiykipichu = not in your house (question/negative)', 'middle', 'L')
    s += t(240, 123, 'wasiykipichum = and not in your house (evidential!)', 'middle', 'Ls')
    s += hr(131)
    s += sh(139, 'EVIDENTIALITY — UNIQUE FEATURE')
    s += t(240, 150, 'Quechua requires marking HOW you know information:', 'middle', 'L')
    s += t(240, 161, '-m/-mi: direct evidence (I saw it myself)', 'middle', 'L')
    s += t(240, 172, '-s/-si: reported/hearsay (I heard it from someone)', 'middle', 'L')
    s += t(240, 183, '-ch\u02bc/-chi: inference (I deduce it from clues)', 'middle', 'L')
    s += t(240, 194, 'Para-m paran  "It is raining" (I can see it)', 'middle', 'Ls')
    s += t(240, 204, 'Para-s paran  "They say it is raining" (hearsay)', 'middle', 'Ls')
    s += hr(212)
    s += sh(220, 'PERSONAL SUFFIXES ON VERBS')
    s += t(240, 231, 'Verbs mark person of subject and object simultaneously:', 'middle', 'Ls')
    s += t(240, 242, 'riku-ni = I see  \u2022  riku-nki = you see  \u2022  riku-n = s/he sees', 'middle', 'Ls')
    s += t(240, 253, 'riku-wa-nki = you see me  (object -wa- inserted)', 'middle', 'Ls')
    s += hr(261)
    # Divider
    s += sec_divider(268, 'AYMARA GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(293, 'AYMARA AGGLUTINATION')
    s += t(240, 304, 'Same agglutinative structure as Quechua:', 'middle', 'L')
    s += t(240, 315, 'uta = house  \u2022  utaja = my house  \u2022  utajana = in my house', 'middle', 'L')
    s += hr(323)
    s += sh(331, 'AYMARA EVIDENTIALITY')
    s += t(240, 342, 'Aymara also has grammaticalized evidentiality!', 'middle', 'L')
    s += t(240, 353, '-wa: personal knowledge  \u2022  -tayna: historical/inferred', 'middle', 'L')
    s += t(240, 364, 'Para-wa "It is raining" (I know directly)', 'middle', 'Ls')
    s += t(240, 375, 'Same evidentiality system as Quechua — areal feature!', 'middle', 'Ls')
    s += hr(383)
    s += sh(391, 'UNIQUE AYMARA FEATURE: SPATIAL TENSE')
    s += t(240, 402, 'Aymara encodes future as BEHIND, past as AHEAD:', 'middle', 'L')
    s += t(240, 413, 'Future = what you cannot see (behind you)', 'middle', 'Ls')
    s += t(240, 424, 'Past = what you have already seen (in front of you)', 'middle', 'Ls')
    s += t(240, 435, 'Opposite of English spatial metaphor for time', 'middle', 'Ls')
    s += hr(443)
    s += sh(451, 'SHARED GRAMMATICAL FEATURES')
    s += t(240, 462, 'Both: SOV  \u2022  agglutinative  \u2022  postpositions  \u2022  evidentiality', 'middle', 'L')
    s += t(240, 473, 'Both: no grammatical gender  \u2022  no articles', 'middle', 'L')
    s += t(240, 484, 'Both: verbs agree with subject and object person/number', 'middle', 'Ls')
    s += footer('46', 'QUECHUA', 'AYMARA', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 46d  HISTORY ───────────────────────────────────────────────────────
def plate46d():
    s = open_svg()
    s += t(240, 28, 'QUECHUA', 'middle', 'T')
    s += t(240, 40, 'HISTORY & ANDEAN CIVILIZATIONS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'QUECHUA ORIGINS')
    s += t(240, 68, 'Proto-Quechua: central Peru highlands, ~500 BCE', 'middle', 'L')
    s += t(240, 79, 'Wari Empire (600-1000 CE) spread Quechua across Andes', 'middle', 'Ls')
    s += t(240, 90, '1438-1533: Inca Empire (Tawantinsuyu) adopted Quechua as lingua franca', 'middle', 'Ls')
    s += t(240, 101, 'Runasimi ("people-speech"): Quechua\'s own name for itself', 'middle', 'L')
    s += t(240, 112, 'Inca administrators required Quechua throughout the empire', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'INCA EMPIRE (TAWANTINSUYU)')
    s += t(240, 139, 'Tawantinsuyu = "Four Quarters Together" — largest pre-Columbian state', 'middle', 'Ls')
    s += t(240, 150, 'Stretched 4,300 miles from Ecuador to central Chile', 'middle', 'Ls')
    s += t(240, 161, '1533: Spanish conquest — Francisco Pizarro captures Atahualpa', 'middle', 'Ls')
    s += t(240, 172, 'Colonial use: missionaries used Quechua to spread Christianity', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'QUECHUA TODAY')
    s += t(240, 199, '~8-10M speakers; official in Peru, Bolivia, Ecuador', 'middle', 'L')
    s += t(240, 210, '44 distinct Quechua varieties — not all mutually intelligible', 'middle', 'Ls')
    s += t(240, 221, 'English borrowings: puma, condor, llama, quinoa, coca', 'middle', 'L')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'AYMARA HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'TIWANAKU CIVILIZATION')
    s += t(240, 272, 'Tiwanaku (500-1000 CE): major Andean civilization at Lake Titicaca', 'middle', 'Ls')
    s += t(240, 283, 'Aymara likely spoken during Tiwanaku\u2019s peak influence', 'middle', 'Ls')
    s += t(240, 294, 'Gateway of the Sun: iconic monument at Tiwanaku', 'middle', 'L')
    s += t(240, 305, 'Tiwanaku collapsed ~1000 CE — Aymara kingdoms arose', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'INCA CONQUEST OF AYMARA LANDS')
    s += t(240, 332, '1430s: Inca Viracocha subjugated Aymara kingdoms', 'middle', 'L')
    s += t(240, 343, 'Aymara nobles incorporated into Inca administration', 'middle', 'Ls')
    s += t(240, 354, 'Quechua overlaid on Aymara territory — bilingualism began', 'middle', 'Ls')
    s += t(240, 365, 'Lake Titicaca (3,812m): sacred to both Inca and Aymara', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'AYMARA TODAY')
    s += t(240, 392, '~2M speakers; official language of Bolivia alongside Quechua', 'middle', 'L')
    s += t(240, 403, 'Bolivia: first president of Aymara descent — Evo Morales (2006)', 'middle', 'L')
    s += t(240, 414, 'Aymara concepts: "suma qamana" (good living) in Bolivian constitution', 'middle', 'Ls')
    s += hr(422)
    s += sh(430, 'ANDEAN LANGUAGE BOND')
    s += t(240, 441, '3000 years of coexistence in the Andes', 'middle', 'L')
    s += t(240, 452, 'Quechua spread through empire; Aymara preceded it', 'middle', 'Ls')
    s += t(240, 463, 'Both shaped by altitude, Andean cosmology, agricultural cycle', 'middle', 'Ls')
    s += t(240, 474, 'Pachamama (Quechua) and Pachamama (Aymara) — same Earth goddess', 'middle', 'Ls')
    s += t(240, 485, 'Two peoples, two languages, one mountain world', 'middle', 'L')
    s += footer('46', 'QUECHUA', 'AYMARA', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate46a_quechua_aymara_script_alt.svg', plate46a()),
                  ('plate46b_quechua_aymara_phonology_alt.svg', plate46b()),
                  ('plate46c_quechua_aymara_grammar_alt.svg', plate46c()),
                  ('plate46d_quechua_aymara_history_alt.svg', plate46d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
