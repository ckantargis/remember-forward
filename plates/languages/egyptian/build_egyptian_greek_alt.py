"""
Batch 14 — Ancient Egyptian + Greek alt plates (Series 61, plates 61a–61d)
Secondary language: Greek (~13M speakers, Indo-European)
Geographic link: Alexandria to Athens ~1300mi; BUT Egypt and Greek in same land 332-30 BCE
Rosetta Stone (196 BCE): hieroglyphs + Demotic + Greek — perfect pairing
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

# ── PLATE 61a  SCRIPT ────────────────────────────────────────────────────────
def plate61a():
    s = open_svg()
    s += t(240, 28, 'ANCIENT EGYPTIAN', 'middle', 'T')
    s += t(240, 40, 'SCRIPT — HIEROGLYPHS AND THE ROSETTA STONE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'HIEROGLYPHIC WRITING SYSTEM')
    s += t(240, 68, '~700 standard hieroglyphs; logograms + phonograms combined', 'middle', 'L')
    s += t(240, 79, 'Three types: logogram (word) / phonogram (sound) / determinative (category)', 'middle', 'L')
    s += t(240, 90, 'Uniliteral signs (alphabet-like): 24 consonant signs exist', 'middle', 'L')
    s += t(240, 101, 'Hieratic (cursive) and Demotic (even more cursive): later developments', 'middle', 'Ls')
    s += hr(109)
    s += sh(117, 'DIRECTION AND ORIENTATION')
    s += t(240, 128, 'Can be read right-to-left, left-to-right, or top-to-bottom', 'middle', 'L')
    s += t(240, 139, 'Direction: follow the gaze of animal/human signs (they face the start)', 'middle', 'L')
    s += t(240, 150, 'Columns: typically read right-to-left (in most monumental texts)', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'THE THREE SCRIPTS OF THE ROSETTA STONE')
    s += t(240, 177, 'Rosetta Stone (196 BCE): decree of Ptolemy V in three scripts', 'middle', 'L')
    s += t(240, 188, 'Top: hieroglyphic (sacred script for monuments)', 'middle', 'L')
    s += t(240, 199, 'Middle: Demotic (everyday Egyptian script of the era)', 'middle', 'L')
    s += t(240, 210, 'Bottom: Greek (language of the Ptolemaic government)', 'middle', 'Ls')
    s += hr(218)
    s += sh(226, 'CHAMPOLLION\'S DECIPHERMENT (1822)')
    s += t(240, 237, 'Champollion: used Greek text to decode royal cartouches in hieroglyphs', 'middle', 'L')
    s += t(240, 248, 'Ptolemy and Cleopatra names in Greek matched cartouche letters', 'middle', 'Ls')
    s += hr(256)
    # Divider
    s += sec_divider(263, 'GREEK  \u00b7  SECONDARY LANGUAGE')
    s += sh(288, 'GREEK ALPHABET: ROSETTA KEY')
    s += t(240, 299, 'Greek text on Rosetta Stone: the only fully readable section in 1799', 'middle', 'L')
    s += t(240, 310, 'Greek alphabet: 24 letters, fully voweled, left-to-right', 'middle', 'L')
    s += t(240, 321, 'Classical Greek: upper/lowercase developed later; all caps in ancient texts', 'middle', 'Ls')
    s += hr(329)
    s += sh(337, 'COPTIC: THE BRIDGE BETWEEN THEM')
    s += t(240, 348, 'Coptic = Ancient Egyptian written in Greek alphabet + 6 Egyptian letters', 'middle', 'L')
    s += t(240, 359, 'Champollion used Coptic to understand Egyptian vowels (hieroglyphs: no vowels)', 'middle', 'L')
    s += t(240, 370, 'Coptic = critical missing link; Greek letters unlocked Egyptian sounds', 'middle', 'Ls')
    s += hr(378)
    s += sh(386, 'SCRIPT COMPARISON')
    s += t(240, 397, 'Egyptian: logographic + phonographic; complex; no vowels written', 'middle', 'L')
    s += t(240, 408, 'Greek: pure alphabet; simple; all vowels written', 'middle', 'L')
    s += t(240, 419, 'The Rosetta Stone: these two scripts on one stone unlocked history', 'middle', 'L')
    s += t(240, 430, 'Without Greek, hieroglyphs would remain unreadable for far longer', 'middle', 'Ls')
    s += footer('61', 'ANCIENT EGYPTIAN', 'GREEK', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 61b  PHONOLOGY ─────────────────────────────────────────────────────
def plate61b():
    s = open_svg()
    s += t(240, 28, 'ANCIENT EGYPTIAN', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY — RECONSTRUCTING A DEAD LANGUAGE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'EGYPTIAN PHONOLOGICAL RECONSTRUCTION')
    s += t(240, 68, 'Hieroglyphs record only consonants; vowels unknown from writing alone', 'middle', 'L')
    s += t(240, 79, 'Reconstruction uses: Coptic vowels + Semitic cognates + Greek transcriptions', 'middle', 'L')
    s += t(240, 90, 'Result: approximate; Egyptologists use "school pronunciations" (Egyptological)', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'EGYPTIAN CONSONANT SYSTEM')
    s += t(240, 117, '~24 distinct consonants reconstructed from hieroglyphic evidence', 'middle', 'L')
    s += t(240, 128, 'Pharyngeals: aleph /\u02be/ and ayin /\u02bf/ (like Semitic!)', 'middle', 'L')
    s += t(240, 139, 'Emphatics: /q/ and laterals  \u2022  No Semitic shin; had /s/ and /\u0161/', 'middle', 'L')
    s += t(240, 150, 'Unique: lateral /\u026b/  \u2022  alveolar /r/  \u2022  voiced fricatives /\u0263/', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'STAGES OF EGYPTIAN')
    s += t(240, 177, 'Old Egyptian (~2600-2000 BCE): Pyramid Texts', 'middle', 'L')
    s += t(240, 188, 'Middle Egyptian (~2000-1300 BCE): classical form, hieroglyphic standard', 'middle', 'L')
    s += t(240, 199, 'Late Egyptian (~1300-700 BCE): colloquial forms emerge in writing', 'middle', 'L')
    s += t(240, 210, 'Demotic (~700 BCE-400 CE) \u2022 Coptic (~200-1300 CE): final stages', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'GREEK PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'ANCIENT GREEK PHONOLOGICAL RICHNESS')
    s += t(240, 261, 'Aspirated stops: ph /p\u02b0/ th /t\u02b0/ kh /k\u02b0/ (later became fricatives)', 'middle', 'L')
    s += t(240, 272, 'Pitch accent: each syllable had high, low, or circumflex pitch', 'middle', 'L')
    s += t(240, 283, 'Long vs short vowels: alpha, eta, iota each had long/short pair', 'middle', 'L')
    s += t(240, 294, 'Modern Greek: lost aspiration, pitch accent, and vowel length', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'GREEK-COPTIC PHONOLOGICAL INTERACTION')
    s += t(240, 321, 'Coptic vowel system: directly from Greek vowels + Egyptian sounds', 'middle', 'L')
    s += t(240, 332, 'Coptic: 7 vowels (from Greek) representing Egyptian pronunciation', 'middle', 'L')
    s += t(240, 343, 'Coptic preserves Egyptian vowel sounds Greek alphabet could encode', 'middle', 'Ls')
    s += hr(351)
    s += sh(359, 'RECONSTRUCTING THROUGH CONTACT')
    s += t(240, 370, 'Greek transcriptions of Egyptian names: Amenhotep, Ramesses, Thutmose', 'middle', 'L')
    s += t(240, 381, 'Greek versions preserve vowels: e.g., Amenophis \u2192 Amun-hotep', 'middle', 'L')
    s += t(240, 392, 'Without Greek: Egyptian vowels would be entirely lost', 'middle', 'L')
    s += t(240, 403, 'Greek served as phonological key to unlock Egyptian voice across 4000 years', 'middle', 'Ls')
    s += footer('61', 'ANCIENT EGYPTIAN', 'GREEK', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 61c  GRAMMAR ───────────────────────────────────────────────────────
def plate61c():
    s = open_svg()
    s += t(240, 28, 'ANCIENT EGYPTIAN', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR — AFROASIATIC STRUCTURE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'EGYPTIAN LANGUAGE FAMILY')
    s += t(240, 68, 'Egyptian: member of Afroasiatic family (same as Semitic, Berber, Cushitic)', 'middle', 'L')
    s += t(240, 79, 'Closest Afroasiatic relatives: Berber languages, then Semitic', 'middle', 'L')
    s += t(240, 90, 'Egyptian is NOT Semitic, but shares Afroasiatic features with Arabic/Hebrew', 'middle', 'Ls')
    s += hr(98)
    s += sh(106, 'EGYPTIAN VERB SYSTEM')
    s += t(240, 117, 'VSO word order (same as Classical Arabic and Biblical Hebrew)', 'middle', 'L')
    s += t(240, 128, 'Verbal sentence: sdm.f "he hears" = root S-D-M + subject suffix .f', 'middle', 'L')
    s += t(240, 139, 'Two genders: masculine and feminine (feminine = -t suffix)', 'middle', 'L')
    s += t(240, 150, 'Dual number: specific suffix for pairs (like Arabic/Hebrew)', 'middle', 'Ls')
    s += hr(158)
    s += sh(166, 'EGYPTIAN NOUN SYSTEM')
    s += t(240, 177, 'No case system (unlike Greek)  \u2022  gender and number in nouns', 'middle', 'L')
    s += t(240, 188, 'Definite article: pa/ta/na (developed in Later Egyptian)', 'middle', 'L')
    s += t(240, 199, 'Coptic: pa/psi/pi = the (direct descendant)', 'middle', 'Ls')
    s += t(240, 210, 'Pronoun: subject encoded in verb suffix (like Semitic: sdm.f)', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'GREEK GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'CLASSICAL GREEK CASE SYSTEM')
    s += t(240, 261, '5 cases (Ancient): nominative, accusative, genitive, dative, vocative', 'middle', 'L')
    s += t(240, 272, 'Case endings fully encode noun grammatical role (word order flexible)', 'middle', 'L')
    s += t(240, 283, 'Greek is highly inflected: noun, verb, adjective all inflect', 'middle', 'Ls')
    s += hr(291)
    s += sh(299, 'GREEK ASPECT AND TENSE')
    s += t(240, 310, 'Aspect-based: present (ongoing) / aorist (punctual) / perfect (state)', 'middle', 'L')
    s += t(240, 321, 'Plus tense (past vs non-past) on top of aspect = complex system', 'middle', 'L')
    s += t(240, 332, 'Aorist: no equivalent in most modern languages; "simple past without duration"', 'middle', 'Ls')
    s += hr(340)
    s += sh(348, 'GRAMMAR COMPARISON')
    s += t(240, 359, 'Egyptian: VSO, two genders, dual, verb-suffix pronouns (Afroasiatic)', 'middle', 'L')
    s += t(240, 370, 'Greek: flexible SVO/VSO, 3 genders, rich case system, aspect-based (IE)', 'middle', 'L')
    s += t(240, 381, 'Both: distinguished singular / dual / plural', 'middle', 'L')
    s += t(240, 392, 'Both: grammatical gender system governing agreement', 'middle', 'Ls')
    s += t(240, 403, 'Greek provided grammatical framework for Coptic (final Egyptian stage)', 'middle', 'L')
    s += footer('61', 'ANCIENT EGYPTIAN', 'GREEK', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 61d  HISTORY ───────────────────────────────────────────────────────
def plate61d():
    s = open_svg()
    s += t(240, 28, 'ANCIENT EGYPTIAN', 'middle', 'T')
    s += t(240, 40, 'HISTORY — 4000 YEARS OF CIVILIZATION', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'ANCIENT EGYPTIAN LANGUAGE TIMELINE')
    s += t(240, 68, '~3200 BCE: earliest hieroglyphic inscriptions (Narmer Palette)', 'middle', 'L')
    s += t(240, 79, '~2600-700 BCE: Old, Middle, Late Egyptian (living language)', 'middle', 'L')
    s += t(240, 90, '~700 BCE-400 CE: Demotic (cursive administrative script)', 'middle', 'L')
    s += t(240, 101, '~200-1300 CE: Coptic (last stage; Greek-alphabet Egyptian)', 'middle', 'Ls')
    s += t(240, 112, '~1300 CE: Arabic replaces Coptic as vernacular; language "dies"', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'WORLD\'S LONGEST RECORDED LANGUAGE HISTORY')
    s += t(240, 139, 'Egyptian: continuous written record ~3200 BCE to ~1300 CE = 4500 years', 'middle', 'L')
    s += t(240, 150, 'Longest attested language in human history', 'middle', 'L')
    s += t(240, 161, 'Surpasses even Chinese, Sanskrit, and Greek in written continuity', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'GREAT TEXTS IN EGYPTIAN')
    s += t(240, 188, 'Pyramid Texts (~2400 BCE): oldest religious corpus', 'middle', 'L')
    s += t(240, 199, 'Book of the Dead (~1550 BCE): guide for the afterlife', 'middle', 'L')
    s += t(240, 210, 'Amarna Letters (~1350 BCE): diplomatic correspondence in Akkadian', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'GREEK HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'GREEK IN EGYPT: 1000 YEARS')
    s += t(240, 261, '332 BCE: Alexander founds Alexandria; Greek becomes Egypt\'s official language', 'middle', 'L')
    s += t(240, 272, 'Ptolemaic dynasty: Greek pharaohs for 275 years; bilingual courts', 'middle', 'L')
    s += t(240, 283, '30 BCE-642 CE: Roman then Byzantine rule; Greek remains administrative', 'middle', 'L')
    s += t(240, 294, 'Total: ~1000 years of Greek as Egypt\'s official language', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'THE SEPTUAGINT AND CHRISTIAN EGYPT')
    s += t(240, 321, '~250 BCE: 70 Jewish scholars translate Torah into Greek (Septuagint)', 'middle', 'L')
    s += t(240, 332, 'Translated in Alexandria; became Christian Old Testament', 'middle', 'L')
    s += t(240, 343, 'Christianity reached Egypt ~42 CE (tradition: St. Mark in Alexandria)', 'middle', 'Ls')
    s += t(240, 354, 'Coptic Christians: Greek Christian theology in Egyptian language', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'DECIPHERMENT AND MODERN LEGACY')
    s += t(240, 381, '1799: Napoleon\'s soldiers find Rosetta Stone near Rashid', 'middle', 'L')
    s += t(240, 392, '1822: Champollion deciphers using Greek text as key', 'middle', 'L')
    s += t(240, 403, 'Without Greek: 4000 years of Egyptian history would still be silent', 'middle', 'L')
    s += t(240, 414, 'Greek was the key that opened the oldest written language on Earth', 'middle', 'Ls')
    s += footer('61', 'ANCIENT EGYPTIAN', 'GREEK', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate61a_ancient_egyptian_greek_script_alt.svg', plate61a()),
                  ('plate61b_ancient_egyptian_greek_phonology_alt.svg', plate61b()),
                  ('plate61c_ancient_egyptian_greek_grammar_alt.svg', plate61c()),
                  ('plate61d_ancient_egyptian_greek_history_alt.svg', plate61d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
