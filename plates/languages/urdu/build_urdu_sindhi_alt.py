"""
Batch 12 — Urdu + Sindhi alt plates (Series 54, plates 54a–54d)
Secondary language: Sindhi (~33M speakers, Indo-Aryan, Pakistan/India)
Geographic link: Karachi (Sindhi center) to Islamabad (Urdu/Pakistan capital) ~500mi
Both Indo-Aryan; Urdu is Pakistan's national language; Sindhi is provincial official language of Sindh
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

# ── PLATE 54a  SCRIPT ────────────────────────────────────────────────────────
def plate54a():
    s = open_svg()
    s += t(240, 28, 'URDU', 'middle', 'T')
    s += t(240, 40, 'NASTALIQ SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'NASTALIQ — HANGING CALLIGRAPHY')
    s += t(240, 68, 'Urdu written in Nastaliq: most elegant Arabic-script style', 'middle', 'L')
    s += t(240, 79, 'Nastaliq = "hanging" \u2014 letters hang diagonally rightward', 'middle', 'L')
    s += t(240, 90, 'Developed in Persia (~15th c.); perfected in Mughal India', 'middle', 'Ls')
    s += t(240, 101, 'Right-to-left; 36 base letters; abjad (vowels optional)', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'URDU-SPECIFIC LETTERS')
    s += t(240, 128, 'Added letters not in Arabic: \u0679 /\u0288/ \u0688 /\u0256/ \u0691 /\u027c/ \u06ba /\u014b/ \u06be /\u02b0/', 'middle', 'L')
    s += t(240, 139, 'These represent retroflex sounds from Sanskrit heritage', 'middle', 'Ls')
    s += t(240, 150, 'do chashmi he (\u06be): aspirate marker in Nastaliq', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'SAMPLE TEXT')
    s += t(240, 178, '\u0622\u067e \u06a9\u06cc\u0633\u06d2 \u06c1\u06cc\u06ba\u061f  "Aap kaise hain?" (How are you? formal)', 'middle', 'L')
    s += t(240, 189, '\u0634\u06a9\u0631\u06cc\u06c1  "Shukriya" (Thank you)', 'middle', 'L')
    s += t(240, 200, '\u0627\u0631\u062f\u0648  Urdu (the language)', 'middle', 'L')
    s += hr(208)
    s += sh(216, 'URDU vs. HINDI — ONE SPOKEN LANGUAGE')
    s += t(240, 227, 'Urdu and Hindi are mutually intelligible in everyday speech', 'middle', 'L')
    s += t(240, 238, 'Urdu: Nastaliq script  \u2022  Hindi: Devanagari script', 'middle', 'L')
    s += t(240, 249, 'Urdu: Persian/Arabic vocabulary layer  \u2022  Hindi: Sanskrit vocabulary', 'middle', 'Ls')
    s += hr(257)
    # Divider
    s += sec_divider(264, 'SINDHI  \u00b7  \u0633\u0646\u068c\u064a  \u00b7  SECONDARY LANGUAGE')
    s += sh(289, 'SINDHI PERSO-ARABIC SCRIPT (52 LETTERS)')
    s += t(240, 300, 'Largest Perso-Arabic alphabet of any language (52 letters!)', 'middle', 'L')
    s += t(240, 311, 'Standard Arabic has 28 \u2022 Urdu Nastaliq has 36 \u2022 Sindhi has 52', 'middle', 'L')
    s += t(240, 322, 'Extra letters represent unique Sindhi phonemes:', 'middle', 'H')
    s += t(240, 333, '\u068c /\u0253/  \u0684 /\u0257/  \u0683 /\u0272/  \u06b3 /\u014b/ (implosives + velar nasal)', 'middle', 'L')
    s += hr(341)
    s += sh(349, 'SINDHI ALSO IN DEVANAGARI')
    s += t(240, 360, 'In India: Hindu Sindhis use Devanagari for Sindhi', 'middle', 'L')
    s += t(240, 371, 'Same language, two scripts (like Urdu/Hindi!)', 'middle', 'L')
    s += t(240, 382, 'Pakistan Sindhi: Perso-Arabic  \u2022  India Sindhi: Devanagari', 'middle', 'Ls')
    s += hr(390)
    s += sh(398, 'SCRIPT COMPARISON')
    s += t(240, 409, 'Both: right-to-left Perso-Arabic scripts', 'middle', 'L')
    s += t(240, 420, 'Urdu: 36 letters  \u2022  Sindhi: 52 letters (more phonemic coverage)', 'middle', 'L')
    s += t(240, 431, 'Both: abjad system (short vowels usually omitted)', 'middle', 'L')
    s += t(240, 442, 'Shared Arabic letter base; different supplementary letters', 'middle', 'Ls')
    s += footer('54', 'URDU', 'SINDHI', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 54b  PHONOLOGY ─────────────────────────────────────────────────────
def plate54b():
    s = open_svg()
    s += t(240, 28, 'URDU', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'URDU CONSONANT SYSTEM')
    s += t(240, 68, 'Stops: p b ph bh  t d th dh  T D Th Dh  k g kh gh', 'middle', 'L')
    s += t(240, 79, '(T D Th Dh = retroflex series)', 'middle', 'Ls')
    s += t(240, 90, 'Aspirates: ph bh th dh Th Dh kh gh (full Sanskrit set)', 'middle', 'L')
    s += t(240, 101, 'Fricatives from Arabic/Persian: q f z x G (not in Sanskrit)', 'middle', 'L')
    s += t(240, 112, 'q = /q/ uvular  \u2022  x = /x/ velar  \u2022  G = /\u0263/ uvular voiced', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'URDU VOWELS')
    s += t(240, 139, 'Short: a i u  \u2022  Long: aa ii uu  \u2022  Diphthongs: ai au', 'middle', 'L')
    s += t(240, 150, 'Nasalized vowels: \u00e3 \u0129 \u00f5 (from Sanskrit nasals)', 'middle', 'L')
    s += t(240, 161, 'No tones; stress generally penultimate', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'URDU ASPIRATES')
    s += t(240, 188, 'Aspiration is phonemic: pal "moment" vs. phal "fruit"', 'middle', 'L')
    s += t(240, 199, 'All four stop series have aspirated pairs (unlike Arabic)', 'middle', 'Ls')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'SINDHI PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'SINDHI IMPLOSIVE CONSONANTS')
    s += t(240, 250, 'Four implosive stops: /\u0253/ /\u0257/ /\u0284/ /\u0260/', 'middle', 'L')
    s += t(240, 261, 'Implosives: air pulled inward during stop closure (opposite of ejective)', 'middle', 'L')
    s += t(240, 272, 'Bilabial /\u0253/  \u2022  Dental /\u0257/  \u2022  Palatal /\u0284/  \u2022  Velar /\u0260/', 'middle', 'L')
    s += t(240, 283, 'Only Sindhi and Saraiki have all four in an Indo-Aryan language', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'SINDHI ASPIRATES')
    s += t(240, 310, 'Sindhi has the same aspirate series as Urdu: kh gh ph bh th dh...', 'middle', 'L')
    s += t(240, 321, 'PLUS four aspirated implosives: unique worldwide!', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'PHONOLOGICAL COMPARISON')
    s += t(240, 348, 'Both: retroflex series T D Th Dh (Sanskrit heritage)', 'middle', 'L')
    s += t(240, 359, 'Both: aspirated stops ph bh kh gh etc.', 'middle', 'L')
    s += t(240, 370, 'Both: Arabic loan phonemes q x (limited integration)', 'middle', 'L')
    s += t(240, 381, 'Sindhi: + 4 implosives  \u2022  Urdu: no implosives', 'middle', 'L')
    s += t(240, 392, 'Urdu: larger Arabic/Persian vocabulary layer', 'middle', 'Ls')
    s += footer('54', 'URDU', 'SINDHI', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 54c  GRAMMAR ───────────────────────────────────────────────────────
def plate54c():
    s = open_svg()
    s += t(240, 28, 'URDU', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & HONORIFICS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'URDU WORD ORDER: SOV')
    s += t(240, 68, 'Main aap ko pyaar karta hoon. "I you to love do am."', 'middle', 'L')
    s += t(240, 79, '"I love you." (SOV with postpositions)', 'middle', 'Ls')
    s += t(240, 90, 'Postpositions follow nouns: ghar mein "house in" = "in the house"', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'THREE-LEVEL HONORIFIC SYSTEM')
    s += t(240, 117, 'Aap: most formal/respectful "you" (verb in plural)', 'middle', 'L')
    s += t(240, 128, 'Tum: familiar "you" (informal but not intimate)', 'middle', 'L')
    s += t(240, 139, 'Tu: intimate "you" (close friends, children, prayer to God)', 'middle', 'L')
    s += t(240, 150, 'Verb forms, pronouns, honorifics all shift at each level', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'URDU GENDER & AGREEMENT')
    s += t(240, 177, 'Two genders: masculine / feminine', 'middle', 'L')
    s += t(240, 188, 'Verbs, adjectives, postpositions all agree with gender', 'middle', 'L')
    s += t(240, 199, 'larki (girl, FEM) \u2022 larka (boy, MASC)', 'middle', 'L')
    s += t(240, 210, 'larki gayi (girl went-FEM) \u2022 larka gaya (boy went-MASC)', 'middle', 'Ls')
    s += hr(218)
    s += sh(226, 'ERGATIVE IN PAST TENSE')
    s += t(240, 237, 'Past transitive: agent takes -ne; verb agrees with object', 'middle', 'L')
    s += t(240, 248, 'Main-ne kitaab parhi. "I-ERG book read-FEM." (book is feminine)', 'middle', 'L')
    s += t(240, 259, 'Split ergativity: present = nominative; past = ergative', 'middle', 'Ls')
    s += hr(267)
    # Divider
    s += sec_divider(274, 'SINDHI GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(299, 'SINDHI CASE SYSTEM')
    s += t(240, 310, 'Four cases: nominative \u2022 oblique \u2022 ablative \u2022 vocative', 'middle', 'L')
    s += t(240, 321, 'Agglutinative postpositions attach to oblique stem', 'middle', 'Ls')
    s += t(240, 332, 'Three genders: masculine / feminine / neuter (unlike Urdu 2!)', 'middle', 'L')
    s += hr(340)
    s += sh(348, 'SINDHI VERB SYSTEM')
    s += t(240, 359, 'SOV same as Urdu; postpositions same pattern', 'middle', 'L')
    s += t(240, 370, 'Sindhi also split ergative (past transitive uses oblique agent)', 'middle', 'L')
    s += t(240, 381, 'Causative: -aayanu suffix  \u2022  Passive: periphrastic construction', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'GRAMMATICAL PARALLELS')
    s += t(240, 408, 'Both: SOV  \u2022  postpositions  \u2022  split ergativity', 'middle', 'L')
    s += t(240, 419, 'Both: verb agrees with gender  \u2022  honorific pronouns', 'middle', 'L')
    s += t(240, 430, 'Urdu: 2 genders  \u2022  Sindhi: 3 genders (preserves Sanskrit neuter)', 'middle', 'Ls')
    s += t(240, 441, 'Both: descended from Sanskrit via Apabhramsha prakrits', 'middle', 'Ls')
    s += footer('54', 'URDU', 'SINDHI', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 54d  HISTORY ───────────────────────────────────────────────────────
def plate54d():
    s = open_svg()
    s += t(240, 28, 'URDU', 'middle', 'T')
    s += t(240, 40, 'HISTORY & PAKISTAN', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'URDU ORIGINS')
    s += t(240, 68, 'Urdu developed in Delhi Sultanate military camps (~1200 CE)', 'middle', 'L')
    s += t(240, 79, '"Urdu" from Turkic: "ordu" = army/camp; Zaban-e-Urdu = "army language"', 'middle', 'L')
    s += t(240, 90, 'Hindi-Urdu: same spoken base; diverged in script and vocabulary register', 'middle', 'Ls')
    s += t(240, 101, 'Mughal Empire (1526-1857): Persian official; Urdu literary language', 'middle', 'Ls')
    s += t(240, 112, 'Mir Taqi Mir, Mirza Ghalib: greatest Urdu poets; 18th-19th c.', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'PARTITION AND PAKISTAN (1947)')
    s += t(240, 139, '1947: Pakistan independence; Urdu chosen as sole national language', 'middle', 'L')
    s += t(240, 150, 'Only 7% of Pakistanis had Urdu as mother tongue at partition', 'middle', 'L')
    s += t(240, 161, '1952: Language Movement in East Pakistan (Bengali speakers protest)', 'middle', 'Ls')
    s += t(240, 172, 'Eventually led to Bangladesh independence (1971)', 'middle', 'Ls')
    s += t(240, 183, 'Today: ~170M Urdu speakers in South Asia and diaspora', 'middle', 'L')
    s += hr(191)
    # Divider
    s += sec_divider(198, 'SINDHI HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(223, 'SINDH AND THE INDUS CIVILIZATION')
    s += t(240, 234, 'Mohenjo-daro: largest city of Indus Valley Civilization (in Sindh)', 'middle', 'L')
    s += t(240, 245, '~3300-1300 BCE: Indus script used in Sindh (still undeciphered)', 'middle', 'Ls')
    s += t(240, 256, '711 CE: Muhammad bin Qasim conquers Sindh for the Umayyad Caliphate', 'middle', 'Ls')
    s += t(240, 267, 'First permanent Muslim presence in South Asia', 'middle', 'Ls')
    s += hr(275)
    s += sh(283, 'SINDHI UNDER BRITISH AND PAKISTAN')
    s += t(240, 294, '1843: British annexation of Sindh by Charles Napier', 'middle', 'L')
    s += t(240, 305, '1947: Sindh joins Pakistan; Hindu Sindhis flee to India', 'middle', 'L')
    s += t(240, 316, 'Pakistan: Urdu national language imposed over Sindhi in schools', 'middle', 'Ls')
    s += t(240, 327, 'Sindhi activists resist: G.M. Syed leads Sindhi nationalist movement', 'middle', 'Ls')
    s += hr(335)
    s += sh(343, 'URDU-SINDHI TENSION IN PAKISTAN')
    s += t(240, 354, 'Sindh province: Urdu-speaking muhajir (migrants) vs. native Sindhi', 'middle', 'L')
    s += t(240, 365, 'Karachi: majority Urdu-speaking muhajir city in Sindhi province', 'middle', 'L')
    s += t(240, 376, 'MQM (Muhajir party) vs. PPP (Sindhi-based party): ongoing tension', 'middle', 'Ls')
    s += t(240, 387, 'Sindhi language: official in Sindh province; Urdu: national official', 'middle', 'Ls')
    s += hr(395)
    s += sh(403, 'SISTER LANGUAGES, COMPETING IDENTITIES')
    s += t(240, 414, 'Both: Indo-Aryan, descended from same Sanskrit root', 'middle', 'Ls')
    s += t(240, 425, 'Both: use Perso-Arabic script (though different sizes)', 'middle', 'Ls')
    s += t(240, 436, 'Urdu: symbol of Pakistan\u2019s Muslim identity and nationhood', 'middle', 'Ls')
    s += t(240, 447, 'Sindhi: symbol of regional identity, pre-Islamic Indus heritage', 'middle', 'Ls')
    s += t(240, 458, 'Both within the same river-basin civilization', 'middle', 'L')
    s += footer('54', 'URDU', 'SINDHI', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate54a_urdu_sindhi_script_alt.svg', plate54a()),
                  ('plate54b_urdu_sindhi_phonology_alt.svg', plate54b()),
                  ('plate54c_urdu_sindhi_grammar_alt.svg', plate54c()),
                  ('plate54d_urdu_sindhi_history_alt.svg', plate54d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
