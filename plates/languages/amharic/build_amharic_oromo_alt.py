#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Amharic / Oromo alt plate series 31A–31D for Remember Forward.
Secondary language: Oromo (Afaan Oromoo) — Qubee Latin alphabet.
Geographic basis: Oromo is Ethiopia's largest language (~40M speakers),
spoken throughout the same country and within 500mi of Amharic's center.
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
        '  .La{font-size:11px} .Las{font-size:9px}\n'
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
    """Bold section break for secondary language."""
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


# ─── PLATE 31A ALT — SCRIPT ───────────────────────────────────────────────────

def build_31a_alt():
    g = open_svg()
    g += t(240, 30, 'AMHARIC + OROMO \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 31A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: AMHARIC FIDEL ──
    g += sh(63, 'AMHARIC \u2014 ETHIOPIC SCRIPT (FIDEL) \u2014 AN ABUGIDA')
    g += t(240, 73, 'Each Fidel symbol encodes consonant + vowel. ~234 syllable signs. Reads left-to-right.', 'middle', 'Ls')
    g += t(240, 82, 'Descended from South Arabian (Sabaean) script via ancient Ge\'ez (~4th c. CE). Never replaced by Latin.', 'middle', 'Lx')
    g += hr(89)

    g += sh(97, 'SAMPLE \u2014 CONSONANT h IN ALL 7 VOWEL ORDERS')
    g += t(240, 107, 'Each consonant has 7 forms \u2014 one per vowel order. Base form carries inherent /\u0259/ vowel.', 'middle', 'Lx')
    col_xs = [32, 78, 120, 162, 202, 242, 282, 336]
    vowel_hdrs = ['\u0259', 'u', 'i', 'a', 'e', '\u2014', 'o', 'C']
    rows = [
        ('\u1200','\u1201','\u1202','\u1203','\u1204','\u1205','\u1206','h\u2026'),
        ('\u1208','\u1209','\u120a','\u120b','\u120c','\u120d','\u120e','l\u2026'),
        ('\u1218','\u1219','\u121a','\u121b','\u121c','\u121d','\u121e','m\u2026'),
    ]
    for ci, vh in enumerate(vowel_hdrs):
        g += t(col_xs[ci], 116, vh, 'middle', 'Lx')
    for ri, row in enumerate(rows):
        y = 126 + ri * 14
        for ci, ch in enumerate(row):
            g += t(col_xs[ci], y, ch, 'middle', 'La' if ci < 7 else 'Lx')
    g += hr(170)

    g += sh(178, '7 VOWEL ORDERS')
    orders = [('1st','\u0259','base / like "about"'),('2nd','u','"boot"'),
               ('3rd','i','"see"'),('4th','a','"father"'),
               ('5th','e','"bed"'),('6th','\u2014','consonant only / short schwa'),
               ('7th','o','"go"')]
    for i, (ord_n, v, d) in enumerate(orders):
        y = 187 + i * 10
        g += t(60, y, ord_n, 'middle', 'Lx')
        g += t(130, y, v, 'middle', 'Ls')
        g += t(310, y, d, 'middle', 'Lx')
    g += hr(260)

    g += sh(268, 'NOTES')
    g += t(240, 278, 'Script also used for Tigrinya, Ge\'ez (liturgical), and Tigre. Fidel reads left-to-right.', 'middle', 'Lx')
    g += t(240, 287, 'Modern Amharic: official language of Ethiopia, ~35M native speakers (~100M L1+L2).', 'middle', 'Lx')
    g += t(240, 296, 'Semitic language \u2014 related to Arabic, Hebrew, Tigrinya; unrelated to Oromo (Cushitic).', 'middle', 'Lx')

    # ── SECONDARY DIVIDER ──
    g += sec_divider(308, 'OROMO (AFAAN OROMOO) \u00b7 SCRIPT \u00b7 QUBEE LATIN ALPHABET')

    # ── SECONDARY: OROMO QUBEE ──
    g += t(240, 340, 'Oromo is written in Qubee \u2014 a Latin-based alphabet adopted officially in 1991.', 'middle', 'Ls')
    g += t(240, 349, 'Qubee replaced Ethiopic script for Oromo, reflecting its Cushitic (not Semitic) identity.', 'middle', 'Lx')
    g += t(240, 358, '~40M native speakers. Official language of Oromia, Ethiopia. Left-to-right. ~33 letters.', 'middle', 'Lx')
    g += hr(366)

    g += sh(374, 'QUBEE \u2014 VOWELS: 5 SHORT + 5 LONG')
    g += t(240, 384, 'Short:  a   e   i   o   u', 'middle', 'L')
    g += t(240, 394, 'Long:  aa  ee  ii  oo  uu   \u2014 vowel length changes meaning', 'middle', 'Ls')
    g += t(240, 403, 'Example: qaba = to hold  vs.  qaabaa = name  vs.  qaabba = to stand', 'middle', 'Lx')
    g += hr(410)

    g += sh(418, 'SPECIAL CONSONANTS IN QUBEE')
    specials = [
        ('c',  '/t\u0283/',        'like "ch" in church'),
        ('ch', '/t\u0283\u02b0/', 'aspirated affricate'),
        ('dh', '/\u0253/',        'implosive dental \u2014 unique to Oromo / Cushitic'),
        ('ny', '/\u0272/',        'palatal nasal \u2014 like Spanish \u00f1'),
        ('q',  "/k\u02bc/",       'ejective velar \u2014 shared with Amharic'),
        ('sh', '/\u0283/',        'like English "sh"'),
        ('x',  '/x/',             'velar fricative (dialectal)'),
    ]
    for i, (ltr, ipa, note) in enumerate(specials):
        y = 427 + i * 10
        g += t(38, y, ltr, 'start', 'Ls')
        g += t(70, y, ipa, 'start', 'Lx')
        g += t(170, y, note, 'start', 'Lx')
    g += hr(502)

    g += sh(510, 'SCRIPT BRIDGE \u2014 KEY WORDS IN BOTH SCRIPTS')
    bridge = [
        ('\u12cd\u1203', 'w\u0259ha',  'bishaan',  'water'),
        ('\u12d5\u1265', "ts'at",      'ibidda',   'fire'),
        ('\u121d\u12f5\u122d', 'm\u0259dr', 'lafaa', 'earth'),
        ('\u1230\u12c8', 's\u0259w',   'namaa',    'person'),
        ('\u12c8\u122d\u1215', 'w\u0259rh', "ji'a", 'moon'),
    ]
    for lbl, x in zip(['Amharic', 'Translit.', 'Oromo (Qubee)', 'English'], [72, 172, 290, 400]):
        g += t(x, 520, lbl, 'middle', 'Lx')
    g += hr(525, sw=0.2)
    for i, (am, am_t, or_q, en) in enumerate(bridge):
        y = 534 + i * 12
        g += t(72,  y, am,   'middle', 'Las')
        g += t(172, y, am_t, 'middle', 'Lx')
        g += t(290, y, or_q, 'middle', 'Ls')
        g += t(400, y, en,   'middle', 'Lx')

    g += footer('31', 'AMHARIC', 'OROMO', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 31B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_31b_alt():
    g = open_svg()
    g += t(240, 30, 'AMHARIC + OROMO \u2014 PHONOLOGY \u00b7 SOUND SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 31B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: AMHARIC PHONOLOGY ──
    g += sh(63, 'AMHARIC \u2014 7 VOWELS')
    vowels = [('/\u0259/','1st order','central mid \u2014 "about"'),('/u/','2nd','high back \u2014 "boot"'),
               ('/i/','3rd','high front \u2014 "see"'),('/a/','4th','low central \u2014 "father"'),
               ('/e/','5th','mid front \u2014 "bed"'),('/\u0268/','6th','high central \u2014 short schwa'),
               ('/o/','7th','mid back \u2014 "go"')]
    for i, (ipa, order, desc) in enumerate(vowels):
        y = 72 + i * 10
        g += t(55,  y, ipa,   'middle', 'Lx')
        g += t(130, y, order, 'middle', 'Lx')
        g += t(330, y, desc,  'middle', 'Lx')
    g += hr(147)

    g += sh(155, 'EJECTIVE CONSONANTS \u2014 KEY AMHARIC FEATURE')
    g += t(240, 165, 'Ejectives: produced with glottalic airstream \u2014 glottal + oral closure, then burst. Phonemically distinct.', 'middle', 'Ls')
    ejectives = [("p\u02bc", '/p\u02bc/', 'ejective bilabial \u2014 rare'),
                 ("t\u02bc", '/t\u02bc/', 'ejective alveolar \u2014 frequent'),
                 ("k\u02bc", '/k\u02bc/', 'ejective velar \u2014 very common: k\'al (word)'),
                 ("ts\u02bc",'/ts\u02bc/','ejective affricate \u2014 common'),
                 ("ch\u02bc",'/t\u0283\u02bc/','ejective palatal affricate')]
    for i, (ltr, ipa, note) in enumerate(ejectives):
        y = 174 + i * 10
        g += t(50,  y, ltr,  'middle', 'Ls')
        g += t(110, y, ipa,  'middle', 'Lx')
        g += t(320, y, note, 'middle', 'Lx')
    g += hr(226)

    g += sh(234, 'PHARYNGEALS \u00b7 GEMINATION')
    g += t(240, 244, 'Pharyngeals \u02bf \u02be: fricative sounds at back of throat \u2014 Semitic heritage shared with Arabic, Hebrew.', 'middle', 'Ls')
    g += t(240, 253, 'Gemination: doubled consonants phonemically distinct. t\u0259bab\u0259 "wrapped" \u2260 t\u0259babbb\u0259t "wrapped intensely".', 'middle', 'Lx')
    g += t(240, 262, 'Gemination also marks verb-object agreement: y\u0259-s\u0259ma (he hears) vs. y\u0259-ss\u0259m\u0259\u02bf (he listens).', 'middle', 'Lx')

    # ── SECONDARY DIVIDER ──
    g += sec_divider(274, 'OROMO (AFAAN OROMOO) \u00b7 PHONOLOGY \u00b7 SOUND SYSTEM')

    # ── SECONDARY: OROMO PHONOLOGY ──
    g += t(240, 306, 'Oromo is a Cushitic language (Afro-Asiatic). Shares geographic range with Amharic but distinct phonology.', 'middle', 'Ls')
    g += hr(313)

    g += sh(321, 'OROMO \u2014 5 VOWELS + PHONEMIC LENGTH')
    g += t(240, 331, 'Five vowels: /a/ /e/ /i/ /o/ /u/ \u2014 each has a short and long form.', 'middle', 'Ls')
    g += t(240, 340, 'Long vowels written doubled: aa, ee, ii, oo, uu. Length is phonemically contrastive:', 'middle', 'Lx')
    vowel_pairs = [('lafa','earth (short a)','lafaa','of the earth (long aa \u2014 genitive)'),
                   ("ji'a","moon (short i)",'jiia','[emphatic, dialectal]'),
                   ('baay\u2019ee','very/much','bayee','[variant]')]
    for i, (s1, g1, s2, g2) in enumerate(vowel_pairs):
        y = 349 + i * 10
        g += t(80,  y, s1, 'middle', 'Ls'); g += t(180, y, g1, 'middle', 'Lx')
        g += t(290, y, s2, 'middle', 'Ls'); g += t(400, y, g2, 'middle', 'Lx')
    g += hr(384)

    g += sh(392, 'KEY CONSONANT FEATURES')
    features = [
        ('dh = /\u0253/','Implosive alveolar \u2014 unique Cushitic feature. Not present in Amharic.'),
        ('q = /k\u02bc/', 'Ejective velar \u2014 shared with Amharic and many Ethiopian languages.'),
        ('c = /t\u0283/','Affricate, like "ch" \u2014 written as single letter c in Qubee.'),
        ('Gemination','Double consonants phonemically distinct: biyya (country) \u2260 biyyaa (your country).'),
        ('No pharyngeals','Unlike Amharic, Oromo has no \u02bf \u02be pharyngeal sounds \u2014 Cushitic, not Semitic.'),
        ('No lexical tone','Oromo has NO tonal distinctions. Meaning carried by vowel length, not pitch.'),
    ]
    for i, (feat, desc) in enumerate(features):
        y = 401 + i * 18
        g += t(60,  y,    feat, 'start', 'Ls')
        g += t(60,  y+9,  desc, 'start', 'Lx')
    g += hr(512)

    g += sh(520, 'COMPARATIVE NOTE \u2014 AMHARIC VS. OROMO PHONOLOGY')
    g += t(240, 530, 'Both: ejective q, affricate ch, gemination, no lexical tone.', 'middle', 'Ls')
    g += t(240, 539, 'Amharic has: 7 vowels, pharyngeals \u02bf \u02be, more ejective series.', 'middle', 'Lx')
    g += t(240, 548, 'Oromo has: 5 vowels + length, implosive dh, no pharyngeals.', 'middle', 'Lx')
    g += t(240, 557, 'Despite geography, these are unrelated language families sharing acoustic environment.', 'middle', 'Lx')

    g += footer('31', 'AMHARIC', 'OROMO', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 31C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_31c_alt():
    g = open_svg()
    g += t(240, 30, 'AMHARIC + OROMO \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 31C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: AMHARIC GRAMMAR ──
    g += sh(63, 'AMHARIC \u2014 SOV \u00b7 VERB-FINAL \u00b7 SEMITIC ROOTS')
    g += t(240, 73, 'Amharic is SOV (Subject-Object-Verb). Verb always last. Extensive prefix/suffix system.', 'middle', 'Ls')
    g += t(240, 82, 'Semitic 3-consonant root: s-b-r = "break" \u2192 s\u0259bb\u0259r\u0259 (he broke) / as\u0259bb\u0259r\u0259 (he broke it, causative).', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'VERB CONJUGATION \u2014 n\u0259gg\u0259r\u0259 "spoke"')
    conj = [('1sg','n\u0259gg\u0259r-ku','I spoke'),('2sg M','n\u0259gg\u0259r-k','you (m) spoke'),
            ('2sg F','n\u0259gg\u0259r-sh','you (f) spoke'),('3sg M','n\u0259gg\u0259r\u0259','he spoke'),
            ('3sg F','n\u0259gg\u0259r-\u0259tch','she spoke'),('1pl','n\u0259gg\u0259rn\u0259','we spoke'),
            ('2pl','n\u0259gg\u0259r-\u0259chu','you (pl) spoke'),('3pl','n\u0259gg\u0259ru','they spoke')]
    for i, (pers, form, gl) in enumerate(conj):
        y = 108 + i * 10
        g += t(55, y, pers, 'middle', 'Lx'); g += t(170, y, form, 'middle', 'Ls'); g += t(340, y, gl, 'middle', 'Lx')
    g += hr(192)

    g += sh(200, 'CORE AMHARIC VOCABULARY \u2014 20 WORDS')
    vocab_am = [
        ('\u12cd\u1203','w\u0259ha','water'), ('\u12d5\u1265',"ts'at",'fire'),
        ('\u121d\u12f5\u122d','m\u0259dr','earth'), ('\u1230\u12c8','s\u0259w','person'),
        ('\u12c8\u122d\u1215','w\u0259rh','moon'), ('\u12b0\u12ad\u12d3\u1275',"wk'iat",'star'),
        ('\u12a3\u12cd\u1295\u1275','awunt','yes'), ('\u12a0\u12ed\u12f0\u120d\u121d','ayd\u0259l\u0259m','no'),
        ('\u12a5\u1294','\u0259n\u0259','I'), ('\u12a0\u1295\u1270','ant\u0259','you(m)'),
        ('\u134d\u1240\u122d','f\u0268q\u0259r','love'), ('\u1270\u1235\u134a','t\u0259sf\u0268a','freedom'),
        ('\u12c8\u12f0\u12d3\u12ed\u1275','w\u0259d\u0259ayt','future'), ('\u12d3\u1208\u121d','al\u0259m','world'),
        ('\u1240\u1293','q\u0259na','good'), ('\u121e\u1275','mot\u0259','death'),
        ('\u12d8\u1218\u1295','z\u0259men','life/time'), ('\u1219\u1273','\u0259muta','gratitude'),
        ('\u1218\u127d','m\u0259tch','when'), ('\u12e8\u1275','yet','where'),
    ]
    cols = [vocab_am[:10], vocab_am[10:]]
    for ci, col in enumerate(cols):
        for ri, (am, tr, en) in enumerate(col):
            y = 210 + ri * 10
            x0 = 20 + ci * 240
            g += t(x0+10, y, am, 'start', 'Las')
            g += t(x0+60, y, tr, 'start', 'Lx')
            g += t(x0+130, y, en, 'start', 'Lx')
    g += hr(316)

    # ── SECONDARY DIVIDER ──
    g += sec_divider(324, 'OROMO (AFAAN OROMOO) \u00b7 GRAMMAR \u00b7 VOCABULARY')

    # ── SECONDARY: OROMO GRAMMAR ──
    g += t(240, 356, 'Oromo is also SOV \u2014 verb-final. Both Amharic and Oromo share this word order despite being unrelated.', 'middle', 'Ls')
    g += t(240, 365, 'Example: Ani nyaata nyaadha = I food eat ("I eat food"). Verb nyaadha always comes last.', 'middle', 'Lx')
    g += t(240, 374, 'Agglutinative: suffixes stack onto verb root. Tense: -a (present), -e (past), -u (imperative).', 'middle', 'Lx')
    g += hr(381)

    g += sh(389, 'CORE OROMO VOCABULARY \u2014 AFAAN OROMOO (QUBEE)')
    vocab_or = [
        ('bishaan','water'), ('ibidda','fire'), ('lafaa','earth'),
        ('namaa','person/human'), ("ji'a",'moon'), ('aduu','sun'),
        ('eeyyee','yes'), ('lakki','no'), ('ani','I'), ('ati','you (sg)'),
        ('jaalala','love'), ('bilisummaa','freedom'), ('fuuldura','forward / future'),
        ('addunyaa','world'), ('gaarii','good'), ('du\'a','death'),
        ('jireenya','life'), ('galata','gratitude'), ('yoom','when'), ('eessa','where'),
    ]
    cols_or = [vocab_or[:10], vocab_or[10:]]
    for ci, col in enumerate(cols_or):
        for ri, (or_w, en) in enumerate(col):
            y = 399 + ri * 10
            x0 = 20 + ci * 240
            g += t(x0+10, y, or_w, 'start', 'Ls')
            g += t(x0+110, y, en,  'start', 'Lx')
    g += hr(506)

    g += sh(514, 'SIDE-BY-SIDE \u2014 SAME CONCEPTS, DIFFERENT ROOTS')
    # comparison table
    comp = [
        ('future','w\u0259d\u0259ayt','fuuldura'),
        ('freedom','t\u0259sf\u0268a','bilisummaa'),
        ('person','s\u0259w','namaa'),
        ('love','f\u0268q\u0259r','jaalala'),
    ]
    g += hr(510, sw=0.3)
    g += sh(518, 'SIDE-BY-SIDE \u2014 SAME CONCEPTS, DIFFERENT ROOTS')
    for lbl, x in zip(['Concept', 'Amharic', 'Oromo'], [100, 240, 370]):
        g += t(x, 528, lbl, 'middle', 'Lx')
    g += hr(533, sw=0.2)
    for i, (con, am, oo) in enumerate(comp):
        y = 542 + i * 10
        g += t(100, y, con, 'middle', 'Lx')
        g += t(240, y, am,  'middle', 'Ls')
        g += t(370, y, oo,  'middle', 'Ls')

    g += footer('31', 'AMHARIC', 'OROMO', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 31D ALT — RUNNING TEXT ────────────────────────────────────────────

def build_31d_alt():
    g = open_svg()
    g += t(240, 30, 'AMHARIC + OROMO \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 31D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: AMHARIC TEXT ──
    g += sh(63, 'AMHARIC \u2014 PASSAGE 1 \u00b7 ETHIOPIAN PROVERB')
    g += t(240, 74, '\u12a0\u1218\u1233 \u1208\u12ab\u12d5\u1299 \u12eb\u1235\u1233\u1323\u120d\u1362', 'middle', 'La')
    g += t(240, 87, "\u0259m\u0259sa l\u0259k'aN\u0259tu yas\u0259sat\u0259al.", 'middle', 'Lx')
    g += t(240, 96, '"A fish is caught because of its mouth." \u2014 Be careful what you say.', 'middle', 'Ls')
    g += hr(104)

    g += sh(112, 'AMHARIC \u2014 PASSAGE 2 \u00b7 MOTTO')
    g += t(240, 123, '\u12a2\u1275\u12ee\u1335\u12eb \u1208\u12a0\u1208\u121d', 'middle', 'La')
    g += t(240, 136, "Ityopy'a l\u0259al\u0259m", 'middle', 'Lx')
    g += t(240, 145, '"Ethiopia forever." \u2014 Traditional patriotic expression.', 'middle', 'Ls')
    g += hr(153)

    g += sh(161, 'AMHARIC \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g += t(240, 173, '\u12ed\u1205 \u12e8\u1270\u1233\u1290\u12cd \u1218\u120d\u12a5\u12ad\u1275 \u1260\u1290\u1333 \u1270\u12f8\u129d\u1290\u12cd\u1290\u1275 \u1208\u12d8\u12ad\u1275 \u1270\u12f0\u1228\u1308\u1362', 'middle', 'Las')
    g += t(240, 185, 'Y\u0259h y\u0259t\u0259saN\u0259w\u0259 m\u0259l\u0259\u0259kt b\u0259n\u0259ts\'ina t\u0259z\u0259\u0268w\u0259n\u0259w\u0259nt l\u0259z\u0259kt t\u0259d\u0259r\u0259g\u0259.', 'middle', 'Lx')
    g += t(240, 194, 'This message  freely  who-remembered  forward  was-made.', 'middle', 'Lx')
    g += t(240, 203, '"This message was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    g += hr(211)

    g += sh(219, 'LANGUAGE NOTE \u2014 "FUTURE" IN AMHARIC')
    g += t(240, 229, 'w\u0259d\u0259ayt: "future" \u2014 lit. "the-forward-direction." From w\u0259d (toward) + ayt (direction).', 'middle', 'Ls')
    g += t(240, 238, 'Amharic orients time spatially: what is ahead (w\u0259d) = the future; what is behind = the past.', 'middle', 'Lx')
    g += t(240, 247, 'b\u0259n\u0259ts\'ina: "freely" \u2014 from n\u0259ts\u02bc (freedom) \u2014 the gift is etymologically rooted in liberty.', 'middle', 'Lx')

    # ── SECONDARY DIVIDER ──
    g += sec_divider(259, 'OROMO (AFAAN OROMOO) \u00b7 RUNNING TEXT \u00b7 PASSAGES')

    # ── SECONDARY: OROMO TEXT ──
    g += sh(290, 'OROMO \u2014 PASSAGE 1 \u00b7 OROMO PROVERB')
    g += t(240, 300, 'Namni nama tolcha.', 'middle', 'L')
    g += t(240, 310, 'Person  person  builds.', 'middle', 'Lx')
    g += t(240, 319, '"A person builds a person." \u2014 We are built by each other. Community is the foundation.', 'middle', 'Ls')
    g += hr(327)

    g += sh(335, 'OROMO \u2014 PASSAGE 2 \u00b7 PROVERB')
    g += t(240, 345, 'Ollaan ollaa barbaada.', 'middle', 'L')
    g += t(240, 355, 'Neighbor  neighbor  seeks.', 'middle', 'Lx')
    g += t(240, 364, '"A neighbor seeks a neighbor." \u2014 Humans are social beings who need one another.', 'middle', 'Ls')
    g += hr(372)

    g += sh(380, 'OROMO \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g += t(240, 391, 'Kun isiniif bilisaan, namoota fuuldura isin yaadataniin, hojjetame.', 'middle', 'L')
    g += t(240, 401, 'This  for-you  freely,  people  forward   you  remembered-by,  was-made.', 'middle', 'Lx')
    g += t(240, 411, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    g += hr(419)

    g += sh(427, 'LANGUAGE NOTE \u2014 "FORWARD" IN OROMO')
    g += t(240, 437, 'fuuldura: "forward" \u2014 lit. "in front of the face." From fuul (face) + dura (before/in-front).', 'middle', 'Ls')
    g += t(240, 447, 'Oromo conceptualizes the future as what stands before you \u2014 visible, ahead, faced directly.', 'middle', 'Lx')
    g += t(240, 456, 'bilisaan: "freely" \u2014 from bilisaa (free). Root shared with bilisummaa (freedom).', 'middle', 'Lx')
    g += t(240, 465, 'yaadataniin: "who remembered" \u2014 from yaadachuu (to remember) + -aniin (relative clause marker).', 'middle', 'Lx')
    g += hr(473)

    g += sh(481, 'DECODING NOTE \u2014 FOR FUTURE READERS')
    g += t(240, 491, 'Amharic: official language of Ethiopia, ~35M native speakers. Written in Ethiopic/Fidel abugida.', 'middle', 'Ls')
    g += t(240, 500, 'Oromo: largest language in Ethiopia, ~40M native speakers. Written in Latin-based Qubee alphabet.', 'middle', 'Ls')
    g += t(240, 509, 'Both are Afro-Asiatic languages but from different branches: Amharic = Semitic; Oromo = Cushitic.', 'middle', 'Ls')
    g += t(240, 518, 'Both are SOV. Both have ejective consonants. Both originate in the same highland region.', 'middle', 'Lx')
    g += t(240, 527, 'See plates 31A\u201331C for scripts, phonology, and grammar. Plate 34A\u201334D covers Tigrinya (related to Amharic).', 'middle', 'Lx')

    g += footer('31', 'AMHARIC', 'OROMO', 'D', 'Text')
    return g + close_svg()


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate31a_amharic_oromo_script_alt.svg':    build_31a_alt(),
        'plate31b_amharic_oromo_phonology_alt.svg': build_31b_alt(),
        'plate31c_amharic_oromo_grammar_alt.svg':   build_31c_alt(),
        'plate31d_amharic_oromo_text_alt.svg':      build_31d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
