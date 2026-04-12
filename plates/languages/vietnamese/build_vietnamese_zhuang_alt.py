"""
Batch 12 — Vietnamese + Zhuang alt plates (Series 38, plates 38a–38d)
Secondary language: Zhuang (~17M speakers, Tai-Kadai, Guangxi/China)
Geographic link: Hanoi (Vietnamese center) to Nanning (Zhuang center) ~200mi
Both mainland SE Asian tonal languages; Vietnam-Guangxi border shared; ancient trade connections
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

# ── PLATE 38a  SCRIPT ────────────────────────────────────────────────────────
def plate38a():
    s = open_svg()
    s += t(240, 28, 'VIETNAMESE', 'middle', 'T')
    s += t(240, 40, 'QUOC NGU SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'QUOC NGU — "NATIONAL LANGUAGE" SCRIPT')
    s += t(240, 68, 'Vietnamese uses Latin alphabet; developed by Alexandre de Rhodes (~1651)', 'middle', 'L')
    s += t(240, 79, 'Catholic missionary designed system to represent Vietnamese sounds', 'middle', 'Ls')
    s += t(240, 90, '29 letters; 5 diacritics for modified vowels; 6 tone marks', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'MODIFIED VOWEL LETTERS')
    s += t(240, 117, '\u0103 /\u0250/ (short a) \u2022 \u00e2 /\u0250:/ (long back a) \u2022 \u0111 /d/ (implosive d)', 'middle', 'L')
    s += t(240, 128, '\u00ea /e/ (closed e) \u2022 \u00f4 /o/ (closed o) \u2022 \u01a1 /\u0254:/ (open o)', 'middle', 'L')
    s += t(240, 139, '\u01b0 /\u026f/ (unrounded u)', 'middle', 'L')
    s += hr(147)
    s += sh(155, 'SIX TONE DIACRITICS')
    s += t(240, 166, 'Level a (no mark) \u2022 Falling \u00e0 \u2022 Rising \u00e1', 'middle', 'L')
    s += t(240, 177, 'Broken-falling \u1ea3 \u2022 Rising-stopped \u00e3 \u2022 Short-stopped \u1ea1', 'middle', 'L')
    s += t(240, 188, 'Diacritics stack: ch\u1ea9ng = tone mark on modified vowel', 'middle', 'L')
    s += hr(196)
    s += sh(204, 'SAMPLE TEXT')
    s += t(240, 216, 'Xin ch\u00e0o!  "Hello!"  (lit. "please greet")', 'middle', 'L')
    s += t(240, 227, 'C\u1ea3m \u01a1n.  "Thank you."', 'middle', 'L')
    s += hr(235)
    # Divider
    s += sec_divider(242, 'ZHUANG  \u00b7  SAWCUENGH  \u00b7  SECONDARY LANGUAGE')
    s += sh(267, 'ZHUANG WRITING HISTORY')
    s += t(240, 278, 'Sawndip: classical script using Chinese characters for Zhuang', 'middle', 'L')
    s += t(240, 289, '~1000+ years of Sawndip use; each character = Zhuang word/syllable', 'middle', 'Ls')
    s += t(240, 300, '1955: Latin Sawcuengh alphabet created for Zhuang (PRC policy)', 'middle', 'L')
    s += t(240, 311, 'Sawcuengh: tone suffixes instead of diacritics (q x j b h z)', 'middle', 'L')
    s += hr(319)
    s += sh(327, 'SAWCUENGH TONE ENCODING')
    s += t(240, 338, 'Tone 1 (level): no suffix  \u2022  Tone 2: z  \u2022  Tone 3: j', 'middle', 'L')
    s += t(240, 349, 'Tone 4: x  \u2022  Tone 5: q  \u2022  Tone 6: h  \u2022  Tone 8: (final p/t/k)', 'middle', 'L')
    s += t(240, 360, 'Tone suffix at END of syllable (not above vowel like Vietnamese)', 'middle', 'Ls')
    s += hr(368)
    s += sh(376, 'SCRIPT COMPARISON')
    s += t(240, 387, 'Both: Latin-based scripts for tonal languages', 'middle', 'L')
    s += t(240, 398, 'Vietnamese: diacritics ABOVE vowels  \u2022  Zhuang: tone letters AT END', 'middle', 'L')
    s += t(240, 409, 'Vietnamese: more letters per syllable  \u2022  Zhuang: cleaner syllables', 'middle', 'Ls')
    s += t(240, 420, 'Both had Chinese-character scripts before Latin: chu Nom / Sawndip', 'middle', 'Ls')
    s += footer('38', 'VIETNAMESE', 'ZHUANG', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 38b  PHONOLOGY ─────────────────────────────────────────────────────
def plate38b():
    s = open_svg()
    s += t(240, 28, 'VIETNAMESE', 'middle', 'T')
    s += t(240, 40, 'TONAL PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SIX TONES OF VIETNAMESE')
    s += t(240, 68, 'ngang: level mid tone  (a)  \u2014 flat and sustained', 'middle', 'L')
    s += t(240, 79, 'huy\u1ec1n: falling tone  (\u00e0)  \u2014 low falling', 'middle', 'L')
    s += t(240, 90, 's\u1eafc: rising tone  (\u00e1)  \u2014 high rising', 'middle', 'L')
    s += t(240, 101, 'h\u1ecfi: dipping tone  (\u1ea3)  \u2014 mid-low dip then rise', 'middle', 'L')
    s += t(240, 112, 'ng\u00e3: creaky-rising  (\u00e3)  \u2014 rising with glottalization', 'middle', 'L')
    s += t(240, 123, 'n\u1eb7ng: stopped  (\u1ea1)  \u2014 low, short, glottal stop final', 'middle', 'L')
    s += t(240, 134, 'ma m\u00e0 m\u00e1 m\u1ea3 m\u00e3 m\u1ea1 = 6 different words!', 'middle', 'Ls')
    s += hr(142)
    s += sh(150, 'CONSONANT SYSTEM')
    s += t(240, 161, 'Initial: b d \u0111 g gi kh l m n nh ng ngh ph qu r s t th tr v x', 'middle', 'L')
    s += t(240, 172, '\u0111 /\u0257/ = implosive (pulled-in d)  \u2022  gi /z/ = palatal fricative', 'middle', 'L')
    s += t(240, 183, 'Final: -c -ch -ng -nh -p -t -m -n only (no voiced finals)', 'middle', 'L')
    s += hr(191)
    s += sh(199, 'VOWEL SYSTEM')
    s += t(240, 210, '14 vowel nuclei; 3 diphthongs; relatively complex for SE Asia', 'middle', 'L')
    s += t(240, 221, '/\u026f/ (unrounded u) unique to Vietnamese in SE Asian context', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'ZHUANG PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'ZHUANG TONES (6-8)')
    s += t(240, 272, 'Standard Zhuang: 6 tones (some dialects 8)', 'middle', 'L')
    s += t(240, 283, 'Tone 1 (high level)  \u2022  Tone 2 (mid rising)  \u2022  Tone 3 (mid falling)', 'middle', 'L')
    s += t(240, 294, 'Tone 4 (low falling)  \u2022  Tone 5 (low rising)  \u2022  Tone 6 (mid level)', 'middle', 'L')
    s += t(240, 305, 'Tone 7 + 8: checked tones (syllable-final stop closure)', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'ZHUANG CONSONANTS')
    s += t(240, 332, 'Initial consonants: p b m f v d t n l g k ng h r s z', 'middle', 'L')
    s += t(240, 343, 'Prenasalized stops: mb nd mg (like Bantu!  different origin)', 'middle', 'Ls')
    s += t(240, 354, 'No complex consonant clusters at syllable onset', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'SHARED SE ASIAN TONAL FEATURES')
    s += t(240, 381, 'Both: monosyllabic roots  \u2022  both: tonal systems (6+ tones)', 'middle', 'L')
    s += t(240, 392, 'Both: simple syllable structure CV(C)  \u2022  no consonant clusters', 'middle', 'L')
    s += t(240, 403, 'Vietnamese: Austroasiatic family  \u2022  Zhuang: Tai-Kadai family', 'middle', 'Ls')
    s += t(240, 414, 'Converged phonologically through Southeast Asian Mainland sprachbund', 'middle', 'Ls')
    s += footer('38', 'VIETNAMESE', 'ZHUANG', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 38c  GRAMMAR ───────────────────────────────────────────────────────
def plate38c():
    s = open_svg()
    s += t(240, 28, 'VIETNAMESE', 'middle', 'T')
    s += t(240, 40, 'ISOLATING GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'VIETNAMESE WORD ORDER: SVO')
    s += t(240, 68, 'T\u00f4i \u0103n c\u01a1m.  "I eat rice." (SVO like English)', 'middle', 'L')
    s += t(240, 79, 'Modifiers FOLLOW head: c\u01a1m tr\u1eafng "rice white" = "white rice"', 'middle', 'L')
    s += t(240, 90, 'No inflection: no case, gender, number, tense on nouns/verbs', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'CLASSIFIERS')
    s += t(240, 117, 'Nouns need classifiers when counted or with modifiers:', 'middle', 'L')
    s += t(240, 128, 'con = classifier for animals: con ch\u00f3 "CL dog" = "the dog"', 'middle', 'L')
    s += t(240, 139, 'c\u00e1i = general classifier for things: c\u00e1i b\u00e0n "CL table"', 'middle', 'L')
    s += t(240, 150, 'qu\u1ea3 = classifier for round things: qu\u1ea3 t\u00e1o "CL apple"', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'TENSE THROUGH PARTICLES')
    s += t(240, 177, 'No verb conjugation; particles mark time:', 'middle', 'L')
    s += t(240, 188, '\u0111\u00e3 (past) \u2022 \u0111ang (progressive) \u2022 s\u1ebd (future)', 'middle', 'L')
    s += t(240, 199, 'T\u00f4i \u0111\u00e3 \u0103n c\u01a1m.  "I already-ate rice." = "I ate rice."', 'middle', 'L')
    s += hr(207)
    s += sh(215, 'PRONOUNS BASED ON KINSHIP')
    s += t(240, 226, 'Vietnamese uses kin terms as pronouns:', 'middle', 'L')
    s += t(240, 237, 't\u00f4i "I" (formal neutral) \u2022 anh "I/you" (older male) \u2022 ch\u1ecb "I/you" (older female)', 'middle', 'Ls')
    s += t(240, 248, 'em "I/you" (younger person) \u2022 b\u00e0 "grandmother/ma\'am"', 'middle', 'Ls')
    s += hr(256)
    # Divider
    s += sec_divider(263, 'ZHUANG GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(288, 'ZHUANG WORD ORDER: SVO')
    s += t(240, 299, 'Zhuang is also SVO (same as Vietnamese!)', 'middle', 'L')
    s += t(240, 310, 'Gou gwn haeux.  "I eat rice." (identical SVO structure)', 'middle', 'L')
    s += t(240, 321, 'Modifiers follow head: same pattern as Vietnamese', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'ZHUANG CLASSIFIERS')
    s += t(240, 348, 'Zhuang also uses classifiers! (Mainland SE Asia areal feature)', 'middle', 'L')
    s += t(240, 359, 'duz = classifier for animals  \u2022  giz = classifier for people', 'middle', 'L')
    s += t(240, 370, 'Parallel classifier system to Vietnamese', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'SHARED MAINLAND SE ASIAN GRAMMAR')
    s += t(240, 397, 'Both: SVO word order  \u2022  both: isolating morphology', 'middle', 'L')
    s += t(240, 408, 'Both: classifiers  \u2022  both: particles for tense/aspect', 'middle', 'L')
    s += t(240, 419, 'Both: modifiers AFTER noun head (not before as in English)', 'middle', 'L')
    s += t(240, 430, 'Both: no gender  \u2022  both: no case inflection', 'middle', 'L')
    s += t(240, 441, 'These features: Mainland SE Asia Sprachbund convergence', 'middle', 'Ls')
    s += footer('38', 'VIETNAMESE', 'ZHUANG', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 38d  HISTORY ───────────────────────────────────────────────────────
def plate38d():
    s = open_svg()
    s += t(240, 28, 'VIETNAMESE', 'middle', 'T')
    s += t(240, 40, 'HISTORY & INDOCHINA', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'VIETNAMESE ORIGINS')
    s += t(240, 68, 'Austroasiatic family: related to Khmer, Mon, Muong', 'middle', 'L')
    s += t(240, 79, '~111 BCE-939 CE: Chinese rule; massive Chinese loanword layer', 'middle', 'L')
    s += t(240, 90, 'Sino-Vietnamese vocabulary: ~60% of formal words from Chinese', 'middle', 'L')
    s += t(240, 101, '939 CE: Independence after Battle of Bach Dang River', 'middle', 'L')
    s += t(240, 112, 'Chu nom: Vietnamese characters adapted from Chinese (~10th c.)', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'COLONIAL PERIOD')
    s += t(240, 139, '1651: Alexandre de Rhodes publishes Vietnamese-Latin dictionary', 'middle', 'L')
    s += t(240, 150, '1885-1954: French Indochina; Quoc Ngu promoted by French', 'middle', 'L')
    s += t(240, 161, 'Ho Chi Minh: used Quoc Ngu to spread revolutionary literacy', 'middle', 'Ls')
    s += t(240, 172, '~90M speakers; 13th most spoken language in world', 'middle', 'L')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'ZHUANG HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'ZHUANG IN GUANGXI')
    s += t(240, 223, 'Guangxi Zhuang Autonomous Region: created 1958 for Zhuang people', 'middle', 'L')
    s += t(240, 234, 'Zhuang: indigenous Tai-Kadai people of Southern China', 'middle', 'L')
    s += t(240, 245, 'Proto-Tai: ancestors of Thai, Lao, and Zhuang split ~2000 years ago', 'middle', 'Ls')
    s += t(240, 256, 'Nong Zhigao: Zhuang leader who resisted Song dynasty (1052 CE)', 'middle', 'Ls')
    s += hr(264)
    s += sh(272, 'VIETNAMESE-ZHUANG ANCIENT CONNECTIONS')
    s += t(240, 283, 'Nanyue Kingdom (204-111 BCE): encompassed both Guangxi and Vietnam', 'middle', 'L')
    s += t(240, 294, 'Zhao Tuo (Trieu Da): ruled unified Vietnam + Guangxi region', 'middle', 'Ls')
    s += t(240, 305, 'Shared archaeological culture: Dong Son bronze drums found in both', 'middle', 'Ls')
    s += t(240, 316, 'Guangxi-Vietnam border: ~1000km; long shared history', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'ZHUANG TODAY')
    s += t(240, 343, '~17M speakers; China\'s largest ethnic minority', 'middle', 'L')
    s += t(240, 354, 'Most Zhuang are bilingual in Mandarin; Sawcuengh Latin rarely used', 'middle', 'Ls')
    s += t(240, 365, 'Zhuang language: taught in some schools; regional TV broadcasting', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'MAINLAND SE ASIA LANGUAGE FAMILY')
    s += t(240, 392, 'Vietnamese (Austroasiatic) and Zhuang (Tai-Kadai): different families', 'middle', 'Ls')
    s += t(240, 403, 'But: same region, same ecology, same cultural complex', 'middle', 'Ls')
    s += t(240, 414, 'Both languages shaped by: Chinese culture, rice agriculture, river systems', 'middle', 'Ls')
    s += t(240, 425, 'Dong Son drums: shared Bronze Age heritage across both territories', 'middle', 'L')
    s += footer('38', 'VIETNAMESE', 'ZHUANG', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate38a_vietnamese_zhuang_script_alt.svg', plate38a()),
                  ('plate38b_vietnamese_zhuang_phonology_alt.svg', plate38b()),
                  ('plate38c_vietnamese_zhuang_grammar_alt.svg', plate38c()),
                  ('plate38d_vietnamese_zhuang_history_alt.svg', plate38d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
