#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Hindi / Rajasthani alt plate series 25A–25D for Remember Forward.
Secondary language: Rajasthani (राजस्थानी) — spoken across Rajasthan state
and parts of Gujarat, Punjab, Haryana. ~70-80 million speakers.
Geographic basis: Rajasthan directly borders the Hindi-speaking heartland (UP, MP, Delhi);
Jaipur is ~270km from Delhi. Rajasthani is the largest regional language within
500mi of New Delhi, the anchor city for the Hindi series.
Rajasthani: Indo-Aryan, closely related to Hindi/Braj Bhasha.
Not officially recognized as separate language in India's constitution,
but strongly distinct in phonology (breathy voiced consonants, retroflex, tones in some dialects).
"""
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
        '  .Ld{font-size:13px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')

def close_svg(): return '</svg>\n'
def t(x, y, s, a='middle', c='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'
def hr(y, x1=20, x2=460, sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y, txt, c='H'):
    return t(240, y, f'\u2014 {txt} \u2014', 'middle', c)
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


# ─── PLATE 25A ALT — SCRIPT ───────────────────────────────────────────────────

def build_25a_alt():
    g = open_svg()
    g += t(240, 30, 'HINDI + RAJASTHANI \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 25A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HINDI \u2014 DEVANAGARI SCRIPT \u00b7 AN ABUGIDA')
    g += t(240, 73, 'Devanagari: abugida script. Each consonant carries inherent /a/ vowel. Diacritics add other vowels.', 'middle', 'Ls')
    g += t(240, 82, '47 primary characters (14 vowels, 33 consonants). Written left to right with top \u201cheadstroke\u201d line.', 'middle', 'Lx')
    g += t(240, 91, 'Used for Sanskrit, Hindi, Marathi, Nepali, Maithili, and other South Asian languages.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'DEVANAGARI VOWELS \u2014 14 INDEPENDENT FORMS')
    vowels = [
        ('\u0905','a'), ('\u0906','\u0101'), ('\u0907','i'), ('\u0908','\u012b'),
        ('\u0909','u'), ('\u090a','\u016b'), ('\u090b','r\u0325'), ('\u090f','e'),
        ('\u0910','ai'), ('\u0913','o'), ('\u0914','au'), ('\u0902','M (anusvara)'),
        ('\u0903','H (visarga)'), ('\u0901','\u1e7d (chandrabindu)'),
    ]
    for i, (ch, name) in enumerate(vowels):
        col = i % 4; row = i // 4
        x = 55 + col * 105; y = 117 + row * 14
        g += t(x, y, ch, 'middle', 'Ld')
        g += t(x, y + 9, name, 'middle', 'Lx')
    g += hr(167)

    g += sh(175, 'DEVANAGARI CONSONANTS \u2014 5 SERIES + OTHERS')
    g += t(240, 185, 'Sanskrit-derived 5\u00d75 grid: velar/palatal/retroflex/dental/labial \u00d7 vl/asp/vd/asp-vd/nasal.', 'middle', 'Lx')
    cons_rows = [
        '\u0915 \u0916 \u0917 \u0918 \u0919  (ka kha ga gha \u1e45a \u2014 velars)',
        '\u091a \u091b \u091c \u091d \u091e  (ca cha ja jha \u00f1a \u2014 palatals)',
        '\u091f \u0920 \u0921 \u0922 \u0923  (\u1e6da \u1e6dha \u1e0da \u1e0dha \u1e47a \u2014 retroflexes)',
        '\u0924 \u0925 \u0926 \u0927 \u0928  (ta tha da dha na \u2014 dentals)',
        '\u092a \u092b \u092c \u092d \u092e  (pa pha ba bha ma \u2014 labials)',
        '\u092f \u0930 \u0932 \u0935 \u0936 \u0937 \u0938 \u0939  (ya ra la va sha \u1e63a sa ha)',
    ]
    for i, row in enumerate(cons_rows):
        g += t(240, 195 + i * 11, row, 'middle', 'Ld' if i < 5 else 'Ls')
    g += hr(265)

    g += sh(273, 'VOWEL MATRAS \u2014 CONSONANT-ATTACHED FORMS')
    g += t(240, 283, 'When vowels follow consonants, they use matra (diacritic) forms: \u0915 + \u093e = \u0915\u093e (kaa)', 'middle', 'Ls')
    matras = [('\u093e','\u0101'),('\u093f','i'),('\u0940','\u012b'),('\u0941','u'),('\u0942','\u016b'),('\u0947','e'),('\u0948','ai'),('\u094b','o'),('\u094c','au')]
    for i, (m, v) in enumerate(matras):
        x = 50 + i * 48
        g += t(x, 295, f'\u0915{m}', 'middle', 'Ld')
        g += t(x, 305, f'k{v}', 'middle', 'Lx')

    g += sec_divider(315, 'SECONDARY \u2014 RAJASTHANI (\u0930\u093e\u091c\u0938\u094d\u0925\u093e\u0928\u0940) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(341, 'RAJASTHANI \u2014 DEVANAGARI + MAHAJANI SCRIPTS')
    g += t(240, 351, 'Rajasthani is primarily written in Devanagari (same as Hindi). Fully mutually intelligible in writing.', 'middle', 'Ls')
    g += t(240, 360, 'Historical script: Mahajani \u2014 a merchant script used for trade records in Rajasthan/Marwar (now rare).', 'middle', 'Lx')
    g += t(240, 369, 'Also written in Modi script (Maharashtra/Rajasthan), Kaithi, and Arabic-derived scripts by Muslim communities.', 'middle', 'Lx')
    g += hr(377)

    g += sh(385, 'RAJASTHANI SAMPLE \u2014 DEVANAGARI')
    raj_samples = [
        ('\u0930\u093e\u091c\u0938\u094d\u0925\u093e\u0928', 'Rajasthan', 'Land of Kings (r\u0101j + sth\u0101n)'),
        ('\u092a\u093e\u0923\u0940', 'pa\u1e47\u012b', 'water (Hindi: paani)'),
        ('\u0906\u0917', 'aag', 'fire (Hindi: aag \u2014 same)'),
        ('\u0927\u0930\u0924\u0940', 'dharati', 'earth (Hindi: dharti)'),
        ('\u092e\u093e\u0928\u0916\u094b', 'm\u0101nakho', 'person (Hindi: insaan/\u0101dm\u012b)'),
    ]
    for i, (deva, roman, note) in enumerate(raj_samples):
        y = 395 + i * 10
        g += t(60, y, deva, 'middle', 'Ld')
        g += t(145, y, roman, 'middle', 'Ls')
        g += t(340, y, note, 'middle', 'Lx')
    g += hr(452)

    g += sh(460, 'SCRIPT BRIDGE \u2014 SHARED DEVANAGARI, DISTINCT LANGUAGE')
    g += t(240, 470, 'Both Hindi and Rajasthani use Devanagari. A Rajasthani speaker can read Hindi script and vice versa.', 'middle', 'Ls')
    g += t(240, 479, 'Distinction lies in phonology (breathy vowels, tones in Marwari dialect), vocabulary (Rajput/Persian blend).', 'middle', 'Lx')
    g += t(240, 488, 'Rajasthani has no official status in India \u2014 classified as a Hindi dialect officially, but linguists count it separately.', 'middle', 'Lx')

    g += footer('25', 'Hindi', 'Rajasthani', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 25B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_25b_alt():
    g = open_svg()
    g += t(240, 30, 'HINDI + RAJASTHANI \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 25B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HINDI PHONOLOGY \u2014 CONSONANT SYSTEM')
    g += t(240, 73, 'Hindi has one of the richest consonant systems of any major language: 5 place \u00d7 4 manner distinctions.', 'middle', 'Ls')
    g += t(240, 82, 'Contrast: voiceless / aspirated / voiced / voiced-aspirated (breathy) across bilabial, alveolar, retroflex, palatal, velar.', 'middle', 'Lx')
    g += t(240, 91, 'Retroflex consonants (\u1e6d \u1e6dh \u1e0d \u1e0dh \u1e47): tongue tip curled back. Absent from most European languages.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'HINDI \u2014 BREATHY/MURMURED VOICED CONSONANTS')
    g += t(240, 117, 'Breathy voice (murmur): b\u02b0 d\u02b0 \u1e0d\u02b0 \u025f\u02b0 g\u02b0 \u2014 simultaneous voicing + open glottis = breathy quality.', 'middle', 'Ls')
    bh = [
        ('bh', '/b\u02b0/', '\u092d\u093e\u0932\u0942 bh\u0101l\u016b (bear), bh\u0101rat (India)'),
        ('dh', '/d\u02b0/', '\u0927\u093e\u0917\u093e dh\u0101g\u0101 (thread), dhan (wealth)'),
        ('\u1e0dh', '/\u1e0d\u02b0/', '\u0922\u093e\u0901\u091a\u093e \u1e0dh\u0101\u1e45\u0101 (framework)'),
        ('jh', '/\u025f\u02b0/', '\u091d\u0930\u0928\u093e jharanaa (waterfall)'),
        ('gh', '/g\u02b0/', '\u0918\u0930 ghar (home/house)'),
    ]
    for i, (spell, ipa, ex) in enumerate(bh):
        y = 127 + i * 10
        g += t(60, y, spell, 'middle', 'Ls')
        g += t(120, y, ipa, 'middle', 'Lx')
        g += t(310, y, ex, 'middle', 'Lx')
    g += hr(178)

    g += sh(186, 'HINDI VOWEL SYSTEM')
    g += t(240, 196, '10+ vowels: short/long pairs a/\u0101 i/\u012b u/\u016b plus e ai o au. Nasalization: p\u0101\u1e45c (five), h\u0101\u1e45 (yes).', 'middle', 'Ls')
    g += t(240, 205, 'Schwa deletion: common in standard Hindi \u2014 karna /karn/ not /karna/. Context-dependent.', 'middle', 'Lx')
    g += hr(213)

    g += sh(221, 'HINDI STRESS AND RHYTHM')
    g += t(240, 231, 'Stress: quantity-sensitive, falling on heavy syllables (long vowel or closed). Not phonemically contrastive.', 'middle', 'Ls')
    g += t(240, 240, 'Hindi is mora-timed. Rhythm differs from English stress-timing.', 'middle', 'Lx')

    g += sec_divider(250, 'SECONDARY \u2014 RAJASTHANI (\u0930\u093e\u091c\u0938\u094d\u0925\u093e\u0928\u0940) \u2014 PHONOLOGY')

    g += sh(276, 'RAJASTHANI \u2014 PHONOLOGICAL DISTINCTIONS FROM HINDI')
    g += t(240, 286, 'Rajasthani preserves phonological features lost in standard Hindi, plus some unique developments.', 'middle', 'Ls')
    raj_phon = [
        ('Tones (Marwari)', 'Some dialects have 2 tones: a feature absent from standard Hindi.'),
        ('Breathy vowels', 'Vowel breathiness (murmured vowels) in some words: distinctive from Hindi.'),
        ('Initial /v-/', 'Where Hindi has /v/, Rajasthani may have /b/ \u2014 vaana \u2192 baano (clothes).'),
        ('\u015b \u2192 s', 'Some dialects merge /\u015b/ with /s/ \u2014 reduces consonant inventory vs. Hindi.'),
        ('\u0101 \u2192 o', 'Final long \u0101 often becomes o: k\u0101n\u0101 (ear) \u2192 k\u0101no (Rajasthani).'),
    ]
    for i, (feat, desc) in enumerate(raj_phon):
        y = 296 + i * 11
        g += t(110, y, feat, 'middle', 'Ls')
        g += t(330, y, desc, 'middle', 'Lx')
    g += hr(357)

    g += sh(365, 'RAJASTHANI DIALECTS \u2014 MAJOR VARIETIES')
    dialects = [
        ('Marwari', 'Jodhpur/western Rajasthan. Largest dialect. Tones, breathy vowels. ~14M speakers.'),
        ('Mewari', 'Udaipur area. Mewar kingdom dialect. More archaic vocabulary.'),
        ('Dhundhari', 'Jaipur/eastern Rajasthan. Closer to standard Hindi. Jaipur is capital.'),
        ('Harauti', 'Kota/Bundi area. Transitional to Hindi. Also called Hadoti.'),
        ('Braj Bhasha', 'Mathura/Agra. Classical literary Hindi; influenced Rajasthani court poetry.'),
    ]
    for i, (name, desc) in enumerate(dialects):
        y = 375 + i * 11
        g += t(95, y, name, 'middle', 'Ls')
        g += t(310, y, desc, 'middle', 'Lx')
    g += hr(432)

    g += sh(440, 'PHONOLOGICAL BRIDGE \u2014 FAMILY RESEMBLANCE')
    comp = [
        ('Feature', 'Hindi', 'Rajasthani'),
        ('Tones', 'No', 'Yes (Marwari dialect)'),
        ('Aspirates', '4 series (vl/asp/vd/asp-vd)', '4 series (same)'),
        ('Retroflexes', 'Yes', 'Yes'),
        ('Final vowel', '-\u0101 preserved', '-\u0101 \u2192 -o (Marwari)'),
        ('Script', 'Devanagari', 'Devanagari (+ Mahajani)'),
    ]
    for i, row in enumerate(comp):
        y = 450 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('25', 'Hindi', 'Rajasthani', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 25C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_25c_alt():
    g = open_svg()
    g += t(240, 30, 'HINDI + RAJASTHANI \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 25C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HINDI GRAMMAR \u2014 SOV \u00b7 POSTPOSITIONS \u00b7 GENDER')
    g += t(240, 73, 'Hindi is SOV: Subject-Object-Verb. Verb always final. Postpositions (ne, ko, se, mein) follow nouns.', 'middle', 'Ls')
    g += t(240, 82, '2 genders: masculine and feminine. No neuter (unlike Sanskrit). Gender affects verb agreement.', 'middle', 'Lx')
    g += t(240, 91, 'Ergative-absolutive alignment in past transitive: subject takes -ne postposition.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'HINDI POSTPOSITIONS')
    posts = [
        ('ne', 'ergative agent: Ram ne kh\u0101y\u0101 (Ram ate, -ne marks agent of past trans.)'),
        ('ko', 'dative/accusative: mujhe/mujh ko (to me), use (him/her, acc.)'),
        ('se', 'instrumental/ablative: k\u0101m se (by work), Delhi se (from Delhi)'),
        ('mein', 'locative inessive: ghar mein (in the house)'),
        ('par', 'locative superessive: mez par (on the table)'),
        ('k\u0101/k\u012b/ke', 'genitive: mer\u0101 ghar (my house) \u2014 agrees with possessed noun gender'),
    ]
    for i, (p, gloss) in enumerate(posts):
        y = 117 + i * 10
        g += t(55, y, p, 'middle', 'Ls')
        g += t(310, y, gloss, 'middle', 'Lx')
    g += hr(178)

    g += sh(186, 'HINDI CORE VOCABULARY')
    hvocab = [
        ('\u092a\u093e\u0928\u0940', 'p\u0101n\u012b', 'water'), ('\u0906\u0917', '\u0101g', 'fire'),
        ('\u0927\u0930\u0924\u0940', 'dharat\u012b', 'earth'), ('\u0906\u0926\u092e\u0940', '\u0101dm\u012b', 'person'),
        ('\u091a\u093e\u0901\u0926', 'c\u0101\u1e45d', 'moon'), ('\u092f\u093e\u0926', 'y\u0101d', 'memory'),
        ('\u092d\u0935\u093f\u0937\u094d\u092f', 'bhavishy', 'future'), ('\u0906\u091c\u093c\u093e\u0926\u0940', '\u0101z\u0101d\u012b', 'freedom'),
    ]
    for i, (deva, roman, en) in enumerate(hvocab):
        col = i % 2; row = i // 2
        x = 60 + col * 210; y = 196 + row * 10
        g += t(x, y, deva, 'middle', 'Ld')
        g += t(x + 50, y, roman, 'middle', 'Lx')
        g += t(x + 110, y, en, 'middle', 'Lx')

    g += sec_divider(242, 'SECONDARY \u2014 RAJASTHANI \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(268, 'RAJASTHANI GRAMMAR \u2014 SOV \u00b7 SIMILARITIES AND DIFFERENCES')
    g += t(240, 278, 'Rajasthani is also SOV, uses postpositions, has gender \u2014 same as Hindi. Grammar is mutually intelligible.', 'middle', 'Ls')
    g += t(240, 287, 'Key differences: verb forms, some postpositions, vocabulary (Rajput court + Persian + native Rajasthani).', 'middle', 'Lx')
    g += hr(295)

    g += sh(303, 'RAJASTHANI \u2014 DISTINCT GRAMMATICAL FORMS')
    raj_gram = [
        ('Copula', 'Hindi: hai (is) \u2192 Rajasthani: chhe/ch (eastern) or hai (western)'),
        ('Oblique', 'Rajasthani -\u0101 masculine nouns \u2192 oblique -\u0101ne/ro (vs. Hindi -e/-a)'),
        ('Genitive', 'Rajasthani: ro/r\u012b/r\u0101 (my horse: mer\u014d ghor\u014d) vs. Hindi k\u0101/k\u012b/ke'),
        ('Imperfective', 'Rajasthani: -e\u0305 suffix on verbs (vs. Hindi -t\u0101/-t\u012b)'),
        ('Plural', 'Rajasthani often -\u0101/\u014d vs. Hindi -e\u0305 for masculine nouns'),
    ]
    for i, (feat, desc) in enumerate(raj_gram):
        y = 313 + i * 11
        g += t(85, y, feat, 'middle', 'Ls')
        g += t(310, y, desc, 'middle', 'Lx')
    g += hr(373)

    g += sh(381, 'RAJASTHANI CORE VOCABULARY')
    rvocab = [
        ('\u092a\u093e\u0923\u0940', 'p\u0101\u1e47\u012b', 'water (vs. Hindi p\u0101n\u012b)'),
        ('\u0906\u0917', '\u0101g', 'fire (same as Hindi)'),
        ('\u0927\u0930\u0924\u0940', 'dharati', 'earth (same root)'),
        ('\u092e\u093e\u0928\u0916\u094b', 'm\u0101nakho', 'person (distinct from Hindi)'),
        ('\u091a\u093e\u0902\u0926', 'c\u0101\u1e45d', 'moon (same root)'),
        ('\u092f\u093e\u0926', 'y\u0101d', 'memory (same as Hindi)'),
        ('\u0906\u0935\u0923\u0947\u0930\u094b', '\u0101va\u1e47ero', 'future (lit. the-coming-one)'),
        ('\u0906\u091c\u093c\u093e\u0926\u0940', '\u0101z\u0101d\u012b', 'freedom (same)'),
        ('\u0939\u093f\u092f\u094b', 'hiyo', 'heart (vs. Hindi dil)'),
        ('\u092a\u093f\u0930\u0947\u092e', 'pire m', 'love (vs. Hindi py\u0101r)'),
    ]
    for i, (deva, roman, en) in enumerate(rvocab):
        col = i % 2; row = i // 2
        x = 50 + col * 210; y = 391 + row * 10
        g += t(x, y, deva, 'middle', 'Ld')
        g += t(x + 55, y, roman, 'middle', 'Lx')
        g += t(x + 120, y, en, 'middle', 'Lx')

    g += hr(453)
    g += sh(461, 'GRAMMAR BRIDGE \u2014 HINDI\u2019S CLOSEST SISTER')
    g += t(240, 471, 'Hindi and Rajasthani diverged from the same Apabhramsha ancestor ~12th\u201314th century CE.', 'middle', 'Ls')
    g += t(240, 480, 'Mutual intelligibility is high \u2014 yet phonological, lexical, and some morphological differences are real and consistent.', 'middle', 'Lx')
    g += t(240, 489, 'Rajasthani poetry (Braj, Pingal style) was the dominant literary form of medieval North India.', 'middle', 'Lx')

    g += footer('25', 'Hindi', 'Rajasthani', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 25D ALT — TEXT ─────────────────────────────────────────────────────

def build_25d_alt():
    g = open_svg()
    g += t(240, 30, 'HINDI + RAJASTHANI \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 25D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. KABIR \u2014 DOHA (15TH C. CE)')
    g += t(240, 73, '\u0915\u093e\u0932 \u0915\u0930\u0947 \u0938\u094b \u0906\u091c \u0915\u0930, \u0906\u091c \u0915\u0930\u0947 \u0938\u094b \u0905\u092c \u0964', 'middle', 'Ld')
    g += t(240, 89, 'k\u0101l kare so \u0101j kar, \u0101j kare so ab.', 'middle', 'Ls')
    g += t(240, 98, 'Tomorrow-do that today-do \u00b7 today-do that now.', 'middle', 'Lx')
    g += t(240, 107, '"Do tomorrow\u2019s work today; do today\u2019s work now." \u2014 Kabir Das. Hindi\u2019s most beloved sant-poet.', 'middle', 'F')
    g += hr(115)

    g += sh(123, 'II. HINDI PROVERB \u2014 ON KNOWLEDGE')
    g += t(240, 133, '\u0935\u093f\u0926\u094d\u092f\u093e \u0927\u0928 \u0938\u092c \u0927\u0928\u094b\u0902 \u0915\u0940 \u0926\u093e\u0926\u0940 \u0939\u0948\u0964', 'middle', 'Ld')
    g += t(240, 149, 'vidy\u0101 dhan sab dhano\u1e45 k\u012b d\u0101d\u012b hai.', 'middle', 'Ls')
    g += t(240, 158, '"Knowledge is the greatest of all wealth." \u2014 Hindi proverb.', 'middle', 'F')
    g += hr(166)

    g += sh(174, 'III. HINDI BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 186, '\u092f\u0939 \u0906\u092a\u0915\u0947 \u0932\u093f\u090f \u092c\u0928\u093e\u092f\u093e \u0917\u092f\u093e \u0925\u093e, \u092e\u0941\u092b\u093c\u094d\u0924 \u092e\u0947\u0902,', 'middle', 'Ld')
    g += t(240, 203, '\u0909\u0928 \u0932\u094b\u0917\u094b\u0902 \u0928\u0947 \u091c\u093f\u0928\u094d\u0939\u094b\u0902\u0928\u0947 \u092d\u0935\u093f\u0937\u094d\u092f \u0915\u094b \u092f\u093e\u0926 \u0915\u093f\u092f\u093e\u0964', 'middle', 'Ld')
    g += t(240, 218, 'Yah \u0101pke lie ban\u0101y\u0101 gay\u0101 th\u0101, muft me\u1e45, / un logo\u1e45 ne jinhonn\u0113 bhavishy ko y\u0101d kiy\u0101.', 'middle', 'Lx')
    g += t(240, 227, '"This was made for you, freely, by those who remembered the future." (Hindi)', 'middle', 'F')
    g += hr(235)

    g += sh(243, 'HINDI NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 253, 'Bhavishy (\u092d\u0935\u093f\u0937\u094d\u092f) = future (Sanskrit: what is to become). Y\u0101d karn\u0101 = to remember (Urdu/Hindi: memory-do).', 'middle', 'Ls')
    g += t(240, 262, 'Muft = free of charge (from Persian/Arabic muft). Ergative -ne: jinhonn\u0113 (those who) marks agent of past act.', 'middle', 'Lx')

    g += sec_divider(272, 'SECONDARY \u2014 RAJASTHANI \u2014 RUNNING TEXT')

    g += sh(298, 'I. MEERA BAI \u2014 BHAJAN (16TH C. CE, RAJASTHANI/BRAJ)')
    g += t(240, 308, '\u092a\u093e\u092f\u094b \u091c\u0940 \u092e\u0948\u0902\u0928\u0947 \u0930\u093e\u092e \u0930\u0924\u0928 \u0927\u0928 \u092a\u093e\u092f\u094b\u0964', 'middle', 'Ld')
    g += t(240, 324, 'p\u0101yo j\u012b main-ne R\u0101m ratan dhan p\u0101yo.', 'middle', 'Ls')
    g += t(240, 333, '"I have found the jewel-wealth of Ram\u2019s name." \u2014 Meera Bai, Rajput princess and poet-saint.', 'middle', 'F')
    g += hr(341)

    g += sh(349, 'II. RAJASTHANI PROVERB \u2014 ON MEMORY AND LAND')
    g += t(240, 359, 'Dharati m\u0101 s\u014d chh\u0113, dhara\u1e47o v\u0101l\u014d n\u0101 bh\u016blo.', 'middle', 'L')
    g += t(240, 370, 'Earth  mother is  earth-giving (those) not-forget.', 'middle', 'Lx')
    g += t(240, 379, '"The earth is mother; those who give earth must not be forgotten." (Rajasthani proverb on land and memory)', 'middle', 'F')
    g += hr(387)

    g += sh(395, 'III. RAJASTHANI BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 406, 'Y\u0113 \u0101p\u0101\u1e45r\u0113 v\u0101st\u0113 ban\u0101y\u014d ga\u0304y\u014d, muft m\u0113\u1e45,', 'middle', 'L')
    g += t(240, 418, 'un\u0101 m\u0101\u1e45kh\u0101\u1e45 dv\u0101r\u0101 j\u014dh\u0101\u1e45 bhavishy n\u0113 y\u0101d r\u0101khy\u014d.', 'middle', 'L')
    g += t(240, 430, 'This for-you made was  freely / those people by  who-had future remembered-kept.', 'middle', 'Lx')
    g += t(240, 439, '"This was made for you, freely, by people who remembered the future." (Rajasthani)', 'middle', 'F')
    g += hr(447)

    g += sh(455, 'RAJASTHANI NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 465, '\u0100va\u1e47ero = the future (lit. \u201cthe one that is coming/arriving\u201d \u2014 present participle of \u0101vanu = to come).', 'middle', 'Ls')
    g += t(240, 474, 'Y\u0101d r\u0101khvu\u1e45 = to keep in memory (remember). Literal: memory-keep. Same root as Hindi y\u0101d.', 'middle', 'Lx')
    g += hr(482)

    g += sh(490, 'LANGUAGE BRIDGE \u2014 TWO NORTH INDIAN SISTERS')
    g += t(240, 500, 'Hindi: ~600M speakers (L1+L2). Official language of India. Written in Devanagari. National prestige.', 'middle', 'Ls')
    g += t(240, 509, 'Rajasthani: ~70-80M speakers. No official status. Preserved in oral poetry, folk music, and domestic life.', 'middle', 'Ls')
    g += t(240, 518, 'Meera Bai, Kabir, and the bhakti poet-saints wrote in Rajasthani/Braj \u2014 not standard Hindi. Literature predates Hindi.', 'middle', 'Lx')

    g += footer('25', 'Hindi', 'Rajasthani', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate25a_hindi_rajasthani_script_alt.svg':    build_25a_alt(),
        'plate25b_hindi_rajasthani_phonology_alt.svg': build_25b_alt(),
        'plate25c_hindi_rajasthani_grammar_alt.svg':   build_25c_alt(),
        'plate25d_hindi_rajasthani_text_alt.svg':      build_25d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
