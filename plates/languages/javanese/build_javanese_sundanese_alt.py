#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Javanese / Sundanese alt plate series 43A–43D for Remember Forward.
Secondary language: Sundanese (Basa Sunda) — spoken in West Java and Banten,
~42 million speakers. Geographic basis: Sunda region (Bandung/Bogor area) is
~150–250km from Javanese heartland (Yogyakarta/Solo). Well within 500mi.
Both Austronesian, both use speech levels (register system), both use
Brahmic-derived scripts plus Latin. The Sundanese Sunda script (Aksara Sunda)
is distinct from the Javanese Hanacaraka script.
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


# ─── PLATE 43A ALT — SCRIPT ───────────────────────────────────────────────────

def build_43a_alt():
    g = open_svg()
    g += t(240, 30, 'JAVANESE + SUNDANESE \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 43A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'JAVANESE \u2014 HANACARAKA SCRIPT (AKSARA JAWA)')
    g += t(240, 73, 'Javanese Hanacaraka: an abugida descended from Brahmi via Kawi script (~9th c. CE).', 'middle', 'Ls')
    g += t(240, 82, '20 base consonants arranged in a traditional order. Each carries inherent /a/. Diacritics modify vowels.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'HANACARAKA \u2014 20 BASE CONSONANTS')
    hana = [
        ('\u0a9f\u0aa6', 'ha na'), ('\u0a9a\u0ab0', 'ca ra'), ('\u0a95\u0aa6', 'ka da'),
        ('\u0aa4\u0a9a', 'ta sa'), ('\u0ab5\u0ab2', 'wa la'), ('\u0aaa\u0aa7', 'pa da'),
        ('\u0a9c\u0aaf', 'ja ya'), ('\u0aac\u0aac', 'nya ma'), ('\u0aab\u0a97', 'ga ba'),
        ('\u0aa5\u0a99', 'tha nga'),
    ]
    # Use Latin since Javanese Unicode rendering is font-dependent
    jav_cons = [
        ('ha na ca ra ka', 'da ta sa wa la'),
        ('pa dha ja ya nya', 'ma ga ba tha nga'),
    ]
    g += t(240, 108, 'ha  na  ca  ra  ka  da  ta  sa  wa  la', 'middle', 'L')
    g += t(240, 122, 'pa  dha  ja  ya  nya  ma  ga  ba  tha  nga', 'middle', 'L')
    g += t(240, 136, '(Traditional order of 20 Javanese syllabic consonants \u2014 each carries inherent /a/)', 'middle', 'Lx')
    g += hr(143)

    g += sh(151, 'HANACARAKA \u2014 KEY DIACRITICS')
    diac = [
        ('wulu', 'adds /i/: consonant + wulu = C+i'),
        ('suku', 'adds /u/: consonant + suku = C+u'),
        ('taling', 'adds /e/ before consonant'),
        ('pepet', 'adds /\u0259/: the schwa vowel'),
        ('p\u00e9pét', 'adds /e/ (close)'),
        ('pangkon', 'removes inherent vowel (virama/killer stroke)'),
    ]
    for i, (name, desc) in enumerate(diac):
        y = 161 + i * 10
        g += t(100, y, name, 'middle', 'Ls')
        g += t(300, y, desc, 'middle', 'Lx')
    g += hr(218)

    g += sh(226, 'JAVANESE WRITING HISTORY')
    g += t(240, 236, 'Oldest Javanese inscription: Sukabumi (804 CE). Kawi script used for Sanskrit/Old Javanese literature.', 'middle', 'Ls')
    g += t(240, 245, 'Hanacaraka developed ~14th\u201316th c. CE. Kakawin Ramayana (~9th c.) is oldest major Old Javanese text.', 'middle', 'Lx')
    g += t(240, 254, 'Today: Latin script dominant in everyday use. Hanacaraka taught in schools, used for Javanese cultural texts.', 'middle', 'Lx')

    g += sec_divider(264, 'SECONDARY \u2014 SUNDANESE (BASA SUNDA) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(290, 'SUNDANESE \u2014 AKSARA SUNDA BAKU (STANDARD SUNDANESE SCRIPT)')
    g += t(240, 300, 'Aksara Sunda Baku: an abugida standardized in 1997, officially adopted by West Java province 2008.', 'middle', 'Ls')
    g += t(240, 309, 'Based on the ancient Sundanese script found in 14th\u201316th c. inscriptions (related to Kawi).', 'middle', 'Lx')
    g += t(240, 318, 'Unicode block: Sundanese U+1B80\u2013U+1BBF. 14 vowels, 18 consonants + additional marks.', 'middle', 'Lx')
    g += hr(326)

    g += sh(334, 'AKSARA SUNDA \u2014 SAMPLE CHARACTERS')
    g += t(240, 344, '\u1b80\u1b81\u1b82\u1b83\u1b84\u1b85\u1b86\u1b87\u1b88\u1b89\u1b8a\u1b8b\u1b8c\u1b8d  (Sundanese vowels)', 'middle', 'Ls')
    g += t(240, 356, '\u1b8e\u1b8f\u1b90\u1b91\u1b92\u1b93\u1b94\u1b95\u1b96\u1b97\u1b98\u1b99\u1b9a\u1b9b\u1b9c\u1b9d\u1b9e\u1b9f  (Sundanese consonants)', 'middle', 'Ls')
    g += hr(365)

    g += sh(373, 'SUNDANESE LATIN ALPHABET (STANDARD)')
    g += t(240, 383, 'Latin script now dominant in everyday Sundanese. 26 base letters. Accent: \u00e9 for close e, e for schwa.', 'middle', 'Ls')
    g += t(240, 392, '\u00e9ta (that), \u00e9mok (sitting), but e in \u201ceuy\u201d (/\u0259j/ \u2014 Sundanese discourse particle, no direct translation).', 'middle', 'Lx')
    g += hr(400)

    g += sh(408, 'SCRIPT BRIDGE \u2014 TWO BRAHMIC ABUGIDAS ON ONE ISLAND')
    g += t(240, 418, 'Java is one of the few places on earth where two distinct Brahmic-derived abugidas coexist on the same island.', 'middle', 'Ls')
    g += t(240, 427, 'Hanacaraka (Javanese) and Aksara Sunda: same Brahmi ancestor, diverged via different regional Kawi traditions.', 'middle', 'Lx')
    g += t(240, 436, 'Both revived as cultural/identity scripts in the 1990s\u20132000s. Both taught in regional schools alongside Latin.', 'middle', 'Lx')

    g += footer('43', 'Javanese', 'Sundanese', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 43B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_43b_alt():
    g = open_svg()
    g += t(240, 30, 'JAVANESE + SUNDANESE \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 43B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'JAVANESE PHONOLOGY \u2014 BREATHY VOICE AND RETROFLEXES')
    g += t(240, 73, 'Javanese has breathy/murmured consonants (b\u02b0 d\u02b0 g\u02b0 j\u02b0) and retroflex stops (\u1e6d \u1e0d).', 'middle', 'Ls')
    g += t(240, 82, 'Breathy voice: simultaneous vibration + open glottis = a \u201cbreathy\u201d or \u201cmurmured\u201d quality.', 'middle', 'Lx')
    g += t(240, 91, 'Retroflex: tongue tip curled back to touch the roof of the mouth \u2014 same feature as Sanskrit/Hindi.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'JAVANESE VOWELS \u2014 6 + SCHWA')
    jvowels = [
        ('/a/', 'bapak (father)'), ('/i/', 'iki (this)'),
        ('/u/', 'uwong (person)'), ('/e/', 'seger (fresh)'),
        ('/o/', 'omah (house)'), ('/\u0254/', 'bol\u00e9h (may/can)'),
        ('/\u0259/', 'pepet: a + pepet (Javanese schwa)'),
    ]
    for i, (ipa, ex) in enumerate(jvowels):
        col = i % 2; row = i // 2
        x = 80 + col * 220; y = 117 + row * 10
        g += t(x, y, ipa, 'middle', 'Lx')
        g += t(x + 55, y, ex, 'middle', 'Lx')
    g += hr(165)

    g += sh(173, 'JAVANESE CONSONANT INVENTORY')
    g += t(240, 183, 'Full 4-way stop series: voiceless / voiced / aspirated-voiced (breathy) / voiced retroflex.', 'middle', 'Ls')
    g += t(240, 192, 'p b b\u02b0  \u00b7  t d d\u02b0  \u00b7  \u1e6d \u1e0d \u1e0d\u02b0  \u00b7  k g g\u02b0  \u00b7  (\u02a4 \u025f \u025f\u02b0)  \u2014 palatal affricates', 'middle', 'Ls')
    g += t(240, 201, 'Nasals: m n \u0272 \u014b. Glides: w y. Liquids: r l. Fricatives: s h. Glottal stop /?/ word-finally.', 'middle', 'Lx')
    g += hr(209)

    g += sh(217, 'JAVANESE STRESS AND RHYTHM')
    g += t(240, 227, 'Stress typically falls on penultimate syllable of a root. Reduced vowel (schwa) in unstressed positions.', 'middle', 'Ls')
    g += t(240, 236, 'Javanese has a \u201cflat\u201d prosody \u2014 less dynamic than stress-timed languages. Long vs. short syllable distinction minor.', 'middle', 'Lx')

    g += sec_divider(246, 'SECONDARY \u2014 SUNDANESE (BASA SUNDA) \u2014 PHONOLOGY')

    g += sh(272, 'SUNDANESE PHONOLOGY \u2014 NO BREATHY CONSONANTS')
    g += t(240, 282, 'Sundanese lacks the breathy/murmured consonants of Javanese. Simpler stop series: voiceless/voiced only.', 'middle', 'Ls')
    g += t(240, 291, 'p b  \u00b7  t d  \u00b7  k g  \u00b7  (\u02a4 \u025f)  \u2014 no breathy voice. This is a major phonological difference from Javanese.', 'middle', 'Lx')
    g += hr(299)

    g += sh(307, 'SUNDANESE VOWELS \u2014 7 VOWELS')
    svowels = [
        ('/a/', 'cai (water)'), ('/i/', 'tiis (cold)'),
        ('/u/', 'buku (book)'), ('/e/', '\u00e9ta (that, close e)'),
        ('/o/', 'bodo (stupid)'), ('/\u0254/', 'col\u00e9\u0301k (to poke)'),
        ('/\u0259/', 'e: e.g. euy (discourse particle)'),
    ]
    for i, (ipa, ex) in enumerate(svowels):
        col = i % 2; row = i // 2
        x = 80 + col * 220; y = 317 + row * 10
        g += t(x, y, ipa, 'middle', 'Lx')
        g += t(x + 55, y, ex, 'middle', 'Lx')
    g += hr(358)

    g += sh(366, 'SUNDANESE \u2014 PHONOLOGICAL FEATURES')
    g += t(240, 376, 'Word-final glottal stop: many Sundanese words end in /?/ \u2014 not always written. Distinct from Javanese.', 'middle', 'Ls')
    g += t(240, 385, 'Distinction \u00e9 (close /e/) vs. e (schwa /\u0259/): grammatically important \u2014 marked by acute in Latin script.', 'middle', 'Lx')
    g += t(240, 394, 'Prenasalized consonants: mb nd \u014bg \u014bd\u0292 occur in some loanwords from Dutch and Sanskrit.', 'middle', 'Lx')
    g += hr(402)

    g += sh(410, 'PHONOLOGICAL BRIDGE \u2014 TWO AUSTRONESIAN COUSINS')
    comp = [
        ('Feature', 'Javanese', 'Sundanese'),
        ('Breathy voice', 'Yes (b\u02b0 d\u02b0 g\u02b0)', 'No'),
        ('Retroflexes', 'Yes (\u1e6d \u1e0d)', 'No'),
        ('Vowels', '6 + schwa', '7'),
        ('Word-final stop', 'Glottal /?/', 'Glottal /?/ (common)'),
        ('Stress', 'Penultimate', 'Penultimate'),
    ]
    for i, row in enumerate(comp):
        y = 420 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('43', 'Javanese', 'Sundanese', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 43C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_43c_alt():
    g = open_svg()
    g += t(240, 30, 'JAVANESE + SUNDANESE \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 43C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'JAVANESE GRAMMAR \u2014 SVO \u00b7 SPEECH LEVELS (UNGGAH-UNGGUH)')
    g += t(240, 73, 'Javanese is famous for its elaborate speech level system: Ngoko (informal), Madya (middle), Kram\u00e0 (formal).', 'middle', 'Ls')
    g += t(240, 82, 'Choosing the wrong level is a serious social error. Level depends on relative age, status, familiarity.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'JAVANESE SPEECH LEVELS \u2014 SAMPLE WORDS')
    levels = [
        ('Concept', 'Ngoko (informal)', 'Kram\u00e0 (formal)'),
        ('I', 'aku', 'kul\u00e0'),
        ('you', 'kok\u00f3 / kowe', 'panj\u00e9n\u00e9ngan'),
        ('eat', 'mangan', 'dhahar'),
        ('sleep', 'turu', 'sare'),
        ('go', 'lungo', 'tindak'),
        ('house', 'omah', 'dalem'),
        ('water', 'banyu', 'toya'),
    ]
    for i, row in enumerate(levels):
        y = 108 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx' if i == 0 else 'Ls')
        g += t(240, y, row[1], 'middle', 'Lx' if i == 0 else 'Ls')
        g += t(380, y, row[2], 'middle', 'Lx' if i == 0 else 'Ls')
    g += hr(195)

    g += sh(203, 'JAVANESE CORE VOCABULARY (NGOKO)')
    jvocab = [
        ('banyu', 'water'), ('geni', 'fire'), ('lemah', 'earth'),
        ('uwong', 'person'), ('wulan', 'moon'), ('eling', 'remember'),
        ('besa\u00f3k', 'future'), ('merd\u00e9k\u00e0', 'freedom'),
        ('ati', 'heart'), ('tresn\u00e0', 'love'), ('donya', 'world'),
        ('urip', 'life'),
    ]
    for i, (jv, en) in enumerate(jvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 213 + row * 10
        g += t(x, y, jv, 'middle', 'Ls')
        g += t(x + 58, y, en, 'middle', 'Lx')

    g += sec_divider(258, 'SECONDARY \u2014 SUNDANESE (BASA SUNDA) \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(284, 'SUNDANESE GRAMMAR \u2014 SVO \u00b7 SPEECH LEVELS (UNDAK USUK BASA)')
    g += t(240, 294, 'Sundanese also has a speech level system: Loma (informal), Lemes (polite), Kasar (very informal/crude).', 'middle', 'Ls')
    g += t(240, 303, 'Lemes level used for respected persons and elders. Loma for equals/friends. Kasar to be avoided.', 'middle', 'Lx')
    g += t(240, 312, 'Both Javanese and Sundanese speech level systems reflect Hindu-Buddhist courtly culture of the Majapahit era.', 'middle', 'Lx')
    g += hr(320)

    g += sh(328, 'SUNDANESE SPEECH LEVELS \u2014 SAMPLE')
    slevels = [
        ('Concept', 'Loma (informal)', 'Lemes (polite)'),
        ('I', 'abdi', 'sim kuring'),
        ('eat', 'dahar', 'tuang'),
        ('go', 'indit', 'angkat'),
        ('water', 'cai', 'c\u00e9\u0301 / toya'),
        ('house', 'imah', 'griya'),
    ]
    for i, row in enumerate(slevels):
        y = 338 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx' if i == 0 else 'Ls')
        g += t(240, y, row[1], 'middle', 'Lx' if i == 0 else 'Ls')
        g += t(380, y, row[2], 'middle', 'Lx' if i == 0 else 'Ls')
    g += hr(402)

    g += sh(410, 'SUNDANESE CORE VOCABULARY (LOMA)')
    svocab = [
        ('cai', 'water'), ('seuneu', 'fire'), ('taneuh', 'earth'),
        ('jalma', 'person'), ('bulan', 'moon'), ('inget', 'remember'),
        ('hareup\u00e9un', 'future'), ('merdeka', 'freedom'),
        ('hate', 'heart'), ('cinta', 'love'), ('dunya', 'world'),
        ('hirup', 'life'),
    ]
    for i, (su, en) in enumerate(svocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 420 + row * 10
        g += t(x, y, su, 'middle', 'Ls')
        g += t(x + 58, y, en, 'middle', 'Lx')
    g += hr(465)

    g += sh(473, 'GRAMMAR BRIDGE \u2014 SHARED SPEECH LEVEL CULTURE')
    g += t(240, 483, 'Both Javanese and Sundanese: SVO, Austronesian, agglutinative, elaborate speech levels.', 'middle', 'Ls')
    g += t(240, 492, 'Speech levels are not just politeness: they encode a whole world view about hierarchy and relation.', 'middle', 'Lx')
    g += t(240, 501, 'This is a shared legacy of Hindu-Buddhist Majapahit court culture, adapted independently in each language.', 'middle', 'Lx')

    g += footer('43', 'Javanese', 'Sundanese', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 43D ALT — TEXT ─────────────────────────────────────────────────────

def build_43d_alt():
    g = open_svg()
    g += t(240, 30, 'JAVANESE + SUNDANESE \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 43D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. JAVANESE PROVERB \u2014 ON PATIENCE')
    g += t(240, 73, 'Alon-alon asal kelakon.', 'middle', 'L')
    g += t(240, 84, 'Slowly-slowly  as-long-as accomplished.', 'middle', 'Lx')
    g += t(240, 93, '"Slowly but surely, as long as it is accomplished." \u2014 Core Javanese virtue: kesabaran (patience).', 'middle', 'F')
    g += hr(101)

    g += sh(109, 'II. JAVANESE PROVERB \u2014 ON MEMORY AND ANCESTORS')
    g += t(240, 119, 'Sing sapa lali marang leluhure, bakal nemoni cilaka.', 'middle', 'L')
    g += t(240, 130, 'Who forget  toward  ancestors  will  meet   calamity.', 'middle', 'Lx')
    g += t(240, 139, '"Whoever forgets their ancestors will encounter calamity." \u2014 Javanese ancestral reverence proverb.', 'middle', 'F')
    g += hr(147)

    g += sh(155, 'III. JAVANESE BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 166, 'Iki digawe kanggo kowé, tanpa bayar,', 'middle', 'L')
    g += t(240, 178, 'dening wong-wong sing eling marang masa depan.', 'middle', 'L')
    g += t(240, 190, 'This was-made for you   without pay / by  people  who  remember toward  future-time.', 'middle', 'Lx')
    g += t(240, 199, '"This was made for you, freely, by people who remembered the future." (Javanese, Ngoko level)', 'middle', 'F')
    g += hr(207)

    g += sh(215, 'JAVANESE NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 225, 'Masa depan = future time (from Malay/Indonesian masa = time/era + depan = front/ahead).', 'middle', 'Ls')
    g += t(240, 234, 'Eling = to remember (Ngoko). Kram\u00e0 equivalent: \u00e9ling-\u00e9ling = to keep remembering (iterative).', 'middle', 'Lx')
    g += t(240, 243, 'Tanpa bayar = without paying = freely. Speech level: Ngoko (informal, appropriate for cross-community message).', 'middle', 'Lx')

    g += sec_divider(253, 'SECONDARY \u2014 SUNDANESE (BASA SUNDA) \u2014 RUNNING TEXT')

    g += sh(279, 'I. SUNDANESE PROVERB \u2014 ON COMMUNITY')
    g += t(240, 289, 'Kudu silih asah, silih asih, silih asuh.', 'middle', 'L')
    g += t(240, 300, 'Must mutual-sharpen mutual-love mutual-care.', 'middle', 'Lx')
    g += t(240, 309, '"We must sharpen each other, love each other, care for each other." \u2014 Core Sundanese communal ethics.', 'middle', 'F')
    g += hr(317)

    g += sh(325, 'II. SUNDANESE PROVERB \u2014 ON MEMORY')
    g += t(240, 335, 'Nu teu inget ka purwadaksi, moal uninga ka nu bakal datang.', 'middle', 'L')
    g += t(240, 346, 'Who not  remember to origins    will-not know to what will  come.', 'middle', 'Lx')
    g += t(240, 355, '"Those who do not remember their origins will not know what is coming." (Sundanese memory proverb)', 'middle', 'F')
    g += hr(363)

    g += sh(371, 'III. SUNDANESE BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 382, 'Ieu dijieun keur anjeun, bébas,', 'middle', 'L')
    g += t(240, 394, 'ku jalma-jalma nu inget ka nu bakal datang.', 'middle', 'L')
    g += t(240, 406, 'This made   for you    free / by people   who remember to who will  come.', 'middle', 'Lx')
    g += t(240, 415, '"This was made for you, freely, by people who remembered what is coming." (Sundanese)', 'middle', 'F')
    g += hr(423)

    g += sh(431, 'SUNDANESE NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 441, 'Nu bakal datang = what will come (the one that is going to arrive) \u2014 future as arriving.', 'middle', 'Ls')
    g += t(240, 450, 'Inget = to remember, recall. Bébas = free (physically or as in free of charge).', 'middle', 'Ls')
    g += t(240, 459, 'Silih (mutual) pattern in Sundanese proverb above: three actions, all mutual \u2014 community as reciprocity.', 'middle', 'Lx')
    g += hr(467)

    g += sh(475, 'LANGUAGE BRIDGE \u2014 JAVA\u2019S TWO GREAT VOICES')
    g += t(240, 485, 'Javanese: ~82M speakers. World\u2019s largest language without official national status. Elaborate speech levels.', 'middle', 'Ls')
    g += t(240, 494, 'Sundanese: ~42M speakers. West Java. Own Brahmic script. Silih pattern: mutuality as core value.', 'middle', 'Ls')
    g += t(240, 503, 'Both: Austronesian, shared island, shared Brahmic script heritage, shared speech-level culture.', 'middle', 'Lx')
    g += t(240, 512, 'Different: phonology (breathy consonants), vocabulary, script. Two languages, one island.', 'middle', 'Lx')

    g += footer('43', 'Javanese', 'Sundanese', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate43a_javanese_sundanese_script_alt.svg':    build_43a_alt(),
        'plate43b_javanese_sundanese_phonology_alt.svg': build_43b_alt(),
        'plate43c_javanese_sundanese_grammar_alt.svg':   build_43c_alt(),
        'plate43d_javanese_sundanese_text_alt.svg':      build_43d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
