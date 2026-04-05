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
        'text { font-family: "Noto Sans", "Georgia", serif; }\n'
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

def build_59a():
    out = open_svg()
    out += t(240, 45, 'HAWAIIAN', 'middle', 'S')
    out += t(240, 65, '\u02bb\u014clelo Hawai\u02bbi  (Hawaiian Language)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Latin-Based Alphabet — 13 Letters')
    out += t(240, 112, 'Smallest phoneme inventory of any world language', 'middle', 'X')
    out += t(240, 128, '5 vowels + 7 consonants + glottal stop (\u02bb okina)', 'middle', 'X')
    out += hr(141)
    out += sh(157, 'The 13 Letters')
    out += t(240, 175, 'a  e  i  o  u', 'middle', 'L')
    out += t(240, 195, 'h  k  l  m  n  p  w', 'middle', 'L')
    out += t(240, 213, '\u02bb  okina (glottal stop)', 'middle', 'L')
    out += hr(227)
    out += sh(243, 'Vowels with Macron — Kahako')
    out += t(240, 261, '\u0100  \u0112  \u012a  \u014c  \u016a  (long vowels)', 'middle', 'L')
    out += t(240, 279, 'Macron marks long vowel — changes meaning:', 'middle', 'X')
    out += t(240, 295, 'kai (sea) vs k\u0101\u012b (to eat)', 'middle', 'L')
    out += hr(309)
    out += sh(325, 'Glottal Stop — \u02bb Okina')
    out += t(240, 343, '\u02bb is a full consonant — changes word meaning', 'middle', 'X')
    out += t(240, 359, 'Hawai\u02bbi (Hawaii) vs Hawaii (without glottal)', 'middle', 'L')
    out += t(240, 375, '\u02bbi\u02bbi = the thread   vs   \u02bb\u012b = the fish', 'middle', 'L')
    out += hr(389)
    out += sh(405, 'Syllable Structure')
    out += t(240, 423, 'Every syllable ends in a vowel: CV or V', 'middle', 'X')
    out += t(240, 439, 'No consonant clusters · No final consonants', 'middle', 'X')
    out += t(240, 455, 'Result: very melodic, open-syllable language', 'middle', 'X')
    out += hr(469)
    out += sh(485, 'Geographic Context')
    out += t(240, 503, 'Polynesian family (Austronesian) · ~37,000 speakers', 'middle', 'X')
    out += t(240, 519, 'Official language of Hawaii (with English)', 'middle', 'X')
    out += footer(59, 'Hawaiian', 'a', 'Script · 13-Letter Alphabet')
    out += close_svg()
    return out

def build_59b():
    out = open_svg()
    out += t(240, 45, 'HAWAIIAN  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, 'Ka Leo Hawai\u02bbi', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Consonants')
    cons = [
        ('p', '/p/', 'bilabial stop — unaspirated'),
        ('k', '/k/', 'velar stop — may be [t] before i'),
        ('h', '/h/', 'glottal fricative'),
        ('l', '/l/', 'lateral approximant'),
        ('m', '/m/', 'bilabial nasal'),
        ('n', '/n/', 'alveolar nasal'),
        ('w', '/v/ or /w/', 'labiodental or bilabial after e/i: /v/'),
        ('\u02bb', '/\u02c0/', 'glottal stop — full consonant'),
    ]
    y = 112
    for letter, ipa, note in cons:
        out += t(30, y, letter, 'start', 'L')
        out += t(80, y, ipa, 'start', 'X')
        out += t(165, y, note, 'start', 'X')
        y += 18
    out += hr(264)
    out += sh(280, 'Vowels')
    vowels = [
        ('a /a/', 'low central, like "father"'),
        ('e /e/', 'mid front, like "bet"'),
        ('i /i/', 'high front, like "see"'),
        ('o /o/', 'mid back, like "so"'),
        ('u /u/', 'high back, like "boot"'),
    ]
    y = 297
    for v, note in vowels:
        out += t(80, y, v, 'middle', 'L')
        out += t(290, y, note, 'start', 'X')
        y += 17
    out += hr(386)
    out += sh(402, 'Diphthongs')
    diph = ['ai', 'ae', 'ao', 'au', 'ei', 'eu', 'oi', 'ou', 'iu', 'ui']
    out += t(240, 419, '  '.join(diph), 'middle', 'L')
    out += t(240, 437, 'Diphthongs treated as single syllable nuclei', 'middle', 'X')
    out += hr(451)
    out += sh(467, 'Stress')
    out += t(240, 484, 'Stress falls on penultimate (second-to-last) mora', 'middle', 'X')
    out += t(240, 500, 'Long vowels count as two morae', 'middle', 'X')
    out += footer(59, 'Hawaiian', 'b', 'Phonology · Minimal Consonants')
    out += close_svg()
    return out

