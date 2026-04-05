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

def build_55a():
    out = open_svg()
    out += t(240, 45, 'PASHTO', 'middle', 'S')
    out += t(240, 65, '\u067e\u069a\u062a\u0648  (Pax\u02b0to)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Pashto Script')
    out += t(240, 112, 'Extended Perso-Arabic · right-to-left · cursive', 'middle', 'X')
    out += t(240, 128, '44 letters — largest Arabic-based alphabet', 'middle', 'X')
    out += t(240, 144, 'Extra letters added for sounds unique to Pashto', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Unique Pashto Letters')
    unique = [
        ('\u0681  tsay  /\u02a3/', '\u0685  che  /\u02a7/'),
        ('\u069a  shin-xe  /\u0283\u02b0/', '\u0693  rre  /\u0256/'),
        ('\u0696  zhe  /\u0292/', '\u0698  zhe2  /d\u0292/'),
        ('\u06bc  noon-ghunna  /\u014b/', '\u06cd  ye-barri  /aj/'),
        ('\u06d0  ye  /e/', '\u0636  dvad  /\u0256/'),
    ]
    y = 190
    for a, b in unique:
        out += t(130, y, a, 'middle', 'L')
        out += t(340, y, b, 'middle', 'L')
        y += 18
    out += hr(382)
    out += sh(398, 'Shared Arabic Letters')
    out += t(240, 415, '\u0627 \u0628 \u062a \u062b \u062c \u062d \u062e \u062f \u0630 \u0631 \u0632', 'middle', 'L')
    out += t(240, 433, '\u0633 \u0634 \u0635 \u0636 \u0637 \u0638 \u0639 \u063a \u0641 \u0642 \u0643 \u0644 \u0645 \u0646 \u0648 \u06cc \u06c1', 'middle', 'L')
    out += hr(448)
    out += sh(464, 'Geographic Context')
    out += t(240, 481, 'Afghanistan (co-official) · NW Pakistan', 'middle', 'X')
    out += t(240, 497, '~50 million speakers · Eastern Iranian family', 'middle', 'X')
    out += t(240, 513, 'Closely related to Dari (Afghan Persian)', 'middle', 'X')
    out += footer(55, 'Pashto', 'a', 'Script · Pashto-Extended Arabic')
    out += close_svg()
    return out

def build_55b():
    out = open_svg()
    out += t(240, 45, 'PASHTO  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, '\u0622\u0648\u0627\u0632\u0648\u0646\u0647  (Awāzonah)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Distinctive Sounds')
    sounds = [
        ('/\u0283\u02b0/', 'retroflex aspirated sh — xin with aspiration'),
        ('/\u0256/', 'retroflex d — rare cross-linguistically'),
        ('/\u02a3/ /\u02a7/', 'affricates: ts and ch'),
        ('/x/ /\u0263/', 'velar fricatives from Persian'),
        ('/\u0292/', 'voiced postalveolar fricative (zh)'),
        ('/q/', 'uvular stop — Arabic-origin words'),
        ('/\u02bf/', 'pharyngeal — \u02bfain from Arabic'),
    ]
    y = 112
    for ipa, note in sounds:
        out += t(75, y, ipa, 'middle', 'L')
        out += t(270, y, note, 'start', 'X')
        y += 18
    out += hr(248)
    out += sh(264, 'Vowels')
    vowels = [
        ('a  short low', '\u0101  long low'),
        ('i  short high front', '\u012b  long high front'),
        ('u  short back', '\u016b  long back'),
        ('e  mid front', 'o  mid back'),
    ]
    y = 281
    for a, b in vowels:
        out += t(120, y, a, 'middle', 'X')
        out += t(340, y, b, 'middle', 'X')
        y += 17
    out += hr(352)
    out += sh(368, 'Dialect Variation')
    out += t(240, 385, 'Southern (Kandahari): distinguishes /\u0283/ vs /\u0445/', 'middle', 'X')
    out += t(240, 401, 'Northern (Peshawar): merges some retroflex sounds', 'middle', 'X')
    out += t(240, 417, 'Eastern: preserves older vowel contrasts', 'middle', 'X')
    out += hr(430)
    out += sh(446, 'Stress')
    out += t(240, 463, 'Stress is contrastive and marks grammatical function', 'middle', 'X')
    out += t(240, 479, 'Verb stems shift stress in conjugation', 'middle', 'X')
    out += footer(55, 'Pashto', 'b', 'Phonology · Retroflex · Uvulars')
    out += close_svg()
    return out

def build_55c():
    out = open_svg()
    out += t(240, 45, 'PASHTO  GRAMMAR', 'middle', 'S')
    out += t(240, 65, '\u0622\u0695\u0648\u0646\u062f  (Ārwand)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Split Ergativity')
    out += t(240, 112, 'Pashto has a split ergative system:', 'middle', 'X')
    out += t(240, 128, 'Present: nominative-accusative (subject = agent)', 'middle', 'X')
    out += t(240, 144, 'Past/Perfective: ergative (agent takes oblique case)', 'middle', 'X')
    out += t(240, 160, '\u0645\u0627 \u067e\u0644\u0627\u0631 \u0644\u06cc\u062f\u0647 = mā palār līda (I saw father)', 'middle', 'L')
    out += t(240, 176, '"mā" (I) is in ergative/oblique case in past', 'middle', 'X')
    out += hr(190)
    out += sh(206, 'Cases')
    cases = [
        ('Direct', '\u0642\u0627\u0639\u062f\u06d0 \u062d\u0627\u0644\u062a', 'subject of intrans./pres. trans.'),
        ('Oblique', '\u063a\u06cc\u0631 \u0645\u0633\u062a\u0642\u06cc\u0645', 'object, past-tense agent, postpositional'),
        ('Vocative', '\u0646\u062f\u0627\u06cc\u06cd', 'direct address'),
    ]
    y = 222
    for eng, pash, note in cases:
        out += t(80, y, eng, 'end', 'X')
        out += t(90, y, pash, 'start', 'L')
        out += t(295, y, note, 'start', 'X')
        y += 18
    out += hr(264)
    out += sh(280, 'Verb Agreement')
    out += t(240, 297, 'Verbs agree with subject in present, and with', 'middle', 'X')
    out += t(240, 313, 'OBJECT in past transitive (ergative agreement)', 'middle', 'X')
    out += t(240, 329, 'Gender (masc./fem.) and number marked on verbs', 'middle', 'X')
    out += hr(342)
    out += sh(358, 'Word Order  SOV')
    out += t(240, 375, '\u0686\u06d0 \u067e\u0627\u0646\u06cc \u0633\u062a\u06cc  (ce pānī stī?)', 'middle', 'L')
    out += t(240, 391, '"Is there water?" — question by rising intonation', 'middle', 'X')
    out += hr(404)
    out += sh(420, 'Core Vocabulary')
    vocab = [
        ('\u0627\u0648\u0628\u0647','obah','water'),('\u0689\u0648\u06a9','ḍok','bread'),
        ('\u06a9\u0648\u0631','\u0643or','house'),('\u0645\u0648\u0631','mor','mother'),
        ('\u0648\u0631\u0648\u0631','wror','brother'),('\u0647\u0648','ho','yes'),
        ('\u0646\u0647','na','no'),('\u0646\u0648\u0645','num','name'),
    ]
    y = 436
    for i in range(0, len(vocab), 2):
        p1, r1, g1 = vocab[i]
        p2, r2, g2 = vocab[i+1]
        out += t(50, y, p1, 'middle', 'L')
        out += t(115, y, r1, 'middle', 'X')
        out += t(180, y, g1, 'middle', 'X')
        out += t(275, y, p2, 'middle', 'L')
        out += t(350, y, r2, 'middle', 'X')
        out += t(430, y, g2, 'middle', 'X')
        y += 18
    out += footer(55, 'Pashto', 'c', 'Grammar · Split Ergativity · Cases')
    out += close_svg()
    return out

def build_55d():
    out = open_svg()
    out += t(240, 45, 'PASHTO  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, '\u0645\u062a\u0646 \u0627\u0648 \u062f \u062f\u0648\u06d0 \u062f \u067e\u0644 \u062c\u0648\u0693', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Rahman Baba — 17th-century Pashto poet')
    lines = [
        ('\u062f \u0645\u06d0\u0646\u06d0 \u067e\u0627\u06cc\u0644\u06d0 \u0698\u0648\u0628\u0627 \u0634\u0627\u0647 \u062f\u06d0',
         'da mene pāyla zhoba shāh da'),
        ('\u067e\u0647 \u0644\u0627\u0631 \u06ba\u0627\u0646\u062f\u0644 \u062e\u067e\u0644 \u06a9\u06d0\u0698\u06cd',
         'pa lār nandal xpal kejy'),
        ('\u06cd \u062f\u06d0 \u0688\u0648\u0644 \u0631\u0627\u062d\u062a \u0648\u06d0',
         'ye da dhol rāhat way'),
    ]
    y = 112
    for pash, rom in lines:
        out += t(240, y, pash, 'middle', 'L')
        out += t(240, y+14, rom, 'middle', 'X')
        y += 34
    out += t(240, y, '"Pashto is the queen of languages / walk in its path"', 'middle', 'X')
    out += hr(230)
    out += sh(246, 'Proverb')
    out += t(240, 263, '\u067e\u069a\u062a\u0648\u0646 \u067e\u069a\u062a\u0648\u0646\u0647 \u06a9\u0648\u06d0', 'middle', 'L')
    out += t(240, 279, 'Paxtūn paxtonaʰ kaway — "A Pashtun does Pashtunwali"', 'middle', 'X')
    out += t(240, 295, '(Pashtunwali = code of honor, hospitality, and justice)', 'middle', 'X')
    out += hr(309)
    out += sh(325, 'Bridge Phrase')
    out += t(240, 345, '\u062f\u0627 \u0633\u062a\u0627\u0633\u0648 \u0644\u067e\u0627\u0631\u0647 \u062c\u0648\u0693\u06d0 \u0634\u0648\u06d0,', 'middle', 'L')
    out += t(240, 361, '\u0628\u0644\u0646\u062f\u067e\u0631\u06d0\u0632\u06d0, \u062f \u0647\u063a\u0648 \u062f \u062e\u0644\u06a9\u0648 \u0644\u0647 \u0686\u06d0', 'middle', 'L')
    out += t(240, 377, '\u067e\u0647 \u0645\u062e\u06a9\u06d0 \u0648\u0695\u0627\u0646\u062f\u0644.', 'middle', 'L')
    out += t(240, 397, 'Dā stāso lapāra joṛe shwe, bilnde payreze,', 'middle', 'X')
    out += t(240, 413, 'da hagho da xalko le ce', 'middle', 'X')
    out += t(240, 429, 'pa maxke wuṛāndal.', 'middle', 'X')
    out += t(240, 447, '"This was made for you, freely, by people', 'middle', 'X')
    out += t(240, 461, 'who remembered forward."', 'middle', 'X')
    out += hr(475)
    out += t(240, 492, 'Pashto · ~50M speakers · Eastern Iranian', 'middle', 'X')
    out += t(240, 508, 'Afghanistan + Pakistan · Pashtunwali oral tradition', 'middle', 'X')
    out += footer(55, 'Pashto', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate55a_pashto_script.svg', build_55a()),
        ('plate55b_pashto_phonology.svg', build_55b()),
        ('plate55c_pashto_grammar.svg', build_55c()),
        ('plate55d_pashto_text.svg', build_55d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
