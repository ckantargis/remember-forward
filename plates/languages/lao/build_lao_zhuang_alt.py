# build_lao_zhuang_alt.py  — Series 41 ALT  (Lao + Zhuang)
# Secondary language: Zhuang (~17M speakers, Guangxi, ~400mi from Vientiane)
# Geographic basis: standard 500mi radius from Vientiane (17.97°N, 102.6°E)
# Tai-Kadai family: Lao and Zhuang are sister languages within the same family
# Outputs: plate41a–41d_lao_zhuang_*_alt.svg

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
def build_41a_alt():
    svg = open_svg()
    svg += t(240, 32, 'LAO (ພາສາລາວ) / ZHUANG (壯語 · VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'TAI-KADAI FAMILY · SISTER LANGUAGES · ~400MI APART', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 41A ALT · SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LAO SCRIPT (ອັກສອນລາວ) —')
    svg += t(240, 89, 'Abugida: each consonant carries inherent vowel /aː/ (or /o/ in closed syllables)', 'middle', 'Ls')
    svg += t(240, 100, '33 consonant letters · 28 vowel diacritic forms · written left-to-right', 'middle', 'Ls')
    svg += t(240, 111, 'Vowels placed above, below, before, or after consonant · no capital letters', 'middle', 'Ls')
    svg += t(240, 122, 'Spaces mark phrase/clause boundaries, not word boundaries', 'middle', 'Ls')
    svg += hr(128, sw=0.3)
    svg += sh(138, 'THREE CONSONANT CLASSES (govern base tone)')
    svg += t(100, 149, 'CLASS', 'middle', 'Lx')
    svg += t(240, 149, 'SAMPLE LETTERS', 'middle', 'Lx')
    svg += t(390, 149, 'BASE TONE QUALITY', 'middle', 'Lx')
    svg += hr(153, sw=0.3)
    svg += t(100, 162, 'HIGH (ສູງ)', 'middle', 'Ls')
    svg += t(240, 162, 'ຂ ຜ ຝ ຫ ສ', 'middle', 'Ls')
    svg += t(390, 162, 'Rising / high-falling', 'middle', 'Ls')
    svg += t(100, 173, 'MID (ກາງ)', 'middle', 'Ls')
    svg += t(240, 173, 'ກ ຈ ດ ຕ ບ ປ ອ', 'middle', 'Ls')
    svg += t(390, 173, 'Mid level / low', 'middle', 'Ls')
    svg += t(100, 184, 'LOW (ຕ່ຳ)', 'middle', 'Ls')
    svg += t(240, 184, 'ງ ນ ມ ວ ລ ຍ', 'middle', 'Ls')
    svg += t(390, 184, 'Low / high (with marks)', 'middle', 'Ls')
    svg += hr(189, sw=0.3)
    svg += sh(199, 'TONE MARKS (ວັນນະຍຸດ)')
    svg += t(240, 210, 'ໄມ້ເອກ ( ່ ) and ໄມ້ໂທ ( ້ ) placed above consonant', 'middle', 'Ls')
    svg += t(240, 221, 'Consonant class + tone mark = one of 6 tones', 'middle', 'Ls')
    svg += t(240, 232, '6 tones: mid · low · falling · high · rising · high-rising', 'middle', 'Ls')
    svg += hr(238, sw=0.3)
    svg += sh(248, 'VOWEL PLACEMENT EXAMPLES')
    svg += t(240, 259, 'ກາ /kaː/ (crow)  ·  ກິ /ki/ (to eat)  ·  ເກ /keː/ (honor)', 'middle', 'Ls')
    svg += t(240, 270, 'ແກ /kɛː/ (goat)  ·  ໂກ /koː/ (deceive)  ·  ກົ /ko/ (neck)', 'middle', 'Ls')
    svg += hr(276, sw=0.3)
    svg += sh(286, 'SCRIPT ORIGIN')
    svg += t(240, 297, 'Derived from Old Khmer script · introduced ~14th c. CE · Lan Xang Kingdom', 'middle', 'Ls')
    svg += t(240, 308, 'Ancestry: Brahmi (India ~3rd c. BCE) → Mon → Khmer → Lao', 'middle', 'Ls')
    svg += t(240, 319, 'Related scripts: Thai · Khmer — share same consonant-class tone system', 'middle', 'Ls')
    svg += hr(325, sw=0.3)
    svg += sh(335, 'SAMPLE WORDS')
    svg += t(240, 346, 'ສະຫວັດດີ /sa.wàt.diː/ hello  ·  ຂອບໃຈ /khɔ̀ːp tɕaːj/ thank you', 'middle', 'Ls')

    svg += sec_divider(357, 'ZHUANG (壯語 VAHCUENGH) — TAI-KADAI SISTER · GUANGXI, CHINA')

    svg += sh(385, '— ZHUANG SCRIPTS: SAWNDIP & LATIN —')
    svg += t(240, 397, 'SAWNDIP (方块壮字): traditional logographic script ~1,000+ years old', 'middle', 'Ls')
    svg += t(240, 408, 'Borrows and invents Chinese-character forms for Zhuang sounds and meanings', 'middle', 'Ls')
    svg += t(240, 419, 'Not standardized; regional variants; preserved in ritual texts and folk songs', 'middle', 'Ls')
    svg += hr(425, sw=0.3)
    svg += sh(435, 'ZHUANG LATIN ALPHABET (SAWCUENGH)')
    svg += t(240, 447, 'Standardized 1957, revised 1982 · 26 letters + digraphs (mb, nd, ng, nj...)', 'middle', 'Ls')
    svg += t(240, 458, 'Tones marked by suffix letters appended to syllable (no diacritics)', 'middle', 'Ls')
    svg += hr(464, sw=0.3)
    svg += sh(474, 'TONE SUFFIXES IN ZHUANG LATIN')
    svg += t(100, 484, 'SUFFIX', 'middle', 'Lx')
    svg += t(240, 484, 'TONE', 'middle', 'Lx')
    svg += t(390, 484, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(488, sw=0.3)
    svg += t(100, 497, '(none)', 'middle', 'Ls')
    svg += t(240, 497, 'Tone 1 — mid level', 'middle', 'Ls')
    svg += t(390, 497, 'ma (horse)', 'middle', 'Ls')
    svg += t(100, 507, '-b', 'middle', 'Ls')
    svg += t(240, 507, 'Tone 2 — low rising', 'middle', 'Ls')
    svg += t(390, 507, 'mab (son)', 'middle', 'Ls')
    svg += t(100, 517, '-x', 'middle', 'Ls')
    svg += t(240, 517, 'Tone 3 — mid falling', 'middle', 'Ls')
    svg += t(390, 517, 'max (sesame)', 'middle', 'Ls')
    svg += t(100, 527, '-j', 'middle', 'Ls')
    svg += t(240, 527, 'Tone 4 — high level', 'middle', 'Ls')
    svg += t(390, 527, 'maj (come)', 'middle', 'Ls')
    svg += t(100, 537, '-q / -h', 'middle', 'Ls')
    svg += t(240, 537, 'Tones 5–6 — checked / low', 'middle', 'Ls')
    svg += t(390, 537, 'maq / mah', 'middle', 'Ls')
    svg += hr(543, sw=0.3)
    svg += sh(553, 'SAMPLE VOCABULARY')
    svg += t(240, 565, 'vah = word/speech  ·  miz = have  ·  mbouj = not  ·  raeuz = we', 'middle', 'Ls')
    svg += t(240, 576, 'gij = what/which  ·  ndaej = can/obtain  ·  aeu = want/take', 'middle', 'Ls')
    svg += hr(582, sw=0.3)
    svg += sh(592, 'SHARED ANCESTRY')
    svg += t(240, 604, 'Lao and Zhuang share Proto-Tai roots: cognate words for numbers, body, kin', 'middle', 'Ls')
    svg += t(240, 615, 'Mutual intelligibility is LOW after centuries of divergence — ancestry is shared', 'middle', 'Ls')

    svg += footer(41, 'LAO', 'ZHUANG', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_41b_alt():
    svg = open_svg()
    svg += t(240, 32, 'LAO (ພາສາລາວ) / ZHUANG (壯語 · VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'TAI-KADAI FAMILY · PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 41B ALT · PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LAO PHONOLOGY —')
    svg += sh(88, 'SIX TONES OF LAO')
    svg += t(90, 99, 'TONE', 'start', 'Lx')
    svg += t(210, 99, 'MARK / CLASS', 'start', 'Lx')
    svg += t(340, 99, 'EXAMPLE', 'start', 'Lx')
    svg += hr(103, sw=0.3)
    svg += t(90, 112, '1. Mid level (ສາມັນ)', 'start', 'Ls')
    svg += t(210, 112, 'Low-class, no mark', 'start', 'Ls')
    svg += t(340, 112, 'ຂ້າວ /kʰâːw/ rice', 'start', 'Ls')
    svg += t(90, 122, '2. Low level (ເອກ)', 'start', 'Ls')
    svg += t(210, 122, 'Mid-class + ່', 'start', 'Ls')
    svg += t(340, 122, 'ກ່າ /kàː/ to kill', 'start', 'Ls')
    svg += t(90, 132, '3. Falling (ໂທ)', 'start', 'Ls')
    svg += t(210, 132, 'Mid-class + ້', 'start', 'Ls')
    svg += t(340, 132, 'ກ້າ /kâː/ brave', 'start', 'Ls')
    svg += t(90, 142, '4. High level (ຕີ)', 'start', 'Ls')
    svg += t(210, 142, 'High-class, no mark', 'start', 'Ls')
    svg += t(340, 142, 'ຂາ /kʰáː/ leg', 'start', 'Ls')
    svg += t(90, 152, '5. Rising (ຈັດຕະວາ)', 'start', 'Ls')
    svg += t(210, 152, 'Low-class + ່', 'start', 'Ls')
    svg += t(340, 152, 'ງ່ານ /ŋân/ work', 'start', 'Ls')
    svg += t(90, 162, '6. High-rising (ສູງ)', 'start', 'Ls')
    svg += t(210, 162, 'Low-class + ້', 'start', 'Ls')
    svg += t(340, 162, 'ງ້ານ /ŋâːn/ sesame', 'start', 'Ls')
    svg += hr(167, sw=0.3)
    svg += sh(177, 'VOWELS: LENGTH IS PHONEMIC')
    svg += t(240, 188, 'Short: ກິ /ki/ · Long: ກີ /kiː/ — different meaning; 18 vowel nuclei', 'middle', 'Ls')
    svg += t(240, 199, 'Vowel length + tone + consonant class = full syllable identity', 'middle', 'Ls')
    svg += hr(205, sw=0.3)
    svg += sh(215, 'CONSONANTS')
    svg += t(240, 226, 'Initial consonants: /p pʰ b/ · /t tʰ d/ · /k kʰ/ · /m n ŋ/ · /f s h/', 'middle', 'Ls')
    svg += t(240, 237, 'Final consonants: only sonorants + /k p t/ allowed — no final fricatives', 'middle', 'Ls')
    svg += t(240, 248, 'No consonant clusters in initial position (unlike Thai clusters: /kl pr tr/)', 'middle', 'Ls')
    svg += hr(254, sw=0.3)
    svg += sh(264, 'MORA TIMING & SYLLABLE STRUCTURE')
    svg += t(240, 275, 'Lao is syllable-timed · (C)(G)V(V)(C) structure · G = glide /w j/', 'middle', 'Ls')
    svg += t(240, 286, 'Open syllables (no final): most common · closed syllables restrict final Cs', 'middle', 'Ls')
    svg += hr(292, sw=0.3)
    svg += sh(302, 'MINIMAL TONE PAIRS')
    svg += t(240, 313, 'ກາ /kaː/ crow  vs  ກ້າ /kâː/ brave  vs  ກ່າ /kàː/ to kill', 'middle', 'Ls')
    svg += t(240, 324, 'ຂາ /kʰáː/ leg  vs  ຂ່າ /kʰâː/ galangal  vs  ຂ້າ /kʰàː/ slave', 'middle', 'Ls')
    svg += t(240, 335, 'Tone is the ONLY difference — a single mark changes meaning entirely', 'middle', 'Ls')

    svg += sec_divider(347, 'ZHUANG (VAHCUENGH) — PHONOLOGY · TAI-KADAI SISTER')

    svg += sh(373, '— ZHUANG PHONOLOGY: NORTHERN ZHUANG STANDARD —')
    svg += sh(384, 'SIX TONES (STANDARD ZHUANG LATIN ENCODING)')
    svg += t(90, 395, 'SUFFIX', 'start', 'Lx')
    svg += t(200, 395, 'CONTOUR', 'start', 'Lx')
    svg += t(320, 395, 'EXAMPLE & GLOSS', 'start', 'Lx')
    svg += hr(399, sw=0.3)
    svg += t(90, 408, '(none) T1', 'start', 'Ls')
    svg += t(200, 408, 'Mid level 33', 'start', 'Ls')
    svg += t(320, 408, 'sa (three)', 'start', 'Ls')
    svg += t(90, 418, '-b  T2', 'start', 'Ls')
    svg += t(200, 418, 'Low rising 13', 'start', 'Ls')
    svg += t(320, 418, 'saeb (receive)', 'start', 'Ls')
    svg += t(90, 428, '-x  T3', 'start', 'Ls')
    svg += t(200, 428, 'High falling 53', 'start', 'Ls')
    svg += t(320, 428, 'sax (narrow)', 'start', 'Ls')
    svg += t(90, 438, '-j  T4', 'start', 'Ls')
    svg += t(200, 438, 'High level 55', 'start', 'Ls')
    svg += t(320, 438, 'saj (thin)', 'start', 'Ls')
    svg += t(90, 448, '-q  T5', 'start', 'Ls')
    svg += t(200, 448, 'Mid rising 35', 'start', 'Ls')
    svg += t(320, 448, 'saq (die, checked)', 'start', 'Ls')
    svg += t(90, 458, '-h  T6', 'start', 'Ls')
    svg += t(200, 458, 'Low level 11', 'start', 'Ls')
    svg += t(320, 458, 'sah (scatter)', 'start', 'Ls')
    svg += hr(464, sw=0.3)
    svg += sh(474, 'CONSONANTS & CLUSTERS')
    svg += t(240, 485, 'Zhuang preserves Proto-Tai clusters: mb- nd- nj- ng- (pre-nasalized stops)', 'middle', 'Ls')
    svg += t(240, 496, 'mbouj /m̩bou/ = not  ·  ndaej /n̩dai/ = obtain', 'middle', 'Ls')
    svg += t(240, 507, 'Pre-nasalization: a shared Tai-Kadai feature, reduced in modern Lao/Thai', 'middle', 'Ls')
    svg += hr(513, sw=0.3)
    svg += sh(523, 'PROTO-TAI COGNATES: LAO ↔ ZHUANG')
    svg += t(100, 533, 'MEANING', 'middle', 'Lx')
    svg += t(240, 533, 'LAO', 'middle', 'Lx')
    svg += t(370, 533, 'ZHUANG', 'middle', 'Lx')
    svg += hr(537, sw=0.3)
    svg += t(100, 546, 'water', 'middle', 'Ls')
    svg += t(240, 546, 'ນ້ຳ /náːm/', 'middle', 'Ls')
    svg += t(370, 546, 'raemx', 'middle', 'Ls')
    svg += t(100, 556, 'fish', 'middle', 'Ls')
    svg += t(240, 556, 'ປາ /paː/', 'middle', 'Ls')
    svg += t(370, 556, 'bya', 'middle', 'Ls')
    svg += t(100, 566, 'rice (cooked)', 'middle', 'Ls')
    svg += t(240, 566, 'ເຂົ້າ /kʰâw/', 'middle', 'Ls')
    svg += t(370, 566, 'haeux', 'middle', 'Ls')
    svg += t(100, 576, 'sky/heaven', 'middle', 'Ls')
    svg += t(240, 576, 'ຟ້າ /fáː/', 'middle', 'Ls')
    svg += t(370, 576, 'mbwn', 'middle', 'Ls')
    svg += hr(581, sw=0.3)
    svg += sh(591, 'PHONOLOGICAL KEY DIFFERENCE')
    svg += t(240, 602, 'Lao /f/ → Zhuang /v/ in many cognates (common Tai-Kadai shift)', 'middle', 'Ls')
    svg += t(240, 613, 'Both lack /r/ as native phoneme; /l/ serves initial liquid position in Lao', 'middle', 'Ls')

    svg += footer(41, 'LAO', 'ZHUANG', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_41c_alt():
    svg = open_svg()
    svg += t(240, 32, 'LAO (ພາສາລາວ) / ZHUANG (壯語 · VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'TAI-KADAI FAMILY · GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 41C ALT · GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LAO GRAMMAR —')
    svg += t(240, 88, 'Word order: SVO · no inflection for case, number, or grammatical gender', 'middle', 'Ls')
    svg += t(240, 99, 'Verbs do not conjugate for person or tense; aspect marked by particles', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'ASPECT PARTICLES (NOT TENSE)')
    svg += t(100, 126, 'PARTICLE', 'middle', 'Lx')
    svg += t(240, 126, 'FUNCTION', 'middle', 'Lx')
    svg += t(390, 126, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(130, sw=0.3)
    svg += t(100, 139, 'ໄດ້ /dâːj/', 'middle', 'Ls')
    svg += t(240, 139, 'Completed action (past)', 'middle', 'Ls')
    svg += t(390, 139, 'ຂ້ອຍ ໄດ້ ກິນ (I ate)', 'middle', 'Ls')
    svg += t(100, 149, 'ຈະ /tɕaʔ/', 'middle', 'Ls')
    svg += t(240, 149, 'Future / intention', 'middle', 'Ls')
    svg += t(390, 149, 'ຂ້ອຍ ຈະ ໄປ (I will go)', 'middle', 'Ls')
    svg += t(100, 159, 'ກຳລັງ /kam.laŋ/', 'middle', 'Ls')
    svg += t(240, 159, 'Ongoing (progressive)', 'middle', 'Ls')
    svg += t(390, 159, 'ກຳລັງ ກິນ (is eating)', 'middle', 'Ls')
    svg += hr(164, sw=0.3)
    svg += sh(174, 'NEGATION & QUESTIONS')
    svg += t(240, 185, 'Negation: ບໍ່ /bɔː/ before verb · ບໍ່ດີ = not good · ຂ້ອຍ ບໍ່ໄປ = I not go', 'middle', 'Ls')
    svg += t(240, 196, 'Yes/no question: add ບໍ /bɔː/ at end · ເຈົ້າໄປ ບໍ? = Are you going?', 'middle', 'Ls')
    svg += t(240, 207, 'WH-questions: question word in situ (same position as answer)', 'middle', 'Ls')
    svg += hr(213, sw=0.3)
    svg += sh(223, 'CLASSIFIERS (USED WITH ALL NOUNS + NUMBERS)')
    svg += t(240, 234, 'ຄົນ /kʰon/ humans · ໂຕ /toː/ animals · ອັນ /an/ small objects', 'middle', 'Ls')
    svg += t(240, 245, 'ສາມ ຄົນ = 3 people · ສອງ ໂຕ = 2 animals (not *ສາມ ຄົນ without clf)', 'middle', 'Ls')
    svg += hr(251, sw=0.3)
    svg += sh(261, 'CORE VOCABULARY')
    svg += t(100, 272, 'LGLOSS', 'middle', 'Lx')
    svg += t(240, 272, 'LAO', 'middle', 'Lx')
    svg += t(390, 272, 'ROMANIZATION', 'middle', 'Lx')
    svg += hr(276, sw=0.3)
    svg += t(100, 285, 'I / me', 'middle', 'Ls')
    svg += t(240, 285, 'ຂ້ອຍ', 'middle', 'Ls')
    svg += t(390, 285, '/kʰɔːj/', 'middle', 'Ls')
    svg += t(100, 295, 'you (sg.)', 'middle', 'Ls')
    svg += t(240, 295, 'ເຈົ້າ', 'middle', 'Ls')
    svg += t(390, 295, '/tɕâw/', 'middle', 'Ls')
    svg += t(100, 305, 'eat', 'middle', 'Ls')
    svg += t(240, 305, 'ກິນ', 'middle', 'Ls')
    svg += t(390, 305, '/kin/', 'middle', 'Ls')
    svg += t(100, 315, 'water', 'middle', 'Ls')
    svg += t(240, 315, 'ນ້ຳ', 'middle', 'Ls')
    svg += t(390, 315, '/náːm/', 'middle', 'Ls')
    svg += t(100, 325, 'where?', 'middle', 'Ls')
    svg += t(240, 325, 'ໃສ', 'middle', 'Ls')
    svg += t(390, 325, '/sǎj/ (at end)', 'middle', 'Ls')

    svg += sec_divider(337, 'ZHUANG (VAHCUENGH) — GRAMMAR & VOCABULARY')

    svg += sh(362, '— ZHUANG GRAMMAR —')
    svg += t(240, 373, 'Word order: SVO — same as Lao · no grammatical gender · no inflection', 'middle', 'Ls')
    svg += t(240, 384, 'Aspect particles function similarly to Lao; tense context-dependent', 'middle', 'Ls')
    svg += hr(390, sw=0.3)
    svg += sh(400, 'NEGATION & QUESTIONS')
    svg += t(240, 411, 'Negation: mbouj (main) · mbouj ndaej = cannot · mbouj miz = have-not', 'middle', 'Ls')
    svg += t(240, 422, 'Yes/no: add lwi/maz at end · Gou bae lwi? = Did I go?', 'middle', 'Ls')
    svg += hr(428, sw=0.3)
    svg += sh(438, 'CLASSIFIERS (PARALLEL TO LAO)')
    svg += t(240, 449, 'boux: humans · duz: animals · aen: small round objects · goenq: long obj.', 'middle', 'Ls')
    svg += t(240, 460, 'sam boux vunz = three (clf) people — classifier required same as Lao', 'middle', 'Ls')
    svg += hr(466, sw=0.3)
    svg += sh(476, 'CORE VOCABULARY (LATIN SCRIPT)')
    svg += t(100, 487, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 487, 'ZHUANG (LATIN)', 'middle', 'Lx')
    svg += t(390, 487, 'PROTO-TAI LINK', 'middle', 'Lx')
    svg += hr(491, sw=0.3)
    svg += t(100, 500, 'I / me', 'middle', 'Ls')
    svg += t(240, 500, 'gou', 'middle', 'Ls')
    svg += t(390, 500, '*ku (Proto-Tai)', 'middle', 'Ls')
    svg += t(100, 510, 'you (sg.)', 'middle', 'Ls')
    svg += t(240, 510, 'mwngz', 'middle', 'Ls')
    svg += t(390, 510, '*muŋ (Proto-Tai)', 'middle', 'Ls')
    svg += t(100, 520, 'eat', 'middle', 'Ls')
    svg += t(240, 520, 'gwn', 'middle', 'Ls')
    svg += t(390, 520, 'cf. Lao ກິນ /kin/', 'middle', 'Ls')
    svg += t(100, 530, 'water', 'middle', 'Ls')
    svg += t(240, 530, 'raemx', 'middle', 'Ls')
    svg += t(390, 530, 'cf. Lao ນ້ຳ /náːm/', 'middle', 'Ls')
    svg += t(100, 540, 'not', 'middle', 'Ls')
    svg += t(240, 540, 'mbouj', 'middle', 'Ls')
    svg += t(390, 540, 'cf. Lao ບໍ່ /bɔː/', 'middle', 'Ls')
    svg += t(100, 550, 'good', 'middle', 'Ls')
    svg += t(240, 550, 'ndei', 'middle', 'Ls')
    svg += t(390, 550, 'cf. Lao ດີ /diː/', 'middle', 'Ls')
    svg += hr(556, sw=0.3)
    svg += sh(566, 'GRAMMATICAL PARALLEL: SERIAL VERB')
    svg += t(240, 578, 'Both Lao and Zhuang use serial verb constructions freely:', 'middle', 'Ls')
    svg += t(240, 589, 'Lao: ຂ້ອຍ ໄປ ຊື້ ເຂົ້າ (I go buy rice) — two verbs in sequence', 'middle', 'Ls')
    svg += t(240, 600, 'Zhuang: Gou bae cawx haeux (I go buy rice) — same structure', 'middle', 'Ls')
    svg += t(240, 612, 'Serial verbs: a classic Tai-Kadai syntactic signature', 'middle', 'Ls')

    svg += footer(41, 'LAO', 'ZHUANG', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_41d_alt():
    svg = open_svg()
    svg += t(240, 32, 'LAO (ພາສາລາວ) / ZHUANG (壯語 · VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'TAI-KADAI FAMILY · HISTORY & SHARED HERITAGE', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 41D ALT · HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LAO: HISTORY & LITERARY TRADITION —')
    svg += sh(88, 'LAN XANG KINGDOM (~1353–1707 CE)')
    svg += t(240, 99, '"Land of a Million Elephants" — unified Lao-speaking peoples of the Mekong valley', 'middle', 'Ls')
    svg += t(240, 110, 'Script and Theravada Buddhism arrived together; temples became literacy centers', 'middle', 'Ls')
    svg += t(240, 121, 'Classical literature: Phra Lak Phra Lam (Lao Ramayana), Sin Xay epic poem', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'COLONIAL PERIOD & MODERN NATION')
    svg += t(240, 148, 'French Indochina 1893–1953 · Lao language suppressed in favor of French', 'middle', 'Ls')
    svg += t(240, 159, 'Independence 1953 · Pathet Lao 1975 → Lao PDR (People\'s Democratic Republic)', 'middle', 'Ls')
    svg += t(240, 170, 'Lao declared sole official language; Lao script standardized under socialist policy', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'ISAN: THE INVISIBLE 23 MILLION')
    svg += t(240, 197, 'Isan dialect (NE Thailand): ~23M speakers of a Lao variety, not called "Lao"', 'middle', 'Ls')
    svg += t(240, 208, 'Written in Thai script · politically Thai · linguistically Lao', 'middle', 'Ls')
    svg += t(240, 219, 'More native Lao-speakers live in Thailand than in Laos itself', 'middle', 'Ls')
    svg += hr(225, sw=0.3)
    svg += sh(235, 'LAO TRADITIONAL MUSIC & ORAL POETRY')
    svg += t(240, 246, 'Mor lam: traditional sung poetry form; mɔː = expert, lam = to sing', 'middle', 'Ls')
    svg += t(240, 257, 'Competitions feature improvised verse in call-and-response format', 'middle', 'Ls')
    svg += t(240, 268, 'Instrument: khaen (bamboo mouth organ) — UNESCO intangible heritage (2017)', 'middle', 'Ls')
    svg += hr(274, sw=0.3)
    svg += sh(284, 'SURVIVAL PHRASE')
    svg += t(240, 295, 'ຂ້ອຍ ຮຽນ ພາສາ ລາວ · /kʰɔːj hian pʰaːsaː laːw/', 'middle', 'Ls')
    svg += t(240, 306, '"I am studying the Lao language"', 'middle', 'Ls')
    svg += t(240, 317, 'ຍິນດີທີ່ໄດ້ຮູ້ຈັກ · Nice to meet you (lit. "glad to have met")', 'middle', 'Ls')

    svg += sec_divider(329, 'ZHUANG (VAHCUENGH) — HISTORY & CULTURAL LEGACY')

    svg += sh(354, '— ZHUANG: HISTORY & IDENTITY —')
    svg += sh(365, 'INDIGENOUS PRESENCE: 5,000+ YEARS IN GUANGXI')
    svg += t(240, 376, 'Zhuang are the largest ethnic minority in China (~17M) · Guangxi home for millennia', 'middle', 'Ls')
    svg += t(240, 387, 'Ancient Luoyue/Baiyue peoples identified as Zhuang ancestors', 'middle', 'Ls')
    svg += t(240, 398, 'Bronze drum tradition (~700 BCE): still used in ritual; UNESCO intangible heritage', 'middle', 'Ls')
    svg += hr(404, sw=0.3)
    svg += sh(414, 'SAWNDIP: SCRIPT AS CULTURAL MEMORY')
    svg += t(240, 425, 'Sawndip (~方块壮字) developed ~10th c. CE · over 10,000 characters documented', 'middle', 'Ls')
    svg += t(240, 436, 'Used for Zhuang folk songs (baeuqrox), rituals, and epics — not official literacy', 'middle', 'Ls')
    svg += t(240, 447, 'Each village may use different character forms — no central standardization', 'middle', 'Ls')
    svg += hr(453, sw=0.3)
    svg += sh(463, 'GUANGXI ZHUANG AUTONOMOUS REGION (1958)')
    svg += t(240, 474, 'Established 1958 under PRC minority-nationality policy', 'middle', 'Ls')
    svg += t(240, 485, 'Zhuang Latin alphabet created 1957 for mass literacy — revised 1982', 'middle', 'Ls')
    svg += t(240, 496, 'Today: Mandarin dominant in education; Zhuang taught in some primary schools', 'middle', 'Ls')
    svg += hr(502, sw=0.3)
    svg += sh(512, 'FOLK SONG TRADITION: LIUGONG MOUNTAIN FESTIVAL')
    svg += t(240, 523, 'Third day of third lunar month: Liu Sanjie ("Third Sister Liu") festival', 'middle', 'Ls')
    svg += t(240, 534, 'Antiphonal singing (haj) between villages: a living oral literature tradition', 'middle', 'Ls')
    svg += t(240, 545, 'Liu Sanjie legend: peasant woman who sang truth to power, became immortal', 'middle', 'Ls')
    svg += hr(551, sw=0.3)
    svg += sh(561, 'THE TAI-KADAI CONTINUUM')
    svg += t(240, 572, 'Zhuang · Lao · Thai · Shan · Dai · Tay-Nung · Bouyei — all Tai-Kadai', 'middle', 'Ls')
    svg += t(240, 583, 'Scattered across S. China, Laos, Thailand, Vietnam, NE India — 100M+ speakers', 'middle', 'Ls')
    svg += hr(589, sw=0.3)
    svg += sh(599, 'SURVIVAL PHRASE (ZHUANG LATIN)')
    svg += t(240, 611, 'Gou roxnyinh Vahcuengh · "I understand (know) the Zhuang language"', 'middle', 'Ls')

    svg += footer(41, 'LAO', 'ZHUANG', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate41a_lao_zhuang_script_alt.svg',    build_41a_alt),
        ('plate41b_lao_zhuang_phonology_alt.svg',  build_41b_alt),
        ('plate41c_lao_zhuang_grammar_alt.svg',    build_41c_alt),
        ('plate41d_lao_zhuang_history_alt.svg',    build_41d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
