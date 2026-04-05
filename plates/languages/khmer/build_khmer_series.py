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
        'text { font-family: "Noto Serif Khmer", "Noto Sans Khmer", serif; }\n'
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

def build_58a():
    out = open_svg()
    out += t(240, 45, 'KHMER', 'middle', 'S')
    out += t(240, 65, '\u1797\u17b6\u179f\u17b6\u1781\u17d2\u1798\u17c2\u179a  (Phiasaa Khmaer)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Khmer Script')
    out += t(240, 112, 'Oldest dated inscription in mainland SE Asia: 611 CE', 'middle', 'X')
    out += t(240, 128, 'Abugida: consonants carry inherent vowel /a/ or /\u0254/', 'middle', 'X')
    out += t(240, 144, 'Two registers: first series (voiced) and second series', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Consonants — First Series (a-register)')
    cons1 = [
        ('\u1780 k', '\u1781 kh', '\u1782 g', '\u1783 gh'),
        ('\u1784 ng', '\u1785 c', '\u1786 ch', '\u1787 j'),
        ('\u1788 jh', '\u1789 ny', '\u178a d', '\u178b t'),
    ]
    y = 190
    for row in cons1:
        out += t(70, y, row[0], 'middle', 'L')
        out += t(180, y, row[1], 'middle', 'L')
        out += t(300, y, row[2], 'middle', 'L')
        out += t(410, y, row[3], 'middle', 'L')
        y += 18
    out += hr(250)
    out += sh(265, 'Consonants — Continued')
    cons2 = [
        ('\u178c th', '\u178d d', '\u178e dh', '\u178f n'),
        ('\u1790 p', '\u1791 ph', '\u1792 b', '\u1793 bh'),
        ('\u1794 m', '\u1799 y', '\u179a r', '\u179b l'),
        ('\u179c v', '\u179f s', '\u17a0 h', '\u17a1 l'),
    ]
    y = 282
    for row in cons2:
        out += t(70, y, row[0], 'middle', 'L')
        out += t(180, y, row[1], 'middle', 'L')
        out += t(300, y, row[2], 'middle', 'L')
        out += t(410, y, row[3], 'middle', 'L')
        y += 18
    out += hr(360)
    out += sh(376, 'Independent Vowels')
    vowels = '\u17a2 \u17a3 \u17a4 \u17a5 \u17a6 \u17a7 \u17a8 \u17a9 \u17aa \u17ab \u17ac \u17ad \u17ae \u17af \u17b0 \u17b1 \u17b2 \u17b3'
    out += t(240, 394, vowels, 'middle', 'L')
    out += hr(410)
    out += sh(426, 'Subscript Consonants')
    out += t(240, 443, 'Consonant clusters use subscript (coeng) forms', 'middle', 'X')
    out += t(240, 459, 'Written below the base consonant', 'middle', 'X')
    out += footer(58, 'Khmer', 'a', 'Script · Abugida · Two Registers')
    out += close_svg()
    return out

def build_58b():
    out = open_svg()
    out += t(240, 45, 'KHMER  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, '\u179f\u1784\u17d2\u1782\u17b9\u178f\u179f\u17d2\u178f\u179a  (sangkhetsathar)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Register System')
    out += t(240, 112, 'Each consonant belongs to one of two series:', 'middle', 'X')
    out += t(240, 128, '1st series: consonant + inherent vowel /a/', 'middle', 'X')
    out += t(240, 144, '2nd series: consonant + inherent vowel /\u0254/', 'middle', 'X')
    out += t(240, 160, 'Same vowel diacritic = different sound by register', 'middle', 'X')
    out += hr(174)
    out += sh(190, 'Initial Consonants')
    out += t(240, 207, 'Khmer lost voiced/voiceless distinction historically', 'middle', 'X')
    out += t(240, 223, 'Replaced by register contrast in vowel quality', 'middle', 'X')
    out += t(240, 239, 'Modern: /k kh p ph t th c ch m n ng/ etc.', 'middle', 'X')
    out += hr(253)
    out += sh(269, 'Vowels')
    out += t(240, 286, 'Rich vowel system: ~30 vowel sounds', 'middle', 'X')
    out += t(240, 302, 'Short/long pairs + diphthongs + register variants', 'middle', 'X')
    vowels = [
        ('a / \u0259', 'aa / \u0268\u0259', 'i / \u026a', '\u012b / \u0268\u026a'),
        ('u / \u028a', '\u016b / \u0268\u028a', 'e / \u025b', 'ei / \u026a\u025b'),
        ('ae / a\u025b', 'ao / ao', 'oa / \u0254\u0259', 'ua / \u0268\u0259'),
    ]
    y = 318
    for row in vowels:
        out += t(60, y, row[0], 'middle', 'X')
        out += t(175, y, row[1], 'middle', 'X')
        out += t(300, y, row[2], 'middle', 'X')
        out += t(415, y, row[3], 'middle', 'X')
        y += 18
    out += hr(378)
    out += sh(394, 'No Tones')
    out += t(240, 411, 'Khmer is NOT tonal (unlike Thai and Vietnamese)', 'middle', 'X')
    out += t(240, 427, 'Rhythm is iambic: weak + STRONG syllable pairs', 'middle', 'X')
    out += hr(441)
    out += sh(457, 'Stress')
    out += t(240, 474, 'Stress falls on final syllable of a word', 'middle', 'X')
    out += t(240, 490, 'Minor syllables (presyllables) are unstressed', 'middle', 'X')
    out += footer(58, 'Khmer', 'b', 'Phonology · Register · Vowels')
    out += close_svg()
    return out

def build_58c():
    out = open_svg()
    out += t(240, 45, 'KHMER  GRAMMAR', 'middle', 'S')
    out += t(240, 65, '\u179c\u17b9\u1799\u17b6\u1780\u179a\u178e\u17cd  (veyiakorn)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Analytic Language  ·  SVO  Order')
    out += t(240, 112, '\u1781\u17d2\u1789\u17bb\u1798 \u1795\u17b9\u1780 \u178f\u17b9\u1780', 'middle', 'L')
    out += t(240, 128, 'Khnhom phik teuk — "I drink water"', 'middle', 'X')
    out += hr(141)
    out += sh(157, 'No Inflection')
    out += t(240, 174, 'Khmer has NO grammatical inflection:', 'middle', 'X')
    out += t(240, 190, 'No verb conjugation · No noun declension', 'middle', 'X')
    out += t(240, 206, 'No grammatical gender · No tense markers on verbs', 'middle', 'X')
    out += t(240, 222, 'Tense conveyed by time words and aspect particles', 'middle', 'X')
    out += hr(236)
    out += sh(252, 'Particles and Auxiliaries')
    parts = [
        ('\u1794\u17b6\u1793', 'baan', 'past/ability marker'),
        ('\u1793\u17b9\u1784', 'neung', 'future marker'),
        ('\u1780\u1798\u17d2\u1796\u17bb\u1784', 'kampung', 'progressive aspect'),
        ('\u17a0\u17be\u1799', 'haei', 'already/completion'),
        ('\u178f\u17be', 'teh', 'negation (sentence-final)'),
    ]
    y = 269
    for khm, rom, gloss in parts:
        out += t(65, y, khm, 'middle', 'L')
        out += t(140, y, rom, 'middle', 'X')
        out += t(290, y, gloss, 'start', 'X')
        y += 18
    out += hr(363)
    out += sh(379, 'Classifiers')
    out += t(240, 396, 'Nouns take classifiers when counted:', 'middle', 'X')
    out += t(240, 412, '\u1798\u1793\u17bb\u179f\u17d2\u179f\u1796\u17b8\u179a \u1798\u17d2\u1793\u17b6\u1780 (person: mneak)', 'middle', 'L')
    out += t(240, 428, '\u179f\u178f\u17d2\u179c \u1780\u1794\u17b6\u179b (animal: kbal)', 'middle', 'L')
    out += hr(442)
    out += sh(458, 'Core Vocabulary')
    vocab = [
        ('\u178f\u17b9\u1780','teuk','water'),('\u1793\u17c6\u1794\u17b6\u1789','nambang','bread'),
        ('\u1796\u17d0\u1780','pteah','house'),('\u1798\u17d0\u1791\u17b6\u1799','madaay','mother'),
        ('\u1794\u17b6\u1791','\u1794\u17b6\u1791','friend'),('\u1794\u17b6\u178f\u17ba','baateu','yes'),
        ('\u17a2\u178f\u17b8','atei','no'),('\u1785\u17d2\u1798\u17d2\u17a2\u17c2\u179f','chmaaes','name'),
    ]
    y = 474
    for i in range(0, len(vocab), 2):
        k1, r1, g1 = vocab[i]
        k2, r2, g2 = vocab[i+1]
        out += t(50, y, k1, 'middle', 'L')
        out += t(115, y, r1, 'middle', 'X')
        out += t(185, y, g1, 'middle', 'X')
        out += t(280, y, k2, 'middle', 'L')
        out += t(355, y, r2, 'middle', 'X')
        out += t(430, y, g2, 'middle', 'X')
        y += 18
    out += footer(58, 'Khmer', 'c', 'Grammar · Analytic · Particles')
    out += close_svg()
    return out

def build_58d():
    out = open_svg()
    out += t(240, 45, 'KHMER  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, '\u179f\u17d2\u178f\u17b9\u1796\u1796\u17b6\u179f\u17b6\u1781\u17d2\u1798\u17c2\u179a', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Cpap (Khmer classical verse code)')
    out += t(240, 112, '\u1780\u17bc\u1793\u1787\u17b6\u178f\u17b7\u1780\u1798\u17d2\u1798\u1780\u17a2\u17d2\u1793\u1780\u1787\u17b6\u178f\u17b7\u179f\u17d2\u179a\u17b8', 'middle', 'L')
    out += t(240, 128, 'Kun jaat kami ka anak jaat sri', 'middle', 'X')
    out += t(240, 144, '"Know your origin, know your birth status"', 'middle', 'X')
    out += t(240, 160, 'From the Cpap Srei — code of conduct for women', 'middle', 'X')
    out += hr(174)
    out += sh(190, 'Proverb')
    out += t(240, 207, '\u178f\u17d2\u179c\u17b6\u1799\u178f\u17d2\u179a\u1780\u17b6\u179b\u1780\u17d0\u179a\u1798\u17b9\u1793\u17b6\u1793\u178f\u17d2\u179c\u17b6\u1799', 'middle', 'L')
    out += t(240, 223, 'The great tree gives shade to all below it', 'middle', 'X')
    out += hr(237)
    out += sh(253, 'Bridge Phrase')
    out += t(240, 273, '\u178e\u17be\u179f\u17be\u179c\u17d2\u179c\u17b6\u178f\u17d2\u179c\u17bc\u178f\u179f\u1798\u17d2\u179a\u17b6\u1794\u17cb\u17a2\u1793\u1780,', 'middle', 'L')
    out += t(240, 291, '\u178f\u17c2\u1794\u17d0\u179a\u1793\u17cb\u1782\u17b7\u178f\u1787\u1793', 'middle', 'L')
    out += t(240, 309, '\u178a\u17be\u179b\u1793\u17b9\u1780\u1793\u17bb\u179c\u17d0\u1793\u1793\u17b6\u1780\u17c6\u179b\u1784\u1798\u17bb\u1781\u1793\u17b9\u1784\u178f.',  'middle', 'L')
    out += t(240, 331, 'Nih tveu sraap neak, doy mein kic,', 'middle', 'X')
    out += t(240, 347, 'dael prak nit jn', 'middle', 'X')
    out += t(240, 363, 'del neuk nuov vean neak kmleng muk neung t.', 'middle', 'X')
    out += t(240, 381, '"This was made for you, freely, by people', 'middle', 'X')
    out += t(240, 395, 'who remembered forward."', 'middle', 'X')
    out += hr(410)
    out += t(240, 427, 'Khmer · ~16M speakers · Cambodia (official)', 'middle', 'X')
    out += t(240, 443, 'Austroasiatic family · oldest SE Asian script', 'middle', 'X')
    out += footer(58, 'Khmer', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate58a_khmer_script.svg', build_58a()),
        ('plate58b_khmer_phonology.svg', build_58b()),
        ('plate58c_khmer_grammar.svg', build_58c()),
        ('plate58d_khmer_text.svg', build_58d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
