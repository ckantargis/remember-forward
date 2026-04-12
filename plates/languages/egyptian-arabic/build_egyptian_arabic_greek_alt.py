"""
Batch 14 — Egyptian Arabic + Greek alt plates (Series 60, plates 60a–60d)
Secondary language: Greek (~13M speakers, Indo-European, Athens)
Geographic link: Alexandria to Crete ~300mi; Alexandria to Athens ~1300mi (via sea)
Ptolemaic Egypt: Greek was official language for 300 years; Greek-Egyptian contact 2500+ years
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

# ── PLATE 60a  SCRIPT ────────────────────────────────────────────────────────
def plate60a():
    s = open_svg()
    s += t(240, 28, 'EGYPTIAN ARABIC', 'middle', 'T')
    s += t(240, 40, 'SCRIPT — TWO ALPHABETS, ONE LAND', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'EGYPTIAN ARABIC SCRIPT')
    s += t(240, 68, 'Written in Arabic Perso-Arabic abjad; right-to-left; 28 letters', 'middle', 'L')
    s += t(240, 79, 'Same script as Modern Standard Arabic (MSA); dialect is spoken, not usually written', 'middle', 'L')
    s += t(240, 90, 'Formal writing: MSA  \u2022  Social media, texts: Egyptian Colloquial Arabic', 'middle', 'L')
    s += t(240, 101, 'When written informally: same alphabet, dialectal spellings', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'EGYPTIAN ARABIC IN LATIN SCRIPT')
    s += t(240, 128, 'Egyptian Arabic romanization: common online, no official standard', 'middle', 'L')
    s += t(240, 139, '"3" = ayin /\u02bf/  \u2022  "7" = h\u0323a /h\u0323/  \u2022  "2" = hamza /\u02be/', 'middle', 'L')
    s += t(240, 150, 'Numbers-in-text: internet convention for Semitic sounds lacking Latin letters', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'COPTIC SCRIPT: ANCESTOR IN EGYPT')
    s += t(240, 177, 'Coptic: Greek alphabet + 6-7 Demotic Egyptian letters', 'middle', 'L')
    s += t(240, 188, 'Used to write Ancient Egyptian in Christian era (2nd-17th century CE)', 'middle', 'L')
    s += t(240, 199, 'Still used in Coptic Christian liturgy: ~10% of Egypt is Coptic Christian', 'middle', 'Ls')
    s += hr(207)
    s += sh(215, 'SAMPLE EGYPTIAN ARABIC')
    s += t(240, 226, 'Izzayak? "How are you?" (masc.)  \u2022  Kwayyis, shukran "Fine, thanks"', 'middle', 'L')
    s += t(240, 237, 'Sabah el-kheir "Good morning"  \u2022  Maassalama "Goodbye"', 'middle', 'L')
    s += hr(245)
    # Divider
    s += sec_divider(252, 'GREEK  \u00b7  SECONDARY LANGUAGE')
    s += sh(277, 'GREEK ALPHABET')
    s += t(240, 288, '24 letters; left-to-right (opposite direction to Arabic)', 'middle', 'L')
    s += t(240, 299, 'Greek alphabet ~800 BCE: adapted from Phoenician, added vowel letters', 'middle', 'L')
    s += t(240, 310, 'First fully voweled alphabet in history (Phoenician was consonantal)', 'middle', 'L')
    s += t(240, 321, 'Greek letters became ancestor of Latin, Cyrillic, Coptic scripts', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'GREEK IN EGYPT: HISTORICAL ROLE')
    s += t(240, 348, 'Alexander the Great conquered Egypt 332 BCE: Greek became official language', 'middle', 'L')
    s += t(240, 359, 'Ptolemaic dynasty (~305-30 BCE): pharaohs wrote in Greek', 'middle', 'L')
    s += t(240, 370, 'Rosetta Stone (196 BCE): same decree in hieroglyphs, Demotic, and Greek', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'SCRIPT COMPARISON')
    s += t(240, 397, 'Arabic: right-to-left abjad (consonants only, vowels optional)', 'middle', 'L')
    s += t(240, 408, 'Greek: left-to-right full alphabet (all vowels written)', 'middle', 'L')
    s += t(240, 419, 'Coptic: bridge script (Greek alphabet + Egyptian sounds) used in Egypt', 'middle', 'L')
    s += t(240, 430, 'Egypt hosted all three script families: Semitic, Indo-European, hybrid Coptic', 'middle', 'Ls')
    s += footer('60', 'EGYPTIAN ARABIC', 'GREEK', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 60b  PHONOLOGY ─────────────────────────────────────────────────────
def plate60b():
    s = open_svg()
    s += t(240, 28, 'EGYPTIAN ARABIC', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY — DIALECT FEATURES', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'EGYPTIAN ARABIC DISTINCT SOUNDS')
    s += t(240, 68, '/q/ \u2192 /\u02be/ (glottal stop): qalb "heart" \u2192 alb  (Cairo Egyptian)', 'middle', 'L')
    s += t(240, 79, '/j/ \u2192 /g/: jamal "camel" \u2192 gamal (distinctive Egyptian feature)', 'middle', 'L')
    s += t(240, 90, 'Jim as /g/: marks Egyptian Arabic worldwide (not in Levantine/Gulf)', 'middle', 'L')
    s += t(240, 101, 'Preserves /\u02bf/ (ayin) as full pharyngeal; also preserves /h\u0323/ (ha)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'VOWEL SYSTEM')
    s += t(240, 128, 'Classical Arabic: 3 short + 3 long vowels  \u2022  Egyptian: 5+ distinct vowels', 'middle', 'L')
    s += t(240, 139, 'Long vowels shortened in unstressed syllables (Cairene rule)', 'middle', 'L')
    s += t(240, 150, 'Imala: Classical /a/ \u2192 /e/ before front consonants (ancient Egyptian vowel shift?)', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'WHY EGYPTIAN ARABIC IS UNDERSTOOD GLOBALLY')
    s += t(240, 177, 'Egyptian cinema from 1930s: Umm Kulthum, Abdel Halim Hafez', 'middle', 'L')
    s += t(240, 188, 'Egyptian TV: exported across Arab world for 80+ years', 'middle', 'L')
    s += t(240, 199, 'Result: most Arabic speakers understand Egyptian dialect passively', 'middle', 'L')
    s += t(240, 210, '~100M speakers; de facto prestige dialect globally', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'GREEK PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'MODERN GREEK PHONOLOGY')
    s += t(240, 261, '5 vowels: a e i o u (all short; long/short distinction lost from Ancient Greek)', 'middle', 'L')
    s += t(240, 272, 'Fricatives: th /\u03b8/ \u2022 dh /\u00f0/ \u2022 gh /\u0263/ \u2022 ch /x/  (not in Arabic)', 'middle', 'L')
    s += t(240, 283, 'No aspiration distinction  \u2022  stress is phonemic (written with accent marks)', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'ANCIENT VS MODERN GREEK PHONOLOGY')
    s += t(240, 310, 'Ancient: aspiration /p\u02b0 t\u02b0 k\u02b0/ \u2022 pitch accent \u2022 length distinctions', 'middle', 'L')
    s += t(240, 321, 'Modern: no aspiration \u2022 stress accent \u2022 all long vowels shortened', 'middle', 'L')
    s += t(240, 332, 'Eta (\u03b7) and iota (\u03b9) and upsilon (\u03c5) all = /i/ in Modern Greek', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'CONTACT PHONOLOGY')
    s += t(240, 359, 'Coptic (Egyptian in Greek alphabet) preserves sound layer between both', 'middle', 'L')
    s += t(240, 370, 'Greek loanwords in Egyptian Arabic: fanela (vest), garaaj (garage via French)', 'middle', 'Ls')
    s += t(240, 381, 'Arabic loanwords in Greek: magazines, coffee, algebra — via Ottoman period', 'middle', 'Ls')
    s += footer('60', 'EGYPTIAN ARABIC', 'GREEK', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 60c  GRAMMAR ───────────────────────────────────────────────────────
def plate60c():
    s = open_svg()
    s += t(240, 28, 'EGYPTIAN ARABIC', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — DIALECT VS STANDARD', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'EGYPTIAN ARABIC VERB SYSTEM')
    s += t(240, 68, 'Prefix conjugation: bi- marks present/habitual (dialectal innovation)', 'middle', 'L')
    s += t(240, 79, 'Biyiktib "he writes (habitually)"  \u2022  hayiktib "he will write"', 'middle', 'L')
    s += t(240, 90, 'Katab "he wrote" (past, same as MSA)  \u2022  ha- = future prefix', 'middle', 'L')
    s += t(240, 101, 'MSA has no bi- present marker; this is Egyption/Levantine innovation', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'NEGATION: MISH AND MA...SH')
    s += t(240, 128, 'Egyptian: ma + verb + sh = "not"  (circumfix negation)', 'middle', 'L')
    s += t(240, 139, 'Makatab-sh "he didn\'t write"  \u2022  mish ktib "not written"', 'middle', 'L')
    s += t(240, 150, '-sh suffix: possible Coptic origin (Coptic negation: an/en)', 'middle', 'Ls')
    s += t(240, 161, 'MSA: la/lam + verb (no circumfix)  \u2014 Egyptian negation unique', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'EGYPTIAN ARABIC WORD ORDER: SVO')
    s += t(240, 188, 'Colloquial Egyptian: SVO (subject-verb-object)', 'middle', 'L')
    s += t(240, 199, 'MSA: VSO  \u2022  Egyptian Arabic: SVO (parallel to Modern Hebrew shift)', 'middle', 'L')
    s += t(240, 210, 'Ana katab-t el-gawab "I wrote the letter" (SVO)', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'GREEK GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'MODERN GREEK CASE SYSTEM')
    s += t(240, 261, '4 cases: nominative, accusative, genitive, vocative', 'middle', 'L')
    s += t(240, 272, 'Ancient Greek had 5 cases (added dative); Modern lost dative', 'middle', 'L')
    s += t(240, 283, 'Definite article agrees with noun in case, gender, number', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'GREEK VERB SYSTEM')
    s += t(240, 310, 'Two aspects: imperfective and perfective (parallel to Semitic!)', 'middle', 'L')
    s += t(240, 321, 'Aspect rather than tense is the core distinction (like Arabic/Hebrew)', 'middle', 'L')
    s += t(240, 332, 'Three persons, two numbers; verb encodes subject (pro-drop language)', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'GRAMMAR COMPARISON')
    s += t(240, 359, 'Egyptian Arabic: SVO, aspect-based verbs, circumfix negation', 'middle', 'L')
    s += t(240, 370, 'Greek: SVO (flexible), aspect-based verbs, 4-case nouns', 'middle', 'L')
    s += t(240, 381, 'Both: pro-drop (subject pronouns optional)', 'middle', 'L')
    s += t(240, 392, 'Both: aspect at core of verbal system (shared Mediterranean typology)', 'middle', 'Ls')
    s += footer('60', 'EGYPTIAN ARABIC', 'GREEK', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 60d  HISTORY ───────────────────────────────────────────────────────
def plate60d():
    s = open_svg()
    s += t(240, 28, 'EGYPTIAN ARABIC', 'middle', 'T')
    s += t(240, 40, 'HISTORY — EGYPT AND THE MEDITERRANEAN', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ARABIC COMES TO EGYPT')
    s += t(240, 68, '639-642 CE: Arab-Muslim conquest of Egypt under Amr ibn al-As', 'middle', 'L')
    s += t(240, 79, 'Byzantine (Greek-speaking) Egypt became Arabophone over 2-3 centuries', 'middle', 'L')
    s += t(240, 90, 'Coptic spoken as vernacular until ~14th century; then Arabic replaced it', 'middle', 'L')
    s += t(240, 101, 'Coptic survived only in church liturgy (still today)', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'EGYPT AS ARAB CULTURAL CENTER')
    s += t(240, 128, 'Cairo (founded 969 CE): center of Islamic scholarship and culture', 'middle', 'L')
    s += t(240, 139, 'Al-Azhar University (970 CE): oldest university in continuous operation', 'middle', 'L')
    s += t(240, 150, 'Egypt: Arab world\'s most populous country; cultural output unmatched', 'middle', 'L')
    s += t(240, 161, 'Egyptian cinema (1930s+): Hollywood of the Arab world', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'MODERN EGYPT')
    s += t(240, 188, '~106M population; Cairo one of world\'s largest cities (~20M metro)', 'middle', 'L')
    s += t(240, 199, 'Egyptian Arabic = world\'s most widely understood Arabic dialect', 'middle', 'L')
    s += t(240, 210, 'Arab Spring (2011): Tahrir Square uprising in Egyptian Arabic', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'GREEK HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'PTOLEMAIC EGYPT: GREEK PHARAOHS')
    s += t(240, 261, '332 BCE: Alexander the Great takes Egypt; founds Alexandria', 'middle', 'L')
    s += t(240, 272, 'Ptolemy I (305 BCE): Greek general becomes pharaoh; dynasty lasts 275 years', 'middle', 'L')
    s += t(240, 283, 'Cleopatra VII: last Ptolemaic pharaoh; first of her dynasty to learn Egyptian', 'middle', 'L')
    s += t(240, 294, '30 BCE: Rome conquers Egypt; Greek remains co-official for centuries', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'ALEXANDRIA: THE WORLD CITY')
    s += t(240, 321, 'Library of Alexandria: largest knowledge repository of antiquity', 'middle', 'L')
    s += t(240, 332, 'Translation: 72 Jewish scholars translated Torah into Greek (Septuagint)', 'middle', 'L')
    s += t(240, 343, 'Philo of Alexandria: Jewish philosophy in Greek  \u2022  Euclid worked here', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'GREEK TODAY AND EGYPT')
    s += t(240, 370, '~13M Greek speakers; large Greek communities in Alexandria until 1950s', 'middle', 'L')
    s += t(240, 381, 'Greek exodus from Egypt after 1952 revolution and Nasser nationalization', 'middle', 'L')
    s += t(240, 392, 'Constantine Cavafy: Greek-Egyptian poet; voice of Alexandrian memory', 'middle', 'Ls')
    s += t(240, 403, 'Egypt and Greece: 2500 years of intertwined history on the Mediterranean', 'middle', 'L')
    s += footer('60', 'EGYPTIAN ARABIC', 'GREEK', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate60a_egyptian_arabic_greek_script_alt.svg', plate60a()),
                  ('plate60b_egyptian_arabic_greek_phonology_alt.svg', plate60b()),
                  ('plate60c_egyptian_arabic_greek_grammar_alt.svg', plate60c()),
                  ('plate60d_egyptian_arabic_greek_history_alt.svg', plate60d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
