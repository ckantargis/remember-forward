import os, re

OUT = os.path.join(os.path.dirname(__file__))

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680">\n'
        '<rect x="8" y="8" width="464" height="664" rx="10" ry="10" '
        'fill="none" stroke="#1a1a2e" stroke-width="2"/>\n'
        '<rect x="14" y="14" width="452" height="652" rx="8" ry="8" '
        'fill="none" stroke="#1a1a2e" stroke-width="0.5"/>\n'
        '<style>\n'
        'text { font-family: "Noto Nastaliq Urdu", "Noto Sans Arabic", serif; }\n'
        '.T { font-size: 13px; fill: #1a1a2e; }\n'
        '.H { font-size: 11px; fill: #5a4a6b; font-style: italic; }\n'
        '.L { font-size: 12px; fill: #1a1a2e; }\n'
        '.S { font-size: 15px; fill: #1a1a2e; font-weight: bold; }\n'
        '.X { font-size: 11px; fill: #3a3a5c; }\n'
        '.F { font-size: 9px; fill: #7a7a9a; }\n'
        '</style>\n'
    )

def close_svg(): return '</svg>\n'

def t(x, y, s, a='middle', c='L', extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{esc(s)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#1a1a2e" stroke-width="{sw}"/>\n'

def sh(y, txt):
    return t(240, y, f'— {txt} —', 'middle', 'H')

def footer(num, lang, letter, desc):
    out = hr(610)
    out += t(240, 625, f'PLATE {num}{letter.upper()}  ·  {lang.upper()}', 'middle', 'F')
    out += t(240, 640, desc, 'middle', 'F')
    out += t(240, 655, 'REMEMBER FORWARD', 'middle', 'F')
    return out

def build_54a():
    out = open_svg()
    out += t(240, 45, 'URDU', 'middle', 'S')
    out += t(240, 65, '\u0627\u0631\u062f\u0648  (Urdū)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Nastaliq Script')
    out += t(240, 112, 'Nastaliq = hanging style of Arabic calligraphy', 'middle', 'X')
    out += t(240, 128, 'Right-to-left · Cursive · Context-sensitive letter forms', 'middle', 'X')
    out += t(240, 144, 'Each letter has 4 forms: isolated / initial / medial / final', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Selected Letters')
    rows = [
        ('\u0627 alif', '\u0628 be', '\u067e pe', '\u062a te'),
        ('\u062c jeem', '\u062e khe', '\u062f dal', '\u0630 zal'),
        ('\u0631 re', '\u0633 seen', '\u0634 sheen', '\u0635 suad'),
        ('\u0639 ain', '\u063a ghain', '\u0641 fe', '\u0642 qaf'),
        ('\u06a9 kaf', '\u06af gaf', '\u0644 lam', '\u0645 meem'),
        ('\u0646 nun', '\u0648 wao', '\u06cc ye', '\u06c1 he'),
    ]
    y = 190
    for row in rows:
        out += t(70, y, row[0], 'middle', 'L')
        out += t(180, y, row[1], 'middle', 'L')
        out += t(300, y, row[2], 'middle', 'L')
        out += t(410, y, row[3], 'middle', 'L')
        y += 18
    out += hr(312)
    out += sh(328, 'Unique Urdu Letters (not in Arabic)')
    unique = [
        ('\u067e  pe  p', '\u0679  tte  \u1e6d'),
        ('\u0688  dde  \u1e0d', '\u06ba  noon ghunna  \u1e3f'),
        ('\u06af  gaf  g', '\u06c1  choti he  h'),
    ]
    y = 345
    for a, b in unique:
        out += t(130, y, a, 'middle', 'L')
        out += t(350, y, b, 'middle', 'L')
        y += 18
    out += hr(396)
    out += sh(412, 'Vowel Diacritics (Harakat)')
    out += t(240, 429, 'Short vowels usually omitted in everyday text', 'middle', 'X')
    y = 447
    for xi, item in enumerate(('\u064e  zabar = a', '\u0650  zer = i', '\u064f  pesh = u')):
        out += t(80 + xi*130, y, item, 'middle', 'L')
    y += 18
    out += t(240, 465, 'Shadda \u0651 = consonant doubling', 'middle', 'X')
    out += t(240, 481, '\u0622 alef madd = long /aa/', 'middle', 'L')
    out += footer(54, 'Urdu', 'a', 'Script · Nastaliq · Letters')
    out += close_svg()
    return out

def build_54b():
    out = open_svg()
    out += t(240, 45, 'URDU  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, '\u0635\u0648\u062a\u06cc\u0627\u062a  (Sautiyāt)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Consonants')
    out += t(240, 112, 'Urdu has 4-way stop contrast at bilabial and dental:', 'middle', 'X')
    stops = [
        ('p','plain voiceless','b','plain voiced'),
        ('ph','aspirated vl.','bh','murmured/breathy'),
    ]
    y = 128
    for a, b, c, d in stops:
        out += t(60, y, a, 'middle', 'L')
        out += t(150, y, b, 'middle', 'X')
        out += t(290, y, c, 'middle', 'L')
        out += t(380, y, d, 'middle', 'X')
        y += 16
    out += hr(162)
    out += sh(178, 'Special Sounds')
    sounds = [
        ('q  \u0642', '/q/', 'uvular stop — Arabic loanwords'),
        ('x  \u062e', '/x/', 'velar fricative — kha\u1e6d\u1e6d\u0101 (letters)'),
        ('gh \u063a', '/\u0263/', 'voiced velar fricative — \u0121ussul (solution)'),
        ('\u1e96 / h', '/\u02b0/', 'murmur/aspiration — bh, dh, gh, jh...'),
        ('\u0294  \u0639', '/\u02bf/', 'pharyngeal — Arabic \u02bbain'),
        ('\u1e96', '/h/', 'glottal — he in Urdu'),
    ]
    y = 195
    for sym, ipa, note in sounds:
        out += t(70, y, sym, 'middle', 'L')
        out += t(130, y, ipa, 'middle', 'X')
        out += t(290, y, note, 'start', 'X')
        y += 17
    out += hr(308)
    out += sh(324, 'Vowels')
    vowels = [
        ('a','short low central','\u0101','long low'),
        ('i','short high front','\u012b','long high front'),
        ('u','short high back','\u016b','long high back'),
        ('e','mid front','o','mid back'),
        ('ai','/\u025b/ or /\u00e6/','au','/\u0254/'),
    ]
    y = 341
    for a, b, c, d in vowels:
        out += t(55, y, a, 'middle', 'L')
        out += t(150, y, b, 'middle', 'X')
        out += t(270, y, c, 'middle', 'L')
        out += t(385, y, d, 'middle', 'X')
        y += 17
    out += hr(428)
    out += sh(444, 'Nasalization')
    out += t(240, 461, 'Nasalized vowels contrast with oral vowels', 'middle', 'X')
    out += t(240, 477, '\u06c1\u0648\u0646\u0627  honā (to be) vs \u06c1\u0648\u0722  ho\u1e43 (be!)', 'middle', 'L')
    out += footer(54, 'Urdu', 'b', 'Phonology · Stops · Murmur')
    out += close_svg()
    return out

def build_54c():
    out = open_svg()
    out += t(240, 45, 'URDU  GRAMMAR', 'middle', 'S')
    out += t(240, 65, '\u0642\u0648\u0627\u0639\u062f  (Qawā\u02bfid)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Word Order  SOV')
    out += t(240, 112, '\u0645\u06cc\u06ba \u067e\u0627\u0646\u06cc \u067e\u06cc\u062a\u0627 \u06c1\u0648\u06ba', 'middle', 'L')
    out += t(240, 128, 'maĩ pānī pītā hūṃ — "I drink water"', 'middle', 'X')
    out += hr(141)
    out += sh(157, 'Postpositions')
    posts = [
        ('\u06a9\u0627/\u06a9\u06cc/\u06a9\u06d2', 'kā/kī/ke', 'of (genitive; agrees with possessed)'),
        ('\u06a9\u0648', 'ko', 'to, DATIVE / marks definite object'),
        ('\u0633\u06d2', 'se', 'from, with, ABLATIVE/INSTRUMENTAL'),
        ('\u0645\u06cc\u06ba', 'mẽ', 'in, LOCATIVE'),
        ('\u067e\u0631', 'par', 'on, at'),
        ('\u06a9\u06d2 \u0644\u06cc\u06d2', 'ke lie', 'for, PURPOSE'),
        ('\u06a9\u06d2 \u0633\u0627\u062a\u06be', 'ke sāth', 'with, COMITATIVE'),
    ]
    y = 174
    for urd, rom, gloss in posts:
        out += t(65, y, urd, 'middle', 'L')
        out += t(145, y, rom, 'middle', 'X')
        out += t(295, y, gloss, 'start', 'X')
        y += 17
    out += hr(298)
    out += sh(314, 'Verb System')
    out += t(240, 331, 'Verbs inflect for gender, number, tense, aspect', 'middle', 'X')
    out += t(240, 347, '\u0644\u06aa\u06be\u0646\u0627  likhna = to write', 'middle', 'L')
    verbs = [
        ('\u0645\u06cc\u06ba \u0644\u06a9\u06be\u062a\u0627/\u0644\u06a9\u06be\u062a\u06cc \u06c1\u0648\u06ba', 'I write (m./f.)'),
        ('\u0645\u06cc\u06ba \u0646\u06d2 \u0644\u06a9\u06be\u0627', 'maĩ ne likhā — I wrote (perfective)'),
    ]
    y = 364
    for urd, gloss in verbs:
        out += t(240, y, urd, 'middle', 'L')
        out += t(240, y+14, gloss, 'middle', 'X')
        y += 32
    out += hr(432)
    out += sh(448, 'Core Vocabulary')
    vocab = [
        ('\u067e\u0627\u0646\u06cc','pānī','water'),('\u0631\u0648\u0679\u06cc','roṭī','bread'),
        ('\u06af\u06be\u0631','ghar','house'),('\u0645\u0627\u06ba','māṃ','mother'),
        ('\u062f\u0648\u0633\u062a','dost','friend'),('\u06c1\u0627\u06ba','hāṃ','yes'),
        ('\u0646\u06c1\u06cc\u06ba','nahīṃ','no'),('\u0646\u0627\u0645','nām','name'),
    ]
    y = 465
    for i in range(0, len(vocab), 2):
        u1, r1, g1 = vocab[i]
        u2, r2, g2 = vocab[i+1]
        out += t(50, y, u1, 'middle', 'L')
        out += t(120, y, r1, 'middle', 'X')
        out += t(190, y, g1, 'middle', 'X')
        out += t(280, y, u2, 'middle', 'L')
        out += t(360, y, r2, 'middle', 'X')
        out += t(430, y, g2, 'middle', 'X')
        y += 18
    out += footer(54, 'Urdu', 'c', 'Grammar · Postpositions · Verbs')
    out += close_svg()
    return out

def build_54d():
    out = open_svg()
    out += t(240, 45, 'URDU  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, '\u0627\u0631\u062f\u0648 \u0645\u062a\u0646 \u0627\u0648\u0631 \u0633\u06cc\u062a\u0648 \u0633\u062e\u0646', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Allama Iqbal — Lab Pe Aati Hai Dua')
    lines = [
        ('\u0644\u0628 \u067e\u06d2 \u0622\u062a\u06cc \u06c1\u06d2 \u062f\u0639\u0627 \u0628\u0646 \u06a9\u06d2 \u062a\u0645\u0646\u0651\u0627 \u0645\u06cc\u0631\u06cc',
         'Lab pe ātī hai duā ban ke tamannā merī'),
        ('\u0632\u0646\u062f\u06af\u06cc \u0634\u0645\u0639 \u06a9\u06cc \u0635\u0648\u0631\u062a \u06c1\u0648 \u062e\u062f\u0627\u06cc\u0627 \u0645\u06cc\u0631\u06cc',
         'Zindagī sham\u02bf kī sūrat ho Khudāyā merī'),
        ('\u06c1\u0648 \u0645\u06cc\u0631\u0627 \u06a9\u0627\u0645 \u063a\u0631\u06cc\u0628\u0648\u06ba \u06a9\u06cc \u062d\u0645\u0627\u06cc\u062a \u06a9\u0631\u0646\u0627',
         'Ho merā kām ġharīboṃ kī himāyat karnā'),
    ]
    y = 112
    for urd, rom in lines:
        out += t(240, y, urd, 'middle', 'L')
        out += t(240, y+14, rom, 'middle', 'X')
        y += 34
    out += t(240, y, '"My prayer rises to my lips as a wish..."', 'middle', 'X')
    out += hr(230)
    out += sh(246, 'Proverb')
    out += t(240, 263, '\u0639\u0642\u0644 \u0628\u0691\u06cc \u0686\u06cc\u0632 \u06c1\u06d2', 'middle', 'L')
    out += t(240, 279, '\u02bfAql baṛī cīz hai — "Intellect is a great thing"', 'middle', 'X')
    out += hr(293)
    out += sh(309, 'Bridge Phrase')
    out += t(240, 329, '\u06cc\u06c1 \u0622\u067e \u06a9\u06d2 \u0644\u06cc\u06d2 \u0628\u0646\u0627\u06cc\u0627 \u06af\u06cc\u0627 \u062a\u06be\u0627,', 'middle', 'L')
    out += t(240, 347, '\u0645\u0641\u062a \u0645\u06cc\u06ba, \u0627\u0646 \u0644\u0648\u06af\u0648\u06ba \u06a9\u06cc \u0637\u0631\u0641 \u0633\u06d2', 'middle', 'L')
    out += t(240, 365, '\u062c\u0646\u06be\u0648\u06ba \u0646\u06d2 \u0622\u06af\u06d2 \u06a9\u0648 \u06cc\u0627\u062f \u06a9\u06cc\u0627\u06d4', 'middle', 'L')
    out += t(240, 387, 'Yih āp ke lie banāyā gayā thā, muft mẽ,', 'middle', 'X')
    out += t(240, 403, 'un logoṃ kī ṭaraf se jinhoṃ ne', 'middle', 'X')
    out += t(240, 419, 'āge ko yād kiyā.', 'middle', 'X')
    out += t(240, 437, '"This was made for you, freely, by people', 'middle', 'X')
    out += t(240, 451, 'who remembered forward."', 'middle', 'X')
    out += hr(465)
    out += t(240, 482, 'Urdu · ~70M native + 100M L2 speakers', 'middle', 'X')
    out += t(240, 498, 'Pakistan (official) · India · literary tradition', 'middle', 'X')
    out += footer(54, 'Urdu', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate54a_urdu_script.svg', build_54a()),
        ('plate54b_urdu_phonology.svg', build_54b()),
        ('plate54c_urdu_grammar.svg', build_54c()),
        ('plate54d_urdu_text.svg', build_54d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
