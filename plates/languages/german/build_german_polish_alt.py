#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build German / Polish alt plate series 52A–52D for Remember Forward.
Secondary language: Polish (język polski) — largest Slavic language within
~500 miles of German geographic center (roughly central Germany / Leipzig area).
~45 million native speakers. West Slavic, 7 noun cases, rich consonant clusters.
Geographic basis: Poland directly borders Germany; Warsaw ~800km from Berlin,
Wrocław/Breslau just 350km — well within 500mi.
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


# ─── PLATE 52A ALT — SCRIPT ───────────────────────────────────────────────────

def build_52a_alt():
    g = open_svg()
    g += t(240, 30, 'GERMAN + POLISH \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 52A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'GERMAN \u2014 LATIN ALPHABET \u00b7 26 + 4 SPECIAL CHARACTERS')
    g += t(240, 73, 'German uses 26 standard Latin letters plus 4 special characters: \u00e4 \u00f6 \u00fc (umlauts) and \u00df (Eszett/sharp-s).', 'middle', 'Ls')
    g += t(240, 82, 'Eszett (\u00df): represents /ss/ in native German words: Stra\u00dfe (street), wei\u00df (white). Uppercase: SS or \u1e9e.', 'middle', 'Lx')
    g += t(240, 91, 'Umlaut vowels: \u00e4 /\u025b/ like air \u00b7 \u00f6 /\u00f8/ like French eu \u00b7 \u00fc /y/ like French u.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'GERMAN ALPHABET \u2014 ALL 26 + 4')
    alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z \u00c4 \u00d6 \u00dc \u1e9e'
    g += t(240, 117, alpha, 'middle', 'Ls')
    g += hr(124)

    g += sh(132, 'GERMAN DIGRAPHS AND SPELLING CONVENTIONS')
    digraphs = [
        ('sch', '/\u0283/', 'Schule (school), waschen (wash)'),
        ('ch', '/x/ or /\u00e7/', 'Buch /bux/ (book), ich /\u026a\u00e7/ (I)'),
        ('sp / st', '/\u0283p/ /\u0283t/', 'Sprechen (speak), Stunde (hour) \u2014 word-initial'),
        ('ei', '/a\u026a/', 'Stein (stone), Wein (wine)'),
        ('eu / \u00e4u', '/\u0254\u028f/', 'Europa, H\u00e4user (houses)'),
        ('ie', '/i\u02d0/', 'lieb (dear), Brief (letter)'),
        ('qu', '/kv/', 'Quelle (source) \u2014 not /kw/ as in English'),
    ]
    for i, (dg, ipa, ex) in enumerate(digraphs):
        y = 142 + i * 11
        g += t(55, y, dg, 'middle', 'Ls')
        g += t(130, y, ipa, 'middle', 'Lx')
        g += t(330, y, ex, 'middle', 'Lx')
    g += hr(222)

    g += sh(230, 'GERMAN CAPITALIZATION')
    g += t(240, 240, 'ALL NOUNS are capitalized in German: der Mensch (the person), das Wasser (the water), die Freiheit (freedom).', 'middle', 'Ls')
    g += t(240, 249, 'This rule applies universally \u2014 a major orthographic distinction from all other European languages.', 'middle', 'Lx')
    g += t(240, 258, 'Adjectives and verbs NOT capitalized: Das Wasser ist kalt. (The water is cold.)', 'middle', 'Lx')

    g += sec_divider(268, 'SECONDARY \u2014 POLISH (J\u0118ZYK POLSKI) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(294, 'POLISH \u2014 LATIN ALPHABET \u00b7 32 LETTERS')
    g += t(240, 304, 'Polish uses 32 letters: standard 26 Latin + 9 diacritic letters.', 'middle', 'Ls')
    special = '\u0105 \u0107 \u0119 \u0142 \u0144 \u00f3 \u015b \u017a \u017c'
    g += t(240, 314, f'Special letters: {special}', 'middle', 'Ls')
    g += hr(321)

    g += sh(329, 'POLISH DIACRITICS \u2014 9 SPECIAL LETTERS')
    pl_diac = [
        ('\u0105', 'a with ogonek', '/\u0254\u0303/ or /\u0254/ \u2014 nasal a: m\u0105\u017c (husband), r\u0119ka (hand)'),
        ('\u0107', 'c with acute', '/t\u0255\u02b2/ soft c: czy (whether), \u0107ma (moth)'),
        ('\u0119', 'e with ogonek', '/\u025b/ or /\u025b\u0303/: jeden (one), si\u0119 (oneself)'),
        ('\u0142', 'l with stroke', '/w/ \u2014 sounds like English w: \u0142adny (pretty), z\u0142oty (gold)'),
        ('\u0144', 'n with acute', '/\u0272/ soft n: ko\u0144 (horse), nie (no)'),
        ('\u00f3', 'o with acute', '/u/ historically long o: m\u00f3j (my), k\u00f3\u0142 (wheels)'),
        ('\u015b', 's with acute', '/\u0255/ soft s: \u015bwiat (world), \u015brodek (center)'),
        ('\u017a', 'z with acute', '/\u0292\u02b2/ soft z: \u017a\u00f3\u0142w (turtle), \u017areni (sated)'),
        ('\u017c', 'z with dot', '/\u0292/ like French j: \u017cy\u0107 (to live), r\u00f3\u017ca (rose)'),
    ]
    for i, (ch, name, desc) in enumerate(pl_diac):
        y = 339 + i * 10
        g += t(42, y, ch, 'middle', 'Ls')
        g += t(120, y, name, 'middle', 'Lx')
        g += t(330, y, desc, 'middle', 'Lx')
    g += hr(435)

    g += sh(443, 'POLISH DIGRAPHS AND CLUSTERS')
    pl_dg = [
        ('cz', '/t\u0283/', 'Czech, czarny (black)'),
        ('sz', '/\u0283/', 'szko\u0142a (school), szary (grey)'),
        ('dz', '/dz/', 'dzban (jug), ojdzie (uncle)'),
        ('d\u017c', '/d\u0292/', 'd\u017cungla (jungle), d\u017cem (jam)'),
        ('rz', '/\u0292/', 'rzeka (river) \u2014 historically /r\u02b2/'),
        ('szcz', '/\u0283t\u0283/', 'szcz\u0119\u015bcie (happiness/luck)'),
    ]
    for i, (dg, ipa, ex) in enumerate(pl_dg):
        y = 453 + i * 10
        g += t(55, y, dg, 'middle', 'Ls')
        g += t(130, y, ipa, 'middle', 'Lx')
        g += t(310, y, ex, 'middle', 'Lx')

    g += footer('52', 'German', 'Polish', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 52B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_52b_alt():
    g = open_svg()
    g += t(240, 30, 'GERMAN + POLISH \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 52B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'GERMAN VOWELS \u2014 LONG/SHORT PAIRS + UMLAUTS')
    g += t(240, 73, 'German has phonemic vowel length: short vs. long vowels are contrastive.', 'middle', 'Ls')
    gv = [
        ('/a/ vs /a\u02d0/', 'Mann (man) vs. Bahn (track)'),
        ('/\u026a/ vs /i\u02d0/', 'mit (with) vs. miet (rent)'),
        ('/\u028a/ vs /u\u02d0/', 'und (and) vs. Hut (hat)'),
        ('/\u025b/ vs /e\u02d0/', 'Bett (bed) vs. Beet (flowerbed)'),
        ('/\u0254/ vs /o\u02d0/', 'Gott (God) vs. Boot (boat)'),
        ('/\u00f8/ vs /\u00f8\u02d0/', 'H\u00f6lle (hell) vs. H\u00f6hle (cave)'),
        ('/y/ vs /y\u02d0/', 'h\u00fcbsch (pretty) vs. f\u00fchlen (feel)'),
    ]
    for i, (ipa, ex) in enumerate(gv):
        y = 83 + i * 10
        g += t(120, y, ipa, 'middle', 'Lx')
        g += t(320, y, ex, 'middle', 'Lx')
    g += hr(158)

    g += sh(166, 'GERMAN CONSONANTS \u2014 KEY FEATURES')
    g += t(240, 176, '/x/ vs /\u00e7/: velar [x] after back vowels (Buch), palatal [\u00e7] after front vowels (ich).', 'middle', 'Ls')
    g += t(240, 185, 'Word-final devoicing (Auslautverhärtung): Rad /r\u0251\u02d0t/ (wheel) vs. Räder /r\u025bd\u0259r/ (wheels, pl.).', 'middle', 'Ls')
    g += t(240, 194, 'Aspirated stops: /p\u02b0 t\u02b0 k\u02b0/ at word onset \u2014 Pan, Tisch, Kopf. Unaspirated after /s/: Span, Stein.', 'middle', 'Lx')
    g += t(240, 203, 'Uvular /\u0281/ (standard r): produced at back of throat, like French r. Regional variants include trill /r/.', 'middle', 'Lx')
    g += hr(211)

    g += sh(219, 'GERMAN STRESS \u2014 FIRST SYLLABLE (TYPICALLY)')
    g += t(240, 229, 'Stress on first root syllable: \u2019Wasser, \u2019Freiheit, \u2019sprechen. Prefixes: un-, un-be- are unstressed.', 'middle', 'Ls')
    g += t(240, 238, 'Loanwords follow original stress: Muse\u2019um, Univer\u2019sit\u00e4t, Tele\u2019fon.', 'middle', 'Lx')

    g += sec_divider(248, 'SECONDARY \u2014 POLISH (J\u0118ZYK POLSKI) \u2014 PHONOLOGY')

    g += sh(274, 'POLISH VOWELS \u2014 6 ORAL + 2 NASAL')
    g += t(240, 284, 'Polish has 6 oral vowels: /a \u025b i \u0254 u y/ (y = /\u026a/ front unrounded, absent from German/English).', 'middle', 'Ls')
    g += t(240, 293, '\u0105 and \u0119 are historically nasal (/\u0254\u0303 \u025b\u0303/) but in modern Polish pronounced as oral vowels + nasal coda in most positions.', 'middle', 'Lx')
    g += t(240, 302, 'Polish y /\u026a/: as in ryba (fish), dym (smoke). Sounds like a short, centralized i. Key learning difficulty.', 'middle', 'Lx')
    g += hr(310)

    g += sh(318, 'POLISH CONSONANTS \u2014 COMPLEX CLUSTERS')
    g += t(240, 328, 'Polish allows extremely dense consonant clusters, especially word-initial: szcz\u0119\u015bcie /\u0283t\u0283\u025b\u0255t\u0255e/ (happiness).', 'middle', 'Ls')
    g += t(240, 337, 'Palatalization: consonants have hard and soft (palatalized) variants. Soft = with /\u02b2/ offglide.', 'middle', 'Ls')
    g += t(240, 346, 'Hard/soft pairs: t/\u0107 \u00b7 d/d\u017a\u02b2 \u00b7 s/\u015b \u00b7 z/\u017a \u00b7 n/\u0144 \u00b7 l/l\u02b2. These are phonemically distinct.', 'middle', 'Lx')
    g += hr(354)

    g += sh(362, 'POLISH STRESS \u2014 PENULTIMATE (NEAR-UNIVERSAL)')
    g += t(240, 372, 'Polish stress falls on the second-to-last syllable almost universally: \u2019woda (water), wol\u2019no\u015b\u0107 (freedom).', 'middle', 'Ls')
    g += t(240, 381, 'Exceptions: 1st person plural past verbs (sz\u0142i\u015bmy), some loanwords (u\u2019niwersytet).', 'middle', 'Lx')
    g += hr(389)

    g += sh(397, 'PHONOLOGICAL BRIDGE \u2014 COMPARING TWO NEIGHBORS')
    comp = [
        ('Feature', 'German', 'Polish'),
        ('Vowel length', 'Phonemic (lang/kurz)', 'Not phonemic'),
        ('Nasal vowels', 'No', 'Historical (\u0105 \u0119)'),
        ('Consonant clusters', 'Moderate', 'Very dense (szcz-)'),
        ('Stress', '1st syllable (root)', 'Penultimate'),
        ('r-sound', 'Uvular /\u0281/', 'Alveolar trill /r/'),
        ('Final devoicing', 'Yes (Auslautverh.)', 'Yes (similar rule)'),
    ]
    for i, row in enumerate(comp):
        y = 407 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('52', 'German', 'Polish', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 52C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_52c_alt():
    g = open_svg()
    g += t(240, 30, 'GERMAN + POLISH \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 52C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'GERMAN GRAMMAR \u2014 4 CASES \u00b7 3 GENDERS \u00b7 SOV SUBORDINATE')
    g += t(240, 73, 'German has 4 cases: Nominative (subject), Accusative (direct object), Dative (indirect object), Genitive (possession).', 'middle', 'Ls')
    g += t(240, 82, '3 genders: masculine (der), feminine (die), neuter (das). Gender is grammatical, not natural.', 'middle', 'Lx')
    g += t(240, 91, 'Main clause: SVO \u2014 Ich lese das Buch. Subordinate clause: SOV \u2014 \u2026weil ich das Buch lese.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'GERMAN CASE SYSTEM \u2014 DER/DIE/DAS TABLE')
    cases = [
        ('Case', 'Masc.', 'Fem.', 'Neut.', 'Plural'),
        ('Nom.', 'der', 'die', 'das', 'die'),
        ('Acc.', 'den', 'die', 'das', 'die'),
        ('Dat.', 'dem', 'der', 'dem', 'den'),
        ('Gen.', 'des', 'der', 'des', 'der'),
    ]
    for i, row in enumerate(cases):
        y = 117 + i * 11
        g += t(55, y, row[0], 'middle', 'Lx')
        g += t(160, y, row[1], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(255, y, row[2], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(340, y, row[3], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(425, y, row[4], 'middle', 'Ls' if i > 0 else 'Lx')
    g += hr(175)

    g += sh(183, 'GERMAN CORE VOCABULARY')
    gvocab = [
        ('Wasser', 'water'), ('Feuer', 'fire'), ('Erde', 'earth'), ('Mensch', 'person'),
        ('Mond', 'moon'), ('Erinnerung', 'memory'), ('Zukunft', 'future'), ('Freiheit', 'freedom'),
        ('Herz', 'heart'), ('Liebe', 'love'), ('Welt', 'world'), ('Leben', 'life'),
    ]
    for i, (de, en) in enumerate(gvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 193 + row * 10
        g += t(x, y, de, 'middle', 'Ls')
        g += t(x + 55, y, en, 'middle', 'Lx')

    g += sec_divider(238, 'SECONDARY \u2014 POLISH (J\u0118ZYK POLSKI) \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(264, 'POLISH GRAMMAR \u2014 7 CASES \u00b7 3 GENDERS \u00b7 FREE WORD ORDER')
    g += t(240, 274, 'Polish has 7 grammatical cases: Nominative, Genitive, Dative, Accusative, Instrumental, Locative, Vocative.', 'middle', 'Ls')
    g += t(240, 283, '3 genders: masculine (animate/inanimate), feminine, neuter. Animacy affects accusative form.', 'middle', 'Lx')
    g += t(240, 292, 'Free word order: case endings mark grammar, so subject-verb order is flexible (SOV, SVO, OVS all possible).', 'middle', 'Lx')
    g += hr(300)

    g += sh(308, 'POLISH CASE ENDINGS \u2014 woda (water, fem.)')
    pl_cases = [
        ('Nominative', 'woda', 'subject: Woda jest zimna (Water is cold)'),
        ('Genitive', 'wody', 'possession/negation: szklanka wody (glass of water)'),
        ('Dative', 'wodzie', 'indirect object: daj mi wod\u0119 (give me water)'),
        ('Accusative', 'wod\u0119', 'direct object: pij\u0119 wod\u0119 (I drink water)'),
        ('Instrumental', 'wod\u0105', 'with/by: myj\u0119 wod\u0105 (I wash with water)'),
        ('Locative', 'wodzie', 'location: m\u00f3wi\u0107 o wodzie (to talk about water)'),
        ('Vocative', 'wodo!', 'address: direct address, poetry'),
    ]
    for i, (case, form, ex) in enumerate(pl_cases):
        y = 318 + i * 10
        g += t(80, y, case, 'middle', 'Lx')
        g += t(185, y, form, 'middle', 'Ls')
        g += t(360, y, ex, 'middle', 'Lx')
    g += hr(393)

    g += sh(401, 'POLISH CORE VOCABULARY')
    pvocab = [
        ('woda', 'water'), ('ogie\u0144', 'fire'), ('ziemia', 'earth'), ('cz\u0142owiek', 'person'),
        ('ksi\u0119\u017cyc', 'moon'), ('pami\u0119\u0107', 'memory'), ('przysz\u0142o\u015b\u0107', 'future'), ('wolno\u015b\u0107', 'freedom'),
        ('serce', 'heart'), ('mi\u0142o\u015b\u0107', 'love'), ('\u015bwiat', 'world'), ('\u017cycie', 'life'),
    ]
    for i, (pl, en) in enumerate(pvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 411 + row * 10
        g += t(x, y, pl, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')
    g += hr(455)

    g += sh(463, 'GRAMMAR BRIDGE \u2014 CASE SYSTEMS COMPARED')
    g += t(240, 473, 'German: 4 cases, marked on articles and adjectives (not always noun endings).', 'middle', 'Ls')
    g += t(240, 482, 'Polish: 7 cases, marked directly on noun endings (and adjectives). No articles at all.', 'middle', 'Ls')
    g += t(240, 491, 'Both descended from Proto-Indo-European \u2014 German cases simplified from PIE; Polish preserved more.', 'middle', 'Lx')

    g += footer('52', 'German', 'Polish', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 52D ALT — TEXT ─────────────────────────────────────────────────────

def build_52d_alt():
    g = open_svg()
    g += t(240, 30, 'GERMAN + POLISH \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 52D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. GOETHE \u2014 FAUST (1808 CE)')
    g += t(240, 73, 'Grau, teurer Freund, ist alle Theorie,', 'middle', 'L')
    g += t(240, 84, 'Und gr\u00fcn des Lebens goldner Baum.', 'middle', 'L')
    g += t(240, 95, 'Grey  dear    friend  is all   theory / And green of-the life  golden tree.', 'middle', 'Lx')
    g += t(240, 104, '"All theory, dear friend, is grey, but the golden tree of life is ever green." \u2014 Goethe, Mephistopheles.', 'middle', 'F')
    g += hr(112)

    g += sh(120, 'II. GERMAN PROVERB \u2014 ON MEMORY AND TIME')
    g += t(240, 130, 'Wer die Vergangenheit nicht kennt, kann die Zukunft nicht gestalten.', 'middle', 'L')
    g += t(240, 141, 'Who the past not knows can the future not shape.', 'middle', 'Lx')
    g += t(240, 150, '"Those who do not know the past cannot shape the future." (German proverb)', 'middle', 'F')
    g += hr(158)

    g += sh(166, 'III. GERMAN BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 177, 'Dies wurde f\u00fcr Sie gemacht, kostenlos,', 'middle', 'L')
    g += t(240, 189, 'von Menschen, die vorausgedacht haben.', 'middle', 'L')
    g += t(240, 200, 'This was for you made  freely / by people  who  forward-thought have.', 'middle', 'Lx')
    g += t(240, 209, '"This was made for you, freely, by people who thought forward." (German)', 'middle', 'F')
    g += hr(217)

    g += sh(225, 'GERMAN NOTE \u2014 \u201cFORWARD\u201d')
    g += t(240, 235, 'Vorausdenken = to think ahead / forward. Zukunft = future (lit. \u201ccoming-toward\u201d, from zukommen).', 'middle', 'Ls')
    g += t(240, 244, 'Verb-final in subordinate clause (vorausgedacht haben) shows German SOV in embedded clauses.', 'middle', 'Lx')

    g += sec_divider(254, 'SECONDARY \u2014 POLISH (J\u0118ZYK POLSKI) \u2014 RUNNING TEXT')

    g += sh(280, 'I. ADAM MICKIEWICZ \u2014 PAN TADEUSZ (1834 CE)')
    g += t(240, 290, 'Litwo! Ojczyzno moja! ty jeste\u015b jak zdrowie;', 'middle', 'L')
    g += t(240, 301, 'Lithuania my-fatherland  you are   like health', 'middle', 'Lx')
    g += t(240, 310, '"Lithuania, my fatherland! You are like health." \u2014 Opening of Poland\u2019s national epic. Vocative case: Litwo!', 'middle', 'F')
    g += hr(318)

    g += sh(326, 'II. POLISH PROVERB \u2014 ON MEMORY')
    g += t(240, 336, 'Cz\u0142owiek uczy si\u0119 przez ca\u0142e \u017cycie.', 'middle', 'L')
    g += t(240, 347, 'Person learns refl. through whole life.', 'middle', 'Lx')
    g += t(240, 356, '"A person learns through their whole life." \u2014 Polish proverb on lifelong knowledge.', 'middle', 'F')
    g += hr(364)

    g += sh(372, 'III. POLISH BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 383, 'To zosta\u0142o zrobione dla ciebie, bezp\u0142atnie,', 'middle', 'L')
    g += t(240, 395, 'przez ludzi, kt\u00f3rzy pami\u0119tali o przysz\u0142o\u015bci.', 'middle', 'L')
    g += t(240, 407, 'This was    done   for you  freely  / by people who remembered about future.', 'middle', 'Lx')
    g += t(240, 416, '"This was made for you, freely, by people who remembered the future." (Polish)', 'middle', 'F')
    g += hr(424)

    g += sh(432, 'POLISH NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 442, 'Przysz\u0142o\u015b\u0107 = future (from przyj\u015b\u0107 \u201cto come\u201d \u2014 the future as what is arriving).', 'middle', 'Ls')
    g += t(240, 451, 'Pami\u0119ta\u0107 = to remember (from pami\u0119\u0107 \u201cmemory\u201d). O przysz\u0142o\u015bci = about the future (Locative case).', 'middle', 'Ls')
    g += t(240, 460, 'Note case: dla ciebie (Genitive \u201cfor you\u201d), przez ludzi (Accusative \u201cby people\u201d).', 'middle', 'Lx')
    g += hr(468)

    g += sh(476, 'LANGUAGE BRIDGE \u2014 NEIGHBORS ACROSS A BORDER')
    g += t(240, 486, 'German: ~90M speakers. West Germanic. 4 cases. Verb-final embedded clauses. All nouns capitalized.', 'middle', 'Ls')
    g += t(240, 495, 'Polish: ~45M speakers. West Slavic. 7 cases. Free word order. No articles. Dense consonant clusters.', 'middle', 'Ls')
    g += t(240, 504, 'Shared millennium of contact: loanwords flow both directions. Wrocław/Breslau: both Polish and German names.', 'middle', 'Lx')

    g += footer('52', 'German', 'Polish', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate52a_german_polish_script_alt.svg':    build_52a_alt(),
        'plate52b_german_polish_phonology_alt.svg': build_52b_alt(),
        'plate52c_german_polish_grammar_alt.svg':   build_52c_alt(),
        'plate52d_german_polish_text_alt.svg':      build_52d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
