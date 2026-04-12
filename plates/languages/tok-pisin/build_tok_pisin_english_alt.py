"""
Batch 11 — Tok Pisin + English alt plates (Series 45, plates 45a–45d)
Secondary language: English (~400M L1 speakers; official in Papua New Guinea)
Geographic expansion: ~1500mi (no other major language within standard 500mi of PNG)
Tok Pisin is an English-based creole; English is the co-official language and the lexifier
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

# ── PLATE 45a  SCRIPT ────────────────────────────────────────────────────────
def plate45a():
    s = open_svg()
    s += t(240, 28, 'TOK PISIN', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TOK PISIN LATIN ALPHABET')
    s += t(240, 68, 'Tok Pisin uses Latin alphabet; phonemic spelling system', 'middle', 'L')
    s += t(240, 79, '"Tok Pisin" = Talk Pidgin (from English "Talk Pidgin")', 'middle', 'L')
    s += t(240, 90, 'High degree of spelling-pronunciation correspondence', 'middle', 'Ls')
    s += t(240, 101, 'No silent letters; c/x/q rare; phonetic respelling of English words', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'ENGLISH WORDS IN TOK PISIN SPELLING')
    s += t(240, 128, 'English word  \u2192  Tok Pisin respelling:', 'middle', 'H')
    s += t(240, 139, 'school \u2192 skul  \u2022  hospital \u2192 hausik  \u2022  church \u2192 sios', 'middle', 'L')
    s += t(240, 150, 'nothing \u2192 nating  \u2022  garden \u2022 gaden  \u2022  shirt \u2192 s\u00e2t', 'middle', 'L')
    s += t(240, 161, 'belly \u2192 bel  \u2022  bird \u2192 pisin  \u2022  talk \u2192 tok', 'middle', 'L')
    s += hr(169)
    s += sh(177, 'UNIQUE TOK PISIN WORDS')
    s += t(240, 188, 'bilong = "of/belonging to" (from English "belong")', 'middle', 'L')
    s += t(240, 199, 'baimbai (bai) = future marker (from "by and by")', 'middle', 'L')
    s += t(240, 210, 'gras bilong fes = "grass of face" = beard', 'middle', 'L')
    s += t(240, 221, 'gras bilong lek = "grass of leg" = pubic hair', 'middle', 'Ls')
    s += t(240, 232, 'siosop = "church soap" = communion wafer', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'ENGLISH  \u00b7  LEXIFIER LANGUAGE  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'ENGLISH WRITING SYSTEM')
    s += t(240, 283, '26 letters; notoriously non-phonemic spelling', 'middle', 'L')
    s += t(240, 294, 'through / though / thought / tough — all different pronunciations', 'middle', 'L')
    s += t(240, 305, 'gh = silent (night) / /f/ (enough) / /g/ (ghost)', 'middle', 'L')
    s += t(240, 316, 'Historical layers: Old English + Norman French + Latin/Greek', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'TOK PISIN vs. ENGLISH SPELLING')
    s += t(240, 343, 'English "beautiful"  \u2192  Tok Pisin: "biutiful" (phonetic)', 'middle', 'L')
    s += t(240, 354, 'English "church"  \u2192  Tok Pisin: "sios" (from /t\u0283\u0259t\u0283/ \u2192 /sios/)', 'middle', 'L')
    s += t(240, 365, 'English "work"  \u2192  Tok Pisin: "wok" (phonetic respelling)', 'middle', 'L')
    s += t(240, 376, 'Tok Pisin: regular  \u2022  English: historical spellings preserved', 'middle', 'Ls')
    s += footer('45', 'TOK PISIN', 'ENGLISH', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 45b  PHONOLOGY ─────────────────────────────────────────────────────
def plate45b():
    s = open_svg()
    s += t(240, 28, 'TOK PISIN', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TOK PISIN CONSONANT SYSTEM')
    s += t(240, 68, 'Reduced consonant inventory compared to English:', 'middle', 'L')
    s += t(240, 79, 'p b \u2022 t d \u2022 k g \u2022 f v \u2022 s \u2022 m n \u2022 r l \u2022 w j', 'middle', 'L')
    s += t(240, 90, 'No /\u03b8/ (thin) or /\u00f0/ (this) — replaced by t/d', 'middle', 'L')
    s += t(240, 101, 'No /\u0292/ (measure) or /\u0283/ (shoe) in many dialects', 'middle', 'L')
    s += t(240, 112, 'English "three" \u2192 "tri"  \u2022  English "that" \u2192 "dat"', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'TOK PISIN VOWELS')
    s += t(240, 139, 'Five vowels: a e i o u (simpler than English!)', 'middle', 'L')
    s += t(240, 150, 'No English schwa (/\u0259/) — each vowel fully pronounced', 'middle', 'L')
    s += t(240, 161, 'English "about" /\u0259ba\u028at/ \u2192 Tok Pisin "abaut" /a.ba.ut/', 'middle', 'L')
    s += t(240, 172, 'No diphthongs in core Tok Pisin (some in loanwords)', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'STRESS & RHYTHM')
    s += t(240, 199, 'Syllable-timed rhythm (unlike English stress-timed)', 'middle', 'L')
    s += t(240, 210, 'Each syllable given roughly equal duration', 'middle', 'Ls')
    s += t(240, 221, 'Stress on penultimate syllable generally', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'ENGLISH PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'ENGLISH VOWEL CHAOS')
    s += t(240, 272, '~20 vowel phonemes in RP English: 12 monophthongs + 8 diphthongs', 'middle', 'L')
    s += t(240, 283, 'bat/bet/bit/bot/boot/but — 6 near-identical short vowels', 'middle', 'L')
    s += t(240, 294, 'Schwa /\u0259/ in unstressed syllables: "the" "a" "of" "to"', 'middle', 'L')
    s += t(240, 305, 'Great Vowel Shift (1400-1700): explains spelling-sound mismatch', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'ENGLISH CONSONANTS')
    s += t(240, 332, '24 consonant phonemes; dental fricatives rare cross-linguistically', 'middle', 'L')
    s += t(240, 343, '/\u03b8/ thin  \u2022  /\u00f0/ this: absent from most world languages', 'middle', 'L')
    s += t(240, 354, '/h/: word-initial (hat) but not word-final', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'CREOLE SIMPLIFICATION')
    s += t(240, 381, 'Tok Pisin systematically simplified English phonology:', 'middle', 'L')
    s += t(240, 392, '\u03b8/\u00f0 \u2192 t/d  \u2022  20 vowels \u2192 5 vowels  \u2022  stress-timed \u2192 syllable-timed', 'middle', 'L')
    s += t(240, 403, 'Simplified because learners lacked English native phonology', 'middle', 'Ls')
    s += t(240, 414, 'Tok Pisin phonology closer to Melanesian Austronesian substrate', 'middle', 'Ls')
    s += footer('45', 'TOK PISIN', 'ENGLISH', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 45c  GRAMMAR ───────────────────────────────────────────────────────
def plate45c():
    s = open_svg()
    s += t(240, 28, 'TOK PISIN', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — A NEW LANGUAGE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'TOK PISIN: NOT BROKEN ENGLISH')
    s += t(240, 68, 'Tok Pisin is a fully-fledged language with its own grammar', 'middle', 'L')
    s += t(240, 79, 'Native speakers: 2-4M (nativized creole, not pidgin)', 'middle', 'L')
    s += t(240, 90, 'Total speakers: ~4-8M including L2 in Papua New Guinea', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'DUAL PRONOUNS (ENGLISH LACKS THESE)')
    s += t(240, 117, 'Tok Pisin has FOUR numbers for pronouns: singular, dual, trial, plural!', 'middle', 'L')
    s += t(240, 128, 'mi = I  \u2022  mitupela = we two  \u2022  mitripela = we three  \u2022  mipela = we', 'middle', 'L')
    s += t(240, 139, 'yu = you  \u2022  yutupela = you two  \u2022  yupela = you (plural)', 'middle', 'L')
    s += t(240, 150, 'em = he/she/it  \u2022  tupela = they two  \u2022  ol = they', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'INCLUSIVE vs. EXCLUSIVE "WE"')
    s += t(240, 177, 'Tok Pisin distinguishes whether "we" includes the listener:', 'middle', 'L')
    s += t(240, 188, 'mipela = "we" (exclusive: I + others, NOT you)', 'middle', 'L')
    s += t(240, 199, 'yumi = "we" (inclusive: I + you + others)', 'middle', 'L')
    s += t(240, 210, 'English has no equivalent distinction', 'middle', 'Ls')
    s += hr(218)
    s += sh(226, 'ASPECT MARKERS (NOT TENSES)')
    s += t(240, 237, 'bai: future/irrealis  \u2022  bin: past/completive  \u2022  stap: progressive', 'middle', 'L')
    s += t(240, 248, 'Em i kaikai stap. "He is eating." (stap = continuous)', 'middle', 'L')
    s += t(240, 259, 'Em i bin kaikai. "He ate/has eaten." (bin = past)', 'middle', 'L')
    s += hr(267)
    # Divider
    s += sec_divider(274, 'ENGLISH GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(299, 'ENGLISH GRAMMAR')
    s += t(240, 310, 'SVO word order \u2022 no case inflection on nouns \u2022 articles', 'middle', 'L')
    s += t(240, 321, 'Two tenses (past/non-past): I walk / I walked', 'middle', 'L')
    s += t(240, 332, 'Rich tense-aspect system using auxiliaries:', 'middle', 'Ls')
    s += t(240, 343, 'I walk / I walked / I will walk / I am walking / I have walked', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'ENGLISH PRONOUNS (SIMPLE)')
    s += t(240, 370, 'I / you / he-she-it / we / you(pl.) / they', 'middle', 'L')
    s += t(240, 381, 'No dual or trial  \u2022  No inclusive/exclusive "we" distinction', 'middle', 'L')
    s += t(240, 392, 'Tok Pisin grammaticalizes distinctions English ignores', 'middle', 'Ls')
    s += hr(400)
    s += sh(408, 'GRAMMAR DIVERGENCE FROM ENGLISH')
    s += t(240, 419, 'i: predicate marker after subject (no English equivalent)', 'middle', 'L')
    s += t(240, 430, 'Em i go. "He goes." (i marks predicate boundary)', 'middle', 'L')
    s += t(240, 441, 'This feature from Austronesian substrate (not from English)', 'middle', 'Ls')
    s += t(240, 452, 'Tok Pisin is creole: English vocabulary + Melanesian grammar', 'middle', 'L')
    s += footer('45', 'TOK PISIN', 'ENGLISH', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 45d  HISTORY ───────────────────────────────────────────────────────
def plate45d():
    s = open_svg()
    s += t(240, 28, 'TOK PISIN', 'middle', 'T')
    s += t(240, 40, 'HISTORY & CREOLIZATION', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'PAPUA NEW GUINEA LINGUISTIC LANDSCAPE')
    s += t(240, 68, 'PNG: ~840 languages — most linguistically diverse country on Earth', 'middle', 'L')
    s += t(240, 79, '8M people \u2022 840 languages \u2022 = one language per ~9,500 people', 'middle', 'L')
    s += t(240, 90, 'Tok Pisin arose as lingua franca to bridge this diversity', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'ORIGIN OF TOK PISIN')
    s += t(240, 117, '19th c.: South Pacific Pidgin English on trade and plantation ships', 'middle', 'L')
    s += t(240, 128, 'Sandalwood trade, labor recruiting, missionary contact — English spread', 'middle', 'Ls')
    s += t(240, 139, '1880s-1920s: German colonial period in PNG; Tok Pisin stabilizes', 'middle', 'Ls')
    s += t(240, 150, '1975: PNG independence; Tok Pisin declared official language', 'middle', 'L')
    s += hr(158)
    s += sh(166, 'CREOLIZATION: PIDGIN BECOMES LANGUAGE')
    s += t(240, 177, 'Pidgin: simplified contact language with no native speakers', 'middle', 'L')
    s += t(240, 188, 'Creole: pidgin acquired as first language by children', 'middle', 'L')
    s += t(240, 199, 'Creolization adds: pronouns, grammar rules, expanded vocabulary', 'middle', 'Ls')
    s += t(240, 210, 'Tok Pisin: completed creolization in 20th century; 2-4M native speakers', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'ENGLISH HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'ENGLISH IN PAPUA NEW GUINEA')
    s += t(240, 261, '1884: British colonize SE Papua; English officially introduced', 'middle', 'L')
    s += t(240, 272, 'Australian administration (1906-1975): English language schooling', 'middle', 'Ls')
    s += t(240, 283, 'English: official language of PNG alongside Tok Pisin + Hiri Motu', 'middle', 'L')
    s += t(240, 294, 'But: only ~2% of PNG population speaks English as L1', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'WHY ENGLISH EXPANDED GLOBALLY')
    s += t(240, 321, 'British Empire: covered 25% of Earth\'s land area at peak (1920)', 'middle', 'L')
    s += t(240, 332, 'Industrial Revolution, trade, science, technology in English', 'middle', 'Ls')
    s += t(240, 343, 'USA dominance post-WWII: Hollywood, internet, academia', 'middle', 'Ls')
    s += t(240, 354, 'Today: ~1.5B English speakers worldwide (L1 + L2)', 'middle', 'L')
    s += hr(362)
    s += sh(370, 'THE CREOLE PARADOX')
    s += t(240, 381, 'Tok Pisin: child of English, but grammatically independent', 'middle', 'L')
    s += t(240, 392, 'English speakers cannot understand Tok Pisin without study', 'middle', 'L')
    s += t(240, 403, '"Gras bilong fes i no save gro long ston."', 'middle', 'L')
    s += t(240, 414, '"Grass of face does not know how to grow on stone."', 'middle', 'Ls')
    s += t(240, 425, '= "A beard cannot grow on a stone." (proverb)', 'middle', 'Ls')
    s += t(240, 436, 'New language; same root; distant enough to be a separate tongue', 'middle', 'L')
    s += footer('45', 'TOK PISIN', 'ENGLISH', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate45a_tok_pisin_english_script_alt.svg', plate45a()),
                  ('plate45b_tok_pisin_english_phonology_alt.svg', plate45b()),
                  ('plate45c_tok_pisin_english_grammar_alt.svg', plate45c()),
                  ('plate45d_tok_pisin_english_history_alt.svg', plate45d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
