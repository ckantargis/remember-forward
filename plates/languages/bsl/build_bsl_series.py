"""
build_bsl_series.py
British Sign Language (BSL) — plates 63A–63D
Run from repo root: python plates/languages/bsl/build_bsl_series.py
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'asl'))
from sign_lang_helpers import *

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = BASE

# BSL two-handed manual alphabet: letter -> (dominant hand shape, base hand shape, note)
BSL_ALPHA = [
    ('A', 'Index points at A side of base', 'Base: flat B hand; touch left side'),
    ('B', 'Index + middle point at base',   'Base: flat B; touch right side palm'),
    ('C', 'Index traces C on base',          'Base: flat B; touch left curve'),
    ('D', 'Index to base, arc',             'Base: flat B; tap right thumb/index'),
    ('E', 'All fingers extended, touch',    'Base: B; brush dorsal side'),
    ('F', 'All fingers and thumb together', 'Base: B; touch fingertips to base'),
    ('G', 'Index + thumb, touch base',      'Base: B; touch with G shape'),
    ('H', 'Index + middle, touch base',     'Base: B; touch with H shape'),
    ('I', 'Pinky touches base',             'Base: B; touch pinky to palm'),
    ('J', 'Pinky traces J on base',         'Base: B; motion letter'),
    ('K', 'Index + middle + thumb',         'Base: B; tap'),
    ('L', 'L-shape touches base',           'Base: B; touch thumb+index'),
    ('M', 'Three fingers on base palm',     'Base: B facing up; place 3 fingers'),
    ('N', 'Two fingers on base palm',       'Base: B facing up; place 2 fingers'),
    ('O', 'O-shape on base',               'Base: B; O touches palm'),
    ('P', 'Like K, pointing down',         'Base: B; tap'),
    ('Q', 'G-shape, pointing down',        'Base: B; tap'),
    ('R', 'Crossed index+middle',          'Base: B; touch crossed fingers'),
    ('S', 'Closed fist on base',           'Base: B facing up; fist rests on palm'),
    ('T', 'Thumb between i+m on base',     'Base: B; touch thumb between fingers'),
    ('U', 'Index + middle up on base',     'Base: B; tap two-finger tips'),
    ('V', 'V-shape on base',              'Base: B; V touches palm'),
    ('W', 'W-shape on base',             'Base: B; three fingers touch palm'),
    ('X', 'Hooked index on base',         'Base: B; hooked finger taps'),
    ('Y', 'Pinky + thumb extended',        'Base: B; touch with Y shape'),
    ('Z', 'Index traces Z on base',        'Base: B; motion letter'),
]

def build_63a():
    out = open_svg()
    out += t(240, 32, 'BRITISH SIGN LANGUAGE (BSL)', 'middle', 'T')
    out += t(240, 47, 'TWO-HANDED MANUAL ALPHABET \u00b7 HANDSHAPES \u00b7 SERIES 63A', 'middle', 'S')
    out += hr(55)

    out += t(240, 65, 'BSL is used by ~150,000 native signers in the United Kingdom. Although English is the', 'middle', 'Lx')
    out += t(240, 74, 'surrounding spoken language (as in the US), BSL and ASL are MUTUALLY UNINTELLIGIBLE \u2014', 'middle', 'Lx')
    out += t(240, 83, 'they are distinct languages. Only ~31% of signs are identical between BSL and ASL.', 'middle', 'Lx')
    out += hr(91, 0.3)

    # Two-handed vs one-handed comparison
    out += sh(98, 'TWO-HANDED VS ONE-HANDED FINGERSPELLING')
    y = 109
    comparison = [
        ('BSL', 'TWO-HANDED', 'Both hands used. Non-dominant (base) hand = passive platform; dominant hand = active.'),
        ('ASL', 'ONE-HANDED',  'Only dominant hand. Borrowed from LSF (French Sign Language) via Gallaudet 1817.'),
        ('LSF', 'ONE-HANDED',  'French Sign Language \u2014 ancestor of ASL; one-handed alphabet similar to ASL.'),
        ('Auslan', 'TWO-HANDED', 'Australian Sign Language shares BSL\u2019s two-handed alphabet; historically related.'),
    ]
    ccols = [36, 105, 165]
    for vals in comparison:
        for v, x in zip(vals, ccols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # BSL alphabet table
    out += sh(y, 'BSL TWO-HANDED ALPHABET \u2014 ALL 26 LETTERS')
    y += 10
    out += t(240, y, 'Base hand (non-dominant): flat B-hand, palm toward signer. Dominant hand makes active shape.', 'middle', 'Lx')
    y += 10

    # Draw BSL alphabet as a table (text-based since two hands don't fit in simple icon)
    COLS = 2
    col_w = 228
    for i, (ltr, active, base_note) in enumerate(BSL_ALPHA):
        col = i % COLS
        row = i // COLS
        cx_left = 36 + col * col_w
        ry = y + row * 9
        out += t(cx_left,      ry, ltr + ':',       'start', 'Ls')
        out += t(cx_left + 22, ry, active,           'start', 'Lx')

    y += ((len(BSL_ALPHA) + 1) // COLS) * 9 + 6

    out += hr(y+2, 0.3)
    y += 8

    # Key letter comparisons
    out += sh(y, 'BSL vs ASL: KEY DIFFERENCES IN FINGERSPELLING')
    y += 10
    diffs = [
        ('A\u2013Z general', 'Two-handed (both hands)', 'One-handed (dominant only)'),
        ('A',      'Index at left side of flat base',  'Closed fist, thumb on side'),
        ('B',      'Index+middle at right of base',    'Flat open hand, thumb across'),
        ('D',      'Index arc over base thumb',        'D-shape: index up, others bent'),
        ('G',      'Index+thumb pinch at base',        'Index+thumb pointing sideways'),
        ('I',      'Pinky touches base palm',          'Pinky only up, others in fist'),
        ('R',      'Crossed fingers tap base',         'Crossed index+middle, up'),
        ('Y',      'Pinky+thumb out, tap base',        'Shaka: pinky+thumb extended'),
    ]
    dcols = [36, 130, 295]
    dhdrs = ['Letter', 'BSL', 'ASL']
    for h, x in zip(dhdrs, dcols):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 9
    for row in diffs:
        for v, x in zip(row, dcols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9

    out += hr(y+4, 0.3)
    out += t(240, y+13, 'BASE HAND POSITIONS: Most BSL letters use flat B as base (palm in or palm up).', 'middle', 'Lx')
    out += t(240, y+22, 'For vowels (A, E, I, O, U), the dominant hand taps the matching finger on the base hand.', 'middle', 'Lx')

    out += footer('PLATE 63A', '63', 'BRITISH SIGN LANGUAGE', 'BSL \u00b7 UK \u00b7 ~150,000 NATIVE SIGNERS')
    out += close_svg()
    return out

def build_63b():
    out = open_svg()
    out += t(240, 32, 'BRITISH SIGN LANGUAGE (BSL)', 'middle', 'T')
    out += t(240, 47, 'PHONOLOGICAL PARAMETERS \u00b7 GRAMMAR OVERVIEW \u00b7 SERIES 63B', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'BSL PHONOLOGICAL PARAMETERS')
    y = 74
    out += t(36, y, 'BSL, like all sign languages, has a formal phonological structure with minimal pairs:', 'start', 'Lx')
    y += 10

    params = [
        ('HANDSHAPE', 'The shape of the hand(s); ~44 handshapes documented in BSL'),
        ('LOCATION',  'Where relative to the body: forehead/chin/chest/neutral space'),
        ('MOVEMENT',  'Direction, path, manner, and repetition of hand motion'),
        ('ORIENTATION','Palm direction: up, down, toward/away from signer, left/right'),
        ('NMS',       'Non-manual signals: facial expression, lip patterns, body position'),
    ]
    for param, desc in params:
        out += t(36,  y, param + ':', 'start', 'H')
        out += t(130, y, desc,         'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'BSL GRAMMAR: KEY FEATURES')
    y += 12
    gram_features = [
        ('WORD ORDER', 'SOV (subject-object-verb) is unmarked baseline in BSL,',
         'contrasting with ASL\u2019s SVO. Both allow topic-comment reordering.'),
        ('TOPIC-COMMENT', 'Topic established first (brow raise NMS), then comment.',
         'BOOK, ME READ  (The book, I read it)  \u2014 most natural BSL structure.'),
        ('NMS GRAMMAR', 'BSL relies more on body movement, less on facial expression than ASL.',
         'Shoulder shift, body lean, head tilt all carry grammatical meaning.'),
        ('LIP PATTERNS', 'BSL signers often mouth English words simultaneously.',
         'This is distinct from ASL and reflects different contact with English.'),
        ('NEGATION', 'Head shake + NEG sign, or head shake alone for short sentences.',
         'NOT, NEVER, NONE: distinct signs + head shake NMS.'),
        ('QUESTIONS', 'Y/N: brow raise; WH-: brow furrow (same as ASL).',
         'WHAT, WHERE, WHO, WHEN, WHY, HOW \u2014 at end of sentence.'),
    ]
    for feat, line1, line2 in gram_features:
        out += t(36, y, feat, 'start', 'H')
        y += 9
        out += t(50, y, line1, 'start', 'Lx')
        y += 8
        out += t(50, y, line2, 'start', 'Lx')
        y += 10
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'BSL vs ASL: MUTUAL UNINTELLIGIBILITY')
    y += 12
    mi_facts = [
        'Despite sharing English as the surrounding spoken language, BSL and ASL are distinct.',
        'Historical origin: BSL developed independently in Britain (18th\u201319th c.).',
        'ASL originated from LSF (French), brought to the US by Laurent Clerc in 1817.',
        'Lexical similarity: ~31% of signs identical; ~44% cognate (related but different).',
        'Both belong to different language families:',
        '  BSL family: BSL, Auslan (Australia), NZSL (New Zealand) \u2014 BANZSL group.',
        '  ASL family: ASL, LSF, many African, Middle Eastern, Asian sign languages.',
        'Contact signing: "Signed Supported English" (SSE) is a contact variety, not BSL.',
    ]
    for line in mi_facts:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += hr(y+2, 0.3)
    y += 8

    # Signing space
    out += sh(y, 'SIGNING SPACE & SPATIAL GRAMMAR')
    y += 12
    ss = [
        'BSL uses the same spatial grammar as ASL: referents assigned to locations,',
        'agreement verbs move between locations, classifiers represent object categories.',
        'The signing space is the area in front of the signer\u2019s body (roughly head to waist,',
        'shoulder-width to either side) \u2014 this space is the grammar.',
    ]
    for line in ss:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += footer('PLATE 63B', '63', 'BRITISH SIGN LANGUAGE', 'SOV \u00b7 BANZSL FAMILY \u00b7 NMS GRAMMAR')
    out += close_svg()
    return out

def build_63c():
    out = open_svg()
    out += t(240, 32, 'BRITISH SIGN LANGUAGE (BSL)', 'middle', 'T')
    out += t(240, 47, 'GRAMMAR DETAIL \u00b7 CLASSIFIER PREDICATES \u00b7 CORE VOCABULARY \u00b7 SERIES 63C', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'CORE VOCABULARY (BSL GLOSS)')
    y = 74
    vocab = [
        ('ME', 'index to chest'),             ('YOU', 'point at addressee'),
        ('NAME', 'N-hand at forehead'),        ('DEAF', 'index: ear to mouth'),
        ('HEARING', 'index circles at mouth'), ('SIGN', 'two index fingers circle'),
        ('UNDERSTAND', 'index taps forehead'), ('KNOW', 'flat hand at head'),
        ('SEE', 'V from eyes'),               ('LOOK-AT', 'V points forward'),
        ('GO', 'flat hand sweeps forward'),   ('COME', 'curve hand toward signer'),
        ('GIVE', 'palm up, extend forward'),  ('TAKE', 'palm down, draw back'),
        ('MAKE', 'fists rotate together'),    ('WANT', 'bent fingers draw toward'),
        ('LIKE', 'flat hand on chest, out'),  ('LOVE', 'crossed arms on chest'),
        ('GOOD', 'thumbs up'),                ('BAD', 'thumbs down'),
        ('FREE', 'wrists crossed, open out'), ('HELP', 'fist on palm, lift'),
        ('REMEMBER', 'A-hand temple fwd'),    ('FORWARD', 'flat hand push fwd'),
        ('PEOPLE', 'P-hands alternating'),    ('TOGETHER', 'both fists side by side'),
    ]
    vcols3 = [(36, 122), (196, 282), (346, 445)]
    per_col3 = (len(vocab) + 2) // 3
    for ci, (x1, x2) in enumerate(vcols3):
        chunk = vocab[ci*per_col3:(ci+1)*per_col3]
        cy3 = y
        for gloss, desc in chunk:
            out += t(x1, cy3, gloss, 'start', 'Ls')
            out += t(x2, cy3, desc,  'start', 'Lx')
            cy3 += 9
    y += max(per_col3, 1) * 9 + 8

    out += hr(y, 0.3)
    y += 8

    out += sh(y, 'CLASSIFIER PREDICATES IN BSL')
    y += 12
    bsl_cl = [
        ('CL:1',  'Person/upright object: single index = person standing/moving'),
        ('CL:V',  'Person moving: inverted V fingers walk forward = person walks'),
        ('CL:B',  'Flat surface: B-hand = floor, table, wall, road'),
        ('CL:C',  'Cylindrical/container: C-hand = cup, pipe, tree trunk'),
        ('CL:G',  'Thin flat object: index+thumb pinch = card, paper, book'),
        ('CL:3',  'Vehicle: 3-hand (thumb+index+middle) = car, lorry, bus'),
    ]
    for cl, desc in bsl_cl:
        out += t(36, y, cl,   'start', 'Ls')
        out += t(80, y, desc, 'start', 'Lx')
        y += 9

    out += hr(y+4, 0.3)
    y += 10

    out += sh(y, 'BSL REGIONAL VARIATION')
    y += 12
    reg = [
        'BSL has significant regional dialects across the UK:',
        'Northern England, Scotland, London, and Belfast variants may differ substantially',
        'in signs for common concepts (colours, numbers, days of week can vary by city).',
        'This is more pronounced than regional ASL variation.',
        'BBC "See Hear" programme and British Deaf Association use a prestige standard.',
        'There is no official written form of BSL; SignWriting and HamNoSys are used',
        'by researchers. BSL gained official language recognition in the UK in 2003.',
    ]
    for line in reg:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += hr(y+4, 0.3)
    y += 10

    out += sh(y, 'DEAF COMMUNITY & CULTURE')
    y += 12
    culture = [
        'BSL carries Deaf culture, identity, and heritage, not just communication.',
        'Deaf history: The first known British school for the Deaf was established 1760',
        '  by Thomas Braidwood in Edinburgh; his methods were kept secret from other educators.',
        'Oralism controversy: In the 1880 Milan Congress, oral methods were imposed on Deaf',
        '  education, suppressing sign languages for nearly a century. BSL survived informally.',
        'Current: BSL recognised as a language in 2003; GCSE BSL qualification introduced 2022.',
    ]
    for line in culture:
        out += t(36, y, line, 'start', 'Lx')
        y += 9

    out += footer('PLATE 63C', '63', 'BRITISH SIGN LANGUAGE', 'CLASSIFIERS \u00b7 REGIONAL VARIATION \u00b7 CULTURE')
    out += close_svg()
    return out

def build_63d():
    out = open_svg()
    out += t(240, 32, 'BRITISH SIGN LANGUAGE (BSL)', 'middle', 'T')
    out += t(240, 47, 'DISCOURSE \u00b7 BRIDGE PHRASE \u00b7 BSL vs ASL COMPARISON \u00b7 SERIES 63D', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'BRIDGE PHRASE IN BSL GLOSS')
    y = 74
    out += bx(36, y, 404, 16)
    out += t(240, y+12, 'THIS  MAKE  FOR-YOU  FREE  PEOPLE  REMEMBER  FORWARD', 'middle', 'Lg')
    y += 22
    out += t(240, y, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Lx')
    y += 12
    out += t(240, y, 'BSL gloss for this phrase is essentially identical to ASL gloss \u2014 the concepts align.', 'middle', 'Lx')
    y += 9
    out += t(240, y, 'The execution differs: BSL tends toward SOV, so: PEOPLE \u2192 THIS MAKE \u2192 FOR-YOU FREE REMEMBER FORWARD.', 'middle', 'Lx')
    out += hr(y+11, 0.3)
    y += 18

    out += sh(y, 'BSL SAMPLE DISCOURSE')
    y += 12
    disc = [
        ('LONG-AGO DOCUMENT THIS \u2013 MAKE  WHO?  PEOPLE',       'This document \u2014 who made it? People.'),
        ('PEOPLE WHY MAKE?  FUTURE YOU FIND',                    'Why did people make it? For you to find in the future.'),
        ('FREE GIVE YOU \u2013 LOVE REASON',                        'Given freely to you \u2014 out of love.'),
        ('REMEMBER FORWARD \u2013 PEOPLE OLD THIS MAKE',            'These people, in the past, remembered forward.'),
    ]
    for gloss, english in disc:
        out += bx(36, y, 404, 14)
        out += t(240, y+10, gloss, 'middle', 'Ls')
        y += 18
        out += t(240, y, english, 'middle', 'Lx')
        y += 11
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'BSL / ASL STRUCTURAL COMPARISON')
    y += 12
    comp = [
        ('Feature',          'BSL',                          'ASL'),
        ('Fingerspelling',   'Two-handed alphabet',          'One-handed alphabet (from LSF)'),
        ('Unmarked word order','SOV',                        'SVO'),
        ('NMS emphasis',     'Body movement, lip patterns',  'Facial expression dominant'),
        ('Language family',  'BANZSL (British, Auslan, NZ)', 'French SL family'),
        ('Official status',  'UK law 2003',                  'No federal law (Deaf Ed. Act 1975)'),
        ('Mutual intellig.', '31% identical signs',         '58% cognate with LSF'),
        ('Writing system',   'None standardized (SignWrit.)', 'None standardized (SignWrit.)'),
    ]
    ccols3 = [36, 145, 310]
    for i, row in enumerate(comp):
            c3 = 'H' if i == 0 else 'Lx'
            for v, x in zip(row, ccols3):
                out += t(x, y, v, 'start', c3)
            if i == 0: out += hr(y+3, 0.3)
            y += 9

    out += hr(y+4, 0.3)
    y += 8

    out += sh(y, 'NOTES ON WRITTEN BSL')
    y += 12
    wnotes = [
        'BSL has no universally accepted writing system. Three notation systems are used:',
        '1. GLOSS: Capital English words (as shown above) \u2014 used for linguistic analysis.',
        '2. SignWriting (Sutton): Visual featural script; Unicode block U+1D800\u2013U+1DAAF.',
        '   Font: Noto Sans SignWriting. Captures handshape, location, movement, orientation.',
        '3. HamNoSys: Hamburg Notation System \u2014 phonetic transcription for research.',
        '',
        'For a time capsule context: SignWriting is the most visually self-evident system',
        'and closest in spirit to this project\u2019s goal of cross-cultural readability.',
    ]
    for line in wnotes:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 63D', '63', 'BRITISH SIGN LANGUAGE', 'BRIDGE PHRASE \u00b7 BSL vs ASL')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate63a_bsl_manual_alphabet.svg', build_63a),
        ('plate63b_bsl_parameters.svg',      build_63b),
        ('plate63c_bsl_grammar.svg',         build_63c),
        ('plate63d_bsl_text.svg',            build_63d),
    ]
    for fname, fn in plates:
        path = os.path.join(OUT, fname)
        content = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK  {fname}  ({len(content)//1024} KB)')

if __name__ == '__main__':
    main()
