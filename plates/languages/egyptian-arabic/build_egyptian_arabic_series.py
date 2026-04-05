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
        'text { font-family: "Noto Naskh Arabic", "Noto Sans Arabic", serif; }\n'
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

def build_60a():
    out = open_svg()
    out += t(240, 45, 'EGYPTIAN ARABIC', 'middle', 'S')
    out += t(240, 65, '\u0639\u0627\u0645\u0650\u064a\u0629 \u0645\u0635\u0631\u064a\u0629  (Masri)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Arabic Script — Naskh Style')
    out += t(240, 112, 'Right-to-left cursive · 28 base letters', 'middle', 'X')
    out += t(240, 128, 'Each letter has 4 contextual forms: isolated/initial/medial/final', 'middle', 'X')
    out += t(240, 144, 'Egyptian Arabic is most-understood Arabic dialect globally', 'middle', 'X')
    out += hr(157)
    out += sh(173, 'Arabic Alphabet — 28 Letters')
    rows = [
        ('\u0627 alif', '\u0628 ba', '\u062a ta', '\u062b tha', '\u062c jeem'),
        ('\u062d ha', '\u062e kha', '\u062f dal', '\u0630 dhal', '\u0631 ra'),
        ('\u0632 zay', '\u0633 seen', '\u0634 sheen', '\u0635 suad', '\u0636 duad'),
        ('\u0637 tuah', '\u0638 zuah', '\u0639 ain', '\u063a ghain', '\u0641 fa'),
        ('\u0642 qaf', '\u0643 kaf', '\u0644 lam', '\u0645 meem', '\u0646 nun'),
        ('\u0647 ha', '\u0648 waw', '\u064a ya', '', ''),
    ]
    y = 192
    for row in rows:
        x = 50
        for item in row:
            if item:
                out += t(x, y, item, 'middle', 'L')
            x += 80
        y += 18
    out += hr(310)
    out += sh(326, 'Egyptian-Specific Letters')
    out += t(240, 343, '\u062c  = /g/ in Egyptian (not /d\u0292/ like Modern Standard)', 'middle', 'L')
    out += t(240, 359, '\u0642  = /\u02bc/ (glottal stop) in most Egyptian words', 'middle', 'L')
    out += t(240, 375, '\u062b  = /s/ in colloquial (not /\u03b8/)', 'middle', 'L')
    out += hr(390)
    out += sh(406, 'Diglossia')
    out += t(240, 423, 'Masri (spoken) vs Fusha (written formal Arabic)', 'middle', 'X')
    out += t(240, 439, 'Speakers switch registers by context', 'middle', 'X')
    out += t(240, 455, 'Most Egyptians understand 3+ Arabic varieties', 'middle', 'X')
    out += footer(60, 'Egyptian Arabic', 'a', 'Script · Arabic · Diglossia')
    out += close_svg()
    return out

