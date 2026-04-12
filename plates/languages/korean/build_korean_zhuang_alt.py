#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Korean / Zhuang alt plate series 50A–50D for Remember Forward.
Secondary language: Zhuang (Cuengh / 壮语) — spoken in Guangxi, south China.
Geographic basis: All nearest major neighbors of Korea (Mandarin, Japanese, Russian)
are already in the series. Expanded to ~1500mi radius from Seoul reaches Guangxi
(Zhuang homeland) ~2200km. Zhuang: Tai-Kadai family, SVO, 6 tones, ~17M speakers.
Korean itself is a language isolate with no proven relatives. Zhuang is the
nearest significant non-series language reachable within the expanded radius.
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


# ─── PLATE 50A ALT — SCRIPT ───────────────────────────────────────────────────

def build_50a_alt():
    g = open_svg()
    g += t(240, 30, 'KOREAN + ZHUANG \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 50A \u00b7 REMEMBER FORWARD \u00b7 EXPANDED ~1500MI RADIUS', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'KOREAN \u2014 HANGEUL \u00b7 AN ALPHABET IN SYLLABLE BLOCKS')
    g += t(240, 73, 'Hangeul: invented in 1443 CE by King Sejong and royal scholars. World\u2019s only historically documented alphabet invention.', 'middle', 'Ls')
    g += t(240, 82, 'Letters (jamo) are not written linearly but assembled into syllable blocks: consonant + vowel [+ final consonant].', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'HANGEUL CONSONANTS \u2014 19 JAMO')
    cons_rows = [
        '\u3131\u3132\u3134\u3137\u3138\u3139\u3141\u3142\u3143\u3144',
        '\u3145\u3146\u3147\u3148\u3149\u314a\u314b\u314c\u314d\u314e',
    ]
    labels = [
        'g/k  kk  n  d/t  dd  r/l  m  b/p  bb  bs',
        's   ss   ng  j   jj   ch  k   t   p   h',
    ]
    for i, (row, label) in enumerate(zip(cons_rows, labels)):
        y = 108 + i * 18
        g += t(240, y, row, 'middle', 'L')
        g += t(240, y + 10, label, 'middle', 'Lx')
    g += hr(140)

    g += sh(148, 'HANGEUL VOWELS \u2014 21 JAMO')
    vowel_rows = [
        '\u314f\u3150\u3151\u3152\u3153\u3154\u3155\u3156\u3157\u3158\u3159',
        '\u315a\u315b\u315c\u315d\u315e\u315f\u3160\u3161\u3162\u3163',
    ]
    vlabels = [
        'a  ae  ya  yae  eo  e  yeo  ye  o  wa  wae',
        'oe  yo  u  wo  we  wi  yu  eu  ui  i',
    ]
    for i, (row, label) in enumerate(zip(vowel_rows, vlabels)):
        y = 158 + i * 18
        g += t(240, y, row, 'middle', 'L')
        g += t(240, y + 10, label, 'middle', 'Lx')
    g += hr(190)

    g += sh(198, 'HANGEUL SYLLABLE BLOCK STRUCTURE')
    blocks = [
        ('\ud55c', '= \u3131(\u03b7\u02b0) + \u3161(eu) + \u3134(n): han'),
        ('\uad6d', '= \u3131(g) + \u315c(u) + \u3147(ng) + : guk'),
        ('\uc5b4', '= \u3147(silent) + \u3153(\u0254): eo'),
        ('\uc0ac', '= \u3145(s) + \u314f(a): sa'),
    ]
    for i, (block, note) in enumerate(blocks):
        y = 208 + i * 11
        g += t(70, y, block, 'middle', 'L')
        g += t(300, y, note, 'middle', 'Lx')
    g += hr(258)

    g += sh(266, 'KOREAN WRITING HISTORY')
    g += t(240, 276, 'Before Hangeul: Classical Chinese (Hanja) used for writing. Only educated elite could read.', 'middle', 'Ls')
    g += t(240, 285, 'Hangeul published in Hunminjeongeum (1446 CE): \u201cCorrect sounds for instructing the people.\u201d Designed for literacy.', 'middle', 'Lx')
    g += t(240, 294, 'Today: Hangeul-only in South Korea for most contexts. North Korea: also Hangeul-only. ~77M speakers.', 'middle', 'Lx')

    g += sec_divider(304, 'SECONDARY \u2014 ZHUANG (CUENGH / \u58EE\u8BED) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(330, 'ZHUANG \u2014 TWO WRITING TRADITIONS: LATIN AND SAWNDIP')
    g += t(240, 340, 'Standard Zhuang Script: Latin-based, 26 letters + tone-marking consonant letters. Official since 1982.', 'middle', 'Ls')
    g += t(240, 349, 'Sawndip (\u65b9\u5757\u58ee\u6587): Chinese-character-based script for Zhuang sounds. Used for centuries in ritual/literary context.', 'middle', 'Lx')
    g += t(240, 358, 'Sawndip uses Chinese characters with Zhuang phonetic values, not their Mandarin readings.', 'middle', 'Lx')
    g += hr(366)

    g += sh(374, 'ZHUANG LATIN TONE LETTERS')
    ztones = [
        ('(no mark)', '= Tone 1 high level: ma (horse/sesame)'),
        ('-z', '= Tone 2 high rising: maz'),
        ('-j', '= Tone 3 dipping: maj'),
        ('-x', '= Tone 4 low: max'),
        ('-q', '= Tone 5 low checked (glottal): maq'),
        ('-h', '= Tone 6 high checked: mah'),
    ]
    for i, (mark, desc) in enumerate(ztones):
        y = 384 + i * 10
        g += t(75, y, mark, 'middle', 'Ls')
        g += t(290, y, desc, 'middle', 'Lx')
    g += hr(450)

    g += sh(458, 'SCRIPT BRIDGE \u2014 TWO INVENTED SYSTEMS')
    g += t(240, 468, 'Hangeul (1443): deliberately invented to promote literacy among Korean people. Top-down government design.', 'middle', 'Ls')
    g += t(240, 477, 'Zhuang Latin (1957): deliberately standardized by linguists and government to promote Zhuang literacy.', 'middle', 'Lx')
    g += t(240, 486, 'Both: modern, phonemic alphabets designed for maximal literacy access. Same purpose, different approaches.', 'middle', 'Lx')

    g += footer('50', 'Korean', 'Zhuang', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 50B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_50b_alt():
    g = open_svg()
    g += t(240, 30, 'KOREAN + ZHUANG \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 50B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'KOREAN PHONOLOGY \u2014 THREE-WAY STOP CONTRAST')
    g += t(240, 73, 'Korean has a unique three-way distinction for stops: plain/aspirated/tense (fortis).', 'middle', 'Ls')
    g += t(240, 82, 'Plain: /p b/ \u2014 Aspirated: /p\u02b0/ \u2014 Tense (fortis): /p\u02bc/ (glottalized, no VOT).', 'middle', 'Ls')
    g += t(240, 91, 'This three-way contrast is rare cross-linguistically. Applies to: p/ph/pp, t/th/tt, k/kh/kk, c/ch/cc.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'KOREAN THREE-WAY STOP TABLE')
    stops = [
        ('Place', 'Plain', 'Aspirated', 'Tense'),
        ('Bilabial', '\u3142 /p/', '\u314b /p\u02b0/', '\u3143 /p\u02bc/'),
        ('Alveolar', '\u3137 /t/', '\u314c /t\u02b0/', '\u3138 /t\u02bc/'),
        ('Velar', '\u3131 /k/', '\u314a /k\u02b0/', '\u3132 /k\u02bc/'),
        ('Palatal', '\u3148 /t\u0255/', '\u314b /t\u0255\u02b0/', '\u3149 /t\u0255\u02bc/'),
    ]
    for i, row in enumerate(stops):
        y = 117 + i * 11
        g += t(70, y, row[0], 'middle', 'Lx')
        g += t(200, y, row[1], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(305, y, row[2], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(400, y, row[3], 'middle', 'Ls' if i > 0 else 'Lx')
    g += hr(178)

    g += sh(186, 'KOREAN VOWELS \u2014 10 MONOPHTHONGS')
    g += t(240, 196, 'Korean has 10 vowel phonemes: /a \u025b \u0259 i o u \u0153 y/ and additional diphthongs.', 'middle', 'Ls')
    kv = [('/a/','arm'), ('/\u025b/','bait'), ('/\u0259/','above'), ('/i/','bee'),
          ('/o/','boat'), ('/u/','boot'), ('/\u0153/','eu (front rounded)'), ('/y/','yi (front rounded)')]
    for i, (ipa, ex) in enumerate(kv):
        col = i % 4; row = i // 4
        x = 55 + col * 105; y = 206 + row * 10
        g += t(x, y, f'{ipa} \u2248 {ex}', 'middle', 'Lx')
    g += hr(232)

    g += sh(240, 'KOREAN CONSONANT ALTERATIONS')
    g += t(240, 250, 'Korean consonants change significantly by position: word-initial, intervocalic, and final positions are all different.', 'middle', 'Ls')
    g += t(240, 259, '/k/ word-final \u2192 unreleased /k\u032a\u0325/. Intervocalic: /g/. Initial: /k/ or /k\u02b0/. Same letter, three sounds.', 'middle', 'Lx')

    g += sec_divider(269, 'SECONDARY \u2014 ZHUANG (CUENGH) \u2014 PHONOLOGY')

    g += sh(295, 'ZHUANG PHONOLOGY \u2014 6 TONES (STANDARD DIALECT)')
    g += t(240, 305, 'Zhuang has 6 tones in standard (Wuming) dialect. Other dialects have up to 9 tones.', 'middle', 'Ls')
    zt = [('Tone 1', 'mid-high level'), ('Tone 2 -z', 'high rising'),
          ('Tone 3 -j', 'mid dipping'), ('Tone 4 -x', 'low falling'),
          ('Tone 5 -q', 'low short checked (glottal coda)'), ('Tone 6 -h', 'high short checked')]
    for i, (name, desc) in enumerate(zt):
        y = 315 + i * 10
        g += t(110, y, name, 'middle', 'Lx')
        g += t(310, y, desc, 'middle', 'Lx')
    g += hr(380)

    g += sh(388, 'ZHUANG CONSONANTS AND ASPIRATION')
    g += t(240, 398, 'Zhuang has voiceless/voiced/aspirated distinctions: p/b/ph, t/d/th, k/g/kh.', 'middle', 'Ls')
    g += t(240, 407, 'Only two-way stop contrast (vs. Korean\u2019s three-way). But 6 tones (vs. Korean\u2019s pitch accent system).', 'middle', 'Lx')
    g += hr(415)

    g += sh(423, 'PHONOLOGICAL BRIDGE \u2014 CONTRAST IN STOP SYSTEMS')
    comp = [
        ('Feature', 'Korean', 'Zhuang'),
        ('Stop series', '3-way: plain/asp/tense', '2-way: vl/vd + asp'),
        ('Tonal', 'Pitch accent', '6 tones'),
        ('Vowels', '10 monophthongs', '6-7 vowels'),
        ('Syllable', 'Complex (C)(C)V(C)(C)', 'CV(C) simpler'),
        ('Language family', 'Isolate', 'Tai-Kadai'),
    ]
    for i, row in enumerate(comp):
        y = 433 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('50', 'Korean', 'Zhuang', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 50C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_50c_alt():
    g = open_svg()
    g += t(240, 30, 'KOREAN + ZHUANG \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 50C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'KOREAN GRAMMAR \u2014 SOV \u00b7 AGGLUTINATIVE \u00b7 PARTICLES')
    g += t(240, 73, 'Korean is SOV. Particles (postpositions) attach to nouns: \uc774/\uac00 (subject), \uc744/\ub97c (object), \uc5d0/\uc5d0\uc11c (location).', 'middle', 'Ls')
    g += t(240, 82, 'Rich honorific system: verb endings change depending on relative social status of speaker and listener.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'KOREAN PARTICLES')
    kpart = [
        ('\uc774/\uac00', 'subject marker: \ucc44\ubbf8\uac00 \ub9db\uc788\ub2e4 (food is tasty)'),
        ('\uc740/\ub294', 'topic marker: \ub098\ub294 \ud559\uc0dd\uc774\ub2e4 (I [topic] am a student)'),
        ('\uc744/\ub97c', 'object marker: \ucc45\uc744 \uc77d\ub2e4 (read a book)'),
        ('\uc5d0', 'location/time: \ud559\uad50\uc5d0 (at school), 3\uc2dc\uc5d0 (at 3 o\u2019clock)'),
        ('\uc5d0\uc11c', 'action location: \ud558\uad50\uc5d0\uc11c (at school, doing action)'),
        ('\uc758', 'genitive: \ub098\uc758 \uccd0 (my book)'),
    ]
    for i, (p, gloss) in enumerate(kpart):
        y = 108 + i * 10
        g += t(60, y, p, 'middle', 'Ls')
        g += t(290, y, gloss, 'middle', 'Lx')
    g += hr(175)

    g += sh(183, 'KOREAN CORE VOCABULARY')
    kvocab = [
        ('\ubb3c', 'mul', 'water'), ('\ubd88', 'bul', 'fire'), ('\ub545', 'ttang', 'earth'),
        ('\uc0ac\ub78c', 'saram', 'person'), ('\ub2ec', 'dal', 'moon'), ('\uae30\uc5b5', 'gieok', 'memory'),
        ('\ubbf8\ub798', 'mirae', 'future'), ('\uc790\uc720', 'jayu', 'freedom'),
        ('\ub9c8\uc74c', 'maeum', 'heart'), ('\uc0ac\ub791', 'sarang', 'love'), ('\uc138\uacc4', 'segye', 'world'),
        ('\uc0dd\uba85', 'saengmyeong', 'life'),
    ]
    for i, (ko, rom, en) in enumerate(kvocab):
        col = i % 3; row = i // 3
        x = 55 + col * 135; y = 193 + row * 10
        g += t(x, y, ko, 'middle', 'Ls')
        g += t(x + 48, y, rom, 'middle', 'Lx')
        g += t(x + 90, y, en, 'middle', 'Lx')

    g += sec_divider(238, 'SECONDARY \u2014 ZHUANG (CUENGH) \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(264, 'ZHUANG GRAMMAR \u2014 SVO \u00b7 ISOLATING \u00b7 CLASSIFIERS')
    g += t(240, 274, 'Zhuang is SVO and isolating. Korean (SOV) and Zhuang (SVO) are typological opposites in word order.', 'middle', 'Ls')
    g += t(240, 283, 'Both: no grammatical gender. Both: aspect over tense. Zhuang: noun classifiers. Korean: postpositions.', 'middle', 'Lx')
    g += hr(291)

    g += sh(299, 'ZHUANG CLASSIFIERS \u2014 SAMPLE')
    zclf = [
        ('boux', 'human: boux vunz (a person), boux lwgnyez (a child)'),
        ('duz', 'animal: duz ma (a dog), duz gaeq (a chicken)'),
        ('aen', 'round/3D: aen ndwen (the moon), aen gij (something)'),
        ('mbat', 'flat: mbat saw (a book), mbat bohmeh (a paper)'),
    ]
    for i, (cl, ex) in enumerate(zclf):
        y = 309 + i * 10
        g += t(60, y, cl, 'middle', 'Ls')
        g += t(300, y, ex, 'middle', 'Lx')
    g += hr(358)

    g += sh(366, 'ZHUANG CORE VOCABULARY')
    zvocab = [
        ('raemx', 'water'), ('feiz', 'fire'), ('deih', 'earth'),
        ('vunz', 'person'), ('ndwen', 'moon'), ('naengh', 'remember'),
        ('laeng', 'future/forward'), ('swhyouh', 'freedom'),
        ('sim', 'heart'), ('yinx', 'love'), ('seiqgyaiq', 'world'),
        ('mingh', 'life'),
    ]
    for i, (zh, en) in enumerate(zvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 376 + row * 10
        g += t(x, y, zh, 'middle', 'Ls')
        g += t(x + 62, y, en, 'middle', 'Lx')
    g += hr(420)

    g += sh(428, 'GRAMMAR BRIDGE \u2014 SOV ISOLATE MEETS SVO CLASSIFIER')
    g += t(240, 438, 'Korean (SOV): n\u014d-ga mul-eul masinda. I-SUBJ water-OBJ drink. = I drink water.', 'middle', 'Ls')
    g += t(240, 447, 'Zhuang (SVO): Gou gwn raemx. I drink water. No particles, no inflection, 6 tones carry meaning.', 'middle', 'Ls')
    g += t(240, 456, 'Korean: agglutinative (many suffixes). Zhuang: isolating (no morphological marking). Maximum contrast.', 'middle', 'Lx')

    g += footer('50', 'Korean', 'Zhuang', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 50D ALT — TEXT ─────────────────────────────────────────────────────

def build_50d_alt():
    g = open_svg()
    g += t(240, 30, 'KOREAN + ZHUANG \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 50D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. KOREAN PROVERB \u2014 ON PATIENCE')
    g += t(240, 73, '\uc2dc\uc791\uc774 \ubc18\uc774\ub2e4. (Sijak-i bani-da.)', 'middle', 'L')
    g += t(240, 87, 'Beginning is  half.', 'middle', 'Lx')
    g += t(240, 96, '"Well begun is half done." \u2014 Korean proverb. Encourages starting as the core act of completion.', 'middle', 'F')
    g += hr(104)

    g += sh(112, 'II. KOREAN PROVERB \u2014 ON MEMORY')
    g += t(240, 122, '\ubc30\uc6b4 \uac83\uc744 \uc78a\uc9c0 \ub9c8\ub77c. (Baeun geot-eul itji mara.)', 'middle', 'L')
    g += t(240, 136, 'Learned thing-ACC forget not do.', 'middle', 'Lx')
    g += t(240, 145, '"Do not forget what you have learned." \u2014 Core Korean educational proverb.', 'middle', 'F')
    g += hr(153)

    g += sh(161, 'III. KOREAN BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 172, '\uc774\uac83\uc740 \ub2f9\uc2e0\uc744 \uc704\ud574, \ubb34\ub8cc\ub85c,', 'middle', 'L')
    g += t(240, 185, '\ubbf8\ub798\ub97c \uae30\uc5b5\ud55c \uc0ac\ub78c\ub4e4\uc774 \ub9cc\ub4e4\uc5c8\uc2b5\ub2c8\ub2e4.', 'middle', 'L')
    g += t(240, 198, 'This-TOP you-ACC for  free-of-charge / future-ACC remembered people-NOM made-HON.', 'middle', 'Lx')
    g += t(240, 207, '"This was made for you, freely, by people who remembered the future." (Korean, formal register)', 'middle', 'F')
    g += hr(215)

    g += sh(223, 'KOREAN NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 233, '\ubbf8\ub798 (mirae) = future (not-yet-come). \uae30\uc5b5\ud558\ub2e4 (gieok-hada) = to remember (memory-do).', 'middle', 'Ls')
    g += t(240, 242, 'Verb-final (SOV): \uae30\uc5b5\ud55c \uc0ac\ub78c\ub4e4\uc774 \ub9cc\ub4e4\uc5c8\uc2b5\ub2c8\ub2e4 = remembered-people-NOM made-HON. Honorific verb ending.', 'middle', 'Lx')

    g += sec_divider(252, 'SECONDARY \u2014 ZHUANG (CUENGH) \u2014 RUNNING TEXT')

    g += sh(278, 'I. ZHUANG PROVERB \u2014 ON MOUNTAIN AND RIVER')
    g += t(240, 288, 'Bya ranz, haeux raemx cingq.', 'middle', 'L')
    g += t(240, 299, 'Mountain home  rice  water right/correct.', 'middle', 'Lx')
    g += t(240, 308, '"Mountain is home, rice and water are right." \u2014 Zhuang proverb on land, sustenance, and belonging.', 'middle', 'F')
    g += hr(316)

    g += sh(324, 'II. ZHUANG PROVERB \u2014 ON MEMORY AND ROOTS')
    g += t(240, 334, 'Vunz rox giz daeuj rox bya, vunz rox naengh rox sim.', 'middle', 'L')
    g += t(240, 345, 'Person knows where from knows mountain  person knows remember knows heart.', 'middle', 'Lx')
    g += t(240, 354, '"One who knows where they came from knows the mountain; one who can remember knows the heart." (Zhuang)', 'middle', 'F')
    g += hr(362)

    g += sh(370, 'III. ZHUANG BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 381, 'Neix guh hawj mwngz, byaij mbouj gwn cienz,', 'middle', 'L')
    g += t(240, 393, 'youq vunz naengh laeng daeuj guh.', 'middle', 'L')
    g += t(240, 405, 'This made for you  walk not eat money / by people remember forward come made.', 'middle', 'Lx')
    g += t(240, 414, '"This was made for you, freely, by people who remembered the future." (Zhuang)', 'middle', 'F')
    g += hr(422)

    g += sh(430, 'ZHUANG NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 440, 'Laeng = forward/ahead \u2014 spatial-temporal. Naengh = to remember (to sit with / hold alongside).', 'middle', 'Ls')
    g += t(240, 449, 'Byaij mbouj gwn cienz = walk without eating money = \u201cfor free\u201d. Idiom: cost nothing to receive.', 'middle', 'Lx')
    g += hr(457)

    g += sh(465, 'LANGUAGE BRIDGE \u2014 ISOLATE AND KADAI')
    g += t(240, 475, 'Korean: ~77M speakers. A language isolate \u2014 no proven relatives. Hangeul: the world\u2019s most rational alphabet.', 'middle', 'Ls')
    g += t(240, 484, 'Zhuang: ~17M speakers. Largest minority language of China. Tai-Kadai family. Tonal, isolating, SVO.', 'middle', 'Ls')
    g += t(240, 493, 'Expanded ~1500mi radius connects an East Asian isolate with a South Chinese Tai-Kadai community.', 'middle', 'Lx')

    g += footer('50', 'Korean', 'Zhuang', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate50a_korean_zhuang_script_alt.svg':    build_50a_alt(),
        'plate50b_korean_zhuang_phonology_alt.svg': build_50b_alt(),
        'plate50c_korean_zhuang_grammar_alt.svg':   build_50c_alt(),
        'plate50d_korean_zhuang_text_alt.svg':      build_50d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
