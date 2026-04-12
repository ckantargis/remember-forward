"""
Batch 15 — CSL + KSL alt plates (Series 65, plates 65a–65d)
Secondary language: KSL — Korean Sign Language (~300K users, Seoul-centered)
Geographic link: Beijing to Seoul ~600mi; shared East Asian Deaf education history
Both East Asian sign languages; CSL influenced JSL which in turn influenced KSL historically
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

def plate65a():
    s = open_svg()
    s += t(240, 28, 'CSL — CHINESE SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'NOTATION — EAST ASIAN SIGN LANGUAGES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'CSL: CHINESE SIGN LANGUAGE')
    s += t(240, 68, 'CSL: most widely used sign language in the world by population (~20M users)', 'middle', 'L')
    s += t(240, 79, 'Developed primarily in Shanghai (1887: first school for Deaf in China)', 'middle', 'L')
    s += t(240, 90, 'Two major varieties: Shanghai SL and Beijing SL (partially unified post-1949)', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'CSL MANUAL SYSTEMS')
    s += t(240, 117, 'Chinese finger-spelling: handshapes for Mandarin pinyin sounds (zhuyin-based)', 'middle', 'L')
    s += t(240, 128, 'CSL also uses some signs derived from written Chinese character shapes', 'middle', 'L')
    s += t(240, 139, 'Iconic signs: many CSL signs visually trace Chinese characters (unique feature)', 'middle', 'L')
    s += t(240, 150, 'No established standard writing system for CSL; video-primary', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'CSL RECOGNITION')
    s += t(240, 177, 'CSL: recognized in China\'s Disability Act; taught in Deaf schools', 'middle', 'L')
    s += t(240, 188, 'CODA (China Organization of Deaf Affairs): promotes CSL standardization', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'TAIWAN SIGN LANGUAGE (TSL) NOTE')
    s += t(240, 215, 'TSL: used in Taiwan; different from CSL (separate development under Japan)', 'middle', 'L')
    s += t(240, 226, 'TSL is closer to JSL historically; CSL is mainland Chinese', 'middle', 'Ls')
    s += hr(234)
    s += sec_divider(241, 'KSL  \u00b7  SECONDARY LANGUAGE')
    s += sh(266, 'KOREAN SIGN LANGUAGE (KSL)')
    s += t(240, 277, 'KSL: ~300,000 users in South Korea; Seoul-centered', 'middle', 'L')
    s += t(240, 288, 'First school: Pyongyang (1909, Japanese colonial period); JSL influence', 'middle', 'L')
    s += t(240, 299, 'KSL developed from JSL (Japanese SL) base during colonial period (1910-1945)', 'middle', 'Ls')
    s += hr(307)
    s += sh(315, 'KSL FINGERSPELLING')
    s += t(240, 326, 'KSL: one-handed manual alphabet for hangul syllables', 'middle', 'L')
    s += t(240, 337, 'Handshapes represent Korean syllable blocks (not individual letters)', 'middle', 'L')
    s += t(240, 348, 'Very different from Western fingerspelling systems', 'middle', 'Ls')
    s += hr(356)
    s += sh(364, 'NOTATION COMPARISON')
    s += t(240, 375, 'CSL: fingerspelling based on pinyin romanization', 'middle', 'L')
    s += t(240, 386, 'KSL: fingerspelling based on hangul syllable-block system', 'middle', 'L')
    s += t(240, 397, 'Both: no standard written form; video is primary medium', 'middle', 'L')
    s += t(240, 408, 'Both: character-based scripts inform sign language notation approaches', 'middle', 'Ls')
    s += footer('65', 'CSL', 'KSL', 'a', 'NOTATION')
    s += close_svg()
    return s

def plate65b():
    s = open_svg()
    s += t(240, 28, 'CSL — CHINESE SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'CHEROLOGY — EAST ASIAN SIGN PARAMETERS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'CSL HANDSHAPES AND ICONICITY')
    s += t(240, 68, 'CSL: many signs iconic traces of Chinese characters (unique to East Asian SLs)', 'middle', 'L')
    s += t(240, 79, 'PERSON: index fingers trace human outline (universal iconic sign)', 'middle', 'L')
    s += t(240, 90, 'Numbers 1-10: one-hand Chinese number system (fist=10, etc.)', 'middle', 'L')
    s += t(240, 101, 'Number signs: widely shared across East Asia (same counting tradition)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'CSL MOVEMENT AND SPACE')
    s += t(240, 128, 'CSL: uses signing space similar to other sign languages', 'middle', 'L')
    s += t(240, 139, 'Spatial loci: same grammatical function as ASL/LSF/DGS', 'middle', 'L')
    s += t(240, 150, 'CSL: some signs more body-anchored than neutral-space-heavy ASL', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'CSL NMM')
    s += t(240, 177, 'NMM: same grammatical function (eyebrows, gaze, head movement)', 'middle', 'L')
    s += t(240, 188, 'Chinese mouthing: Mandarin words mouthed with signs (common in CSL)', 'middle', 'L')
    s += t(240, 199, 'Tonal mouthing: some signers mouth with Mandarin tones visible on face', 'middle', 'Ls')
    s += hr(207)
    s += sec_divider(214, 'KSL CHEROLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'KSL HANDSHAPES')
    s += t(240, 250, 'KSL handshapes: overlap with JSL (shared colonial-era origin)', 'middle', 'L')
    s += t(240, 261, 'Some CSL-influenced signs in KSL (historical Chinese cultural influence)', 'middle', 'L')
    s += t(240, 272, 'KSL modern development: diverged from JSL since 1945 independence', 'middle', 'Ls')
    s += hr(280)
    s += sh(288, 'KSL SPATIAL GRAMMAR')
    s += t(240, 299, 'KSL: same spatial grammar as other sign languages (universal)', 'middle', 'L')
    s += t(240, 310, 'Loci, verb agreement, classifiers: all present in KSL', 'middle', 'L')
    s += t(240, 321, 'KSL NMM: Korean mouthing common; facial grammar same as other SLs', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'EAST ASIAN SIGN LANGUAGE FEATURES')
    s += t(240, 348, 'Both CSL and KSL: number signs reflect East Asian counting system', 'middle', 'L')
    s += t(240, 359, 'Both: some signs iconic from respective written scripts', 'middle', 'L')
    s += t(240, 370, 'Both: mouthing from spoken national language frequent', 'middle', 'L')
    s += t(240, 381, 'Both: same five parameters as all sign languages (universal cherology)', 'middle', 'Ls')
    s += footer('65', 'CSL', 'KSL', 'b', 'CHEROLOGY')
    s += close_svg()
    return s

def plate65c():
    s = open_svg()
    s += t(240, 28, 'CSL — CHINESE SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — EAST ASIAN SIGN SYNTAX', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'CSL WORD ORDER')
    s += t(240, 68, 'CSL: primarily SOV word order (mirrors Mandarin Chinese)', 'middle', 'L')
    s += t(240, 79, 'PERSON BOOK GIVE: "Person gives book" (SOV structure)', 'middle', 'L')
    s += t(240, 90, 'Topic-comment also very frequent (matching Chinese spoken style)', 'middle', 'L')
    s += t(240, 101, 'Time signed first (same as spoken Chinese: time-topic then action)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'CSL VERB SYSTEM')
    s += t(240, 128, 'CSL: aspect system (same as all sign languages; no tense morphology)', 'middle', 'L')
    s += t(240, 139, 'Movement modification: repeated = habitual; slow = prolonged', 'middle', 'L')
    s += t(240, 150, 'Spatial verb agreement: directional verbs move between loci', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'CSL CLASSIFIERS')
    s += t(240, 177, 'CSL: rich classifier system (proforms) like other sign languages', 'middle', 'L')
    s += t(240, 188, 'Some classifiers: trace shapes of Chinese characters (iconic + conventional)', 'middle', 'Ls')
    s += hr(196)
    s += sh(204, 'CSL NEGATION')
    s += t(240, 215, 'Headshake: simultaneous negative NMM (same as all sign languages)', 'middle', 'L')
    s += t(240, 226, 'NO/NOT sign also used; combined = emphatic negation', 'middle', 'Ls')
    s += hr(234)
    s += sec_divider(241, 'KSL GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(266, 'KSL WORD ORDER: SOV')
    s += t(240, 277, 'KSL: SOV word order (mirrors Korean spoken grammar)', 'middle', 'L')
    s += t(240, 288, 'PERSON BOOK GIVE: same SOV order as CSL', 'middle', 'L')
    s += t(240, 299, 'Korean spoken language: SOV  \u2022  KSL: SOV (parallel influence)', 'middle', 'Ls')
    s += hr(307)
    s += sh(315, 'KSL UNIQUE GRAMMAR FEATURES')
    s += t(240, 326, 'KSL: rich use of spatial grammar (loci, agreement verbs)', 'middle', 'L')
    s += t(240, 337, 'Some Korean honorific system reflected in KSL (like Korean spoken)', 'middle', 'L')
    s += t(240, 348, 'Politeness distinctions: some signs have formal/informal variants', 'middle', 'Ls')
    s += hr(356)
    s += sh(364, 'GRAMMAR COMPARISON')
    s += t(240, 375, 'Both CSL and KSL: SOV (reflecting their respective spoken languages)', 'middle', 'L')
    s += t(240, 386, 'Both: topic-comment  \u2022  both: aspect over tense', 'middle', 'L')
    s += t(240, 397, 'Both: spatial grammar  \u2022  both: classifiers', 'middle', 'L')
    s += t(240, 408, 'SOV sign languages: DGS, CSL, KSL  \u2022  SVO sign languages: ASL, LSF, BSL', 'middle', 'Ls')
    s += footer('65', 'CSL', 'KSL', 'c', 'GRAMMAR')
    s += close_svg()
    return s

def plate65d():
    s = open_svg()
    s += t(240, 28, 'CSL — CHINESE SIGN LANGUAGE', 'middle', 'T')
    s += t(240, 40, 'HISTORY — DEAF EDUCATION IN EAST ASIA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'CSL ORIGINS')
    s += t(240, 68, '1887: C.R. Mills opens first Deaf school in China (Shanghai)', 'middle', 'L')
    s += t(240, 79, 'American missionaries brought oral + sign methods; sign language survived', 'middle', 'L')
    s += t(240, 90, '1949: PRC government standardizes education; CSL begins unification effort', 'middle', 'L')
    s += t(240, 101, '1960s: Standard CSL dictionary issued; regional varieties persist', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'CSL IN THE PEOPLE\'S REPUBLIC')
    s += t(240, 128, 'China Disabled Persons\' Federation (1988): oversees CSL standardization', 'middle', 'L')
    s += t(240, 139, 'CSL broadcasts on CCTV; sign interpreters in government events', 'middle', 'L')
    s += t(240, 150, '~20M Deaf in China; vast majority use CSL', 'middle', 'L')
    s += t(240, 161, 'Shanghai vs Beijing dialectal signs: ongoing tension in standardization', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'CHINESE DEAF CULTURE')
    s += t(240, 188, 'Deaf schools: historically boarding (same as most countries)', 'middle', 'L')
    s += t(240, 199, 'Strong Deaf community identity in major cities (Beijing, Shanghai)', 'middle', 'Ls')
    s += hr(207)
    s += sec_divider(214, 'KSL HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'KSL COLONIAL ORIGINS')
    s += t(240, 250, '1909: first Korean school for Deaf opens in Pyongyang (under Japanese rule)', 'middle', 'L')
    s += t(240, 261, 'Japanese teachers brought JSL (Japanese Sign Language) to Korea', 'middle', 'L')
    s += t(240, 272, 'KSL developed from JSL base; diverged significantly since 1945', 'middle', 'Ls')
    s += hr(280)
    s += sh(288, 'NORTH AND SOUTH KSL')
    s += t(240, 299, 'Korea divided 1945-1953: North and South Deaf communities separated', 'middle', 'L')
    s += t(240, 310, 'NKSL (North Korean): different from South KSL; diverged ~70+ years', 'middle', 'L')
    s += t(240, 321, 'South KSL: based in Seoul; officially recognized in Korea Welfare Law 2016', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'KSL RECOGNITION AND COMMUNITY')
    s += t(240, 348, '2016: KSL recognized as official language of Korea', 'middle', 'L')
    s += t(240, 359, '~300,000 KSL users; Korean Deaf Association promotes KSL', 'middle', 'L')
    s += t(240, 370, 'KSL interpreters required for government events, courts, hospitals', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'CSL AND KSL: EAST ASIAN SIBLINGS')
    s += t(240, 397, 'Both: emerged from Japanese/Western Deaf education in late 19th/early 20th c.', 'middle', 'L')
    s += t(240, 408, 'Both: SOV word order matching their spoken national languages', 'middle', 'L')
    s += t(240, 419, 'Both: officially recognized in 21st century after long advocacy', 'middle', 'L')
    s += t(240, 430, 'Both: large Deaf communities maintaining culture across political boundaries', 'middle', 'Ls')
    s += footer('65', 'CSL', 'KSL', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate65a_csl_ksl_notation_alt.svg', plate65a()),
                  ('plate65b_csl_ksl_cherology_alt.svg', plate65b()),
                  ('plate65c_csl_ksl_grammar_alt.svg', plate65c()),
                  ('plate65d_csl_ksl_history_alt.svg', plate65d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
