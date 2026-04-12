# build_persian_kurdish_alt.py  — Series 23 ALT  (Persian/Farsi + Kurdish)
# Secondary language: Kurdish (~30M speakers, Kurdistan region of Turkey/Iraq/Iran/Syria)
# Geographic basis: standard 500mi radius from Tehran (35.7°N, 51.4°E)
# Iranian Kurdistan is within ~200mi of Tehran; Erbil (Iraqi Kurdistan) ~640km (~400mi)
# Both: Northwestern and Southwestern Iranian languages; same Indo-Iranian subfamily
# Persian has heavily influenced Kurdish vocabulary; both written in Arabic-based scripts
# Outputs: plate23a–23d_persian_kurdish_*_alt.svg

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

def t(x, y, text, anchor='middle', cls='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.5):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y, label, cls='H'):
    return t(240, y, label, 'middle', cls)

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

# ─────────────────────────────────────────────────────────────────────────────
def build_23a_alt():
    svg = open_svg()
    svg += t(240, 32, 'PERSIAN (\u0641\u0627\u0631\u0633\u06cc) / KURDISH (\u06a9\u0648\u0631\u062f\u06cc)', 'middle', 'T')
    svg += t(240, 44, 'IRANIAN BRANCH \u00b7 INDO-EUROPEAN \u00b7 SISTER LANGUAGES ACROSS ZAGROS', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 23A ALT \u00b7 SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PERSIAN: SCRIPT & WRITING \u2014')
    svg += t(240, 89, 'Script: Perso-Arabic (Nastaliq calligraphic style) \u00b7 right-to-left', 'middle', 'Ls')
    svg += t(240, 100, '32 letters: Arabic 28 + 4 Persian additions: \u067e (p) \u0686 (ch) \u0698 (zh) \u06af (g)', 'middle', 'Ls')
    svg += t(240, 111, 'Vowels: short vowels omitted in adult writing (inferred from context)', 'middle', 'Ls')
    svg += t(240, 122, 'Three short vowels (a e o) are diacritics; three long vowels (a: i: u:) are letters', 'middle', 'Ls')
    svg += hr(128, sw=0.3)
    svg += sh(138, 'PERSIAN PHONOLOGY')
    svg += t(240, 149, 'Consonants: /p b t d k g/ \u00b7 /f v s z \u0283 \u0292 x \u0263 h/ \u00b7 /m n/ \u00b7 /r l/ \u00b7 /j w/', 'middle', 'Ls')
    svg += t(240, 160, '6 vowels: /a \u0259 i e o u/ in Modern Persian (length distinction reduced)', 'middle', 'Ls')
    svg += t(240, 171, 'No tones \u00b7 no grammatical gender \u00b7 stress: final syllable in most words', 'middle', 'Ls')
    svg += hr(177, sw=0.3)
    svg += sh(187, 'PERSIAN EZAFE CONSTRUCTION (\u0627\u0636\u0627\u0641\u0647)')
    svg += t(240, 198, 'Ezafe: linking particle -e/-ye connects noun to modifier', 'middle', 'Ls')
    svg += t(240, 209, 'ketab-e man = book-EZAFE me = "my book" (possessor follows noun)', 'middle', 'Ls')
    svg += t(240, 220, 'ketab-e bozorg = book-EZAFE big = "big book" (adjective follows noun)', 'middle', 'Ls')
    svg += t(240, 231, 'Ezafe chains: khane-ye bozorg-e man = house-E big-E me = "my big house"', 'middle', 'Ls')
    svg += hr(237, sw=0.3)
    svg += sh(247, 'PERSIAN SAMPLE WORDS')
    svg += t(240, 258, '\u0633\u0644\u0627\u0645 (salam) = hello \u00b7 \u0645\u0645\u0646\u0648\u0646\u0645 (mamnunam) = thank you', 'middle', 'Ls')
    svg += t(240, 269, '\u0622\u0628 (ab) = water \u00b7 \u067e\u0627\u0631\u0633\u06cc (parsi/farsi) = Persian language', 'middle', 'Ls')
    svg += hr(275, sw=0.3)
    svg += sh(285, 'PERSIAN LOANWORDS IN WORLD LANGUAGES')
    svg += t(240, 296, 'English via French/Latin: azure (lazur) \u00b7 chess (shah) \u00b7 check (shah, same root)', 'middle', 'Ls')
    svg += t(240, 307, 'Also: paradise (pardis) \u00b7 bazaar (bazar) \u00b7 caravan (karvan) \u00b7 shawl (shal)', 'middle', 'Ls')
    svg += t(240, 318, 'Persian was the lingua franca of Islamic high culture: Mughal, Ottoman, Safavid courts', 'middle', 'Ls')
    svg += hr(324, sw=0.3)
    svg += sh(334, 'SAMPLE LITERARY PERSIAN')
    svg += t(240, 345, '\u0628\u0634\u0646\u0648 \u0627\u06cc\u0646 \u0646\u06cc \u0686\u0648\u0646 \u0634\u06a9\u0627\u06cc\u062a \u0645\u06cc\u200c\u06a9\u0646\u062f = "Listen to this reed, how it complains" (Rumi)', 'middle', 'Ls')

    svg += sec_divider(357, 'KURDISH (\u06a9\u0648\u0631\u062f\u06cc) \u2014 IRANIAN SISTER \u00b7 NORTHWESTERN BRANCH')

    svg += sh(382, '\u2014 KURDISH: TWO SCRIPTS, TWO MAJOR DIALECTS \u2014')
    svg += t(240, 393, 'Kurmanji (North Kurdish): ~15-20M speakers \u00b7 Turkey, Syria, diaspora', 'middle', 'Ls')
    svg += t(240, 404, 'Kurmanji script: LATIN alphabet (Turkey forced this in 1932; now a blessing)', 'middle', 'Ls')
    svg += t(240, 415, 'Sorani (Central Kurdish): ~6-7M speakers \u00b7 Iraqi Kurdistan, NW Iran', 'middle', 'Ls')
    svg += t(240, 426, 'Sorani script: Arabic-based (similar to Persian script) \u00b7 right-to-left', 'middle', 'Ls')
    svg += hr(432, sw=0.3)
    svg += sh(442, 'KURMANJI LATIN ORTHOGRAPHY')
    svg += t(240, 453, '31 letters + digraphs: ch, gh, kh, rr, sh, wh, xh \u00b7 special: \u00ea \u00ee \u00fb', 'middle', 'Ls')
    svg += t(240, 464, '\u00ea /e:/ \u00b7 \u00ee /i:/ \u00b7 \u00fb /u:/ \u2014 circumflex marks long vowels', 'middle', 'Ls')
    svg += hr(470, sw=0.3)
    svg += sh(480, 'KURDISH PHONOLOGY (KURMANJI)')
    svg += t(240, 491, 'Consonants: /p b t d k g q/ \u00b7 /f v s z \u0283 \u0292 x \u0281 h/ \u00b7 /m n/ \u00b7 /r \u0281/ \u00b7 /l/', 'middle', 'Ls')
    svg += t(240, 502, 'Uvular /q/ and /\u0281/ distinguish Kurdish from Persian', 'middle', 'Ls')
    svg += t(240, 513, '6 vowels: /a \u025b i o u \u0259/ \u2014 similar to Persian', 'middle', 'Ls')
    svg += hr(519, sw=0.3)
    svg += sh(529, 'SCRIPT COMPARISON')
    svg += t(100, 540, 'DIALECT', 'middle', 'Lx')
    svg += t(240, 540, 'SCRIPT', 'middle', 'Lx')
    svg += t(390, 540, 'DIRECTION', 'middle', 'Lx')
    svg += hr(544, sw=0.3)
    svg += t(100, 553, 'Kurmanji', 'middle', 'Ls')
    svg += t(240, 553, 'Latin (Hawar alphabet)', 'middle', 'Ls')
    svg += t(390, 553, 'Left-to-right', 'middle', 'Ls')
    svg += t(100, 563, 'Sorani', 'middle', 'Ls')
    svg += t(240, 563, 'Arabic/Persian-based', 'middle', 'Ls')
    svg += t(390, 563, 'Right-to-left', 'middle', 'Ls')
    svg += t(100, 573, 'Zazaki/Gorani', 'middle', 'Ls')
    svg += t(240, 573, 'Latin or Arabic', 'middle', 'Ls')
    svg += t(390, 573, 'Varies', 'middle', 'Ls')
    svg += hr(578, sw=0.3)
    svg += sh(588, 'KURDISH SAMPLE WORDS (KURMANJI)')
    svg += t(240, 599, 'Silav / Merheba = hello \u00b7 av = water \u00b7 spas = thank you', 'middle', 'Ls')
    svg += t(240, 610, 'kurd = Kurd/strong one \u00b7 Kurmanci = northern Kurdish language', 'middle', 'Ls')

    svg += footer(23, 'PERSIAN', 'KURDISH', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_23b_alt():
    svg = open_svg()
    svg += t(240, 32, 'PERSIAN (\u0641\u0627\u0631\u0633\u06cc) / KURDISH (\u06a9\u0648\u0631\u062f\u06cc)', 'middle', 'T')
    svg += t(240, 44, 'IRANIAN BRANCH \u00b7 PHONOLOGY & GRAMMAR COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 23B ALT \u00b7 PHONOLOGY & GRAMMAR')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PERSIAN GRAMMAR \u2014')
    svg += t(240, 88, 'SOV word order \u00b7 no case inflection \u00b7 no grammatical gender \u00b7 postpositions', 'middle', 'Ls')
    svg += t(240, 99, 'Verb conjugation: person + number + tense + mood encoded in suffix', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'PERSIAN VERB STRUCTURE')
    svg += t(100, 126, 'FORM', 'middle', 'Lx')
    svg += t(240, 126, 'PERSIAN', 'middle', 'Lx')
    svg += t(390, 126, 'GLOSS', 'middle', 'Lx')
    svg += hr(130, sw=0.3)
    svg += t(100, 139, 'Infinitive', 'middle', 'Ls')
    svg += t(240, 139, 'raftan (\u0631\u0641\u062a\u0646)', 'middle', 'Ls')
    svg += t(390, 139, 'to go', 'middle', 'Ls')
    svg += t(100, 149, '1sg pres.', 'middle', 'Ls')
    svg += t(240, 149, 'mi-ravam (\u0645\u06cc\u0631\u0648\u0645)', 'middle', 'Ls')
    svg += t(390, 149, 'I go (mi- = imperfective)', 'middle', 'Ls')
    svg += t(100, 159, '3sg pres.', 'middle', 'Ls')
    svg += t(240, 159, 'mi-ravad (\u0645\u06cc\u0631\u0648\u062f)', 'middle', 'Ls')
    svg += t(390, 159, 's/he goes', 'middle', 'Ls')
    svg += t(100, 169, '1sg past', 'middle', 'Ls')
    svg += t(240, 169, 'raftam (\u0631\u0641\u062a\u0645)', 'middle', 'Ls')
    svg += t(390, 169, 'I went', 'middle', 'Ls')
    svg += t(100, 179, 'Subjunctive', 'middle', 'Ls')
    svg += t(240, 179, 'be-ravam (\u0628\u0631\u0648\u0645)', 'middle', 'Ls')
    svg += t(390, 179, 'that I go', 'middle', 'Ls')
    svg += hr(184, sw=0.3)
    svg += sh(194, 'PERSIAN PLURAL MARKERS')
    svg += t(240, 205, '-ha (\u0647\u0627): general plural \u00b7 -an (\u0627\u0646): animate/classical plural', 'middle', 'Ls')
    svg += t(240, 216, 'ketab-ha (books) \u00b7 mard-an (men, classical) \u00b7 ketab-ha-ye bozorg (big books)', 'middle', 'Ls')
    svg += hr(222, sw=0.3)
    svg += sh(232, 'CORE VOCABULARY (PERSIAN)')
    svg += t(100, 243, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 243, 'PERSIAN', 'middle', 'Lx')
    svg += t(390, 243, 'ROMANIZATION', 'middle', 'Lx')
    svg += hr(247, sw=0.3)
    svg += t(100, 256, 'I', 'middle', 'Ls')
    svg += t(240, 256, '\u0645\u0646', 'middle', 'Ls')
    svg += t(390, 256, 'man', 'middle', 'Ls')
    svg += t(100, 266, 'you', 'middle', 'Ls')
    svg += t(240, 266, '\u062a\u0648', 'middle', 'Ls')
    svg += t(390, 266, 'to', 'middle', 'Ls')
    svg += t(100, 276, 'water', 'middle', 'Ls')
    svg += t(240, 276, '\u0622\u0628', 'middle', 'Ls')
    svg += t(390, 276, 'ab', 'middle', 'Ls')
    svg += t(100, 286, 'not', 'middle', 'Ls')
    svg += t(240, 286, '\u0646\u0647', 'middle', 'Ls')
    svg += t(390, 286, 'na/ne', 'middle', 'Ls')
    svg += t(100, 296, 'love', 'middle', 'Ls')
    svg += t(240, 296, '\u0639\u0634\u0642', 'middle', 'Ls')
    svg += t(390, 296, 'eshq', 'middle', 'Ls')
    svg += t(100, 306, 'heart', 'middle', 'Ls')
    svg += t(240, 306, '\u062f\u0644', 'middle', 'Ls')
    svg += t(390, 306, 'del', 'middle', 'Ls')

    svg += sec_divider(318, 'KURDISH \u2014 GRAMMAR & VOCABULARY')

    svg += sh(342, '\u2014 KURDISH GRAMMAR (KURMANJI) \u2014')
    svg += t(240, 353, 'SOV \u00b7 two grammatical genders (masc/fem) \u00b7 split ergativity in past tenses', 'middle', 'Ls')
    svg += t(240, 364, 'Case marking: nominative vs oblique (2 cases) \u2014 more than modern Persian', 'middle', 'Ls')
    svg += hr(370, sw=0.3)
    svg += sh(380, 'SPLIT ERGATIVITY IN KURDISH')
    svg += t(240, 391, 'Present: subject in nominative (like Persian)', 'middle', 'Ls')
    svg += t(240, 402, 'Past transitive: AGENT takes oblique case, verb agrees with PATIENT', 'middle', 'Ls')
    svg += t(240, 413, 'Min av xwar = I-OBL water ate: "I drank water" (min = oblique of ez)', 'middle', 'Ls')
    svg += t(240, 424, 'Ez av dixwim = I-NOM water drink: "I drink water" (ez = nominative)', 'middle', 'Ls')
    svg += hr(430, sw=0.3)
    svg += sh(440, 'KURDISH CORE VOCABULARY (KURMANJI)')
    svg += t(100, 451, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 451, 'KURMANJI', 'middle', 'Lx')
    svg += t(390, 451, 'PERSIAN COGNATE?', 'middle', 'Lx')
    svg += hr(455, sw=0.3)
    svg += t(100, 464, 'I', 'middle', 'Ls')
    svg += t(240, 464, 'ez', 'middle', 'Ls')
    svg += t(390, 464, 'cf. Persian man', 'middle', 'Ls')
    svg += t(100, 474, 'you', 'middle', 'Ls')
    svg += t(240, 474, 'tu', 'middle', 'Ls')
    svg += t(390, 474, 'YES \u2014 Persian to', 'middle', 'Ls')
    svg += t(100, 484, 'water', 'middle', 'Ls')
    svg += t(240, 484, 'av', 'middle', 'Ls')
    svg += t(390, 484, 'YES \u2014 Persian ab', 'middle', 'Ls')
    svg += t(100, 494, 'good', 'middle', 'Ls')
    svg += t(240, 494, 'baş / bas', 'middle', 'Ls')
    svg += t(390, 494, 'cf. Persian khub (differ)', 'middle', 'Ls')
    svg += t(100, 504, 'heart', 'middle', 'Ls')
    svg += t(240, 504, 'dil', 'middle', 'Ls')
    svg += t(390, 504, 'YES \u2014 Persian del', 'middle', 'Ls')
    svg += t(100, 514, 'mountain', 'middle', 'Ls')
    svg += t(240, 514, 'ç\u00eay / k\u00f4h', 'middle', 'Ls')
    svg += t(390, 514, 'koh \u2014 same root!', 'middle', 'Ls')
    svg += hr(519, sw=0.3)
    svg += sh(529, 'PERSIAN LOANWORDS IN KURDISH')
    svg += t(240, 540, '~40% of Sorani Kurdish vocabulary is Persian loanwords', 'middle', 'Ls')
    svg += t(240, 551, 'Core words (water, mountain, heart) often share Iranian roots', 'middle', 'Ls')
    svg += t(240, 562, 'Kurmanji has more distinct vocabulary; Sorani more Persian-influenced', 'middle', 'Ls')
    svg += hr(568, sw=0.3)
    svg += sh(578, 'NUMBERS COMPARISON')
    svg += t(100, 589, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 589, 'PERSIAN', 'middle', 'Lx')
    svg += t(390, 589, 'KURMANJI', 'middle', 'Lx')
    svg += hr(593, sw=0.3)
    svg += t(100, 602, '1 / 2 / 3', 'middle', 'Ls')
    svg += t(240, 602, 'yek / do / se', 'middle', 'Ls')
    svg += t(390, 602, 'yek / du / s\u00ea', 'middle', 'Ls')
    svg += t(100, 612, '4 / 5 / 6', 'middle', 'Ls')
    svg += t(240, 612, 'chahar / panj / shesh', 'middle', 'Ls')
    svg += t(390, 612, 'ch\u00ear / p\u00eanc / sh\u00ea', 'middle', 'Ls')

    svg += footer(23, 'PERSIAN', 'KURDISH', 'B', 'PHONOLOGY & GRAMMAR')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_23c_alt():
    svg = open_svg()
    svg += t(240, 32, 'PERSIAN (\u0641\u0627\u0631\u0633\u06cc) / KURDISH (\u06a9\u0648\u0631\u062f\u06cc)', 'middle', 'T')
    svg += t(240, 44, 'IRANIAN BRANCH \u00b7 CORE VOCABULARY & LITERATURE', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 23C ALT \u00b7 CORE VOCABULARY & LITERATURE')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PERSIAN: SURVIVAL PHRASES & LITERARY TRADITION \u2014')
    svg += sh(88, 'ESSENTIAL PERSIAN PHRASES')
    svg += t(240, 99, '\u0633\u0644\u0627\u0645 / Salam = Hello \u00b7 \u062e\u062f\u0627\u062d\u0627\u0641\u0638 / Khodahafez = Goodbye (God protect you)', 'middle', 'Ls')
    svg += t(240, 110, '\u0645\u0645\u0646\u0648\u0646\u0645 / Mamnunam = Thank you \u00b7 \u0628\u0628\u062e\u0634\u06cc\u062f / Bebakhshid = Excuse me/Sorry', 'middle', 'Ls')
    svg += t(240, 121, '\u0622\u0628 \u06a9\u062c\u0627\u0633\u062a / Ab kujast? = Where is water?', 'middle', 'Ls')
    svg += t(240, 132, '\u0646\u0645\u06cc\u200c\u0641\u0647\u0645\u0645 / Nemi-fahmanam = I don\'t understand', 'middle', 'Ls')
    svg += t(240, 143, '\u06a9\u0645\u06a9 \u06a9\u0646\u06cc\u062f / Komak konid! = Help! (plural/formal)', 'middle', 'Ls')
    svg += hr(149, sw=0.3)
    svg += sh(159, 'CORE VOCABULARY')
    svg += t(100, 170, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 170, 'PERSIAN', 'middle', 'Lx')
    svg += t(390, 170, 'ROMANIZATION', 'middle', 'Lx')
    svg += hr(174, sw=0.3)
    svg += t(100, 183, 'fire', 'middle', 'Ls')
    svg += t(240, 183, '\u0622\u062a\u0634 / \u0622\u062a\u0648\u0631', 'middle', 'Ls')
    svg += t(390, 183, 'atash / atur', 'middle', 'Ls')
    svg += t(100, 193, 'earth/land', 'middle', 'Ls')
    svg += t(240, 193, '\u0632\u0645\u06cc\u0646', 'middle', 'Ls')
    svg += t(390, 193, 'zamin', 'middle', 'Ls')
    svg += t(100, 203, 'sun', 'middle', 'Ls')
    svg += t(240, 203, '\u062e\u0648\u0631\u0634\u06cc\u062f', 'middle', 'Ls')
    svg += t(390, 203, 'khorshid', 'middle', 'Ls')
    svg += t(100, 213, 'night', 'middle', 'Ls')
    svg += t(240, 213, '\u0634\u0628', 'middle', 'Ls')
    svg += t(390, 213, 'shab', 'middle', 'Ls')
    svg += t(100, 223, 'day', 'middle', 'Ls')
    svg += t(240, 223, '\u0631\u0648\u0632', 'middle', 'Ls')
    svg += t(390, 223, 'ruz', 'middle', 'Ls')
    svg += t(100, 233, 'child', 'middle', 'Ls')
    svg += t(240, 233, '\u0628\u0686\u0647', 'middle', 'Ls')
    svg += t(390, 233, 'bache', 'middle', 'Ls')
    svg += hr(238, sw=0.3)
    svg += sh(248, 'PERSIAN LITERARY GIANTS')
    svg += t(240, 259, 'Ferdowsi (940\u20131020 CE): Shahnameh (Book of Kings) \u2014 60,000 couplets, Iranian epic', 'middle', 'Ls')
    svg += t(240, 270, 'Omar Khayyam (~1048\u20131131): Rubaiyat \u2014 quatrains on life, wine, transience', 'middle', 'Ls')
    svg += t(240, 281, 'Rumi (1207\u20131273): Masnavi \u2014 25,000 verses; most read poet in the US today', 'middle', 'Ls')
    svg += t(240, 292, 'Hafez (1315\u20131390): Divan \u2014 every Iranian home has a copy for divination', 'middle', 'Ls')

    svg += sec_divider(304, 'KURDISH \u2014 VOCABULARY & ORAL TRADITION')

    svg += sh(328, '\u2014 KURDISH: SURVIVAL PHRASES & ORAL HERITAGE \u2014')
    svg += sh(339, 'ESSENTIAL KURMANJI PHRASES')
    svg += t(240, 350, 'Silav / Merheba = Hello \u00b7 Spas = Thank you', 'middle', 'Ls')
    svg += t(240, 361, 'Xatir bimini / Bi xatir e = Goodbye \u00b7 Bibore = Sorry/Excuse me', 'middle', 'Ls')
    svg += t(240, 372, 'Av kuja ye? = Where is water? (av=water, kuja=where, ye=is)', 'middle', 'Ls')
    svg += t(240, 383, 'Ez nefam = I don\'t understand \u00b7 Bibe aliyar min! = Help me!', 'middle', 'Ls')
    svg += hr(389, sw=0.3)
    svg += sh(399, 'KURDISH CORE VOCABULARY')
    svg += t(100, 410, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 410, 'KURMANJI', 'middle', 'Lx')
    svg += t(390, 410, 'SORANI', 'middle', 'Lx')
    svg += hr(414, sw=0.3)
    svg += t(100, 423, 'fire', 'middle', 'Ls')
    svg += t(240, 423, 'agir', 'middle', 'Ls')
    svg += t(390, 423, 'agir', 'middle', 'Ls')
    svg += t(100, 433, 'earth', 'middle', 'Ls')
    svg += t(240, 433, 'erd / ax', 'middle', 'Ls')
    svg += t(390, 433, 'zewi', 'middle', 'Ls')
    svg += t(100, 443, 'sun', 'middle', 'Ls')
    svg += t(240, 443, 'ro / h\u00eav', 'middle', 'Ls')
    svg += t(390, 443, 'xor', 'middle', 'Ls')
    svg += t(100, 453, 'night', 'middle', 'Ls')
    svg += t(240, 453, 'shev', 'middle', 'Ls')
    svg += t(390, 453, 'shew', 'middle', 'Ls')
    svg += t(100, 463, 'day', 'middle', 'Ls')
    svg += t(240, 463, 'ro\u00e9 / r\u00f4', 'middle', 'Ls')
    svg += t(390, 463, 'ro\u00fbj', 'middle', 'Ls')
    svg += t(100, 473, 'child', 'middle', 'Ls')
    svg += t(240, 473, 'zarok / k\u00f4r', 'middle', 'Ls')
    svg += t(390, 473, 'zarok / kur', 'middle', 'Ls')
    svg += hr(478, sw=0.3)
    svg += sh(488, 'KURDISH ORAL TRADITION: DENGBEJ')
    svg += t(240, 499, 'Dengbej: traditional Kurdish bards who sing kilam (epic narratives)', 'middle', 'Ls')
    svg += t(240, 510, 'Dengbej tradition: oral history preserved over centuries despite suppression', 'middle', 'Ls')
    svg += t(240, 521, 'Ahmade Khani (1651\u20131707): Mem u Zin \u2014 Kurdish Romeo and Juliet epic poem', 'middle', 'Ls')
    svg += t(240, 532, 'Cigerxwin (1903\u20131984): modern Kurdish poet, wrote in exile', 'middle', 'Ls')
    svg += hr(538, sw=0.3)
    svg += sh(548, 'SURVIVAL PHRASE (PERSIAN)')
    svg += t(240, 559, 'In baraye shoma sakhteh shodeh ast, azaadaneh, az taraf kasani keh be pish negar budan.', 'middle', 'Lx')
    svg += t(240, 571, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 582, '(be pish negar = forward-looking; pish = forward/front)', 'middle', 'Ls')
    svg += hr(588, sw=0.3)
    svg += sh(598, 'SURVIVAL PHRASE (KURDISH / KURMANJI)')
    svg += t(240, 609, 'Ev ji bo te hatiye amade kirin, bi azadi, ji aliye kesane ku ber xwe digerin.', 'middle', 'Lx')
    svg += t(240, 621, '"This was made for you, freely, by people who were looking forward."', 'middle', 'Ls')

    svg += footer(23, 'PERSIAN', 'KURDISH', 'C', 'CORE VOCABULARY & LITERATURE')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_23d_alt():
    svg = open_svg()
    svg += t(240, 32, 'PERSIAN (\u0641\u0627\u0631\u0633\u06cc) / KURDISH (\u06a9\u0648\u0631\u062f\u06cc)', 'middle', 'T')
    svg += t(240, 44, 'IRANIAN BRANCH \u00b7 HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 23D ALT \u00b7 HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PERSIAN: HISTORY OF A WORLD LITERARY LANGUAGE \u2014')
    svg += sh(88, 'THREE EMPIRES, ONE LANGUAGE')
    svg += t(240, 99, 'Achaemenid Persian (550\u2013330 BCE): Old Persian inscriptions at Persepolis', 'middle', 'Ls')
    svg += t(240, 110, 'Sasanian Persian (224\u2013651 CE): Middle Persian / Pahlavi; Avestan sacred texts', 'middle', 'Ls')
    svg += t(240, 121, 'New Persian (900 CE\u2013present): Arabic script adopted; Samanid cultural renaissance', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'PERSIAN AS COURT LANGUAGE OF THE ISLAMIC WORLD')
    svg += t(240, 148, 'Persian became the prestige literary language of the Islamic world 900\u20131800 CE', 'middle', 'Ls')
    svg += t(240, 159, 'Mughal India: official court language was Persian, not Hindi or Urdu', 'middle', 'Ls')
    svg += t(240, 170, 'Ottoman court: poets wrote Persian \u00b7 Central Asia: Persian = high culture', 'middle', 'Ls')
    svg += t(240, 181, 'Persian was to the Islamic world what Latin was to medieval Europe', 'middle', 'Ls')
    svg += hr(187, sw=0.3)
    svg += sh(197, 'MODERN PERSIAN: THREE STANDARDS')
    svg += t(240, 208, 'Farsi: spoken in Iran \u00b7 Dari: spoken in Afghanistan \u00b7 Tajik: spoken in Tajikistan', 'middle', 'Ls')
    svg += t(240, 219, 'Same language, three names, three scripts (Arabic/Arabic/Cyrillic)', 'middle', 'Ls')
    svg += t(240, 230, '~80M native speakers; ~130M total including L2', 'middle', 'Ls')
    svg += hr(236, sw=0.3)
    svg += sh(246, 'SURVIVAL PHRASE (PERSIAN)')
    svg += t(240, 257, 'In baraye shoma, azadaneh, az taraf kasani ke be ayandeh negar budand, sakhteh shodeh.', 'middle', 'Lx')
    svg += t(240, 269, '"This was made for you, freely, by people who looked toward the future."', 'middle', 'Ls')
    svg += t(240, 280, '(ayandeh = future; negar = looking; sakhteh shodeh = was made)', 'middle', 'Ls')

    svg += sec_divider(292, 'KURDISH \u2014 HISTORY: THE NATION WITHOUT A STATE')

    svg += sh(317, '\u2014 KURDISH: HISTORY OF DISPERSAL & RESISTANCE \u2014')
    svg += sh(328, 'WHO ARE THE KURDS? THE LARGEST STATELESS NATION')
    svg += t(240, 339, '~30-40M Kurds: largest ethnic group in the world without a recognized state', 'middle', 'Ls')
    svg += t(240, 350, 'Distributed across: Turkey (~15M) \u00b7 Iran (~8M) \u00b7 Iraq (~6M) \u00b7 Syria (~3M) \u00b7 diaspora', 'middle', 'Ls')
    svg += t(240, 361, 'Kurdish homeland: the Zagros Mountains \u2014 same mountains where agriculture began', 'middle', 'Ls')
    svg += hr(367, sw=0.3)
    svg += sh(377, 'THE MEDES: FIRST KURDISH EMPIRE (~678\u2013550 BCE)')
    svg += t(240, 388, 'Median Empire: possibly the first Iranian-speaking state; capital at Ecbatana', 'middle', 'Ls')
    svg += t(240, 399, 'Medes conquered Assyria (612 BCE) with Babylonian allies', 'middle', 'Ls')
    svg += t(240, 410, 'Conquered by Cyrus the Great (~550 BCE) \u2014 absorbed into Achaemenid Persia', 'middle', 'Ls')
    svg += hr(416, sw=0.3)
    svg += sh(426, 'TREATY OF SEVRES (1920) & ITS BETRAYAL')
    svg += t(240, 437, '1920 Treaty of Sevres: promised an independent Kurdish state after WWI', 'middle', 'Ls')
    svg += t(240, 448, '1923 Treaty of Lausanne: replaced Sevres \u2014 Kurdish state removed from text', 'middle', 'Ls')
    svg += t(240, 459, 'Kurdish uprisings in Turkey 1925, 1930, 1937\u201338; all suppressed violently', 'middle', 'Ls')
    svg += t(240, 470, 'Kurdish language banned in Turkey 1924\u20131991 \u2014 could not legally teach or publish', 'middle', 'Ls')
    svg += hr(476, sw=0.3)
    svg += sh(486, 'IRAQI KURDISTAN: THE CLOSEST THING TO A KURDISH STATE')
    svg += t(240, 497, 'Kurdistan Regional Government (KRG) since 1992: autonomous in northern Iraq', 'middle', 'Ls')
    svg += t(240, 508, 'Erbil (Hawler): capital; ~1M people; Kurdish-majority, internationally recognized', 'middle', 'Ls')
    svg += t(240, 519, 'Peshmerga: Kurdish militia fought ISIS 2014\u201317; key US ally', 'middle', 'Ls')
    svg += hr(525, sw=0.3)
    svg += sh(535, 'KURDISH LANGUAGE TODAY')
    svg += t(240, 546, 'Kurmanji: Turkish Kurdistan + northern Syria \u2014 written in Latin since 1932', 'middle', 'Ls')
    svg += t(240, 557, 'Sorani: Iraqi Kurdistan + Iranian Kurdistan \u2014 written in Arabic-based script', 'middle', 'Ls')
    svg += t(240, 568, 'Kurdish-language media: Rudaw TV, Kurdistan24 \u2014 broadcasting in Sorani and Kurmanji', 'middle', 'Ls')
    svg += hr(574, sw=0.3)
    svg += sh(584, 'SURVIVAL PHRASE (KURDISH / KURMANJI)')
    svg += t(240, 595, 'Ev ji bo te hatiye amade kirin, belaş, ji aliye kesane ku li ber xwe dinerin.', 'middle', 'Lx')
    svg += t(240, 607, '"This was made for you, freely, by people who look forward."', 'middle', 'Ls')
    svg += t(240, 618, '(belaş = free/gratis; li ber xwe dinerin = looking forward)', 'middle', 'Ls')

    svg += footer(23, 'PERSIAN', 'KURDISH', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate23a_persian_kurdish_script_alt.svg',    build_23a_alt),
        ('plate23b_persian_kurdish_phonology_alt.svg',  build_23b_alt),
        ('plate23c_persian_kurdish_vocabulary_alt.svg', build_23c_alt),
        ('plate23d_persian_kurdish_history_alt.svg',    build_23d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