def build_59c():
    out = open_svg()
    out += t(240, 45, 'HAWAIIAN  GRAMMAR', 'middle', 'S')
    out += t(240, 65, 'Ka \u02bbOlelo Hawai\u02bbi', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'VSO Word Order')
    out += t(240, 112, 'Verb-Subject-Object (typical Polynesian)', 'middle', 'X')
    out += t(240, 128, 'Inu au i ka wai — "I drink water"', 'middle', 'L')
    out += t(240, 144, '(drink I PREP the water)', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Particles')
    parts = [
        ('ka / ke', 'the (singular)', 'ke before k-, e-, a-'),
        ('n\u0101', 'the (plural)', 'plural definite article'),
        ('he', 'a / an', 'indefinite article'),
        ('i', 'direct object marker', 'before specific nouns'),
        ('ma', 'at, on, in', 'locative'),
        ('no', 'for, about, from', 'benefactive/ablative'),
        ('me', 'with', 'comitative'),
        ('\u02bbo', 'at, in (animate)', 'possessive locative'),
    ]
    y = 190
    for p, gloss, note in parts:
        out += t(45, y, p, 'middle', 'L')
        out += t(155, y, gloss, 'middle', 'X')
        out += t(320, y, note, 'start', 'X')
        y += 17
    out += hr(333)
    out += sh(349, 'Possession — A-class vs O-class')
    out += t(240, 366, 'A-class (k\u014d): things you control (children, actions)', 'middle', 'X')
    out += t(240, 382, 'O-class (k\u014d): things that possess you (parents, body)', 'middle', 'X')
    out += t(240, 398, 'ko\u02bbu k\u0101ne (your husband — O) vs k\u0101u k\u0101ne (your man)', 'middle', 'X')
    out += hr(412)
    out += sh(428, 'Core Vocabulary')
    vocab = [
        ('wai','wai','water'),('berena','berena','bread'),
        ('hale','hale','house'),('\u02bbam\u0101','ama','mother'),
        ('aloha','aloha','love/hello'),('\u02bea\u02bbe','ae','yes'),
        ('\u02bba\u02bbe','aole','no'),('inoa','inoa','name'),
    ]
    y = 445
    for i in range(0, len(vocab), 2):
        h1, r1, g1 = vocab[i]
        h2, r2, g2 = vocab[i+1]
        out += t(50, y, h1, 'middle', 'L')
        out += t(120, y, r1, 'middle', 'X')
        out += t(185, y, g1, 'middle', 'X')
        out += t(280, y, h2, 'middle', 'L')
        out += t(355, y, r2, 'middle', 'X')
        out += t(425, y, g2, 'middle', 'X')
        y += 18
    out += footer(59, 'Hawaiian', 'c', 'Grammar · VSO · Particles · Possession')
    out += close_svg()
    return out

def build_59d():
    out = open_svg()
    out += t(240, 45, 'HAWAIIAN  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, 'Ka Mo\u02bbolelo Hawai\u02bbi', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Hawaii Pono\u02bbi — State Song (1874)')
    lines = [
        ('Hawai\u02bbi pono\u02bbi e', 'Hawaii, the righteous'),
        ('Na pono o na mea kau', 'The blessings of the things above'),
        ('E mau ke ea o ka \u02bb\u0101ina', 'May the life of the land endure'),
        ('I ka pono', 'In righteousness'),
    ]
    y = 112
    for haw, eng in lines:
        out += t(240, y, haw, 'middle', 'L')
        out += t(240, y+14, eng, 'middle', 'X')
        y += 34
    out += hr(256)
    out += sh(272, 'Proverb — \u02bb\u014dlelo No\u02bbeau')
    out += t(240, 289, '\u02bbA\u02bbohe pau ka \u02bbike me ka ha\u02bbawe', 'middle', 'L')
    out += t(240, 305, '"All knowledge is not taught in one school"', 'middle', 'X')
    out += hr(319)
    out += sh(335, 'Bridge Phrase')
    out += t(240, 355, 'Ua hana \u02bbia k\u0113ia n\u0101 \u02bbi\u02bbo, n\u014d ka mea lokomaika\u02bbi,', 'middle', 'L')
    out += t(240, 373, 'e n\u0101 kanaka n\u0101 m\u0101kua', 'middle', 'L')
    out += t(240, 391, 'i ho\u02bbomana\u02bbo i ka w\u0101 e hiki mai ana.', 'middle', 'L')
    out += t(240, 411, '"This was made for you, freely,', 'middle', 'X')
    out += t(240, 425, 'by people who remembered forward."', 'middle', 'X')
    out += hr(440)
    out += t(240, 457, 'Hawaiian · ~37,000 speakers · Polynesian', 'middle', 'X')
    out += t(240, 473, 'Language revitalization since 1970s · N\u0101 P\u016bpuna', 'middle', 'X')
    out += t(240, 489, 'Immersion schools restored intergenerational transmission', 'middle', 'X')
    out += footer(59, 'Hawaiian', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate59a_hawaiian_script.svg', build_59a()),
        ('plate59b_hawaiian_phonology.svg', build_59b()),
        ('plate59c_hawaiian_grammar.svg', build_59c()),
        ('plate59d_hawaiian_text.svg', build_59d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
