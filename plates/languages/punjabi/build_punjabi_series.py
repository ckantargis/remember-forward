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
        'text { font-family: "Noto Sans Gurmukhi", "Noto Sans", serif; }\n'
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

def build_53a():
    out = open_svg()
    out += t(240, 45, 'PUNJABI', 'middle', 'S')
    out += t(240, 65, 'ਪੰਜਾਬੀ  (Pañjābī)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Gurmukhi Script')
    out += t(240, 118, 'Gurmukhi = "from the mouth of the Guru"', 'middle', 'X')
    out += t(240, 134, 'Created by Guru Angad Dev (2nd Sikh Guru) ~1539 CE', 'middle', 'X')
    out += t(240, 150, 'Abugida: each consonant carries inherent vowel /a/', 'middle', 'X')
    out += t(240, 166, 'Vowel diacritics (lāhā/mātrā) modify the base consonant', 'middle', 'X')
    out += hr(178)
    out += sh(193, 'Vowel Carriers')
    rows = [
        ('ਅ  a', 'ਆ  ā', 'ਇ  i', 'ਈ  ī'),
        ('ਉ  u', 'ਊ  ū', 'ਏ  e', 'ਔ  au'),
    ]
    y = 212
    for row in rows:
        out += t(70, y, row[0], 'middle', 'L')
        out += t(180, y, row[1], 'middle', 'L')
        out += t(300, y, row[2], 'middle', 'L')
        out += t(410, y, row[3], 'middle', 'L')
        y += 20
    out += hr(242)
    out += sh(258, 'Consonants — Selected')
    cons = [
        ('ਕ k', 'ਖ kh', 'ਗ g', 'ਘ gh'),
        ('ਚ c', 'ਛ ch', 'ਜ j', 'ਝ jh'),
        ('ਟ ṭ', 'ਠ ṭh', 'ਡ ḍ', 'ਢ ḍh'),
        ('ਤ t', 'ਥ th', 'ਦ d', 'ਧ dh'),
        ('ਪ p', 'ਫ ph', 'ਬ b', 'ਭ bh'),
        ('ਮ m', 'ਨ n', 'ਰ r', 'ਲ l'),
        ('ਸ s', 'ਹ h', 'ਵ v', 'ਯ y'),
    ]
    y = 276
    for row in cons:
        out += t(70, y, row[0], 'middle', 'L')
        out += t(180, y, row[1], 'middle', 'L')
        out += t(300, y, row[2], 'middle', 'L')
        out += t(410, y, row[3], 'middle', 'L')
        y += 18
    out += hr(406)
    out += sh(420, 'Numerals')
    nums = [('੦ 0','੧ 1','੨ 2','੩ 3','੪ 4'),('੫ 5','੬ 6','੭ 7','੮ 8','੯ 9')]
    y = 438
    for row in nums:
        x = 60
        for item in row:
            out += t(x, y, item, 'middle', 'L')
            x += 80
        y += 20
    out += hr(468)
    out += t(240, 484, 'Written right-to-left in Shahmukhi script (Urdu)', 'middle', 'X')
    out += t(240, 500, '(Pakistani Punjabi) · Gurmukhi used in India', 'middle', 'X')
    out += t(240, 516, '~100 million speakers (5th most spoken language)', 'middle', 'X')
    out += footer(53, 'Punjabi', 'a', 'Script · Gurmukhi Abugida')
    out += close_svg()
    return out

