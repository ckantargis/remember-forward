#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build French / Italian alt plate series 28A–28D for Remember Forward.
Secondary language: Italian (italiano) — spoken in Italy, Ticino (Switzerland),
Val d'Aosta. Within ~500 miles of Paris/France geographic center.
~65 million native speakers. Romance family. Most conservative heir to Latin vowels.
Geographic basis: Italy borders France; Italian is the largest Romance language
within the 500mi radius of mainland France.
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


# ─── PLATE 28A ALT — SCRIPT ───────────────────────────────────────────────────

def build_28a_alt():
    g = open_svg()
    g += t(240, 30, 'FRENCH + ITALIAN \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 28A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: FRENCH SCRIPT ──
    g += sh(63, 'FRENCH \u2014 LATIN ALPHABET \u00b7 26 LETTERS + DIACRITICS')
    g += t(240, 73, 'French uses the standard 26-letter Latin alphabet. Spelling is historically conservative \u2014 many silent letters.', 'middle', 'Ls')
    g += t(240, 82, 'Spelling preserves medieval Latin forms even when pronunciation has radically shifted.', 'middle', 'Lx')
    g += hr(89)

    g += sh(97, 'FRENCH DIACRITICS \u2014 SIX TYPES')
    diac = [
        ('\u00e9', 'Acute (aigu)', '/e/ close: \u00e9t\u00e9, pr\u00e9, b\u00e9b\u00e9'),
        ('\u00e8 \u00ea', 'Grave / Circumflex', '/\u025b/ open: m\u00e8re, f\u00eate, t\u00eate'),
        ('\u00e0 \u00f9', 'Grave (a/u)', 'Disambiguates: a (has) vs \u00e0 (to); ou vs o\u00f9'),
        ('\u00e2 \u00f4', 'Circumflex (a/o)', 'Marks long vowel or lost -s: h\u00f4pital < hospitale'),
        ('\u00eb \u00ef', 'Di\u00e9r\u00e8se (trema)', 'Vowel sounded separately: no\u00ebl, na\u00efve'),
        ('\u00e7', 'C\u00e9dille', 'C = /s/ before a/o/u: fran\u00e7ais, gar\u00e7on'),
    ]
    for i, (ch, name, func) in enumerate(diac):
        y = 107 + i * 11
        g += t(45, y, ch, 'middle', 'Ls')
        g += t(130, y, name, 'middle', 'Lx')
        g += t(330, y, func, 'middle', 'Lx')
    g += hr(177)

    g += sh(185, 'FRENCH SILENT LETTERS \u2014 KEY FEATURE')
    g += t(240, 195, 'Final consonants usually silent: grand /g\u0281\u00e3/, beaux /bo/, petit /p\u0259ti/. Liaison restores them before vowels.', 'middle', 'Ls')
    g += t(240, 204, 'eau = /o/ \u00b7 oi = /wa/ \u00b7 initial h always silent \u00b7 -ent (3rd pl verb) = silent', 'middle', 'Lx')
    g += t(240, 213, 'Liaison: les amis = /le.za.mi/ \u00b7 Elision: le + ami = l\u2019ami \u00b7 de + elle = d\u2019elle', 'middle', 'Lx')
    g += hr(221)

    g += sh(229, 'FRENCH SCRIPT HISTORY')
    g += t(240, 239, 'Serments de Strasbourg 842 CE: first document in Old French. Acad\u00e9mie fran\u00e7aise founded 1635.', 'middle', 'Ls')
    g += t(240, 248, '~80M native speakers; ~275M total. Official in 29 countries, UN, EU, African Union, Olympic Committee.', 'middle', 'Lx')

    # ── SECONDARY: ITALIAN SCRIPT ──
    g += sec_divider(258, 'SECONDARY \u2014 ITALIAN (ITALIANO) \u2014 SCRIPT \u00b7 WRITING SYSTEM')

    g += sh(284, 'ITALIAN \u2014 21-LETTER LATIN ALPHABET')
    g += t(240, 294, 'Italian uses 21 native letters: A B C D E F G H I L M N O P Q R S T U V Z.', 'middle', 'Ls')
    g += t(240, 303, 'Letters J K W X Y appear only in loanwords (jeans, whisky, taxi). Core vocabulary uses 21 letters only.', 'middle', 'Lx')
    g += t(240, 312, 'Italian spelling is highly phonemic \u2014 almost every letter is pronounced. Far fewer silent letters than French.', 'middle', 'Ls')
    g += hr(320)

    g += sh(328, 'ITALIAN DIACRITICS \u2014 ACCENT MARKS')
    it_diac = [
        ('\u00e8', 'Grave (e)', 'Open /\u025b/: \u00e8 (is), caff\u00e8, perch\u00e9 \u2192 caff\u00e8'),
        ('\u00e9', 'Acute (e)', 'Close /e/: perch\u00e9 (why/because), n\u00e9 (nor)'),
        ('\u00e0 \u00ec \u00f2 \u00f9', 'Grave (a,i,o,u)', 'Marks word-final stress: citt\u00e0, cos\u00ec, per\u00f2, virt\u00f9'),
    ]
    for i, (ch, name, func) in enumerate(it_diac):
        y = 338 + i * 11
        g += t(45, y, ch, 'middle', 'Ls')
        g += t(130, y, name, 'middle', 'Lx')
        g += t(330, y, func, 'middle', 'Lx')
    g += hr(375)

    g += sh(383, 'ITALIAN \u2014 GEMINATE CONSONANTS')
    g += t(240, 393, 'Italian doubles consonants phonemically: nono (ninth) vs. nonno (grandfather).', 'middle', 'Ls')
    g += t(240, 402, 'fato (fate) vs. fatto (done) \u00b7 casa (house) vs. cassa (cash register) \u00b7 pala (shovel) vs. palla (ball).', 'middle', 'Lx')
    g += t(240, 411, 'Written double = phonetically long consonant. This feature is absent from French. Preserved from Latin.', 'middle', 'Lx')
    g += hr(419)

    g += sh(427, 'SCRIPT BRIDGE \u2014 TWO LATIN DAUGHTERS')
    g += t(240, 437, 'Both French and Italian descend from Vulgar Latin and use the Latin alphabet.', 'middle', 'Ls')
    g += t(240, 446, 'French: heavy Germanic (Frankish) influence changed sounds radically. Spelling frozen in Old French.', 'middle', 'Lx')
    g += t(240, 455, 'Italian: more conservative. Closer to Latin vowels and pronunciation. Fewer silent letters. Geminates preserved.', 'middle', 'Lx')
    g += t(240, 464, 'Dante\u2019s Divina Commedia (1308\u20131320 CE): standardized literary Italian. First major work in Italian vernacular.', 'middle', 'Lx')

    g += footer('28', 'French', 'Italian', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 28B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_28b_alt():
    g = open_svg()
    g += t(240, 30, 'FRENCH + ITALIAN \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 28B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: FRENCH PHONOLOGY ──
    g += sh(63, 'FRENCH \u2014 VOWEL SYSTEM \u2014 12 ORAL + 4 NASAL')
    g += t(240, 73, 'French has one of the most complex vowel systems of any European language.', 'middle', 'Ls')
    g += t(240, 82, 'Front rounded vowels /y \u00f8 \u0153/ are unique among major European languages (absent from Italian, English, Spanish).', 'middle', 'Lx')
    oral = [
        ('/i/', 'vie'), ('/e/', '\u00e9t\u00e9'), ('/\u025b/', 'm\u00e8re'), ('/a/', 'patte'),
        ('/y/', 'lune'), ('/\u00f8/', 'feu'), ('/\u0153/', 'peur'), ('/u/', 'loup'),
        ('/o/', 'beau'), ('/\u0254/', 'or'), ('/\u0259/', 'le'), ('/\u0251/', 'p\u00e2te'),
    ]
    for i, (ipa, ex) in enumerate(oral):
        col = i % 4; row = i // 4
        x = 55 + col * 105; y = 92 + row * 10
        g += t(x, y, f'{ipa} {ex}', 'middle', 'Lx')
    g += t(240, 122, 'Nasal vowels: /\u00e3/ blanc \u00b7 /\u025b\u0303/ bain \u00b7 /\u0254\u0303/ bon \u00b7 /\u0153\u0303/ brun', 'middle', 'Ls')
    g += hr(130)

    g += sh(138, 'FRENCH \u2014 KEY CONSONANTS')
    g += t(240, 148, 'Uvular /\u0281/: French r is produced at the back of the throat. Not a tongue-tip trill (unlike Italian r).', 'middle', 'Ls')
    g += t(240, 157, 'Palatal nasal /\u0272/: gagner, montagne. Glides: /j/ yeux \u00b7 /w/ oui \u00b7 /\u0265/ lui (rounded palatal).', 'middle', 'Lx')
    g += t(240, 166, 'French is syllable-timed \u2014 equal syllable duration. Stress on final syllable of phrase, not word.', 'middle', 'Lx')

    g += hr(174)
    g += sh(182, 'FRENCH \u2014 NASAL VOWELS')
    g += t(240, 192, 'Nasal vowels form when vowel precedes n/m in same syllable: bon /b\u0254\u0303/, bain /b\u025b\u0303/.', 'middle', 'Ls')
    g += t(240, 201, 'The n/m disappears from the consonant inventory \u2014 the nasality is absorbed into the vowel itself.', 'middle', 'Lx')
    g += t(240, 210, 'Italian has no nasal vowels. This is one of the clearest phonological divides between the two languages.', 'middle', 'Lx')

    # ── SECONDARY: ITALIAN PHONOLOGY ──
    g += sec_divider(220, 'SECONDARY \u2014 ITALIAN (ITALIANO) \u2014 PHONOLOGY')

    g += sh(246, 'ITALIAN \u2014 VOWEL SYSTEM \u2014 7 VOWELS')
    g += t(240, 256, 'Italian has 7 vowel phonemes: /a e \u025b i o \u0254 u/ \u2014 closer to Latin than French.', 'middle', 'Ls')
    it_vowels = [
        ('/i/', 'vino (wine)', 'high front unrounded'),
        ('/e/', 'verde (green)', 'mid front close'),
        ('/\u025b/', 'bello (beautiful)', 'mid front open'),
        ('/a/', 'mare (sea)', 'low central'),
        ('/o/', 'sole (sun)', 'mid back close'),
        ('/\u0254/', 'cosa (thing)', 'mid back open'),
        ('/u/', 'luna (moon)', 'high back rounded'),
    ]
    for i, (ipa, ex, label) in enumerate(it_vowels):
        y = 266 + i * 10
        g += t(60, y, ipa, 'middle', 'Lx')
        g += t(145, y, ex, 'middle', 'Lx')
        g += t(330, y, label, 'middle', 'Lx')
    g += hr(340)

    g += sh(348, 'ITALIAN \u2014 CONSONANT INVENTORY')
    g += t(240, 358, 'Italian r: alveolar trill /r/ \u2014 tongue-tip vibration (unlike French uvular /\u0281/).', 'middle', 'Ls')
    g += t(240, 367, 'Affricates: /ts/ (pizza, grazie) \u00b7 /dz/ (zero) \u00b7 /t\u0283/ (ciao, cielo) \u00b7 /d\u0292/ (giorno, gente).', 'middle', 'Lx')
    g += t(240, 376, 'Geminate consonants: phonemically distinct length. notte (night) /n\u0254tte/ vs. note (notes) /n\u0254te/.', 'middle', 'Lx')
    g += hr(384)

    g += sh(392, 'ITALIAN \u2014 STRESS AND RHYTHM')
    g += t(240, 402, 'Italian is stress-timed. Stress is lexical and contrastive: \u00e0ncora (anchor) vs. anc\u00f3ra (still/yet).', 'middle', 'Ls')
    g += t(240, 411, 'Final-syllable accent marked with grave: citt\u00e0, virt\u00f9. Usually penultimate stress (default).', 'middle', 'Lx')
    g += hr(419)

    g += sh(427, 'PHONOLOGICAL BRIDGE \u2014 TWO ROMANCE SISTERS')
    comp = [
        ('Feature', 'French', 'Italian'),
        ('Nasal vowels', 'Yes \u2014 4 (/\u00e3 \u025b\u0303 \u0254\u0303 \u0153\u0303/)', 'No \u2014 absent'),
        ('Front rounded vowels', 'Yes \u2014 /y \u00f8 \u0153/', 'No \u2014 absent'),
        ('Geminate consonants', 'No \u2014 merged', 'Yes \u2014 phonemic'),
        ('r-sound', 'Uvular /\u0281/', 'Alveolar trill /r/'),
        ('Rhythm', 'Syllable-timed', 'Stress-timed'),
    ]
    for i, (feat, fr, it) in enumerate(comp):
        y = 437 + i * 10
        c = 'Ls' if i > 0 else 'Lx'
        g += t(90, y, feat, 'middle', c)
        g += t(255, y, fr, 'middle', 'Lx')
        g += t(395, y, it, 'middle', 'Lx')

    g += footer('28', 'French', 'Italian', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 28C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_28c_alt():
    g = open_svg()
    g += t(240, 30, 'FRENCH + ITALIAN \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 28C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: FRENCH GRAMMAR ──
    g += sh(63, 'FRENCH GRAMMAR \u2014 SVO \u00b7 OBLIGATORY SUBJECT')
    g += t(240, 73, 'French is SVO. Subject pronouns are obligatory \u2014 unlike Italian (pro-drop). Two genders: M/F.', 'middle', 'Ls')
    g += t(240, 82, 'Articles required: le/la/les (def.), un/une/des (indef.). Gender not predictable \u2014 must be memorized.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'FRENCH VERB CONJUGATION \u2014 parler')
    pres = [('je','parle'), ('tu','parles'), ('il/elle','parle'),
            ('nous','parlons'), ('vous','parlez'), ('ils/elles','parlent')]
    for i, (pro, form) in enumerate(pres):
        col = i % 2; row = i // 2
        x = 70 + col * 205; y = 108 + row * 10
        g += t(x, y, f'{pro}  {form}', 'middle', 'Ls')
    g += t(240, 140, 'Pass\u00e9 compos\u00e9: j\u2019ai parl\u00e9 (I spoke). \u00catre verbs: je suis all\u00e9(e) (I went).', 'middle', 'Lx')
    g += t(240, 149, 'Negation: ne\u2026pas: Je ne parle pas. Spoken: je parle pas (ne dropped in colloquial).', 'middle', 'Lx')
    g += hr(157)

    g += sh(165, 'FRENCH CORE VOCABULARY')
    fvocab = [
        ('eau', 'water'), ('feu', 'fire'), ('terre', 'earth'), ('personne', 'person'),
        ('lune', 'moon'), ('m\u00e9moire', 'memory'), ('avenir', 'future'), ('libert\u00e9', 'freedom'),
        ('c\u0153ur', 'heart'), ('amour', 'love'), ('monde', 'world'), ('vie', 'life'),
    ]
    for i, (fr, en) in enumerate(fvocab):
        col = i % 3; row = i // 3
        x = 65 + col * 130; y = 175 + row * 10
        g += t(x, y, fr, 'middle', 'Ls')
        g += t(x + 55, y, en, 'middle', 'Lx')

    # ── SECONDARY: ITALIAN GRAMMAR ──
    g += sec_divider(222, 'SECONDARY \u2014 ITALIAN (ITALIANO) \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(248, 'ITALIAN GRAMMAR \u2014 SVO \u00b7 PRO-DROP')
    g += t(240, 258, 'Italian is SVO and pro-drop \u2014 subject pronouns can be omitted: parla = (he/she/it) speaks.', 'middle', 'Ls')
    g += t(240, 267, 'Two genders (M/F): il libro (M), la tavola (F). Agreement: adjectives match noun gender + number.', 'middle', 'Lx')
    g += t(240, 276, 'Articles: il/la/i/le (def.), un/una (indef.). Plural: -o \u2192 -i (M), -a \u2192 -e (F): libro \u2192 libri.', 'middle', 'Lx')
    g += hr(284)

    g += sh(292, 'ITALIAN VERB CONJUGATION \u2014 parlare')
    it_pres = [('io','parlo'), ('tu','parli'), ('lui/lei','parla'),
               ('noi','parliamo'), ('voi','parlate'), ('loro','parlano')]
    for i, (pro, form) in enumerate(it_pres):
        col = i % 2; row = i // 2
        x = 70 + col * 205; y = 302 + row * 10
        g += t(x, y, f'{pro}  {form}', 'middle', 'Ls')
    g += t(240, 334, 'Passato prossimo: ho parlato (I spoke). Imperfetto: parlavo (I was speaking/used to speak).', 'middle', 'Lx')
    g += t(240, 343, 'Negation: non before verb: Non parlo italiano. Question: intonation only (Parli italiano?).', 'middle', 'Lx')
    g += hr(351)

    g += sh(359, 'ITALIAN CORE VOCABULARY')
    ivocab = [
        ('acqua', 'water'), ('fuoco', 'fire'), ('terra', 'earth'), ('persona', 'person'),
        ('luna', 'moon'), ('memoria', 'memory'), ('futuro', 'future'), ('libert\u00e0', 'freedom'),
        ('cuore', 'heart'), ('amore', 'love'), ('mondo', 'world'), ('vita', 'life'),
    ]
    for i, (it, en) in enumerate(ivocab):
        col = i % 3; row = i // 3
        x = 65 + col * 130; y = 369 + row * 10
        g += t(x, y, it, 'middle', 'Ls')
        g += t(x + 55, y, en, 'middle', 'Lx')

    g += hr(412)
    g += sh(420, 'SIDE-BY-SIDE \u2014 LATIN INHERITANCE')
    comp = [
        ('CONCEPT', 'FRENCH', 'ITALIAN', 'LATIN ORIGIN'),
        ('water', 'eau', 'acqua', 'aqua'),
        ('fire', 'feu', 'fuoco', 'focus'),
        ('earth', 'terre', 'terra', 'terra'),
        ('person', 'personne', 'persona', 'persona'),
        ('heart', 'c\u0153ur', 'cuore', 'cor/cordis'),
        ('world', 'monde', 'mondo', 'mundus'),
        ('freedom', 'libert\u00e9', 'libert\u00e0', 'libertas'),
    ]
    for i, row in enumerate(comp):
        y = 430 + i * 10
        g += t(60, y, row[0], 'middle', 'Lx')
        g += t(175, y, row[1], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(290, y, row[2], 'middle', 'Ls' if i > 0 else 'Lx')
        g += t(400, y, row[3], 'middle', 'Lx')

    g += footer('28', 'French', 'Italian', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 28D ALT — RUNNING TEXT ─────────────────────────────────────────────

def build_28d_alt():
    g = open_svg()
    g += t(240, 30, 'FRENCH + ITALIAN \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 28D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: FRENCH TEXT ──
    g += sh(63, 'I. DESCARTES \u2014 DISCOURS DE LA M\u00c9THODE (1637)')
    g += t(240, 73, 'Je pense, donc je suis.', 'middle', 'L')
    g += t(240, 83, 'I  think  therefore I   am. \u2014 "I think, therefore I am." Foundation of modern Western philosophy.', 'middle', 'Lx')
    g += hr(91)

    g += sh(99, 'II. VICTOR HUGO \u2014 LES MIS\u00c9RABLES (1862)')
    g += t(240, 109, 'Aimer, c\u2019est agir.', 'middle', 'L')
    g += t(240, 119, '"To love is to act." \u2014 Hugo. One of the most translated novels in history.', 'middle', 'Lx')
    g += hr(127)

    g += sh(135, 'III. D\u00c9CLARATION DES DROITS DE L\u2019HOMME (1789)')
    g += t(240, 145, 'Les hommes naissent et demeurent libres et \u00e9gaux en droits.', 'middle', 'L')
    g += t(240, 155, '"Men are born and remain free and equal in rights." \u2014 Article 1.', 'middle', 'Lx')
    g += hr(163)

    g += sh(171, 'IV. FRENCH BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 182, 'Ce message a \u00e9t\u00e9 fait pour vous, gratuitement,', 'middle', 'L')
    g += t(240, 194, 'par des personnes qui se sont souvenues de l\u2019avenir.', 'middle', 'L')
    g += t(240, 206, 'This was made for you freely by people who remembered the future.', 'middle', 'Lx')
    g += t(240, 215, '"This was made for you, freely, by people who remembered the future." (French)', 'middle', 'F')
    g += hr(223)

    g += sh(231, 'FRENCH NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 241, 'Avenir = \u00e0 + venir: \u201cto come toward\u201d \u2014 the future as what comes to us. Se souvenir = to come to oneself again.', 'middle', 'Ls')
    g += t(240, 250, 'Gratuitement = freely. Pass\u00e9 compos\u00e9 (se sont souvenues): completed act, feminine agreement.', 'middle', 'Lx')

    # ── SECONDARY: ITALIAN TEXT ──
    g += sec_divider(260, 'SECONDARY \u2014 ITALIAN (ITALIANO) \u2014 RUNNING TEXT \u00b7 PASSAGES')

    g += sh(286, 'I. DANTE ALIGHIERI \u2014 DIVINA COMMEDIA (c.1308\u20131320 CE)')
    g += t(240, 296, 'Nel mezzo del cammin di nostra vita', 'middle', 'L')
    g += t(240, 307, 'mi ritrovai per una selva oscura.', 'middle', 'L')
    g += t(240, 318, 'In the middle of  the journey of  our    life  I found-myself in  a  forest  dark.', 'middle', 'Lx')
    g += t(240, 327, '"In the middle of the journey of our life, I found myself in a dark forest." \u2014 Inferno, Canto I.', 'middle', 'F')
    g += hr(335)

    g += sh(343, 'II. ITALIAN PROVERB \u2014 ON MEMORY')
    g += t(240, 353, 'Chi non ricorda il passato \u00e8 condannato a ripeterlo.', 'middle', 'L')
    g += t(240, 364, 'Who not remembers the past  is condemned to repeat-it.', 'middle', 'Lx')
    g += t(240, 373, '"He who does not remember the past is condemned to repeat it." (Italian proverb, attr. Santayana)', 'middle', 'F')
    g += hr(381)

    g += sh(389, 'III. ITALIAN BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 400, 'Questo \u00e8 stato fatto per voi, gratuitamente,', 'middle', 'L')
    g += t(240, 412, 'da persone che hanno ricordato il futuro.', 'middle', 'L')
    g += t(240, 424, 'This  has been made   for you  freely       by people  who  have   remembered the  future.', 'middle', 'Lx')
    g += t(240, 433, '"This was made for you, freely, by people who remembered the future." (Italian)', 'middle', 'F')
    g += hr(441)

    g += sh(449, 'ITALIAN NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 459, 'Futuro: from Latin futurus (about to be). Ricordare = to remember \u2014 from re + cor/cordis (heart).', 'middle', 'Ls')
    g += t(240, 468, 'To remember in Italian is literally to \u201cbring back to the heart.\u201d The etymology reveals the felt quality of memory.', 'middle', 'Lx')
    g += t(240, 477, 'Gratuitamente = freely/gratis. Passato prossimo (hanno ricordato): completed act, personal relevance.', 'middle', 'Lx')
    g += hr(485)

    g += sh(493, 'LANGUAGE BRIDGE \u2014 TWO ROMANCE NEIGHBORS')
    g += t(240, 503, 'French: ~80M native speakers. Official in 29 countries. Uvular r, nasal vowels, silent letters.', 'middle', 'Ls')
    g += t(240, 512, 'Italian: ~65M native speakers. Official in Italy, San Marino, Switzerland (Ticino/Val d\u2019Aosta).', 'middle', 'Ls')
    g += t(240, 521, 'Both descended from Vulgar Latin. Diverged after ~5th c. CE as Roman Empire fragmented.', 'middle', 'Lx')
    g += t(240, 530, 'Italian preserved more Latin phonology; French underwent radical Germanic-influenced sound changes.', 'middle', 'Lx')

    g += footer('28', 'French', 'Italian', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate28a_french_italian_script_alt.svg':    build_28a_alt(),
        'plate28b_french_italian_phonology_alt.svg': build_28b_alt(),
        'plate28c_french_italian_grammar_alt.svg':   build_28c_alt(),
        'plate28d_french_italian_text_alt.svg':      build_28d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
