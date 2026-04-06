"""
build_egyptian_series.py
Ancient Egyptian (Middle Egyptian, c. 2000 BCE) — plates 61A–61D
Run from repo root:  python plates/languages/egyptian/build_egyptian_series.py
"""

import os, math

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = BASE

# ── Transliteration characters (BMP) ─────────────────────────────────────────
ALEPH = '\ua723'   # ꜣ  U+A723
AYIN  = '\ua725'   # ꜥ  U+A725
HH    = '\u1e25'   # ḥ  dotted-h
KH    = '\u1e2b'   # ḫ  h-breve-below
EZH   = '\u1e96'   # ẖ  h-line-below
SH    = '\u0161'   # š
TJ    = '\u1e6f'   # ṯ
DJ    = '\u1e0f'   # ḏ
IM    = '\u012b'   # ī  long i
AE    = '\u00e6'   # æ  used for æ
MDOT  = '\u1e43'   # ṃ

# ── Hieroglyph Unicode codepoints (SMP — need chr()) ─────────────────────────
# Verified via Python unicodedata.lookup()
G1  = chr(0x1313F)   # vulture       ꜣ
M17 = chr(0x131CB)   # reed          i
G43 = chr(0x13171)   # quail chick   w
D36 = chr(0x1309D)   # forearm       ꜥ
D58 = chr(0x130C0)   # lower leg     b
Q3  = chr(0x132AA)   # mat/stool     p
I9  = chr(0x13191)   # horned viper  f
G17 = chr(0x13153)   # owl           m
N35 = chr(0x13216)   # water         n
D21 = chr(0x1308B)   # mouth         r
O4  = chr(0x13254)   # shelter       h
V28 = chr(0x1339B)   # wick          ḥ
Aa1 = chr(0x1340D)   # placenta      ḫ
F32 = chr(0x13121)   # animal belly  ẖ
S29 = chr(0x132F4)   # folded cloth  s
O34 = chr(0x13283)   # door bolt     z
N37 = chr(0x13219)   # pool          š
N29 = chr(0x1320E)   # hill slope    q
V31 = chr(0x133A1)   # basket        k
W11 = chr(0x133BC)   # jar stand     g
X1  = chr(0x133CF)   # bread loaf    t
V13 = chr(0x1337F)   # rope          ṯ
D46 = chr(0x130A7)   # hand          d
I10 = chr(0x13193)   # cobra         ḏ

# 24 uniliteral signs: (hieroglyph_char, Gardiner, transliteration, English_name)
SIGNS_24 = [
    (G1,  'G1',  ALEPH, 'vulture'),
    (M17, 'M17', 'i',   'reed'),
    (G43, 'G43', 'w',   'quail chick'),
    (D36, 'D36', AYIN,  'forearm'),
    (D58, 'D58', 'b',   'lower leg'),
    (Q3,  'Q3',  'p',   'mat/stool'),
    (I9,  'I9',  'f',   'horned viper'),
    (G17, 'G17', 'm',   'owl'),
    (N35, 'N35', 'n',   'water'),
    (D21, 'D21', 'r',   'mouth'),
    (O4,  'O4',  'h',   'reed shelter'),
    (V28, 'V28', HH,    'twisted wick'),
    (Aa1, 'Aa1', KH,    'placenta'),
    (F32, 'F32', EZH,   'animal belly'),
    (S29, 'S29', 's',   'folded cloth'),
    (O34, 'O34', 'z',   'door bolt'),
    (N37, 'N37', SH,    'basin/pool'),
    (N29, 'N29', 'q',   'hill/slope'),
    (V31, 'V31', 'k',   'basket + handle'),
    (W11, 'W11', 'g',   'jar stand'),
    (X1,  'X1',  't',   'bread loaf'),
    (V13, 'V13', TJ,    'tethering rope'),
    (D46, 'D46', 'd',   'hand'),
    (I10, 'I10', DJ,    'cobra'),
]

