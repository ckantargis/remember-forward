# build_pashto_sindhi_alt.py  — Series 55 ALT  (Pashto + Sindhi)
# Secondary language: Sindhi (~33M speakers, Sindh province, Pakistan)
# Geographic basis: standard 500mi radius from Kandahar (31.6°N, 65.7°E)
# Quetta (Pakistan) to Karachi ~700km (~435mi) — Sindhi homeland within 500mi
# Pashto: Iranian branch · Sindhi: Indo-Aryan branch — crossing the great divide
# Both at the Indus crossroads; Sindh historically connected to Afghan/Pashtun areas
# Outputs: plate55a–55d_pashto_sindhi_*_alt.svg

from pathlib import Path

OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text { font-family: Georgia, serif; }\n'
        '  .T{font-size:11px;font-weight:bold;letter-spacing:1.5px}\n'
        '  .S{font-size:6.5px;letter-spacing:1.5px}\n'
        '  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}\n'
        '  .Hb{font-size:7px;font-weight:bold;letter-spacing:2px}\n'
        '  .L{font-size:7px} .Ls{font-size:6px} .Lx{font-size:5.5px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')

def close_svg(): return '</svg>\n'

def t(x, y, text, anchor='middle', cls='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.5):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y, label, cls='H'):
    return t(240, y, label, 'middle', cls)

def sec_divider(y, label):
    out  = hr(y, sw=1.5)
    out += f'<rect x="20" y="{y+3}" width="440" height="14" fill="black"/>\n'
    out += f'<text x="240" y="{y+13}" text-anchor="middle" class="Hb" fill="white">{esc(label)}</text>\n'
    out += hr(y+17, sw=0.3)
    return out

def footer(num, lang1, lang2, letter, desc):
    return (hr(625)
        + t(240, 620,
            f'PLATE {esc(num)}{esc(letter)} ALT \u00b7 {esc(lang1)} / {esc(lang2)}'
            f' \u00b7 {esc(desc.upper())} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG',
            'middle', 'M')
        + hr(633)
        + t(240, 648,
            'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.',
            'middle', 'Fb')
        + t(240, 663,
            'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET',
            'middle', 'F'))

# ─────────────────────────────────────────────────────────────────────────────
def build_55a_alt():
    svg = open_svg()
    svg += t(240, 32, 'PASHTO (\u067e\u069a\u062a\u0648) / SINDHI (\u0633\u0646\u068c\u064a)', 'middle', 'T')
    svg += t(240, 44, 'INDO-IRANIAN \u00b7 IRANIAN / INDO-ARYAN BRANCH \u00b7 INDUS CROSSROADS', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 55A ALT \u00b7 SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PASHTO: SCRIPT & SOUNDS \u2014')
    svg += t(240, 89, 'Script: modified Perso-Arabic (Nastaliq style), right-to-left', 'middle', 'Ls')
    svg += t(240, 100, '44 letters (Arabic 28 + 16 extra for Pashto sounds): \u0681 \u0685 \u0693 \u0696 \u0698 \u069a \u0693 \u069f \u06cd \u0626 \u0624', 'middle', 'Ls')
    svg += t(240, 111, 'Two main scripts: Kandahari Pashto (Pakistan) vs Kabuli (Afghanistan)', 'middle', 'Ls')
    svg += hr(117, sw=0.3)
    svg += sh(127, 'PASHTO DISTINCTIVE SOUNDS')
    svg += t(240, 138, 'Retroflex series: /\u0288 \u0256 \u0273 \u027d/ \u2014 tip of tongue curled back (shared with Sindhi!)', 'middle', 'Ls')
    svg += t(240, 149, 'Dental series: /t d n/ \u2014 tip of tongue at upper teeth', 'middle', 'Ls')
    svg += t(240, 160, 'Distinction: /t/ (dental) vs /\u0288/ (retroflex) = different meaning', 'middle', 'Ls')
    svg += t(240, 171, 'Also: /\u0283/ /\u0292/ /x/ /\u0263/ /q/ \u2014 uvular and velar sounds from Arabic influence', 'middle', 'Ls')
    svg += hr(177, sw=0.3)
    svg += sh(187, 'PASHTO VOWELS')
    svg += t(240, 198, '7 vowels: /a \u0101 e i o u \u0259/ (schwa in unstressed position)', 'middle', 'Ls')
    svg += t(240, 209, 'Vowel length phonemic in classical/literary Pashto; varies by dialect', 'middle', 'Ls')
    svg += hr(215, sw=0.3)
    svg += sh(225, 'GRAMMATICAL GENDER: TWO CLASSES')
    svg += t(240, 236, 'Masculine: ends in consonant or -\u0259 \u00b7 Feminine: ends in -a or -\u0259', 'middle', 'Ls')
    svg += t(240, 247, 'soor (masc. red) vs soora (fem. red) \u2014 adjective agrees with noun', 'middle', 'Ls')
    svg += t(240, 258, 'Historical: Pashto had 4 genders (masc/fem proximate/distal) \u2014 now merged to 2', 'middle', 'Ls')
    svg += hr(264, sw=0.3)
    svg += sh(274, 'PASHTO SAMPLE WORDS')
    svg += t(240, 285, '\u0633\u0644\u0627\u0645 (salam) = hello \u00b7 \u0627\u0648 (ob) = water \u00b7 \u062e\u062f\u0627\u06cc \u062f\u06d0 (khudaye de) = thank you (God-given)', 'middle', 'Ls')
    svg += t(240, 296, '\u067e\u069a\u062a\u0648\u0646 (pashtun) = Pashtun person \u00b7 \u067e\u069a\u062a\u0648 (pashto) = the language', 'middle', 'Ls')
    svg += hr(302, sw=0.3)
    svg += sh(312, 'PASHTUNWALI: CODE OF HONOR ENCODED IN LANGUAGE')
    svg += t(240, 323, 'Melmastia (hospitality) \u00b7 Nanawatai (asylum) \u00b7 Badal (justice/revenge)', 'middle', 'Ls')
    svg += t(240, 334, 'Namus (honor) \u00b7 Tureh (courage) \u2014 vocabulary of the honor code', 'middle', 'Ls')

    svg += sec_divider(346, 'SINDHI (\u0633\u0646\u068c\u064a) \u2014 INDO-ARYAN \u00b7 SINDH, PAKISTAN \u00b7 ~500MI')

    svg += sh(371, '\u2014 SINDHI: SCRIPT & DISTINCTIVE FEATURES \u2014')
    svg += t(240, 382, 'Script: Perso-Arabic with Sindhi additions: 52 letters (most in any Arabic-based script)', 'middle', 'Ls')
    svg += t(240, 393, 'Also written in Devanagari by Hindu Sindhi diaspora (India, globally)', 'middle', 'Ls')
    svg += t(240, 404, 'Direction: right-to-left (like Pashto) \u00b7 Nastaliq style standard', 'middle', 'Ls')
    svg += hr(410, sw=0.3)
    svg += sh(420, 'SINDHI IMPLOSIVE CONSONANTS: UNIQUE FEATURE')
    svg += t(240, 431, 'Sindhi is famous for 4 phonemic implosive consonants:', 'middle', 'Ls')
    svg += t(100, 442, 'IMPLOSIVE', 'middle', 'Lx')
    svg += t(240, 442, 'IPA', 'middle', 'Lx')
    svg += t(390, 442, 'SINDHI LETTER', 'middle', 'Lx')
    svg += hr(446, sw=0.3)
    svg += t(100, 455, 'Bilabial', 'middle', 'Ls')
    svg += t(240, 455, '/\u0253/ (b-implosive)', 'middle', 'Ls')
    svg += t(390, 455, '\u0628\u0332', 'middle', 'Ls')
    svg += t(100, 465, 'Alveolar', 'middle', 'Ls')
    svg += t(240, 465, '/\u0257/ (d-implosive)', 'middle', 'Ls')
    svg += t(390, 465, '\u062f\u0332', 'middle', 'Ls')
    svg += t(100, 475, 'Palatal', 'middle', 'Ls')
    svg += t(240, 475, '/\u0284/ (j-implosive)', 'middle', 'Ls')
    svg += t(390, 475, '\u062c\u0332', 'middle', 'Ls')
    svg += t(100, 485, 'Velar', 'middle', 'Ls')
    svg += t(240, 485, '/\u0260/ (g-implosive)', 'middle', 'Ls')
    svg += t(390, 485, '\u06af\u0332', 'middle', 'Ls')
    svg += hr(490, sw=0.3)
    svg += sh(500, 'WHAT IS AN IMPLOSIVE?')
    svg += t(240, 511, 'Regular stops: air pushed OUT (plosive/explosive)', 'middle', 'Ls')
    svg += t(240, 522, 'Implosives: glottis closes while tongue creates stop, airflow reversed inward', 'middle', 'Ls')
    svg += t(240, 533, 'A "click-like" effect \u2014 Sindhi is one of few Indo-Aryan languages with implosives', 'middle', 'Ls')
    svg += hr(539, sw=0.3)
    svg += sh(549, 'RETROFLEX CONSONANTS (SHARED WITH PASHTO)')
    svg += t(240, 560, 'Sindhi has the full retroflex series /\u0288 \u0256 \u0273 \u027d/ like Pashto', 'middle', 'Ls')
    svg += t(240, 571, 'This shared feature comes from ancient Indus Valley substratum', 'middle', 'Ls')
    svg += hr(577, sw=0.3)
    svg += sh(587, 'SAMPLE WORDS (SINDHI)')
    svg += t(240, 598, '\u0622\u0633\u0627\u0646\u06cc (asani) = ease/peace (greeting) \u00b7 \u067e\u0627\u06a4 (paun) = water', 'middle', 'Ls')
    svg += t(240, 609, '\u0645\u06be\u0646\u062c\u0648 (mhanju) = mine/my \u00b7 \u062a\u0648\u06be\u0646\u062c\u0648 (tuhnju) = yours', 'middle', 'Ls')

    svg += footer(55, 'PASHTO', 'SINDHI', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_55b_alt():
    svg = open_svg()
    svg += t(240, 32, 'PASHTO (\u067e\u069a\u062a\u0648) / SINDHI (\u0633\u0646\u068c\u064a)', 'middle', 'T')
    svg += t(240, 44, 'INDO-IRANIAN \u00b7 PHONOLOGY: CROSSING THE IRANIAN/INDO-ARYAN DIVIDE', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 55B ALT \u00b7 PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PASHTO PHONOLOGY \u2014')
    svg += sh(88, 'FULL CONSONANT INVENTORY')
    svg += t(240, 99, 'Stops: /p b t d \u0288 \u0256 k g q/ \u2014 bilabial + dental + retroflex + velar + uvular', 'middle', 'Ls')
    svg += t(240, 110, 'Affricates: /ts dz t\u0283 d\u0292/ \u2014 simple + palatal series', 'middle', 'Ls')
    svg += t(240, 121, 'Fricatives: /f s z \u0283 \u0292 x \u0263 h/ \u2014 includes uvular fricatives from Arabic', 'middle', 'Ls')
    svg += t(240, 132, 'Nasals: /m n \u0273/ \u2014 bilabial + alveolar + retroflex', 'middle', 'Ls')
    svg += t(240, 143, 'Rhotic: /r \u027d/ \u2014 alveolar trill + retroflex flap', 'middle', 'Ls')
    svg += hr(149, sw=0.3)
    svg += sh(159, 'PASHTO DIALECT COMPARISON')
    svg += t(100, 170, 'FEATURE', 'middle', 'Lx')
    svg += t(240, 170, 'KANDAHARI (S)', 'middle', 'Lx')
    svg += t(390, 170, 'KABULI (N)', 'middle', 'Lx')
    svg += hr(174, sw=0.3)
    svg += t(100, 183, '/\u0283/ sound', 'middle', 'Ls')
    svg += t(240, 183, '\u0293 (\u0292 with subscript)', 'middle', 'Ls')
    svg += t(390, 183, '\u0283 (standard sh)', 'middle', 'Ls')
    svg += t(100, 193, '/\u0292/ sound', 'middle', 'Ls')
    svg += t(240, 193, '\u026c (voiceless l)', 'middle', 'Ls')
    svg += t(390, 193, '\u0292 (standard zh)', 'middle', 'Ls')
    svg += hr(198, sw=0.3)
    svg += sh(208, 'ERGATIVE CONSTRUCTION IN PASHTO')
    svg += t(240, 219, 'Past transitive verbs are ERGATIVE: subject takes oblique case, verb agrees with object', 'middle', 'Ls')
    svg += t(240, 230, 'Ahmad kitab okod = Ahmad book read-MASC: "Ahmad read the book" (book is agent)', 'middle', 'Ls')
    svg += t(240, 241, 'This ergativity is Iranian, not Indic \u2014 marks Pashto as Iranian', 'middle', 'Ls')
    svg += hr(247, sw=0.3)
    svg += sh(257, 'PASHTO NUMBERS')
    svg += t(240, 268, 'yaw (1) \u00b7 dwa (2) \u00b7 dre (3) \u00b7 tsalor (4) \u00b7 pinja (5)', 'middle', 'Ls')
    svg += t(240, 279, 'shpag (6) \u00b7 owa (7) \u00b7 ata (8) \u00b7 nah (9) \u00b7 las (10)', 'middle', 'Ls')
    svg += hr(285, sw=0.3)
    svg += sh(295, 'SHARED INDO-IRANIAN FEATURES')
    svg += t(240, 306, 'Both Pashto and Sindhi: SOV \u00b7 postpositions \u00b7 retroflex consonants', 'middle', 'Ls')
    svg += t(240, 317, 'Both Indo-Iranian: shared ancestry in Proto-Indo-Iranian ~4000 BCE', 'middle', 'Ls')
    svg += t(240, 328, 'Divided ~2000 BCE: Iranian branch west \u2192 Pashto; Indic branch east \u2192 Sindhi', 'middle', 'Ls')

    svg += sec_divider(340, 'SINDHI (\u0633\u0646\u068c\u064a) \u2014 PHONOLOGY')

    svg += sh(365, '\u2014 SINDHI PHONOLOGY IN DEPTH \u2014')
    svg += sh(376, 'FOUR-WAY STOP CONTRAST (UNIQUE TYPOLOGICALLY)')
    svg += t(240, 387, 'At each point of articulation, Sindhi has 4 stops:', 'middle', 'Ls')
    svg += t(100, 398, 'TYPE', 'middle', 'Lx')
    svg += t(220, 398, 'BILABIAL', 'middle', 'Lx')
    svg += t(350, 398, 'ALVEOLAR', 'middle', 'Lx')
    svg += hr(402, sw=0.3)
    svg += t(100, 411, 'Voiceless', 'middle', 'Ls')
    svg += t(220, 411, '/p/', 'middle', 'Ls')
    svg += t(350, 411, '/t/', 'middle', 'Ls')
    svg += t(100, 421, 'Voiced', 'middle', 'Ls')
    svg += t(220, 421, '/b/', 'middle', 'Ls')
    svg += t(350, 421, '/d/', 'middle', 'Ls')
    svg += t(100, 431, 'Aspirated', 'middle', 'Ls')
    svg += t(220, 431, '/p\u02b0/', 'middle', 'Ls')
    svg += t(350, 431, '/t\u02b0/', 'middle', 'Ls')
    svg += t(100, 441, 'Implosive', 'middle', 'Ls')
    svg += t(220, 441, '/\u0253/', 'middle', 'Ls')
    svg += t(350, 441, '/\u0257/', 'middle', 'Ls')
    svg += t(240, 451, '4-way contrast at bilabial + alveolar + retroflex + velar = very complex system', 'middle', 'Ls')
    svg += hr(457, sw=0.3)
    svg += sh(467, 'TONES? NOT QUITE \u2014 REGISTER DISTINCTIONS')
    svg += t(240, 478, 'Sindhi does not have lexical tone, but vowel + laryngeal distinctions', 'middle', 'Ls')
    svg += t(240, 489, 'Some dialects: breathy voice on vowels functions tone-like; phonemically active', 'middle', 'Ls')
    svg += hr(495, sw=0.3)
    svg += sh(505, 'SINDHI NUMBERS')
    svg += t(240, 516, 'ha\u1e0bu (1) \u00b7 \u0253a (2) \u00b7 tr\u012b (3) \u00b7 c\u0101ri (4) \u00b7 panja (5)', 'middle', 'Ls')
    svg += t(240, 527, 'cha (6) \u00b7 sata (7) \u00b7 a\u1e6dha (8) \u00b7 nava (9) \u00b7 daha (10)', 'middle', 'Ls')
    svg += hr(533, sw=0.3)
    svg += sh(543, 'PHONOLOGICAL COMPARISON')
    svg += t(100, 554, 'FEATURE', 'middle', 'Lx')
    svg += t(240, 554, 'PASHTO', 'middle', 'Lx')
    svg += t(390, 554, 'SINDHI', 'middle', 'Lx')
    svg += hr(558, sw=0.3)
    svg += t(100, 567, 'Retroflex stops', 'middle', 'Ls')
    svg += t(240, 567, 'YES', 'middle', 'Ls')
    svg += t(390, 567, 'YES', 'middle', 'Ls')
    svg += t(100, 577, 'Implosives', 'middle', 'Ls')
    svg += t(240, 577, 'NO', 'middle', 'Ls')
    svg += t(390, 577, 'YES (4 phonemes)', 'middle', 'Ls')
    svg += t(100, 587, 'Ergativity', 'middle', 'Ls')
    svg += t(240, 587, 'YES (past trans.)', 'middle', 'Ls')
    svg += t(390, 587, 'PARTIAL', 'middle', 'Ls')
    svg += t(100, 597, 'Uvular /q/', 'middle', 'Ls')
    svg += t(240, 597, 'YES', 'middle', 'Ls')
    svg += t(390, 597, 'in loanwords', 'middle', 'Ls')

    svg += footer(55, 'PASHTO', 'SINDHI', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_55c_alt():
    svg = open_svg()
    svg += t(240, 32, 'PASHTO (\u067e\u069a\u062a\u0648) / SINDHI (\u0633\u0646\u068c\u064a)', 'middle', 'T')
    svg += t(240, 44, 'INDO-IRANIAN \u00b7 GRAMMAR & CORE VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 55C ALT \u00b7 GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PASHTO GRAMMAR \u2014')
    svg += t(240, 88, 'SOV word order \u00b7 split ergative (present: nominative; past transitive: ergative)', 'middle', 'Ls')
    svg += t(240, 99, 'Two genders (masculine/feminine) \u00b7 adjectives agree with nouns in gender and case', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'PASHTO CASE SYSTEM (4 CASES)')
    svg += t(100, 126, 'CASE', 'middle', 'Lx')
    svg += t(240, 126, 'FUNCTION', 'middle', 'Lx')
    svg += t(390, 126, 'EXAMPLE (soor = red, masc.)', 'middle', 'Lx')
    svg += hr(130, sw=0.3)
    svg += t(100, 139, 'Nominative', 'middle', 'Ls')
    svg += t(240, 139, 'Subject of present verb', 'middle', 'Ls')
    svg += t(390, 139, 'soor (red)', 'middle', 'Ls')
    svg += t(100, 149, 'Oblique', 'middle', 'Ls')
    svg += t(240, 149, 'After postpositions + past agent', 'middle', 'Ls')
    svg += t(390, 149, 'soori (red-OBL)', 'middle', 'Ls')
    svg += t(100, 159, 'Vocative', 'middle', 'Ls')
    svg += t(240, 159, 'Direct address', 'middle', 'Ls')
    svg += t(390, 159, 'soora! (O red one!)', 'middle', 'Ls')
    svg += t(100, 169, 'Feminine', 'middle', 'Ls')
    svg += t(240, 169, 'Feminine agreement', 'middle', 'Ls')
    svg += t(390, 169, 'soora (red, fem.)', 'middle', 'Ls')
    svg += hr(174, sw=0.3)
    svg += sh(184, 'PASHTO CORE VOCABULARY')
    svg += t(100, 195, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 195, 'PASHTO', 'middle', 'Lx')
    svg += t(390, 195, 'ROMANIZATION', 'middle', 'Lx')
    svg += hr(199, sw=0.3)
    svg += t(100, 208, 'I', 'middle', 'Ls')
    svg += t(240, 208, '\u0632\u0647', 'middle', 'Ls')
    svg += t(390, 208, 'za', 'middle', 'Ls')
    svg += t(100, 218, 'you', 'middle', 'Ls')
    svg += t(240, 218, '\u062a\u0647', 'middle', 'Ls')
    svg += t(390, 218, 'ta', 'middle', 'Ls')
    svg += t(100, 228, 'water', 'middle', 'Ls')
    svg += t(240, 228, '\u0627\u0648\u0628\u0647', 'middle', 'Ls')
    svg += t(390, 228, 'oba', 'middle', 'Ls')
    svg += t(100, 238, 'eat', 'middle', 'Ls')
    svg += t(240, 238, '\u062e\u0648\u0631\u0644', 'middle', 'Ls')
    svg += t(390, 238, 'khorl', 'middle', 'Ls')
    svg += t(100, 248, 'come', 'middle', 'Ls')
    svg += t(240, 248, '\u0631\u0627\u062a\u0644', 'middle', 'Ls')
    svg += t(390, 248, 'ratl', 'middle', 'Ls')
    svg += t(100, 258, 'good', 'middle', 'Ls')
    svg += t(240, 258, '\u063a\u0648\u0631', 'middle', 'Ls')
    svg += t(390, 258, 'ghor', 'middle', 'Ls')

    svg += sec_divider(270, 'SINDHI (\u0633\u0646\u068c\u064a) \u2014 GRAMMAR & VOCABULARY')

    svg += sh(294, '\u2014 SINDHI GRAMMAR \u2014')
    svg += t(240, 305, 'SOV word order \u00b7 postpositions \u00b7 2 genders (masc/fem) \u00b7 3 cases', 'middle', 'Ls')
    svg += t(240, 316, 'Verbs agree with subject in person, number, gender', 'middle', 'Ls')
    svg += hr(322, sw=0.3)
    svg += sh(332, 'SINDHI CASE SYSTEM')
    svg += t(100, 343, 'CASE', 'middle', 'Lx')
    svg += t(240, 343, 'USE', 'middle', 'Lx')
    svg += t(390, 343, 'SUFFIX (MASC. SG.)', 'middle', 'Lx')
    svg += hr(347, sw=0.3)
    svg += t(100, 356, 'Nominative', 'middle', 'Ls')
    svg += t(240, 356, 'Subject (present)', 'middle', 'Ls')
    svg += t(390, 356, '(zero)', 'middle', 'Ls')
    svg += t(100, 366, 'Oblique', 'middle', 'Ls')
    svg += t(240, 366, 'After postpositions', 'middle', 'Ls')
    svg += t(390, 366, '-a', 'middle', 'Ls')
    svg += t(100, 376, 'Vocative', 'middle', 'Ls')
    svg += t(240, 376, 'Direct address', 'middle', 'Ls')
    svg += t(390, 376, '-a (same as oblique)', 'middle', 'Ls')
    svg += hr(381, sw=0.3)
    svg += sh(391, 'SINDHI CORE VOCABULARY')
    svg += t(100, 402, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 402, 'SINDHI', 'middle', 'Lx')
    svg += t(390, 402, 'PASHTO LINK?', 'middle', 'Lx')
    svg += hr(406, sw=0.3)
    svg += t(100, 415, 'I', 'middle', 'Ls')
    svg += t(240, 415, '\u0645\u0627\u06cd / \u06be\u0627\u0646 (maa / hhaan)', 'middle', 'Ls')
    svg += t(390, 415, 'cf. Pashto za', 'middle', 'Ls')
    svg += t(100, 425, 'you', 'middle', 'Ls')
    svg += t(240, 425, '\u062a\u0648\u06be\u06cc\u06ba (tuhhin)', 'middle', 'Ls')
    svg += t(390, 425, 'cf. Pashto ta', 'middle', 'Ls')
    svg += t(100, 435, 'water', 'middle', 'Ls')
    svg += t(240, 435, '\u067e\u0627\u06a4 (paun)', 'middle', 'Ls')
    svg += t(390, 435, 'cf. Pashto oba (differ)', 'middle', 'Ls')
    svg += t(100, 445, 'eat', 'middle', 'Ls')
    svg += t(240, 445, '\u06a9\u06be\u0627\u0626\u06ba (khaan)', 'middle', 'Ls')
    svg += t(390, 445, 'both from PIIran *khaw-', 'middle', 'Ls')
    svg += t(100, 455, 'good', 'middle', 'Ls')
    svg += t(240, 455, '\u0633\u0631\u06be\u0648 (sarhu)', 'middle', 'Ls')
    svg += t(390, 455, 'cf. Pashto ghor (differ)', 'middle', 'Ls')
    svg += hr(460, sw=0.3)
    svg += sh(470, 'SURVIVAL PHRASES')
    svg += t(240, 481, 'Pa khair ose! = Farewell! (Pashto) \u00b7 Khuda hafiz = God protect you (both)', 'middle', 'Ls')
    svg += t(240, 492, 'Cha hal ahyan? = How are you? (Sindhi)', 'middle', 'Ls')
    svg += t(240, 503, 'Pani kite ahe? = Where is the water? (Sindhi: pani=water kite=where ahe=is)', 'middle', 'Ls')
    svg += t(240, 514, 'Ob charta dey? = Where is water? (Pashto: ob=water charta=where dey=is)', 'middle', 'Ls')
    svg += hr(520, sw=0.3)
    svg += sh(530, 'GRAMMATICAL PARALLEL: POSTPOSITIONS')
    svg += t(240, 541, 'Both: SOV \u00b7 postpositions follow noun \u00b7 verb final in clause', 'middle', 'Ls')
    svg += t(240, 552, 'Pashto: pa kor ke = in-house-LOC: "in the house" (pa...ke = locative frame)', 'middle', 'Ls')
    svg += t(240, 563, 'Sindhi: ghar me = house in: "in the house" (me = locative postposition)', 'middle', 'Ls')

    svg += footer(55, 'PASHTO', 'SINDHI', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_55d_alt():
    svg = open_svg()
    svg += t(240, 32, 'PASHTO (\u067e\u069a\u062a\u0648) / SINDHI (\u0633\u0646\u068c\u064a)', 'middle', 'T')
    svg += t(240, 44, 'INDO-IRANIAN \u00b7 HISTORY & LEGACY AT THE INDUS CROSSROADS', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 55D ALT \u00b7 HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PASHTO: HISTORY & PASHTUN IDENTITY \u2014')
    svg += sh(88, 'ANCIENT ROOTS: AVESTAN COUSINS')
    svg += t(240, 99, 'Pashto: member of Eastern Iranian family; related to Avestan (sacred Zoroastrian)', 'middle', 'Ls')
    svg += t(240, 110, 'First written attestation: poems of Amir Kror Suri (~8th c. CE)', 'middle', 'Ls')
    svg += t(240, 121, 'Khushal Khan Khattak (1613\u20131689): warrior-poet; golden age of Pashto literature', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'PASHTUNWALI: THE LIVING CODE')
    svg += t(240, 148, 'Pashtunwali: oral customary law predating Islam in the region', 'middle', 'Ls')
    svg += t(240, 159, 'Melmastia (hospitality): obligation to shelter any guest, even an enemy', 'middle', 'Ls')
    svg += t(240, 170, 'Nanawatai (asylum): even an enemy who enters and seeks protection must be sheltered', 'middle', 'Ls')
    svg += t(240, 181, 'Badal (justice): redress of wrongs \u2014 not "revenge" but restoration of balance', 'middle', 'Ls')
    svg += hr(187, sw=0.3)
    svg += sh(197, 'CROSSROADS OF EMPIRE')
    svg += t(240, 208, 'Alexander the Great marched through Pashto-speaking territory ~327 BCE', 'middle', 'Ls')
    svg += t(240, 219, 'Mughal Empire (Babur was Pashtun): Pashto and Persian co-existed at court', 'middle', 'Ls')
    svg += t(240, 230, 'British "Great Game": Pashto speakers at center of Anglo-Russian competition', 'middle', 'Ls')
    svg += t(240, 241, 'Today: ~60M speakers in Afghanistan and Pakistan \u00b7 one of world\'s fastest growing', 'middle', 'Ls')
    svg += hr(247, sw=0.3)
    svg += sh(257, 'SURVIVAL PHRASE (PASHTO)')
    svg += t(240, 268, 'Da wakhto la makhkhe da hagho keso pa laar jowr sho chi makhke rawan wu.', 'middle', 'Lx')
    svg += t(240, 280, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 291, '(makhke = forward/ahead; rawan = going; wu = were)', 'middle', 'Ls')

    svg += sec_divider(303, 'SINDHI (\u0633\u0646\u068c\u064a) \u2014 HISTORY & CULTURAL LEGACY')

    svg += sh(328, '\u2014 SINDHI: CRADLE OF CIVILIZATION \u2014')
    svg += sh(339, 'INDUS VALLEY CIVILIZATION (3300\u20131300 BCE)')
    svg += t(240, 350, 'Mohenjo-daro and Harappa: within the Sindhi-speaking homeland of today', 'middle', 'Ls')
    svg += t(240, 361, 'Most sophisticated urban civilization of the ancient world: plumbing, grid streets', 'middle', 'Ls')
    svg += t(240, 372, 'Indus script: still undeciphered \u2014 one of the great puzzles of linguistics', 'middle', 'Ls')
    svg += hr(378, sw=0.3)
    svg += sh(388, 'ARAB CONQUEST & SUFI TRANSFORMATION (711 CE)')
    svg += t(240, 399, 'Muhammad bin Qasim conquered Sindh 711 CE \u2014 first permanent Arab territory in S. Asia', 'middle', 'Ls')
    svg += t(240, 410, 'Sindh became a major center of Islamic scholarship and Sufi mysticism', 'middle', 'Ls')
    svg += t(240, 421, 'Shah Abdul Latif Bhittai (1689\u20131752): greatest Sindhi poet; Shah Jo Risalo (his verse)', 'middle', 'Ls')
    svg += t(240, 432, 'Risalo: 30 sur (chapters) of mystical verse \u2014 still sung at shrines today', 'middle', 'Ls')
    svg += hr(438, sw=0.3)
    svg += sh(448, 'THE SINDHI PARTITION (1947)')
    svg += t(240, 459, '1947: India\u2013Pakistan partition; Sindh went to Pakistan; Hindu Sindhis fled to India', 'middle', 'Ls')
    svg += t(240, 470, 'Sindhi Hindus: ~3M in India, diaspora in Singapore, Hong Kong, UK, USA', 'middle', 'Ls')
    svg += t(240, 481, 'Unique: Sindhi is one of India\'s 22 official languages but has no Indian state', 'middle', 'Ls')
    svg += t(240, 492, 'In India: written in Devanagari \u00b7 in Pakistan: Perso-Arabic \u2014 same language, two scripts', 'middle', 'Ls')
    svg += hr(498, sw=0.3)
    svg += sh(508, 'SINDHI MUSICAL TRADITION')
    svg += t(240, 519, 'Sindhi folk music: kafis (devotional poems), waai, sohar (lullabies)', 'middle', 'Ls')
    svg += t(240, 530, 'Allan Faqir (1932\u20132000): Sufi singer; "Voice of Sindh"; UNESCO recognition', 'middle', 'Ls')
    svg += hr(536, sw=0.3)
    svg += sh(546, 'SINDHI AT THE CROSSROADS')
    svg += t(240, 557, 'Sindhi vocabulary: Sanskrit roots + Persian/Arabic loans + Sindhi-original words', 'middle', 'Ls')
    svg += t(240, 568, 'Sits between Iranian Pashto and Indo-Aryan Sanskrit \u2014 the living Indo-Iranian border', 'middle', 'Ls')
    svg += hr(574, sw=0.3)
    svg += sh(584, 'SURVIVAL PHRASE (SINDHI)')
    svg += t(240, 595, 'Hii tokhaan laai bnayo viyo ahe, muft, unhan maanshen jinhan aaindaren yaad rakhyo.', 'middle', 'Lx')
    svg += t(240, 607, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 618, '(aaindare = future/ahead; yaad rakhyo = remembered)', 'middle', 'Ls')

    svg += footer(55, 'PASHTO', 'SINDHI', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate55a_pashto_sindhi_script_alt.svg',    build_55a_alt),
        ('plate55b_pashto_sindhi_phonology_alt.svg',  build_55b_alt),
        ('plate55c_pashto_sindhi_grammar_alt.svg',    build_55c_alt),
        ('plate55d_pashto_sindhi_history_alt.svg',    build_55d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
