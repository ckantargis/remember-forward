"""
Batch 15 — LIBRAS + LSA alt plates (Series 66, plates 66a–66d)
Secondary language: LSA — Lengua de Senas Argentina (Argentine Sign Language, ~90K users)
Geographic link: Sao Paulo to Buenos Aires ~700mi (slightly over 500; standard South American)
Both South American sign languages; both with French Sign Language (LSF) historical influence
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

def plate66a():
    s = open_svg()
    s += t(240, 28, 'LIBRAS', 'middle', 'T')
    s += t(240, 40, 'NOTATION — SOUTH AMERICAN SIGN LANGUAGES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LIBRAS: LINGUA BRASILEIRA DE SINAIS')
    s += t(240, 68, 'LIBRAS: sign language of Brazil\'s Deaf community; ~3M users', 'middle', 'L')
    s += t(240, 79, 'Among the 10 largest sign languages in the world by user count', 'middle', 'L')
    s += t(240, 90, 'Origins: 1857, Rio de Janeiro, via French Sign Language (LSF)', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'LIBRAS MANUAL ALPHABET')
    s += t(240, 117, 'LIBRAS: one-handed manual alphabet (adapted from LSF via Portugal)', 'middle', 'L')
    s += t(240, 128, '26 handshapes for Portuguese alphabet letters; includes nasal vowels', 'middle', 'L')
    s += t(240, 139, 'Accented letters (a with tilde, o with tilde): specific handshapes', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'SUTTON SIGNWRITING IN BRAZIL')
    s += t(240, 166, 'Brazil: one of countries with most active SignWriting use', 'middle', 'L')
    s += t(240, 177, 'LIBRAS written with SignWriting in Deaf schools and some publications', 'middle', 'L')
    s += t(240, 188, 'Sign-Wiki: online LIBRAS dictionary with video + SignWriting', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'LIBRAS RECOGNITION')
    s += t(240, 215, '2002: Brazilian law 10.436 recognizes LIBRAS as official language', 'middle', 'L')
    s += t(240, 226, '2005: Decree 5626 mandates LIBRAS interpreters in federal services', 'middle', 'Ls')
    s += hr(234)
    s += sec_divider(241, 'LSA  \u00b7  SECONDARY LANGUAGE')
    s += sh(266, 'LSA: LENGUA DE SENAS ARGENTINA')
    s += t(240, 277, 'LSA: ~90,000 users in Argentina; Buenos Aires-centered', 'middle', 'L')
    s += t(240, 288, 'Founded: 1857, Buenos Aires (same year as LIBRAS in Rio!)', 'middle', 'L')
    s += t(240, 299, 'Spanish and French missionaries brought sign methods to Argentina', 'middle', 'Ls')
    s += hr(307)
    s += sh(315, 'LSA MANUAL ALPHABET')
    s += t(240, 326, 'LSA: one-handed manual alphabet for Spanish letters', 'middle', 'L')
    s += t(240, 337, 'Includes ene (\u00f1): separate handshape for Spanish nasal palatal', 'middle', 'L')
    s += t(240, 348, 'Based on Spanish fingerspelling tradition from LSE (Spanish SL)', 'middle', 'Ls')
    s += hr(356)
    s += sh(364, 'NOTATION COMPARISON')
    s += t(240, 375, 'Both: one-handed manual alphabets (shared LSF influence)', 'middle', 'L')
    s += t(240, 386, 'LIBRAS: Portuguese alphabet  \u2022  LSA: Spanish alphabet (similar base)', 'middle', 'L')
    s += t(240, 397, 'Both: no universal written standard; video primary', 'middle', 'L')
    s += t(240, 408, 'LIBRAS: SignWriting use growing  \u2022  LSA: glossing predominates in research', 'middle', 'Ls')
    s += footer('66', 'LIBRAS', 'LSA', 'a', 'NOTATION')
    s += close_svg()
    return s

def plate66b():
    s = open_svg()
    s += t(240, 28, 'LIBRAS', 'middle', 'T')
    s += t(240, 40, 'CHEROLOGY — SOUTH AMERICAN SIGN PARAMETERS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LIBRAS HANDSHAPES')
    s += t(240, 68, 'LIBRAS: broad range of handshapes; some shared with LSF/ASL (LSF ancestor)', 'middle', 'L')
    s += t(240, 79, 'Iconic handshapes common: many LIBRAS signs visually motivated', 'middle', 'L')
    s += t(240, 90, 'Some handshapes initialized from Portuguese letters', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'LIBRAS LOCATION AND BODY SPACE')
    s += t(240, 117, 'LIBRAS: rich use of body space; many signs on torso/arms', 'middle', 'L')
    s += t(240, 128, 'Neutral space: in front of signer; body contact: specific meaning', 'middle', 'L')
    s += t(240, 139, 'LIBRAS NMM: facial expression + mouth patterns in Portuguese', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'LIBRAS REGIONAL VARIATION')
    s += t(240, 166, 'Brazil is vast: significant LIBRAS regional variation (North vs South)', 'middle', 'L')
    s += t(240, 177, 'Rio de Janeiro vs Sao Paulo: different signs for common words', 'middle', 'L')
    s += t(240, 188, 'INES (National Institute of Deaf Education): works toward standardization', 'middle', 'Ls')
    s += hr(196)
    s += sec_divider(203, 'LSA CHEROLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(228, 'LSA PARAMETERS')
    s += t(240, 239, 'LSA: same five parameters as all sign languages', 'middle', 'L')
    s += t(240, 250, 'LSA handshapes: some overlap with LIBRAS (shared LSF heritage)', 'middle', 'L')
    s += t(240, 261, 'But most content signs: different from LIBRAS (distinct languages)', 'middle', 'Ls')
    s += hr(269)
    s += sh(277, 'LSA NMM AND MOUTH PATTERNS')
    s += t(240, 288, 'LSA: Spanish mouthing common with signs', 'middle', 'L')
    s += t(240, 299, 'Eyebrow grammar: same as all sign languages (yes/no vs wh-questions)', 'middle', 'L')
    s += t(240, 310, 'Gaze: important in LSA spatial grammar', 'middle', 'Ls')
    s += hr(318)
    s += sh(326, 'SHARED SOUTH AMERICAN FEATURES')
    s += t(240, 337, 'Both LIBRAS and LSA: five-parameter sign languages (universal)', 'middle', 'L')
    s += t(240, 348, 'Both: signed iconicity common; many visually motivated signs', 'middle', 'L')
    s += t(240, 359, 'Both: mouthing from national spoken language (Portuguese / Spanish)', 'middle', 'L')
    s += t(240, 370, 'Despite geographic proximity: LIBRAS and LSA are distinct, not mutually intelligible', 'middle', 'Ls')
    s += footer('66', 'LIBRAS', 'LSA', 'b', 'CHEROLOGY')
    s += close_svg()
    return s

def plate66c():
    s = open_svg()
    s += t(240, 28, 'LIBRAS', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — SOUTH AMERICAN SIGN SYNTAX', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LIBRAS WORD ORDER')
    s += t(240, 68, 'LIBRAS: SOV is most common, but SVO also occurs', 'middle', 'L')
    s += t(240, 79, 'PESSOA LIVRO DAR: "Person gives book" (SOV)', 'middle', 'L')
    s += t(240, 90, 'Topic-comment very frequent: LIVRO [brows] PESSOA DAR', 'middle', 'L')
    s += t(240, 101, 'More flexible than spoken Portuguese (spatial grammar reduces word-order need)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'LIBRAS SPATIAL GRAMMAR')
    s += t(240, 128, 'Loci: nouns assigned locations in space; pointing = pronoun', 'middle', 'L')
    s += t(240, 139, 'Agreement verbs: move between loci to show who acts on whom', 'middle', 'L')
    s += t(240, 150, 'Classifiers (proforms): represent categories of referents', 'middle', 'L')
    s += t(240, 161, 'Same spatial grammar as ASL, LSF (shared through LSF ancestor)', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'LIBRAS ASPECT')
    s += t(240, 188, 'Aspect over tense: same as all sign languages', 'middle', 'L')
    s += t(240, 199, 'Movement modification: repeated = habitual; tense = time sign + context', 'middle', 'L')
    s += t(240, 210, 'Timeline: future = space forward  \u2022  past = space behind (universal SL feature)', 'middle', 'Ls')
    s += hr(218)
    s += sec_divider(225, 'LSA GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'LSA WORD ORDER')
    s += t(240, 261, 'LSA: tends toward SOV; topic-comment also common', 'middle', 'L')
    s += t(240, 272, 'PERSONA LIBRO DAR: "Person gives book" (SOV like LIBRAS)', 'middle', 'L')
    s += t(240, 283, 'Both LIBRAS and LSA: SOV with spatial modification (parallel)', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'LSA SPATIAL GRAMMAR')
    s += t(240, 310, 'LSA: same spatial grammar system as LIBRAS (universal to sign languages)', 'middle', 'L')
    s += t(240, 321, 'Loci, verb agreement, classifiers: all present', 'middle', 'L')
    s += t(240, 332, 'Argentina research: Universidad Nacional del Comahue; APSA (Deaf association)', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'GRAMMAR COMPARISON')
    s += t(240, 359, 'Both: SOV-preferred  \u2022  both: topic-comment  \u2022  both: spatial grammar', 'middle', 'L')
    s += t(240, 370, 'Both: aspect over tense  \u2022  both: classifiers', 'middle', 'L')
    s += t(240, 381, 'Vocabulary: largely distinct (different languages)', 'middle', 'L')
    s += t(240, 392, 'Grammar: largely parallel (shared sign language universals + LSF heritage)', 'middle', 'Ls')
    s += footer('66', 'LIBRAS', 'LSA', 'c', 'GRAMMAR')
    s += close_svg()
    return s

def plate66d():
    s = open_svg()
    s += t(240, 28, 'LIBRAS', 'middle', 'T')
    s += t(240, 40, 'HISTORY — DEAF COMMUNITY IN SOUTH AMERICA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'LIBRAS ORIGINS: 1857')
    s += t(240, 68, '1855: Edward Huet, Deaf French teacher, arrives in Brazil', 'middle', 'L')
    s += t(240, 79, '1857: Emperor Pedro II founds Instituto Nacional de Surdos-Mudos (Rio)', 'middle', 'L')
    s += t(240, 90, 'Huet brings LSF; mixes with indigenous Brazilian sign languages', 'middle', 'L')
    s += t(240, 101, 'Result: LIBRAS (Lingua Brasileira de Sinais) \u2014 distinct from Portuguese', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'LIBRAS AND ORALISM IN BRAZIL')
    s += t(240, 128, '1880 Milan: Brazil adopted oralism in Deaf education (like most countries)', 'middle', 'L')
    s += t(240, 139, 'LIBRAS survived in Deaf community despite oralist suppression', 'middle', 'L')
    s += t(240, 150, '1970s-1990s: Brazilian Deaf movement advocated for LIBRAS rights', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'LEGAL RECOGNITION AND ACADEMIA')
    s += t(240, 177, '2002: Brazil Law 10.436: LIBRAS recognized as official language', 'middle', 'L')
    s += t(240, 188, '2005: Decree 5626: LIBRAS instruction required in education courses', 'middle', 'L')
    s += t(240, 199, 'University LIBRAS programs: thousands of hearing students learn LIBRAS', 'middle', 'L')
    s += t(240, 210, 'FENEIS (National Federation of Deaf): main Deaf advocacy organization', 'middle', 'Ls')
    s += hr(218)
    s += sec_divider(225, 'LSA HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'LSA ORIGINS: ALSO 1857')
    s += t(240, 261, '1857: Instituto Nacional de Sordomudos founded in Buenos Aires', 'middle', 'L')
    s += t(240, 272, 'Same year as LIBRAS founding (Rio) \u2014 remarkable historical coincidence', 'middle', 'L')
    s += t(240, 283, 'Spanish and French sign methods brought to Argentina; LSA develops', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'LSA AND ORALISM')
    s += t(240, 310, 'Argentina also adopted oralism post-1880; LSA survived in community', 'middle', 'L')
    s += t(240, 321, '1987: APSA (Asociacion de Padres y Amigos del Sordo) advocates for LSA', 'middle', 'L')
    s += t(240, 332, 'Argentina: no federal LSA recognition law as of early 2020s (still pending)', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'BOTH FOUNDED IN 1857')
    s += t(240, 359, 'LIBRAS (Rio, 1857) and LSA (Buenos Aires, 1857): born the same year', 'middle', 'L')
    s += t(240, 370, 'Both born from same wave of LSF-influenced Deaf education spreading globally', 'middle', 'L')
    s += t(240, 381, 'Laurent Clerc\'s 1817 voyage created a chain: LSF \u2192 ASL \u2192 influenced Brazil + Argentina', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'SOUTH AMERICAN DEAF COMMUNITY')
    s += t(240, 408, 'Both communities: strong cultural identity; Deaf clubs, Deaf schools', 'middle', 'L')
    s += t(240, 419, 'Both: fighting for legal recognition; LIBRAS won in 2002', 'middle', 'L')
    s += t(240, 430, 'Sign language is not spoken through the air alone \u2014 it is carried in hands', 'middle', 'L')
    s += t(240, 441, 'Passed from generation to generation: the oldest gesture of belonging', 'middle', 'Ls')
    s += footer('66', 'LIBRAS', 'LSA', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate66a_libras_lsa_notation_alt.svg', plate66a()),
                  ('plate66b_libras_lsa_cherology_alt.svg', plate66b()),
                  ('plate66c_libras_lsa_grammar_alt.svg', plate66c()),
                  ('plate66d_libras_lsa_history_alt.svg', plate66d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
