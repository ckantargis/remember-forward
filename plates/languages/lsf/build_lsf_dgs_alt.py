"""
Batch 15 — LSF + DGS alt plates (Series 64, plates 64a–64d)
Secondary language: DGS — Deutsche Gebaerdensprache (German Sign Language, ~200K users)
Geographic link: Paris to Berlin ~540mi; LSF and DGS both influenced by same Enlightenment-era schools
LSF is parent of ASL; both LSF and DGS shaped by shared French educational model (Abbe de l'Epee)
"""
from pathlib import Path

OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">
<rect x="0" y="0" width="480" height="680" fill="#fffff8"/>
<rect x="6" y="6" width="468" height="668" fill="none" stroke="#222" stroke-width="1.5"/>
<rect x="10" y="10" width="460" height="660" fill="none" stroke="#222" stroke-width="0.5"/>
<style>
text{font-family:Georgia,serif;fill:#111;}
.T{font-size:11px;font-weight:bold;}
.S{font-size:6.5px;}
.H{font-size:6.5px;font-weight:bold;}
.Hb{font-size:7px;font-weight:bold;fill:#fff;}
.L{font-size:7px;}
.Ls{font-size:6px;}
.Lx{font-size:5.5px;}
.M{font-size:6px;}
.F{font-size:7px;font-style:italic;}
.Fb{font-size:7.5px;font-weight:bold;}
</style>
'''

def close_svg(): return '</svg>\n'

def t(x, y, text, anchor='middle', cls='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.5):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#555" stroke-width="{sw}"/>\n'

def sh(y, label, cls='H'):
    return t(240, y, label, 'middle', cls)

def sec_divider(y, label):
    return (f'<rect x="10" y="{y}" width="460" height="13" fill="#111"/>\n'
            + f'<text x="240" y="{y+9.5}" text-anchor="middle" class="Hb">{esc(label)}</text>\n')

def footer(num, lang1, lang2, letter, desc):
    return (hr(634) +
            t(240, 643, f'PLATE {num}{letter} ALT  \u00b7  {lang1} / {lang2}  \u00b7  {desc}', 'middle', 'M') +
            t(240, 652, 'CC BY-SA 4.0  \u00b7  REMEMBERFORWARD.ORG', 'middle', 'M'))

def plate64a():
    s = open_svg()
    s += t(240, 28, 'LSF — LANGUE DES SIGNES FRANCAISE', 'middle', 'T')
    s += t(240, 40, 'NOTATION — PARENT OF MODERN SIGN LANGUAGES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LSF: FRENCH SIGN LANGUAGE')
    s += t(240, 68, 'LSF: ~100,000 users in France; also Belgium, Switzerland, Luxembourg', 'middle', 'L')
    s += t(240, 79, 'Parent language: LSF is ancestor of ASL, LSM, and influenced DGS', 'middle', 'L')
    s += t(240, 90, 'Without LSF, modern Deaf education worldwide would be entirely different', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'LSF ONE-HANDED MANUAL ALPHABET')
    s += t(240, 117, 'LSF: one-handed manual alphabet; same system adopted by ASL in 1817', 'middle', 'L')
    s += t(240, 128, 'Laurent Clerc brought LSF alphabet to America; became ASL manual alphabet', 'middle', 'L')
    s += t(240, 139, 'LSF alphabet: 26 handshapes + accented letters (e with accent, etc.)', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'LSF GLOSSING')
    s += t(240, 166, 'LSF glossed in French: FEMME DONNER LIVRE = "The woman gives the book"', 'middle', 'L')
    s += t(240, 177, 'ELIX: LSF dictionary database; ALIS: French LSF research institute', 'middle', 'L')
    s += t(240, 188, 'LSF recognized as official language of France in 2005 (education law)', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'SAMPLE LSF CHARACTERISTICS')
    s += t(240, 215, 'LSF uses face-neutral signing space heavily (more than ASL)', 'middle', 'L')
    s += t(240, 226, 'French mouthing: less prominent in LSF than English mouthing in BSL', 'middle', 'Ls')
    s += hr(234)
    s += sec_divider(241, 'DGS  \u00b7  SECONDARY LANGUAGE')
    s += sh(266, 'DGS AND LSF: HISTORICAL SIBLINGS')
    s += t(240, 277, 'Both LSF and DGS influenced by Abbe de l\'Epee\'s Paris institute (1760)', 'middle', 'L')
    s += t(240, 288, 'German Deaf students exposed to French methods; brought signs to Germany', 'middle', 'L')
    s += t(240, 299, 'DGS: more independently developed than ASL from LSF', 'middle', 'Ls')
    s += hr(307)
    s += sh(315, 'EUROPEAN SIGN LANGUAGE FAMILY')
    s += t(240, 326, 'LSF family: LSF, ASL, LSM, Irish SL, many others', 'middle', 'L')
    s += t(240, 337, 'DGS: more independent origin but French influence via educational exchange', 'middle', 'L')
    s += t(240, 348, 'Both: one-handed manual alphabet (shared French tradition)', 'middle', 'Ls')
    s += hr(356)
    s += sh(364, 'NOTATION COMPARISON')
    s += t(240, 375, 'Both: SignWriting and HamNoSys used for research', 'middle', 'L')
    s += t(240, 386, 'Both: glossing in respective national spoken languages', 'middle', 'L')
    s += t(240, 397, 'Both: one-handed manual alphabet (important shared feature)', 'middle', 'L')
    s += t(240, 408, 'LSF: parent  \u2022  DGS: sibling/descendant — both shaped by Enlightenment', 'middle', 'Ls')
    s += footer('64', 'LSF', 'DGS', 'a', 'NOTATION')
    s += close_svg()
    return s

def plate64b():
    s = open_svg()
    s += t(240, 28, 'LSF — LANGUE DES SIGNES FRANCAISE', 'middle', 'T')
    s += t(240, 40, 'CHEROLOGY — ENLIGHTENMENT-ERA SIGN SYSTEMS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LSF CHEROLOGY (PHONOLOGY)')
    s += t(240, 68, 'LSF parameters: handshape, location, movement, orientation, NMM', 'middle', 'L')
    s += t(240, 79, 'Same five parameters as all sign languages (universal feature of SLs)', 'middle', 'L')
    s += t(240, 90, 'LSF handshapes: many are same as or related to ASL handshapes (shared ancestor)', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'LSF DISTINCTIVE FEATURES')
    s += t(240, 117, 'Initialized signs: handshape = first letter of French word (common in LSF)', 'middle', 'L')
    s += t(240, 128, 'FAMILLE (family): F-handshape  \u2022  MONDE (world): M-handshape', 'middle', 'L')
    s += t(240, 139, 'Initialization in LSF carried into ASL (some ASL signs also initialized)', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'LSF NMM')
    s += t(240, 166, 'Mouth morphemes in LSF: French word mouthed simultaneously with signs', 'middle', 'L')
    s += t(240, 177, 'Eyebrows: same grammatical functions as all sign languages', 'middle', 'L')
    s += t(240, 188, 'Gaze: important in LSF spatial grammar (like all sign languages)', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'LSF REGIONAL VARIATION')
    s += t(240, 215, 'Paris: de facto standard  \u2022  regional variants throughout France', 'middle', 'L')
    s += t(240, 226, 'Belgian French Sign Language (LSFB): related but distinct from LSF', 'middle', 'Ls')
    s += hr(234)
    s += sec_divider(241, 'DGS CHEROLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(266, 'DGS PHONOLOGICAL SYSTEM')
    s += t(240, 277, 'DGS: same five-parameter system as LSF and all sign languages', 'middle', 'L')
    s += t(240, 288, 'DGS handshapes: some overlap with LSF/ASL, some unique to German tradition', 'middle', 'L')
    s += t(240, 299, 'DGS compounds: combine two signs to form new concept (very productive)', 'middle', 'Ls')
    s += hr(307)
    s += sh(315, 'LSF VS DGS: SIGN COMPARISON')
    s += t(240, 326, 'LEARN: LSF and DGS have different signs for this concept', 'middle', 'L')
    s += t(240, 337, 'HOUSE: different signs (iconic but differ in which features are selected)', 'middle', 'L')
    s += t(240, 348, 'Despite shared educational history: most content signs are distinct', 'middle', 'Ls')
    s += hr(356)
    s += sh(364, 'SHARED CHEROLOGY')
    s += t(240, 375, 'Both: same five parameters (universal to all sign languages)', 'middle', 'L')
    s += t(240, 386, 'Both: similar NMM grammar (eyebrows, gaze, head movement)', 'middle', 'L')
    s += t(240, 397, 'Both: one-handed manual alphabet (shared French tradition)', 'middle', 'Ls')
    s += footer('64', 'LSF', 'DGS', 'b', 'CHEROLOGY')
    s += close_svg()
    return s

def plate64c():
    s = open_svg()
    s += t(240, 28, 'LSF — LANGUE DES SIGNES FRANCAISE', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — SPATIAL SYNTAX', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LSF WORD ORDER')
    s += t(240, 68, 'LSF: tends toward SVO with frequent topic-comment structures', 'middle', 'L')
    s += t(240, 79, 'HOMME [topic] LIVRE DONNER: "The man, [he] gives a book"', 'middle', 'L')
    s += t(240, 90, 'Flexible: spatial grammar reduces need for rigid word order', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'LSF VERB AGREEMENT')
    s += t(240, 117, 'Directional verbs: move between loci to encode subject and object', 'middle', 'L')
    s += t(240, 128, 'Non-directional verbs: subject/object shown by loci + separate agreement signs', 'middle', 'L')
    s += t(240, 139, 'Same agreement system as ASL (inherited from LSF parent)', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'LSF ASPECT SYSTEM')
    s += t(240, 166, 'Aspect encoded in movement: repeated = habitual  \u2022  fast = sudden', 'middle', 'L')
    s += t(240, 177, 'No morphological tense on verbs; time signed separately or from context', 'middle', 'L')
    s += t(240, 188, 'Future timeline: space in front of signer  \u2022  past: behind signer', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'LSF CLASSIFIERS')
    s += t(240, 215, 'Proforms (classifiers): same system as ASL (inherited)', 'middle', 'L')
    s += t(240, 226, 'Handling classifiers, size-and-shape specifiers, semantic classifiers', 'middle', 'Ls')
    s += hr(234)
    s += sec_divider(241, 'DGS GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(266, 'DGS WORD ORDER: SOV')
    s += t(240, 277, 'DGS: SOV word order (Subject-Object-Verb)', 'middle', 'L')
    s += t(240, 288, 'MANN BUCH GEBEN-SOV: "The man gives the book" (SOV)', 'middle', 'L')
    s += t(240, 299, 'Mirrors German spoken grammar: German verb moves to end in subordinate', 'middle', 'Ls')
    s += hr(307)
    s += sh(315, 'DGS VS LSF GRAMMAR')
    s += t(240, 326, 'LSF: SVO-preferred  \u2022  DGS: SOV-preferred (notable difference!)', 'middle', 'L')
    s += t(240, 337, 'Both: topic-comment  \u2022  both: spatial verb agreement', 'middle', 'L')
    s += t(240, 348, 'DGS SOV: possibly influenced by German spoken word order', 'middle', 'Ls')
    s += hr(356)
    s += sh(364, 'GRAMMAR COMPARISON')
    s += t(240, 375, 'Both: spatial grammar, NMM question-marking, verb agreement', 'middle', 'L')
    s += t(240, 386, 'Both: aspect over tense  \u2022  both: topic-comment structures', 'middle', 'L')
    s += t(240, 397, 'Key difference: SVO (LSF) vs SOV (DGS) base word order', 'middle', 'L')
    s += t(240, 408, 'Sign language grammar partially shaped by surrounding spoken language', 'middle', 'Ls')
    s += footer('64', 'LSF', 'DGS', 'c', 'GRAMMAR')
    s += close_svg()
    return s

def plate64d():
    s = open_svg()
    s += t(240, 28, 'LSF — LANGUE DES SIGNES FRANCAISE', 'middle', 'T')
    s += t(240, 40, 'HISTORY — ABBE DE L\'EPEE AND DEAF EDUCATION', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ABBE CHARLES DE L\'EPEE (1712-1789)')
    s += t(240, 68, '1760: Abbe de l\'Epee founds first free public school for the Deaf in Paris', 'middle', 'L')
    s += t(240, 79, 'Observed Deaf siblings signing; recognized it as language', 'middle', 'L')
    s += t(240, 90, 'Combined natural Old French Sign Language with artificial "methodical signs"', 'middle', 'L')
    s += t(240, 101, 'His approach: sign language + speech together (not pure oralism)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'LSF SPREADS TO THE WORLD')
    s += t(240, 128, '1817: Laurent Clerc (Deaf French teacher) sails to America with Gallaudet', 'middle', 'L')
    s += t(240, 139, 'Clerc brings LSF to Hartford, CT; mixed with Martha\'s Vineyard SL = ASL', 'middle', 'L')
    s += t(240, 150, 'ASL: ~60% LSF-derived signs in core vocabulary', 'middle', 'L')
    s += t(240, 161, 'LSF model also exported to: Ireland, Russia, Scandinavia, Germany', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'THE ABBÉ SICARD AND AFTER')
    s += t(240, 188, 'Roch-Ambroise Sicard succeeded l\'Epee; trained Laurent Clerc', 'middle', 'L')
    s += t(240, 199, 'Paris school became INJS (Institut National de Jeunes Sourds) \u2014 still exists', 'middle', 'L')
    s += t(240, 210, '1880 Milan: France voted to suppress LSF in its own schools', 'middle', 'Ls')
    s += hr(218)
    s += sec_divider(225, 'DGS HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'DGS AND FRENCH INFLUENCE')
    s += t(240, 261, '1778: Samuel Heinicke opens Leipzig school (oral method)', 'middle', 'L')
    s += t(240, 272, 'Despite oralism: Deaf communities in Germany signed independently', 'middle', 'L')
    s += t(240, 283, 'French SL model arrived via Prussian educational exchange in early 1800s', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'NAZI PERIOD AND AFTERMATH')
    s += t(240, 310, '1933-1945: ~17,000 Deaf Germans sterilized; DGS community devastated', 'middle', 'L')
    s += t(240, 321, 'Post-WWII: DGS reconstructed slowly; Hamburg becomes center', 'middle', 'L')
    s += t(240, 332, '2002: DGS formally recognized  \u2022  Hamburg University: major research center', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'LSF AND DGS TODAY')
    s += t(240, 359, 'LSF: 2005 French law guarantees Deaf students right to LSF education', 'middle', 'L')
    s += t(240, 370, 'DGS: 2002 recognition; growing academic presence; DGS interpretation corps', 'middle', 'L')
    s += t(240, 381, 'Both: recovering communities after ~100 years of oralist suppression', 'middle', 'Ls')
    s += t(240, 392, 'LSF: founded modern Deaf education worldwide from Paris in 1760', 'middle', 'L')
    s += t(240, 403, 'The Abbe\'s gift: one teacher who listened, changed how the world hears', 'middle', 'L')
    s += footer('64', 'LSF', 'DGS', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate64a_lsf_dgs_notation_alt.svg', plate64a()),
                  ('plate64b_lsf_dgs_cherology_alt.svg', plate64b()),
                  ('plate64c_lsf_dgs_grammar_alt.svg', plate64c()),
                  ('plate64d_lsf_dgs_history_alt.svg', plate64d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
