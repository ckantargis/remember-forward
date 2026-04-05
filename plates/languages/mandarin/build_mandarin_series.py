#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Mandarin Chinese plate series 17A–17D for Remember Forward."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))


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
        '  .M  { font-size:6px; }\n'
        '  .F  { font-size:7px; font-style:italic; }\n'
        '  .Fb { font-size:7.5px; font-weight:bold; }\n'
        '  .Lc { font-size:13px; }\n'
        '  .Lcl{ font-size:17px; }\n'
        '  .Lcs{ font-size:10px; }\n'
        '  .Lcx{ font-size:8px; }\n'
        '</style>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="#000" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="#000" stroke-width="0.75"/>\n'
    )


def close_svg(pid, desc):
    return (
        '<line x1="20" y1="607" x2="460" y2="607" stroke="#000" stroke-width="0.3"/>\n'
        f'<text x="240" y="615" text-anchor="middle" class="M">'
        f'PLATE {esc(pid)} \u00b7 MANDARIN CHINESE \u00b7 {esc(desc)} \u00b7 CC BY-SA 4.0 \u00b7 rememberforward.org'
        f'</text>\n'
        '<line x1="20" y1="622" x2="460" y2="622" stroke="#000" stroke-width="0.3"/>\n'
        '<text x="240" y="631" text-anchor="middle" class="M">SERIES 17 OF 50 \u00b7 REMEMBER FORWARD</text>\n'
        '<line x1="20" y1="638" x2="460" y2="638" stroke="#000" stroke-width="0.3"/>\n'
        '<text x="240" y="648" text-anchor="middle" class="Fb">'
        'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.'
        '</text>\n'
        '<text x="240" y="663" text-anchor="middle" class="F">'
        'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET'
        '</text>\n'
        '</svg>\n'
    )


