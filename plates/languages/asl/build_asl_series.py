"""
build_asl_series.py
American Sign Language (ASL) — plates 62A–62D
Run from repo root: python plates/languages/asl/build_asl_series.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from sign_lang_helpers import *

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = BASE

# ── Plate 62A — Manual Alphabet & Script ─────────────────────────────────────
def build_62a():
    out = open_svg()
    out += t(240, 32, 'AMERICAN SIGN LANGUAGE (ASL)', 'middle', 'T')
    out += t(240, 47, 'MANUAL ALPHABET \u00b7 HANDSHAPE INVENTORY \u00b7 SERIES 62A', 'middle', 'S')
    out += hr(55)

    # What sign languages are
    out += t(240, 65, 'Sign languages are complete natural human languages \u2014 not codes for spoken languages.', 'middle', 'Lx')
    out += t(240, 74, 'ASL is the primary language of Deaf communities in the United States and Canada.', 'middle', 'Lx')
    out += t(240, 83, 'c. 500,000 native signers. Descended from French Sign Language (LSF) via Gallaudet/Clerc, 1817.', 'middle', 'Lx')
    out += hr(91, 0.3)

    # Manual alphabet
    out += sh(98, 'ASL ONE-HANDED MANUAL ALPHABET (FINGERSPELLING)')
    out += t(240, 108, 'Each letter = a handshape used to spell out names, technical terms, or unknown signs.', 'middle', 'Lx')

    alpha_svg, next_y = draw_asl_alphabet(30, 115, cell_w=31, cell_h=44)
    out += alpha_svg

    out += hr(next_y + 2, 0.3)

    # Handshape inventory categories
    out += sh(next_y + 9, 'HANDSHAPE INVENTORY CATEGORIES')
    out += t(240, next_y + 20, 'ASL uses ~50 distinct handshapes. Key categories:', 'middle', 'Lx')
    y = next_y + 28

    hs_cats = [
        ('OPEN HAND',   'All fingers extended: B (flat), 5 (spread)'),
        ('CLOSED/FIST', 'A (fist), S (knuckles over thumb), E (bent)'),
        ('SELECTED',    'Specific fingers: G/L/D (index), I/Y (pinky), V/K (two)'),
        ('BENT',        'Curved fingers: C, O, F (circle), X (hook)'),
        ('COMPOUND',    'Complex: T (thumb between), R (crossed), W (three spread)'),
    ]
    for cat, desc in hs_cats:
        out += t(36, y, cat + ':',  'start', 'H')
        out += t(110, y, desc, 'start', 'Lx')
        y += 9

    out += hr(y + 3, 0.3)

    # Numbers 1-10
    out += sh(y + 10, 'NUMBERS 1\u201310 (COMPACT REFERENCE)')
    y += 20
    nums = [
        ('1', 'Index up'),
        ('2', 'V/peace'),
        ('3', 'Thumb+idx+mid'),
        ('4', '4 fingers up'),
        ('5', 'Open 5-spread'),
        ('6', 'Pinky+thumb touch'),
        ('7', 'Ring+thumb touch'),
        ('8', 'Mid+thumb touch'),
        ('9', 'Idx+thumb circle'),
        ('10', 'Fist, thumb up, shake'),
    ]
    ncol = 5
    nw = 408 // ncol
    for i, (n, desc) in enumerate(nums):
        nx = 36 + (i % ncol) * nw
        ny = y + (i // ncol) * 18
        out += t(nx, ny,     n,    'start', 'Ls')
        out += t(nx + 14, ny, desc, 'start', 'Lx')

    y += (((len(nums)-1) // ncol) + 1) * 18 + 4
    out += hr(y, 0.3)
    out += t(240, y+10, 'J and Z are motion letters: the handshape traces the letter in space. Shown above with motion dots.', 'middle', 'Lx')
    out += t(240, y+20, 'SignWriting notation (Unicode U+1D800\u2013U+1DAAF) provides a complete written form for signs.', 'middle', 'Lx')

    out += footer('PLATE 62A', '62', 'AMERICAN SIGN LANGUAGE', 'ASL \u00b7 USA / CANADA \u00b7 ~500,000 NATIVE SIGNERS')
    out += close_svg()
    return out

# ── Plate 62B — Phonological Parameters ──────────────────────────────────────
def build_62b():
    out = open_svg()
    out += t(240, 32, 'AMERICAN SIGN LANGUAGE (ASL)', 'middle', 'T')
    out += t(240, 47, 'PHONOLOGICAL PARAMETERS \u00b7 THE 5 CHEREMES \u00b7 SERIES 62B', 'middle', 'S')
    out += hr(55)

    out += t(240, 65, 'Like spoken languages, sign languages have "phonology" \u2014 a system of minimal units.', 'middle', 'Lx')
    out += t(240, 74, 'In sign languages these are called CHEREMES (Stokoe 1960). Changing one parameter', 'middle', 'Lx')
    out += t(240, 83, 'changes the meaning, just as changing a phoneme does in spoken language.', 'middle', 'Lx')
    out += hr(91, 0.3)

    # 5 parameter boxes in 2 rows
    params = [
        ('1. HANDSHAPE (DEZ)', 'Dez \u2014 Designator', [
            '~50 distinct handshapes in ASL',
            'Ex: MOTHER vs FATHER differ only',
            '  in handshape (5-spread vs A-fist)',
            'Most semantically loaded parameter',
        ]),
        ('2. LOCATION (TAB)', 'Tab \u2014 Tabula', [
            '12 major signing-space zones',
            'Head, face, neck, chest, abdomen,',
            '  waist, upper/lower arm, wrist,',
            '  dominant/non-dominant hand',
        ]),
        ('3. MOVEMENT (SIG)', 'Sig \u2014 Signation', [
            'Path: arc, straight, circular',
            'Direction: up/down, in/out, across',
            'Manner: smooth, tense, repeated',
            'Internal: finger wiggle, wrist twist',
        ]),
        ('4. PALM ORIENTATION', 'Orientation of palm face', [
            'Up, down, in (toward signer),',
            '  out (away from signer),',
            '  left, right',
            'GIVE: palm up vs TAKE: palm down',
        ]),
        ('5. NON-MANUAL SIGNALS', 'NMS \u2014 Face + body', [
            'Facial expressions: brow raise/furrow',
            'Mouth morphemes, eye gaze, head tilt',
            'YES/NO question: brow raise + eye widen',
            'WH- question: brow furrow + head tilt',
        ]),
    ]

    bw, bh = 194, 95
    pad = 10
    positions = [(36, 100), (242, 100), (36, 202), (242, 202), (36, 304)]

    for (bx_pos, by_pos), (label, sub, items) in zip(positions, params):
        out += param_diagram(bx_pos, by_pos, bw, bh, label, sub, items)

    out += hr(410, 0.3)

    # Minimal pairs
    out += sh(417, 'MINIMAL PAIRS (ONE PARAMETER DIFFERS)')
    y = 428
    pairs = [
        ('MOTHER / FATHER', 'Location', 'Both: 5-spread hand, tapping cheek vs chin'),
        ('APPLE / CANDY',   'Location', 'X-hand at cheek (A) vs at chin (C)'),
        ('KNOW / FEEL',     'Handshape', 'Flat B at forehead (K) vs curved 5 at chest (F)'),
        ('BORROW / LEND',   'Direction', 'Same handshape+location; movement toward/away signer'),
        ('SAY / TALK',      'Repetition', 'One movement (SAY) vs repeated (TALK)'),
    ]
    pcols = [36, 165, 255]
    hdrs = ['Pair', 'Param.', 'Description']
    for h, x in zip(hdrs, pcols):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 10
    for pair, param, desc in pairs:
        for v, x in zip([pair, param, desc], pcols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9

    out += hr(y+4, 0.3)
    out += t(240, y+13, 'SIMULTANEITY: Sign languages can express multiple parameters AT ONCE (simultaneous morphology).', 'middle', 'Lx')
    out += t(240, y+22, 'A single sign can encode subject, object, aspect, and classifier in one articulation.', 'middle', 'Lx')

    out += footer('PLATE 62B', '62', 'AMERICAN SIGN LANGUAGE', 'STOKOE NOTATION \u00b7 5 CHEREMES')
    out += close_svg()
    return out

# ── Plate 62C — Grammar ───────────────────────────────────────────────────────
def build_62c():
    out = open_svg()
    out += t(240, 32, 'AMERICAN SIGN LANGUAGE (ASL)', 'middle', 'T')
    out += t(240, 47, 'GRAMMAR \u00b7 SPATIAL SYNTAX \u00b7 AGREEMENT VERBS \u00b7 SERIES 62C', 'middle', 'S')
    out += hr(55)

    # Word order
    out += sh(63, 'WORD ORDER: TOPIC-COMMENT & SVO')
    y = 74
    out += t(36, y, 'TOPIC-COMMENT: Topic (what it\'s about) signed first, then comment about it.', 'start', 'Lx')
    y += 9
    out += bx(36, y, 404, 14)
    out += t(240, y+10, 'BOOK  ME  BUY  (I bought the book)  \u2014  vs.  ME  BUY  BOOK  (SVO neutral)', 'middle', 'Lx')
    y += 20
    out += t(36, y, 'Both orders are grammatical; topic-comment is more natural for discourse structure.', 'start', 'Lx')
    out += hr(y+10, 0.3)
    y += 18

    # Agreement verbs
    out += sh(y, 'AGREEMENT VERBS (SPATIAL GRAMMAR)')
    y += 12
    out += t(36, y, 'AGREEMENT VERBS move in space between the locations assigned to subject and object.', 'start', 'Lx')
    y += 9
    out += t(36, y, 'Step 1: Assign referent A a location in signing space (e.g., left = HE/SHE).', 'start', 'Lx')
    y += 9
    out += t(36, y, 'Step 2: Assign referent B a location (e.g., right = ANOTHER PERSON).', 'start', 'Lx')
    y += 9
    out += t(36, y, 'Step 3: GIVE moves from A\u2019s location to B\u2019s location \u2014 encoding "A gives B".', 'start', 'Lx')
    y += 9
    out += t(36, y, 'Reversing the movement = "B gives A" with no additional signs required.', 'start', 'Lx')
    y += 9
    # Diagram of agreement verb space
    out += bx(36, y, 404, 38)
    out += t(80, y+14, 'LOC-A', 'middle', 'H')
    out += t(80, y+25, '(left)', 'middle', 'Lx')
    out += t(240, y+14, 'NEUTRAL SPACE', 'middle', 'H')
    out += t(240, y+25, 'signing area', 'middle', 'Lx')
    out += t(360, y+14, 'LOC-B', 'middle', 'H')
    out += t(360, y+25, '(right)', 'middle', 'Lx')
    # Arrow
    out += f'<line x1="106" y1="{y+19}" x2="334" y2="{y+19}" stroke="#555" stroke-width="0.8"/>\n'
    out += f'<polygon points="334,{y+15} 342,{y+19} 334,{y+23}" fill="#555"/>\n'
    out += t(240, y+35, 'GIVE (A\u2192B)', 'middle', 'Lx')
    y += 46
    out += hr(y, 0.3)
    y += 8

    # Classifier predicates
    out += sh(y, 'CLASSIFIER PREDICATES')
    y += 12
    out += t(36, y, 'Classifiers are handshapes that represent a category of objects in predicates.', 'start', 'Lx')
    y += 9
    classifiers = [
        ('CL:V',  'Legs',      'Inverted V = person walking; V-walk encodes movement + manner'),
        ('CL:1',  'Upright',   'Index finger = tall thin object (person, pole, tree)'),
        ('CL:B',  'Flat surf.','Flat hand = surface (table, floor, wall)'),
        ('CL:C',  'Container', 'C-shape = cup, glass, cylindrical container'),
        ('CL:G',  'Small obj.','Index+thumb = small flat object (coin, card, paper)'),
        ('CL:5',  'Vehicle',   'Open 5 = car, boat, plane in motion'),
    ]
    ccols = [36, 90, 155]
    for cl, cat, desc in classifiers:
        for v, x in zip([cl, cat, desc], ccols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # Grammar features
    out += sh(y, 'KEY GRAMMATICAL FEATURES')
    y += 12
    features = [
        ('ASPECT',        'Modulate verb movement: slow/repeated = ongoing, fast/sharp = sudden'),
        ('NEGATION',      'Head shake (NMS) simultaneously with or after verb; NEG sign'),
        ('YES/NO Q.',     'Brow raise + eye widening + slight forward head tilt (NMS)'),
        ('WH- Q.',        'Brow furrow + slight head tilt + WH-sign at end (WHERE, WHO, WHAT, WHY)'),
        ('ROLE SHIFT',    'Shift body/eye gaze to "become" each character in narrative'),
        ('BUOY SIGNS',    'Signs that hold a topic in space while continuing discourse'),
    ]
    fcols = [36, 140]
    for feat, desc in features:
        out += t(fcols[0], y, feat, 'start', 'H')
        out += t(fcols[1], y, desc, 'start', 'Lx')
        y += 9

    out += hr(y+2, 0.3)
    y += 8

    # Core vocabulary (ASL gloss)
    out += sh(y, 'CORE VOCABULARY (ASL GLOSS NOTATION)')
    y += 11
    vocab = [
        ('ME / I', 'Index to chest'), ('YOU', 'Index to addressee'), ('HE/SHE/IT', 'Index to referent location'),
        ('GIVE', 'Palm up, move toward'), ('TAKE', 'Palm down, move toward'), ('MAKE', 'Fists rotate on each other'),
        ('KNOW', 'Flat hand at forehead'), ('NOT-KNOW', 'B-hand, flip out'), ('WANT', 'Claw hands, draw in'),
        ('GO', 'Bent V, arc forward'), ('COME', 'Index crook toward signer'), ('SEE', 'V from eyes forward'),
        ('GOOD', 'Flat hand chin to palm'), ('BAD', 'Flat hand chin, flip out'), ('FREE', 'F-hands cross then open'),
        ('REMEMBER', 'A-hand at temple'), ('FORWARD', 'B-hand, push forward'), ('PEOPLE', 'P-hands alternating'),
        ('MAKE', 'S-hands rotate on each other'), ('THIS', 'Index point down at obj'), ('WORD',  'Index + G at mouth'),
    ]
    vcols = [(36, 148), (196, 308), (356, 450)]
    per_col = (len(vocab) + 2) // 3
    for ci, (x1, x2) in enumerate(vcols):
        chunk = vocab[ci*per_col:(ci+1)*per_col]
        cy2 = y
        for gloss, desc in chunk:
            out += t(x1, cy2, gloss, 'start', 'Ls')
            out += t(x2, cy2, desc,  'start', 'Lx')
            cy2 += 9

    out += footer('PLATE 62C', '62', 'AMERICAN SIGN LANGUAGE', 'SPATIAL SYNTAX \u00b7 CLASSIFIERS \u00b7 AGREEMENT')
    out += close_svg()
    return out

# ── Plate 62D — Running Text & Bridge Phrase ──────────────────────────────────
def build_62d():
    out = open_svg()
    out += t(240, 32, 'AMERICAN SIGN LANGUAGE (ASL)', 'middle', 'T')
    out += t(240, 47, 'DISCOURSE \u00b7 GLOSS NOTATION \u00b7 BRIDGE PHRASE \u00b7 SERIES 62D', 'middle', 'S')
    out += hr(55)

    # Gloss notation explanation
    out += sh(63, 'ASL GLOSS NOTATION')
    y = 74
    out += t(36, y, 'Since ASL has no traditional writing system, linguists use GLOSS NOTATION:', 'start', 'L')
    y += 10
    gloss_rules = [
        'CAPITAL LETTERS = one sign  (BOOK = the sign for "book")',
        'HYPHEN = multi-word English for one sign  (GIVE-UP, NOT-YET, LONG-AGO)',
        'Hash # = fingerspelled loan sign  (#DO, #JOB, #CAR)',
        'fs- prefix = fingerspelling  (fs-MARY)',
        'Subscript numbers = spatial loci  (PRO\u2081 = pronoun at locus 1)',
        'NMS above gloss line = non-manual signal (wh-, y/n, neg, cond)',
        'MOUTH MORPHEME: mm, th, puff-cheeks, oo, etc. (shown above line)',
    ]
    for rule in gloss_rules:
        out += t(36, y, rule, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    # Sample discourse
    out += sh(y, 'SAMPLE: THE TORTOISE AND THE HARE (OPENING)')
    y += 12
    story_lines = [
        ('LONG-AGO TORTOISE HARE RACE',
         'Long ago, [there was] a tortoise and a hare [who had] a race.'),
        ('HARE THINK SELF WIN EASY',
         'The hare thought he himself would win easily.'),
        ('TORTOISE SLOW WALK WALK WALK NOT-STOP',
         'The tortoise walked slowly [and] did not stop.'),
        ('FINALLY TORTOISE WIN, HARE LOSE',
         'Finally the tortoise won; the hare lost.'),
    ]
    for gloss, english in story_lines:
        out += bx(36, y, 404, 14)
        out += t(240, y+10, gloss, 'middle', 'Ls')
        y += 18
        out += t(240, y, english, 'middle', 'Lx')
        y += 11

    out += hr(y+2, 0.3)
    y += 8

    # Bridge phrase
    out += sh(y, 'BRIDGE PHRASE IN ASL GLOSS')
    y += 12
    out += bx(36, y, 404, 16)
    out += t(240, y+12, 'THIS  MAKE  FOR-YOU  FREE  PEOPLE  REMEMBER  FORWARD', 'middle', 'Lg')
    y += 22
    out += t(240, y, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Lx')
    y += 12

    # Interlinear analysis
    words = [
        ('THIS',     'index point at object'),
        ('MAKE',     'S-hands rotate on each other'),
        ('FOR-YOU',  'directed toward addressee'),
        ('FREE',     'F-hands cross, open outward'),
        ('PEOPLE',   'P-hands alternating'),
        ('REMEMBER', 'A-hand at temple, move fwd'),
        ('FORWARD',  'B-hand, push forward in space'),
    ]
    cw = 57
    for i, (gloss, desc) in enumerate(words):
        gx = 36 + i * cw
        if gx + cw > 452: break
        out += t(gx + cw//2, y,    gloss, 'middle', 'Ls')
        out += t(gx + cw//2, y+8,  desc,  'middle', 'Lx')
    y += 22

    out += hr(y+2, 0.3)
    y += 8

    # Linguistic notes
    out += sh(y, 'LINGUISTIC NOTES')
    y += 12
    notes = [
        'THIS: Point/index downward at the object being referenced \u2014 deixis in signing space.',
        'FOR-YOU: The sign FOR directed toward the addressee encodes benefaction spatially.',
        'FREE: F-hands crossed (bound) then opening outward \u2014 iconic for liberation / no cost.',
        'PEOPLE: P-handshape (index+middle extended, palm out) alternating = plural humans.',
        'REMEMBER: A-hand taps temple (where memory resides), then moves forward.',
        '  This forward movement simultaneously encodes both "remembering" and "forward in time".',
        'FORWARD: B-hand pushes forward \u2014 spatial metaphor identical to the English phrase.',
        '',
        'NOTE ON TENSE: ASL establishes time on a time line \u2014 past is behind the signer,',
        'future is in front. FORWARD (ahead in space) = forward in time = future orientation.',
        'The phrase "remembered forward" maps perfectly to ASL\'s spatial time metaphor.',
        '',
        'SignWriting (U+1D800\u2013U+1DAAF, Noto Sans SignWriting font) provides a written',
        'visual script for ASL signs that can be used for full written representation.',
    ]
    for line in notes:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 62D', '62', 'AMERICAN SIGN LANGUAGE', 'GLOSS NOTATION \u00b7 BRIDGE PHRASE')
    out += close_svg()
    return out

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate62a_asl_manual_alphabet.svg',   build_62a),
        ('plate62b_asl_parameters.svg',        build_62b),
        ('plate62c_asl_grammar.svg',           build_62c),
        ('plate62d_asl_text.svg',              build_62d),
    ]
    for fname, fn in plates:
        path = os.path.join(OUT, fname)
        content = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK  {fname}  ({len(content)//1024} KB)')

if __name__ == '__main__':
    main()
