"""
build_libras_series.py
Brazilian Sign Language (Libras — Língua Brasileira de Sinais) — plates 66A–66D
Run from repo root: python plates/languages/libras/build_libras_series.py
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'asl'))
from sign_lang_helpers import *

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = BASE

def build_66a():
    out = open_svg()
    out += t(240, 32, 'BRAZILIAN SIGN LANGUAGE (LIBRAS)', 'middle', 'T')
    out += t(240, 47, 'L\u00cdNGUA BRASILEIRA DE SINAIS \u00b7 MANUAL ALPHABET \u00b7 SERIES 66A', 'middle', 'S')
    out += hr(55)

    out += t(240, 65, 'Libras (L\u00edngua Brasileira de Sinais) is the sign language of Deaf communities in Brazil.', 'middle', 'Lx')
    out += t(240, 74, '3\u201310 million signers estimated. Libras was officially recognised by Brazilian federal law', 'middle', 'Lx')
    out += t(240, 83, '(Law 10.436, 2002) as "a means of communication and expression" of the Brazilian Deaf community.', 'middle', 'Lx')
    out += hr(91, 0.3)

    out += sh(98, 'LIBRAS ONE-HANDED MANUAL ALPHABET')
    out += t(240, 108, 'Libras uses a one-handed fingerspelling alphabet. Largely similar to ASL/LSF, with some differences.', 'middle', 'Lx')
    alpha_svg, next_y = draw_asl_alphabet(30, 115, cell_w=31, cell_h=44)
    out += alpha_svg
    out += hr(next_y + 2, 0.3)

    y = next_y + 8
    out += sh(y, 'LIBRAS vs ASL ALPHABET DIFFERENCES')
    y += 10
    diffs = [
        ('CH', 'Libras has a separate sign for CH (no equivalent in ASL 26-letter set)'),
        ('NH', 'Libras has a NH handshape (Portuguese digraph not in English/ASL)'),
        ('LH', 'Libras has a LH handshape (Portuguese palatal lateral)'),
        ('H',  'Libras H differs slightly from ASL H in palm orientation'),
        ('J',  'Both are motion letters; Libras traces J with index'),
        ('Z',  'Both trace Z; Libras uses same basic shape'),
    ]
    for ltr, desc in diffs:
        out += t(36, y, ltr + ':', 'start', 'Ls')
        out += t(65, y, desc, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'LIBRAS HANDSHAPE INVENTORY')
    y += 10
    out += t(240, y, 'Libras has 111 distinct handshapes documented (vs ~50 in ASL) \u2014 the most of any sign language', 'middle', 'Lx')
    y += 9
    out += t(240, y, 'studied. This larger inventory reflects the richness of Libras\u2019 phonological system.', 'middle', 'Lx')
    y += 9
    cat = [
        ('Flat/open',  'B, B-bent, 5-spread, open-A'),
        ('Curved',     'C, O, baby-O, bent-5'),
        ('Extended',   'D, G, H, I, K, L, U, V, W, Y'),
        ('Closed',     'A, E, S, T, N, M, X'),
        ('Compound',   'F, P, Q, R, unique Libras forms'),
    ]
    for cat_name, desc in cat:
        out += t(36,  y, cat_name + ':', 'start', 'H')
        out += t(105, y, desc, 'start', 'Lx')
        y += 9

    out += footer('PLATE 66A', '66', 'LIBRAS (BRAZILIAN SIGN LANGUAGE)', 'BRAZIL \u00b7 3\u201310M SIGNERS \u00b7 111 HANDSHAPES')
    out += close_svg()
    return out

def build_66b():
    out = open_svg()
    out += t(240, 32, 'BRAZILIAN SIGN LANGUAGE (LIBRAS)', 'middle', 'T')
    out += t(240, 47, 'PARAMETERS \u00b7 GRAMMAR \u00b7 VERB TYPES \u00b7 SERIES 66B', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'LIBRAS PHONOLOGICAL PARAMETERS (5)')
    y = 74
    for param, desc in [
        ('HANDSHAPE (Configuração de mão)', '111 distinct handshapes (most documented of any SL)'),
        ('LOCATION (Locação/Ponto de articulação)', 'Head zones, trunk, neutral space; arm/hand location'),
        ('MOVEMENT (Movimento)',           'Path, direction, internal finger movement, wrist twist'),
        ('ORIENTATION (Orientação)',        'Palm direction: 6 primary orientations'),
        ('NMS (Expressões não-manuais)',    'Facial expression, mouth morphemes, body posture'),
    ]:
        out += t(36,  y, param + ':', 'start', 'H')
        out += t(240, y, desc, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'WORD ORDER: SVO + TOPIC-COMMENT')
    y += 12
    wo = [
        'Unmarked order: SVO (subject-verb-object) \u2014 same as English and ASL.',
        'Topic-comment also common: BOOK, I READ (topicalizing the book first).',
        'When using topic-comment, brow raise NMS marks the topic.',
        'SOV order also occurs, particularly with focus on the object or classifier predicates.',
    ]
    for line in wo:
        out += t(36, y, line, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'LIBRAS VERB TYPES')
    y += 12
    verb_types = [
        ('PLAIN VERBS', 'No spatial agreement. Move in neutral space.', 'GOSTAR (like), QUERER (want), SABER (know)'),
        ('AGREEMENT VERBS', 'Incorporate subject/object via spatial movement.', 'DAR (give), PAGAR (pay), PERGUNTAR (ask)'),
        ('SPATIAL VERBS', 'Encode location of objects, not persons.', 'COLOCAR (put), IR (go), VIR (come)'),
    ]
    vcols = [36, 130, 260]
    vhdrs = ['Type', 'Feature', 'Examples']
    for h, x in zip(vhdrs, vcols):
        out += t(x, y, h, 'start', 'H')
    out += hr(y+3, 0.3)
    y += 10
    for typ, feat, ex in verb_types:
        for v, x in zip([typ, feat, ex], vcols):
            out += t(x, y, v, 'start', 'Lx')
        y += 9
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'SPATIAL MARKING IN LIBRAS')
    y += 12
    spatial = [
        'Libras shows a precise spatial marking system for definite vs indefinite referents:',
        '',
        'STRONG/DEFINITE reference: NP assigned to right or left space \u2014 persists in discourse.',
        'WEAK/INDEFINITE reference: NP placed in neutral central space.',
        'Pronouns: point to the previously assigned locus (no separate pronoun handshape required).',
        '',
        'This spatial grammar is a universal feature of natural sign languages, not a quirk.',
        'It is structurally equivalent to case marking or article systems in spoken languages.',
    ]
    for line in spatial:
        out += t(36, y, line, 'start', 'Lx')
        y += 8
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'KEY GRAMMATICAL FEATURES')
    y += 12
    features = [
        ('ASPECT',    'Verb movement modulated: repeated/slow = habitual, fast/tense = punctual'),
        ('NEGATION',  'Head shake NMS + N\u00c3O sign, or head shake alone (short clauses)'),
        ('QUESTIONS', 'Y/N: brow raise; WH-: brow furrow + WH-sign (O QU\u00ca, QUEM, ONDE, QUANDO)'),
        ('CLASSIFIERS','Large inventory; CL:1 person, CL:V walk, CL:C container, CL:B flat surface'),
        ('SIMULTANEITY','Multiple parameters used simultaneously \u2014 single sign = multiple morphemes'),
    ]
    for feat, desc in features:
        out += t(36,  y, feat + ':', 'start', 'H')
        out += t(130, y, desc, 'start', 'Lx')
        y += 9

    out += footer('PLATE 66B', '66', 'LIBRAS (BRAZILIAN SIGN LANGUAGE)', 'SVO \u00b7 AGREEMENT VERBS \u00b7 111 HANDSHAPES')
    out += close_svg()
    return out

def build_66c():
    out = open_svg()
    out += t(240, 32, 'BRAZILIAN SIGN LANGUAGE (LIBRAS)', 'middle', 'T')
    out += t(240, 47, 'CORE VOCABULARY \u00b7 LIBRAS IN BRAZIL \u00b7 SERIES 66C', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'CORE VOCABULARY (LIBRAS GLOSS)')
    y = 74
    vocab = [
        ('EU (I/ME)',        'index to chest'),
        ('VOC\u00ca (YOU)',  'index to addressee'),
        ('ELE/ELA (HE/SHE)', 'index to locus'),
        ('NOME (NAME)',      'N at forehead'),
        ('SURDO (DEAF)',     'index ear to chin'),
        ('OUVINTE (HEARING)','index circles at ear'),
        ('SINALIZAR (SIGN)', 'two indices circle'),
        ('ENTENDER (UNDERSTAND)', 'index at forehead'),
        ('SABER (KNOW)',     'flat hand at head'),
        ('VER (SEE)',        'V from eyes'),
        ('DAR (GIVE)',       'palm up, extend fwd'),
        ('FAZER (MAKE/DO)',  'fists rotate'),
        ('QUERER (WANT)',    'bent fingers draw in'),
        ('IR (GO)',          'index arc forward'),
        ('VIR (COME)',       'index curve toward'),
        ('BOM (GOOD)',       'thumbs up'),
        ('RUIM (BAD)',       'thumbs down'),
        ('LIVRE (FREE)',     'wrists cross, open'),
        ('LEMBRAR (REMEMBER)', 'A-hand temple fwd'),
        ('FRENTE/AVAN\u00c7AR', 'flat hand push fwd'),
        ('PESSOAS (PEOPLE)', 'P-hands alternating'),
        ('AMOR (LOVE)',      'crossed arms on chest'),
        ('OBRIGADO (THANKS)','flat hand from chin'),
        ('POR FAVOR (PLEASE)','circular on chest'),
    ]
    vcols = [(36, 148), (246, 358)]
    per_col = (len(vocab) + 1) // 2
    for ci, (x1, x2) in enumerate(vcols):
        cy2 = y
        for gloss, desc in vocab[ci*per_col:(ci+1)*per_col]:
            out += t(x1, cy2, gloss, 'start', 'Ls')
            out += t(x2, cy2, desc,  'start', 'Lx')
            cy2 += 9
    y += max(per_col, 1) * 9 + 8
    out += hr(y, 0.3)
    y += 8

    out += sh(y, 'LIBRAS IN BRAZIL \u2014 LEGAL STATUS & EDUCATION')
    y += 12
    legal = [
        'Law 10.436 (2002): Libras recognised as "a means of communication and expression".',
        'Decree 5.626 (2005): Libras made compulsory in teacher education curricula.',
        'Federal University of Santa Catarina (UFSC) leads Libras research in Brazil.',
        'National Policy on Special Education (2008): inclusive education with Libras interpreters.',
        '',
        'INES (Instituto Nacional de Educa\u00e7\u00e3o de Surdos, Rio de Janeiro, 1856):',
        '  Founded by Edouard Huet (French Deaf teacher, student of same Paris tradition as Clerc).',
        '  Libras developed from French Sign Language influence + Brazilian indigenous signs.',
        '  Brazil\u2019s Deaf community is the largest in Latin America.',
    ]
    for line in legal:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 66C', '66', 'LIBRAS (BRAZILIAN SIGN LANGUAGE)', 'VOCABULARY \u00b7 LAW 10.436/2002')
    out += close_svg()
    return out

def build_66d():
    out = open_svg()
    out += t(240, 32, 'BRAZILIAN SIGN LANGUAGE (LIBRAS)', 'middle', 'T')
    out += t(240, 47, 'BRIDGE PHRASE \u00b7 DISCOURSE \u00b7 SIGN LANGUAGE OVERVIEW \u00b7 SERIES 66D', 'middle', 'S')
    out += hr(55)

    out += sh(63, 'BRIDGE PHRASE IN LIBRAS GLOSS')
    y = 74
    out += bx(36, y, 404, 16)
    out += t(240, y+12, 'ISSO  FAZER  PARA-VOC\u00ca  LIVRE  PESSOAS  LEMBRAR  AVAN\u00c7AR', 'middle', 'Lg')
    y += 22
    out += t(240, y, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Lx')
    y += 12
    notes_b = [
        'ISSO (this): Index points at the object; deictic reference.',
        'FAZER (make): S-hands rotate on each other (cognate with ASL MAKE, LSF FAIRE).',
        'PARA-VOC\u00ca (for-you): preposition PARA directed toward addressee\'s locus.',
        'LIVRE (free): wrists crossed (bound), open outward (iconic: liberation from constraint).',
        'LEMBRAR (remember): A-hand at temple, moves forward \u2014 memory + forward direction.',
        'AVAN\u00c7AR (advance/forward): flat hand pushed forward in neutral space.',
        'FUTURITY NOTE: Like ASL, Libras uses a horizontal timeline (past=behind, future=ahead).',
        'LEMBRAR+AVAN\u00c7AR maps perfectly to the spatial metaphor: remembering toward the future.',
    ]
    for line in notes_b:
        out += t(36, y, line, 'start', 'Lx')
        y += 8
    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'SIGN LANGUAGE SERIES SUMMARY \u2014 ALL 5 LANGUAGES (SERIES 62\u201366)')
    y += 12
    summary = [
        ('Series', 'Language', 'Signers', 'Alphabet', 'Base order', 'Family'),
        ('62', 'ASL (American)',   '~500k native', '1-handed', 'SVO',  'French SL'),
        ('63', 'BSL (British)',    '~150k native', '2-handed', 'SOV',  'BANZSL'),
        ('64', 'LSF (French)',     '~100k native', '1-handed', 'SVO',  'French SL (parent)'),
        ('65', 'CSL (Chinese)',    '~20M',          'Pinyin',   'SOV',  'Independent'),
        ('66', 'Libras (Brazilian)','3\u201310M',  '1-handed', 'SVO',  'French SL lineage'),
    ]
    scols = [36, 70, 148, 235, 300, 355]
    for i, row in enumerate(summary):
        c_s = 'H' if i == 0 else 'Lx'
        for v, x in zip(row, scols):
            out += t(x, y, v, 'start', c_s)
        if i == 0: out += hr(y+3, 0.3)
        y += 9

    out += hr(y+2, 0.3)
    y += 8

    out += sh(y, 'UNIVERSAL FEATURES OF NATURAL SIGN LANGUAGES')
    y += 12
    univ = [
        'All natural sign languages share these properties (independent of each other):',
        '',
        '1. SPATIAL GRAMMAR: Referents assigned to locations; agreement verbs track them.',
        '2. CLASSIFIER PREDICATES: Handshapes represent semantic categories in predicates.',
        '3. NON-MANUAL SIGNALS: Face and body carry grammatical distinctions (not just emotion).',
        '4. SIMULTANEITY: Multiple morphological elements expressed in one sign.',
        '5. DUALITY OF PATTERNING: Meaningless units (handshapes) combine into meaningful signs.',
        '6. PRODUCTIVITY: New signs can be created systematically (compounds, classifiers).',
        '7. ARBITRARINESS: Most signs are arbitrary (not merely pantomime), with iconic minority.',
        '',
        'These features demonstrate that sign languages are COMPLETE NATURAL HUMAN LANGUAGES,',
        'not codes, inventions, or derivatives of spoken languages.',
        '',
        'A finder of this capsule who encounters a signing community can use the',
        'parameters and spatial grammar described in Series 62\u201366 as a universal bootstrap.',
    ]
    for line in univ:
        out += t(36, y, line, 'start', 'Lx')
        y += 8

    out += footer('PLATE 66D', '66', 'LIBRAS (BRAZILIAN SIGN LANGUAGE)', 'BRIDGE PHRASE \u00b7 SERIES 62\u201366 SUMMARY')
    out += close_svg()
    return out

def main():
    plates = [
        ('plate66a_libras_manual_alphabet.svg', build_66a),
        ('plate66b_libras_grammar.svg',         build_66b),
        ('plate66c_libras_vocabulary.svg',      build_66c),
        ('plate66d_libras_discourse.svg',       build_66d),
    ]
    for fname, fn in plates:
        path = os.path.join(OUT, fname)
        content = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK  {fname}  ({len(content)//1024} KB)')

if __name__ == '__main__':
    main()
