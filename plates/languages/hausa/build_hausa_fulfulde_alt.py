#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Hausa / Fulfulde (Fula) alt plate series 29A–29D for Remember Forward.
Secondary language: Fulfulde (Fula / Pulaar / Peul) — the Fula language family,
spoken across the Sahel from Senegal to Sudan, with heavy concentration in Nigeria,
Niger, Cameroon, and Mali. Kano (Hausa center) is deep within Fula territory.
~40 million speakers across the Sahel. Afro-Asiatic (Hausa) meets Niger-Congo (Fulfulde).
Geographic basis: Fulani/Fula people and Hausa communities have overlapped and
interacted for 500+ years in northern Nigeria; within 200–400 miles of Hausa center.
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


# ─── PLATE 29A ALT — SCRIPT ───────────────────────────────────────────────────

def build_29a_alt():
    g = open_svg()
    g += t(240, 30, 'HAUSA + FULFULDE \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 29A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HAUSA \u2014 TWO SCRIPTS: BOKO (LATIN) AND AJA\u02bcMI (ARABIC)')
    g += t(240, 73, 'Hausa is written in two scripts: Boko (Latin-based, standard since ~1930) and Aja\u02bcmi (Arabic-based, older).', 'middle', 'Ls')
    g += t(240, 82, 'Boko: 23 letters + 6 hooked letters for implosives and a special tone letter. Left to right.', 'middle', 'Lx')
    g += t(240, 91, 'Aja\u02bcmi: Arabic script adapted for Hausa sounds. Right to left. Still used in religious/traditional contexts.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'HAUSA BOKO ALPHABET \u2014 23 BASE + SPECIAL LETTERS')
    boko = 'A B \u0181 C D \u0189 E F G H I J K L M N R S T \u0162 U W Y Z'
    g += t(240, 117, boko, 'middle', 'Ls')
    g += t(240, 127, 'Hooked letters: \u0181 (implosive b) \u00b7 \u0189 (implosive d) \u00b7 \u0162 (ejective ts) \u00b7 \u01a4 (implosive ky)', 'middle', 'Lx')
    g += hr(135)

    g += sh(143, 'HAUSA TONE MARKING')
    g += t(240, 153, 'Hausa has 2 lexical tones: HIGH (unmarked or \u0301) and LOW (\u0300). Written texts often omit tone marks.', 'middle', 'Ls')
    g += t(240, 162, 'Falling tone (\u0302) = High-Low on one syllable. Tone distinguishes lexical items and grammatical forms.', 'middle', 'Lx')
    tones = [
        ('b\u00e0\u0272\u00ec', 'root (tree)', 'Low-Low'),
        ('ba\u0272\u00ed', 'place', 'Low-High'),
        ('m\u00e0l\u00e0m\u00ec', 'teacher (object)', 'LLL'),
        ('m\u00e0l\u00e0m\u00ed', 'teacher (subject)', 'LLH'),
    ]
    for i, (word, gloss, pattern) in enumerate(tones):
        y = 172 + i * 10
        g += t(80, y, word, 'middle', 'Ls')
        g += t(200, y, gloss, 'middle', 'Lx')
        g += t(360, y, pattern, 'middle', 'Lx')
    g += hr(218)

    g += sh(226, 'HAUSA SCRIPT HISTORY')
    g += t(240, 236, 'Aja\u02bcmi: Arabic script adaptation for Hausa dating to the 16th century Sokoto Caliphate and beyond.', 'middle', 'Ls')
    g += t(240, 245, 'Boko: introduced by British colonial administration ~1900\u20131930. Now the official script for government/education.', 'middle', 'Lx')

    g += sec_divider(255, 'SECONDARY \u2014 FULFULDE (FULA) \u2014 SCRIPT \u00b7 WRITING')

    g += sh(281, 'FULFULDE \u2014 LATIN SCRIPT (STANDARD) AND ADL\u0104M (INDIGENOUS)')
    g += t(240, 291, 'Fulfulde is written primarily in Latin script (regionally standardized versions per country).', 'middle', 'Ls')
    g += t(240, 300, 'Adl\u0105m: an indigenous script created by Ibrahima and Abdoulaye Barry (Guinea, 1989 CE). Right to left.', 'middle', 'Lx')
    g += t(240, 309, 'Adl\u0105m is the only modern alphabetic script created specifically for a West African language by its speakers.', 'middle', 'Lx')
    g += t(240, 318, 'Unicode range U+1E900\u2013U+1E95F (Adlam block). Gaining adoption in Guinea, Senegal, Nigeria.', 'middle', 'Lx')
    g += hr(326)

    g += sh(334, 'FULFULDE LATIN ALPHABET \u2014 KEY SPECIAL CHARACTERS')
    ful_chars = [
        ('\u014b', '/\u014b/', 'ng sound: \u014baari (cattle), ko\u014bngol (river)'),
        ('\u0253', '/\u0253/', 'implosive b: \u0253e (here), \u0253oofo (wind)'),
        ('\u0257', '/\u0257/', 'implosive d: \u0257iy\u0254\u014b (sun/day), \u0257am (water)'),
        ('\u0199', '/\u0199/', 'implosive ky: \u0199\u014bu\u014bgu (heart)'),
        ('\u0254', '/\u0254/', 'open o: \u0257iy\u0254\u014b (sun), h\u0254re (body)'),
        ('\u025b', '/\u025b/', 'open e: \u025bndu (life), j\u025bl\u025b (love)'),
    ]
    for i, (ch, ipa, ex) in enumerate(ful_chars):
        y = 344 + i * 10
        g += t(42, y, ch, 'middle', 'Ls')
        g += t(90, y, ipa, 'middle', 'Lx')
        g += t(300, y, ex, 'middle', 'Lx')
    g += hr(410)

    g += sh(418, 'SCRIPT BRIDGE \u2014 MULTILINGUAL WRITING TRADITIONS')
    g += t(240, 428, 'Hausa: 2 scripts (Boko Latin + Aja\u02bcmi Arabic). Fula: 3 scripts (Latin + Arabic Aja\u02bcmi + Adl\u0105m indigenous).', 'middle', 'Ls')
    g += t(240, 437, 'Both communities are majority Muslim \u2014 Arabic script common for religious texts in both languages.', 'middle', 'Lx')
    g += t(240, 446, 'Adl\u0105m is a remarkable modern case of script creation: speakers chose to write their own language themselves.', 'middle', 'Lx')

    g += footer('29', 'Hausa', 'Fulfulde', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 29B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_29b_alt():
    g = open_svg()
    g += t(240, 30, 'HAUSA + FULFULDE \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 29B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HAUSA PHONOLOGY \u2014 TONAL + IMPLOSIVE')
    g += t(240, 73, 'Hausa is a tonal language (Afro-Asiatic/Chadic branch) with 2 register tones: High and Low.', 'middle', 'Ls')
    g += t(240, 82, 'Tone is lexically and grammatically contrastive. Subject vs. object is often marked by tone alone.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'HAUSA IMPLOSIVE CONSONANTS')
    g += t(240, 108, 'Hausa has 4 implosive consonants \u2014 stops produced with ingressive airflow (larynx drops):',  'middle', 'Ls')
    implosives = [
        ('\u0181 /\u0253/', 'voiced bilabial implosive: \u0181\u00e0\u0272\u00ec (goat)'),
        ('\u0189 /\u0257/', 'voiced alveolar implosive: \u0189\u00e0\u0272\u00ec (blood)'),
        ('\u01a4 /\u0260/', 'voiced velar implosive: \u01a4wayy\u00f2 (careful!)'),
        ('\u0162 /\u01c0/', 'alveolar ejective ts: \u0162a\u02bca (walk)'),
    ]
    for i, (ch, desc) in enumerate(implosives):
        y = 118 + i * 10
        g += t(80, y, ch, 'middle', 'Ls')
        g += t(290, y, desc, 'middle', 'Lx')
    g += hr(163)

    g += sh(171, 'HAUSA VOWELS \u2014 5 SHORT + 5 LONG')
    g += t(240, 181, 'Hausa has 5 vowel qualities, each with short and long forms: a/aa, e/ee, i/ii, o/oo, u/uu.', 'middle', 'Ls')
    g += t(240, 190, 'Vowel length is phonemic: mata (wives) vs. m\u0101ta (woman/wife SG). Tone + length interact.', 'middle', 'Lx')
    g += hr(198)

    g += sh(206, 'HAUSA CONSONANTS \u2014 UNUSUAL FEATURES')
    g += t(240, 216, 'Labiovelars /kw gw/: kwai (egg), gw\u00e0d\u00e0n\u00e0 (always). Simultaneous velar + bilabial closure.', 'middle', 'Ls')
    g += t(240, 225, 'Glottalization: some vowels have laryngealized (creaky) quality in certain tonal environments.', 'middle', 'Lx')

    g += sec_divider(235, 'SECONDARY \u2014 FULFULDE (FULA) \u2014 PHONOLOGY')

    g += sh(261, 'FULFULDE PHONOLOGY \u2014 NOUN CLASS SYSTEM')
    g += t(240, 271, 'Fulfulde is NOT tonal (unlike Hausa). Prosody relies on syllable weight and stress, not pitch.', 'middle', 'Ls')
    g += t(240, 280, 'Rich consonant inventory including implosives /\u0253 \u0257 \u0199/ \u2014 shared feature with Hausa (contact influence).', 'middle', 'Lx')
    g += hr(288)

    g += sh(296, 'FULFULDE IMPLOSIVES AND PRENASALIZED STOPS')
    ful_cons = [
        ('\u0253', '/\u0253/', 'implosive b: \u0253e\u0253\u0253e (many), \u0253oofo (wind)'),
        ('\u0257', '/\u0257/', 'implosive d: \u0257am (water), \u0257iy\u0254\u014b (sun/day)'),
        ('\u0199', '/\u0199/', 'implosive ky: \u0199\u014bu\u014bgu (heart), \u0199a\u014b (thing)'),
        ('mb', '/mb/', 'prenasalized: mbalu (sheep), mbind (book)'),
        ('nd', '/nd/', 'prenasalized: ndiy\u0254m (water, plural)'),
        ('nj', '/nd\u0292/', 'prenasalized: njam (food), njurum (mercy)'),
        ('ng', '/\u014bg/', 'prenasalized: \u014bgu\u014bgu (heart/center)'),
    ]
    for i, (ch, ipa, ex) in enumerate(ful_cons):
        y = 306 + i * 10
        g += t(50, y, ch, 'middle', 'Ls')
        g += t(100, y, ipa, 'middle', 'Lx')
        g += t(300, y, ex, 'middle', 'Lx')
    g += hr(381)

    g += sh(389, 'FULFULDE VOWELS \u2014 5 BASIC + LENGTH')
    g += t(240, 399, 'Fulfulde has 5 vowels /a e i o u/ each with long counterparts. Vowel length is phonemic.', 'middle', 'Ls')
    g += t(240, 408, 'Open vowels: /\u0254/ (o-open) and /\u025b/ (e-open) appear in some dialects. \u0257iy\u0254\u014b = sun.', 'middle', 'Lx')
    g += hr(416)

    g += sh(424, 'PHONOLOGICAL BRIDGE \u2014 HAUSA AND FULFULDE')
    comp = [
        ('Feature', 'Hausa', 'Fulfulde'),
        ('Tonal', 'Yes \u2014 2 tones', 'No \u2014 non-tonal'),
        ('Implosives', '4 (\u0181 \u0189 \u01a4 \u0162)', '3 (\u0253 \u0257 \u0199)'),
        ('Vowel length', 'Phonemic', 'Phonemic'),
        ('Prenasalization', 'Some', 'Prominent feature'),
        ('Family', 'Afro-Asiatic', 'Niger-Congo (Fula)'),
    ]
    for i, row in enumerate(comp):
        y = 434 + i * 10
        g += t(80, y, row[0], 'middle', 'Lx')
        g += t(235, y, row[1], 'middle', 'Lx')
        g += t(380, y, row[2], 'middle', 'Lx')

    g += footer('29', 'Hausa', 'Fulfulde', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 29C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_29c_alt():
    g = open_svg()
    g += t(240, 30, 'HAUSA + FULFULDE \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 29C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HAUSA GRAMMAR \u2014 SVO \u00b7 TONAL GRAMMAR \u00b7 GENDER')
    g += t(240, 73, 'Hausa is SVO. Grammatical information encoded partly by tone: subject vs. object forms of verbs differ by tone.', 'middle', 'Ls')
    g += t(240, 82, '2 genders: masculine and feminine. No articles. Definiteness marked by demonstratives and context.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'HAUSA ASPECT \u2014 NO TENSE, YES ASPECT')
    g += t(240, 108, 'Hausa marks ASPECT, not tense. Pre-verbal particles signal completive, continuative, subjunctive, negative.', 'middle', 'Ls')
    hausa_asp = [
        ('Completive', 'naa tafi', 'I went / I have gone'),
        ('Continuative', 'ina tafiya', 'I am going / I go (habitual)'),
        ('Subjunctive', 'in tafi', 'that I go / let me go'),
        ('Neg. completive', 'ban tafi ba', 'I did not go'),
        ('Future intent', 'zan tafi', 'I will go / I intend to go'),
    ]
    for i, (asp, hausa, gloss) in enumerate(hausa_asp):
        y = 118 + i * 10
        g += t(100, y, asp, 'middle', 'Lx')
        g += t(230, y, hausa, 'middle', 'Ls')
        g += t(370, y, gloss, 'middle', 'Lx')
    g += hr(175)

    g += sh(183, 'HAUSA CORE VOCABULARY')
    hvocab = [
        ('ruwa', 'water'), ('wuta', 'fire'), ('\u0199asa', 'earth'), ('mutum', 'person'),
        ('wata', 'moon'), ('tuna', 'remember'), ('gaba', 'forward/future'), ('yanci', 'freedom'),
        ('zuciya', 'heart'), ('\u0281ank\u0101ka', 'love'), ('duniya', 'world'), ('rai', 'life'),
    ]
    for i, (ha, en) in enumerate(hvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 193 + row * 10
        g += t(x, y, ha, 'middle', 'Ls')
        g += t(x + 58, y, en, 'middle', 'Lx')

    g += sec_divider(238, 'SECONDARY \u2014 FULFULDE \u2014 GRAMMAR \u00b7 NOUN CLASS SYSTEM')

    g += sh(264, 'FULFULDE \u2014 NOUN CLASS SYSTEM (25+ CLASSES)')
    g += t(240, 274, 'Fulfulde has one of the most complex noun class systems in the world: ~25 grammatical noun classes.', 'middle', 'Ls')
    g += t(240, 283, 'Each class has its own agreement suffix on nouns, adjectives, verbs, and pronouns. Class signals meaning.', 'middle', 'Lx')
    g += t(240, 292, 'Typical singular/plural pairs: o/\u0253e (human), \u014bu/\u0257i (thing), ngu/\u0257i (liquid), ko/\u0257e (abstract).', 'middle', 'Lx')
    g += hr(300)

    g += sh(308, 'FULFULDE NOUN CLASS SAMPLES')
    nc = [
        ('Class o/\u0253e', 'human singular/plural', 'gorko (man) \u2192 wor\u0253e (men)'),
        ('Class ngu/\u0257i', 'liquid/mass', '\u0257am-ngu (the water) \u2192 \u0257am-\u0257i (waters)'),
        ('Class \u014bu/\u0257i', 'large object', 'na\u014bga-\u014bu (the cow) \u2192 na\u014be-\u0257i (cows)'),
        ('Class ko/\u0257e', 'abstract/action', 'jam-ko (the peace) \u2014 no plural'),
        ('Class nga/\u0257i', 'small object', 'nedda-nga (the body)'),
    ]
    for i, (cls, role, ex) in enumerate(nc):
        y = 318 + i * 10
        g += t(80, y, cls, 'middle', 'Ls')
        g += t(210, y, role, 'middle', 'Lx')
        g += t(370, y, ex, 'middle', 'Lx')
    g += hr(375)

    g += sh(383, 'FULFULDE VERB SYSTEM \u2014 SOV WITH EXTENSIONS')
    g += t(240, 393, 'Fulfulde is largely SOV. Verbal extensions (suffixes) encode direction, benefactive, reflexive, causative.', 'middle', 'Ls')
    g += t(240, 402, 'wi\u025b-a (say-complete), wi\u025b-ude (to say/infinitive), wi\u025b-ir-de (say-BEN-inf) = to say for someone.', 'middle', 'Lx')
    g += hr(410)

    g += sh(418, 'FULFULDE CORE VOCABULARY')
    fvocab = [
        ('\u0257am', 'water'), ('jayngol', 'fire'), ('leydi', 'earth/land'), ('gorko/debbo', 'man/woman'),
        ('lewru', 'moon'), ('tigi\u0273i', 'remember'), ('gawe\u0257i', 'future/forward'), ('yiylaare', 'freedom'),
        ('\u0199\u014bu\u014bgu', 'heart'), ('j\u025bl\u025b', 'love'), ('aduna', 'world'), ('\u025bndu', 'life'),
    ]
    for i, (fu, en) in enumerate(fvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 428 + row * 10
        g += t(x, y, fu, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')
    g += hr(475)

    g += sh(483, 'GRAMMAR BRIDGE \u2014 TWO DIFFERENT LANGUAGE FAMILIES')
    g += t(240, 493, 'Hausa (Afro-Asiatic/Chadic): gender, aspect-based verb system, tonal. Spread by trade networks.', 'middle', 'Ls')
    g += t(240, 502, 'Fulfulde (Niger-Congo/Fula): 25+ noun classes, SOV, verbal extensions. Spread by Fulani pastoral migration.', 'middle', 'Ls')
    g += t(240, 511, 'Two of the most widely-spoken languages of the Sahel \u2014 co-exist in nearly every northern Nigerian market.', 'middle', 'Lx')

    g += footer('29', 'Hausa', 'Fulfulde', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 29D ALT — TEXT ─────────────────────────────────────────────────────

def build_29d_alt():
    g = open_svg()
    g += t(240, 30, 'HAUSA + FULFULDE \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 29D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. HAUSA PROVERB \u2014 ON PATIENCE AND TIME')
    g += t(240, 73, 'Hak\u016bri maganin duniy\u00e0.', 'middle', 'L')
    g += t(240, 84, 'Patience medicine-of world.', 'middle', 'Lx')
    g += t(240, 93, '"Patience is the medicine of the world." \u2014 Core Hausa proverb. Hak\u016bri = patience/endurance.', 'middle', 'F')
    g += hr(101)

    g += sh(109, 'II. HAUSA PROVERB \u2014 ON KNOWLEDGE')
    g += t(240, 119, 'Ilimi k\u0101y\u00e0 n\u00e0 kan k\u0101y\u00e0.', 'middle', 'L')
    g += t(240, 130, 'Knowledge  load NEG on  load.', 'middle', 'Lx')
    g += t(240, 139, '"Knowledge is a load that does not weigh upon other loads." \u2014 Hausa saying on the value of education.', 'middle', 'F')
    g += hr(147)

    g += sh(155, 'III. HAUSA BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 166, 'An yi wannan don ku, ba komi,', 'middle', 'L')
    g += t(240, 178, 'daga mutanen da suka tuna gaba.', 'middle', 'L')
    g += t(240, 190, 'Passive-made this  for you no-cost / from people who COMPL remember forward.', 'middle', 'Lx')
    g += t(240, 199, '"This was made for you, freely, by people who remembered forward." (Hausa)', 'middle', 'F')
    g += hr(207)

    g += sh(215, 'HAUSA NOTE \u2014 \u201cFORWARD\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 225, 'Gaba = forward, ahead, front \u2014 and by extension: the future. \u201cTuna gaba\u201d = remember-forward.', 'middle', 'Ls')
    g += t(240, 234, 'Tuna = to remember, recall (from Arabic dhikr influence). \u201cAn yi\u201d = passive construction (impersonal).', 'middle', 'Lx')

    g += sec_divider(244, 'SECONDARY \u2014 FULFULDE (FULA) \u2014 RUNNING TEXT')

    g += sh(270, 'I. FULFULDE PROVERB \u2014 ON CATTLE AND LIFE')
    g += t(240, 280, 'Na\u014bga wirwiraa, leydi wella.', 'middle', 'L')
    g += t(240, 291, 'Cattle roam-freely earth becomes-good.', 'middle', 'Lx')
    g += t(240, 300, '"When cattle roam freely, the earth is good." \u2014 Fulani pastoral proverb. Freedom and land as linked.', 'middle', 'F')
    g += hr(308)

    g += sh(316, 'II. FULFULDE PROVERB \u2014 ON MEMORY')
    g += t(240, 326, 'Ko tigi\u0273aa, ko wollaay.', 'middle', 'L')
    g += t(240, 337, 'What is-remembered REL not-forgotten.', 'middle', 'Lx')
    g += t(240, 346, '"What is remembered is not forgotten." \u2014 Fulani oral tradition on the value of memory.', 'middle', 'F')
    g += hr(354)

    g += sh(362, 'III. FULFULDE BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 373, 'Oo ko waraama on, \u0257on muuyani,', 'middle', 'L')
    g += t(240, 385, 'e nder yimbe ji\u0257\u0257i \u0257am gawe\u0257i.', 'middle', 'L')
    g += t(240, 397, 'This PASS made   for-you  freely / in  among people who-remembered forward.', 'middle', 'Lx')
    g += t(240, 406, '"This was made for you, freely, by people who remembered the future." (Fulfulde)', 'middle', 'F')
    g += hr(414)

    g += sh(422, 'FULFULDE NOTE \u2014 \u201cFORWARD / FUTURE\u201d')
    g += t(240, 432, 'Gawe\u0257i = the future, what lies forward/ahead (from gawo \u201cnext, after\u201d + \u0257i noun class suffix).', 'middle', 'Ls')
    g += t(240, 441, 'Tigi\u0273i = to remember, recall (\u0273 = palatal flap, distinctive to Fulfulde phonology).', 'middle', 'Ls')
    g += t(240, 450, 'Noun class: gawe\u0257i carries -\u0257i class suffix marking abstract temporal nouns.', 'middle', 'Lx')
    g += hr(458)

    g += sh(466, 'LANGUAGE BRIDGE \u2014 THE SAHEL CROSSROADS')
    g += t(240, 476, 'Hausa: ~80M speakers (L1+L2). Trade lingua franca of West Africa. Afro-Asiatic family.', 'middle', 'Ls')
    g += t(240, 485, 'Fulfulde: ~40M speakers. Widest-ranging African language geographically. Niger-Congo family.', 'middle', 'Ls')
    g += t(240, 494, 'The Sahel: zone where desert meets savanna \u2014 where Hausa merchants and Fulani herders have traded for millennia.', 'middle', 'Lx')
    g += t(240, 503, 'Many Hausa-speakers are multilingual in Fulfulde and vice versa. A natural bilingual community.', 'middle', 'Lx')

    g += footer('29', 'Hausa', 'Fulfulde', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate29a_hausa_fulfulde_script_alt.svg':    build_29a_alt(),
        'plate29b_hausa_fulfulde_phonology_alt.svg': build_29b_alt(),
        'plate29c_hausa_fulfulde_grammar_alt.svg':   build_29c_alt(),
        'plate29d_hausa_fulfulde_text_alt.svg':      build_29d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