def build_60b():
    out = open_svg()
    out += t(240, 45, 'EGYPTIAN ARABIC  PHONOLOGY', 'middle', 'S')
    out += t(240, 65, '\u0635\u0648\u062a\u064a\u0627\u062a  (Sawtiyaat)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Egyptian vs Classical Arabic Sounds')
    diffs = [
        ('MSA /q/', 'Masri /\u02bc/', 'qalb \u2192 \u02bca\u02bdb = heart'),
        ('MSA /\u03b8/', 'Masri /t/ or /s/', 'thal\u0101tha \u2192 tala\u02bda = three'),
        ('MSA /\u00f0/', 'Masri /z/ or /d/', 'dh\u0101hib \u2192 d\u0101hib = going'),
        ('MSA /d\u0292/', 'Masri /g/', 'jamal \u2192 gamal = camel'),
        ('MSA /x/', 'Masri /x/', 'shared — velar fricative'),
    ]
    y = 112
    for msa, masri, ex in diffs:
        out += t(100, y, msa, 'end', 'X')
        out += t(110, y, masri, 'start', 'L')
        out += t(285, y, ex, 'start', 'X')
        y += 18
    out += hr(210)
    out += sh(226, 'Pharyngeals and Emphatics')
    out += t(240, 243, '\u02bf  = voiced pharyngeal fricative (/\u02bf ain/) — unique', 'middle', 'L')
    out += t(240, 259, '\u0127  = voiceless pharyngeal fricative (/\u1e25 a/)', 'middle', 'L')
    out += t(240, 275, 'Emphatics: \u1e63 \u1e0d \u1e6d \u1e93 — pharyngealized consonants', 'middle', 'L')
    out += t(240, 291, 'Emphatics cause vowels to become back/low', 'middle', 'X')
    out += hr(305)
    out += sh(321, 'Vowels')
    out += t(240, 338, 'Short: a  i  u  (often reduced or deleted)', 'middle', 'X')
    out += t(240, 354, 'Long: \u0101  \u012b  \u016b', 'middle', 'X')
    out += t(240, 370, 'Diphthongs: ay  aw', 'middle', 'X')
    out += t(240, 386, 'Short vowels often not written in Arabic script', 'middle', 'X')
    out += hr(400)
    out += sh(416, 'Stress')
    out += t(240, 433, 'Stress falls on last heavy syllable (CVV or CVC)', 'middle', 'X')
    out += t(240, 449, 'Light syllables (CV) attract stress only if final', 'middle', 'X')
    out += footer(60, 'Egyptian Arabic', 'b', 'Phonology · Pharyngeals · Emphatics')
    out += close_svg()
    return out

