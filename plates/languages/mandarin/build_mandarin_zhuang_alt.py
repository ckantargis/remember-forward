# build_mandarin_zhuang_alt.py  — Series 17 ALT  (Mandarin + Zhuang)
# Secondary language: Zhuang (~17M speakers, Guangxi Zhuang Autonomous Region, S. China)
# Geographic basis: Mandarin spoken throughout China; Zhuang homeland (Guangxi) is within China
# Zhuang speakers are bilingual in Mandarin; Sawndip borrowed Chinese characters;
# Zhuang is the largest ethnic minority language within the Chinese-speaking world
# Outputs: plate17a–17d_mandarin_zhuang_*_alt.svg

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
def build_17a_alt():
    svg = open_svg()
    svg += t(240, 32, 'MANDARIN (\u666e\u901a\u8bdd) / ZHUANG (\u58ee\u8bed \u00b7 VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'SINO-TIBETAN / TAI-KADAI \u00b7 WITHIN CHINA \u00b7 MILLENNIA OF CONTACT', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 17A ALT \u00b7 SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MANDARIN: SCRIPT & WRITING \u2014')
    svg += t(240, 89, 'Logographic script: each character = morpheme (meaning unit), not a sound', 'middle', 'Ls')
    svg += t(240, 100, 'Simplified (mainland China, Singapore) vs Traditional (Taiwan, HK, Macau)', 'middle', 'Ls')
    svg += t(240, 111, '~2,000 commonly used characters; ~50,000 in historical dictionaries', 'middle', 'Ls')
    svg += t(240, 122, 'Pinyin romanization (1958): used for input, teaching, transliteration', 'middle', 'Ls')
    svg += hr(128, sw=0.3)
    svg += sh(138, 'CHARACTER STRUCTURE')
    svg += t(240, 149, 'Radicals: 214 semantic classifiers index characters in dictionaries', 'middle', 'Ls')
    svg += t(240, 160, '\u6c34 (water) \u2192 \u6c34\u679c (fruit) \u00b7 \u6c34\u5e73 (level/horizontal) \u00b7 \u6d2a\u6c34 (flood)', 'middle', 'Ls')
    svg += t(240, 171, '\u4eba (person) + \u6751 (village) = \u4f0f (crouch) \u2014 semantic combination', 'middle', 'Ls')
    svg += t(240, 182, 'Phono-semantic compounds: ~80% of characters have phonetic + semantic components', 'middle', 'Ls')
    svg += hr(188, sw=0.3)
    svg += sh(198, 'FOUR TONES + NEUTRAL TONE')
    svg += t(100, 209, 'TONE', 'middle', 'Lx')
    svg += t(200, 209, 'MARK', 'middle', 'Lx')
    svg += t(300, 209, 'CONTOUR', 'middle', 'Lx')
    svg += t(400, 209, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(213, sw=0.3)
    svg += t(100, 222, 'Tone 1', 'middle', 'Ls')
    svg += t(200, 222, '\u0101 (\u00af)', 'middle', 'Ls')
    svg += t(300, 222, 'High level (55)', 'middle', 'Ls')
    svg += t(400, 222, 'm\u0101 \u5988 mother', 'middle', 'Ls')
    svg += t(100, 232, 'Tone 2', 'middle', 'Ls')
    svg += t(200, 232, '\u00e1 (\u02f1)', 'middle', 'Ls')
    svg += t(300, 232, 'Rising (35)', 'middle', 'Ls')
    svg += t(400, 232, 'm\u00e1 \u9ebb hemp', 'middle', 'Ls')
    svg += t(100, 242, 'Tone 3', 'middle', 'Ls')
    svg += t(200, 242, '\u01ce (\u02c7)', 'middle', 'Ls')
    svg += t(300, 242, 'Dipping (214)', 'middle', 'Ls')
    svg += t(400, 242, 'm\u01ce \u9a6c horse', 'middle', 'Ls')
    svg += t(100, 252, 'Tone 4', 'middle', 'Ls')
    svg += t(200, 252, '\u00e0 (\u0060)', 'middle', 'Ls')
    svg += t(300, 252, 'Falling (51)', 'middle', 'Ls')
    svg += t(400, 252, 'm\u00e0 \u9a82 scold', 'middle', 'Ls')
    svg += t(100, 262, 'Neutral', 'middle', 'Ls')
    svg += t(200, 262, '(no mark)', 'middle', 'Ls')
    svg += t(300, 262, 'Unstressed, short', 'middle', 'Ls')
    svg += t(400, 262, 'ma \u5417 (question particle)', 'middle', 'Ls')
    svg += hr(267, sw=0.3)
    svg += sh(277, 'PINYIN SPECIAL PRONUNCIATIONS')
    svg += t(240, 288, 'x = /\u6cc9/ (not /ks/) \u00b7 zh = /t\u0283/ \u00b7 q = /t\u0255/ \u00b7 c = /ts/ \u00b7 r = /\u0279\u02b0/', 'middle', 'Ls')
    svg += t(240, 299, 'ui = uei \u00b7 iu = iou \u00b7 un = uen \u2014 written short but pronounced full', 'middle', 'Ls')
    svg += hr(305, sw=0.3)
    svg += sh(315, 'SAMPLE CHARACTERS')
    svg += t(240, 326, '\u4eba /r\u00e9n/ person \u00b7 \u5927 /d\u00e0/ big \u00b7 \u5c0f /xi\u01ceo/ small \u00b7 \u65e5 /r\u00ec/ sun/day', 'middle', 'Ls')
    svg += t(240, 337, '\u6708 /yu\u00e8/ moon/month \u00b7 \u6c34 /shu\u01d0/ water \u00b7 \u706b /hu\u01d2/ fire \u00b7 \u5c71 /sh\u0101n/ mountain', 'middle', 'Ls')

    svg += sec_divider(349, 'ZHUANG (\u58ee\u8bed VAHCUENGH) \u2014 TAI-KADAI \u00b7 GUANGXI \u00b7 WITHIN CHINA')

    svg += sh(375, '\u2014 ZHUANG: TWO WRITING SYSTEMS \u2014')
    svg += t(240, 386, 'SAWNDIP (\u65b9\u5757\u58ee\u5b57): traditional logographic, borrows/invents Chinese characters', 'middle', 'Ls')
    svg += t(240, 397, '~10th c. CE: Zhuang adapted Chinese characters for Zhuang sounds and meanings', 'middle', 'Ls')
    svg += t(240, 408, 'Unlike Chinese, Sawndip characters encode Zhuang words (Tai-Kadai morphemes)', 'middle', 'Ls')
    svg += hr(414, sw=0.3)
    svg += sh(424, 'ZHUANG LATIN (SAWCUENGH) SCRIPT')
    svg += t(240, 435, 'Standardized 1957, revised 1982 \u00b7 26 letters + digraphs', 'middle', 'Ls')
    svg += t(240, 446, 'Tones encoded by suffix letters: (none)=T1 b=T2 x=T3 j=T4 q=T5 h=T6', 'middle', 'Ls')
    svg += hr(452, sw=0.3)
    svg += sh(462, 'MANDARIN vs ZHUANG SCRIPT CONTRAST')
    svg += t(100, 473, 'FEATURE', 'middle', 'Lx')
    svg += t(240, 473, 'MANDARIN', 'middle', 'Lx')
    svg += t(390, 473, 'ZHUANG', 'middle', 'Lx')
    svg += hr(477, sw=0.3)
    svg += t(100, 486, 'Script type', 'middle', 'Ls')
    svg += t(240, 486, 'Logographic (characters)', 'middle', 'Ls')
    svg += t(390, 486, 'Latin + Sawndip', 'middle', 'Ls')
    svg += t(100, 496, 'Characters', 'middle', 'Ls')
    svg += t(240, 496, '~50,000 historically', 'middle', 'Ls')
    svg += t(390, 496, '26 letters + tone suffixes', 'middle', 'Ls')
    svg += t(100, 506, 'Tone marking', 'middle', 'Ls')
    svg += t(240, 506, 'Diacritics over vowels', 'middle', 'Ls')
    svg += t(390, 506, 'Suffix letters (b/x/j/q/h)', 'middle', 'Ls')
    svg += t(100, 516, 'Tones', 'middle', 'Ls')
    svg += t(240, 516, '4 + neutral', 'middle', 'Ls')
    svg += t(390, 516, '6 tones (Northern Zhuang)', 'middle', 'Ls')
    svg += hr(521, sw=0.3)
    svg += sh(531, 'CHINESE LOANWORDS IN ZHUANG')
    svg += t(240, 542, 'Centuries of Mandarin contact: Zhuang has many Sinitic loanwords', 'middle', 'Ls')
    svg += t(240, 553, 'suh (\u66f8 shu, book) \u00b7 biengz (\u8fb9 bian, side/border) \u00b7 mwngz (\u4e0b\u4eba, inferior)', 'middle', 'Ls')
    svg += hr(559, sw=0.3)
    svg += sh(569, 'SAMPLE ZHUANG WORDS (LATIN SCRIPT)')
    svg += t(240, 580, 'vah (word/speech) \u00b7 miz (have) \u00b7 mbouj (not) \u00b7 raeuz (we)', 'middle', 'Ls')
    svg += t(240, 591, 'gij (what/which) \u00b7 ndaej (can/obtain) \u00b7 Vahcuengh (Zhuang language)', 'middle', 'Ls')

    svg += footer(17, 'MANDARIN', 'ZHUANG', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_17b_alt():
    svg = open_svg()
    svg += t(240, 32, 'MANDARIN (\u666e\u901a\u8bdd) / ZHUANG (\u58ee\u8bed \u00b7 VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'SINO-TIBETAN / TAI-KADAI \u00b7 PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 17B ALT \u00b7 PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MANDARIN PHONOLOGY \u2014')
    svg += sh(88, 'INITIALS (CONSONANTS IN ONSET POSITION)')
    svg += t(240, 99, 'Stops: b p d t g k \u00b7 Affricates: z c zh ch j q', 'middle', 'Ls')
    svg += t(240, 110, 'Fricatives: f s sh x h r \u00b7 Nasals: m n \u00b7 Lateral: l \u00b7 Glide: y w', 'middle', 'Ls')
    svg += t(240, 121, 'Three-way distinction: alveolar (z/c/s) vs retroflex (zh/ch/sh/r) vs palatal (j/q/x)', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'FINALS (RIMES): STRUCTURE (C)V(V)(N)')
    svg += t(240, 148, 'Simple: a e i o u \u00fc (u-umlaut = /y/ as in French "tu")', 'middle', 'Ls')
    svg += t(240, 159, 'Diphthongs: ai ei ao ou ia ie ua uo \u00fcn \u00fce', 'middle', 'Ls')
    svg += t(240, 170, 'Nasal finals: -n (alveolar) and -ng (/\u014b/) only \u2014 no /m/ or /p t k/ finals', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'SYLLABLE STRUCTURE: MAXIMALLY (C)(G)V(V)(C)')
    svg += t(240, 197, 'Mandarin syllables are relatively simple: never CCV, never VC at start', 'middle', 'Ls')
    svg += t(240, 208, 'Contrast with English "strengths" /str\u025b\u014bk\u03b8s/ — Mandarin forbids such clusters', 'middle', 'Ls')
    svg += hr(214, sw=0.3)
    svg += sh(224, 'MEASURE WORDS (CLASSIFIERS) \u2014 REQUIRED WITH NUMBERS')
    svg += t(240, 235, '\u4e00 \u4e2a\u4eba (one ge person) \u00b7 \u4e09 \u5f20\u7eb8 (three zhang paper) \u00b7 \u4e24 \u6761\u9c7c (two tiao fish)', 'middle', 'Ls')
    svg += t(240, 246, '~200 classifiers; ge (\u4e2a) is default/universal for many nouns', 'middle', 'Ls')
    svg += t(240, 257, 'Zhuang also has classifiers \u2014 both languages require them (different family, same feature)', 'middle', 'Ls')
    svg += hr(263, sw=0.3)
    svg += sh(273, 'ASPECT PARTICLES')
    svg += t(100, 284, 'PARTICLE', 'middle', 'Lx')
    svg += t(240, 284, 'FUNCTION', 'middle', 'Lx')
    svg += t(390, 284, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(288, sw=0.3)
    svg += t(100, 297, '\u4e86 le', 'middle', 'Ls')
    svg += t(240, 297, 'Completion / change of state', 'middle', 'Ls')
    svg += t(390, 297, '\u5403\u4e86 ch\u012b le (ate)', 'middle', 'Ls')
    svg += t(100, 307, '\u8fc7 guo', 'middle', 'Ls')
    svg += t(240, 307, 'Experiential (at some time)', 'middle', 'Ls')
    svg += t(390, 307, '\u53bb\u8fc7 q\u00f9 guo (went before)', 'middle', 'Ls')
    svg += t(100, 317, '\u7740 zhe', 'middle', 'Ls')
    svg += t(240, 317, 'Ongoing state / gerund', 'middle', 'Ls')
    svg += t(390, 317, '\u5403\u7740 ch\u012b zhe (is eating)', 'middle', 'Ls')
    svg += hr(322, sw=0.3)
    svg += sh(332, 'MINIMAL TONE PAIRS')
    svg += t(240, 343, 'm\u0101 \u5988 (mother) \u00b7 m\u00e1 \u9ebb (hemp) \u00b7 m\u01ce \u9a6c (horse) \u00b7 m\u00e0 \u9a82 (scold)', 'middle', 'Ls')
    svg += t(240, 354, 'sh\u016b \u4e66 (book) \u00b7 sh\u00fa \u719f (ripe) \u00b7 sh\u01d4 \u9f20 (rat) \u00b7 sh\u00f9 \u6570 (number)', 'middle', 'Ls')

    svg += sec_divider(366, 'ZHUANG (VAHCUENGH) \u2014 PHONOLOGY')

    svg += sh(391, '\u2014 ZHUANG PHONOLOGY: NORTHERN STANDARD \u2014')
    svg += sh(402, 'SIX TONES (SUFFIX-ENCODED IN LATIN)')
    svg += t(100, 413, 'SUFFIX', 'middle', 'Lx')
    svg += t(200, 413, 'CONTOUR', 'middle', 'Lx')
    svg += t(300, 413, 'DESCRIPTION', 'middle', 'Lx')
    svg += t(420, 413, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(417, sw=0.3)
    svg += t(100, 426, '(none)', 'middle', 'Ls')
    svg += t(200, 426, '33', 'middle', 'Ls')
    svg += t(300, 426, 'Mid level', 'middle', 'Ls')
    svg += t(420, 426, 'sa (three)', 'middle', 'Ls')
    svg += t(100, 436, '-b', 'middle', 'Ls')
    svg += t(200, 436, '13', 'middle', 'Ls')
    svg += t(300, 436, 'Low rising', 'middle', 'Ls')
    svg += t(420, 436, 'saeb (receive)', 'middle', 'Ls')
    svg += t(100, 446, '-x', 'middle', 'Ls')
    svg += t(200, 446, '53', 'middle', 'Ls')
    svg += t(300, 446, 'High falling', 'middle', 'Ls')
    svg += t(420, 446, 'sax (narrow)', 'middle', 'Ls')
    svg += t(100, 456, '-j', 'middle', 'Ls')
    svg += t(200, 456, '55', 'middle', 'Ls')
    svg += t(300, 456, 'High level', 'middle', 'Ls')
    svg += t(420, 456, 'saj (thin)', 'middle', 'Ls')
    svg += t(100, 466, '-q', 'middle', 'Ls')
    svg += t(200, 466, '35', 'middle', 'Ls')
    svg += t(300, 466, 'Mid rising', 'middle', 'Ls')
    svg += t(420, 466, 'saq (checked)', 'middle', 'Ls')
    svg += t(100, 476, '-h', 'middle', 'Ls')
    svg += t(200, 476, '11', 'middle', 'Ls')
    svg += t(300, 476, 'Low level', 'middle', 'Ls')
    svg += t(420, 476, 'sah (scatter)', 'middle', 'Ls')
    svg += hr(481, sw=0.3)
    svg += sh(491, 'PRE-NASALIZED CONSONANTS')
    svg += t(240, 502, 'mb- nd- nj- ng-: prenasalized stops written as digraphs in Latin', 'middle', 'Ls')
    svg += t(240, 513, 'mbouj /m\u0329bou/ (not) \u00b7 ndaej /n\u0329dai/ (obtain) \u00b7 ngoenx (day)', 'middle', 'Ls')
    svg += hr(519, sw=0.3)
    svg += sh(529, 'TONE TYPOLOGY: MANDARIN vs ZHUANG')
    svg += t(240, 540, 'Both tonal \u2014 but UNRELATED tone systems: Sinitic vs Tai-Kadai', 'middle', 'Ls')
    svg += t(240, 551, 'Mandarin: 4 contours (level/rising/dipping/falling) + neutral', 'middle', 'Ls')
    svg += t(240, 562, 'Zhuang: 6 contours including checked tones in some dialects', 'middle', 'Ls')
    svg += t(240, 573, 'Mandarin lost /p t k/ final stops; some Zhuang dialects retain them', 'middle', 'Ls')
    svg += hr(579, sw=0.3)
    svg += sh(589, 'CLASSIFIER PARALLEL')
    svg += t(240, 600, 'Both Mandarin and Zhuang require classifiers between number and noun', 'middle', 'Ls')
    svg += t(240, 611, 'Mandarin: \u4e00\u4e2a (yi ge) \u00b7 Zhuang: ndeu boux — same syntactic requirement', 'middle', 'Ls')

    svg += footer(17, 'MANDARIN', 'ZHUANG', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_17c_alt():
    svg = open_svg()
    svg += t(240, 32, 'MANDARIN (\u666e\u901a\u8bdd) / ZHUANG (\u58ee\u8bed \u00b7 VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'SINO-TIBETAN / TAI-KADAI \u00b7 GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 17C ALT \u00b7 GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MANDARIN GRAMMAR \u2014')
    svg += t(240, 88, 'Highly analytic: no case endings, no grammatical gender, minimal inflection', 'middle', 'Ls')
    svg += t(240, 99, 'Word order: SVO (flexible for topic-comment structures)', 'middle', 'Ls')
    svg += t(240, 110, 'Topic-comment: \u9c7c\uff0c\u6211\u5403\u4e86 "Fish, I ate" = topic-prominent structure', 'middle', 'Ls')
    svg += hr(116, sw=0.3)
    svg += sh(126, 'SENTENCE PATTERNS')
    svg += t(240, 137, '\u6211\u662f\u5b66\u751f / W\u01d2 sh\u00ec xu\u00e9sh\u0113ng / I am student: "I am a student"', 'middle', 'Ls')
    svg += t(240, 148, '\u4f60\u53eb\u4ec0\u4e48\u540d\u5b57 / N\u01d0 ji\u00e0o sh\u00e9nme m\u00edngzi / You called what name: "What is your name?"', 'middle', 'Ls')
    svg += t(240, 159, '\u8fd9\u662f\u54ea\u91cc / Zh\u00e8 sh\u00ec n\u01cei li / This is where: "Where is this?"', 'middle', 'Ls')
    svg += hr(165, sw=0.3)
    svg += sh(175, 'CORE VOCABULARY')
    svg += t(100, 186, 'GLOSS', 'middle', 'Lx')
    svg += t(230, 186, 'CHARACTER', 'middle', 'Lx')
    svg += t(360, 186, 'PINYIN', 'middle', 'Lx')
    svg += hr(190, sw=0.3)
    svg += t(100, 199, 'I / me', 'middle', 'Ls')
    svg += t(230, 199, '\u6211', 'middle', 'Ls')
    svg += t(360, 199, 'w\u01d2', 'middle', 'Ls')
    svg += t(100, 209, 'you (sg.)', 'middle', 'Ls')
    svg += t(230, 209, '\u4f60 / \u60a8 (formal)', 'middle', 'Ls')
    svg += t(360, 209, 'n\u01d0 / n\u00edn', 'middle', 'Ls')
    svg += t(100, 219, 'water', 'middle', 'Ls')
    svg += t(230, 219, '\u6c34', 'middle', 'Ls')
    svg += t(360, 219, 'shu\u01d0', 'middle', 'Ls')
    svg += t(100, 229, 'eat', 'middle', 'Ls')
    svg += t(230, 229, '\u5403', 'middle', 'Ls')
    svg += t(360, 229, 'ch\u012b', 'middle', 'Ls')
    svg += t(100, 239, 'not', 'middle', 'Ls')
    svg += t(230, 239, '\u4e0d', 'middle', 'Ls')
    svg += t(360, 239, 'b\u00f9', 'middle', 'Ls')
    svg += t(100, 249, 'good', 'middle', 'Ls')
    svg += t(230, 249, '\u597d', 'middle', 'Ls')
    svg += t(360, 249, 'h\u01ceo', 'middle', 'Ls')
    svg += t(100, 259, 'person', 'middle', 'Ls')
    svg += t(230, 259, '\u4eba', 'middle', 'Ls')
    svg += t(360, 259, 'r\u00e9n', 'middle', 'Ls')
    svg += t(100, 269, 'thank you', 'middle', 'Ls')
    svg += t(230, 269, '\u8c22\u8c22', 'middle', 'Ls')
    svg += t(360, 269, 'xi\u00e8xi\u00e8', 'middle', 'Ls')
    svg += hr(274, sw=0.3)
    svg += sh(284, 'NUMBERS 1\u201310')
    svg += t(240, 295, '\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341 / y\u012b \u00e8r s\u0101n s\u00ec w\u01d4 li\u00f9 q\u012b b\u0101 ji\u01d4 sh\u00ed', 'middle', 'Ls')

    svg += sec_divider(307, 'ZHUANG (VAHCUENGH) \u2014 GRAMMAR & VOCABULARY')

    svg += sh(331, '\u2014 ZHUANG GRAMMAR \u2014')
    svg += t(240, 342, 'Word order: SVO \u2014 same as Mandarin \u00b7 analytic \u00b7 no case or gender inflection', 'middle', 'Ls')
    svg += t(240, 353, 'Classifiers required with numbers (parallel to Mandarin)', 'middle', 'Ls')
    svg += t(240, 364, 'Verbs mark aspect not tense; context + adverbs indicate time', 'middle', 'Ls')
    svg += hr(370, sw=0.3)
    svg += sh(380, 'CLASSIFIERS (ZHUANG)')
    svg += t(100, 391, 'CLASSIFIER', 'middle', 'Lx')
    svg += t(240, 391, 'USAGE', 'middle', 'Lx')
    svg += t(390, 391, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(395, sw=0.3)
    svg += t(100, 404, 'boux', 'middle', 'Ls')
    svg += t(240, 404, 'humans', 'middle', 'Ls')
    svg += t(390, 404, 'sam boux vunz (3 people)', 'middle', 'Ls')
    svg += t(100, 414, 'duz', 'middle', 'Ls')
    svg += t(240, 414, 'animals', 'middle', 'Ls')
    svg += t(390, 414, 'song duz ma (2 dogs)', 'middle', 'Ls')
    svg += t(100, 424, 'aen', 'middle', 'Ls')
    svg += t(240, 424, 'small round/compact objects', 'middle', 'Ls')
    svg += t(390, 424, 'ndeu aen (one clf)', 'middle', 'Ls')
    svg += hr(429, sw=0.3)
    svg += sh(439, 'CORE VOCABULARY (ZHUANG LATIN)')
    svg += t(100, 450, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 450, 'ZHUANG', 'middle', 'Lx')
    svg += t(390, 450, 'MANDARIN COGNATE?', 'middle', 'Lx')
    svg += hr(454, sw=0.3)
    svg += t(100, 463, 'I / me', 'middle', 'Ls')
    svg += t(240, 463, 'gou', 'middle', 'Ls')
    svg += t(390, 463, 'No (Tai-Kadai root)', 'middle', 'Ls')
    svg += t(100, 473, 'you', 'middle', 'Ls')
    svg += t(240, 473, 'mwngz', 'middle', 'Ls')
    svg += t(390, 473, 'No (Tai-Kadai root)', 'middle', 'Ls')
    svg += t(100, 483, 'water', 'middle', 'Ls')
    svg += t(240, 483, 'raemx', 'middle', 'Ls')
    svg += t(390, 483, 'No (Proto-Tai)', 'middle', 'Ls')
    svg += t(100, 493, 'eat', 'middle', 'Ls')
    svg += t(240, 493, 'gwn', 'middle', 'Ls')
    svg += t(390, 493, 'No (Proto-Tai)', 'middle', 'Ls')
    svg += t(100, 503, 'book', 'middle', 'Ls')
    svg += t(240, 503, 'suh', 'middle', 'Ls')
    svg += t(390, 503, 'YES \u2014 from \u4e66 sh\u016b', 'middle', 'Ls')
    svg += t(100, 513, 'not', 'middle', 'Ls')
    svg += t(240, 513, 'mbouj', 'middle', 'Ls')
    svg += t(390, 513, 'No (Tai-Kadai root)', 'middle', 'Ls')
    svg += hr(518, sw=0.3)
    svg += sh(528, 'SURVIVAL PHRASES')
    svg += t(240, 539, 'Gou mbouj ndaej gangj Vahcuengh. = I cannot speak Zhuang.', 'middle', 'Ls')
    svg += t(240, 550, 'W\u01d2 b\u00f9 hu\u00ec shu\u014d P\u01d4t\u014dnghu\u00e0. = I cannot speak Mandarin. (\u6211\u4e0d\u4f1a\u8bf4\u666e\u901a\u8bdd)', 'middle', 'Ls')
    svg += hr(556, sw=0.3)
    svg += sh(566, 'LANGUAGE CONTACT NOTE')
    svg += t(240, 577, 'Core vocabulary differs (different families); loanwords from Mandarin into Zhuang', 'middle', 'Ls')
    svg += t(240, 588, 'show the 1,000+ year contact history on the southern Chinese frontier', 'middle', 'Ls')

    svg += footer(17, 'MANDARIN', 'ZHUANG', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_17d_alt():
    svg = open_svg()
    svg += t(240, 32, 'MANDARIN (\u666e\u901a\u8bdd) / ZHUANG (\u58ee\u8bed \u00b7 VAHCUENGH)', 'middle', 'T')
    svg += t(240, 44, 'SINO-TIBETAN / TAI-KADAI \u00b7 HISTORY & CULTURAL LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 17D ALT \u00b7 HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 MANDARIN: HISTORY OF THE STANDARD \u2014')
    svg += sh(88, 'FROM MANY DIALECTS TO ONE STANDARD')
    svg += t(240, 99, '"Mandarin" (from Portuguese Mandarim < Malay mantri < Sanskrit mantrin = minister)', 'middle', 'Ls')
    svg += t(240, 110, 'Official standard: Putonghua (\u666e\u901a\u8bdd) = "common speech" \u2014 based on Beijing dialect', 'middle', 'Ls')
    svg += t(240, 121, 'Republic of China (1913): guoyu (\u56fd\u8bed "national language") promoted as standard', 'middle', 'Ls')
    svg += t(240, 132, 'PRC (1955): putonghua defined; compulsory in education from 1956', 'middle', 'Ls')
    svg += hr(138, sw=0.3)
    svg += sh(148, 'CHINESE WRITING: ORACLE BONES TO DIGITAL')
    svg += t(240, 159, '~1200 BCE: oracle bone script (jiaguwen \u7532\u9aa8\u6587) at Shang dynasty Anyang', 'middle', 'Ls')
    svg += t(240, 170, '221 BCE: Qin Shi Huang standardized script across unified China', 'middle', 'Ls')
    svg += t(240, 181, '1956: PRC introduces Simplified Characters \u2014 reduce stroke complexity', 'middle', 'Ls')
    svg += t(240, 192, '2000: Putonghua Law mandates standard in public education, media, government', 'middle', 'Ls')
    svg += hr(198, sw=0.3)
    svg += sh(208, 'MANDARIN AS SECOND LANGUAGE')
    svg += t(240, 219, '~1B native speakers \u00b7 ~200M L2 speakers \u00b7 world\'s most spoken language by natives', 'middle', 'Ls')
    svg += t(240, 230, 'Cantonese, Shanghainese, Hokkien: distinct Chinese languages (not dialects of Mandarin)', 'middle', 'Ls')
    svg += t(240, 241, 'All share writing system; spoken forms are mutually unintelligible', 'middle', 'Ls')
    svg += hr(247, sw=0.3)
    svg += sh(257, 'MANDARIN IN THE WORLD')
    svg += t(240, 268, 'Official language: China, Taiwan, Singapore \u00b7 UN official language', 'middle', 'Ls')
    svg += t(240, 279, 'Fastest growing language of international business in SE Asia', 'middle', 'Ls')
    svg += hr(285, sw=0.3)
    svg += sh(295, 'SURVIVAL PHRASE')
    svg += t(240, 306, '\u8fd9\u662f\u4e3a\u4f60\u505a\u7684\uff0c\u514d\u8d39\u7684\uff0c\u7531\u8bb0\u5f97\u5411\u524d\u770b\u7684\u4eba\u505a\u7684\u3002', 'middle', 'Ls')
    svg += t(240, 317, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 328, '(\u5411\u524d = xi\u00e0ng qi\u00e1n, "toward the front/forward")', 'middle', 'Ls')

    svg += sec_divider(340, 'ZHUANG (VAHCUENGH) \u2014 HISTORY & CULTURAL LEGACY')

    svg += sh(365, '\u2014 ZHUANG: 5,000+ YEARS IN GUANGXI \u2014')
    svg += sh(376, 'ANCIENT LUOYUE: THE ZHUANG ANCESTORS')
    svg += t(240, 387, 'Luoyue / Baiyue peoples of Guangxi: ancestors of modern Zhuang, ~5,000 BCE', 'middle', 'Ls')
    svg += t(240, 398, 'Bronze drum tradition (~700 BCE): still used in ritual \u2014 UNESCO heritage', 'middle', 'Ls')
    svg += t(240, 409, 'Guangxi rock art at Huashan (flower mountain): ~2,500 years old, thousands of figures', 'middle', 'Ls')
    svg += hr(415, sw=0.3)
    svg += sh(425, 'SAWNDIP: WRITING BETWEEN TWO WORLDS')
    svg += t(240, 436, 'Sawndip developed ~10th c. CE: Zhuang borrowed Chinese characters creatively', 'middle', 'Ls')
    svg += t(240, 447, 'Some characters borrowed wholesale; others invented for Zhuang sounds not in Chinese', 'middle', 'Ls')
    svg += t(240, 458, 'Preserved in folk epics (beu), ritual texts, and wedding songs (haiq)', 'middle', 'Ls')
    svg += hr(464, sw=0.3)
    svg += sh(474, 'GUANGXI ZHUANG AUTONOMOUS REGION (1958)')
    svg += t(240, 485, 'Named for Zhuang people; Zhuang = largest ethnic minority in China (~17M)', 'middle', 'Ls')
    svg += t(240, 496, 'Latin script created 1957; revised 1982 \u2014 Mao-era literacy promotion', 'middle', 'Ls')
    svg += t(240, 507, 'Today: Mandarin dominant in education; Zhuang taught in selected primary schools', 'middle', 'Ls')
    svg += hr(513, sw=0.3)
    svg += sh(523, 'LIU SANJIE: THE FOLK HERO WHO SANG TRUTH')
    svg += t(240, 534, 'Liu Sanjie (Third Sister Liu): legendary Zhuang peasant woman, sang truth to power', 'middle', 'Ls')
    svg += t(240, 545, '1961 film: one of first major Chinese films in Zhuang cultural setting', 'middle', 'Ls')
    svg += t(240, 556, 'Third Day of Third Month: Zhuang New Year festival, antiphonal singing tradition', 'middle', 'Ls')
    svg += hr(562, sw=0.3)
    svg += sh(572, 'SURVIVAL PHRASE (ZHUANG LATIN)')
    svg += t(240, 583, 'Neix guh hawj mwngz, mbouj ngaenz, ndaej raeuz lajmbwn cungj naeuz.', 'middle', 'Ls')
    svg += t(240, 594, '"This was made for you, freely, by those under heaven who remembered forward."', 'middle', 'Ls')
    svg += t(240, 605, '(lajmbwn = under heaven/sky; naeuz = say/remember; cungj = all)', 'middle', 'Ls')

    svg += footer(17, 'MANDARIN', 'ZHUANG', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate17a_mandarin_zhuang_script_alt.svg',    build_17a_alt),
        ('plate17b_mandarin_zhuang_phonology_alt.svg',  build_17b_alt),
        ('plate17c_mandarin_zhuang_grammar_alt.svg',    build_17c_alt),
        ('plate17d_mandarin_zhuang_history_alt.svg',    build_17d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
