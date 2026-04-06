"""
build_csl_series.py
Chinese Sign Language (CSL / ZGS — Zhongguo Shouyu) — plates 65A–65D
Run from repo root: python plates/languages/csl/build_csl_series.py
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'asl'))
from sign_lang_helpers import *

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = BASE

def build_65a():
    out = open_svg()
    out += t(240, 32, 'CHINESE SIGN LANGUAGE (CSL / ZGS)', 'middle', 'T')
    out += t(240, 47, '\u4e2d\u56fd\u624b\u8bed (Zh\u014dnggu\u00f3 Sh\u01d2uy\u01d4) \u00b7 MANUAL ALPHABET \u00b7 SERIES 65A', 'middle', 'S')
    out += hr(55)

    out += t(240, 65, 'Chinese Sign Language is the world\'s largest sign language by number of users:', 'middle', 'Lx')
    out += t(240, 74, 'approximately 20 million signers in the People\'s Republic of China. CSL developed', 'middle', 'Lx')
    out += t(240, 83, 'independently of Western sign languages and reflects Chinese linguistic and cultural context.', 'middle', 'Lx')
    out += hr(91, 0.3)

    # CSL fingerspelling (pinyin-based)
    out += sh(98, 'CSL FINGERSPELLING \u2014 PINYIN-BASED SYSTEM (1963)')
    y = 109
    out += t(240, y, 'The official CSL fingerspelling scheme, adopted December 1963, is based on Pinyin romanization.', 'middle', 'Lx')
    y += 9
    out += t(240, y, '21 initials (声母 sh\u0113ngm\u01d4) and 6 finals (韵母 y\u00f9nm\u01d4) are represented by handshapes.', 'middle', 'Lx')
    y += 9
    out += t(240, y, 'Consonant clusters ZH, CH, SH, NG are treated as single signs (reflecting Mandarin phonemics).', 'middle', 'Lx')
    out += hr(y+11, 0.3)
    y += 18

    # Pinyin initials table
    out += sh(y, 'PINYIN INITIALS \u2014 CSL HANDSHAPES (SELECTED)')
    y += 10
    initials = [
        ('b', 'Index+thumb press together (like \u201cb\u201d bilabial closure)'),
        ('p', 'Similar to b, with slight puff (aspiration gesture)'),
        ('m', 'Three fingers pressed to lips (nasal resonance)'),
        ('f', 'Teeth-on-lip shape \u2014 upper teeth on lower lip hint'),
        ('d', 'One finger tap (dental stop)'),
        ('t', 'Like d, aspiration indicated'),
        ('n', 'One finger at nostril (nasal)'),
        ('l', 'Tongue-tip gesture (lateral)'),
        ('g', 'Open hand, velar approximation'),
        ('k', 'Open hand, aspiration'),
        ('h', 'Open hand at throat (glottal/velar)'),
        ('j', 'Index+middle crossed (palatal gesture)'),
        ('q', 'Like j with different tension'),
        ('x', 'Index+middle side (palatal fricative)'),
        ('zh','Curved hand (retroflex \u2014 curled tongue)'),
        ('ch','Like zh, with aspiration'),
        ('sh','Curved hand (retroflex fricative)'),
        ('r', 'Curved fingers (retroflex liquid)'),
        ('z', 'Flat hand (alveolar affricate)'),
        ('c', 'Like z, aspiration'),
        ('s', 'Flat hand (alveolar fricative)'),
    ]
    icols = [(36, 60), (240, 264)]
    half = len(initials) // 2
    for i, (initial, desc) in enumerate(initials):
        col = 0 if i < half else 1
        row = i if i < half else i - half
        cx1, cx2 = icols[col]
        ry = y + row * 8
        out += t(cx1, ry, initial + ':', 'start', 'Ls')
        out += t(cx2,  ry, desc, 'start', 'Lx')
    y += half * 8 + 4
    out += hr(y, 0.3)
    y += 8

    # Chinese writing in the air
    out += sh(y, 'WRITING IN THE AIR (\u7a7a\u5199 K\u014dngxi\u011b)')
    y += 12
    air_write = [
        'A distinctive feature of CSL: signers trace Chinese characters in the air with the index finger.',
        'Called \u7a7a\u5199 (k\u014dng xi\u011b, "air writing") \u2014 used when a specific character is needed.',
        'Stroke order follows standard Chinese character stroke order.',
        'This is unique to Chinese-context sign languages and has no equivalent in ASL/BSL/LSF.',
        'Numbers 1\u201310 in CSL can be signed with one hand (unlike ASL which needs two for 6\u201310).',
    ]
    for line in air_write:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += footer('PLATE 65A', '65', 'CHINESE SIGN LANGUAGE (CSL)', '\u4e2d\u56fd\u624b\u8bed \u00b7 ~20,000,000 SIGNERS \u00b7 PINYIN FINGERSPELLING')
    out += close_svg()
    return out

def build_65b():
    out = open_svg()
    out += t(240, 32, 'CHINESE SIGN LANGUAGE (CSL / ZGS)', 'middle', 'T')
    out += t(240, 47, 'PARAMETERS \u00b7 GRAMMAR \u00b7 CHINESE CULTURAL FEATURES \u00b7 SERIES 65B', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'CSL PHONOLOGICAL PARAMETERS')
    y = 74
    for param, desc in [
        ('HANDSHAPE (\u624b\u578b)', 'Numerous handshapes; Chinese character forms influence iconic shapes'),
        ('LOCATION (\u4f4d\u7f6e)',  'Body zones similar to other sign languages; neutral space widely used'),
        ('MOVEMENT (\u52a8\u4f5c)', 'Path, direction, internal (finger/wrist); tone-related movement exists'),
        ('ORIENTATION (\u671d\u5411)','Palm direction carries grammatical distinctions'),
        ('NMS (\u975e\u624b\u52a8\u4fe1\u53f7)',  'Facial expression + mouthing of Mandarin words common'),
    ]:
        out += t(36,  y, param + ':', 'start', 'H')
        out += t(175, y, desc,         'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'CSL GRAMMAR')
    y += 12
    gram = [
        ('WORD ORDER', 'SOV (subject-object-verb) is the unmarked order in CSL,',
         'reflecting influence of Chinese grammatical structure.'),
        ('TOPIC-COMMENT', 'Topic established first (like Mandarin topic-comment structure).',
         'Close parallel to Mandarin\u2019s own topic-prominent grammar.'),
        ('SPATIAL GRAMMAR', 'Agreement verbs, classifier predicates, and spatial referencing',
         'are used (universal features of natural sign languages).'),
        ('CLASSIFIERS', 'CSL classifier system reflects Chinese noun categories:',
         'flat objects, round objects, vehicles, persons, animals, etc.'),
        ('HONORIFICS', 'Distinct signs for kinship terms (older/younger sibling, etc.)',
         'reflecting Chinese cultural distinctions absent in English-based SLs.'),
        ('MOUTHING', 'Mandarin mouthing (lip-syncing Chinese words) is common in CSL,',
         'more so than English mouthing in ASL. Part of CSL\u2019s contact with Mandarin.'),
    ]
    for feat, l1, l2 in gram:
        out += t(36, y, feat, 'start', 'H')
        y += 9
        out += t(50, y, l1, 'start', 'Lx')
        y += 8
        out += t(50, y, l2, 'start', 'Lx')
        y += 11
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'CHINESE CULTURAL FEATURES IN CSL')
    y += 12
    cult = [
        'KINSHIP TERMS: CSL has distinct signs for elder/younger brother and sister,',
        '  reflecting Chinese kinship system (unlike ASL\u2019s generic BROTHER/SISTER).',
        'NUMBER SYSTEM: CSL can sign 1\u201310 on one hand using a compact system:',
        '  1\u20135 = fingers up; 6 = pinky+thumb; 7 = three middle fingers; 8 = index+middle;',
        '  9 = hooked index; 10 = fist with thumb alongside (or crossed index-pinky).',
        'CHINESE CHARACTER HANDSHAPES: Some CSL signs are iconic to Chinese character forms.',
        '  Example: The sign for PERSON (\u4eba r\u00e9n) resembles the character \u4eba (two strokes meeting).',
        '  Example: MOUNTAIN (\u5c71 sh\u0101n) \u2014 three fingers up, mimicking the character.',
        'REGIONAL VARIATION: CSL varies significantly between regions; Shanghai SL and',
        '  Beijing SL have different signs for many common concepts.',
    ]
    for line in cult:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 65B', '65', 'CHINESE SIGN LANGUAGE (CSL)', 'SOV \u00b7 CHINESE CULTURAL FEATURES')
    out += close_svg()
    return out

def build_65c():
    out = open_svg()
    out += t(240, 32, 'CHINESE SIGN LANGUAGE (CSL / ZGS)', 'middle', 'T')
    out += t(240, 47, 'CORE VOCABULARY \u00b7 BRIDGE PHRASE \u00b7 SERIES 65C', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'BRIDGE PHRASE IN CSL GLOSS')
    y = 74
    out += bx(36, y, 404, 16)
    out += t(240, y+12, '\u8fd9  \u5236\u4f5c  \u4e3a-\u4f60  \u514d\u8d39  \u4eba\u4eec  \u8bb0\u5f97  \u524d\u8fdb', 'middle', 'Lg')
    y += 22
    out += bx(36, y, 404, 14)
    out += t(240, y+10, 'ZH\u00c8  ZH\u00ccZU\u00d2  W\u00c8I-N\u01d0  MI\u01ceNF\u00c8I  R\u00c9NMEN  J\u00ccDE  QI\u00c1NJ\u00ccN', 'middle', 'Ls')
    y += 20
    out += t(240, y, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Lx')
    y += 12

    gloss_items = [
        ('\u8fd9 ZH\u00c8', 'this/this one'),
        ('\u5236\u4f5c ZH\u00ccZU\u00d2', 'to make/create'),
        ('\u4e3a\u4f60 W\u00c8IN\u01d0', 'for-you (directed)'),
        ('\u514d\u8d39 MI\u01ceNF\u00c8I', 'free of charge'),
        ('\u4eba\u4eec R\u00c9NMEN', 'people (plural)'),
        ('\u8bb0\u5f97 J\u00ccDE', 'to remember'),
        ('\u524d\u8fdb QI\u00c1NJ\u00ccN', 'forward/advance'),
    ]
    cw = 57
    for i, (char_py, desc) in enumerate(gloss_items):
        gx = 36 + i * cw
        if gx + cw > 452: break
        out += t(gx + cw//2, y,    char_py, 'middle', 'Ls')
        out += t(gx + cw//2, y+8,  desc,    'middle', 'Lx')
    y += 22
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'LINGUISTIC NOTES')
    y += 12
    notes = [
        '\u524d\u8fdb (qi\u00e1nj\u00ecn, "forward/advance"): compound of \u524d (qi\u00e1n, forward/front) + \u8fdb (j\u00ecn, advance/move).',
        'The spatial metaphor of future-as-forward is identical in Chinese and English.',
        '\u8bb0\u5f97 (j\u00ecde, "remember"): literally \u8bb0 "record/note" + \u5f97 "obtain/get" = internalize as memory.',
        '\u4e3a\u4f60 (w\u00e8i n\u01d0): preposition \u4e3a (for/on behalf of) + \u4f60 (you) = spatial benefactive.',
        'CSL would sign this in SOV-influenced order: PEOPLE THIS MAKE FOR-YOU FREE',
        'REMEMBER FORWARD \u2014 slightly different from ASL\'s SVO gloss.',
    ]
    for line in notes:
        out += t(36, y, line, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'CORE VOCABULARY (CSL GLOSS)')
    y += 12
    vocab = [
        ('\u6211 W\u014e (ME)',    'index to chest'),
        ('\u4f60 N\u01d0 (YOU)',  'index to addressee'),
        ('\u4eba R\u00c9N (PERSON)', 'two fingers, meet like \u4eba'),
        ('\u540d\u5b57 (NAME)',   'N at forehead'),
        ('\u804b\u624b\u8bed',   'two indices circle (SIGN)'),
        ('\u660e\u767d (UNDERSTAND)', 'index taps forehead'),
        ('\u77e5\u9053 (KNOW)',  'flat B at forehead'),
        ('\u770b (SEE)',          'V from eyes forward'),
        ('\u7ed9 G\u011bI (GIVE)', 'palm up, extend'),
        ('\u53d6 Q\u01d4 (TAKE)', 'claw hand, draw back'),
        ('\u505a ZU\u00d2 (MAKE)', 'fists rotate'),
        ('\u514d\u8d39 (FREE)',  'wrists cross, open'),
        ('\u8bb0 J\u00cc (REMEMBER)', 'A-hand temple fwd'),
        ('\u524d\u8fdb (FORWARD)', 'flat hand push fwd'),
        ('\u4eba\u4eec (PEOPLE)', 'P-hands alternate'),
        ('\u5c71 SH\u0100N (MOUNTAIN)', '3 fingers up, like \u5c71'),
        ('\u5929 TI\u0100N (SKY/DAY)', 'index overhead'),
        ('\u6c34 SHU\u01d0 (WATER)',  'W at lips'),
        ('\u706b HU\u01d2 (FIRE)',    'rising flame gesture'),
        ('\u7231 \u00c0I (LOVE)',     'crossed arms on chest'),
    ]
    vcols = [(36, 148), (246, 358)]
    per_col = (len(vocab) + 1) // 2
    for ci, (x1, x2) in enumerate(vcols):
        cy2 = y
        for gloss, desc in vocab[ci*per_col:(ci+1)*per_col]:
            out += t(x1, cy2, gloss, 'start', 'Ls')
            out += t(x2, cy2, desc,  'start', 'Lx')
            cy2 += 9

    out += footer('PLATE 65C', '65', 'CHINESE SIGN LANGUAGE (CSL)', 'BRIDGE PHRASE \u00b7 CORE VOCABULARY')
    out += close_svg()
    return out

def build_65d():
    out = open_svg()
    out += t(240, 32, 'CHINESE SIGN LANGUAGE (CSL / ZGS)', 'middle', 'T')
    out += t(240, 47, 'CSL DISCOURSE \u00b7 NUMBERS \u00b7 REGIONAL VARIATION \u00b7 SERIES 65D', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'CSL NUMBER SYSTEM (ONE-HANDED)')
    y = 74
    out += t(240, y, 'CSL can represent 1\u201310 on one hand \u2014 a unique feature reflecting Chinese cultural efficiency.', 'middle', 'Lx')
    y += 10
    numbers = [
        ('1', 'Index finger up'),
        ('2', 'Index + middle up (V)'),
        ('3', 'Thumb + index + middle up'),
        ('4', 'Four fingers up (no thumb)'),
        ('5', 'Open hand, all 5 extended'),
        ('6', 'Pinky + thumb extended (shaka-like)'),
        ('7', 'Thumb + index + middle together (touching)'),
        ('8', 'Index + middle extended, thumb out'),
        ('9', 'Index finger hooked/bent'),
        ('10','Index finger pointing, wrist twist (or crossed index+pinky)'),
    ]
    ncols = [(36, 110), (246, 320)]
    half = len(numbers) // 2
    for i, (n, desc) in enumerate(numbers):
        col = 0 if i < half else 1
        row = i if i < half else i - half
        cx1, cx2 = ncols[col]
        ry = y + row * 9
        out += t(cx1, ry, n + ':', 'start', 'Ls')
        out += t(cx2, ry, desc,    'start', 'Lx')
    y += half * 9 + 6
    out += hr(y, 0.3)
    y += 8

    out += sh(y, 'REGIONAL VARIATION IN CSL')
    y += 12
    regional = [
        'CSL varies significantly between regions. Beijing SL and Shanghai SL differ',
        'substantially and are sometimes considered separate dialects or related languages.',
        '',
        'Standardization efforts began in the 1950s but regional variation persists.',
        'The official CSL dictionary (first published 1987) has helped standardize some signs.',
        '',
        'Examples of regional variation:',
        '  MONDAY: Beijing uses one sign; Shanghai uses a different handshape.',
        '  COLORS: Red, green, blue may be signed differently across provinces.',
        '  NUMBERS 6\u201310: One-handed vs two-handed variants exist by region.',
    ]
    for line in regional:
        out += t(36, y, line, 'start', 'Lx')
        y += 8
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'CSL AND DEAF EDUCATION IN CHINA')
    y += 12
    edu = [
        'Deaf education in China dates to the early 20th century (1898, first Deaf school).',
        'Like elsewhere, oralism dominated for much of the 20th century.',
        'Current: bilingual-bicultural education (Mandarin + CSL) increasingly adopted.',
        'China Disabled Persons\u2019 Federation oversees Deaf education policy.',
        'CSL Research Center at Nanjing Normal University is the primary research body.',
        '',
        'DEAF POPULATION: China has ~27 million deaf/hard-of-hearing persons,',
        'making it the world\u2019s largest Deaf population in absolute numbers.',
        'Of these, ~20 million are estimated to use CSL as a primary language.',
    ]
    for line in edu:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'CSL SAMPLE DISCOURSE')
    y += 12
    disc = [
        ('THIS  DOCUMENT  IMPORTANT  KEEP', 'This document is important \u2014 keep it.'),
        ('PEOPLE  PAST  MAKE  FOR-YOU  FREE', 'People in the past made it for you, freely.'),
        ('REMEMBER  FORWARD  \u2014  MEANING  WHAT?', 'What does "remembered forward" mean?'),
        ('CARE  FUTURE  PEOPLE  \u2014  THAT  MEANING', 'It means to care about future people.'),
    ]
    for gloss, english in disc:
        out += bx(36, y, 404, 14)
        out += t(240, y+10, gloss, 'middle', 'Ls')
        y += 18
        out += t(240, y, english, 'middle', 'Lx')
        y += 11

    out += footer('PLATE 65D', '65', 'CHINESE SIGN LANGUAGE (CSL)', 'NUMBERS \u00b7 REGIONAL VARIATION \u00b7 DISCOURSE')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate65a_csl_manual_alphabet.svg', build_65a),
        ('plate65b_csl_grammar.svg',         build_65b),
        ('plate65c_csl_vocabulary.svg',      build_65c),
        ('plate65d_csl_discourse.svg',       build_65d),
    ]
    for fname, fn in plates:
        path = os.path.join(OUT, fname)
        content = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK  {fname}  ({len(content)//1024} KB)')

if __name__ == '__main__':
    main()
