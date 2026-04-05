import os

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
        'text { font-family: "Noto Sans Mongolian", "Noto Sans", serif; }\n'
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

def build_57a():
    out = open_svg()
    out += t(240, 45, 'MONGOLIAN', 'middle', 'S')
    out += t(240, 65, '\u041c\u043e\u043d\u0433\u043e\u043b  (\u041c\u043e\u043d\u0433\u043e\u043b \u0445\u044d\u043b)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Two Scripts')
    out += t(240, 112, 'Traditional Mongolian Script: vertical, top-to-bottom', 'middle', 'X')
    out += t(240, 128, 'Used in Inner Mongolia (China) · revived in Mongolia', 'middle', 'X')
    out += t(240, 144, 'Cyrillic: introduced 1941 · official script in Mongolia', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Cyrillic Alphabet — 35 Letters')
    cyrillic = [
        '\u0410 \u0411 \u0412 \u0413 \u0414 \u0415 \u0401 \u0416 \u0417 \u0418',
        '\u0419 \u041a \u041b \u041c \u041d \u041e \u04e8 \u041f \u0420 \u0421',
        '\u0422 \u0423 \u04ae \u0424 \u0425 \u0426 \u0427 \u0428 \u0429 \u042a',
        '\u042b \u042c \u042d \u042e \u042f',
    ]
    y = 192
    for row in cyrillic:
        out += t(240, y, row, 'middle', 'L')
        y += 18
    out += hr(298)
    out += sh(314, 'Unique Mongolian Cyrillic Letters')
    out += t(240, 331, '\u04e8  \u04e8\u04e9  = vowel /\u00f8/ (front rounded o)', 'middle', 'L')
    out += t(240, 347, '\u04ae  \u04af  = vowel /y/ (front rounded u)', 'middle', 'L')
    out += t(240, 363, 'These distinguish Mongolian from Russian Cyrillic', 'middle', 'X')
    out += hr(378)
    out += sh(394, 'Traditional Script Basics')
    out += t(240, 411, 'Written vertically: top to bottom, columns left to right', 'middle', 'X')
    out += t(240, 427, 'Derived from Uyghur script via Sogdian (Aramaic)', 'middle', 'X')
    out += t(240, 443, 'Letters have initial/medial/final forms', 'middle', 'X')
    out += t(240, 459, 'Unicode block: U+1800-U+18AF', 'middle', 'X')
    out += hr(474)
    out += t(240, 491, '~5.2M speakers · Mongolia + Inner Mongolia', 'middle', 'X')
    out += t(240, 507, 'Mongolic language family · agglutinative', 'middle', 'X')
    out += footer(57, 'Mongolian', 'a', 'Script · Cyrillic + Traditional')
    out += close_svg()
    return out

def build_57b():
    out = open_svg()
    out += t(240, 45, 'MONGOLIAN  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, '\u0414\u0443\u0443 \u0437\u04af\u0439\u043d \u0448\u0438\u043d\u0436\u043b\u044d\u043b', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Vowel Harmony')
    out += t(240, 112, 'Vowels divide into FRONT and BACK groups:', 'middle', 'X')
    out += t(240, 128, 'Back: a  o  u  (\u0430 \u043e \u0443)', 'middle', 'L')
    out += t(240, 144, 'Front: \u0259  \u00f8  y (\u044d \u04e9 \u04af)', 'middle', 'L')
    out += t(240, 160, 'Neutral: i (\u0438) — compatible with both', 'middle', 'L')
    out += t(240, 176, 'All vowels in a word must belong to same class', 'middle', 'X')
    out += hr(190)
    out += sh(206, 'Consonants')
    cons = [
        ('Stops:', 'p b t d k g (aspirated in some positions)'),
        ('Fricatives:', 's z sh zh x h'),
        ('Affricates:', 'ts ch j (dz)'),
        ('Nasals:', 'm n ng (\u014b)'),
        ('Liquids:', 'l r'),
        ('Approximants:', 'w y'),
    ]
    y = 223
    for label, val in cons:
        out += t(90, y, label, 'end', 'X')
        out += t(100, y, val, 'start', 'L')
        y += 18
    out += hr(341)
    out += sh(357, 'Long Vowels')
    out += t(240, 374, 'Vowel length is contrastive:', 'middle', 'X')
    out += t(240, 390, '\u0445\u043e\u043b  (khol) = boiled  vs  \u0445\u043e\u043e\u043b (khool) = food', 'middle', 'L')
    out += hr(404)
    out += sh(420, 'Stress')
    out += t(240, 437, 'Word-initial stress in most words', 'middle', 'X')
    out += t(240, 453, 'Long vowels in non-initial syllables attract stress', 'middle', 'X')
    out += hr(466)
    out += sh(482, 'Consonant Clusters')
    out += t(240, 499, 'Rich onset clusters: \u0433\u0440, \u0434\u0436, \u0442\u0440...', 'middle', 'X')
    out += footer(57, 'Mongolian', 'b', 'Phonology · Vowel Harmony · Tones')
    out += close_svg()
    return out

def build_57c():
    out = open_svg()
    out += t(240, 45, 'MONGOLIAN  GRAMMAR', 'middle', 'S')
    out += t(240, 65, '\u0414\u04af\u0440\u043c\u0438\u0439\u043d \u0437\u04af\u0439', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Agglutinative  ·  SOV  Word Order')
    out += t(240, 112, '\u0411\u0438 \u0443\u0441 \u0443\u0443\u0491\u043d\u0430', 'middle', 'L')
    out += t(240, 128, 'Bi us uudhna — "I drink water"', 'middle', 'X')
    out += hr(141)
    out += sh(157, 'Cases — 8 Cases via Suffixes')
    cases = [
        ('\u041d\u044d\u0440\u043b\u044d\u043b', 'nominative', '-\u00d8', 'subject'),
        ('\u0425\u0430\u0440\u044c\u044f\u043b\u0430\u043b', 'accusative', '-\u0438\u0439\u0433', 'definite object'),
        ('\u0413\u0430\u0440\u0430\u0445', 'genitive', '-\u044b\u043d/\u0438\u0439\u043d', 'possession'),
        ('\u04e8\u0433\u04e9\u0445', 'dative', '-\u0434/\u0442', 'to, for'),
        ('\u0417\u0430\u0439\u043d', 'locative', '-\u0434/\u0442', 'at, in'),
        ('\u0413\u0430\u0440\u0430\u0445', 'ablative', '-\u0430\u0430\u0441/\u044d\u044d\u0441', 'from'),
        ('\u0425\u044d\u0440\u044d\u0433\u043b\u044d\u043b', 'instrumental', '-\u0430\u0430\u0440/\u044d\u044d\u0440', 'by means of'),
        ('\u0425\u0430\u043c\u0442\u0440\u0430\u043d', 'comitative', '-\u0442\u0430\u0439', 'together with'),
    ]
    y = 174
    for mon, eng, suf, gloss in cases:
        out += t(55, y, mon, 'middle', 'X')
        out += t(155, y, eng, 'middle', 'X')
        out += t(240, y, suf, 'middle', 'L')
        out += t(340, y, gloss, 'start', 'X')
        y += 17
    out += hr(322)
    out += sh(338, 'Core Vocabulary')
    vocab = [
        ('\u0443\u0441','us','water'),('\u0442\u0430\u043b\u0445','talkh','bread'),
        ('\u0433\u044d\u0440','ger','house/yurt'),('\u044d\u044d\u0436','eej','mother'),
        ('\u043d\u04af\u0445\u04e9\u0440','nukhur','friend'),('\u0442\u0438\u0439\u043c','tiim','yes'),
        ('\u04af\u0433\u04af\u0439','ugui','no'),('\u043d\u044d\u0440','ner','name'),
    ]
    y = 355
    for i in range(0, len(vocab), 2):
        m1, r1, g1 = vocab[i]
        m2, r2, g2 = vocab[i+1]
        out += t(55, y, m1, 'middle', 'L')
        out += t(115, y, r1, 'middle', 'X')
        out += t(180, y, g1, 'middle', 'X')
        out += t(275, y, m2, 'middle', 'L')
        out += t(345, y, r2, 'middle', 'X')
        out += t(415, y, g2, 'middle', 'X')
        y += 18
    out += footer(57, 'Mongolian', 'c', 'Grammar · 8 Cases · Agglutination')
    out += close_svg()
    return out

def build_57d():
    out = open_svg()
    out += t(240, 45, 'MONGOLIAN  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, '\u0422\u0435\u043a\u0441\u0442 \u0431\u0430 \u0433\u04af\u04af\u0440', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Secret History of the Mongols — c. 1227')
    out += t(240, 112, '\u0427\u0438\u043d\u0433\u0433\u0438\u0441 \u0425\u0430\u0430\u043d\u0438\u0439 \u0442\u0430\u043d\u0438\u043b\u0446\u0430\u0430 \u043d\u044c \u0442\u044d\u0440\u0433\u04af\u04af\u043b', 'middle', 'L')
    out += t(240, 128, '"The secret history of Chinggis Khan"', 'middle', 'X')
    out += t(240, 144, 'Oldest surviving Mongolic literature', 'middle', 'X')
    out += t(240, 160, '\u041e\u0440\u0447\u043b\u0430\u043d \u0445\u0443\u0432\u0430\u0440\u0433\u0438 \u0438\u0445 \u0442\u04af\u0433\u044d\u044d \u0433\u0430\u0440\u0447 \u0445\u0430\u0440\u0430\u0445\u0434\u0430\u0430', 'middle', 'L')
    out += t(240, 176, '"The sky has ordered it thus — the earth has agreed"', 'middle', 'X')
    out += hr(190)
    out += sh(206, 'Proverb')
    out += t(240, 223, '\u0414\u044d\u043b\u0445\u0438\u0439\u0446\u0438\u0439\u0433 \u043d\u044c \u0445\u044f\u043c\u0442 \u0434\u044d\u043b\u0445\u0438\u0439\u0446 \u0434\u0430\u0440\u0430\u0430\u0433\u0443\u0439', 'middle', 'L')
    out += t(240, 239, '"Tame the tongue, and it will become your ally"', 'middle', 'X')
    out += hr(253)
    out += sh(269, 'Bridge Phrase')
    out += t(240, 289, '\u042d\u043d\u044d \u0442\u0430\u043d\u044b \u0442\u04af\u043b\u04e9\u04e9 \u0447\u04e9\u043b\u04e9\u04e9\u043b\u0441\u04e9\u043d,', 'middle', 'L')
    out += t(240, 305, '\u04af\u043d\u044d\u0433\u04af\u0439\u0433\u044d\u044d\u0440, \u0446\u0430\u0430\u0448\u0434\u0430 \u0445\u0430\u0440\u0430\u0433\u0434\u0441\u0430\u043d \u0445\u04af\u043c\u04af\u04af\u0441\u0438\u0439\u043d', 'middle', 'L')
    out += t(240, 321, '\u0438\u0440\u0433\u044d\u0434\u0438\u0439\u0433 \u0441\u0430\u043d\u0430\u0441\u0430\u043d \u0445\u04af\u043c\u04af\u04af\u0441\u0438\u0439\u043d\u044d\u0440 \u0445\u0438\u0439\u0433\u044d\u044d\u0441\u044d\u043d.', 'middle', 'L')
    out += t(240, 341, 'Ene tany tulo\u00f6l choloolson,', 'middle', 'X')
    out += t(240, 357, 'unegiigeer, tsaashda kharagdsan khumuusiin', 'middle', 'X')
    out += t(240, 373, 'irgediyig sanasan khumuusiiner khiygeesen.', 'middle', 'X')
    out += t(240, 391, '"This was made for you, freely, by people', 'middle', 'X')
    out += t(240, 405, 'who remembered forward."', 'middle', 'X')
    out += hr(420)
    out += t(240, 437, 'Mongolian · ~5.2M speakers · Mongolic family', 'middle', 'X')
    out += t(240, 453, 'Mongolia + Inner Mongolia · steppe heritage', 'middle', 'X')
    out += footer(57, 'Mongolian', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate57a_mongolian_script.svg', build_57a()),
        ('plate57b_mongolian_phonology.svg', build_57b()),
        ('plate57c_mongolian_grammar.svg', build_57c()),
        ('plate57d_mongolian_text.svg', build_57d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
