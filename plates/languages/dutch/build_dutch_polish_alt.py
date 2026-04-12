#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Dutch / Polish alt plate series 49A–49D for Remember Forward.
Secondary language: Polish — within ~450mi of Amsterdam (Poland's western border).
Dutch: Germanic, 23M speakers. Polish: West Slavic, ~45M speakers.
"""
from pathlib import Path
OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text{font-family:Georgia,serif;}\n'
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
def t(x,y,s,a='middle',c='L'): return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'
def hr(y,x1=20,x2=460,sw=0.3): return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y,txt): return t(240,y,f'\u2014 {txt} \u2014','middle','H')
def sec_divider(y,label):
    return (hr(y,sw=1.5)
        + f'<rect x="20" y="{y+3}" width="440" height="14" fill="black"/>\n'
        + f'<text x="240" y="{y+13}" text-anchor="middle" class="Hb" fill="white">{esc(label)}</text>\n'
        + hr(y+17,sw=0.3))
def footer(num,l1,l2,letter,desc):
    return (hr(625)
        + t(240,620,f'PLATE {num}{letter} ALT \u00b7 {l1} / {l2} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        + hr(633)
        + t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        + t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))


# ─── PLATE 49A ALT — SCRIPT ───────────────────────────────────────────────────

def build_49a_alt():
    g = open_svg()
    g += t(240,30,'DUTCH + POLISH \u2014 SCRIPT \u00b7 WRITING SYSTEMS','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 49A \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: DUTCH SCRIPT
    g += sh(63,'DUTCH \u2014 LATIN ALPHABET + DIGRAPHS')
    g += t(240,73,'Dutch uses 26 standard Latin letters. The digraph ij (also written \u0133) functions as a single letter.','middle','Ls')
    g += t(240,82,'Special vowel combinations: aa, ee, oo, uu (long vowels) \u00b7 ie (like "ee") \u00b7 oe (like "oo" in "moon").','middle','Lx')
    g += t(240,91,'Dutch orthography is largely phonemic: spelling reliably predicts pronunciation.','middle','Lx')
    g += hr(99)

    g += sh(107,'DUTCH \u2014 KEY LETTER-SOUND RULES')
    rules = [('g / ch','/\u0263/ or /x/','voiced / voiceless velar fricative \u2014 "guttural g"'),
             ('v / w','/v/ and /\u028b/','v = voiced labiodental \u00b7 w = labiodental approximant'),
             ('ij / ei','/\u025b\u026a/','diphthong \u2014 like English "ay" in "day"'),
             ('ui','/\u0153y/','diphthong \u2014 no close English equivalent: like rounded "oy"'),
             ('ou / au','/\u0251u/','diphthong \u2014 like English "ow" in "cow"'),
             ('oe','/u/','like "oo" in moon'),
             ('eu','/\u00f8/','front rounded vowel \u2014 like French "eu"'),
             ('tj','/c/','palatal affricate, as in "tjilpen" (to chirp)'),]
    for i,(let,ipa,note) in enumerate(rules):
        y = 116 + i*10
        g += t(55,y,let,'middle','Ls'); g += t(120,y,ipa,'middle','Lx'); g += t(330,y,note,'middle','Lx')
    g += hr(204)

    g += sh(212,'DUTCH ALPHABET \u2014 26 LETTERS + KEY DIGRAPH IJ')
    g += t(240,222,'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z \u2014 plus IJ as 27th letter in dictionaries.','middle','Ls')
    g += t(240,231,'In alphabetization, IJ sorts after Y. Dutch children learn to capitalize IJ together: IJsberg (iceberg).','middle','Lx')

    # DIVIDER
    g += sec_divider(242,'POLISH (J\u0118ZYK POLSKI) \u00b7 SCRIPT \u00b7 LATIN + DIACRITICS')

    # SECONDARY: POLISH SCRIPT
    g += t(240,274,'Polish uses the Latin alphabet with diacritics: 32 letters. No q, v, x (only in foreign words).','middle','Ls')
    g += t(240,283,'Added letters: \u0105 \u0107 \u0119 \u0142 \u0144 \u00f3 \u015b \u017a \u017c \u2014 each marks a distinct sound not in basic Latin.','middle','Ls')
    g += hr(290)

    g += sh(298,'POLISH SPECIAL LETTERS \u2014 ALL 9')
    polish_spec = [('\u0105','/\u00f5/','nasal a \u2014 like French "an" \u2014 no English equivalent'),
                   ('\u0107','/t\u0255/','palatal affricate \u2014 soft "ch" sound'),
                   ('\u0119','/\u0259/ or /\u1ebd/','nasal e \u2014 like French "in"'),
                   ('\u0142','/w/','crossed l \u2014 sounds like English "w"'),
                   ('\u0144','/\u0272/','palatal nasal \u2014 like Spanish \u00f1 or Italian "gn"'),
                   ('\u00f3','/u/','same as u \u2014 historical o that shifted to /u/ sound'),
                   ('\u015b','/\u0255/','palatal sibilant \u2014 soft "sh" sound'),
                   ('\u017a','/\u0291/','palatal voiced sibilant \u2014 soft "zh" sound'),
                   ('\u017c','/\u0292/','"zed with dot" \u2014 retroflex "zh" \u2014 harder than \u017a')]
    for i,(ltr,ipa,note) in enumerate(polish_spec):
        y = 307 + i*10
        g += t(35,y,ltr,'middle','L'); g += t(75,y,ipa,'middle','Lx'); g += t(300,y,note,'middle','Lx')
    g += hr(403)

    g += sh(411,'POLISH \u2014 DIGRAPHS AND CLUSTERS')
    g += t(240,421,'cz = /t\u0283/ \u00b7 sz = /\u0283/ \u00b7 ch = /x/ \u00b7 rz = /\u0292/ \u00b7 dz = /dz/ \u00b7 d\u017a = /d\u0291/ \u00b7 d\u017c = /d\u0292/','middle','Ls')
    g += t(240,430,'Polish allows long consonant clusters: szcz = /\u0283t\u0283/ \u00b7 prz = /p\u0282/ \u00b7 strz = /st\u0282/','middle','Lx')
    g += t(240,439,'Example: "Chrz\u0105szcz" (beetle) = /xf\u00f5\u0283t\u0283/ \u2014 one of Polish\u2019s famously dense words.','middle','Lx')
    g += hr(447)

    g += sh(455,'SCRIPT BRIDGE \u2014 SAME WORDS, DUTCH VS. POLISH')
    bridge = [('water','water','woda'),('fire','vuur','ogie\u0144'),('earth','aarde','ziemia'),
               ('person','mens','cz\u0142owiek'),('freedom','vrijheid','wolno\u015b\u0107')]
    for lbl,x in zip(['English','Dutch','Polish'],[100,240,370]):
        g += t(x,465,lbl,'middle','Lx')
    g += hr(469,sw=0.2)
    for i,(en,nl,pl) in enumerate(bridge):
        y = 478 + i*10
        g += t(100,y,en,'middle','Lx'); g += t(240,y,nl,'middle','Ls'); g += t(370,y,pl,'middle','Ls')

    g += footer('49','DUTCH','POLISH','A','Script')
    return g + close_svg()


# ─── PLATE 49B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_49b_alt():
    g = open_svg()
    g += t(240,30,'DUTCH + POLISH \u2014 PHONOLOGY \u00b7 SOUND SYSTEMS','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 49B \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: DUTCH PHONOLOGY
    g += sh(63,'DUTCH \u2014 VOWEL SYSTEM')
    g += t(240,73,'Dutch has one of the largest vowel inventories in Europe: 13+ monophthongs + diphthongs.','middle','Ls')
    vowels = [('/i/','ie','like "ee" in "feet"'),('/y/','uu','like French "u" \u2014 front rounded'),
               ('/u/','oe','like "oo" in "moon"'),('/e/','ee','like "ay" in "day" but monophthong'),
               ('/\u00f8/','eu','like French "eu" \u2014 mid front rounded'),('/o/','oo','like "o" in "no"'),
               ('/a/','a','short: like "a" in "cat"'),('/a:/','aa','long: like "a" in "father"'),
               ('/\u025b\u026a/','ij / ei','diphthong: like "ay" in "day"'),('/\u0153y/','ui','diphthong: no English equivalent'),
               ('/\u0251u/','ou / au','diphthong: like "ow" in "cow"')]
    for i,(ipa,spl,note) in enumerate(vowels):
        y = 82 + i*10
        g += t(55,y,ipa,'middle','Lx'); g += t(115,y,spl,'middle','Ls'); g += t(310,y,note,'middle','Lx')
    g += hr(196)

    g += sh(204,'DUTCH \u2014 GUTTURAL G \u00b7 KEY CONSONANTS')
    g += t(240,214,'The Dutch g/ch: velar/uvular fricative. Most distinctive feature for foreign listeners.','middle','Ls')
    g += t(240,223,'Southern Dutch: voiced /\u0263/ \u00b7 Northern Dutch: voiceless /x/. Both written as g or ch.','middle','Lx')
    g += t(240,232,'v and f: in final position, v \u2192 f (devoicing). leven /\u02c8le.v\u0259n/ \u2192 leef /le:f/ (life \u2192 live).','middle','Lx')

    # DIVIDER
    g += sec_divider(243,'POLISH (J\u0118ZYK POLSKI) \u00b7 PHONOLOGY \u00b7 SOUND SYSTEM')

    # SECONDARY: POLISH PHONOLOGY
    g += t(240,275,'Polish phonology: extensive consonant system, nasal vowels, palatal series, fixed stress.','middle','Ls')
    g += hr(282)

    g += sh(290,'POLISH \u2014 VOWELS (6 ORAL + 2 NASAL)')
    g += t(240,300,'Oral: /a/ /e/ /i/ /o/ /u/ (written u or \u00f3) /\u0268/ (written y)','middle','Ls')
    g += t(240,309,'Nasal: /\u00f5/ (written \u0105) \u00b7 /\u1ebd/ (written \u0119) \u2014 nasality weakens before fricatives, disappears word-finally.','middle','Lx')
    g += t(240,318,'y (/\u0268/): central unrounded \u2014 like Russian \u044b. No English equivalent. Common in Polish.','middle','Lx')
    g += hr(325)

    g += sh(333,'POLISH \u2014 PALATAL CONSONANT SERIES')
    palatals = [('/t\u0255/ \u0107','soft-ch: like "ch" in "cheap" but softer'),
                ('/d\u0291/ d\u017a','soft-dzh: voiced palatal affricate'),
                ('/\u0272/ \u0144','palatal nasal: like "ny" in "canyon"'),
                ('/\u0255/ \u015b','palatal sibilant: soft "sh"'),
                ('/\u0291/ \u017a','palatal voiced sibilant: soft "zh"'),
                ('/j/ j','palatal glide: like y in "yes"')]
    for i,(sym,note) in enumerate(palatals):
        y = 342 + i*10
        g += t(80,y,sym,'middle','Ls'); g += t(310,y,note,'middle','Lx')
    g += hr(408)

    g += sh(416,'STRESS \u00b7 RHYTHM')
    g += t(240,426,'Dutch: variable stress, penultimate default. Tonal distinctions in some dialects (Limburg).','middle','Ls')
    g += t(240,435,'Polish: fixed stress on penultimate syllable (second-to-last). Very regular.','middle','Ls')
    g += t(240,444,'Polish rhythm: consonant-heavy syllable structure. Up to 4 initial consonants: spr-, strz-.','middle','Lx')
    g += hr(452)

    g += sh(460,'COMPARATIVE NOTE \u2014 DUTCH / POLISH')
    g += t(240,470,'Both: Latin script, ~same geographic neighborhood (500mi), no lexical tone.','middle','Ls')
    g += t(240,479,'Dutch: large vowel inventory, guttural fricatives, SVO. Germanic.','middle','Ls')
    g += t(240,488,'Polish: nasal vowels, rich palatals, free word order (inflected), fixed stress. Slavic.','middle','Ls')
    g += t(240,497,'Shared words via Latin: biblioteka/bibliotheek (library) \u00b7 muzeum/museum \u00b7 telefon/telefoon.','middle','Lx')

    g += footer('49','DUTCH','POLISH','B','Phonology')
    return g + close_svg()


# ─── PLATE 49C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_49c_alt():
    g = open_svg()
    g += t(240,30,'DUTCH + POLISH \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 49C \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: DUTCH GRAMMAR
    g += sh(63,'DUTCH \u2014 SVO \u00b7 TWO GENDERS \u00b7 V2 RULE')
    g += t(240,73,'Word order: SVO. V2 rule: verb always second when clause begins with non-subject.','middle','Ls')
    g += t(240,82,'"Ik ga morgen" (I go tomorrow) \u2192 "Morgen ga ik" (Tomorrow go I). Verb stays 2nd.','middle','Lx')
    g += t(240,91,'Two grammatical genders: de (common, m+f merged) and het (neuter). ~3/4 nouns take de.','middle','Lx')
    g += hr(99)

    g += sh(107,'DUTCH VERB \u2014 SCHRIJVEN "TO WRITE"')
    nl_conj = [('ik schrijf','I write'),('jij schrijft','you write'),('hij/zij schrijft','he/she writes'),
               ('wij schrijven','we write'),('jullie schrijven','you (pl) write'),('zij schrijven','they write')]
    for i,(form,gl) in enumerate(nl_conj):
        y = 116 + i*10
        g += t(150,y,form,'middle','Ls'); g += t(340,y,gl,'middle','Lx')
    g += hr(181)

    g += sh(189,'DUTCH CORE VOCABULARY \u2014 20 WORDS')
    nl_vocab = [('water','water'),('vuur','fire'),('aarde','earth'),('mens','person'),('maan','moon'),
                ('zon','sun'),('ja','yes'),('nee','no'),('ik','I'),('jij','you'),
                ('liefde','love'),('vrijheid','freedom'),('toekomst','future'),('wereld','world'),('goed','good'),
                ('dood','death'),('leven','life'),('dank','thanks'),('wanneer','when'),('waar','where')]
    for i,(nl,en) in enumerate(nl_vocab):
        col = i//10; row = i%10
        y = 198 + row*10
        x0 = 30 + col*240
        g += t(x0,y,nl,'start','Ls'); g += t(x0+100,y,en,'start','Lx')
    g += hr(304)

    # DIVIDER
    g += sec_divider(312,'POLISH (J\u0118ZYK POLSKI) \u00b7 GRAMMAR \u00b7 VOCABULARY')

    # SECONDARY: POLISH GRAMMAR
    g += t(240,344,'Polish is highly inflected: 7 cases, 3 genders, 2 numbers. Word order is flexible because case marks roles.','middle','Ls')
    g += t(240,353,'"Pies gryzie kota" = "Kot\u0119 gryzie pies" = "The dog bites the cat." \u2014 same meaning, different emphasis.','middle','Lx')
    g += hr(360)

    g += sh(368,'POLISH NOUN CASES \u2014 7 CASES')
    cases = [('Nominative (who/what)','cz\u0142owiek','the person (subject)'),
             ('Genitive (of/from)','cz\u0142owieka','of the person'),
             ('Dative (to/for)','cz\u0142owiekowi','to the person'),
             ('Accusative (direct obj.)','cz\u0142owieka','the person (object)'),
             ('Instrumental (by/with)','cz\u0142owiekiem','by/with the person'),
             ('Locative (in/on/about)','cz\u0142owieku','about/in the person'),
             ('Vocative (address)','cz\u0142owieku!','O person! (calling)')]
    for i,(case,form,gl) in enumerate(cases):
        y = 377 + i*10
        g += t(60,y,case,'start','Lx'); g += t(250,y,form,'middle','Ls'); g += t(400,y,gl,'start','Lx')
    g += hr(452)

    g += sh(460,'POLISH CORE VOCABULARY \u2014 20 WORDS')
    pl_vocab = [('woda','water'),('ogie\u0144','fire'),('ziemia','earth'),('cz\u0142owiek','person'),('ksi\u0119\u017cyc','moon'),
                ('s\u0142o\u0144ce','sun'),('tak','yes'),('nie','no'),('ja','I'),('ty','you'),
                ('mi\u0142o\u015b\u0107','love'),('wolno\u015b\u0107','freedom'),('przysz\u0142o\u015b\u0107','future'),('\u015bwiat','world'),('dobry','good'),
                ('\u015bmier\u0107','death'),('\u017cycie','life'),('dzi\u0119kuj\u0119','thanks'),('kiedy','when'),('gdzie','where')]
    for i,(pl,en) in enumerate(pl_vocab):
        col = i//10; row = i%10
        y = 469 + row*10
        x0 = 30 + col*240
        g += t(x0,y,pl,'start','Ls'); g += t(x0+120,y,en,'start','Lx')

    g += footer('49','DUTCH','POLISH','C','Grammar')
    return g + close_svg()


# ─── PLATE 49D ALT — RUNNING TEXT ────────────────────────────────────────────

def build_49d_alt():
    g = open_svg()
    g += t(240,30,'DUTCH + POLISH \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 49D \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: DUTCH TEXT
    g += sh(63,'DUTCH \u2014 PASSAGE 1 \u00b7 SPINOZA')
    g += t(240,73,'"De vrijheid is de erkenning van de noodzakelijkheid."','middle','L')
    g += t(240,83,'"Freedom is the recognition of necessity." \u2014 Baruch Spinoza (Amsterdam, 1677).','middle','Ls')
    g += hr(91)

    g += sh(99,'DUTCH \u2014 PASSAGE 2 \u00b7 PROVERB')
    g += t(240,109,'"Oost west, thuis best."','middle','L')
    g += t(240,119,'East  west,  home  best.','middle','Lx')
    g += t(240,128,'"East or west, home is best." \u2014 Universal human longing; Dutch phrase ~16th century.','middle','Ls')
    g += hr(136)

    g += sh(144,'DUTCH \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g += t(240,154,'Dit werd voor jou gemaakt, gratis, door mensen die vooruit hebben gedacht.','middle','L')
    g += t(240,164,'This  was-made  for you,  freely,  by  people  who  forward  have  thought.','middle','Lx')
    g += t(240,173,'"This was made for you, freely, by people who thought forward."','middle','Ls')
    g += hr(181)

    g += sh(189,'LANGUAGE NOTE \u2014 "FORWARD" IN DUTCH')
    g += t(240,199,'vooruit: "forward" \u2014 lit. "before-out." Voor (before/in front) + uit (out). Directional prefix.','middle','Ls')
    g += t(240,208,'toekomst: "future" \u2014 lit. "to-come." Toe (to/toward) + komst (coming). The future approaches.','middle','Lx')
    g += t(240,217,'Dutch toekomst and English "to come" share Germanic root. The future is what comes toward you.','middle','Lx')

    # DIVIDER
    g += sec_divider(228,'POLISH (J\u0118ZYK POLSKI) \u00b7 RUNNING TEXT \u00b7 PASSAGES')

    # SECONDARY: POLISH TEXT
    g += sh(259,'POLISH \u2014 PASSAGE 1 \u00b7 CHOPIN / PROVERB')
    g += t(240,269,'"Czego si\u0119 nie robi, tego si\u0119 nie ma."','middle','L')
    g += t(240,279,'What  self  not  does,  that  self  not  has.','middle','Lx')
    g += t(240,288,'"What you don\'t do, you don\'t have." \u2014 Polish proverb. Act to achieve.','middle','Ls')
    g += hr(296)

    g += sh(304,'POLISH \u2014 PASSAGE 2 \u00b7 WISŁAWA SZYMBORSKA')
    g += t(240,314,'"Ka\u017cdy pocz\u0105tek to tylko ci\u0105g dal\u2026"','middle','L')
    g += t(240,324,'"Every beginning is only a continuation\u2026"','middle','Ls')
    g += t(240,333,'\u2014 Wis\u0142awa Szymborska, Nobel Lecture, 1996.','middle','Lx')
    g += hr(341)

    g += sh(349,'POLISH \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g += t(240,360,'To zosta\u0142o stworzone dla ciebie, bezp\u0142atnie, przez ludzi, kt\u00f3rzy pami\u0119tali o przysz\u0142o\u015bci.','middle','L')
    g += t(240,371,'This  was-created  for  you,  freely,  by  people  who  remembered  about  future.','middle','Lx')
    g += t(240,380,'"This was made for you, freely, by people who remembered the future."','middle','Ls')
    g += hr(388)

    g += sh(396,'LANGUAGE NOTE \u2014 "FUTURE" IN POLISH')
    g += t(240,406,'przysz\u0142o\u015b\u0107: "future" \u2014 from przyj\u015b\u0107 (to come/arrive) + abstract suffix. Lit. "that which will arrive."','middle','Ls')
    g += t(240,415,'naprz\u00f3d: "forward" \u2014 directional. Na (on/to) + prz\u00f3d (front). Common in commands: Id\u017a naprz\u00f3d! (Go forward!).','middle','Lx')
    g += t(240,424,'pami\u0119tali: "they remembered" \u2014 from pami\u0119ta\u0107 (to remember/to keep in mind).','middle','Lx')
    g += t(240,433,'Polish carries memory in its very word for care: pami\u0119\u0107 (memory) shares root with pami\u0119ta\u0107 (to remember).','middle','Lx')
    g += hr(441)

    g += sh(449,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g += t(240,459,'Dutch: ~23M speakers, Netherlands and Belgium. Germanic language closely related to German and English.','middle','Ls')
    g += t(240,468,'Polish: ~45M speakers, Poland + diaspora. West Slavic; closely related to Czech, Slovak, Sorbian.','middle','Ls')
    g += t(240,477,'Geographic link: Amsterdam to Warsaw ~1,100km. Within 500mi radius of Amsterdam, Poland\u2019s western edge.','middle','Ls')
    g += t(240,486,'Both languages use Latin script. Dutch: 26 + ij. Polish: 32 letters including 9 diacritic letters.','middle','Lx')
    g += t(240,495,'See plates 49A\u201349C for full scripts, phonology, and grammar of Dutch.','middle','Lx')

    g += footer('49','DUTCH','POLISH','D','Text')
    return g + close_svg()


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate49a_dutch_polish_script_alt.svg':    build_49a_alt(),
        'plate49b_dutch_polish_phonology_alt.svg': build_49b_alt(),
        'plate49c_dutch_polish_grammar_alt.svg':   build_49c_alt(),
        'plate49d_dutch_polish_text_alt.svg':      build_49d_alt(),
    }
    for fname,content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
