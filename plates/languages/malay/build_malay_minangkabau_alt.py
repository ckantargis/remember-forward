# build_malay_minangkabau_alt.py  — Series 19 ALT  (Malay + Minangkabau)
# Secondary language: Minangkabau (~6M speakers, West Sumatra, Indonesia)
# Geographic basis: standard 500mi radius from Kuala Lumpur (3.14°N, 101.69°E)
# Padang (West Sumatra capital) is ~450mi from KL — within 500mi radius
# Minangkabau is closely related to Malay (same Austronesian branch) and
# is the world's largest matrilineal society; merantau tradition
# Outputs: plate19a–19d_malay_minangkabau_*_alt.svg

from pathlib import Path

OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text { font-family: Georgia, serif; }\n'
        '  .T{font-size:11px;font-weight:bold;letter-spacing:1.5px}\n'
        '  .S{font-size:6.5px;letter-spacing:1.5px}\n'
        '  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}\n'
        '  .Hb{font-size:7px;font-weight:bold;letter-spacing:2px}\n'
        '  .L{font-size:7px} .Ls{font-size:6px} .Lx{font-size:5.5px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')

def close_svg(): return '</svg>\n'

def t(x, y, text, anchor='middle', cls='L'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>\n'

def hr(y, x1=20, x2=460, sw=0.5):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y, label, cls='H'):
    return t(240, y, label, 'middle', cls)

def sec_divider(y, label):
    out  = hr(y, sw=1.5)
    out += f'<rect x="20" y="{y+3}" width="440" height="14" fill="black"/>\n'
    out += f'<text x="240" y="{y+13}" text-anchor="middle" class="Hb" fill="white">{esc(label)}</text>\n'
    out += hr(y+17, sw=0.3)
    return out

def footer(num, lang1, lang2, letter, desc):
    return (hr(625)
        + t(240, 620,
            f'PLATE {esc(num)}{esc(letter)} ALT \u00b7 {esc(lang1)} / {esc(lang2)}'
            f' \u00b7 {esc(desc.upper())} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG',
            'middle', 'M')
        + hr(633)
        + t(240, 648,
            'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.',
            'middle', 'Fb')
        + t(240, 663,
            'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET',
            'middle', 'F'))

