#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Japanese / Zhuang alt plate series 18A–18D for Remember Forward.
Secondary language: Zhuang (壮语 / Cuengh) — largest minority language of China,
spoken primarily in Guangxi Zhuang Autonomous Region, ~17 million speakers.
Geographic basis: All nearest major neighbors of Japan (Mandarin, Korean, Russian,
Mongolian) are already in the series. Expanded to ~1500mi radius from Tokyo/Osaka
reaches the south China coast including Guangxi (Zhuang homeland) ~2000km.
Zhuang: Tai-Kadai family, tonal, SVO, closest relative of Thai.
Written in Zhuang Latin alphabet (standardized 1957, revised 1982).
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


# ─── PLATE 18A ALT — SCRIPT ───────────────────────────────────────────────────

def build_18a_alt():
    g = open_svg()
    g += t(240, 30, 'JAPANESE + ZHUANG \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 18A \u00b7 REMEMBER FORWARD \u00b7 EXPANDED ~1500MI RADIUS', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'JAPANESE \u2014 THREE SCRIPTS USED SIMULTANEOUSLY')
    g += t(240, 73, 'Japanese writing uses THREE scripts at once: Hiragana, Katakana, and Kanji (Chinese characters).', 'middle', 'Ls')
    g += t(240, 82, 'A single sentence may contain all three: \u79c1\u306f\u30b3\u30fc\u30d2\u30fc\u304c\u597d\u304d\u3067\u3059. (Watashi wa k\u014dhii ga suki desu. = I like coffee.)', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'HIRAGANA \u2014 46 SYLLABLE CHARACTERS')
    g += t(240, 108, 'Hiragana: cursive syllabary for native Japanese words, grammatical particles, verb/adjective endings.', 'middle', 'Ls')
    hira_rows = [
        '\u3042\u3044\u3046\u3048\u304a  (a i u e o)',
        '\u304b\u304d\u304f\u3051\u3053  (ka ki ku ke ko)',
        '\u3055\u3057\u3059\u305b\u305d  (sa shi su se so)',
        '\u305f\u3061\u3064\u3066\u3068  (ta chi tsu te to)',
        '\u306a\u306b\u306c\u306d\u306e  (na ni nu ne no)',
        '\u306f\u3072\u3075\u3078\u307b  (ha hi fu he ho)',
        '\u307e\u307f\u3080\u3081\u3082  (ma mi mu me mo)',
        '\u3084\u3086\u3088        (ya yu yo)',
        '\u3089\u308a\u308b\u308c\u308d  (ra ri ru re ro)',
        '\u308f\u3092\u3093      (wa wo n)',
    ]
    for i, row in enumerate(hira_rows):
        g += t(240, 118 + i * 11, row, 'middle', 'Ls')
    g += hr(230)

    g += sh(238, 'KATAKANA \u2014 46 CHARACTERS FOR FOREIGN WORDS')
    g += t(240, 248, 'Katakana: angular syllabary. Used for: loanwords, foreign names, scientific terms, sound effects.', 'middle', 'Ls')
    kata_sample = '\u30a2\u30a4\u30a6\u30a8\u30aa \u30ab\u30ad\u30af\u30b1\u30b3 \u30b5\u30b7\u30b9\u30bb\u30bd \u30bf\u30c1\u30c4\u30c6\u30c8'
    g += t(240, 258, kata_sample, 'middle', 'Ls')
    g += t(240, 268, 'K\u014dhii (\u30b3\u30fc\u30d2\u30fc) = coffee \u00b7 Terebi (\u30c6\u30ec\u30d3) = TV \u00b7 Aisu kr\u012bmu (\u30a2\u30a4\u30b9\u30af\u30ea\u30fc\u30e0) = ice cream', 'middle', 'Lx')
    g += hr(276)

    g += sh(284, 'KANJI \u2014 CHINESE-DERIVED LOGOGRAPHS')
    g += t(240, 294, 'Kanji: ~2000 in standard use (j\u014dy\u014d kanji). Each represents a morpheme, often with multiple readings.', 'middle', 'Ls')
    kanji = [('\u6c34','mizu/sui','water'), ('\u706b','hi/ka','fire'), ('\u571f','tsuchi/do','earth'),
             ('\u4eba','hito/jin','person'), ('\u6708','tsuki/getsu','moon'), ('\u672a\u6765','mirai','future')]
    for i, (k, rom, en) in enumerate(kanji):
        col = i % 3; row = i // 3
        x = 65 + col * 130; y = 304 + row * 14
        g += t(x, y, k, 'middle', 'L')
        g += t(x, y + 8, f'{rom} = {en}', 'middle', 'Lx')

    g += sec_divider(338, 'SECONDARY \u2014 ZHUANG (CUENGH / \u58EE\u8BED) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(364, 'ZHUANG \u2014 LATIN ALPHABET (STANDARD ZHUANG SCRIPT)')
    g += t(240, 374, 'Zhuang uses a Latin-based alphabet standardized in 1957 (revised 1982). 26 letters + tone letters.', 'middle', 'Ls')
    g += t(240, 383, 'Before standardization: many Zhuang speakers used a script called Sawndip \u2014 Chinese-style characters.', 'middle', 'Lx')
    g += t(240, 392, 'Sawndip: borrowed Chinese characters with new phonetic/semantic values for Zhuang sounds. Still in use.', 'middle', 'Lx')
    g += hr(400)

    g += sh(408, 'ZHUANG TONE MARKING \u2014 LETTER-BASED SYSTEM')
    g += t(240, 418, 'Tones marked by adding consonant letters at end of syllable: z=tone1, j=tone2, x=tone3, etc.', 'middle', 'Ls')
    tones = [
        ('(no mark)', 'Tone 1 (level high): ma (horse/sesame)'),
        ('-z', 'Tone 2 (rising): maz (scold)'),
        ('-j', 'Tone 3 (dipping): maj (hemp)'),
        ('-x', 'Tone 4 (low): max (ant)'),
        ('-q', 'Tone 5 (low checked): maq (rice)'),
        ('-h', 'Tone 6 (high falling): mah (go)'),
    ]
    for i, (mark, desc) in enumerate(tones):
        y = 428 + i * 10
        g += t(75, y, mark, 'middle', 'Ls')
        g += t(290, y, desc, 'middle', 'Lx')
    g += hr(497)

    g += sh(505, 'SCRIPT BRIDGE \u2014 SINOGRAPHIC ROOTS, LATIN FUTURE')
    g += t(240, 515, 'Japanese: adapted Chinese characters (kanji) ~5th c. CE. Added two native syllabaries on top.', 'middle', 'Ls')
    g += t(240, 524, 'Zhuang: created Sawndip (Chinese-style characters) independently for Zhuang sounds. Now uses Latin.', 'middle', 'Lx')
    g += t(240, 533, 'Both cultures demonstrate the same pattern: Chinese script adopted, then adapted, then supplemented.', 'middle', 'Lx')

    g += footer('18', 'Japanese', 'Zhuang', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 18B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_18b_alt():
    g = open_svg()
    g += t(240, 30, 'JAPANESE + ZHUANG \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 18B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'JAPANESE PHONOLOGY \u2014 MORA-TIMED, PITCH ACCENT')
    g += t(240, 73, 'Japanese is mora-timed (not syllable-timed). Each mora takes equal time: ka, ki, ku, ke, ko each = 1 mora.', 'middle', 'Ls')
    g += t(240, 82, 'Long vowels = 2 morae: k\u014dhi (k\u014d = 2, h = 1, i = 1 = 4 morae). Double consonants (geminate) also = 2 morae.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'JAPANESE PITCH ACCENT')
    g += t(240, 108, 'Japanese has pitch accent (not tonal in the Mandarin sense): words have a \u201cdrop\u201d point from H to L.', 'middle', 'Ls')
    pitch = [
        ('\u96e8 (ame)', 'H-L: rain', '\u5929\u6c17 (tenki) H-HL-L: weather'),
        ('\u4e57 (ame)', 'L-H: candy', '\u7ae5\u5fc3 (d\u014dsin) L-HH-L: childlike'),
    ]
    for i, (w1, p1, w2) in enumerate(pitch):
        y = 118 + i * 11
        g += t(80, y, w1, 'middle', 'Ls')
        g += t(200, y, p1, 'middle', 'Lx')
        g += t(360, y, w2, 'middle', 'Lx')
    g += hr(145)

    g += sh(153, 'JAPANESE CONSONANTS AND SPECIAL SOUNDS')
    jcons = [
        ('/ts/', 'tsu (\u3064): /tsu/ \u2014 the only /ts/ onset in standard Japanese'),
        ('/t\u0283/', 'chi (\u3061): /t\u0283i/ \u2014 not /ti/; palatal affricate before i'),
        ('/\u0266/', 'fu (\u3075): bilabial fricative \u2014 not /f/ but close; lips approach without full contact'),
        ('/n\u0307/', 'n (\u3093): syllabic nasal; a full mora; assimilates to following consonant place'),
        ('/\u0279/', 'r (\u3089): a flap, neither English r nor l. Between the two.'),
    ]
    for i, (ipa, desc) in enumerate(jcons):
        y = 163 + i * 10
        g += t(65, y, ipa, 'middle', 'Lx')
        g += t(290, y, desc, 'middle', 'Lx')
    g += hr(220)

    g += sh(228, 'JAPANESE VOWELS \u2014 5 PURE VOWELS')
    g += t(240, 238, 'Japanese has exactly 5 vowels: /a i u e o/. Short and long forms. No diphthongs (except in some loans).', 'middle', 'Ls')
    g += t(240, 247, '/u/ is unrounded (more like /\u026f/): lips not rounded. Distinctive from English /u\u02d0/.', 'middle', 'Lx')

    g += sec_divider(257, 'SECONDARY \u2014 ZHUANG (CUENGH) \u2014 PHONOLOGY')

    g += sh(283, 'ZHUANG PHONOLOGY \u2014 6 TONES (STANDARD DIALECT)')
    g += t(240, 293, 'Standard Zhuang (Wuming dialect) has 6 tones. Other dialects have up to 9 tones.', 'middle', 'Ls')
    ztones = [
        ('Tone 1 (unmarked)', 'mid-high level /\u02e6/: ma (horse)'),
        ('Tone 2 (-z)', 'high rising /\u02e7\u02e5/: maz (scold)'),
        ('Tone 3 (-j)', 'mid dipping /\u02e8\u02e6/: maj (hemp)'),
        ('Tone 4 (-x)', 'low falling /\u02e9/: max (ant)'),
        ('Tone 5 (-q)', 'low short checked: maq (rice) \u2014 glottal stop coda'),
        ('Tone 6 (-h)', 'high short checked: mah (go) \u2014 /h/ coda'),
    ]
    for i, (name, desc) in enumerate(ztones):
        y = 303 + i * 10
        g += t(120, y, name, 'middle', 'Lx')
        g += t(330, y, desc, 'middle', 'Lx')
    g += hr(370)

    g += sh(378, 'ZHUANG CONSONANTS')
    g += t(240, 388, 'Zhuang has rich consonant inventory: /p b d g m n \u014b l r h/ plus aspirated /p\u02b0 t\u02b0 k\u02b0/.', 'middle', 'Ls')
    g += t(240, 397, 'Distinctive: labial-velar /kw gw/ \u2014 shared with Hausa, Igbo, and other languages worldwide.', 'middle', 'Lx')
    g += t(240, 406, 'Implosives: some dialects have /\u0253 \u0257/ (bilabial/alveolar implosives). Shared feature with West African languages.', 'middle', 'Lx')
    g += hr(414)

    g += sh(422, 'PHONOLOGICAL BRIDGE \u2014 TWO TONAL NEIGHBORS')
    comp = [
        ('Feature', 'Japanese', 'Zhuang'),
        ('Tonal', 'Pitch accent (2 levels)', '6 tones (9 in some dialects)'),
        ('Syllable', 'Mora-timed (C)V(N)', 'CV(C) open/closed'),
        ('Vowels', '5 pure vowels', '6+ vowels'),
        ('r-sound', 'Flap /\u027e/', 'Trill /r/ or flap'),
        ('Clustering', 'None (pure CV)', 'Initial clusters in some dialects'),
    ]
    for i, row in enumerate(comp):
        y = 432 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('18', 'Japanese', 'Zhuang', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 18C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_18c_alt():
    g = open_svg()
    g += t(240, 30, 'JAPANESE + ZHUANG \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 18C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'JAPANESE GRAMMAR \u2014 SOV \u00b7 PARTICLES \u00b7 AGGLUTINATIVE')
    g += t(240, 73, 'Japanese is SOV. All grammatical relations expressed by postposed particles after each noun phrase.', 'middle', 'Ls')
    g += t(240, 82, 'Watashi-wa hon-wo yomimasu. I-TOP book-OBJ read-POLITE. \u201cI read a book.\u201d', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'JAPANESE PARTICLES')
    jpart = [
        ('\u306f (wa)', 'topic marker: \u79c1\u306f = as for me / I (topic)'),
        ('\u304c (ga)', 'subject marker: \u96e8\u304c\u964d\u308b = rain falls'),
        ('\u3092 (wo)', 'object marker: \u672c\u3092\u8aad\u3080 = read a book'),
        ('\u306b (ni)', 'dative/location: \u90fd\u5e02\u306b = in/to the city'),
        ('\u3067 (de)', 'instrumental/location: \u8eca\u3067 = by car \u00b7 \u516c\u5712\u3067 = at the park'),
        ('\u306e (no)', 'genitive: \u79c1\u306e\u672c = my book'),
    ]
    for i, (p, gloss) in enumerate(jpart):
        y = 108 + i * 10
        g += t(70, y, p, 'middle', 'Ls')
        g += t(300, y, gloss, 'middle', 'Lx')
    g += hr(175)

    g += sh(183, 'JAPANESE CORE VOCABULARY')
    jvocab = [
        ('\u6c34 mizu', 'water'), ('\u706b hi', 'fire'), ('\u571f tsuchi', 'earth'),
        ('\u4eba hito', 'person'), ('\u6708 tsuki', 'moon'), ('\u8a18\u686b kioku', 'memory'),
        ('\u672a\u6765 mirai', 'future'), ('\u81ea\u7531 jiy\u016b', 'freedom'),
        ('\u5fc3 kokoro', 'heart'), ('\u611b ai', 'love'), ('\u4e16\u754c sekai', 'world'),
        ('\u547d inochi', 'life'),
    ]
    for i, (jp, en) in enumerate(jvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 193 + row * 10
        g += t(x, y, jp, 'middle', 'Ls')
        g += t(x + 65, y, en, 'middle', 'Lx')

    g += sec_divider(238, 'SECONDARY \u2014 ZHUANG (CUENGH) \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(264, 'ZHUANG GRAMMAR \u2014 SVO \u00b7 ISOLATING \u00b7 NO INFLECTION')
    g += t(240, 274, 'Zhuang is SVO and highly isolating \u2014 words do not change form for tense, number, or case.', 'middle', 'Ls')
    g += t(240, 283, 'Aspect and time expressed by adverbs and particles placed before or after the verb.', 'middle', 'Lx')
    g += t(240, 292, 'Classifier system: nouns require a classifier when counted. Different classes for humans, animals, flat things.', 'middle', 'Lx')
    g += hr(300)

    g += sh(308, 'ZHUANG CLASSIFIERS \u2014 SAMPLE')
    clf = [
        ('boux', 'human classifier: boux vunz (one person), boux lwgnyez (one child)'),
        ('duz', 'animal classifier: duz gaeq (one chicken), duz ma (one dog)'),
        ('aen', 'round/3D object: aen mbwn (the sky), aen mboq (a stone)'),
        ('mbat', 'flat/thin object: mbat saw (a book), mbat bohmeh (a paper)'),
        ('bak', 'opening/mouth: bak roen (a road), bak raemx (water source)'),
    ]
    for i, (cl, ex) in enumerate(clf):
        y = 318 + i * 10
        g += t(60, y, cl, 'middle', 'Ls')
        g += t(310, y, ex, 'middle', 'Lx')
    g += hr(378)

    g += sh(386, 'ZHUANG CORE VOCABULARY')
    zvocab = [
        ('raemx', 'water'), ('feiz', 'fire'), ('deih', 'earth/land'),
        ('vunz', 'person'), ('ndwen', 'moon'), ('naengh', 'remember'),
        ('laeng', 'future/forward'), ('swhyouh', 'freedom'),
        ('sim', 'heart'), ('yinx', 'love'), ('seiqgyaiq', 'world'),
        ('mingh', 'life'),
    ]
    for i, (zh, en) in enumerate(zvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 396 + row * 10
        g += t(x, y, zh, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')
    g += hr(440)

    g += sh(448, 'GRAMMAR BRIDGE \u2014 SOV MEETS SVO')
    g += t(240, 458, 'Japanese (SOV): Watashi-wa mizu-wo nomimasu. I-TOP water-OBJ drink-POL. = I drink water.', 'middle', 'Ls')
    g += t(240, 467, 'Zhuang (SVO): Gou gwn raemx. I drink water. No particles, no inflection. Tone carries meaning.', 'middle', 'Ls')
    g += t(240, 476, 'Japanese: agglutinative particles after every phrase. Zhuang: isolating, no morphological marking.', 'middle', 'Lx')
    g += t(240, 485, 'Both Tai-Kadai (Zhuang) and Japanese: classifier systems shared across East/Southeast Asia.', 'middle', 'Lx')

    g += footer('18', 'Japanese', 'Zhuang', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 18D ALT — TEXT ─────────────────────────────────────────────────────

def build_18d_alt():
    g = open_svg()
    g += t(240, 30, 'JAPANESE + ZHUANG \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 18D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. MATSUO BASH\u014c \u2014 HAIKU (1686 CE)')
    g += t(240, 73, '\u53e4\u6c60\u3084\u3000\u86d9\u98db\u3073\u8fbc\u3080\u3000\u6c5f\u306e\u97f3', 'middle', 'L')
    g += t(240, 86, 'furuike ya / kawazu tobikomu / mizu no oto', 'middle', 'Ls')
    g += t(240, 95, 'old pond / frog leaps in / sound of water', 'middle', 'Lx')
    g += t(240, 104, '"An old pond \u2014 a frog leaps in \u2014 the sound of water." \u2014 Bash\u014c. Most famous haiku in history.', 'middle', 'F')
    g += hr(112)

    g += sh(120, 'II. JAPANESE PROVERB \u2014 ON MEMORY')
    g += t(240, 130, '\u8bb0\u61b6\u306f\u672a\u6765\u3092\u4f5c\u308b\u3002', 'middle', 'L')
    g += t(240, 143, 'Kioku wa mirai wo tsukuru.', 'middle', 'Ls')
    g += t(240, 152, '"Memory creates the future." (Japanese proverb on the relationship between past and future.)', 'middle', 'F')
    g += hr(160)

    g += sh(168, 'III. JAPANESE BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 179, '\u3053\u308c\u306f\u3001\u672a\u6765\u3092\u5fc3\u306b\u523a\u3057\u3066\u3044\u305f\u4eba\u305f\u3061\u306b\u3088\u3063\u3066\u3001', 'middle', 'L')
    g += t(240, 192, '\u3042\u306a\u305f\u306e\u305f\u3081\u306b\u3001\u7121\u511f\u3067\u3001\u4f5c\u3089\u308c\u307e\u3057\u305f\u3002', 'middle', 'L')
    g += t(240, 204, 'This / future-ACC heart-in pierced-PAST people-by / you-for / free-of-charge / was-made.', 'middle', 'Lx')
    g += t(240, 213, '"This was made for you, freely, by people who held the future in their heart." (Japanese)', 'middle', 'F')
    g += hr(221)

    g += sh(229, 'JAPANESE NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 239, '\u672a\u6765 (mirai) = future (not-yet-come). \u8a18\u61b6 (kioku) = memory. Kanji carry the conceptual weight.', 'middle', 'Ls')
    g += t(240, 248, '\u5fc3\u306b\u523a\u3059 = to pierce the heart / to hold in heart. SOV verb-final construction preserved throughout.', 'middle', 'Lx')

    g += sec_divider(258, 'SECONDARY \u2014 ZHUANG (CUENGH) \u2014 RUNNING TEXT')

    g += sh(284, 'I. ZHUANG PROVERB \u2014 ON MOUNTAIN AND MEMORY')
    g += t(240, 294, 'Bya sang naengh bwnroengz, vunz laeg naengh sim.', 'middle', 'L')
    g += t(240, 305, 'Mountain tall remember-in roots  person old remember heart.', 'middle', 'Lx')
    g += t(240, 314, '"The tall mountain holds its roots; the old person holds memory in the heart." (Zhuang proverb)', 'middle', 'F')
    g += hr(322)

    g += sh(330, 'II. ZHUANG PROVERB \u2014 ON THE RIVER (LAI YA IDIOM)')
    g += t(240, 340, 'Raemxdah rox roen, vunz rox boux.', 'middle', 'L')
    g += t(240, 351, 'River knows path person knows person.', 'middle', 'Lx')
    g += t(240, 360, '"The river knows its way; a person knows another person." (Zhuang: empathy and recognition)', 'middle', 'F')
    g += hr(368)

    g += sh(376, 'III. ZHUANG BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 387, 'Neix guh hawj mwngz, byaij mbouj gwn cienz,', 'middle', 'L')
    g += t(240, 399, 'youq vunz naengh laeng daeuj guh.', 'middle', 'L')
    g += t(240, 411, 'This made for you  walk not eat money / by people remember forward come made.', 'middle', 'Lx')
    g += t(240, 420, '"This was made for you, freely, by people who remembered the future." (Zhuang)', 'middle', 'F')
    g += hr(428)

    g += sh(436, 'ZHUANG NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 446, 'Laeng = forward/ahead \u2014 and by extension: future. Daeuj = come (directional toward speaker).', 'middle', 'Ls')
    g += t(240, 455, 'Naengh = to remember, to keep/hold in mind (lit. to sit with / to keep alongside).', 'middle', 'Ls')
    g += t(240, 464, 'Byaij mbouj gwn cienz = walk not eat money = \u201cfreely\u201d (walk without spending money = do for free).', 'middle', 'Lx')
    g += hr(472)

    g += sh(480, 'LANGUAGE BRIDGE \u2014 ACROSS THE EAST CHINA SEA')
    g += t(240, 490, 'Japanese: ~125M speakers. Island language, 3-script system, pitch accent, mora-timing.', 'middle', 'Ls')
    g += t(240, 499, 'Zhuang: ~17M speakers. Largest minority language of China. SVO isolating, 6 tones, Tai-Kadai family.', 'middle', 'Ls')
    g += t(240, 508, 'Expanded radius (1500mi) bridges two languages that share East Asian cultural context via China.', 'middle', 'Lx')

    g += footer('18', 'Japanese', 'Zhuang', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate18a_japanese_zhuang_script_alt.svg':    build_18a_alt(),
        'plate18b_japanese_zhuang_phonology_alt.svg': build_18b_alt(),
        'plate18c_japanese_zhuang_grammar_alt.svg':   build_18c_alt(),
        'plate18d_japanese_zhuang_text_alt.svg':      build_18d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
