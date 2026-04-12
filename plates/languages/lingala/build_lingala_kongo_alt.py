# build_lingala_kongo_alt.py  — Series 33 ALT  (Lingala + Kongo/Kikongo)
# Secondary language: Kongo (Kikongo) ~10M speakers, SW DRC/Angola/Rep. of Congo
# Geographic basis: standard 500mi radius from Kinshasa (4.32°S, 15.32°E)
# Kongo homeland (Bas-Congo/Kongo Central) is within ~200mi of Kinshasa
# Both are Bantu languages; Kongo is the historic source of much of Lingala's vocabulary
# Outputs: plate33a–33d_lingala_kongo_*_alt.svg

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
def build_33a_alt():
    svg = open_svg()
    svg += t(240, 32, 'LINGALA / KONGO (KIKONGO)', 'middle', 'T')
    svg += t(240, 44, 'BANTU FAMILY · CONGO BASIN · ~200MI APART', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 33A ALT · SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LINGALA: SCRIPT & PHONOLOGY OVERVIEW —')
    svg += t(240, 89, 'Latin alphabet + 4 tone-marked vowels: e\u0301 o\u0301 e\u0300 o\u0300 (high/low marked)', 'middle', 'Ls')
    svg += t(240, 100, 'In practice: tones often unmarked in everyday writing — context + Bantu rules', 'middle', 'Ls')
    svg += t(240, 111, '~35 consonant-vowel phonemes · 5 vowels /a e i o u/ · open syllable preference', 'middle', 'Ls')
    svg += hr(117, sw=0.3)
    svg += sh(127, 'LINGALA CONSONANTS (SELECTED)')
    svg += t(240, 138, '/p b t d k g/ · /m n/ · /f v s z/ · /l/ · prenasalized: /mb nd ng nz/', 'middle', 'Ls')
    svg += t(240, 149, 'Prenasalized stops: mb- nd- ng- nz- are SINGLE phonemes, not clusters', 'middle', 'Ls')
    svg += t(240, 160, 'e.g. mboka (village) · ndeko (sibling) · ngai (I/me) · nzela (road/path)', 'middle', 'Ls')
    svg += hr(166, sw=0.3)
    svg += sh(176, 'TONES: TWO LEVELS (HIGH AND LOW)')
    svg += t(240, 187, 'Lingala has 2 contrastive tones: HIGH (H) and LOW (L)', 'middle', 'Ls')
    svg += t(240, 198, 'Tone is grammatically significant: changes meaning AND grammatical function', 'middle', 'Ls')
    svg += t(240, 209, 'motema (heart, L-H-L) vs motema (love/desire — same word, context distinguishes)', 'middle', 'Ls')
    svg += t(240, 220, 'Verb tense/aspect can be distinguished by tone pattern alone', 'middle', 'Ls')
    svg += hr(226, sw=0.3)
    svg += sh(236, 'SYLLABLE STRUCTURE')
    svg += t(240, 247, 'Lingala is open-syllable dominant: CV pattern preferred (ba-na na-na ko-be-ya)', 'middle', 'Ls')
    svg += t(240, 258, 'No consonant clusters · nasal prefix Ng- always syllabic', 'middle', 'Ls')
    svg += hr(264, sw=0.3)
    svg += sh(274, 'NOUN CLASS SYSTEM (7 CLASSES)')
    svg += t(100, 285, 'PREFIX', 'middle', 'Lx')
    svg += t(240, 285, 'CLASS / MEANING', 'middle', 'Lx')
    svg += t(390, 285, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(289, sw=0.3)
    svg += t(100, 298, 'mo- / mi-', 'middle', 'Ls')
    svg += t(240, 298, 'Class 1/2: people (sg./pl.)', 'middle', 'Ls')
    svg += t(390, 298, 'moto / bato (person/people)', 'middle', 'Ls')
    svg += t(100, 308, 'e- / bi-', 'middle', 'Ls')
    svg += t(240, 308, 'Class 7/8: objects', 'middle', 'Ls')
    svg += t(390, 308, 'eloko / biloko (thing/things)', 'middle', 'Ls')
    svg += t(100, 318, 'li- / ma-', 'middle', 'Ls')
    svg += t(240, 318, 'Class 5/6: body parts, abstracts', 'middle', 'Ls')
    svg += t(390, 318, 'liso / miso (eye/eyes)', 'middle', 'Ls')
    svg += t(100, 328, 'lo-', 'middle', 'Ls')
    svg += t(240, 328, 'Class 11: liquids, slender objects', 'middle', 'Ls')
    svg += t(390, 328, 'lopango (fence)', 'middle', 'Ls')
    svg += hr(333, sw=0.3)
    svg += sh(343, 'SAMPLE WORDS')
    svg += t(240, 354, 'mbote (hello) · matondi (thank you) · ngai (I/me) · yo (you)', 'middle', 'Ls')

    svg += sec_divider(365, 'KONGO (KIKONGO) — BANTU · SW DRC / ANGOLA · ~200MI')

    svg += sh(390, '— KONGO: SCRIPT & PHONOLOGY —')
    svg += t(240, 401, 'Latin alphabet standardized during Belgian/Portuguese colonial period', 'middle', 'Ls')
    svg += t(240, 412, 'Modern orthography: K replaces C/Q; diacritics mark tones in scholarly texts', 'middle', 'Ls')
    svg += t(240, 423, 'THREE CONTRASTIVE TONES: High · Mid · Low (more complex than Lingala)', 'middle', 'Ls')
    svg += hr(429, sw=0.3)
    svg += sh(439, 'KONGO CONSONANTS')
    svg += t(240, 450, '/p b t d k g/ · /m n/ · /f v s z/ · prenasalized: /mb nd ng nz/', 'middle', 'Ls')
    svg += t(240, 461, 'Also: /nk/, /mv/, /nts/ — richer prenasalized inventory than Lingala', 'middle', 'Ls')
    svg += t(240, 472, 'Shared feature with Lingala: prenasalized stops as single phonemes', 'middle', 'Ls')
    svg += hr(478, sw=0.3)
    svg += sh(488, 'NOUN CLASS SYSTEM: 15 CLASSES')
    svg += t(240, 499, 'Kongo preserves 15 Bantu noun classes (vs Lingala\'s simplified 7)', 'middle', 'Ls')
    svg += t(240, 510, 'muntu (person) · bantu (people) — the root "ntu" = entity/being', 'middle', 'Ls')
    svg += t(240, 521, '"Bantu" literally means "people" — the name of the entire language family', 'middle', 'Ls')
    svg += hr(527, sw=0.3)
    svg += sh(537, 'KONGO VOWELS & VOWEL HARMONY')
    svg += t(240, 548, '7 vowels: /a e \u025b i o \u0254 u/ — distinct open/close mid vowels', 'middle', 'Ls')
    svg += t(240, 559, 'Vowel harmony in suffixes: verb extensions agree in vowel quality', 'middle', 'Ls')
    svg += hr(565, sw=0.3)
    svg += sh(575, 'SAMPLE WORDS')
    svg += t(240, 586, 'mbote (hello — same as Lingala!) · nzambi (God/spirit)', 'middle', 'Ls')
    svg += t(240, 597, 'kongo = hunter (etymon of the kingdom\'s name)', 'middle', 'Ls')
    svg += t(240, 608, 'yandi (s/he/it) · beto (we) · mono (I/me)', 'middle', 'Ls')

    svg += footer(33, 'LINGALA', 'KONGO', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_33b_alt():
    svg = open_svg()
    svg += t(240, 32, 'LINGALA / KONGO (KIKONGO)', 'middle', 'T')
    svg += t(240, 44, 'BANTU FAMILY · CONGO BASIN · PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 33B ALT · PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LINGALA PHONOLOGY —')
    svg += sh(88, 'TONE SYSTEM IN DEPTH')
    svg += t(240, 99, 'Lingala has 2 register tones: HIGH (H) marked with acute accent, LOW (L) unmarked', 'middle', 'Ls')
    svg += t(240, 110, 'Downstep: H after L-H sequence may be phonetically lower than preceding H', 'middle', 'Ls')
    svg += t(240, 121, 'Floating tones: grammatical morphemes carry tone without phonological host', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'TONE AND GRAMMAR')
    svg += t(240, 148, 'ko-bina (to dance) vs na-bi-na-kI (I am dancing) — tone shift marks aspect', 'middle', 'Ls')
    svg += t(240, 159, 'a-lak-I (he/she arrived, past) vs a-lak-a (he/she arrives, habitual)', 'middle', 'Ls')
    svg += t(240, 170, 'Subject prefix tone + verb tone = grammatical tense/aspect encoding', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'VOWELS')
    svg += t(240, 197, 'Five vowels: /a e i o u/ — all short; no phonemic vowel length in Lingala', 'middle', 'Ls')
    svg += t(240, 208, 'Lingala simplified Proto-Bantu\'s 7-vowel system to 5 (merged /e/ and /\u025b/, /o/ and /\u0254/)', 'middle', 'Ls')
    svg += hr(214, sw=0.3)
    svg += sh(224, 'VERB EXTENSIONS (BANTU DERIVATIONAL MORPHOLOGY)')
    svg += t(100, 235, 'EXTENSION', 'middle', 'Lx')
    svg += t(240, 235, 'MEANING', 'middle', 'Lx')
    svg += t(390, 235, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(239, sw=0.3)
    svg += t(100, 248, '-is-', 'middle', 'Ls')
    svg += t(240, 248, 'Causative ("make/cause to")', 'middle', 'Ls')
    svg += t(390, 248, 'loba → lobisa (cause to speak)', 'middle', 'Ls')
    svg += t(100, 258, '-am-', 'middle', 'Ls')
    svg += t(240, 258, 'Passive / stative', 'middle', 'Ls')
    svg += t(390, 258, 'boma → bomama (be killed)', 'middle', 'Ls')
    svg += t(100, 268, '-an-', 'middle', 'Ls')
    svg += t(240, 268, 'Reciprocal ("each other")', 'middle', 'Ls')
    svg += t(390, 268, 'linga → lingana (love each other)', 'middle', 'Ls')
    svg += t(100, 278, '-el-', 'middle', 'Ls')
    svg += t(240, 278, 'Applicative ("for/to")', 'middle', 'Ls')
    svg += t(390, 278, 'pesa → pesela (give for/to)', 'middle', 'Ls')
    svg += hr(283, sw=0.3)
    svg += sh(293, 'NOUN CLASS AGREEMENT (CONCORD)')
    svg += t(240, 304, 'Every noun class triggers agreement on: verbs, adjectives, pronouns, numbers', 'middle', 'Ls')
    svg += t(240, 315, 'moto moko alali malamu = person one slept well (class 1 concord throughout)', 'middle', 'Ls')
    svg += t(240, 326, 'bato babale balali malamu = people two slept well (class 2 concord)', 'middle', 'Ls')

    svg += sec_divider(338, 'KONGO (KIKONGO) — PHONOLOGY')

    svg += sh(362, '— KONGO PHONOLOGY —')
    svg += sh(373, 'THREE-TONE SYSTEM')
    svg += t(240, 384, 'Kongo has H (high) · M (mid) · L (low) — 3 register tones', 'middle', 'Ls')
    svg += t(240, 395, 'Marked in scholarly texts only; everyday writing often unmarked', 'middle', 'Ls')
    svg += t(240, 406, 'nitu (body, H-H) vs nitu (they, H-L) — tone distinguishes homographs', 'middle', 'Ls')
    svg += hr(412, sw=0.3)
    svg += sh(422, 'SEVEN VOWELS')
    svg += t(240, 433, '/a \u025b e i \u0254 o u/ — open and close mid vowels contrast phonemically', 'middle', 'Ls')
    svg += t(240, 444, 'kele /e/ vs kele /\u025b/ — different meanings (same consonants, different vowel)', 'middle', 'Ls')
    svg += t(240, 455, 'Proto-Bantu 7-vowel system preserved in Kongo (unlike Lingala\'s 5)', 'middle', 'Ls')
    svg += hr(461, sw=0.3)
    svg += sh(471, 'VERB EXTENSIONS (PARALLEL TO LINGALA)')
    svg += t(100, 482, 'EXTENSION', 'middle', 'Lx')
    svg += t(240, 482, 'MEANING', 'middle', 'Lx')
    svg += t(390, 482, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(486, sw=0.3)
    svg += t(100, 495, '-isa-', 'middle', 'Ls')
    svg += t(240, 495, 'Causative', 'middle', 'Ls')
    svg += t(390, 495, 'vanda → vandisa', 'middle', 'Ls')
    svg += t(100, 505, '-ana-', 'middle', 'Ls')
    svg += t(240, 505, 'Reciprocal', 'middle', 'Ls')
    svg += t(390, 505, 'zaba → zabana (know each other)', 'middle', 'Ls')
    svg += t(100, 515, '-ila-', 'middle', 'Ls')
    svg += t(240, 515, 'Applicative', 'middle', 'Ls')
    svg += t(390, 515, 'tuma → tumila (send to/for)', 'middle', 'Ls')
    svg += hr(520, sw=0.3)
    svg += sh(530, 'COGNATE COMPARISON: LINGALA \u2194 KONGO')
    svg += t(100, 541, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 541, 'LINGALA', 'middle', 'Lx')
    svg += t(380, 541, 'KONGO', 'middle', 'Lx')
    svg += hr(545, sw=0.3)
    svg += t(100, 554, 'hello', 'middle', 'Ls')
    svg += t(240, 554, 'mbote', 'middle', 'Ls')
    svg += t(380, 554, 'mbote', 'middle', 'Ls')
    svg += t(100, 564, 'person', 'middle', 'Ls')
    svg += t(240, 564, 'moto', 'middle', 'Ls')
    svg += t(380, 564, 'muntu', 'middle', 'Ls')
    svg += t(100, 574, 'water', 'middle', 'Ls')
    svg += t(240, 574, 'mai', 'middle', 'Ls')
    svg += t(380, 574, 'masa', 'middle', 'Ls')
    svg += t(100, 584, 'road', 'middle', 'Ls')
    svg += t(240, 584, 'nzela', 'middle', 'Ls')
    svg += t(380, 584, 'nzila', 'middle', 'Ls')
    svg += t(100, 594, 'child', 'middle', 'Ls')
    svg += t(240, 594, 'mwana', 'middle', 'Ls')
    svg += t(380, 594, 'mwana', 'middle', 'Ls')
    svg += hr(599, sw=0.3)
    svg += sh(609, 'COGNATE NOTE')
    svg += t(240, 620, 'Many Lingala words derive from Kongo; Lingala emerged as a simplified contact', 'middle', 'Ls')

    svg += footer(33, 'LINGALA', 'KONGO', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_33c_alt():
    svg = open_svg()
    svg += t(240, 32, 'LINGALA / KONGO (KIKONGO)', 'middle', 'T')
    svg += t(240, 44, 'BANTU FAMILY · CONGO BASIN · GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 33C ALT · GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LINGALA GRAMMAR —')
    svg += t(240, 88, 'Word order: SVO · verb carries prefix for subject, object, tense, aspect', 'middle', 'Ls')
    svg += t(240, 99, 'No separate subject pronouns required — prefix on verb encodes both person and class', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'VERB STRUCTURE: PREFIX + ROOT + EXTENSION + SUFFIX')
    svg += t(240, 126, 'a - lak - I = he/she - arrive - PAST.REMOTE: "he arrived (long ago)"', 'middle', 'Ls')
    svg += t(240, 137, 'na - boma - ki = I - kill - PAST.NEAR: "I killed (recently)"', 'middle', 'Ls')
    svg += t(240, 148, 'to - ko - bima = we - FUT - go out: "we will go out"', 'middle', 'Ls')
    svg += hr(154, sw=0.3)
    svg += sh(164, 'TENSE / ASPECT SUFFIXES')
    svg += t(100, 175, 'SUFFIX', 'middle', 'Lx')
    svg += t(260, 175, 'MEANING', 'middle', 'Lx')
    svg += hr(179, sw=0.3)
    svg += t(100, 188, '-a', 'middle', 'Ls')
    svg += t(260, 188, 'Habitual / present (a-bina = s/he dances)', 'middle', 'Ls')
    svg += t(100, 198, '-aki', 'middle', 'Ls')
    svg += t(260, 198, 'Recent past (a-bina-ki = s/he just danced)', 'middle', 'Ls')
    svg += t(100, 208, '-alaki', 'middle', 'Ls')
    svg += t(260, 208, 'Remote past (a-bina-laki = s/he danced long ago)', 'middle', 'Ls')
    svg += t(100, 218, 'ko- prefix', 'middle', 'Ls')
    svg += t(260, 218, 'Future (to-ko-bina = we will dance)', 'middle', 'Ls')
    svg += hr(223, sw=0.3)
    svg += sh(233, 'CORE VOCABULARY')
    svg += t(100, 244, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 244, 'LINGALA', 'middle', 'Lx')
    svg += t(390, 244, 'NOTES', 'middle', 'Lx')
    svg += hr(248, sw=0.3)
    svg += t(100, 257, 'I / me', 'middle', 'Ls')
    svg += t(240, 257, 'ngai', 'middle', 'Ls')
    svg += t(390, 257, 'or: na- (verb prefix)', 'middle', 'Ls')
    svg += t(100, 267, 'you (sg.)', 'middle', 'Ls')
    svg += t(240, 267, 'yo', 'middle', 'Ls')
    svg += t(390, 267, 'o- (verb prefix)', 'middle', 'Ls')
    svg += t(100, 277, 'we', 'middle', 'Ls')
    svg += t(240, 277, 'biso', 'middle', 'Ls')
    svg += t(390, 277, 'to- (verb prefix)', 'middle', 'Ls')
    svg += t(100, 287, 'water', 'middle', 'Ls')
    svg += t(240, 287, 'mai', 'middle', 'Ls')
    svg += t(390, 287, 'class 6 (ma-)', 'middle', 'Ls')
    svg += t(100, 297, 'eat', 'middle', 'Ls')
    svg += t(240, 297, 'kolia', 'middle', 'Ls')
    svg += t(390, 297, 'infinitive ko-lia', 'middle', 'Ls')
    svg += t(100, 307, 'go', 'middle', 'Ls')
    svg += t(240, 307, 'kokende', 'middle', 'Ls')
    svg += t(390, 307, 'infinitive (ko + kend)', 'middle', 'Ls')
    svg += t(100, 317, 'love / want', 'middle', 'Ls')
    svg += t(240, 317, 'kolinga', 'middle', 'Ls')
    svg += t(390, 317, 'ko-ling-a', 'middle', 'Ls')

    svg += sec_divider(329, 'KONGO (KIKONGO) — GRAMMAR & VOCABULARY')

    svg += sh(353, '— KONGO GRAMMAR —')
    svg += t(240, 364, 'Word order: SVO · agglutinative · 15 noun classes with full concord system', 'middle', 'Ls')
    svg += t(240, 375, 'Verb: SUBJECT PREFIX + TENSE MARKER + ROOT + EXTENSION(S) + FINAL VOWEL', 'middle', 'Ls')
    svg += hr(381, sw=0.3)
    svg += sh(391, 'KONGO VERB STRUCTURE')
    svg += t(240, 402, 'u - di - - - a = you - PRES - eat - FV: "you eat"', 'middle', 'Ls')
    svg += t(240, 413, 'mu - mono - ku - sumb - il - e = he-who I-saw buy-APPL-PAST: "who I saw buying for"', 'middle', 'Ls')
    svg += t(240, 424, 'Relative clauses embedded in verb morphology — highly synthetic structure', 'middle', 'Ls')
    svg += hr(430, sw=0.3)
    svg += sh(440, 'CORE VOCABULARY')
    svg += t(100, 451, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 451, 'KONGO (KIKONGO)', 'middle', 'Lx')
    svg += t(390, 451, 'NOTES', 'middle', 'Lx')
    svg += hr(455, sw=0.3)
    svg += t(100, 464, 'I / me', 'middle', 'Ls')
    svg += t(240, 464, 'mono', 'middle', 'Ls')
    svg += t(390, 464, 'mu- verb prefix', 'middle', 'Ls')
    svg += t(100, 474, 'you (sg.)', 'middle', 'Ls')
    svg += t(240, 474, 'ngeye', 'middle', 'Ls')
    svg += t(390, 474, 'u- verb prefix', 'middle', 'Ls')
    svg += t(100, 484, 'we', 'middle', 'Ls')
    svg += t(240, 484, 'beto', 'middle', 'Ls')
    svg += t(390, 484, 'tu- verb prefix', 'middle', 'Ls')
    svg += t(100, 494, 'water', 'middle', 'Ls')
    svg += t(240, 494, 'masa', 'middle', 'Ls')
    svg += t(390, 494, 'cf. Lingala mai', 'middle', 'Ls')
    svg += t(100, 504, 'eat', 'middle', 'Ls')
    svg += t(240, 504, 'dia', 'middle', 'Ls')
    svg += t(390, 504, 'cf. Lingala lia', 'middle', 'Ls')
    svg += t(100, 514, 'person', 'middle', 'Ls')
    svg += t(240, 514, 'muntu', 'middle', 'Ls')
    svg += t(390, 514, 'pl. bantu = people', 'middle', 'Ls')
    svg += t(100, 524, 'God / spirit', 'middle', 'Ls')
    svg += t(240, 524, 'Nzambi', 'middle', 'Ls')
    svg += t(390, 524, 'supreme being', 'middle', 'Ls')
    svg += hr(529, sw=0.3)
    svg += sh(539, 'SURVIVAL PHRASES')
    svg += t(240, 550, 'Mbote! = Hello! (both Lingala and Kongo share this greeting)', 'middle', 'Ls')
    svg += t(240, 561, 'Mono ve nlangu. = I have no water. (Kongo)', 'middle', 'Ls')
    svg += t(240, 572, 'Sala malamu! = Work well! / Farewell! (Lingala)', 'middle', 'Ls')
    svg += t(240, 583, 'Wiza awa! = Come here! (Kongo)', 'middle', 'Ls')
    svg += hr(589, sw=0.3)
    svg += sh(599, 'GRAMMATICAL PARALLEL')
    svg += t(240, 610, 'Both: agglutinative verb morphology · noun class concord · SVO · Bantu extensions', 'middle', 'Ls')

    svg += footer(33, 'LINGALA', 'KONGO', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_33d_alt():
    svg = open_svg()
    svg += t(240, 32, 'LINGALA / KONGO (KIKONGO)', 'middle', 'T')
    svg += t(240, 44, 'BANTU FAMILY · CONGO BASIN · HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 33D ALT · HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LINGALA: HISTORY & IDENTITY —')
    svg += sh(88, 'ORIGIN: A RIVER TRADE LANGUAGE')
    svg += t(240, 99, 'Lingala emerged as a contact/trade language along the Congo River ~19th c.', 'middle', 'Ls')
    svg += t(240, 110, 'Base: Bobangi (a Bantu river-trade language) + Belgian colonial influence', 'middle', 'Ls')
    svg += t(240, 121, 'Not anyone\'s mother tongue at first — it grew from commerce and mobility', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'COLONIAL ROLE & MILITARY ADOPTION')
    svg += t(240, 148, 'Force Publique (Belgian colonial army) adopted Lingala as its military language', 'middle', 'Ls')
    svg += t(240, 159, 'Soldiers from across Congo brought Lingala home; it spread with military movement', 'middle', 'Ls')
    svg += t(240, 170, 'Catholic missions in Kinshasa region reinforced Lingala as urban lingua franca', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'LINGALA AS POP CULTURE LANGUAGE')
    svg += t(240, 197, 'Congolese rumba (soukous): 1950s-present · Lingala lyrics reached all of Africa', 'middle', 'Ls')
    svg += t(240, 208, 'Franco (Luambo Makiadi) · Papa Wemba · Tabu Ley Rochereau — icons sang in Lingala', 'middle', 'Ls')
    svg += t(240, 219, 'Lingala music created a continent-wide linguistic prestige that outlasted empires', 'middle', 'Ls')
    svg += hr(225, sw=0.3)
    svg += sh(235, 'TODAY: ~70M SPEAKERS L1+L2')
    svg += t(240, 246, 'Official language of DRC National Army · one of 4 national languages of DRC', 'middle', 'Ls')
    svg += t(240, 257, 'Also widely spoken in Republic of Congo, Central African Republic, Angola', 'middle', 'Ls')
    svg += t(240, 268, '"Kinois" dialect of Kinshasa: urban prestige form, mix of Lingala + French slang', 'middle', 'Ls')
    svg += hr(274, sw=0.3)
    svg += sh(284, 'SURVIVAL PHRASE')
    svg += t(240, 295, 'Biso nyonso tozali bato ya bomoi moko', 'middle', 'Ls')
    svg += t(240, 306, '"We are all people of one life" (biso=we, nyonso=all, bato=people, bomoi=life)', 'middle', 'Ls')

    svg += sec_divider(318, 'KONGO (KIKONGO) — HISTORY & CULTURAL LEGACY')

    svg += sh(343, '— KONGO: THE KINGDOM THAT MET THE WORLD —')
    svg += sh(354, 'KINGDOM OF KONGO (~1390–1914 CE)')
    svg += t(240, 365, 'One of Africa\'s largest pre-colonial states: ~2-3M people at peak', 'middle', 'Ls')
    svg += t(240, 376, 'Capital: Mbanza Kongo (modern NW Angola) — a city of ~100,000 by 1500 CE', 'middle', 'Ls')
    svg += t(240, 387, 'Sophisticated bureaucracy, provincial governors, ambassador network', 'middle', 'Ls')
    svg += hr(393, sw=0.3)
    svg += sh(403, 'FIRST CONTACT WITH EUROPE (1483)')
    svg += t(240, 414, 'Portuguese explorer Diogo Cao arrived 1483 · Kongo king Alfonso I became Christian', 'middle', 'Ls')
    svg += t(240, 425, 'Alfonso I (Mvemba a Nzinga) wrote letters to Portuguese king in Portuguese', 'middle', 'Ls')
    svg += t(240, 436, 'Among earliest surviving African diplomatic correspondence in European language', 'middle', 'Ls')
    svg += hr(442, sw=0.3)
    svg += sh(452, 'SLAVE TRADE & DIASPORA')
    svg += t(240, 463, 'Kongo speakers were among the most numerous enslaved Africans in the Americas', 'middle', 'Ls')
    svg += t(240, 474, 'Kongo cultural elements survive in: Haitian Vodou · Cuban Palo · Brazilian Candomble', 'middle', 'Ls')
    svg += t(240, 485, 'Word "zombie" derives from Kikongo "nzambi" (spirit/divine) via Haitian Creole', 'middle', 'Ls')
    svg += hr(491, sw=0.3)
    svg += sh(501, 'FIRST BIBLE IN A BANTU LANGUAGE')
    svg += t(240, 512, 'Kikongo Bible completed 1905 — first complete Bible in any Bantu language', 'middle', 'Ls')
    svg += t(240, 523, 'Missionaries\' linguistic work created the first standardized Kongo writing system', 'middle', 'Ls')
    svg += hr(529, sw=0.3)
    svg += sh(539, 'KONGO TODAY')
    svg += t(240, 550, '~10M speakers · Kongo Central province (DRC) · northern Angola · Rep. of Congo', 'middle', 'Ls')
    svg += t(240, 561, 'Multiple dialects: Kituba (creolized), Yombe, Laadi, Vili — a dialect continuum', 'middle', 'Ls')
    svg += t(240, 572, 'Kituba: simplified Kongo-based contact language, ~7M speakers regionally', 'middle', 'Ls')
    svg += hr(578, sw=0.3)
    svg += sh(588, 'SURVIVAL PHRASE (KONGO)')
    svg += t(240, 599, 'Bantu nyonso beto n\'kola mosi', 'middle', 'Ls')
    svg += t(240, 610, '"All people, we have one origin" (bantu=people, nyonso=all, n\'kola=origin/elder)', 'middle', 'Ls')

    svg += footer(33, 'LINGALA', 'KONGO', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate33a_lingala_kongo_script_alt.svg',    build_33a_alt),
        ('plate33b_lingala_kongo_phonology_alt.svg',  build_33b_alt),
        ('plate33c_lingala_kongo_grammar_alt.svg',    build_33c_alt),
        ('plate33d_lingala_kongo_history_alt.svg',    build_33d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