def build_53b():
    out = open_svg()
    out += t(240, 45, 'PUNJABI  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, 'ਧੁਨੀ ਵਿਗਿਆਨ  (Dhunī vigiyān)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Tonal System — 3 Tones')
    out += t(240, 112, 'Punjabi is one of the few Indo-Aryan tonal languages', 'middle', 'X')
    tones = [
        ('Level (mid)', 'ਕੋੜਾ  kōṛā', 'whip'),
        ('Rising', 'ਕੋੜਾ  kòṛā', 'leper'),
        ('Falling', 'ਕੋੜਾ  kôṛā', '40 (forty)'),
    ]
    y = 128
    for tone, ipa, gloss in tones:
        out += t(100, y, tone, 'end', 'L')
        out += t(200, y, ipa, 'middle', 'L')
        out += t(380, y, f'"{gloss}"', 'start', 'X')
        y += 18
    out += hr(178)
    out += sh(193, 'Tone Origin — Murmured Consonants')
    out += t(240, 210, 'Tones arose from loss of voiced aspirates (bh, dh, gh)', 'middle', 'X')
    out += t(240, 226, 'Preceding vowel developed compensatory tone contour', 'middle', 'X')
    out += hr(240)
    out += sh(256, 'Consonant Features')
    feats = [
        ('Aspirates:', 'kh, gh, ch, jh, ph, bh (breathy burst)'),
        ('Retroflex:', '\u1e6d \u1e6dh \u1e0d \u1e0dh — tongue tip curled back'),
        ('Nasals:', 'm n \u1e47 \u014b — place-assimilating'),
        ('Trill:', 'r = alveolar trill; \u1e5b = retroflex flap'),
        ('Sibilant:', 's — Punjabi lacks /z/ natively'),
    ]
    y = 274
    for label, val in feats:
        out += t(90, y, label, 'end', 'X')
        out += t(100, y, val, 'start', 'L')
        y += 18
    out += hr(368)
    out += sh(384, 'Vowels')
    out += t(240, 401, 'Short: a  i  u', 'middle', 'L')
    out += t(240, 419, 'Long:  \u0101  \u012b  \u016b  e  o  ai  au', 'middle', 'L')
    out += t(240, 437, 'Vowel length is phonemic (k\u0101l=time vs kal=yesterday)', 'middle', 'X')
    out += hr(450)
    out += sh(466, 'Nasalization')
    out += t(240, 483, 'Tippi ੰ and Bindi \u0a02 mark nasal vowels', 'middle', 'X')
    out += t(240, 499, '\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40  Pañjābī — \u0a70 marks nasalization', 'middle', 'L')
    out += footer(53, 'Punjabi', 'b', 'Phonology · Tones · Consonants')
    out += close_svg()
    return out

def build_53c():
    out = open_svg()
    out += t(240, 45, 'PUNJABI  GRAMMAR', 'middle', 'S')
    out += t(240, 65, 'ਵਿਆਕਰਣ  (Viākraṇ)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Word Order  SOV')
    out += t(240, 112, 'Subject → Object → Verb (like Hindi/Urdu)', 'middle', 'X')
    out += t(240, 128, '\u0a2e\u0a48\u0a02 \u0a2a\u0a3e\u0a23\u0a40 \u0a2a\u0a40\u0a02\u0a26\u0a3e \u0a39\u0a3e\u0a02', 'middle', 'L')
    out += t(240, 144, 'Maĩ pāṇī pīndā hāĩ — "I drink water"', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Postpositions')
    posts = [
        ('\u0a26\u0a3e / \u0a26\u0a40 / \u0a26\u0a47', 'dā/dī/de', 'of (gen., agrees w/ possessed)'),
        ('\u0a28\u0a42\u0a70 / \u0a15\u0a42', 'nū̃/kū', 'to, DATIVE/ACCUSATIVE'),
        ('\u0a24\u0a4b\u0a02', 'tō̃', 'from, ABLATIVE'),
        ('\u0a1a', 'ca', 'in, LOCATIVE (archaic; vich more common)'),
        ('\u0a35\u0a3f\u0a71\u0a1a', 'vich', 'in, inside'),
        ('\u0a28\u0a3e\u0a32', 'nāl', 'with, INSTRUMENTAL'),
    ]
    y = 190
    for pun, rom, gloss in posts:
        out += t(55, y, pun, 'middle', 'L')
        out += t(130, y, rom, 'middle', 'X')
        out += t(300, y, gloss, 'start', 'X')
        y += 17
    out += hr(305)
    out += sh(320, 'Verb Agreement')
    out += t(240, 337, 'Verbs agree with subject in gender and number', 'middle', 'X')
    out += t(240, 353, 'In perfective, verb agrees with OBJECT (ergative)', 'middle', 'X')
    out += t(240, 369, '\u0a2e\u0a41\u0a70\u0a21\u0a47 \u0a30\u0a4b\u0a1f\u0a40 \u0a16\u0a3e\u0a27\u0a40  (munde rotī khādhī)', 'middle', 'L')
    out += t(240, 385, '"The boy ate bread" — verb agrees w/ bread (f.)', 'middle', 'X')
    out += hr(398)
    out += sh(413, 'Core Vocabulary')
    vocab = [
        ('\u0a2a\u0a3e\u0a23\u0a40','pāṇī','water'),('\u0a30\u0a4b\u0a1f\u0a40','rotī','bread'),
        ('\u0a18\u0a30','ghar','house'),('\u0a2e\u0a3e\u0a02','māṃ','mother'),
        ('\u0a2a\u0a3f\u0a70\u0a21','piṇḍ','village'),('\u0a39\u0a3e\u0a02','hāṃ','yes'),
        ('\u0a28\u0a39\u0a40\u0a02','nahī̃','no'),('\u0a28\u0a3e\u0a2e','nām','name'),
    ]
    y = 430
    for i in range(0, len(vocab), 2):
        p1, r1, g1 = vocab[i]
        p2, r2, g2 = vocab[i+1]
        out += t(55, y, p1, 'middle', 'L')
        out += t(120, y, r1, 'middle', 'X')
        out += t(190, y, g1, 'middle', 'X')
        out += t(285, y, p2, 'middle', 'L')
        out += t(360, y, r2, 'middle', 'X')
        out += t(430, y, g2, 'middle', 'X')
        y += 18
    out += footer(53, 'Punjabi', 'c', 'Grammar · Postpositions · Ergativity')
    out += close_svg()
    return out

def build_53d():
    out = open_svg()
    out += t(240, 45, 'PUNJABI  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, 'ਲਿਖਤ ਅਤੇ ਪੁਲ', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'The Mul Mantar (Opening of Sri Guru Granth Sahib)')
    lines_g = [
        '\u0a07\u0a71\u0a15 \u0a13\u0a05\u0a02\u0a15\u0a3e\u0a30',
        '\u0a38\u0a24\u0a3f \u0a28\u0a3e\u0a2e\u0a41 \u0a15\u0a30\u0a24\u0a3e \u0a2a\u0a41\u0a30\u0a16\u0a41',
        '\u0a28\u0a3f\u0a30\u0a2d\u0a4c \u0a28\u0a3f\u0a30\u0a35\u0a48\u0a30\u0a41',
        '\u0a05\u0a15\u0a3e\u0a32 \u0a2e\u0a42\u0a30\u0a24\u0a3f \u0a05\u0a1c\u0a42\u0a28\u0a40',
    ]
    lines_r = [
        'Ikk Oankār',
        'Sat nām, kartā purakh',
        'Nirbhau, nirvair',
        'Akāl mūrat, ajūnī',
    ]
    lines_e = [
        'One Creator God',
        'True Name, the Creator Being',
        'Without fear, without enmity',
        'Timeless form, unborn',
    ]
    y = 112
    for g, r, e in zip(lines_g, lines_r, lines_e):
        out += t(240, y, g, 'middle', 'L')
        out += t(240, y+14, f'{r}  —  {e}', 'middle', 'X')
        y += 32
    out += hr(268)
    out += sh(284, 'Proverb')
    out += t(240, 300, '\u0a2c\u0a70\u0a26\u0a3e \u0a38\u0a4b\u0a1a \u0a35\u0a3f\u0a1a\u0a3e\u0a30 \u0a15\u0a47 \u0a1a\u0a71\u0a32\u0a26\u0a3e \u0a39\u0a48', 'middle', 'L')
    out += t(240, 316, 'Bandā soc vicār ke calldā hai', 'middle', 'X')
    out += t(240, 332, '"A person moves forward through thought and reflection"', 'middle', 'X')
    out += hr(346)
    out += sh(362, 'Bridge Phrase')
    out += t(240, 382, '\u0a07\u0a39 \u0a24\u0a41\u0a39\u0a3e\u0a21\u0a47 \u0a32\u0a08 \u0a2c\u0a23\u0a3e\u0a08 \u0a17\u0a08 \u0a38\u0a40,', 'middle', 'L')
    out += t(240, 398, '\u0a2e\u0a41\u0a2b\u0a3c\u0a24, \u0a09\u0a28 \u0a32\u0a4b\u0a15\u0a3e\u0a02 \u0a26\u0a41\u0a06\u0a30\u0a3e', 'middle', 'L')
    out += t(240, 414, '\u0a1c\u0a3f\u0a28\u0a4d\u0a39\u0a3e\u0a02 \u0a28\u0a47 \u0a05\u0a17\u0a47 \u0a5c\u0a3e\u0a70\u0a15\u0a47 \u0a35\u0a47\u0a16\u0a3f\u0a06\u0a4d', 'middle', 'L')
    out += t(240, 434, 'Ih tuhāḍe laī baṇāī gaī sī, muft,', 'middle', 'X')
    out += t(240, 450, 'un lokāṃ duārā jinhaṃ ne age ṛhāṃke vekhiā.', 'middle', 'X')
    out += t(240, 470, '"This was made for you, freely, by people', 'middle', 'X')
    out += t(240, 484, 'who remembered forward."', 'middle', 'X')
    out += hr(498)
    out += t(240, 515, 'Punjabi · ~100M speakers · Punjab region', 'middle', 'X')
    out += t(240, 531, 'India and Pakistan · Sikh sacred language', 'middle', 'X')
    out += footer(53, 'Punjabi', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate53a_punjabi_script.svg', build_53a()),
        ('plate53b_punjabi_phonology.svg', build_53b()),
        ('plate53c_punjabi_grammar.svg', build_53c()),
        ('plate53d_punjabi_text.svg', build_53d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
