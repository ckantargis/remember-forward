"""
Batch 9 — Sinhala + Malayalam alt plates (Series 44, plates 44a–44d)
Secondary language: Malayalam (~38M speakers, Dravidian, Kerala/India)
Geographic link: Colombo (Sinhala center) to Thiruvananthapuram (Malayalam) ~240mi
Closest mainland Dravidian language to Sri Lanka; ancient trade connections
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

# ── PLATE 44a  SCRIPT ────────────────────────────────────────────────────────
def plate44a():
    s = open_svg()
    s += t(240, 28, 'SINHALA', 'middle', 'T')
    s += t(240, 40, 'SINHALA SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SINHALA SCRIPT — AN ABUGIDA')
    s += t(240, 68, 'Derived from Brahmi via Grantha and Pallava scripts (~3rd c. BCE)', 'middle', 'Ls')
    s += t(240, 79, 'Rounded letterforms (written on palm leaves — curves avoid splits)', 'middle', 'Ls')
    s += t(240, 90, 'Consonants: inherent /a/ vowel, cancelled by diacritics', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'SINHALA CONSONANTS')
    s += t(240, 117, '\u0d9a /k/  \u0d9c /g/  \u0da2 /j/  \u0da7 /\u0288/  \u0dad /t/  \u0db4 /p/  \u0db6 /b/', 'middle', 'L')
    s += t(240, 128, '\u0dbd /l/  \u0dbb /r/  \u0dc0 /v/  \u0dc3 /s/  \u0dc4 /h/  \u0db8 /m/  \u0db1 /n/', 'middle', 'L')
    s += t(240, 139, 'Sinhala has prenasalized stops: \u0db9\u0dca\u0dba \u0dab\u0dca\u0da9 (rare cross-linguistically)', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'SINHALA VOWELS')
    s += t(240, 166, '\u0d85 a  \u0d86 \u0101  \u0d87 \u00e6  \u0d88 \u00e6\u02d0  \u0d89 i  \u0d8a \u012b  \u0d8b u  \u0d8c \u016b', 'middle', 'L')
    s += t(240, 177, '\u0d91 e  \u0d92 \u0113  \u0d94 o  \u0d95 \u014d  \u0d96 au', 'middle', 'L')
    s += t(240, 188, 'Sinhala uniquely preserves Old Sinhala vowels /\u00e6/ and /\u00e6\u02d0/', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'SAMPLE TEXT')
    s += t(240, 216, '\u0d86\u0dba\u0dd4\u0db6\u0ddd\u0d9c\u0db1\u0dca\u0db1', 'middle', 'Fb')
    s += t(240, 227, 'Ayubowan — "May you live long" (Sinhala greeting)', 'middle', 'Ls')
    s += hr(235)
    # Divider
    s += sec_divider(242, 'MALAYALAM  \u00b7  \u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02  \u00b7  SECONDARY LANGUAGE')
    s += sh(267, 'MALAYALAM SCRIPT')
    s += t(240, 278, 'Also from Brahmi via Grantha; closely related to Sinhala script', 'middle', 'Ls')
    s += t(240, 289, 'Rounded letterforms — same palm leaf scribing tradition', 'middle', 'Ls')
    s += t(240, 300, '~500 distinct characters including conjuncts', 'middle', 'L')
    s += t(240, 311, 'Reformed orthography 1971: reduced conjunct forms', 'middle', 'Ls')
    s += hr(319)
    s += sh(327, 'MALAYALAM SAMPLE')
    s += t(240, 339, '\u0d28\u0d2e\u0d38\u0d4d\u0d15\u0d3e\u0d30\u0d02', 'middle', 'Fb')
    s += t(240, 350, 'Namaskaram — "Greetings" (formal greeting)', 'middle', 'Ls')
    s += t(240, 361, '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02 = mountain + valley language (mala + alam)', 'middle', 'Ls')
    s += hr(369)
    s += sh(377, 'SCRIPT COMPARISON')
    s += t(240, 388, 'Both: rounded Brahmi-derived abugidas', 'middle', 'L')
    s += t(240, 399, 'Both: inherent /a/ with vowel diacritics', 'middle', 'L')
    s += t(240, 410, 'Both: left-to-right direction', 'middle', 'L')
    s += t(240, 421, 'Sinhala: 54 consonants  \u2022  Malayalam: 53 consonants', 'middle', 'L')
    s += t(240, 432, 'Both share Grantha heritage — visible in letterform shapes', 'middle', 'Ls')
    s += footer('44', 'SINHALA', 'MALAYALAM', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 44b  PHONOLOGY ─────────────────────────────────────────────────────
def plate44b():
    s = open_svg()
    s += t(240, 28, 'SINHALA', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SINHALA CONSONANT SYSTEM')
    s += t(240, 68, 'Sinhala has prenasalized stops — unique in South Asia:', 'middle', 'L')
    s += t(240, 79, '\u1d50b /\u1d50b/ \u00b7 \u1d50d /\u1d50d/ \u00b7 \u1d50e /\u1d50e/ (prenasalized t, d, g)', 'middle', 'L')
    s += t(240, 90, 'Distinct from nasal + consonant sequences', 'middle', 'Ls')
    s += t(240, 101, 'Retroflex consonants: \u1e6d \u1e0d \u1e47 \u027c (from Dravidian substrate)', 'middle', 'L')
    s += t(240, 112, 'Aspirated stops: kh gh (Sanskrit loans preserve aspiration)', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'SINHALA VOWEL SYSTEM')
    s += t(240, 139, '14 vowel phonemes including short/long pairs:', 'middle', 'L')
    s += t(240, 150, 'a /a/ \u2022 \u0101 /a:/ \u2022 \u00e6 /\u00e6/ \u2022 i /i/ \u2022 \u012b /i:/ \u2022 u /u/ \u2022 \u016b /u:/', 'middle', 'L')
    s += t(240, 161, 'e /e/ \u2022 \u0113 /e:/ \u2022 o /o/ \u2022 \u014d /o:/ \u2022 au /au/', 'middle', 'L')
    s += t(240, 172, '/\u00e6/ and /\u00e6:/ are unique to Sinhala in the region', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'DIGLOSSIA IN SINHALA')
    s += t(240, 199, 'Written (literary) Sinhala differs significantly from spoken:', 'middle', 'L')
    s += t(240, 210, 'Written: gama \u2192 Spoken: game (grammatical suffix drops)', 'middle', 'Ls')
    s += t(240, 221, 'Case endings: written -ta (dative) \u2192 spoken -(a)ta', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'MALAYALAM PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'MALAYALAM CONSONANTS')
    s += t(240, 272, 'Full Dravidian retroflex set: \u0288 \u0256 \u1e37 \u1e43 \u027c', 'middle', 'L')
    s += t(240, 283, 'Dental/retroflex distinction: t/\u0288  d/\u0256  n/\u1e47 (both series)', 'middle', 'L')
    s += t(240, 294, 'Lateral /l/ and retroflex lateral /\u1e37/ both phonemic', 'middle', 'L')
    s += t(240, 305, 'Trill /r/ and approximant /\u027c/ both phonemic (rare distinction)', 'middle', 'L')
    s += hr(313)
    s += sh(321, 'MALAYALAM VOWELS')
    s += t(240, 332, '16 vowels: a \u0101 i \u012b u \u016b \u1e5b \u1e5d e \u0113 ai o \u014d au am ah', 'middle', 'L')
    s += t(240, 343, 'Syllabic /\u1e5b/ (vocalic r) from Sanskrit loans', 'middle', 'Ls')
    s += t(240, 354, 'No prenasalized stops (unlike Sinhala)', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'PHONOLOGICAL CONNECTIONS')
    s += t(240, 381, 'Sinhala retroflexes from Dravidian substrate contact with Tamil/Malayalam', 'middle', 'Ls')
    s += t(240, 392, 'Sri Lanka: Tamil (Dravidian) speakers long preceded Sinhala', 'middle', 'Ls')
    s += t(240, 403, 'Sinhala borrowed retroflex phonemes from Tamil/Malayalam', 'middle', 'Ls')
    s += t(240, 414, 'Both: 5+ point of articulation consonant systems', 'middle', 'Ls')
    s += t(240, 425, 'Both: voiced/voiceless aspiration contrasts (via Sanskrit)', 'middle', 'Ls')
    s += footer('44', 'SINHALA', 'MALAYALAM', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 44c  GRAMMAR ───────────────────────────────────────────────────────
def plate44c():
    s = open_svg()
    s += t(240, 28, 'SINHALA', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SINHALA WORD ORDER & CASES')
    s += t(240, 68, 'SOV with postpositions; 4 cases (nom/gen/dat/acc)', 'middle', 'L')
    s += t(240, 79, 'Nominative: maama "uncle"  \u2022  Genitive: maamine "of uncle"', 'middle', 'L')
    s += t(240, 90, 'Dative: maama-ta "to uncle"  \u2022  Accusative: maama-wa "uncle" (obj)', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'ANIMACY DISTINCTION')
    s += t(240, 117, 'Sinhala distinguishes animate vs. inanimate in agreement:', 'middle', 'L')
    s += t(240, 128, 'Animate (people, animals): maama-la "uncles" (plural -la)', 'middle', 'L')
    s += t(240, 139, 'Inanimate (things): pota "books" (collective/unmarked)', 'middle', 'L')
    s += t(240, 150, 'Verbs also distinguish animate/inanimate subject', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'SINHALA VERB SYSTEM')
    s += t(240, 177, 'Verbs mark tense (past/non-past), aspect, and voice', 'middle', 'L')
    s += t(240, 188, 'Non-past: present and future share same form (context determines)', 'middle', 'Ls')
    s += t(240, 199, 'Involuntary verbs: separate class for actions beyond control', 'middle', 'L')
    s += t(240, 210, '"I fell" uses involuntary form — action happened to subject', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'MALAYALAM GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'MALAYALAM CASE SYSTEM (8 CASES)')
    s += t(240, 261, 'More elaborate case system than Sinhala:', 'middle', 'L')
    s += t(240, 272, 'Nominative \u2022 Accusative \u2022 Dative \u2022 Sociative \u2022 Instrumental', 'middle', 'L')
    s += t(240, 283, 'Genitive \u2022 Locative \u2022 Vocative', 'middle', 'L')
    s += t(240, 294, 'Case suffixes agglutinate to noun stems', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'MALAYALAM GENDER SYSTEM')
    s += t(240, 321, 'Three genders: masculine / feminine / neuter', 'middle', 'L')
    s += t(240, 332, 'Based on animacy and sex: rational (human) vs. irrational', 'middle', 'Ls')
    s += t(240, 343, 'Plants, animals (mostly): neuter \u2022 Humans: masc/fem', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'MALAYALAM VERB AGREEMENT')
    s += t(240, 370, 'Verbs agree with subject in person, number, and gender', 'middle', 'L')
    s += t(240, 381, 'Rich tense system: past / present / future + aspects', 'middle', 'L')
    s += t(240, 392, 'Subjunctive and conditional moods well-developed', 'middle', 'Ls')
    s += hr(400)
    s += sh(408, 'GRAMMATICAL PARALLELS')
    s += t(240, 419, 'Both: SOV word order  \u2022  postpositions  \u2022  agglutinative', 'middle', 'L')
    s += t(240, 430, 'Both: animacy distinction in grammar', 'middle', 'L')
    s += t(240, 441, 'Both: Sanskrit loanword layer in vocabulary', 'middle', 'L')
    s += t(240, 452, 'Sinhala: Indo-Aryan with Dravidian substrate from Malayalam/Tamil', 'middle', 'Ls')
    s += t(240, 463, 'Malayalam: Dravidian with Sanskrit/Prakrit superstrate', 'middle', 'Ls')
    s += t(240, 474, 'Languages shaped each other across the Palk Strait', 'middle', 'Ls')
    s += footer('44', 'SINHALA', 'MALAYALAM', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 44d  HISTORY ───────────────────────────────────────────────────────
def plate44d():
    s = open_svg()
    s += t(240, 28, 'SINHALA', 'middle', 'T')
    s += t(240, 40, 'HISTORY & INDIAN OCEAN CONNECTIONS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SINHALA ORIGINS')
    s += t(240, 68, '~500 BCE: Prince Vijaya from North India arrives in Lanka', 'middle', 'L')
    s += t(240, 79, 'Mahavamsa: Sanskrit chronicle; Sinhala identity tied to Buddhism', 'middle', 'Ls')
    s += t(240, 90, '247 BCE: Buddhism arrives in Lanka (Mahinda, son of Ashoka)', 'middle', 'L')
    s += t(240, 101, 'Sinhala became the language of Theravada Buddhist scholarship', 'middle', 'Ls')
    s += t(240, 112, 'Anuradhapura (377 BCE-1017 CE): ancient Sinhala capital', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'SINHALA LITERATURE')
    s += t(240, 139, '~2nd c. BCE: earliest Sinhala inscriptions at rock caves', 'middle', 'L')
    s += t(240, 150, 'Sigiri graffiti (5th-8th c. CE): earliest Sinhala poetry', 'middle', 'L')
    s += t(240, 161, 'Mahavamsa (~5th c. CE): Buddhist historical epic', 'middle', 'Ls')
    s += t(240, 172, '~10M speakers; official language of Sri Lanka', 'middle', 'L')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'MALAYALAM HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'KERALA — SPICE COAST')
    s += t(240, 223, 'Kerala: world\u2019s most sought pepper, cardamom, ginger, nutmeg', 'middle', 'Ls')
    s += t(240, 234, 'Arab, Chinese, Greek, Roman traders all visited Malayalam coast', 'middle', 'Ls')
    s += t(240, 245, '~830 CE: Malayalam separates from Tamil as distinct language', 'middle', 'L')
    s += t(240, 256, 'Cheraman Perumals: last kings united Kerala before fragmentation', 'middle', 'Ls')
    s += hr(264)
    s += sh(272, 'MALAYALAM LITERARY TRADITION')
    s += t(240, 283, 'Ramacharitam (12th c.): first major Malayalam literary text', 'middle', 'L')
    s += t(240, 294, 'Manipravalam: mixed Sanskrit-Malayalam literary style', 'middle', 'Ls')
    s += t(240, 305, 'Ezhuthachan (16th c.): father of modern Malayalam literature', 'middle', 'Ls')
    s += t(240, 316, 'Thunchaththu Ramanujan Ezhuthachan: adapted Ramayana in Malayalam', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'KERALA TODAY')
    s += t(240, 343, '~38M speakers; official language of Kerala state', 'middle', 'L')
    s += t(240, 354, 'Kerala: 100% literacy rate — highest in India', 'middle', 'L')
    s += t(240, 365, 'Malayalam diaspora: Gulf countries, USA, UK', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'THE PALK STRAIT CONNECTION')
    s += t(240, 392, 'Sri Lanka and Kerala separated by ~240mi of ocean', 'middle', 'L')
    s += t(240, 403, 'Trade: cinnamon (Lanka) \u2212 pepper (Kerala) — ancient exchange', 'middle', 'Ls')
    s += t(240, 414, 'Sinhala absorbed Dravidian phonology from Tamil/Malayalam contact', 'middle', 'Ls')
    s += t(240, 425, 'Malayalam loanwords in Sinhala: hundreds of common terms', 'middle', 'Ls')
    s += t(240, 436, 'Buddhist monks: Malayalam Kerala \u2194 Sri Lanka exchange routes', 'middle', 'Ls')
    s += t(240, 447, 'Two island/coastal peoples shaped by the Indian Ocean', 'middle', 'L')
    s += footer('44', 'SINHALA', 'MALAYALAM', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate44a_sinhala_malayalam_script_alt.svg', plate44a()),
                  ('plate44b_sinhala_malayalam_phonology_alt.svg', plate44b()),
                  ('plate44c_sinhala_malayalam_grammar_alt.svg', plate44c()),
                  ('plate44d_sinhala_malayalam_history_alt.svg', plate44d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
