# build_mongolian_kazakh_alt.py  — Series 57 ALT  (Mongolian + Kazakh)
# Secondary language: Kazakh (~13M speakers, Kazakhstan & western China)
# Geographic basis: Kazakhstan borders Mongolia directly (Bayan-Olgii province has
# ethnic Kazakh communities). ~700mi from Ulaanbaatar to Almaty (~500mi expanded).
# Both: SOV · agglutinative · vowel harmony · Cyrillic scripts · steppe civilizations
# Outputs: plate57a–57d_mongolian_kazakh_*_alt.svg

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
def build_57a_alt():
    svg = open_svg()
    svg += t(240, 32, 'MONGOLIAN (\u043c\u043e\u043d\u0433\u043e\u043b \u0445\u044d\u043b) / KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456)', 'middle', 'T')
    svg += t(240, 44, 'MONGOLIC / TURKIC \u00b7 EURASIAN STEPPE \u00b7 BORDERING PEOPLES', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 57A ALT \u00b7 SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MONGOLIAN: TWO SCRIPTS IN PARALLEL \u2014')
    svg += t(240, 89, 'Traditional Mongolian Script (\u1824\u1820\u1828\u182d\u1820\u182f \u182a\u1822\u1834\u1822\u182d): vertical, read top-to-bottom, left-to-right', 'middle', 'Ls')
    svg += t(240, 100, 'Derived from Old Uyghur script (which came from Sogdian, which came from Aramaic)', 'middle', 'Ls')
    svg += t(240, 111, 'Letters change form depending on position (initial/medial/final) in a word', 'middle', 'Ls')
    svg += t(240, 122, 'Inner Mongolia (China): traditional script officially in use alongside Chinese', 'middle', 'Ls')
    svg += hr(128, sw=0.3)
    svg += sh(138, 'MONGOLIAN CYRILLIC (SINCE 1941)')
    svg += t(240, 149, '35 letters: 33 Russian Cyrillic + 2 added (\u04e8 /\u00f8/ and \u04ae /y/) for Mongolian sounds', 'middle', 'Ls')
    svg += t(240, 160, 'Mongolia (nation): Cyrillic standard since 1941 under Soviet influence', 'middle', 'Ls')
    svg += t(240, 171, '2020: Mongolia announced revival of traditional script alongside Cyrillic', 'middle', 'Ls')
    svg += hr(177, sw=0.3)
    svg += sh(187, 'MONGOLIAN CONSONANTS & VOWELS')
    svg += t(240, 198, 'Consonants: /p b t d ts dz k g/ \u00b7 /m n \u014b/ \u00b7 /f s \u0283 x h/ \u00b7 /r l j w/', 'middle', 'Ls')
    svg += t(240, 209, '7 vowels: /a e i o u \u00f8 y/ \u2014 with Cyrillic: a \u044d \u0438 o \u0443 \u04e9 \u04af', 'middle', 'Ls')
    svg += t(240, 220, 'VOWEL HARMONY: back vowels (a o u) vs front vowels (\u044d \u04e9 \u04af) in each word', 'middle', 'Ls')
    svg += hr(226, sw=0.3)
    svg += sh(236, 'VOWEL HARMONY IN MONGOLIAN')
    svg += t(240, 247, 'Back-vowel word: \u0433\u0430\u0437\u0430\u0440 /\u0261a.z\u0259r/ (gazar) = land/place', 'middle', 'Ls')
    svg += t(240, 258, 'Front-vowel word: \u0442\u04af\u043c\u044d\u043d /t\u00f8.m\u0259n/ (tumen) = 10,000 / abyss', 'middle', 'Ls')
    svg += t(240, 269, 'Suffixes harmonize: -t (+back) vs -\u044d\u0434 (+front) = same grammatical function', 'middle', 'Ls')
    svg += hr(275, sw=0.3)
    svg += sh(285, 'MONGOLIAN TRADITIONAL SCRIPT SAMPLE')
    svg += t(240, 296, '\u1824\u1820\u1828\u182d\u1820\u182f \u182a\u1822\u1834\u1822\u182d = "Mongolian language" (traditional script, read vertically)', 'middle', 'Ls')
    svg += t(240, 307, '\u043c\u043e\u043d\u0433\u043e\u043b \u0445\u044d\u043b = mongol khel (Cyrillic) = Mongolian language', 'middle', 'Ls')
    svg += hr(313, sw=0.3)
    svg += sh(323, 'SAMPLE WORDS (CYRILLIC)')
    svg += t(240, 334, '\u0441\u0430\u0439\u043d \u0431\u0430\u0439\u043d\u0430 (sain baina uu?) = hello (lit. "are you well?")', 'middle', 'Ls')
    svg += t(240, 345, '\u0431\u0430\u044f\u0440\u043b\u0430 (bayarlaa) = thank you \u00b7 \u0443\u0441 (us) = water', 'middle', 'Ls')

    svg += sec_divider(357, 'KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456) \u2014 TURKIC \u00b7 STEPPE NEIGHBOR')

    svg += sh(382, '\u2014 KAZAKH: THREE SCRIPTS, ONE LANGUAGE \u2014')
    svg += t(240, 393, 'Kazakh has been written in THREE different scripts in the modern era:', 'middle', 'Ls')
    svg += t(240, 404, '1. Arabic script (traditional; still used by Kazakhs in China/Xinjiang)', 'middle', 'Ls')
    svg += t(240, 415, '2. Cyrillic (Soviet period, 1940\u2013present; still primary in Kazakhstan)', 'middle', 'Ls')
    svg += t(240, 426, '3. Latin (announced 2017; transition ongoing; target: all by 2031)', 'middle', 'Ls')
    svg += hr(432, sw=0.3)
    svg += sh(442, 'KAZAKH CYRILLIC: 42 LETTERS')
    svg += t(240, 453, '33 Russian Cyrillic + 9 added: \u04d9 \u0493 \u049b \u04a3 \u04e9 \u04af \u04b1 \u0456 \u04bb', 'middle', 'Ls')
    svg += t(240, 464, 'Extra letters mark sounds not in Russian: /q/ /\u0493/ /\u014b/ /\u0262/ /\u0263/ /\u0127/ etc.', 'middle', 'Ls')
    svg += hr(470, sw=0.3)
    svg += sh(480, 'KAZAKH LATIN (CURRENT TRANSITION VERSION)')
    svg += t(240, 491, 'Uses apostrophe-based notation: A\u02bc, O\u02bc, U\u02bc, Y\u02bc, G\u02bc, N\u02bc for special sounds', 'middle', 'Ls')
    svg += t(240, 502, 'Controversial: apostrophes in every other word impede readability', 'middle', 'Ls')
    svg += t(240, 513, 'Revised versions proposed; final form not yet settled (as of 2026)', 'middle', 'Ls')
    svg += hr(519, sw=0.3)
    svg += sh(529, 'KAZAKH VOWEL HARMONY (9 VOWELS)')
    svg += t(240, 540, 'Back: a o u \u044b \u04d9 (\u04d9 = schwa) \u00b7 Front: \u0435 \u04e9 \u04af \u0456', 'middle', 'Ls')
    svg += t(240, 551, 'Suffixes harmonize: -lar (back) vs -ler (front) for plural', 'middle', 'Ls')
    svg += t(240, 562, '\u0430\u0442 /at/ (horse) \u2192 \u0430\u0442-\u0442\u0430\u0440 (horses) \u00b7 \u04af\u0439 /\u00f8j/ (house) \u2192 \u04af\u0439-\u043b\u0435\u0440 (houses)', 'middle', 'Ls')
    svg += hr(568, sw=0.3)
    svg += sh(578, 'SAMPLE WORDS (KAZAKH CYRILLIC)')
    svg += t(240, 589, '\u0421\u04d9\u043b\u0435\u043c\u0435\u0442\u0441\u0456\u0437 \u0431\u0435? (\u0441\u0430\u043b\u0435\u043c\u0435\u0442\u0441\u0456\u0437 \u0431\u0435?) = hello (are you well?)', 'middle', 'Ls')
    svg += t(240, 600, '\u0440\u0430\u0445\u043c\u0435\u0442 (rakhmet) = thank you \u00b7 \u0441\u0443 (su) = water', 'middle', 'Ls')
    svg += t(240, 611, 'Both languages greet with "are you well?" \u2014 steppe hospitality encoded in grammar', 'middle', 'Ls')

    svg += footer(57, 'MONGOLIAN', 'KAZAKH', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_57b_alt():
    svg = open_svg()
    svg += t(240, 32, 'MONGOLIAN (\u043c\u043e\u043d\u0433\u043e\u043b \u0445\u044d\u043b) / KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456)', 'middle', 'T')
    svg += t(240, 44, 'MONGOLIC / TURKIC \u00b7 EURASIAN STEPPE \u00b7 PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 57B ALT \u00b7 PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MONGOLIAN PHONOLOGY \u2014')
    svg += sh(88, 'VOWEL HARMONY IN DETAIL')
    svg += t(240, 99, 'Mongolian has 2 vowel sets. Every word belongs to one set; all suffixes follow:', 'middle', 'Ls')
    svg += t(100, 110, 'BACK VOWELS', 'middle', 'Lx')
    svg += t(300, 110, 'FRONT VOWELS', 'middle', 'Lx')
    svg += hr(114, sw=0.3)
    svg += t(100, 123, 'a /a/ \u2192 \u0430', 'middle', 'Ls')
    svg += t(300, 123, '\u044d /\u025b/ (open-mid front)', 'middle', 'Ls')
    svg += t(100, 133, 'o /o/ \u2192 \u043e', 'middle', 'Ls')
    svg += t(300, 133, '\u04e9 /\u00f8/ (front rounded)', 'middle', 'Ls')
    svg += t(100, 143, 'u /u/ \u2192 \u0443', 'middle', 'Ls')
    svg += t(300, 143, '\u04af /y/ (front rounded)', 'middle', 'Ls')
    svg += t(100, 153, 'i /\u026a/ neutral', 'middle', 'Ls')
    svg += t(300, 153, 'i /i/ (can be in either)', 'middle', 'Ls')
    svg += hr(158, sw=0.3)
    svg += sh(168, 'CONSONANTS: NOTABLE FEATURES')
    svg += t(240, 179, 'No phoneme /p/ in native Mongolian words (only in loanwords)', 'middle', 'Ls')
    svg += t(240, 190, 'Pharyngeal/uvular consonants: /\u0281/ (written r/R) and /\u0262/ (written G)', 'middle', 'Ls')
    svg += t(240, 201, 'Word-initial consonants are strong; word-final consonants weaken', 'middle', 'Ls')
    svg += hr(207, sw=0.3)
    svg += sh(217, 'LONG VOWELS: PHONEMICALLY DISTINCT')
    svg += t(240, 228, '\u0443\u0443\u0440 /u:r/ (ur, door) vs \u0443\u0440 /ur/ (ur, place name) \u2014 length changes meaning', 'middle', 'Ls')
    svg += t(240, 239, '\u0445\u04af\u04af (khuu) = son vs \u0445\u04af (khu) = man/human \u2014 length distinction', 'middle', 'Ls')
    svg += hr(245, sw=0.3)
    svg += sh(255, 'MONGOLIAN CASE ENDINGS (7 CASES)')
    svg += t(100, 266, 'CASE', 'middle', 'Lx')
    svg += t(240, 266, 'SUFFIX (BACK)', 'middle', 'Lx')
    svg += t(390, 266, 'MEANING', 'middle', 'Lx')
    svg += hr(270, sw=0.3)
    svg += t(100, 279, 'Nominative', 'middle', 'Ls')
    svg += t(240, 279, '(zero suffix)', 'middle', 'Ls')
    svg += t(390, 279, 'Subject', 'middle', 'Ls')
    svg += t(100, 289, 'Genitive', 'middle', 'Ls')
    svg += t(240, 289, '-\u044b\u043d / -\u0438\u0439\u043d', 'middle', 'Ls')
    svg += t(390, 289, 'Possession', 'middle', 'Ls')
    svg += t(100, 299, 'Dative', 'middle', 'Ls')
    svg += t(240, 299, '-\u0434', 'middle', 'Ls')
    svg += t(390, 299, 'To/at', 'middle', 'Ls')
    svg += t(100, 309, 'Accusative', 'middle', 'Ls')
    svg += t(240, 309, '-\u0438\u0439\u0433 / -\u0433', 'middle', 'Ls')
    svg += t(390, 309, 'Direct object', 'middle', 'Ls')
    svg += t(100, 319, 'Ablative', 'middle', 'Ls')
    svg += t(240, 319, '-\u0430\u0430\u0441 / -\u044d\u044d\u0441', 'middle', 'Ls')
    svg += t(390, 319, 'From', 'middle', 'Ls')
    svg += t(100, 329, 'Instrumental', 'middle', 'Ls')
    svg += t(240, 329, '-\u0430\u0430\u0440 / -\u044d\u044d\u0440', 'middle', 'Ls')
    svg += t(390, 329, 'With/by means of', 'middle', 'Ls')
    svg += t(100, 339, 'Comitative', 'middle', 'Ls')
    svg += t(240, 339, '-\u0442\u0430\u0439 / -\u0442\u044d\u0439', 'middle', 'Ls')
    svg += t(390, 339, 'Together with', 'middle', 'Ls')

    svg += sec_divider(351, 'KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456) \u2014 PHONOLOGY')

    svg += sh(376, '\u2014 KAZAKH PHONOLOGY \u2014')
    svg += sh(387, 'VOWEL HARMONY: FRONT/BACK + ROUNDING')
    svg += t(240, 398, 'Kazakh has 9 vowels: 4 back (a o u \u044b) + 4 front (\u04d9 \u04e9 \u04af \u0456) + 1 neutral (i)', 'middle', 'Ls')
    svg += t(240, 409, 'Rounding harmony: in some dialects, rounded back \u2192 rounded in suffixes', 'middle', 'Ls')
    svg += t(240, 420, 'Plural: -lar/-ler/-dar/-der/-tar/-ter (8 forms!) determined by harmony + voicing', 'middle', 'Ls')
    svg += hr(426, sw=0.3)
    svg += sh(436, 'DISTINCTIVE KAZAKH CONSONANTS')
    svg += t(240, 447, '/q/ (uvular stop) \u00b7 /\u0281/ (uvular fricative) \u00b7 /\u014b/ (velar nasal) \u00b7 /\u0127/ (pharyngeal)', 'middle', 'Ls')
    svg += t(240, 458, 'These uvular/pharyngeal consonants mark Turkic vs Mongolic distinction', 'middle', 'Ls')
    svg += t(240, 469, 'Kazakh lacks /p/ in native words (like Mongolian!) \u2014 parallel restriction', 'middle', 'Ls')
    svg += hr(475, sw=0.3)
    svg += sh(485, 'KAZAKH CASE SYSTEM (7 CASES)')
    svg += t(100, 496, 'CASE', 'middle', 'Lx')
    svg += t(240, 496, 'SUFFIX', 'middle', 'Lx')
    svg += t(390, 496, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(500, sw=0.3)
    svg += t(100, 509, 'Nominative', 'middle', 'Ls')
    svg += t(240, 509, '(zero)', 'middle', 'Ls')
    svg += t(390, 509, '\u0430\u0442 (horse)', 'middle', 'Ls')
    svg += t(100, 519, 'Genitive', 'middle', 'Ls')
    svg += t(240, 519, '-\u043d\u044b\u04a3/-\u043d\u0456\u04a3', 'middle', 'Ls')
    svg += t(390, 519, '\u0430\u0442-\u0442\u044b\u04a3 (of the horse)', 'middle', 'Ls')
    svg += t(100, 529, 'Dative', 'middle', 'Ls')
    svg += t(240, 529, '-\u0493\u0430/-\u0433\u0435', 'middle', 'Ls')
    svg += t(390, 529, '\u0430\u0442-\u049b\u0430 (to the horse)', 'middle', 'Ls')
    svg += t(100, 539, 'Accusative', 'middle', 'Ls')
    svg += t(240, 539, '-\u043d\u044b/-\u043d\u0456', 'middle', 'Ls')
    svg += t(390, 539, '\u0430\u0442-\u0442\u044b (the horse, obj)', 'middle', 'Ls')
    svg += t(100, 549, 'Locative', 'middle', 'Ls')
    svg += t(240, 549, '-\u0434\u0430/-\u0434\u0435', 'middle', 'Ls')
    svg += t(390, 549, '\u04af\u0439-\u0434\u0435 (in the house)', 'middle', 'Ls')
    svg += hr(554, sw=0.3)
    svg += sh(564, 'STEPPE PHONOLOGICAL PARALLEL')
    svg += t(240, 575, 'Both Mongolian and Kazakh: no /p/ in native words, vowel harmony, SOV', 'middle', 'Ls')
    svg += t(240, 586, 'Different families (Mongolic vs Turkic) — parallel features from parallel ecology', 'middle', 'Ls')
    svg += t(240, 597, 'Steppe languages converge: long contact, trade, intermarriage over centuries', 'middle', 'Ls')

    svg += footer(57, 'MONGOLIAN', 'KAZAKH', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_57c_alt():
    svg = open_svg()
    svg += t(240, 32, 'MONGOLIAN (\u043c\u043e\u043d\u0433\u043e\u043b \u0445\u044d\u043b) / KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456)', 'middle', 'T')
    svg += t(240, 44, 'MONGOLIC / TURKIC \u00b7 EURASIAN STEPPE \u00b7 GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 57C ALT \u00b7 GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MONGOLIAN GRAMMAR \u2014')
    svg += t(240, 88, 'SOV word order \u00b7 postpositions (not prepositions) \u00b7 verb always at end', 'middle', 'Ls')
    svg += t(240, 99, 'Agglutinative: suffixes stack for case, number, tense, person, aspect, mood', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'MONGOLIAN VERB STRUCTURE')
    svg += t(240, 126, '\u0431\u0438\u0447-\u0438\u0439\u0433 \u0445\u0430\u0439\u0440-\u0442 = letter-ACC love-PRES: "I love the letter"', 'middle', 'Ls')
    svg += t(240, 137, 'Verb endings encode: tense + aspect + person + number + mood', 'middle', 'Ls')
    svg += t(100, 148, 'ENDING', 'middle', 'Lx')
    svg += t(240, 148, 'MEANING', 'middle', 'Lx')
    svg += t(390, 148, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(152, sw=0.3)
    svg += t(100, 161, '-\u043d\u0430', 'middle', 'Ls')
    svg += t(240, 161, 'Present/future', 'middle', 'Ls')
    svg += t(390, 161, '\u0438\u0440-\u043d\u0430 (come)', 'middle', 'Ls')
    svg += t(100, 171, '-\u0441\u0430\u043d', 'middle', 'Ls')
    svg += t(240, 171, 'Past (completed)', 'middle', 'Ls')
    svg += t(390, 171, '\u0438\u0440-\u0441\u044d\u043d (came)', 'middle', 'Ls')
    svg += t(100, 181, '-\u0434\u0430\u0433', 'middle', 'Ls')
    svg += t(240, 181, 'Participle/past', 'middle', 'Ls')
    svg += t(390, 181, '\u0438\u0440-\u0441\u044d\u043d \u0445\u04af\u043d (a man who came)', 'middle', 'Ls')
    svg += hr(186, sw=0.3)
    svg += sh(196, 'CORE VOCABULARY (MONGOLIAN CYRILLIC)')
    svg += t(100, 207, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 207, 'MONGOLIAN', 'middle', 'Lx')
    svg += t(390, 207, 'ROMANIZATION', 'middle', 'Lx')
    svg += hr(211, sw=0.3)
    svg += t(100, 220, 'I / me', 'middle', 'Ls')
    svg += t(240, 220, '\u0431\u0438', 'middle', 'Ls')
    svg += t(390, 220, 'bi', 'middle', 'Ls')
    svg += t(100, 230, 'you', 'middle', 'Ls')
    svg += t(240, 230, '\u0447\u0438', 'middle', 'Ls')
    svg += t(390, 230, 'chi', 'middle', 'Ls')
    svg += t(100, 240, 'water', 'middle', 'Ls')
    svg += t(240, 240, '\u0443\u0441', 'middle', 'Ls')
    svg += t(390, 240, 'us', 'middle', 'Ls')
    svg += t(100, 250, 'eat', 'middle', 'Ls')
    svg += t(240, 250, '\u0438\u0434\u044d\u0445', 'middle', 'Ls')
    svg += t(390, 250, 'idekh', 'middle', 'Ls')
    svg += t(100, 260, 'not', 'middle', 'Ls')
    svg += t(240, 260, '\u0431\u0438\u0448', 'middle', 'Ls')
    svg += t(390, 260, 'bish', 'middle', 'Ls')
    svg += t(100, 270, 'horse', 'middle', 'Ls')
    svg += t(240, 270, '\u043c\u043e\u0440\u044c', 'middle', 'Ls')
    svg += t(390, 270, 'mor\u02b9', 'middle', 'Ls')
    svg += t(100, 280, 'good', 'middle', 'Ls')
    svg += t(240, 280, '\u0441\u0430\u0439\u043d', 'middle', 'Ls')
    svg += t(390, 280, 'sain', 'middle', 'Ls')
    svg += t(100, 290, 'thank you', 'middle', 'Ls')
    svg += t(240, 290, '\u0431\u0430\u044f\u0440\u043b\u0430\u043b\u0430\u0430', 'middle', 'Ls')
    svg += t(390, 290, 'bayarlalaa', 'middle', 'Ls')
    svg += hr(295, sw=0.3)
    svg += sh(305, 'NUMBERS 1\u201310')
    svg += t(240, 316, '\u043d\u044d\u0433 \u0445\u043e\u0451\u0440 \u0433\u0443\u0440\u0430\u0432 \u0434\u04e9\u0440\u04e9\u0432 \u0442\u0430\u0432 \u0437\u0443\u0440\u0433\u0430\u0430\u043d \u0434\u043e\u043b\u043e\u043e\u043d \u043d\u0430\u0439\u043c \u044e\u0441 \u0430\u0440\u0430\u0432', 'middle', 'Ls')

    svg += sec_divider(328, 'KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456) \u2014 GRAMMAR & VOCABULARY')

    svg += sh(352, '\u2014 KAZAKH GRAMMAR \u2014')
    svg += t(240, 363, 'SOV word order (same as Mongolian) \u00b7 postpositions \u00b7 verb final', 'middle', 'Ls')
    svg += t(240, 374, 'Agglutinative: suffixes for case, number, tense, voice, mood, person', 'middle', 'Ls')
    svg += t(240, 385, 'No grammatical gender \u00b7 no articles (like Mongolian)', 'middle', 'Ls')
    svg += hr(391, sw=0.3)
    svg += sh(401, 'KAZAKH VERB STRUCTURE')
    svg += t(240, 412, 'Root + voice + tense/mood + person agreement', 'middle', 'Ls')
    svg += t(240, 423, 'bar-a-myn = go-PRES-1SG = "I am going"', 'middle', 'Ls')
    svg += t(240, 434, 'bar-d\u044b = go-PAST = "went" (no person marking in past simple)', 'middle', 'Ls')
    svg += hr(440, sw=0.3)
    svg += sh(450, 'CORE VOCABULARY (KAZAKH CYRILLIC)')
    svg += t(100, 461, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 461, 'KAZAKH', 'middle', 'Lx')
    svg += t(390, 461, 'MONGOLIAN LINK?', 'middle', 'Lx')
    svg += hr(465, sw=0.3)
    svg += t(100, 474, 'I / me', 'middle', 'Ls')
    svg += t(240, 474, '\u043c\u0435\u043d', 'middle', 'Ls')
    svg += t(390, 474, 'Turkic root', 'middle', 'Ls')
    svg += t(100, 484, 'you', 'middle', 'Ls')
    svg += t(240, 484, '\u0441\u0435\u043d', 'middle', 'Ls')
    svg += t(390, 484, 'Turkic root', 'middle', 'Ls')
    svg += t(100, 494, 'water', 'middle', 'Ls')
    svg += t(240, 494, '\u0441\u0443', 'middle', 'Ls')
    svg += t(390, 494, 'cf. Mongol \u0443\u0441', 'middle', 'Ls')
    svg += t(100, 504, 'eat', 'middle', 'Ls')
    svg += t(240, 504, '\u0436\u0435\u0443', 'middle', 'Ls')
    svg += t(390, 504, 'Turkic root', 'middle', 'Ls')
    svg += t(100, 514, 'horse', 'middle', 'Ls')
    svg += t(240, 514, '\u0436\u044b\u043b\u049b\u044b', 'middle', 'Ls')
    svg += t(390, 514, 'cf. Mongol \u043c\u043e\u0440\u044c (differ)', 'middle', 'Ls')
    svg += t(100, 524, 'good', 'middle', 'Ls')
    svg += t(240, 524, '\u0436\u0430\u049b\u0441\u044b', 'middle', 'Ls')
    svg += t(390, 524, 'cf. Mongol \u0441\u0430\u0439\u043d (differ)', 'middle', 'Ls')
    svg += t(100, 534, 'thank you', 'middle', 'Ls')
    svg += t(240, 534, '\u0440\u0430\u0445\u043c\u0435\u0442', 'middle', 'Ls')
    svg += t(390, 534, 'From Arabic rahmat', 'middle', 'Ls')
    svg += hr(539, sw=0.3)
    svg += sh(549, 'NUMBERS 1\u201310 (KAZAKH)')
    svg += t(240, 560, '\u0431\u0456\u0440 \u0435\u043a\u0456 \u04af\u0448 \u0442\u04e9\u0440\u0442 \u0431\u0435\u0441 \u0430\u043b\u0442\u044b \u0436\u0435\u0442\u0456 \u0441\u0435\u0433\u0456\u0437 \u0442\u043e\u0493\u044b\u0437 \u043e\u043d', 'middle', 'Ls')
    svg += hr(566, sw=0.3)
    svg += sh(576, 'GRAMMATICAL PARALLEL: SOV AGGLUTINATION')
    svg += t(240, 587, 'Both: SOV \u00b7 postpositions \u00b7 agglutinative \u00b7 vowel harmony \u00b7 no gender \u00b7 7 cases', 'middle', 'Ls')
    svg += t(240, 598, 'Different families but shared steppe contact: many parallel structural features', 'middle', 'Ls')

    svg += footer(57, 'MONGOLIAN', 'KAZAKH', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_57d_alt():
    svg = open_svg()
    svg += t(240, 32, 'MONGOLIAN (\u043c\u043e\u043d\u0433\u043e\u043b \u0445\u044d\u043b) / KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456)', 'middle', 'T')
    svg += t(240, 44, 'MONGOLIC / TURKIC \u00b7 EURASIAN STEPPE \u00b7 HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 57D ALT \u00b7 HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MONGOLIAN: HISTORY & EMPIRE \u2014')
    svg += sh(88, 'CHINGGIS KHAN AND THE MONGOL EMPIRE (~1206\u20131368 CE)')
    svg += t(240, 99, '1206: Temujin unifies Mongol tribes; proclaimed Chinggis (Genghis) Khan', 'middle', 'Ls')
    svg += t(240, 110, 'Peak territory: ~24M km\u00b2 \u2014 largest contiguous empire in human history', 'middle', 'Ls')
    svg += t(240, 121, 'Covered: China, Persia, Russia, Central Asia, Korea, parts of SE Europe', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, "THE \u2018PHAGS-PA SCRIPT (1269 CE)")
    svg += t(240, 148, 'Khublai Khan commissioned a universal script for all empire languages', 'middle', 'Ls')
    svg += t(240, 159, '\u2018Phags-pa: designed by Tibetan monk Drogon Chogyal Phagpa \u2014 square Brahmi-based', 'middle', 'Ls')
    svg += t(240, 170, 'Used briefly; replaced by traditional Mongolian script in practice', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'TRADITIONAL SCRIPT & LITERACY')
    svg += t(240, 197, 'Traditional Mongolian script: created ~1204 CE, based on Old Uyghur', 'middle', 'Ls')
    svg += t(240, 208, 'Unique vertical orientation: the only surviving major vertical-LTR script', 'middle', 'Ls')
    svg += t(240, 219, 'The Secret History of the Mongols (~1240): oldest Mongolian literary work', 'middle', 'Ls')
    svg += hr(225, sw=0.3)
    svg += sh(235, 'MODERN MONGOLIA')
    svg += t(240, 246, '1924: Mongolian People\'s Republic (Soviet satellite) \u00b7 1990: democratic transition', 'middle', 'Ls')
    svg += t(240, 257, '1941: Cyrillic adopted \u00b7 2020: traditional script revival mandated alongside Cyrillic', 'middle', 'Ls')
    svg += t(240, 268, 'Inner Mongolia (China): ~4M speakers, traditional script officially maintained', 'middle', 'Ls')
    svg += hr(274, sw=0.3)
    svg += sh(284, 'SURVIVAL PHRASE')
    svg += t(240, 295, '\u042d\u043d\u044d \u0447\u0430\u043c\u044b\u0433\u043b\u0430 \u04af\u043d\u044d \u0445\u04af\u043c\u04af\u04af\u0441\u0438\u0439\u043d \u0445\u0430\u0440\u0441\u0430\u0430\u043d \u0432\u0438\u0434\u044d\u0432\u0447\u0438\u0434\u0438\u0439\u043d \u0445\u04af\u043c\u04af\u04af\u0441\u044d\u043b\u044d\u0440 \u0447\u0438\u043d\u044d\u044d\u043f \u04af\u0439\u043b\u0434\u04af\u0432\u0441\u044d\u043d.', 'middle', 'Lx')
    svg += t(240, 307, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 318, '(\u04af\u043d\u044d\u0445\u04af\u043c\u04af\u04af\u0441 = forward; \u0447\u0438\u043d\u044d = with/by \u2014 instrumental case)', 'middle', 'Ls')

    svg += sec_divider(330, 'KAZAKH (\u049b\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456) \u2014 HISTORY & CULTURAL LEGACY')

    svg += sh(355, '\u2014 KAZAKH: THE GREAT STEPPE CIVILIZATION \u2014')
    svg += sh(366, 'KAZAKH KHANATE (1465 CE) AND THE ZHUZ SYSTEM')
    svg += t(240, 377, 'Kazakh identity emerged ~1465 when Sultans Kerei and Janibek broke from Uzbek Khanate', 'middle', 'Ls')
    svg += t(240, 388, 'Organized into 3 zhuz (hordes): Great Zhuz · Middle Zhuz · Small Zhuz', 'middle', 'Ls')
    svg += t(240, 399, 'Zhuz system reflects pastoral territory divisions; clans within each zhuz', 'middle', 'Ls')
    svg += hr(405, sw=0.3)
    svg += sh(415, 'NOMADIC LIFE: YURT, HORSE, EAGLE')
    svg += t(240, 426, 'Yurt (kiyiz \u04af\u0439): portable felt dwelling \u2014 central to Kazakh identity and oral tradition', 'middle', 'Ls')
    svg += t(240, 437, 'Eagle hunting (berkutchi): falconry with golden eagles \u2014 UNESCO 2016 heritage', 'middle', 'Ls')
    svg += t(240, 448, 'Dombra: 2-string lute; oral epics (zhyrau) performed to dombra accompaniment', 'middle', 'Ls')
    svg += hr(454, sw=0.3)
    svg += sh(464, 'RUSSIAN COLONIZATION & SOVIET PERIOD')
    svg += t(240, 475, '1731\u201348: Kazakhs accepted Russian protectorate under nomadic pressure', 'middle', 'Ls')
    svg += t(240, 486, '1929\u201333: Soviet collectivization killed ~1.5M Kazakhs (Asharshylyk famine)', 'middle', 'Ls')
    svg += t(240, 497, '1936: Kazakh SSR formed \u00b7 1991: Republic of Kazakhstan independent', 'middle', 'Ls')
    svg += hr(503, sw=0.3)
    svg += sh(513, 'SCRIPT TRANSITIONS: ARABIC \u2192 CYRILLIC \u2192 LATIN')
    svg += t(240, 524, 'Arabic script used until 1929 \u00b7 1929: Latin \u00b7 1940: Cyrillic (Soviet policy)', 'middle', 'Ls')
    svg += t(240, 535, '2017: President Nazarbayev announced return to Latin by 2025 (now 2031)', 'middle', 'Ls')
    svg += t(240, 546, 'Three scripts = three different literacies in living Kazakh speakers today', 'middle', 'Ls')
    svg += hr(552, sw=0.3)
    svg += sh(562, 'WESTERN MONGOLIA: WHERE KAZAKH AND MONGOLIAN MEET')
    svg += t(240, 573, 'Bayan-Olgii province: ~90% ethnic Kazakh, within Mongolia\'s borders', 'middle', 'Ls')
    svg += t(240, 584, 'Trilingual area: Kazakh · Mongolian · Russian spoken in same households', 'middle', 'Ls')
    svg += hr(590, sw=0.3)
    svg += sh(600, 'SURVIVAL PHRASE (KAZAKH)')
    svg += t(240, 611, '\u0411\u04b1\u043b \u0441\u0456\u0437\u0434\u0456\u04a3 \u04af\u0448\u0456\u043d \u0436\u0430\u0441\u0430\u043b\u0493\u0430\u043d, \u0442\u0435\u0433\u0456\u043d, \u0430\u043b\u0493\u0430 \u0430\u0441\u049b\u0430\u043d \u0430\u0434\u0430\u043c\u0434\u0430\u0440 \u0436\u0430\u0441\u0430\u0493\u0430\u043d.', 'middle', 'Lx')
    svg += t(240, 622, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')

    svg += footer(57, 'MONGOLIAN', 'KAZAKH', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate57a_mongolian_kazakh_script_alt.svg',    build_57a_alt),
        ('plate57b_mongolian_kazakh_phonology_alt.svg',  build_57b_alt),
        ('plate57c_mongolian_kazakh_grammar_alt.svg',    build_57c_alt),
        ('plate57d_mongolian_kazakh_history_alt.svg',    build_57d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