# ─────────────────────────────────────────────────────────────────────────────
def build_19a_alt():
    svg = open_svg()
    svg += t(240, 32, 'MALAY (BAHASA MELAYU) / MINANGKABAU (BASO MINANG)', 'middle', 'T')
    svg += t(240, 44, 'AUSTRONESIAN · MALAYO-POLYNESIAN · SISTER LANGUAGES · ~450MI APART', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 19A ALT · SCRIPT & SOUNDS')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— MALAY: SCRIPT & WRITING SYSTEMS —')
    svg += t(240, 89, 'Two scripts in active use: RUMI (Latin) and JAWI (Arabic-based)', 'middle', 'Ls')
    svg += t(240, 100, 'Rumi: standard in Malaysia, Indonesia (as Bahasa Indonesia), Singapore, Brunei', 'middle', 'Ls')
    svg += t(240, 111, 'Jawi: traditional script, still used in religious texts, Brunei official, Kelantan', 'middle', 'Ls')
    svg += hr(117, sw=0.3)
    svg += sh(127, 'JAWI SCRIPT (ARABIC-BASED)')
    svg += t(240, 138, 'Adapted from Arabic abjad (right-to-left) with 6 added letters for Malay sounds', 'middle', 'Ls')
    svg += t(240, 149, 'Added: ca (\u0686) · nga · pa · ga · nya · va — not in Arabic', 'middle', 'Ls')
    svg += t(240, 160, 'Vowels marked partially (as in Arabic harakat); often omitted in daily texts', 'middle', 'Ls')
    svg += t(240, 171, 'Historical: Malay was written in Jawi for ~700 years before Rumi was adopted', 'middle', 'Ls')
    svg += hr(177, sw=0.3)
    svg += sh(187, 'MALAY PHONOLOGY OVERVIEW')
    svg += t(240, 198, '6 vowels: /a e \u0259 i o u/ · schwa /\u0259/ in unstressed syllables', 'middle', 'Ls')
    svg += t(240, 209, 'No tones · stress: penultimate syllable (with schwa exceptions)', 'middle', 'Ls')
    svg += t(240, 220, 'Final consonant allowed: /p t k m n \u014b l r h/ (but many reduce to glottal stop)', 'middle', 'Ls')
    svg += hr(226, sw=0.3)
    svg += sh(236, 'CONSONANT INVENTORY')
    svg += t(240, 247, '/p b t d k g/ · /m n \u014b/ · /f v s z/ · /t\u0283 d\u0292/ · /r l/ · /h j w/', 'middle', 'Ls')
    svg += t(240, 258, 'Glottal stop at word-final position (bakul /bakU\u0294/ basket)', 'middle', 'Ls')
    svg += hr(264, sw=0.3)
    svg += sh(274, 'MORPHOLOGY: AFFIXATION')
    svg += t(240, 285, 'Prefix me-: verb-forming from nouns/adjectives', 'middle', 'Ls')
    svg += t(240, 296, 'Prefix pe-: agentive (pelari = runner, from lari = run)', 'middle', 'Ls')
    svg += t(240, 307, 'Suffix -an: nominalization (makanan = food, from makan = eat)', 'middle', 'Ls')
    svg += t(240, 318, 'Circumfix me-...-kan: causative transitivizer (me-lari-kan = to make run)', 'middle', 'Ls')
    svg += hr(324, sw=0.3)
    svg += sh(334, 'SAMPLE WORDS')
    svg += t(240, 345, 'air (water) · makan (eat) · rumah (house) · saya (I) · anda (you formal)', 'middle', 'Ls')

    svg += sec_divider(357, 'MINANGKABAU (BASO MINANG) — W. SUMATRA · ~6M SPEAKERS')

    svg += sh(382, '— MINANGKABAU: SCRIPT & SOUNDS —')
    svg += t(240, 393, 'Script: Latin (primary) and Jawi (traditional) — same as Malay', 'middle', 'Ls')
    svg += t(240, 404, 'Closely related to Malay but DISTINCT language with significant differences', 'middle', 'Ls')
    svg += hr(410, sw=0.3)
    svg += sh(420, 'KEY PHONOLOGICAL DIFFERENCES FROM MALAY')
    svg += t(100, 431, 'MALAY', 'middle', 'Lx')
    svg += t(240, 431, 'FEATURE', 'middle', 'Lx')
    svg += t(380, 431, 'MINANGKABAU', 'middle', 'Lx')
    svg += hr(435, sw=0.3)
    svg += t(100, 444, 'rumah', 'middle', 'Ls')
    svg += t(240, 444, 'house (final -h)', 'middle', 'Ls')
    svg += t(380, 444, 'rumah', 'middle', 'Ls')
    svg += t(100, 454, 'malam', 'middle', 'Ls')
    svg += t(240, 454, 'night (-m final)', 'middle', 'Ls')
    svg += t(380, 454, 'malam', 'middle', 'Ls')
    svg += t(100, 464, 'apa', 'middle', 'Ls')
    svg += t(240, 464, 'what', 'middle', 'Ls')
    svg += t(380, 464, 'apo', 'middle', 'Ls')
    svg += t(100, 474, 'saya', 'middle', 'Ls')
    svg += t(240, 474, 'I (formal)', 'middle', 'Ls')
    svg += t(380, 474, 'ambo / den', 'middle', 'Ls')
    svg += t(100, 484, 'tidak', 'middle', 'Ls')
    svg += t(240, 484, 'no / not', 'middle', 'Ls')
    svg += t(380, 484, 'indak / indeh', 'middle', 'Ls')
    svg += hr(489, sw=0.3)
    svg += sh(499, 'MINANGKABAU VOWELS')
    svg += t(240, 510, 'Final /a/ in Malay often corresponds to /o/ in Minangkabau', 'middle', 'Ls')
    svg += t(240, 521, 'saya → ambo · apa → apo · kita → kito · dia → inyo', 'middle', 'Ls')
    svg += t(240, 532, 'This -a → -o shift is a consistent diagnostic of Minang vs Malay', 'middle', 'Ls')
    svg += hr(538, sw=0.3)
    svg += sh(548, 'UNIQUE MINANGKABAU SOUNDS')
    svg += t(240, 559, '/au/ diphthong in Malay becomes /o/ in Minang: kalau → kalo (if)', 'middle', 'Ls')
    svg += t(240, 570, '/ai/ diphthong → /e/ in Minang: pakai → pake (use)', 'middle', 'Ls')
    svg += hr(576, sw=0.3)
    svg += sh(586, 'SAMPLE WORDS (MINANGKABAU)')
    svg += t(240, 597, 'ambo (I) · ang / awak (you) · inyo (s/he) · kito (we, incl.)', 'middle', 'Ls')
    svg += t(240, 608, 'aie (water) · makan (eat — same!) · rumah gadang (great house, matrilineal home)', 'middle', 'Ls')

    svg += footer(19, 'MALAY', 'MINANGKABAU', 'A', 'SCRIPT & SOUNDS')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_19b_alt():
    svg = open_svg()
    svg += t(240, 32, 'MALAY (BAHASA MELAYU) / MINANGKABAU (BASO MINANG)', 'middle', 'T')
    svg += t(240, 44, 'AUSTRONESIAN · MALAYO-POLYNESIAN · PHONOLOGY COMPARISON', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 19B ALT · PHONOLOGY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— MALAY PHONOLOGY IN DEPTH —')
    svg += sh(88, 'THE MALAY VOWEL SYSTEM')
    svg += t(100, 99, 'VOWEL', 'middle', 'Lx')
    svg += t(240, 99, 'IPA', 'middle', 'Lx')
    svg += t(390, 99, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(103, sw=0.3)
    svg += t(100, 112, 'a', 'middle', 'Ls')
    svg += t(240, 112, '/a/', 'middle', 'Ls')
    svg += t(390, 112, 'api (fire)', 'middle', 'Ls')
    svg += t(100, 122, 'e (pepet)', 'middle', 'Ls')
    svg += t(240, 122, '/\u0259/ schwa', 'middle', 'Ls')
    svg += t(390, 122, 'emak (mother)', 'middle', 'Ls')
    svg += t(100, 132, 'e (taling)', 'middle', 'Ls')
    svg += t(240, 132, '/e/', 'middle', 'Ls')
    svg += t(390, 132, 'enam (six)', 'middle', 'Ls')
    svg += t(100, 142, 'i', 'middle', 'Ls')
    svg += t(240, 142, '/i/', 'middle', 'Ls')
    svg += t(390, 142, 'ikan (fish)', 'middle', 'Ls')
    svg += t(100, 152, 'o', 'middle', 'Ls')
    svg += t(240, 152, '/o/', 'middle', 'Ls')
    svg += t(390, 152, 'orang (person)', 'middle', 'Ls')
    svg += t(100, 162, 'u', 'middle', 'Ls')
    svg += t(240, 162, '/u/', 'middle', 'Ls')
    svg += t(390, 162, 'ular (snake)', 'middle', 'Ls')
    svg += hr(167, sw=0.3)
    svg += sh(177, 'STRESS AND RHYTHM')
    svg += t(240, 188, 'Stress: penultimate syllable by default (except: schwa syllable skipped)', 'middle', 'Ls')
    svg += t(240, 199, 'emak /\u02c8e.mak/ vs empat /\u02c8em.pat/ — schwa moves stress leftward', 'middle', 'Ls')
    svg += t(240, 210, 'Malay is non-tonal: no lexical tone contrast (unlike neighboring Mandarin, Lao)', 'middle', 'Ls')
    svg += hr(216, sw=0.3)
    svg += sh(226, 'REDUPLICATION')
    svg += t(240, 237, 'Full reduplication = plural: orang-orang (people) from orang (person)', 'middle', 'Ls')
    svg += t(240, 248, 'Partial/modified reduplication = variety: sayur-mayur (all kinds of vegetables)', 'middle', 'Ls')
    svg += t(240, 259, 'Reduplication of verb = continuity: jalan-jalan (walking around, strolling)', 'middle', 'Ls')
    svg += hr(265, sw=0.3)
    svg += sh(275, 'MALAY-INDONESIAN DIVERGENCE (SAME LANGUAGE, TWO STANDARDS)')
    svg += t(240, 286, 'Malaysian Malay and Bahasa Indonesia are mutually intelligible but diverging', 'middle', 'Ls')
    svg += t(240, 297, 'Vocab: rumah sakit (MY hospital) vs rumah sakit (ID same) · kereta vs mobil (car)', 'middle', 'Ls')
    svg += t(240, 308, 'Indonesian pronunciation more open vowels; Malaysian more conservative', 'middle', 'Ls')
    svg += hr(314, sw=0.3)
    svg += sh(324, 'NUMBERS 1–10')
    svg += t(240, 335, 'satu · dua · tiga · empat · lima · enam · tujuh · lapan · sembilan · sepuluh', 'middle', 'Ls')

    svg += sec_divider(347, 'MINANGKABAU (BASO MINANG) — PHONOLOGY')

    svg += sh(372, '— MINANGKABAU PHONOLOGY —')
    svg += sh(383, 'SYSTEMATIC -A TO -O VOWEL SHIFT')
    svg += t(240, 394, 'Word-final /a/ in Proto-Malay consistently → /o/ in Minangkabau:', 'middle', 'Ls')
    svg += t(100, 405, 'PROTO-MALAY', 'middle', 'Lx')
    svg += t(240, 405, 'MALAY', 'middle', 'Lx')
    svg += t(380, 405, 'MINANGKABAU', 'middle', 'Lx')
    svg += hr(409, sw=0.3)
    svg += t(100, 418, '*kita', 'middle', 'Ls')
    svg += t(240, 418, 'kita (we-incl)', 'middle', 'Ls')
    svg += t(380, 418, 'kito', 'middle', 'Ls')
    svg += t(100, 428, '*dia', 'middle', 'Ls')
    svg += t(240, 428, 'dia (s/he)', 'middle', 'Ls')
    svg += t(380, 428, 'inyo', 'middle', 'Ls')
    svg += t(100, 438, '*apa', 'middle', 'Ls')
    svg += t(240, 438, 'apa (what)', 'middle', 'Ls')
    svg += t(380, 438, 'apo', 'middle', 'Ls')
    svg += t(100, 448, '*saya', 'middle', 'Ls')
    svg += t(240, 448, 'saya (I formal)', 'middle', 'Ls')
    svg += t(380, 448, 'ambo', 'middle', 'Ls')
    svg += hr(453, sw=0.3)
    svg += sh(463, 'DIPHTHONG SIMPLIFICATION')
    svg += t(240, 474, 'Malay /au/ → Minang /o/: kalau → kalo · pulau → pulo', 'middle', 'Ls')
    svg += t(240, 485, 'Malay /ai/ → Minang /e/: pakai → pake · lantai → lante', 'middle', 'Ls')
    svg += hr(491, sw=0.3)
    svg += sh(501, 'MINANGKABAU CONSONANTS')
    svg += t(240, 512, 'Similar to Malay; preserves /r/ as a distinct rhotic /r/ (not reduced to /\u0281/)', 'middle', 'Ls')
    svg += t(240, 523, 'Final /-k/ often reduces to glottal stop [\u0294] as in Malay', 'middle', 'Ls')
    svg += hr(529, sw=0.3)
    svg += sh(539, 'REDUPLICATION IN MINANGKABAU')
    svg += t(240, 550, 'Same reduplication system as Malay: anak-anak (children) from anak (child)', 'middle', 'Ls')
    svg += t(240, 561, 'Minang reduplication: baraja-raja (keep studying) — continuative meaning', 'middle', 'Ls')
    svg += hr(567, sw=0.3)
    svg += sh(577, 'NUMBERS 1–10 (MINANGKABAU)')
    svg += t(240, 588, 'ciek · duo · tigo · ampek · limo · anam · tujuah · salapan · sambilan · sapuluah', 'middle', 'Ls')
    svg += t(240, 599, 'cf. Malay: satu · dua · tiga · empat · lima · enam · tujuh · lapan · sembilan · sepuluh', 'middle', 'Ls')
    svg += hr(605, sw=0.3)
    svg += sh(615, 'MUTUAL INTELLIGIBILITY')
    svg += t(240, 626, 'High intelligibility with Malay but distinct enough to be a separate language', 'middle', 'Ls')

    svg += footer(19, 'MALAY', 'MINANGKABAU', 'B', 'PHONOLOGY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_19c_alt():
    svg = open_svg()
    svg += t(240, 32, 'MALAY (BAHASA MELAYU) / MINANGKABAU (BASO MINANG)', 'middle', 'T')
    svg += t(240, 44, 'AUSTRONESIAN · MALAYO-POLYNESIAN · GRAMMAR & VOCABULARY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 19C ALT · GRAMMAR & CORE VOCABULARY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— MALAY GRAMMAR —')
    svg += t(240, 88, 'Highly analytic: no case, no grammatical gender, no verb conjugation for person', 'middle', 'Ls')
    svg += t(240, 99, 'No tense marking on verbs — time expressed by adverbs (semalam, esok, sekarang)', 'middle', 'Ls')
    svg += t(240, 110, 'SVO word order · adjectives follow nouns · question words in-situ', 'middle', 'Ls')
    svg += hr(116, sw=0.3)
    svg += sh(126, 'MALAY AFFIXATION SYSTEM')
    svg += t(100, 137, 'AFFIX', 'middle', 'Lx')
    svg += t(240, 137, 'FUNCTION', 'middle', 'Lx')
    svg += t(390, 137, 'EXAMPLE', 'middle', 'Lx')
    svg += hr(141, sw=0.3)
    svg += t(100, 150, 'me-', 'middle', 'Ls')
    svg += t(240, 150, 'Active transitive verb', 'middle', 'Ls')
    svg += t(390, 150, 'makan → memakan', 'middle', 'Ls')
    svg += t(100, 160, 'di-', 'middle', 'Ls')
    svg += t(240, 160, 'Passive verb', 'middle', 'Ls')
    svg += t(390, 160, 'dimakan (is eaten)', 'middle', 'Ls')
    svg += t(100, 170, '-kan', 'middle', 'Ls')
    svg += t(240, 170, 'Causative/benefactive', 'middle', 'Ls')
    svg += t(390, 170, 'makankan (feed to)', 'middle', 'Ls')
    svg += t(100, 180, '-an', 'middle', 'Ls')
    svg += t(240, 180, 'Nominalization', 'middle', 'Ls')
    svg += t(390, 180, 'makanan (food)', 'middle', 'Ls')
    svg += t(100, 190, 'ter-', 'middle', 'Ls')
    svg += t(240, 190, 'Accidental/superlative', 'middle', 'Ls')
    svg += t(390, 190, 'termakan (accidentally eaten)', 'middle', 'Ls')
    svg += t(100, 200, 'ber-', 'middle', 'Ls')
    svg += t(240, 200, 'Stative / intransitive', 'middle', 'Ls')
    svg += t(390, 200, 'berjalan (to walk)', 'middle', 'Ls')
    svg += hr(205, sw=0.3)
    svg += sh(215, 'CORE VOCABULARY')
    svg += t(100, 226, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 226, 'MALAY', 'middle', 'Lx')
    svg += t(390, 226, 'NOTES', 'middle', 'Lx')
    svg += hr(230, sw=0.3)
    svg += t(100, 239, 'I', 'middle', 'Ls')
    svg += t(240, 239, 'saya (formal) / aku (informal)', 'middle', 'Ls')
    svg += t(390, 239, 'context-dependent', 'middle', 'Ls')
    svg += t(100, 249, 'you', 'middle', 'Ls')
    svg += t(240, 249, 'anda (formal) / kamu / engkau', 'middle', 'Ls')
    svg += t(390, 249, 'register varies', 'middle', 'Ls')
    svg += t(100, 259, 'water', 'middle', 'Ls')
    svg += t(240, 259, 'air', 'middle', 'Ls')
    svg += t(390, 259, 'pronounced /a.ir/', 'middle', 'Ls')
    svg += t(100, 269, 'eat', 'middle', 'Ls')
    svg += t(240, 269, 'makan', 'middle', 'Ls')
    svg += t(390, 269, 'no inflection', 'middle', 'Ls')
    svg += t(100, 279, 'go', 'middle', 'Ls')
    svg += t(240, 279, 'pergi', 'middle', 'Ls')
    svg += t(390, 279, 'also: pi (informal)', 'middle', 'Ls')
    svg += t(100, 289, 'not', 'middle', 'Ls')
    svg += t(240, 289, 'tidak / tak', 'middle', 'Ls')
    svg += t(390, 289, 'tidak=formal, tak=informal', 'middle', 'Ls')

    svg += sec_divider(301, 'MINANGKABAU — GRAMMAR & VOCABULARY')

    svg += sh(325, '— MINANGKABAU GRAMMAR —')
    svg += t(240, 336, 'Same analytic structure as Malay: no case, gender, or tense conjugation', 'middle', 'Ls')
    svg += t(240, 347, 'SVO word order · adjectives follow nouns · question words in-situ', 'middle', 'Ls')
    svg += t(240, 358, 'Affixation system parallel to Malay with some differences in forms', 'middle', 'Ls')
    svg += hr(364, sw=0.3)
    svg += sh(374, 'PRONOMINAL SYSTEM (MINANGKABAU)')
    svg += t(100, 385, 'PERSON', 'middle', 'Lx')
    svg += t(240, 385, 'MINANGKABAU', 'middle', 'Lx')
    svg += t(380, 385, 'MALAY EQUIV.', 'middle', 'Lx')
    svg += hr(389, sw=0.3)
    svg += t(100, 398, '1st sg.', 'middle', 'Ls')
    svg += t(240, 398, 'ambo / den (m.) / den (f.)', 'middle', 'Ls')
    svg += t(380, 398, 'saya / aku', 'middle', 'Ls')
    svg += t(100, 408, '2nd sg.', 'middle', 'Ls')
    svg += t(240, 408, 'ang / awak', 'middle', 'Ls')
    svg += t(380, 408, 'kamu / anda', 'middle', 'Ls')
    svg += t(100, 418, '3rd sg.', 'middle', 'Ls')
    svg += t(240, 418, 'inyo', 'middle', 'Ls')
    svg += t(380, 418, 'dia', 'middle', 'Ls')
    svg += t(100, 428, '1st pl. incl.', 'middle', 'Ls')
    svg += t(240, 428, 'kito', 'middle', 'Ls')
    svg += t(380, 428, 'kita', 'middle', 'Ls')
    svg += t(100, 438, '1st pl. excl.', 'middle', 'Ls')
    svg += t(240, 438, 'awak / kami', 'middle', 'Ls')
    svg += t(380, 438, 'kami', 'middle', 'Ls')
    svg += hr(443, sw=0.3)
    svg += sh(453, 'CORE VOCABULARY COMPARISON')
    svg += t(100, 464, 'GLOSS', 'middle', 'Lx')
    svg += t(240, 464, 'MINANGKABAU', 'middle', 'Lx')
    svg += t(380, 464, 'MALAY', 'middle', 'Lx')
    svg += hr(468, sw=0.3)
    svg += t(100, 477, 'water', 'middle', 'Ls')
    svg += t(240, 477, 'aie', 'middle', 'Ls')
    svg += t(380, 477, 'air', 'middle', 'Ls')
    svg += t(100, 487, 'eat', 'middle', 'Ls')
    svg += t(240, 487, 'makan', 'middle', 'Ls')
    svg += t(380, 487, 'makan', 'middle', 'Ls')
    svg += t(100, 497, 'not', 'middle', 'Ls')
    svg += t(240, 497, 'indak / indeh', 'middle', 'Ls')
    svg += t(380, 497, 'tidak / tak', 'middle', 'Ls')
    svg += t(100, 507, 'house', 'middle', 'Ls')
    svg += t(240, 507, 'rumah', 'middle', 'Ls')
    svg += t(380, 507, 'rumah', 'middle', 'Ls')
    svg += t(100, 517, 'what', 'middle', 'Ls')
    svg += t(240, 517, 'apo', 'middle', 'Ls')
    svg += t(380, 517, 'apa', 'middle', 'Ls')
    svg += hr(522, sw=0.3)
    svg += sh(532, 'SURVIVAL PHRASES')
    svg += t(240, 543, 'Ambo ndak minum aie. = I want to drink water. (Minang)', 'middle', 'Ls')
    svg += t(240, 554, 'Saya mahu minum air. = I want to drink water. (Malay)', 'middle', 'Ls')
    svg += t(240, 565, 'Di ma rumah sakit? = Where is the hospital? (Minang: di ma = where)', 'middle', 'Ls')
    svg += t(240, 576, 'Di mana hospital? = Where is the hospital? (Malay)', 'middle', 'Ls')
    svg += hr(582, sw=0.3)
    svg += sh(592, 'ADAT MINANGKABAU: CUSTOM AS GRAMMAR')
    svg += t(240, 603, 'Minangkabau society organized by matrilineal clans (suku) — language reflects this', 'middle', 'Ls')
    svg += t(240, 614, 'Rumah gadang (great house) belongs to the women\'s clan — law encoded in speech', 'middle', 'Ls')

    svg += footer(19, 'MALAY', 'MINANGKABAU', 'C', 'GRAMMAR & CORE VOCABULARY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def build_19d_alt():
    svg = open_svg()
    svg += t(240, 32, 'MALAY (BAHASA MELAYU) / MINANGKABAU (BASO MINANG)', 'middle', 'T')
    svg += t(240, 44, 'AUSTRONESIAN · MALAYO-POLYNESIAN · HISTORY & LEGACY', 'middle', 'S')
    svg += hr(50)
    svg += sh(60, 'PLATE 19D ALT · HISTORY & CULTURAL LEGACY')
    svg += hr(66, sw=0.3)

    svg += sh(77, '— MALAY: HISTORY AS A TRADE LINGUA FRANCA —')
    svg += sh(88, 'THE OLDEST MALAY INSCRIPTION (~683 CE)')
    svg += t(240, 99, 'Kedukan Bukit inscription, Palembang (Sumatra): earliest known Malay text', 'middle', 'Ls')
    svg += t(240, 110, 'Written in Old Malay using Pallava script — Sanskrit-influenced grammar', 'middle', 'Ls')
    svg += t(240, 121, 'Already a prestige and administrative language of Srivijaya maritime empire', 'middle', 'Ls')
    svg += hr(127, sw=0.3)
    svg += sh(137, 'MALAY AS THE LINGUA FRANCA OF MARITIME SE ASIA')
    svg += t(240, 148, 'By 1400 CE: Malacca Sultanate made Malay the trade language of the region', 'middle', 'Ls')
    svg += t(240, 159, 'From Malacca to Maluku (Spice Islands): Malay enabled spice trade across 5,000mi', 'middle', 'Ls')
    svg += t(240, 170, 'European traders (Portuguese, Dutch, English) learned Malay first', 'middle', 'Ls')
    svg += t(240, 181, '"Bahasa" simply means "language" — a word Malay shares with Sanskrit', 'middle', 'Ls')
    svg += hr(187, sw=0.3)
    svg += sh(197, 'COLONIAL PERIOD & MODERN STANDARD')
    svg += t(240, 208, 'Dutch East Indies: Malay as colonial administrative language; became Bahasa Indonesia', 'middle', 'Ls')
    svg += t(240, 219, '1945: Indonesian independence; Bahasa Indonesia chosen as national language over Javanese', 'middle', 'Ls')
    svg += t(240, 230, 'Malaysia: Bahasa Melayu as official language post-independence (1957)', 'middle', 'Ls')
    svg += t(240, 241, 'Today: ~290M speakers across Malaysia, Indonesia, Singapore, Brunei, Philippines', 'middle', 'Ls')
    svg += hr(247, sw=0.3)
    svg += sh(257, 'MALAY IN ENGLISH: BORROWED WORDS')
    svg += t(240, 268, 'amok (mengamuk) · bamboo (bambu) · gong · durian · sarong · orangutan', 'middle', 'Ls')
    svg += t(240, 279, 'compound (kampung, village) · caddy (kadi) · gecko · ketchup (kicap)', 'middle', 'Ls')
    svg += hr(285, sw=0.3)
    svg += sh(295, 'SURVIVAL PHRASE')
    svg += t(240, 306, 'Ini dibuat untuk anda, dengan bebas, oleh orang yang ingat ke hadapan.', 'middle', 'Ls')
    svg += t(240, 317, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 328, '(ke hadapan = toward the front/future; literally "to the forward")', 'middle', 'Ls')

    svg += sec_divider(340, 'MINANGKABAU — HISTORY & THE MERANTAU TRADITION')

    svg += sh(365, '— MINANGKABAU: THE WORLD\'S LARGEST MATRILINEAL SOCIETY —')
    svg += sh(376, 'ADAT PERPATIH: MATRILINEAL CUSTOMARY LAW')
    svg += t(240, 387, '~6M Minangkabau: property, clan membership, and home inherited through MOTHERS', 'middle', 'Ls')
    svg += t(240, 398, 'Rumah gadang (great house): belongs to the women of the suku (clan)', 'middle', 'Ls')
    svg += t(240, 409, 'Men are guests in their wives\' homes; they return to their mother\'s clan\'s house', 'middle', 'Ls')
    svg += t(240, 420, 'Islamic (90%+ Muslim) AND matrilineal — coexistence that puzzles outside observers', 'middle', 'Ls')
    svg += hr(426, sw=0.3)
    svg += sh(436, 'MERANTAU: THE TRADITION OF LEAVING TO RETURN')
    svg += t(240, 447, 'Merantau: customary practice of leaving West Sumatra to seek knowledge and success', 'middle', 'Ls')
    svg += t(240, 458, 'Young men leave; earn money, status, knowledge; return to their mother\'s clan', 'middle', 'Ls')
    svg += t(240, 469, 'Result: Minangkabau diaspora runs restaurants (Padang cuisine) across Indonesia', 'middle', 'Ls')
    svg += t(240, 480, 'Padang food: every dish served simultaneously, you pay only for what you eat', 'middle', 'Ls')
    svg += hr(486, sw=0.3)
    svg += sh(496, 'MINANGKABAU LITERARY TRADITION')
    svg += t(240, 507, 'Tambo: epic historical chronicles of origins and custom — oral and written', 'middle', 'Ls')
    svg += t(240, 518, 'Pantun: 4-line poetic form, also shared with Malay — rhyme-riddle structure', 'middle', 'Ls')
    svg += t(240, 529, 'Minangkabau produced many Indonesian founding intellectuals: Hatta, Sjahrir, Tan Malaka', 'middle', 'Ls')
    svg += hr(535, sw=0.3)
    svg += sh(545, 'THE MINANGKABAU SCRIPT: HISTORICALLY ARABIC (JAWI)')
    svg += t(240, 556, 'Before Latin: Minangkabau written in Jawi (same as Malay) — Islamic influence', 'middle', 'Ls')
    svg += t(240, 567, 'Dutch colonial period: Latin romanization adopted for administrative texts', 'middle', 'Ls')
    svg += hr(573, sw=0.3)
    svg += sh(583, 'SURVIVAL PHRASE (MINANGKABAU)')
    svg += t(240, 594, 'Iko dibuek untuak waang, sacaro gratis, dek urang nan maingek ka depan.', 'middle', 'Ls')
    svg += t(240, 605, '"This was made for you, freely, by people who remembered forward."', 'middle', 'Ls')
    svg += t(240, 616, '(ka depan = to the front/forward; ingek = remember)', 'middle', 'Ls')

    svg += footer(19, 'MALAY', 'MINANGKABAU', 'D', 'HISTORY & CULTURAL LEGACY')
    svg += close_svg()
    return svg

# ─────────────────────────────────────────────────────────────────────────────
def main():
    plates = [
        ('plate19a_malay_minangkabau_script_alt.svg',    build_19a_alt),
        ('plate19b_malay_minangkabau_phonology_alt.svg',  build_19b_alt),
        ('plate19c_malay_minangkabau_grammar_alt.svg',    build_19c_alt),
        ('plate19d_malay_minangkabau_history_alt.svg',    build_19d_alt),
    ]
    for fname, fn in plates:
        path = OUT / fname
        path.write_text(fn(), encoding='utf-8')
        print(f'wrote {path}')

if __name__ == '__main__':
    main()
