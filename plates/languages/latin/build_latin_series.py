#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Latin plate series 22A–22D for Remember Forward."""

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


def footer(series_num, lang_name, plate_letter, descriptor):
    lines = []
    lines.append(hr(625))
    lines.append(t(240, 620, f'SERIES {series_num} \u00b7 {lang_name.upper()} \u00b7 PLATE {plate_letter} \u00b7 {descriptor.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG', 'middle', 'M'))
    lines.append(hr(633))
    lines.append(t(240, 648, 'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.', 'middle', 'Fb'))
    lines.append(t(240, 663, 'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET', 'middle', 'F'))
    return ''.join(lines)


# ─── PLATE 22A — SCRIPT ──────────────────────────────────────────────────────

def build_22a():
    g = open_svg()
    g += t(240, 32, 'LATIN — SCRIPT · WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 22A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'THE LATIN ALPHABET — ORIGIN AND SPREAD')
    g += t(240, 79, 'Latin is written in the Latin alphabet — the most widely used writing system on Earth today.', 'middle', 'L')
    g += t(240, 89, 'Descended from Etruscan script (7th c. BCE), itself from Greek, ultimately from Phoenician.', 'middle', 'Ls')
    g += t(240, 98, 'Classical Latin used 23 letters. Modern Latin-based alphabets vary from 18 (Hawaiian) to 40+ letters.', 'middle', 'Ls')
    g += hr(106)

    # Classical alphabet
    g += sh(115, 'CLASSICAL LATIN ALPHABET — 23 LETTERS')
    g += t(240, 125, 'Letters I/J and U/V were single letters in Classical Latin (I=vowel/consonant; V=vowel/consonant).', 'middle', 'Lx')
    g += t(240, 133, 'Letter W did not exist. K and Y/Z were rare (used in Greek loanwords only).', 'middle', 'Lx')

    classical = [
        ('A', 'a', '/a/', 'as in "father"'),
        ('B', 'b', '/b/', 'bilabial stop'),
        ('C', 'c', '/k/', 'always hard [k]; no /s/ in Classical Latin'),
        ('D', 'd', '/d/', 'alveolar stop'),
        ('E', 'e', '/e/', 'short, like "bed"'),
        ('F', 'f', '/f/', 'labiodental fricative'),
        ('G', 'g', '/ɡ/', 'always hard [g]'),
        ('H', 'h', '/h/', 'weakly aspirated, often silent'),
        ('I', 'i', '/i/ or /j/', 'vowel or glide (consonant before vowel)'),
        ('K', 'k', '/k/', 'rare; used in Kalendae and Greek loans'),
        ('L', 'l', '/l/', 'lateral approximant'),
        ('M', 'm', '/m/', 'bilabial nasal'),
        ('N', 'n', '/n/', 'alveolar nasal; [ŋ] before velar'),
        ('O', 'o', '/o/', 'mid back vowel'),
        ('P', 'p', '/p/', 'bilabial stop, unaspirated'),
        ('Q', 'q', '/k/', 'used only before V: QV = [kw]'),
        ('R', 'r', '/r/', 'trilled alveolar [r]'),
        ('S', 's', '/s/', 'always voiceless [s]'),
        ('T', 't', '/t/', 'alveolar stop, unaspirated'),
        ('V', 'v', '/u/ or /w/', 'vowel [u] or consonant [w]'),
        ('X', 'x', '/ks/', 'digraph sound'),
        ('Y', 'y', '/y/', 'Greek upsilon; rare in loans'),
        ('Z', 'z', '/z/', 'Greek zeta; rare in loans'),
    ]

    col_x = [32, 60, 95, 155, 360]
    g += t(32,  143, 'MAJ', 'middle', 'Lx')
    g += t(60,  143, 'min', 'middle', 'Lx')
    g += t(95,  143, 'IPA', 'middle', 'Lx')
    g += t(270, 143, 'Notes', 'middle', 'Lx')
    for i, (maj, mn, ipa, note) in enumerate(classical):
        y = 151 + i * 9
        g += t(32,  y, maj, 'middle', 'Ls')
        g += t(60,  y, mn, 'middle', 'Lx')
        g += t(95,  y, ipa, 'middle', 'Lx')
        g += t(275, y, note, 'middle', 'Lx')
    g += hr(360)

    # Numerals
    g += sh(368, 'ROMAN NUMERALS')
    g += t(240, 378, 'Additive-subtractive system using letter symbols. No zero. Positional value limited.', 'middle', 'Ls')
    nums = [
        ('I=1', 'V=5', 'X=10', 'L=50'),
        ('C=100', 'D=500', 'M=1000', ''),
    ]
    for ri, row in enumerate(nums):
        for ci, val in enumerate(row):
            if val:
                g += t(80 + ci * 90, 388 + ri * 10, val, 'middle', 'Ls')

    g += t(240, 409, 'Subtraction rule: smaller before larger = subtract (IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)', 'middle', 'Lx')
    g += t(240, 418, 'MCMXCIX = 1999 · MMXXVI = 2026 · Overbar: V\u0305 = 5000 · M\u0305 = 1,000,000', 'middle', 'Lx')
    g += hr(427)

    # Script history
    g += sh(436, 'SCRIPT HISTORY AND EVOLUTION')
    g += t(240, 447, '~700 BCE: Etruscan alphabet adapted from western Greek (Euboean) variant at Cumae', 'middle', 'Ls')
    g += t(240, 456, '~600 BCE: Romans adapt Etruscan alphabet — dropping unused letters, adding G (Spurius Carvilius, 3rd c.)', 'middle', 'Ls')
    g += t(240, 465, '1st c. BCE: Classical 23-letter Latin alphabet stabilized — monumental inscriptions (CAPITALIS QUADRATA)', 'middle', 'Ls')
    g += t(240, 474, '2nd–4th c. CE: Rustic capitals (handwriting), then uncial (rounded) for manuscripts', 'middle', 'Ls')
    g += t(240, 483, '8th–9th c.: Carolingian minuscule — lowercase letters standardized by Alcuin under Charlemagne', 'middle', 'Ls')
    g += t(240, 492, '15th c.: Humanist script (basis of modern Roman type) — Poggio Bracciolini from Carolingian models', 'middle', 'Ls')
    g += t(240, 501, '1450s: Gutenberg moveable type — Latin letters cast in metal, spread Latin alphabet globally', 'middle', 'Ls')
    g += hr(510)

    g += sh(519, 'INSCRIPTION EXAMPLE — TRAJAN\'S COLUMN, 113 CE')
    g += t(240, 530, 'SENATVS POPVLVSQVE ROMANVS', 'middle', 'L')
    g += t(240, 540, 'Senatus Populusque Romanus', 'middle', 'Lx')
    g += t(240, 549, '"The Senate and People of Rome" — SPQR, official motto of Rome, still used today', 'middle', 'Ls')
    g += t(240, 558, 'Note V for both U and W sounds · Q followed by V as [kw] · No word spacing in early inscriptions', 'middle', 'Lx')
    g += hr(566)

    g += sh(575, 'MODERN LATIN ALPHABET (26 LETTERS)')
    g += t(240, 585, 'Added letters: J (from I, ~15th c.) · U (from V, vowel use, ~16th c.) · W (from VV, ~10th c. Germanic)', 'middle', 'Ls')
    g += t(240, 595, 'Modern variants add diacritics: é ñ ü ç ø ă — same 26 base letters underlie ~70 national alphabets', 'middle', 'Ls')
    g += t(240, 604, 'Latin alphabet now writes: English, Spanish, French, Portuguese, German, Malay, Swahili, Vietnamese, and more', 'middle', 'Ls')
    g += t(240, 613, 'Estimated 4+ billion people read some form of Latin-script language today', 'middle', 'Ls')

    g += footer('22', 'Latin', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 22B — PHONOLOGY ───────────────────────────────────────────────────

def build_22b():
    g = open_svg()
    g += t(240, 32, 'LATIN — PHONOLOGY · SOUND SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 22B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'CLASSICAL LATIN PRONUNCIATION')
    g += t(240, 79, 'Classical Latin (1st c. BCE – 2nd c. CE) pronunciation reconstructed from grammarians, meter, and borrowings.', 'middle', 'L')
    g += t(240, 89, 'Latin is quantity-sensitive: vowel length (short vs. long) is phonemic — it changes meaning.', 'middle', 'Ls')
    g += t(240, 98, 'malum (short a) = "evil" · mālum (long ā) = "apple" — distinguished only by vowel length', 'middle', 'Ls')
    g += hr(106)

    # Vowel system
    g += sh(115, 'VOWELS — 5 SHORT + 5 LONG')
    vowel_data = [
        ('a / ā', '/a/ vs /aː/', 'low central open', 'pater / māter'),
        ('e / ē', '/e/ vs /eː/', 'mid front', 'et / rēx'),
        ('i / ī', '/i/ vs /iː/', 'high front', 'in / vīta'),
        ('o / ō', '/o/ vs /oː/', 'mid back rounded', 'os / vōx'),
        ('u / ū', '/u/ vs /uː/', 'high back rounded', 'ut / lūna'),
        ('y / ȳ', '/y/ vs /yː/', 'high front rounded (Greek loans)', 'tyrannus'),
    ]
    g += t(55,  125, 'Letter', 'middle', 'Lx')
    g += t(130, 125, 'IPA', 'middle', 'Lx')
    g += t(250, 125, 'Quality', 'middle', 'Lx')
    g += t(390, 125, 'Example', 'middle', 'Lx')
    for i, (ltr, ipa, qual, ex) in enumerate(vowel_data):
        y = 134 + i * 11
        g += t(55,  y, ltr, 'middle', 'Ls')
        g += t(130, y, ipa, 'middle', 'Lx')
        g += t(250, y, qual, 'middle', 'Lx')
        g += t(390, y, ex, 'middle', 'Lx')

    # Diphthongs
    g += t(240, 206, 'Diphthongs: ae /ae\u0306/ → "eye" · oe /oe\u0306/ → rare · au /au\u0306/ → "ow" · eu /eu\u0306/ → rare', 'middle', 'Ls')
    g += hr(214)

    # Consonants
    g += sh(223, 'CONSONANT INVENTORY')
    cons = [
        ('p b', '/p b/', 'bilabial stops', 'unaspirated — pater, bellum'),
        ('t d', '/t d/', 'alveolar stops', 'unaspirated — terra, deus'),
        ('c g', '/k ɡ/', 'velar stops', 'always hard — caelum, gloria'),
        ('f',   '/f/',   'labiodental fricative', 'filia, fortis'),
        ('s',   '/s/',   'always voiceless', 'sol, rosa (never /z/)'),
        ('h',   '/h/',   'glottal, often silent', 'homo, herba'),
        ('m n', '/m n/', 'nasals', '[ŋ] before velars: nunc /nuŋk/'),
        ('l r', '/l r/', 'lateral / trill', 'r = trilled [r], l = clear [l]'),
        ('v',   '/w/',   'labio-velar glide', 'vir = [wir], not [vir]'),
        ('i/j', '/j/',   'palatal glide', 'iam = [jam], iocus = [jokus]'),
        ('qu', '/kw/',  'labiovelar cluster', 'quis, aqua = /akwa/'),
        ('x',  '/ks/',  'consonant cluster', 'rex /reks/'),
        ('z',  '/z/ or /dz/', 'Greek loans only', 'zona /zona/'),
    ]
    for i, (ltr, ipa, label, note) in enumerate(cons):
        y = 233 + i * 12
        g += t(45,  y, ltr, 'middle', 'Ls')
        g += t(100, y, ipa, 'middle', 'Lx')
        g += t(185, y, label, 'middle', 'Lx')
        g += t(360, y, note, 'middle', 'Lx')
    g += hr(394)

    # Quantity and stress
    g += sh(403, 'SYLLABLE QUANTITY AND STRESS')
    g += t(240, 414, 'A syllable is HEAVY (long) if: (1) it contains a long vowel/diphthong, OR (2) it is closed by a consonant.', 'middle', 'L')
    g += t(240, 424, 'A syllable is LIGHT (short) if: it contains a short vowel and ends in that vowel.', 'middle', 'Ls')
    g += t(240, 433, 'Stress rule: stress the PENULTIMATE (second-to-last) syllable IF it is heavy.', 'middle', 'Ls')
    g += t(240, 442, 'If penultimate is light, stress falls on ANTEPENULTIMATE (third from last).', 'middle', 'Ls')
    g += t(240, 451, 'Two-syllable words: always stress first syllable.', 'middle', 'Ls')
    g += t(240, 460, 'amī-cus: ami- heavy (long ī) → stress ami- → a-MĪ-cus', 'middle', 'Lx')
    g += t(240, 469, 'do-mi-nus: -mi- light (short i, open) → stress DOM- → DŌ-mi-nus', 'middle', 'Lx')
    g += t(240, 478, 're-pub-li-ca: -pub- heavy (closed by b) → stress -pub- → re-PŪB-li-ca', 'middle', 'Lx')
    g += hr(486)

    # Prosody
    g += sh(495, 'POETIC METER — DACTYLIC HEXAMETER')
    g += t(240, 506, 'Homer and Virgil use dactylic hexameter: six feet per line, dactyl (— ∪ ∪) or spondee (— —).', 'middle', 'L')
    g += t(240, 516, 'Arma virumque cano — AR-ma vi-RUM-que CA-no (Aeneid I.1)', 'middle', 'Ls')
    g += t(240, 525, '— ∪∪ | — — | — — | — ∪∪ | — ∪∪ | — —', 'middle', 'Lx')
    g += t(240, 534, '"I sing of arms and the man" — quantity-based, NOT stress-based meter', 'middle', 'Ls')
    g += hr(542)

    g += sh(551, 'VOWEL CHANGES IN VULGAR LATIN → ROMANCE')
    g += t(240, 562, 'By 4th–5th c. CE: vowel length distinctions collapsed; stressed syllable quality (open/close) replaced them.', 'middle', 'Ls')
    g += t(240, 571, 'This collapse drove Romance divergence: Latin ē and ĭ merged in many areas; ō and ŭ merged elsewhere.', 'middle', 'Ls')
    g += t(240, 580, 'Latin caballum → Spanish caballo, French cheval, Italian cavallo, Portuguese cavalo', 'middle', 'Ls')
    g += t(240, 589, 'Latin noctem → Spanish noche, French nuit, Italian notte, Portuguese noite', 'middle', 'Ls')
    g += t(240, 598, 'The sound changes that built five modern languages are visible in the Latin source words.', 'middle', 'Ls')

    g += footer('22', 'Latin', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 22C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_22c():
    g = open_svg()
    g += t(240, 32, 'LATIN — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 22C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'INFLECTED LANGUAGE — SIX NOUN CASES')
    g += t(240, 79, 'Latin is highly inflected: endings mark grammatical role, not word order. Word order is flexible.', 'middle', 'L')
    g += t(240, 89, 'Nouns decline for: CASE (6) × NUMBER (singular/plural) × GENDER (M/F/N) × DECLENSION (5 patterns).', 'middle', 'Ls')

    cases = [
        ('Nominative', 'NOM', 'Subject', 'Puella amat.', 'The girl loves.'),
        ('Genitive', 'GEN', 'Possession / of', 'amor puellae', 'love of the girl'),
        ('Dative', 'DAT', 'Indirect object / to', 'dat puellae', 'gives to the girl'),
        ('Accusative', 'ACC', 'Direct object', 'amat puellam', 'loves the girl'),
        ('Ablative', 'ABL', 'By/with/from/in', 'cum puellā', 'with the girl'),
        ('Vocative', 'VOC', 'Direct address', 'O puella!', 'O girl!'),
    ]
    g += t(60,  99, 'Case', 'middle', 'Lx')
    g += t(115, 99, 'Abbr', 'middle', 'Lx')
    g += t(185, 99, 'Function', 'middle', 'Lx')
    g += t(310, 99, 'Example', 'middle', 'Lx')
    g += t(415, 99, 'Gloss', 'middle', 'Lx')
    for i, (case, abbr, func, ex, gl) in enumerate(cases):
        y = 108 + i * 11
        g += t(60,  y, case, 'middle', 'Lx')
        g += t(115, y, abbr, 'middle', 'Lx')
        g += t(185, y, func, 'middle', 'Lx')
        g += t(310, y, ex, 'middle', 'Lx')
        g += t(415, y, gl, 'middle', 'Lx')
    g += hr(177)

    # 1st declension
    g += sh(186, '1ST DECLENSION — puella "girl" (Feminine)')
    g += t(240, 196, 'Pattern -a stems: puella, terra, aqua, via, luna, stella — mostly feminine nouns', 'middle', 'Lx')
    dec1 = [
        ('NOM', 'puella', 'puellae'),
        ('GEN', 'puellae', 'puellarum'),
        ('DAT', 'puellae', 'puellis'),
        ('ACC', 'puellam', 'puellas'),
        ('ABL', 'puellā', 'puellis'),
        ('VOC', 'puella', 'puellae'),
    ]
    g += t(120, 204, 'Singular', 'middle', 'Lx')
    g += t(320, 204, 'Plural', 'middle', 'Lx')
    for i, (case, sg, pl) in enumerate(dec1):
        y = 212 + i * 9
        g += t(60, y, case, 'middle', 'Lx')
        g += t(155, y, sg, 'middle', 'Ls')
        g += t(320, y, pl, 'middle', 'Ls')
    g += hr(269)

    # Verb system
    g += sh(278, 'VERB SYSTEM — amare "to love"')
    g += t(240, 288, 'Latin verbs conjugate for: PERSON (1/2/3) × NUMBER (sg/pl) × TENSE × MOOD × VOICE (active/passive).', 'middle', 'Ls')
    g += t(240, 297, '6 tenses: present, imperfect, future, perfect, pluperfect, future perfect.', 'middle', 'Lx')
    g += t(240, 306, '4 moods: indicative, subjunctive, imperative, infinitive.', 'middle', 'Lx')

    present = [
        ('1sg', 'amō', 'I love'),
        ('2sg', 'amās', 'you love'),
        ('3sg', 'amat', 'he/she/it loves'),
        ('1pl', 'amāmus', 'we love'),
        ('2pl', 'amātis', 'you (pl) love'),
        ('3pl', 'amant', 'they love'),
    ]
    g += t(120, 314, 'Present Active Indicative', 'middle', 'Lx')
    for i, (person, form, gloss) in enumerate(present):
        y = 322 + i * 10
        g += t(70, y, person, 'middle', 'Lx')
        g += t(155, y, form, 'middle', 'Ls')
        g += t(270, y, gloss, 'middle', 'Lx')

    # Perfect
    perfect = [
        ('1sg', 'amāvī', 'I loved / have loved'),
        ('2sg', 'amāvistī', 'you loved'),
        ('3sg', 'amāvit', 'he/she loved'),
        ('1pl', 'amāvimus', 'we loved'),
        ('2pl', 'amāvistis', 'you (pl) loved'),
        ('3pl', 'amāvērunt', 'they loved'),
    ]
    g += t(360, 314, 'Perfect Active Indicative', 'middle', 'Lx')
    for i, (person, form, gloss) in enumerate(perfect):
        y = 322 + i * 10
        g += t(320, y, person, 'middle', 'Lx')
        g += t(385, y, form, 'middle', 'Ls')
        g += t(450, y, gloss, 'start', 'Lx')
    g += hr(386)

    # Core vocabulary
    g += sh(395, 'CORE VOCABULARY — 25 WORDS')
    vocab = [
        ('ita / non', 'yes / no'),
        ('et / sed', 'and / but'),
        ('ego / tu', 'I / you'),
        ('hic / ille', 'this / that'),
        ('ubi', 'where'),
        ('quid', 'what'),
        ('quando', 'when'),
        ('quis', 'who'),
        ('cur', 'why'),
        ('aqua', 'water'),
        ('ignis', 'fire'),
        ('terra', 'earth'),
        ('homo', 'human being'),
        ('deus', 'god'),
        ('vita', 'life'),
        ('mors', 'death'),
        ('tempus', 'time'),
        ('lux', 'light'),
        ('verba', 'words'),
        ('memoria', 'memory'),
        ('futurum', 'the future'),
        ('liber', 'book / free'),
        ('pax', 'peace'),
        ('amor', 'love'),
        ('omnia', 'all things'),
    ]
    col_va = [70, 200]
    col_vb = [300, 430]
    half = len(vocab) // 2 + len(vocab) % 2
    for i, (lat, eng) in enumerate(vocab):
        if i < half:
            y = 405 + i * 10
            g += t(col_va[0], y, lat, 'middle', 'Ls')
            g += t(col_va[1], y, eng, 'middle', 'Lx')
        else:
            y = 405 + (i - half) * 10
            g += t(col_vb[0], y, lat, 'middle', 'Ls')
            g += t(col_vb[1], y, eng, 'middle', 'Lx')
    g += hr(540)

    # Word order note
    g += sh(549, 'WORD ORDER AND STYLE')
    g += t(240, 560, 'Latin has NO fixed word order — case endings carry meaning. Any order is grammatically valid.', 'middle', 'L')
    g += t(240, 570, 'Preferred order: SOV in prose (Caesar, Cicero). Verb-final marks emphasis and closure.', 'middle', 'Ls')
    g += t(240, 579, '"Gallia est omnis divisa in partes tres" — Gaul as a whole is divided into three parts (Caesar, BG I.1)', 'middle', 'Ls')
    g += t(240, 588, 'Adjectives usually follow their noun; possessives precede; emphatics can go anywhere.', 'middle', 'Ls')
    g += t(240, 597, 'No definite or indefinite article (no "the" / "a"). Context determines specificity.', 'middle', 'Ls')
    g += t(240, 606, 'Latin vocabulary survives in: ~60% of English vocabulary, legal/scientific/medical terms worldwide.', 'middle', 'Ls')

    g += footer('22', 'Latin', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 22D — RUNNING TEXT ─────────────────────────────────────────────────

def build_22d():
    g = open_svg()
    g += t(240, 32, 'LATIN — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 22D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1 — Virgil
    g += sh(67, 'PASSAGE 1 — VIRGIL, AENEID I.1–3 (19 BCE)')
    g += t(240, 78, 'Arma virumque cano, Troiae qui primus ab oris', 'middle', 'L')
    g += t(240, 88, 'arms man-and I-sing  Troy-of who first from shores', 'middle', 'Lx')
    g += t(240, 97, 'Italiam, fato profugus, Laviniaque venit', 'middle', 'L')
    g += t(240, 107, 'Italy fate-by exile-NOM Lavinian-and came', 'middle', 'Lx')
    g += t(240, 116, 'litora — multum ille et terris iactatus et alto', 'middle', 'L')
    g += t(240, 126, 'shores — much he both on-lands tossed and on-deep', 'middle', 'Lx')
    g += t(240, 135, '"I sing of arms and the man, who first from the shores of Troy, exiled by fate,', 'middle', 'Ls')
    g += t(240, 143, 'came to Italy and the Lavinian shores — tossed much on land and sea."', 'middle', 'Ls')
    g += hr(151)

    # Passage 2 — Caesar
    g += sh(159, 'PASSAGE 2 — CAESAR, DE BELLO GALLICO I.1 (52 BCE)')
    g += t(240, 170, 'Gallia est omnis divisa in partes tres,', 'middle', 'L')
    g += t(240, 180, 'Gaul  is  all   divided into parts  three', 'middle', 'Lx')
    g += t(240, 189, 'quarum unam incolunt Belgae, aliam Aquitani,', 'middle', 'L')
    g += t(240, 199, 'of-which one  inhabit  Belgians another Aquitanians', 'middle', 'Lx')
    g += t(240, 208, 'tertiam qui ipsorum lingua Celtae, nostra Galli appellantur.', 'middle', 'Ls')
    g += t(240, 217, '"All of Gaul is divided into three parts, one of which the Belgians inhabit,', 'middle', 'Ls')
    g += t(240, 225, 'another the Aquitanians, the third those who in their own language are called Celts, in ours Gauls."', 'middle', 'Ls')
    g += hr(233)

    # Passage 3 — Cicero
    g += sh(241, 'PASSAGE 3 — CICERO, DE SENECTUTE 2.5 (44 BCE)')
    g += t(240, 252, 'Omnia aliena sunt, tempus tantum nostrum.', 'middle', 'L')
    g += t(240, 262, 'All   foreign are  time   only    our-own', 'middle', 'Lx')
    g += t(240, 271, '"All things are foreign to us; time alone is our own."', 'middle', 'Ls')
    g += t(240, 281, 'Dum differtur vita transcurrit.', 'middle', 'L')
    g += t(240, 291, 'While it-is-delayed life runs-past', 'middle', 'Lx')
    g += t(240, 300, '"While we delay, life runs on."  — Seneca, Epistulae I.1', 'middle', 'Ls')
    g += hr(308)

    # Passage 4 — Horace
    g += sh(316, 'PASSAGE 4 — HORACE, ODES I.11 (23 BCE)')
    g += t(240, 327, 'Carpe diem, quam minimum credula postero.', 'middle', 'L')
    g += t(240, 337, 'Seize day   how  least   trusting  to-tomorrow', 'middle', 'Lx')
    g += t(240, 346, '"Seize the day, trusting as little as possible in the next."', 'middle', 'Ls')
    g += t(240, 356, 'Note: carpe is imperative of carpo "to pluck/harvest" — more "pluck the day (like fruit)" than merely seize.', 'middle', 'Lx')
    g += hr(364)

    # Passage 5 — Marcus Aurelius (Latin trans. of Greek)
    g += sh(372, 'PASSAGE 5 — LUCRETIUS, DE RERUM NATURA I.1–2 (60s BCE)')
    g += t(240, 383, 'Aeneadum genetrix, hominum divumque voluptas,', 'middle', 'L')
    g += t(240, 393, 'Of-Aeneas-sons mother  humans-of gods-and  pleasure', 'middle', 'Lx')
    g += t(240, 402, 'alma Venus, caeli subter labentia signa', 'middle', 'L')
    g += t(240, 412, 'nurturing Venus  sky-of beneath gliding  signs', 'middle', 'Lx')
    g += t(240, 421, '"Mother of the sons of Aeneas, delight of men and gods, nurturing Venus,', 'middle', 'Ls')
    g += t(240, 429, 'who beneath the gliding signs of heaven…" — opening of the first Latin philosophical poem.', 'middle', 'Ls')
    g += hr(437)

    # Bridge phrase
    g += sh(446, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 458, 'Hoc vobis, gratis, ab hominibus qui futura memoria tenebant, factum est.', 'middle', 'L')
    g += t(240, 469, 'This  for-you freely by  men       who  future-ACC memory  held        made   is', 'middle', 'Lx')
    g += t(240, 479, '"This was made for you, freely, by people who held the future in their memory."', 'middle', 'Ls')
    g += hr(487)

    # Language note
    g += sh(496, 'LANGUAGE NOTE — "FUTURE" IN LATIN')
    g += t(240, 507, 'Latin expresses "forward in time" via futurum (neut. gerundive of esse "to be" = "what is about to be").', 'middle', 'L')
    g += t(240, 517, 'futurum = "that which will be" — a participial noun, not an abstract concept: the future as event in motion.', 'middle', 'Ls')
    g += t(240, 527, 'memoria tenebant: "held in memory" — tenere is to hold physically; memory as something grasped, not merely stored.', 'middle', 'Ls')
    g += t(240, 537, 'gratis: ablative plural of gratia "grace/favor" — freely given, without expectation of return.', 'middle', 'Ls')
    g += t(240, 547, 'factum est: perfect passive — "it was made" — emphasizing the completed act and its recipient, not the maker.', 'middle', 'Ls')
    g += hr(556)

    g += sh(565, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 576, 'Latin is the ancestor of French, Spanish, Portuguese, Italian, Romanian, and Catalan.', 'middle', 'Ls')
    g += t(240, 585, 'It underlies ~60% of English vocabulary, all scientific nomenclature, and most legal and medical terms.', 'middle', 'Ls')
    g += t(240, 594, 'If this script is unfamiliar: the Latin alphabet is the same script used in English. All 26 letters appear above.', 'middle', 'Ls')
    g += t(240, 603, 'Latin was spoken ~700 BCE – 7th c. CE; thereafter it became the language of scholarship until ~1700 CE.', 'middle', 'Ls')
    g += t(240, 612, 'Estimated native speakers today: none. Estimated readers: millions. It is a living scholarly language.', 'middle', 'Ls')

    g += footer('22', 'Latin', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate22a_latin_script.svg': build_22a(),
        'plate22b_latin_phonology.svg': build_22b(),
        'plate22c_latin_grammar.svg': build_22c(),
        'plate22d_latin_text.svg': build_22d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
