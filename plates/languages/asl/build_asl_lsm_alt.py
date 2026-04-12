"""
Batch 14 — ASL + LSM alt plates (Series 62, plates 62a–62d)
Secondary language: LSM — Lengua de Señas Mexicana (Mexican Sign Language, ~100K users)
Geographic link: US-Mexico border communities share Deaf education networks; geographic neighbors
Both Western Hemisphere sign languages; ASL has historical influence on LSM development
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

# ── PLATE 62a  NOTATION ──────────────────────────────────────────────────────
def plate62a():
    s = open_svg()
    s += t(240, 28, 'AMERICAN SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'NOTATION — WRITING VISUAL LANGUAGES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SIGN LANGUAGES: NO UNIVERSAL WRITING SYSTEM')
    s += t(240, 68, 'Sign languages are full natural languages; not codes for spoken language', 'middle', 'L')
    s += t(240, 79, 'No single writing system dominates; video is the primary "text" medium', 'middle', 'L')
    s += t(240, 90, 'Three main notation approaches used in research and education:', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'SIGNWRITING (SUTTON 1974)')
    s += t(240, 117, 'SignWriting: visual symbols for handshapes, movement, location, expression', 'middle', 'L')
    s += t(240, 128, 'Written top-to-bottom; handshape symbols + movement arrows', 'middle', 'L')
    s += t(240, 139, 'Used in Deaf education in some countries (Nicaragua, Denmark, Brazil)', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'HAMNOSYS AND STOKOE NOTATION')
    s += t(240, 166, 'HamNoSys: Hamburg Notation System; used in linguistic research', 'middle', 'L')
    s += t(240, 177, 'Stokoe notation (1960): first formal sign language analysis system', 'middle', 'L')
    s += t(240, 188, 'William Stokoe: proved ASL is a complete language, not "signed English"', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'GLOSSING: PRACTICAL NOTATION')
    s += t(240, 215, 'Glossing: write English word for each sign in caps (IX-1 = "I/me")', 'middle', 'L')
    s += t(240, 226, 'WOMAN GIVE BOOK IX-3 = "The woman gives him/her a book"', 'middle', 'L')
    s += t(240, 237, 'Gloss shows meaning but not form; used by interpreters and researchers', 'middle', 'Ls')
    s += hr(245)
    # Divider
    s += sec_divider(252, 'LSM  \u00b7  SECONDARY LANGUAGE')
    s += sh(277, 'LENGUA DE SENAS MEXICANA (LSM) NOTATION')
    s += t(240, 288, 'LSM: same notation systems as ASL (SignWriting, glossing, HamNoSys)', 'middle', 'L')
    s += t(240, 299, 'LSM glosses use Spanish words: MUJER DA LIBRO = "The woman gives a book"', 'middle', 'L')
    s += t(240, 310, 'LSM has its own distinct signs; not same as ASL (different languages)', 'middle', 'Ls')
    s += hr(318)
    s += sh(326, 'FINGERSPELLING: MANUAL ALPHABETS')
    s += t(240, 337, 'ASL: one-handed manual alphabet (26 handshapes for A-Z)', 'middle', 'L')
    s += t(240, 348, 'LSM: uses same one-handed alphabet as ASL (shared with Spanish)', 'middle', 'L')
    s += t(240, 359, 'BSL: two-handed manual alphabet (different from ASL!)', 'middle', 'Ls')
    s += hr(367)
    s += sh(375, 'NOTATION COMPARISON')
    s += t(240, 386, 'Both: no standard written form for everyday use', 'middle', 'L')
    s += t(240, 397, 'Both: fingerspelling for proper nouns and borrowed words', 'middle', 'L')
    s += t(240, 408, 'Both: video recordings now serve as the primary "text" medium', 'middle', 'L')
    s += t(240, 419, 'Sign languages: oral languages with no writing = normal; not a deficit', 'middle', 'Ls')
    s += footer('62', 'ASL', 'LSM', 'a', 'NOTATION')
    s += close_svg()
    return s

# ── PLATE 62b  PHONOLOGY (CHEROLOGY) ─────────────────────────────────────────
def plate62b():
    s = open_svg()
    s += t(240, 28, 'AMERICAN SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'CHEROLOGY — PARAMETERS OF SIGN LANGUAGE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'FIVE PARAMETERS OF ASL SIGNS')
    s += t(240, 68, 'Phonology of sign language = "cherology" (from Greek: hand)', 'middle', 'L')
    s += t(240, 79, '1. Handshape: configuration of the hand (A, B, C, 5, etc.)', 'middle', 'L')
    s += t(240, 90, '2. Location: where the sign is made (forehead, chin, chest, neutral space)', 'middle', 'L')
    s += t(240, 101, '3. Movement: path, direction, repetition (up, down, circular, etc.)', 'middle', 'L')
    s += t(240, 112, '4. Palm orientation: which direction palm faces', 'middle', 'L')
    s += t(240, 123, '5. Non-manual markers (NMM): facial expression, mouth, eyebrows', 'middle', 'L')
    s += hr(131)
    s += sh(139, 'MINIMAL PAIRS IN ASL')
    s += t(240, 150, 'MOTHER vs FATHER: same handshape + movement; only location differs', 'middle', 'L')
    s += t(240, 161, '(chin vs forehead)  \u2014  location is phonemic in ASL', 'middle', 'L')
    s += t(240, 172, 'APPLE vs CANDY: same handshape + location; movement differs', 'middle', 'L')
    s += t(240, 183, 'SICK vs FUNNY: same parameters; NMM (mouth morpheme) differs', 'middle', 'Ls')
    s += hr(191)
    s += sh(199, 'NON-MANUAL MARKERS (NMM)')
    s += t(240, 210, 'Eyebrows raised: yes/no question  \u2022  furrowed: wh- question', 'middle', 'L')
    s += t(240, 221, 'Puffed cheeks: "large"  \u2022  sucked in: "small"  (grammatical!)', 'middle', 'L')
    s += t(240, 232, 'Mouth morphemes: "th" = careless  \u2022  "oo" = small/precise', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'LSM CHEROLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'LSM PARAMETERS')
    s += t(240, 283, 'LSM: same five parameters as ASL (universal to all sign languages)', 'middle', 'L')
    s += t(240, 294, 'Handshape, location, movement, orientation, NMM: universal sign grammar', 'middle', 'L')
    s += t(240, 305, 'All sign languages discovered to date use these same five parameters', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'ASL VS LSM: SIGN DIFFERENCES')
    s += t(240, 332, 'Same concept, different sign: WATER differs in ASL vs LSM', 'middle', 'L')
    s += t(240, 343, 'ASL WATER: W-handshape tapped on chin', 'middle', 'L')
    s += t(240, 354, 'LSM WATER: different handshape or location (distinct signs)', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'ICONICITY IN SIGN LANGUAGES')
    s += t(240, 381, 'Many signs are iconic: shape/movement resembles the referent', 'middle', 'L')
    s += t(240, 392, 'TREE: one hand = trunk, other = branches spreading out', 'middle', 'L')
    s += t(240, 403, 'But iconic signs differ cross-linguistically (bird looks different in each SL)', 'middle', 'Ls')
    s += t(240, 414, 'Iconicity is starting point; arbitrary signs increase over time (arbitrarization)', 'middle', 'Ls')
    s += footer('62', 'ASL', 'LSM', 'b', 'CHEROLOGY')
    s += close_svg()
    return s

# ── PLATE 62c  GRAMMAR ───────────────────────────────────────────────────────
def plate62c():
    s = open_svg()
    s += t(240, 28, 'AMERICAN SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — SPATIAL SYNTAX', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ASL SPATIAL GRAMMAR')
    s += t(240, 68, 'ASL exploits 3D signing space for grammar (not possible in spoken language)', 'middle', 'L')
    s += t(240, 79, 'Nouns introduced and assigned to specific locations in space', 'middle', 'L')
    s += t(240, 90, 'Pointing to those locations = pronouns (no spoken pronouns needed)', 'middle', 'L')
    s += t(240, 101, 'Verbs can be directed between locations = subject-object agreement', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'TOPIC-COMMENT STRUCTURE')
    s += t(240, 128, 'ASL word order: Topic-Comment (not SVO/SOV like English)', 'middle', 'L')
    s += t(240, 139, 'BOOK [raised brows] WOMAN GIVE = "The book, the woman gave it"', 'middle', 'L')
    s += t(240, 150, 'Topic marked by raised eyebrows (NMM); comment follows', 'middle', 'L')
    s += t(240, 161, 'Flexibility: word order serves discourse, not syntactic grammar', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'CLASSIFIERS IN ASL')
    s += t(240, 188, 'Classifiers: handshapes that represent categories of referents', 'middle', 'L')
    s += t(240, 199, 'Flat hand = vehicle  \u2022  2-finger V = person walking  \u2022  C = cylinder', 'middle', 'L')
    s += t(240, 210, 'VEHICLE-CL move-in-arc = "the car drove around the corner"', 'middle', 'L')
    s += t(240, 221, 'Classifiers: simultaneous morphology (impossible in linear speech)', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'LSM GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'LSM SPATIAL GRAMMAR')
    s += t(240, 272, 'LSM uses same spatial grammar as ASL (universal sign language feature)', 'middle', 'L')
    s += t(240, 283, 'Loci (locations in space), verb agreement, topic-comment: all present', 'middle', 'L')
    s += t(240, 294, 'Spatial grammar appears in ALL sign languages studied worldwide', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'LSM UNIQUE FEATURES')
    s += t(240, 321, 'LSM: some signs influenced by Mexican Spanish mouthing/lipreading', 'middle', 'L')
    s += t(240, 332, 'Initialized signs: handshape = first letter of Spanish word (like ASL uses English)', 'middle', 'L')
    s += t(240, 343, 'Number signs: differ from ASL (Mexican vs US counting conventions)', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'WHAT ALL SIGN LANGUAGES SHARE')
    s += t(240, 370, 'All sign languages: spatial grammar, classifiers, NMM, iconicity', 'middle', 'L')
    s += t(240, 381, 'All sign languages: topic-comment or OSV-biased word order', 'middle', 'L')
    s += t(240, 392, 'All sign languages: simultaneous morphology (encode multiple meanings at once)', 'middle', 'L')
    s += t(240, 403, 'Signed languages: NOT universal; each community has its own language', 'middle', 'Ls')
    s += footer('62', 'ASL', 'LSM', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 62d  HISTORY ───────────────────────────────────────────────────────
def plate62d():
    s = open_svg()
    s += t(240, 28, 'AMERICAN SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'HISTORY — DEAF CULTURE AND COMMUNITY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ORIGINS OF ASL')
    s += t(240, 68, 'Martha\'s Vineyard, MA (~1700s): high hereditary deafness; whole community signed', 'middle', 'L')
    s += t(240, 79, '1817: American School for the Deaf founded in Hartford, CT', 'middle', 'L')
    s += t(240, 90, 'Thomas Hopkins Gallaudet + Laurent Clerc (Deaf French signer) founded it', 'middle', 'L')
    s += t(240, 101, 'ASL = mix of Martha\'s Vineyard Sign + LSF (French Sign Language)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'GALLAUDET UNIVERSITY')
    s += t(240, 128, '1864: Gallaudet University founded in Washington DC (Lincoln signed charter)', 'middle', 'L')
    s += t(240, 139, 'World\'s only liberal arts university for the Deaf; instruction in ASL', 'middle', 'L')
    s += t(240, 150, '1988: Deaf President Now protest; first Deaf president selected (I. King Jordan)', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'ORALISM AND SUPPRESSION')
    s += t(240, 177, '1880: Milan Conference; hearing educators voted to ban sign language in schools', 'middle', 'L')
    s += t(240, 188, '~100 years of oralism: Deaf children forced to speak, not sign', 'middle', 'L')
    s += t(240, 199, '1960: Stokoe publishes "Sign Language Structure" \u2014 proves ASL is language', 'middle', 'L')
    s += t(240, 210, 'Resurgence: ASL recognized, Deaf culture reclaimed from ~1970s on', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'LSM HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'LSM ORIGINS')
    s += t(240, 261, 'Mexico: first school for the Deaf founded 1867 in Mexico City', 'middle', 'L')
    s += t(240, 272, 'French Sign Language influence via French educational missionaries', 'middle', 'L')
    s += t(240, 283, 'LSM developed independently from ASL despite geographic proximity', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'LSM STANDARDIZATION')
    s += t(240, 310, '~100,000 LSM users estimated in Mexico', 'middle', 'L')
    s += t(240, 321, '2005: Mexico officially recognizes LSM as national language', 'middle', 'L')
    s += t(240, 332, 'CELAM (Centro LSM) and FENASCOL: standardization efforts', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'DEAF CULTURE: SHARED VALUES')
    s += t(240, 359, 'Deaf culture (capital D): identity, not disability', 'middle', 'L')
    s += t(240, 370, 'Both ASL and LSM communities: strong cultural identity, Deaf schools, Deaf clubs', 'middle', 'L')
    s += t(240, 381, 'Cross-border Deaf communities: sign language conferences, Deaflympics', 'middle', 'Ls')
    s += t(240, 392, 'Cochlear implant controversy: Deaf culture vs medical model of deafness', 'middle', 'Ls')
    s += t(240, 403, '~500,000 ASL users in US  \u2022  ~100,000 LSM users in Mexico', 'middle', 'L')
    s += footer('62', 'ASL', 'LSM', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate62a_asl_lsm_notation_alt.svg', plate62a()),
                  ('plate62b_asl_lsm_cherology_alt.svg', plate62b()),
                  ('plate62c_asl_lsm_grammar_alt.svg', plate62c()),
                  ('plate62d_asl_lsm_history_alt.svg', plate62d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
