#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Japanese plate series 18A–18D for Remember Forward."""

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
        '  .Lj { font-size:14px; }\n'
        '  .Ljs{ font-size:10px; }\n'
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


# ─── PLATE 18A — SCRIPT ──────────────────────────────────────────────────────

def build_18a():
    g = open_svg()
    g += t(240, 32, 'JAPANESE — SCRIPT · WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 18A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Overview
    g += sh(68, 'THREE SCRIPTS — USED TOGETHER')
    g += t(240, 79, 'Japanese uses three interlocking scripts simultaneously in standard writing.', 'middle', 'L')
    g += t(80, 90, 'Hiragana ひらがな', 'middle', 'Ls')
    g += t(240, 90, 'Katakana カタカナ', 'middle', 'Ls')
    g += t(400, 90, 'Kanji 漢字', 'middle', 'Ls')
    g += t(80, 99, '46 base syllables, native words', 'middle', 'Lx')
    g += t(240, 99, '46 base syllables, loanwords', 'middle', 'Lx')
    g += t(400, 99, 'Chinese-origin logographs', 'middle', 'Lx')
    g += hr(107)

    # Hiragana table
    g += sh(116, 'HIRAGANA TABLE — 46 BASE SYLLABLES')
    g += t(240, 125, 'Rows: vowel order a-i-u-e-o · Columns: consonant series', 'middle', 'Lx')

    # Header row
    hdr_vowels = ['', 'a', 'i', 'u', 'e', 'o']
    col_x = [28, 100, 166, 232, 298, 364, 430]
    row_labels = ['—', 'k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w', 'n']
    # Hiragana rows: [consonant, a, i, u, e, o]
    hira_rows = [
        ['—',  'あ','い','う','え','お'],
        ['k',  'か','き','く','け','こ'],
        ['s',  'さ','し','す','せ','そ'],
        ['t',  'た','ち','つ','て','と'],
        ['n',  'な','に','ぬ','ね','の'],
        ['h',  'は','ひ','ふ','へ','ほ'],
        ['m',  'ま','み','む','め','も'],
        ['y',  'や','—', 'ゆ','—', 'よ'],
        ['r',  'ら','り','る','れ','ろ'],
        ['w',  'わ','—', '—', '—', 'を'],
        ['N',  'ん','—', '—', '—', '—'],
    ]
    # Romaji rows for below each kana
    hira_romaji = [
        ['',   'a',  'i',  'u',  'e',  'o'],
        ['',   'ka', 'ki', 'ku', 'ke', 'ko'],
        ['',   'sa', 'shi','su', 'se', 'so'],
        ['',   'ta', 'chi','tsu','te', 'to'],
        ['',   'na', 'ni', 'nu', 'ne', 'no'],
        ['',   'ha', 'hi', 'fu', 'he', 'ho'],
        ['',   'ma', 'mi', 'mu', 'me', 'mo'],
        ['',   'ya', '',   'yu', '',   'yo'],
        ['',   'ra', 'ri', 'ru', 're', 'ro'],
        ['',   'wa', '',   '',   '',   'wo'],
        ['',   'n',  '',   '',   '',   ''],
    ]
    col_xs = [30, 100, 166, 232, 298, 364]
    # Column headers
    for ci, (vow, cx) in enumerate(zip(['', 'a', 'i', 'u', 'e', 'o'], col_xs)):
        if ci == 0:
            g += t(cx, 133, 'C\\V', 'middle', 'Lx')
        else:
            g += t(cx, 133, vow, 'middle', 'Lx')

    y0 = 135
    row_h = 14
    for ri, (row, rom) in enumerate(zip(hira_rows, hira_romaji)):
        ry = y0 + ri * row_h
        for ci, (ch, rx) in enumerate(zip(row, col_xs)):
            if ci == 0:
                g += t(rx, ry + 8, ch, 'middle', 'Lx')
            else:
                if ch != '—' and ch != '':
                    g += t(rx, ry + 6, ch, 'middle', 'Ljs')
                    g += t(rx, ry + 13, rom[ci], 'middle', 'Lx')
                else:
                    g += t(rx, ry + 8, '—', 'middle', 'Lx')

    # Voiced / p-row note
    y_after = y0 + len(hira_rows) * row_h + 4
    g += t(240, y_after, 'Voiced (dakuten ゛): が ga, ざ za, だ da, ば ba · Semi-voiced (handakuten ゜): ぱ pa', 'middle', 'Lx')
    g += t(240, y_after + 8, 'Combination kana (youon): きゃ kya, しゅ shu, ちょ cho — small ya/yu/yo', 'middle', 'Lx')
    g += hr(y_after + 14)

    # Katakana table
    y_k = y_after + 22
    g += sh(y_k, 'KATAKANA TABLE — 46 BASE SYLLABLES')
    g += t(240, y_k + 9, 'Used for loanwords, foreign names, scientific terms, emphasis — same phonetic values as hiragana', 'middle', 'Lx')

    kata_rows = [
        ['—',  'ア','イ','ウ','エ','オ'],
        ['k',  'カ','キ','ク','ケ','コ'],
        ['s',  'サ','シ','ス','セ','ソ'],
        ['t',  'タ','チ','ツ','テ','ト'],
        ['n',  'ナ','ニ','ヌ','ネ','ノ'],
        ['h',  'ハ','ヒ','フ','ヘ','ホ'],
        ['m',  'マ','ミ','ム','メ','モ'],
        ['y',  'ヤ','—', 'ユ','—', 'ヨ'],
        ['r',  'ラ','リ','ル','レ','ロ'],
        ['w',  'ワ','—', '—', '—', 'ヲ'],
        ['N',  'ン','—', '—', '—', '—'],
    ]
    kata_romaji = hira_romaji  # same readings

    # Column headers
    for ci, (vow, cx) in enumerate(zip(['', 'a', 'i', 'u', 'e', 'o'], col_xs)):
        if ci == 0:
            g += t(cx, y_k + 17, 'C\\V', 'middle', 'Lx')
        else:
            g += t(cx, y_k + 17, vow, 'middle', 'Lx')

    y0k = y_k + 19
    for ri, (row, rom) in enumerate(zip(kata_rows, kata_romaji)):
        ry = y0k + ri * row_h
        for ci, (ch, cx) in enumerate(zip(row, col_xs)):
            if ci == 0:
                g += t(cx, ry + 8, ch, 'middle', 'Lx')
            else:
                if ch != '—' and ch != '':
                    g += t(cx, ry + 6, ch, 'middle', 'Ljs')
                    g += t(cx, ry + 13, rom[ci], 'middle', 'Lx')
                else:
                    g += t(cx, ry + 8, '—', 'middle', 'Lx')

    y_after2 = y0k + len(kata_rows) * row_h + 4
    g += hr(y_after2)

    # Kanji intro
    y_kj = y_after2 + 8
    g += sh(y_kj, 'KANJI — LOGOGRAPHIC CHARACTERS')
    g += t(240, y_kj + 10, 'Approx. 2,136 jōyō kanji (常用漢字) required for literacy · Each has ON (Chinese) + kun (Japanese) readings', 'middle', 'Lx')

    kanji_ex = [
        ('山', 'yama/SAN', 'mountain'),
        ('川', 'kawa/SEN', 'river'),
        ('火', 'hi/KA', 'fire'),
        ('水', 'mizu/SUI', 'water'),
        ('木', 'ki/MOKU', 'tree'),
        ('日', 'hi/NICHI', 'sun/day'),
        ('月', 'tsuki/GETSU', 'moon/month'),
        ('人', 'hito/JIN', 'person'),
        ('大', 'ōkii/DAI', 'big'),
        ('小', 'chiisai/SHŌ', 'small'),
    ]
    kx_cols = [50, 150, 250, 350, 440]
    for i, (kj, rd, mn) in enumerate(kanji_ex):
        cx = kx_cols[i % 5]
        ry = y_kj + 20 + (i // 5) * 22
        g += t(cx, ry, kj, 'middle', 'Ljs')
        g += t(cx, ry + 8, rd, 'middle', 'Lx')
        g += t(cx, ry + 14, mn, 'middle', 'Lx')

    y_hist = y_kj + 64
    g += hr(y_hist)
    g += sh(y_hist + 8, 'SCRIPT HISTORY')
    g += t(240, y_hist + 18, '300–700 CE: Chinese kanji adopted · 9th c: hiragana from cursive man\'yōgana · katakana from radical elements', 'middle', 'Lx')
    g += t(240, y_hist + 26, 'Man\'yōgana (万葉仮名): oldest Japanese writing — Chinese characters used phonetically, not semantically', 'middle', 'Lx')
    g += t(240, y_hist + 34, 'Meiji era (1868–): national literacy drive · 1946: postwar simplification of kanji forms and official list', 'middle', 'Lx')
    g += t(240, y_hist + 42, 'Writing direction: traditionally right→left, top→bottom in columns; modern: left→right horizontal rows', 'middle', 'Lx')

    g += footer('18', 'Japanese', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 18B — PHONOLOGY ───────────────────────────────────────────────────

def build_18b():
    g = open_svg()
    g += t(240, 32, 'JAPANESE — PHONOLOGY · SOUND SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 18B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Mora timing
    g += sh(68, 'MORA-TIMED LANGUAGE')
    g += t(240, 79, 'Japanese is MORA-timed, not syllable-timed. Each mora (haku 拍) takes equal duration.', 'middle', 'L')
    g += t(240, 89, 'A mora = one kana character. Long vowels, double consonants, and ん each count as one mora.', 'middle', 'Ls')
    g += t(240, 98, 'Example: 東京 Tō·kyō = 4 morae (TO + U + KYO + U)  ·  さっぽろ Sap·po·ro = 4 morae', 'middle', 'Ls')
    g += hr(106)

    # Vowel system
    g += sh(115, 'VOWEL SYSTEM — 5 SHORT + 5 LONG')
    vowels = [
        ('/a/', 'あ a', 'low central, like "ah"'),
        ('/i/', 'い i', 'high front, like "ee"'),
        ('/ɯ/', 'う u', 'high back unrounded — NO lip rounding'),
        ('/e/', 'え e', 'mid front, like "eh"'),
        ('/o/', 'お o', 'mid back, like "oh"'),
    ]
    for i, (ipa, kana, desc) in enumerate(vowels):
        y = 125 + i * 14
        g += t(50, y, ipa, 'middle', 'Ls')
        g += t(120, y, kana, 'middle', 'Ls')
        g += t(310, y, desc, 'middle', 'Lx')

    g += t(240, 197, 'Long vowels: double duration — おばさん obasan (aunt) vs おばあさん obāsan (grandmother)', 'middle', 'Ls')
    g += t(240, 206, 'Vowel devoicing: /i/ and /u/ often whispered between voiceless consonants: です desu → "des"', 'middle', 'Ls')
    g += hr(214)

    # Consonant inventory
    g += sh(223, 'CONSONANT INVENTORY')
    g += t(240, 233, 'Japanese has a small consonant inventory — no /l/, /v/, /θ/, /ð/ in native phonology', 'middle', 'Ls')

    cons_data = [
        ('p b', 'bilabial stops', 'は row /h/ → /p/ with ゜, voiced /b/ with ゛'),
        ('t d', 'alveolar stops', '/t/ → [tɕ] before i, [ts] before u (affrication)'),
        ('k g', 'velar stops', '/g/ also realized as [ŋ] (nasal) in medial position'),
        ('s z', 'fricatives', '/s/ → [ɕ] before i (し shi) · /z/ → [dʑ] before i (じ ji)'),
        ('n m', 'nasals', 'ん /N/ is a special moraic nasal: [m] [n] [ŋ] [ɴ] by context'),
        ('r',   'liquid', 'Japanese /r/ = flap [ɾ] — between English r and l; neither exactly'),
        ('h',   'glottal', '/h/ → [ç] before i (ひ hi) · [ɸ] before u (ふ fu)'),
        ('y w', 'glides', 'Palatal and labial-velar approximants'),
    ]
    for i, (phon, label, note) in enumerate(cons_data):
        y = 244 + i * 16
        g += t(50, y, phon, 'middle', 'Ls')
        g += t(130, y, label, 'middle', 'Lx')
        g += t(320, y, note, 'middle', 'Lx')
    g += hr(374)

    # Syllable structure
    g += sh(382, 'SYLLABLE STRUCTURE — CV DOMINANT')
    g += t(240, 392, 'Native Japanese syllables are (C)V — consonant-vowel — with very few exceptions.', 'middle', 'L')
    g += t(240, 401, 'Closed syllables occur only in loanwords: ミルク miruku (milk) → syllabified MU·RU·KU', 'middle', 'Ls')
    g += t(240, 410, 'Geminate (double) consonants: っ/ッ (small tsu) — ざっし zasshi (magazine) = ZA+S+SHI (3 morae)', 'middle', 'Ls')
    g += hr(418)

    # Pitch accent
    g += sh(427, 'PITCH ACCENT — TOKYO DIALECT')
    g += t(240, 437, 'Japanese uses PITCH accent (not stress): syllables are High (H) or Low (L) tone.', 'middle', 'L')
    g += t(240, 447, 'First mora sets pitch; subsequent morae follow pattern; a downstep (drop) occurs at most once.', 'middle', 'Ls')
    g += t(240, 456, 'Four accent classes in Tokyo dialect — defined by position of downstep (if any)', 'middle', 'Ls')

    # Minimal pairs
    g += t(240, 467, 'Pitch accent minimal pairs (Tokyo standard):', 'middle', 'Ls')
    pairs = [
        ('はし', 'hashi', 'H-L', 'chopsticks'),
        ('はし', 'hashi', 'L-H', 'bridge'),
        ('はし', 'hashi', 'L-H-↓', 'edge'),
        ('あめ', 'ame', 'H-L', 'rain'),
        ('あめ', 'ame', 'L-H', 'candy'),
        ('かき', 'kaki', 'H-L', 'oyster'),
        ('かき', 'kaki', 'L-H', 'persimmon'),
        ('かき', 'kaki', 'L-H-↓', 'fence'),
    ]
    col4 = [60, 140, 220, 320]
    for i, (kana, rom, pitch, gloss) in enumerate(pairs):
        y = 477 + (i // 4) * 16
        cx = col4[i % 4]
        g += t(cx, y, kana, 'middle', 'Ljs')
        g += t(cx, y + 7, f'{rom} {pitch}', 'middle', 'Lx')
        g += t(cx, y + 13, gloss, 'middle', 'Lx')

    g += hr(510)

    # Prosody notes
    g += sh(518, 'PROSODY AND PHONOLOGICAL NOTES')
    g += t(240, 528, 'Particles は wa, が ga, を wo retain kana spelling but shift pronunciation (は = /wa/ as topic marker)', 'middle', 'Ls')
    g += t(240, 537, 'Pitch accent varies by dialect: Kyoto-Osaka has more complex system; many dialects are accentless (flat)', 'middle', 'Ls')
    g += t(240, 546, 'Loanword phonology: adapts to CV structure — "strike" → ストライク sutoraiku (6 morae)', 'middle', 'Ls')
    g += t(240, 555, 'Rendaku (sequential voicing 連濁): second element of compound gains voiced consonant: hana+bi → hanabi 花火', 'middle', 'Ls')
    g += t(240, 564, 'Onomatopoeia (擬音語 giongo, 擬態語 gitaigo): extremely productive — pika-pika, fura-fura, kira-kira', 'middle', 'Ls')
    g += t(240, 573, 'N-mora ん: pronounced [m] before b/p, [n] before t/d/n, [ŋ] before k/g, [ɴ] phrase-finally', 'middle', 'Ls')

    g += footer('18', 'Japanese', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 18C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_18c():
    g = open_svg()
    g += t(240, 32, 'JAPANESE — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 18C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # SOV
    g += sh(68, 'SENTENCE STRUCTURE — SOV + POSTPOSITIONS')
    g += t(240, 79, 'Japanese is strictly SOV (Subject–Object–Verb). Verb ALWAYS comes last.', 'middle', 'L')
    g += t(240, 89, 'わたしは　りんごを　たべます。  Watashi-wa ringo-wo tabemasu.  "I eat an apple."', 'middle', 'Ls')
    g += t(240, 98, 'S=わたし(I) + は(topic) · O=りんご(apple) + を(obj) · V=たべます(eat-POLITE)', 'middle', 'Lx')
    g += t(240, 107, 'Particles follow the noun they mark — they are POSTPOSITIONS not prepositions.', 'middle', 'Ls')

    # Particles table
    particles = [
        ('は wa', 'topic marker', 'わたしは watashi-wa "as for me"'),
        ('が ga', 'subject marker', 'ねこがいる neko-ga iru "a cat exists"'),
        ('を wo', 'direct object', 'りんごをたべる ringo-wo taberu "eat apple"'),
        ('に ni', 'direction/time/location', 'がっこうに gakkō-ni "to school / at school"'),
        ('で de', 'location of action/means', 'バスで basu-de "by bus"'),
        ('の no', 'possession/attribution', 'わたしの hon watashi-no hon "my book"'),
        ('と to', 'and / with', 'ともだちと tomodachi-to "with friend"'),
        ('か ka', 'question marker', 'これはなんですか? "What is this?"'),
        ('も mo', 'also / even', 'わたしも watashi-mo "I also"'),
        ('から kara', 'from / because', 'とうきょうから Tōkyō-kara "from Tokyo"'),
        ('まで made', 'until / up to', 'ごじまで goji-made "until 5 o\'clock"'),
    ]
    g += hr(116)
    g += sh(124, 'PARTICLES — GRAMMATICAL MARKERS')
    for i, (part, func, ex) in enumerate(particles):
        y = 133 + i * 12
        g += t(70, y, part, 'middle', 'Ls')
        g += t(170, y, func, 'middle', 'Lx')
        g += t(340, y, ex, 'middle', 'Lx')
    g += hr(268)

    # Verb conjugation
    g += sh(277, 'VERB CONJUGATION — GROUP 1 (U-VERBS): たべる → taberu')
    conj_data = [
        ('Dictionary', 'たべる', 'taberu', 'plain non-past'),
        ('Polite', 'たべます', 'tabemasu', 'formal non-past'),
        ('Negative plain', 'たべない', 'tabenai', 'plain negative'),
        ('Negative polite', 'たべません', 'tabemasen', 'formal negative'),
        ('Past plain', 'たべた', 'tabeta', 'plain past'),
        ('Past polite', 'たべました', 'tabemashita', 'formal past'),
        ('Te-form', 'たべて', 'tabete', 'connective / request base'),
        ('Volitional', 'たべよう', 'tabeyō', '"let\'s eat" / "I will eat"'),
        ('Conditional', 'たべれば', 'tabereba', '"if (one) eats"'),
        ('Potential', 'たべられる', 'taberareru', '"can eat"'),
    ]
    col3x = [80, 180, 270, 380]
    for i, (form, kana, rom, gloss) in enumerate(conj_data):
        y = 287 + i * 12
        g += t(80, y, form, 'middle', 'Lx')
        g += t(185, y, kana, 'middle', 'Ls')
        g += t(285, y, rom, 'middle', 'Lx')
        g += t(400, y, gloss, 'middle', 'Lx')
    g += hr(409)

    # Core vocabulary
    g += sh(418, 'CORE VOCABULARY — 25 WORDS')
    vocab = [
        ('はい / いいえ', 'hai / iie', 'yes / no'),
        ('ありがとう', 'arigatō', 'thank you'),
        ('すみません', 'sumimasen', 'excuse me / sorry'),
        ('わたし / あなた', 'watashi / anata', 'I / you'),
        ('これ / それ / あれ', 'kore/sore/are', 'this / that / that (far)'),
        ('どこ', 'doko', 'where'),
        ('なに', 'nani', 'what'),
        ('いつ', 'itsu', 'when'),
        ('だれ', 'dare', 'who'),
        ('なぜ', 'naze', 'why'),
        ('みず', 'mizu', 'water'),
        ('たべもの', 'tabemono', 'food'),
        ('ひと', 'hito', 'person / people'),
        ('ほん', 'hon', 'book'),
        ('でんしゃ', 'densha', 'train'),
        ('まち', 'machi', 'town / city'),
        ('やま', 'yama', 'mountain'),
        ('そら', 'sora', 'sky'),
        ('ひ / つき', 'hi / tsuki', 'sun / moon'),
        ('ことば', 'kotoba', 'word / language'),
        ('おおきい / ちいさい', 'ōkii / chiisai', 'big / small'),
        ('あたらしい / ふるい', 'atarashii / furui', 'new / old'),
        ('いい / わるい', 'ii / warui', 'good / bad'),
        ('みらい', 'mirai', 'future'),
        ('おもいで', 'omoide', 'memory / remembrance'),
    ]
    col_v = [70, 185, 290, 420]
    for i, (kana, rom, eng) in enumerate(vocab):
        y = 428 + i * 11
        g += t(70, y, kana, 'middle', 'Lx')
        g += t(210, y, rom, 'middle', 'Lx')
        g += t(370, y, eng, 'middle', 'Lx')
    g += hr(708 if 428 + 25*11 > 708 else 428 + 25*11 + 2)

    # Honorific system note
    yl = 428 + 25 * 11 + 8
    if yl < 595:
        g += sh(yl, 'POLITENESS LEVELS — KEIGO 敬語')
        g += t(240, yl+10, 'Japanese has grammaticalized politeness: plain (友達言葉), polite (丁寧語), honorific (尊敬語), humble (謙譲語)', 'middle', 'Lx')
        g += t(240, yl+19, '"eat": たべる (plain) · たべます (polite) · めしあがる (honorific) · いただく (humble)', 'middle', 'Lx')

    g += footer('18', 'Japanese', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 18D — RUNNING TEXT ─────────────────────────────────────────────────

def build_18d():
    g = open_svg()
    g += t(240, 32, 'JAPANESE — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 18D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1
    g += sh(67, 'PASSAGE 1 — GREETING AND INTRODUCTION')
    g += t(240, 77, 'はじめまして。わたしは　にんげんです。', 'middle', 'Ljs')
    g += t(240, 87, 'Hajimemashite.  Watashi wa  ningen  desu.', 'middle', 'Lx')
    g += t(240, 95, 'How-do-you-do  I     TOPIC  human  am/be-POLITE', 'middle', 'Lx')
    g += t(240, 103, '"How do you do. I am a human being."', 'middle', 'Ls')
    g += t(240, 112, 'ことばは　きおくです。きおくは　みらいへの　てがみです。', 'middle', 'Ljs')
    g += t(240, 122, 'Kotoba wa  kioku  desu.  Kioku wa  mirai e-no  tegami  desu.', 'middle', 'Lx')
    g += t(240, 130, 'Language TOP memory be.   Memory TOP future to-GEN letter  be.', 'middle', 'Lx')
    g += t(240, 138, '"Language is memory. Memory is a letter to the future."', 'middle', 'Ls')
    g += hr(145)

    # Passage 2
    g += sh(153, 'PASSAGE 2 — NATURE PASSAGE')
    g += t(240, 163, 'やまは　たかく、かわは　ふかい。', 'middle', 'Ljs')
    g += t(240, 173, 'Yama wa  takaku,  kawa wa  fukai.', 'middle', 'Lx')
    g += t(240, 181, 'Mountain TOP tall-CONJ  river TOP deep.', 'middle', 'Lx')
    g += t(240, 189, '"The mountain is high, the river is deep."', 'middle', 'Ls')
    g += t(240, 198, 'はるに　はなが　さき、ふゆに　ゆきが　ふる。', 'middle', 'Ljs')
    g += t(240, 208, 'Haru-ni  hana-ga  saki,  fuyu-ni  yuki-ga  furu.', 'middle', 'Lx')
    g += t(240, 216, 'Spring-LOC flower-SUBJ bloom,  winter-LOC snow-SUBJ fall.', 'middle', 'Lx')
    g += t(240, 224, '"In spring flowers bloom; in winter snow falls."', 'middle', 'Ls')
    g += hr(231)

    # Passage 3
    g += sh(239, 'PASSAGE 3 — TIME AND MEMORY (CLASSICAL STYLE)')
    g += t(240, 249, 'ゆく　かわの　ながれは　たえずして…', 'middle', 'Ljs')
    g += t(240, 259, 'Yuku  kawa-no  nagare wa  taezu-shite…', 'middle', 'Lx')
    g += t(240, 267, 'Going river-GEN flow  TOP  cease-not-CONJ…', 'middle', 'Lx')
    g += t(240, 275, '"The flow of a passing river never ceases…"  — Kamo no Chōmei, Hōjōki (1212)', 'middle', 'Ls')
    g += t(240, 284, 'むかしの　ひとの　こころも、いまの　わたしたちの　こころも、おなじ。', 'middle', 'Ljs')
    g += t(240, 294, 'Mukashi-no hito-no kokoro mo, ima-no watashitachi-no kokoro mo, onaji.', 'middle', 'Lx')
    g += t(240, 302, 'Old-GEN  person-GEN heart also, now-GEN we-GEN  heart also, same.', 'middle', 'Lx')
    g += t(240, 310, '"The hearts of people of old and the hearts of us today are the same."', 'middle', 'Ls')
    g += hr(317)

    # Passage 4
    g += sh(325, 'PASSAGE 4 — WISDOM SAYING')
    g += t(240, 335, 'なせばなる。なさねばならぬ。なにごとも。', 'middle', 'Ljs')
    g += t(240, 345, 'Naseba naru.  Nasaneba naranu.  Nanigoto mo.', 'middle', 'Lx')
    g += t(240, 353, 'Do-if become.  Do-not-if become-not.  Any-thing also.', 'middle', 'Lx')
    g += t(240, 361, '"If you try, you can. If you do not try, you cannot. In anything."  — Uesugi Yōzan', 'middle', 'Ls')
    g += hr(369)

    # Bridge phrase
    g += sh(378, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 390, 'この　ことばは　あなたのために、みらいを　おぼえた　ひとびとによって、じゆうに　つくられた。', 'middle', 'Ljs')
    g += t(240, 404, 'Kono kotoba wa anata-no tame-ni, mirai-wo oboeta hitobito-ni-yotte, jiyū-ni tsukureta.', 'middle', 'Lx')
    g += t(240, 413, 'This word/message TOP you-GEN for-PURP, future-ACC remembered people-by, freely made-was.', 'middle', 'Lx')
    g += t(240, 423, '"This message was made for you, freely, by people who remembered the future."', 'middle', 'Ls')
    g += hr(430)

    # Language note on "forward/future"
    g += sh(439, 'LANGUAGE NOTE — "FUTURE" IN JAPANESE')
    g += t(240, 450, 'Japanese expresses "forward in time" as 未来 mirai (not-yet-arrived) or 将来 shōrai (soon-coming).', 'middle', 'L')
    g += t(240, 461, 'mirai 未来: "not-yet + arrived" — the future as what has not yet come; used for distant/abstract future.', 'middle', 'Ls')
    g += t(240, 471, 'shōrai 将来: "about to + come" — the future as what is on its way; personal future, career, near-term.', 'middle', 'Ls')
    g += t(240, 481, 'The phrase uses おぼえた oboeta (remembered, past tense) with 未来 mirai — a deliberate paradox:', 'middle', 'Ls')
    g += t(240, 491, '"people who remembered the future" — echoing the project name: Remember Forward (未来へ向けて記憶する).', 'middle', 'Ls')
    g += t(240, 501, 'に よって ni yotte: "by means of / by (agent)" — the grammatical marker for passive agency in Japanese.', 'middle', 'Ls')
    g += t(240, 511, 'じゆうに jiyū-ni: "freely" — literally "free + ADV" — freedom from cost and from constraint.', 'middle', 'Ls')
    g += hr(520)

    # Kana encoding note
    g += sh(528, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 538, 'If the kana symbols are unfamiliar: consult Plate 18A for the full hiragana and katakana syllabary tables.', 'middle', 'Ls')
    g += t(240, 547, 'Each symbol represents one syllable (mora). Read left to right, top to bottom in modern printed text.', 'middle', 'Ls')
    g += t(240, 556, 'Romaji (Latin-alphabet transcription) is provided line-by-line above for all passages on this plate.', 'middle', 'Ls')
    g += t(240, 565, 'Japanese is spoken by ~125 million people, primarily in Japan. It is a language isolate — no confirmed relatives.', 'middle', 'Ls')

    g += footer('18', 'Japanese', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate18a_japanese_script.svg': build_18a(),
        'plate18b_japanese_phonology.svg': build_18b(),
        'plate18c_japanese_grammar.svg': build_18c(),
        'plate18d_japanese_text.svg': build_18d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
