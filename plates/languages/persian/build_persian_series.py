#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Persian/Farsi plate series 23A–23D for Remember Forward."""

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
        '  .Lp { font-size:13px; }\n'
        '  .Lps{ font-size:10px; }\n'
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


# ─── PLATE 23A — SCRIPT ──────────────────────────────────────────────────────

def build_23a():
    g = open_svg()
    g += t(240, 32, 'PERSIAN / FARSI — SCRIPT · WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 23A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'PERSO-ARABIC SCRIPT — READ RIGHT TO LEFT')
    g += t(240, 79, 'Persian is written in a modified Arabic script (Perso-Arabic), reading RIGHT to LEFT.', 'middle', 'L')
    g += t(240, 89, '32 letters total (Arabic 28 + 4 Persian additions). Letters change form by position in word.', 'middle', 'Ls')
    g += t(240, 98, 'Cursive by nature: letters connect to their neighbors (some letters do not connect on the left).', 'middle', 'Ls')
    g += t(240, 107, 'Vowels: three long vowels written; three short vowels usually OMITTED in standard text (implied from context).', 'middle', 'Ls')
    g += hr(115)

    # The alphabet table — 32 letters with forms
    g += sh(124, 'THE 32 LETTERS — ISOLATED · INITIAL · MEDIAL · FINAL')
    g += t(240, 134, 'Each letter shown in isolated form with transliteration and name. Forms vary by position.', 'middle', 'Lx')

    letters = [
        ('\u0627', 'a/\u0101', 'alef'),
        ('\u0628', 'b', 'be'),
        ('\u067e', 'p', 'pe'),
        ('\u062a', 't', 'te'),
        ('\u062b', 's', 'se'),
        ('\u062c', 'j', 'jim'),
        ('\u0686', 'ch', 'che'),
        ('\u062d', 'h', 'he'),
        ('\u062e', 'kh', 'khe'),
        ('\u062f', 'd', 'dal'),
        ('\u0630', 'z', 'zal'),
        ('\u0631', 'r', 're'),
        ('\u0632', 'z', 'ze'),
        ('\u0698', 'zh', 'zhe'),
        ('\u0633', 's', 'sin'),
        ('\u0634', 'sh', 'shin'),
        ('\u0635', 's', 'sad'),
        ('\u0636', 'z', 'zad'),
        ('\u0637', 't', 'ta'),
        ('\u0638', 'z', 'za'),
        ('\u0639', '\u02bf', '\u02bfayn'),
        ('\u063a', 'gh', 'gheyn'),
        ('\u0641', 'f', 'fe'),
        ('\u0642', 'q', 'qaf'),
        ('\u06a9', 'k', 'kaf'),
        ('\u06af', 'g', 'gaf'),
        ('\u0644', 'l', 'lam'),
        ('\u0645', 'm', 'mim'),
        ('\u0646', 'n', 'nun'),
        ('\u0648', 'v/w/u\u0304', 'vav'),
        ('\u0647', 'h', 'he'),
        ('\u06cc', 'y/\u012b', 'ye'),
    ]

    # 4 columns of 8
    col_xs = [60, 180, 300, 420]
    col_data = [letters[i::4] for i in range(4)]
    # Reorder: left-to-right columns but note RTL reading
    g += t(240, 143, '(Note: Persian text shown below reads right-to-left)', 'middle', 'Lx')
    for ci, col in enumerate(col_data):
        cx = col_xs[ci]
        for ri, (char, trans, name) in enumerate(col):
            y = 152 + ri * 14
            g += t(cx, y, char, 'middle', 'Lp')
            g += t(cx, y + 8, f'{trans} · {name}', 'middle', 'Lx')
    g += hr(272)

    # The 4 Persian letters not in Arabic
    g += sh(280, 'FOUR PERSIAN LETTERS — NOT IN ARABIC')
    persian_only = [
        ('\u067e', 'pe /p/', 'p sound — not in Arabic'),
        ('\u0686', 'che /tʃ/', 'ch sound — "church"'),
        ('\u0698', 'zhe /ʒ/', 'zh sound — "measure"'),
        ('\u06af', 'gaf /ɡ/', 'g sound — hard g'),
    ]
    for i, (char, trans, desc) in enumerate(persian_only):
        cx = 70 + i * 100
        g += t(cx, 293, char, 'middle', 'Lp')
        g += t(cx, 303, trans, 'middle', 'Ls')
        g += t(cx, 312, desc, 'middle', 'Lx')
    g += hr(320)

    # Vowel markers (harakat)
    g += sh(329, 'VOWELS — SHORT (USUALLY OMITTED) AND LONG')
    g += t(240, 340, 'Short vowels: /a/ (zabar \u064e), /e/ (zir \u0650), /o/ (pish \u064f) — written only in religious texts, poetry, children\'s books', 'middle', 'Ls')
    g += t(240, 349, 'Long vowels (always written): \u0627 a\u0304 · \u06cc \u012b · \u0648 u\u0304 (u\u0304 also represents /v/ and /o/ in some positions)', 'middle', 'Ls')
    g += t(240, 358, 'hamze (\u0621): glottal stop — may appear on alef, vav, or ye; written \u0627\u0652/\u0624/\u0626', 'middle', 'Ls')
    g += hr(366)

    # Numerals
    g += sh(375, 'PERSIAN / EASTERN ARABIC NUMERALS')
    g += t(240, 386, 'Persian uses its own numeral glyphs (based on Eastern Arabic forms), not Western Arabic (0–9).', 'middle', 'Ls')
    nums = [
        ('\u06f0', '0'), ('\u06f1', '1'), ('\u06f2', '2'), ('\u06f3', '3'), ('\u06f4', '4'),
        ('\u06f5', '5'), ('\u06f6', '6'), ('\u06f7', '7'), ('\u06f8', '8'), ('\u06f9', '9'),
    ]
    for i, (persian_n, arabic_n) in enumerate(nums):
        cx = 45 + i * 40
        g += t(cx, 398, persian_n, 'middle', 'Lp')
        g += t(cx, 408, arabic_n, 'middle', 'Lx')
    g += hr(415)

    # Script history
    g += sh(424, 'SCRIPT HISTORY')
    g += t(240, 435, 'Old Persian (~600–300 BCE): cuneiform script — 36 signs, semi-syllabic, used for Achaemenid inscriptions.', 'middle', 'Ls')
    g += t(240, 444, 'Middle Persian / Pahlavi (~3rd c. BCE – 9th c. CE): Aramaic-derived script, 20 letters (highly ambiguous).', 'middle', 'Ls')
    g += t(240, 453, '7th–10th c. CE: Arab conquest → Perso-Arabic script adopted. Persian adapted Arabic letters, adding 4 new ones.', 'middle', 'Ls')
    g += t(240, 462, '10th c.: New Persian (Dari/Farsi) written in Perso-Arabic — Rudaki, Ferdowsi write the first great Persian poetry.', 'middle', 'Ls')
    g += t(240, 471, 'Perso-Arabic script also adopted by Urdu, Pashto, Ottoman Turkish, Uyghur, Kashmiri, and others.', 'middle', 'Ls')
    g += t(240, 480, 'Direction: RIGHT to LEFT. Numbers written left to right within RTL text.', 'middle', 'Ls')
    g += t(240, 489, 'Today: Farsi (Iran), Dari (Afghanistan), Tajik (uses Cyrillic in Tajikistan, Perso-Arabic elsewhere).', 'middle', 'Ls')

    g += footer('23', 'Persian', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 23B — PHONOLOGY ───────────────────────────────────────────────────

def build_23b():
    g = open_svg()
    g += t(240, 32, 'PERSIAN / FARSI — PHONOLOGY · SOUND SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 23B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'MODERN TEHRANI FARSI — STANDARD DIALECT')
    g += t(240, 79, 'Standard Persian (Farsi) is based on the Tehran dialect. 80+ million speakers across Iran, Afghanistan, Tajikistan.', 'middle', 'L')
    g += t(240, 89, 'Persian is an Indo-European language (Iranian branch) — related to English, Latin, and Sanskrit.', 'middle', 'Ls')
    g += hr(97)

    # Vowels
    g += sh(106, 'VOWEL SYSTEM — 6 VOWELS')
    g += t(240, 117, 'Modern Farsi has 6 vowels (the Classical long/short distinction has collapsed in Tehrani dialect).', 'middle', 'L')
    vowels = [
        ('/ɑː/', '\u0627', 'a\u0304', 'low back, like "father" — \u0622b a\u0304b "water"'),
        ('/æ/',  '(zabar)', 'a', 'low front, like "cat" — \u0628\u062f bad "bad"'),
        ('/e/',  '(zir)', 'e', 'mid front, like "bed" — \u062f\u0644 del "heart"'),
        ('/i/',  '\u06cc', 'i\u0304/i', 'high front, like "see" — \u0634\u06cc\u0631 shi\u0304r "lion"'),
        ('/o/',  '(pish)', 'o', 'mid back rounded — \u062f\u0633\u062a dost "friend"'),
        ('/u/',  '\u0648', 'u\u0304/u', 'high back rounded — \u06a9\u0648\u062f ku\u0304d "child"'),
    ]
    g += t(50, 127, 'IPA', 'middle', 'Lx')
    g += t(100, 127, 'Script', 'middle', 'Lx')
    g += t(145, 127, 'Translit', 'middle', 'Lx')
    g += t(340, 127, 'Description + example', 'middle', 'Lx')
    for i, (ipa, scr, tr, desc) in enumerate(vowels):
        y = 136 + i * 12
        g += t(50, y, ipa, 'middle', 'Lx')
        g += t(100, y, scr, 'middle', 'Lps')
        g += t(145, y, tr, 'middle', 'Lx')
        g += t(320, y, desc, 'middle', 'Lx')
    g += hr(212)

    # Consonants
    g += sh(221, 'CONSONANT INVENTORY — 23 CONSONANTS')
    cons = [
        ('p b', '/p b/', 'bilabial stops', 'pa\u0304 "foot", ba\u0304d "wind"'),
        ('t d', '/t d/', 'alveolar stops', 'ta\u0304j "crown", da\u0304r "tree"'),
        ('k g', '/k ɡ/', 'velar stops', 'ka\u0304r "work", gol "flower"'),
        ('\u02bc', '/\u02bc/', 'glottal stop', '\u0639ayn — in Arabic loans'),
        ('f v', '/f v/', 'labiodentals', 'fa\u0304rs "Persia", va\u0304\u017e\u025b "clear"'),
        ('s z', '/s z/', 'alveolar fricatives', 'sa\u0304l "year", za\u0304r "gold"'),
        ('sh zh', '/ʃ ʒ/', 'palato-alveolar', 'sha\u0304h "king", \u017eha\u0304n "world"'),
        ('kh', '/x/', 'velar fricative', 'kha\u0304ne "house" — like German "Bach"'),
        ('gh', '/ɣ/', 'voiced velar fricative', 'gha\u0304r "cave" — voiced "Bach"'),
        ('q', '/q/', 'uvular stop', 'qa\u0304lam "pen" — Arabic loans'),
        ('h', '/h/', 'glottal fricative', 'ha\u0304r "each"'),
        ('m n', '/m n/', 'nasals', 'ma\u0304h "moon", na\u0304m "name"'),
        ('l r', '/l r/', 'lateral / tap', 'la\u0304b "edge", ra\u0304h "road"'),
        ('y', '/j/', 'palatal glide', 'ya\u0304r "friend"'),
        ('ch', '/tʃ/', 'affricate', 'cha\u0304y "tea"'),
        ('j', '/dʒ/', 'voiced affricate', 'jangal "forest"'),
    ]
    for i, (ltr, ipa, label, note) in enumerate(cons):
        y = 231 + i * 11
        g += t(40,  y, ltr, 'middle', 'Ls')
        g += t(95,  y, ipa, 'middle', 'Lx')
        g += t(175, y, label, 'middle', 'Lx')
        g += t(355, y, note, 'middle', 'Lx')
    g += hr(410)

    # Stress
    g += sh(419, 'STRESS AND PROSODY')
    g += t(240, 430, 'Stress: usually on the LAST syllable of the word (final stress), with exceptions for enclitics and some suffixes.', 'middle', 'L')
    g += t(240, 440, 'Prefixed verbs: stress shifts to the prefix (negative mi- or na- takes stress: NA-miram "I don\'t go").', 'middle', 'Ls')
    g += t(240, 449, 'Ezafe construction (see grammar plate) is unstressed — functions as a clitic.', 'middle', 'Ls')
    g += hr(457)

    # Key features
    g += sh(466, 'KEY PHONOLOGICAL FEATURES')
    g += t(240, 477, 'No tones. No consonant clusters at syllable onset in native words (up to 2 in codas).', 'middle', 'Ls')
    g += t(240, 486, 'Syllable structure: (C)V(C)(C) — open syllables preferred in native vocabulary.', 'middle', 'Ls')
    g += t(240, 495, '/q/ and glottal stop /\u02bc/: inherited from Arabic loanwords — some speakers merge /q/ with /k/ or /gh/.', 'middle', 'Ls')
    g += t(240, 504, 'Persian /r/ is a tap [ɾ] (single-contact trill), similar to Spanish "pero".', 'middle', 'Ls')
    g += t(240, 513, 'Word-final consonant clusters: possible (e.g. dast /dæst/ "hand", mard /mærd/ "man").', 'middle', 'Ls')
    g += t(240, 522, 'Colloquial Tehran: /\u0251\u02d0/ often shortens to /\u00e6/, /ou\u0306/ diphthong emerges from /av/ — significant dialect variation.', 'middle', 'Ls')
    g += t(240, 531, 'Borrowed Arabic emphatic consonants /s\u0330 z\u0330 t\u0330 \u0292\u0330/ merged with plain counterparts in most spoken Persian.', 'middle', 'Ls')

    g += footer('23', 'Persian', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 23C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_23c():
    g = open_svg()
    g += t(240, 32, 'PERSIAN / FARSI — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 23C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'SOV LANGUAGE — VERB-FINAL, POSTPOSITIONS')
    g += t(240, 79, 'Persian is SOV (Subject–Object–Verb). Verb comes last. No grammatical gender. No case endings on nouns.', 'middle', 'L')
    g += t(240, 89, 'man sib mikharam. (I apple buy-PRES.1SG) = "I am buying an apple."', 'middle', 'Ls')
    g += t(240, 98, 'man = I · sib = apple · mi- = present prefix · kharam = buy-1sg', 'middle', 'Lx')
    g += hr(106)

    # Ezafe
    g += sh(115, 'THE EZAFE CONSTRUCTION — NOUN CHAINS')
    g += t(240, 126, 'Ezafe (-e/-ye after vowel): links noun + adjective OR noun + possessor. Written as short /e/ (often omitted in script).', 'middle', 'L')
    g += t(240, 136, 'keta\u0304b-e khub = "good book" (book-EZ good) — adjective FOLLOWS noun, joined by ezafe', 'middle', 'Ls')
    g += t(240, 145, 'keta\u0304b-e ma\u0304n = "my book" (book-EZ I) — possessor follows, joined by ezafe', 'middle', 'Ls')
    g += t(240, 154, 'keta\u0304b-e khub-e ma\u0304n = "my good book" — chains extend: book-EZ good-EZ my', 'middle', 'Ls')
    g += hr(162)

    # Verb conjugation
    g += sh(171, 'VERB CONJUGATION — kardan "to do/make" (present stem: kon-)')
    present = [
        ('1sg', 'mikonam', 'I do / am doing'),
        ('2sg', 'mikoni', 'you do'),
        ('3sg', 'mikonad', 'he/she/it does'),
        ('1pl', 'mikonim', 'we do'),
        ('2pl', 'mikonid', 'you (pl) do'),
        ('3pl', 'mikonand', 'they do'),
    ]
    past = [
        ('1sg', 'kardam', 'I did / made'),
        ('2sg', 'kardi', 'you did'),
        ('3sg', 'kard', 'he/she did'),
        ('1pl', 'kardim', 'we did'),
        ('2pl', 'kardid', 'you (pl) did'),
        ('3pl', 'kardand', 'they did'),
    ]
    g += t(100, 181, 'Present (mi- + stem + ending)', 'middle', 'Lx')
    g += t(360, 181, 'Simple past (past stem + ending)', 'middle', 'Lx')
    for i, ((p1, f1, gl1), (p2, f2, gl2)) in enumerate(zip(present, past)):
        y = 190 + i * 11
        g += t(55, y, p1, 'middle', 'Lx')
        g += t(120, y, f1, 'middle', 'Ls')
        g += t(195, y, gl1, 'middle', 'Lx')
        g += t(300, y, p2, 'middle', 'Lx')
        g += t(365, y, f2, 'middle', 'Ls')
        g += t(440, y, gl2, 'middle', 'Lx')
    g += t(240, 258, 'Negation: na- prefix before verb: nami-konam "I do not do" · nakard "he did not do"', 'middle', 'Ls')
    g += hr(266)

    # Grammar features
    g += sh(275, 'KEY GRAMMATICAL FEATURES')
    g += t(240, 286, 'ra (\u0631\u0627): direct object marker — added to definite/specific direct objects: "I bought the apple" → sib-ra kharidam', 'middle', 'Ls')
    g += t(240, 295, 'No articles ("a" / "the") in formal Persian; -i suffix indicates indefinite: ketab-i "a book"', 'middle', 'Ls')
    g += t(240, 304, 'Plural: -ha\u0304 suffix for all nouns: keta\u0304b-ha\u0304 "books" · a\u0304dam-ha\u0304 "people"', 'middle', 'Ls')
    g += t(240, 313, 'Relative clause: ke "that/which/who" — ma\u0304rdi ke a\u0304mad "the man who came"', 'middle', 'Ls')
    g += t(240, 322, 'Verb-object compounds: very common — del-tan-e man shodeh "I am missing you" (lit. "my heart became tight")', 'middle', 'Ls')
    g += hr(330)

    # Core vocabulary
    g += sh(339, 'CORE VOCABULARY — 25 WORDS')
    vocab = [
        ('\u0628\u0644\u0647 / \u0646\u0647', 'bale / na', 'yes / no'),
        ('\u0645\u0646 / \u062a\u0648', 'man / to', 'I / you'),
        ('\u0627\u06cc\u0646 / \u0622\u0646', 'in / a\u0304n', 'this / that'),
        ('\u06a9\u062c\u0627', 'koja\u0304', 'where'),
        ('\u0686\u06cc', 'chi', 'what'),
        ('\u06a9\u06cc', 'ki', 'who'),
        ('\u0686\u0631\u0627', 'chera\u0304', 'why'),
        ('\u0622\u0628', 'a\u0304b', 'water'),
        ('\u0622\u062a\u0634', 'a\u0304tash', 'fire'),
        ('\u062e\u0627\u06a9', 'kha\u0304k', 'earth/soil'),
        ('\u0622\u062f\u0645', 'a\u0304dam', 'person/human'),
        ('\u062f\u0648\u0633\u062a', 'dust', 'friend'),
        ('\u06a9\u062a\u0627\u0628', 'keta\u0304b', 'book'),
        ('\u0632\u0645\u0627\u0646', 'zama\u0304n', 'time'),
        ('\u0645\u0627\u0647', 'ma\u0304h', 'moon/month'),
        ('\u0633\u062a\u0627\u0631\u0647', 'seta\u0304re', 'star'),
        ('\u062f\u0644', 'del', 'heart'),
        ('\u0639\u0634\u0642', 'eshq', 'love'),
        ('\u0622\u0632\u0627\u062f', 'a\u0304za\u0304d', 'free/freedom'),
        ('\u06cc\u0627\u062f', 'ya\u0304d', 'memory/remembrance'),
        ('\u0622\u06cc\u0646\u062f\u0647', 'a\u0304yande', 'future'),
        ('\u062f\u06cc\u0631\u0648\u0632', 'diru\u0304z', 'yesterday'),
        ('\u0641\u0631\u062f\u0627', 'farda\u0304', 'tomorrow/future'),
        ('\u062e\u0648\u0628 / \u0628\u062f', 'khub / bad', 'good / bad'),
        ('\u0647\u0645\u0647 \u0686\u06cc\u0632', 'hame chiz', 'everything'),
    ]
    col_va = [40, 115, 210]
    col_vb = [265, 340, 435]
    half = 13
    for i, (persian, translit, eng) in enumerate(vocab):
        if i < half:
            y = 349 + i * 10
            g += t(col_va[0], y, persian, 'middle', 'Lps')
            g += t(col_va[1], y, translit, 'middle', 'Lx')
            g += t(col_va[2], y, eng, 'middle', 'Lx')
        else:
            y = 349 + (i - half) * 10
            g += t(col_vb[0], y, persian, 'middle', 'Lps')
            g += t(col_vb[1], y, translit, 'middle', 'Lx')
            g += t(col_vb[2], y, eng, 'middle', 'Lx')
    g += hr(483)

    g += sh(492, 'PERSIAN LOANWORDS IN OTHER LANGUAGES')
    g += t(240, 503, 'Persian was the language of high culture, trade, and administration across a vast region for centuries.', 'middle', 'L')
    g += t(240, 513, 'English loans: check (chess piece), lemon, jasmine, paradise (Av. pairi-daeza "walled garden"), azure, caravan', 'middle', 'Ls')
    g += t(240, 522, 'Urdu, Hindi, Turkish, Azerbaijani, Armenian, Georgian all contain large Persian vocabulary layers.', 'middle', 'Ls')
    g += t(240, 531, 'Arabic borrowed from Persian too: shir (lion), khandaq (trench), zanjir (chain).', 'middle', 'Ls')
    g += t(240, 540, 'Persian was the court language of the Mughal Empire (India, 1526–1858) and the Ottoman court.', 'middle', 'Ls')

    g += footer('23', 'Persian', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 23D — RUNNING TEXT ─────────────────────────────────────────────────

def build_23d():
    g = open_svg()
    g += t(240, 32, 'PERSIAN / FARSI — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 23D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # RTL note
    g += t(240, 68, 'Note: Persian text reads RIGHT TO LEFT. Transliteration and translation read left to right below each line.', 'middle', 'Ls')
    g += hr(76)

    # Passage 1 — Hafez
    g += sh(85, 'PASSAGE 1 — HAFEZ, DIVAN (14th c.)')
    g += t(240, 97, '\u0627\u0644\u0627 \u06cc\u0627 \u0627\u06cc\u0647\u0627 \u0633\u0627\u0642\u06cc\u0627 \u0627\u062f\u0631 \u06a9\u0623\u0633\u0627 \u0648 \u0646\u0627\u0648\u0644\u0647\u0627', 'middle', 'Lp')
    g += t(240, 109, 'Ala ya ayyu-ha saqi adri kasan wa nawil-ha', 'middle', 'Lx')
    g += t(240, 118, 'O you, O cup-bearer, bring the cup and pass it around', 'middle', 'Ls')
    g += t(240, 127, '\u06a9\u0647 \u0639\u0634\u0642 \u0622\u0633\u0627\u0646 \u0646\u0645\u0648\u062f \u0627\u0648\u0644 \u0648\u0644\u06cc \u0627\u0641\u062a\u0627\u062f \u0645\u0634\u06a9\u0644\u0647\u0627', 'middle', 'Lp')
    g += t(240, 139, 'ke eshq a\u0304sa\u0304n namud avval vali oftad moshkelha\u0304', 'middle', 'Lx')
    g += t(240, 148, '"Love seemed easy at first, but then the difficulties arose."', 'middle', 'Ls')
    g += hr(156)

    # Passage 2 — Rumi
    g += sh(165, 'PASSAGE 2 — RUMI, MASNAVI I.1 (13th c.)')
    g += t(240, 177, '\u0628\u0634\u0646\u0648 \u0627\u06cc\u0646 \u0646\u06cc \u0686\u0648\u0646 \u0634\u06a9\u0627\u06cc\u062a \u0645\u06cc\u200c\u06a9\u0646\u062f', 'middle', 'Lp')
    g += t(240, 189, 'Beshno in ney chon shekayyat mikonad', 'middle', 'Lx')
    g += t(240, 198, 'Listen, how this reed-flute tells a tale of separations', 'middle', 'Ls')
    g += t(240, 207, '\u0627\u0632 \u062c\u062f\u0627\u06cc\u06cc\u200c\u0647\u0627 \u062d\u06a9\u0627\u06cc\u062a \u0645\u06cc\u200c\u06a9\u0646\u062f', 'middle', 'Lp')
    g += t(240, 219, 'Az jodayiha\u0304 heka\u0304yat mikonad', 'middle', 'Lx')
    g += t(240, 228, '"Listen to this reed, how it tells a tale — of separations it narrates."', 'middle', 'Ls')
    g += hr(236)

    # Passage 3 — Ferdowsi
    g += sh(245, 'PASSAGE 3 — FERDOWSI, SHAHNAMEH (c. 1000 CE)')
    g += t(240, 257, '\u062a\u0648\u0627\u0646\u0627 \u0628\u0648\u062f \u0647\u0631 \u06a9\u0647 \u062f\u0627\u0646\u0627 \u0628\u0648\u062f', 'middle', 'Lp')
    g += t(240, 269, 'Tava\u0304na\u0304 bud har ke da\u0304na\u0304 bud', 'middle', 'Lx')
    g += t(240, 278, 'Powerful was he who was wise', 'middle', 'Ls')
    g += t(240, 287, '\u062f\u0627\u0646\u0634 \u06cc\u06a9\u06cc \u0627\u0633\u062a \u0648 \u062a\u0648\u0627\u0646\u0627\u06cc\u06cc \u062f\u06af\u0631', 'middle', 'Lp')
    g += t(240, 299, 'Da\u0304nesh yeki-st va tava\u0304na\u0304yi digar', 'middle', 'Lx')
    g += t(240, 308, '"Knowledge is one thing and power is another — Powerful was he who was wise."', 'middle', 'Ls')
    g += hr(316)

    # Passage 4 — proverb
    g += sh(325, 'PASSAGE 4 — PERSIAN PROVERBS')
    g += t(240, 336, '\u0639\u0645\u0631 \u062f\u0631 \u062c\u0648\u06cc\u0627\u06cc \u06cc\u0627\u0631 \u06af\u0630\u0631\u062f', 'middle', 'Lp')
    g += t(240, 348, 'Omr dar juyay-e ya\u0304r gozasht.', 'middle', 'Lx')
    g += t(240, 357, '"Life passed in the search for a friend." — on the value of human connection', 'middle', 'Ls')
    g += t(240, 367, '\u0647\u0631 \u06a9\u06cc \u0628\u06cc\u0631 \u0634\u062f \u0627\u0645\u06cc\u062f\u0648\u0627\u0631\u0634 \u062c\u0648\u0627\u0646 \u0634\u062f', 'middle', 'Lp')
    g += t(240, 379, 'Har ke pir shod omidva\u0304rash java\u0304n shod.', 'middle', 'Lx')
    g += t(240, 388, '"Whoever grew old, their hope grew young." — on the endurance of hope', 'middle', 'Ls')
    g += hr(396)

    # Bridge phrase
    g += sh(405, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 417, '\u0627\u06cc\u0646 \u067e\u06cc\u0627\u0645 \u0628\u0631\u0627\u06cc \u0634\u0645\u0627\u060c \u0622\u0632\u0627\u062f\u0627\u0646\u0647\u060c \u062a\u0648\u0633\u0637 \u06a9\u0633\u0627\u0646\u06cc \u0633\u0627\u062e\u062a\u0647 \u0634\u062f\u0647 \u06a9\u0647 \u0622\u06cc\u0646\u062f\u0647 \u0631\u0627 \u0628\u0647 \u06cc\u0627\u062f \u0645\u06cc\u200c\u0633\u067e\u0631\u062f\u0646\u062f.', 'middle', 'Lps')
    g += t(240, 430, 'In peyya\u0304m bara\u0304ye shoma\u0304, a\u0304za\u0304da\u0304ne, tavasat-e kesa\u0304ni sakhte shode ke a\u0304yande ra\u0304 be ya\u0304d mi-sperand.', 'middle', 'Lx')
    g += t(240, 440, '"This message was made for you, freely, by people who entrusted the future to memory."', 'middle', 'Ls')
    g += hr(448)

    g += sh(457, 'LANGUAGE NOTE — "FUTURE" IN PERSIAN')
    g += t(240, 468, 'Persian has two key words for future: a\u0304yande (\u0622\u06cc\u0646\u062f\u0647) = "the coming one" (participle of a\u0304madan "to come")', 'middle', 'L')
    g += t(240, 478, 'and farda\u0304 (\u0641\u0631\u062f\u0627) = "tomorrow" — the concrete near future, also used poetically for "the future" in general.', 'middle', 'Ls')
    g += t(240, 488, 'The phrase uses a\u0304yande ra\u0304 be ya\u0304d sperand: "committed the future to memory" — ra\u0304 is the direct object marker.', 'middle', 'Ls')
    g += t(240, 498, 'ya\u0304d (\u06cc\u0627\u062f): "memory / remembrance" — the root of ya\u0304da\u0304var "memorable", ya\u0304dbud "memorial".', 'middle', 'Ls')
    g += t(240, 508, 'a\u0304za\u0304da\u0304ne (\u0622\u0632\u0627\u062f\u0627\u0646\u0647): "freely" — from a\u0304za\u0304d "free" + -a\u0304ne (adverbial suffix). a\u0304za\u0304d derives from Old Persian.', 'middle', 'Ls')
    g += hr(517)

    g += sh(526, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 537, 'Persian is spoken by ~80 million people as a first language; ~110 million total. Three main varieties:', 'middle', 'Ls')
    g += t(240, 546, 'Farsi (Iran), Dari (Afghanistan), Tajik (Tajikistan — written in Cyrillic script since Soviet era).', 'middle', 'Ls')
    g += t(240, 555, 'Script: Perso-Arabic, reading right to left. If unfamiliar, consult Plate 23A for the full letter table.', 'middle', 'Ls')
    g += t(240, 564, 'Persian is an Indo-European language: it is related to English, Latin, Greek, Sanskrit, and Russian.', 'middle', 'Ls')
    g += t(240, 573, 'Persian literature is among the oldest continuous literary traditions: Ferdowsi\'s Shahnameh (c. 1000 CE)', 'middle', 'Ls')
    g += t(240, 582, 'contains 50,000 couplets — one of the longest epic poems in world literature.', 'middle', 'Ls')

    g += footer('23', 'Persian', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate23a_persian_script.svg': build_23a(),
        'plate23b_persian_phonology.svg': build_23b(),
        'plate23c_persian_grammar.svg': build_23c(),
        'plate23d_persian_text.svg': build_23d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
