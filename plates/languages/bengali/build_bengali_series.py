#!/usr/bin/env python3
"""
Build Bengali language series — plates 16A–16D
Remember Forward · The Patient Message · CC BY-SA 4.0 · rememberforward.org
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

STYLE = """<defs><style>
  text{font-family:Georgia,serif;fill:#000;}
  .T{font-size:12px;font-weight:bold;letter-spacing:2px;}
  .S{font-size:7px;letter-spacing:1.5px;}
  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px;}
  .L{font-size:7px;}
  .Ls{font-size:6px;}
  .Lx{font-size:5.5px;}
  .Lb{font-size:14px;}
  .Lbm{font-size:11px;}
  .Lbs{font-size:9px;}
  .M{font-size:6px;letter-spacing:1px;}
  .F{font-size:7px;font-style:italic;}
  .Fb{font-size:7.5px;font-weight:bold;}
</style></defs>"""

def svg_open():
    return (f'<svg viewBox="0 0 480 680" xmlns="http://www.w3.org/2000/svg">\n{STYLE}\n'
            '<rect x="6" y="6" width="468" height="668" rx="4" fill="none" stroke="#000" stroke-width="3"/>\n'
            '<rect x="12" y="12" width="456" height="656" rx="2" fill="none" stroke="#000" stroke-width="0.75"/>')

def svg_close():
    return ('<line x1="18" y1="615" x2="462" y2="615" stroke="#000" stroke-width="0.5"/>\n'
            '<text x="240" y="624" text-anchor="middle" class="M">'
            'REMEMBER FORWARD \u00b7 THE PATIENT MESSAGE \u00b7 CC BY-SA 4.0 \u00b7 rememberforward.org'
            '</text>\n'
            '<line x1="18" y1="630" x2="462" y2="630" stroke="#000" stroke-width="1"/>\n'
            '<text x="240" y="648" text-anchor="middle" class="Fb">'
            'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.'
            '</text>\n'
            '<text x="240" y="663" text-anchor="middle" class="F">'
            'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET'
            '</text>\n</svg>')

def title_block(title, subtitle):
    return (f'<text x="240" y="32" text-anchor="middle" class="T">{esc(title)}</text>\n'
            '<line x1="18" y1="39" x2="462" y2="39" stroke="#000" stroke-width="0.75"/>\n'
            f'<text x="240" y="50" text-anchor="middle" class="S">{esc(subtitle)}</text>\n'
            '<line x1="18" y1="56" x2="462" y2="56" stroke="#000" stroke-width="0.5"/>')

def sh(y, t):
    return f'<text x="240" y="{y}" text-anchor="middle" class="H">\u2014 \u00b7 \u2014  {esc(t)}  \u2014 \u00b7 \u2014</text>'

def hl(y, w=0.3):
    return f'<line x1="22" y1="{y}" x2="458" y2="{y}" stroke="#000" stroke-width="{w}"/>'

def tx(x, y, s, anchor='middle', cls='Lx'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(s)}</text>'

def bx(x, y, w, h, sw=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#000" stroke-width="{sw}"/>'


# ═══════════════════════════════════════════════════════════════
# PLATE 16A  ·  BENGALI  ·  SCRIPT
# ═══════════════════════════════════════════════════════════════
def build_16a():
    out = [svg_open(),
           title_block("PLATE 16A  \u00b7  BENGALI  \u00b7  SCRIPT",
                       "\u09ac\u09be\u0982\u09b2\u09be \u00b7 1,000 years \u00b7 Indo-Aryan \u00b7"
                       " abugida \u00b7 left to right \u00b7 11 vowels \u00b7 39 consonants")]

    # Intro
    out.append(sh(67, "BENGALI  \u00b7  THE LANGUAGE OF GOLDEN BENGAL"))
    out.append(hl(71))
    out.append(tx(240,  79, "Bengali (\u09ac\u09be\u0982\u09b2\u09be Bangla) is the 7th most spoken language  \u00b7  300 million speakers worldwide"))
    out.append(tx(240,  88, "official language of Bangladesh and West Bengal  \u00b7  also used in Assam and Tripura"))
    out.append(tx(240,  97, "abugida: every consonant carries inherent vowel /\u0254/  \u00b7  diacritics override it"))
    out.append(tx(240, 106, "script evolved from Brahmi via Siddhamatrika  \u00b7  Unicode block U+0980\u2013U+09FF"))
    out.append(hl(110, 0.5))

    # Vowels
    out.append(sh(117, "11 INDEPENDENT VOWELS  \u00b7  \u09b8\u09cd\u09ac\u09b0\u09ac\u09b0\u09cd\u09a3  \u00b7  SHOROBORNO"))
    out.append(hl(121))
    out.append(tx(240, 129, "vowels stand alone at syllable start \u00b7 as diacritics on consonants otherwise \u00b7 /\u0254/ is the inherent vowel"))

    vowels = [
        ('\u0985','\u00f4','/\u0254/'), ('\u0986','\u0101','/a/'), ('\u0987','i','/i/'),
        ('\u0988','\u012b','/i/'),       ('\u0989','u','/u/'),      ('\u098a','\u016b','/u/'),
        ('\u098b','\u1e5b','/ri/'),      ('\u098f','e','/e/'),      ('\u0990','oi','/oi\u032f/'),
        ('\u0993','o','/o/'),            ('\u0994','ou','/ou\u032f/'),
    ]
    bw, bh, y0 = 39, 38, 133
    for i, (ltr, rom, ipa) in enumerate(vowels):
        x = 22 + i*bw
        out.append(bx(x, y0, bw, bh))
        out.append(tx(x+19, y0+17, ltr, 'middle', 'Lb'))
        out.append(tx(x+19, y0+28, rom, 'middle', 'Lx'))
        out.append(tx(x+19, y0+36, ipa, 'middle', 'Lx'))
    out.append(hl(175, 0.5))

    # Diacritics
    out.append(sh(181, "VOWEL DIACRITICS  \u00b7  \u0995\u09be\u09b0  \u00b7  KAAR  \u00b7  SHOWN ON CONSONANT \u0995 (K)"))
    out.append(hl(185))
    out.append(tx(240, 193, "consonant + diacritic replaces /\u0254/ \u00b7 hasanta \u09cd removes inherent vowel entirely \u00b7 \u0995 alone = /k\u0254/"))

    diacritics = [
        ('\u0995\u09be','k\u0101','\u0101'), ('\u0995\u09bf','ki','i'), ('\u0995\u09c0','k\u012b','\u012b'),
        ('\u0995\u09c1','ku','u'),            ('\u0995\u09c2','k\u016b','\u016b'), ('\u0995\u09c3','k\u1e5b','\u1e5b'),
        ('\u0995\u09c7','ke','e'),            ('\u0995\u09c8','koi','oi'), ('\u0995\u09cb','ko','o'),
        ('\u0995\u09cc','kou','ou'),
    ]
    dbw, dbh, dy = 43, 34, 198
    for i, (frm, rom, lbl) in enumerate(diacritics):
        x = 22 + i*dbw
        out.append(bx(x, dy, dbw, dbh))
        out.append(tx(x+21, dy+16, frm, 'middle', 'Lb'))
        out.append(tx(x+21, dy+26, rom, 'middle', 'Lx'))
        out.append(tx(x+21, dy+33, lbl, 'middle', 'Lx'))
    out.append(tx(240, 237, "\u0995\u09cd = /k/ (hasanta kills /\u0254/) \u00b7 conjunct: \u0995 + \u09cd + \u09b7 = \u0995\u09cd\u09b7 /k\u0283/ \u00b7 clusters of up to 4 consonants fuse into one ligature"))
    out.append(hl(242, 0.5))

    # Consonants
    out.append(sh(248, "32 BASIC CONSONANTS  \u00b7  \u09ac\u09cd\u09af\u099e\u09cd\u099c\u09a8\u09ac\u09b0\u09cd\u09a3  \u00b7  BYANJANBORNO"))
    out.append(hl(252))
    out.append(tx(240, 258, "ordered by place of articulation: velar \u2192 palatal \u2192 retroflex \u2192 dental \u2192 labial \u2192 other"))

    lw, cbh = 26, 28
    cw5 = 82   # (458-22-26) / 5 = 82
    cw7 = 58   # (458-22-26) / 7 ≈ 58

    con_rows = [
        ('velar',    [('\u0995','k'),('\u0996','kh'),('\u0997','g'),('\u0998','gh'),('\u0999','ng')]),
        ('palatal',  [('\u099a','c'),('\u099b','ch'),('\u099c','j'),('\u099d','jh'),('\u099e','\u00f1')]),
        ('retroflex',[('\u099f','\u1e6d'),('\u09a0','\u1e6dh'),('\u09a1','\u1e0d'),('\u09a2','\u1e0dh'),('\u09a3','\u1e47')]),
        ('dental',   [('\u09a4','t'),('\u09a5','th'),('\u09a6','d'),('\u09a7','dh'),('\u09a8','n')]),
        ('labial',   [('\u09aa','p'),('\u09ab','ph'),('\u09ac','b'),('\u09ad','bh'),('\u09ae','m')]),
    ]
    cy = 263
    for lbl, row in con_rows:
        out.append(bx(22, cy, lw, cbh, 0.6))
        out.append(tx(22+lw//2, cy+cbh//2+3, lbl, 'middle', 'Lx'))
        for j, (ltr, rom) in enumerate(row):
            x = 22 + lw + j*cw5
            out.append(bx(x, cy, cw5, cbh, 0.6))
            out.append(tx(x+cw5//2, cy+17, ltr, 'middle', 'Lb'))
            out.append(tx(x+cw5//2, cy+26, rom, 'middle', 'Lx'))
        cy += cbh

    other = [('\u09af','y'),('\u09b0','r'),('\u09b2','l'),('\u09b6','\u015b'),('\u09b7','\u1e63'),('\u09b8','s'),('\u09b9','h')]
    out.append(bx(22, cy, lw, cbh, 0.6))
    out.append(tx(22+lw//2, cy+cbh//2+3, 'other', 'middle', 'Lx'))
    for j, (ltr, rom) in enumerate(other):
        x = 22 + lw + j*cw7
        out.append(bx(x, cy, cw7, cbh, 0.6))
        out.append(tx(x+cw7//2, cy+17, ltr, 'middle', 'Lb'))
        out.append(tx(x+cw7//2, cy+26, rom, 'middle', 'Lx'))
    cy += cbh  # cy = 263 + 6*28 = 431
    out.append(hl(cy, 0.5))

    # Numerals
    cy += 6
    out.append(sh(cy, "BENGALI NUMERALS  \u00b7  \u09ac\u09be\u0982\u09b2\u09be \u09b8\u0982\u0996\u09cd\u09af\u09be"))
    cy += 4
    out.append(hl(cy))
    cy += 6

    nums = [('\u09e6','0'),('\u09e7','1'),('\u09e8','2'),('\u09e9','3'),('\u09ea','4'),
            ('\u09eb','5'),('\u09ec','6'),('\u09ed','7'),('\u09ee','8'),('\u09ef','9')]
    nbw, nbh = 43, 28
    for i, (bn, ar) in enumerate(nums):
        x = 22 + i*nbw + 2
        out.append(bx(x, cy, nbw, nbh))
        out.append(tx(x+nbw//2, cy+16, bn, 'middle', 'Lb'))
        out.append(tx(x+nbw//2, cy+26, ar, 'middle', 'Lx'))
    cy += nbh + 4
    out.append(hl(cy, 0.5))

    # Conjuncts
    cy += 6
    out.append(sh(cy, "CONJUNCT CONSONANTS  \u00b7  \u09af\u09c1\u0995\u09cd\u09a4\u09ac\u09cd\u09af\u099e\u09cd\u099c\u09a8  \u00b7  JOINED CLUSTERS"))
    cy += 4
    out.append(hl(cy))
    cy += 7
    out.append(tx(240, cy, "hasanta \u09cd (U+09CD) joins consonants \u00b7 removes inherent vowel \u00b7 creates ligature clusters of up to 4"))
    cy += 9

    conj = [('\u0995\u09cd\u09b7','k+\u1e63','ksha'),('\u09b7\u09cd\u099f','\u1e63+\u1e6d','sh\u1e6da'),
            ('\u09a8\u09cd\u09a4','n+t','nta'),('\u09a4\u09cd\u09b0','t+r','tra'),
            ('\u09aa\u09cd\u09b0','p+r','pra'),('\u09b8\u09cd\u09a5','s+th','stha')]
    cwb, cwh = 72, 33
    for i, (frm, comp, rom) in enumerate(conj):
        x = 22 + i*cwb
        out.append(bx(x, cy, cwb, cwh))
        out.append(tx(x+cwb//2, cy+16, frm, 'middle', 'Lb'))
        out.append(tx(x+cwb//2, cy+25, comp, 'middle', 'Lx'))
        out.append(tx(x+cwb//2, cy+32, rom, 'middle', 'Lx'))
    cy += cwh + 5
    out.append(tx(240, cy,
                  "\u09dc /\u1e5d/ retroflex flap  \u00b7  \u09dd /\u1e5dh/  \u00b7  \u09df /\u1e8f/  "
                  "\u00b7  \u09ce final /t/  \u00b7  \u0982 /\u014b/ anusvara  \u00b7  \u0983 visarga  \u00b7  \u0981 chandrabindu (nasal)"))

    out.append(svg_close())
    return '\n'.join(out)


# ═══════════════════════════════════════════════════════════════
# PLATE 16B  ·  BENGALI  ·  PHONOLOGY
# ═══════════════════════════════════════════════════════════════
def build_16b():
    out = [svg_open(),
           title_block("PLATE 16B  \u00b7  BENGALI  \u00b7  PHONOLOGY",
                       "7 oral vowels \u00b7 4-way stop contrast \u00b7 aspiration \u00b7 retroflex series \u00b7 no vowel length \u00b7 initial stress")]

    out.append(sh(67, "BENGALI  \u00b7  SOUNDS THAT SHAPED A CIVILIZATION"))
    out.append(hl(71))
    out.append(tx(240,  79, "Bengali has 7 phonemic oral vowels and ~29 consonants  \u00b7  read left to right"))
    out.append(tx(240,  88, "key feature: 4-way stop contrast \u2014 voiceless/voiced \u00d7 unaspirated/aspirated \u2014 rare among world languages"))
    out.append(tx(240,  97, "retroflex consonants: tongue tip curled back to hard palate  \u00b7  5 retroflex sounds vs 5 dental sounds"))
    out.append(tx(240, 106, "no phonemic tone  \u00b7  primary stress always on first syllable  \u00b7  trochaic rhythm"))
    out.append(hl(110, 0.5))

    # Vowels
    out.append(sh(117, "VOWEL SYSTEM  \u00b7  7 ORAL VOWELS  +  2 DIPHTHONGS"))
    out.append(hl(121))
    out.append(tx(240, 129, "vowel length NOT phonemic  \u00b7  \u0987/\u0988 = same /i/  \u00b7  \u0989/\u098a = same /u/  \u00b7  distinction is spelling-only (Sanskrit heritage)"))

    vowel_ph = [
        ('\u0985','/\u0254/','mid-back\nunrounded'),
        ('\u0986','/a/','open\nfront'),
        ('\u0987/\u0988','/i/','close\nfront'),
        ('\u0989/\u098a','/u/','close\nback'),
        ('\u098f','/e/','close-mid\nfront'),
        ('\u098f','/\u025b/','open-mid\n(before nasal)'),
        ('\u0993','/o/','close-mid\nback'),
        ('\u0990','/oi\u032f/','diphthong'),
        ('\u0994','/ou\u032f/','diphthong'),
    ]
    pw, ph_v = 48, 44
    for i, (ltr, ipa, desc) in enumerate(vowel_ph):
        x = 24 + i*pw
        out.append(bx(x, 134, pw, ph_v))
        out.append(tx(x+pw//2, 134+16, ltr, 'middle', 'Lb'))
        out.append(tx(x+pw//2, 134+27, ipa, 'middle', 'Lx'))
        for k, dl in enumerate(desc.split('\n')):
            out.append(tx(x+pw//2, 134+35+k*8, dl, 'middle', 'Lx'))
    out.append(tx(240, 184, "Note: /\u025b/ and /e/ are allophones in complementary distribution  \u00b7  \u0985 (inherent /\u0254/) is the most common vowel"))
    out.append(hl(189, 0.5))

    # 4-way contrast
    out.append(sh(195, "FOUR-WAY STOP CONTRAST  \u00b7  THE DEFINING FEATURE OF INDO-ARYAN"))
    out.append(hl(199))
    out.append(tx(240, 206, "Bengali distinguishes FOUR types of stop at each place of articulation \u2014 this is extremely rare globally"))
    out.append(tx(240, 214, "voiceless unaspirated  \u00b7  voiceless aspirated  \u00b7  voiced unaspirated  \u00b7  voiced aspirated"))

    demo = [
        ('\u0995','/k/','voiceless\nunasp.'),
        ('\u0996','/k\u02b0/','voiceless\nasp.'),
        ('\u0997','/\u0261/','voiced\nunasp.'),
        ('\u0998','/\u0261\u02b1/','voiced\nasp.'),
    ]
    dw, dh, dy2 = 101, 48, 220
    for i, (ltr, ipa, desc) in enumerate(demo):
        x = 22 + i*(dw+2)
        out.append(bx(x, dy2, dw, dh, 1.0))
        out.append(tx(x+dw//2, dy2+18, ltr, 'middle', 'Lb'))
        out.append(tx(x+dw//2, dy2+29, ipa, 'middle', 'Ls'))
        for k, dl in enumerate(desc.split('\n')):
            out.append(tx(x+dw//2, dy2+37+k*8, dl, 'middle', 'Lx'))
    out.append(tx(240, 274, "same 4-way pattern at 5 places of articulation: velar \u00b7 palatal \u00b7 retroflex \u00b7 dental \u00b7 labial = 20 stops total"))
    out.append(hl(279, 0.5))

    # Full stop grid
    out.append(sh(285, "FULL STOP GRID  \u00b7  5 PLACES \u00d7 5 MANNER ROWS"))
    out.append(hl(289))

    col_labels = ['VELAR','PALATAL','RETROFLEX','DENTAL','LABIAL']
    row_labels = ['vl. unasp.','vl. asp.','vd. unasp.','vd. asp.','nasal']
    stops = [
        ['\u0995 /k/','\u099a /t\u0283/','\u099f /\u0288/','\u09a4 /t\u032a/','\u09aa /p/'],
        ['\u0996 /k\u02b0/','\u099b /t\u0283\u02b0/','\u09a0 /\u0288\u02b0/','\u09a5 /t\u032a\u02b0/','\u09ab /p\u02b0/'],
        ['\u0997 /\u0261/','\u099c /d\u0292/','\u09a1 /\u0256/','\u09a6 /d\u032a/','\u09ac /b/'],
        ['\u0998 /\u0261\u02b1/','\u099d /d\u0292\u02b1/','\u09a2 /\u0256\u02b1/','\u09a7 /d\u032a\u02b1/','\u09ad /b\u02b1/'],
        ['\u0999 /\u014b/','\u099e /n/','\u09a3 /n/','\u09a8 /n/','\u09ae /m/'],
    ]
    rlw, cgw, rgh = 42, 83, 18
    gy = 294
    out.append(bx(22, gy, rlw, rgh, 0.6))
    for ci, cl in enumerate(col_labels):
        out.append(bx(22+rlw+ci*cgw, gy, cgw, rgh, 0.6))
        out.append(tx(22+rlw+ci*cgw+cgw//2, gy+12, cl, 'middle', 'Lx'))
    gy += rgh
    for rl, row in zip(row_labels, stops):
        out.append(bx(22, gy, rlw, rgh, 0.6))
        out.append(tx(22+rlw//2, gy+12, rl, 'middle', 'Lx'))
        for ci, cell in enumerate(row):
            out.append(bx(22+rlw+ci*cgw, gy, cgw, rgh, 0.6))
            out.append(tx(22+rlw+ci*cgw+cgw//2, gy+12, cell, 'middle', 'Lx'))
        gy += rgh
    # gy = 294 + 6*18 = 402
    out.append(hl(gy, 0.5))

    # Retroflex vs dental
    gy += 6
    out.append(sh(gy, "RETROFLEX VS DENTAL  \u00b7  TONGUE POSITION CHANGES MEANING"))
    gy += 4
    out.append(hl(gy))
    gy += 7
    out.append(tx(240, gy, "retroflex: tongue tip curled back to hard palate  \u00b7  dental: tongue tip at upper teeth"))
    gy += 9

    pairs = [
        ('\u099f /\u1e6d/\nretroflex stop','\u09a4 /t/\ndental stop'),
        ('\u09a1 /\u1e0d/\nretroflex D','\u09a6 /d/\ndental d'),
        ('\u09a3 /n/\nretrofl. nasal','\u09a8 /n/\ndental nasal'),
        ('\u09dc /\u1e5d/\nretrofl. flap','\u09b0 /r/\ndental trill'),
    ]
    pw2, ph2 = 108, 42
    for i, (left, right) in enumerate(pairs):
        x = 22 + i*(pw2+1)
        out.append(bx(x, gy, pw2, ph2, 0.8))
        ml = x + pw2//4
        mr = x + 3*pw2//4
        out.append(f'<line x1="{x+pw2//2}" y1="{gy}" x2="{x+pw2//2}" y2="{gy+ph2}" stroke="#000" stroke-width="0.4"/>')
        for k, ll in enumerate(left.split('\n')):
            out.append(tx(ml, gy+13+k*10, ll, 'middle', 'Lx'))
        for k, rl in enumerate(right.split('\n')):
            out.append(tx(mr, gy+13+k*10, rl, 'middle', 'Lx'))
    gy += ph2 + 4
    out.append(hl(gy, 0.5))

    # Sibilant merger + stress
    gy += 6
    out.append(sh(gy, "SIBILANT MERGER  \u00b7  AND  \u00b7  STRESS"))
    gy += 4
    out.append(hl(gy))
    gy += 7
    out.append(tx(240, gy, "\u09b6 \u09b7 \u09b8 \u2014 three sibilant letters all merge to /\u0283/ in modern spoken Bengali  \u00b7  distinction is spelling-only"))
    gy += 8
    out.append(tx(240, gy, "chandrabindu \u0981 marks nasalization of a vowel  \u00b7  nasalized vowels are phonemic: \u0993 /o/ vs \u0993\u0981 /\u00f5/"))
    gy += 8
    out.append(tx(240, gy, "primary stress always on the FIRST syllable  \u00b7  \u09ac\u09be\u0982\u09b2\u09be = BANG-la  \u00b7  \u09ae\u09be\u09a8\u09c1\u09b7 = MA-nush  \u00b7  \u09ad\u09ac\u09bf\u09b7\u09cd\u09af\u09ce = BHO-bi-shot"))

    out.append(svg_close())
    return '\n'.join(out)


# ═══════════════════════════════════════════════════════════════
# PLATE 16C  ·  BENGALI  ·  GRAMMAR AND VOCABULARY
# ═══════════════════════════════════════════════════════════════
def build_16c():
    out = [svg_open(),
           title_block("PLATE 16C  \u00b7  BENGALI  \u00b7  GRAMMAR AND VOCABULARY",
                       "SOV order \u00b7 verb-final \u00b7 postpositions \u00b7 honorific levels \u00b7 case endings \u00b7 30 core words")]

    out.append(sh(67, "BENGALI GRAMMAR  \u00b7  SOV  \u00b7  VERB COMES LAST"))
    out.append(hl(71))
    out.append(tx(240,  79, "Bengali is Subject-Object-Verb  \u00b7  the verb always ends the clause"))
    out.append(tx(240,  88, "agglutinative: meaning built by chaining suffixes to roots  \u00b7  highly inflected verbs"))
    out.append(tx(240,  97, "no grammatical gender for verbs  \u00b7  postpositions (not prepositions)  \u00b7  verb encodes person and honor"))
    out.append(tx(240, 106, "determiners -\u099f\u09be/-\u099f\u09bf (singular 'the') and -\u0997\u09c1\u09b2\u09cb (plural) follow the noun"))
    out.append(hl(110, 0.5))

    # SOV diagram
    out.append(sh(117, "WORD ORDER  \u00b7  SUBJECT \u2192 OBJECT \u2192 VERB"))
    out.append(hl(121))
    bxw, bxh = 130, 22
    out.append(bx(22,  126, bxw, bxh, 1.0))
    out.append(tx(87,  137, "SUBJECT  \u00b7  \u0995\u09b0\u09cd\u09a4\u09be", 'middle', 'Ls'))
    out.append(f'<line x1="{22+bxw}" y1="137" x2="{22+bxw+18}" y2="137" stroke="#000" stroke-width="0.7"/>')
    out.append(f'<polygon points="{22+bxw+18},135 {22+bxw+23},137 {22+bxw+18},139" fill="#000"/>')
    out.append(bx(175, 126, bxw, bxh, 1.0))
    out.append(tx(240, 137, "OBJECT  \u00b7  \u0995\u09b0\u09cd\u09ae", 'middle', 'Ls'))
    out.append(f'<line x1="{175+bxw}" y1="137" x2="{175+bxw+18}" y2="137" stroke="#000" stroke-width="0.7"/>')
    out.append(f'<polygon points="{175+bxw+18},135 {175+bxw+23},137 {175+bxw+18},139" fill="#000"/>')
    out.append(bx(328, 126, 110, bxh, 1.0))
    out.append(tx(383, 137, "VERB  \u00b7  \u0995\u09cd\u09b0\u09bf\u09af\u09bc\u09be", 'middle', 'Ls'))
    out.append(tx(240, 158, "\u0986\u09ae\u09bf \u09ad\u09be\u09a4 \u0996\u09be\u0987  \u00b7  ami bhat khai  \u00b7  I rice eat  =  I eat rice", 'middle', 'Lbm'))
    out.append(tx(240, 169, "\u09b8\u09c7 \u09ac\u09be\u09dc\u09bf \u09af\u09be\u09af\u09bc  \u00b7  she bari jay  \u00b7  s/he house goes  =  s/he goes home", 'middle', 'Lx'))
    out.append(hl(175, 0.5))

    # Verb morphology
    out.append(sh(181, "VERB MORPHOLOGY  \u00b7  ROOT + ASPECT + TENSE + PERSON"))
    out.append(hl(185))
    out.append(tx(240, 192, "template: VERB ROOT  +  aspect marker  +  tense marker  +  person/honor suffix"))
    out.append(tx(240, 200, "aspects: simple (no mark) \u00b7 continuous -\u099a\u09cd\u099b/-\u099a\u09cd\u099b\u09bf \u00b7 perfect -\u09af\u09bc\u09c7\u099b/-\u09af\u09bc\u09c7\u099b\u09bf"))
    out.append(tx(22,  207, "\u0996\u09be\u0993\u09af\u09bc\u09be (kha-oẏa) = to eat  \u2014  1st person forms:", 'start', 'Lbm'))

    verb_rows = [
        ("simple pres.",  "\u0996\u09be\u0987",           "khai",           "I eat"),
        ("continuous",    "\u0996\u09be\u099a\u09cd\u099b\u09bf", "khacchi",  "I am eating"),
        ("simple past",   "\u0996\u09c7\u09b2\u09be\u09ae",  "khelam",        "I ate"),
        ("perfect",       "\u0996\u09c7\u09af\u09bc\u09c7\u099b\u09bf", "kheyechi", "I have eaten"),
        ("future",        "\u0996\u09be\u09ac",            "khabo",          "I will eat"),
    ]
    vcols = [(22,80),(102,80),(182,90),(272,186)]  # (x, w)
    vhdr  = ['TENSE/ASPECT','BENGALI','ROMAN.','MEANING']
    vrh   = 16
    vy    = 214
    for (cx, cw), hdr in zip(vcols, vhdr):
        out.append(bx(cx, vy, cw, vrh, 0.6))
        out.append(tx(cx+cw//2, vy+11, hdr, 'middle', 'Lx'))
    vy += vrh
    for tense, ben, rom, mean in verb_rows:
        for (cx, cw), cell in zip(vcols, [tense, ben, rom, mean]):
            out.append(bx(cx, vy, cw, vrh, 0.5))
            out.append(tx(cx+cw//2, vy+11, cell, 'middle', 'Lx'))
        vy += vrh
    # vy = 214 + 6*16 = 310
    out.append(hl(vy, 0.5))

    # Honorifics
    vy += 6
    out.append(sh(vy, "HONORIFIC LEVELS  \u00b7  5 FORMS  \u00b7  VERB CONJUGATION CHANGES WITH EACH"))
    vy += 4
    out.append(hl(vy))
    vy += 7
    out.append(tx(240, vy, "Bengali has 5 distinct levels of address  \u00b7  each changes the verb ending  \u00b7  using wrong level is a social error"))
    vy += 8

    hon_rows = [
        ('\u09a4\u09c1\u0987 tui',    '2nd intimate',  '\u0996\u09be\u09b8 khas',    '\u0997\u09c7\u09b2\u09bf geli'),
        ('\u09a4\u09c1\u09ae\u09bf tumi', '2nd familiar',  '\u0996\u09be\u0993 khao',   '\u0997\u09c7\u09b2\u09c7 gele'),
        ('\u0986\u09aa\u09a8\u09bf apni', '2nd formal',    '\u0996\u09be\u09a8 khan',   '\u0997\u09c7\u09b2\u09c7\u09a8 gelen'),
        ('\u09b8\u09c7/\u0993 she/o',   '3rd familiar',  '\u0996\u09be\u09af\u09bc khay',  '\u0997\u09c7\u09b2 gelo'),
        ('\u09a4\u09bf\u09a8\u09bf tini', '3rd formal',    '\u0996\u09be\u09a8 khan',   '\u0997\u09c7\u09b2\u09c7\u09a8 gelen'),
    ]
    hcols = [(22,72),(94,84),(178,84),(262,84),(346,112)]
    hhdrs = ['PRONOUN','REGISTER','eat (pres.)','go (past)','ENGLISH']
    hrh   = 16
    for (cx, cw), hdr in zip(hcols, hhdrs):
        out.append(bx(cx, vy, cw, hrh, 0.6))
        out.append(tx(cx+cw//2, vy+11, hdr, 'middle', 'Lx'))
    vy += hrh
    for row in hon_rows:
        for (cx, cw), cell in zip(hcols, row):
            out.append(bx(cx, vy, cw, hrh, 0.5))
            out.append(tx(cx+cw//2, vy+11, cell, 'middle', 'Lx'))
        vy += hrh
    # vy = (start_of_table) + 6*16 = 332 + 96 = 428
    out.append(hl(vy, 0.5))
    vy += 6

    # Case endings
    out.append(sh(vy, "CASE ENDINGS  \u00b7  POSTPOSITIONS  \u00b7  NO PREPOSITIONS IN BENGALI"))
    vy += 4
    out.append(hl(vy))
    vy += 7
    out.append(tx(240, vy,
                  "\u09ac\u09be\u09dc\u09bf-\u09b0 (bari-r) = of the house  \u00b7  "
                  "\u0986\u09ae\u09be-\u0995\u09c7 (ama-ke) = to me  \u00b7  "
                  "\u0998\u09b0-\u09c7 (ghor-e) = in the room  \u00b7  "
                  "\u0995\u09b2\u09ae-\u09c7 (kolom-e) = by pen"))
    vy += 8
    out.append(tx(240, vy,
                  "genitive -\u098f\u09b0 (of/belonging to)  \u00b7  objective -\u0995\u09c7/-\u09b0\u09c7 (to/for)  \u00b7  "
                  "locative -\u09a4\u09c7/-\u098f (in/at)  \u00b7  postpositions: \u09a6\u09cd\u09ac\u09be\u09b0\u09be (by), \u099c\u09a8\u09cd\u09af (for), \u09b8\u09be\u09a5\u09c7 (with)"))
    vy += 10
    out.append(hl(vy, 0.5))
    vy += 6

    # Core vocabulary
    out.append(sh(vy, "CORE VOCABULARY  \u00b7  30 ESSENTIAL WORDS"))
    vy += 4
    out.append(hl(vy))
    vy += 6

    vocab = [
        ("\u0986\u09ae\u09bf ami","I"),
        ("\u09a4\u09c1\u09ae\u09bf tumi","you (fam.)"),
        ("\u09b8\u09c7 she","he/she/it"),
        ("\u0986\u09ae\u09b0\u09be amra","we"),
        ("\u098f\u099f\u09be eta","this"),
        ("\u0993\u099f\u09be ota","that"),
        ("\u09b9\u09cd\u09af\u09be\u0981 hya","yes"),
        ("\u09a8\u09be na","no"),
        ("\u09ae\u09be\u09a8\u09c1\u09b7 manush","person"),
        ("\u099c\u09b2 jol","water"),
        ("\u0996\u09be\u09ac\u09be\u09b0 khabar","food"),
        ("\u09ae\u09be\u099f\u09bf mati","earth/soil"),
        ("\u0986\u0995\u09be\u09b6 akash","sky"),
        ("\u09b8\u09c2\u09b0\u09cd\u09af surjo","sun"),
        ("\u0986\u09b2\u09cb alo","light"),
        ("\u0986\u0997\u09c1\u09a8 agun","fire"),
        ("\u09ac\u09be\u09dc\u09bf bari","house"),
        ("\u09a6\u09bf\u09a8 din","day"),
        ("\u09b0\u09be\u09a4 rat","night"),
        ("\u09b8\u09ae\u09af\u09bc shomoy","time"),
        ("\u09ad\u09be\u09b7\u09be bhasha","language"),
        ("\u09b2\u09c7\u0996\u09be lekha","writing"),
        ("\u09ac\u09b2\u09be bola","speak"),
        ("\u09b6\u09cb\u09a8\u09be shona","hear"),
        ("\u09a6\u09c7\u0996\u09be dekha","see"),
        ("\u09ad\u09be\u09b2\u09cb bhalo","good"),
        ("\u0996\u09be\u09b0\u09be\u09aa kharap","bad"),
        ("\u09ac\u09dc boro","big"),
        ("\u099b\u09cb\u099f chhoto","small"),
        ("\u09ad\u09ac\u09bf\u09b7\u09cd\u09af\u09ce bhobishyot","future"),
    ]
    vcw = 144
    vcx = [22, 168, 314]
    vrh2 = 13
    for i, (word, meaning) in enumerate(vocab):
        col = i % 3
        row = i // 3
        cx = vcx[col]
        vy2 = vy + row*vrh2
        out.append(bx(cx, vy2, vcw, vrh2, 0.4))
        out.append(tx(cx+vcw//2, vy2+9, f"{word}  \u00b7  {meaning}", 'middle', 'Lx'))

    out.append(svg_close())
    return '\n'.join(out)


# ═══════════════════════════════════════════════════════════════
# PLATE 16D  ·  BENGALI  ·  RUNNING TEXT
# ═══════════════════════════════════════════════════════════════
def build_16d():
    out = [svg_open(),
           title_block("PLATE 16D  \u00b7  BENGALI  \u00b7  RUNNING TEXT",
                       "Tagore \u00b7 Gitanjali \u00b7 Amar Sonar Bangla \u00b7 proverb \u00b7 bridge phrase  \u00b7  read left to right")]

    out.append(tx(240, 64, "read left to right  \u00b7  Bengali above  \u00b7  transliteration middle  \u00b7  translation below"))
    out.append(hl(68, 0.4))

    def passage(y, section_title, bengali_text, roman, translation, note):
        result = []
        result.append(sh(y, section_title))
        y += 5
        result.append(hl(y))
        y += 3
        box_y = y
        result.append(bx(22, box_y, 436, 42, 0.9))
        result.append(tx(240, box_y+13, bengali_text, 'middle', 'Lbm'))
        result.append(tx(240, box_y+25, roman,        'middle', 'Lx'))
        result.append(tx(240, box_y+35, translation,  'middle', 'Lx'))
        note_y = box_y + 42 + 8
        result.append(tx(22, note_y, note, 'start', 'Lx'))
        line_y = note_y + 8
        result.append(hl(line_y, 0.4))
        return '\n'.join(result), line_y + 6

    y = 76
    p, y = passage(y,
        "GITANJALI \u00b7 SONG 1 \u00b7 RABINDRANATH TAGORE \u00b7 1910",
        "\u0986\u09ae\u09be\u09b0\u09c7 \u09a4\u09c1\u09ae\u09bf \u0985\u09b6\u09c7\u09b7 \u0995\u09b0\u09c7\u099b, \u098f\u09ae\u09a8\u09bf \u09b2\u09c0\u09b2\u09be \u09a4\u09ac\u0964",
        "amare tumi oshesh korechho, emni lila tabo.",
        "You have made me endless \u2014 such is your divine delight.",
        "Note: amare=me \u00b7 oshesh=endless \u00b7 korechho=have made \u00b7 lila=divine play \u00b7 tabo=your  \u00b7  Nobel Prize Literature 1913"
    )
    out.append(p)

    p, y = passage(y,
        "WHERE THE MIND IS WITHOUT FEAR \u00b7 GITANJALI 35 \u00b7 TAGORE",
        "\u099a\u09bf\u09a4\u09cd\u09a4 \u09af\u09c7\u09a5\u09be \u09ad\u09af\u09bc\u09b6\u09c2\u09a8\u09cd\u09af \u0989\u099a\u09cd\u099a \u09af\u09c7\u09a5\u09be \u09b6\u09bf\u09b0",
        "chitta jetha bhoyshu\u00f4nyô, uccho jetha shir",
        "Where the mind is without fear and the head is held high",
        "Note: chitta=mind/heart \u00b7 jetha=where \u00b7 bhoyshunyô=fear-empty \u00b7 uccho=high \u00b7 shir=head"
    )
    out.append(p)

    p, y = passage(y,
        "AMAR SONAR BANGLA \u00b7 NATIONAL ANTHEM OF BANGLADESH \u00b7 TAGORE 1906",
        "\u0986\u09ae\u09be\u09b0 \u09b8\u09cb\u09a8\u09be\u09b0 \u09ac\u09be\u0982\u09b2\u09be, \u0986\u09ae\u09bf \u09a4\u09cb\u09ae\u09be\u09af\u09bc \u09ad\u09be\u09b2\u09cb\u09ac\u09be\u09b8\u09bf\u0964",
        "amar shonar bangla, ami tomay bhalobashi.",
        "My golden Bengal, I love you.",
        "Note: amar=my \u00b7 shonar=golden \u00b7 bangla=Bengal \u00b7 ami=I \u00b7 tomay=you \u00b7 bhalobashi=love  \u00b7  also India's national song"
    )
    out.append(p)

    p, y = passage(y,
        "BENGALI PROVERB  \u00b7  ON CARE AND REWARD",
        "\u09af\u09a4\u09cd\u09a8 \u0995\u09b0\u09b2\u09c7 \u09b0\u09a4\u09cd\u09a8 \u09ae\u09c7\u09b2\u09c7\u0964",
        "jotno korle rotno mele.",
        "With care, precious things are found.",
        "Note: jotno=care/attention \u00b7 korle=if one does \u00b7 rotno=gem/jewel \u00b7 mele=is obtained  \u00b7  proverb on the reward of diligence"
    )
    out.append(p)

    # Bridge phrase — two lines of Bengali
    out.append(sh(y, "THE BRIDGE PHRASE  \u00b7  IN BENGALI"))
    y += 5
    out.append(hl(y))
    y += 3
    box_y = y
    out.append(bx(22, box_y, 436, 55, 0.9))
    out.append(tx(240, box_y+13,
                  "\u098f\u099f\u09bf \u09a4\u09cb\u09ae\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09a4\u09c8\u09b0\u09bf \u0995\u09b0\u09be \u09b9\u09af\u09bc\u09c7\u099b\u09c7 \u2014 \u09ac\u09bf\u09a8\u09be\u09ae\u09c2\u09b2\u09cd\u09af\u09c7 \u2014",
                  'middle', 'Lbm'))
    out.append(tx(240, box_y+26,
                  "\u09a4\u09be\u09a6\u09c7\u09b0 \u09a6\u09cd\u09ac\u09be\u09b0\u09be \u09af\u09be\u09b0\u09be \u09ad\u09ac\u09bf\u09b7\u09cd\u09af\u09ce\u0995\u09c7 \u09ae\u09a8\u09c7 \u09b0\u09c7\u0996\u09c7\u099b\u09bf\u09b2\u0964",
                  'middle', 'Lbm'))
    out.append(tx(240, box_y+38,
                  "eti tomar jonno toiri kora hoyeche \u2014 binamulle \u2014 tader dwara jara bhobishotkke mone rekhechhilo.",
                  'middle', 'Lx'))
    out.append(tx(240, box_y+48,
                  "This was made for you \u2014 freely \u2014 by those who kept the future in their hearts.",
                  'middle', 'Lx'))
    y = box_y + 55 + 6
    out.append(tx(22, y,
                  "Note: \u09ad\u09ac\u09bf\u09b7\u09cd\u09af\u09ce (bhobishyot) = future / what is yet to become  \u00b7  \u09ae\u09a8\u09c7 \u09b0\u09be\u0996\u09be (mone rakha) = to keep in mind/heart",
                  'start', 'Lx'))
    y += 8
    out.append(tx(22, y,
                  "Bengali expresses \u2018remembered forward\u2019 as \u09ae\u09a8\u09c7 \u09b0\u09c7\u0996\u09c7\u099b\u09bf\u09b2 \u2014 had kept in the heart \u2014 the future cherished from the present.",
                  'start', 'Lx'))

    out.append(svg_close())
    return '\n'.join(out)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
def main():
    plates = [
        ('plate16a_bengali_script.svg',    build_16a()),
        ('plate16b_bengali_phonology.svg',  build_16b()),
        ('plate16c_bengali_grammar.svg',    build_16c()),
        ('plate16d_bengali_text.svg',       build_16d()),
    ]
    for fname, content in plates:
        path = os.path.join(BASE, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')
    print('Done. Bengali series 16A\u201316D complete.')

if __name__ == '__main__':
    main()
