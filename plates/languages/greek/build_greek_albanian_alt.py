#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Greek / Albanian alt plate series 21A–21D for Remember Forward.
Secondary language: Albanian (shqip) — spoken in Albania, Kosovo, North Macedonia,
and northwest Greece. Within ~500 miles of Greek geographic center (Athens area).
~7.5 million native speakers. An independent branch of Indo-European — no close relatives.
Geographic basis: Albania directly borders Greece. Tirana ~370km from Athens.
Albanian is the most distinct language in the immediate neighborhood of Greece
(not another Hellenic, not Slavic, not Romance — a genuine isolate branch).
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
        '  .Lg{font-size:12px}\n'
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


# ─── PLATE 21A ALT — SCRIPT ───────────────────────────────────────────────────

def build_21a_alt():
    g = open_svg()
    g += t(240, 30, 'GREEK + ALBANIAN \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 21A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'GREEK \u2014 GREEK ALPHABET \u00b7 24 LETTERS')
    g += t(240, 73, 'The Greek alphabet: first in history to represent both consonants AND vowels (from ~800 BCE).', 'middle', 'Ls')
    g += t(240, 82, 'Ancestor of Latin, Cyrillic, Coptic, Gothic, and Armenian scripts. Written left to right.', 'middle', 'Lx')
    g += hr(89)

    g += sh(97, 'ALL 24 GREEK LETTERS \u2014 UPPER AND LOWER CASE')
    letters = [
        ('\u0391\u03b1','Alpha','/a/'), ('\u0392\u03b2','Beta','/v/ mod.'), ('\u0393\u03b3','Gamma','/\u0263/'),
        ('\u0394\u03b4','Delta','/\u00f0/'), ('\u0395\u03b5','Epsilon','/e/'), ('\u0396\u03b6','Zeta','/z/'),
        ('\u0397\u03b7','Eta','/i/'), ('\u0398\u03b8','Theta','/\u03b8/'), ('\u0399\u03b9','Iota','/i/'),
        ('\u039a\u03ba','Kappa','/k/'), ('\u039b\u03bb','Lambda','/l/'), ('\u039c\u03bc','Mu','/m/'),
        ('\u039d\u03bd','Nu','/n/'), ('\u039e\u03be','Xi','/ks/'), ('\u039f\u03bf','Omicron','/o/'),
        ('\u03a0\u03c0','Pi','/p/'), ('\u03a1\u03c1','Rho','/r/'), ('\u03a3\u03c3\u03c2','Sigma','/s/'),
        ('\u03a4\u03c4','Tau','/t/'), ('\u03a5\u03c5','Upsilon','/i/'), ('\u03a6\u03c6','Phi','/f/'),
        ('\u03a7\u03c7','Chi','/x/'), ('\u03a8\u03c8','Psi','/ps/'), ('\u03a9\u03c9','Omega','/o/'),
    ]
    for i, (ltr, name, ipa) in enumerate(letters):
        col = i % 4; row = i // 4
        x = 55 + col * 105; y = 107 + row * 13
        g += t(x, y, ltr, 'middle', 'Lg')
        g += t(x, y + 8, f'{name} {ipa}', 'middle', 'Lx')
    g += hr(195)

    g += sh(203, 'GREEK DIGRAPHS AND MODERN PRONUNCIATION')
    dg = [
        ('\u03b1\u03b9', '/e/', 'aisle \u2192 /e/: \u03c0\u03b1\u03b9\u03b4\u03af (child)'),
        ('\u03bf\u03b9', '/i/', 'oi \u2192 /i/: \u03bf\u03b9\u03ba\u03bf\u03b3\u03ad\u03bd\u03b5\u03b9\u03b1 (family)'),
        ('\u03b5\u03b9', '/i/', 'ei \u2192 /i/: \u03b5\u03b9\u03c1\u03ae\u03bd\u03b7 (peace)'),
        ('\u03c5\u03b9', '/i/', 'yi \u2192 /i/: rare'),
        ('\u03bc\u03c0', '/b/ or /mb/', '\u03bc\u03c0\u03b1\u03bb\u03ba\u03cc\u03bd\u03b9 (balcony)'),
        ('\u03bd\u03c4', '/d/ or /nd/', '\u03bd\u03c4\u03bf\u03bc\u03ac\u03c4\u03b1 (tomatoes)'),
        ('\u03b3\u03ba', '/g/ or /ng/', '\u03b3\u03ba\u03b1\u03c1\u03c3\u03cc\u03bd (waiter)'),
    ]
    for i, (dg_c, ipa, ex) in enumerate(dg):
        y = 213 + i * 10
        g += t(55, y, dg_c, 'middle', 'Ls')
        g += t(115, y, ipa, 'middle', 'Lx')
        g += t(310, y, ex, 'middle', 'Lx')
    g += hr(288)

    g += sh(296, 'GREEK SCRIPT HISTORY')
    g += t(240, 306, 'Linear B (Mycenaean, ~1450 BCE) \u2192 Greek alphabet (~800 BCE, from Phoenician) \u2192 Classical Greek.', 'middle', 'Ls')
    g += t(240, 315, 'Greek letters became names: alpha, beta, gamma \u2192 alphabet. Used for mathematics, science, theology for 2700+ years.', 'middle', 'Lx')

    g += sec_divider(325, 'SECONDARY \u2014 ALBANIAN (SHQIP) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(351, 'ALBANIAN \u2014 LATIN ALPHABET \u00b7 36 LETTERS')
    g += t(240, 361, 'Modern Albanian uses a 36-letter Latin alphabet standardized in 1908 (Congress of Manastir).', 'middle', 'Ls')
    g += t(240, 370, 'Before 1908: Albanian written in Greek, Latin, Arabic, and multiple competing local alphabets.', 'middle', 'Lx')
    g += t(240, 379, 'Elbasan script (18th c. CE) and other native scripts existed but were not standardized.', 'middle', 'Lx')
    g += hr(387)

    g += sh(395, 'ALBANIAN SPECIAL LETTERS')
    alb_letters = [
        ('\u00eb', '/\u0259/', 'schwa: \u00ebsht\u00eb (is), m\u00ebso (learn)'),
        ('\u00e7', '/t\u0283/', 'affricate: \u00e7do (every), \u00e7\u00e7upa (girl)'),
        ('dh', '/\u00f0/', 'like th in \u201cthis\u201d: dhe (and/earth), dh\u00ebndr\u00ebr (son-in-law)'),
        ('gj', '/\u025f/', 'palatal g: gjak (blood), gjuh\u00eb (language/tongue)'),
        ('ll', '/\u026b/', 'dark l: lloj (type), mall (longing)'),
        ('nj', '/\u0272/', 'palatal n: njeri (person), nj\u00ebzet (twenty)'),
        ('rr', '/r/', 'trill r: rr\u00ebnja (root), rrug\u00eb (road)'),
        ('sh', '/\u0283/', 'like sh in \u201cshoe\u201d: shqip (Albanian), sh\u00ebndeti (health)'),
        ('th', '/\u03b8/', 'like th in \u201cthin\u201d: them (I say), thik\u00eb (knife)'),
        ('xh', '/d\u0292/', 'like j in \u201cjump\u201d: xhami (window/glass), xhaxha (uncle)'),
        ('zh', '/\u0292/', 'like s in \u201cpleasure\u201d: zhurmoj (to make noise)'),
    ]
    for i, (ch, ipa, ex) in enumerate(alb_letters):
        y = 405 + i * 10
        g += t(42, y, ch, 'middle', 'Ls')
        g += t(100, y, ipa, 'middle', 'Lx')
        g += t(310, y, ex, 'middle', 'Lx')

    g += footer('21', 'Greek', 'Albanian', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 21B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_21b_alt():
    g = open_svg()
    g += t(240, 30, 'GREEK + ALBANIAN \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 21B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'GREEK PHONOLOGY \u2014 MODERN GREEK')
    g += t(240, 73, 'Modern Greek has 5 vowels: /a e i o u/ \u2014 much simpler than Ancient Greek (no long/short vowel distinction).', 'middle', 'Ls')
    g += t(240, 82, 'Seven letters/digraphs \u2192 /i/: \u03b7 \u03b9 \u03c5 \u03b1\u03b9 \u03b5\u03b9 \u03bf\u03b9 \u03c5\u03b9 \u2014 all pronounced identically in Modern Greek.', 'middle', 'Ls')
    g += t(240, 91, 'This iotacism (merger of front vowels) is a major feature of modern pronunciation.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'GREEK CONSONANTS \u2014 MODERN VALUES')
    gcons = [
        ('\u03b2', '/v/', 'was /b/ in Ancient; now bilabial fricative'),
        ('\u03b3', '/\u0263/ or /j/', 'velar fricative; /j/ before front vowels'),
        ('\u03b4', '/\u00f0/', 'was /d/; now dental fricative like \u201cthis\u201d'),
        ('\u03b8', '/\u03b8/', 'was aspirated /t\u02b0/; now dental fricative like \u201cthin\u201d'),
        ('\u03c6', '/f/', 'was aspirated /p\u02b0/; now labiodental fricative'),
        ('\u03c7', '/x/ or /\u00e7/', 'was aspirated /k\u02b0/; now velar/palatal fricative'),
        ('\u03c3/\u03c2', '/s/', 'standard sibilant; \u03c2 word-final only'),
        ('\u03c1', '/r/', 'alveolar, often uvular in some dialects'),
    ]
    for i, (ch, ipa, note) in enumerate(gcons):
        y = 117 + i * 10
        g += t(45, y, ch, 'middle', 'Lg')
        g += t(90, y, ipa, 'middle', 'Lx')
        g += t(310, y, note, 'middle', 'Lx')
    g += hr(200)

    g += sh(208, 'GREEK STRESS \u2014 TONIC ACCENT')
    g += t(240, 218, 'Modern Greek has a fixed tonic (pitch/intensity) accent, marked with an acute: \u03ac \u03ad \u03ae \u03af \u03cc \u03cd \u03ce.', 'middle', 'Ls')
    g += t(240, 227, 'Stress is lexical and can fall on one of the last three syllables. \u03b8\u03ac\u03bb\u03b1\u03c3\u03c3\u03b1 (sea), \u03b1\u03b3\u03ac\u03c0\u03b7 (love).', 'middle', 'Lx')
    g += t(240, 236, 'Ancient Greek had pitch accent (high/low tones). Modern: intensity accent. Accent can shift with case.', 'middle', 'Lx')
    g += hr(244)

    g += sh(252, 'GREEK PITCH ACCENT VS. MODERN STRESS')
    g += t(240, 262, 'Ancient: three accents \u2014 acute (\u0301), grave (\u0300), circumflex (\u0302) \u2014 encoding pitch melody over syllables.', 'middle', 'Ls')
    g += t(240, 271, 'Modern: single acute only \u2014 marks syllable receiving stress. Historical accent preserved in spelling only.', 'middle', 'Lx')

    g += sec_divider(281, 'SECONDARY \u2014 ALBANIAN (SHQIP) \u2014 PHONOLOGY')

    g += sh(307, 'ALBANIAN VOWELS \u2014 7 PHONEMES')
    g += t(240, 317, 'Albanian has 7 vowels: /a e \u025b i o u \u0259/. The schwa /\u0259/ (written \u00eb) is distinctive and common.', 'middle', 'Ls')
    alb_v = [
        ('/a/', '\u00e2n\u00eb (breath)'), ('/e/', 'emr (name)'), ('/\u025b/', '\u00ebsht\u00eb (is)'),
        ('/i/', 'im (my)'), ('/o/', 'or (gold)'), ('/u/', 'uj\u00eb (water)'), ('/\u0259/', '\u00ebnd\u00ebr (dream)'),
    ]
    for i, (ipa, ex) in enumerate(alb_v):
        col = i % 4; row = i // 4
        x = 55 + col * 105; y = 327 + row * 11
        g += t(x, y, f'{ipa} {ex}', 'middle', 'Lx')
    g += hr(353)

    g += sh(361, 'ALBANIAN CONSONANTS \u2014 RHOTICS AND AFFRICATES')
    g += t(240, 371, 'Albanian distinguishes r (flap /\u027e/) vs. rr (trill /r/): rruga (road) vs. arusha (bear).', 'middle', 'Ls')
    g += t(240, 380, 'l (lateral /l/) vs. ll (dark lateral /\u026b/): like English l in \u201clid\u201d vs. \u201cmall\u201d.', 'middle', 'Lx')
    g += t(240, 389, 'Rich affricate series: c /ts/, \u00e7 /t\u0283/, x /dz/, xh /d\u0292/ \u2014 all phonemically distinct.', 'middle', 'Lx')
    g += t(240, 398, 'gj /\u025f/ and nj /\u0272/: palatalized stops, preserved from Proto-Albanian.', 'middle', 'Lx')
    g += hr(406)

    g += sh(414, 'ALBANIAN STRESS \u2014 PENULTIMATE DEFAULT')
    g += t(240, 424, 'Stress typically falls on penultimate syllable: \u2019gjuh\u00eb (language), \u2019njeri (person), \u2019liri (freedom).', 'middle', 'Ls')
    g += t(240, 433, 'Final syllable stress in some loanwords and grammatical forms (e.g., definite article suffixes).', 'middle', 'Lx')
    g += hr(441)

    g += sh(449, 'PHONOLOGICAL BRIDGE \u2014 GREEK AND ALBANIAN')
    comp = [
        ('Feature', 'Greek', 'Albanian'),
        ('Vowels', '5 (/a e i o u/)', '7 (incl. schwa /\u0259/)'),
        ('Schwa', 'No', 'Yes \u2014 \u00eb is common'),
        ('Rhotics', '1 (/r/)', '2 (r flap, rr trill)'),
        ('Laterals', '1 (/l/)', '2 (l clear, ll dark)'),
        ('Script', 'Greek alphabet', 'Latin (since 1908)'),
    ]
    for i, row in enumerate(comp):
        y = 459 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('21', 'Greek', 'Albanian', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 21C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_21c_alt():
    g = open_svg()
    g += t(240, 30, 'GREEK + ALBANIAN \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 21C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'GREEK GRAMMAR \u2014 SVO \u00b7 INFLECTING \u00b7 3 GENDERS')
    g += t(240, 73, 'Modern Greek is SVO with relatively free word order (inflection carries grammar).', 'middle', 'Ls')
    g += t(240, 82, '3 genders: masculine, feminine, neuter. 4 cases: nominative, genitive, accusative, vocative.', 'middle', 'Lx')
    g += t(240, 91, 'Articles: definite \u03bf/\u03b7/\u03c4\u03bf (M/F/N) \u00b7 indefinite \u03ad\u03bd\u03b1\u03c2/\u03bc\u03af\u03b1/\u03ad\u03bd\u03b1. Must agree in gender, number, case.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'GREEK VERB SYSTEM \u2014 \u03b3\u03c1\u03ac\u03c6\u03c9 (write)')
    gverb = [
        ('\u03b3\u03c1\u03ac\u03c6\u03c9', 'I write'), ('\u03b3\u03c1\u03ac\u03c6\u03b5\u03b9\u03c2', 'you write'),
        ('\u03b3\u03c1\u03ac\u03c6\u03b5\u03b9', 'he/she writes'), ('\u03b3\u03c1\u03ac\u03c6\u03bf\u03c5\u03bc\u03b5', 'we write'),
        ('\u03b3\u03c1\u03ac\u03c6\u03b5\u03c4\u03b5', 'you (pl) write'), ('\u03b3\u03c1\u03ac\u03c6\u03bf\u03c5\u03bd', 'they write'),
    ]
    for i, (form, gloss) in enumerate(gverb):
        col = i % 2; row = i // 2
        x = 80 + col * 220; y = 117 + row * 10
        g += t(x, y, form, 'middle', 'Ls')
        g += t(x + 80, y, gloss, 'middle', 'Lx')
    g += t(240, 150, 'Aspect: imperfective vs. perfective. Past: \u03ad\u03b3\u03c1\u03b1\u03c8\u03b1 (I wrote). Future: \u03b8\u03b1 \u03b3\u03c1\u03ac\u03c8\u03c9.', 'middle', 'Lx')
    g += hr(158)

    g += sh(166, 'GREEK CORE VOCABULARY')
    gvocab = [
        ('\u03bd\u03b5\u03c1\u03cc', 'water'), ('\u03c6\u03c9\u03c4\u03b9\u03ac', 'fire'), ('\u03b3\u03b7', 'earth'), ('\u03ac\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03c2', 'person'),
        ('\u03c6\u03b5\u03b3\u03b3\u03ac\u03c1\u03b9', 'moon'), ('\u03bc\u03bd\u03ae\u03bc\u03b7', 'memory'), ('\u03bc\u03ad\u03bb\u03bb\u03bf\u03bd', 'future'), ('\u03b5\u03bb\u03b5\u03c5\u03b8\u03b5\u03c1\u03af\u03b1', 'freedom'),
        ('\u03ba\u03b1\u03c1\u03b4\u03b9\u03ac', 'heart'), ('\u03b1\u03b3\u03ac\u03c0\u03b7', 'love'), ('\u03ba\u03cc\u03c3\u03bc\u03bf\u03c2', 'world'), ('\u03b6\u03c9\u03ae', 'life'),
    ]
    for i, (gr, en) in enumerate(gvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 176 + row * 10
        g += t(x, y, gr, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')

    g += sec_divider(221, 'SECONDARY \u2014 ALBANIAN (SHQIP) \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(247, 'ALBANIAN GRAMMAR \u2014 UNIQUE FEATURES')
    g += t(240, 257, 'Albanian is SVO. Suffixed definite article (postposed): gjuh + \u00eb = gjuha (the language).', 'middle', 'Ls')
    g += t(240, 266, 'This is typologically unusual in Europe \u2014 article comes AFTER the noun (like Romanian, Bulgarian, Scandinavian).', 'middle', 'Lx')
    g += t(240, 275, '5 cases: nominative, genitive, dative, accusative, ablative. Genitive = Dative in many paradigms.', 'middle', 'Lx')
    g += t(240, 284, '2 dialects: Gheg (north, Kosovo) and Tosk (south, standard). Differ in phonology and some morphology.', 'middle', 'Lx')
    g += hr(292)

    g += sh(300, 'ALBANIAN DEFINITE ARTICLE \u2014 SUFFIXED')
    alb_art = [
        ('Masc.', 'njeri (man)', 'njeriu (the man)', '-u suffix'),
        ('Fem.', 'gjuh\u00eb (language)', 'gjuha (the language)', '-a suffix'),
        ('Neut.', 'ujk (wolf)', 'ujku (the wolf)', '-u suffix'),
    ]
    for i, (gen, indef, defin, note) in enumerate(alb_art):
        y = 310 + i * 11
        g += t(55, y, gen, 'middle', 'Lx')
        g += t(150, y, indef, 'middle', 'Ls')
        g += t(280, y, defin, 'middle', 'Ls')
        g += t(390, y, note, 'middle', 'Lx')
    g += hr(348)

    g += sh(356, 'ALBANIAN VERB SYSTEM \u2014 flas (speak)')
    alb_verb = [
        ('flas', 'I speak'), ('flet', 'you speak'),
        ('flet', 'he/she speaks'), ('flasim', 'we speak'),
        ('flisni', 'you (pl) speak'), ('flasin', 'they speak'),
    ]
    for i, (form, gloss) in enumerate(alb_verb):
        col = i % 2; row = i // 2
        x = 80 + col * 220; y = 366 + row * 10
        g += t(x, y, form, 'middle', 'Ls')
        g += t(x + 70, y, gloss, 'middle', 'Lx')
    g += t(240, 399, 'Past: fola (I spoke). Future: do t\u00eb flas (will to speak \u2014 periphrastic). Negation: nuk flas.', 'middle', 'Lx')
    g += hr(407)

    g += sh(415, 'ALBANIAN CORE VOCABULARY')
    avocab = [
        ('uj\u00eb', 'water'), ('zjarr', 'fire'), ('tok\u00eb', 'earth'), ('njeri', 'person'),
        ('h\u00ebn\u00eb', 'moon'), ('kujtim', 'memory'), ('e ardhmja', 'future'), ('liri', 'freedom'),
        ('zem\u00ebr', 'heart'), ('dashuri', 'love'), ('bot\u00eb', 'world'), ('jet\u00eb', 'life'),
    ]
    for i, (alb, en) in enumerate(avocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 425 + row * 10
        g += t(x, y, alb, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')
    g += hr(470)

    g += sh(478, 'GRAMMAR BRIDGE \u2014 AN ISOLATED BRANCH')
    g += t(240, 488, 'Albanian has no close relatives in Indo-European. It shares the same ancestor but diverged early and completely.', 'middle', 'Ls')
    g += t(240, 497, 'Many Greek loanwords in Albanian: \u00ebsht\u00eb (is) \u2190 Greek \u03b5\u03c3\u03c4\u03af. Millennia of close geographic contact.', 'middle', 'Lx')

    g += footer('21', 'Greek', 'Albanian', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 21D ALT — TEXT ─────────────────────────────────────────────────────

def build_21d_alt():
    g = open_svg()
    g += t(240, 30, 'GREEK + ALBANIAN \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 21D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. HERACLITUS \u2014 ON CHANGE (~500 BCE)')
    g += t(240, 73, '\u03a0\u03ac\u03bd\u03c4\u03b1 \u03c1\u03b5\u03af. (Panta rhei.)', 'middle', 'Lg')
    g += t(240, 89, '"Everything flows." \u2014 Heraclitus of Ephesus. Oldest Greek philosophical fragment on change and time.', 'middle', 'Ls')
    g += hr(97)

    g += sh(105, 'II. PLATO \u2014 REPUBLIC (380 BCE)')
    g += t(240, 115, '\u0393\u03bd\u03ce\u03b8\u03b9 \u03c3\u03b5\u03b1\u03c5\u03c4\u03cc\u03bd. (Gnothi seauton.)', 'middle', 'Lg')
    g += t(240, 131, '"Know thyself." \u2014 Inscribed at Delphi; foundational principle of Greek philosophy and Western ethics.', 'middle', 'Ls')
    g += hr(139)

    g += sh(147, 'III. GREEK BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 159, '\u0391\u03c5\u03c4\u03cc \u03ad\u03b3\u03b9\u03bd\u03b5 \u03b3\u03b9\u03b1 \u03c3\u03ad\u03bd\u03b1, \u03b4\u03c9\u03c1\u03b5\u03ac\u03bd,', 'middle', 'Lg')
    g += t(240, 176, '\u03b1\u03c0\u03cc \u03b1\u03bd\u03b8\u03c1\u03ce\u03c0\u03bf\u03c5\u03c2 \u03c0\u03bf\u03c5 \u03b8\u03c5\u03bc\u03ae\u03b8\u03b7\u03ba\u03b1\u03bd \u03c4\u03bf \u03bc\u03ad\u03bb\u03bb\u03bf\u03bd.', 'middle', 'Lg')
    g += t(240, 193, 'This was-made for you  freely / by people who remembered the future.', 'middle', 'Lx')
    g += t(240, 202, '"This was made for you, freely, by people who remembered the future." (Greek)', 'middle', 'F')
    g += hr(210)

    g += sh(218, 'GREEK NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 228, '\u03bc\u03ad\u03bb\u03bb\u03bf\u03bd = future (from \u03bc\u03ad\u03bb\u03bb\u03c9, to be about to, to intend). \u03b8\u03c5\u03bc\u03ac\u03bc\u03b1\u03b9 = to remember (lit. to call to mind).', 'middle', 'Ls')
    g += t(240, 237, '\u03b4\u03c9\u03c1\u03b5\u03ac\u03bd = freely (adverb from \u03b4\u03ce\u03c1\u03bf = gift). Greek encodes free giving as gift-giving.', 'middle', 'Lx')

    g += sec_divider(247, 'SECONDARY \u2014 ALBANIAN (SHQIP) \u2014 RUNNING TEXT')

    g += sh(273, 'I. NAIM FRASH\u00cbRI \u2014 ALBANIAN POET (1846\u20131900)')
    g += t(240, 283, 'Shqip\u00ebria m\u00eb thirri, \u00eb dashur dhe e nder\u00ebshme,', 'middle', 'L')
    g += t(240, 294, 'Albania me called  beloved   and  honorable', 'middle', 'Lx')
    g += t(240, 303, '"Albania called to me, beloved and honorable." \u2014 Frash\u00ebri, father of Albanian national literature.', 'middle', 'F')
    g += hr(311)

    g += sh(319, 'II. ALBANIAN PROVERB \u2014 ON MEMORY AND KNOWLEDGE')
    g += t(240, 329, 'Ai q\u00eb nuk di t\u00eb lexoj\u00eb, \u00ebsht\u00eb i verb\u00ebr.', 'middle', 'L')
    g += t(240, 340, 'He who not can to-read   is   blind.', 'middle', 'Lx')
    g += t(240, 349, '"He who cannot read is blind." \u2014 Albanian proverb. Context: Albanian literacy campaigns 1940s\u20131980s.', 'middle', 'F')
    g += hr(357)

    g += sh(365, 'III. ALBANIAN BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 376, 'Kjo \u00ebsht\u00eb b\u00ebr\u00eb p\u00ebr ju, falas,', 'middle', 'L')
    g += t(240, 388, 'nga njer\u00ebz q\u00eb mbajt\u00ebn mend t\u00eb ardhmen.', 'middle', 'L')
    g += t(240, 400, 'This is   made for you  freely / by  people who kept   in-mind the future.', 'middle', 'Lx')
    g += t(240, 409, '"This was made for you, freely, by people who kept the future in mind." (Albanian)', 'middle', 'F')
    g += hr(417)

    g += sh(425, 'ALBANIAN NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 435, 'E ardhmja = the future (definite article e + ardhme from \u201carrive/come\u201d \u2014 the future as what is arriving).', 'middle', 'Ls')
    g += t(240, 444, 'Mbaj mend = to remember (lit. to keep/hold + mind). A bodylike metaphor \u2014 memory as something held.', 'middle', 'Ls')
    g += t(240, 453, 'Falas = freely/for free. Suffixed definite article in \u201ce ardhmja\u201d shows the postposed article system.', 'middle', 'Lx')
    g += hr(461)

    g += sh(469, 'LANGUAGE BRIDGE \u2014 AN ANCIENT NEIGHBORHOOD')
    g += t(240, 479, 'Greek: 3500+ year written tradition. Ancestor of Western alphabets. ~13M speakers.', 'middle', 'Ls')
    g += t(240, 488, 'Albanian: ~7.5M speakers. An isolated Indo-European branch \u2014 no close relatives. Ancient substrate.', 'middle', 'Ls')
    g += t(240, 497, 'Shared region for millennia: Greeks and Illyrians (Albanian ancestors) were neighbors in antiquity.', 'middle', 'Lx')
    g += t(240, 506, 'Albanian preserves features of ancient Balkan languages that Greek absorbed and replaced.', 'middle', 'Lx')

    g += footer('21', 'Greek', 'Albanian', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate21a_greek_albanian_script_alt.svg':    build_21a_alt(),
        'plate21b_greek_albanian_phonology_alt.svg': build_21b_alt(),
        'plate21c_greek_albanian_grammar_alt.svg':   build_21c_alt(),
        'plate21d_greek_albanian_text_alt.svg':      build_21d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
