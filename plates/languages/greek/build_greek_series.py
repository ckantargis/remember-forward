#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Greek plate series 21A–21D for Remember Forward."""

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
        '  .Lg { font-size:10px; }\n'
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


# ─── PLATE 21A — SCRIPT ──────────────────────────────────────────────────────

def build_21a():
    g = open_svg()
    g += t(240, 32, 'GREEK — SCRIPT · ALPHABET · HISTORY', 'middle', 'T')
    g += t(240, 50, 'SERIES 21A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(67, 'THE GREEK ALPHABET — 24 LETTERS')
    g += t(240, 76, 'The Greek alphabet (c. 800 BCE) is the ancestor of Latin, Cyrillic, Coptic, Gothic, and Armenian scripts.', 'middle', 'Ls')
    g += t(240, 84, 'First alphabet to systematically represent vowels — adapted from Phoenician consonantal abjad.', 'middle', 'Ls')

    # Full alphabet table: uppercase, lowercase, name, transliteration, IPA (ancient/modern)
    alphabet = [
        ('Α', 'α', 'Alpha',   'A',  '/a, aː/  →  /a/'),
        ('Β', 'β', 'Beta',    'B',  '/b/      →  /v/'),
        ('Γ', 'γ', 'Gamma',   'G',  '/ɡ/      →  /ɣ/ or /j/'),
        ('Δ', 'δ', 'Delta',   'D',  '/d/      →  /ð/'),
        ('Ε', 'ε', 'Epsilon', 'E',  '/e/      →  /e/'),
        ('Ζ', 'ζ', 'Zeta',    'Z',  '/zd/ or /dz/ →  /z/'),
        ('Η', 'η', 'Eta',     'Ē',  '/ɛː/     →  /i/'),
        ('Θ', 'θ', 'Theta',   'Th', '/tʰ/     →  /θ/'),
        ('Ι', 'ι', 'Iota',    'I',  '/i, iː/  →  /i/'),
        ('Κ', 'κ', 'Kappa',   'K',  '/k/      →  /k/'),
        ('Λ', 'λ', 'Lambda',  'L',  '/l/      →  /l/'),
        ('Μ', 'μ', 'Mu',      'M',  '/m/      →  /m/'),
        ('Ν', 'ν', 'Nu',      'N',  '/n/      →  /n/'),
        ('Ξ', 'ξ', 'Xi',      'X',  '/ks/     →  /ks/'),
        ('Ο', 'ο', 'Omicron', 'O',  '/o/      →  /o/'),
        ('Π', 'π', 'Pi',      'P',  '/p/      →  /p/'),
        ('Ρ', 'ρ', 'Rho',     'R',  '/r/      →  /r/'),
        ('Σ', 'σ/ς','Sigma',  'S',  '/s/      →  /s/'),
        ('Τ', 'τ', 'Tau',     'T',  '/t/      →  /t/'),
        ('Υ', 'υ', 'Upsilon', 'Y/U','/y, yː/  →  /i/'),
        ('Φ', 'φ', 'Phi',     'Ph', '/pʰ/     →  /f/'),
        ('Χ', 'χ', 'Chi',     'Ch', '/kʰ/     →  /x/ or /ç/'),
        ('Ψ', 'ψ', 'Psi',     'Ps', '/ps/     →  /ps/'),
        ('Ω', 'ω', 'Omega',   'Ō',  '/ɔː/     →  /o/'),
    ]

    # 4-column layout with 6 letters per column group
    col_groups = [alphabet[i:i+6] for i in range(0, 24, 6)]
    cx_starts = [22, 142, 262, 382]
    for ci, (group, cx) in enumerate(zip(col_groups, cx_starts)):
        for ri, (uc, lc, name, translit, ipa) in enumerate(group):
            y = 96 + ri * 19
            g += t(cx, y, uc, 'middle', 'Lg')
            g += t(cx + 12, y, lc, 'middle', 'Lg')
            g += t(cx + 30, y - 3, name, 'middle', 'Lx')
            g += t(cx + 30, y + 4, translit, 'middle', 'Lx')
            g += t(cx + 72, y, ipa, 'middle', 'Lx')

    g += t(240, 213, 'σ is used medially; ς is used only in word-final position.  Σίγμα = Sigma (example).', 'middle', 'Lx')
    g += hr(220)

    # Historical development
    g += sh(228, 'HISTORICAL DEVELOPMENT FROM PHOENICIAN')
    hist = [
        ('Aleph → Alpha Α', 'Phoenician ox-head (\\u05d0) → Greek vowel A'),
        ('Beth → Beta Β', 'Phoenician house → Greek B (reversed in early forms)'),
        ('Gimel → Gamma Γ', 'Phoenician camel → Greek G (later became Latin C, G)'),
        ('Daleth → Delta Δ', 'Phoenician door → Greek Δ (triangle form)'),
        ('He → Epsilon Ε', 'Phoenician window → Greek vowel E'),
        ('Yodh → Iota Ι', 'Phoenician hand → Greek vowel I (most-used letter)'),
    ]
    for i, (phoen, note) in enumerate(hist):
        y = 238 + i * 12
        g += t(130, y, phoen, 'middle', 'Ls')
        g += t(340, y, note, 'middle', 'Lx')
    g += t(240, 315, 'Phoenician script (c. 1050 BCE) was abjad (consonants only). Greeks added vowel letters ~800 BCE.', 'middle', 'Lx')
    g += hr(323)

    # Ancient vs modern
    g += sh(331, 'ANCIENT vs. MODERN PRONUNCIATION — KEY CHANGES')
    changes = [
        ('Β β', 'Ancient /b/ → Modern /v/', 'βήτα: "beta" → "vita"'),
        ('Δ δ', 'Ancient /d/ → Modern /ð/', 'δέλτα: "delta" → "thelta"'),
        ('Η η', 'Ancient /ɛː/ (long e) → Modern /i/', 'ήτα: sounds like "ee"'),
        ('Θ θ', 'Ancient /tʰ/ (aspirated t) → Modern /θ/', 'θ: like English "th" in "thin"'),
        ('Υ υ', 'Ancient /y/ (front rounded) → Modern /i/', 'ύψιλον: now = "ee"'),
        ('Φ φ', 'Ancient /pʰ/ (aspirated p) → Modern /f/', 'φ: now = "f"'),
        ('Χ χ', 'Ancient /kʰ/ (aspirated k) → Modern /x/', 'χ: like German "ch" in "Bach"'),
        ('ΟΙ/ΕΙ/ΥΙ', 'Ancient diphthongs → Modern /i/', 'iotacism: many spellings → /i/ sound'),
    ]
    for i, (letter, change, note) in enumerate(changes):
        y = 341 + i * 12
        g += t(45, y, letter, 'middle', 'Ls')
        g += t(175, y, change, 'middle', 'Lx')
        g += t(370, y, note, 'middle', 'Lx')
    g += hr(440)

    # Greek numerals
    g += sh(448, 'GREEK NUMERALS — ALPHABETIC SYSTEM')
    g += t(240, 457, 'Ancient Greeks used letters as numerals (iota-style). Three archaic letters added: digamma (6), koppa (90), sampi (900).', 'middle', 'Lx')
    nums = [
        ('α=1','β=2','γ=3','δ=4','ε=5','ϛ=6','ζ=7','η=8','θ=9'),
        ('ι=10','κ=20','λ=30','μ=40','ν=50','ξ=60','ο=70','π=80','ϟ=90'),
        ('ρ=100','σ=200','τ=300','υ=400','φ=500','χ=600','ψ=700','ω=800','ϡ=900'),
    ]
    for ri, row in enumerate(nums):
        for ci, cell in enumerate(row):
            g += t(30 + ci * 50, 467 + ri * 11, cell, 'middle', 'Lx')
    g += t(240, 503, 'Thousands: ͵α = 1000, ͵β = 2000 (lower comma prefix). Myriad (M) = 10,000.', 'middle', 'Lx')
    g += hr(511)

    # Diacritics
    g += sh(519, 'DIACRITICS — ANCIENT POLYTONIC SYSTEM')
    g += t(240, 529, 'Ancient Greek uses BREATHING MARKS and ACCENT marks. Modern Greek (1982+) uses monotonic (single accent only).', 'middle', 'Lx')
    diacritics = [
        ('ἁ (rough breathing)', 'h-sound before vowel: ἡ hē (or)'),
        ('ἀ (smooth breathing)', 'no h-sound: ἐ e'),
        ('ά (acute accent)', 'high pitch on that syllable'),
        ('ὰ (grave accent)', 'falling or secondary stress'),
        ('ᾶ (circumflex)', 'rise-fall pitch (long vowels)'),
        ('ᾳ (iota subscript)', 'historical /j/ written under long vowels'),
    ]
    for i, (mark, desc) in enumerate(diacritics):
        y = 539 + i * 11
        g += t(115, y, mark, 'middle', 'Ls')
        g += t(330, y, desc, 'middle', 'Lx')

    g += footer('21', 'Greek', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 21B — PHONOLOGY ───────────────────────────────────────────────────

def build_21b():
    g = open_svg()
    g += t(240, 32, 'GREEK — PHONOLOGY · ANCIENT AND MODERN', 'middle', 'T')
    g += t(240, 50, 'SERIES 21B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(67, 'TWO SYSTEMS — ANCIENT ATTIC AND MODERN GREEK')
    g += t(240, 77, 'Ancient Greek (Attic dialect, c. 5th–4th BCE) and Modern Greek (Demotic, post-1976) differ substantially.', 'middle', 'L')
    g += t(240, 87, 'Ancient: pitch accent, vowel quantity distinctions, aspirated stops, front-rounded vowel /y/.', 'middle', 'Ls')
    g += t(240, 96, 'Modern: stress accent, all vowels simplified, spirantized stops, iotacism (η υ ει οι → /i/).', 'middle', 'Ls')
    g += hr(104)

    # Vowel comparison
    g += sh(112, 'VOWEL SYSTEMS — ANCIENT (ATTIC) vs MODERN')
    g += t(130, 121, 'Letter', 'middle', 'Lx')
    g += t(220, 121, 'Ancient IPA', 'middle', 'Lx')
    g += t(310, 121, 'Modern IPA', 'middle', 'Lx')
    g += t(410, 121, 'Note', 'middle', 'Lx')
    vowel_comp = [
        ('α Α',   '/a/ short, /aː/ long',   '/a/',    'unchanged'),
        ('ε Ε',   '/e/ short',              '/e/',    'unchanged'),
        ('η Η',   '/ɛː/ long e',            '/i/',    'iotacism — sounds like "ee"'),
        ('ι Ι',   '/i/ short, /iː/ long',   '/i/',    'unchanged'),
        ('ο Ο',   '/o/ short',              '/o/',    'unchanged'),
        ('υ Υ',   '/y/ short, /yː/ long',   '/i/',    'front-rounded → iotacism'),
        ('ω Ω',   '/ɔː/ long o',            '/o/',    'merged with omicron'),
        ('ει',    '/eː/ long e',            '/i/',    'diphthong → iotacism'),
        ('οι',    '/oi/ diphthong',         '/i/',    'merged to /i/'),
        ('αι',    '/ai/ diphthong',         '/e/',    'simplified'),
        ('αυ',    '/au/ diphthong',         '/av/ or /af/','context-dependent'),
        ('ευ',    '/eu/ diphthong',         '/ev/ or /ef/','context-dependent'),
    ]
    for i, (ltr, anc, mod, note) in enumerate(vowel_comp):
        y = 131 + i * 12
        g += t(60, y, ltr, 'middle', 'Ls')
        g += t(180, y, anc, 'middle', 'Lx')
        g += t(290, y, mod, 'middle', 'Lx')
        g += t(405, y, note, 'middle', 'Lx')
    g += hr(279)

    # Consonant comparison
    g += sh(287, 'CONSONANT CHANGES — ANCIENT TO MODERN')
    cons_change = [
        ('β', '/b/', '/v/', 'spirantization — bilabial stop → labiodental fric.'),
        ('γ', '/ɡ/', '/ɣ/ or /j/', 'velar stop → voiced velar/palatal fricative'),
        ('δ', '/d/', '/ð/', 'dental stop → dental fricative (like English "the")'),
        ('ζ', '/zd/ or /dz/', '/z/', 'simplified to simple fricative'),
        ('θ', '/tʰ/', '/θ/', 'aspirated stop → voiceless dental fricative'),
        ('φ', '/pʰ/', '/f/', 'aspirated stop → labiodental fricative'),
        ('χ', '/kʰ/', '/x/ or /ç/', 'aspirated stop → velar/palatal fricative'),
        ('π,τ,κ', '/p t k/', '/p t k/', 'voiceless stops — UNCHANGED'),
        ('μπ,ντ,γκ', '—', '/b d ɡ/', 'modern voiced stops formed by clusters'),
    ]
    for i, (ltr, anc, mod, note) in enumerate(cons_change):
        y = 297 + i * 12
        g += t(40, y, ltr, 'middle', 'Ls')
        g += t(90, y, anc, 'middle', 'Lx')
        g += t(145, y, mod, 'middle', 'Lx')
        g += t(330, y, note, 'middle', 'Lx')
    g += hr(410)

    # Breathing marks
    g += sh(418, 'BREATHING MARKS — ANCIENT POLYTONIC')
    g += t(240, 428, 'Every ancient Greek word beginning with a vowel carries a breathing mark.', 'middle', 'L')
    g += t(240, 437, 'Rough breathing (ἁ ἐ ἱ ὁ ὑ): a preceding /h/ sound — ἡμέρα hēméra (day).', 'middle', 'Ls')
    g += t(240, 446, 'Smooth breathing (ἀ ἐ ἰ ὀ): no /h/ — ἀνήρ anēr (man).', 'middle', 'Ls')
    g += t(240, 455, 'Rho at word start always carries rough breathing: ῥήτωρ rhētor (orator, root of "rhetoric").', 'middle', 'Ls')
    g += t(240, 464, 'Modern Greek: breathing marks abolished in 1982 reform (monotonic orthography).', 'middle', 'Ls')
    g += hr(472)

    # Pitch accent
    g += sh(480, 'PITCH ACCENT — ANCIENT GREEK')
    g += t(240, 490, 'Ancient Greek had lexical PITCH accent: syllables were high (acute ´) or low (grave `) or both (circumflex ˆ).', 'middle', 'Ls')
    g += t(240, 499, 'The circumflex (ᾶ) could only appear on long vowels/diphthongs: a rising-then-falling tone.', 'middle', 'Ls')
    g += t(240, 508, 'Three-syllable rule: accent cannot fall more than 3 syllables from the end of the word.', 'middle', 'Ls')
    g += t(240, 517, 'Example: ἄνθρωπος ánthrōpos (human being) — accent on first syllable, acute.', 'middle', 'Ls')
    g += t(240, 526, 'Modern Greek: stress accent replaces pitch — one stressed syllable, marked with ά έ ή ί ό ύ ώ.', 'middle', 'Ls')
    g += hr(534)

    # Modern phoneme inventory
    g += sh(542, 'MODERN GREEK PHONEME INVENTORY')
    g += t(240, 552, 'Vowels: /a e i o u/ — 5 vowels (iotacism collapsed many distinctions).', 'middle', 'Ls')
    g += t(240, 561, 'Consonants: /p b t d k ɡ f v θ ð s z ʃ x ɣ m n ɲ l r j/', 'middle', 'Ls')
    g += t(240, 570, 'Note /b d ɡ/ are written μπ ντ γκ/γγ respectively (e.g., μπαμπάς bampas = dad).', 'middle', 'Ls')
    g += t(240, 579, 'Geminate consonants: not phonemic in Modern Greek (simplified from ancient forms).', 'middle', 'Ls')
    g += t(240, 588, 'Stress: always marked in writing (except monosyllables). Position is lexically unpredictable.', 'middle', 'Ls')

    g += footer('21', 'Greek', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 21C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_21c():
    g = open_svg()
    g += t(240, 32, 'GREEK — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 21C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(67, 'INFLECTED LANGUAGE — CASES, GENDERS, VERB SYSTEM')
    g += t(240, 77, 'Greek is HIGHLY INFLECTED: nouns, adjectives, and verbs all change their endings.', 'middle', 'L')
    g += t(240, 87, 'Modern Greek: 4 cases (nominative, genitive, accusative, vocative). Ancient Greek: +dative (5).', 'middle', 'Ls')
    g += t(240, 96, '3 grammatical genders: masculine (ο), feminine (η), neuter (το). Articles indicate class.', 'middle', 'Ls')
    g += hr(104)

    # Definite article
    g += sh(112, 'DEFINITE ARTICLE — THE KEY TO NOUN CLASS')
    g += t(240, 121, 'The definite article agrees with gender and case. Masculine/Feminine/Neuter:')
    art_data = [
        ('Case', 'Masc.', 'Fem.', 'Neut.', 'Masc.PL', 'Fem.PL', 'Neut.PL'),
        ('Nominative', 'ο', 'η', 'το', 'οι', 'οι', 'τα'),
        ('Genitive', 'του', 'της', 'του', 'των', 'των', 'των'),
        ('Accusative', 'τον', 'την', 'το', 'τους', 'τις', 'τα'),
        ('Vocative', '—', '—', '—', '—', '—', '—'),
    ]
    col_art = [30, 100, 155, 210, 265, 330, 400]
    for ri, row in enumerate(art_data):
        for ci, cell in enumerate(row):
            y = 131 + ri * 13
            c = 'Lx' if ri == 0 else 'Ls'
            g += t(col_art[ci], y, cell, 'middle', c)
    g += hr(200)

    # Verb conjugation
    g += sh(208, 'VERB CONJUGATION — PRESENT ACTIVE (λύω / λύνω — "to free/solve")')
    g += t(240, 217, 'Ancient Greek (Attic)  vs  Modern Greek — present active indicative', 'middle', 'Ls')

    verb_data = [
        ('1sg', 'λύω', 'lýō', 'λύνω', 'líno', 'I free/solve'),
        ('2sg', 'λύεις', 'lýeis', 'λύνεις', 'líneis', 'you free'),
        ('3sg', 'λύει', 'lýei', 'λύνει', 'línei', 'he/she frees'),
        ('1pl', 'λύομεν', 'lýomen', 'λύνουμε', 'línoume', 'we free'),
        ('2pl', 'λύετε', 'lýete', 'λύνετε', 'línete', 'you (pl) free'),
        ('3pl', 'λύουσι(ν)', 'lýousi', 'λύνουν', 'línoun', 'they free'),
    ]
    col_v = [30, 100, 160, 230, 295, 390]
    g += t(col_v[0], 228, 'Person', 'middle', 'Lx')
    g += t(col_v[1], 228, 'Ancient', 'middle', 'Lx')
    g += t(col_v[2], 228, 'Translit.', 'middle', 'Lx')
    g += t(col_v[3], 228, 'Modern', 'middle', 'Lx')
    g += t(col_v[4], 228, 'Translit.', 'middle', 'Lx')
    g += t(col_v[5], 228, 'Meaning', 'middle', 'Lx')
    for ri, (prs, anc, at, mod, mt, gloss) in enumerate(verb_data):
        y = 238 + ri * 13
        g += t(col_v[0], y, prs, 'middle', 'Lx')
        g += t(col_v[1], y, anc, 'middle', 'Ls')
        g += t(col_v[2], y, at, 'middle', 'Lx')
        g += t(col_v[3], y, mod, 'middle', 'Ls')
        g += t(col_v[4], y, mt, 'middle', 'Lx')
        g += t(col_v[5], y, gloss, 'middle', 'Lx')
    g += hr(320)

    # Noun declension sample
    g += sh(328, 'NOUN DECLENSION — ANCIENT: ἄνθρωπος (HUMAN BEING, MASC.)')
    decl_data = [
        ('Nom.', 'ἄνθρωπος', 'anthrōpos', 'the human being (subject)'),
        ('Gen.', 'ἀνθρώπου', 'anthrōpou', 'of the human being'),
        ('Dat.', 'ἀνθρώπῳ', 'anthrōpōi', 'to/for the human being'),
        ('Acc.', 'ἄνθρωπον', 'anthrōpon', 'the human being (object)'),
        ('Voc.', 'ἄνθρωπε', 'anthrōpe', 'O human being! (address)'),
    ]
    for i, (case, greek, translit, gloss) in enumerate(decl_data):
        y = 338 + i * 12
        g += t(40, y, case, 'middle', 'Lx')
        g += t(110, y, greek, 'middle', 'Ls')
        g += t(195, y, translit, 'middle', 'Lx')
        g += t(360, y, gloss, 'middle', 'Lx')
    g += hr(402)

    # Core vocabulary
    g += sh(410, 'CORE VOCABULARY — 25 WORDS (MODERN GREEK)')
    vocab_gr = [
        ('ναι / όχι', 'nai / óchi', 'yes / no'),
        ('ευχαριστώ', 'efcharistó', 'thank you'),
        ('παρακαλώ / συγγνώμη', 'parakaló / sygnómi', 'please / sorry'),
        ('εγώ / εσύ', 'egó / esý', 'I / you'),
        ('αυτός / αυτή', 'aftós / aftí', 'he / she'),
        ('εδώ / εκεί', 'edó / ekéi', 'here / there'),
        ('που', 'pou', 'where / who'),
        ('τι', 'ti', 'what'),
        ('πότε', 'póte', 'when'),
        ('γιατί', 'giati', 'why'),
        ('νερό', 'neró', 'water'),
        ('φαγητό', 'fagitó', 'food'),
        ('άνθρωπος', 'ánthrōpos', 'human being'),
        ('σπίτι', 'spíti', 'house/home'),
        ('δρόμος', 'drómos', 'road/way'),
        ('ημέρα / νύχτα', 'iméra / níchta', 'day / night'),
        ('βιβλίο', 'vivlío', 'book'),
        ('γλώσσα', 'glóssa', 'language/tongue'),
        ('κόσμος', 'kósmos', 'world/cosmos'),
        ('αγάπη', 'agápi', 'love'),
        ('μεγάλος / μικρός', 'megálos / mikrós', 'big / small'),
        ('καλός / κακός', 'kalós / kakós', 'good / bad'),
        ('νέος / παλιός', 'néos / palios', 'new / old'),
        ('μέλλον', 'méllon', 'future (neut. noun)'),
        ('θυμάμαι / θυμούμαι', 'thimámai', 'I remember'),
    ]
    for i, (gr, translit, eng) in enumerate(vocab_gr):
        col = i % 2
        row = i // 2
        cx = 80 if col == 0 else 320
        y = 420 + row * 12
        g += t(cx, y, gr, 'middle', 'Ls')
        g += t(cx + 100, y, translit, 'middle', 'Lx')
        g += t(cx + 170, y, eng, 'middle', 'Lx')

    yl = 420 + 13 * 12 + 4
    g += hr(yl)
    g += sh(yl + 8, 'WORD ORDER AND SYNTAX')
    g += t(240, yl + 18, 'Greek word order is flexible (due to inflection indicating roles) but SVO is most common.', 'middle', 'Ls')
    g += t(240, yl + 27, 'The famous Greek copula: είμαι (I am) — Είμαι άνθρωπος. "I am a human being."', 'middle', 'Ls')

    g += footer('21', 'Greek', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 21D — RUNNING TEXT ─────────────────────────────────────────────────

def build_21d():
    g = open_svg()
    g += t(240, 32, 'GREEK — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 21D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1 — Homer
    g += sh(67, 'PASSAGE 1 — HOMER, ILIAD I.1 (c. 8th BCE)')
    g += t(240, 77, 'Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος', 'middle', 'Lg')
    g += t(240, 89, 'Mēnin áeide theà Pēlēiádeō Achilēos', 'middle', 'Lx')
    g += t(240, 97, 'Rage    sing   goddess  of-Peleus\'s-son  of-Achilles', 'middle', 'Lx')
    g += t(240, 105, '"Sing, goddess, the rage of Achilles son of Peleus"  — opening line of Western literature', 'middle', 'Ls')
    g += hr(113)

    # Passage 2 — Plato
    g += sh(121, 'PASSAGE 2 — PLATO, APOLOGY 38A (c. 399 BCE)')
    g += t(240, 131, 'ὁ δὲ ἀνεξέταστος βίος οὐ βιωτὸς ἀνθρώπῳ', 'middle', 'Lg')
    g += t(240, 143, 'ho dè anexétastos bíos ou biōtòs anthrōpōi', 'middle', 'Lx')
    g += t(240, 151, 'the but unexamined  life not livable  for-human', 'middle', 'Lx')
    g += t(240, 159, '"The unexamined life is not worth living for a human being."  — Socrates (via Plato)', 'middle', 'Ls')
    g += hr(167)

    # Passage 3 — New Testament
    g += sh(175, 'PASSAGE 3 — JOHN 1:1, NEW TESTAMENT GREEK (c. 90–100 CE)')
    g += t(240, 185, 'Ἐν ἀρχῇ ἦν ὁ Λόγος, καὶ ὁ Λόγος ἦν πρὸς τὸν Θεόν', 'middle', 'Lg')
    g += t(240, 197, 'En archēi  ēn  ho Lógos, kaì  ho Lógos  ēn  pròs  tòn  Theón', 'middle', 'Lx')
    g += t(240, 205, 'In beginning was the Word,  and the Word   was toward the  God', 'middle', 'Lx')
    g += t(240, 213, '"In the beginning was the Word, and the Word was with God."  — Koine Greek', 'middle', 'Ls')
    g += hr(221)

    # Passage 4 — Modern
    g += sh(229, 'PASSAGE 4 — GREEK NATIONAL ANTHEM, FIRST STANZA (1823, SOLOMOS)')
    g += t(240, 239, 'Σε γνωρίζω από την κόψη', 'middle', 'Lg')
    g += t(240, 249, 'Se gnorízo apó tin kópsi', 'middle', 'Lx')
    g += t(240, 257, 'You I-recognize from the edge', 'middle', 'Lx')
    g += t(240, 267, 'του σπαθιού την τρομερή,', 'middle', 'Lg')
    g += t(240, 277, 'tou spathioú tin tromerí,', 'middle', 'Lx')
    g += t(240, 285, 'of the-sword the terrible,', 'middle', 'Lx')
    g += t(240, 295, '"I know you by the fearsome edge of your sword" — Hymn to Liberty, Dionysios Solomos', 'middle', 'Ls')
    g += hr(303)

    # Bridge phrase
    g += sh(311, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 323, 'Αυτό φτιάχτηκε για σένα, ελεύθερα, από ανθρώπους που θυμήθηκαν το μέλλον.', 'middle', 'Lg')
    g += t(240, 337, 'Aftó ftiáchtike gia séna, eléfthera, apó anthrópous pou thimíthikan to méllon.', 'middle', 'Lx')
    g += t(240, 345, 'This was-made   for you,  freely,    from people       who remembered    the future.', 'middle', 'Lx')
    g += t(240, 353, '"This was made for you, freely, by people who remembered the future."', 'middle', 'Ls')
    g += hr(361)

    # Language note
    g += sh(369, 'LANGUAGE NOTE — "FUTURE" IN GREEK')
    g += t(240, 379, 'μέλλον (méllon): "the future" — from μέλλω (méllo) "to be about to, to intend."', 'middle', 'L')
    g += t(240, 389, 'The future is literally "what is about to happen" — a participial noun from the verb of intention.', 'middle', 'Ls')
    g += t(240, 399, 'θυμήθηκαν (thimíthikan): 3rd person plural aorist passive of θυμάμαι (remember) — "they remembered."', 'middle', 'Ls')
    g += t(240, 408, 'ελεύθερα (eléfthera): adverb from ελεύθερος (free) — root of "Eleutherios", freedom, liberty.', 'middle', 'Ls')
    g += t(240, 417, 'ελεύθερος shares roots with German "lieb" and English "love" — Proto-Indo-European *leudʰ-.', 'middle', 'Ls')
    g += t(240, 426, 'ἄνθρωπος / άνθρωπος (anthrōpos): "human being" — root of anthropology, philanthropy, misanthropy.', 'middle', 'Ls')
    g += hr(434)

    # Timeline of Greek
    g += sh(442, 'TIMELINE OF THE GREEK LANGUAGE')
    timeline = [
        ('~1500 BCE', 'Mycenaean Greek — Linear B syllabary (not alphabet)'),
        ('~800 BCE', 'Archaic Greek — first alphabetic inscriptions, Homer'),
        ('~500–300 BCE', 'Classical Greek — Attic dialect: Plato, Aristotle, Sophocles'),
        ('~300 BCE–300 CE', 'Hellenistic Koine — Alexander\'s empire lingua franca; New Testament'),
        ('~300–1453 CE', 'Byzantine Greek — Eastern Roman Empire; Orthodox liturgy'),
        ('1453–1830', 'Early Modern Greek — Ottoman period; diglossia begins'),
        ('1830–1976', 'Katharevousa — purist form (official); Demotic (spoken)'),
        ('1976–present', 'Modern Standard (Demotic) — official; monotonic orthography from 1982'),
    ]
    for i, (era, note) in enumerate(timeline):
        y = 452 + i * 12
        g += t(95, y, era, 'middle', 'Ls')
        g += t(320, y, note, 'middle', 'Lx')
    g += hr(550)

    # Decoding note
    g += sh(558, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 568, 'The 24 Greek letters and their sounds are given on Plate 21A. Read left to right, top to bottom.', 'middle', 'Ls')
    g += t(240, 577, 'Modern Greek has 5 vowel sounds: α=/a/ ε=/e/ η υ ει οι=/i/ ο ω=/o/ ου=/u/. Mostly phonemic.', 'middle', 'Ls')
    g += t(240, 586, 'Greek gave us: democracy, philosophy, alphabet, history, theatre, cosmos, and ~30% of English.', 'middle', 'Ls')

    g += footer('21', 'Greek', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate21a_greek_script.svg': build_21a(),
        'plate21b_greek_phonology.svg': build_21b(),
        'plate21c_greek_grammar.svg': build_21c(),
        'plate21d_greek_text.svg': build_21d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
