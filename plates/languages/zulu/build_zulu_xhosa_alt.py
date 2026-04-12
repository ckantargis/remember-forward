"""
Batch 12 — Zulu + Xhosa alt plates (Series 37, plates 37a–37d)
Secondary language: Xhosa (~8M speakers, Nguni Bantu, Eastern Cape, South Africa)
Geographic link: Durban (Zulu center) to Mthatha/East London (Xhosa heartland) ~300mi
Both Nguni Bantu languages; both with click consonants; neighboring peoples in South Africa
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

# ── PLATE 37a  SCRIPT ────────────────────────────────────────────────────────
def plate37a():
    s = open_svg()
    s += t(240, 28, 'ZULU', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ZULU LATIN ALPHABET')
    s += t(240, 68, 'Zulu written in Latin alphabet; 26 standard letters plus digraphs', 'middle', 'L')
    s += t(240, 79, 'First written by missionaries (1840s): John William Colenso', 'middle', 'Ls')
    s += t(240, 90, 'Standardized orthography adopted mid-20th century', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'ZULU CLICK LETTERS')
    s += t(240, 117, 'c = dental click /|/  \u2022  q = palatal click /!/', 'middle', 'L')
    s += t(240, 128, 'x = lateral click /\u0258/  (three distinct clicks)', 'middle', 'L')
    s += t(240, 139, 'Clicks can be voiced, nasalized, or aspirated: gc, ngc, gq, ngq...', 'middle', 'L')
    s += t(240, 150, 'Clicks borrowed from Khoisan peoples during Nguni southward migration', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'ZULU DIGRAPHS')
    s += t(240, 177, 'dl = lateral affricate  \u2022  hl = voiceless lateral fricative', 'middle', 'L')
    s += t(240, 188, 'tsh = aspirated affricate  \u2022  mb, nd, ng = prenasalized stops', 'middle', 'L')
    s += t(240, 199, 'sh /\u0283/  \u2022  ny /\u0272/  \u2022  ng /\u014b/ (velar nasal)', 'middle', 'L')
    s += hr(207)
    s += sh(215, 'SAMPLE TEXT')
    s += t(240, 227, 'Sawubona!  "I see you!" (standard greeting)', 'middle', 'L')
    s += t(240, 238, 'Ngikhona.  "I am here." (standard response)', 'middle', 'L')
    s += hr(246)
    # Divider
    s += sec_divider(253, 'XHOSA  \u00b7  SECONDARY LANGUAGE')
    s += sh(278, 'XHOSA LATIN ALPHABET')
    s += t(240, 289, 'Xhosa also uses Latin alphabet; same base as Zulu', 'middle', 'L')
    s += t(240, 300, 'First written by Johannes van der Kemp (1799); Tiyo Soga contributions', 'middle', 'Ls')
    s += t(240, 311, 'Xhosa click letters:', 'middle', 'H')
    s += t(240, 322, 'c = dental  \u2022  q = palatal  \u2022  x = lateral (same symbols as Zulu!)', 'middle', 'L')
    s += t(240, 333, 'gc, ngc, nkc, gq, ngq, nkq, gx, ngx, nkx = 9 click series', 'middle', 'L')
    s += hr(341)
    s += sh(349, 'XHOSA ADDITIONAL LETTERS')
    s += t(240, 360, 'r /r/ (Xhosa has /r/; Zulu uses /l/ where Xhosa uses /r/ or /l/)', 'middle', 'L')
    s += t(240, 371, 'Xhosa has more click phonemes than Zulu (~15 vs ~12)', 'middle', 'L')
    s += hr(379)
    s += sh(387, 'SCRIPT COMPARISON')
    s += t(240, 398, 'Both: Latin alphabet, same click letters (c, q, x)', 'middle', 'L')
    s += t(240, 409, 'Both: same prenasalized stop spellings (mb, nd, ng)', 'middle', 'L')
    s += t(240, 420, 'Xhosa: more click combinations  \u2022  Zulu: slightly fewer clicks', 'middle', 'L')
    s += t(240, 431, 'Xhosa: has /r/  \u2022  Zulu: no /r/ phoneme (uses /l/ instead)', 'middle', 'Ls')
    s += footer('37', 'ZULU', 'XHOSA', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 37b  PHONOLOGY ─────────────────────────────────────────────────────
def plate37b():
    s = open_svg()
    s += t(240, 28, 'ZULU', 'middle', 'T')
    s += t(240, 40, 'NGUNI CLICK PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ZULU CLICK CONSONANTS')
    s += t(240, 68, 'Dental click /|/ (c): tongue tip against upper teeth, release forward', 'middle', 'L')
    s += t(240, 79, 'Palatal click /!/ (q): tongue body against palate, release upward', 'middle', 'L')
    s += t(240, 90, 'Lateral click /\u0258/ (x): tongue sides, release laterally (tsk sound)', 'middle', 'L')
    s += t(240, 101, 'Each click has voiced (g-), nasalized (ng-), and aspirated (kh-) forms', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'ZULU TONES')
    s += t(240, 128, 'Zulu is tonal: High vs Low tones (not marked in standard spelling)', 'middle', 'L')
    s += t(240, 139, 'Tone is phonemic: umlilo "fire" vs. umlilo (different tones = diff. word)', 'middle', 'L')
    s += t(240, 150, 'Tone changes with verb tense: present vs. past tones differ', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'ZULU VOWELS & CONSONANTS')
    s += t(240, 177, '5 vowels: a e i o u (short only; no long vowels)', 'middle', 'L')
    s += t(240, 188, 'No aspiration contrast in stops (unlike English)', 'middle', 'L')
    s += t(240, 199, 'Rich fricative set: f v s z sh hl dl h', 'middle', 'L')
    s += hr(207)
    # Divider
    s += sec_divider(214, 'XHOSA PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(239, 'XHOSA CLICKS')
    s += t(240, 250, 'Same three click types as Zulu (c, q, x) plus more combinations', 'middle', 'L')
    s += t(240, 261, 'Xhosa has ~15 distinct click phonemes vs Zulu ~12', 'middle', 'L')
    s += t(240, 272, 'Additional: breathy-voiced clicks (ghc, etc.) in some analyses', 'middle', 'Ls')
    s += t(240, 283, 'Click frequency higher in Xhosa than Zulu in everyday speech', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'XHOSA TONES')
    s += t(240, 310, 'Also tonal: High vs Low (same binary system as Zulu)', 'middle', 'L')
    s += t(240, 321, 'Tone marks verb tenses and noun classes in parallel to Zulu', 'middle', 'L')
    s += hr(329)
    s += sh(337, 'XHOSA UNIQUE FEATURES')
    s += t(240, 348, 'Has /r/ phoneme (Zulu does not); used in Xhosa loanwords', 'middle', 'L')
    s += t(240, 359, 'Implosive /\u0253/ (b with downward airflow) in some dialects', 'middle', 'L')
    s += t(240, 370, 'Slightly more retroflex sounds than Zulu', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'SHARED NGUNI PHONOLOGY')
    s += t(240, 397, 'Both: 3 click types (dental, palatal, lateral)', 'middle', 'L')
    s += t(240, 408, 'Both: binary H/L tone system  \u2022  both: 5 vowels', 'middle', 'L')
    s += t(240, 419, 'Both: prenasalized stops (mb, nd, ng, nj)', 'middle', 'L')
    s += t(240, 430, 'Clicks inherited from Khoisan contact during southern migration', 'middle', 'Ls')
    s += footer('37', 'ZULU', 'XHOSA', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 37c  GRAMMAR ───────────────────────────────────────────────────────
def plate37c():
    s = open_svg()
    s += t(240, 28, 'ZULU', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & NOUN CLASS SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ZULU NOUN CLASSES')
    s += t(240, 68, 'Zulu has 15 noun classes (Bantu gender system)', 'middle', 'L')
    s += t(240, 79, 'Each class has prefix: um-/aba- (people), i-/ama- (things), u-/o- (names)', 'middle', 'L')
    s += t(240, 90, 'umuntu "person"  \u2022  abantu "people"  (class 1/2)', 'middle', 'L')
    s += t(240, 101, 'Class determines verb agreement, adjective agreement, and pronouns', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'SUBJECT CONCORD SYSTEM')
    s += t(240, 128, 'Verb agrees with subject noun class: prefix changes with class', 'middle', 'L')
    s += t(240, 139, 'Umuntu u-ya-dla  "The person is eating" (um- class: u- concord)', 'middle', 'L')
    s += t(240, 150, 'Abantu ba-ya-dla  "The people are eating" (aba- class: ba- concord)', 'middle', 'L')
    s += t(240, 161, 'Every noun class has unique subject, object, and possessive concords', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'ZULU VERB STRUCTURE')
    s += t(240, 188, 'Verb = subject concord + tense marker + object concord + root + suffix', 'middle', 'L')
    s += t(240, 199, 'Ngi-ya-m-thanda  "I love him/her" (ngi=I, ya=present, m=him/her)', 'middle', 'L')
    s += t(240, 210, 'Word order: SVO  \u2022  but much encoded in verb prefixes', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'XHOSA GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'XHOSA NOUN CLASSES')
    s += t(240, 261, 'Xhosa also has 15 noun classes; same Bantu system', 'middle', 'L')
    s += t(240, 272, 'umuntu "person"  \u2022  abantu "people"  (identical to Zulu!)', 'middle', 'L')
    s += t(240, 283, 'Most noun prefixes identical or near-identical between Zulu and Xhosa', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'XHOSA VERB SYSTEM')
    s += t(240, 310, 'Identical structure to Zulu: concord + tense + object + root + suffix', 'middle', 'L')
    s += t(240, 321, 'Ndi-ya-m-thanda  "I love him/her" (ndi=I in Xhosa vs. ngi=I in Zulu)', 'middle', 'L')
    s += t(240, 332, 'Key difference: Xhosa 1st person = ndi-  \u2022  Zulu 1st person = ngi-', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'XHOSA VS ZULU: GRAMMAR DIFFERENCES')
    s += t(240, 359, 'Xhosa: -ndi- (I)  vs Zulu: -ngi- (I)  \u2014 different 1st person prefix', 'middle', 'L')
    s += t(240, 370, 'Xhosa: ya-  vs Zulu: ya-  (same present tense marker)', 'middle', 'L')
    s += t(240, 381, 'Xhosa plural 2nd person: nin-  \u2022  Zulu: ni- (near-identical)', 'middle', 'Ls')
    s += hr(389)
    s += sh(397, 'MUTUAL INTELLIGIBILITY')
    s += t(240, 408, 'Zulu and Xhosa are mutually intelligible at ~70-80% level', 'middle', 'L')
    s += t(240, 419, 'Grammar is so parallel that a Zulu speaker can learn Xhosa in weeks', 'middle', 'L')
    s += t(240, 430, 'Biggest differences: phonology (more Xhosa clicks) and vocabulary', 'middle', 'Ls')
    s += footer('37', 'ZULU', 'XHOSA', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 37d  HISTORY ───────────────────────────────────────────────────────
def plate37d():
    s = open_svg()
    s += t(240, 28, 'ZULU', 'middle', 'T')
    s += t(240, 40, 'HISTORY & NGUNI PEOPLES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'NGUNI BANTU ORIGINS')
    s += t(240, 68, 'Nguni: branch of Bantu languages spoken along southeastern coast', 'middle', 'L')
    s += t(240, 79, 'Zulu, Xhosa, Swati, Ndebele: all Nguni, all share click consonants', 'middle', 'L')
    s += t(240, 90, 'Clicks absorbed from Khoisan hunters during southward Bantu migration', 'middle', 'L')
    s += t(240, 101, 'Migration complete by ~1000 CE; settled KwaZulu-Natal coast', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'THE ZULU KINGDOM')
    s += t(240, 128, 'Shaka kaSenzangakhona (~1787-1828): founded unified Zulu Kingdom', 'middle', 'L')
    s += t(240, 139, 'Shaka reorganized military: ibutho regiment system, iklwa short spear', 'middle', 'L')
    s += t(240, 150, 'Mfecane (~1815-1840): Zulu expansion caused massive regional displacement', 'middle', 'L')
    s += t(240, 161, 'Battle of Isandlwana (1879): Zulu defeated British regiment \u2014 famous victory', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'ZULU TODAY')
    s += t(240, 188, '~13M speakers; largest ethnolinguistic group in South Africa', 'middle', 'L')
    s += t(240, 199, 'KwaZulu-Natal province; Durban largest Zulu-speaking city', 'middle', 'L')
    s += t(240, 210, 'Official language of South Africa; Nelson Mandela spoke Zulu', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'XHOSA HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'XHOSA AND THE CAPE')
    s += t(240, 261, 'Xhosa settled Eastern Cape by ~1000-1300 CE; border: Great Fish River', 'middle', 'L')
    s += t(240, 272, 'First Africans encountered by Dutch settlers (1652) in significant numbers', 'middle', 'L')
    s += t(240, 283, '9 Cape Frontier Wars (1779-1879): Xhosa vs British/Dutch colonists', 'middle', 'L')
    s += t(240, 294, 'Longest colonial resistance in African history', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'THE GREAT CATTLE KILLING (1856-1857)')
    s += t(240, 321, 'Nongqawuse: young Xhosa prophetess; saw vision from ancestors', 'middle', 'L')
    s += t(240, 332, 'Prophecy: kill all cattle and destroy crops; ancestors would rise', 'middle', 'L')
    s += t(240, 343, '~400,000 cattle killed; ~40,000 Xhosa died of famine', 'middle', 'L')
    s += t(240, 354, 'Catastrophic; weakened Xhosa resistance to colonial annexation', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'XHOSA AND SOUTH AFRICAN LIBERATION')
    s += t(240, 381, 'Nelson Mandela: Thembu/Xhosa; born Mvezo, Eastern Cape', 'middle', 'L')
    s += t(240, 392, 'Walter Sisulu, Oliver Tambo: Xhosa ANC leaders', 'middle', 'L')
    s += t(240, 403, 'Steve Biko: Xhosa; founder Black Consciousness Movement', 'middle', 'Ls')
    s += t(240, 414, '~8M speakers; Eastern Cape and Western Cape provinces', 'middle', 'L')
    s += hr(422)
    s += sh(430, 'ZULU + XHOSA: NGUNI SIBLINGS')
    s += t(240, 441, 'Neighboring peoples; mutual intelligibility; shared click heritage', 'middle', 'L')
    s += t(240, 452, 'Different colonial histories shaped distinct identities', 'middle', 'Ls')
    s += t(240, 463, 'Both: cornerstone languages of democratic South Africa (11 official)', 'middle', 'L')
    s += footer('37', 'ZULU', 'XHOSA', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate37a_zulu_xhosa_script_alt.svg', plate37a()),
                  ('plate37b_zulu_xhosa_phonology_alt.svg', plate37b()),
                  ('plate37c_zulu_xhosa_grammar_alt.svg', plate37c()),
                  ('plate37d_zulu_xhosa_history_alt.svg', plate37d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
