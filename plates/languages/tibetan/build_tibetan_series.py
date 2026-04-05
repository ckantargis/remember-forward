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
        'text { font-family: "Noto Serif Tibetan", "Noto Sans Tibetan", serif; }\n'
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

def build_56a():
    out = open_svg()
    out += t(240, 45, 'TIBETAN', 'middle', 'S')
    out += t(240, 65, '\u0f56\u0f7c\u0f51\u0f0b\u0f66\u0f90\u0f51\u0f0b  (Bod skad)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Uchen Script — Dbu-can')
    out += t(240, 112, '"Uchen" = headed/upright · the formal print style', 'middle', 'X')
    out += t(240, 128, 'Derived from Brahmi via Gupta script · ~620 CE', 'middle', 'X')
    out += t(240, 144, 'Abugida: consonants stack vertically, vowels are diacritics', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Consonants — 30 Radicals')
    cons = [
        ('\u0f40 ka', '\u0f41 kha', '\u0f42 ga', '\u0f44 nga'),
        ('\u0f45 ca', '\u0f46 cha', '\u0f47 ja', '\u0f49 nya'),
        ('\u0f4f ta', '\u0f50 tha', '\u0f51 da', '\u0f53 na'),
        ('\u0f54 pa', '\u0f55 pha', '\u0f56 ba', '\u0f58 ma'),
        ('\u0f5f tsa', '\u0f60 wa', '\u0f61 zha', '\u0f62 ra'),
        ('\u0f63 la', '\u0f64 sha', '\u0f66 sa', '\u0f67 ha'),
        ('\u0f68 a', '\u0f0b tsek', '\u0f0d shad', '\u0f01 yig mgo'),
    ]
    y = 190
    for row in cons:
        out += t(70, y, row[0], 'middle', 'L')
        out += t(180, y, row[1], 'middle', 'L')
        out += t(300, y, row[2], 'middle', 'L')
        out += t(410, y, row[3], 'middle', 'L')
        y += 18
    out += hr(334)
    out += sh(350, 'Vowel Diacritics')
    out += t(240, 367, '\u0f71 aa  \u0f72 i  \u0f74 u  \u0f7a e  \u0f7c o', 'middle', 'L')
    out += t(240, 385, 'Written above or below the base consonant', 'middle', 'X')
    out += hr(398)
    out += sh(414, 'Stacking')
    out += t(240, 431, 'Consonant clusters stack vertically:', 'middle', 'X')
    out += t(240, 449, '\u0f66\u0f90\u0f62\u0f0b (sgra) = sound — s+g+r stacked', 'middle', 'L')
    out += t(240, 467, 'Superscript and subscript positions defined by tradition', 'middle', 'X')
    out += footer(56, 'Tibetan', 'a', 'Script · Uchen · Stacking')
    out += close_svg()
    return out

def build_56b():
    out = open_svg()
    out += t(240, 45, 'TIBETAN  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, '\u0f66\u0f92\u0fb2\u0f0b\u0f51\u0f56\u0f5e\u0f71\u0f53\u0f0b  (sgra dbyangs)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Classical vs Spoken Tibetan')
    out += t(240, 112, 'Classical script preserves archaic spelling', 'middle', 'X')
    out += t(240, 128, 'Modern Lhasa dialect dropped many consonants', 'middle', 'X')
    out += t(240, 144, 'Written "bkra shis" — pronounced "Trashi"', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Tonal System — Lhasa Dialect')
    out += t(240, 190, 'Two tones: HIGH and LOW (from earlier voicing contrast)', 'middle', 'X')
    tones = [
        ('High', 'from voiceless onset consonants'),
        ('Low', 'from voiced/preaspirated onset consonants'),
        ('High rising', 'short syllables on high tone'),
        ('Low falling', 'long syllables on low tone'),
    ]
    y = 206
    for tone, note in tones:
        out += t(110, y, tone, 'end', 'L')
        out += t(120, y, note, 'start', 'X')
        y += 17
    out += hr(284)
    out += sh(300, 'Initial Consonants')
    out += t(240, 317, 'Lhasa: /p t k ts/ voiceless, aspiration contrastive', 'middle', 'X')
    out += t(240, 333, 'Voiced stops of Classical: merged or tonal in spoken', 'middle', 'X')
    out += t(240, 349, 'Pre-nasalization (nga, na) survives in some dialects', 'middle', 'X')
    out += hr(362)
    out += sh(378, 'Vowels — Lhasa')
    out += t(240, 395, 'a  i  u  e  o  plus \u025b (open-e) and \u00f8', 'middle', 'X')
    out += t(240, 411, 'Vowel length is contrastive', 'middle', 'X')
    out += hr(424)
    out += sh(440, 'Dialects')
    out += t(240, 457, 'Lhasa (prestige) · Kham · Amdo · Ladakhi', 'middle', 'X')
    out += t(240, 473, 'Dzongkha (Bhutan) is closely related', 'middle', 'X')
    out += footer(56, 'Tibetan', 'b', 'Phonology · Tones · Dialects')
    out += close_svg()
    return out

def build_56c():
    out = open_svg()
    out += t(240, 45, 'TIBETAN  GRAMMAR', 'middle', 'S')
    out += t(240, 65, '\u0f56\u0f62\u0f9c\u0f0b\u0f51\u0f42\u0f0b  (brjod dgos)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Word Order  SOV')
    out += t(240, 112, '\u0f44\u0f0b\u0f66\u0f72\u0f66\u0f0b\u0f46\u0f74\u0f0b\u0f42\u0f66\u0f72\u0f53\u0f0b\u0f61\u0f7c\u0f51\u0f0b', 'middle', 'L')
    out += t(240, 128, 'Nga si chu gyinyor yod — "I am drinking water"', 'middle', 'X')
    out += hr(141)
    out += sh(157, 'Case Particles')
    cases = [
        ('\u0f42\u0f72', 'gi / i', 'GENITIVE — possessive'),
        ('\u0f63\u0f0b / \u0f62\u0f0b', 'la / ra', 'DATIVE/LOCATIVE — to, at, for'),
        ('\u0f53\u0f66\u0f0b', 'nas', 'ABLATIVE — from, by'),
        ('\u0f66\u0f0b', 's', 'AGENTIVE (ergative) — marks agent'),
        ('\u0f51\u0f44\u0f0b', 'dang', 'COMITATIVE — with, and'),
    ]
    y = 174
    for tib, rom, gloss in cases:
        out += t(50, y, tib, 'middle', 'L')
        out += t(130, y, rom, 'middle', 'X')
        out += t(295, y, gloss, 'start', 'X')
        y += 18
    out += hr(268)
    out += sh(284, 'Evidentiality')
    out += t(240, 301, 'Tibetan marks HOW the speaker knows information:', 'middle', 'X')
    evid = [
        ('\u0f61\u0f7c\u0f51', 'yod', 'direct knowledge (I know from experience)'),
        ('\u0f62\u0f7a\u0f51', "red", 'reported/general fact'),
        ('\u0f66\u0f7a\u0f0b\u0f66\u0f94', 'se song', 'inferential (I deduce)'),
    ]
    y = 317
    for tib, rom, gloss in evid:
        out += t(55, y, tib, 'middle', 'L')
        out += t(120, y, rom, 'middle', 'X')
        out += t(270, y, gloss, 'start', 'X')
        y += 18
    out += hr(374)
    out += sh(390, 'Core Vocabulary')
    vocab = [
        ('\u0f45\u0f74', 'chu', 'water'),('\u0f56\u0f42\u0f62\u0f9a', 'bagru', 'bread'),
        ('\u0f41\u0f72\u0f58', 'khyim', 'house'),('\u0f68\u0f58\u0f0b\u0f63\u0f42\u0f66', 'a-ma', 'mother'),
        ('\u0f38\u0f7c\u0f51', 'chos', 'dharma/teaching'),('\u0f63\u0f42\u0f66', 'lags', 'yes (honorific)'),
        ('\u0f58\u0f72\u0f53', 'min', 'no/not'),('\u0f58\u0f72\u0f44', 'ming', 'name'),
    ]
    y = 406
    for i in range(0, len(vocab), 2):
        t1, r1, g1 = vocab[i]
        t2, r2, g2 = vocab[i+1]
        out += t(50, y, t1, 'middle', 'L')
        out += t(115, y, r1, 'middle', 'X')
        out += t(180, y, g1, 'middle', 'X')
        out += t(275, y, t2, 'middle', 'L')
        out += t(350, y, r2, 'middle', 'X')
        out += t(430, y, g2, 'middle', 'X')
        y += 18
    out += footer(56, 'Tibetan', 'c', 'Grammar · Cases · Evidentiality')
    out += close_svg()
    return out

def build_56d():
    out = open_svg()
    out += t(240, 45, 'TIBETAN  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, '\u0f66\u0f90\u0f51\u0f0b\u0f46\u0f71', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Om Mani Padme Hum')
    out += t(240, 120, '\u0f00\u0f58\u0f0b\u0f58\u0f23\u0f72\u0f0b\u0f54\u0f51\u0f0b\u0f58\u0f7a\u0f0d', 'middle', 'L')
    out += t(240, 142, 'om ma-ni pad-me hum', 'middle', 'X')
    out += t(240, 158, '"The jewel in the lotus" — most recited mantra', 'middle', 'X')
    out += t(240, 174, 'Engraved on mani stones throughout Tibet and Ladakh', 'middle', 'X')
    out += hr(188)
    out += sh(204, 'Tibetan Proverb')
    out += t(240, 221, '\u0f51\u0f42\u0f7c\u0f53\u0f0b\u0f54\u0f0b\u0f62\u0f44\u0f0b\u0f63\u0f58\u0f0b\u0f61\u0f7c\u0f51\u0f0d', 'middle', 'L')
    out += t(240, 237, 'dgon pa rang lam yod', 'middle', 'X')
    out += t(240, 253, '"Every monastery has its own path"', 'middle', 'X')
    out += hr(267)
    out += sh(283, 'Bridge Phrase')
    out += t(240, 303, '\u0f51\u0f72\u0f0b\u0f46\u0f74\u0f44\u0f0b\u0f41\u0f7c\u0f0b\u0f40\u0f71\u0f0b\u0f56\u0f63\u0f66\u0f56\u0f66\u0f0b', 'middle', 'L')
    out += t(240, 321, '\u0f54\u0f62\u0f64\u0f71\u0f0b\u0f58\u0f7a\u0f51\u0f0b\u0f60\u0f56\u0f61\u0f74\u0f44\u0f0b\u0f5e\u0f62\u0f0b\u0f40\u0f61\u0f71\u0f53', 'middle', 'L')
    out += t(240, 339, '\u0f51\u0f7a\u0f0b\u0f44\u0f71\u0f0b\u0f66\u0f71\u0f62\u0f0b\u0f56\u0f63\u0f66\u0f56\u0f66\u0f0b\u0f61\u0f7c\u0f51\u0f0d', 'middle', 'L')
    out += t(240, 361, 'Di khyong kho kā blas bas,', 'middle', 'X')
    out += t(240, 377, 'par shad med par, khyod rnams kyi chan', 'middle', 'X')
    out += t(240, 393, 'de nā sāra blas bas yod.', 'middle', 'X')
    out += t(240, 411, '"This was made for you, freely, by people', 'middle', 'X')
    out += t(240, 425, 'who remembered forward."', 'middle', 'X')
    out += hr(440)
    out += t(240, 457, 'Tibetan · ~6M native speakers · Sino-Tibetan family', 'middle', 'X')
    out += t(240, 473, 'Tibetan Plateau · language of Vajrayana Buddhism', 'middle', 'X')
    out += footer(56, 'Tibetan', 'd', 'Text · Bridge Phrase · Context')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate56a_tibetan_script.svg', build_56a()),
        ('plate56b_tibetan_phonology.svg', build_56b()),
        ('plate56c_tibetan_grammar.svg', build_56c()),
        ('plate56d_tibetan_text.svg', build_56d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
