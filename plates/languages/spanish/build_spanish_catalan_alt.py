"""
Batch 9 — Spanish + Catalan alt plates (Series 26, plates 26a–26d)
Secondary language: Catalan (~10M speakers, Romance, Catalonia/Valencia/Balearics/Andorra)
Geographic link: Madrid to Barcelona ~400mi — within 500mi
Both Ibero-Romance languages; Catalan geographically and linguistically bridges Spanish and Occitan/French
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

# ── PLATE 26a  SCRIPT ────────────────────────────────────────────────────────
def plate26a():
    s = open_svg()
    s += t(240, 28, 'SPANISH', 'middle', 'T')
    s += t(240, 40, 'WRITING SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SPANISH LATIN ALPHABET (27 LETTERS)')
    s += t(240, 68, 'Same as English plus: \u00f1 (enye) and ch/ll as traditional digraphs', 'middle', 'L')
    s += t(240, 79, '\u00f1: unique Spanish letter — "ny" sound /\u0272/', 'middle', 'L')
    s += t(240, 90, 'ca\u00f1on \u2022 ma\u00f1ana \u2022 ni\u00f1o \u2022 espa\u00f1ol', 'middle', 'L')
    s += t(240, 101, 'Acute accent marks stress when irregular: caf\u00e9, m\u00fasica, el\u00e9ctrico', 'middle', 'L')
    s += t(240, 112, 'Interrogative/exclamatory: inverted \u00bf and \u00a1 at start of phrase', 'middle', 'L')
    s += hr(120)
    s += sh(128, 'SPANISH SPELLING REGULARITY')
    s += t(240, 139, 'Spanish spelling is highly phonemic — words spelled as pronounced', 'middle', 'L')
    s += t(240, 150, 'One-to-one correspondence (mostly): cada letra, un sonido', 'middle', 'Ls')
    s += t(240, 161, 'Exception: h is always silent (hola, hablar, historia)', 'middle', 'Ls')
    s += t(240, 172, 'Exception: g before e/i = /x/ (gente, girasol)', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'REAL ACADEMIA ESPA\u00d1OLA (RAE)')
    s += t(240, 199, 'Founded 1713: standardizes Spanish spelling and grammar', 'middle', 'L')
    s += t(240, 210, '1994: ch and ll removed from alphabet (now letter pairs)', 'middle', 'Ls')
    s += t(240, 221, 'Unifies spelling across 20+ Spanish-speaking countries', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'CATALAN  \u00b7  CATAL\u00c0  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'CATALAN LATIN ALPHABET (26 LETTERS)')
    s += t(240, 272, 'Latin alphabet with key additions and digraphs:', 'middle', 'L')
    s += t(240, 283, '\u00e0 \u00e8 \u00e9 \u00f3 \u00f2 \u00fa \u00fc \u00ef: accented vowels mark quality and stress', 'middle', 'L')
    s += t(240, 294, '\u00e7 (ce-trencada): /s/ before a/o/u \u2022 for\u00e7a "strength"', 'middle', 'L')
    s += t(240, 305, '\u00b7l (ela geminada): doubled L \u2022 intel\u00b7lig\u00e8ncia "intelligence"', 'middle', 'L')
    s += t(240, 316, 'ny = /\u0272/ (same as Spanish \u00f1) \u2022 ny in "Catalunya"', 'middle', 'L')
    s += hr(324)
    s += sh(332, 'CATALAN DISTINCTIVE SPELLINGS')
    s += t(240, 343, 'tg/tj = /d\u0292/ (affricate): viatge "journey", jutge "judge"', 'middle', 'L')
    s += t(240, 354, 'ig at word end = /t\u0283/: mig "half", boig "crazy"', 'middle', 'L')
    s += t(240, 365, 'Final devoicing: not in spelling but in pronunciation', 'middle', 'Ls')
    s += hr(373)
    s += sh(381, 'PARALLEL & DIVERGENT SPELLINGS')
    s += t(240, 392, 'Spanish: ma\u00f1ana  \u2022  Catalan: dem\u00e0 (different word, same meaning)', 'middle', 'L')
    s += t(240, 403, 'Spanish: agua  \u2022  Catalan: aigua (preserved Latin diphthong)', 'middle', 'L')
    s += t(240, 414, 'Spanish: ca\u00f1on  \u2022  Catalan: ca\u00f1\u00f3 (same \u00f1 letter!)', 'middle', 'L')
    s += t(240, 425, 'Shared Latin base; divergent Romance evolution visible in text', 'middle', 'Ls')
    s += footer('26', 'SPANISH', 'CATALAN', 'a', 'SCRIPT')
    s += close_svg()
    return s

# ── PLATE 26b  PHONOLOGY ─────────────────────────────────────────────────────
def plate26b():
    s = open_svg()
    s += t(240, 28, 'SPANISH', 'middle', 'T')
    s += t(240, 40, 'PHONOLOGY', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SPANISH VOWEL SYSTEM')
    s += t(240, 68, 'Five pure vowels: a e i o u — no diphthongs, no long/short', 'middle', 'L')
    s += t(240, 79, 'Pure vowels never reduce (unlike English schwa tendency)', 'middle', 'L')
    s += t(240, 90, 'Diphthongs: ie (bien) \u2022 ue (puedo) \u2022 ei (ley) \u2022 ou (bou)', 'middle', 'L')
    s += hr(98)
    s += sh(106, 'SPANISH CONSONANTS')
    s += t(240, 117, 'Distinction: Castilian vs. Latin American \u201cceceo/seseo\u201d:', 'middle', 'L')
    s += t(240, 128, 'Castilian: c (before e/i) and z = /\u03b8/ (like English "thin")', 'middle', 'L')
    s += t(240, 139, 'Latin American: c and z both = /s/ (no dental fricative)', 'middle', 'L')
    s += t(240, 150, 'Trill /r/: perro "dog" vs. flap /\u027e/: pero "but"', 'middle', 'L')
    s += t(240, 161, 'Velar /x/: jota sound in hijo, gente, reloj', 'middle', 'L')
    s += hr(169)
    s += sh(177, 'STRESS RULES')
    s += t(240, 188, 'Default: penultimate stress if word ends in vowel, n, or s', 'middle', 'L')
    s += t(240, 199, 'Default: final stress if word ends in consonant (except n/s)', 'middle', 'L')
    s += t(240, 210, 'Accent mark: any deviation from default rule', 'middle', 'Ls')
    s += hr(218)
    # Divider
    s += sec_divider(225, 'CATALAN PHONOLOGY  \u00b7  SECONDARY LANGUAGE')
    s += sh(250, 'CATALAN VOWEL SYSTEM (EASTERN DIALECT)')
    s += t(240, 261, 'Seven stressed vowels: a \u025b e i \u0254 o u', 'middle', 'L')
    s += t(240, 272, 'But unstressed: a/e \u2192 /\u0259/ (schwa!), o/u \u2192 /u/', 'middle', 'L')
    s += t(240, 283, 'Catalan reduces unstressed vowels — MORE like French than Spanish', 'middle', 'L')
    s += t(240, 294, 'pa "bread" /pa/ but pans /p\u0259ns/ (a becomes schwa)', 'middle', 'Ls')
    s += hr(302)
    s += sh(310, 'CATALAN CONSONANTS')
    s += t(240, 321, 'Final devoicing: b/d/g \u2192 p/t/k at word end (like German!)', 'middle', 'L')
    s += t(240, 332, 'l\u00b7l /l:/ geminate lateral: difference from French/Spanish', 'middle', 'L')
    s += t(240, 343, 'No /x/ (jota) — Catalan lacks this Spanish sound', 'middle', 'Ls')
    s += t(240, 354, 'Affricate /t\u0283/ \u2022 /d\u0292/: txi\u0301xer "woodpecker"', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'PHONOLOGICAL COMPARISON')
    s += t(240, 381, 'Spanish: no schwa \u2022 Catalan: schwa in unstressed position', 'middle', 'L')
    s += t(240, 392, 'Spanish: no final devoicing \u2022 Catalan: b\u2192p d\u2192t g\u2192k', 'middle', 'L')
    s += t(240, 403, 'Spanish: /\u03b8/ in Castilian \u2022 Catalan: no /\u03b8/', 'middle', 'L')
    s += t(240, 414, 'Both: 5 core vowels \u2022 trill vs. flap /r/ \u2022 /\u0272/ phoneme', 'middle', 'Ls')
    s += t(240, 425, 'Catalan phonology: between Spanish and French', 'middle', 'Ls')
    s += footer('26', 'SPANISH', 'CATALAN', 'b', 'PHONOLOGY')
    s += close_svg()
    return s

# ── PLATE 26c  GRAMMAR ───────────────────────────────────────────────────────
def plate26c():
    s = open_svg()
    s += t(240, 28, 'SPANISH', 'middle', 'T')
    s += t(240, 40, 'GRAMMAR & VERB SYSTEM', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SPANISH VERB SYSTEM')
    s += t(240, 68, 'Three conjugation classes: -ar \u2022 -er \u2022 -ir', 'middle', 'L')
    s += t(240, 79, 'hablar (speak): hablo \u2022 hablas \u2022 habla \u2022 hablamos \u2022 hablan', 'middle', 'L')
    s += t(240, 90, '14 tenses/moods: indicative (6) \u2022 subjunctive (4) \u2022 imperative...', 'middle', 'L')
    s += t(240, 101, 'Subjunctive: quiero que vengas "I want you to come"', 'middle', 'L')
    s += hr(109)
    s += sh(117, 'SER vs. ESTAR')
    s += t(240, 128, 'Two "to be" verbs (unique in Romance family):', 'middle', 'L')
    s += t(240, 139, 'SER: permanent qualities, identity, origin, time', 'middle', 'L')
    s += t(240, 150, 'ESTAR: temporary states, location, feelings, ongoing actions', 'middle', 'L')
    s += t(240, 161, 'Ella es guapa "She is beautiful" (general quality)', 'middle', 'Ls')
    s += t(240, 172, 'Ella est\u00e1 guapa "She looks beautiful" (right now)', 'middle', 'Ls')
    s += hr(180)
    s += sh(188, 'SPANISH NOUN SYSTEM')
    s += t(240, 199, 'Two genders: masculine / feminine (no neuter)', 'middle', 'L')
    s += t(240, 210, 'el libro (masc.) \u2022 la mesa (fem.) \u2022 los libros \u2022 las mesas', 'middle', 'L')
    s += t(240, 221, 'Articles and adjectives agree: un libro rojo \u2022 una mesa roja', 'middle', 'Ls')
    s += hr(229)
    # Divider
    s += sec_divider(236, 'CATALAN GRAMMAR  \u00b7  SECONDARY LANGUAGE')
    s += sh(261, 'CATALAN VERB SYSTEM')
    s += t(240, 272, 'Three conjugation classes: -ar \u2022 -er \u2022 -re / -ir', 'middle', 'L')
    s += t(240, 283, 'parlar (speak): parlo \u2022 parles \u2022 parla \u2022 parlem \u2022 parlen', 'middle', 'L')
    s += t(240, 294, 'Periphrastic past: vaig parlar "I spoke" (vaig + infinitive)', 'middle', 'L')
    s += t(240, 305, 'Catalan uses periphrastic past in speech (not simple past)', 'middle', 'Ls')
    s += hr(313)
    s += sh(321, 'CATALAN SER vs. ESTAR')
    s += t(240, 332, 'Catalan ALSO has ser/estar distinction (like Spanish)!', 'middle', 'L')
    s += t(240, 343, '\u00e9s (ser, permanent) \u2022 est\u00e0 (estar, temporary)', 'middle', 'L')
    s += t(240, 354, 'French lacks this; Catalan shares it with Spanish and Portuguese', 'middle', 'Ls')
    s += hr(362)
    s += sh(370, 'CATALAN NOUN SYSTEM')
    s += t(240, 381, 'Two genders: masculine / feminine', 'middle', 'L')
    s += t(240, 392, 'el (masc.) \u2022 la (fem.) \u2022 els / les (plurals)', 'middle', 'L')
    s += t(240, 403, 'Partitive article: del/de la (not in Spanish standard)', 'middle', 'L')
    s += hr(411)
    s += sh(419, 'GRAMMATICAL PARALLELS')
    s += t(240, 430, 'Both: two genders \u2022 noun-adjective agreement \u2022 articles', 'middle', 'L')
    s += t(240, 441, 'Both: ser/estar distinction \u2022 subjunctive mood', 'middle', 'L')
    s += t(240, 452, 'Both: pro-drop (subject pronouns optional)', 'middle', 'L')
    s += t(240, 463, 'Catalan: periphrastic past dominant \u2022 Spanish: simple past common', 'middle', 'Ls')
    s += footer('26', 'SPANISH', 'CATALAN', 'c', 'GRAMMAR')
    s += close_svg()
    return s

# ── PLATE 26d  HISTORY ───────────────────────────────────────────────────────
def plate26d():
    s = open_svg()
    s += t(240, 28, 'SPANISH', 'middle', 'T')
    s += t(240, 40, 'HISTORY & IBERIAN ROMANCE', 'middle', 'S')
    s += hr(47)
    s += sh(57, 'SPANISH ORIGINS')
    s += t(240, 68, 'Latin brought to Iberia by Roman conquest (218 BCE)', 'middle', 'L')
    s += t(240, 79, 'Vulgar Latin + Visigothic influence \u2192 Ibero-Romance', 'middle', 'Ls')
    s += t(240, 90, '711 CE: Moorish conquest; Arabic influence begins (800+ loanwords)', 'middle', 'L')
    s += t(240, 101, 'El Cantar de Mio Cid (~1200): earliest major Castilian text', 'middle', 'L')
    s += t(240, 112, '1492: Reconquista complete; Nebrija publishes first Spanish grammar', 'middle', 'L')
    s += t(240, 123, 'Same year: Columbus sets sail; Spanish becomes global language', 'middle', 'Ls')
    s += hr(131)
    s += sh(139, 'SPANISH TODAY')
    s += t(240, 150, '~500M native speakers; 2nd most spoken language by natives', 'middle', 'L')
    s += t(240, 161, 'Official in 20 countries; UN official language', 'middle', 'Ls')
    s += t(240, 172, 'Cervantes: Don Quijote (1605) — first modern novel', 'middle', 'L')
    s += hr(180)
    # Divider
    s += sec_divider(187, 'CATALAN HISTORY  \u00b7  SECONDARY LANGUAGE')
    s += sh(212, 'CATALAN ORIGINS')
    s += t(240, 223, '9th c.: Catalan emerges in the Marca Hispanica (Carolingian)', 'middle', 'L')
    s += t(240, 234, 'County of Barcelona: independent from both France and Castile', 'middle', 'L')
    s += t(240, 245, '13th c.: Crown of Aragon expands; Catalan becomes empire language', 'middle', 'Ls')
    s += t(240, 256, 'Catalan spoken in: Sicily, Sardinia, Greece under Aragon rule', 'middle', 'Ls')
    s += hr(264)
    s += sh(272, 'GOLDEN AGE TO SUPPRESSION')
    s += t(240, 283, 'Ramon Llull (1232-1316): first major Catalan prose author', 'middle', 'L')
    s += t(240, 294, 'Joanot Martorell: Tirant lo Blanc (1490) — early European novel', 'middle', 'L')
    s += t(240, 305, '1716: Nueva Planta decree — Castilian replaces Catalan officially', 'middle', 'Ls')
    s += t(240, 316, 'Renaixenca (19th c.): Catalan literary and cultural revival', 'middle', 'Ls')
    s += t(240, 327, '1936-75: Franco dictatorship bans Catalan in public life', 'middle', 'L')
    s += hr(335)
    s += sh(343, 'CATALAN TODAY')
    s += t(240, 354, '~10M speakers; co-official in Catalonia, Valencia, Balearics', 'middle', 'L')
    s += t(240, 365, 'Andorra: Catalan is the SOLE official language', 'middle', 'L')
    s += t(240, 376, 'Also spoken in Alghero (Sardinia) and Roussillon (France)', 'middle', 'Ls')
    s += t(240, 387, 'Independence debate (2017 referendum): language as identity', 'middle', 'Ls')
    s += hr(395)
    s += sh(403, 'ROMANCE SIBLINGS')
    s += t(240, 414, 'Both: descended from Vulgar Latin of Iberian Peninsula', 'middle', 'Ls')
    s += t(240, 425, 'Both: influenced by Arabic during Moorish period', 'middle', 'Ls')
    s += t(240, 436, 'Spanish: expanded south and west  \u2022  Catalan: expanded east and south', 'middle', 'Ls')
    s += t(240, 447, 'Catalan: closer to Occitan/French  \u2022  Spanish: closer to Portuguese', 'middle', 'Ls')
    s += t(240, 458, 'Two Romance languages, one Iberian history, distinct identities', 'middle', 'L')
    s += footer('26', 'SPANISH', 'CATALAN', 'd', 'HISTORY')
    s += close_svg()
    return s

for fn, plate in [('plate26a_spanish_catalan_script_alt.svg', plate26a()),
                  ('plate26b_spanish_catalan_phonology_alt.svg', plate26b()),
                  ('plate26c_spanish_catalan_grammar_alt.svg', plate26c()),
                  ('plate26d_spanish_catalan_history_alt.svg', plate26d())]:
    path = OUT / fn
    path.write_text(plate, encoding='utf-8')
    print(f'wrote {path}')
