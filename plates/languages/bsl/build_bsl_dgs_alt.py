"""
Batch 14 — BSL + DGS alt plates (Series 63, plates 63a–63d)
Secondary language: DGS — Deutsche Gebaerdensprache (German Sign Language, ~200K users)
Geographic link: London to Berlin ~600mi (slightly over 500; standard European pairing)
Both Western European sign languages; BSL and DGS share historical ties via French Sign Language
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

# ── PLATE 63a  NOTATION ──────────────────────────────────────────────────────
def plate63a():
    s = open_svg()
    s += t(240, 28, 'BRITISH SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'NOTATION — TWO-HANDED VS ONE-HANDED', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'BSL: BRITISH SIGN LANGUAGE')
    s += t(240, 68, 'BSL: natural sign language of UK Deaf community; ~125,000 users', 'middle', 'L')
    s += t(240, 79, 'NOT related to ASL (despite both being English-country sign languages)', 'middle', 'L')
    s += t(240, 90, 'BSL and ASL are mutually unintelligible; different grammars and signs', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'BSL TWO-HANDED MANUAL ALPHABET')
    s += t(240, 117, 'BSL fingerspelling: TWO-HANDED (ASL: one-handed)', 'middle', 'L')
    s += t(240, 128, 'Each letter: specific configuration of both hands together', 'middle', 'L')
    s += t(240, 139, 'Example: A = right fist on left palm  \u2022  B = both hands flat, fingers together', 'middle', 'L')
    s += t(240, 150, 'Two-handed alphabet: more visually distinctive but requires both hands free', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'BSL GLOSSING AND NOTATION')
    s += t(240, 177, 'Same glossing conventions as ASL: CAPS for signs, IX for index/pointing', 'middle', 'L')
    s += t(240, 188, 'BSL-specific: FS: = fingerspelling follows  \u2022  MM = mouth morpheme', 'middle', 'L')
    s += t(240, 199, 'BSL corpus: University of Bristol BSL Corpus (survey of 249 signers)', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'BSL RECOGNITION')
    s += t(240, 226, '2003: UK Parliament recognizes BSL as official language of Great Britain', 'middle', 'L')
    s += t(240, 237, '2022: BSL Act: BSL becomes statutory recognized language (Scotland 2015)', 'middle', 'L')
    s += hr(245)
    # Divider
    s += sec_divider(252, 'DGS  \u00b7  SECONDARY LANGUAGE')
    s += sh(277, 'DEUTSCHE GEBAERDENSPRACHE (DGS)')
    s += t(240, 288, 'DGS: sign language of Germany; ~200,000 users (Deaf + hearing)', 'middle', 'L')
    s += t(240, 299, '2002: DGS recognized as official language in Germany', 'middle', 'L')
    s += t(240, 310, 'Also used in: Austria, Luxembourg (alongside local varieties)', 'middle', 'Ls')
    s += hr(318)
    s += sh(326, 'DGS MANUAL ALPHABET')
    s += t(240, 337, 'DGS: one-handed manual alphabet (like ASL, unlike BSL)', 'middle', 'L')
    s += t(240, 348, 'German manual alphabet: based on Franciscan traditions; some French SL influence', 'middle', 'L')
    s += t(240, 359, 'Includes umlauts: separate handshapes for \u00e4, \u00f6, \u00fc', 'middle', 'Ls')
    s += hr(367)
    s += sh(375, 'NOTATION COMPARISON')
    s += t(240, 386, 'BSL: two-handed fingerspelling (unique among major sign languages)', 'middle', 'L')
    s += t(240, 397, 'DGS: one-handed (shared with ASL, LSF, most European sign languages)', 'middle', 'L')
    s += t(240, 408, 'Both: SignWriting and HamNoSys used in research', 'middle', 'L')
    s += t(240, 419, 'Both: glossing used in interpreting and linguistics (different gloss languages)', 'middle', 'Ls')
    s += footer('63', 'BSL', 'DGS', 'a', 'NOTATION')
    s += close_svg()
    return s

# ── PLATE 63b  CHEROLOGY ──────────────────────────────────────────────────────
def plate63b():
    s = open_svg()
    s += t(240, 28, 'BRITISH SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'CHEROLOGY — EUROPEAN SIGN LANGUAGE PARAMETERS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'BSL HANDSHAPES')
    s += t(240, 68, 'BSL uses many of the same handshape categories as other sign languages', 'middle', 'L')
    s += t(240, 79, 'Some handshapes unique to BSL: reflect BSL lexical history', 'middle', 'L')
    s += t(240, 90, 'Two-handed signs: dominant + non-dominant hand interact differently than ASL', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'BSL LOCATION AND MOVEMENT')
    s += t(240, 117, 'BSL signs often more body-anchored than ASL signs', 'middle', 'L')
    s += t(240, 128, 'Many BSL signs: contact with specific body part (head, chest, forearm)', 'middle', 'L')
    s += t(240, 139, 'Movement: same categories (linear, arc, circular, wiggle) as all sign languages', 'middle', 'Ls')
    s += hr(147)
    s += sh(155, 'BSL NON-MANUAL MARKERS')
    s += t(240, 166, 'Eyebrows: same grammatical function as ASL (question marking)', 'middle', 'L')
    s += t(240, 177, 'Mouth patterns: BSL uses English lip patterns more than ASL uses English', 'middle', 'L')
    s += t(240, 188, 'English mouthing: visible with signs in BSL; varies by signer and context', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'BSL REGIONAL VARIATION')
    s += t(240, 215, 'BSL: significant dialect variation across UK regions', 'middle', 'L')
    s += t(240, 226, 'London, Manchester, Edinburgh, Cardiff: different signs for common words', 'middle', 'L')
    s += t(240, 237, 'Color signs especially variable: no standard across UK', 'middle', 'Ls')
    s += hr(245)
    # Divider
    s += sec_divider(252, 'DGS CHEROLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(277, 'DGS PARAMETERS')
    s += t(240, 288, 'DGS uses same five parameters as all sign languages', 'middle', 'L')
    s += t(240, 299, 'DGS handshapes: some overlap with ASL (shared French SL ancestors)', 'middle', 'L')
    s += t(240, 310, 'DGS has compound signs: two signs combined = new meaning (common in DGS)', 'middle', 'Ls')
    s += hr(318)
    s += sh(326, 'DGS REGIONAL VARIATION')
    s += t(240, 337, 'DGS: strong dialect variation (North vs South Germany)', 'middle', 'L')
    s += t(240, 348, 'Hamburg variety: often taken as standard (Hamburg SL research center)', 'middle', 'L')
    s += t(240, 359, 'Bayern (Bavaria): notably different from Hamburg variety', 'middle', 'Ls')
    s += hr(367)
    s += sh(375, 'EUROPEAN SIGN LANGUAGE FEATURES')
    s += t(240, 386, 'BSL and DGS: both use signing space grammatically (universal)', 'middle', 'L')
    s += t(240, 397, 'Both: NMM mark questions, topics, negation', 'middle', 'L')
    s += t(240, 408, 'Both: verb agreement through spatial modification', 'middle', 'L')
    s += t(240, 419, 'Despite European geographic proximity: BSL and DGS are NOT mutually intelligible', 'middle', 'Ls')
    s += footer('63', 'BSL', 'DGS', 'b', 'CHEROLOGY')
    s += close_svg()
    return s

# ── PLATE 63c  GRAMMAR ───────────────────────────────────────────────────────
def plate63c():
    s = open_svg()
    s += t(240, 28, 'BRITISH SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — SPATIAL LANGUAGE STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'BSL WORD ORDER')
    s += t(240, 68, 'BSL: tends toward SVO + topic-comment structures', 'middle', 'L')
    s += t(240, 79, 'Topic fronting common: TIME [topic brows] WOMAN GO SHOP', 'middle', 'L')
    s += t(240, 90, 'Spatial reference: verb modification replaces many function words', 'middle', 'L')
    s += t(240, 101, 'BSL more flexible word order than English (spatial grammar enables this)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'BSL NEGATION')
    s += t(240, 128, 'BSL negation: headshake simultaneously with signed sentence', 'middle', 'L')
    s += t(240, 139, 'NOT sign can also be used; combined NMM + sign = emphatic negation', 'middle', 'L')
    s += t(240, 150, 'Incorporated negation: some verbs have negative handshape variant', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'BSL ASPECT AND TENSE')
    s += t(240, 177, 'No morphological tense markers on verbs (like most sign languages)', 'middle', 'L')
    s += t(240, 188, 'Time: indicated by timeline in signing space (future = forward, past = back)', 'middle', 'L')
    s += t(240, 199, 'Aspect: movement modification (repeated = habitual, slow = prolonged)', 'middle', 'Ls')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'DGS GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'DGS WORD ORDER: SOV BIAS')
    s += t(240, 250, 'DGS: tends toward SOV (Subject-Object-Verb), unlike ASL/BSL (SVO)', 'middle', 'L')
    s += t(240, 261, 'WOMAN BOOK GIVE = "The woman gives the book" (SOV)', 'middle', 'L')
    s += t(240, 272, 'SOV order: matches German spoken grammar! (German is also SOV in subordinate)', 'middle', 'Ls')
    s += hr(280)
    s += sh(288, 'DGS VERB AGREEMENT')
    s += t(240, 299, 'DGS: rich spatial verb agreement (like ASL and BSL)', 'middle', 'L')
    s += t(240, 310, 'Verbs move between loci (locations) to show who does what to whom', 'middle', 'L')
    s += t(240, 321, 'More regular agreement morphology than BSL according to some analyses', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'GRAMMAR COMPARISON')
    s += t(240, 348, 'BSL: SVO \u2022 DGS: SOV (notable difference between the two)', 'middle', 'L')
    s += t(240, 359, 'Both: spatial grammar, verb agreement, NMM, topic-comment', 'middle', 'L')
    s += t(240, 370, 'BSL closer to ASL in word order; DGS closer to German spoken word order', 'middle', 'L')
    s += t(240, 381, 'Intriguing: sign language grammar partially mirrors surrounding spoken language', 'middle', 'Ls')
    s += footer('63', 'BSL', 'DGS', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 63d  HISTORY ───────────────────────────────────────────────────────
def plate63d():
    s = open_svg()
    s += t(240, 28, 'BRITISH SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'HISTORY — EUROPEAN DEAF EDUCATION', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'BSL ORIGINS')
    s += t(240, 68, 'BSL: emerged from Deaf communities in England; no clear founding date', 'middle', 'L')
    s += t(240, 79, '1760: Thomas Braidwood opens first school for the Deaf in Edinburgh', 'middle', 'L')
    s += t(240, 90, '1783: Braidwood Academy moves to London; oral methods emphasis', 'middle', 'L')
    s += t(240, 101, 'BSL community preserved sign language despite oralist educational pressure', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'MILAN CONFERENCE 1880: GLOBAL SUPPRESSION')
    s += t(240, 128, '1880: Second International Congress of Educators of the Deaf, Milan', 'middle', 'L')
    s += t(240, 139, 'Vote (mostly hearing educators): sign languages banned from schools', 'middle', 'L')
    s += t(240, 150, 'Oralism mandated: Deaf children must learn to speak, lip-read only', 'middle', 'L')
    s += t(240, 161, '~100 years: BSL, DGS, ASL all suppressed in formal education', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'BSL RECOGNITION AND REVIVAL')
    s += t(240, 188, '1970s: British Deaf Association advocates for BSL recognition', 'middle', 'L')
    s += t(240, 199, '1992: first BSL TV programs; 2003: UK government recognition', 'middle', 'L')
    s += t(240, 210, '2022: BSL Act \u2014 BSL statutory protected language in England, Wales, Scotland', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'DGS HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'DGS ORIGINS')
    s += t(240, 261, 'Germany: first Deaf school founded 1778 in Leipzig by Samuel Heinicke', 'middle', 'L')
    s += t(240, 272, 'Heinicke: oral method proponent; DGS developed despite oralist pressure', 'middle', 'Ls')
    s += t(240, 283, 'Hamburg: major Deaf community center; DGS standardized around Hamburg', 'middle', 'L')
    s += hr(291)
    s += sh(299, 'DGS AND NAZI PERSECUTION')
    s += t(240, 310, '1933-1945: Nazi regime sterilized Deaf Germans under eugenics laws', 'middle', 'L')
    s += t(240, 321, 'Estimated 17,000 Deaf Germans forcibly sterilized; some sent to camps', 'middle', 'L')
    s += t(240, 332, 'DGS survived; community rebuilt slowly after WWII', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'DGS RECOGNITION')
    s += t(240, 359, '2002: DGS recognized in German Disability Equality Act', 'middle', 'L')
    s += t(240, 370, '~200,000 DGS users; Hamburg University: major DGS research center', 'middle', 'L')
    s += hr(378)
    s += sh(386, 'BSL AND DGS: SHARED EUROPEAN STRUGGLE')
    s += t(240, 397, 'Both: suppressed by 1880 Milan Conference for ~100 years', 'middle', 'L')
    s += t(240, 408, 'Both: survived in Deaf communities despite educational bans', 'middle', 'L')
    s += t(240, 419, 'Both: officially recognized early 21st century after long advocacy', 'middle', 'L')
    s += t(240, 430, 'Sign languages: endured because communities passed them hand to hand', 'middle', 'Ls')
    s += footer('63', 'BSL', 'DGS', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate63a_bsl_dgs_notation_alt.svg', plate63a()),
                  ('plate63b_bsl_dgs_cherology_alt.svg', plate63b()),
                  ('plate63c_bsl_dgs_grammar_alt.svg', plate63c()),
                  ('plate63d_bsl_dgs_history_alt.svg', plate63d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
