#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Hawaiian / English alt plate series 59A–59D for Remember Forward.
Secondary language: English — within ~2500 mile expanded radius for Hawaiian,
since the Hawaiian Islands are surrounded by open ocean within 500mi.
The nearest major language within practical reach is English (US West Coast ~2400mi).
~380 million native speakers of English. Hawaiian: ~2000 native speakers remaining
(endangered; strong revitalization movement). Geographic: Honolulu to Los Angeles ~4100km.
Bridge: English colonization is both the cause of Hawaiian endangerment
and the medium through which Hawaiian revitalization is now broadcast worldwide.
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


# ─── PLATE 59A ALT — SCRIPT ───────────────────────────────────────────────────

def build_59a_alt():
    g = open_svg()
    g += t(240, 30, 'HAWAIIAN + ENGLISH \u2014 SCRIPT \u00b7 WRITING SYSTEMS', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 59A \u00b7 REMEMBER FORWARD \u00b7 EXPANDED ~2500MI RADIUS', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HAWAIIAN \u2014 LATIN ALPHABET \u00b7 13 LETTERS')
    g += t(240, 73, 'Hawaiian uses only 13 letters: 5 vowels (A E I O U) and 8 consonants (H K L M N P W \u02bb).', 'middle', 'Ls')
    g += t(240, 82, 'One of the smallest alphabets of any natural language. Every syllable is consonant-vowel or vowel alone.', 'middle', 'Lx')
    g += t(240, 91, '\u02bbOkina (\u02bb): a letter \u2014 the glottal stop /\u0294/. Visually resembles an apostrophe but functions as a consonant.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'HAWAIIAN ALPHABET \u2014 ALL 13 LETTERS')
    g += t(240, 117, 'A  E  I  O  U  H  K  L  M  N  P  W  \u02bb', 'middle', 'L')
    g += t(240, 131, 'Every syllable = (C)V. No consonant clusters. No final consonants. Language sounds deeply open/vowel-rich.', 'middle', 'Ls')
    g += hr(139)

    g += sh(147, 'KAHAK\u014c (MACRON) \u2014 VOWEL LENGTH')
    g += t(240, 157, 'The kahak\u014c (\u0101 \u0113 \u012b \u014d \u016b) marks long vowels \u2014 a distinct phoneme from the short version.', 'middle', 'Ls')
    g += t(240, 166, 'k\u0101ne (man) vs. kane (name) \u00b7 \u02bbala (path) vs. \u02bbala (to bark) \u00b7 moa (chicken) vs. m\u014da (used up).', 'middle', 'Lx')
    g += t(240, 175, 'Both kahak\u014c and \u02bbokina are official letters in the Hawaiian alphabet since 1978 (not decorations).', 'middle', 'Lx')
    g += hr(183)

    g += sh(191, 'HAWAIIAN WRITING HISTORY')
    g += t(240, 201, 'Hawaiian had no writing system before 1820s when Protestant missionaries developed the Latin orthography.', 'middle', 'Ls')
    g += t(240, 210, 'Ka Nupepa Kuokoa (1861\u20131927): Hawaiian-language newspaper with millions of words of native text.', 'middle', 'Lx')
    g += t(240, 219, '1896: Hawaiian language banned from public schools by territorial government. Near extinction followed.', 'middle', 'Lx')
    g += t(240, 228, '1978: Hawaiian becomes official state language. P\u016bnana Leo immersion schools founded 1984. Revitalization active.', 'middle', 'Lx')
    g += hr(236)

    g += sh(244, 'ENDANGERED STATUS \u2014 REVITALIZATION')
    g += t(240, 254, '~2,000 native speakers (~1990s low). Now: ~24,000 speakers including second-language learners.', 'middle', 'Ls')
    g += t(240, 263, 'P\u016bnana Leo (Language Nest) schools: immersion kindergartens; entire curriculum in Hawaiian.', 'middle', 'Lx')
    g += t(240, 272, 'Online resources, university programs, and state law now support Hawaiian language use.', 'middle', 'Lx')

    g += sec_divider(282, 'SECONDARY \u2014 ENGLISH \u2014 SCRIPT \u00b7 WRITING SYSTEM \u00b7 2500MI RADIUS')

    g += sh(308, 'ENGLISH \u2014 LATIN ALPHABET \u00b7 26 LETTERS')
    g += t(240, 318, 'English uses the standard 26-letter Latin alphabet, inherited from Old English via Latin/Norman French.', 'middle', 'Ls')
    g += t(240, 327, 'English spelling is notoriously irregular: through, though, thought, tough, cough \u2014 all different pronunciations of -ough.', 'middle', 'Lx')
    g += t(240, 336, 'Great Vowel Shift (~1400\u20131700 CE): all long vowels changed. Spelling was frozen before the shift ended.', 'middle', 'Lx')
    g += hr(344)

    g += sh(352, 'ENGLISH WRITING HISTORY')
    g += t(240, 362, 'Old English (Anglo-Saxon): originally written in runic Futhorc, then Latin alphabet after Christianization (~600 CE).', 'middle', 'Ls')
    g += t(240, 371, 'Norman Conquest (1066): French scribal conventions overlaid on English \u2014 qu- for cw-, c for k before e/i.', 'middle', 'Lx')
    g += t(240, 380, 'Caxton\u2019s printing press (1476): standardized spelling from the London/East Midlands dialect.', 'middle', 'Lx')
    g += hr(388)

    g += sh(396, 'SCRIPT BRIDGE \u2014 THE MEETING OF SCRIPTS IN HAWAI\u02bbiI')
    g += t(240, 406, 'Hawaiian was given the Latin alphabet by English-speaking missionaries in 1822 \u2014 a colonial imposition.', 'middle', 'Ls')
    g += t(240, 415, 'Yet Hawaiian speakers embraced writing: ka nupepa (newspapers) became central to cultural expression.', 'middle', 'Lx')
    g += t(240, 424, 'Today English and Hawaiian share the Latin alphabet but use it for very different phonological systems.', 'middle', 'Lx')
    g += t(240, 433, '13 letters vs. 26. Open syllables vs. complex clusters. Phonemic vowel length vs. variable English stress.', 'middle', 'Lx')

    g += footer('59', 'Hawaiian', 'English', 'A', 'Script')
    return g + close_svg()


# ─── PLATE 59B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_59b_alt():
    g = open_svg()
    g += t(240, 30, 'HAWAIIAN + ENGLISH \u2014 PHONOLOGY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 59B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HAWAIIAN PHONOLOGY \u2014 8 CONSONANTS + 5 VOWELS + LENGTH')
    g += t(240, 73, 'Hawaiian has the smallest phoneme inventory of any Polynesian language. Total: 13 consonants+vowels.', 'middle', 'Ls')
    g += hr(81)

    g += sh(89, 'HAWAIIAN CONSONANTS')
    hcons = [
        ('h', '/h/', 'glottal fricative: hale (house), hou (new)'),
        ('k', '/k/', 'velar stop: kai (sea), k\u0101ne (man)'),
        ('l', '/l/', 'lateral: lani (sky/chief), luna (above)'),
        ('m', '/m/', 'bilabial nasal: mea (thing), moana (ocean)'),
        ('n', '/n/', 'alveolar nasal: nani (beauty), nui (big)'),
        ('p', '/p/', 'bilabial stop: p\u014c (night), pua (flower)'),
        ('w', '/v/ or /w/', 'varies by dialect: wai (water), wiki (fast)'),
        ('\u02bb', '/\u0294/', 'glottal stop \u2014 a full consonant letter: \u02bbaina (land), \u02bbohana (family)'),
    ]
    for i, (ch, ipa, ex) in enumerate(hcons):
        y = 99 + i * 10
        g += t(42, y, ch, 'middle', 'Ls')
        g += t(85, y, ipa, 'middle', 'Lx')
        g += t(290, y, ex, 'middle', 'Lx')
    g += hr(186)

    g += sh(194, 'HAWAIIAN VOWELS \u2014 5 SHORT + 5 LONG')
    hvowels = [
        ('a /a/', '\u0101 /a\u02d0/', 'low central: aloha, k\u0101ne'),
        ('e /\u025b/', '\u0113 /\u025b\u02d0/', 'mid front: hele (go), m\u0113a (person)'),
        ('i /i/', '\u012b /i\u02d0/', 'high front: kai (sea), \u012blio (dog)'),
        ('o /o/', '\u014d /o\u02d0/', 'mid back: one (sand), \u014cahu (Oahu)'),
        ('u /u/', '\u016b /u\u02d0/', 'high back: ukulele, \u016bniki (secret)'),
    ]
    for i, (sh_v, lng, ex) in enumerate(hvowels):
        y = 204 + i * 10
        g += t(90, y, sh_v, 'middle', 'Lx')
        g += t(220, y, lng, 'middle', 'Lx')
        g += t(370, y, ex, 'middle', 'Lx')
    g += hr(261)

    g += sh(269, 'HAWAIIAN DIPHTHONGS')
    g += t(240, 279, 'Hawaiian has 8 diphthongs (vowel pairs in one syllable): ai, ae, ao, au, ei, eu, oi, ou.', 'middle', 'Ls')
    g += t(240, 288, 'ao = /ao/ (cloud/light \u2014 also: daytime); au = /au/ (current/tide); aloha has a+l+o+h+a \u2014 5 syllables.', 'middle', 'Lx')

    g += sec_divider(298, 'SECONDARY \u2014 ENGLISH \u2014 PHONOLOGY')

    g += sh(324, 'ENGLISH PHONOLOGY \u2014 44 PHONEMES IN 26 LETTERS')
    g += t(240, 334, 'English has ~44 phonemes (varies by dialect) encoded in only 26 letters \u2014 a fundamental mismatch.', 'middle', 'Ls')
    g += t(240, 343, '20 vowel sounds in standard varieties (12 monophthongs, 8 diphthongs). Many homophones, few minimal pairs resolved by spelling.', 'middle', 'Lx')
    g += hr(351)

    g += sh(359, 'ENGLISH KEY VOWEL CONTRASTS')
    ev = [
        ('/i\u02d0/ vs /\u026a/', 'beat vs. bit \u2014 tense/lax distinction'),
        ('/u\u02d0/ vs /\u028a/', 'food vs. foot \u2014 tense/lax distinction'),
        ('/e\u026a/ vs /\u025b/', 'bait vs. bet \u2014 diphthong vs. monophthong'),
        ('/a\u026a/ vs /\u0251/', 'time vs. tom \u2014 diphthong vs. low back'),
        ('/\u0254\u026a/ vs /\u0254/', 'toy vs. thought \u2014 diphthong vs. long vowel'),
    ]
    for i, (ipa, ex) in enumerate(ev):
        y = 369 + i * 10
        g += t(120, y, ipa, 'middle', 'Lx')
        g += t(330, y, ex, 'middle', 'Lx')
    g += hr(426)

    g += sh(434, 'ENGLISH CONSONANTS \u2014 KEY FEATURES')
    g += t(240, 444, 'English /\u03b8 \u00f0/: dental fricatives \u201cthin/this\u201d \u2014 absent from most world languages and a common learning difficulty.', 'middle', 'Ls')
    g += t(240, 453, '/r/: English rhotic is not a trill \u2014 a retroflex approximant in American, a uvular in some British dialects.', 'middle', 'Lx')
    g += t(240, 462, 'Final consonant clusters: strengths /str\u025b\u014bk\u03b8s/ = 8-phoneme word with 3 final consonants.', 'middle', 'Lx')
    g += hr(470)

    g += sh(478, 'PHONOLOGICAL BRIDGE \u2014 MAXIMUM CONTRAST')
    g += t(240, 488, 'Hawaiian: 13 phonemes, open syllables (CV/V), phonemic vowel length, glottal stop as letter.', 'middle', 'Ls')
    g += t(240, 497, 'English: 44 phonemes, complex clusters (str-, -ngths), stress-timed, no phonemic length.', 'middle', 'Ls')
    g += t(240, 506, 'These two languages represent near-opposite ends of phonological complexity and syllable structure.', 'middle', 'Lx')

    g += footer('59', 'Hawaiian', 'English', 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 59C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_59c_alt():
    g = open_svg()
    g += t(240, 30, 'HAWAIIAN + ENGLISH \u2014 GRAMMAR \u00b7 VOCABULARY', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 59C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'HAWAIIAN GRAMMAR \u2014 VSO \u00b7 PARTICLES \u00b7 NO INFLECTION')
    g += t(240, 73, 'Hawaiian is Verb-Subject-Object (VSO). The verb comes first.', 'middle', 'Ls')
    g += t(240, 82, 'Ua hele au i ka hale. PAST go I DIR the house. \u201cI went to the house.\u201d', 'middle', 'Lx')
    g += t(240, 91, 'No inflection for person, number, tense \u2014 these are expressed by particles before or after the verb.', 'middle', 'Lx')
    g += hr(99)

    g += sh(107, 'HAWAIIAN TENSE/ASPECT PARTICLES')
    hpart = [
        ('ua', 'perfective (completed): ua hele (went / has gone)'),
        ('e\u2026ana', 'progressive (ongoing): e hele ana (going, is going)'),
        ('e', 'imperfective/command: e hele (go! / will go)'),
        ('ke\u2026nei', 'present progressive: ke hele nei (is going now)'),
        ('mai', 'negative command: mai hele (don\u2019t go)'),
        ('\u02bea\u02bbe', 'past: \u02bea\u02bbe hele (was going/used to go)'),
    ]
    for i, (p, gloss) in enumerate(hpart):
        y = 117 + i * 10
        g += t(70, y, p, 'middle', 'Ls')
        g += t(290, y, gloss, 'middle', 'Lx')
    g += hr(178)

    g += sh(186, 'HAWAIIAN \u2014 INCLUSIVE VS. EXCLUSIVE WE')
    g += t(240, 196, 'Hawaiian distinguishes k\u0101kou (we, including you) from m\u0101kou (we, excluding you).', 'middle', 'Ls')
    g += t(240, 205, 'Also: dual pronouns \u2014 l\u0101ua (they two), m\u0101ua (we two, excl.), k\u0101ua (we two, incl.).', 'middle', 'Lx')
    g += hr(213)

    g += sh(221, 'HAWAIIAN CORE VOCABULARY')
    hvocab = [
        ('wai', 'water'), ('ahi', 'fire'), ('\u02bbaina', 'land/earth'), ('kanaka', 'person'),
        ('mahina', 'moon'), ('ho\u02bbomana\u02bbo', 'remember'), ('w\u0101', 'time/future era'), ('ku\u02bbokoaloko', 'freedom'),
        ('pu\u02bbuwai', 'heart'), ('aloha', 'love/compassion'), ('honua', 'world/earth'), ('ola', 'life'),
    ]
    for i, (hw, en) in enumerate(hvocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 231 + row * 10
        g += t(x, y, hw, 'middle', 'Ls')
        g += t(x + 60, y, en, 'middle', 'Lx')

    g += sec_divider(276, 'SECONDARY \u2014 ENGLISH \u2014 GRAMMAR \u00b7 VOCABULARY')

    g += sh(302, 'ENGLISH GRAMMAR \u2014 SVO \u00b7 ANALYTIC \u00b7 NO GENDER')
    g += t(240, 312, 'English is SVO and highly analytic \u2014 minimal inflection, word order carries most grammatical meaning.', 'middle', 'Ls')
    g += t(240, 321, 'No grammatical gender for nouns (unlike most European languages). No case on nouns (only he/him, she/her).', 'middle', 'Lx')
    g += t(240, 330, 'Aspect: progressive (is going), perfect (has gone), perfect progressive (has been going) expressed with auxiliaries.', 'middle', 'Lx')
    g += hr(338)

    g += sh(346, 'ENGLISH VERB TENSE SYSTEM')
    etense = [
        ('Simple present', 'I go / she goes (3rd sg -s)'),
        ('Present progressive', 'I am going (be + -ing)'),
        ('Simple past', 'I went (irregular) / I walked (regular -ed)'),
        ('Past progressive', 'I was going'),
        ('Present perfect', 'I have gone (have + past participle)'),
        ('Future (modal)', 'I will go / I am going to go'),
    ]
    for i, (name, ex) in enumerate(etense):
        y = 356 + i * 10
        g += t(120, y, name, 'middle', 'Lx')
        g += t(330, y, ex, 'middle', 'Lx')
    g += hr(425)

    g += sh(433, 'ENGLISH CORE VOCABULARY')
    evocab = [
        ('water', 'water'), ('fire', 'fire'), ('earth', 'earth'), ('person', 'person'),
        ('moon', 'moon'), ('memory', 'memory'), ('future', 'future'), ('freedom', 'freedom'),
        ('heart', 'heart'), ('love', 'love'), ('world', 'world'), ('life', 'life'),
    ]
    for i, (en, _) in enumerate(evocab):
        col = i % 3; row = i // 3
        x = 60 + col * 130; y = 443 + row * 10
        g += t(x, y, en, 'middle', 'Ls')
    g += hr(480)

    g += sh(488, 'GRAMMAR BRIDGE \u2014 VSO MEETS SVO')
    g += t(240, 498, 'Hawaiian VSO: Ua \u02bbai au i ka \u02bbai (PAST eat I DIR the food) = I ate the food.', 'middle', 'Ls')
    g += t(240, 507, 'English SVO: I ate the food. Subject must come first. Both languages: no grammatical case on nouns.', 'middle', 'Ls')
    g += t(240, 516, 'Hawaiian: rich particle system. English: rich auxiliary system. Both are analytic in their own way.', 'middle', 'Lx')

    g += footer('59', 'Hawaiian', 'English', 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 59D ALT — TEXT ─────────────────────────────────────────────────────

def build_59d_alt():
    g = open_svg()
    g += t(240, 30, 'HAWAIIAN + ENGLISH \u2014 RUNNING TEXT \u00b7 PASSAGES', 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 59D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    g += sh(63, 'I. HAWAIIAN \u2014 \u02bbALEKOKI (NUUANU PALI LOOKOUT PASSAGE)')
    g += t(240, 73, 'I n\u0101 mea \u02bbino o ka \u02bb\u0101ina,', 'middle', 'L')
    g += t(240, 84, 'e ho\u02bbomana\u02bbo i n\u0101 kupuna.', 'middle', 'L')
    g += t(240, 95, 'In the evil-times of the land / remember the ancestors.', 'middle', 'Lx')
    g += t(240, 104, '"In difficult times for the land, remember the ancestors." (Hawaiian teaching, oral tradition)', 'middle', 'F')
    g += hr(112)

    g += sh(120, 'II. QUEEN LILI\u02bbUOKALANI \u2014 \u02bbALOHA \u02bbOE (1878 CE)')
    g += t(240, 130, '\u02bbAloha \u02bboe, \u02bbaloha \u02bboe,', 'middle', 'L')
    g += t(240, 141, 'E ke onaona noho i ka lipo,', 'middle', 'L')
    g += t(240, 152, 'Farewell to you farewell to you / The gentle breezes blowing to the deep.', 'middle', 'Lx')
    g += t(240, 161, '"Aloha \u02bbOe" \u2014 composed by Queen Lili\u02bbuokalani, last monarch of Hawaii\u02bbi (deposed 1893).', 'middle', 'F')
    g += hr(169)

    g += sh(177, 'III. HAWAIIAN BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 188, 'Ua hana \u02bbia k\u0113ia no \u02bboukou, me ka lokomaika\u02bbi,', 'middle', 'L')
    g += t(240, 200, 'e n\u0101 kanaka n\u0101na i ho\u02bbomana\u02bbo i n\u0101 w\u0101 e hiki mai ana.', 'middle', 'L')
    g += t(240, 212, 'PAST make PASS this for you   with the   generosity / by the people who  remembered the era coming.', 'middle', 'Lx')
    g += t(240, 221, '"This was made for you, generously, by people who remembered the time to come." (Hawaiian)', 'middle', 'F')
    g += hr(229)

    g += sh(237, 'HAWAIIAN NOTE \u2014 \u201cFUTURE\u201d AND \u201cREMEMBER\u201d')
    g += t(240, 247, 'N\u0101 w\u0101 e hiki mai ana = the times that are coming (no single word for \u201cfuture\u201d \u2014 a temporal phrase).', 'middle', 'Ls')
    g += t(240, 256, 'Ho\u02bbomana\u02bbo = to remember, to commemorate. Ho\u02bbo- = causative prefix + mana\u02bbo (thought/intention).', 'middle', 'Lx')
    g += t(240, 265, 'Lokomaika\u02bbi = generosity, kindness (loko = inside + maika\u02bbi = good). Free giving from the inside.', 'middle', 'Lx')

    g += sec_divider(275, 'SECONDARY \u2014 ENGLISH \u2014 RUNNING TEXT \u00b7 PASSAGES')

    g += sh(301, 'I. EMILY DICKINSON \u2014 ON MEMORY (c.1863 CE)')
    g += t(240, 311, 'The Brain \u2014 is wider than the Sky \u2014', 'middle', 'L')
    g += t(240, 322, 'For \u2014 put them side by side \u2014 / The one the other will contain.', 'middle', 'L')
    g += t(240, 333, '"The brain is wider than the sky." \u2014 Emily Dickinson. On the interior infinity of memory and imagination.', 'middle', 'F')
    g += hr(341)

    g += sh(349, 'II. ENGLISH PROVERB \u2014 ON TIME')
    g += t(240, 359, 'The present moment always will have been.', 'middle', 'L')
    g += t(240, 370, '"The present moment always will have been." \u2014 The permanence of past moments. Core Remember Forward concept.', 'middle', 'F')
    g += hr(378)

    g += sh(386, 'III. ENGLISH BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 397, 'This was made for you, freely,', 'middle', 'L')
    g += t(240, 409, 'by people who remembered forward.', 'middle', 'L')
    g += t(240, 421, '"This was made for you, freely, by people who remembered forward." (English \u2014 the project\u2019s own language)', 'middle', 'F')
    g += hr(429)

    g += sh(437, 'ENGLISH NOTE \u2014 \u201cFORWARD\u201d')
    g += t(240, 447, '\u201cRemember forward\u201d: an English oxymoron. You cannot remember what has not happened.', 'middle', 'Ls')
    g += t(240, 456, 'Yet: you can act now as if the future were already a past worth honoring. That is the project\u2019s name.', 'middle', 'Ls')
    g += t(240, 465, '\u201cFreely\u201d: from Old English freodom. Gift-giving without expectation of return. The grammar of generosity.', 'middle', 'Lx')
    g += hr(473)

    g += sh(481, 'LANGUAGE BRIDGE \u2014 AN OCEAN APART, FOREVER ENTANGLED')
    g += t(240, 491, 'Hawaiian: ~2000 native speakers (critically endangered, revitalizing). Polynesian origin, 1000+ years on islands.', 'middle', 'Ls')
    g += t(240, 500, 'English: ~380M native speakers. Global lingua franca. The language of the colonization that endangered Hawaiian.', 'middle', 'Ls')
    g += t(240, 509, 'Today English is also the medium through which Hawaiian revitalization reaches the world. Complicated neighbors.', 'middle', 'Lx')

    g += footer('59', 'Hawaiian', 'English', 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate59a_hawaiian_english_script_alt.svg':    build_59a_alt(),
        'plate59b_hawaiian_english_phonology_alt.svg': build_59b_alt(),
        'plate59c_hawaiian_english_grammar_alt.svg':   build_59c_alt(),
        'plate59d_hawaiian_english_text_alt.svg':      build_59d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
