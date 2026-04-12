# build_portuguese_tamazight_alt.py  — Series 27 ALT  (Portuguese + Tamazight/Amazigh)
# Secondary language: Tamazight/Amazigh (~8-10M speakers, Morocco & Algeria)
# Geographic basis: anchored to Lisbon (38.7°N, 9.1°W) per user instruction
# Rabat, Morocco is ~880km (~545mi) — at edge of 500mi; Rif mountains (northern Morocco)
# closer; Morocco is the nearest African country to Portugal; ~14km at Gibraltar Strait
# Historical: Portugal conquered Ceuta 1415, Tangier 1471; shared Atlantic-Mediterranean border
# Outputs: plate27a–27d_portuguese_tamazight_*_alt.svg

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
def build_27a_alt():
    svg = open_svg()
    svg += t(240, 32, 'PORTUGUESE (PORTUGU\u00caS) / TAMAZIGHT (\u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN / AFROASIATIC \u00b7 ATLANTIC NEIGHBORS \u00b7 ACROSS THE STRAIT', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 27A ALT \u00b7 SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PORTUGUESE: SCRIPT & PHONOLOGY OVERVIEW \u2014')
    svg += t(240, 89, 'Latin alphabet \u00b7 orthography reflects historical pronunciation more than current', 'middle', 'Ls')
    svg += t(240, 100, 'Diacritics: \u00e3 \u00e0 \u00e2 \u00e1 \u00e9 \u00ea \u00ed \u00f3 \u00f4 \u00fa \u00fc \u00e7 \u2014 nasal vowels (unique in Romance)', 'middle', 'Ls')
    svg += t(240, 111, 'European Portuguese vs Brazilian Portuguese: significant pronunciation difference', 'middle', 'Ls')
    svg += hr(117, sw=0.3)
    svg += sh(127, 'NASAL VOWELS: PORTUGUESE SIGNATURE FEATURE')
    svg += t(240, 138, '/\u00e3/ (masc. pl. suffix) \u00b7 /\u00f5/ (they, from Latin -unt) \u00b7 /\u025b\u0303/ /i\u0303/ /\u0289\u0303/', 'middle', 'Ls')
    svg += t(240, 149, 'p\u00e3o (bread) /p\u0250\u0303w/ \u00b7 irm\u00e3 (sister) \u00b7 aten\u00e7\u00e3o (attention)', 'middle', 'Ls')
    svg += t(240, 160, 'Nasal vowels: unique to Portuguese among major Romance languages', 'middle', 'Ls')
    svg += hr(166, sw=0.3)
    svg += sh(176, 'EUROPEAN vs BRAZILIAN PRONUNCIATION')
    svg += t(240, 187, 'European: vowel reduction/deletion in unstressed syllables (prato = /pratu/)', 'middle', 'Ls')
    svg += t(240, 198, 'Brazilian: full vowel quality preserved (prato = /pra.tu/) \u2014 more open', 'middle', 'Ls')
    svg += t(240, 209, 'Both: same orthography; mutual intelligibility high in writing, moderate in speech', 'middle', 'Ls')
    svg += hr(215, sw=0.3)
    svg += sh(225, 'PORTUGUESE CONSONANTS')
    svg += t(240, 236, '/p b t d k g/ \u00b7 /f v s z \u0283 \u0292/ \u00b7 /m n \u0272/ \u00b7 /l \u028e/ \u00b7 /r \u0281 \u027e/', 'middle', 'Ls')
    svg += t(240, 247, 'Palatal sounds: lh /\u028e/ (filho=son) \u00b7 nh /\u0272/ (vinho=wine) \u2014 from Latin groups', 'middle', 'Ls')
    svg += t(240, 258, 'Sibilants: s/z before vowels; sh/zh before consonants (European) or s/z (Brazilian)', 'middle', 'Ls')
    svg += hr(264, sw=0.3)
    svg += sh(274, 'SAMPLE WORDS')
    svg += t(240, 285, 'ol\u00e1 (hello) \u00b7 obrigado/a (thank you) \u00b7 \u00e1gua (\u00e1gua) = water', 'middle', 'Ls')
    svg += t(240, 296, 'saud\u00e0de (longing/nostalgia) \u2014 the Portuguese untranslatable', 'middle', 'Ls')
    svg += t(240, 307, 'S\u00e3o Paulo (Saint Paul) \u00b7 \u00e3 = nasal vowel in city name', 'middle', 'Ls')
    svg += hr(313, sw=0.3)
    svg += sh(323, 'PORTUGUESE AROUND THE WORLD')
    svg += t(240, 334, '~260M speakers \u00b7 official in: Portugal, Brazil, Angola, Mozambique, Cape Verde', 'middle', 'Ls')
    svg += t(240, 345, 'Also: Guinea-Bissau, S\u00e3o Tom\u00e9 and Pr\u00edncipe, East Timor, Macau, Equatorial Guinea', 'middle', 'Ls')

    svg += sec_divider(357, 'TAMAZIGHT (\u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c TAMAZIGHT) \u2014 MOROCCO/ALGERIA \u00b7 ~550MI')

    svg += sh(382, '\u2014 TAMAZIGHT: THREE SCRIPTS \u2014')
    svg += t(240, 393, 'TIFINAGH: ancient Berber script; modern Neo-Tifinagh standardized by IRCAM (2003)', 'middle', 'Ls')
    svg += t(240, 404, 'Morocco official: Neo-Tifinagh \u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c for official Amazigh language', 'middle', 'Ls')
    svg += t(240, 415, 'Latin (Kabyle Algeria, diaspora, online) \u00b7 Arabic (some communities)', 'middle', 'Ls')
    svg += hr(421, sw=0.3)
    svg += sh(431, 'TIFINAGH SCRIPT: ANCIENT & REVIVED')
    svg += t(240, 442, 'Tifinagh: 2,000+ years old \u00b7 found in rock inscriptions across North Africa', 'middle', 'Ls')
    svg += t(240, 453, 'Tuareg still use traditional Tifinagh (Tamahaq) \u2014 mostly women preserved it', 'middle', 'Ls')
    svg += t(240, 464, 'Neo-Tifinagh: Unicode block U+2D30\u2013U+2D7F \u00b7 added to Unicode 4.1 (2005)', 'middle', 'Ls')
    svg += hr(470, sw=0.3)
    svg += sh(480, 'TAMAZIGHT VARIETIES')
    svg += t(240, 491, 'Tachelhit/Shilha: ~8M, SW Morocco (High Atlas, Souss) \u2014 largest variety', 'middle', 'Ls')
    svg += t(240, 502, 'Central Atlas Tamazight: ~3M, Atlas Mountains, central Morocco', 'middle', 'Ls')
    svg += t(240, 513, 'Tarifit/Rif Berber: ~1.5M, Rif mountains, N Morocco \u2014 closest to Iberia', 'middle', 'Ls')
    svg += t(240, 524, 'Kabyle: ~5M, Kabylie, NE Algeria \u2014 most documented; diaspora in France', 'middle', 'Ls')
    svg += hr(530, sw=0.3)
    svg += sh(540, 'TAMAZIGHT PHONOLOGY OVERVIEW')
    svg += t(240, 551, '3 short vowels: /a i u/ \u00b7 some dialects: schwa /\u0259/ in consonant clusters', 'middle', 'Ls')
    svg += t(240, 562, 'Rich consonant inventory: pharyngeals /\u0127 \u0295/ \u00b7 uvulars /q \u0281/ \u00b7 emphatics /\u0282 \u1e93 \u1e6d \u1e91/', 'middle', 'Ls')
    svg += hr(568, sw=0.3)
    svg += sh(578, 'SAMPLE WORDS (TIFINAGH + LATIN)')
    svg += t(240, 589, '\u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c = tamazight (the language/the free language)', 'middle', 'Ls')
    svg += t(240, 600, 'azul (hello in Kabyle) \u00b7 aman (water) \u00b7 tanemmirt (thank you, Tachelhit)', 'middle', 'Ls')
    svg += t(240, 611, 'amazigh = free person (origin of Berber identity term)', 'middle', 'Ls')

    svg += footer(27, 'PORTUGUESE', 'TAMAZIGHT', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_27b_alt():
    svg = open_svg()
    svg += t(240, 32, 'PORTUGUESE (PORTUGU\u00caS) / TAMAZIGHT (\u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN / AFROASIATIC \u00b7 PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 27B ALT \u00b7 PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PORTUGUESE PHONOLOGY IN DEPTH \u2014')
    svg += sh(88, 'VOWEL SYSTEM')
    svg += t(240, 99, 'Oral vowels: /a e \u025b i o \u0254 u/ \u2014 7 distinct phonemes in stressed positions', 'middle', 'Ls')
    svg += t(240, 110, 'Nasal vowels: /\u00e3 \u025b\u0303 \u0129 \u00f5 u\u0303/ \u2014 5 nasal phonemes (unique in Romance)', 'middle', 'Ls')
    svg += t(240, 121, 'Nasal diphthongs: /\u00e3w/ (p\u00e3o) \u00b7 /\u00e3j/ (m\u00e3e) \u00b7 /\u00f5j/ (p\u00f5e)', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'EUROPEAN PORTUGUESE: EXTREME VOWEL REDUCTION')
    svg += t(240, 148, 'Unstressed /a e o/ often reduced to /\u0259 \u0268 u/ or deleted entirely:', 'middle', 'Ls')
    svg += t(240, 159, 'professor /pr\u0268.f\u025b.sor/ \u2014 2nd vowel nearly deleted in casual speech', 'middle', 'Ls')
    svg += t(240, 170, 'This reduction makes European Portuguese very hard for Brazilian speakers to parse', 'middle', 'Ls')
    svg += hr(176, sw=0.3)
    svg += sh(186, 'SIBILANT SYSTEM (COMPLEX AND REGIONAL)')
    svg += t(240, 197, 'European: cena /\u02c8se.n\u0250/ before vowels BUT /\u0283/ before consonants and word-finally', 'middle', 'Ls')
    svg += t(240, 208, 'Brazilian: sibilants generally /s z/ \u2014 no automatic palatalization', 'middle', 'Ls')
    svg += t(240, 219, 'Rio de Janeiro: /\u0283 \u0292/ used where SP uses /s z/ \u2014 "carioca" dialect', 'middle', 'Ls')
    svg += hr(225, sw=0.3)
    svg += sh(235, 'NUMBERS 1\u201310')
    svg += t(240, 246, 'um/uma \u00b7 dois/duas \u00b7 tr\u00eas \u00b7 quatro \u00b7 cinco', 'middle', 'Ls')
    svg += t(240, 257, 'seis \u00b7 sete \u00b7 oito \u00b7 nove \u00b7 dez', 'middle', 'Ls')
    svg += hr(263, sw=0.3)
    svg += sh(273, 'REDUPLICATION IN PORTUGUESE')
    svg += t(240, 284, 'No productive reduplication (unlike Malay/Bantu) \u2014 emphatic doubling colloquial only', 'middle', 'Ls')
    svg += t(240, 295, 'Agora agora = right now, really now \u2014 emphatic intensification only', 'middle', 'Ls')
    svg += hr(301, sw=0.3)
    svg += sh(311, 'AFRIKAANS, GALICIAN, SPANISH: SISTER LANGUAGES')
    svg += t(240, 322, 'Portuguese and Spanish: ~89% lexical similarity (close but not identical)', 'middle', 'Ls')
    svg += t(240, 333, 'Galician (NW Spain): most similar to Portuguese \u2014 historically one language', 'middle', 'Ls')
    svg += t(240, 344, 'Portuguese \u2260 Spanish: grammar, pronunciation, and many core words differ', 'middle', 'Ls')

    svg += sec_divider(356, 'TAMAZIGHT \u2014 PHONOLOGY: AFROASIATIC DEPTH')

    svg += sh(381, '\u2014 TAMAZIGHT PHONOLOGY \u2014')
    svg += sh(392, 'CONSONANT INVENTORY: PHARYNGEALS AND EMPHATICS')
    svg += t(240, 403, 'Pharyngeal fricatives: /\u0127/ (voiceless) \u00b7 /\u0295/ (voiced) \u2014 in throat, not in Portuguese', 'middle', 'Ls')
    svg += t(240, 414, 'Uvular stops: /q/ (voiceless) \u00b7 emphatic/pharyngealized series: /\u1e63 \u1e93 \u1e6d/', 'middle', 'Ls')
    svg += t(240, 425, 'Emphatic consonants: produced with pharyngeal co-articulation; change vowel quality', 'middle', 'Ls')
    svg += hr(431, sw=0.3)
    svg += sh(441, 'SYLLABLE STRUCTURE: CONSONANT CLUSTERS')
    svg += t(240, 452, 'Tamazight allows heavy consonant clusters; schwa may emerge in speech', 'middle', 'Ls')
    svg += t(240, 463, 'Tachelhit allows syllabic obstruents: /tft/ = she sewed (all consonants)', 'middle', 'Ls')
    svg += t(240, 474, 'Berber languages have among the heaviest consonant clusters in human languages', 'middle', 'Ls')
    svg += hr(480, sw=0.3)
    svg += sh(490, 'THREE-VOWEL SYSTEM')
    svg += t(240, 501, 'Classical: /a i u/ \u2014 same 3 vowels as Arabic and many Afroasiatic languages', 'middle', 'Ls')
    svg += t(240, 512, 'Schwa: /\u0259/ appears in consonant clusters as a buffer in pronunciation', 'middle', 'Ls')
    svg += t(240, 523, 'No nasal vowels (contrast: Portuguese has 5 nasal vowels)', 'middle', 'Ls')
    svg += hr(529, sw=0.3)
    svg += sh(539, 'NUMBERS 1\u201310 (TAMAZIGHT \u2014 TACHELHIT VARIETY)')
    svg += t(240, 550, 'yan/yat \u00b7 sin \u00b7 krad \u00b7 kkuz \u00b7 semmus', 'middle', 'Ls')
    svg += t(240, 561, 'sddis \u00b7 sa \u00b7 tam \u00b7 tza \u00b7 mraw', 'middle', 'Ls')
    svg += t(240, 572, 'Gender in numbers: yan (1 masc.) vs yat (1 fem.) \u2014 gendered number system', 'middle', 'Ls')
    svg += hr(578, sw=0.3)
    svg += sh(588, 'KEY CONTRAST: PORTUGUESE vs TAMAZIGHT')
    svg += t(100, 599, 'FEATURE', 'middle', 'Lx')
    svg += t(240, 599, 'PORTUGUESE', 'middle', 'Lx')
    svg += t(390, 599, 'TAMAZIGHT', 'middle', 'Lx')
    svg += hr(603, sw=0.3)
    svg += t(100, 612, 'Vowels', 'middle', 'Ls')
    svg += t(240, 612, '7 oral + 5 nasal', 'middle', 'Ls')
    svg += t(390, 612, '3 (/a i u/)', 'middle', 'Ls')

    svg += footer(27, 'PORTUGUESE', 'TAMAZIGHT', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_27c_alt():
    svg = open_svg()
    svg += t(240, 32, 'PORTUGUESE (PORTUGU\u00caS) / TAMAZIGHT (\u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN / AFROASIATIC \u00b7 GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 27C ALT \u00b7 GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PORTUGUESE GRAMMAR \u2014')
    svg += t(240, 88, 'SVO word order \u00b7 2 genders (masc/fem) \u00b7 verb conjugation rich in person and tense', 'middle', 'Ls')
    svg += t(240, 99, 'Personal infinitive: unique to Portuguese \u2014 the infinitive inflects for person', 'middle', 'Ls')
    svg += hr(105, sw=0.3)
    svg += sh(115, 'PERSONAL INFINITIVE (UNIQUE TO PORTUGUESE)')
    svg += t(240, 126, 'Most languages: infinitive does not inflect \u2014 in Portuguese it does:', 'middle', 'Ls')
    svg += t(240, 137, 'para eu falar = for I-to-speak (1sg) \u00b7 para tu falares = for you-to-speak (2sg)', 'middle', 'Ls')
    svg += t(240, 148, 'para ele falar = for him-to-speak (3sg) \u00b7 para n\u00f3s falarmos = for us-to-speak (1pl)', 'middle', 'Ls')
    svg += t(240, 159, 'This allows unambiguous reference in purpose clauses without a conjunction', 'middle', 'Ls')
    svg += hr(165, sw=0.3)
    svg += sh(175, 'PORTUGUESE VERB TENSES')
    svg += t(240, 186, 'Indicative: present \u00b7 imperfect \u00b7 perfect \u00b7 pluperfect \u00b7 future \u00b7 conditional', 'middle', 'Ls')
    svg += t(240, 197, 'Subjunctive: present \u00b7 imperfect \u00b7 future \u2014 yes, FUTURE SUBJUNCTIVE!', 'middle', 'Ls')
    svg += t(240, 208, 'Future subjunctive: "If I am [in the future] there..." \u2014 unique in Romance', 'middle', 'Ls')
    svg += hr(214, sw=0.3)
    svg += sh(224, 'CORE VOCABULARY')
    svg += t(100, 235, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 235, 'PORTUGUESE', 'middle', 'Lx')
    svg += t(390, 235, 'NOTES', 'middle', 'Lx')
    svg += hr(239, sw=0.3)
    svg += t(100, 248, 'I', 'middle', 'Ls')
    svg += t(240, 248, 'eu', 'middle', 'Ls')
    svg += t(390, 248, 'from Latin ego', 'middle', 'Ls')
    svg += t(100, 258, 'you', 'middle', 'Ls')
    svg += t(240, 258, 'tu / voc\u00ea', 'middle', 'Ls')
    svg += t(390, 258, 'tu=intimate, voc\u00ea=polite', 'middle', 'Ls')
    svg += t(100, 268, 'water', 'middle', 'Ls')
    svg += t(240, 268, '\u00e1gua', 'middle', 'Ls')
    svg += t(390, 268, 'Latin aqua', 'middle', 'Ls')
    svg += t(100, 278, 'eat', 'middle', 'Ls')
    svg += t(240, 278, 'comer', 'middle', 'Ls')
    svg += t(390, 278, 'Latin comedere', 'middle', 'Ls')
    svg += t(100, 288, 'go', 'middle', 'Ls')
    svg += t(240, 288, 'ir', 'middle', 'Ls')
    svg += t(390, 288, 'suppletive: vou/vai (pres)', 'middle', 'Ls')
    svg += t(100, 298, 'love', 'middle', 'Ls')
    svg += t(240, 298, 'amor', 'middle', 'Ls')
    svg += t(390, 298, 'amar = verb form', 'middle', 'Ls')

    svg += sec_divider(310, 'TAMAZIGHT \u2014 GRAMMAR: STATE, GENDER & ROOT SYSTEM')

    svg += sh(334, '\u2014 TAMAZIGHT GRAMMAR \u2014')
    svg += t(240, 345, 'VSO or SVO word order (debated; varies by variety)', 'middle', 'Ls')
    svg += t(240, 356, 'TWO STATES: free (absolute) vs annexed (construct) \u2014 noun changes based on syntax', 'middle', 'Ls')
    svg += hr(362, sw=0.3)
    svg += sh(372, 'THE TWO STATES OF NOUNS')
    svg += t(240, 383, 'FREE (absolute) state: used when noun is predicate, after "and", at start of sentence', 'middle', 'Ls')
    svg += t(240, 394, 'ANNEXED (construct) state: after verb (subject), after numbers, after prepositions', 'middle', 'Ls')
    svg += t(100, 405, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 405, 'FREE STATE', 'middle', 'Lx')
    svg += t(390, 405, 'ANNEXED STATE', 'middle', 'Lx')
    svg += hr(409, sw=0.3)
    svg += t(100, 418, 'man', 'middle', 'Ls')
    svg += t(240, 418, 'argaz', 'middle', 'Ls')
    svg += t(390, 418, 'urgaz (after verb/prep)', 'middle', 'Ls')
    svg += t(100, 428, 'house', 'middle', 'Ls')
    svg += t(240, 428, 'axxam', 'middle', 'Ls')
    svg += t(390, 428, 'uxxam (after verb/prep)', 'middle', 'Ls')
    svg += t(100, 438, 'woman', 'middle', 'Ls')
    svg += t(240, 438, 'tamghart', 'middle', 'Ls')
    svg += t(390, 438, 'temghart (annexed)', 'middle', 'Ls')
    svg += hr(443, sw=0.3)
    svg += sh(453, 'GENDER: t- CIRCUMFIX FOR FEMININE')
    svg += t(240, 464, 'Masculine: a- prefix \u00b7 Feminine: t-...-t circumfix', 'middle', 'Ls')
    svg += t(240, 475, 'argaz (man, masc.) \u00b7 tamghart (woman, fem.) \u2014 same root, different shape', 'middle', 'Ls')
    svg += t(240, 486, 'Amzigh (free man) \u00b7 Tamazight (free woman = the language name)', 'middle', 'Ls')
    svg += hr(492, sw=0.3)
    svg += sh(502, 'CORE VOCABULARY (TACHELHIT)')
    svg += t(100, 513, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 513, 'TACHELHIT', 'middle', 'Lx')
    svg += t(390, 513, 'KABYLE (N. ALGERIA)', 'middle', 'Lx')
    svg += hr(517, sw=0.3)
    svg += t(100, 526, 'water', 'middle', 'Ls')
    svg += t(240, 526, 'aman', 'middle', 'Ls')
    svg += t(390, 526, 'aman (same!)', 'middle', 'Ls')
    svg += t(100, 536, 'eat', 'middle', 'Ls')
    svg += t(240, 536, 'ttcha / etch', 'middle', 'Ls')
    svg += t(390, 536, 'etch', 'middle', 'Ls')
    svg += t(100, 546, 'I', 'middle', 'Ls')
    svg += t(240, 546, 'nkk / nek', 'middle', 'Ls')
    svg += t(390, 546, 'nec', 'middle', 'Ls')
    svg += t(100, 556, 'house', 'middle', 'Ls')
    svg += t(240, 556, 'axxam', 'middle', 'Ls')
    svg += t(390, 556, 'axxam (same!)', 'middle', 'Ls')
    svg += t(100, 566, 'good', 'middle', 'Ls')
    svg += t(240, 566, 'ifulki / iyzdi', 'middle', 'Ls')
    svg += t(390, 566, 'yelha / ifrir', 'middle', 'Ls')
    svg += hr(571, sw=0.3)
    svg += sh(581, 'SURVIVAL PHRASES')
    svg += t(240, 592, 'Azul! / Marhba! = Hello! (Kabyle / Tachelhit)', 'middle', 'Ls')
    svg += t(240, 603, 'Tanemmirt = Thank you (Tachelhit) \u00b7 Tanmirt = Thank you (Kabyle)', 'middle', 'Ls')
    svg += t(240, 614, 'Aman lla? = Where is water? (Kabyle: aman=water, lla=where)', 'middle', 'Ls')

    svg += footer(27, 'PORTUGUESE', 'TAMAZIGHT', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_27d_alt():
    svg = open_svg()
    svg += t(240, 32, 'PORTUGUESE (PORTUGU\u00caS) / TAMAZIGHT (\u2d5c\u2d30\u2d4e\u2d30\u2d63\u2d49\u2d56\u2d5c)', 'middle', 'T')
    svg += t(240, 44, 'INDO-EUROPEAN / AFROASIATIC \u00b7 HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 27D ALT \u00b7 HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '\u2014 PORTUGUESE: HISTORY & THE AGE OF EXPLORATION \u2014')
    svg += sh(88, 'GALICIAN-PORTUGUESE: THE ORIGIN')
    svg += t(240, 99, 'Galician-Portuguese: medieval language of Iberian lyric poetry (~1200\u20131350)', 'middle', 'Ls')
    svg += t(240, 110, 'Galician and Portuguese diverged ~14th c. as Portugal gained independence (1143)', 'middle', 'Ls')
    svg += t(240, 121, 'Cante\u00e0s de amor, cante\u00e0s de amigo, cante\u00e0s de escarnho \u2014 troubadour tradition', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'THE PORTUGUESE EMPIRE (1415\u20131975 CE)')
    svg += t(240, 148, '1415: Ceuta captured from Marinid Morocco \u2014 first Portuguese African territory', 'middle', 'Ls')
    svg += t(240, 159, '1498: Vasco da Gama reaches India via Cape of Good Hope \u2014 reshapes world trade', 'middle', 'Ls')
    svg += t(240, 170, '1500: Cabral reaches Brazil \u2014 largest Portuguese-speaking nation today', 'middle', 'Ls')
    svg += t(240, 181, 'Portuguese: first European language in sub-Saharan Africa, South Asia, SE Asia', 'middle', 'Ls')
    svg += hr(187, sw=0.3)
    svg += sh(197, 'SAUDADE: THE PORTUGUESE SOUL')
    svg += t(240, 208, 'Saudade: nostalgic longing for something loved and absent; an untranslatable emotion', 'middle', 'Ls')
    svg += t(240, 219, 'Fado music: genre built on saudade \u00b7 UNESCO intangible heritage 2011', 'middle', 'Ls')
    svg += t(240, 230, 'Pessoa, Saramago, Pessoa: Portuguese literature deeply infused with saudade', 'middle', 'Ls')
    svg += hr(236, sw=0.3)
    svg += sh(246, 'PORTUGUESE ACROSS THE ATLANTIC')
    svg += t(240, 257, 'Brazil: ~215M people; 97%+ Portuguese speakers; diverging from European standard', 'middle', 'Ls')
    svg += t(240, 268, 'PALOP: Portuguese-speaking African countries \u2014 new literature emerging (Mia Couto)', 'middle', 'Ls')
    svg += hr(274, sw=0.3)
    svg += sh(284, 'SURVIVAL PHRASE (PORTUGUESE)')
    svg += t(240, 295, 'Isto foi feito para ti, de gra\u00e7a, por pessoas que se lembraram do futuro.', 'middle', 'Ls')
    svg += t(240, 306, '"This was made for you, freely, by people who remembered the future."', 'middle', 'Ls')
    svg += t(240, 317, '(de gra\u00e7a = for free; se lembraram = remembered; futuro = future)', 'middle', 'Ls')

    svg += sec_divider(329, 'TAMAZIGHT \u2014 HISTORY: THE ORIGINAL NORTH AFRICANS')

    svg += sh(354, '\u2014 TAMAZIGHT: THE AMAZIGH PEOPLE \u2014')
    svg += sh(365, 'AMAZIGH: THE FREE PEOPLE (10,000+ YEARS IN NORTH AFRICA)')
    svg += t(240, 376, 'Imazighen (pl.): indigenous people of North Africa; "Berber" is exonym', 'middle', 'Ls')
    svg += t(240, 387, 'Predating Arab conquest (647 CE) by millennia \u2014 descendants of ancient Libyans', 'middle', 'Ls')
    svg += t(240, 398, 'Cave paintings of Tassili n\'Ajjer (Algeria): ~10,000 BCE \u2014 earliest African art', 'middle', 'Ls')
    svg += hr(404, sw=0.3)
    svg += sh(414, 'HISTORICAL AMAZIGH KINGDOMS')
    svg += t(240, 425, 'Numidia (~202\u201346 BCE): Massinissa \u2014 allied with Rome against Carthage', 'middle', 'Ls')
    svg += t(240, 436, 'Jugurtha (r. 112\u201305 BCE): resisted Rome; wars documented by Sallust', 'middle', 'Ls')
    svg += t(240, 447, 'Saint Augustine (354\u2013430 CE): born in Numidia (modern Algeria) \u2014 Amazigh heritage', 'middle', 'Ls')
    svg += hr(453, sw=0.3)
    svg += sh(463, 'ARAB CONQUEST & CULTURAL RESISTANCE')
    svg += t(240, 474, '647\u2013711 CE: Arab-Islamic conquest of North Africa', 'middle', 'Ls')
    svg += t(240, 485, 'Dihya (Kahina): Amazigh queen who led resistance to Arab conquest ~688 CE', 'middle', 'Ls')
    svg += t(240, 496, 'Arabization: Amazigh persisted in mountains and desert; Arabic in cities and plains', 'middle', 'Ls')
    svg += t(240, 507, 'Almoravid dynasty (~1050\u20131147): Sanhaja Berber empire from Morocco to Spain', 'middle', 'Ls')
    svg += hr(513, sw=0.3)
    svg += sh(523, 'MOROCCO 2011: OFFICIAL RECOGNITION')
    svg += t(240, 534, 'Arab Spring protests in Morocco: Amazigh (Tamazight) demands included', 'middle', 'Ls')
    svg += t(240, 545, '2011 Morocco constitution: Tamazight recognized as official language alongside Arabic', 'middle', 'Ls')
    svg += t(240, 556, 'IRCAM (Royal Institute of Amazigh Culture): standardizing Neo-Tifinagh script', 'middle', 'Ls')
    svg += hr(562, sw=0.3)
    svg += sh(572, 'TIFINAGH ACROSS NORTH AFRICA')
    svg += t(240, 583, 'Tuareg (Mali, Niger, Libya): still use traditional Tifinagh \u2014 passed by women', 'middle', 'Ls')
    svg += t(240, 594, 'Tifinagh survived 2,000+ years without institutional support \u2014 oral + rock inscriptions', 'middle', 'Ls')
    svg += hr(600, sw=0.3)
    svg += sh(610, 'SURVIVAL PHRASE (TAMAZIGHT \u2014 TACHELHIT)')
    svg += t(240, 621, 'Nni-s ttwag i kk, s ufus, s imdanen yura ighf-nns di tdwuri.', 'middle', 'Ls')

    svg += footer(27, 'PORTUGUESE', 'TAMAZIGHT', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate27a_portuguese_tamazight_script_alt.svg',    build_27a_alt),
        ('plate27b_portuguese_tamazight_phonology_alt.svg',  build_27b_alt),
        ('plate27c_portuguese_tamazight_grammar_alt.svg',    build_27c_alt),
        ('plate27d_portuguese_tamazight_history_alt.svg',    build_27d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
