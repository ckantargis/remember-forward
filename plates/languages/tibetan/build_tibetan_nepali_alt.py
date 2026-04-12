"""
Batch 11 — Tibetan + Nepali alt plates (Series 56, plates 56a–56d)
Secondary language: Nepali (~17M speakers, Indo-Aryan, Nepal/India/Bhutan)
Geographic link: Lhasa (Tibetan center) to Kathmandu (Nepal) ~350mi
Both Himalayan languages; Nepal is Tibet's southern neighbor; ancient trade and pilgrimage routes
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

# ── PLATE 56a  SCRIPT ────────────────────────────────────────────────────────
def plate56a():
    s = open_svg()
    s += t(240, 28, 'TIBETAN', 'middle', 'T')
    s += t(240, 40, 'TIBETAN SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'UCHEN SCRIPT — "HEAD LETTER"')
    s += t(240, 68, 'Tibetan script created ~620 CE by Thonmi Sambhota', 'middle', 'L')
    s += t(240, 79, 'Commissioned by King Songtsen Gampo to translate Buddhist texts', 'middle', 'Ls')
    s += t(240, 90, 'Derived from Brahmi via Gupta script tradition', 'middle', 'Ls')
    s += t(240, 101, 'Abugida: 30 consonants + inherent /a/ vowel', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'TIBETAN CONSONANTS')
    s += t(240, 128, '\u0f40 k  \u0f41 kh  \u0f42 g  \u0f44 ng  \u0f45 c  \u0f46 ch  \u0f47 j  \u0f49 ny', 'middle', 'L')
    s += t(240, 139, '\u0f4f t  \u0f50 th  \u0f51 d  \u0f53 n  \u0f54 p  \u0f55 ph  \u0f56 b  \u0f58 m', 'middle', 'L')
    s += t(240, 150, '\u0f5e ts  \u0f5f tsh  \u0f60 dz  \u0f61 w  \u0f62 zh  \u0f63 z  \u0f63 \u0027  \u0f64 y', 'middle', 'L')
    s += t(240, 161, '\u0f65 r  \u0f66 l  \u0f67 sh  \u0f68 s  \u0f69 h  \u0f6a a', 'middle', 'L')
    s += hr(169)
    s += sh(177, 'STACKED LETTERS')
    s += t(240, 188, 'Tibetan uses vertical stacks for consonant clusters:', 'middle', 'L')
    s += t(240, 199, 'Superscripts and subscripts modify pronunciation', 'middle', 'Ls')
    s += t(240, 210, '\u0f54\u0fb2\u0f0b\u0f40 = "Prak" (superscribed r)', 'middle', 'L')
    s += t(240, 221, 'Most stacks are now silent (archaic orthography)', 'middle', 'Ls')
    s += hr(229)
    s += sh(237, 'SAMPLE')
    s += t(240, 249, '\u0f60\u0f42\u0f62\u0f7c\u0f66 \u0f60\u0f51\u0f7a\u0f56\u0f66\u0f0b \u0f54\u0f7c\u0f0b  "Tashi Delek" (Good Luck/Blessings)', 'middle', 'L')
    s += hr(257)
    # Divider
    s += sec_divider(264, 'NEPALI  \u00b7  \u0928\u0947\u092a\u093e\u0932\u0940  \u00b7  SECONDARY LANGUAGE')
    s += sh(289, 'DEVANAGARI SCRIPT FOR NEPALI')
    s += t(240, 300, 'Nepali written in Devanagari (same as Hindi, Marathi, Sanskrit)', 'middle', 'L')
    s += t(240, 311, 'Devanagari: "city of the gods" script; left-to-right abugida', 'middle', 'Ls')
    s += t(240, 322, '36+ consonants; inherent /a/ vowel; vowel matras above/below/beside', 'middle', 'Ls')
    s += hr(330)
    s += sh(338, 'NEPALI DEVANAGARI SAMPLE')
    s += t(240, 350, '\u0928\u092e\u0938\u094d\u0924\u0947  Namaste "Hello" (also: "I bow to you")', 'middle', 'L')
    s += t(240, 361, '\u0928\u0947\u092a\u093e\u0932  Nepal "Nepal"', 'middle', 'L')
    s += t(240, 372, '\u0927\u0928\u094d\u092f\u0935\u093e\u0926  Dhanyavaad "Thank you"', 'middle', 'L')
    s += hr(380)
    s += sh(388, 'SCRIPT CONTRAST')
    s += t(240, 399, 'Tibetan: Uchen (with serifs, angular base)', 'middle', 'L')
    s += t(240, 410, 'Nepali: Devanagari (horizontal headline bar connects letters)', 'middle', 'L')
    s += t(240, 421, 'Both: abugida (inherent vowel + vowel diacritics)', 'middle', 'L')
    s += t(240, 432, 'Both: Brahmi ancestry — same scriptural root, different branches', 'middle', 'Ls')
    s += t(240, 443, 'Tibetan script also used for writing Nepali by Tibetan communities', 'middle', 'Ls')
    s += footer('56', 'TIBETAN', 'NEPALI', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 56b  PHONOLOGY ─────────────────────────────────────────────────────
def plate56b():
    s = open_svg()
    s += t(240, 28, 'TIBETAN', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TIBETAN TONAL SYSTEM')
    s += t(240, 68, 'Central Tibetan (Lhasa dialect): 2 register tones', 'middle', 'L')
    s += t(240, 79, 'High register: voiceless onset + high or falling pitch', 'middle', 'L')
    s += t(240, 90, 'Low register: voiced onset (or historical voiced) + low or rising', 'middle', 'L')
    s += t(240, 101, 'Tones arose from historical voiced/voiceless consonant distinction', 'middle', 'Ls')
    s += t(240, 112, 'Classic Tibetan script does NOT mark tones (oral tradition)', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'SILENT CONSONANT STACKS')
    s += t(240, 139, 'Classical spelling preserves many now-silent consonants:', 'middle', 'L')
    s += t(240, 150, 'brgya = written /b-r-g-y-a/ = spoken /gya/ "hundred"', 'middle', 'L')
    s += t(240, 161, 'mkhan = written /m-k-h-a-n/ = spoken /khen/ "master"', 'middle', 'Ls')
    s += t(240, 172, 'Script reflects classical pronunciation from ~700 CE', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'TIBETAN VOWELS')
    s += t(240, 199, 'Four vowels: a i u e (+ long counterparts)', 'middle', 'L')
    s += t(240, 210, 'Vowel quality tied to register: high = tenser vowels', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'NEPALI PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'NEPALI CONSONANT SYSTEM')
    s += t(240, 261, 'Full Indo-Aryan four-way stop contrast:', 'middle', 'L')
    s += t(240, 272, 'p ph b bh \u2022 t th d dh \u2022 k kh g gh', 'middle', 'L')
    s += t(240, 283, 'Retroflex series: \u0288 \u0288h \u0256 \u0256h \u1e47 (from Sanskrit)', 'middle', 'L')
    s += t(240, 294, 'No tones (unlike Tibetan)', 'middle', 'L')
    s += hr(302)
    s += sh(310, 'NEPALI VOWELS')
    s += t(240, 321, 'Six oral vowels: a \u0101 i \u012b u \u016b e o', 'middle', 'L')
    s += t(240, 332, 'Nasalized vowels marked with chandrabindu: \u0101\u0303 \u0129 \u00f5', 'middle', 'L')
    s += t(240, 343, 'No long/short distinction in spoken modern Nepali', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'PHONOLOGICAL CONTRAST')
    s += t(240, 370, 'Tibetan: tonal, few aspirates in modern spoken form', 'middle', 'L')
    s += t(240, 381, 'Nepali: non-tonal, four-way aspirate contrast', 'middle', 'L')
    s += t(240, 392, 'Both: aspiration as phonemic (but different systems)', 'middle', 'Ls')
    s += t(240, 403, 'Nepali: retroflex series  \u2022  Tibetan: no retroflexes', 'middle', 'Ls')
    s += t(240, 414, 'Mountain altitude shaped both: minimal articulatory energy', 'middle', 'Ls')
    s += footer('56', 'TIBETAN', 'NEPALI', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 56c  GRAMMAR ───────────────────────────────────────────────────────
def plate56c():
    s = open_svg()
    s += t(240, 28, 'TIBETAN', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TIBETAN WORD ORDER: SOV')
    s += t(240, 68, 'Strictly verb-final: S + O + V', 'middle', 'L')
    s += t(240, 79, 'nga dpe-cha klog-pa-yin "I book read-do" = "I read a book"', 'middle', 'L')
    s += t(240, 90, 'Postpositions: la (to/at) \u2022 nas (from/since) \u2022 gi (gen.)', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'TIBETAN CASE SYSTEM (7 CASES)')
    s += t(240, 117, 'Agentive (ergative marker): =gyis marks agent of transitive verb', 'middle', 'L')
    s += t(240, 128, 'Absolutive: unmarked; patient of transitive and subject of intransitive', 'middle', 'L')
    s += t(240, 139, 'Genitive \u2022 Dative \u2022 Ablative \u2022 Locative \u2022 Associative', 'middle', 'L')
    s += t(240, 150, 'Tibetan is ergative-absolutive! (uncommon alignment)', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'EVIDENTIALITY IN TIBETAN')
    s += t(240, 177, 'Verbs mark how speaker knows the information:', 'middle', 'L')
    s += t(240, 188, 'Direct evidence: -song (I witnessed it)', 'middle', 'L')
    s += t(240, 199, 'Reported: -zer (someone told me)', 'middle', 'L')
    s += t(240, 210, 'Inference: -yod-pa-red (I deduce from evidence)', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'NEPALI GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'NEPALI WORD ORDER: SOV')
    s += t(240, 261, 'Same SOV order as Tibetan: Subject + Object + Verb', 'middle', 'L')
    s += t(240, 272, 'Ma kitaab pardhchu. "I book read." = "I read a book."', 'middle', 'L')
    s += t(240, 283, 'Postpositions: maa (in) \u2022 le (ergative) \u2022 laai (dative) \u2022 bata (from)', 'middle', 'L')
    s += hr(291)
    s += sh(299, 'NEPALI ERGATIVITY')
    s += t(240, 310, 'Nepali is ALSO split ergative (like Tibetan)!', 'middle', 'L')
    s += t(240, 321, 'Past transitive: agent takes -le; verb agrees with object', 'middle', 'L')
    s += t(240, 332, 'Usle kitaab paryo. "He-ERG book read-3SG." (agent takes -le)', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'NEPALI VERB SYSTEM')
    s += t(240, 359, 'Verbs agree with subject and object in person and number', 'middle', 'L')
    s += t(240, 370, 'Rich honorific system: three politeness levels in verb forms', 'middle', 'L')
    s += t(240, 381, 'Tapai (polite) / timi (familiar) / ta (intimate)', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'HIMALAYAN GRAMMATICAL PARALLELS')
    s += t(240, 408, 'Both: SOV word order  \u2022  postpositions  \u2022  split ergativity', 'middle', 'L')
    s += t(240, 419, 'Both: honorific systems (social register in grammar)', 'middle', 'L')
    s += t(240, 430, 'Tibetan: evidentiality system  \u2022  Nepali: simpler tense-aspect', 'middle', 'Ls')
    s += t(240, 441, 'Tibetan: ergative-absolutive  \u2022  Nepali: split ergativity (simpler)', 'middle', 'Ls')
    s += footer('56', 'TIBETAN', 'NEPALI', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 56d  HISTORY ───────────────────────────────────────────────────────
def plate56d():
    s = open_svg()
    s += t(240, 28, 'TIBETAN', 'middle', 'T')
    s += t(240, 40, 'HISTORY & THE HIMALAYAN WORLD', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TIBETAN EMPIRE')
    s += t(240, 68, '~618-842 CE: Tibetan Empire; one of Asia\'s great powers', 'middle', 'L')
    s += t(240, 79, 'Songtsen Gampo: unified Tibet, created script, married Nepali princess!', 'middle', 'L')
    s += t(240, 90, 'Bhrikuti: Nepali princess brought Buddhism to Tibet from Nepal', 'middle', 'Ls')
    s += t(240, 101, '763 CE: Tibetan armies briefly occupy Chang\'an (Chinese capital)', 'middle', 'Ls')
    s += t(240, 112, '842 CE: Imperial collapse; fragmentation into petty kingdoms', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'BUDDHISM AND TIBETAN CULTURE')
    s += t(240, 139, '7th c.: Buddhism enters Tibet from India and Nepal', 'middle', 'L')
    s += t(240, 150, 'Padmasambhava: brought Vajrayana Buddhism; Tibetan Buddhist canon', 'middle', 'Ls')
    s += t(240, 161, '~6M speakers; Buddhist scripture preserves vast Indian knowledge', 'middle', 'L')
    s += t(240, 172, 'Kangyur + Tengyur: 100+ volumes of translated Buddhist texts', 'middle', 'Ls')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'NEPALI HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'NEPAL AS HIMALAYAN CROSSROADS')
    s += t(240, 223, 'Kathmandu Valley: ancient trade route between India and Tibet', 'middle', 'L')
    s += t(240, 234, 'Licchavi dynasty (400-750 CE): Nepal as cultural bridge state', 'middle', 'Ls')
    s += t(240, 245, 'Bhrikuti: princess who took Buddhism north to Tibet (~630 CE)', 'middle', 'L')
    s += t(240, 256, 'Newari: indigenous language of Kathmandu valley; different from Nepali', 'middle', 'Ls')
    s += hr(264)
    s += sh(272, 'GORKHA KINGDOM & PRITHVI NARAYAN SHAH')
    s += t(240, 283, '1768: Prithvi Narayan Shah unifies Nepal; Nepali becomes national language', 'middle', 'L')
    s += t(240, 294, 'Nepali (Gorkhali): spread by Gurkha soldiers across Himalayan region', 'middle', 'Ls')
    s += t(240, 305, 'Gurkha regiments: served British Empire; took Nepali language across Asia', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'NEPALI TODAY')
    s += t(240, 332, '~17M speakers; official language of Nepal', 'middle', 'L')
    s += t(240, 343, 'Also spoken in Darjeeling, Sikkim, Bhutan, and by diaspora', 'middle', 'Ls')
    s += t(240, 354, 'Scheduled language of India (Sikkim); recognized in Bhutan', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'HIMALAYAN BOND: TIBET & NEPAL')
    s += t(240, 381, 'Mount Everest / Sagarmatha / Chomolungma: named in both languages', 'middle', 'L')
    s += t(240, 392, 'Nepal: buffer between India and Tibet; always both Buddhist and Hindu', 'middle', 'Ls')
    s += t(240, 403, 'Lhasa-Kathmandu trade route: centuries of wool, salt, grain exchange', 'middle', 'Ls')
    s += t(240, 414, 'Tibetan refugees: 20,000+ in Nepal since 1959 (Dalai Lama exile)', 'middle', 'Ls')
    s += t(240, 425, 'Two mountain peoples: shaped by altitude, Buddhism, trade', 'middle', 'L')
    s += footer('56', 'TIBETAN', 'NEPALI', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate56a_tibetan_nepali_script_alt.svg', plate56a()),
                  ('plate56b_tibetan_nepali_phonology_alt.svg', plate56b()),
                  ('plate56c_tibetan_nepali_grammar_alt.svg', plate56c()),
                  ('plate56d_tibetan_nepali_history_alt.svg', plate56d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
