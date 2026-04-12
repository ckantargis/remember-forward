"""
Batch 8 — Russian + Ukrainian alt plates (Series 24, plates 24a–24d)
Secondary language: Ukrainian (~35M speakers, East Slavic, Ukraine)
Geographic link: Moscow to Kyiv ~470mi — within 500mi radius
Both East Slavic languages descending from Old East Slavic (Kievan Rus)
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

# ── PLATE 24a  SCRIPT ────────────────────────────────────────────────────────
def plate24a():
    s = open_svg()
    s += t(240, 28, 'RUSSIAN', 'middle', 'T')
    s += t(240, 40, 'CYRILLIC SCRIPT', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'RUSSIAN CYRILLIC ALPHABET (33 LETTERS)')
    s += t(240, 68, 'Developed from Greek uncials; missionary Cyril (863 CE)', 'middle', 'Ls')
    s += t(240, 79, '\u0410 \u0411 \u0412 \u0413 \u0414 \u0415 \u0401 \u0416 \u0417 \u0418 \u0419 \u041a \u041b \u041c \u041d \u041e \u041f', 'middle', 'L')
    s += t(240, 90, '\u0420 \u0421 \u0422 \u0423 \u0424 \u0425 \u0426 \u0427 \u0428 \u0429 \u042a \u042b \u042c \u042d \u042e \u042f', 'middle', 'L')
    s += t(240, 101, 'Hard sign \u042a: separates prefix from vowel (ob\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0435)', 'middle', 'Ls')
    s += t(240, 112, 'Soft sign \u042c: palatalizes preceding consonant', 'middle', 'Ls')
    s += t(240, 123, '\u042b: unique vowel /\u0268/ — no equivalent in most languages', 'middle', 'Ls')
    s += hr(131)
    s += sh(139, 'PALATAL CONSONANTS')
    s += t(240, 150, 'Every Russian consonant has a hard/soft (palatalized) pair:', 'middle', 'L')
    s += t(240, 161, '/n/ vs. /n\u02b2/ (soft) \u2022 /t/ vs. /t\u02b2/ \u2022 /l/ vs. /l\u02b2/', 'middle', 'L')
    s += t(240, 172, 'Soft sign \u044c after consonant signals palatalization', 'middle', 'Ls')
    s += t(240, 183, 'brat (\u0431\u0440\u0430\u0442 "brother") vs. brat\u02bc (\u0431\u0440\u0430\u0442\u044c "to take") — different words!', 'middle', 'Ls')
    s += hr(191)
    s += sh(199, 'STRESS & VOWEL REDUCTION')
    s += t(240, 210, 'Stress is unpredictable — must be memorized per word', 'middle', 'L')
    s += t(240, 221, 'Unstressed /o/ \u2192 /\u0250/ (schwa): gorod /\u0261\u00f3r\u0259t/ "city"', 'middle', 'L')
    s += t(240, 232, 'Unstressed /a/ \u2192 /\u0259/: moloko /m\u0259l\u0250\u02c8ko/ "milk"', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'UKRAINIAN  \u00b7  \u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0410  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'UKRAINIAN CYRILLIC (33 LETTERS + 1 EXTRA)')
    s += t(240, 283, 'Ukrainian uses the same Cyrillic base but with key differences:', 'middle', 'Ls')
    s += t(240, 294, '\u0406 (\u0438) \u2022 \u0407 (\u0439\u0438) \u2022 \u0404 (\u0439\u0435) \u2014 letters absent in Russian', 'middle', 'L')
    s += t(240, 305, '\u0490 (Hh) \u2014 Ukrainian \u0093G\u0094 letter (pronounced /h/, not /\u0261/)', 'middle', 'L')
    s += t(240, 316, 'Russian \u0413 = /\u0261/ (voiced velar) \u2022 Ukrainian \u0433 = /\u0281/ (uvular fricative)', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'THE /H/ vs. /G/ DISTINCTION')
    s += t(240, 343, 'Ukrainian uses /\u0266/ (voiced glottal fricative) where Russian uses /\u0261/', 'middle', 'Ls')
    s += t(240, 354, 'Russian \u0433\u043e\u0440\u043e\u0434 /\u0261\u00f3r\u0259t/ \u2022 Ukrainian \u043c\u0456\u0441\u0442\u043e /\u02c8m\u02b2isto/ "city"', 'middle', 'Ls')
    s += t(240, 365, 'Ukrainian \u0433\u0430\u0440\u043d\u043e /\u02c8\u0266arno/ "fine" — /\u0266/ not /\u0261/', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'DISTINCTIVE UKRAINIAN LETTERS IN USE')
    s += t(240, 392, '\u0406 in: \u0440\u0456\u043a\u0430 "river" \u2022 \u0441\u0456\u043c\u02bc\u044f "family" \u2022 \u0456\u0441\u0442\u043e\u0440\u0456\u044f "history"', 'middle', 'L')
    s += t(240, 403, '\u0407 in: \u0457\u0436\u0430\u043a "hedgehog" \u2022 \u0454\u0432\u0440\u043e\u043f\u0435\u0439\u0441\u044c\u043a\u0438\u0439 "European"', 'middle', 'L')
    s += t(240, 414, 'Ukrainian apostrophe: m\u02bc\u044f\u0441\u043e "meat" \u2022 p\u02bc\u044f\u0442\u044c "five"', 'middle', 'Ls')
    s += hr(422)
    s += sh(430, 'SHARED SLAVIC HERITAGE')
    s += t(240, 441, 'Both derived from Old Church Slavonic Cyrillic (c. 900 CE)', 'middle', 'Ls')
    s += t(240, 452, 'Diverged as Russian/Ukrainian literary standards separated', 'middle', 'Ls')
    s += t(240, 463, 'Mutual intelligibility ~60% (higher than English/German)', 'middle', 'Ls')
    s += footer('24', 'RUSSIAN', 'UKRAINIAN', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 24b  PHONOLOGY ─────────────────────────────────────────────────────
def plate24b():
    s = open_svg()
    s += t(240, 28, 'RUSSIAN', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'CONSONANT SYSTEM (36 PHONEMES)')
    s += t(240, 68, 'Voiced/voiceless pairs: p/b  t/d  k/g  f/v  s/z  sh/zh', 'middle', 'L')
    s += t(240, 79, 'Each paired with palatalized counterpart: p\u02b2/b\u02b2  t\u02b2/d\u02b2 etc.', 'middle', 'L')
    s += t(240, 90, 'Retroflex: no retroflexes (unlike Indo-Iranian neighbors)', 'middle', 'Ls')
    s += t(240, 101, 'Affricates: /ts/ (\u0446) and /t\u0283/ (\u0447)', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'VOWEL REDUCTION')
    s += t(240, 128, 'Six vowels when stressed: a e i o u y', 'middle', 'L')
    s += t(240, 139, 'Unstressed /o/ \u2192 /\u0250/ (schwa) or /\u028c/ after hard consonants', 'middle', 'L')
    s += t(240, 150, 'Unstressed /e/ \u2192 /\u026a/ after soft consonants', 'middle', 'L')
    s += t(240, 161, 'Written vowels do NOT predict pronunciation — must learn stress', 'middle', 'Ls')
    s += hr(169)
    s += sh(177, 'CONSONANT CLUSTERS')
    s += t(240, 188, 'Russian tolerates long consonant clusters:', 'middle', 'L')
    s += t(240, 199, 'vzglyad /vzgl\u02b2at/ "glance" — 4 consonants at start', 'middle', 'L')
    s += t(240, 210, 'vstrecha /f\u02c8str\u02b2e\u02b7\u0259/ "meeting"', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'UKRAINIAN PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'UKRAINIAN VOWEL SYSTEM')
    s += t(240, 261, 'Six vowels: a e i o u i (Ukrainian \u0456 = /i/ not /\u0268/)', 'middle', 'L')
    s += t(240, 272, 'Key difference: Ukrainian has NO vowel reduction!', 'middle', 'L')
    s += t(240, 283, 'Ukrainian /o/ stays /o/ even unstressed (unlike Russian)', 'middle', 'L')
    s += t(240, 294, 'Ukrainian sounds "cleaner" to Russian speakers — vowels distinct', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, '/H/ vs. /G/ — THE DEFINING DIFFERENCE')
    s += t(240, 321, 'Russian: \u0413 = /\u0261/ (same as English "go")', 'middle', 'L')
    s += t(240, 332, 'Ukrainian: \u0433 = /\u0266/ (voiced glottal fricative — like breathy H)', 'middle', 'L')
    s += t(240, 343, 'Russian \u0433\u0440\u0430\u0434 "city" /\u0261rat/ \u2022 Ukrainian \u0433\u0440\u0430\u0434 /\u0266rad/', 'middle', 'Ls')
    s += t(240, 354, 'Same letter, different sound — major shibboleth', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'OTHER UKRAINIAN SOUND FEATURES')
    s += t(240, 381, 'Ukrainian /\u028c/ (like English "good") is distinct phoneme', 'middle', 'Ls')
    s += t(240, 392, 'Ukrainian /l\u02b2/ is softer than Russian equivalent', 'middle', 'Ls')
    s += t(240, 403, 'Ukrainian has syllabic /n\u0329/ in some words', 'middle', 'Ls')
    s += t(240, 414, 'Ukrainian \u0432 at word end = /w/ (not devoiced like Russian)', 'middle', 'Ls')
    s += hr(422)
    s += sh(430, 'PHONOLOGICAL PARALLELS')
    s += t(240, 441, 'Both: palatalized consonant pairs \u2022 Cyrillic alphabet', 'middle', 'L')
    s += t(240, 452, 'Both: 6 vowels \u2022 fixed stress (though Ukrainian less reduced)', 'middle', 'L')
    s += t(240, 463, 'Russian: heavy reduction \u2022 Ukrainian: faithful vowel quality', 'middle', 'Ls')
    s += t(240, 474, 'These differences made Ukrainian distinct under tsarist pressure', 'middle', 'Ls')
    s += footer('24', 'RUSSIAN', 'UKRAINIAN', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 24c  GRAMMAR ───────────────────────────────────────────────────────
def plate24c():
    s = open_svg()
    s += t(240, 28, 'RUSSIAN', 'middle', 'T')
    s += t(240, 40, 'CASE SYSTEM & GRAMMAR', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SIX CASES OF RUSSIAN')
    s += t(240, 68, 'Nominative (subject): brat "brother"', 'middle', 'L')
    s += t(240, 79, 'Genitive (possession/absence): brata "of brother; no brother"', 'middle', 'L')
    s += t(240, 90, 'Dative (indirect object): bratu "to/for brother"', 'middle', 'L')
    s += t(240, 101, 'Accusative (direct object): brata "brother" (animate)', 'middle', 'L')
    s += t(240, 112, 'Instrumental (means/companion): bratom "with/by brother"', 'middle', 'L')
    s += t(240, 123, 'Prepositional (location, after prep): brate "about brother"', 'middle', 'L')
    s += hr(131)
    s += sh(139, 'GRAMMATICAL GENDER (3)')
    s += t(240, 150, 'Masculine: brat "brother" \u2022 stol "table" \u2022 dom "house"', 'middle', 'L')
    s += t(240, 161, 'Feminine: sestra "sister" \u2022 kniga "book" \u2022 noch\u02bc "night"', 'middle', 'L')
    s += t(240, 172, 'Neuter: okno "window" \u2022 slovo "word" \u2022 imya "name"', 'middle', 'L')
    s += hr(180)
    s += sh(188, 'ASPECT — PERFECTIVE vs. IMPERFECTIVE')
    s += t(240, 199, 'Every verb has an aspectual pair:', 'middle', 'L')
    s += t(240, 210, 'pisat\u02bc (write, imperfective) \u2022 napisat\u02bc (write-completely, perfective)', 'middle', 'Ls')
    s += t(240, 221, 'Imperfective: ongoing, repeated, or habitual action', 'middle', 'Ls')
    s += t(240, 232, 'Perfective: completed, single, resultative action', 'middle', 'Ls')
    s += hr(240)
    # Divider
    s += sec_divider(247, 'UKRAINIAN GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(272, 'SEVEN CASES OF UKRAINIAN')
    s += t(240, 283, 'Ukrainian adds VOCATIVE case — preserved from Proto-Slavic!', 'middle', 'L')
    s += t(240, 294, 'Nominative: brat "brother"  \u2022  Vocative: bratu! "O brother!"', 'middle', 'L')
    s += t(240, 305, 'Used when directly addressing a person or personified object', 'middle', 'Ls')
    s += t(240, 316, 'Russian lost vocative (only archaic: "Gospodi!" = "O Lord!")', 'middle', 'Ls')
    s += hr(324)
    s += sh(332, 'UKRAINIAN GENDER & AGREEMENT')
    s += t(240, 343, 'Same three genders as Russian: masculine / feminine / neuter', 'middle', 'L')
    s += t(240, 354, 'But some nouns differ in gender between the two languages!', 'middle', 'Ls')
    s += t(240, 365, 'Russian: step\u02bc (FEM) \u2022 Ukrainian: step (MASC) "steppe"', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'UKRAINIAN ASPECT SYSTEM')
    s += t(240, 392, 'Same imperfective/perfective distinction as Russian', 'middle', 'L')
    s += t(240, 403, 'But Ukrainian uses -uvaty suffix more broadly for imperfective', 'middle', 'Ls')
    s += t(240, 414, 'Some verbs differ: Ukr. kazaty / Rus. govorit\u02bc "to say"', 'middle', 'Ls')
    s += hr(422)
    s += sh(430, 'GRAMMATICAL PARALLELS')
    s += t(240, 441, 'Both: case-marked nouns \u2022 grammatical gender \u2022 aspect pairs', 'middle', 'L')
    s += t(240, 452, 'Both: free word order (cases convey grammatical function)', 'middle', 'L')
    s += t(240, 463, 'Ukrainian extra: 7th vocative case (more archaic)', 'middle', 'Ls')
    s += t(240, 474, 'Ukrainian extra: /h/ vs. Russian /g/ — structural branching point', 'middle', 'Ls')
    s += footer('24', 'RUSSIAN', 'UKRAINIAN', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 24d  HISTORY ───────────────────────────────────────────────────────
def plate24d():
    s = open_svg()
    s += t(240, 28, 'RUSSIAN', 'middle', 'T')
    s += t(240, 40, 'HISTORY & EAST SLAVIC ORIGINS', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'KIEVAN RUS — SHARED ANCESTOR')
    s += t(240, 68, '862 CE: Varangian (Viking) prince Rurik founds Rus in Novgorod', 'middle', 'Ls')
    s += t(240, 79, '882 CE: Oleg moves capital to KYIV — both nations\u2019 origin city', 'middle', 'L')
    s += t(240, 90, '988 CE: Christianization of Kievan Rus under Vladimir the Great', 'middle', 'Ls')
    s += t(240, 101, 'Old East Slavic: ancestor of Russian, Ukrainian, AND Belarusian', 'middle', 'Ls')
    s += t(240, 112, '1240 CE: Mongol invasion destroys Kyiv; Rus splinters', 'middle', 'Ls')
    s += hr(120)
    s += sh(128, 'RUSSIAN LITERARY LANGUAGE')
    s += t(240, 139, 'Moscow emerged as center after Mongol period (14th c.)', 'middle', 'L')
    s += t(240, 150, 'Russian Church Slavonic remained literary standard for centuries', 'middle', 'Ls')
    s += t(240, 161, '1703: Peter the Great reforms Russian alphabet (civil script)', 'middle', 'Ls')
    s += t(240, 172, '~150M native speakers; official in 4 UN member states', 'middle', 'L')
    s += t(240, 183, 'Russian is the 8th most spoken language in the world', 'middle', 'Ls')
    s += hr(191)
    # Divider
    s += sec_divider(198, 'UKRAINIAN HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(223, 'UKRAINIAN LITERARY TRADITION')
    s += t(240, 234, 'Ukrainian distinct from Russian by 13th century', 'middle', 'L')
    s += t(240, 245, '1596: Union of Brest — Catholic/Orthodox split shapes Ukraine', 'middle', 'Ls')
    s += t(240, 256, '1798: Ivan Kotliarevsky writes Eneida in modern Ukrainian', 'middle', 'Ls')
    s += t(240, 267, 'Taras Shevchenko (1814-1861): national poet; Kobzar collection', 'middle', 'L')
    s += t(240, 278, 'Shevchenko established Ukrainian as literary language', 'middle', 'Ls')
    s += hr(286)
    s += sh(294, 'SUPPRESSION & REVIVAL')
    s += t(240, 305, '1863 Ems Decree: Russian Empire banned Ukrainian publications', 'middle', 'L')
    s += t(240, 316, '1876 Ems Decree expanded: banned all Ukrainian language use', 'middle', 'Ls')
    s += t(240, 327, 'Soviet Ukrainization (1920s) then reversed by Stalinist terror', 'middle', 'Ls')
    s += t(240, 338, 'Executed Renaissance (Rozstriliane vidrodzhennya): writers killed', 'middle', 'Ls')
    s += t(240, 349, '1991 independence: Ukrainian becomes sole official language', 'middle', 'L')
    s += hr(357)
    s += sh(365, 'HOLODOMOR (1932-33)')
    s += t(240, 376, 'Soviet-engineered famine killed 3.5-7.5M Ukrainians', 'middle', 'L')
    s += t(240, 387, 'Ukrainian farmers targeted; cultural elite executed', 'middle', 'Ls')
    s += t(240, 398, 'Recognized as genocide by 30+ countries', 'middle', 'Ls')
    s += hr(406)
    s += sh(414, 'TWO LANGUAGES, ONE ORIGIN, SEPARATE IDENTITIES')
    s += t(240, 425, 'Kyiv: founding city of Kievan Rus — claimed by BOTH nations', 'middle', 'L')
    s += t(240, 436, 'Russian: global power; UN language; Pushkin, Tolstoy, Dostoevsky', 'middle', 'Ls')
    s += t(240, 447, 'Ukrainian: national resistance language; Shevchenko, Franko', 'middle', 'Ls')
    s += t(240, 458, 'Linguistic difference: vocative case, /h/, vowel quality', 'middle', 'Ls')
    s += t(240, 469, 'Political difference: sovereignty, self-determination, identity', 'middle', 'Ls')
    s += footer('24', 'RUSSIAN', 'UKRAINIAN', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate24a_russian_ukrainian_script_alt.svg', plate24a()),
                  ('plate24b_russian_ukrainian_phonology_alt.svg', plate24b()),
                  ('plate24c_russian_ukrainian_grammar_alt.svg', plate24c()),
                  ('plate24d_russian_ukrainian_history_alt.svg', plate24d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
