#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Swahili plate series 20A–20D for Remember Forward."""

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


def bx(x, y, w, h, sw=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="black" stroke-width="{sw}"/>\n'


def footer(series_num, lang_name, plate_letter, descriptor):
    lines = []
    lines.append(hr(625))
    lines.append(t(240, 620, f'SERIES {series_num} \u00b7 {lang_name.upper()} \u00b7 PLATE {plate_letter} \u00b7 {descriptor.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG', 'middle', 'M'))
    lines.append(hr(633))
    lines.append(t(240, 648, 'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.', 'middle', 'Fb'))
    lines.append(t(240, 663, 'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET', 'middle', 'F'))
    return ''.join(lines)


# ─── PLATE 20A — SCRIPT ──────────────────────────────────────────────────────

def build_20a():
    g = open_svg()
    g += t(240, 32, 'SWAHILI — SCRIPT · WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 20A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(67, 'LATIN SCRIPT — STANDARD SINCE ~1900')
    g += t(240, 77, 'Swahili (Kiswahili) is written in the Latin alphabet — 26 letters, highly phonemic spelling.', 'middle', 'L')
    g += t(240, 87, 'Standardized by the Inter-Territorial Language Committee (ITLC) in 1930 for East Africa.', 'middle', 'Ls')
    g += t(240, 96, 'Before Latin script: Arabic-based Ajami script used from ~14th century along Swahili coast.', 'middle', 'Ls')
    g += hr(104)

    # Alphabet
    g += sh(112, 'THE 26-LETTER LATIN ALPHABET IN SWAHILI')
    g += t(240, 121, 'One letter = one sound. No silent letters. No tonal diacritics needed.', 'middle', 'Ls')
    letters_sw = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    values_sw = [
        '/a/','b','ch','d','/e/','f','g','h','/i/','j/dʒ',
        'k','l','m','n','/o/','p','q(loan)','r','s','t',
        '/u/','v','w','x(loan)','y/j','z'
    ]
    col_x6 = [30, 110, 190, 270, 350, 430]
    for i, (ltr, val) in enumerate(zip(letters_sw, values_sw)):
        col = i % 6
        row = i // 6
        cx = col_x6[col]
        ry = 130 + row * 15
        g += t(cx, ry, ltr, 'middle', 'L')
        g += t(cx, ry + 8, val, 'middle', 'Lx')
    g += hr(202)

    # Digraphs
    g += sh(210, 'SWAHILI DIGRAPHS AND CONSONANT CLUSTERS')
    digraphs_sw = [
        ('ch', '/tʃ/', 'palatal affricate', 'chakula (food), chini (below)'),
        ('sh', '/ʃ/', 'postalveolar fric.', 'shule (school), shamba (farm)'),
        ('gh', '/ɣ/', 'voiced velar fric.', 'ghali (expensive), balagha (rhetoric)'),
        ('ng\'','/ ŋ/','velar nasal (standalone)','ng\'ombe (cattle), ng\'o (emphatic)'),
        ('ny', '/ɲ/', 'palatal nasal', 'nyumba (house), nyama (meat)'),
        ('dh', '/ð/', 'voiced dental fric.', 'dhahabu (gold), dhana (concept)'),
        ('th', '/θ/', 'voiceless dental', 'thamani (value), thithi (gruel)'),
        ('mb', '/mb/', 'prenasalized stop', 'mbwa (dog), mbali (far)'),
        ('nd', '/nd/', 'prenasalized stop', 'ndizi (banana), ndani (inside)'),
        ('ng', '/ŋg/', 'prenasalized stop', 'ngoja (wait), ngapi (how many)'),
        ('nj', '/ndʒ/', 'prenasalized affric.', 'njia (path/way), njiwa (dove)'),
    ]
    for i, (dg, ipa, name, ex) in enumerate(digraphs_sw):
        y = 220 + i * 13
        g += t(35, y, dg, 'middle', 'Ls')
        g += t(70, y, ipa, 'middle', 'Lx')
        g += t(150, y, name, 'middle', 'Lx')
        g += t(340, y, ex, 'middle', 'Lx')
    g += hr(364)

    # Ajami
    g += sh(372, 'AJAMI — ARABIC-BASED HISTORICAL SCRIPT')
    g += t(240, 382, 'Ajami = Arabic script adapted for Swahili. Used ~14th–early 20th century along coast.', 'middle', 'Ls')
    g += t(240, 391, 'Coastal city-states (Mombasa, Malindi, Zanzibar, Kilwa) produced Ajami manuscripts and poetry.', 'middle', 'Ls')
    g += t(240, 400, 'Utendi wa Tambuka (Epic of Heraklios, 1728) is among the oldest surviving Swahili texts in Ajami.', 'middle', 'Ls')
    g += t(240, 409, 'Read right-to-left like Arabic. Vowel diacritics added to mark Swahili vowels not in Arabic.', 'middle', 'Ls')
    g += t(240, 418, 'Sample: كيسواحيلي = Kiswahili · متو = mtu (person) · ماجي = maji (water)', 'middle', 'Ls')
    g += hr(426)

    # Noun class system preview
    g += sh(434, 'NOUN CLASS SYSTEM — OVERVIEW (8 MAJOR CLASSES)')
    g += t(240, 444, 'Swahili nouns belong to grammatical classes marked by prefixes. Each class has its own agreement prefix.', 'middle', 'Ls')
    classes = [
        ('M/WA', 'M-/WA-', 'mtu/watu', 'people/humans'),
        ('M/MI', 'M-/MI-', 'mti/miti', 'trees/plants'),
        ('MA', 'Ø/MA-', 'tunda/matunda', 'fruits/paired things'),
        ('KI/VI', 'KI-/VI-', 'kitu/vitu', 'things/objects'),
        ('N/N', 'N-/N-', 'nyumba/nyumba', 'houses/animals'),
        ('U/U', 'U-/Ø-', 'ukuta/kuta', 'walls/abstract'),
        ('PA', 'PA-', 'mahali', 'specific place'),
        ('KU', 'KU-', 'kusoma', 'verbal nouns (infinitive)'),
    ]
    for i, (cls, pfx, example, gloss) in enumerate(classes):
        col = i % 2
        row = i // 2
        cx = 120 if col == 0 else 360
        y = 454 + row * 15
        g += t(cx - 60, y, cls, 'middle', 'Ls')
        g += t(cx, y, pfx, 'middle', 'Lx')
        g += t(cx + 70, y, example, 'middle', 'Lx')
        g += t(cx + 130, y, gloss, 'middle', 'Lx')
    g += hr(516)

    # History
    g += sh(524, 'LANGUAGE HISTORY AND SPREAD')
    g += t(240, 534, 'Swahili = Bantu base (~50-70%) + Arabic (~20-30%) + Persian, Portuguese, English, Hindi loanwords.', 'middle', 'Ls')
    g += t(240, 543, 'Origin: Swahili coast trade lingua franca from ~1st millennium CE. Name from Arabic sawahil (coasts).', 'middle', 'Ls')
    g += t(240, 552, 'Official language of Tanzania, Kenya, Uganda, Rwanda, DRC, Comoros. UN official language (2022).', 'middle', 'Ls')
    g += t(240, 561, '~15-20M native speakers; ~100-200M as second language across East and Central Africa.', 'middle', 'Ls')
    g += t(240, 570, '5 vowels /a e i o u/ — the same as Italian/Spanish. All pure, no diphthongs in native words.', 'middle', 'Ls')

    g += footer('20', 'Swahili', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 20B — PHONOLOGY ───────────────────────────────────────────────────

def build_20b():
    g = open_svg()
    g += t(240, 32, 'SWAHILI — PHONOLOGY · SOUND SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 20B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(67, 'OVERVIEW — NON-TONAL, PENULTIMATE STRESS')
    g += t(240, 77, 'Swahili is NON-TONAL. Stress always falls on the PENULTIMATE (second-to-last) syllable.', 'middle', 'L')
    g += t(240, 87, 'ki-ta-BU (book) · ma-JI (water) · ra-FI-ki (friend) · u-je-MB-o (building)', 'middle', 'Ls')
    g += t(240, 96, 'Exception: Arabic/English loanwords may carry non-penultimate stress in careful speech.', 'middle', 'Lx')
    g += hr(104)

    # Vowels
    g += sh(112, 'VOWEL SYSTEM — 5 PURE VOWELS')
    vowels_sw = [
        ('/a/', 'a', 'low open central', 'asali (honey), baba (father)', '"ah" — never reduced'),
        ('/e/', 'e', 'mid front', 'embe (mango), peke (alone)', '"eh" — always clear'),
        ('/i/', 'i', 'high front', 'ina (has), imani (faith)', '"ee" — pure'),
        ('/o/', 'o', 'mid back rounded', 'oa (marry), mto (river)', '"oh" — always full'),
        ('/u/', 'u', 'high back rounded', 'ua (flower/kill), mtu (person)', '"oo" — always full'),
    ]
    for i, (ipa, spell, desc, ex, note) in enumerate(vowels_sw):
        y = 122 + i * 14
        g += t(40, y, ipa, 'middle', 'Ls')
        g += t(78, y, spell, 'middle', 'Ls')
        g += t(145, y, desc, 'middle', 'Lx')
        g += t(280, y, ex, 'middle', 'Lx')
        g += t(420, y, note, 'middle', 'Lx')
    g += t(240, 194, 'NO schwa. NO diphthongs in native vocabulary. Vowels maintain full quality in all positions.', 'middle', 'Ls')
    g += hr(202)

    # Consonants
    g += sh(210, 'CONSONANT SYSTEM')
    g += t(240, 219, 'Standard Swahili has ~25 consonant phonemes including a unique set of prenasalized stops.', 'middle', 'Ls')
    cons_sw = [
        ('p b', '/p b/', 'bilabial stops', 'paka (cat), baba (father)'),
        ('t d', '/t d/', 'alveolar stops', 'tatu (three), dawa (medicine)'),
        ('k g', '/k ɡ/', 'velar stops', 'kazi (work), gari (vehicle)'),
        ('ch j', '/tʃ dʒ/', 'palatal affricates', 'chakula (food), jiwe (stone)'),
        ('f v', '/f v/', 'labiodentals', 'fupi (short), vita (war)'),
        ('s z', '/s z/', 'alveolar fricatives', 'saba (seven), zawadi (gift)'),
        ('sh', '/ʃ/', 'postalveolar fric.', 'shule (school), shida (problem)'),
        ('th dh', '/θ ð/', 'dental fricatives', 'thamani (value), dhahabu (gold)'),
        ('gh', '/ɣ/', 'voiced velar fric.', 'ghali (expensive)'),
        ('h', '/h/', 'glottal fric.', 'hapa (here), hewa (air)'),
        ('m n', '/m n/', 'nasals', 'mama (mother), nne (four)'),
        ('ny ng\'', '/ɲ ŋ/', 'palatal/velar nasals', 'nyama (meat), ng\'ombe (cow)'),
        ('l r', '/l r/', 'lateral/trill', 'leo (today), rafiki (friend)'),
        ('w y', '/w j/', 'glides', 'watu (people), yeye (he/she)'),
    ]
    for i, (spell, ipa, desc, ex) in enumerate(cons_sw):
        y = 230 + i * 12
        col = i % 2
        cx = 20 if col == 0 else 250
        g += t(cx + 25, y, spell, 'middle', 'Ls')
        g += t(cx + 60, y, ipa, 'middle', 'Lx')
        g += t(cx + 110, y, desc, 'middle', 'Lx')
        g += t(cx + 175, y, ex, 'middle', 'Lx')
    g += hr(400)

    # Prenasalized consonants
    g += sh(408, 'PRENASALIZED CONSONANTS — SINGLE PHONEMES')
    g += t(240, 418, 'Prenasalized consonants are SINGLE phonemes in Swahili — the nasal is not a separate syllable.', 'middle', 'L')
    g += t(240, 427, 'They allow word-initial consonant clusters not found in most other Bantu languages\' loanword adaptations.', 'middle', 'Ls')
    prenas = [
        ('mb', '/mb/', 'mbwa (dog), mbali (far), mbuzi (goat)'),
        ('mv', '/mv/', 'mvua (rain), mvuke (steam)'),
        ('nd', '/nd/', 'ndizi (banana), ndugu (sibling/comrade)'),
        ('nj', '/ndʒ/', 'njia (path), njema (good — in phrases)'),
        ('ng', '/ŋɡ/', 'ngoma (drum), ngoja (wait)'),
        ('ng\'', '/ŋ/', 'ng\'ombe (cattle) — same velar nasal, no stop'),
    ]
    for i, (cl, ipa, ex) in enumerate(prenas):
        y = 437 + i * 12
        g += t(50, y, cl, 'middle', 'Ls')
        g += t(90, y, ipa, 'middle', 'Lx')
        g += t(290, y, ex, 'middle', 'Lx')
    g += hr(516)

    # Syllable structure
    g += sh(524, 'SYLLABLE STRUCTURE AND PROSODY')
    g += t(240, 534, 'Syllable structure: (C)V — open syllables dominate. Final consonants are rare (only in loans).', 'middle', 'Ls')
    g += t(240, 543, 'Prenasalized consonants (mb, nd, ng) count as single consonants: mbu-zi = 2 syllables, not 3.', 'middle', 'Ls')
    g += t(240, 552, 'N- class nouns use the nasal as a consonant: n-dizi (banana) = 3 syllables: ndi-zi (2) Wait — N is prefix.', 'middle', 'Lx')
    g += t(240, 560, 'Vowel length: contrastive in some loanwords (from Arabic) — kaa (sit) vs. kaa (charcoal).', 'middle', 'Ls')
    g += t(240, 569, 'Intonation: declarative falls, question rises — but the language lacks lexical tone contrast.', 'middle', 'Ls')
    g += t(240, 578, 'IPA summary: /p b t d k ɡ tʃ dʒ f v s z ʃ θ ð ɣ h m n ɲ ŋ mb nd ndʒ ŋɡ l r w j/ + /a e i o u/', 'middle', 'Lx')

    g += footer('20', 'Swahili', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 20C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_20c():
    g = open_svg()
    g += t(240, 32, 'SWAHILI — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 20C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(67, 'NOUN CLASS AGREEMENT SYSTEM')
    g += t(240, 77, 'EVERY Swahili verb, adjective, and relative clause must AGREE with the noun class of its subject.', 'middle', 'L')
    g += t(240, 87, 'The prefix changes depending on noun class, tense, and mood. The root of the verb stays fixed.', 'middle', 'Ls')
    # Class agreement table
    g += t(240, 96, 'Format: [SUBJECT PREFIX] + [TENSE MARKER] + [OBJECT PREFIX] + [VERB ROOT]', 'middle', 'Lx')

    classes_full = [
        ('M/WA (1/2)', 'mtu/watu', 'a-/wa-', 'A-na-soma / Wa-na-soma', 'He reads / They read'),
        ('M/MI (3/4)', 'mti/miti', 'u-/i-', 'U-na-anguka / I-na-anguka', 'Tree falls / Trees fall'),
        ('MA (5/6)', 'tunda/matunda', 'li-/ya-', 'Li-na-anguka / Ya-na-anguka', 'Fruit falls / Fruits fall'),
        ('KI/VI (7/8)', 'kitu/vitu', 'ki-/vi-', 'Ki-na-anguka / Vi-na-anguka', 'Thing falls / Things fall'),
        ('N/N (9/10)', 'nyumba/nyumba', 'i-/zi-', 'I-na-anguka / Zi-na-anguka', 'House falls / Houses fall'),
        ('U (11)', 'ukuta', 'u-', 'U-na-anguka', 'Wall falls'),
        ('PA (16)', 'mahali', 'pa-', 'Pa-na-kelewa', 'Place is understood'),
    ]
    g += hr(104)
    g += sh(112, 'NOUN CLASS TABLE — SUBJECT AGREEMENT')
    for i, (cls, example, pfx, verb_ex, gloss) in enumerate(classes_full):
        y = 122 + i * 14
        g += t(50, y, cls, 'middle', 'Lx')
        g += t(115, y, example, 'middle', 'Lx')
        g += t(165, y, pfx, 'middle', 'Lx')
        g += t(285, y, verb_ex, 'middle', 'Lx')
        g += t(415, y, gloss, 'middle', 'Lx')
    g += hr(222)

    # Tense system
    g += sh(230, 'TENSE SYSTEM — TENSE MARKERS IN VERB COMPLEX')
    g += t(240, 239, 'Tense is marked by an infix between subject prefix and verb root. Root stays constant.', 'middle', 'Ls')
    tenses = [
        ('-na-', 'present continuous', 'A-na-soma', 'He is reading'),
        ('-li-', 'simple past', 'A-li-soma', 'He read'),
        ('-ta-', 'future', 'A-ta-soma', 'He will read'),
        ('-me-', 'perfect', 'A-me-soma', 'He has read'),
        ('-ku-', 'past (negative/infinitive)', 'A-ku-soma', 'He used to read / to read'),
        ('-nge-', 'conditional', 'A-nge-soma', 'He would read'),
        ('-ngeli-', 'past conditional', 'A-ngeli-soma', 'He would have read'),
    ]
    for i, (marker, name, ex, gloss) in enumerate(tenses):
        y = 249 + i * 13
        g += t(50, y, marker, 'middle', 'Ls')
        g += t(120, y, name, 'middle', 'Lx')
        g += t(245, y, ex, 'middle', 'Lx')
        g += t(380, y, gloss, 'middle', 'Lx')
    g += hr(342)

    # Negation
    g += sh(350, 'NEGATION')
    g += t(240, 360, 'Negation changes the subject prefix: a- (pos.) → ha- (neg.) for M/WA class:', 'middle', 'Ls')
    g += t(240, 369, 'Anasoma (He reads) → Hasomi (He does not read) — note: negative present drops -na-, uses -i ending.', 'middle', 'Ls')
    g += t(240, 378, 'Negative past: Hakusoma (He did not read) · Negative future: Hatasoma (He will not read)', 'middle', 'Ls')
    g += hr(386)

    # Core vocab
    g += sh(394, 'CORE VOCABULARY — 25 WORDS WITH NOUN CLASS')
    vocab_sw = [
        ('ndiyo / hapana', 'M/WA', 'yes / no'),
        ('asante', '—', 'thank you'),
        ('tafadhali / samahani', '—', 'please / excuse me'),
        ('mimi / wewe', 'M/WA', 'I / you'),
        ('yeye / sisi', 'M/WA', 'he/she / we'),
        ('hii / hiyo', 'N class', 'this / that'),
        ('wapi', '—', 'where'),
        ('nini', '—', 'what'),
        ('nani', 'M/WA', 'who'),
        ('kwa nini', '—', 'why'),
        ('maji', 'MA (6)', 'water'),
        ('chakula', 'KI/VI (7)', 'food'),
        ('mtu / watu', 'M/WA (1/2)', 'person / people'),
        ('nyumba', 'N (9)', 'house'),
        ('njia', 'N (9)', 'path / way'),
        ('leo / jana', '—', 'today / yesterday'),
        ('kesho', '—', 'tomorrow'),
        ('kitabu / vitabu', 'KI/VI (7/8)', 'book / books'),
        ('lugha', 'N (9)', 'language'),
        ('dunia', 'N (9)', 'world'),
        ('kubwa / ndogo', '—', 'big / small'),
        ('nzuri / mbaya', '—', 'good / bad'),
        ('mpya / kale', 'M/MI', 'new / old'),
        ('siku zijazo / kesho', '—', 'future / tomorrow'),
        ('kumbuka', '—', 'remember (verb)'),
    ]
    for i, (sw, cls, eng) in enumerate(vocab_sw):
        y = 404 + i * 11
        col = i % 2
        cx = 80 if col == 0 else 320
        g += t(cx, y, sw, 'middle', 'Lx')
        g += t(cx + 90, y, cls, 'middle', 'Lx')
        g += t(cx + 140, y, eng, 'middle', 'Lx')

    yl = 404 + 25 * 11
    g += hr(yl + 2)
    g += sh(yl + 10, 'WORD ORDER AND ADJECTIVE AGREEMENT')
    g += t(240, yl + 20, 'SVO order: Mtoto anasoma kitabu. Child is-reading book. "The child is reading a book."', 'middle', 'Ls')
    g += t(240, yl + 29, 'Adjective follows noun and takes noun class prefix: kitabu -zuri → kitabu kizuri (a good book).', 'middle', 'Ls')

    g += footer('20', 'Swahili', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 20D — RUNNING TEXT ─────────────────────────────────────────────────

def build_20d():
    g = open_svg()
    g += t(240, 32, 'SWAHILI — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 20D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1
    g += sh(67, 'PASSAGE 1 — GREETING AND INTRODUCTION')
    g += t(240, 77, 'Habari  yako?   Nzuri  sana,  asante.  Karibu.', 'middle', 'L')
    g += t(240, 87, 'News-of you?   Good   very,   thanks.   Welcome.', 'middle', 'Lx')
    g += t(240, 95, '"How are you? Very well, thank you. Welcome."', 'middle', 'Ls')
    g += t(240, 105, 'Mimi  ni   binadamu.  Ninakuandikia   kutoka  zamani  zilizopita.', 'middle', 'L')
    g += t(240, 115, 'I     am   human.     I-write-to-you   from    times   which-passed.', 'middle', 'Lx')
    g += t(240, 123, '"I am a human. I write to you from times that have passed."', 'middle', 'Ls')
    g += hr(131)

    # Passage 2
    g += sh(139, 'PASSAGE 2 — NATURE')
    g += t(240, 149, 'Bahari  ni  kubwa,    lakini   moyo  wa  binadamu  ni  mkubwa  zaidi.', 'middle', 'L')
    g += t(240, 159, 'Ocean   is  big/great, but      heart of  human     is  bigger   more.', 'middle', 'Lx')
    g += t(240, 167, '"The ocean is great, but the heart of a human is greater still."', 'middle', 'Ls')
    g += t(240, 177, 'Mto   hauzuii     safari  —  mtu   hodari    huvuka.', 'middle', 'L')
    g += t(240, 187, 'River not-stops  journey —  person  capable  crosses.', 'middle', 'Lx')
    g += t(240, 195, '"A river does not stop a journey — a capable person crosses it."  — Swahili proverb', 'middle', 'Ls')
    g += hr(203)

    # Passage 3
    g += sh(211, 'PASSAGE 3 — MSEMO (SWAHILI PROVERB)')
    g += t(240, 221, 'Usiku  ukijua  siri,   mchana  ukifichue.', 'middle', 'L')
    g += t(240, 231, 'Night  you-know secret, daytime you-reveal-it.', 'middle', 'Lx')
    g += t(240, 239, '"What the night hides, the day reveals." — Swahili saying', 'middle', 'Ls')
    g += t(240, 249, 'Elimu  ni  nuru,    ujinga  ni  giza.', 'middle', 'L')
    g += t(240, 259, 'Knowledge is light,  ignorance is darkness.', 'middle', 'Lx')
    g += t(240, 267, '"Knowledge is light; ignorance is darkness."  — common Swahili wisdom', 'middle', 'Ls')
    g += hr(275)

    # Passage 4
    g += sh(283, 'PASSAGE 4 — INDEPENDENCE DECLARATION ECHO')
    g += t(240, 293, 'Uhuru  na  Umoja.  Tanzania  ilipata  uhuru  wake  mwaka  wa  elfu  moja,', 'middle', 'L')
    g += t(240, 303, 'Freedom and Unity.  Tanzania  received  freedom its   year   of  thousand one,', 'middle', 'Lx')
    g += t(240, 313, 'mia  tisa  sitini  na  moja.  Kumbukumbu  yake  inadumu  milele.', 'middle', 'L')
    g += t(240, 323, 'hundred nine  sixty  and  one.   Memory       its   endures   forever.', 'middle', 'Lx')
    g += t(240, 331, '"Freedom and Unity. Tanzania received independence in 1961. Its memory endures forever."', 'middle', 'Ls')
    g += hr(339)

    # Bridge phrase
    g += sh(347, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 357, 'Hii  ilitengenezwa  kwa  ajili  yako,  bure,  na  watu  waliokumbuka  mbele.', 'middle', 'L')
    g += t(240, 367, 'This was-made      for  sake   your,  free,  by  people who-remembered  ahead/forward.', 'middle', 'Lx')
    g += t(240, 377, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    g += hr(385)

    # Language note
    g += sh(393, 'LANGUAGE NOTE — "FORWARD / FUTURE" IN SWAHILI')
    g += t(240, 403, '"mbele" = forward, ahead, in front — the SAME word for spatial "in front" and temporal "ahead."', 'middle', 'L')
    g += t(240, 413, 'Swahili time is spatial: mbele (future/ahead), nyuma (past/behind) — identical to Malay/Indonesian.', 'middle', 'Ls')
    g += t(240, 422, '"siku zijazo" = "the days that will come" — formal word for future.  "kesho" = tomorrow/future.', 'middle', 'Ls')
    g += t(240, 431, '"kumbuka" = to remember · "waliokumbuka" = "who remembered" (relative clause with past tense).', 'middle', 'Ls')
    g += t(240, 440, '"bure" = free of charge / freely / without cost — the same word as "in vain" in some contexts.', 'middle', 'Ls')
    g += t(240, 449, '"ilitengenezwa" = it was made — passive voice: i- (N class) + li- (past) + tengenez- (make) + -wa (passive).', 'middle', 'Ls')
    g += hr(457)

    # Decoding note
    g += sh(465, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 475, 'Swahili uses the 26-letter Latin alphabet. One letter = one sound. Completely phonemic.', 'middle', 'Ls')
    g += t(240, 484, 'Every noun carries a class prefix — the prefix on verbs/adjectives tells you the noun class.', 'middle', 'Ls')
    g += t(240, 493, 'Stress is always on the second-to-last syllable of each word. No exceptions in native words.', 'middle', 'Ls')
    g += t(240, 502, 'Spoken across East and Central Africa; official in Tanzania, Kenya, Uganda, Rwanda, DRC.', 'middle', 'Ls')
    g += t(240, 511, 'Swahili was added as a United Nations working language in 2022 — a major living world language.', 'middle', 'Ls')
    g += t(240, 520, 'Consult Plate 20A for the script, digraphs, and noun class overview if starting from scratch.', 'middle', 'Ls')

    g += footer('20', 'Swahili', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate20a_swahili_script.svg': build_20a(),
        'plate20b_swahili_phonology.svg': build_20b(),
        'plate20c_swahili_grammar.svg': build_20c(),
        'plate20d_swahili_text.svg': build_20d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
