# build_latin_italian_alt.py  — Series 22 ALT  (Latin + Italian)
# Secondary language: Italian (~65M speakers, Italian Peninsula, same geographic center)
# Geographic basis: Latin's center = Rome; Italian is the primary language of Rome
# Italian: closest living language to Classical Latin in phonology; direct descendant of Vulgar Latin
# Outputs: plate22a–22d_latin_italian_*_alt.svg

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
def build_22a_alt():
    svg = open_svg()
    svg += t(240, 32, 'LATIN (LATINA) / ITALIAN (ITALIANO)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN · ITALIC BRANCH · PARENT & CLOSEST LIVING DAUGHTER', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 22A ALT · SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LATIN SCRIPT & ALPHABET —')
    svg += t(240, 89, 'Latin alphabet derived from Etruscan · itself from Greek Euboean colony scripts', 'middle', 'Ls')
    svg += t(240, 100, 'Classical Latin: 23 letters (no J, U, or W; V served as both /u/ and /w/)', 'middle', 'Ls')
    svg += t(240, 111, 'No distinction between upper/lowercase in classical inscriptions (all capitals)', 'middle', 'Ls')
    svg += hr(117, sw=0.3)
    svg += sh(127, 'CLASSICAL LATIN PRONUNCIATION (RECONSTRUCTED)')
    svg += t(100, 138, 'LETTER', 'middle', 'Lx')
    svg += t(250, 138, 'CLASSICAL VALUE', 'middle', 'Lx')
    svg += t(390, 138, 'COMMON MISTAKE', 'middle', 'Lx')
    svg += hr(142, sw=0.3)
    svg += t(100, 151, 'C', 'middle', 'Ls')
    svg += t(250, 151, 'Always /k/ · Caesar = /ˈkaɪ.sar/', 'middle', 'Ls')
    svg += t(390, 151, 'Not /s/ or /tʃ/', 'middle', 'Ls')
    svg += t(100, 161, 'V', 'middle', 'Ls')
    svg += t(250, 161, 'Always /w/ · veni = /ˈweː.niː/', 'middle', 'Ls')
    svg += t(390, 161, 'Not /v/', 'middle', 'Ls')
    svg += t(100, 171, 'AE', 'middle', 'Ls')
    svg += t(250, 171, 'Diphthong /aɪ/ · Caesar = /kaɪ.sar/', 'middle', 'Ls')
    svg += t(390, 171, 'Not /iː/', 'middle', 'Ls')
    svg += t(100, 181, 'QU', 'middle', 'Ls')
    svg += t(250, 181, '/kw/ · aqua = /ˈa.kwa/', 'middle', 'Ls')
    svg += t(390, 181, 'Not /kj/', 'middle', 'Ls')
    svg += t(100, 191, 'Long vowel', 'middle', 'Ls')
    svg += t(250, 191, 'Macron: ā ē ī ō ū — phonemically distinct', 'middle', 'Ls')
    svg += t(390, 191, 'Changes meaning', 'middle', 'Ls')
    svg += hr(196, sw=0.3)
    svg += sh(206, 'VOWEL QUANTITY: PHONEMICALLY CONTRASTIVE')
    svg += t(240, 217, 'malum (apple) /ˈma.lum/  vs  mālum (evil) /ˈmaː.lum/', 'middle', 'Ls')
    svg += t(240, 228, 'anus (old woman)  vs  ānus (ring/anus) — length = meaning', 'middle', 'Ls')
    svg += hr(234, sw=0.3)
    svg += sh(244, 'ECCLESIASTICAL vs CLASSICAL PRONUNCIATION')
    svg += t(240, 255, 'Ecclesiastical (Church Latin): C before E/I = /tʃ/ · V = /v/ · AE = /eː/', 'middle', 'Ls')
    svg += t(240, 266, 'Classical: C always /k/ · V = /w/ · AE = /aɪ/ — two very different sounds', 'middle', 'Ls')
    svg += hr(272, sw=0.3)
    svg += sh(282, 'THE 6 CASES (DECLENSION SYSTEM)')
    svg += t(240, 293, 'Nominative (subject) · Genitive (possession) · Dative (indirect object)', 'middle', 'Ls')
    svg += t(240, 304, 'Accusative (direct object) · Ablative (separation/means) · Vocative (address)', 'middle', 'Ls')
    svg += t(240, 315, 'Word order is FREE because endings carry grammatical relationships', 'middle', 'Ls')
    svg += hr(321, sw=0.3)
    svg += sh(331, 'SAMPLE: ROSA (ROSE) — 1ST DECLENSION')
    svg += t(240, 342, 'rosa (nom.) · rosae (gen.) · rosae (dat.) · rosam (acc.) · rosa (abl.)', 'middle', 'Ls')

    svg += sec_divider(354, 'ITALIAN (ITALIANO) — CLOSEST LIVING LANGUAGE TO LATIN')

    svg += sh(380, '— ITALIAN SCRIPT & SOUNDS —')
    svg += t(240, 391, '21-letter Latin alphabet (no J K W X Y in native Italian words)', 'middle', 'Ls')
    svg += t(240, 402, 'Spelling is highly phonemic — Italian is pronounced almost exactly as written', 'middle', 'Ls')
    svg += hr(408, sw=0.3)
    svg += sh(418, 'SEVEN VOWELS (STRESSED POSITIONS)')
    svg += t(240, 429, '/a e ɛ i o ɔ u/ — front/back mid vowel distinction in stressed syllables', 'middle', 'Ls')
    svg += t(240, 440, 'e.g. /e/ (closed) in sera (evening) vs /ɛ/ (open) in sella (saddle)', 'middle', 'Ls')
    svg += t(240, 451, 'Unstressed vowels merge toward mid quality — contrast reduced', 'middle', 'Ls')
    svg += hr(457, sw=0.3)
    svg += sh(467, 'GEMINATE (DOUBLE) CONSONANTS')
    svg += t(240, 478, 'Italian preserves Latin geminates as a phonemic distinction:', 'middle', 'Ls')
    svg += t(240, 489, 'nono /ˈnɔ.no/ (ninth)  vs  nonno /ˈnon.no/ (grandfather)', 'middle', 'Ls')
    svg += t(240, 500, 'pala (shovel)  vs  palla (ball) · fato (fate)  vs  fatto (done)', 'middle', 'Ls')
    svg += hr(506, sw=0.3)
    svg += sh(516, 'SOUND CHANGES FROM LATIN TO ITALIAN')
    svg += t(100, 527, 'LATIN', 'middle', 'Lx')
    svg += t(240, 527, 'CHANGE', 'middle', 'Lx')
    svg += t(380, 527, 'ITALIAN', 'middle', 'Lx')
    svg += hr(531, sw=0.3)
    svg += t(100, 540, 'aqua', 'middle', 'Ls')
    svg += t(240, 540, '/kw/ → /kk/', 'middle', 'Ls')
    svg += t(380, 540, 'acqua', 'middle', 'Ls')
    svg += t(100, 550, 'nox, noctis', 'middle', 'Ls')
    svg += t(240, 550, 'case lost; vowel shift', 'middle', 'Ls')
    svg += t(380, 550, 'notte (night)', 'middle', 'Ls')
    svg += t(100, 560, 'filius', 'middle', 'Ls')
    svg += t(240, 560, '-ius → -io', 'middle', 'Ls')
    svg += t(380, 560, 'figlio (son)', 'middle', 'Ls')
    svg += t(100, 570, 'bonus', 'middle', 'Ls')
    svg += t(240, 570, '-us dropped', 'middle', 'Ls')
    svg += t(380, 570, 'buono (good)', 'middle', 'Ls')
    svg += hr(576, sw=0.3)
    svg += sh(586, 'REGIONAL ACCENTS')
    svg += t(240, 598, 'Tuscan (Florence) considered prestige standard — Dante\'s literary language', 'middle', 'Ls')
    svg += t(240, 609, 'Southern: open vowels · Northern: closer vowels, some devoicing', 'middle', 'Ls')

    svg += footer(22, 'LATIN', 'ITALIAN', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_22b_alt():
    svg = open_svg()
    svg += t(240, 32, 'LATIN (LATINA) / ITALIAN (ITALIANO)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN · ITALIC BRANCH · GRAMMAR COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 22B ALT · GRAMMAR')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LATIN GRAMMAR —')
    svg += sh(88, 'THE CASE SYSTEM IN ACTION')
    svg += t(240, 99, 'Latin encodes grammar in word ENDINGS, not word ORDER', 'middle', 'Ls')
    svg += t(240, 110, 'Marcus amat Iuliam = Iuliam amat Marcus = Iuliam Marcus amat', 'middle', 'Ls')
    svg += t(240, 121, 'All mean "Marcus loves Julia" — -am marks object regardless of position', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'NOUN DECLENSION: 5 CLASSES')
    svg += t(240, 148, '1st: -a stems (rosa, terra) — mostly feminine', 'middle', 'Ls')
    svg += t(240, 159, '2nd: -us/-um stems (dominus, bellum) — mostly masculine/neuter', 'middle', 'Ls')
    svg += t(240, 170, '3rd: consonant stems (rex, pax, homo) — all genders, most complex', 'middle', 'Ls')
    svg += t(240, 181, '4th: -us stems (manus, exercitus) · 5th: -es stems (dies, res)', 'middle', 'Ls')
    svg += hr(187, sw=0.3)
    svg += sh(197, 'VERB CONJUGATION: PERSON × NUMBER × TENSE × MOOD × VOICE')
    svg += t(240, 208, 'amo, amas, amat, amamus, amatis, amant — (I, you, s/he, we, you-pl, they) love', 'middle', 'Ls')
    svg += t(240, 219, '6 tenses: present · imperfect · perfect · pluperfect · future · future perfect', 'middle', 'Ls')
    svg += t(240, 230, 'Moods: indicative · subjunctive · imperative · infinitive · participle · gerund', 'middle', 'Ls')
    svg += t(240, 241, 'Voice: active (amo) and passive (amor) — passive formed with endings', 'middle', 'Ls')
    svg += hr(247, sw=0.3)
    svg += sh(257, 'SUBJUNCTIVE: OBLIGATORY IN SUBORDINATE CLAUSES')
    svg += t(240, 268, 'Rogo ut venias "I ask that you come" — venias = subjunctive (not indicative)', 'middle', 'Ls')
    svg += t(240, 279, 'Cum vidissem... "When I had seen..." — cum + pluperfect subjunctive', 'middle', 'Ls')
    svg += hr(285, sw=0.3)
    svg += sh(295, 'WORD ORDER TENDENCY: SOV')
    svg += t(240, 306, 'Default tendency SOV in prose · SVO for emphasis · verb-final in subordinate clauses', 'middle', 'Ls')
    svg += t(240, 317, 'Cicero: balanced periods with main verb at end — stylistic preference, not rule', 'middle', 'Ls')
    svg += hr(323, sw=0.3)
    svg += sh(333, 'NO DEFINITE OR INDEFINITE ARTICLE')
    svg += t(240, 344, 'homo = man / a man / the man (context determines)', 'middle', 'Ls')

    svg += sec_divider(356, 'ITALIAN (ITALIANO) — GRAMMAR: LATIN SIMPLIFIED & REBUILT')

    svg += sh(382, '— ITALIAN GRAMMAR: WHAT CHANGED —')
    svg += t(240, 393, 'Latin\'s 6-case system reduced to ZERO grammatical cases in Italian', 'middle', 'Ls')
    svg += t(240, 404, 'Case relationships now expressed by prepositions + fixed word order (SVO)', 'middle', 'Ls')
    svg += hr(410, sw=0.3)
    svg += sh(420, 'DEFINITE ARTICLES (ABSENT IN LATIN)')
    svg += t(240, 431, 'il (m. sg.) · lo (m. before s+cons, z) · la (f. sg.) · i (m. pl.) · le (f. pl.)', 'middle', 'Ls')
    svg += t(240, 442, 'il libro (the book) · lo studente · la rosa · i libri · le rose', 'middle', 'Ls')
    svg += hr(448, sw=0.3)
    svg += sh(458, 'VERB CONJUGATION: SIMPLIFIED YET RICH')
    svg += t(100, 469, 'PERSON', 'middle', 'Lx')
    svg += t(240, 469, 'AMARE (to love)', 'middle', 'Lx')
    svg += t(390, 469, 'LATIN AMO', 'middle', 'Lx')
    svg += hr(473, sw=0.3)
    svg += t(100, 482, 'io', 'middle', 'Ls')
    svg += t(240, 482, 'amo', 'middle', 'Ls')
    svg += t(390, 482, 'amo', 'middle', 'Ls')
    svg += t(100, 492, 'tu', 'middle', 'Ls')
    svg += t(240, 492, 'ami', 'middle', 'Ls')
    svg += t(390, 492, 'amas', 'middle', 'Ls')
    svg += t(100, 502, 'lui/lei', 'middle', 'Ls')
    svg += t(240, 502, 'ama', 'middle', 'Ls')
    svg += t(390, 502, 'amat', 'middle', 'Ls')
    svg += t(100, 512, 'noi', 'middle', 'Ls')
    svg += t(240, 512, 'amiamo', 'middle', 'Ls')
    svg += t(390, 512, 'amamus', 'middle', 'Ls')
    svg += t(100, 522, 'voi', 'middle', 'Ls')
    svg += t(240, 522, 'amate', 'middle', 'Ls')
    svg += t(390, 522, 'amatis', 'middle', 'Ls')
    svg += t(100, 532, 'loro', 'middle', 'Ls')
    svg += t(240, 532, 'amano', 'middle', 'Ls')
    svg += t(390, 532, 'amant', 'middle', 'Ls')
    svg += hr(537, sw=0.3)
    svg += sh(547, 'ITALIAN SUBJUNCTIVE: ALIVE AND REQUIRED')
    svg += t(240, 558, 'Voglio che tu venga "I want you to come" — venga = subjunctive', 'middle', 'Ls')
    svg += t(240, 569, 'Subjunctive required after: volere · sperare · credere · sebbene · affinché', 'middle', 'Ls')
    svg += hr(575, sw=0.3)
    svg += sh(585, 'PASSATO PROSSIMO (LATIN LEGACY)')
    svg += t(240, 597, 'Built from essere/avere (be/have) + past participle — same as French, Spanish', 'middle', 'Ls')
    svg += t(240, 608, 'Ho mangiato (I have eaten / I ate) · Sono andato (I went) — aux. varies by verb', 'middle', 'Ls')

    svg += footer(22, 'LATIN', 'ITALIAN', 'B', 'GRAMMAR')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_22c_alt():
    svg = open_svg()
    svg += t(240, 32, 'LATIN (LATINA) / ITALIAN (ITALIANO)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN · ITALIC BRANCH · CORE VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 22C ALT · CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LATIN CORE VOCABULARY —')
    svg += t(100, 88, 'LATIN', 'middle', 'Lx')
    svg += t(220, 88, 'CLASS', 'middle', 'Lx')
    svg += t(350, 88, 'MEANING', 'middle', 'Lx')
    svg += hr(92, sw=0.3)
    svg += t(100, 101, 'aqua, -ae (f.)', 'middle', 'Ls')
    svg += t(220, 101, '1st decl.', 'middle', 'Ls')
    svg += t(350, 101, 'water', 'middle', 'Ls')
    svg += t(100, 111, 'ignis, -is (m.)', 'middle', 'Ls')
    svg += t(220, 111, '3rd decl.', 'middle', 'Ls')
    svg += t(350, 111, 'fire', 'middle', 'Ls')
    svg += t(100, 121, 'terra, -ae (f.)', 'middle', 'Ls')
    svg += t(220, 121, '1st decl.', 'middle', 'Ls')
    svg += t(350, 121, 'earth / land', 'middle', 'Ls')
    svg += t(100, 131, 'vita, -ae (f.)', 'middle', 'Ls')
    svg += t(220, 131, '1st decl.', 'middle', 'Ls')
    svg += t(350, 131, 'life', 'middle', 'Ls')
    svg += t(100, 141, 'mors, mortis (f.)', 'middle', 'Ls')
    svg += t(220, 141, '3rd decl.', 'middle', 'Ls')
    svg += t(350, 141, 'death', 'middle', 'Ls')
    svg += t(100, 151, 'tempus, -oris (n.)', 'middle', 'Ls')
    svg += t(220, 151, '3rd decl.', 'middle', 'Ls')
    svg += t(350, 151, 'time', 'middle', 'Ls')
    svg += t(100, 161, 'homo, hominis (m.)', 'middle', 'Ls')
    svg += t(220, 161, '3rd decl.', 'middle', 'Ls')
    svg += t(350, 161, 'human being', 'middle', 'Ls')
    svg += t(100, 171, 'pax, pacis (f.)', 'middle', 'Ls')
    svg += t(220, 171, '3rd decl.', 'middle', 'Ls')
    svg += t(350, 171, 'peace', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'SURVIVAL PHRASES IN LATIN')
    svg += t(240, 197, 'Ubi est aqua? — Where is water?', 'middle', 'Ls')
    svg += t(240, 208, 'Da mihi panem, quaeso. — Give me bread, please.', 'middle', 'Ls')
    svg += t(240, 219, 'Non intellego. — I do not understand.', 'middle', 'Ls')
    svg += t(240, 230, 'Adiuva me! — Help me! (imperative)', 'middle', 'Ls')
    svg += t(240, 241, 'Vale! / Valete! — Farewell! (sg. / pl.)', 'middle', 'Ls')
    svg += t(240, 252, 'Quid est nomen tibi? — What is your name? (lit. "what is the name to you?")', 'middle', 'Ls')
    svg += hr(258, sw=0.3)
    svg += sh(268, 'NUMBERS 1–10')
    svg += t(240, 279, 'I unus · II duo · III tres · IV quattuor · V quinque', 'middle', 'Ls')
    svg += t(240, 290, 'VI sex · VII septem · VIII octo · IX novem · X decem', 'middle', 'Ls')
    svg += t(240, 301, 'mille (1000) · centum (100) · the root of Italian mille · cento', 'middle', 'Ls')
    svg += hr(307, sw=0.3)
    svg += sh(317, 'LATIN SAYINGS STILL IN USE')
    svg += t(240, 328, 'Veni, vidi, vici — I came, I saw, I conquered (Caesar)', 'middle', 'Ls')
    svg += t(240, 339, 'Carpe diem — Seize the day (Horace)', 'middle', 'Ls')
    svg += t(240, 350, 'In hoc signo vinces — In this sign you shall conquer (Constantine)', 'middle', 'Ls')

    svg += sec_divider(362, 'ITALIAN (ITALIANO) — VOCABULARY: LATIN EVOLVED')

    svg += sh(387, '— ITALIAN VOCABULARY: THE DIRECT LINE FROM LATIN —')
    svg += t(100, 398, 'LATIN', 'middle', 'Lx')
    svg += t(240, 398, 'ITALIAN', 'middle', 'Lx')
    svg += t(380, 398, 'GLOSS', 'middle', 'Lx')
    svg += hr(402, sw=0.3)
    svg += t(100, 411, 'aqua', 'middle', 'Ls')
    svg += t(240, 411, 'acqua', 'middle', 'Ls')
    svg += t(380, 411, 'water', 'middle', 'Ls')
    svg += t(100, 421, 'ignis', 'middle', 'Ls')
    svg += t(240, 421, 'fuoco (< focus)', 'middle', 'Ls')
    svg += t(380, 421, 'fire (hearth shifted)', 'middle', 'Ls')
    svg += t(100, 431, 'nox/noctis', 'middle', 'Ls')
    svg += t(240, 431, 'notte', 'middle', 'Ls')
    svg += t(380, 431, 'night', 'middle', 'Ls')
    svg += t(100, 441, 'homo/hominis', 'middle', 'Ls')
    svg += t(240, 441, 'uomo', 'middle', 'Ls')
    svg += t(380, 441, 'man/person', 'middle', 'Ls')
    svg += t(100, 451, 'pax/pacis', 'middle', 'Ls')
    svg += t(240, 451, 'pace', 'middle', 'Ls')
    svg += t(380, 451, 'peace', 'middle', 'Ls')
    svg += t(100, 461, 'vita', 'middle', 'Ls')
    svg += t(240, 461, 'vita', 'middle', 'Ls')
    svg += t(380, 461, 'life (unchanged)', 'middle', 'Ls')
    svg += t(100, 471, 'tempus', 'middle', 'Ls')
    svg += t(240, 471, 'tempo', 'middle', 'Ls')
    svg += t(380, 471, 'time / weather', 'middle', 'Ls')
    svg += hr(476, sw=0.3)
    svg += sh(486, 'SURVIVAL PHRASES IN ITALIAN')
    svg += t(240, 497, 'Dove\'e\' l\'acqua? — Where is the water?', 'middle', 'Ls')
    svg += t(240, 508, 'Dammi del pane, per favore. — Give me bread, please.', 'middle', 'Ls')
    svg += t(240, 519, 'Non capisco. — I do not understand.', 'middle', 'Ls')
    svg += t(240, 530, 'Aiutatemi! — Help me! (formal plural)', 'middle', 'Ls')
    svg += t(240, 541, 'Arrivederci! — Goodbye! (lit. "until we see each other again")', 'middle', 'Ls')
    svg += hr(547, sw=0.3)
    svg += sh(557, 'NUMBERS 1–10')
    svg += t(240, 568, 'uno · due · tre · quattro · cinque', 'middle', 'Ls')
    svg += t(240, 579, 'sei · sette · otto · nove · dieci', 'middle', 'Ls')
    svg += t(240, 590, 'mille (1000) · cento (100) — direct from Latin mille · centum', 'middle', 'Ls')
    svg += hr(596, sw=0.3)
    svg += sh(606, 'ITALIAN: MOST LATIN-PRESERVING ROMANCE LANGUAGE')
    svg += t(240, 617, 'Italian retains Latin vowel quality, geminate consonants, and -o/-a endings', 'middle', 'Ls')

    svg += footer(22, 'LATIN', 'ITALIAN', 'C', 'CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_22d_alt():
    svg = open_svg()
    svg += t(240, 32, 'LATIN (LATINA) / ITALIAN (ITALIANO)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN · ITALIC BRANCH · HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 22D ALT · HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— LATIN: HISTORY & INFLUENCE —')
    svg += sh(88, 'FROM VILLAGE DIALECT TO WORLD LANGUAGE')
    svg += t(240, 99, '753 BCE (trad.): Rome founded · Latin a minor Italic dialect of Latium', 'middle', 'Ls')
    svg += t(240, 110, '3rd–1st c. BCE: Republican expansion → Latin spreads throughout Italy then empire', 'middle', 'Ls')
    svg += t(240, 121, '~27 BCE–476 CE: Roman Empire · Latin as administrative language from Britain to Mesopotamia', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'VULGAR LATIN: WHAT PEOPLE ACTUALLY SPOKE')
    svg += t(240, 148, 'Classical Latin: prestige written register — few spoke it natively', 'middle', 'Ls')
    svg += t(240, 159, 'Vulgar Latin: colloquial spoken form, varied by region, lost noun cases early', 'middle', 'Ls')
    svg += t(240, 170, 'Graffiti at Pompeii shows Vulgar Latin in action: simplified grammar, new words', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'THE ROMANCE FAMILY: LATIN\'S LIVING DESCENDANTS')
    svg += t(240, 197, 'Spanish ~490M · Portuguese ~260M · French ~280M', 'middle', 'Ls')
    svg += t(240, 208, 'Italian ~65M · Romanian ~25M · Catalan ~10M · Occitan ~1M', 'middle', 'Ls')
    svg += t(240, 219, 'All descend from Vulgar Latin, not Classical Latin — the spoken form survived', 'middle', 'Ls')
    svg += hr(225, sw=0.3)
    svg += sh(235, 'LATIN\'S SECOND LIFE: MEDIEVAL & RENAISSANCE')
    svg += t(240, 246, 'Church Latin (Ecclesiastical): Mass, theology, liturgy 400–1962 CE', 'middle', 'Ls')
    svg += t(240, 257, 'Medieval Latin: science, law, philosophy — lingua franca of scholars', 'middle', 'Ls')
    svg += t(240, 268, 'Renaissance: Classical Latin revived as ideal — Cicero imitated over medieval style', 'middle', 'Ls')
    svg += t(240, 279, 'Latin as scientific nomenclature: still used in biology, medicine, law today', 'middle', 'Ls')
    svg += hr(285, sw=0.3)
    svg += sh(295, 'LATIN IN ENGLISH: ~60% OF ENGLISH VOCABULARY')
    svg += t(240, 306, 'Direct: via French after 1066 (Norman Conquest) · aqua-, terra-, vita-', 'middle', 'Ls')
    svg += t(240, 317, 'Legal: habeas corpus, in absentia, mens rea, prima facie', 'middle', 'Ls')
    svg += t(240, 328, 'Scientific: Homo sapiens, Tyrannosaurus rex, Rosa canina (dog rose)', 'middle', 'Ls')

    svg += sec_divider(340, 'ITALIAN (ITALIANO) — HISTORY & LITERARY LEGACY')

    svg += sh(365, '— ITALIAN: THE LANGUAGE DANTE BUILT —')
    svg += sh(376, 'BEFORE STANDARD ITALIAN: ITALIAN DIALECTS')
    svg += t(240, 387, 'Before ~1300: no "Italian" — dozens of mutually unintelligible Romance dialects', 'middle', 'Ls')
    svg += t(240, 398, 'Venetian, Sicilian, Neapolitan, Lombard — each with own literature', 'middle', 'Ls')
    svg += hr(404, sw=0.3)
    svg += sh(414, 'DANTE ALIGHIERI (1265–1321): THE FATHER OF ITALIAN')
    svg += t(240, 425, 'La Divina Commedia (Inferno, Purgatorio, Paradiso): written in Tuscan vernacular', 'middle', 'Ls')
    svg += t(240, 436, 'Chose volgare (common tongue) over Latin to reach a wider audience', 'middle', 'Ls')
    svg += t(240, 447, 'Boccaccio\'s Decameron, Petrarch\'s Canzoniere: established Tuscan as prestige model', 'middle', 'Ls')
    svg += hr(453, sw=0.3)
    svg += sh(463, 'RISORGIMENTO & NATIONAL LANGUAGE (19TH C.)')
    svg += t(240, 474, 'Italian unification 1861: a country unified before a common language', 'middle', 'Ls')
    svg += t(240, 485, 'Manzoni\'s I Promessi Sposi (The Betrothed, 1827/1840) modeled standard Italian', 'middle', 'Ls')
    svg += t(240, 496, '~1861: only 2–3% of Italians spoke standard Italian; rest spoke dialects', 'middle', 'Ls')
    svg += t(240, 507, 'Television (RAI, 1954) and compulsory schooling unified the spoken language', 'middle', 'Ls')
    svg += hr(513, sw=0.3)
    svg += sh(523, 'ITALIAN IN THE ARTS: A UNIVERSAL LANGUAGE')
    svg += t(240, 534, 'Opera: Verdi · Puccini · Rossini — Italian the language of classical opera worldwide', 'middle', 'Ls')
    svg += t(240, 545, 'Music terms in every language: piano · forte · allegro · soprano · crescendo', 'middle', 'Ls')
    svg += t(240, 556, 'Cuisine vocabulary: pasta · pizza · espresso · prosciutto — Italian exports', 'middle', 'Ls')
    svg += hr(562, sw=0.3)
    svg += sh(572, 'THE CONTINUOUS THREAD')
    svg += t(240, 583, 'Latin → Vulgar Latin → Old Italian → Dante\'s Tuscan → Modern Italian', 'middle', 'Ls')
    svg += t(240, 594, '~2,000 years of continuous Latin-family speech in the same peninsula', 'middle', 'Ls')
    svg += hr(600, sw=0.3)
    svg += sh(610, 'SURVIVAL PHRASE')
    svg += t(240, 621, 'Siamo tutti umani — We are all human (cf. Latin: Omnes homines sumus)', 'middle', 'Ls')

    svg += footer(22, 'LATIN', 'ITALIAN', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate22a_latin_italian_script_alt.svg',    build_22a_alt),
        ('plate22b_latin_italian_grammar_alt.svg',    build_22b_alt),
        ('plate22c_latin_italian_vocabulary_alt.svg', build_22c_alt),
        ('plate22d_latin_italian_history_alt.svg',    build_22d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
