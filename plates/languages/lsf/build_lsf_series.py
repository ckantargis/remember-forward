"""
build_lsf_series.py
French Sign Language (LSF — Langue des Signes Française) — plates 64A–64D
Run from repo root: python plates/languages/lsf/build_lsf_series.py
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'asl'))
from sign_lang_helpers import *

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = BASE

def build_64a():
    out = open_svg()
    out += t(240, 32, 'FRENCH SIGN LANGUAGE (LSF)', 'middle', 'T')
    out += t(240, 47, 'LANGUE DES SIGNES FRAN\u00c7AISE \u00b7 MANUAL ALPHABET \u00b7 SERIES 64A', 'middle', 'S')
    out += hr(55)

    out += t(240, 65, 'LSF \u2014 Langue des Signes Fran\u00e7aise \u2014 is the sign language of France and parts of French-speaking', 'middle', 'Lx')
    out += t(240, 74, 'Europe. c. 100,000 native signers. LSF is the PARENT LANGUAGE OF ASL: in 1817, French Deaf', 'middle', 'Lx')
    out += t(240, 83, 'teacher Laurent Clerc brought LSF to the USA with Thomas Hopkins Gallaudet to found the', 'middle', 'Lx')
    out += t(240, 92, 'American School for the Deaf. ~58% of modern ASL signs are cognate with historical LSF.', 'middle', 'Lx')
    out += hr(100, 0.3)

    # Historical lineage diagram
    out += sh(107, 'HISTORICAL LINEAGE')
    y = 118
    out += bx(36, y, 404, 52)
    # Draw simple lineage tree
    out += t(240, y+12, 'OLD FRENCH SIGN LANGUAGE  (Paris Deaf community, 18th century)', 'middle', 'H')
    out += f'<line x1="240" y1="{y+16}" x2="240" y2="{y+24}" stroke="#555" stroke-width="0.7"/>\n'
    out += f'<line x1="120" y1="{y+24}" x2="360" y2="{y+24}" stroke="#555" stroke-width="0.7"/>\n'
    out += f'<line x1="120" y1="{y+24}" x2="120" y2="{y+32}" stroke="#555" stroke-width="0.7"/>\n'
    out += f'<line x1="360" y1="{y+24}" x2="360" y2="{y+32}" stroke="#555" stroke-width="0.7"/>\n'
    out += t(120, y+40, 'LSF (modern, France)', 'middle', 'Lx')
    out += t(360, y+40, 'ASL (USA/Canada, 1817+)', 'middle', 'Lx')
    y += 62

    out += t(240, y, 'LSF and ASL diverged after 1817 and are now distinct languages (though still cognate-rich).', 'middle', 'Lx')
    out += hr(y+10, 0.3)
    y += 18

    # LSF manual alphabet (one-handed, similar to ASL)
    out += sh(y, 'LSF ONE-HANDED MANUAL ALPHABET')
    y += 10
    out += t(240, y, 'LSF uses a one-handed fingerspelling alphabet. It differs from ASL in 4 letters: H, J, X, T.', 'middle', 'Lx')
    y += 12

    # Draw ASL alphabet (base), note differences
    alpha_svg, next_y = draw_asl_alphabet(30, y, cell_w=31, cell_h=44)
    out += alpha_svg

    out += hr(next_y + 2, 0.3)
    y = next_y + 8

    out += sh(y, 'LSF vs ASL ALPHABET DIFFERENCES')
    y += 10
    diffs = [
        ('H', 'LSF: index+middle together, palm out, sideways', 'ASL: index+middle sideways (similar but distinct palm orientation)'),
        ('J', 'LSF: J traced with index in the air',            'ASL: pinky up, trace J in air (both motion letters)'),
        ('T', 'LSF: index+middle V, thumb between (different)', 'ASL: thumb between index+middle of fist'),
        ('X', 'LSF: hooked index, touch thumb',                 'ASL: hooked index (very similar)'),
    ]
    y += 2
    for ltr, lsf_desc, asl_desc in diffs:
        out += t(36, y, ltr + ':',     'start', 'Ls')
        out += t(55, y, 'LSF: ' + lsf_desc, 'start', 'Lx')
        y += 8
        out += t(55, y, 'ASL: ' + asl_desc, 'start', 'Lx')
        y += 10

    out += footer('PLATE 64A', '64', 'FRENCH SIGN LANGUAGE (LSF)', 'FRANCE \u00b7 ~100,000 NATIVE SIGNERS \u00b7 PARENT OF ASL')
    out += close_svg()
    return out

def build_64b():
    out = open_svg()
    out += t(240, 32, 'FRENCH SIGN LANGUAGE (LSF)', 'middle', 'T')
    out += t(240, 47, 'PARAMETERS \u00b7 GRAMMAR \u00b7 LSF vs ASL COMPARISON \u00b7 SERIES 64B', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'LSF PARAMETERS')
    y = 74
    out += t(36, y, 'LSF uses the same 5-parameter phonological system as ASL and BSL:', 'start', 'Lx')
    y += 10
    for param, desc in [
        ('HANDSHAPE (Forme)', '~60 handshapes documented in LSF'),
        ('LOCATION (Lieu)',   'Neutral space + body zones: forehead, face, mouth, chin, chest'),
        ('MOVEMENT (Mouvement)', 'Path, direction, manner, repetition'),
        ('ORIENTATION (Orientation)', 'Palm direction; grammatically significant'),
        ('NMS (Signaux non-manuels)', 'Facial expression, mouth movements, body posture'),
    ]:
        out += t(36,  y, param + ':', 'start', 'H')
        out += t(200, y, desc,         'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'LSF GRAMMAR')
    y += 12
    features = [
        ('WORD ORDER', 'SVO (similar to ASL) as unmarked order; topic-comment also used.',
         'BOOK, JE ACHETER (The book, I bought it) = topic-comment.'),
        ('SPATIAL GRAMMAR', 'Same spatial assignment of referents as ASL; agreement verbs',
         'move between loci. Classifiers used for categories of objects.'),
        ('TENSE', 'Timeline: past = behind signer; future = in front. Explicit time signs',
         '(YESTERDAY, TOMORROW, LONG-AGO, FUTURE) mark tense.'),
        ('ASPECT', 'Verb movement modulated: repeated/slow = habitual/ongoing.',
         'Single sharp movement = completed/punctual.'),
        ('NEGATION', 'Head shake + sign NON, or head shake alone for simple negation.',
         'PAS ENCORE (not yet), JAMAIS (never): distinct sign + NMS.'),
    ]
    for feat, l1, l2 in features:
        out += t(36, y, feat, 'start', 'H')
        y += 9
        out += t(50, y, l1, 'start', 'Lx')
        y += 8
        out += t(50, y, l2, 'start', 'Lx')
        y += 11
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'HISTORICAL SIGNIFICANCE')
    y += 12
    hist = [
        'Institut National des Jeunes Sourds de Paris (1760): first national Deaf school.',
        'Abb\u00e9 de l\u2019\u00c9p\u00e9e (1712\u20131789): pioneered education of Deaf children using sign.',
        'LSF became prestigious through the Paris school; Deaf teachers trained across Europe.',
        'When Gallaudet brought Clerc to the USA in 1817, they brought the Paris school method.',
        'As LSF and ASL evolved separately, they diverged; modern ASL is now more distinct.',
        'Many sign languages worldwide contain LSF-lineage elements (Mali, Morocco, Turkey).',
    ]
    for line in hist:
        out += t(36, y, line, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'CORE VOCABULARY (LSF GLOSS)')
    y += 12
    vocab = [
        ('MOI (I/ME)', 'index to chest'), ('TOI (YOU)', 'index to addressee'),
        ('LUI/ELLE (HE/SHE)', 'index to locus'), ('NOM (NAME)', 'N at forehead'),
        ('SOURD (DEAF)', 'index ear to mouth'), ('ENTENDANT (HEARING)', 'index circles at mouth'),
        ('SIGNER', 'two indices circle'),  ('COMPRENDRE', 'index taps forehead'),
        ('DONNER (GIVE)', 'palm up, extend'), ('PRENDRE (TAKE)', 'palm down, draw back'),
        ('FAIRE (MAKE)', 'fists rotate'),   ('LIBRE (FREE)', 'wrists cross then open'),
        ('SE SOUVENIR', 'A-hand temple fwd'), ('AVANT (FORWARD)', 'flat hand forward'),
        ('PERSONNES', 'P-hands alternate'),  ('ENSEMBLE (TOGETHER)', 'fists side by side'),
    ]
    vcols = [(36, 148), (246, 358)]
    per_col = (len(vocab) + 1) // 2
    for ci, (x1, x2) in enumerate(vcols):
        cy2 = y
        for gloss, desc in vocab[ci*per_col:(ci+1)*per_col]:
            out += t(x1, cy2, gloss, 'start', 'Ls')
            out += t(x2, cy2, desc,  'start', 'Lx')
            cy2 += 9

    out += footer('PLATE 64B', '64', 'FRENCH SIGN LANGUAGE (LSF)', 'SVO \u00b7 SPATIAL GRAMMAR \u00b7 ASL PARENT')
    out += close_svg()
    return out

def build_64c():
    out = open_svg()
    out += t(240, 32, 'FRENCH SIGN LANGUAGE (LSF)', 'middle', 'T')
    out += t(240, 47, 'DISCOURSE \u00b7 BRIDGE PHRASE \u00b7 LSF\u2013ASL\u2013BSL FAMILY TREE \u00b7 SERIES 64C', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'BRIDGE PHRASE IN LSF GLOSS')
    y = 74
    out += bx(36, y, 404, 16)
    out += t(240, y+12, 'CE  FABRIQUER  POUR-TOI  LIBRE  PERSONNES  SE-SOUVENIR  AVANT', 'middle', 'Lg')
    y += 22
    out += t(240, y, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Lx')
    y += 10
    notes_bridge = [
        'FABRIQUER: make/create \u2014 S-hands rotate on each other (cognate with ASL MAKE).',
        'POUR-TOI: benefactive preposition POUR directed toward the addressee\'s locus.',
        'LIBRE: free/liberty \u2014 wrists crossed (bound), then open outward (iconic liberation).',
        'SE-SOUVENIR: reflexive \u2014 A-hand at temple, moves forward (memory + forward).',
        'AVANT: before/forward \u2014 flat hand pushed forward in space (same spatial metaphor as ASL).',
    ]
    for line in notes_bridge:
        out += t(36, y, line, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'SIGN LANGUAGE FAMILY TREE')
    y += 12
    tree_notes = [
        'Sign languages, like spoken languages, form genetic families through common ancestry.',
        '',
        'OLD FRENCH SIGN LANGUAGE (Paris, 18th century)',
        '  \u2514\u2500 LSF (modern France, Belgium) \u2014 100,000 signers',
        '  \u2514\u2500 ASL (USA, Canada) \u2014 via Clerc 1817 \u2014 500,000 native',
        '       \u2514\u2500 Many African sign languages (Mali SL, etc.)',
        '',
        'OLD BRITISH SIGN LANGUAGE (Braidwood school, Edinburgh 1760)',
        '  \u2514\u2500 BSL (UK) \u2014 150,000 signers',
        '  \u2514\u2500 Auslan (Australia) \u2014 part of BANZSL family',
        '  \u2514\u2500 NZSL (New Zealand) \u2014 part of BANZSL family',
        '',
        'INDEPENDENTLY DEVELOPED:',
        '  Chinese SL \u2014 20,000,000 signers (largest)',
        '  Japanese SL (JSL)',
        '  Israeli SL (ISL)',
        '  Indian SL \u2014 3,000,000+ signers',
        '  Brazilian SL (Libras) \u2014 3\u201310,000,000 signers',
        '',
        'Note: Geographic proximity does NOT determine sign language relationship.',
        'BSL and ASL are as distinct as French and Finnish, despite sharing English context.',
        'International Sign (IS): a contact variety used at international Deaf events;',
        'not a full natural language but facilitates communication across SL families.',
    ]
    for line in tree_notes:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 64C', '64', 'FRENCH SIGN LANGUAGE (LSF)', 'FAMILY TREE \u00b7 BRIDGE PHRASE')
    out += close_svg()
    return out

def build_64d():
    out = open_svg()
    out += t(240, 32, 'FRENCH SIGN LANGUAGE (LSF)', 'middle', 'T')
    out += t(240, 47, 'SIGN LANGUAGE PRESERVATION \u00b7 DEAF HISTORY \u00b7 SERIES 64D', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'DEAF HISTORY & SIGN LANGUAGE SUPPRESSION')
    y = 74
    hist_timeline = [
        ('1760', 'Edinburgh', 'Thomas Braidwood founds first Deaf school in Britain (oral method)'),
        ('1760', 'Paris',     'Abb\u00e9 de l\u2019\u00c9p\u00e9e founds Paris Deaf school using sign method'),
        ('1778', 'Paris',     'LSF begins consolidating from diverse regional village sign languages'),
        ('1817', 'Hartford',  'Gallaudet & Clerc found American School for the Deaf; ASL branches from LSF'),
        ('1880', 'Milan',     'Second International Congress of Educators of the Deaf: ORAL METHOD voted'),
        ('1880', 'worldwide', 'Sign languages banned in Deaf education worldwide for nearly 100 years'),
        ('1960', 'USA',       'William Stokoe proves ASL is a complete language; launches sign linguistics'),
        ('1968', 'France',    'LSF returned to Deaf education in France'),
        ('1990', 'USA',       'ADA (Americans with Disabilities Act) \u2014 interpreter access required'),
        ('2003', 'UK',        'BSL officially recognised as a language of the UK'),
        ('2005', 'France',    'LSF officially recognised in French law'),
    ]
    tcols = [36, 84, 140]
    thdrs = ['Year', 'Place', 'Event']
    for h, x in zip(thdrs, tcols):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 9
    for yr, place, event in hist_timeline:
        for v, x in zip([yr, place, event], tcols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'THE 1880 MILAN CONGRESS \u2014 ORALISM')
    y += 12
    milan = [
        'The Second International Congress on Education of the Deaf (Milan, 1880) voted',
        'to impose oral-only education on Deaf children worldwide.',
        'Sign languages were banned from classrooms. Deaf teachers were dismissed.',
        'Children were forced to speak and lip-read instead of sign.',
        'Research now shows oral-only methods are far less effective for many Deaf children.',
        'Sign languages survived through Deaf communities outside school settings.',
        'The 2010 International Congress formally repudiated the 1880 resolution.',
        '',
        'IMPLICATION FOR THIS CAPSULE:',
        'Sign languages are suppressed natural languages with documented near-extinction events.',
        'Including them here is an act of the same forward-remembering this project embodies.',
    ]
    for line in milan:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'SIGNWRITING \u2014 A COMPLETE WRITTEN FORM FOR SIGN LANGUAGES')
    y += 12
    sw_notes = [
        'Invented by Valerie Sutton (1974, expanded from DanceWriting).',
        'SignWriting represents: handshape, location on body, movement, palm orientation.',
        'Written vertically, top to bottom, left to right within a signing column.',
        'Unicode block: Sutton SignWriting, U+1D800\u2013U+1DAAF (679 characters, Unicode 8.0+).',
        'Font: Noto Sans SignWriting (Google Fonts) \u2014 37,886 glyphs.',
        'Actively used in Nicaragua, Brazil (Libras), and parts of ASL/LSF communities.',
        'SignBank and SignPuddle: online databases of signs in SignWriting notation.',
        '',
        'For this capsule: SignWriting notation is the closest written approximation',
        'of a sign language\'s visual form. A finder who encounters a signer can use',
        'the SignWriting plates to establish communication without shared spoken language.',
    ]
    for line in sw_notes:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 64D', '64', 'FRENCH SIGN LANGUAGE (LSF)', 'DEAF HISTORY \u00b7 MILAN 1880 \u00b7 SIGNWRITING')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate64a_lsf_manual_alphabet.svg', build_64a),
        ('plate64b_lsf_grammar.svg',         build_64b),
        ('plate64c_lsf_discourse.svg',        build_64c),
        ('plate64d_lsf_history.svg',         build_64d),
    ]
    for fname, fn in plates:
        path = os.path.join(OUT, fname)
        content = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK  {fname}  ({len(content)//1024} KB)')

if __name__ == '__main__':
    main()
