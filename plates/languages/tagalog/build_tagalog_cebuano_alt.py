"""
Batch 10 — Tagalog + Cebuano alt plates (Series 42, plates 42a–42d)
Secondary language: Cebuano (~20M speakers, Austronesian, Visayas/Mindanao, Philippines)
Geographic link: Manila (Tagalog center) to Cebu City ~350mi
Both Philippine languages; Cebuano is the 2nd most spoken Philippine language
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

# ── PLATE 42a  SCRIPT ────────────────────────────────────────────────────────
def plate42a():
    s = open_svg()
    s += t(240, 28, 'TAGALOG', 'middle', 'T')
    s += t(240, 40, 'BAYBAYIN & MODERN SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'BAYBAYIN — INDIGENOUS SCRIPT')
    s += t(240, 68, 'Baybayin: pre-colonial abugida derived from Brahmi via Kawi', 'middle', 'L')
    s += t(240, 79, '~300 CE arrival in Philippines; used until ~1800s', 'middle', 'Ls')
    s += t(240, 90, '17 characters: 3 vowels + 14 consonants (each with inherent /a/)', 'middle', 'L')
    s += t(240, 101, 'Kudlit diacritic: above consonant = /e/ or /i/ \u2022 below = /o/ or /u/', 'middle', 'L')
    s += t(240, 112, 'Cruz kudlit (cross): added by Spanish missionaries to write /no vowel/', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'BAYBAYIN SAMPLE')
    s += t(240, 140, '\ua992\ua9a4\ua997 (ba-yan = nation/homeland)', 'middle', 'Fb')
    s += t(240, 151, 'Baybayin Unicode: U+A980\u2013U+A9DF', 'middle', 'Ls')
    s += hr(159)
    s += sh(167, 'MODERN FILIPINO LATIN ALPHABET (28 LETTERS)')
    s += t(240, 178, 'Spanish-derived Latin alphabet + English letters (c, f, j, q, v, x, z)', 'middle', 'Ls')
    s += t(240, 189, 'ng: single letter /\u014b/ — not n+g but its own unit', 'middle', 'L')
    s += t(240, 200, 'ng before vowels: ngayon "now" /\u014ba\u02c8jon/', 'middle', 'L')
    s += t(240, 211, 'Glottal stop /\u0294/: marked with hyphen in some styles or unmarked', 'middle', 'Ls')
    s += hr(219)
    # Divider
    s += sec_divider(226, 'CEBUANO  \u00b7  BISAYA  \u00b7  SECONDARY LANGUAGE')
    s += sh(251, 'CEBUANO BAYBAYIN HERITAGE')
    s += t(240, 262, 'Cebuano region: also used Baybayin pre-colonial', 'middle', 'L')
    s += t(240, 273, 'Visayan Baybayin: slight variant of Tagalog Baybayin', 'middle', 'Ls')
    s += t(240, 284, 'Spanish missionaries brought Latin to Cebu in 1565', 'middle', 'Ls')
    s += hr(292)
    s += sh(300, 'MODERN CEBUANO LATIN ALPHABET')
    s += t(240, 311, '20 letters in standard Cebuano; same Latin base as Tagalog', 'middle', 'L')
    s += t(240, 322, 'ng = /\u014b/ (same as Tagalog)', 'middle', 'L')
    s += t(240, 333, 'Glottal stop: often marked with dash or apostrophe', 'middle', 'L')
    s += t(240, 344, 'Cebuano also called Bisaya/Visayan (Bisaya = Visayan people)', 'middle', 'Ls')
    s += hr(352)
    s += sh(360, 'SCRIPT SAMPLE COMPARISON')
    s += t(240, 371, 'Tagalog: Magandang umaga!  "Good morning!"', 'middle', 'L')
    s += t(240, 382, 'Cebuano: Maayong buntag!  "Good morning!"', 'middle', 'L')
    s += t(240, 393, 'Tagalog: Salamat  "Thank you"', 'middle', 'L')
    s += t(240, 404, 'Cebuano: Salamat  "Thank you"  (identical!)', 'middle', 'L')
    s += t(240, 415, 'Both share Malay "salamat" via Austronesian links', 'middle', 'Ls')
    s += footer('42', 'TAGALOG', 'CEBUANO', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 42b  PHONOLOGY ─────────────────────────────────────────────────────
def plate42b():
    s = open_svg()
    s += t(240, 28, 'TAGALOG', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TAGALOG CONSONANT SYSTEM')
    s += t(240, 68, '21 phonemes; stops, fricatives, nasals, approximants', 'middle', 'L')
    s += t(240, 79, 'Stops: p b \u2022 t d \u2022 k g \u2022 /\u0294/ (glottal stop)', 'middle', 'L')
    s += t(240, 90, 'Glottal stop: phonemic, often unmarked in spelling', 'middle', 'L')
    s += t(240, 101, 'ba\u02c8ba (door) vs. b\u00e1\u0294ba (dip) — stress + glottal distinguish', 'middle', 'L')
    s += t(240, 112, 'ng /\u014b/: can occur at word start (unlike English)', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'TAGALOG VOWELS')
    s += t(240, 139, 'Five vowels: a e i o u  \u2022  /e/ and /i/ sometimes merge', 'middle', 'L')
    s += t(240, 150, 'Stress is phonemic: \u00e1raw "sun" vs. ar\u00e1w "day"', 'middle', 'L')
    s += t(240, 161, 'Final glottal stop after stressed vowel: bangk\u00f3\u0294 "chair"', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'STRESS PATTERNS')
    s += t(240, 188, 'Stress on penultimate or final syllable (plus glottal-final type)', 'middle', 'L')
    s += t(240, 199, 'Stress + glottal stop patterns mark vocabulary meaning', 'middle', 'Ls')
    s += t(240, 210, 'Spanish loanwords: keep original stress (opisina "office")', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'CEBUANO PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'CEBUANO CONSONANT SYSTEM')
    s += t(240, 261, 'Similar inventory to Tagalog; same Austronesian stock', 'middle', 'L')
    s += t(240, 272, 'Glottal stop /\u0294/ also phonemic: kamot\u0294 "hand" vs. kamot "to scratch"', 'middle', 'L')
    s += t(240, 283, 'ng /\u014b/ at word start: ngano "why" \u2022 ngil-ad "ugly"', 'middle', 'L')
    s += hr(291)
    s += sh(299, 'CEBUANO VOWELS')
    s += t(240, 310, 'Three contrastive vowels: /a/ /i/ /u/ (more archaic than Tagalog)', 'middle', 'L')
    s += t(240, 321, 'Tagalog has 5 vowels \u2022 Cebuano has 3 core vowels', 'middle', 'L')
    s += t(240, 332, '[e] and [o] are allophones of /i/ and /u/ in Cebuano', 'middle', 'Ls')
    s += t(240, 343, 'Reflects more conservative Proto-Philippine vowel system', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'PHONOLOGICAL COMPARISON')
    s += t(240, 370, 'Tagalog 5 vowels  vs.  Cebuano 3 core vowels', 'middle', 'L')
    s += t(240, 381, 'Both: phonemic glottal stop  \u2022  both: /\u014b/ at word start', 'middle', 'L')
    s += t(240, 392, 'Both: stress as phonemic  \u2022  both: CV syllable preference', 'middle', 'L')
    s += t(240, 403, 'Cebuano: more archaic vowel system  \u2022  Tagalog: more vowel distinctions', 'middle', 'Ls')
    s += t(240, 414, 'Both lack tone — unlike mainland SE Asian languages', 'middle', 'Ls')
    s += footer('42', 'TAGALOG', 'CEBUANO', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 42c  GRAMMAR ───────────────────────────────────────────────────────
def plate42c():
    s = open_svg()
    s += t(240, 28, 'TAGALOG', 'middle', 'T')
    s += t(240, 40, 'FOCUS SYSTEM & GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'THE PHILIPPINE FOCUS SYSTEM')
    s += t(240, 68, 'Tagalog verbs mark which argument is "in focus" (prominent)', 'middle', 'L')
    s += t(240, 79, 'Actor Focus (AF): -um- / mag- marks subject as actor', 'middle', 'L')
    s += t(240, 90, 'Bumili ako ng mangga sa tindahan.', 'middle', 'L')
    s += t(240, 101, '"I bought mango at the store." (actor in focus)', 'middle', 'Ls')
    s += t(240, 112, 'Object Focus (OF): -in- marks object as focus', 'middle', 'L')
    s += t(240, 123, 'Binili ko ang mangga sa tindahan.', 'middle', 'L')
    s += t(240, 134, '"The mango was bought by me at the store." (object in focus)', 'middle', 'Ls')
    s += hr(142)
    s += sh(150, 'FOCUS TYPES')
    s += t(240, 161, 'Actor (-um-/mag-) \u2022 Object (-in-) \u2022 Locative (-an)', 'middle', 'L')
    s += t(240, 172, 'Benefactive (-an/-in-an) \u2022 Instrumental (i-)', 'middle', 'L')
    s += t(240, 183, '"ang" particle marks the focused argument', 'middle', 'Ls')
    s += hr(191)
    s += sh(199, 'TAGALOG WORD ORDER')
    s += t(240, 210, 'Predicate-initial: VSO or VOS typical', 'middle', 'L')
    s += t(240, 221, 'Verb comes first; subject follows; topic marked by ang', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'CEBUANO GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'CEBUANO FOCUS SYSTEM')
    s += t(240, 272, 'Cebuano has the SAME Philippine focus system!', 'middle', 'L')
    s += t(240, 283, 'Actor Focus: mo-/mag- prefix (Cebuano uses mo- where Tagalog uses um-)', 'middle', 'L')
    s += t(240, 294, 'Moadto ko sa merkado.  "I will go to the market." (AF)', 'middle', 'L')
    s += t(240, 305, 'Object Focus: -on suffix (Tagalog uses -in)', 'middle', 'L')
    s += t(240, 316, 'Adtoon nako ang merkado.  "The market I will go to." (OF)', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'CEBUANO FOCUS MARKERS')
    s += t(240, 343, 'ang = topic marker (same as Tagalog!)', 'middle', 'L')
    s += t(240, 354, 'ni/sa = non-topic markers (similar to Tagalog ng/sa)', 'middle', 'L')
    s += t(240, 365, 'Shared particles: ang, sa, ni — core Philippine grammar', 'middle', 'L')
    s += hr(373)
    s += sh(381, 'SHARED PHILIPPINE GRAMMAR')
    s += t(240, 392, 'Both: predicate-initial VSO word order', 'middle', 'L')
    s += t(240, 403, 'Both: ang topic marker  \u2022  sa locative  \u2022  focus morphology', 'middle', 'L')
    s += t(240, 414, 'Both: no grammatical gender  \u2022  no case inflection on nouns', 'middle', 'L')
    s += t(240, 425, 'Tagalog: -um-/-in-  vs.  Cebuano: mo-/-on  (parallel system)', 'middle', 'Ls')
    s += t(240, 436, 'Mutual intelligibility: LOW for core vocabulary, HIGH for grammar', 'middle', 'Ls')
    s += footer('42', 'TAGALOG', 'CEBUANO', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 42d  HISTORY ───────────────────────────────────────────────────────
def plate42d():
    s = open_svg()
    s += t(240, 28, 'TAGALOG', 'middle', 'T')
    s += t(240, 40, 'HISTORY & THE PHILIPPINES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'AUSTRONESIAN ARRIVAL')
    s += t(240, 68, '~2200 BCE: Austronesian speakers arrive in Philippines from Taiwan', 'middle', 'L')
    s += t(240, 79, 'Proto-Philippine: ancestor of Tagalog, Cebuano, Ilocano, and 170+ others', 'middle', 'Ls')
    s += t(240, 90, 'Tagalog = "taga-ilog" (people of the river) — Luzon river peoples', 'middle', 'L')
    s += t(240, 101, 'Kawi-influenced Baybayin: shows Indian Ocean trade connections', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'SPANISH COLONIAL PERIOD (1565-1898)')
    s += t(240, 128, '1565: Miguel Lopez de Legazpi founds Spanish settlement in Cebu', 'middle', 'L')
    s += t(240, 139, 'Spanish: 4,000+ loanwords in Filipino (kumusta, mesa, pera...)', 'middle', 'L')
    s += t(240, 150, 'Latin alphabet replaces Baybayin under Spanish influence', 'middle', 'Ls')
    s += t(240, 161, '1896: Philippine Revolution — Jose Rizal writes novels in Spanish', 'middle', 'Ls')
    s += t(240, 172, '1898: Spanish-American War; Philippines becomes US territory', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'TAGALOG AS NATIONAL LANGUAGE')
    s += t(240, 199, '1937: Institute of National Language chooses Tagalog as basis', 'middle', 'L')
    s += t(240, 210, '1987: Filipino (Tagalog-based) declared official alongside English', 'middle', 'L')
    s += t(240, 221, '~80M speakers; 3rd most widely spoken Asian language', 'middle', 'L')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'CEBUANO HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'CEBU: FIRST SPANISH CONTACT')
    s += t(240, 272, '1521: Magellan lands in Cebu — first European contact in Philippines', 'middle', 'L')
    s += t(240, 283, 'Lapu-Lapu: Cebuano chieftain who killed Magellan in Battle of Mactan', 'middle', 'L')
    s += t(240, 294, 'Lapu-Lapu: Philippine national hero; face on 1-centavo coin', 'middle', 'Ls')
    s += t(240, 305, '1565: Legazpi returns; Cebu becomes first Spanish settlement', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'CEBUANO SPREAD')
    s += t(240, 332, 'Cebuano expanded across Visayas and Mindanao via migration', 'middle', 'L')
    s += t(240, 343, '~20M native speakers; actually MORE than Tagalog L1 speakers', 'middle', 'L')
    s += t(240, 354, 'Bisaya identity: strong regional pride, distinct from Manila Tagalog', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'TAGALOG vs. CEBUANO RIVALRY')
    s += t(240, 381, 'Cebuano speakers resented Tagalog being chosen as national base', 'middle', 'L')
    s += t(240, 392, 'Cebuano: more speakers L1, but geographically dispersed', 'middle', 'Ls')
    s += t(240, 403, 'Tagalog: centered in Manila (political capital)', 'middle', 'Ls')
    s += t(240, 414, 'Today: Filipino (Tagalog-based) taught in all Philippine schools', 'middle', 'Ls')
    s += t(240, 425, 'Cebuano: remains vibrant; Sto. Nino shrine keeps Cebu as spiritual center', 'middle', 'Ls')
    s += t(240, 436, 'Both peoples: Austronesian kin, 500 years of shared colonial history', 'middle', 'L')
    s += footer('42', 'TAGALOG', 'CEBUANO', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate42a_tagalog_cebuano_script_alt.svg', plate42a()),
                  ('plate42b_tagalog_cebuano_phonology_alt.svg', plate42b()),
                  ('plate42c_tagalog_cebuano_grammar_alt.svg', plate42c()),
                  ('plate42d_tagalog_cebuano_history_alt.svg', plate42d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
