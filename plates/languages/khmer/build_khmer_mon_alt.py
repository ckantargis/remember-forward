#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Khmer / Mon alt plate series 58A–58D for Remember Forward.
Secondary language: Mon (မောန် / မည်) — spoken in Mon State (Myanmar) and
in the Thai-Burmese border region. ~800,000-1M speakers. Austroasiatic family.
Geographic basis: Phnom Penh (Khmer center) to Mon homeland ~500km.
Mon is historically critical: the Mon script is the ancestor of the Khmer,
Burmese, and Thai scripts. Mon was the dominant culture of mainland SE Asia
before the Khmer and Burmese kingdoms rose. Khmer borrowed their script FROM Mon.
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


# ─── PLATE 58A ALT — SCRIPT ───────────────────────────────────────────────────

def build_58a_alt():
    g = open_svg()
    g += t(240, 30, 'KHMER + MON \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 58A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'KHMER \u2014 KHMER SCRIPT \u00b7 AN ABUGIDA')
    g += t(240, 73, 'Khmer script: descended from South Indian Brahmi via the Pallava and Mon scripts. ~7th c. CE.', 'middle', 'Ls')
    g += t(240, 82, '33 consonants. Inherent vowel /a\u0254/ (a-o). Diacritics above/below/around modify vowels. No tone marks.', 'middle', 'Lx')
    g += t(240, 91, 'Oldest inscription in Southeast Asia using Khmer: Veal Kantel stele (611 CE, Sanskrit + Khmer).', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'KHMER CONSONANTS \u2014 TWO SERIES (A\u2013SERIES AND O\u2013SERIES)')
    g += t(240, 117, 'Khmer consonants belong to two \u201cseries\u201d (registers) that affect the vowel values of diacritics used with them.', 'middle', 'Ls')
    g += t(240, 126, 'A-series (1st register): 15 consonants with \u201ca\u201d quality. O-series (2nd register): 18 with \u201co\u201d quality.', 'middle', 'Lx')
    g += t(240, 135, 'Example: \u1780 (ka, A-series) + \u17B6 = \u1780\u17B6 /kaa/. \u1782 (kho, O-series) + \u17B6 = /k\u028ao/.', 'middle', 'Lx')
    g += hr(143)

    g += sh(151, 'KHMER SAMPLE CONSONANTS')
    kh_cons = [
        ('\u1780','\u1780\u1780a'), ('\u1781','\u1781\u1781ha'), ('\u1782','\u1782\u1782o'), ('\u1783','\u1783\u1783ho'), ('\u1784','\u1784\u1784a'),
        ('\u1785','\u1785\u1785a'), ('\u1786','\u1786\u1786ha'), ('\u1787','\u1787\u1787o'), ('\u1788','\u1788\u1788ho'), ('\u1789','\u1789\u1789o'),
    ]
    for i, (ch, label) in enumerate(kh_cons):
        col = i % 5; row = i // 5
        x = 55 + col * 85; y = 161 + row * 14
        g += t(x, y, ch, 'middle', 'L')
        g += t(x, y + 9, label.replace(ch, ''), 'middle', 'Lx')
    g += hr(198)

    g += sh(206, 'KHMER VOWEL DIACRITICS')
    g += t(240, 216, '\u17B6\u17B7\u17B8\u17B9\u17BA\u17BB\u17BC\u17BD\u17BE\u17BF\u17C0\u17C1\u17C2\u17C3\u17C4\u17C5  (16 main vowel signs)', 'middle', 'L')
    g += t(240, 230, 'Each vowel sign has different phonetic value depending on the register (A or O series) of the consonant.', 'middle', 'Lx')
    g += hr(238)

    g += sh(246, 'KHMER SCRIPT HISTORY')
    g += t(240, 256, 'Mon script (itself Brahmi-derived) \u2192 Khmer script ~7th c. CE \u2192 Khmer passed script to Thai and Lao.', 'middle', 'Ls')
    g += t(240, 265, 'Angkor Wat (built 1113\u201315 CE) inscriptions are primary corpus of classical Khmer. Cambodia\u2019s cultural core.', 'middle', 'Lx')

    g += sec_divider(275, 'SECONDARY \u2014 MON (\u1019\u1014\u103a\u1019\u102c) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(301, 'MON SCRIPT \u2014 ANCESTOR OF KHMER, BURMESE, AND THAI SCRIPTS')
    g += t(240, 311, 'The Mon script is the source script for Khmer, Burmese, and (indirectly) Thai and Lao writing systems.', 'middle', 'Ls')
    g += t(240, 320, 'Mon received Brahmi from South India (~5th c. CE) and became the dominant writing system of mainland SE Asia.', 'middle', 'Lx')
    g += t(240, 329, 'Mon script uses the same Unicode block as Burmese (U+1000\u2013U+109F) with Mon-specific extensions.', 'middle', 'Lx')
    g += hr(337)

    g += sh(345, 'MON SCRIPT SAMPLE CHARACTERS')
    g += t(240, 355, 'Mon uses most Burmese script characters but with different phonetic values.', 'middle', 'Ls')
    mon_sam = [
        ('\u1000', 'ka (same as Burmese)'),
        ('\u1001', 'kha (same)'),
        ('\u1019', 'ma (same shape, same sound)'),
        ('\u101c', 'la (same shape, same sound)'),
    ]
    for i, (ch, note) in enumerate(mon_sam):
        y = 365 + i * 10
        g += t(70, y, ch, 'middle', 'L')
        g += t(270, y, note, 'middle', 'Lx')
    g += hr(412)

    g += sh(420, 'SCRIPT BRIDGE \u2014 PARENT AND CHILD')
    g += t(240, 430, 'Brahmi (India) \u2192 Pallava \u2192 Mon script (~5th c.) \u2192 Khmer script (~7th c.) \u2192 Thai/Lao (~13th c.)', 'middle', 'Ls')
    g += t(240, 439, 'Brahmi (India) \u2192 Pallava \u2192 Mon script (~5th c.) \u2192 Burmese script (~11th c.)', 'middle', 'Ls')
    g += t(240, 448, 'Mon script is the common ancestor of most mainland Southeast Asian writing systems.', 'middle', 'Ls')
    g += t(240, 457, 'Khmer and Mon are now written in related but diverged Brahmic scripts \u2014 the child and the parent.', 'middle', 'Lx')

    g += footer('58', 'Khmer', 'Mon', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 58B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_58b_alt():
    g = open_svg()
    g += t(240, 30, 'KHMER + MON \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 58B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'KHMER PHONOLOGY \u2014 REGISTER SYSTEM (NOT TONAL)')
    g += t(240, 73, 'Khmer is NOT tonal in the Mandarin/Thai sense, but has a \u201cregister\u201d contrast that functions similarly.', 'middle', 'Ls')
    g += t(240, 82, 'Two registers: \u201cchest\u201d voice (lower pitch, breathier) vs. \u201chead\u201d voice (higher, clearer). Historically from tone merger.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'KHMER CONSONANTS \u2014 KEY FEATURES')
    g += t(240, 108, '33 consonants including aspirated pairs: k/kh, c/ch, \u1e6d/\u1e6dh, t/th, p/ph \u2014 voiceless/aspirated.', 'middle', 'Ls')
    g += t(240, 117, 'Implosives: /\u0253/ and /\u0257/ \u2014 present in Khmer. These ingressive sounds add to the distinctive quality.', 'middle', 'Lx')
    g += t(240, 126, 'Final consonant clusters: Khmer allows complex final clusters that are rare in neighboring Thai/Lao.', 'middle', 'Lx')
    g += hr(134)

    g += sh(142, 'KHMER VOWELS \u2014 LONG/SHORT + DIPHTHONGS')
    g += t(240, 152, 'Khmer has ~20+ vowel phonemes including long/short pairs and many diphthongs.', 'middle', 'Ls')
    khv = [
        ('/a/ vs /a\u02d0/', 'short vs. long a'), ('/\u025b/ vs /\u025b\u02d0/', 'short vs. long \u00e9'),
        ('/\u0254/ vs /\u0254\u02d0/', 'short vs. long o'), ('/\u026a/ vs /i\u02d0/', 'short vs. long i'),
        ('/u/ vs /u\u02d0/', 'short vs. long u'), ('/\u0259\u0259/ ', 'schwa-like neutral vowel'),
        ('/ia/', 'diphthong ea'), ('/ua/', 'diphthong oa'),
    ]
    for i, (ipa, desc) in enumerate(khv):
        col = i % 2; row = i // 2
        x = 80 + col * 220; y = 162 + row * 10
        g += t(x, y, ipa, 'middle', 'Lx')
        g += t(x + 55, y, desc, 'middle', 'Lx')
    g += hr(208)

    g += sh(216, 'KHMER STRESS AND RHYTHM')
    g += t(240, 226, 'Stress: typically final syllable of a word. Khmer is neither clearly stress-timed nor syllable-timed.', 'middle', 'Ls')
    g += t(240, 235, 'Many words have an unstressed \u201cminor syllable\u201d (schwa + consonant) preceding the main syllable: bpram (five) = bp + ram.', 'middle', 'Lx')

    g += sec_divider(245, 'SECONDARY \u2014 MON \u2014 PHONOLOGY')

    g += sh(271, 'MON PHONOLOGY \u2014 REGISTERS + TONES')
    g += t(240, 281, 'Mon has TWO registers (like Khmer) PLUS 2 tones, giving 4 phonological distinctions per vowel.', 'middle', 'Ls')
    g += t(240, 290, 'Register 1 (low): modal voice + low/mid pitch. Register 2 (high): creaky voice + high/falling pitch.', 'middle', 'Lx')
    g += t(240, 299, 'This is historically earlier than Khmer\u2019s system \u2014 Mon preserved both register and tone contrast.', 'middle', 'Lx')
    g += hr(307)

    g += sh(315, 'MON VOWELS \u2014 RICH SYSTEM')
    g += t(240, 325, 'Mon has ~30+ vowel phonemes across registers and tones. One of the most complex vowel systems in SE Asia.', 'middle', 'Ls')
    g += t(240, 334, 'Like Khmer, Mon has short/long pairs and many diphthongs. Mon may have preserved archaic Austroasiatic vowels.', 'middle', 'Lx')
    g += hr(342)

    g += sh(350, 'MON CONSONANTS')
    g += t(240, 360, 'Mon has 31 consonants including voiced aspirates (b\u02b0 d\u02b0) \u2014 rare in mainland Southeast Asia.', 'middle', 'Ls')
    g += t(240, 369, 'Also: implosives /\u0253 \u0257/, the labial-velar /kp/, and prenasalized stops /mb nd \u014bg/.', 'middle', 'Lx')
    g += hr(377)

    g += sh(385, 'PHONOLOGICAL BRIDGE \u2014 SHARED AUSTROASIATIC FEATURES')
    comp = [
        ('Feature', 'Khmer', 'Mon'),
        ('Register', '2 registers', '2 registers + 2 tones'),
        ('Tonal', 'No (register only)', 'Yes (register + tone)'),
        ('Implosives', 'Yes /\u0253 \u0257/', 'Yes /\u0253 \u0257/'),
        ('Vowel count', '~20', '~30'),
        ('Script origin', 'Mon-derived', 'Brahmi/Pallava'),
    ]
    for i, row in enumerate(comp):
        y = 395 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('58', 'Khmer', 'Mon', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 58C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_58c_alt():
    g = open_svg()
    g += t(240, 30, 'KHMER + MON \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 58C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'KHMER GRAMMAR \u2014 SVO \u00b7 ISOLATING \u00b7 NO INFLECTION')
    g += t(240, 73, 'Khmer is SVO and highly isolating. Grammatical relations expressed by word order and particles.', 'middle', 'Ls')
    g += t(240, 82, 'No inflection for tense, number, gender, or case. Aspect markers placed before/after verbs.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'KHMER ASPECT AND TENSE MARKERS')
    kh_asp = [
        ('\u1794\u17b6\u1793 (baan)', 'completive past: \u1781\u17d2\u1789\u17bb\u1798 baan si (ate \u2014 completed)'),
        ('\u1793\u17c9\u1784 (ning)', 'future: \u1793\u17c9\u1784 tow (will go)'),
        ('\u1780\u17c6\u1796\u17bb\u1784 (kampung)', 'progressive: am doing'),
        ('\u1794\u17b6\u1793\u1787\u17b6 (baanjaa)', 'already done: have already eaten'),
    ]
    for i, (marker, gloss) in enumerate(kh_asp):
        y = 108 + i * 11
        g += t(90, y, marker, 'middle', 'Ls')
        g += t(300, y, gloss, 'middle', 'Lx')
    g += hr(155)

    g += sh(163, 'KHMER CORE VOCABULARY')
    kvocab = [
        ('\u178f\u17b9\u1780 t\u1ecbk', 'water'), ('\u1779\u17d2\u1793\u17b9\u1784 ph\u0148l\u0153ng', 'fire'), ('\u178f\u17d2\u1798\u17b8 tmei', 'earth'),
        ('\u1798\u1793\u17bb\u179f\u17d2\u179f mnu\u1e63\u1e63', 'person'), ('\u1785\u1793\u17d2\u1791\u17d2\u179a chan', 'moon'), ('\u1785\u1784\u17d4\u1787\u17b6\u1798 ch\u0103mja\u0304m', 'remember'),
        ('\u1799\u1780\u1780\u17b6\u179b anakot', 'future'), ('\u179f\u17b9\u179a\u17b7\u1797\u17b6\u1796 seriphiap', 'freedom'),
        ('\u1785\u17b7\u178f\u17d4 chi\u0304t', 'heart'), ('\u179f\u17c1\u1785\u1780\u17d4\u1782\u17d2\u1793\u17b6 sech\u0103kgn\u0101', 'love'),
        ('\u1796\u17b7\u1797\u1796\u179b\u17b9\u1780 ph\u012bph\u0254\u0304l\u0153k', 'world'), ('\u1787\u17b8\u179c\u17b7\u178f ji\u0304vit', 'life'),
    ]
    for i, (kh, en) in enumerate(kvocab):
        col = i % 3; row = i // 3
        x = 55 + col * 130; y = 173 + row * 10
        g += t(x, y, kh, 'middle', 'Lx')
        g += t(x + 68, y, en, 'middle', 'Lx')

    g += sec_divider(220, 'SECONDARY \u2014 MON \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(246, 'MON GRAMMAR \u2014 SVO \u00b7 ISOLATING \u00b7 CLASSIFIER SYSTEM')
    g += t(240, 256, 'Mon is SVO and isolating \u2014 same as Khmer. Both Austroasiatic languages share this structural feature.', 'middle', 'Ls')
    g += t(240, 265, 'Mon has a rich classifier system: nouns use classifiers when counted. Different for humans, animals, flat things.', 'middle', 'Lx')
    g += t(240, 274, 'No inflection for tense, number, or gender. Context, particles, and time words signal tense.', 'middle', 'Lx')
    g += hr(282)

    g += sh(290, 'MON CORE VOCABULARY')
    mvocab = [
        ('krui\u0304', 'water'), ('me', 'fire'), ('pa\u014b', 'earth/land'),
        ('mi\u0254', 'person'), ('kl\u025bh', 'moon'), ('yo\u0304m', 'remember'),
        ('pat\u0254n', 'future'), ('cetana\u0304', 'freedom'),
        ('ni\u0254', 'heart'), ('y\u0101\u014b', 'love'), ('bhav', 'world'),
        ('\u0101yu', 'life'),
    ]
    for i, (mo, en) in enumerate(mvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 300 + row * 10
        g += t(x, y, mo, 'middle', 'Ls')
        g += t(x + 58, y, en, 'middle', 'Lx')
    g += hr(348)

    g += sh(356, 'SIDE-BY-SIDE \u2014 KHMER VS. MON (SAME FAMILY)')
    comp = [
        ('CONCEPT', 'KHMER', 'MON'),
        ('water', 't\u1ecbk (\u178f\u17b9\u1780)', 'krui\u0304'),
        ('fire', 'ph\u0148l\u0153ng', 'me'),
        ('person', 'mnu\u1e63\u1e63', 'mi\u0254'),
        ('moon', 'chan', 'kl\u025bh'),
        ('life', 'ji\u0304vit', '\u0101yu'),
    ]
    for i, row in enumerate(comp):
        y = 366 + i * 11
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(240, y, row[1], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(380, y, row[2], 'middle', 'Ls' if i > 0 else 'Lx')
    g += hr(435)

    g += sh(443, 'GRAMMAR BRIDGE \u2014 AUSTROASIATIC COUSINS')
    g += t(240, 453, 'Khmer and Mon are the two major branches of Austroasiatic: Khmeric and Monic. Shared deep grammar.', 'middle', 'Ls')
    g += t(240, 462, 'SVO, isolating, classifier systems, no inflection \u2014 all hallmarks of Austroasiatic structure.', 'middle', 'Ls')
    g += t(240, 471, 'Mon\u2019s historical dominance (Dvaravati, Haripunjaya kingdoms) shaped all of mainland SE Asia\u2019s writing systems.', 'middle', 'Lx')

    g += footer('58', 'Khmer', 'Mon', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 58D ALT — TEXT ─────────────────────────────────────────────────────

def build_58d_alt():
    g = open_svg()
    g += t(240, 30, 'KHMER + MON \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 58D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. KHMER PROVERB \u2014 ON WATER')
    g += t(240, 73, '\u178f\u17b9\u1780\u1785\u17d2\u179a\u17b9\u1793\u1785\u17d2\u179a\u17c2\u1793\u178f\u17c2\u1789 \u1780\u17bb\u1798\u17d2\u1794\u17b6\u179b\u1798\u17b7\u1793\u1791\u17b9\u1780\u178f\u17b9\u1780\u1787\u17b8\u179c\u17b7\u178f\u1787\u17b6\u1793\u1785\u17d2\u179a\u17b9\u1793\u1787\u17b8\u179c\u17b7\u178f\u1793\u17c9\u17bc\u1780', 'middle', 'Ls')
    g += t(240, 87, 'T\u1ecbk ch\u0103roen ch\u0113n t\u0113y, kumpal min t\u1ecbk ji\u0304vit ja\u0304n ch\u0103roen ji\u0304vit noek.', 'middle', 'Ls')
    g += t(240, 96, '"Water flowing downstream never stops; cannot stop the river of life either." (Khmer proverb)', 'middle', 'F')
    g += hr(104)

    g += sh(112, 'II. ANGKOR WAT INSCRIPTION \u2014 ON TIME (~12TH C. CE)')
    g += t(240, 122, 'Yasa\u1e6dha niri\u0302yam\u0101nam pi\u0304\u1e47\u1e0da m\u0101\u1e47atv\u0101 sarvam etad iti cetasi...', 'middle', 'Ls')
    g += t(240, 132, 'Sanskrit: \u201cKnowing all this to be impermanent in one\u2019s heart...\u201d \u2014 Angkor inscription fragment.', 'middle', 'Lx')
    g += t(240, 141, 'Khmer inscriptions often mixed Sanskrit with Khmer \u2014 the language of the gods alongside the language of the people.', 'middle', 'F')
    g += hr(149)

    g += sh(157, 'III. KHMER BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 168, '\u1793\u17c1\u17a0\u17d0\u1780\u1793\u17c1\u17a0\u1780\u17d2\u179a\u1798\u1794\u17b6\u1793\u1787\u17b6\u179f\u1798\u17d2\u179a\u17b6\u1794\u17cb\u17a2\u17d2\u1793\u1780\u178f\u17be\u178f\u1798\u17d2\u179b\u17c1\u1785\u1787\u17b6\u1798\u1793\u17c1\u17a0\u1780\u179f\u17bc\u1798 \u178f\u17b9\u1780\u17b6\u1793\u17cb\u1785\u1784\u17d4\u1787\u17b6\u1798\u17b6\u1793\u1780\u17b6\u179b\u1796\u17d2\u179a\u17c2', 'middle', 'Ls')
    g += t(240, 183, 'N\u0113h baan ja\u0304 samr\u0101p anak t\u0113 tmel jaa mn\u0113h ks\u016bm \u00b7 ti\u0304k\u0101\u014b chan j\u0101m k\u0101l phr\u0113y', 'middle', 'Lx')
    g += t(240, 192, '"This was made for you, freely, by people who remembered the future." (Khmer)', 'middle', 'F')
    g += hr(200)

    g += sh(208, 'KHMER NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 218, 'Anakot (\u1799\u1780\u1780\u17b6\u179b) = future (from Sanskrit an\u0101gata \u201cnot yet come\u201d). Chan j\u0101m = remember.', 'middle', 'Ls')
    g += t(240, 227, 'Sanskrit loanwords dominate Khmer abstract vocabulary \u2014 the legacy of Angkor\u2019s Hindu-Buddhist civilization.', 'middle', 'Lx')

    g += sec_divider(237, 'SECONDARY \u2014 MON \u2014 RUNNING TEXT')

    g += sh(263, 'I. MON PROVERB \u2014 ON MEMORY AND RIVERS')
    g += t(240, 273, 'Krui\u0304 l\u0254p p\u0101 ceika\u0304, mi\u0254 l\u0254p p\u0101 yo\u0304m.', 'middle', 'L')
    g += t(240, 284, 'River flows to  sea   person flows to  memory.', 'middle', 'Lx')
    g += t(240, 293, '"The river flows to the sea; a person flows into memory." (Mon proverb on the persistence of the dead in memory)', 'middle', 'F')
    g += hr(301)

    g += sh(309, 'II. MON INSCRIPTION \u2014 WAT MAHEYONG (~11TH C. CE)')
    g += t(240, 319, 'Restored Mon text: \u201cBy the merit of this deed, may all sentient beings attain peace.\u201d', 'middle', 'Ls')
    g += t(240, 328, 'Mon temple inscriptions (~11th\u201313th c.) are among the oldest texts of mainland Southeast Asia.', 'middle', 'Lx')
    g += hr(336)

    g += sh(344, 'III. MON BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 355, 'N\u025b kr\u0254 mi\u0254 kl\u025bh samr\u0101p c\u0101\u014b, dot kr\u0101k,', 'middle', 'L')
    g += t(240, 367, 'yo\u0304m mi\u0254 pat\u0254n h\u0254n.', 'middle', 'L')
    g += t(240, 379, 'This by people made for you freely / remember person future also.', 'middle', 'Lx')
    g += t(240, 388, '"This was made for you, freely, by people who remembered the future." (Mon)', 'middle', 'F')
    g += hr(396)

    g += sh(404, 'MON NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 414, 'Pat\u0254n = future/ahead (lit. the forward path). Yo\u0304m = to remember, to keep in heart.', 'middle', 'Ls')
    g += t(240, 423, 'Dot kr\u0101k = freely/without cost (lit. without price). Mon preserves archaic Austroasiatic vocabulary.', 'middle', 'Lx')
    g += hr(431)

    g += sh(439, 'LANGUAGE BRIDGE \u2014 A PARENT AND ITS CHILD')
    g += t(240, 449, 'Mon: ~800K speakers. Endangered. Once the dominant culture of mainland SE Asia. Ancestor of Khmer script.', 'middle', 'Ls')
    g += t(240, 458, 'Khmer: ~16M speakers. Official language of Cambodia. Inherited its script from Mon. Now the larger language.', 'middle', 'Ls')
    g += t(240, 467, 'History reversed: the child-script (Khmer) now belongs to a larger community than the parent (Mon).', 'middle', 'Lx')
    g += t(240, 476, 'This plate pairs them as equals \u2014 a reminder that cultural inheritance runs in all directions.', 'middle', 'Lx')

    g += footer('58', 'Khmer', 'Mon', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate58a_khmer_mon_script_alt.svg':    build_58a_alt(),
        'plate58b_khmer_mon_phonology_alt.svg': build_58b_alt(),
        'plate58c_khmer_mon_grammar_alt.svg':   build_58c_alt(),
        'plate58d_khmer_mon_text_alt.svg':      build_58d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