# ── SVG helpers ───────────────────────────────────────────────────────────────
STYLE = """<style>
  .T  { font: bold 12px/1 Georgia,serif; letter-spacing: 2px; }
  .S  { font: 7px/1 Georgia,serif; letter-spacing: 1.5px; }
  .H  { font: bold 6.5px/1 Georgia,serif; letter-spacing: 2.5px; }
  .L  { font: 7px/1.35 Georgia,serif; }
  .Ls { font: 6px/1.35 Georgia,serif; }
  .Lx { font: 5.5px/1.35 Georgia,serif; }
  .Le { font: 18px/1 "Noto Sans Egyptian Hieroglyphs",serif; }
  .Lm { font: italic 7.5px/1.2 Georgia,serif; }
  .M  { font: 6px/1 Georgia,serif; letter-spacing: 0.5px; }
  .F  { font: italic 7px/1 Georgia,serif; }
  .Fb { font: bold 7.5px/1 Georgia,serif; }
</style>"""

def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def open_svg():
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 480 680" width="480" height="680">\n'
        + STYLE + '\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="#111" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="#111" stroke-width="0.75"/>\n'
    )

def close_svg():
    return '</svg>\n'

def t(x, y, s, a='middle', c='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'

def hr(y, w=0.3):
    return f'<line x1="24" y1="{y}" x2="456" y2="{y}" stroke="#111" stroke-width="{w}"/>\n'

def sh(y, txt):
    return (
        f'<line x1="30" y1="{y}" x2="118" y2="{y}" stroke="#111" stroke-width="0.3"/>\n'
        f'<text x="240" y="{y+4}" text-anchor="middle" class="H">— {esc(txt)} —</text>\n'
        f'<line x1="362" y1="{y}" x2="450" y2="{y}" stroke="#111" stroke-width="0.3"/>\n'
    )

def bx(x, y, w, h, sw=0.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#555" stroke-width="{sw}"/>\n'

def footer(pid):
    DOI = '10.5281/zenodo.19433177'
    return (
        '<line x1="24" y1="607" x2="456" y2="607" stroke="#111" stroke-width="0.3"/>\n'
        f'<text x="240" y="616" text-anchor="middle" class="M">'
        f'{pid}  \u00b7  SERIES 61  \u00b7  ANCIENT EGYPTIAN  \u00b7  '
        f'MIDDLE EGYPTIAN c. 2000 BCE  \u00b7  U+13000\u2013U+13431'
        f'</text>\n'
        '<line x1="24" y1="622" x2="456" y2="622" stroke="#111" stroke-width="0.3"/>\n'
        f'<text x="240" y="631" text-anchor="middle" class="M">'
        f'CC BY-SA 4.0  \u00b7  rememberforward.org  \u00b7  DOI {DOI}'
        f'</text>\n'
        '<line x1="24" y1="638" x2="456" y2="638" stroke="#111" stroke-width="0.5"/>\n'
        '<text x="240" y="649" text-anchor="middle" class="Fb">'
        'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.'
        '</text>\n'
        '<text x="240" y="663" text-anchor="middle" class="F">'
        'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET'
        '</text>\n'
    )

# ── Plate 61A — Script ────────────────────────────────────────────────────────
def build_61a():
    out = open_svg()
    # Title
    out += t(240, 32, 'ANCIENT EGYPTIAN', 'middle', 'T')
    out += t(240, 47, 'SCRIPT \u00b7 MIDDLE EGYPTIAN c. 2000 BCE \u00b7 HIEROGLYPHIC \u00b7 HIERATIC \u00b7 DEMOTIC', 'middle', 'S')
    out += hr(55)

    # Three writing systems
    out += sh(63, 'THE THREE WRITING SYSTEMS')
    cols = [100, 240, 380]
    systems = [
        ('HIEROGLYPHIC', 'Formal / monumental', 'c. 3200 BCE \u2013 400 CE', 'Stone inscriptions, temple', 'walls, coffins, papyrus', '1,000+ signs'),
        ('HIERATIC', 'Cursive reed-pen script', 'c. 2700 BCE \u2013 200 CE', 'Papyrus, ostraca (pottery)', 'Literary, religious, admin', 'Simplified from hieroglyphs'),
        ('DEMOTIC', 'Rapid cursive with ligatures', 'c. 650 BCE \u2013 400 CE', 'Admin, legal, personal use', 'On Rosetta Stone (196 BCE)', 'Highly abbreviated'),
    ]
    for cx, (name, d1, d2, d3, d4, d5) in zip(cols, systems):
        out += t(cx, 75, name, 'middle', 'H')
        for i, line in enumerate([d1, d2, d3, d4, d5]):
            out += t(cx, 85 + i*9, line, 'middle', 'Lx')
    out += hr(136, 0.3)

    # 24 uniliteral signs
    out += sh(143, '24 UNILITERAL CONSONANT SIGNS')
    out += t(240, 153, 'The Egyptian consonantal "alphabet" \u2014 each sign = one consonant sound', 'middle', 'Lx')

    # Grid: 8 columns x 3 rows
    COLS = 8
    cell_w = 54
    cell_h = 48
    x0 = 30
    y0 = 160

    for i, (glyph, gardiner, translit, name) in enumerate(SIGNS_24):
        col = i % COLS
        row = i // COLS
        cx = x0 + col * cell_w + cell_w // 2
        cy = y0 + row * cell_h

        out += bx(x0 + col*cell_w, cy, cell_w, cell_h - 2, 0.4)
        # Hieroglyph character
        out += f'<text x="{cx}" y="{cy+22}" text-anchor="middle" class="Le">{glyph}</text>\n'
        # Gardiner + transliteration
        out += t(cx, cy+33, f'{gardiner}', 'middle', 'Lx')
        out += t(cx, cy+41, translit, 'middle', 'Ls')
        out += t(cx, cy+47, name, 'middle', 'Lx')

    out += hr(310, 0.3)

    # Reading conventions
    out += sh(317, 'READING CONVENTIONS')
    y = 328
    convs = [
        'DIRECTION: Follow where human/animal figures face. Figures face start of text.',
        'Can read left-to-right, right-to-left, or top-to-bottom (in columns).',
        'CARTOUCHE: Oval ring enclosing a royal name \u2014 oval indicates a living king.',
        'DETERMINATIVE: Unpronounced sign that classifies the word (e.g., \u2295 after city names).',
        'LOGOGRAM: Sign read as a whole word \u2014 often has a vertical stroke below.',
        'PHONOGRAM: Sign read for its consonant sounds only (ignoring original meaning).',
    ]
    for line in convs:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += hr(396, 0.3)

    # Font note
    out += sh(403, 'UNICODE & FONT')
    fn_lines = [
        'Hieroglyphic Unicode block: U+13000\u2013U+1342F (1,072 characters)',
        'Font required: Noto Sans Egyptian Hieroglyphs (Google Fonts, free)',
        'All hieroglyphs are in the Supplementary Multilingual Plane (SMP)',
        'Coptic Unicode block (descendant script): U+2C80\u2013U+2CFF',
    ]
    y = 413
    for line in fn_lines:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += hr(448, 0.3)

    # Sign types summary table
    out += sh(455, 'HIEROGLYPH SIGN TYPES')
    types = [
        ('LOGOGRAM', 'Sign = whole word', 'pr', 'house'),
        ('PHONOGRAM', 'Sign = sound(s)', 'm', 'owl = sound /m/'),
        ('BILITERAL', '2-consonant sign', 'mn', 'gaming board'),
        ('TRILITERAL', '3-consonant sign', 'nfr', 'windpipe/heart'),
        ('DETERMINATIVE', 'Unpronounced classifier', '\u2295', 'after city names'),
    ]
    headers = ['TYPE', 'FUNCTION', 'EXAMPLE', 'NOTE']
    xs = [50, 140, 270, 350]
    y = 464
    for hdr, x in zip(headers, xs):
        out += t(x, y, hdr, 'start', 'H')
    out += hr(y + 3, 0.3)
    y += 10
    for typ, func, ex, note in types:
        vals = [typ, func, ex, note]
        for v, x in zip(vals, xs):
            out += t(x, y, v, 'start', 'Lx')
        y += 9

    out += hr(510, 0.3)
    out += t(240, 520, 'HISTORICAL NOTE: Egyptian is the world\'s oldest attested writing system (c. 3200 BCE)', 'middle', 'Lx')
    out += t(240, 530, 'and the direct ancestor of Coptic (3rd\u201317th CE), which preserves the vowel sounds.', 'middle', 'Lx')
    out += t(240, 540, 'Hieroglyphs were deciphered in 1822 by Jean-Fran\u00e7ois Champollion using the Rosetta Stone.', 'middle', 'Lx')
    out += t(240, 550, 'The Rosetta Stone (196 BCE) contains the same decree in hieroglyphic, demotic, and Greek.', 'middle', 'Lx')
    out += t(240, 560, 'See Plate 01 (Rosetta Index) for the symbolic connection to this project\'s design.', 'middle', 'Lx')

    out += footer('PLATE 61A')
    out += close_svg()
    return out

# ── Plate 61B — Phonology ─────────────────────────────────────────────────────
def build_61b():
    out = open_svg()
    out += t(240, 32, 'ANCIENT EGYPTIAN', 'middle', 'T')
    out += t(240, 47, 'PHONOLOGY \u00b7 CONSONANTAL SCRIPT \u00b7 NO VOWELS WRITTEN \u00b7 COPTIC PRESERVES VOWELS', 'middle', 'S')
    out += hr(55)

    # Consonant inventory
    out += sh(63, 'CONSONANT INVENTORY (24 PRIMARY CONSONANTS)')
    headers = ['Sign', 'Translit', 'IPA', 'Type', 'Description']
    xs = [36, 100, 150, 205, 280]
    y = 75
    for h, x in zip(headers, xs):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 10

    consonants = [
        (ALEPH, ALEPH,    '\u0294', 'glottal', 'Glottal stop / laryngeal'),
        ('i/y', 'i / y',  'j',     'approx.', 'Palatal approximant (like English y)'),
        ('w',   'w',       'w',     'approx.', 'Labio-velar approximant'),
        (AYIN,  AYIN,     '\u02bf', 'pharyn.', 'Voiced pharyngeal fricative'),
        ('b',   'b',       'b',     'stop',    'Voiced bilabial stop'),
        ('p',   'p',       'p',     'stop',    'Voiceless bilabial stop'),
        ('f',   'f',       'f',     'fric.',   'Voiceless labiodental fricative'),
        ('m',   'm',       'm',     'nasal',   'Bilabial nasal'),
        ('n',   'n',       'n',     'nasal',   'Dental/alveolar nasal'),
        ('r',   'r',       'r\u0329', 'liquid', 'Rhotacized syllabic / trill'),
        ('h',   'h',       'h',     'fric.',   'Voiceless glottal fricative'),
        (HH,    HH,       '\u0127', 'fric.',   'Voiceless pharyngeal fricative'),
        (KH,    KH,       '\u03c7', 'fric.',   'Voiceless velar fricative (like Scots loch)'),
        (EZH,   EZH,     '\xe7',   'fric.',   'Voiceless palatal fricative'),
        ('z',   'z/s',    's\u02c8', 'fric.', 'Voiceless sibilant (merged with s in later periods)'),
        ('s',   's',       's',     'fric.',   'Voiceless alveolar fricative'),
        (SH,    SH,       '\u0283', 'fric.',   'Voiceless postalveolar fricative (sh)'),
        ('q',   'q',       'q',     'stop',    'Voiceless uvular stop'),
        ('k',   'k',       'k',     'stop',    'Voiceless velar stop'),
        ('g',   'g',       '\u0261', 'stop',  'Voiced velar stop'),
        ('t',   't',       't',     'stop',    'Voiceless dental stop'),
        (TJ,    TJ,       't\u0283','affr.',  'Voiceless palatal affricate'),
        ('d',   'd',       'd',     'stop',    'Voiced dental stop'),
        (DJ,    DJ,       'd\u0292','affr.',  'Voiced palatal affricate'),
    ]
    for sign, tr, ipa, typ, desc in consonants:
        row = [sign, tr, ipa, typ, desc]
        for v, x in zip(row, xs):
            out += t(x, y, v, 'start', 'Lx')
        y += 8

    out += hr(y+2, 0.3)
    y += 8

    # The vowel problem
    out += sh(y, 'THE VOWEL PROBLEM')
    y += 12
    vow_lines = [
        'Egyptian hieroglyphs record CONSONANTS ONLY. Vowels are not written.',
        'Egyptologists conventionally insert the vowel "e" between consonants for pronunciation.',
        'Example: nfr (beautiful) = pronounced approximately "ne-fer".',
        'The word pr (house) might be read "per", sn (brother) = "sen".',
    ]
    for line in vow_lines:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += hr(y+2, 0.3)
    y += 8

    # Coptic as key to vowels
    out += sh(y, 'COPTIC \u2014 THE VOWEL KEY')
    y += 12
    cop_lines = [
        'Coptic (3rd\u201317th CE) is the final stage of the Egyptian language, written in the Greek',
        'alphabet plus 6\u20137 demotic-derived letters. It PRESERVES VOWELS, revealing what the',
        'hieroglyphic consonants actually sounded like.',
        'Three primary vowel qualities: a, i, u (plus schwa \u0259 in unstressed syllables).',
        'Key: Egyptian ꜣ often = Coptic a, Egyptian i = Coptic i, Egyptian w = Coptic u/ou.',
        'Stress falls on the last heavy syllable (closed or with long vowel).',
    ]
    for line in cop_lines:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += hr(y+2, 0.3)
    y += 8

    # Transliteration system table
    out += sh(y, 'TRANSLITERATION SYSTEM (MANUEL DE CODAGE)')
    y += 12
    out += t(240, y, 'Standard Egyptological transliteration symbols with approximate IPA values:', 'middle', 'Lx')
    y += 10

    trow_h = [
        (ALEPH, 'U+A723', '\u0294', 'Glottal stop (laryngeal)'),
        (AYIN,  'U+A725', '\u02bf', 'Voiced pharyngeal fricative'),
        (HH,    'U+1E25', '\u0127', 'Voiceless pharyngeal (h-underdot)'),
        (KH,    'U+1E2B', '\u03c7', 'Voiceless velar fricative (h-breve-below)'),
        (EZH,   'U+1E96', '\xe7',   'Voiceless palatal fricative (h-line-below)'),
        (SH,    'U+0161', '\u0283', 'Postalveolar fricative (s-caron)'),
        (TJ,    'U+1E6F', 't\u0283','Palatal affricate (t-line-below)'),
        (DJ,    'U+1E0F', 'd\u0292','Voiced palatal affricate (d-line-below)'),
    ]
    cols4 = [50, 130, 210, 290]
    hdrs4 = ['Symbol', 'Unicode', 'IPA', 'Description']
    for h, x in zip(hdrs4, cols4):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 10
    for sym, uni, ipa, desc in trow_h:
        for v, x in zip([sym, uni, ipa, desc], cols4):
            out += t(x, y, v, 'start', 'Lx')
        y += 8

    out += hr(y+2, 0.3)
    y += 8

    # Coptic alphabet note
    out += sh(y, 'COPTIC ALPHABET (DESCENDANT OF EGYPTIAN)')
    y += 12
    coptic = '\u2c80\u2c81\u2c82\u2c83\u2c84\u2c85\u2c86\u2c87\u2c88\u2c89\u2c8a\u2c8b\u2c8c\u2c8d\u2c8e\u2c8f\u2c90\u2c91\u2c92\u2c93\u2c94\u2c95\u2c96\u2c97\u2c98\u2c99\u2c9a\u2c9b\u2c9c\u2c9d\u2c9e\u2c9f'
    out += t(240, y, 'Coptic letters: ' + coptic, 'middle', 'L')
    y += 11
    out += t(240, y, '(Greek-alphabet base + Demotic-derived signs for Egyptian sounds without Greek equivalents)', 'middle', 'Lx')
    y += 9
    out += t(240, y, 'Unicode block U+2C80\u2013U+2CFF \u00b7 Font: Noto Sans Coptic', 'middle', 'Lx')

    out += footer('PLATE 61B')
    out += close_svg()
    return out

# ── Plate 61C — Grammar ───────────────────────────────────────────────────────
def build_61c():
    out = open_svg()
    out += t(240, 32, 'ANCIENT EGYPTIAN', 'middle', 'T')
    out += t(240, 47, 'GRAMMAR \u00b7 VSO WORD ORDER \u00b7 SUFFIX CONJUGATION \u00b7 MIDDLE EGYPTIAN', 'middle', 'S')
    out += hr(55)

    # Word order
    out += sh(63, 'WORD ORDER: VERB \u2013 SUBJECT \u2013 OBJECT')
    y = 74
    out += t(36, y, 'Egyptian is VSO: the verb comes first, then subject, then object.', 'start', 'L')
    y += 12
    out += bx(36, y, 404, 32)
    out += t(240, y+12, 'sDm  nTr  s', 'middle', 'Lm')
    out += t(240, y+24, '"hears / god / man"  \u2192  The god hears the man', 'middle', 'Lx')
    y += 40
    out += t(36, y, 'Adverbs and prepositional phrases follow the verb. Negation precedes the verb.', 'start', 'Lx')
    out += hr(y+10, 0.3)
    y += 18

    # Suffix conjugation
    out += sh(y, 'SUFFIX CONJUGATION')
    y += 12
    out += t(36, y, 'Tense/aspect is encoded by suffixes on the verbal root. The key form is sDm.n=f (he heard).', 'start', 'Lx')
    y += 10
    suff_forms = [
        ('sDm.f',    'Imperfective', 'He hears / he habitually hears (present/future)'),
        ('sDm.n.f',  'Perfective',   'He heard (past, completed action — the n-form)'),
        ('sDm.w.f',  'Passive',      'It is heard / he is heard'),
        ('sDm.xr.f', 'Sequential',   'Then he heard (narrative sequence)'),
        ('sDm.kA.f', 'Prospective',  'He will/shall hear'),
    ]
    cols3 = [36, 140, 220]
    hdrs3 = ['Form', 'Aspect', 'Meaning']
    for h, x in zip(hdrs3, cols3):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 9
    for form, asp, meaning in suff_forms:
        for v, x in zip([form, asp, meaning], cols3):
            out += t(x, y, v, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # Pronouns
    out += sh(y, 'SUFFIX PRONOUNS')
    y += 11
    pronouns = [
        ('=i', '1sg', 'I/me'),
        ('=k', '2sg.m', 'you (masc.)'),
        ('=T', '2sg.f', 'you (fem.)'),
        ('=f', '3sg.m', 'he/him'),
        ('=s', '3sg.f', 'she/her'),
        ('=n', '1pl', 'we/us'),
        ('=Tn', '2pl', 'you (pl.)'),
        ('=sn', '3pl', 'they/them'),
    ]
    pcols = [36, 100, 150, 250, 320, 370]
    p2 = pronouns[:4]
    p3 = pronouns[4:]
    for (sf, num, gl), (sf2, num2, gl2) in zip(p2, p3):
        out += t(36,  y, sf,  'start', 'Ls'); out += t(76,  y, num,  'start', 'Lx'); out += t(120, y, gl,  'start', 'Lx')
        out += t(240, y, sf2, 'start', 'Ls'); out += t(280, y, num2, 'start', 'Lx'); out += t(330, y, gl2, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # Nouns
    out += sh(y, 'NOUNS: GENDER, NUMBER, GENITIVE')
    y += 12
    noun_data = [
        ('Masculine', 'No ending', 'pr', 'house'),
        ('Feminine', '-t suffix', 'pr.t', 'house (fem.) / "going out"'),
        ('Dual', '-wy (m.) / -ty (f.)', 'ir.ty', 'the two eyes'),
        ('Plural', '-w (m.) / -wt (f.)', 'Hwt-nTrw', 'temples (lit. god-houses)'),
    ]
    ncols = [36, 130, 230, 300]
    nhdrs = ['Gender/Number', 'Marker', 'Example', 'Gloss']
    for h, x in zip(nhdrs, ncols):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 9
    for row in noun_data:
        for v, x in zip(row, ncols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # Negation
    out += sh(y, 'NEGATION')
    y += 10
    neg_data = [
        ('n sDm.n=f',  'He did not hear',         'Past negation with n + perfective'),
        ('nn sDm=f',   'He does/will not hear',    'Present/future negation'),
        ('tm=f sDm',   'Without his hearing',      'Negative complement infinitive'),
        ('n wn ... m', 'There is no ... in ...',   'Existential negation: n wn + noun + m'),
    ]
    for form, gloss, note in neg_data:
        out += t(36,  y, form,  'start', 'Ls')
        out += t(150, y, gloss, 'start', 'Lx')
        out += t(290, y, note,  'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # Core vocabulary
    out += sh(y, 'CORE VOCABULARY (MIDDLE EGYPTIAN)')
    y += 10
    vocab = [
        ('nTr',  'god / divine'),
        ('s',    'man / person'),
        ('pr',   'house / to go out'),
        ('mAa',  'true / to show'),
        ('nfr',  'beautiful / good'),
        ('anx',  'life / to live'),
        ('wn',   'to be / to exist'),
        ('ii',   'to come'),
        (SH+'m', 'to go'),
        ('di',   'to give / to place'),
        ('ir',   'to do / to make'),
        ('in',   'by / it is (introduces agent)'),
        ('n',    'for / to / of (dative)'),
        ('m',    'in / with / as / from'),
        ('Hr',   'upon / face / above'),
        ('nb',   'lord / all / every'),
        ('Htp',  'peace / offering / to be satisfied'),
        ('mri',  'to love / desire'),
        ('xnt',  'in front of / forward / before (in space/time)'),
        ('sAA',  'to remember / to be mindful of'),
        ('rn',   'name'),
        ('pt',   'sky / heaven'),
        ('tA',   'earth / land'),
        ('rmT',  'people / human beings'),
        ('nfrw', 'beauty / goodness / freely'),
        ('sA',   'son / protection / back (future descendants)'),
        ('Hfnw', 'freely / at no cost / graciously'),
    ]
    # Three columns
    col_size = (len(vocab) + 2) // 3
    vcols = [(36, 140), (190, 290), (344, 450)]
    for ci, (cx1, cx2) in enumerate(vcols):
        chunk = vocab[ci*col_size:(ci+1)*col_size]
        cy = y
        for word, meaning in chunk:
            out += t(cx1, cy, word,    'start', 'Ls')
            out += t(cx2, cy, meaning, 'start', 'Lx')
            cy += 9

    out += footer('PLATE 61C')
    out += close_svg()
    return out

# ── Plate 61D — Running Text ──────────────────────────────────────────────────
def build_61d():
    out = open_svg()
    out += t(240, 32, 'ANCIENT EGYPTIAN', 'middle', 'T')
    out += t(240, 47, 'RUNNING TEXT \u00b7 ROSETTA STONE \u00b7 PYRAMID TEXTS \u00b7 HYMN TO THE ATEN', 'middle', 'S')
    out += hr(55)

    # Text 1: Rosetta Stone
    out += sh(63, 'ROSETTA STONE \u2014 OPENING (196 BCE, DECREE OF PTOLEMY V)')
    y = 74
    out += t(36, y, 'Hieroglyphic version (transliteration):', 'start', 'H')
    y += 10
    rosetta_translit = ALEPH + 'nk Pt-wlmys s n Pt-wlmys mi ' + ALEPH + 'nk Pt-wlmys s n Ars-t'
    out += bx(36, y, 404, 14)
    out += t(240, y+10, esc(rosetta_translit), 'middle', 'Lm')
    y += 18
    rosetta_gloss = 'In the reign of Ptolemy, son of Ptolemy \u2014 as Ptolemy, son of Arsinoe'
    out += t(240, y, rosetta_gloss, 'middle', 'Lx')
    y += 10
    out += t(36, y, 'NOTE: The Rosetta Stone (196 BCE) records the same decree in three scripts:', 'start', 'Lx')
    y += 9
    out += t(36, y, 'HIEROGLYPHIC (for priests) \u00b7 DEMOTIC (for Egyptians) \u00b7 GREEK (for rulers)', 'start', 'Lx')
    y += 9
    out += t(36, y, 'Jean-Fran\u00e7ois Champollion used it to decipher hieroglyphs in 1822 CE.', 'start', 'Lx')
    out += hr(y+11, 0.3)
    y += 18

    # Text 2: Pyramid Texts
    out += sh(y, 'PYRAMID TEXTS \u2014 SPELL 213 (c. 2375 BCE, OLDEST RELIGIOUS CORPUS)')
    y += 12
    pt_translit = 'nD Hr=k Wsr nD Hr=k \u2014 Hail to you, Osiris \u2014 Hail to you'
    out += bx(36, y, 404, 14)
    out += t(240, y+10, esc(pt_translit), 'middle', 'Lm')
    y += 18
    pt2 = 'wn=k m nTr mnx \u2014 "You are as an excellent god"'
    out += t(240, y, pt2, 'middle', 'Lx')
    y += 9
    out += t(36, y, 'ir.n.k ib=k n=i \u2014 "You have set your heart for me"', 'start', 'Lx')
    y += 9
    out += t(36, y, '(Inscribed on pyramid walls at Saqqara for Pharaoh Unas; oldest written corpus, c. 2375 BCE)', 'start', 'Lx')
    out += hr(y+11, 0.3)
    y += 18

    # Text 3: Hymn to the Aten
    out += sh(y, 'GREAT HYMN TO THE ATEN (AKHENATEN, c. 1346 BCE)')
    y += 12
    aten_lines = [
        ('nfr xr=k r Axt pt',                'Beautiful you appear on the horizon of heaven'),
        ('Itn anx xpr m tpw',                 'Living Aten, who originated life at the beginning'),
        ('di=k nTrw r tA nbt',                'You set every god upon the earth'),
        ('ir.n=k rmT nb mi anx.w',            'You made all people as if they were alive'),
    ]
    for translit, english in aten_lines:
        out += t(36, y, translit, 'start', 'Ls')
        y += 9
        out += t(50, y, english,  'start', 'Lx')
        y += 10
    out += t(36, y, '(Akhenaten\'s monotheistic hymn to the sun disc; parallels Psalm 104; unique theological document)', 'start', 'Lx')
    out += hr(y+11, 0.3)
    y += 18

    # Bridge phrase
    out += sh(y, 'BRIDGE PHRASE IN MIDDLE EGYPTIAN')
    y += 12
    out += bx(36, y, 404, 16)
    bridge_translit = 'ir.n.sn sw n=k, m nfrw, in rmT sAA.n.(sn) xnt'
    out += t(240, y+12, bridge_translit, 'middle', 'Lm')
    y += 22
    # Interlinear gloss
    gloss_words = [
        ('ir.n.sn', 'made-PERF-they'),
        ('sw',      'it/this'),
        ('n=k',     'for-you'),
        ('m nfrw',  'in beauty / freely'),
        ('in rmT',  'by people'),
        ('sAA.n.(sn)', 'remembered-PERF'),
        ('xnt',     'forward/before'),
    ]
    gw = 57
    gx = 36
    for i, (word, gloss) in enumerate(gloss_words):
        gxc = gx + i * gw
        if gxc + gw > 452: break
        out += t(gxc + gw//2, y,    word,  'middle', 'Ls')
        out += t(gxc + gw//2, y+9,  gloss, 'middle', 'Lx')
    y += 22

    out += bx(36, y, 404, 14)
    out += t(240, y+10, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Lx')
    y += 22

    # Linguistic notes
    out += t(36, y, 'LINGUISTIC NOTES ON THE PHRASE:', 'start', 'H')
    y += 10
    notes = [
        'ir.n.sn \u2014 Perfective (n-form) of ir "to make/do"; subject suffix sn "they".',
        'n=k \u2014 Dative particle n "for/to" + suffix pronoun =k (2sg.masc.).',
        'm nfrw \u2014 Preposition m "in/with" + nfrw "beauty, goodness, excellence" = "freely/graciously".',
        'in \u2014 Particle introducing the agent in a passive or cleft construction.',
        'sAA.n.sn \u2014 Perfective of sAA "to remember, be mindful of" \u2014 closest to "remembered".',
        'xnt \u2014 Preposition/adverb "forward, in front of, before" \u2014 spatial metaphor for future time.',
        'FUTURITY NOTE: Egyptian expresses the future spatially as xnt "what lies ahead / forward".',
        'This aligns exactly with the English phrase "remembered forward" \u2014 an active orientation toward',
        'future time, encoded in the same spatial metaphor (future = forward) across both languages.',
    ]
    for line in notes:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 61D')
    out += close_svg()
    return out

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate61a_ancient_egyptian_script.svg',    build_61a),
        ('plate61b_ancient_egyptian_phonology.svg', build_61b),
        ('plate61c_ancient_egyptian_grammar.svg',   build_61c),
        ('plate61d_ancient_egyptian_text.svg',      build_61d),
    ]
    for fname, fn in plates:
        path = os.path.join(OUT, fname)
        content = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK  {fname}  ({len(content)//1024} KB)')

if __name__ == '__main__':
    main()
