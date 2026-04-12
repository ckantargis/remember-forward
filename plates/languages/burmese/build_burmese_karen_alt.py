#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Burmese / S'gaw Karen alt plate series 40A–40D for Remember Forward.
Secondary language: S'gaw Karen (ကညီကျိာ်) — spoken across eastern Myanmar
and western Thailand. Within ~500 miles of Burmese geographic center (Naypyidaw).
~2–3 million speakers. Tibeto-Burman family. SVO order (typological contrast with Burmese SOV).
Script: adapted Burmese/Mon-based script established ~1832 CE.
"""
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
        '  .Lb{font-size:11px} .Lbs{font-size:8px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')

def close_svg(): return '</svg>\n'

def t(x, y, s, a='middle', c='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y, txt, c='H'):
    return t(240, y, f'\u2014 {txt} \u2014', 'middle', c)

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


# ─── PLATE 40A ALT — SCRIPT ───────────────────────────────────────────────────

def build_40a_alt():
    g = open_svg()
    g += t(240, 30, "BURMESE + S\u2019GAW KAREN \u2014 SCRIPT \u00b7 WRITING SYSTEMS", 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 40A \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: BURMESE SCRIPT ──
    g += sh(63, 'BURMESE \u2014 ABUGIDA SCRIPT \u2014 BRAHMIC ORIGIN')
    g += t(240, 73, 'Burmese script: abugida descended from Mon script \u2014 itself from South Indian Brahmic (~4th c. CE).', 'middle', 'Ls')
    g += t(240, 82, 'Distinctive rounded letterforms: developed writing on palm leaves, where angular strokes tear the surface.', 'middle', 'Lx')
    g += t(240, 91, 'Written left to right. Consonants carry inherent /a/. Diacritics modify vowel. 33 consonants, 3 tones.', 'middle', 'Lx')
    g += hr(98)

    g += sh(106, 'CORE CONSONANTS \u2014 SAMPLE (6 ROWS)')
    rows = [
        [('\u1000','ka'), ('\u1001','hka'), ('\u1002','ga'), ('\u1004','nga'), ('\u1005','ca')],
        [('\u1006','hca'), ('\u1007','ja'), ('\u1009','nya'), ('\u100a','nnya'), ('\u100b','ta')],
        [('\u100f','na'), ('\u1010','ta'), ('\u1011','hta'), ('\u1012','da'), ('\u1014','na')],
        [('\u1015','pa'), ('\u1016','hpa'), ('\u1017','ba'), ('\u1018','bha'), ('\u1019','ma')],
        [('\u101a','ya'), ('\u101b','ra'), ('\u101c','la'), ('\u101d','wa'), ('\u101e','sa')],
        [('\u101f','ha'), ('\u1020','la'), ('\u1021','a'), ('',''), ('','')],
    ]
    for row_i, row in enumerate(rows):
        y = 116 + row_i * 13
        for col_i, (ch, gloss) in enumerate(row):
            if ch:
                x = 55 + col_i * 80
                g += t(x, y, ch, 'middle', 'Lb')
                g += t(x, y + 8, gloss, 'middle', 'Lx')

    g += hr(198)
    g += sh(206, 'TONE DIACRITICS \u2014 3 TONES')
    tones = [
        ('\u1000\u102c', 'Level (ka)', 'short, modal, mid-low'),
        ('\u1000\u102c\u1038', 'Heavy (kaa)', 'long, creaky, falling'),
        ('\u1000\u102d\u1037', "Creaky (ka')", 'short, creaky+glottal'),
    ]
    for i, (syl, name, desc) in enumerate(tones):
        y = 216 + i * 11
        g += t(70, y, syl, 'middle', 'Lb')
        g += t(180, y, name, 'middle', 'Ls')
        g += t(360, y, desc, 'middle', 'Lx')

    g += hr(252)
    g += sh(260, 'BURMESE NUMERALS  \u1040\u1041\u1042\u1043\u1044\u1045\u1046\u1047\u1048\u1049')
    g += t(240, 272, 'Brahmi-origin numerals. Same base-10 structure as Devanagari and Arabic numerals.', 'middle', 'Lx')

    # ── SECONDARY: S'GAW KAREN ──
    g += sec_divider(282, "SECONDARY \u2014 S\u2019GAW KAREN \u2014 ကညီကျိာ် \u2014 SCRIPT \u00b7 WRITING")

    g += sh(308, "S\u2019GAW KAREN SCRIPT \u2014 BURMESE-BASED ADAPTATION")
    g += t(240, 318, "S\u2019gaw Karen uses a modified form of the Burmese/Mon script established ~1832 CE by", 'middle', 'Ls')
    g += t(240, 327, 'Baptist missionary Jonathan Wade and Karen evangelist Ko Tha Byu. Same Unicode block (U+1000\u2013U+109F).', 'middle', 'Lx')
    g += t(240, 336, 'Karen letters use Burmese character shapes but with different phonemic values and additional stacking.', 'middle', 'Lx')
    g += hr(344)

    g += sh(352, "S\u2019GAW KAREN \u2014 SAMPLE SYLLABLES (ROMANIZED + SCRIPT NOTES)")
    karen_syl = [
        ('kaw lah', "S\u2019gaw Karen", 'self-name: \u201cKaw Lah\u201d (people/human)'),
        ('pga k\u0302nyw\u0302', 'language / word', 'lit. mouth/voice of the people'),
        ('ta', 'one', 'monosyllabic base form'),
        ('ler', 'water', 'core vocabulary'),
        ('mu', 'sky / heaven', 'also: world above'),
        ('naw', 'woman', 'gender-marked pronoun base'),
        ('saw', 'man / person', 'also personal name prefix'),
    ]
    for i, (rom, gloss, note) in enumerate(karen_syl):
        y = 362 + i * 10
        g += t(80, y, rom, 'middle', 'Ls')
        g += t(200, y, gloss, 'middle', 'Lx')
        g += t(370, y, note, 'middle', 'Lx')

    g += hr(435)
    g += sh(443, 'SCRIPT BRIDGE \u2014 SHARED ORIGIN, DIVERGENT PATHS')
    g += t(240, 453, 'Burmese and Karen scripts share the same Mon/Brahmic ancestor and Unicode block.', 'middle', 'Ls')
    g += t(240, 462, 'Burmese: organic Brahmic evolution. Karen: missionary adaptation for new phonology and tones.', 'middle', 'Lx')
    g += t(240, 471, "S\u2019gaw Karen has 7 tones \u2014 more than Burmese (3+1). Extra diacritics encode the additional tone distinctions.", 'middle', 'Lx')
    g += t(240, 480, 'Both read left to right. Karen adds tone letters after the rhyme, whereas Burmese uses diacritic marks.', 'middle', 'Lx')

    g += footer('40', 'Burmese', "S\u2019gaw Karen", 'A', 'Script')
    return g + close_svg()


# ─── PLATE 40B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_40b_alt():
    g = open_svg()
    g += t(240, 30, "BURMESE + S\u2019GAW KAREN \u2014 PHONOLOGY", 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 40B \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: BURMESE PHONOLOGY ──
    g += sh(63, 'BURMESE \u2014 THREE-TONE SYSTEM')
    g += t(240, 73, 'Burmese is a tonal language with 3 phonemic tones + a 4th \u201cchecked\u201d syllable type:', 'middle', 'Ls')
    tones = [
        ('Level (low)', 'short, modal voice, mid-low pitch: ma = horse'),
        ('Heavy (long)', 'long, creaky voice, falling pitch: m\u00e0 = come'),
        ('Creaky (high)', "short, creaky, glottal stop: ma' = hard"),
        ('Checked (stop)', 'unreleased stop coda; short, high, glottal'),
    ]
    for i, (name, desc) in enumerate(tones):
        y = 83 + i * 11
        g += t(110, y, name, 'middle', 'Ls')
        g += t(330, y, desc, 'middle', 'Lx')
    g += hr(128)

    g += sh(136, 'BURMESE CONSONANTS \u2014 KEY CONTRASTS')
    g += t(240, 146, 'Burmese distinguishes voiceless / aspirated / voiced series. 4 nasal consonants.', 'middle', 'Ls')
    pairs = [
        ('p /p/', 'ph /p\u02b0/', 'b /b/', 'bilabial'),
        ('t /t/', 'th /t\u02b0/', 'd /d/', 'alveolar'),
        ('k /k/', 'kh /k\u02b0/', 'g /g/', 'velar'),
        ('c /t\u0255/', 'ch /t\u0255\u02b0/', 'j /d\u0292/', 'palatal aff.'),
    ]
    for i, (vl, asp, vd, place) in enumerate(pairs):
        y = 156 + i * 11
        g += t(70, y, vl, 'middle', 'Lx')
        g += t(180, y, asp, 'middle', 'Lx')
        g += t(290, y, vd, 'middle', 'Lx')
        g += t(400, y, place, 'middle', 'Lx')
    g += hr(205)

    g += sh(213, 'BURMESE MEDIALS \u2014 COMPLEX ONSET CLUSTERS')
    g += t(240, 223, 'Burmese allows medial consonants (y, w, r, h) before the vowel within one syllable:', 'middle', 'Ls')
    g += t(240, 232, 'kya /t\u0255a/, mya /mja/, kwa /kwa/, hma /m\u0329a/. Medials change the onset phonologically.', 'middle', 'Lx')

    g += hr(241)
    g += sh(249, 'BURMESE VOWEL SYSTEM')
    g += t(240, 259, 'Short/long pairs: a/aa, i/ii, u/uu, e/ee, o/oo. Diphthongs: ai, au, ia, ua.', 'middle', 'Ls')
    g += t(240, 268, 'Schwa /\u0259/ common in unstressed syllables (often written -a). Vowel length + tone = distinct syllable types.', 'middle', 'Lx')

    # ── SECONDARY: S'GAW KAREN ──
    g += sec_divider(278, "SECONDARY \u2014 S\u2019GAW KAREN \u2014 PHONOLOGY \u00b7 SEVEN TONES")

    g += sh(304, "S\u2019GAW KAREN \u2014 SEVEN-TONE SYSTEM")
    g += t(240, 314, "S\u2019gaw Karen has 7 phonemic tones \u2014 more than any of its Burmese neighbors:", 'middle', 'Ls')
    karen_tones = [
        ('Tone 1', 'high level', 'highest pitch, sustained'),
        ('Tone 2', 'high falling', 'starts high, drops quickly'),
        ('Tone 3', 'mid level', 'modal voice, mid pitch'),
        ('Tone 4', 'low falling', 'drops to low register'),
        ('Tone 5', 'low checked', 'short + glottal stop, low'),
        ('Tone 6', 'high rising', 'rises sharply, breathy'),
        ('Tone 7', 'mid checked', 'short stop, mid register'),
    ]
    for i, (name, desc, note) in enumerate(karen_tones):
        y = 324 + i * 10
        g += t(70, y, name, 'middle', 'Lx')
        g += t(190, y, desc, 'middle', 'Lx')
        g += t(360, y, note, 'middle', 'Lx')
    g += hr(398)

    g += sh(406, "S\u2019GAW KAREN \u2014 CONSONANT INVENTORY")
    g += t(240, 416, 'Rich stop series: voiceless/aspirated/voiced across bilabial, alveolar, velar, glottal positions.', 'middle', 'Ls')
    g += t(240, 425, 'Implosive consonants: /\u0253/ (bilabial), /\u0257/ (alveolar) \u2014 absent from Burmese. Distinctive resonant quality.', 'middle', 'Lx')
    g += t(240, 434, 'Uvular stop /q/ and uvular fricative present in some dialects (Pwo Karen sub-group).', 'middle', 'Lx')
    g += hr(442)

    g += sh(450, 'PHONOLOGICAL BRIDGE \u2014 TONAL COMPARISON')
    g += t(240, 460, 'Burmese: 3 tones + checked. Karen: 7 tones. Both are Tibeto-Burman; both are monosyllabic-dominant.', 'middle', 'Ls')
    g += t(240, 469, 'Despite shared family, the tone systems diverged significantly. More tones = more minimal pairs resolved by tone alone.', 'middle', 'Lx')
    g += t(240, 478, 'Example: S\u2019gaw Karen \u201cler\u201d with different tones = water / cry / sky / down. Tone is lexically contrastive.', 'middle', 'Lx')

    g += footer('40', 'Burmese', "S\u2019gaw Karen", 'B', 'Phonology')
    return g + close_svg()


# ─── PLATE 40C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_40c_alt():
    g = open_svg()
    g += t(240, 30, "BURMESE + S\u2019GAW KAREN \u2014 GRAMMAR", 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 40C \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: BURMESE GRAMMAR ──
    g += sh(63, 'BURMESE GRAMMAR \u2014 SOV \u00b7 PARTICLE-MARKING')
    g += t(240, 73, 'Burmese is Subject-Object-Verb (SOV). Verb always comes last. Particles follow every major phrase.', 'middle', 'Ls')
    g += t(240, 82, 'nga htamin sa de \u2014 I rice eat (present). nga=I, htamin=rice, sa=eat, de=assertion particle.', 'middle', 'Lx')
    g += hr(90)

    g += sh(98, 'CASE PARTICLES')
    particles = [
        ('-ga / -k\u0259', 'subject/topic marker'),
        ('-go', 'object / direction'),
        ('-hma', 'locative (at/in/on)'),
        ('-pei', 'benefactive (for)'),
        ('-h\u0259', 'ablative (from)'),
        ('-n\u0259', 'instrumental (with/by)'),
    ]
    for i, (p, gloss) in enumerate(particles):
        y = 108 + i * 10
        g += t(130, y, p, 'middle', 'Ls')
        g += t(320, y, gloss, 'middle', 'Lx')
    g += hr(175)

    g += sh(183, 'VERB ASPECT PARTICLES')
    verbs = [
        ('sa de', 'eats (present assertion)'),
        ('sa m\u025b', 'will eat (future)'),
        ('sa b\u00ed', 'ate (past completive)'),
        ("sa \u02a1\u00e6", 'is eating (progressive)'),
        ('ma-sa-b\u00fa', 'did not eat (past negative)'),
    ]
    for i, (form, gloss) in enumerate(verbs):
        y = 193 + i * 10
        g += t(130, y, form, 'middle', 'Ls')
        g += t(330, y, gloss, 'middle', 'Lx')
    g += hr(252)

    g += sh(260, 'BURMESE CORE VOCABULARY')
    bvocab = [
        ('ye', 'water'), ('m\u00edq', 'fire'), ('m\u0259j\u00e9', 'earth'),
        ('lu', 'person'), ('l\u00e0', 'moon'), ('n\u00e4-n\u00e4', 'future'),
        ('mh\u00e0u-z\u00e0', 'memory'), ('v\u00edq-th\u00e0', 'freedom'),
    ]
    for i, (w, e) in enumerate(bvocab):
        col = i % 2; row = i // 2
        x = 90 + col * 220; y = 270 + row * 10
        g += t(x, y, w, 'middle', 'Ls')
        g += t(x + 80, y, e, 'middle', 'Lx')

    # ── SECONDARY: S'GAW KAREN ──
    g += sec_divider(314, "SECONDARY \u2014 S\u2019GAW KAREN \u2014 GRAMMAR \u00b7 SVO ORDER")

    g += sh(340, "S\u2019GAW KAREN \u2014 SVO WORD ORDER (TYPOLOGICAL CONTRAST)")
    g += t(240, 350, "S\u2019gaw Karen is Subject-Verb-Object (SVO) \u2014 a major typological contrast with Burmese SOV.", 'middle', 'Ls')
    g += t(240, 359, "Despite being geographically adjacent and Tibeto-Burman relatives, these two languages have opposite word order.", 'middle', 'Lx')
    g += t(240, 368, "Karen SVO: Saw ta ler \u2014 Person drinks water. (saw=person, ta=drink, ler=water)", 'middle', 'Lx')
    g += hr(376)

    g += sh(384, "S\u2019GAW KAREN \u2014 ISOLATING STRUCTURE")
    g += t(240, 394, "Karen is highly isolating. Words do not inflect for tense, number, or case. Context + particles signal grammar.", 'middle', 'Ls')
    g += t(240, 403, 'Tense markers: temporal adverbs and particles (yesterday / tomorrow / now) placed before or after the verb.', 'middle', 'Lx')
    g += t(240, 412, 'Negation: particle placed before verb. Yes/no questions: rising intonation or final question particle.', 'middle', 'Lx')
    g += hr(420)

    g += sh(428, "S\u2019GAW KAREN \u2014 CORE VOCABULARY")
    kvocab = [
        ('ler', 'water'), ('mi', 'fire'), ('hsa', 'earth/ground'),
        ('saw', 'person/man'), ('naw', 'woman'), ('ta taw', 'moon'),
        ('pga k\u0302nyw\u0302', 'language'), ('pghe', 'remember'),
        ('tha', 'heart'), ('mu', 'sky / future'), ('k\u0302law', 'freedom'),
        ('kaw lah', 'Karen people'),
    ]
    for i, (w, e) in enumerate(kvocab):
        col = i % 2; row = i // 2
        x = 90 + col * 220; y = 438 + row * 10
        g += t(x, y, w, 'middle', 'Ls')
        g += t(x + 90, y, e, 'middle', 'Lx')

    g += hr(502)
    g += sh(510, 'GRAMMAR BRIDGE \u2014 SOV vs. SVO')
    g += t(240, 520, 'Burmese (SOV): nga htamin sa de \u2014 I rice eat-ASSERT.', 'middle', 'Ls')
    g += t(240, 529, "S\u2019gaw Karen (SVO): Nga ta htamin \u2014 I eat rice. Verb precedes object.", 'middle', 'Ls')
    g += t(240, 538, 'Two Tibeto-Burman languages, 500 miles apart \u2014 opposite word orders. Both monosyllabic, both tonal.', 'middle', 'Lx')

    g += footer('40', 'Burmese', "S\u2019gaw Karen", 'C', 'Grammar')
    return g + close_svg()


# ─── PLATE 40D ALT — TEXT ─────────────────────────────────────────────────────

def build_40d_alt():
    g = open_svg()
    g += t(240, 30, "BURMESE + S\u2019GAW KAREN \u2014 RUNNING TEXT", 'middle', 'T')
    g += t(240, 46, 'ALT DRAFT \u00b7 SERIES 40D \u00b7 REMEMBER FORWARD', 'middle', 'S')
    g += hr(54)

    # ── PRIMARY: BURMESE TEXT ──
    g += sh(63, 'I. BURMESE PROVERB \u2014 ON MEMORY')
    g += t(240, 73, '\u101b\u103e\u1031\u102c\u101e\u1030\u1038\u1000\u102d\u102f \u1019\u103e\u1010\u100a\u100a\u102c\u101e\u100a\u1037 \u1021\u1014\u102c\u1001\u102c\u101c\u102c\u1014\u1031\u1037', 'middle', 'Lb')
    g += t(240, 87, 'yaungo-kyi  mhaw-htaung-tha   ana-kala  la-ne', 'middle', 'Lx')
    g += t(240, 96, '"Remembering the past is how the future comes to us."', 'middle', 'F')
    g += hr(104)

    g += sh(112, 'II. BURMESE SAYING \u2014 ON KNOWLEDGE')
    g += t(240, 122, '\u1015\u100a\u100a\u102c\u1006\u102c\u101e\u100a\u1037 \u1019\u102e\u1038\u1000\u102d\u102f\u1038 \u1019\u1015\u103c\u102f\u1011\u100f\u102c\u1021\u1036', 'middle', 'Lb')
    g += t(240, 136, 'pannya-hka-tha  myi-kyi-mya  ma-pyaw-hpan', 'middle', 'Lx')
    g += t(240, 145, '"The flame of wisdom cannot be extinguished."', 'middle', 'F')
    g += hr(153)

    g += sh(161, 'III. BURMESE BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240, 173, '\u1012\u102e\u1012\u101d\u101c\u102c\u101e\u100a\u1037\u1000\u102d\u102f \u1001\u1004\u102b\u101e\u1030\u1038\u1021\u1010\u103a\u1000\u102c', 'middle', 'Lb')
    g += t(240, 187, '\u1005\u101b\u102d\u102f\u1001\u100a\u1038\u1014\u103e\u1004\u1037\u101e\u100a\u1037', 'middle', 'Lb')
    g += t(240, 200, '\u1021\u101b\u103e\u1031\u102c\u101e\u102d\u102f\u1038 \u101e\u1010\u102d\u1019\u103e\u1010\u102c\u1038\u101e\u100a\u1037 \u101c\u1030\u101c\u102c\u101e\u100a\u1037\u1000\u101e\u102d\u1037', 'middle', 'Lb')
    g += t(240, 213, 'di-da-la-tha kyi u-hka-mhu (this freely for-you was-made)', 'middle', 'Lx')
    g += t(240, 222, 'amyaungo-da-la-tha shi-thma-de lu-la-tha doh-a-hyi (forward remembering people by)', 'middle', 'Lx')
    g += t(240, 231, '"This was made for you, freely, by people who remembered forward." (Burmese)', 'middle', 'F')
    g += hr(240)

    g += sh(248, 'BURMESE NOTE \u2014 \u201cFORWARD\u201d')
    g += t(240, 258, 'A-myaung-go (\u1021\u101b\u103e\u1031\u102c\u101e\u102d\u102f\u1038) = forward/front. In Burmese, the future lies \u201cahead\u201d \u2014 a spatial metaphor.', 'middle', 'Ls')
    g += t(240, 267, 'Mhaw-z\u00e0 (\u1019\u103e\u1031\u102c\u1038\u1038\u101e\u102c) = to remember \u2014 lit. to recall/pick up memory. SOV verb-final structure preserved.', 'middle', 'Lx')

    # ── SECONDARY: S'GAW KAREN ──
    g += sec_divider(278, "SECONDARY \u2014 S\u2019GAW KAREN \u2014 RUNNING TEXT \u00b7 PASSAGES")

    g += sh(304, "I. S\u2019GAW KAREN \u2014 PROVERB ON REMEMBRANCE")
    g += t(240, 314, 'Pghe pga mu eh \u2014 pga pghe kaw lah eh.', 'middle', 'L')
    g += t(240, 324, 'Remember-the-sky \u2014 the-sky remember Karen-people.', 'middle', 'Lx')
    g += t(240, 333, '"Remember the sky \u2014 the sky remembers the Karen people." (Karen oral tradition)', 'middle', 'F')
    g += hr(341)

    g += sh(349, "II. S\u2019GAW KAREN \u2014 BRIDGE PHRASE \u2014 REMEMBER FORWARD")
    g += t(240, 360, 'Ta pga naw deh, keh klaw, saw pghe mu eh ta deh.', 'middle', 'L')
    g += t(240, 371, 'This for-you  made freely  people remember forward who by made.', 'middle', 'Lx')
    g += t(240, 380, '"This was made for you, freely, by people who remembered forward."', 'middle', 'F')
    g += hr(389)

    g += sh(397, "S\u2019GAW KAREN NOTE \u2014 \u201cFORWARD\u201d AND \u201cFUTURE\u201d")
    g += t(240, 407, '\u201cMu\u201d in S\u2019gaw Karen means sky, world-above, heaven \u2014 and by extension: future, what lies ahead.', 'middle', 'Ls')
    g += t(240, 416, 'The spatial metaphor (forward = above/sky) differs from Burmese (forward = ahead/front) \u2014 a cultural contrast.', 'middle', 'Lx')
    g += t(240, 425, '\u201cPghe\u201d = to remember, to recall. In Karen oral tradition, memory is tied to the ancestors and the sky.', 'middle', 'Lx')
    g += hr(434)

    g += sh(442, 'LANGUAGE BRIDGE \u2014 TWO NEIGHBORS')
    g += t(240, 452, 'Burmese: ~33M speakers, official state language of Myanmar. Mon/Brahmic script, SOV, 3 tones.', 'middle', 'Ls')
    g += t(240, 461, "S\u2019gaw Karen: ~2-3M speakers, eastern Myanmar + western Thailand. SVO, 7 tones, Burmese-based script.", 'middle', 'Ls')
    g += t(240, 470, 'Both Sino-Tibetan (Tibeto-Burman); both tonal; opposite word order. Living side by side for millennia.', 'middle', 'Lx')
    g += t(240, 479, 'Karen people maintained cultural autonomy through oral epic tradition. Script established by missionaries 1832 CE.', 'middle', 'Lx')

    g += footer('40', 'Burmese', "S\u2019gaw Karen", 'D', 'Running Text')
    return g + close_svg()


def main():
    plates = {
        'plate40a_burmese_karen_script_alt.svg':    build_40a_alt(),
        'plate40b_burmese_karen_phonology_alt.svg': build_40b_alt(),
        'plate40c_burmese_karen_grammar_alt.svg':   build_40c_alt(),
        'plate40d_burmese_karen_text_alt.svg':      build_40d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
