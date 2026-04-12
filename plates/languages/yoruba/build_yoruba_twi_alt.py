"""
Batch 12 — Yoruba + Twi/Akan alt plates (Series 30, plates 30a–30d)
Secondary language: Twi/Akan (~9M speakers, Niger-Congo, Ghana)
Geographic link: Lagos (Yoruba center) to Kumasi (Twi center) ~400mi
Both West African languages; Yoruba in Nigeria; Akan/Twi in Ghana; both with large diaspora
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

# ── PLATE 30a  SCRIPT ────────────────────────────────────────────────────────
def plate30a():
    s = open_svg()
    s += t(240, 28, 'YORUBA', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'YORUBA LATIN ALPHABET')
    s += t(240, 68, 'Yoruba uses Latin alphabet with diacritics for tone and vowels', 'middle', 'L')
    s += t(240, 79, 'Standardized 1875 by Samuel Crowther (first Nigerian bishop)', 'middle', 'Ls')
    s += t(240, 90, 'No pre-colonial writing system; oral tradition dominant', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'YORUBA SPECIAL LETTERS')
    s += t(240, 117, '\u025b = /\u025b/ (open e)  \u2022  \u0254 = /\u0254/ (open o)  \u2022  \u1e63 = /\u0283/ (sh)', 'middle', 'L')
    s += t(240, 128, 'gb = /gb/ (voiced labio-velar stop \u2014 unique phoneme)', 'middle', 'L')
    s += t(240, 139, 'kp = /kp/ (voiceless labio-velar stop \u2014 also unique)', 'middle', 'L')
    s += t(240, 150, 'These doubly-articulated stops are rare outside West Africa', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'TONE MARKING')
    s += t(240, 177, 'High tone: acute accent (\u00e0)  \u2022  Low tone: grave accent (\u00e0)', 'middle', 'L')
    s += t(240, 188, 'Mid tone: no mark (most common)  \u2022  Downstep: exclamation', 'middle', 'L')
    s += t(240, 199, 'ow\u00f3 "money" \u2022 ow\u014d "hand" \u2022 \u00f2w\u00f2 "drum" (three different words)', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'SAMPLE TEXT')
    s += t(240, 227, 'E k\u00e0\u00e0r\u1ecd!  "Good morning!"', 'middle', 'L')
    s += t(240, 238, '\u00c0l\u00e0\u00e1fi\u00e0  "Peace" (common greeting)', 'middle', 'L')
    s += hr(246)
    # Divider
    s += sec_divider(253, 'TWI / AKAN  \u00b7  SECONDARY LANGUAGE')
    s += sh(278, 'AKAN LATIN ALPHABET')
    s += t(240, 289, 'Twi is a major dialect of Akan; written in Latin alphabet', 'middle', 'L')
    s += t(240, 300, 'Standardized by Basel Mission missionaries (19th century)', 'middle', 'Ls')
    s += t(240, 311, 'Special letters in Akan orthography:', 'middle', 'H')
    s += t(240, 322, '\u025b = /\u025b/ \u2022 \u0254 = /\u0254/ (same open vowels as Yoruba!)', 'middle', 'L')
    s += t(240, 333, 'Nasalized vowels: \u025b\u0303 \u0254\u0303 (marked with tilde in some systems)', 'middle', 'L')
    s += hr(341)
    s += sh(349, 'TWI TONE MARKING')
    s += t(240, 360, 'Tone marked with acute/grave: s\u00e0 vs. s\u00e1 (different meanings)', 'middle', 'L')
    s += t(240, 371, 'Two tones: High and Low (simpler than Yoruba 3-level)', 'middle', 'L')
    s += hr(379)
    s += sh(387, 'SCRIPT COMPARISON')
    s += t(240, 398, 'Both: Latin alphabet with open vowel letters \u025b and \u0254', 'middle', 'L')
    s += t(240, 409, 'Both: tone diacritics on vowels', 'middle', 'L')
    s += t(240, 420, 'Yoruba: 3 tones + downstep  \u2022  Twi: 2 tones', 'middle', 'L')
    s += t(240, 431, 'Yoruba: labio-velars kp/gb  \u2022  Twi: also has kp! (shared feature)', 'middle', 'Ls')
    s += footer('30', 'YORUBA', 'TWI', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 30b  PHONOLOGY ─────────────────────────────────────────────────────
def plate30b():
    s = open_svg()
    s += t(240, 28, 'YORUBA', 'middle', 'T')
    s += t(240, 40, 'WEST AFRICAN PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'YORUBA THREE-TONE SYSTEM')
    s += t(240, 68, 'High (H): marked with acute \u00e0  \u2022  Mid (M): unmarked', 'middle', 'L')
    s += t(240, 79, 'Low (L): marked with grave \u00e0', 'middle', 'L')
    s += t(240, 90, 'Downstep: each H after L is slightly lower than previous H', 'middle', 'L')
    s += t(240, 101, 'Tone sandhi: tones affect neighboring syllables', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'LABIO-VELAR STOPS')
    s += t(240, 128, 'kp /kp/: bilabial + velar closure simultaneously', 'middle', 'L')
    s += t(240, 139, 'gb /gb/: voiced doubly-articulated labio-velar', 'middle', 'L')
    s += t(240, 150, 'These are single consonants, not sequences', 'middle', 'Ls')
    s += t(240, 161, 'Found across West Africa: Yoruba, Igbo, Twi, Ewe, Fon', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'YORUBA VOWELS')
    s += t(240, 188, '7 oral vowels: i e \u025b a o \u0254 u', 'middle', 'L')
    s += t(240, 199, 'Nasal vowels: \u0129 \u025b\u0303 \u00e3 \u0254\u0303 \u0169 (nasalized counterparts)', 'middle', 'L')
    s += t(240, 210, 'Vowel harmony: suffix vowels harmonize with root', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'TWI PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'TWI TONE SYSTEM')
    s += t(240, 261, 'Two tones: High and Low (simpler than Yoruba)', 'middle', 'L')
    s += t(240, 272, 'Tone patterns mark verb tenses and noun classes', 'middle', 'L')
    s += t(240, 283, 'Downstep also present in Twi (shared West African feature)', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'TWI CONSONANTS')
    s += t(240, 310, 'kp /kp/ present in Twi (same labio-velar as Yoruba!)', 'middle', 'L')
    s += t(240, 321, 'Prenasalized stops: mb nd ng  (Bantu-like feature in Akan)', 'middle', 'L')
    s += t(240, 332, '\u0263w = /\u0263w/ (labialized uvular fricative — unique to Akan area)', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'TWI VOWELS')
    s += t(240, 359, '10 vowels: i \u026a e \u025b a o \u0254 u \u028a plus nasalized', 'middle', 'L')
    s += t(240, 370, 'ATR vowel harmony: Advanced Tongue Root system', 'middle', 'L')
    s += t(240, 381, '[+ATR]: i e o u  vs.  [-ATR]: \u026a \u025b \u0254 \u028a (tongue position)', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'SHARED WEST AFRICAN FEATURES')
    s += t(240, 408, 'Both: tonal languages  \u2022  both: labio-velar stops (kp/gb)', 'middle', 'L')
    s += t(240, 419, 'Both: open vowels \u025b and \u0254  \u2022  both: vowel harmony', 'middle', 'L')
    s += t(240, 430, 'Yoruba: 3-level tone  \u2022  Twi: 2-level + ATR vowel harmony', 'middle', 'Ls')
    s += footer('30', 'YORUBA', 'TWI', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 30c  GRAMMAR ───────────────────────────────────────────────────────
def plate30c():
    s = open_svg()
    s += t(240, 28, 'YORUBA', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'YORUBA WORD ORDER: SVO')
    s += t(240, 68, 'Mo j\u1eb9 iy\u00e0n.  "I eat pounded yam." (SVO)', 'middle', 'L')
    s += t(240, 79, 'Modifiers follow nouns: \u00e0d\u00e0ba dud\u00fa "pigeon black" = "black pigeon"', 'middle', 'L')
    s += t(240, 90, 'No morphological case; word order + particles signal grammatical role', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'YORUBA VERB SERIALIZATION')
    s += t(240, 117, 'Serial verbs: multiple verbs in sequence without conjunction:', 'middle', 'L')
    s += t(240, 128, 'Mo m\u00fa ow\u00f3 ra \u00eew\u00e9.  "I take money buy book."', 'middle', 'L')
    s += t(240, 139, '"I bought a book with money." (serial: take-money-buy-book)', 'middle', 'Ls')
    s += t(240, 150, 'Common across West Africa; unusual in world languages', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'YORUBA NOUNS & TONES IN GRAMMAR')
    s += t(240, 177, 'No gender  \u2022  No case  \u2022  No number agreement', 'middle', 'L')
    s += t(240, 188, 'Plural: often indicated by context or reduplication', 'middle', 'Ls')
    s += t(240, 199, 'Tone changes meaning but also grammar: High = noun, Low = verb', 'middle', 'Ls')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'TWI GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'TWI WORD ORDER: SVO')
    s += t(240, 250, 'Twi is also SVO (same as Yoruba)', 'middle', 'L')
    s += t(240, 261, '\u0254berima no d\u025bi fufuo.  "The man eats fufu." (SVO)', 'middle', 'L')
    s += t(240, 272, 'Modifiers follow head: same pattern as Yoruba', 'middle', 'Ls')
    s += hr(280)
    s += sh(288, 'TWI VERB SERIALIZATION')
    s += t(240, 299, 'Twi ALSO uses serial verbs (West African areal feature!)', 'middle', 'L')
    s += t(240, 310, '\u0254 fa sika no k\u0254.  "Take money go."  = "He went with money."', 'middle', 'L')
    s += t(240, 321, 'Parallel structure to Yoruba serial verb construction', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'TWI NOUN CLASSES (AKAN)')
    s += t(240, 348, 'Akan has noun classes (unlike Yoruba which has none):', 'middle', 'L')
    s += t(240, 359, 'Singular: \u0254-baa "woman"  \u2022  Plural: a-baa "women" (prefix changes)', 'middle', 'L')
    s += t(240, 370, 'About 9 noun classes with different plural prefixes', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'SHARED WEST AFRICAN GRAMMAR')
    s += t(240, 397, 'Both: SVO  \u2022  both: serial verbs  \u2022  both: tone-based grammar', 'middle', 'L')
    s += t(240, 408, 'Both: no case  \u2022  both: modifiers after noun', 'middle', 'L')
    s += t(240, 419, 'Yoruba: no noun classes  \u2022  Twi: noun class system', 'middle', 'Ls')
    s += t(240, 430, 'Serial verbs: same construction in both languages', 'middle', 'Ls')
    s += footer('30', 'YORUBA', 'TWI', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 30d  HISTORY ───────────────────────────────────────────────────────
def plate30d():
    s = open_svg()
    s += t(240, 28, 'YORUBA', 'middle', 'T')
    s += t(240, 40, 'HISTORY & WEST AFRICA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'IFE AND THE YORUBA KINGDOMS')
    s += t(240, 68, 'Ile-Ife: spiritual capital; Yoruba trace civilization here', 'middle', 'L')
    s += t(240, 79, '~500-1000 CE: Ife terracotta sculptures — masterworks of African art', 'middle', 'L')
    s += t(240, 90, 'Oyo Empire (~1300-1836): major West African political power', 'middle', 'L')
    s += t(240, 101, 'Oyo cavalry: dominated trade routes from forest to savanna', 'middle', 'Ls')
    s += t(240, 112, 'Benin Kingdom (adj.): Yoruba-influenced brass casting tradition', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'SLAVE TRADE & DIASPORA')
    s += t(240, 139, 'Yoruba: one of most heavily enslaved African groups', 'middle', 'L')
    s += t(240, 150, 'Yoruba religion: Candomble (Brazil) \u2022 Santeria (Cuba) \u2022 Vodou (Haiti)', 'middle', 'L')
    s += t(240, 161, 'Orishas (Yoruba deities) still worshipped across Americas', 'middle', 'Ls')
    s += t(240, 172, '~50M speakers; Nigeria\u2019s largest ethnic group', 'middle', 'L')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'TWI / AKAN HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'ASHANTI EMPIRE')
    s += t(240, 223, 'Akan people: forest region of modern Ghana; gold-rich territory', 'middle', 'L')
    s += t(240, 234, '~1701: Osei Tutu founds Ashanti Confederacy (Asante Empire)', 'middle', 'L')
    s += t(240, 245, 'Golden Stool (Sika Dwa): sacred symbol of Ashanti unity and soul', 'middle', 'L')
    s += t(240, 256, 'Ashanti resisted British annexation 4 times (1823-1900)', 'middle', 'Ls')
    s += hr(264)
    s += sh(272, 'AKAN GOLD AND SLAVE TRADE')
    s += t(240, 283, 'Gold Coast (Ghana): named for Akan gold wealth (British colony)', 'middle', 'L')
    s += t(240, 294, 'Akan also participated in Atlantic slave trade (as captors + captives)', 'middle', 'Ls')
    s += t(240, 305, 'Akan cultural influence in Caribbean: Anansi spider stories', 'middle', 'Ls')
    s += t(240, 316, 'Kwame Nkrumah: Akan; first president of Ghana (1957 independence)', 'middle', 'L')
    s += hr(324)
    s += sh(332, 'TWI TODAY')
    s += t(240, 343, '~9M speakers; Twi (Asante dialect) most widely spoken Akan form', 'middle', 'L')
    s += t(240, 354, 'Ghana: Akan group ~47% of population; Twi = informal lingua franca', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'YORUBA-AKAN: WEST AFRICAN SIBLINGS')
    s += t(240, 381, 'Both: ancient kingdoms with sophisticated political systems', 'middle', 'Ls')
    s += t(240, 392, 'Both: deeply impacted by Atlantic slave trade', 'middle', 'Ls')
    s += t(240, 403, 'Both: living religious traditions in the Americas', 'middle', 'Ls')
    s += t(240, 414, 'Anansi (Akan trickster) and Eshu/Exu (Yoruba trickster): parallel gods', 'middle', 'Ls')
    s += t(240, 425, 'Two great West African civilizations: gold, iron, art, diaspora', 'middle', 'L')
    s += footer('30', 'YORUBA', 'TWI', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate30a_yoruba_twi_script_alt.svg', plate30a()),
                  ('plate30b_yoruba_twi_phonology_alt.svg', plate30b()),
                  ('plate30c_yoruba_twi_grammar_alt.svg', plate30c()),
                  ('plate30d_yoruba_twi_history_alt.svg', plate30d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