def t(x, y, s, a='middle', c='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'


def hr(y, w=0.3):
    return f'<line x1="20" y1="{y}" x2="460" y2="{y}" stroke="#000" stroke-width="{w}"/>\n'


def sh(y, txt):
    return (
        f'<text x="240" y="{y}" text-anchor="middle" class="H">'
        f'\u2014 \u00b7 \u2014  {esc(txt)}  \u2014 \u00b7 \u2014'
        f'</text>\n'
    )


def bx(x, y, w, h, sw=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#000" stroke-width="{sw}"/>\n'


# ─── PLATE 17A — SCRIPT ──────────────────────────────────────────────────────

def build_17a():
    g = open_svg()

    g += t(240, 32, 'MANDARIN CHINESE \u2014 SCRIPT \u00b7 WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 17A OF 50 \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # 1 ─ The Writing System
    g += sh(68, 'THE WRITING SYSTEM')
    g += t(240, 79, 'Logographic script: ~50,000 characters total; ~3,500 required for everyday literacy', 'middle', 'L')
    g += t(240, 89, 'Traditional \u7e41\u9ad4\u5b57 f\u00e1nt\u01d0z\u00ec (Taiwan, HK, Macau) \u00b7 Simplified \u7b80\u4f53\u5b57 ji\u01cen\u01d0z\u00ec (PRC, Singapore)', 'middle', 'Ls')
    g += t(240, 99, 'Unicode: CJK Unified Ideographs U+4E00\u2013U+9FFF (20,992 chars) + extension blocks', 'middle', 'Ls')
    g += t(240, 109, 'Direction: traditionally top\u2192bottom, right\u2192left column; modern usage: left\u2192right', 'middle', 'Ls')
    g += hr(118)

    # 2 ─ Character Structure
    g += sh(127, 'CHARACTER STRUCTURE')
    g += t(240, 138, 'Characters combine a semantic radical (meaning clue) + phonetic component (sound clue)', 'middle', 'L')
    g += t(240, 149, 'Pictographic \u8c61\u5f62 xi\u00e0ngx\u00edng: direct visual representations of objects', 'middle', 'Ls')

    picts = [
        ('\u65e5', 'r\u00ec', 'sun/day'),
        ('\u6708', 'yu\u00e8', 'moon'),
        ('\u5c71', 'sh\u0101n', 'mountain'),
        ('\u6728', 'm\u00f9', 'tree'),
        ('\u6c34', 'shu\u01d0', 'water'),
    ]
    for (ch, py, eng), x in zip(picts, [58, 152, 240, 328, 420]):
        g += t(x, 161, ch, 'middle', 'Lcs')
        g += t(x, 172, py, 'middle', 'Lx')
        g += t(x, 180, eng, 'middle', 'Lx')

    g += t(240, 191, 'Compound \u4f1a\u610f: \u660e m\u00edng (bright) = \u65e5 sun + \u6708 moon \u00b7 \u68ee s\u0113n (forest) = \u6728 + \u6728 + \u6728', 'middle', 'Ls')
    g += t(240, 201, 'Phono-semantic \u5f62\u58f0 x\u00edngsh\u0113ng (~90% of characters): radical signals meaning, phonetic signals sound', 'middle', 'Ls')
    g += hr(210)

    # 3 ─ Stroke Types
    g += sh(219, 'STROKE TYPES \u2014 \u6c38\u5b57\u516b\u6cd5: CHARACTER \u6c38 y\u01d2ng CONTAINS ALL EIGHT')
    strokes = [
        ('\u6a2a h\u00e9ng', '\u2192 horizontal'),
        ('\u7ced sh\u00f9',  '\u2193 vertical'),
        ('\u6487 pi\u011b',  '\u2199 left-falling'),
        ('\u6350 n\u00e0',   '\u2198 right-falling'),
        ('\u70b9 di\u01cen', '\u00b7 dot'),
        ('\u6298 zh\u00e9',  '\u21b1 turning'),
        ('\u9489 g\u014du',  '\u21b3 hook'),
        ('\u63d0 t\u00ed',   '\u2197 rising'),
    ]
    xs4 = [58, 172, 296, 410]
    for i, (name, desc) in enumerate(strokes):
        x = xs4[i % 4]
        y0 = 231 + (i // 4) * 22
        g += t(x, y0, name, 'middle', 'Ls')
        g += t(x, y0 + 11, desc, 'middle', 'Lx')
    g += t(240, 277, 'Rules: top\u2192bottom \u00b7 left\u2192right \u00b7 horizontal before vertical \u00b7 outside before inside', 'middle', 'Ls')
    g += hr(286)

    # 4 ─ Traditional vs Simplified
    g += sh(295, 'TRADITIONAL AND SIMPLIFIED \u2014 KEY PAIRS')
    for lbl, x in zip(['Traditional', 'Simplified', 'Pinyin', 'Meaning'], [78, 174, 268, 364]):
        g += t(x, 306, lbl, 'middle', 'Ls')
    g += hr(311, 0.2)
    pairs = [
        ('\u570b', '\u56fd', 'gu\u00f3',  'country/nation'),
        ('\u8a9e', '\u8bed', 'y\u01d4',   'language/speech'),
        ('\u5b78', '\u5b66', 'xu\u00e9',  'study/learn'),
        ('\u66f8', '\u4e66', 'sh\u016b',  'book/writing'),
        ('\u611b', '\u7231', '\u00e0i',   'love'),
        ('\u8eca', '\u8f66', 'ch\u0113',  'vehicle/car'),
    ]
    for i, (trad, simp, py, eng) in enumerate(pairs):
        y = 322 + i * 13
        g += t(78,  y, trad, 'middle', 'Lcs')
        g += t(174, y, simp, 'middle', 'Lcs')
        g += t(268, y, py,   'middle', 'Ls')
        g += t(364, y, eng,  'middle', 'Ls')
    g += hr(393)

    # 5 ─ Numerals
    g += sh(402, 'CHINESE NUMERALS')
    nums = [
        ('\u96f6', 'l\u00edng', '0'),
        ('\u4e00', 'y\u012b',   '1'),
        ('\u4e8c', '\u00e8r',   '2'),
        ('\u4e09', 's\u0101n',  '3'),
        ('\u56db', 's\u00ec',   '4'),
        ('\u4e94', 'w\u01d4',   '5'),
        ('\u516d', 'li\u00f9',  '6'),
        ('\u4e03', 'q\u012b',   '7'),
        ('\u516b', 'b\u0101',   '8'),
        ('\u4e5d', 'ji\u01d4',  '9'),
        ('\u5341', 'sh\u00ed',  '10'),
        ('\u767e', 'b\u01cei',  '100'),
        ('\u5343', 'qi\u0101n', '1k'),
        ('\u842c', 'w\u00e0n',  '10k'),
    ]
    for i, (ch, py, val) in enumerate(nums):
        x = 26 + i * 31
        g += t(x, 414, ch,  'middle', 'Lcs')
        g += t(x, 424, py,  'middle', 'Lx')
        g += t(x, 432, val, 'middle', 'Lx')
    g += hr(440)

    # 6 ─ Key Radicals
    g += sh(449, 'KEY KANGXI RADICALS \u2014 \u90e8\u9996 B\u00d9SH\u01d2U')
    g += t(240, 459, '214 Kangxi radicals (1716 CE) serve as the indexing system for all Chinese dictionaries', 'middle', 'Lx')
    radicals = [
        ('\u4eba', 'r\u00e9n', 'person (\u4ebb-)'),
        ('\u6c34', 'shu\u01d0', 'water (\u6c35-)'),
        ('\u6728', 'm\u00f9',  'tree/wood'),
        ('\u706b', 'hu\u01d2', 'fire (-\u706c)'),
        ('\u53e3', 'k\u01d2u', 'mouth'),
        ('\u624b', 'sh\u01d2u', 'hand (\u624c-)'),
        ('\u5fc3', 'x\u012bn', 'heart (\u5fc4-)'),
        ('\u76ee', 'm\u00f9',  'eye'),
        ('\u5973', 'n\u01da',  'woman'),
        ('\u5b50', 'z\u01d0',  'child'),
        ('\u5c71', 'sh\u0101n','mountain'),
        ('\u65e5', 'r\u00ec',  'sun/day'),
        ('\u8a00', 'y\u00e1n', 'speech (\u8a01-)'),
        ('\u91d1', 'j\u012bn', 'metal (\u9215-)'),
        ('\u9580', 'm\u00e9n', 'door (\u95e8)'),
        ('\u571f', 't\u01d4',  'earth/soil'),
        ('\u6708', 'yu\u00e8', 'moon/month'),
        ('\u5927', 'd\u00e0',  'big/great'),
        ('\u529b', 'l\u00ec',  'strength'),
        ('\u8db3', 'z\u00fa',  'foot/leg'),
    ]
    xs_r = [58, 172, 296, 410]
    for i, (ch, py, eng) in enumerate(radicals):
        x = xs_r[i % 4]
        y0 = 470 + (i // 4) * 29
        g += t(x, y0,      ch,          'middle', 'Lcs')
        g += t(x, y0 + 11, py + ' \u2014 ' + eng, 'middle', 'Lx')

    g += close_svg('17A', 'SCRIPT')
    return g


# ─── PLATE 17B — PHONOLOGY ───────────────────────────────────────────────────

def build_17b():
    g = open_svg()

    g += t(240, 32, 'MANDARIN CHINESE \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 50, 'SERIES 17B OF 50 \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # 1 ─ Four Tones
    g += sh(68, 'THE FOUR TONES \u2014 \u56db\u58f0 S\u00ccSH\u0112NG')
    tone_data = [
        ('Tone 1', '\u9634\u5e73', '\u0101 \u2014\u2014\u2014', '[55] high-level', '\u5988 m\u0101 = mother'),
        ('Tone 2', '\u9633\u5e73', '\u00e1 \u2197',             '[35] rising',     '\u9ebb m\u00e1 = hemp'),
        ('Tone 3', '\u4e0a\u58f0', '\u01ce \u2198\u2197',       '[214] dip\u2013rise', '\u9a6c m\u01ce = horse'),
        ('Tone 4', '\u53bb\u58f0', '\u00e0 \u2198\u2198',       '[51] falling',    '\u9a82 m\u00e0 = scold'),
    ]
    for i, (label, chin, mark, chao, ex) in enumerate(tone_data):
        x = 22 + i * 110
        g += bx(x, 78, 100, 60)
        g += t(x + 50, 90,  label, 'middle', 'Ls')
        g += t(x + 50, 100, chin,  'middle', 'Lcx')
        g += t(x + 50, 112, mark,  'middle', 'L')
        g += t(x + 50, 122, chao,  'middle', 'Lx')
        g += t(x + 50, 132, ex,    'middle', 'Lx')

    g += t(240, 150, 'Neutral (light) tone \u8f7b\u58f0 q\u012bngsh\u0113ng: \u5417 ma (question) \u00b7 \u4e86 le (completed) \u2014 unstressed, context pitch', 'middle', 'Ls')
    g += t(240, 161, 'Tone sandhi: Tone 3 + Tone 3 \u2192 Tone 2 + Tone 3 \u2014 \u4f60\u597d n\u01d0h\u01ceo \u2192 n\u00edh\u01ceo (hello)', 'middle', 'Ls')
    g += hr(170)

    # 2 ─ 21 Initials
    g += sh(180, 'THE 21 INITIALS \u2014 CONSONANTS')
    g += t(240, 191, 'Bilabial: b [p]  p [p\u02b0]  m [m]  f [f]', 'middle', 'L')
    g += t(240, 202, 'Alveolar: d [t]  t [t\u02b0]  n [n]  l [l]', 'middle', 'L')
    g += t(240, 213, 'Velar: g [k]  k [k\u02b0]  h [x]', 'middle', 'L')
    g += t(240, 224, 'Palatal: j [t\u0255]  q [t\u0255\u02b0]  x [\u0255]  \u2014 only before i and \u00fc', 'middle', 'L')
    g += t(240, 235, 'Retroflex: zh [\u0288\u0282]  ch [\u0288\u0282\u02b0]  sh [\u0282]  r [\u027b]  \u2014 tongue curled back', 'middle', 'L')
    g += t(240, 246, 'Dental sibilant: z [ts]  c [ts\u02b0]  s [s]', 'middle', 'L')
    g += t(240, 257, 'KEY: b/p  d/t  g/k  j/q  zh/ch  z/c \u2014 ASPIRATED vs UNASPIRATED pairs, NOT voiced vs voiceless', 'middle', 'Ls')
    g += hr(266)

    # 3 ─ Finals
    g += sh(276, 'FINALS \u2014 VOWELS AND ENDINGS')
    g += t(240, 287, 'Simple: a [a]  o [o]  e [\u0264/\u0259]  i [i/\u0268]  u [u]  \u00fc [y]', 'middle', 'L')
    g += t(240, 298, 'Compound: ai [ai]  ei [ei]  ao [au]  ou [ou]  ia [ia]  ie [i\u025b]  ua [wa]  uo [wo]', 'middle', 'L')
    g += t(240, 309, 'Nasal -n: an [an]  en [\u0259n]  in [in]  ian [i\u025bn]  uan [wan]  \u00fcn [yn]', 'middle', 'L')
    g += t(240, 320, 'Nasal -ng: ang [a\u014b]  eng [\u0259\u014b]  ing [i\u014b]  ong [\u028a\u014b]  iang [ia\u014b]  uang [wa\u014b]', 'middle', 'L')
    g += t(240, 331, 'Special: er [\u025a] \u2014 rhotacized \u2014 \u4e8c \u00e8r (two) \u00b7 \u513f \u00e9r (child/suffix)', 'middle', 'L')
    g += hr(340)

    # 4 ─ Key Contrasts
    g += sh(350, 'KEY CONTRASTS AND SPECIAL RULES')
    g += t(240, 361, 'Retroflex zh ch sh r: tongue curled to palate \u2014 completely distinct from dental z c s', 'middle', 'L')
    g += t(240, 372, '\u00fc-rule: after j q x, \u00fc is written u \u2014 ju = [t\u0255y]  qu = [t\u0255\u02b0y]  xu = [\u0255y]', 'middle', 'L')
    g += t(240, 383, 'x [\u0255] palatal \u2260 sh [\u0282] retroflex \u2014 \u897f x\u012b (west) \u2260 \u8bd7 sh\u012b (poetry)', 'middle', 'L')
    g += t(240, 394, 'i after zh/ch/sh/r/z/c/s = apical vowel [\u0268] (tongue tip), not clear [i]: \u5e08 sh\u012b', 'middle', 'Ls')
    g += hr(403)

    # 5 ─ Tonal Minimal Sets
    g += sh(413, 'TONAL MINIMAL SETS')
    g += t(240, 424, 'm\u0101  m\u00e1  m\u01ce  m\u00e0  ma', 'middle', 'L')
    g += t(240, 436, '\u5988   \u9ebb   \u9a6c   \u9a82   \u5417', 'middle', 'Lcs')
    g += t(240, 448, 'mother / hemp / horse / scold / question-particle', 'middle', 'Lx')
    g += t(240, 460, 't\u0101ng  t\u00e1ng  t\u01ceng  t\u00e0ng', 'middle', 'L')
    g += t(240, 472, '\u6c64    \u5510    \u8eba    \u70eb', 'middle', 'Lcs')
    g += t(240, 484, 'soup / Tang Dynasty / lie down / scald', 'middle', 'Lx')
    g += hr(493)

    # 6 ─ Tones in Writing and Poetry
    g += sh(503, 'TONES IN WRITING AND POETRY')
    g += t(240, 514, 'Pinyin marks tones on the vowel nucleus: \u0101 \u00e1 \u01ce \u00e0 (no mark = neutral tone)', 'middle', 'L')
    g += t(240, 525, 'Everyday Chinese writing carries no tone marks \u2014 context determines reading', 'middle', 'L')
    g += t(240, 536, 'Classical poetry used tonal patterns (\u5e73\u4ed4 p\u00edngz\u00e8): even (Tones 1\u20132) vs oblique (Tones 3\u20134)', 'middle', 'L')
    g += t(240, 547, 'Tang Dynasty regulated verse (l\u01da sh\u012b): strict tonal alternation per line and matching couplet', 'middle', 'Ls')
    g += hr(556)

    g += close_svg('17B', 'PHONOLOGY')
    return g


# ─── PLATE 17C — GRAMMAR ─────────────────────────────────────────────────────

def build_17c():
    g = open_svg()

    g += t(240, 32, 'MANDARIN CHINESE \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 17C OF 50 \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # 1 ─ Word Order
    g += sh(68, 'BASIC WORD ORDER \u2014 SVO')
    g += t(240, 79, 'Subject \u2192 Verb \u2192 Object (parallel to English; unlike Latin or Japanese)', 'middle', 'L')
    svo = [('\u6211 w\u01d2', 'I'), ('\u5403 ch\u012b', 'eat'), ('\u996d f\u00e0n', 'rice')]
    for i, (chin, eng) in enumerate(svo):
        bx_x = 88 + i * 110
        g += bx(bx_x, 85, 92, 28)
        g += t(bx_x + 46, 97,  chin, 'middle', 'Ls')
        g += t(bx_x + 46, 107, eng,  'middle', 'Lx')
    g += t(184, 99, '\u2192', 'middle', 'L')
    g += t(294, 99, '\u2192', 'middle', 'L')
    g += t(240, 124, 'Modifiers precede: \u7ea2\u8272\u7684\u82f9\u679c h\u00f3ngs\u00e8 de p\u00ednggu\u01d2 = red-DE apple = "red apple"', 'middle', 'Ls')
    g += hr(133)

    # 2 ─ ba construction
    g += sh(143, 'THE \u628a B\u01ce CONSTRUCTION \u2014 DISPOSAL OF OBJECT')
    g += t(240, 154, 'S + \u628a + Object + Verb + Result / Direction', 'middle', 'L')
    g += t(240, 166, '\u6211\u628a\u4e66\u653e\u5728\u684c\u4e0a', 'middle', 'Lcs')
    g += t(240, 179, 'w\u01d2 b\u01ce sh\u016b f\u00e0ng z\u00e0i zhu\u014f sh\u00e0ng', 'middle', 'Ls')
    g += t(240, 189, 'I  BA  book  put  at  table  above  =  \u201cI put the book on the table\u201d', 'middle', 'Lx')
    g += t(240, 199, 'Required when an action has a clear result or physical effect on a specific object', 'middle', 'Ls')
    g += hr(208)

    # 3 ─ Aspect Markers
    g += sh(218, 'ASPECT MARKERS \u2014 \u65f6\u6001 SH\u00cdT\u00c0I')
    g += t(240, 229, 'Chinese marks ASPECT (completion / state) not TENSE \u2014 time is set by context', 'middle', 'Ls')
    aspects = [
        ('\u4e86 le',   'perfective',       '\u6211\u5403\u4e86',           'w\u01d2 ch\u012b le  \u201cI ate / have eaten\u201d'),
        ('\u8fc7 gu\u00f2', 'experiential', '\u6211\u53bb\u8fc7\u5317\u4eac', 'w\u01d2 q\u00f9 gu\u00f2 B\u011dij\u012bng  \u201cI have been to Beijing\u201d'),
        ('\u7740 zhe',  'continuous state',  '\u5979\u7b11\u7740',           't\u0101 xi\u00e0o zhe  \u201cshe is smiling\u201d'),
        ('\u5728 z\u00e0i', 'in progress',  '\u4ed6\u5728\u5403\u996d',      't\u0101 z\u00e0i ch\u012bf\u00e0n  \u201che is eating\u201d'),
    ]
    for i, (marker, meaning, ex_c, ex_e) in enumerate(aspects):
        y = 241 + i * 22
        g += t(58,  y, marker,  'middle', 'Ls')
        g += t(140, y, '\u2014 ' + meaning + ':', 'start', 'Lx')
        g += t(272, y, ex_c,    'middle', 'Lcs')
        g += t(408, y, ex_e,    'middle', 'Lx')
    g += hr(330)

    # 4 ─ Measure Words
    g += sh(340, 'MEASURE WORDS \u2014 \u91cf\u8bcd LI\u00c0NGC\u00cd')
    g += t(240, 351, 'Number + Measure Word + Noun is required \u2014 no direct equivalent in English', 'middle', 'Ls')
    mws = [
        ('\u4e2a g\u00e8',      'general',        '\u4e00\u4e2a\u4eba',        'y\u012b g\u00e8 r\u00e9n',         'one person'),
        ('\u672c b\u011bn',     'bound volumes',  '\u4e09\u672c\u4e66',        's\u0101n b\u011bn sh\u016b',        'three books'),
        ('\u5f20 zh\u0101ng',   'flat objects',   '\u4e00\u5f20\u7eb8',        'y\u012b zh\u0101ng zh\u01d0',       'one sheet of paper'),
        ('\u6761 ti\u00e1o',    'long flexible',  '\u4e00\u6761\u9c7c',        'y\u012b ti\u00e1o y\u00fa',         'one fish'),
        ('\u53ea zh\u012b',     'small creatures','\u4e24\u53ea\u732b',        'li\u01ceng zh\u012b m\u0101o',      'two cats'),
        ('\u5ea7 zu\u00f2',     'large structures','\u4e00\u5ea7\u5c71',       'y\u012b zu\u00f2 sh\u0101n',        'one mountain'),
    ]
    for i, (mw, meaning, ex_c, ex_py, ex_e) in enumerate(mws):
        y = 362 + i * 14
        g += t(52,  y, mw,                   'middle', 'Ls')
        g += t(127, y, '\u2014 ' + meaning,  'start',  'Lx')
        g += t(255, y, ex_c,                  'middle', 'Lcs')
        g += t(350, y, ex_py,                 'middle', 'Lx')
        g += t(430, y, ex_e,                  'middle', 'Lx')
    g += hr(449)

    # 5 ─ The Three DE
    g += sh(459, 'THE THREE DE \u2014 \u7684 \u5730 \u5f97')
    de_data = [
        ('\u7684 de', 'attributive', '\u6211\u7684\u4e66',         'w\u01d2 de sh\u016b',          'my book'),
        ('\u5730 de', 'adverbial',   '\u6162\u6162\u5730\u8d70',   'm\u00e0nm\u00e0n de z\u01d2u',  'walk slowly'),
        ('\u5f97 de', 'resultative', '\u8dd1\u5f97\u5f88\u5feb',   'p\u01ceo de h\u011bn ku\u00e0i','runs very fast'),
    ]
    for i, (ch, meaning, ex_c, ex_py, ex_e) in enumerate(de_data):
        y = 471 + i * 14
        g += t(52,  y, ch,                    'middle', 'Ls')
        g += t(120, y, '\u2014 ' + meaning,   'start',  'Lx')
        g += t(255, y, ex_c,                   'middle', 'Lcs')
        g += t(352, y, ex_py,                  'middle', 'Lx')
        g += t(432, y, ex_e,                   'middle', 'Lx')
    g += hr(509)

    # 6 ─ Vocabulary
    g += sh(519, 'CORE VOCABULARY \u2014 30 WORDS')
    vocab_cols = [
        [('\u4eba r\u00e9n','person'),('\u6c34 shu\u01d0','water'),('\u706b hu\u01d2','fire'),
         ('\u5929 ti\u0101n','sky/heaven'),('\u5730 d\u00ec','earth'),('\u65e5 r\u00ec','sun/day'),
         ('\u6708 yu\u00e8','moon'),('\u5c71 sh\u0101n','mountain'),('\u6728 m\u00f9','tree/wood'),('\u5fc3 x\u012bn','heart')],
        [('\u6211 w\u01d2','I/me'),('\u4f60 n\u01d0','you'),('\u4ed6/\u5979 t\u0101','he/she'),
         ('\u6765 l\u00e1i','come'),('\u53bb q\u00f9','go'),('\u5403 ch\u012b','eat'),
         ('\u559d h\u0113','drink'),('\u8bf4 shu\u014d','speak'),('\u770b k\u00e0n','see/read'),('\u8d70 z\u01d2u','walk/go')],
        [('\u5927 d\u00e0','big'),('\u5c0f xi\u01ceo','small'),('\u597d h\u01ceo','good'),
         ('\u591a du\u014d','many'),('\u5c11 sh\u01ceo','few'),('\u5bb6 ji\u0101','home'),
         ('\u4e66 sh\u016b','book'),('\u8def l\u00f9','road'),('\u7231 \u00e0i','love'),('\u751f sh\u0113ng','life/birth')],
    ]
    for ci, col in enumerate(vocab_cols):
        x = 80 + ci * 160
        for ri, (word, meaning) in enumerate(col):
            g += t(x, 530 + ri * 7, word + '  \u2014  ' + meaning, 'middle', 'Lx')

    g += close_svg('17C', 'GRAMMAR')
    return g


# ─── PLATE 17D — RUNNING TEXT ─────────────────────────────────────────────────

def build_17d():
    g = open_svg()

    g += t(240, 32, 'MANDARIN CHINESE \u2014 RUNNING TEXT \u00b7 INTERLINEAR', 'middle', 'T')
    g += t(240, 50, 'SERIES 17D OF 50 \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # 1 ─ Confucius
    g += sh(68, 'CONFUCIUS \u00b7 ANALECTS 1.1 \u00b7 \u8bba\u8bed \u00b7 c. 500 BCE')
    g += t(240, 80, '\u5b50\u66f0\uff1a\u5b66\u800c\u65f6\u4e60\u4e4b\uff0c\u4e0d\u4ea6\u8bf4\u4e4e\uff1f', 'middle', 'Lcs')
    g += t(240, 93, 'z\u01d0 yu\u0113: xu\u00e9 \u00e9r sh\u00ed x\u00ed zh\u012b, b\u00f9 y\u00ec yu\u00e8 h\u016b?', 'middle', 'Ls')
    g += t(240, 104, 'master says: learn and time/often practice it, not also joy?', 'middle', 'Lx')
    g += t(240, 115, '\u201cThe Master said: To learn, and then to practice it often \u2014 is that not a joy?\u201d', 'middle', 'Ls')
    g += t(240, 125, 'Note: \u8bf4 here is read yu\u00e8 (rejoice), not shu\u014d (speak) \u2014 a Classical Chinese homograph', 'middle', 'Lx')
    g += hr(134)

    # 2 ─ Laozi
    g += sh(144, 'LAOZI \u00b7 TAO TE CHING 1 \u00b7 \u9053\u5fb7\u7ecf \u00b7 c. 400 BCE')
    g += t(240, 156, '\u9053\u53ef\u9053\uff0c\u975e\u5e38\u9053\u3002\u540d\u53ef\u540d\uff0c\u975e\u5e38\u540d\u3002', 'middle', 'Lcs')
    g += t(240, 169, 'd\u00e0o k\u011b d\u00e0o, f\u0113i ch\u00e1ng d\u00e0o. m\u00edng k\u011b m\u00edng, f\u0113i ch\u00e1ng m\u00edng.', 'middle', 'Ls')
    g += t(240, 180, 'way can be-spoken, not eternal way. name can be-named, not eternal name.', 'middle', 'Lx')
    g += t(240, 191, '\u201cThe Way that can be spoken is not the eternal Way. The name that can be named is not the eternal name.\u201d', 'middle', 'Ls')
    g += hr(201)

    # 3 ─ Li Bai
    g += sh(211, 'LI BAI \u00b7 QUIET NIGHT THOUGHT \u00b7 \u9759\u591c\u601d \u00b7 701\u2013762 CE')
    g += t(240, 222, '\u5e8a\u524d\u660e\u6708\u5149\uff0c\u7591\u662f\u5730\u4e0a\u971c\u3002', 'middle', 'Lcs')
    g += t(240, 235, 'chu\u00e1ng qi\u00e1n m\u00edng yu\u00e8 gu\u0101ng, y\u00ed sh\u00ec d\u00ec sh\u00e0ng shu\u0101ng.', 'middle', 'Ls')
    g += t(240, 246, 'bed before bright moon light, suspect is ground above frost.', 'middle', 'Lx')
    g += t(240, 257, '\u201cBefore my bed, bright moonlight \u2014 I thought it was frost on the ground.\u201d', 'middle', 'Ls')
    g += t(240, 268, '\u4e3e\u5934\u671b\u660e\u6708\uff0c\u4f4e\u5934\u601d\u6545\u4e61\u3002', 'middle', 'Lcs')
    g += t(240, 281, 'j\u01d4 t\u00f3u w\u00e0ng m\u00edng yu\u00e8, d\u012b t\u00f3u s\u012b g\u00f9 xi\u0101ng.', 'middle', 'Ls')
    g += t(240, 292, 'raise head gaze bright moon, lower head think old hometown.', 'middle', 'Lx')
    g += t(240, 303, '\u201cI raised my head to gaze at the bright moon; I lowered it and thought of home.\u201d', 'middle', 'Ls')
    g += hr(313)

    # 4 ─ Xunzi
    g += sh(323, 'XUNZI \u00b7 PROVERB \u00b7 \u8346\u5b50 \u00b7 c. 310\u2013235 BCE')
    g += t(240, 335, '\u4e0d\u79ef\u8deb\u6b65\uff0c\u65e0\u4ee5\u81f3\u5343\u91cc\u3002', 'middle', 'Lcs')
    g += t(240, 348, 'b\u00f9 j\u012b ku\u01d0 b\u00f9, w\u00fa y\u01d0 zh\u00ec qi\u0101n l\u01d0.', 'middle', 'Ls')
    g += t(240, 359, 'not accumulate half-steps, no-way reach thousand li.', 'middle', 'Lx')
    g += t(240, 370, '\u201cWithout small steps, one cannot travel a thousand li.\u201d (1 li \u2248 500 m)', 'middle', 'Ls')
    g += hr(381)

    # 5 ─ Bridge Phrase
    g += sh(391, 'THE BRIDGE PHRASE')
    g += bx(20, 398, 440, 92)
    g += t(240, 414, '\u6b64\u7269\u4e3a\u4f60\u800c\u9020\uff0c\u65e0\u507f\u5949\u4e0a\uff0c', 'middle', 'Lcs')
    g += t(240, 432, '\u51fa\u81ea\u90a3\u4e9b\u9298\u8bb0\u672a\u6765\u7684\u4eba\u3002', 'middle', 'Lcs')
    g += t(240, 449, 'c\u01d0 w\u00f9 w\u00e8i n\u01d0 \u00e9r z\u00e0o, w\u00fa ch\u00e1ng f\u00e8ng sh\u00e0ng,', 'middle', 'Ls')
    g += t(240, 460, 'ch\u016b z\u00ec n\u00e0 xi\u0113 m\u00edng j\u00ec w\u00e8il\u00e1i de r\u00e9n.', 'middle', 'Ls')
    g += t(240, 473, '\u201cThis was made for you, freely, by those who kept the future in memory.\u201d', 'middle', 'Ls')
    g += hr(497)

    # 6 ─ Note
    g += sh(507, 'NOTE ON \u201cREMEMBERED FORWARD\u201d')
    g += t(240, 518, 'Chinese expresses "the future" as \u672a\u6765 w\u00e8il\u00e1i \u2014 "what has not yet arrived."', 'middle', 'L')
    g += t(240, 529, '\u524d qi\u00e1n (forward/in front) traditionally meant the PAST \u2014 what you have already passed.', 'middle', 'Ls')
    g += t(240, 539, '\u540e h\u00f2u (behind/after) meant the FUTURE \u2014 what comes after you, not yet seen.', 'middle', 'Ls')
    g += t(240, 549, 'The bridge phrase uses \u9298\u8bb0\u672a\u6765 m\u00edng j\u00ec w\u00e8il\u00e1i: "to engrave the future in memory."', 'middle', 'Ls')
    g += t(240, 559, 'Simplified characters throughout; Traditional equivalents given on Plate 17A.', 'middle', 'Lx')
    g += hr(567)

    g += close_svg('17D', 'RUNNING TEXT')
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = [
        ('plate17a_mandarin_script.svg',    build_17a()),
        ('plate17b_mandarin_phonology.svg', build_17b()),
        ('plate17c_mandarin_grammar.svg',   build_17c()),
        ('plate17d_mandarin_text.svg',      build_17d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {fname}')


if __name__ == '__main__':
    main()
