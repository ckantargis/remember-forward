"""
Batch 8 — Sanskrit + Maithili alt plates (Series 15, plates 15a–15d)
Secondary language: Maithili (~34M speakers, Indo-Aryan, Bihar/Nepal)
Geographic link: Varanasi (Sanskrit tradition center) to Mithila region ~200mi
Maithili is among the most Sanskrit-preserving modern Indo-Aryan languages
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

# ── PLATE 15a  SCRIPT ────────────────────────────────────────────────────────
def plate15a():
    s = open_svg()
    s += t(240, 28, 'SANSKRIT', 'middle', 'T')
    s += t(240, 40, 'DEVANAGARI SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'DEVANAGARI — "CITY OF THE GODS" SCRIPT')
    s += t(240, 68, 'Abugida: each character = consonant + inherent /a/ vowel', 'middle', 'L')
    s += t(240, 79, 'Vowel cancellation: virama (\u094d) silences inherent /a/', 'middle', 'L')
    s += t(240, 90, 'Consonant row: \u0915 \u0916 \u0917 \u0918 \u0919   (ka kha ga gha nga)', 'middle', 'L')
    s += t(240, 101, '\u091a \u091b \u091c \u091d \u091e   (ca cha ja jha nya)', 'middle', 'L')
    s += t(240, 112, '\u091f \u0920 \u0921 \u0922 \u0923   (ta tha da dha na — retroflex)', 'middle', 'L')
    s += t(240, 123, '\u0924 \u0925 \u0926 \u0927 \u0928   (ta tha da dha na — dental)', 'middle', 'L')
    s += t(240, 134, '\u092a \u092b \u092c \u092d \u092e   (pa pha ba bha ma)', 'middle', 'L')
    s += t(240, 145, '\u092f \u0930 \u0932 \u0935 \u0936 \u0937 \u0938 \u0939   (ya ra la va sha sha sa ha)', 'middle', 'L')
    s += hr(153)
    s += sh(161, 'CONJUNCT CONSONANTS')
    s += t(240, 172, 'Consonant clusters form stacked/horizontal ligatures:', 'middle', 'L')
    s += t(240, 183, '\u0915\u094d\u0937 (ksha) \u2022 \u091c\u094d\u091e (jnya) \u2022 \u0924\u094d\u0930 (tra) \u2022 \u0936\u094d\u0930 (shra)', 'middle', 'L')
    s += t(240, 194, 'Sanskrit: dharmakshetre kurukshetre... (Bhagavad Gita)', 'middle', 'Ls')
    s += hr(202)
    s += sh(210, 'VOWELS & LONG VOWELS')
    s += t(240, 221, '\u0905 a  \u0906 \u0101  \u0907 i  \u0908 \u012b  \u0909 u  \u090a \u016b  \u090b r\u0325  \u090f e  \u0910 ai  \u0913 o  \u0914 au', 'middle', 'L')
    s += t(240, 232, 'Vowel length is phonemic: a/\u0101  i/\u012b  u/\u016b distinguish words', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'MAITHILI  \u00b7  \u092e\u0948\u0925\u093f\u0932\u0940  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'TIRHUTA (MITHILAKSHAR) SCRIPT')
    s += t(240, 283, 'Maithili has its own script: Tirhuta (also: Mithilakshar)', 'middle', 'L')
    s += t(240, 294, 'Derived from ancient Brahmi; sister to Bengali and Odia scripts', 'middle', 'Ls')
    s += t(240, 305, 'Distinct from Devanagari; recognizable by curved letterforms', 'middle', 'Ls')
    s += t(240, 316, 'Also written in Devanagari (especially in Bihar, India)', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'TIRHUTA SAMPLE')
    s += t(240, 344, '\U00011480\U00011485\U0001148f\U00011481\U0001148f\U00011489\U0001148f\U00011490', 'middle', 'Fb')
    s += t(240, 355, '(Maithili in Tirhuta script — Unicode 11480-114DF)', 'middle', 'Ls')
    s += t(240, 366, 'In Devanagari: \u092e\u0948\u0925\u093f\u0932\u0940 (Maithili)', 'middle', 'L')
    s += hr(374)
    s += sh(382, 'SCRIPT LINEAGE')
    s += t(240, 393, 'Brahmi (3rd c. BCE) \u2192 Gupta \u2192 Siddham \u2192 Tirhuta', 'middle', 'Ls')
    s += t(240, 404, 'Brahmi \u2192 Devanagari path (Nagari): Sanskrit standard', 'middle', 'Ls')
    s += t(240, 415, 'Both scripts descend from the SAME ancient Brahmi root', 'middle', 'L')
    s += hr(423)
    s += sh(431, 'SCRIPT PARALLEL: SHARED ABUGIDA STRUCTURE')
    s += t(240, 442, 'Both Devanagari and Tirhuta: abugida with inherent /a/', 'middle', 'Ls')
    s += t(240, 453, 'Both: consonant + virama to suppress inherent vowel', 'middle', 'Ls')
    s += t(240, 464, 'Both: conjunct consonants for clusters', 'middle', 'Ls')
    s += t(240, 475, 'Maithili scribes used Tirhuta for Sanskrit texts too', 'middle', 'Ls')
    s += footer('15', 'SANSKRIT', 'MAITHILI', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 15b  PHONOLOGY ─────────────────────────────────────────────────────
def plate15b():
    s = open_svg()
    s += t(240, 28, 'SANSKRIT', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY & SOUND SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SANSKRIT CONSONANT SYSTEM')
    s += t(240, 68, '5 places of articulation x 5 manner classes = 25 stops', 'middle', 'L')
    s += t(240, 79, 'Velars:  k  kh  g  gh  \u1e45', 'middle', 'L')
    s += t(240, 90, 'Palatals:  c  ch  j  jh  \u00f1', 'middle', 'L')
    s += t(240, 101, 'Retroflexes:  \u1e6d  \u1e6dh  \u1e0d  \u1e0dh  \u1e47', 'middle', 'L')
    s += t(240, 112, 'Dentals:  t  th  d  dh  n', 'middle', 'L')
    s += t(240, 123, 'Labials:  p  ph  b  bh  m', 'middle', 'L')
    s += t(240, 134, 'Each row: voiceless plain / voiceless aspirate / voiced plain / voiced aspirate / nasal', 'middle', 'Ls')
    s += hr(142)
    s += sh(150, 'SEMIVOWELS & SIBILANTS')
    s += t(240, 161, 'y r l v  (antahstha "in-between" sounds)', 'middle', 'L')
    s += t(240, 172, '\u015b \u1e63 s h  (three sibilants: palatal, retroflex, dental)', 'middle', 'L')
    s += t(240, 183, 'Three distinct /s/ sounds — preserved from Proto-Indo-European', 'middle', 'Ls')
    s += hr(191)
    s += sh(199, 'VOWEL SYSTEM')
    s += t(240, 210, 'Short: a i u r\u0325 l\u0325  /  Long: \u0101 \u012b \u016b r\u0325\u0304  (quantity distinction)', 'middle', 'L')
    s += t(240, 221, 'Diphthongs: e ai o au (historically \u0101+i, \u0101+u)', 'middle', 'L')
    s += t(240, 232, 'Syllabic /r\u0325/ and /l\u0325/: consonants that act as vowels', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'MAITHILI PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'MAITHILI CONSONANT SYSTEM')
    s += t(240, 283, 'Inherited Sanskrit\u2019s five-place articulation system', 'middle', 'L')
    s += t(240, 294, 'Retroflex stops: \u1e6d \u1e6dh \u1e0d \u1e0dh \u1e47 (preserved from Sanskrit)', 'middle', 'L')
    s += t(240, 305, 'Aspirates: kh gh ch jh \u1e6dh \u1e0dh th dh ph bh (all 10 preserved)', 'middle', 'L')
    s += t(240, 316, 'Maithili preserves more Sanskrit phonemes than Hindi', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'MAITHILI VOWELS')
    s += t(240, 343, 'Seven vowels: a \u0101 i \u012b u \u016b e o', 'middle', 'L')
    s += t(240, 354, 'Nasalized vowels: \u00e3 \u0129 \u00f5 (Sanskrit nasal anusvara preserved)', 'middle', 'L')
    s += t(240, 365, 'Word-final short /a/ often silent (like Hindi, unlike Sanskrit)', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'PHONOLOGICAL CONSERVATION')
    s += t(240, 392, 'Maithili conserves Sanskrit aspirates better than neighboring languages:', 'middle', 'Ls')
    s += t(240, 403, 'Sanskrit bhumi \u2192 Maithili bhumi "earth" (aspirate preserved)', 'middle', 'Ls')
    s += t(240, 414, 'Sanskrit karma \u2192 Maithili karma "action" (direct loan form)', 'middle', 'Ls')
    s += t(240, 425, 'Sanskrit dharma \u2192 Maithili dharma (unchanged!)', 'middle', 'L')
    s += hr(433)
    s += sh(441, 'TONAL FEATURES')
    s += t(240, 452, 'Some Maithili dialects have pitch accent (like ancient Sanskrit!)', 'middle', 'Ls')
    s += t(240, 463, 'Vedic Sanskrit had 3 pitch accents: udatta, anudatta, svarita', 'middle', 'Ls')
    s += t(240, 474, 'Maithili dialects preserve traces of this ancient pitch system', 'middle', 'Ls')
    s += footer('15', 'SANSKRIT', 'MAITHILI', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 15c  GRAMMAR ───────────────────────────────────────────────────────
def plate15c():
    s = open_svg()
    s += t(240, 28, 'SANSKRIT', 'middle', 'T')
    s += t(240, 40, 'GRAMMATICAL STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'EIGHT CASES OF SANSKRIT')
    s += t(240, 68, 'Nominative (kartaa) \u2022 Accusative (karma) \u2022 Instrumental (karaa)', 'middle', 'L')
    s += t(240, 79, 'Dative (sampradaana) \u2022 Ablative (apaadaana) \u2022 Genitive (sambandha)', 'middle', 'L')
    s += t(240, 90, 'Locative (adhikarana) \u2022 Vocative (sambodhana)', 'middle', 'L')
    s += t(240, 101, 'Three numbers: singular / dual / plural', 'middle', 'L')
    s += t(240, 112, 'Three genders: masculine / feminine / neuter', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'VERB SYSTEM')
    s += t(240, 139, '10 verb classes (gaana); complex conjugation table', 'middle', 'L')
    s += t(240, 150, 'Three voices: active (parasmaipada) \u2022 middle (aatmanepada) \u2022 passive', 'middle', 'Ls')
    s += t(240, 161, 'Dual number in verbs: gacchataH "the two go"', 'middle', 'L')
    s += t(240, 172, '10 tenses/moods: present, past, future, conditional, imperative...', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'SANDHI — PHONOLOGICAL FUSION')
    s += t(240, 199, 'Words at boundaries merge and transform (sandhi rules):', 'middle', 'L')
    s += t(240, 210, 'na + iti \u2192 neti "not thus"', 'middle', 'L')
    s += t(240, 221, 'raamaH + aagacchati \u2192 raamaagacchati', 'middle', 'L')
    s += t(240, 232, 'P\u0101nini (4th c. BCE): 3,959 rules for Sanskrit grammar (Ashtadhyayi)', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'MAITHILI GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'MAITHILI CASE SYSTEM')
    s += t(240, 283, 'Postpositional system derived from Sanskrit cases:', 'middle', 'L')
    s += t(240, 294, 'Nominative: ghara "house"  \u2022  Genitive: gharak "of the house"', 'middle', 'L')
    s += t(240, 305, 'Locative: ghara-me "in the house"  (Sanskrit locative suffix -e!)', 'middle', 'L')
    s += t(240, 316, 'Maithili preserves more case-like distinctions than Hindi', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'HONORIFIC SYSTEM — THREE LEVELS')
    s += t(240, 343, 'Maithili marks social register in pronouns and verbs:', 'middle', 'L')
    s += t(240, 354, 'Apan/aapan: highest honorific (elders, deities)', 'middle', 'L')
    s += t(240, 365, 'Ahaa/ahan: medium honorific (respectful address)', 'middle', 'L')
    s += t(240, 376, 'Toohu/tohu: low/intimate (close friends, children)', 'middle', 'L')
    s += t(240, 387, 'Verb forms change completely for each level', 'middle', 'Ls')
    s += hr(395)
    s += sh(403, 'MAITHILI VERB AGREEMENT')
    s += t(240, 414, 'Verbs agree with subject in person, number, gender AND honorific', 'middle', 'Ls')
    s += t(240, 425, '"She goes" at high register \u2260 "she goes" at intimate register', 'middle', 'Ls')
    s += t(240, 436, 'Sanskrit had honorific address but Maithili systematized it', 'middle', 'Ls')
    s += hr(444)
    s += sh(452, 'GRAMMATICAL CONTINUITY')
    s += t(240, 463, 'Sanskrit \u2192 Maithili: Sanskrit 8 cases \u2192 Maithili postpositional', 'middle', 'Ls')
    s += t(240, 474, 'Sanskrit 3 genders preserved in Maithili (unlike Hindi-only 2)', 'middle', 'Ls')
    s += t(240, 485, 'Maithili verbs more conservative than Hindi in aspect marking', 'middle', 'Ls')
    s += footer('15', 'SANSKRIT', 'MAITHILI', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 15d  HISTORY ───────────────────────────────────────────────────────
def plate15d():
    s = open_svg()
    s += t(240, 28, 'SANSKRIT', 'middle', 'T')
    s += t(240, 40, 'HISTORY & THE MITHILA CONNECTION', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SANSKRIT — LANGUAGE OF THE VEDAS')
    s += t(240, 68, '~1500 BCE: Vedic Sanskrit — oldest attested Indo-Iranian', 'middle', 'L')
    s += t(240, 79, 'Rigveda: oldest religious text still in use worldwide', 'middle', 'L')
    s += t(240, 90, '~500-400 BCE: Classical Sanskrit codified by P\u0101\u1e47ini (Ashtadhyayi)', 'middle', 'Ls')
    s += t(240, 101, 'P\u0101nini\u2019s grammar: 3,959 sutras — world\u2019s first formal grammar', 'middle', 'Ls')
    s += t(240, 112, 'Sanskrit = "refined" (sam + krita = "put together perfectly")', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'CLASSICAL SANSKRIT LITERATURE')
    s += t(240, 139, 'Mahabharata (400 BCE-400 CE): 1.8M words — longest epic ever', 'middle', 'Ls')
    s += t(240, 150, 'Ramayana: Valmiki\u2019s 24,000 verses — Rama\u2019s exile and return', 'middle', 'Ls')
    s += t(240, 161, 'Kalidasa (4th c. CE): Shakuntala, Meghaduta — Sanskrit\u2019s height', 'middle', 'Ls')
    s += t(240, 172, 'Ayurveda, Arthashastra, Natyashastra: sciences in Sanskrit', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'SANSKRIT INFLUENCE ON WORLD LANGUAGES')
    s += t(240, 199, 'Proto-Indo-European ancestor: Sanskrit shares roots with Greek, Latin', 'middle', 'Ls')
    s += t(240, 210, 'Sanskrit asvah = Latin equus = English "equine" (horse)', 'middle', 'Ls')
    s += t(240, 221, 'Sanskrit matar = Latin mater = English "mother"', 'middle', 'Ls')
    s += t(240, 232, 'Influenced Persian, Arabic (via loanwords), SE Asian languages', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'MAITHILI HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'MITHILA — LAND OF JANAKA AND SITA')
    s += t(240, 283, 'Mithila: ancient kingdom mentioned in the Ramayana and Mahabharata', 'middle', 'Ls')
    s += t(240, 294, 'King Janaka of Mithila: father of Sita (Ram\u2019s wife)', 'middle', 'L')
    s += t(240, 305, 'Janaka\u2019s court: famous Sanskrit philosophical debates (Upanishads)', 'middle', 'Ls')
    s += t(240, 316, 'Yaajnavalkya and Gargi debated there — first female philosopher?', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'MAITHILI LITERARY TRADITION')
    s += t(240, 343, 'Vidyapati (c. 1352-1448): greatest Maithili poet', 'middle', 'L')
    s += t(240, 354, 'Padavali: Sanskrit-Maithili devotional songs for Radha-Krishna', 'middle', 'Ls')
    s += t(240, 365, 'Vidyapati\u2019s language: bridge between Sanskrit and vernacular', 'middle', 'Ls')
    s += t(240, 376, 'Songs still sung at weddings and festivals in Bihar and Nepal', 'middle', 'Ls')
    s += hr(384)
    s += sh(392, 'MAITHILI RECOGNITION')
    s += t(240, 403, '1965: Sahitya Akademi recognizes Maithili as Indian literature', 'middle', 'L')
    s += t(240, 414, '2003: Added to Eighth Schedule of Indian Constitution', 'middle', 'L')
    s += t(240, 425, '~34M speakers in Bihar (India) and Madhesh Province (Nepal)', 'middle', 'L')
    s += t(240, 436, 'Maithili in Nepal: second most spoken language after Nepali', 'middle', 'Ls')
    s += hr(444)
    s += sh(452, 'THE SANSKRIT-MAITHILI THREAD')
    s += t(240, 463, 'Mithila scribes: wrote both Sanskrit texts and Maithili poetry', 'middle', 'Ls')
    s += t(240, 474, 'Tirhuta script: used for Sanskrit and Maithili interchangeably', 'middle', 'Ls')
    s += t(240, 485, '3000 years of Sanskrit scholarship flowing into Maithili tongue', 'middle', 'L')
    s += footer('15', 'SANSKRIT', 'MAITHILI', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate15a_sanskrit_maithili_script_alt.svg', plate15a()),
                  ('plate15b_sanskrit_maithili_phonology_alt.svg', plate15b()),
                  ('plate15c_sanskrit_maithili_grammar_alt.svg', plate15c()),
                  ('plate15d_sanskrit_maithili_history_alt.svg', plate15d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
