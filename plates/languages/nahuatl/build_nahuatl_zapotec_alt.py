# build_nahuatl_zapotec_alt.py  — Series 47 ALT  (Nahuatl + Zapotec)
# Secondary language: Zapotec (~500K speakers, Oaxaca, Mexico)
# Geographic basis: standard 500mi radius from Mexico City (19.4°N, 99.1°W)
# Oaxaca City is ~420km (~260mi) from Mexico City — well within 500mi radius
# Both: Mesoamerican civilizations; oldest writing system in the Americas (Zapotec glyphs ~500 BCE)
# Outputs: plate47a–47d_nahuatl_zapotec_*_alt.svg

from pathlib import Path

OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text { font-family: Georgia, serif; }\n'
        '  .T{font-size:11px;font-weight:bold;letter-spacing:1.5px}\n'
        '  .S{font-size:6.5px;letter-spacing:1.5px}\n'
        '  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}\n'
        '  .Hb{font-size:7px;font-weight:bold;letter-spacing:2px}\n'
        '  .L{font-size:7px} .Ls{font-size:6px} .Lx{font-size:5.5px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')

def close_svg(): return '</svg>\n'

def t(x, y, text, anchor='middle', cls='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.5):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y, label, cls='H'):
    return t(240, y, label, 'middle', cls)

def sec_divider(y, label):
    out  = hr(y, sw=1.5)
    out += f'<rect x="20" y="{y+3}" width="440" height="14" fill="black"/>\n'
    out += f'<text x="240" y="{y+13}" text-anchor="middle" class="Hb" fill="white">{esc(label)}</text>\n'
    out += hr(y+17, sw=0.3)
    return out

def footer(num, lang1, lang2, letter, desc):
    return (hr(625)
        + t(240, 620,
            f'PLATE {esc(num)}{esc(letter)} ALT \u00b7 {esc(lang1)} / {esc(lang2)}'
            f' \u00b7 {esc(desc.upper())} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG',
            'middle', 'M')
        + hr(633)
        + t(240, 648,
            'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.',
            'middle', 'Fb')
        + t(240, 663,
            'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET',
            'middle', 'F'))

# ─────────────────────────────────────────────────────────────────────────────
def build_47a_alt():
    svg = open_svg()
    svg += t(240, 32, 'NAHUATL (N\u0100HUATL) / ZAPOTEC (BENE ZAZA)', 'middle', 'T')
    svg += t(240, 44, 'UTO-AZTECAN / OTO-MANGUEAN \u00b7 MESOAMERICAN CIVILIZATIONS \u00b7 ~260MI', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 47A ALT \u00b7 SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 NAHUATL: SCRIPT & WRITING \u2014')
    svg += t(240, 89, 'Pre-conquest: pictographic / logographic glyphs in codices (screenfold books)', 'middle', 'Ls')
    svg += t(240, 100, 'Post-conquest: Latin alphabet introduced by Spanish missionaries ~1540 CE', 'middle', 'Ls')
    svg += t(240, 111, 'Classical Nahuatl uses Latin alphabet; modern dialects use modified orthographies', 'middle', 'Ls')
    svg += hr(117, sw=0.3)
    svg += sh(127, 'NAHUATL PHONOLOGY OVERVIEW')
    svg += t(240, 138, 'Consonants: /p t k kw ts tl tsh/ \u00b7 /m n/ \u00b7 /s sh/ \u00b7 /l w j h/', 'middle', 'Ls')
    svg += t(240, 149, 'Distinctive: /tl/ lateral affricate (as in Nahuatl, Quetzalcoatl, atl=water)', 'middle', 'Ls')
    svg += t(240, 160, 'Vowels: /a e i o/ \u00b7 vowel length phonemic: a vs \u0101 (different meaning)', 'middle', 'Ls')
    svg += t(240, 171, 'No tones \u00b7 stress: penultimate syllable in most cases', 'middle', 'Ls')
    svg += hr(177, sw=0.3)
    svg += sh(187, 'THE LATERAL AFFRICATE /tl/')
    svg += t(240, 198, 'Nahuatl = /na.wa.tl/ \u00b7 atl (water) = /atl/ \u00b7 metl (agave) = /metl/', 'middle', 'Ls')
    svg += t(240, 209, 'This /tl/ occurs word-finally (unique among world languages in this position)', 'middle', 'Ls')
    svg += t(240, 220, 'Quetzalcoatl = /ket.sal.ko.atl/ \u2014 feathered serpent deity of the Aztec', 'middle', 'Ls')
    svg += hr(226, sw=0.3)
    svg += sh(236, 'POLYSYNTHETIC MORPHOLOGY')
    svg += t(240, 247, 'Nahuatl packs entire sentences into one word by stacking morphemes', 'middle', 'Ls')
    svg += t(240, 258, 'Ni-tl\u0101-pia = I-something-guard: "I am guarding something"', 'middle', 'Ls')
    svg += t(240, 269, 'Ni-c-tl\u0101-zo-tla = I-it-much-love: "I love it very much"', 'middle', 'Ls')
    svg += t(240, 280, 'Incorporated nouns: ni-c-\u0101-tl-chia = I-it-water-see: "I look for water"', 'middle', 'Ls')
    svg += hr(286, sw=0.3)
    svg += sh(296, 'NAHUATL WORDS IN ENGLISH')
    svg += t(240, 307, 'chocolate (xocolatl) \u00b7 tomato (tomatl) \u00b7 avocado (ahuacatl)', 'middle', 'Ls')
    svg += t(240, 318, 'chili (chilli) \u00b7 coyote (coyotl) \u00b7 mesquite (mizquitl)', 'middle', 'Ls')
    svg += t(240, 329, 'tamale (tamalli) \u00b7 ocelot (ocelotl) \u00b7 guacamole (ahuaqa-molli)', 'middle', 'Ls')
    svg += hr(335, sw=0.3)
    svg += sh(345, 'SAMPLE WORDS')
    svg += t(240, 356, 'n\u0101hutl = clear sound/speech (origin of name) \u00b7 atl = water \u00b7 tlalli = land', 'middle', 'Ls')

    svg += sec_divider(367, 'ZAPOTEC (BENE ZAZA) \u2014 OTO-MANGUEAN \u00b7 OAXACA \u00b7 ~260MI')

    svg += sh(392, '\u2014 ZAPOTEC: SCRIPT & SOUNDS \u2014')
    svg += t(240, 403, 'Pre-Columbian: Monte Alban glyphs (~500 BCE) \u2014 OLDEST writing in the Americas', 'middle', 'Ls')
    svg += t(240, 414, 'Zapotec script: logographic/syllabic; partially deciphered; 50+ distinct symbols', 'middle', 'Ls')
    svg += t(240, 425, 'Modern: Latin alphabet with diacritics; dozens of distinct Zapotec languages', 'middle', 'Ls')
    svg += hr(431, sw=0.3)
    svg += sh(441, 'ZAPOTEC IS A LANGUAGE COMPLEX: 50+ VARIETIES')
    svg += t(240, 452, 'Zapotec is not one language but a family of ~50 mutually unintelligible varieties', 'middle', 'Ls')
    svg += t(240, 463, 'Valley Zapotec (Tlacolula) \u00b7 Sierra Juarez \u00b7 Isthmus Zapotec \u00b7 Coastal Zapotec', 'middle', 'Ls')
    svg += t(240, 474, 'Isthmus Zapotec (~70K speakers): most documented; used here as reference variety', 'middle', 'Ls')
    svg += hr(480, sw=0.3)
    svg += sh(490, 'ZAPOTEC PHONOLOGY: TONES AND LARYNGEALIZATION')
    svg += t(240, 501, '4 tones: High \u00b7 Low \u00b7 Rising \u00b7 Falling (in Isthmus Zapotec)', 'middle', 'Ls')
    svg += t(240, 512, 'Laryngealization: breathy and creaky voice add further contrast', 'middle', 'Ls')
    svg += t(240, 523, 'guela /\u0261ela/ (woman) vs guele\u2019a /\u0261ele\u0294a/ (vulture) \u2014 glottalization changes meaning', 'middle', 'Ls')
    svg += hr(529, sw=0.3)
    svg += sh(539, 'CONSONANTS')
    svg += t(240, 550, '/p b t d k g/ \u00b7 /ts dz/ \u00b7 /m n/ \u00b7 /s z sh/ \u00b7 /l r/ \u00b7 /j w/ \u00b7 glottal /?/', 'middle', 'Ls')
    svg += t(240, 561, 'Labio-velars: /kw gw/ \u00b7 Voiced fricatives contrast with voiceless', 'middle', 'Ls')
    svg += hr(567, sw=0.3)
    svg += sh(577, 'SAMPLE WORDS (ISTHMUS ZAPOTEC)')
    svg += t(240, 588, 'bene = person \u00b7 zaza = those \u00b7 guela = woman \u00b7 xhipe = man', 'middle', 'Ls')
    svg += t(240, 599, 'neza = road/path \u00b7 yoo = house \u00b7 nisado = sea (nisa=water + do=big)', 'middle', 'Ls')
    svg += t(240, 610, 'Zapotec = "people of the clouds" (Bene Za) or "people who eat beans" (folk etym.)', 'middle', 'Ls')

    svg += footer(47, 'NAHUATL', 'ZAPOTEC', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_47b_alt():
    svg = open_svg()
    svg += t(240, 32, 'NAHUATL (N\u0100HUATL) / ZAPOTEC (BENE ZAZA)', 'middle', 'T')
    svg += t(240, 44, 'UTO-AZTECAN / OTO-MANGUEAN \u00b7 PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 47B ALT \u00b7 PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 NAHUATL PHONOLOGY IN DEPTH \u2014')
    svg += sh(88, 'CONSONANT INVENTORY')
    svg += t(100, 99, 'TYPE', 'middle', 'Lx')
    svg += t(240, 99, 'CONSONANTS', 'middle', 'Lx')
    svg += t(390, 99, 'NOTES', 'middle', 'Lx')
    svg += hr(103, sw=0.3)
    svg += t(100, 112, 'Stops', 'middle', 'Ls')
    svg += t(240, 112, '/p t k kw/', 'middle', 'Ls')
    svg += t(390, 112, 'No voiced stops in Classical', 'middle', 'Ls')
    svg += t(100, 122, 'Affricates', 'middle', 'Ls')
    svg += t(240, 122, '/ts ts\u02b0 tl/', 'middle', 'Ls')
    svg += t(390, 122, 'tl = lateral affricate', 'middle', 'Ls')
    svg += t(100, 132, 'Fricatives', 'middle', 'Ls')
    svg += t(240, 132, '/s \u0283 h/', 'middle', 'Ls')
    svg += t(390, 132, 'sh = x in orthography', 'middle', 'Ls')
    svg += t(100, 142, 'Sonorants', 'middle', 'Ls')
    svg += t(240, 142, '/m n l w j/', 'middle', 'Ls')
    svg += t(390, 142, 'no /r/ in Classical Nahuatl', 'middle', 'Ls')
    svg += hr(147, sw=0.3)
    svg += sh(157, 'VOWEL LENGTH: PHONEMICALLY CONTRASTIVE')
    svg += t(240, 168, 'tl\u0101lli (land) /tla:.li/ vs tlalli (dirt/soil) /tla.li/ \u2014 length changes word', 'middle', 'Ls')
    svg += t(240, 179, 'Macron used in Classical notation: \u0101 \u0113 \u012b \u014d (long vowels)', 'middle', 'Ls')
    svg += hr(185, sw=0.3)
    svg += sh(195, 'WORD STRESS')
    svg += t(240, 206, 'Stress falls on penultimate (second-to-last) syllable', 'middle', 'Ls')
    svg += t(240, 217, 'Nahuatl /na.WA.tl/ \u00b7 quetzalli /kет.SA.li/ \u00b7 coatl /CO.atl/', 'middle', 'Ls')
    svg += hr(223, sw=0.3)
    svg += sh(233, 'REDUPLICATION IN NAHUATL')
    svg += t(240, 244, 'Reduplication encodes repetition, plurality, or intensity:', 'middle', 'Ls')
    svg += t(240, 255, 'tlal- \u2192 tlatlatl (lands, plural) \u00b7 tec- \u2192 tectecui (he cuts repeatedly)', 'middle', 'Ls')
    svg += hr(261, sw=0.3)
    svg += sh(271, 'NAHUATL NUMBERS')
    svg += t(240, 282, 'ce (1) \u00b7 ome (2) \u00b7 yei (3) \u00b7 nahui (4) \u00b7 macuilli (5)', 'middle', 'Ls')
    svg += t(240, 293, 'chicuace (6) \u00b7 chicome (7) \u00b7 chicuei (8) \u00b7 chicnahui (9) \u00b7 mahtlactli (10)', 'middle', 'Ls')
    svg += t(240, 304, 'Base-20 vigesimal counting: cempoalli (20) = one score \u00b7 400 = tzontli', 'middle', 'Ls')
    svg += hr(310, sw=0.3)
    svg += sh(320, 'NAHUATL IN MODERN SPANISH (MEXICO)')
    svg += t(240, 331, 'Mexican Spanish has ~500 Nahuatl loanwords in everyday speech:', 'middle', 'Ls')
    svg += t(240, 342, 'chapuline (grasshopper, chapolin) \u00b7 copal (incense) \u00b7 cuate (twin, friend)', 'middle', 'Ls')
    svg += t(240, 353, 'hule (rubber, ulli) \u00b7 petate (palm mat, petatl) \u00b7 escuincle (kid, itzcuintli)', 'middle', 'Ls')

    svg += sec_divider(365, 'ZAPOTEC \u2014 PHONOLOGY: TONES & CONTRASTS')

    svg += sh(390, '\u2014 ZAPOTEC PHONOLOGY: TONES IN DETAIL \u2014')
    svg += t(240, 401, 'Focus: Isthmus Zapotec (Zapotec of the Isthmus of Tehuantepec)', 'middle', 'Ls')
    svg += hr(407, sw=0.3)
    svg += sh(417, 'FOUR LEXICAL TONES')
    svg += t(100, 428, 'TONE', 'middle', 'Lx')
    svg += t(240, 428, 'CONTOUR', 'middle', 'Lx')
    svg += t(390, 428, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(432, sw=0.3)
    svg += t(100, 441, 'High', 'middle', 'Ls')
    svg += t(240, 441, 'Level high (55)', 'middle', 'Ls')
    svg += t(390, 441, 'yaga (tree) high', 'middle', 'Ls')
    svg += t(100, 451, 'Low', 'middle', 'Ls')
    svg += t(240, 451, 'Level low (11)', 'middle', 'Ls')
    svg += t(390, 451, 'yaga (table) low', 'middle', 'Ls')
    svg += t(100, 461, 'Rising', 'middle', 'Ls')
    svg += t(240, 461, 'Low-to-high (13)', 'middle', 'Ls')
    svg += t(390, 461, 'contour up', 'middle', 'Ls')
    svg += t(100, 471, 'Falling', 'middle', 'Ls')
    svg += t(240, 471, 'High-to-low (51)', 'middle', 'Ls')
    svg += t(390, 471, 'contour down', 'middle', 'Ls')
    svg += hr(476, sw=0.3)
    svg += sh(486, 'LARYNGEALIZATION: CREAKY AND BREATHY VOICE')
    svg += t(240, 497, 'Zapotec uses laryngealization as an additional phonemic dimension:', 'middle', 'Ls')
    svg += t(240, 508, 'Plain vowel: /a/ \u00b7 Creaky: /a\u0330/ \u00b7 Breathy: /a\u0324/ \u2014 three voice qualities', 'middle', 'Ls')
    svg += t(240, 519, 'Combined with 4 tones: potentially 12 vowel-tone combinations per syllable', 'middle', 'Ls')
    svg += hr(525, sw=0.3)
    svg += sh(535, 'ZAPOTEC NUMBERS')
    svg += t(240, 546, 'tobi (1) \u00b7 chupa (2) \u00b7 chonna (3) \u00b7 tapa (4) \u00b7 gayu (5)', 'middle', 'Ls')
    svg += t(240, 557, 'xhopa (6) \u00b7 gate (7) \u00b7 xhono (8) \u00b7 za (9) \u00b7 chii (10)', 'middle', 'Ls')
    svg += t(240, 568, 'Also base-20: ca-tobi (20=one score) in the traditional count system', 'middle', 'Ls')
    svg += hr(574, sw=0.3)
    svg += sh(584, 'MESOAMERICAN SHARED FEATURE: BASE-20')
    svg += t(240, 595, 'Both Nahuatl and Zapotec: base-20 (vigesimal) counting system', 'middle', 'Ls')
    svg += t(240, 606, 'Shared across Mesoamerica: Maya, Mixtec, Otomi \u2014 cultural convergence zone', 'middle', 'Ls')

    svg += footer(47, 'NAHUATL', 'ZAPOTEC', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_47c_alt():
    svg = open_svg()
    svg += t(240, 32, 'NAHUATL (N\u0100HUATL) / ZAPOTEC (BENE ZAZA)', 'middle', 'T')
    svg += t(240, 44, 'UTO-AZTECAN / OTO-MANGUEAN \u00b7 GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 47C ALT \u00b7 GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 NAHUATL GRAMMAR \u2014')
    svg += t(240, 88, 'Polysynthetic SOV \u00b7 verbs inflect for subject, object, tense, aspect, mood', 'middle', 'Ls')
    svg += t(240, 99, 'Verb is the core of the sentence; nouns may be absent (pro-drop)', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'SUBJECT PREFIXES ON VERBS')
    svg += t(100, 126, 'PREFIX', 'middle', 'Lx')
    svg += t(240, 126, 'SUBJECT', 'middle', 'Lx')
    svg += t(390, 126, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(130, sw=0.3)
    svg += t(100, 139, 'ni-', 'middle', 'Ls')
    svg += t(240, 139, '1st sg. (I)', 'middle', 'Ls')
    svg += t(390, 139, 'ni-tlahtoa (I speak)', 'middle', 'Ls')
    svg += t(100, 149, 'ti-', 'middle', 'Ls')
    svg += t(240, 149, '2nd sg. (you)', 'middle', 'Ls')
    svg += t(390, 149, 'ti-tlahtoa (you speak)', 'middle', 'Ls')
    svg += t(100, 159, '(zero)', 'middle', 'Ls')
    svg += t(240, 159, '3rd sg. (s/he/it)', 'middle', 'Ls')
    svg += t(390, 159, 'tlahtoa (s/he speaks)', 'middle', 'Ls')
    svg += t(100, 169, 'ti-...-h', 'middle', 'Ls')
    svg += t(240, 169, '1st pl. (we)', 'middle', 'Ls')
    svg += t(390, 169, 'ti-tlahtoa-h (we speak)', 'middle', 'Ls')
    svg += t(100, 179, 'an-...-h', 'middle', 'Ls')
    svg += t(240, 179, '2nd pl. (you-pl.)', 'middle', 'Ls')
    svg += t(390, 179, 'an-tlahtoa-h (y\'all speak)', 'middle', 'Ls')
    svg += hr(184, sw=0.3)
    svg += sh(194, 'OBJECT PREFIXES (ALSO ON VERB)')
    svg += t(240, 205, 'nech- (me) \u00b7 mitz- (you) \u00b7 c- (him/her/it) \u00b7 tech- (us) \u00b7 qu- (them)', 'middle', 'Ls')
    svg += t(240, 216, 'ni-c-mati = I-it-know: "I know it" \u2014 both subject and object on one verb', 'middle', 'Ls')
    svg += hr(222, sw=0.3)
    svg += sh(232, 'CORE VOCABULARY')
    svg += t(100, 243, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 243, 'NAHUATL', 'middle', 'Lx')
    svg += t(390, 243, 'NOTES', 'middle', 'Lx')
    svg += hr(247, sw=0.3)
    svg += t(100, 256, 'water', 'middle', 'Ls')
    svg += t(240, 256, 'atl', 'middle', 'Ls')
    svg += t(390, 256, 'root: a-', 'middle', 'Ls')
    svg += t(100, 266, 'person', 'middle', 'Ls')
    svg += t(240, 266, 'tlacatl', 'middle', 'Ls')
    svg += t(390, 266, 'pl. tlaca', 'middle', 'Ls')
    svg += t(100, 276, 'eat', 'middle', 'Ls')
    svg += t(240, 276, 'ni-tla-qua', 'middle', 'Ls')
    svg += t(390, 276, 'ni=I, tla=object, qua=eat', 'middle', 'Ls')
    svg += t(100, 286, 'heart', 'middle', 'Ls')
    svg += t(240, 286, 'yollo-tl', 'middle', 'Ls')
    svg += t(390, 286, 'source: yollotl', 'middle', 'Ls')
    svg += t(100, 296, 'land', 'middle', 'Ls')
    svg += t(240, 296, 'tlalli', 'middle', 'Ls')
    svg += t(390, 296, 'from tla=earth', 'middle', 'Ls')

    svg += sec_divider(308, 'ZAPOTEC \u2014 GRAMMAR & VOCABULARY')

    svg += sh(332, '\u2014 ZAPOTEC GRAMMAR \u2014')
    svg += t(240, 343, 'Word order: VSO (verb first!) \u2014 opposite of Nahuatl SOV and Spanish SVO', 'middle', 'Ls')
    svg += t(240, 354, 'Verbs: aspect-based, not tense-based \u00b7 completive vs incompletive vs potential', 'middle', 'Ls')
    svg += hr(360, sw=0.3)
    svg += sh(370, 'ASPECT IN ZAPOTEC (NOT TENSE)')
    svg += t(100, 381, 'ASPECT', 'middle', 'Lx')
    svg += t(240, 381, 'MARKER', 'middle', 'Lx')
    svg += t(390, 381, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(385, sw=0.3)
    svg += t(100, 394, 'Completive', 'middle', 'Ls')
    svg += t(240, 394, 'r(i)- prefix', 'middle', 'Ls')
    svg += t(390, 394, 'ri-gaba (s/he ate)', 'middle', 'Ls')
    svg += t(100, 404, 'Incompletive', 'middle', 'Ls')
    svg += t(240, 404, 'g(u)- prefix', 'middle', 'Ls')
    svg += t(390, 404, 'gu-gaba (s/he is eating)', 'middle', 'Ls')
    svg += t(100, 414, 'Potential', 'middle', 'Ls')
    svg += t(240, 414, 'b(i)- prefix', 'middle', 'Ls')
    svg += t(390, 414, 'bi-gaba (s/he will eat)', 'middle', 'Ls')
    svg += hr(419, sw=0.3)
    svg += sh(429, 'RELATIONAL NOUNS (NO PREPOSITIONS)')
    svg += t(240, 440, 'Zapotec uses "relational nouns" instead of prepositions:', 'middle', 'Ls')
    svg += t(240, 451, 'yoo (house) \u00b7 neza (road) \u00b7 guixi (on top of) = relational', 'middle', 'Ls')
    svg += t(240, 462, 'guixi yoo = "top-of house" = "on top of the house"', 'middle', 'Ls')
    svg += hr(468, sw=0.3)
    svg += sh(478, 'CORE VOCABULARY (ISTHMUS ZAPOTEC)')
    svg += t(100, 489, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 489, 'ZAPOTEC', 'middle', 'Lx')
    svg += t(390, 489, 'NOTES', 'middle', 'Lx')
    svg += hr(493, sw=0.3)
    svg += t(100, 502, 'water', 'middle', 'Ls')
    svg += t(240, 502, 'nisa', 'middle', 'Ls')
    svg += t(390, 502, 'nisado = sea (big water)', 'middle', 'Ls')
    svg += t(100, 512, 'person', 'middle', 'Ls')
    svg += t(240, 512, 'bene', 'middle', 'Ls')
    svg += t(390, 512, 'also: bia (person)', 'middle', 'Ls')
    svg += t(100, 522, 'eat', 'middle', 'Ls')
    svg += t(240, 522, 'gaba', 'middle', 'Ls')
    svg += t(390, 522, 'ri-gaba (ate)', 'middle', 'Ls')
    svg += t(100, 532, 'house', 'middle', 'Ls')
    svg += t(240, 532, 'yoo', 'middle', 'Ls')
    svg += t(390, 532, 'also: home, family', 'middle', 'Ls')
    svg += t(100, 542, 'heart', 'middle', 'Ls')
    svg += t(240, 542, 'guidxi', 'middle', 'Ls')
    svg += t(390, 542, 'also: soul/spirit', 'middle', 'Ls')
    svg += hr(547, sw=0.3)
    svg += sh(557, 'KEY CONTRAST: SOV vs VSO')
    svg += t(240, 568, 'Nahuatl SOV: Ni-c-qua in tamalli = I-it-eat the tamale', 'middle', 'Ls')
    svg += t(240, 579, 'Zapotec VSO: Ri-gaba Juan nisa = ate Juan water = "Juan drank water"', 'middle', 'Ls')
    svg += t(240, 590, 'Different word orders across Mesoamerica: no single template', 'middle', 'Ls')

    svg += footer(47, 'NAHUATL', 'ZAPOTEC', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_47d_alt():
    svg = open_svg()
    svg += t(240, 32, 'NAHUATL (N\u0100HUATL) / ZAPOTEC (BENE ZAZA)', 'middle', 'T')
    svg += t(240, 44, 'UTO-AZTECAN / OTO-MANGUEAN \u00b7 HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 47D ALT \u00b7 HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 NAHUATL: HISTORY & EMPIRE \u2014')
    svg += sh(88, 'THE AZTEC EMPIRE (1428\u20131521 CE)')
    svg += t(240, 99, 'Triple Alliance: Tenochtitlan + Texcoco + Tlacopan \u2014 dominated Central Mexico', 'middle', 'Ls')
    svg += t(240, 110, 'Tenochtitlan (modern Mexico City): ~200,000-300,000 people by 1500 CE', 'middle', 'Ls')
    svg += t(240, 121, 'Nahuatl became lingua franca of trade and administration across Mesoamerica', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'PRE-AZTEC NAHUATL: TOLTEC AND TEOTIHUACAN')
    svg += t(240, 148, 'Nahuatl speakers at Teotihuacan (~100 BCE\u2013600 CE): "city of the gods"', 'middle', 'Ls')
    svg += t(240, 159, 'Toltec empire (~900\u20131150 CE): predecessor to Aztec; Nahuatl as prestige language', 'middle', 'Ls')
    svg += t(240, 170, 'Quetzalcoatl: feathered serpent deity worshipped across Mesoamerica', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'CONQUEST & SURVIVAL (1521 CE)')
    svg += t(240, 197, 'Spanish conquest 1521: Hernan Cortes, allied with Tlaxcala; Tenochtitlan fell', 'middle', 'Ls')
    svg += t(240, 208, 'Nahuatl continued as administrative language under colonial rule until ~1700', 'middle', 'Ls')
    svg += t(240, 219, 'Today: ~1.7M speakers in Mexico \u00b7 Nahuatl dialects from Guerrero to Veracruz', 'middle', 'Ls')
    svg += t(240, 230, '"Mexicano": local name for Nahuatl in many communities; pride is resurgent', 'middle', 'Ls')
    svg += hr(236, sw=0.3)
    svg += sh(246, 'NAHUATL IN WORLD CUISINE')
    svg += t(240, 257, 'The Aztec market at Tlatelolco offered 200+ food varieties; Nahuatl names spread:', 'middle', 'Ls')
    svg += t(240, 268, 'chocolate (xocolatl) \u00b7 vanilla (tlilxochitl) \u00b7 chile \u00b7 tomato \u00b7 avocado', 'middle', 'Ls')
    svg += hr(274, sw=0.3)
    svg += sh(284, 'SURVIVAL PHRASE')
    svg += t(240, 295, 'Nochi in tlacah timochihua huan tiquilnamiquia in to huiptla.', 'middle', 'Ls')
    svg += t(240, 306, '"All people we-make and we-remember toward our tomorrow."', 'middle', 'Ls')
    svg += t(240, 317, '(huiptla = the day after tomorrow; used for "future" in classical texts)', 'middle', 'Ls')

    svg += sec_divider(329, 'ZAPOTEC (BENE ZAZA) \u2014 HISTORY & CULTURAL LEGACY')

    svg += sh(354, '\u2014 ZAPOTEC: THE OLDEST CIVILIZATION \u2014')
    svg += sh(365, 'MONTE ALBAN: FIRST CITY OF THE AMERICAS (~500 BCE)')
    svg += t(240, 376, 'Zapotec built Monte Alban (near modern Oaxaca City) ~500 BCE', 'middle', 'Ls')
    svg += t(240, 387, 'Population: ~25,000 at peak \u00b7 dominated Oaxaca Valley 500 BCE\u2013700 CE', 'middle', 'Ls')
    svg += t(240, 398, 'Monuments: pyramids, ball courts, astronomical alignments, carved stelae', 'middle', 'Ls')
    svg += hr(404, sw=0.3)
    svg += sh(414, 'OLDEST WRITING SYSTEM IN THE AMERICAS')
    svg += t(240, 425, 'Monte Alban glyphs (~500 BCE): carved stone monuments with proto-writing', 'middle', 'Ls')
    svg += t(240, 436, 'Danzantes: carved figures with glyphs, likely recording sacrificed captives', 'middle', 'Ls')
    svg += t(240, 447, 'Predates Maya script by ~300 years; Zapotec claim to oldest Mesoamerican writing', 'middle', 'Ls')
    svg += hr(453, sw=0.3)
    svg += sh(463, 'MIXTEC CONQUEST & ZAPOTEC RESILIENCE')
    svg += t(240, 474, '~700 CE: Monte Alban abandoned; Zapotec dispersed to regional centers', 'middle', 'Ls')
    svg += t(240, 485, 'Mixtec expansion from the west \u2014 long rivalry with Zapotec city-states', 'middle', 'Ls')
    svg += t(240, 496, '1521: Spanish conquest \u2014 Zapotec lord Cosijopii negotiated rather than fought', 'middle', 'Ls')
    svg += hr(502, sw=0.3)
    svg += sh(512, 'BENITO JUAREZ: ZAPOTEC PRESIDENT OF MEXICO')
    svg += t(240, 523, 'Benito Juarez (1806\u20131872): born in Guelatao, Oaxaca, to Zapotec parents', 'middle', 'Ls')
    svg += t(240, 534, 'Did not speak Spanish until age 12 \u00b7 became Mexico\'s greatest president', 'middle', 'Ls')
    svg += t(240, 545, '"Among individuals, as among nations, respect for others\' rights is peace."', 'middle', 'Ls')
    svg += hr(551, sw=0.3)
    svg += sh(561, 'ZAPOTEC TODAY')
    svg += t(240, 572, '~500,000 speakers across Oaxaca \u00b7 50+ mutually unintelligible varieties', 'middle', 'Ls')
    svg += t(240, 583, 'Indigenous-language instruction in some Oaxacan schools; radio stations in Zapotec', 'middle', 'Ls')
    svg += hr(589, sw=0.3)
    svg += sh(599, 'SURVIVAL PHRASE (ISTHMUS ZAPOTEC)')
    svg += t(240, 610, 'Bene neza cayaa dxi ti gunaa; bene neza dxita gunaa bia.', 'middle', 'Ls')
    svg += t(240, 621, '"Those who walk the road remember tomorrow; those ahead are remembered."', 'middle', 'Ls')

    svg += footer(47, 'NAHUATL', 'ZAPOTEC', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate47a_nahuatl_zapotec_script_alt.svg',    build_47a_alt),
        ('plate47b_nahuatl_zapotec_phonology_alt.svg',  build_47b_alt),
        ('plate47c_nahuatl_zapotec_grammar_alt.svg',    build_47c_alt),
        ('plate47d_nahuatl_zapotec_history_alt.svg',    build_47d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
