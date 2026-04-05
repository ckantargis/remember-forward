#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Malay/Indonesian plate series 19A–19D for Remember Forward."""

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


# ─── PLATE 19A — SCRIPT ──────────────────────────────────────────────────────

def build_19a():
    g = open_svg()
    g += t(240, 32, 'MALAY / INDONESIAN — SCRIPT · WRITING', 'middle', 'T')
    g += t(240, 50, 'SERIES 19A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Overview
    g += sh(67, 'LATIN SCRIPT — RUMI (SINCE 1972 STANDARDIZATION)')
    g += t(240, 77, 'Malay (Bahasa Melayu) and Indonesian (Bahasa Indonesia) share a standardized Latin orthography.', 'middle', 'L')
    g += t(240, 87, 'The 1972 Melindo/EYD agreement unified spelling across Malaysia, Indonesia, and Brunei.', 'middle', 'Ls')
    g += t(240, 96, 'Official names: Rumi (Malaysia) = "Roman script" · Ejaan yang Disempurnakan (Indonesia) = "Perfected Spelling"', 'middle', 'Ls')
    g += hr(104)

    # The 26 letters
    g += sh(112, 'THE 26-LETTER ALPHABET — RUMI')
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sounds = [
        '/a/','b','tʃ/c','d','/e,ə/','f','g/ɡ/','h','/i/','dʒ/j',
        'k','l','m','n','/o/','p','k/kw','r','s','t',
        '/u/','v','w','ks/z','y/j','z'
    ]
    names_ms = [
        'a','bi','si','di','i','ef','ji','éc','ai','jei',
        'kei','el','em','en','o','pi','kiu','ar','es','ti',
        'yu','vi','dabel-yu','eks','wai','zet'
    ]
    col_x_alpha = [30, 110, 190, 270, 350, 430]
    # 5 rows of ~5 letters
    rows_of = 6
    for i, (ltr, snd, nm) in enumerate(zip(letters, sounds, names_ms)):
        col = i % rows_of
        row = i // rows_of
        cx = col_x_alpha[col]
        ry = 122 + row * 18
        g += t(cx, ry, ltr, 'middle', 'L')
        g += t(cx, ry + 7, snd, 'middle', 'Lx')
        g += t(cx, ry + 13, nm, 'middle', 'Lx')
    g += hr(205)

    # Digraphs
    g += sh(213, 'DIGRAPHS — LETTER COMBINATIONS WITH SPECIAL SOUNDS')
    digraphs = [
        ('ng', '/ŋ/', 'velar nasal', 'berenang (swim), bukan (not)', 'like "ng" in "sing"'),
        ('ny', '/ɲ/', 'palatal nasal', 'nyonya (ma\'am), nyaman (comfortable)', 'like "ny" in Spanish "señor"'),
        ('kh', '/x/', 'velar fricative', 'khas (special), akhir (end)', 'Arabic/Persian borrowing — "ch" in "Bach"'),
        ('gh', '/ɣ/', 'voiced velar fric.', 'ghairah (passion), maghrib (west)', 'Arabic borrowing — voiced "kh"'),
        ('sy', '/ʃ/', 'palato-alveolar fric.', 'syarat (condition), syukur (gratitude)', 'like "sh" in "shoe" — Arabic borrowing'),
    ]
    for i, (dg, ipa, name, example, note) in enumerate(digraphs):
        y = 223 + i * 16
        g += t(35, y, dg, 'middle', 'Ls')
        g += t(70, y, ipa, 'middle', 'Lx')
        g += t(140, y, name, 'middle', 'Lx')
        g += t(275, y, example, 'middle', 'Lx')
        g += t(415, y, note, 'middle', 'Lx')
    g += hr(303)

    # Jawi script
    g += sh(311, 'JAWI — HISTORICAL ARABIC-BASED SCRIPT')
    g += t(240, 321, 'Before Romanization, Malay was written in Jawi — an adapted Arabic alphabet with extra letters for Malay sounds.', 'middle', 'Ls')
    g += t(240, 330, 'Jawi is still used officially in Malaysia (signage, religious texts, royal documents) and in Brunei.', 'middle', 'Ls')
    g += t(240, 339, 'Written right-to-left. 37 letters total: 28 Arabic + 6 added for Malay phonemes (ca, nga, pa, ga, nya, va).', 'middle', 'Ls')
    g += t(240, 348, 'Sample: بهاس ملايو = Bahasa Melayu · كيتا = kita (we) · هاتي = hati (heart)', 'middle', 'Ls')
    g += t(240, 357, 'Jawi literacy is taught in Malaysian schools alongside Rumi, keeping both scripts active.', 'middle', 'Ls')
    g += hr(365)

    # Historical scripts
    g += sh(373, 'HISTORICAL SCRIPTS — RENCONG AND OTHERS')
    g += t(240, 383, 'Before Jawi spread via Islam (~13th–16th c.), Malay was written in indigenous Indic-derived scripts.', 'middle', 'Ls')
    g += t(240, 392, 'Rencong / Incung: abugida script of Sumatra (Kerinci, Rejang, Lampung regions) — written on bamboo.', 'middle', 'Ls')
    g += t(240, 401, 'Pallava/Kawi: Old Malay inscriptions (7th–14th c.) in Tamil Pallava and Javanese Kawi scripts.', 'middle', 'Ls')
    g += t(240, 410, 'Kedukan Bukit inscription (683 CE, Palembang): oldest known Old Malay text — in Pallava script.', 'middle', 'Ls')
    g += t(240, 419, 'Lontara: Bugis/Makassar script still used in Sulawesi — an abugida descended from Brahmi.', 'middle', 'Ls')
    g += hr(427)

    # Spelling system
    g += sh(435, 'SPELLING SYSTEM — KEY RULES')
    rules = [
        ('Stress', 'Always on penultimate (second-to-last) syllable: ba-HA-sa, ma-KAN-an'),
        ('e ambiguity', '<e> = /e/ (clear) or /ə/ (schwa) — context determines: enam (6)=/e/, emak (mum)=/ə/'),
        ('c', 'Always /tʃ/ (like "ch") — cinta (love), cantik (beautiful)'),
        ('j', 'Always /dʒ/ (like "j" in "joy") — jalan (road), juga (also)'),
        ('r', 'Trilled /r/ in careful speech; flap [ɾ] in fast speech'),
        ('f, v, z', 'Appear in Arabic/English loanwords: fikir (think), vitamin, zaman (era)'),
    ]
    for i, (label, rule) in enumerate(rules):
        y = 445 + i * 14
        g += t(70, y, label, 'middle', 'Ls')
        g += t(310, y, rule, 'middle', 'Lx')
    g += hr(530)

    # Relationship note
    g += sh(538, 'MALAY vs INDONESIAN — SAME LANGUAGE?')
    g += t(240, 548, 'Bahasa Malaysia and Bahasa Indonesia are mutually intelligible. Differences are lexical and minor.', 'middle', 'Ls')
    g += t(240, 557, 'Malaysia: kereta (car) vs Indonesia: mobil · Malaysia: pekan vs Indonesia: kota (city)', 'middle', 'Ls')
    g += t(240, 566, 'Combined: ~270 million speakers (Indonesia alone ~199M native) — 4th most-spoken world language.', 'middle', 'Ls')
    g += t(240, 575, 'ISO 639: ms (Malay) · id (Indonesian) — classified separately but share standard written form.', 'middle', 'Ls')
    g += t(240, 584, 'Arabic influence: 40%+ of literary vocabulary via Jawi-era Islam · Dutch/Portuguese in Indonesian.', 'middle', 'Ls')

    g += footer('19', 'Malay/Indonesian', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 19B — PHONOLOGY ───────────────────────────────────────────────────

def build_19b():
    g = open_svg()
    g += t(240, 32, 'MALAY / INDONESIAN — PHONOLOGY · SOUNDS', 'middle', 'T')
    g += t(240, 50, 'SERIES 19B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Overview
    g += sh(67, 'OVERVIEW — NO TONES, PENULTIMATE STRESS')
    g += t(240, 77, 'Malay/Indonesian is a NON-TONAL language with simple syllable structure and fixed stress.', 'middle', 'L')
    g += t(240, 87, 'Stress: always on the PENULTIMATE (second-to-last) syllable in base words.', 'middle', 'Ls')
    g += t(240, 96, 'Exception: words with schwa /ə/ in penultimate position — stress shifts to final syllable.', 'middle', 'Ls')
    g += t(240, 105, 'e.g., em-PAT (4), se-KO-lah (school) · BUT: te-LAH (already), me-NGERT-i (understand)', 'middle', 'Lx')
    g += hr(113)

    # Vowel system
    g += sh(121, 'VOWEL SYSTEM — 6 VOWELS')
    vowels = [
        ('/a/', 'a', 'low central open', 'apa (what), badan (body)', 'like "ah"'),
        ('/e/', 'é', 'mid front', 'enam (six), pergi (go)', 'like "e" in "bed"'),
        ('/ə/', 'e', 'mid central schwa', 'emak (mother), empat (four)', 'like "a" in "about"'),
        ('/i/', 'i', 'high front', 'ini (this), ibu (mother)', 'like "ee"'),
        ('/o/', 'o', 'mid back rounded', 'orang (person), bola (ball)', 'like "oh"'),
        ('/u/', 'u', 'high back rounded', 'ular (snake), buku (book)', 'like "oo"'),
    ]
    for i, (ipa, spell, desc, example, eng) in enumerate(vowels):
        y = 131 + i * 14
        g += t(40, y, ipa, 'middle', 'Ls')
        g += t(75, y, spell, 'middle', 'Ls')
        g += t(135, y, desc, 'middle', 'Lx')
        g += t(270, y, example, 'middle', 'Lx')
        g += t(415, y, eng, 'middle', 'Lx')
    g += hr(217)

    # Consonants
    g += sh(225, 'CONSONANT INVENTORY')
    g += t(240, 234, 'Malay/Indonesian has 19 native consonant phonemes. Loanwords add f, v, z, sy, kh, gh.', 'middle', 'Ls')
    cons = [
        ('p', '/p/', 'bilabial stop', 'pagi (morning)'),
        ('b', '/b/', 'bilabial stop', 'baru (new)'),
        ('t', '/t/', 'alveolar stop', 'tahu (know)'),
        ('d', '/d/', 'alveolar stop', 'dan (and)'),
        ('k', '/k/', 'velar stop', 'kita (we)'),
        ('g', '/g/', 'velar stop', 'guru (teacher)'),
        ('c', '/tʃ/', 'palatal affricate', 'cinta (love)'),
        ('j', '/dʒ/', 'palatal affricate', 'jalan (road)'),
        ('m', '/m/', 'bilabial nasal', 'makan (eat)'),
        ('n', '/n/', 'alveolar nasal', 'nama (name)'),
        ('ng', '/ŋ/', 'velar nasal', 'dengan (with)'),
        ('ny', '/ɲ/', 'palatal nasal', 'nyawa (life)'),
        ('s', '/s/', 'alveolar fricative', 'satu (one)'),
        ('h', '/h/', 'glottal fricative', 'hari (day)'),
        ('r', '/r/', 'alveolar trill', 'rumah (house)'),
        ('l', '/l/', 'lateral approx.', 'laut (sea)'),
        ('w', '/w/', 'labial-velar glide', 'waktu (time)'),
        ('y', '/j/', 'palatal glide', 'yang (which/that)'),
        ('\'', '/ʔ/', 'glottal stop', 'rakyat (people) final k'),
    ]
    for i, (spell, ipa, desc, ex) in enumerate(cons):
        col = i % 2
        row = i // 2
        cx_left = [30, 250]
        y = 244 + row * 12
        cx = cx_left[col]
        g += t(cx + 15, y, spell, 'middle', 'Ls')
        g += t(cx + 45, y, ipa, 'middle', 'Lx')
        g += t(cx + 100, y, desc, 'middle', 'Lx')
        g += t(cx + 175, y, ex, 'middle', 'Lx')
    g += hr(372)

    # Syllable structure
    g += sh(380, 'SYLLABLE STRUCTURE — CV(C)')
    g += t(240, 390, 'Most syllables are CV (consonant-vowel) or V. Final consonants allowed but limited.', 'middle', 'L')
    g += t(240, 399, 'Final position: -k is realized as glottal stop [ʔ] in careful speech: tidak [tɪdaʔ] (not)', 'middle', 'Ls')
    g += t(240, 408, 'Diphthongs: /ai/ → [aɪ] pandai (clever) · /au/ → [aʊ] pulau (island) · /oi/ → [ɔɪ] amboi (wow)', 'middle', 'Ls')
    g += hr(416)

    # Gemination in borrowings
    g += sh(424, 'GEMINATION — DOUBLE CONSONANTS IN BORROWINGS')
    g += t(240, 434, 'Native Malay has no geminate consonants. Loanwords from Arabic may have doubled consonants.', 'middle', 'Ls')
    g += t(240, 443, 'Arabic loanwords: massa (mass), sunnah (tradition), qiblat (prayer direction)', 'middle', 'Ls')
    g += t(240, 452, 'In normal speech, geminates are reduced: kelas (class) /kelas/ not /kell-as/', 'middle', 'Ls')
    g += hr(460)

    # Intonation
    g += sh(468, 'INTONATION — QUESTION FORMATION')
    g += t(240, 478, 'Questions formed by rising intonation OR by adding particle kah/tah (formal) or kan/ke (colloquial).', 'middle', 'Ls')
    g += t(240, 487, 'Dia datang? "Is he coming?" (rising tone) · Adakah dia datang? (formal marker adakah)', 'middle', 'Ls')
    g += t(240, 496, 'Dia datang, kan? "He\'s coming, right?" — tag question with kan', 'middle', 'Ls')
    g += hr(504)

    # Regional variation
    g += sh(512, 'REGIONAL PHONOLOGICAL VARIATION')
    g += t(240, 522, 'Standard (KL/Jakarta): /r/ = trill or flap depending on position and register.', 'middle', 'Ls')
    g += t(240, 531, 'Javanese-influenced Indonesian: /e/ often realized as [ɛ] · /o/ as [ɔ] in open syllables.', 'middle', 'Ls')
    g += t(240, 540, 'Colloquial Malaysian: final /a/ → /ə/ in fast speech: saya → sayə (I/me).', 'middle', 'Ls')
    g += t(240, 549, 'H-deletion: hari (day) → [a.ri] in rapid colloquial speech in many regions.', 'middle', 'Ls')
    g += t(240, 558, 'Northern Malaysian dialects (Kedah, Kelantan): distinct vowel systems, tonal features — not standard.', 'middle', 'Ls')
    g += t(240, 567, 'IPA summary: /p b t d k g tʃ dʒ m n ŋ ɲ s h r l w j ʔ/ + /a e ə i o u/', 'middle', 'Ls')

    g += footer('19', 'Malay/Indonesian', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 19C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_19c():
    g = open_svg()
    g += t(240, 32, 'MALAY / INDONESIAN — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 19C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # SVO
    g += sh(67, 'SENTENCE STRUCTURE — SVO, NO INFLECTION')
    g += t(240, 77, 'Malay/Indonesian is SVO (Subject–Verb–Object) with NO grammatical gender, NO case, NO tense inflection.', 'middle', 'L')
    g += t(240, 87, 'Time is indicated by TIME WORDS, not verb forms: sudah (already), akan (will), sedang (currently).', 'middle', 'Ls')
    g += t(240, 96, 'Saya makan nasi.  "I eat/ate/am eating rice." — context + time words clarify tense.', 'middle', 'Ls')
    g += t(240, 105, 'Dia pergi semalam.  "She went yesterday." — semalam (yesterday) establishes past.', 'middle', 'Ls')
    g += hr(113)

    # Affixes
    g += sh(121, 'AFFIX SYSTEM — DERIVATIONAL MORPHOLOGY')
    g += t(240, 130, 'Malay/Indonesian has a rich system of prefixes and suffixes that derive new words from roots.', 'middle', 'Ls')
    affixes = [
        ('me-', 'active verb', 'makan (eat) → memakan (to eat/is eating)'),
        ('ber-', 'intrans. verb / have', 'kerja (work) → bekerja (to work)'),
        ('-kan', 'causative/transitive', 'tahu (know) → beritahukan (to inform/tell)'),
        ('-an', 'noun/result', 'makan (eat) → makanan (food)'),
        ('pe-', 'agent noun', 'kerja (work) → pekerja (worker)'),
        ('per-...-an', 'abstract noun', 'buat (do) → perbuatan (deed/act)'),
        ('ke-...-an', 'state/condition', 'sakit (sick) → kesakitan (pain/illness)'),
        ('ter-', 'accidental/passive', 'jatuh (fall) → terjatuh (accidentally fell)'),
        ('di-', 'passive voice', 'makan (eat) → dimakan (was eaten)'),
        ('se-', 'one/same/as', 'kolah → sekolah (school, lit. "one class")'),
    ]
    for i, (aff, func, ex) in enumerate(affixes):
        y = 141 + i * 14
        g += t(55, y, aff, 'middle', 'Ls')
        g += t(130, y, func, 'middle', 'Lx')
        g += t(330, y, ex, 'middle', 'Lx')
    g += hr(283)

    # Reduplication
    g += sh(291, 'REDUPLICATION — PLURALS AND EMPHASIS')
    g += t(240, 301, 'Full reduplication of nouns = plural (usually): orang (person) → orang-orang (people)', 'middle', 'Ls')
    g += t(240, 310, 'Reduplication can also indicate variety, intensity, or process rather than strict plurality:', 'middle', 'Ls')
    g += t(240, 319, 'sayur-sayuran (all kinds of vegetables) · berlari-lari (running around) · perlahan-lahan (very slowly)', 'middle', 'Ls')
    g += t(240, 328, 'Note: context often implies plurality without reduplication — no singular/plural confusion in practice.', 'middle', 'Lx')
    g += hr(336)

    # Negation
    g += sh(344, 'NEGATION')
    g += t(240, 354, 'tidak / tak: negates verbs and adjectives — Saya tidak tahu. "I do not know."', 'middle', 'Ls')
    g += t(240, 363, 'bukan: negates nouns and pronouns — Bukan saya. "Not me." · Dia bukan guru. "She is not a teacher."', 'middle', 'Ls')
    g += t(240, 372, 'jangan: prohibitive — Jangan pergi! "Do not go!"', 'middle', 'Ls')
    g += hr(380)

    # Core vocabulary
    g += sh(388, 'CORE VOCABULARY — 25 WORDS')
    vocab = [
        ('ya / tidak', 'yes / no'),
        ('terima kasih', 'thank you'),
        ('maaf / tolong', 'sorry / please/help'),
        ('saya / anda/kamu', 'I (formal) / you'),
        ('kita / kami', 'we (incl.) / we (excl.)'),
        ('ini / itu', 'this / that'),
        ('di mana', 'where'),
        ('apa', 'what'),
        ('siapa', 'who'),
        ('mengapa / kenapa', 'why'),
        ('air', 'water'),
        ('makan / makanan', 'eat / food'),
        ('orang', 'person / people'),
        ('rumah', 'house / home'),
        ('jalan', 'road / walk'),
        ('hari', 'day / sun'),
        ('malam', 'night'),
        ('buku', 'book'),
        ('bahasa', 'language'),
        ('dunia', 'world'),
        ('besar / kecil', 'big / small'),
        ('baik / buruk', 'good / bad'),
        ('baru / lama', 'new / old'),
        ('masa depan', 'future (lit. "time ahead")'),
        ('ingat / kenang', 'remember / recall fondly'),
    ]
    for i, (ms, eng) in enumerate(vocab):
        col = i % 2
        row = i // 2
        cx = 120 if col == 0 else 360
        y = 398 + row * 13
        g += t(cx, y, ms, 'middle', 'Ls')
        g += t(cx + (100 if col==0 else 80), y, eng, 'middle', 'Lx')
    g += hr(558)

    # Question words
    g += sh(566, 'QUESTION WORDS AND TIME MARKERS')
    qw = [('apa','what'),('siapa','who'),('di mana','where'),('bila/kapan','when'),
          ('mengapa','why'),('bagaimana','how'),('sudah','already (past)'),
          ('sedang','currently (prog.)'),('akan','will (future)'),('pernah','ever (exp.)')]
    for i, (w, m) in enumerate(qw):
        col = i % 5
        row = i // 5
        cx = [50, 140, 230, 320, 415][col]
        y = 576 + row * 13
        g += t(cx, y, w, 'middle', 'Ls')
        g += t(cx, y + 8, m, 'middle', 'Lx')

    g += footer('19', 'Malay/Indonesian', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 19D — RUNNING TEXT ─────────────────────────────────────────────────

def build_19d():
    g = open_svg()
    g += t(240, 32, 'MALAY / INDONESIAN — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 19D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1
    g += sh(67, 'PASSAGE 1 — GREETING')
    g += t(240, 77, 'Selamat datang.  Kami  gembira  kerana  anda  ada  di sini.', 'middle', 'L')
    g += t(240, 87, 'Welcome       We-EXCL happy   because  you  exist here.', 'middle', 'Lx')
    g += t(240, 95, '"Welcome. We are glad that you are here."', 'middle', 'Ls')
    g += t(240, 105, 'Bahasa adalah  jambatan  antara  masa  lalu  dan  masa  depan.', 'middle', 'L')
    g += t(240, 115, 'Language is    bridge    between  time  past  and  time  ahead.', 'middle', 'Lx')
    g += t(240, 123, '"Language is the bridge between the past and the future."', 'middle', 'Ls')
    g += hr(131)

    # Passage 2
    g += sh(139, 'PASSAGE 2 — NATURE PASSAGE')
    g += t(240, 149, 'Laut  yang  dalam  menyimpan  rahsia  yang  tidak  terhitung.', 'middle', 'L')
    g += t(240, 159, 'Sea   REL   deep   stores      secrets REL  not   counted.', 'middle', 'Lx')
    g += t(240, 167, '"The deep sea stores uncountable secrets."', 'middle', 'Ls')
    g += t(240, 177, 'Seperti  air,  ilmu  mengalir  ke  tempat  yang  lebih  rendah.', 'middle', 'L')
    g += t(240, 187, 'Like     water knowledge flows  to  place   REL   lower.', 'middle', 'Lx')
    g += t(240, 195, '"Like water, knowledge flows to lower places." — Malay proverb', 'middle', 'Ls')
    g += hr(203)

    # Passage 3
    g += sh(211, 'PASSAGE 3 — PERIBAHASA (MALAY PROVERB)')
    g += t(240, 221, 'Biar  putih  tulang,   jangan  putih  mata.', 'middle', 'L')
    g += t(240, 231, 'Let   white  bones-of, don\'t   white  eyes.', 'middle', 'Lx')
    g += t(240, 239, '"Better to die (bones white) than to live in shame (eyes white with horror)."', 'middle', 'Ls')
    g += t(240, 249, 'Seperti  katak  di  bawah  tempurung  —  menyangka  langit  itu  sempit.', 'middle', 'L')
    g += t(240, 259, 'Like     frog   at  under  coconut-shell — thinks      sky    that  narrow.', 'middle', 'Lx')
    g += t(240, 267, '"Like a frog under a coconut shell, thinking the sky is small." — parochialism', 'middle', 'Ls')
    g += hr(275)

    # Passage 4
    g += sh(283, 'PASSAGE 4 — PANTUN (MALAY POETIC FORM)')
    g += t(240, 293, 'Buah  pisang  masak  sebuah,', 'middle', 'L')
    g += t(240, 301, 'fruit banana  ripe   one-CLASSIFIER', 'middle', 'Lx')
    g += t(240, 311, 'Jatuh  ke  dalam   parit  tua;', 'middle', 'L')
    g += t(240, 319, 'falls  into inside  ditch   old', 'middle', 'Lx')
    g += t(240, 329, 'Kalau   kasih   masih  menanggung,', 'middle', 'L')
    g += t(240, 337, 'If      love    still   endures,', 'middle', 'Lx')
    g += t(240, 347, 'Sampai  mati   tidak  akan  lupa.', 'middle', 'L')
    g += t(240, 355, 'Until   death  not   will  forget.', 'middle', 'Lx')
    g += t(240, 363, 'A pantun: rhyming quatrain (AB AB). Lines 1-2 are imagery; lines 3-4 carry the meaning.', 'middle', 'Lx')
    g += t(240, 371, '"If love still endures, until death we will not forget."', 'middle', 'Ls')
    g += hr(379)

    # Bridge phrase
    g += sh(387, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 397, 'Ini  dibuat  untukmu,  dengan  cuma-cuma,  oleh  orang-orang  yang  mengingat  masa  depan.', 'middle', 'L')
    g += t(240, 407, 'This made   for-you,  with    free-free,  by    person-PLUR REL   remembers  time   ahead.', 'middle', 'Lx')
    g += t(240, 417, '"This was made for you, freely, by people who remembered the future."', 'middle', 'Ls')
    g += hr(425)

    # Language note
    g += sh(433, 'LANGUAGE NOTE — "FORWARD / FUTURE" IN MALAY')
    g += t(240, 443, '"masa depan" = "time ahead" (lit. masa=time, depan=front/ahead) — the future is spatially IN FRONT.', 'middle', 'L')
    g += t(240, 453, 'Malay/Indonesian conceives time as spatial movement: depan (front=future), belakang (back=past).', 'middle', 'Ls')
    g += t(240, 463, 'cuma-cuma: reduplication of cuma (only/free) → "completely free, at no cost" — colloquially natural.', 'middle', 'Ls')
    g += t(240, 472, 'orang-orang: reduplicated plural "people" (not orang alone, which is "a person" without number).', 'middle', 'Ls')
    g += t(240, 481, 'mengingat: active verb with me- prefix from ingat (remember) — "who are remembering / who remembered."', 'middle', 'Ls')
    g += t(240, 490, 'yang: relative clause marker — "people WHO remembered" — the same word as "which/that/who."', 'middle', 'Ls')
    g += hr(498)

    # Decoding note
    g += sh(506, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 516, 'Malay/Indonesian is written in the Latin alphabet — the same 26 letters as English.', 'middle', 'Ls')
    g += t(240, 525, 'Pronunciation is highly phonemic: each letter has a consistent sound. c=/tʃ/ and j=/dʒ/ are key.', 'middle', 'Ls')
    g += t(240, 534, 'If you speak any language using Latin script, you can approximate the sounds from the spelling.', 'middle', 'Ls')
    g += t(240, 543, 'Spoken by ~270M people across Maritime Southeast Asia (Indonesia, Malaysia, Brunei, Singapore).', 'middle', 'Ls')
    g += t(240, 552, 'Related to Tagalog, Javanese, Sundanese, and other Austronesian languages of the Pacific.', 'middle', 'Ls')

    g += footer('19', 'Malay/Indonesian', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate19a_malay_script.svg': build_19a(),
        'plate19b_malay_phonology.svg': build_19b(),
        'plate19c_malay_grammar.svg': build_19c(),
        'plate19d_malay_text.svg': build_19d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