def build_60c():
    out = open_svg()
    out += t(240, 45, 'EGYPTIAN ARABIC  GRAMMAR', 'middle', 'S')
    out += t(240, 65, '\u0642\u0648\u0627\u0639\u062f  (Qawaa\u02bfid)', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Word Order  SVO')
    out += t(240, 112, '\u0623\u0646\u0627 \u0628\u0634\u0631\u0628 \u0645\u064a\u0629', 'middle', 'L')
    out += t(240, 128, '\u02bcana bashrab mayya — "I drink water"', 'middle', 'X')
    out += hr(141)
    out += sh(157, 'Verb Conjugation')
    out += t(240, 174, 'Root system: 3-4 consonant roots + vowel patterns', 'middle', 'X')
    out += t(240, 190, 'k-t-b = writing: katab (wrote), yiktib (writes)', 'middle', 'X')
    conj = [
        ('\u0643\u062a\u0628\u062a', 'katabt', 'I wrote'),
        ('\u0643\u062a\u0628\u062a', 'katabt', 'you (m.) wrote'),
        ('\u0643\u062a\u0628', 'katab', 'he wrote'),
        ('\u0643\u062a\u0628\u062a', 'katabit', 'she wrote'),
        ('\u0643\u062a\u0628\u0646\u0627', 'katabna', 'we wrote'),
    ]
    y = 206
    for ar, rom, gloss in conj:
        out += t(65, y, ar, 'middle', 'L')
        out += t(150, y, rom, 'middle', 'X')
        out += t(285, y, gloss, 'start', 'X')
        y += 16
    out += hr(296)
    out += sh(312, 'Dual and Plural')
    out += t(240, 329, 'Dual suffix: -\u0301\u014dn (2 of something)', 'middle', 'X')
    out += t(240, 345, 'Sound plural: -\u012bn (m.) / -\u0101t (f.)', 'middle', 'X')
    out += t(240, 361, 'Broken plural: internal vowel change (most common)', 'middle', 'X')
    out += t(240, 377, 'k\u012btab (book) \u2192 kutub (books)', 'middle', 'L')
    out += hr(391)
    out += sh(407, 'Core Vocabulary')
    vocab = [
        ('\u0645\u064a\u0629','mayya','water'),('\u0639\u064a\u0634','eesh','bread'),
        ('\u0628\u064a\u062a','beet','house'),('\u0645\u0645\u0627','mama','mother'),
        ('\u0635\u0627\u062d\u0628','saahib','friend'),('\u0622\u0647','aah','yes'),
        ('\u0644\u0623','la\u02bc','no'),('\u0627\u0633\u0645','esm','name'),
    ]
    y = 424
    for i in range(0, len(vocab), 2):
        a1, r1, g1 = vocab[i]
        a2, r2, g2 = vocab[i+1]
        out += t(50, y, a1, 'middle', 'L')
        out += t(115, y, r1, 'middle', 'X')
        out += t(180, y, g1, 'middle', 'X')
        out += t(275, y, a2, 'middle', 'L')
        out += t(350, y, r2, 'middle', 'X')
        out += t(425, y, g2, 'middle', 'X')
        y += 18
    out += footer(60, 'Egyptian Arabic', 'c', 'Grammar · Roots · Broken Plurals')
    out += close_svg()
    return out

def build_60d():
    out = open_svg()
    out += t(240, 45, 'EGYPTIAN ARABIC  TEXT  &  BRIDGE', 'middle', 'S')
    out += t(240, 65, '\u0646\u0635 \u0648\u062c\u0633\u0631', 'middle', 'T')
    out += hr(78)
    out += sh(95, 'Umm Kulthum — Al-Atlal (1966)')
    out += t(240, 112, '\u0625\u0639\u0637\u0646\u064a \u062d\u0631\u064a\u062a\u064a \u0623\u0637\u0644\u0642\u0646\u064a', 'middle', 'L')
    out += t(240, 128, '\u0625\u0639\u0637\u0646\u064a \u0648\u0644\u0627 \u062a\u0638\u0644\u0645\u0646\u064a', 'middle', 'L')
    out += t(240, 144, '\u02bcITni Huriyyati, aTliqni', 'middle', 'X')
    out += t(240, 160, '\u02bcITni wala tazlimni', 'middle', 'X')
    out += t(240, 176, '"Give me my freedom, release me / Give it to me and wrong me not"', 'middle', 'X')
    out += hr(190)
    out += sh(206, 'Proverb')
    out += t(240, 223, '\u0627\u0644\u0644\u064a \u0645\u0627\u064a\u0639\u0631\u0641\u0634 \u064a\u062a\u0639\u0644\u0645', 'middle', 'L')
    out += t(240, 239, 'Illi mayifarafsh, yitallam', 'middle', 'X')
    out += t(240, 255, '"He who does not know — let him learn"', 'middle', 'X')
    out += hr(269)
    out += sh(285, 'Bridge Phrase')
    out += t(240, 305, '\u062f\u0627 \u0639\u0645\u0644\u0648\u0647 \u0639\u0634\u0627\u0646\u0643, \u0628\u062c\u062f \u0648 \u0645\u062c\u0627\u0646\u0627\u064b,', 'middle', 'L')
    out += t(240, 321, '\u0645\u0646 \u0646\u0627\u0633 \u0641\u0627\u0643\u0631\u064a\u0646 \u0641\u064a \u0627\u0644\u0645\u0633\u062a\u0642\u0628\u0644.', 'middle', 'L')
    out += t(240, 341, 'Da \u02bfamalooh \u02bfash\u0101nak, bi-gadd wi-magaanan,', 'middle', 'X')
    out += t(240, 357, 'min naas faakriyn fi l-mustaqbal.', 'middle', 'X')
    out += t(240, 375, '"This was made for you, for real and for free,', 'middle', 'X')
    out += t(240, 389, 'by people who were thinking of the future."', 'middle', 'X')
    out += hr(404)
    out += sh(420, 'Series Complete — 60 Languages')
    out += t(240, 437, 'Egyptian Arabic · ~100M speakers · North Africa', 'middle', 'X')
    out += t(240, 453, 'Most widely understood Arabic dialect globally', 'middle', 'X')
    out += t(240, 469, 'Through film, music, and television since 1930s', 'middle', 'X')
    out += t(240, 489, 'PLATE 60 OF 60  ·  REMEMBER FORWARD', 'middle', 'S')
    out += footer(60, 'Egyptian Arabic', 'd', 'Text · Bridge Phrase · Series Complete')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate60a_egyptian_arabic_script.svg', build_60a()),
        ('plate60b_egyptian_arabic_phonology.svg', build_60b()),
        ('plate60c_egyptian_arabic_grammar.svg', build_60c()),
        ('plate60d_egyptian_arabic_text.svg', build_60d()),
    ]
    for fname, content in plates:
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
