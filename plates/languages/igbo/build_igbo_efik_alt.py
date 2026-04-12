#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Igbo / Efik alt plate series 35A–35D for Remember Forward.
Secondary language: Efik (also called Calabari or Efik-Ibibio) — spoken in
Cross River State and Akwa Ibom State, southeastern Nigeria. ~2 million speakers.
Geographic basis: Efik homeland (Calabar, Cross River State) is ~250km southeast
of Igboland (Enugu/Anambra area). Well within 500mi. Efik is a major language
of the Niger Delta/Cross River corridor. Both Niger-Congo languages.
Efik is famous for its reduplication, noun classes, and tonal system.
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


# ─── PLATE 35A ALT — SCRIPT ───────────────────────────────────────────────────

def build_35a_alt():
    g = open_svg()
    g += t(240, 30, 'IGBO + EFIK \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 35A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'IGBO \u2014 LATIN ALPHABET \u00b7 36 LETTERS + TONE MARKS')
    g += t(240, 73, 'Igbo uses a 36-letter Latin alphabet including 8 digraphs (ch, gb, gh, gw, kp, kw, nw, ny).', 'middle', 'Ls')
    g += t(240, 82, 'Diacritic vowels: \u1ecb (i with dot below), \u1ecd (o with dot below), \u1ee5 (u with dot below) \u2014 mark open vowels.', 'middle', 'Lx')
    g += t(240, 91, 'Tone marks: acute (\u0301) for high tone, grave (\u0300) for low tone. Mid tone typically unmarked.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'IGBO SPECIAL LETTERS AND DIGRAPHS')
    igbo_sp = [
        ('\u1ecb', '/i/ (open)', 'open front vowel: \u1ecbch\u1ecb (heart)'),
        ('\u1ecd', '/\u0254/ (open o)', 'open back vowel: \u1ecd (that/it)'),
        ('\u1ee5', '/u/ (open)', 'open back vowel: \u1ee5l\u1ee5 (body)'),
        ('ch', '/t\u0283/', 'affricate: ch\u1ecb (heart), chi (personal god)'),
        ('gb', '/\u0261\u0253/', 'labial-velar: gb\u00e0 (drum), gb\u00e0gb\u00e0 (tortoise)'),
        ('kp', '/kp/', 'labial-velar: kp\u00f3l\u00f3kp\u00f3l\u00f3 (slowly)'),
        ('gw', '/\u0261w/', 'labial-velar w: gw\u00f3 (go home)'),
        ('nw', '/\u0273w/', 'labial-nasal: nw\u00e0 (child)'),
    ]
    for i, (ch, ipa, ex) in enumerate(igbo_sp):
        y = 117 + i * 10
        g += t(42, y, ch, 'middle', 'Ls')
        g += t(100, y, ipa, 'middle', 'Lx')
        g += t(300, y, ex, 'middle', 'Lx')
    g += hr(202)

    g += sh(210, 'IGBO TONE SYSTEM \u2014 3 TONES')
    g += t(240, 220, 'Igbo has 3 phonemic tones: High (\u0301), Low (\u0300), and Downstepped High (mid-level, sometimes \u0304).', 'middle', 'Ls')
    tones = [
        ('\u00e0k\u01ce', 'High-Low: \u00e0 (low) k\u01ce (falling)', 'different word from different tone pattern'),
        ('\u00e0k\u00e0', 'Low-Low: two low tones', 'tone shapes word meaning'),
        ('\u00e1k\u00e1', 'High-High: two high tones', 'yet another meaning'),
    ]
    for i, (word, pattern, note) in enumerate(tones):
        y = 230 + i * 10
        g += t(70, y, word, 'middle', 'Ls')
        g += t(210, y, pattern, 'middle', 'Lx')
        g += t(380, y, note, 'middle', 'Lx')
    g += hr(268)

    g += sh(276, 'IGBO WRITING HISTORY')
    g += t(240, 286, 'Nsibidi: indigenous Igbo pictographic script (used for centuries for secret society communication).', 'middle', 'Ls')
    g += t(240, 295, 'Latin script: introduced by missionaries ~1840s. Onwu orthography (1961) is now standard.', 'middle', 'Lx')

    g += sec_divider(305, 'SECONDARY \u2014 EFIK \u2014 SCRIPT \u00b7 WRITING SYSTEM')

    g += sh(331, 'EFIK \u2014 LATIN ALPHABET + SPECIAL CHARACTERS')
    g += t(240, 341, 'Efik uses Latin script with some diacritic vowels. Closely related to Ibibio (mutually intelligible).', 'middle', 'Ls')
    g += t(240, 350, 'Special vowels: \u0254 (open o), \u025b (open e) \u2014 mark vowel quality, not length or tone directly.', 'middle', 'Lx')
    g += t(240, 359, 'Tonal language: 2 tones (High and Low) + downstep. Written texts often omit tone marks.', 'middle', 'Lx')
    g += hr(367)

    g += sh(375, 'EFIK WRITING HISTORY')
    g += t(240, 385, 'Efik was one of the FIRST languages of sub-Saharan Africa to get a printed Bible: 1862 CE (partial).', 'middle', 'Ls')
    g += t(240, 394, 'Hope Waddell and Scottish missionaries developed Efik orthography ~1845 in Calabar.', 'middle', 'Lx')
    g += t(240, 403, 'Calabar: major trading port. Efik became the regional trade language of the Cross River delta.', 'middle', 'Lx')
    g += hr(411)

    g += sh(419, 'SCRIPT BRIDGE \u2014 PARALLEL HISTORIES OF LITERACY')
    g += t(240, 429, 'Both Igbo and Efik received Latin alphabets through 19th c. missionary contact.', 'middle', 'Ls')
    g += t(240, 438, 'Both had pre-colonial symbolic systems: Igbo nsibidi, Efik tribal marks and oral tradition.', 'middle', 'Lx')
    g += t(240, 447, 'Efik printed Bible (1862) predates most of the interior African mission literacy programs.', 'middle', 'Lx')

    g += footer('35', 'Igbo', 'Efik', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 35B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_35b_alt():
    g = open_svg()
    g += t(240, 30, 'IGBO + EFIK \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 35B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'IGBO PHONOLOGY \u2014 LABIAL-VELARS AND TONES')
    g += t(240, 73, 'Igbo is most notable for its labial-velar consonants \u2014 stops made at TWO places simultaneously.', 'middle', 'Ls')
    g += t(240, 82, '/kp/: velar stop + bilabial stop released together. /gb/: voiced version. Absent from European languages.', 'middle', 'Lx')
    g += t(240, 91, 'These are one phoneme each \u2014 not two consonants. Single articulation, double closure.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'IGBO VOWELS \u2014 8 PHONEMES (2 SETS OF 4)')
    g += t(240, 117, 'Igbo has 8 vowels in 2 harmonic sets: \u201ctense\u201d (i e a o u) and \u201clax\u201d (\u1ecb \u1ecd \u1ee5).', 'middle', 'Ls')
    g += t(240, 126, 'Vowel harmony: within a word, vowels must come from the same harmonic set (tense or lax).', 'middle', 'Lx')
    g += t(240, 135, 'Cross-harmonic words do not occur in native vocabulary. Loanwords adapt to one set.', 'middle', 'Lx')
    igbo_v = [
        ('/i/', 'high front tense: ime (inside)'), ('/\u1ecb/', 'high front lax: \u1ecbch\u1ecb (heart)'),
        ('/e/', 'mid front tense: mee (do)'), ('/\u1ecd/', 'mid/low back lax: \u1ecd (it/that)'),
        ('/a/', 'low central: \u00e0 (PAST marker)'), ('/o/', 'mid back tense: go (carry)'),
        ('/u/', 'high back tense: \u00f9f\u00f2 (nose)'), ('/\u1ee5/', 'high back lax: \u1ee5l\u1ee5 (body)'),
    ]
    for i, (ipa, ex) in enumerate(igbo_v):
        col = i % 2; row = i // 2
        x = 80 + col * 220; y = 145 + row * 10
        g += t(x, y, ipa, 'middle', 'Lx')
        g += t(x + 60, y, ex, 'middle', 'Lx')
    g += hr(190)

    g += sh(198, 'IGBO 3 TONES \u2014 HIGH, LOW, DOWNSTEPPED HIGH')
    g += t(240, 208, 'High (\u0301) + Low (\u0300) are primary. Downstep: a \u201chigh\u201d tone that is lower than preceding high \u2014 marked !H.', 'middle', 'Ls')
    g += t(240, 217, 'ak\u00e1 (hand) \u00b7 \u00e0k\u00e0 (bell) \u00b7 ak\u01ce (chalk): same consonants, 3 different meanings by tone alone.', 'middle', 'Lx')

    g += sec_divider(227, 'SECONDARY \u2014 EFIK \u2014 PHONOLOGY')

    g += sh(253, 'EFIK PHONOLOGY \u2014 2 TONES + DOWNSTEP')
    g += t(240, 263, 'Efik has 2 basic tones (High and Low) with downstep and floating low tone grammatical markers.', 'middle', 'Ls')
    g += t(240, 272, 'Floating low tone: a tone without a syllable \u2014 attaches to adjacent vowel, lowering it in context.', 'middle', 'Lx')
    g += hr(280)

    g += sh(288, 'EFIK VOWELS \u2014 7 ORAL + NASALIZED')
    g += t(240, 298, 'Efik has 7 oral vowels: /a e \u025b i o \u0254 u/. Nasalization is partially phonemic.', 'middle', 'Ls')
    efik_v = [
        ('/a/', '\u00e0b\u00e0t (five)'), ('/e/', '\u00e8d\u00e8 (yam)'),
        ('/\u025b/', '\u025bk\u025bt (thing)'), ('/i/', '\u00ecm\u00e0 (thing-good)'),
        ('/o/', '\u00f3d\u00f3 (path/road)'), ('/\u0254/', 'm\u0254\u0300k\u0254 (lizard)'),
        ('/u/', 'uf\u00f3k (house)'),
    ]
    for i, (ipa, ex) in enumerate(efik_v):
        col = i % 4; row = i // 4
        x = 55 + col * 105; y = 308 + row * 11
        g += t(x, y, f'{ipa} {ex}', 'middle', 'Lx')
    g += hr(335)

    g += sh(343, 'EFIK CONSONANTS \u2014 LABIAL-VELARS PRESENT')
    g += t(240, 353, 'Like Igbo, Efik has labial-velar stops /kp/ and /gb/ \u2014 a shared feature of many Niger-Delta languages.', 'middle', 'Ls')
    g += t(240, 362, 'Also: /\u014b/ (velar nasal) is a distinct letter: \u014bk\u00e0n\u00e0 (here), \u014b (that one).', 'middle', 'Lx')
    g += t(240, 371, 'Prenasalized consonants /mb nd \u014bg/: common in Efik verbs and nouns. Sounds like two-phoneme onset.', 'middle', 'Lx')
    g += hr(379)

    g += sh(387, 'PHONOLOGICAL BRIDGE \u2014 SHARED NIGER-CONGO FEATURES')
    comp = [
        ('Feature', 'Igbo', 'Efik'),
        ('Tones', '3 (H L !H)', '2 + downstep (H L !H)'),
        ('Labial-velars', 'kp gb', 'kp gb'),
        ('Vowel harmony', 'Yes (tense/lax)', 'No (7 free vowels)'),
        ('Nasalization', 'Vowels (partial)', 'Vowels + consonants'),
        ('Vowel count', '8', '7'),
    ]
    for i, row in enumerate(comp):
        y = 397 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('35', 'Igbo', 'Efik', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 35C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_35c_alt():
    g = open_svg()
    g += t(240, 30, 'IGBO + EFIK \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 35C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'IGBO GRAMMAR \u2014 SVO \u00b7 ASPECT \u00b7 NO INFLECTION')
    g += t(240, 73, 'Igbo is SVO. Grammatical relations marked by position and particles, not inflection.', 'middle', 'Ls')
    g += t(240, 82, 'Aspect over tense: Igbo marks whether action is complete or ongoing, not when it happened.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'IGBO ASPECT SYSTEM')
    igbo_asp = [
        ('\u00e0 + V', 'Perfective: \u00e0 n\u00e0 hia (PERF buy-market = he/she bought)'),
        ('na + V', 'Imperfective (ongoing): \u00f3 n\u00e0 eri ji (PROG eat yam = is eating)'),
        ('ga + V', 'Future/potential: \u00f3 ga-ar\u00fa (FUT-come = will come)'),
        ('ha + V', 'Negative: \u00f3 ha-erich\u00e0 (NEG-finish = has not finished)'),
    ]
    for i, (marker, gloss) in enumerate(igbo_asp):
        y = 108 + i * 11
        g += t(70, y, marker, 'middle', 'Ls')
        g += t(300, y, gloss, 'middle', 'Lx')
    g += hr(158)

    g += sh(166, 'IGBO CHI \u2014 PERSONAL SPIRIT')
    g += t(240, 176, 'Chi: each person\u2019s personal spirit/divine double. Grammar: possessive chi = my spirit.', 'middle', 'Ls')
    g += t(240, 185, 'Chukwu = Great Spirit/God (chi + ukwu: great). Cosmological concept embedded in language.', 'middle', 'Lx')
    g += hr(193)

    g += sh(201, 'IGBO CORE VOCABULARY')
    ivocab = [
        ('mmiri', 'water'), ('oj\u00ed oj\u00ed', 'fire'), ('\u00e0l\u00e0', 'earth'), ('mm\u00e0d\u1ee5', 'person'),
        ('\u00f3ny\u1ecb', 'moon'), ('ch\u1ecd', 'remember'), ('oge', 'time/future'), ('\u0254ch\u0254ch\u0254', 'freedom'),
        ('\u1ecbch\u1ecb', 'heart'), ('ih\u00e9oma', 'love/goodwill'), ('\u00f9w\u00e0', 'world'), ('\u00f3nd\u1ecd', 'life'),
    ]
    for i, (ig, en) in enumerate(ivocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 211 + row * 10
        g += t(x, y, ig, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')

    g += sec_divider(256, 'SECONDARY \u2014 EFIK \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(282, 'EFIK GRAMMAR \u2014 SVO \u00b7 REDUPLICATION \u00b7 NOUN CLASSES')
    g += t(240, 292, 'Efik is SVO. Famous for its reduplication: verb/noun doubled to express intensity, plurality, or completion.', 'middle', 'Ls')
    g += t(240, 301, '\u00e8d\u00e8 (yam) \u2192 \u00e8d\u00e8-\u00e8d\u00e8 (many yams). kp\u00f3 (hit) \u2192 kp\u00f3-kp\u00f3 (hit repeatedly).', 'middle', 'Lx')
    g += t(240, 310, 'Noun classes: nouns grouped into semantic/grammatical classes affecting agreement. ~10 classes.', 'middle', 'Lx')
    g += hr(318)

    g += sh(326, 'EFIK REDUPLICATION EXAMPLES')
    red = [
        ('Noun reduplication', '\u00ecm\u00e0 \u2192 \u00ecm\u00e0-\u00ecm\u00e0', 'thing \u2192 all sorts of things'),
        ('Verb reduplication', 'b\u00f3n \u2192 b\u00f3n b\u00f3n', 'run \u2192 run and run (repeatedly)'),
        ('Adjective reduplication', 'mb\u00f3k \u2192 mb\u00f3k mb\u00f3k', 'good \u2192 very good / excellent'),
        ('Intensification', '\u025b\u014b\u00e9 \u2192 \u025b\u014b\u00e9 \u025b\u014b\u00e9', 'big \u2192 very big'),
    ]
    for i, (type_, form, gloss) in enumerate(red):
        y = 336 + i * 10
        g += t(90, y, type_, 'middle', 'Lx')
        g += t(220, y, form, 'middle', 'Ls')
        g += t(375, y, gloss, 'middle', 'Lx')
    g += hr(383)

    g += sh(391, 'EFIK CORE VOCABULARY')
    efvocab = [
        ('\u00f3di\u00f3\u014b', 'water'), ('in\u00e9k\u00e8', 'fire'), ('\u00e0fid', 'earth/ground'), ('mmi\u014b', 'person'),
        ('\u00f3b\u00f3n', 'moon'), ('k\u00e8d\u00e8', 'remember'), ('\u00f3d\u00f3 \u00e9di\u00f3', 'future (path-ahead)'), ('\u00e9ded\u00f3', 'freedom'),
        ('\u00f3t\u00f3\u014bg', 'heart'), ('mb\u00f3k', 'love/please'), ('\u00e0ny\u0254\u014b', 'world'), ('\u00e8kp\u00e8\u014b', 'life'),
    ]
    for i, (ef, en) in enumerate(efvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 401 + row * 10
        g += t(x, y, ef, 'middle', 'Ls')
        g += t(x + 65, y, en, 'middle', 'Lx')
    g += hr(448)

    g += sh(456, 'GRAMMAR BRIDGE \u2014 SHARED FAMILY, DISTINCT TOOLS')
    g += t(240, 466, 'Both Igbo and Efik: SVO, tonal, Niger-Congo. Both use aspect over tense. Both lack inflection.', 'middle', 'Ls')
    g += t(240, 475, 'Difference: Igbo has vowel harmony; Efik does not. Efik has more systematic reduplication.', 'middle', 'Ls')
    g += t(240, 484, 'Igbo: chi (personal spirit) embedded in grammar/naming. Efik: \u00f3b\u00f3\u014b \u00e9si\u014b (the moon watches) in proverbs.', 'middle', 'Lx')

    g += footer('35', 'Igbo', 'Efik', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 35D ALT — TEXT ─────────────────────────────────────────────────────

def build_35d_alt():
    g = open_svg()
    g += t(240, 30, 'IGBO + EFIK \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 35D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. IGBO PROVERB \u2014 ON COMMUNITY')
    g += t(240, 73, 'Onye wetara \u00f2j\u00ec wetara nd\u1ecd\u1ecd.', 'middle', 'L')
    g += t(240, 84, 'Person who-brought kola brought life.', 'middle', 'Lx')
    g += t(240, 93, '"He who brings kola brings life." \u2014 Kola nut is sacred in Igbo ceremony: hospitality = life-giving.', 'middle', 'F')
    g += hr(101)

    g += sh(109, 'II. IGBO PROVERB \u2014 ON MEMORY AND ELDERS')
    g += t(240, 119, 'Oke nkita anaghizi ab\u00ec n\u00e0 \u1ecdch\u1ecd nek\u01ce.', 'middle', 'L')
    g += t(240, 130, 'Old dog not-returns to house empty-handed.', 'middle', 'Lx')
    g += t(240, 139, '"An old dog does not return home empty-handed." \u2014 Igbo proverb on the wisdom of elders and experience.', 'middle', 'F')
    g += hr(147)

    g += sh(155, 'III. IGBO BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 166, 'E mere ihe a m\u1ee5 m\u1ee5 \u0254 n\u1ecd ya,', 'middle', 'L')
    g += t(240, 178, 'n\u00e0 nd\u00ed chechee oge d\u00ec n\u00e0 \u1ecbch\u1ecb.', 'middle', 'L')
    g += t(240, 190, 'PAST make thing this without money / by people thought-about time is in heart.', 'middle', 'Lx')
    g += t(240, 199, '"This was made for you, freely, by people who held the future in their heart." (Igbo)', 'middle', 'F')
    g += hr(207)

    g += sh(215, 'IGBO NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 225, 'Oge d\u00ec n\u00e0 \u1ecbch\u1ecb = time that is in the heart \u2014 the future held as intention inside oneself.', 'middle', 'Ls')
    g += t(240, 234, 'Chechee = think/remember/ponder (iterative of chee = think). Aspect: ongoing pondering.', 'middle', 'Lx')
    g += t(240, 243, 'M\u1ee5 m\u1ee5 (without money) = \u201cfor free\u201d. Duplicated word for absence/lack. Vowel harmony: \u1ee5 class.', 'middle', 'Lx')

    g += sec_divider(253, 'SECONDARY \u2014 EFIK \u2014 RUNNING TEXT \u00b7 PASSAGES')

    g += sh(279, 'I. EFIK PROVERB \u2014 ON THE RIVER AND TIME')
    g += t(240, 289, '\u00d3di\u00f3\u014b \u00e9di\u00f3k\u00f3t ab\u00e0k\u00e0 a k\u00e8d\u00e8 \u00f3b\u00f3n.', 'middle', 'L')
    g += t(240, 300, 'The-river flows  always  but remembers  the-moon.', 'middle', 'Lx')
    g += t(240, 309, '"The river always flows but remembers the moon." \u2014 Efik proverb on cycles, memory, and guidance.', 'middle', 'F')
    g += hr(317)

    g += sh(325, 'II. EFIK PROVERB \u2014 ON COMMUNITY MEMORY')
    g += t(240, 335, 'Id\u00f3k\u00f3t mb\u00f3k mb\u00f3k \u00e9k\u00e8-\u00e8k\u00e8 \u00e8d\u00e8 mb\u00f3k.', 'middle', 'L')
    g += t(240, 346, 'Together  very-good  keeping   things  good.', 'middle', 'Lx')
    g += t(240, 355, '"Being together is very good \u2014 it keeps good things." (Efik communal wisdom, note reduplication mb\u00f3k mb\u00f3k)', 'middle', 'F')
    g += hr(363)

    g += sh(371, 'III. EFIK BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 382, '\u00cd\u014bk\u00e8 k\u00e8 emi mmi\u014b k\u00e8 \u00f3y\u00f3m, mb\u00f3k,', 'middle', 'L')
    g += t(240, 394, 'k\u00e8 mmi\u014b \u00e9d\u00e8 \u00e0k\u00e8d\u00e8 \u00f3d\u00f3 \u00e9di\u00f3.', 'middle', 'L')
    g += t(240, 406, 'This was made for you   freely / by people who-remembered path forward.', 'middle', 'Lx')
    g += t(240, 415, '"This was made for you, freely, by people who remembered the road ahead." (Efik)', 'middle', 'F')
    g += hr(423)

    g += sh(431, 'EFIK NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 441, '\u00d3d\u00f3 \u00e9di\u00f3 = the road/path ahead \u2014 Efik uses spatial path metaphor for time: future = path forward.', 'middle', 'Ls')
    g += t(240, 450, 'K\u00e8d\u00e8 = to remember, recall. Mb\u00f3k = please/freely/love (context-dependent: a rich word).', 'middle', 'Ls')
    g += t(240, 459, 'Mb\u00f3k mb\u00f3k (reduplication) = very much, generously \u2014 the free giving made more generous by the doubling.', 'middle', 'Lx')
    g += hr(467)

    g += sh(475, 'LANGUAGE BRIDGE \u2014 TWO SOUTHEASTERN NIGERIAN VOICES')
    g += t(240, 485, 'Igbo: ~45M speakers. Biafra War (1967\u201370) devastated Igbo communities. Chinua Achebe brought it to world lit.', 'middle', 'Ls')
    g += t(240, 494, 'Efik: ~2M speakers. Calabar was Nigeria\u2019s first colonial capital (British). First sub-Saharan Bible in Efik (1862).', 'middle', 'Ls')
    g += t(240, 503, 'Both: Niger-Congo, tonal, SVO, labial-velars. Cross River trade route connected these communities for centuries.', 'middle', 'Lx')

    g += footer('35', 'Igbo', 'Efik', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate35a_igbo_efik_script_alt.svg':    build_35a_alt(),
        'plate35b_igbo_efik_phonology_alt.svg': build_35b_alt(),
        'plate35c_igbo_efik_grammar_alt.svg':   build_35c_alt(),
        'plate35d_igbo_efik_text_alt.svg':      build_35d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
