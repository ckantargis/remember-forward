#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Russian plate series 24A–24D for Remember Forward."""

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
        '  .Lr { font-size:13px; }\n'
        '  .Lrs{ font-size:10px; }\n'
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


# ─── PLATE 24A — SCRIPT ──────────────────────────────────────────────────────

def build_24a():
    g = open_svg()
    g += t(240, 32, 'RUSSIAN — SCRIPT · WRITING SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 24A OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'THE CYRILLIC ALPHABET — RUSSIAN 33 LETTERS')
    g += t(240, 79, 'Russian is written in the Cyrillic alphabet, derived from Greek uncial script in the 9th century CE.', 'middle', 'L')
    g += t(240, 89, 'Created by Saints Cyril and Methodius (c. 863 CE) to write Old Church Slavonic for Slavic peoples.', 'middle', 'Ls')
    g += t(240, 98, 'Russian Cyrillic: 33 letters — 10 vowel letters, 21 consonant letters, 2 signs (soft ь, hard ъ).', 'middle', 'Ls')
    g += hr(106)

    # Full alphabet table
    g += sh(115, 'THE 33 LETTERS — PRINTED AND HANDWRITTEN FORMS')
    cyrillic = [
        ('А а', 'a', '/a/', 'as in "father"'),
        ('Б б', 'b', '/b/', 'bilabial stop'),
        ('В в', 'v', '/v/', 'labiodental fricative'),
        ('Г г', 'g', '/ɡ/', 'velar stop'),
        ('Д д', 'd', '/d/', 'alveolar stop'),
        ('Е е', 'ye', '/je/ or /e/', 'iotic e after consonant softens it'),
        ('Ё ё', 'yo', '/jo/', 'always stressed; often written as Е'),
        ('Ж ж', 'zh', '/ʒ/', 'voiced palatal fricative — "measure"'),
        ('З з', 'z', '/z/', 'voiced alveolar fricative'),
        ('И и', 'i', '/i/', 'high front vowel'),
        ('Й й', 'y', '/j/', 'palatal glide — "boy"'),
        ('К к', 'k', '/k/', 'velar stop'),
        ('Л л', 'l', '/l/', 'lateral'),
        ('М м', 'm', '/m/', 'bilabial nasal'),
        ('Н н', 'n', '/n/', 'alveolar nasal'),
        ('О о', 'o', '/o/ (stressed)', 'unstressed: /\u0250/ — vowel reduction'),
        ('П п', 'p', '/p/', 'bilabial stop'),
        ('Р р', 'r', '/r/', 'alveolar trill'),
        ('С с', 's', '/s/', 'voiceless alveolar fricative'),
        ('Т т', 't', '/t/', 'alveolar stop'),
        ('У у', 'u', '/u/', 'high back rounded'),
        ('Ф ф', 'f', '/f/', 'labiodental fricative'),
        ('Х х', 'kh', '/x/', 'velar fricative — like German "Bach"'),
        ('Ц ц', 'ts', '/ts/', 'affricate — "cats"'),
        ('Ч ч', 'ch', '/tʃ/', 'affricate — "church"'),
        ('Ш ш', 'sh', '/ʃ/', 'voiceless palatal fricative'),
        ('Щ щ', 'shch', '/ɕ/', 'long palatal fricative'),
        ('Ъ ъ', '"', 'hard sign', 'separates prefix from iotic vowel'),
        ('Ы ы', 'y', '/\u0268/', 'central high vowel — no English equivalent'),
        ('Ь ь', "'", 'soft sign', 'palatalizes preceding consonant'),
        ('Э э', 'e', '/e/', '"backwards E" — non-iotic front vowel'),
        ('Ю ю', 'yu', '/ju/', 'iotic u'),
        ('Я я', 'ya', '/ja/', 'iotic a'),
    ]
    g += t(38,  124, 'Letter', 'middle', 'Lx')
    g += t(90,  124, 'Translit', 'middle', 'Lx')
    g += t(135, 124, 'IPA', 'middle', 'Lx')
    g += t(310, 124, 'Notes', 'middle', 'Lx')
    for i, (ltr, tr, ipa, note) in enumerate(cyrillic):
        y = 132 + i * 9
        g += t(38,  y, ltr, 'middle', 'Lrs')
        g += t(90,  y, tr, 'middle', 'Lx')
        g += t(135, y, ipa, 'middle', 'Lx')
        g += t(310, y, note, 'middle', 'Lx')
    g += hr(432)

    # Numerals
    g += sh(441, 'RUSSIAN NUMERALS — ARABIC (WESTERN)')
    g += t(240, 452, 'Russian uses standard Western Arabic numerals (0–9) with standard decimal notation.', 'middle', 'Ls')
    g += t(240, 461, 'Ordinals decline like adjectives: первый (pervyy) "first" · второй (vtoroy) "second" · третий (tretiy) "third"', 'middle', 'Ls')
    g += hr(470)

    # Script history
    g += sh(479, 'SCRIPT HISTORY')
    g += t(240, 490, '863 CE: Cyril and Methodius create Glagolitic (first Slavic alphabet) and later Cyrillic for Old Church Slavonic.', 'middle', 'Ls')
    g += t(240, 499, '~10th c.: Cyrillic adopted in Kievan Rus after Christianization (988 CE); early manuscripts in Old Church Slavonic.', 'middle', 'Ls')
    g += t(240, 508, '1708: Peter the Great reforms the alphabet — "civil script" (гражданский шрифт) drops archaic letters.', 'middle', 'Ls')
    g += t(240, 517, '1917–18: Soviet reform removes 4 more letters (ять, і, ижица, фита) — creates modern 33-letter alphabet.', 'middle', 'Ls')
    g += t(240, 526, 'Cyrillic today: used by ~250 million people — Russian, Ukrainian, Bulgarian, Serbian, Kazakh, Mongolian, and more.', 'middle', 'Ls')
    g += t(240, 535, 'Direction: left to right, top to bottom. Same as Latin script.', 'middle', 'Ls')

    g += footer('24', 'Russian', 'A', 'Script')
    g += close_svg()
    return g


# ─── PLATE 24B — PHONOLOGY ───────────────────────────────────────────────────

def build_24b():
    g = open_svg()
    g += t(240, 32, 'RUSSIAN — PHONOLOGY · SOUND SYSTEM', 'middle', 'T')
    g += t(240, 50, 'SERIES 24B OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'KEY FEATURE: PALATALIZATION — SOFT AND HARD CONSONANTS')
    g += t(240, 79, 'Russian has a pervasive contrast between HARD (plain) and SOFT (palatalized) consonants.', 'middle', 'L')
    g += t(240, 89, 'Palatalization: the body of the tongue rises toward the hard palate during the consonant — like adding /j/.', 'middle', 'Ls')
    g += t(240, 98, 'Soft sign ь signals palatalization: брат brat "brother" vs. брать brat\' "to take"', 'middle', 'Ls')
    g += t(240, 107, 'Iotic vowels (е, ё, ю, я, и) also palatalize the preceding consonant automatically.', 'middle', 'Ls')
    g += hr(115)

    # Vowel system
    g += sh(124, 'VOWEL SYSTEM — 6 PHONEMES, STRONG REDUCTION')
    vowels = [
        ('/a/', 'а', 'a', 'low central — stressed: [a], unstressed after hard: [ə]'),
        ('/e/', 'э/е', 'e', 'mid front — stressed: [e], unstressed: [ɪ]'),
        ('/i/', 'и', 'i', 'high front — stable across stress'),
        ('/\u0268/', 'ы', 'y', 'high central — unique to Slavic; no English equivalent'),
        ('/o/', 'о', 'o', 'mid back — stressed: [o], unstressed: [ə] or [ɐ]'),
        ('/u/', 'у', 'u', 'high back rounded — relatively stable'),
    ]
    g += t(50, 134, 'IPA', 'middle', 'Lx')
    g += t(95, 134, 'Letter', 'middle', 'Lx')
    g += t(140, 134, 'Translit', 'middle', 'Lx')
    g += t(330, 134, 'Notes', 'middle', 'Lx')
    for i, (ipa, ltr, tr, note) in enumerate(vowels):
        y = 143 + i * 12
        g += t(50,  y, ipa, 'middle', 'Lx')
        g += t(95,  y, ltr, 'middle', 'Lrs')
        g += t(140, y, tr, 'middle', 'Lx')
        g += t(315, y, note, 'middle', 'Lx')
    g += t(240, 218, 'VOWEL REDUCTION: unstressed /o/ and /a/ reduce toward [ə]/[ɐ] — молоко moloko [məlɐˈko] "milk"', 'middle', 'Ls')
    g += hr(226)

    # Consonant inventory
    g += sh(235, 'CONSONANT INVENTORY — 36 PHONEMES (18 HARD/SOFT PAIRS + OTHERS)')
    g += t(240, 246, 'Most consonants come in hard/soft pairs — 15 pairs = 30 phonemes, plus unpaired consonants:', 'middle', 'Ls')
    cons_pairs = [
        ('п/п\'', '/p/ - /pʲ/', 'п/пь', 'п — папа papa · пь — петь pet\''),
        ('б/б\'', '/b/ - /bʲ/', 'б/бь', 'б — баба baba · бь — бить bit\''),
        ('т/т\'', '/t/ - /tʲ/', 'т/ть', 'т — там tam · ть — тесто testo'),
        ('д/д\'', '/d/ - /dʲ/', 'д/дь', 'д — да da · дь — день den\''),
        ('к/к\'', '/k/ - /kʲ/', 'к/кь', 'к — кот kot · кь — кит kit'),
        ('г/г\'', '/ɡ/ - /ɡʲ/', 'г/гь', 'г — год god · гь — гиря girya'),
        ('с/с\'', '/s/ - /sʲ/', 'с/сь', 'с — сад sad · сь — сесть sest\''),
        ('з/з\'', '/z/ - /zʲ/', 'з/зь', 'з — зал zal · зь — зима zima'),
        ('н/н\'', '/n/ - /nʲ/', 'н/нь', 'н — нос nos · нь — нет net'),
        ('л/л\'', '/l/ - /lʲ/', 'л/ль', 'л — луна luna · ль — лес les'),
        ('р/р\'', '/r/ - /rʲ/', 'р/рь', 'р — рот rot · рь — ряд ryad'),
        ('м/м\'', '/m/ - /mʲ/', 'м/мь', 'м — мать mat\' · мь — мир mir'),
        ('в/в\'', '/v/ - /vʲ/', 'в/вь', 'в — вот vot · вь — весна vesna'),
        ('ф/ф\'', '/f/ - /fʲ/', 'ф/фь', 'ф — факт fakt · фь — фитиль fitil\''),
        ('х/х\'', '/x/ - /xʲ/', 'х/хь', 'х — ход khod · хь — химия khimiya'),
    ]
    for i, (pair, ipa, cyrl, ex) in enumerate(cons_pairs):
        y = 255 + i * 10
        g += t(55, y, pair, 'middle', 'Lx')
        g += t(120, y, ipa, 'middle', 'Lx')
        g += t(180, y, cyrl, 'middle', 'Lx')
        g += t(360, y, ex, 'middle', 'Lx')
    g += t(240, 410, 'Unpaired hard: ж /ʒ/ ш /ʃ/ ц /ts/ · Unpaired soft: ч /tʃ/ щ /ɕ/ й /j/', 'middle', 'Ls')
    g += hr(418)

    # Stress
    g += sh(427, 'STRESS — FREE AND MOBILE')
    g += t(240, 438, 'Russian stress is FREE: it can fall on any syllable. It is MOBILE: shifts in inflected forms.', 'middle', 'L')
    g += t(240, 448, 'рука (ruka) "hand" NOM sg → руку (ruku) ACC sg → руки (ruki) NOM pl — stress shifts each form', 'middle', 'Ls')
    g += t(240, 457, 'Stress is not marked in normal writing. Dictionaries and learner texts mark it with an accent: a\u0301.', 'middle', 'Ls')
    g += t(240, 466, 'Unstressed vowels reduce: это (eto) "this" = [ˈetə]; молоко (moloko) "milk" = [məlɐˈko]', 'middle', 'Ls')
    g += hr(474)

    g += sh(483, 'ASSIMILATION AND FINAL DEVOICING')
    g += t(240, 494, 'Final devoicing: voiced obstruents become voiceless at word end — год god "year" pronounced [ɡot]', 'middle', 'Ls')
    g += t(240, 503, 'Regressive assimilation: consonants assimilate in voicing to the following consonant:', 'middle', 'Ls')
    g += t(240, 512, 'сделать sdelat\' "to do" — с before voiced д → [z]: [zdʲelatʲ]', 'middle', 'Ls')
    g += t(240, 521, 'Consonant clusters: Russian allows complex clusters: встреча vstretcha "meeting" /fstrʲetʃə/', 'middle', 'Ls')

    g += footer('24', 'Russian', 'B', 'Phonology')
    g += close_svg()
    return g


# ─── PLATE 24C — GRAMMAR & VOCABULARY ───────────────────────────────────────

def build_24c():
    g = open_svg()
    g += t(240, 32, 'RUSSIAN — GRAMMAR · VOCABULARY', 'middle', 'T')
    g += t(240, 50, 'SERIES 24C OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    g += sh(68, 'INFLECTED LANGUAGE — 6 CASES, 3 GENDERS')
    g += t(240, 79, 'Russian is highly inflected. Nouns decline for: CASE (6) × NUMBER (sg/pl) × GENDER (M/F/N).', 'middle', 'L')
    g += t(240, 89, 'Word order is flexible (SVO preferred, but any order is grammatically possible for emphasis).', 'middle', 'Ls')

    cases = [
        ('Nominative', 'НОМ', 'Subject', 'Кот спит.', 'The cat sleeps.'),
        ('Genitive', 'РОД', 'Possession / absence', 'нет кота', 'there is no cat'),
        ('Dative', 'ДАТ', 'Indirect object', 'дал коту', 'gave to the cat'),
        ('Accusative', 'ВИН', 'Direct object', 'вижу кота', 'I see the cat'),
        ('Instrumental', 'ТВО', 'By/with/as', 'с котом', 'with the cat'),
        ('Prepositional', 'ПРЕ', 'Location (after prep)', 'о коте', 'about the cat'),
    ]
    g += t(60, 100, 'Case', 'middle', 'Lx')
    g += t(115, 100, 'Abbr', 'middle', 'Lx')
    g += t(185, 100, 'Function', 'middle', 'Lx')
    g += t(310, 100, 'Example', 'middle', 'Lx')
    g += t(415, 100, 'Gloss', 'middle', 'Lx')
    for i, (case, abbr, func, ex, gl) in enumerate(cases):
        y = 109 + i * 11
        g += t(60,  y, case, 'middle', 'Lx')
        g += t(115, y, abbr, 'middle', 'Lx')
        g += t(185, y, func, 'middle', 'Lx')
        g += t(310, y, ex, 'middle', 'Lrs')
        g += t(415, y, gl, 'middle', 'Lx')
    g += hr(177)

    # Noun declension - кот (cat, masculine)
    g += sh(186, 'NOUN DECLENSION — кот "cat" (masculine)')
    dec = [
        ('НОМ', 'кот', 'коты'),
        ('РОД', 'кота', 'котов'),
        ('ДАТ', 'коту', 'котам'),
        ('ВИН', 'кота', 'котов'),
        ('ТВО', 'котом', 'котами'),
        ('ПРЕ', 'коте', 'котах'),
    ]
    g += t(100, 196, 'Singular', 'middle', 'Lx')
    g += t(320, 196, 'Plural', 'middle', 'Lx')
    for i, (case, sg, pl) in enumerate(dec):
        y = 204 + i * 9
        g += t(55, y, case, 'middle', 'Lx')
        g += t(130, y, sg, 'middle', 'Lrs')
        g += t(320, y, pl, 'middle', 'Lrs')
    g += hr(261)

    # Verb conjugation
    g += sh(270, 'VERB CONJUGATION — говорить "to speak" (2nd conjugation)')
    pres = [
        ('я', 'говорю', 'I speak'),
        ('ты', 'говоришь', 'you speak'),
        ('он/она', 'говорит', 'he/she speaks'),
        ('мы', 'говорим', 'we speak'),
        ('вы', 'говорите', 'you (pl/formal) speak'),
        ('они', 'говорят', 'they speak'),
    ]
    past = [
        ('М sg', 'говорил', 'he spoke'),
        ('Ж sg', 'говорила', 'she spoke'),
        ('Ср sg', 'говорило', 'it spoke'),
        ('Мн pl', 'говорили', 'they spoke'),
    ]
    g += t(100, 280, 'Present', 'middle', 'Lx')
    g += t(360, 280, 'Past (agrees with subject gender)', 'middle', 'Lx')
    for i, (pr, form, gl) in enumerate(pres):
        y = 289 + i * 10
        g += t(45, y, pr, 'middle', 'Lrs')
        g += t(130, y, form, 'middle', 'Lrs')
        g += t(210, y, gl, 'middle', 'Lx')
    for i, (pr, form, gl) in enumerate(past):
        y = 289 + i * 10
        g += t(300, y, pr, 'middle', 'Lx')
        g += t(380, y, form, 'middle', 'Lrs')
        g += t(450, y, gl, 'start', 'Lx')
    g += t(240, 353, 'Aspect: Russian verbs have PERFECTIVE (completed) and IMPERFECTIVE (ongoing) pairs:', 'middle', 'Ls')
    g += t(240, 362, 'писать (pisat\') IMPF "to write (repeatedly)" vs написать (napisat\') PERF "to write (once, completely)"', 'middle', 'Lx')
    g += hr(370)

    # Vocabulary
    g += sh(379, 'CORE VOCABULARY — 25 WORDS')
    vocab = [
        ('да / нет', 'da / net', 'yes / no'),
        ('я / ты / вы', 'ya / ty / vy', 'I / you (inf) / you (formal)'),
        ('это', 'eto', 'this / that / it is'),
        ('где', 'gde', 'where'),
        ('что', 'chto', 'what'),
        ('кто', 'kto', 'who'),
        ('когда', 'kogda', 'when'),
        ('почему', 'pochemu', 'why'),
        ('вода', 'voda', 'water'),
        ('огонь', 'ogon\'', 'fire'),
        ('земля', 'zemlya', 'earth'),
        ('человек', 'chelovek', 'person'),
        ('книга', 'kniga', 'book'),
        ('время', 'vremya', 'time'),
        ('луна', 'luna', 'moon'),
        ('звезда', 'zvezda', 'star'),
        ('сердце', 'serdtse', 'heart'),
        ('любовь', 'lyubov\'', 'love'),
        ('свобода', 'svoboda', 'freedom'),
        ('память', 'pamyat\'', 'memory'),
        ('будущее', 'budushcheye', 'the future'),
        ('мир', 'mir', 'world / peace'),
        ('хорошо / плохо', 'khorosho / plokho', 'good / bad'),
        ('всё', 'vsyo', 'everything'),
        ('жизнь', 'zhizn\'', 'life'),
    ]
    col_va = [40, 155, 250]
    col_vb = [265, 380, 465]
    half = 13
    for i, (russ, translit, eng) in enumerate(vocab):
        if i < half:
            y = 389 + i * 10
            g += t(col_va[0], y, russ, 'middle', 'Lrs')
            g += t(col_va[1], y, translit, 'middle', 'Lx')
            g += t(col_va[2], y, eng, 'middle', 'Lx')
        else:
            y = 389 + (i - half) * 10
            g += t(col_vb[0], y, russ, 'middle', 'Lrs')
            g += t(col_vb[1], y, translit, 'middle', 'Lx')
            g += t(col_vb[2], y, eng, 'middle', 'Lx')
    g += hr(524)

    g += sh(533, 'NO ARTICLES — VERBAL ASPECT INSTEAD')
    g += t(240, 544, 'Russian has NO definite or indefinite articles. Context and word order convey specificity.', 'middle', 'L')
    g += t(240, 554, 'The distinction between "a book" and "the book" is handled by context, demonstratives (эта книга), or order.', 'middle', 'Ls')
    g += t(240, 563, 'Instead, Russian grammaticalizes ASPECT — a distinction absent from English but pervasive in Russian:', 'middle', 'Ls')
    g += t(240, 572, 'читать (chitat\') = to be reading / read habitually · прочитать (prochitat\') = to read (and finish)', 'middle', 'Ls')
    g += t(240, 581, 'The perfective prefix changes meaning: написать "write completely", выпить "drink up", уйти "leave (and go)"', 'middle', 'Ls')

    g += footer('24', 'Russian', 'C', 'Grammar')
    g += close_svg()
    return g


# ─── PLATE 24D — RUNNING TEXT ─────────────────────────────────────────────────

def build_24d():
    g = open_svg()
    g += t(240, 32, 'RUSSIAN — RUNNING TEXT · PASSAGES', 'middle', 'T')
    g += t(240, 50, 'SERIES 24D OF 50 · REMEMBER FORWARD', 'middle', 'S')
    g += hr(58)

    # Passage 1 — Pushkin
    g += sh(67, 'PASSAGE 1 — PUSHKIN, EUGENE ONEGIN I.1 (1825)')
    g += t(240, 78, 'Мой дядя самых честных правил,', 'middle', 'Lr')
    g += t(240, 89, 'Moy dyadya samykh chestnykh pravil,', 'middle', 'Lx')
    g += t(240, 98, 'My uncle [of-the] most honest rules,', 'middle', 'Lx')
    g += t(240, 107, 'Когда не в шутку занемог,', 'middle', 'Lr')
    g += t(240, 118, 'Kogda ne v shutku zanemog,', 'middle', 'Lx')
    g += t(240, 127, 'When [not as a] joke fell-ill,', 'middle', 'Lx')
    g += t(240, 136, '"My uncle — of most honest principles — when he fell ill in earnest…"', 'middle', 'Ls')
    g += hr(144)

    # Passage 2 — Tolstoy
    g += sh(152, 'PASSAGE 2 — TOLSTOY, ANNA KARENINA I.1 (1877)')
    g += t(240, 163, 'Все счастливые семьи похожи друг на друга,', 'middle', 'Lr')
    g += t(240, 174, 'Vse schastlivye sem\'i pokhozhi drug na druga,', 'middle', 'Lx')
    g += t(240, 183, 'All happy families resemble one another,', 'middle', 'Lx')
    g += t(240, 192, 'каждая несчастливая семья несчастлива по-своему.', 'middle', 'Lr')
    g += t(240, 203, 'kazhdaya neschastlivaya sem\'ya neschastliva po-svoyemu.', 'middle', 'Lx')
    g += t(240, 212, '"All happy families are alike; each unhappy family is unhappy in its own way."', 'middle', 'Ls')
    g += hr(220)

    # Passage 3 — Dostoevsky
    g += sh(228, 'PASSAGE 3 — DOSTOEVSKY, THE IDIOT (1869)')
    g += t(240, 239, 'Красота спасёт мир.', 'middle', 'Lr')
    g += t(240, 250, 'Krasota spasyot mir.', 'middle', 'Lx')
    g += t(240, 259, 'Beauty will-save world/peace.', 'middle', 'Lx')
    g += t(240, 268, '"Beauty will save the world." — Note: mir means both "world" and "peace" in Russian.', 'middle', 'Ls')
    g += hr(276)

    # Passage 4 — proverb
    g += sh(284, 'PASSAGE 4 — RUSSIAN PROVERBS')
    g += t(240, 295, 'Не откладывай на завтра то, что можно сделать сегодня.', 'middle', 'Lr')
    g += t(240, 306, 'Ne otkladyvay na zavtra to, chto mozhno sdelat\' segodnya.', 'middle', 'Lx')
    g += t(240, 315, '"Do not put off until tomorrow what can be done today."', 'middle', 'Ls')
    g += t(240, 325, 'Язык до Киева доведёт.', 'middle', 'Lr')
    g += t(240, 336, 'Yazyk do Kiyeva dovedet.', 'middle', 'Lx')
    g += t(240, 345, '"The tongue will lead you to Kiev." — Ask and you will find your way.', 'middle', 'Ls')
    g += hr(353)

    # Passage 5 — Chekhov
    g += sh(361, 'PASSAGE 5 — CHEKHOV, THREE SISTERS (1901)')
    g += t(240, 372, 'В Москву! В Москву! В Москву!', 'middle', 'Lr')
    g += t(240, 383, 'V Moskvu! V Moskvu! V Moskvu!', 'middle', 'Lx')
    g += t(240, 392, '"To Moscow! To Moscow! To Moscow!" — the longing for a life not lived, a future not reached.', 'middle', 'Ls')
    g += hr(400)

    # Bridge phrase
    g += sh(409, 'BRIDGE PHRASE — REMEMBER FORWARD')
    g += t(240, 421, 'Это послание создано для вас, бесплатно, людьми, которые помнили о будущем.', 'middle', 'Lr')
    g += t(240, 433, 'Eto poslaniye sozdano dlya vas, besplatno, lyud\'mi, kotorye pomnili o budushchem.', 'middle', 'Lx')
    g += t(240, 443, 'This message  made    for  you  freely   people  who         remembered about future', 'middle', 'Lx')
    g += t(240, 452, '"This message was made for you, freely, by people who remembered the future."', 'middle', 'Ls')
    g += hr(460)

    g += sh(469, 'LANGUAGE NOTE — "FUTURE" IN RUSSIAN')
    g += t(240, 480, 'Russian: будущее (budushcheye) = "the future" — a present active participle of быть (byt\') "to be".', 'middle', 'L')
    g += t(240, 490, 'Literally: "that which is becoming / the becoming" — the future as an ongoing process, not a fixed destination.', 'middle', 'Ls')
    g += t(240, 500, 'помнили (pomnili): past imperfective — they remembered (habitually, over time), not just once.', 'middle', 'Ls')
    g += t(240, 510, 'бесплатно (besplatno): "without payment" — бес (without) + плата (payment) — freely given.', 'middle', 'Ls')
    g += t(240, 520, 'мир (mir): appears in two senses in Russian culture — "world/universe" and "peace/community".', 'middle', 'Ls')
    g += t(240, 530, 'Tolstoy\'s title Война и мир (War and Peace) plays on this — some read it as "War and the World".', 'middle', 'Ls')
    g += hr(539)

    g += sh(548, 'DECODING NOTE — FOR FUTURE READERS')
    g += t(240, 559, 'Russian is an East Slavic language, spoken by ~170 million as a first language, ~300 million total.', 'middle', 'Ls')
    g += t(240, 568, 'Cyrillic alphabet: 33 letters. If unfamiliar, consult Plate 24A for the complete letter table.', 'middle', 'Ls')
    g += t(240, 577, 'Russian is the most widely spoken Slavic language and the 8th most spoken in the world.', 'middle', 'Ls')
    g += t(240, 586, 'Related languages in Cyrillic: Ukrainian, Bulgarian, Serbian, Belarusian, Macedonian.', 'middle', 'Ls')
    g += t(240, 595, 'Russian literature is among the world\'s richest: Pushkin, Tolstoy, Dostoevsky, Chekhov, Akhmatova.', 'middle', 'Ls')

    g += footer('24', 'Russian', 'D', 'Text')
    g += close_svg()
    return g


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate24a_russian_script.svg': build_24a(),
        'plate24b_russian_phonology.svg': build_24b(),
        'plate24c_russian_grammar.svg': build_24c(),
        'plate24d_russian_text.svg': build_24d(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')


if __name__ == '__main__':
    main()
