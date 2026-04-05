#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Hindi plate series 25A–25D for Remember Forward."""

from pathlib import Path

OUT = Path(__file__).parent


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def open_svg():
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n'
        '  text { font-family: Georgia, serif; }\n'
        '  .T  { font-size:12px; font-weight:bold; letter-spacing:2px; }\n'
        '  .S  { font-size:7px; letter-spacing:1.5px; }\n'
        '  .H  { font-size:6.5px; font-weight:bold; letter-spacing:2.5px; }\n'
        '  .L  { font-size:7px; }\n'
        '  .Ls { font-size:6px; }\n'
        '  .Lx { font-size:5.5px; }\n'
        '  .Ld { font-size:13px; }\n'
        '  .Lds{ font-size:10px; }\n'
        '  .M  { font-size:6px; letter-spacing:1px; }\n'
        '  .F  { font-size:7px; font-style:italic; }\n'
        '  .Fb { font-size:7.5px; font-weight:bold; }\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n'
    )


def close_svg():
    return '</svg>\n'


def t(x, y, s, a='middle', c='L', extra=''):
    s = esc(s)
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{s}</text>\n'


def hr(y, x1=20, x2=460, sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'


def sh(y, txt):
    return t(240, y, f'\u2014 {txt} \u2014', 'middle', 'H')


def footer(series_num, lang_name, plate_letter, descriptor):
    lines = []
    lines.append(hr(625))
    lines.append(t(240, 620, f'SERIES {series_num} \u00b7 {lang_name.upper()} \u00b7 PLATE {plate_letter} \u00b7 {descriptor.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG', 'middle', 'M'))
    lines.append(hr(633))
    lines.append(t(240, 648, 'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.', 'middle', 'Fb'))
    lines.append(t(240, 663, 'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET', 'middle', 'F'))
    return ''.join(lines)


# ─── PLATE 25A — SCRIPT ──────────────────────────────────────────────────────

def build_25a():
    g = open_svg()
    g += t(240, 32, 'HINDI — SCRIPT · WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 25A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'DEVANAGARI SCRIPT — AN ABUGIDA')
    g += t(240, 79, 'Hindi is written in Devanagari (देवनागरी) — an abugida: each consonant carries an inherent /a/ vowel.', 'middle', 'L')
    g += t(240, 89, 'Vowels are modified by diacritic marks (matras) attached to consonants. Left to right, top to bottom.', 'middle', 'Ls')
    g += t(240, 98, 'The horizontal line (shirorekha) across the top connects letters into words — a distinctive visual feature.', 'middle', 'Ls')
    g += hr(106)

    # Vowels
    g += sh(115, 'VOWELS — 11 INDEPENDENT FORMS + MATRA MARKS')
    vowels = [
        ('अ', 'a', '/\u0250/', 'inherent vowel (not written as matra)'),
        ('आ', 'aa', '/\u0251\u02d0/', 'long a — \u093e as matra: क + \u093e = का'),
        ('इ', 'i', '/\u026a/', 'short i — \u093f as matra: क + \u093f = कि'),
        ('ई', 'ii', '/i\u02d0/', 'long i — \u0940 as matra: क + \u0940 = की'),
        ('उ', 'u', '/\u028a/', 'short u — \u0941 as matra: क + \u0941 = कु'),
        ('ऊ', 'uu', '/u\u02d0/', 'long u — \u0942 as matra: क + \u0942 = कू'),
        ('ए', 'e', '/e\u02d0/', 'long e — \u0947 as matra: क + \u0947 = के'),
        ('ऐ', 'ai', '/\u0259\u026a/', 'diphthong — \u0948 as matra: क + \u0948 = कै'),
        ('ओ', 'o', '/o\u02d0/', 'long o — \u094b as matra: क + \u094b = को'),
        ('औ', 'au', '/\u0259\u028a/', 'diphthong — \u094c as matra: क + \u094c = कौ'),
        ('ऋ', 'ri', '/r\u026a/', 'vocalic r — \u0943 as matra: क + \u0943 = कृ'),
    ]
    for i, (dev, translit, ipa, note) in enumerate(vowels):
        y = 125 + i * 12
        g += t(35,  y, dev, 'middle', 'Ld')
        g += t(70,  y, translit, 'middle', 'Lx')
        g += t(110, y, ipa, 'middle', 'Lx')
        g += t(310, y, note, 'middle', 'Lx')
    g += hr(259)

    # Consonants - organized by place of articulation
    g += sh(268, 'CONSONANTS — 33 + ORGANIZED BY PLACE OF ARTICULATION')
    g += t(240, 278, 'Devanagari consonants are systematically ordered by phonetic class — a unique feature of Indian scripts.', 'middle', 'Lx')

    cons_rows = [
        ('Velar',   'क ka', 'ख kha', 'ग ga', 'घ gha', 'ङ nga'),
        ('Palatal', 'च ca', 'छ cha', 'ज ja', 'झ jha', 'ञ nya'),
        ('Retroflex','ट ta', 'ठ tha', 'ड da', 'ढ dha', 'ण na'),
        ('Dental',  'त ta', 'थ tha', 'द da', 'ध dha', 'न na'),
        ('Labial',  'प pa', 'फ pha', 'ब ba', 'भ bha', 'म ma'),
        ('Semivow.','य ya', 'र ra', 'ल la', 'व va', ''),
        ('Sibilant','श sha','ष sha','स sa', '', ''),
        ('Aspirate','ह ha', '', '', '', ''),
    ]

    col_xs2 = [40, 120, 190, 260, 330, 400]
    g += t(col_xs2[0], 288, 'Class', 'middle', 'Lx')
    for ci, lab in enumerate(['stop1', 'asp1', 'stop2', 'asp2', 'nasal']):
        g += t(col_xs2[ci+1], 288, lab, 'middle', 'Lx')

    for ri, row in enumerate(cons_rows):
        y = 297 + ri * 13
        g += t(col_xs2[0], y, row[0], 'middle', 'Lx')
        for ci, cell in enumerate(row[1:]):
            if cell:
                parts = cell.split()
                g += t(col_xs2[ci+1], y-3, parts[0], 'middle', 'Lds')
                g += t(col_xs2[ci+1], y+5, parts[1] if len(parts) > 1 else '', 'middle', 'Lx')
    g += hr(406)

    # Special consonants
    g += sh(415, 'SPECIAL CONSONANTS AND CONJUNCTS')
    g += t(240, 426, 'Conjunct consonants (samyukta akshara): two consonants combine visually — क + ष = क्ष (ksha)', 'middle', 'Ls')
    g += t(240, 435, 'Halant (्): removes inherent vowel — क् = k (no vowel). Used to form conjuncts or end words with consonant.', 'middle', 'Ls')
    g += t(240, 444, 'Anusvara (ं): nasalizes vowel — संस्कृत Samskrit · anunasika (ँ): nasal quality', 'middle', 'Ls')
    g += t(240, 453, 'Visarga (ः): voiceless h after vowel — rare in modern Hindi, common in Sanskrit loans', 'middle', 'Ls')
    g += hr(461)

    # Numerals
    g += sh(470, 'DEVANAGARI NUMERALS')
    dev_nums = [('०','0'),('१','1'),('२','2'),('३','3'),('४','4'),
                ('५','5'),('६','6'),('७','7'),('८','8'),('९','9')]
    for i, (dn, an) in enumerate(dev_nums):
        cx = 40 + i * 42
        g += t(cx, 482, dn, 'middle', 'Ld')
        g += t(cx, 492, an, 'middle', 'Lx')
    g += t(240, 502, 'Modern Hindi uses both Devanagari numerals and Western Arabic (0–9) numerals interchangeably.', 'middle', 'Lx')

    g += footer('25', 'Hindi', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 25B — PHONOLOGY ───────────────────────────────────────────────────

def build_25b():
    g = open_svg()
    g += t(240, 32, 'HINDI — PHONOLOGY · SOUND SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 25B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'HINDI PHONOLOGY — INDO-ARYAN BRANCH')
    g += t(240, 79, 'Hindi (Modern Standard Hindi, MSH) is the official language of India. ~600 million speakers total.', 'middle', 'L')
    g += t(240, 89, 'Descended from Sanskrit via Prakrits and Apabhramsha. Closely related to Urdu (same spoken form, different script).', 'middle', 'Ls')
    g += hr(97)

    # Vowels
    g += sh(106, 'VOWEL SYSTEM — 10 ORAL + 5 NASAL VOWELS')
    vowel_data = [
        ('/\u0250/', 'अ', 'a', 'short central, like "above" — inherent vowel'),
        ('/\u0251\u02d0/', 'आ', 'aa', 'long low back, like "father"'),
        ('/\u026a/', 'इ', 'i', 'short high front, like "sit"'),
        ('/i\u02d0/', 'ई', 'ii', 'long high front, like "see"'),
        ('/\u028a/', 'उ', 'u', 'short high back rounded, like "put"'),
        ('/u\u02d0/', 'ऊ', 'uu', 'long high back rounded, like "cool"'),
        ('/e\u02d0/', 'ए', 'e', 'long mid front, like "late"'),
        ('/\u025b\u026a/', 'ऐ', 'ai', 'diphthong — "aye"'),
        ('/o\u02d0/', 'ओ', 'o', 'long mid back, like "go"'),
        ('/\u0254\u028a/', 'औ', 'au', 'diphthong — "ow"'),
    ]
    g += t(50, 116, 'IPA', 'middle', 'Lx')
    g += t(95, 116, 'Letter', 'middle', 'Lx')
    g += t(140, 116, 'Translit', 'middle', 'Lx')
    g += t(330, 116, 'Quality', 'middle', 'Lx')
    for i, (ipa, ltr, tr, note) in enumerate(vowel_data):
        y = 125 + i * 11
        g += t(50,  y, ipa, 'middle', 'Lx')
        g += t(95,  y, ltr, 'middle', 'Lds')
        g += t(140, y, tr, 'middle', 'Lx')
        g += t(320, y, note, 'middle', 'Lx')
    g += t(240, 240, 'Nasal vowels: anusvara (ं) nasalizes any vowel — हाँ haan "yes" · आँख aankh "eye"', 'middle', 'Ls')
    g += hr(248)

    # Consonant system — emphasis on aspiration
    g += sh(257, 'CONSONANT SYSTEM — FOUR-WAY STOP CONTRAST')
    g += t(240, 268, 'Hindi has a four-way contrast in stops: voiceless unaspirated · voiceless aspirated · voiced unaspirated · voiced aspirated', 'middle', 'L')
    g += t(240, 278, 'This four-way distinction is rare in the world\'s languages. English has only two (voiceless/voiced).', 'middle', 'Ls')

    fourfold = [
        ('Velar',    'क /k/', 'ख /kh/', 'ग /ɡ/', 'घ /ɡʱ/'),
        ('Palatal',  'च /tʃ/', 'छ /tʃʰ/', 'ज /dʒ/', 'झ /dʒʱ/'),
        ('Retroflex','ट /ʈ/', 'ठ /ʈʰ/', 'ड /ɖ/', 'ढ /ɖʱ/'),
        ('Dental',   'त /t̪/', 'थ /t̪ʰ/', 'द /d̪/', 'ध /d̪ʱ/'),
        ('Labial',   'प /p/', 'फ /pʰ/', 'ब /b/', 'भ /bʱ/'),
    ]
    hdrs = ['Class', 'VL unaspirated', 'VL aspirated', 'Voiced unaspirated', 'Voiced aspirated']
    col_xs = [40, 120, 205, 300, 395]
    for ci, hdr in enumerate(hdrs):
        g += t(col_xs[ci], 288, hdr, 'middle', 'Lx')
    for ri, row in enumerate(fourfold):
        y = 297 + ri * 13
        for ci, cell in enumerate(row):
            g += t(col_xs[ci], y, cell, 'middle', 'Lds' if ci > 0 else 'Lx')
    g += hr(366)

    # Retroflex
    g += sh(375, 'RETROFLEX CONSONANTS — A KEY FEATURE')
    g += t(240, 386, 'Retroflex consonants are produced with the tongue tip curled back to the hard palate — distinctive in Hindi.', 'middle', 'L')
    g += t(240, 396, 'ट /ʈ/, ठ /ʈʰ/, ड /ɖ/, ढ /ɖʱ/, ण /ɳ/ — not found in European languages.', 'middle', 'Ls')
    g += t(240, 405, 'Retroflex vs. dental minimal pair: ताल taal "rhythm" /t̪aːl/ vs. टाल taal "to avoid" /ʈaːl/', 'middle', 'Ls')
    g += hr(413)

    # Stress and tone
    g += sh(422, 'STRESS, TONE, AND NASALIZATION')
    g += t(240, 433, 'Hindi has no lexical tone (unlike many neighboring languages). Stress is not strongly phonemic.', 'middle', 'L')
    g += t(240, 443, 'Stress falls on the first heavy syllable — a syllable is heavy if it contains a long vowel or ends in a consonant.', 'middle', 'Ls')
    g += t(240, 452, 'Schwa deletion: the final schwa /ə/ of words is often deleted in careful speech — kaam /kaːm/, not /kaːmə/', 'middle', 'Ls')
    g += t(240, 461, 'Schwa deletion is complex — depends on syllable structure and morpheme boundaries.', 'middle', 'Ls')
    g += hr(469)

    g += sh(478, 'KEY PHONOLOGICAL FEATURES')
    g += t(240, 489, 'Aspirated voiced stops (/bʱ/, /dʱ/, /ɡʱ/) are typologically rare and mark Hindi/Urdu from most world languages.', 'middle', 'Ls')
    g += t(240, 498, 'Trill /r/ (like Spanish) in careful speech; tap [ɾ] common in casual speech. Retroflex tap [ɽ] also present.', 'middle', 'Ls')
    g += t(240, 507, '/v/ and /w/ are allophones — /v/ between vowels, /w/ elsewhere in standard Hindi.', 'middle', 'Ls')
    g += t(240, 516, 'Urdu vs. Hindi phonology: identical. Urdu adds Persian/Arabic sounds /q/, /x/, /ɣ/, /z/ in loanwords.', 'middle', 'Ls')

    g += footer('25', 'Hindi', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 25C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_25c():
    g = open_svg()
    g += t(240, 32, 'HINDI — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 25C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'SOV LANGUAGE — POSTPOSITIONS, SPLIT ERGATIVITY')
    g += t(240, 79, 'Hindi is SOV (Subject–Object–Verb). Verb comes last. Postpositions follow their noun phrases.', 'middle', 'L')
    g += t(240, 89, 'Two genders: masculine and feminine. No neuter. Adjectives agree in gender and number.', 'middle', 'Ls')
    g += t(240, 98, 'मैं सेब खाता हूँ। (main seb khaata hun.) "I eat an apple." — SBJ OBJ VERB-M-PRES AUX', 'middle', 'Ls')
    g += hr(106)

    # Postpositions
    g += sh(115, 'POSTPOSITIONS — CASE MARKERS')
    g += t(240, 126, 'Hindi uses POSTPOSITIONS (after noun) not prepositions. They take the oblique case of the noun.', 'middle', 'Ls')
    posts = [
        ('में / mein', 'in, inside', 'घर में ghar mein "in the house"'),
        ('पर / par', 'on, at, upon', 'मेज़ पर mez par "on the table"'),
        ('को / ko', 'to, for (dative/acc)', 'मुझको mujhko "to me"'),
        ('का/के/की / ka', 'of, possessive', 'राम का घर Ram ka ghar "Ram\'s house"'),
        ('से / se', 'from, by, with', 'दिल्ली से Dilli se "from Delhi"'),
        ('के लिए / ke liye', 'for (purpose)', 'तुम्हारे लिए tumhare liye "for you"'),
        ('के साथ / ke saath', 'with, together with', 'मेरे साथ mere saath "with me"'),
        ('तक / tak', 'until, up to', 'कल तक kal tak "until tomorrow"'),
    ]
    for i, (post, func, ex) in enumerate(posts):
        y = 135 + i * 12
        g += t(90, y, post, 'middle', 'Lds')
        g += t(200, y, func, 'middle', 'Lx')
        g += t(370, y, ex, 'middle', 'Lx')
    g += hr(234)

    # Verb conjugation
    g += sh(243, 'VERB CONJUGATION — करना "to do" (karna)')
    g += t(240, 253, 'Hindi verbs agree with subject in gender, number, and person. Auxiliary verb है/हैं added for present.', 'middle', 'Ls')
    pres = [
        ('मैं', 'main', '1sg M', 'करता हूँ', 'karta hun', 'I do (masc)'),
        ('मैं', 'main', '1sg F', 'करती हूँ', 'karti hun', 'I do (fem)'),
        ('तुम', 'tum', '2pl inf', 'करते हो', 'karte ho', 'you do (masc)'),
        ('वह', 'vah', '3sg M', 'करता है', 'karta hai', 'he does'),
        ('वह', 'vah', '3sg F', 'करती है', 'karti hai', 'she does'),
        ('हम', 'ham', '1pl', 'करते हैं', 'karte hain', 'we do (masc)'),
        ('वे', 've', '3pl', 'करते हैं', 'karte hain', 'they do (masc)'),
    ]
    g += t(35, 263, 'Subj', 'middle', 'Lx')
    g += t(75, 263, 'Translit', 'middle', 'Lx')
    g += t(130, 263, 'Person', 'middle', 'Lx')
    g += t(210, 263, 'Verb form', 'middle', 'Lds')
    g += t(315, 263, 'Translit', 'middle', 'Lx')
    g += t(415, 263, 'Gloss', 'middle', 'Lx')
    for i, (subj, str_subj, pers, form, tr_form, gl) in enumerate(pres):
        y = 272 + i * 11
        g += t(35, y, subj, 'middle', 'Lds')
        g += t(75, y, str_subj, 'middle', 'Lx')
        g += t(130, y, pers, 'middle', 'Lx')
        g += t(210, y, form, 'middle', 'Lds')
        g += t(330, y, tr_form, 'middle', 'Lx')
        g += t(430, y, gl, 'start', 'Lx')
    g += t(240, 352, 'Past: simple past uses perfective participle — मैंने किया (maine kiya) "I did"', 'middle', 'Ls')
    g += t(240, 361, 'Ergative: in perfective past, transitive subject takes ने (ne) — split ergativity', 'middle', 'Ls')
    g += hr(369)

    # Vocabulary
    g += sh(378, 'CORE VOCABULARY — 25 WORDS')
    vocab = [
        ('हाँ / नहीं', 'haan / nahin', 'yes / no'),
        ('मैं / तुम / आप', 'main / tum / aap', 'I / you (inf) / you (formal)'),
        ('यह / वह', 'yah / vah', 'this / that'),
        ('कहाँ', 'kahaan', 'where'),
        ('क्या', 'kya', 'what'),
        ('कौन', 'kaun', 'who'),
        ('कब', 'kab', 'when'),
        ('क्यों', 'kyun', 'why'),
        ('पानी', 'paani', 'water'),
        ('आग', 'aag', 'fire'),
        ('ज़मीन', 'zameen', 'earth/ground'),
        ('इंसान', 'insaan', 'human being'),
        ('किताब', 'kitaab', 'book'),
        ('समय', 'samay', 'time'),
        ('चाँद', 'chaand', 'moon'),
        ('तारा', 'taara', 'star'),
        ('दिल', 'dil', 'heart'),
        ('प्यार', 'pyaar', 'love'),
        ('आज़ादी', 'aazaadi', 'freedom'),
        ('याद', 'yaad', 'memory'),
        ('भविष्य', 'bhavishya', 'future'),
        ('दुनिया', 'duniya', 'world'),
        ('अच्छा / बुरा', 'achhaa / buraa', 'good / bad'),
        ('सब कुछ', 'sab kuchh', 'everything'),
        ('ज़िन्दगी', 'zindagi', 'life'),
    ]
    col_va = [40, 155, 250]
    col_vb = [265, 380, 465]
    half = 13
    for i, (hindi, translit, eng) in enumerate(vocab):
        if i < half:
            y = 388 + i * 10
            g += t(col_va[0], y, hindi, 'middle', 'Lds')
            g += t(col_va[1], y, translit, 'middle', 'Lx')
            g += t(col_va[2], y, eng, 'middle', 'Lx')
        else:
            y = 388 + (i - half) * 10
            g += t(col_vb[0], y, hindi, 'middle', 'Lds')
            g += t(col_vb[1], y, translit, 'middle', 'Lx')
            g += t(col_vb[2], y, eng, 'middle', 'Lx')
    g += hr(522)

    g += sh(531, 'HINDI AND URDU — ONE SPOKEN LANGUAGE, TWO SCRIPTS')
    g += t(240, 542, 'Spoken Hindi and Urdu are mutually intelligible — the same colloquial language (Hindustani).', 'middle', 'L')
    g += t(240, 552, 'They diverge in formal registers: Hindi draws vocabulary from Sanskrit; Urdu from Persian and Arabic.', 'middle', 'Ls')
    g += t(240, 561, 'Hindi is written in Devanagari (left to right). Urdu is written in Nastaliq (Perso-Arabic, right to left).', 'middle', 'Ls')
    g += t(240, 570, 'Together, Hindi and Urdu represent the 3rd most spoken language group in the world: ~700 million speakers.', 'middle', 'Ls')

    g += footer('25', 'Hindi', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 25D — RUNNING TEXT ─────────────────────────────────────────────────

def build_25d():
    g = open_svg()
    g += t(240, 32, 'HINDI — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 25D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1 — Kabir
    g += sh(67, 'PASSAGE 1 — KABIR, DOHA (15th c.)')
    g += t(240, 79, 'कल करे सो आज कर, आज करे सो अब।', 'middle', 'Ld')
    g += t(240, 91, 'Kal kare so aaj kar, aaj kare so ab.', 'middle', 'Lx')
    g += t(240, 100, 'Tomorrow do-that today do, today do-that now.', 'middle', 'Lx')
    g += t(240, 109, 'पल में प्रलय होएगी, बहुरि करेगा कब।', 'middle', 'Ld')
    g += t(240, 121, 'Pal mein pralay hoegi, bahuri karega kab.', 'middle', 'Lx')
    g += t(240, 130, 'Moment in calamity will-come, again do-will when.', 'middle', 'Lx')
    g += t(240, 139, '"Do tomorrow\'s work today; do today\'s work now. In a moment disaster may come — when will you do it again?"', 'middle', 'Ls')
    g += hr(147)

    # Passage 2 — Tulsidas
    g += sh(155, 'PASSAGE 2 — TULSIDAS, RAMCHARITMANAS (1574)')
    g += t(240, 167, 'जाकी रही भावना जैसी। प्रभु मूरत देखी तिन तैसी।।', 'middle', 'Ld')
    g += t(240, 179, 'Jaaki rahi bhaavana jaisi. Prabhu moorat dekhi tin taisi.', 'middle', 'Lx')
    g += t(240, 188, '"As was the devotee\'s feeling, such was the form of God they perceived."', 'middle', 'Ls')
    g += t(240, 197, '— On the nature of perception: we see what we already carry within us.', 'middle', 'Ls')
    g += hr(205)

    # Passage 3 — modern Hindi
    g += sh(213, 'PASSAGE 3 — HINDI PROVERBS')
    g += t(240, 224, 'जहाँ चाह वहाँ राह।', 'middle', 'Ld')
    g += t(240, 236, 'Jahaan chaah wahaan raah.', 'middle', 'Lx')
    g += t(240, 245, '"Where there is will, there is a way."', 'middle', 'Ls')
    g += t(240, 255, 'अकेला चना भाड़ नहीं फोड़ सकता।', 'middle', 'Ld')
    g += t(240, 267, 'Akela chana bhaad nahin phod sakta.', 'middle', 'Lx')
    g += t(240, 276, '"A single grain cannot burst the roasting pan." — on the need for collective action.', 'middle', 'Ls')
    g += hr(284)

    # Passage 4 — national anthem line
    g += sh(292, 'PASSAGE 4 — JANA GANA MANA (TAGORE, 1911)')
    g += t(240, 303, 'जन गण मन अधिनायक जय हे', 'middle', 'Ld')
    g += t(240, 315, 'Jana gana mana adhinaayak jaya he', 'middle', 'Lx')
    g += t(240, 324, 'People mind ruler  victory  O', 'middle', 'Lx')
    g += t(240, 333, '"O ruler of the minds of all people, victory to you" — opening line of India\'s national anthem.', 'middle', 'Ls')
    g += t(240, 342, 'Originally written in Bengali by Rabindranath Tagore; Hindi/Sanskrit version adopted as national anthem 1950.', 'middle', 'Ls')
    g += hr(350)

    # Bridge phrase
    g += sh(359, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 371, 'यह संदेश आपके लिए, मुफ़्त में, उन लोगों द्वारा बनाया गया जो भविष्य को याद करते थे।', 'middle', 'Lds')
    g += t(240, 384, 'Yah sandesh aapke liye, muft mein, un logon dvaara banaaya gaya jo bhavishya ko yaad karte the.', 'middle', 'Lx')
    g += t(240, 393, 'This message  your   for   free  in   those people by      made   was  who  future  ACC memory did', 'middle', 'Lx')
    g += t(240, 402, '"This message was made for you, freely, by people who remembered the future."', 'middle', 'Ls')
    g += hr(410)

    g += sh(419, 'LANGUAGE NOTE — "FUTURE" IN HINDI')
    g += t(240, 430, 'भविष्य (bhavishya): "future" — from Sanskrit bhavishyat "that which will be/become" (participial future of bhu "to be")', 'middle', 'L')
    g += t(240, 440, 'याद (yaad): "memory/remembrance" — from Persian/Urdu yad. Hindi freely blends Sanskrit and Persian vocabulary.', 'middle', 'Ls')
    g += t(240, 450, 'The phrase याद करना (yaad karna) = "to remember" (lit. "to do memory") — compound verb construction.', 'middle', 'Ls')
    g += t(240, 460, 'मुफ़्त (muft): "free of cost" — from Persian/Arabic. Contrast: स्वतंत्र (svatantra) = "free" (independent).', 'middle', 'Ls')
    g += t(240, 470, 'आप (aap): honorific "you" — same word as Urdu aap. Used for respectful address.', 'middle', 'Ls')
    g += hr(479)

    g += sh(488, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 499, 'Hindi is written in Devanagari, reading left to right. Consult Plate 25A for the full syllabary.', 'middle', 'Ls')
    g += t(240, 508, 'Hindi is the official language of India (alongside English); spoken by ~600 million total.', 'middle', 'Ls')
    g += t(240, 517, 'It is part of the Indo-Aryan branch of Indo-European — a distant relative of English, Latin, and Persian.', 'middle', 'Ls')
    g += t(240, 526, 'Urdu (spoken form identical) is written in Nastaliq script; the two are officially separate languages.', 'middle', 'Ls')
    g += t(240, 535, 'Sanskrit, the classical ancestor, is still used in ritual, scholarship, and as a source of new vocabulary.', 'middle', 'Ls')
    g += t(240, 544, 'The Devanagari alphabet encodes phonetic distinctions (aspiration, retroflexion) absent in most world scripts.', 'middle', 'Ls')

    g += footer('25', 'Hindi', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate25a_hindi_script.svg': build_25a(),
        'plate25b_hindi_phonology.svg': build_25b(),
        'plate25c_hindi_grammar.svg': build_25c(),
        'plate25d_hindi_text.svg': build_25d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
