#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Arabic / Greek alt plate series 13A–13D for Remember Forward.
Secondary language: Greek — within ~450mi of Cairo (Crete, mainland Greece).
Arabic: RTL abjad, 28 letters. Greek: LTR alphabet, 24 letters.
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
        '  .La{font-size:14px} .Lam{font-size:11px} .Las{font-size:9px}\n'
        '  .Lg{font-size:12px}\n'
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
def sec_divider(y, label):
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


# ─── PLATE 13A ALT — SCRIPT ───────────────────────────────────────────────────

def build_13a_alt():
    g = open_svg()
    g += t(240,30,'ARABIC + GREEK \u2014 SCRIPT \u00b7 WRITING SYSTEMS','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 13A \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: ARABIC
    g += sh(63,'ARABIC \u2014 ABJAD \u00b7 28 LETTERS \u00b7 RIGHT TO LEFT')
    g += t(240,73,'Consonant-only script. Vowels marked optionally with harakat (diacritics). 4 positional forms per letter.','middle','Ls')
    g += t(240,82,'Cursive: letters join. 22 letters connect on both sides; 6 connect only on right (break word).','middle','Lx')
    g += hr(89)
    g += sh(97,'THE 28 ARABIC LETTERS \u2014 ISOLATED FORM (READ RIGHT TO LEFT)')
    # 4 rows of 7 letters
    letters = [
        # (glyph, name, ipa)
        ('\u0627','Alif','\u0101/\u02c0'),('\u0628','Ba','/b/'),('\u062a','Ta','/t/'),
        ('\u062b','Tha','/\u03b8/'),('\u062c','Jim','/d\u0292/'),('\u062d','Ha','/\u1e25/'),('\u062e','Kha','/x/'),
        ('\u062f','Dal','/d/'),('\u0630','Dhal','/\u00f0/'),('\u0631','Ra','/r/'),
        ('\u0632','Zay','/z/'),('\u0633','Sin','/s/'),('\u0634','Shin','/\u0283/'),('\u0635','Sad','/s\u02e4/'),
        ('\u0636','Dad','/d\u02e4/'),('\u0637','Tta','/t\u02e4/'),('\u0638','Dha','/\u00f0\u02e4/'),
        ('\u0639','Ayn','/\u02bf/'),('\u063a','Ghayn','/\u0263/'),('\u0641','Fa','/f/'),('\u0642','Qaf','/q/'),
        ('\u0643','Kaf','/k/'),('\u0644','Lam','/l/'),('\u0645','Mim','/m/'),('\u0646','Nun','/n/'),
        ('\u0647','Ha','/h/'),('\u0648','Waw','/w/\u016b'),('\u064a','Ya','/j/\u012b'),
    ]
    xs = [40,100,160,220,280,340,400]
    for i,( glyph,name,ipa) in enumerate(letters):
        row = i//7; col = i%7
        y_g = 110 + row*28; y_n = y_g+12; y_i = y_g+20
        g += t(xs[col],y_g,glyph,'middle','La')
        g += t(xs[col],y_n,name,'middle','Lx')
        g += t(xs[col],y_i,ipa,'middle','Lx')
    g += hr(228)

    g += sh(236,'HARAKAT \u2014 OPTIONAL VOWEL MARKS')
    g += t(240,246,'Fat\u1e25a (\u064e) = /a/ \u00b7 Kasra (\u064f) = /i/ \u00b7 \u1e8camma (\u064f) = /u/ \u00b7 Sukun = no vowel','middle','Ls')
    g += t(240,255,'Long vowels: \u0627 Alif = /\u0101/ \u00b7 \u064a Ya = /\u012b/ \u00b7 \u0648 Waw = /\u016b/. Script reads right to left.','middle','Lx')
    g += t(240,264,'The Quran preserves Classical Arabic exactly as recited in 650 CE \u2014 the standard reference for script.','middle','Lx')

    # DIVIDER
    g += sec_divider(276,'GREEK (ELLINIK\u0391) \u00b7 SCRIPT \u00b7 24-LETTER ALPHABET')

    # SECONDARY: GREEK
    g += t(240,308,'Greek alphabet: 24 letters, left-to-right. Ancestor of Latin, Cyrillic, and Coptic scripts.','middle','Ls')
    g += t(240,317,'Adopted from Phoenician ~800 BCE. Greeks added vowel letters \u2014 world\u2019s first complete vowel alphabet.','middle','Lx')
    g += hr(324)
    g += sh(332,'THE 24 GREEK LETTERS \u2014 UPPER \u00b7 LOWER \u00b7 NAME \u00b7 SOUND')
    greek = [
        ('\u0391','\u03b1','Alpha','/a/'),('\u0392','\u03b2','Beta','/v/'),('\u0393','\u03b3','Gamma','/\u0263/'),('\u0394','\u03b4','Delta','/\u00f0/'),
        ('\u0395','\u03b5','Epsilon','/e/'),('\u0396','\u03b6','Zeta','/z/'),('\u0397','\u03b7','Eta','/i/'),('\u0398','\u03b8','Theta','/\u03b8/'),
        ('\u0399','\u03b9','Iota','/i/'),('\u039a','\u03ba','Kappa','/k/'),('\u039b','\u03bb','Lambda','/l/'),('\u039c','\u03bc','Mu','/m/'),
        ('\u039d','\u03bd','Nu','/n/'),('\u039e','\u03be','Xi','/ks/'),('\u039f','\u03bf','Omicron','/o/'),('\u03a0','\u03c0','Pi','/p/'),
        ('\u03a1','\u03c1','Rho','/r/'),('\u03a3','\u03c3','Sigma','/s/'),('\u03a4','\u03c4','Tau','/t/'),('\u03a5','\u03c5','Upsilon','/i/'),
        ('\u03a6','\u03c6','Phi','/f/'),('\u03a7','\u03c7','Chi','/x/'),('\u03a8','\u03c8','Psi','/ps/'),('\u03a9','\u03c9','Omega','/o/'),
    ]
    cols_g = [30,90,150,210,270,330,390,450]  # 4 cols of 6 letters
    for i,(up,lo,name,ipa) in enumerate(greek):
        col = i%4; row = i//4
        x = 60 + col*110
        y0 = 343 + row*24
        g += t(x-10,y0+1,up,'middle','Lg'); g += t(x+10,y0+1,lo,'middle','Lg')
        g += t(x,y0+12,name,'middle','Lx'); g += t(x,y0+20,ipa,'middle','Lx')
    g += hr(492)

    g += sh(500,'SCRIPT BRIDGE \u2014 ARABIC AND GREEK ROOTS IN SCIENCE')
    g += t(240,510,'Algebra: from Arabic al-jabr (\u0627\u0644\u062c\u0628\u0631) \u2014 Greek: \u03b1\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1. Arabic transmitted Greek mathematics to Europe.','middle','Lx')
    g += t(240,519,'Algorithm: from al-Khw\u0101rizm\u012b (Arabic mathematician) \u2014 Greek \u03b1\u03c1\u03b9\u03b8\u03bc\u03cc\u03c2 = arithmetic/number.','middle','Lx')
    g += t(240,528,'Chemistry: from Arabic al-k\u012bmy\u0101\u2019 \u2014 originally from Greek kh\u0113me\u012ba (pouring, fusion).','middle','Lx')
    g += t(240,537,'Both scripts shaped science: Greek gave the framework; Arabic preserved and extended it.','middle','Lx')

    g += footer('13','ARABIC','GREEK','A','Script')
    return g + close_svg()


# ─── PLATE 13B ALT — PHONOLOGY ────────────────────────────────────────────────

def build_13b_alt():
    g = open_svg()
    g += t(240,30,'ARABIC + GREEK \u2014 PHONOLOGY \u00b7 SOUND SYSTEMS','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 13B \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: ARABIC PHONOLOGY
    g += sh(63,'ARABIC \u2014 3 SHORT + 3 LONG VOWELS')
    vowels = [('/a/','/\u0101/','short/long low central'),('/i/','/\u012b/','short/long high front'),('/u/','/\u016b/','short/long high back')]
    for i,(sh_v,ln_v,d) in enumerate(vowels):
        y = 72 + i*10
        g += t(60,y,sh_v,'middle','Ls'); g += t(130,y,ln_v,'middle','Ls'); g += t(320,y,d,'middle','Lx')
    g += hr(107)

    g += sh(115,'EMPHATIC (PHARYNGEALIZED) CONSONANTS \u2014 UNIQUE ARABIC FEATURE')
    g += t(240,125,'\u0635 /s\u02e4/  \u0636 /d\u02e4/  \u0637 /t\u02e4/  \u0638 /\u00f0\u02e4/ \u2014 tongue root retracted toward pharynx while articulating','middle','Ls')
    g += t(240,134,'Emphatics affect surrounding vowels: darken the quality, lower pitch. Distinguish minimal pairs.','middle','Lx')
    g += t(240,143,'\u0635\u064e\u0628\u064e\u0631 (sabar = patience) vs. \u0633\u064e\u0628\u064e\u0631 (sabar = cactus) \u2014 emphatic \u0635 vs. plain \u0633.','middle','Lx')
    g += hr(151)

    g += sh(159,'PHARYNGEALS \u00b7 UVULARS \u00b7 GLOTTALS')
    pharyngeals = [('\u0639 /\u02bf/','pharyngeal fricative \u2014 voiced. Tighten pharynx: no English equivalent.'),
                    ('\u063a /\u0263/','uvular fricative \u2014 voiced. Like French r, back of throat.'),
                    ('\u062d /\u1e25/','pharyngeal fricative \u2014 voiceless. Breathy pharynx constriction.'),
                    ('\u0642 /q/','uvular stop \u2014 like /k/ but farther back. Distinct from /k/ (kaf).'),
                    ('\u0621 /\u02c0/','glottal stop (hamza) \u2014 closure of vocal folds. Initial in every vowel-initial word.')]
    for i,(sym,desc) in enumerate(pharyngeals):
        y = 168 + i*10
        g += t(70,y,sym,'middle','Ls'); g += t(310,y,desc,'middle','Lx')
    g += hr(222)

    g += sh(230,'SUN \u00b7 MOON LETTERS \u00b7 ASSIMILATION')
    g += t(240,240,'Definite article \u0627\u0644 (al-): assimilates to "sun letters" (dentals/sibilants): al-shams \u2192 ash-shams (the sun).','middle','Ls')
    g += t(240,249,'"Moon letters" (velars, pharyngeals, etc.) do not assimilate: al-qamar (the moon) stays as-is.','middle','Lx')

    # DIVIDER
    g += sec_divider(260,'GREEK (ELLINIK\u0391) \u00b7 PHONOLOGY \u00b7 SOUND SYSTEM')

    # SECONDARY: GREEK PHONOLOGY
    g += t(240,292,'Modern Greek phonology is simpler than Ancient Greek \u2014 vowel system collapsed, aspirates became fricatives.','middle','Ls')
    g += hr(299)

    g += sh(307,'MODERN GREEK \u2014 5 VOWEL SOUNDS')
    g += t(240,317,'/a/ \u03b1  \u00b7  /e/ \u03b5 \u03b7 \u03b1\u03b9 \u03b5\u03b9  \u00b7  /i/ \u03b9 \u03c5 \u03bf\u03b9 \u03c5\u03b9  \u00b7  /o/ \u03bf \u03c9  \u00b7  /u/ \u03bf\u03c5','middle','Ls')
    g += t(240,326,'Ancient Greek had length distinction (short vs. long) + diphthongs. Modern collapsed to 5 pure vowels.','middle','Lx')
    g += hr(333)

    g += sh(341,'KEY CONSONANTS \u2014 ANCIENT VS. MODERN')
    changes = [('\u03b2 B','ancient /b/','modern /v/'),('\u03b3 G','ancient /g/','modern /\u0263/ before a,o,u or /j/ before e,i'),
               ('\u03b4 D','ancient /d/','modern /\u00f0/ (like English "the")'),
               ('\u03b6 Z','ancient /zd/','modern /z/'),('\u03b8 Th','ancient /t\u02b0/','modern /\u03b8/ (like "think")'),
               ('\u03c6 Ph','ancient /p\u02b0/','modern /f/'),('\u03c7 Ch','ancient /k\u02b0/','modern /x/ or /\u00e7/')]
    for i,(ltr,anc,mod) in enumerate(changes):
        y = 350 + i*10
        g += t(50,y,ltr,'middle','Ls'); g += t(130,y,anc,'middle','Lx'); g += t(320,y,mod,'middle','Lx')
    g += hr(428)

    g += sh(436,'STRESS \u00b7 PITCH \u00b7 ACCENT MARKS')
    g += t(240,446,'Modern Greek: stress accent (not pitch). One stress per word, marked with tonos ( \u00b4 ) since 1982.','middle','Ls')
    g += t(240,455,'Ancient Greek: pitch accent (rising, falling, rise-fall). Three accent marks: acute \u00b4 grave \u0060 circumflex \u02c6.','middle','Lx')
    g += t(240,464,'Modern simplified to single tonos system; polytonic (multi-accent) still used in classical studies.','middle','Lx')
    g += hr(472)

    g += sh(480,'COMPARATIVE NOTE \u2014 ARABIC / GREEK PHONOLOGY')
    g += t(240,490,'Arabic: 3 vowels (short+long), heavy consonant inventory, pharyngeals, uvulars, emphatics.','middle','Ls')
    g += t(240,499,'Greek: 5 vowels, no pharyngeals, aspirates became fricatives, stress not pitch in modern form.','middle','Ls')
    g += t(240,508,'Both have ejective-analog features in classical forms; both influenced European scientific vocabulary.','middle','Lx')

    g += footer('13','ARABIC','GREEK','B','Phonology')
    return g + close_svg()


# ─── PLATE 13C ALT — GRAMMAR ──────────────────────────────────────────────────

def build_13c_alt():
    g = open_svg()
    g += t(240,30,'ARABIC + GREEK \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 13C \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: ARABIC GRAMMAR
    g += sh(63,'ARABIC \u2014 VSO \u00b7 TRILATERAL ROOTS \u00b7 DUAL NUMBER')
    g += t(240,73,'Word order: Verb-Subject-Object. "Kataba l-waladu r-ris\u0101lata" = Wrote the-boy the-letter.','middle','Ls')
    g += t(240,82,'Trilateral root: k-t-b = writing. \u0643\u062a\u0628 kataba (he wrote) \u00b7 \u0643\u062a\u0627\u0628 kit\u0101b (book) \u00b7 \u0645\u0643\u062a\u0628 maktab (office).','middle','Lx')
    g += t(240,91,'Three numbers: singular, dual (two), plural. Dual suffix: -\u0101ni (nom.) / -ayni (acc./gen.).','middle','Lx')
    g += hr(99)

    g += sh(107,'VERB CONJUGATION \u2014 KATABA "WROTE"')
    ar_conj = [('ana katabtu','\u0623\u0646\u0627 \u0643\u062a\u0628\u062a\u064f','I wrote'),
               ('anta katabta','\u0623\u0646\u062a \u0643\u062a\u0628\u062a\u064e','you (m) wrote'),
               ('anti katabti','\u0623\u0646\u062a\u0650 \u0643\u062a\u0628\u062a\u0650','you (f) wrote'),
               ('huwa kataba','\u0647\u0648 \u0643\u062a\u0628\u064e','he wrote'),
               ('hiya katabat','\u0647\u064a \u0643\u062a\u0628\u062a','she wrote'),
               ('na\u1e25nu katabn\u0101','\u0646\u062d\u0646 \u0643\u062a\u0628\u0646\u0627','we wrote')]
    for i,(latin,ar,gl) in enumerate(ar_conj):
        y = 116 + i*10
        g += t(80,y,latin,'middle','Lx'); g += t(240,y,ar,'middle','Lam'); g += t(380,y,gl,'middle','Lx')
    g += hr(183)

    g += sh(191,'CORE ARABIC VOCABULARY \u2014 20 WORDS')
    vocab = [('\u0645\u0627\u0621','m\u0101\u02bc','water'),('\u0646\u0627\u0631','n\u0101r','fire'),('\u0623\u0631\u0636','\u02beard','earth'),('\u0625\u0646\u0633\u0627\u0646','ins\u0101n','human'),
             ('\u0642\u0645\u0631','qamar','moon'),('\u0634\u0645\u0633','shams','sun'),('\u0646\u0639\u0645','naʻam','yes'),('\u0644\u0627','l\u0101','no'),
             ('\u0623\u0646\u0627','an\u0101','I'),('\u0623\u0646\u062a','anta','you(m)'),('\u062d\u0628','hubb','love'),('\u062d\u0631\u064a\u0629','{\u1e25}urriya','freedom'),
             ('\u0645\u0633\u062a\u0642\u0628\u0644','mustaqbal','future'),('\u0639\u0627\u0644\u0645','\u02bfalim','world'),('\u062c\u064a\u062f','jayyid','good'),
             ('\u0645\u0648\u062a','mawt','death'),('\u062d\u064a\u0627\u0629','\u1e25ay\u0101h','life'),('\u0634\u0643\u0631','shukr','thanks'),
             ('\u0645\u062a\u0649','mat\u0101','when'),('\u0623\u064a\u0646','ayna','where')]
    for i,(ar,tr,en) in enumerate(vocab):
        col = i//10; row = i%10
        y = 200 + row*10
        x0 = 20 + col*240
        g += t(x0+10,y,ar,'start','Lam'); g += t(x0+60,y,tr,'start','Lx'); g += t(x0+130,y,en,'start','Lx')
    g += hr(306)

    # DIVIDER
    g += sec_divider(314,'GREEK (ELLINIK\u0391) \u00b7 GRAMMAR \u00b7 VOCABULARY')

    # SECONDARY: GREEK GRAMMAR
    g += t(240,346,'Greek: flexible word order (SVO default). Inflected: nouns/verbs carry case and person markers.','middle','Ls')
    g += t(240,355,'3 genders (M/F/N), 4 cases (nominative, genitive, accusative, vocative in Modern; 5 in Ancient).','middle','Lx')
    g += hr(362)

    g += sh(370,'GREEK VERB \u2014 \u03b3\u03c1\u03ac\u03c6\u03c9 (gr\u00e1fo) "I WRITE"')
    gr_conj = [('\u03b3\u03c1\u03ac\u03c6\u03c9','gr\u00e1fo','I write'),('\u03b3\u03c1\u03ac\u03c6\u03b5\u03b9\u03c2','gr\u00e1feis','you write'),
               ('\u03b3\u03c1\u03ac\u03c6\u03b5\u03b9','gr\u00e1fei','he/she writes'),('\u03b3\u03c1\u03ac\u03c6\u03bf\u03c5\u03bc\u03b5','gr\u00e1foume','we write'),
               ('\u03b3\u03c1\u03ac\u03c6\u03b5\u03c4\u03b5','gr\u00e1fete','you (pl) write'),('\u03b3\u03c1\u03ac\u03c6\u03bf\u03c5\u03bd','gr\u00e1foun','they write')]
    for i,(gr,tr,en) in enumerate(gr_conj):
        y = 379 + i*10
        g += t(80,y,gr,'middle','Ls'); g += t(210,y,tr,'middle','Lx'); g += t(360,y,en,'middle','Lx')
    g += hr(446)

    g += sh(454,'CORE GREEK VOCABULARY \u2014 20 WORDS')
    gr_vocab = [('\u03bd\u03b5\u03c1\u03cc','nero','water'),('\u03c6\u03c9\u03c4\u03b9\u03ac','foti\u00e1','fire'),('\u03b3\u03b7','yi','earth'),('\u03ac\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03c2','anthropos','human'),
                ('\u03c6\u03b5\u03b3\u03b3\u03ac\u03c1\u03b9','fen\u02c8g\u00e1ri','moon'),('\u03ae\u03bb\u03b9\u03bf\u03c2','\u02c8ilios','sun'),('\u03bd\u03b1\u03b9','ne','yes'),('\u03cc\u03c7\u03b9','ochi','no'),
                ('\u03b5\u03b3\u03ce','ego','I'),('\u03b5\u03c3\u03cd','esy','you'),('\u03b1\u03b3\u03ac\u03c0\u03b7','ag\u00e1pi','love'),('\u03b5\u03bb\u03b5\u03c5\u03b8\u03b5\u03c1\u03af\u03b1','elef\u00f0er\u00eda','freedom'),
                ('\u03bc\u03ad\u03bb\u03bb\u03bf\u03bd','m\u00e9llon','future'),('\u03ba\u03cc\u03c3\u03bc\u03bf\u03c2','k\u00f3smos','world'),('\u03ba\u03b1\u03bb\u03cc\u03c2','kal\u00f3s','good'),
                ('\u03b8\u03ac\u03bd\u03b1\u03c4\u03bf\u03c2','\u02c8\u03b8\u00e1natos','death'),('\u03b6\u03c9\u03ae','zo\u00ed','life'),('\u03b5\u03c5\u03c7\u03b1\u03c1\u03b9\u03c3\u03c4\u03ce','ef\u00e7aristo','thank you'),
                ('\u03c0\u03cc\u03c4\u03b5','p\u00f3te','when'),('\u03c0\u03bf\u03cd','pu','where')]
    for i,(gr,tr,en) in enumerate(gr_vocab):
        col = i//10; row = i%10
        y = 463 + row*10
        x0 = 20 + col*240
        g += t(x0+10,y,gr,'start','Ls'); g += t(x0+80,y,tr,'start','Lx'); g += t(x0+150,y,en,'start','Lx')

    g += footer('13','ARABIC','GREEK','C','Grammar')
    return g + close_svg()


# ─── PLATE 13D ALT — RUNNING TEXT ────────────────────────────────────────────

def build_13d_alt():
    g = open_svg()
    g += t(240,30,'ARABIC + GREEK \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g += t(240,46,'ALT DRAFT \u00b7 SERIES 13D \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(54)

    # PRIMARY: ARABIC TEXT
    g += sh(63,'ARABIC \u2014 PASSAGE 1 \u00b7 SURAH AL-FATIHA (OPENING)')
    g += t(240,74,'\u0628\u0650\u0633\u0652\u0645\u0650 \u0627\u0644\u0644\u0651\u064e\u0647\u0650 \u0627\u0644\u0631\u0651\u064e\u062d\u0652\u0645\u064e\u0646\u0650 \u0627\u0644\u0631\u0651\u064e\u062d\u0650\u064a\u0645\u0650','middle','La')
    g += t(240,86,'Bismi ll\u0101hi r-ra\u1e25m\u0101ni r-ra\u1e25\u012bm','middle','Lx')
    g += t(240,95,'"In the name of God, the Most Gracious, the Most Merciful."','middle','Ls')
    g += hr(103)

    g += sh(111,'ARABIC \u2014 PASSAGE 2 \u00b7 PROVERB')
    g += t(240,122,'\u0627\u0644\u0639\u0644\u0645 \u0641\u064a \u0627\u0644\u0635\u063a\u0631 \u0643\u0627\u0644\u0646\u0642\u0634 \u0639\u0644\u0649 \u0627\u0644\u062d\u062c\u0631','middle','Lam')
    g += t(240,133,'Al-\u02bfilmu fi\u02be\u1e63-\u1e63ighari ka\u02be\u02ban-naqshi \u02bfala\u02be\u02bc-\u1e25ajar','middle','Lx')
    g += t(240,142,'"Knowledge in youth is like carving on stone." \u2014 Early learning endures.','middle','Ls')
    g += hr(150)

    g += sh(158,'ARABIC \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g += t(240,169,'\u0647\u0630\u0647 \u0627\u0644\u0631\u0633\u0627\u0644\u0629 \u0635\u064f\u0646\u0650\u0639\u064e\u062a \u0644\u0643\u060c \u0645\u062c\u0627\u0646\u0627\u064b\u060c \u0645\u0646 \u0623\u0646\u0627\u0633\u064d \u062a\u0630\u0643\u0651\u064e\u0631\u0648\u0627 \u0627\u0644\u0645\u0633\u062a\u0642\u0628\u064e\u0644','middle','Lam')
    g += t(240,180,'H\u0101dhihi r-ris\u0101latu \u1e63uni\u02bfat laka, majj\u0101nan, min un\u0101sin tadhakkar\u016b l-mustaqbal.','middle','Lx')
    g += t(240,189,'This  message  was-made  for-you,  freely,  from  people  who-remembered  the-future.','middle','Lx')
    g += t(240,198,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g += hr(206)

    g += sh(214,'LANGUAGE NOTE \u2014 "FUTURE" IN ARABIC')
    g += t(240,224,'\u0627\u0644\u0645\u0633\u062a\u0642\u0628\u0644 al-mustaqbal: lit. "what will be received / what lies ahead to be embraced."','middle','Ls')
    g += t(240,233,'Root q-b-l: to face, to receive. The future is what stands before you, facing you.','middle','Lx')
    g += t(240,242,'\u0625\u0644\u0649 \u0627\u0644\u0623\u0645\u0627\u0645 il\u0101 l-am\u0101m: "forward" \u2014 lit. "toward the front." Am\u0101m = in front.','middle','Lx')

    # DIVIDER
    g += sec_divider(253,'GREEK (ELLINIK\u0391) \u00b7 RUNNING TEXT \u00b7 PASSAGES')

    # SECONDARY: GREEK TEXT
    g += sh(284,'GREEK \u2014 PASSAGE 1 \u00b7 HERACLITUS')
    g += t(240,294,'\u03c0\u03ac\u03bd\u03c4\u03b1 \u03c1\u03b5\u03af','middle','Lg')
    g += t(240,306,'P\u00e1nta re\u00ed','middle','Lx')
    g += t(240,315,'"Everything flows." \u2014 Heraclitus, ~500 BCE. All things are in constant change.','middle','Ls')
    g += hr(323)

    g += sh(331,'GREEK \u2014 PASSAGE 2 \u00b7 PROTAGORAS')
    g += t(240,341,'\u03c0\u03ac\u03bd\u03c4\u03c9\u03bd \u03c7\u03c1\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03bc\u03ad\u03c4\u03c1\u03bf\u03bd \u03ac\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03c2','middle','Lg')
    g += t(240,352,'P\u00e1nton chr\u0113m\u00e1ton m\u00e9tron \u00e1nthr\u014dpos.','middle','Lx')
    g += t(240,361,'"Man is the measure of all things." \u2014 Protagoras, ~450 BCE.','middle','Ls')
    g += hr(369)

    g += sh(377,'GREEK \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g += t(240,388,'\u0391\u03c5\u03c4\u03cc \u03c6\u03c4\u03b9\u03ac\u03c7\u03c4\u03b7\u03ba\u03b5 \u03b3\u03b9\u03b1 \u03c3\u03ad\u03bd\u03b1, \u03b4\u03c9\u03c1\u03b5\u03ac\u03bd, \u03b1\u03c0\u03cc \u03b1\u03bd\u03b8\u03c1\u03ce\u03c0\u03bf\u03c5\u03c2 \u03c0\u03bf\u03c5 \u03b8\u03c5\u03bc\u03ae\u03b8\u03b7\u03ba\u03b1\u03bd \u03c4\u03bf \u03bc\u03ad\u03bb\u03bb\u03bf\u03bd.','middle','Lg')
    g += t(240,400,'Af\u00f3 ftiaxt\u00edke ya s\u00e9na, dore\u00e1n, ap\u00f3 antr\u00f3pous pou thim\u00edthikan to m\u00e9llon.','middle','Lx')
    g += t(240,409,'This  was-made  for  you,  freely,  by  people  who  remembered  the-future.','middle','Lx')
    g += t(240,418,'"This was made for you, freely, by people who remembered the future."','middle','Ls')
    g += hr(426)

    g += sh(434,'LANGUAGE NOTE \u2014 "FUTURE" IN GREEK')
    g += t(240,444,'\u03bc\u03ad\u03bb\u03bb\u03bf\u03bd (m\u00e9llon): "future" \u2014 from \u03bc\u03ad\u03bb\u03bb\u03c9 (m\u00e9llo) = to be about to, to intend.','middle','Ls')
    g += t(240,453,'The Greek future is grammatically the "about-to-be" \u2014 the imminent, the intended.','middle','Lx')
    g += t(240,462,'\u03bc\u03c0\u03c1\u03bf\u03c3\u03c4\u03ac (brost\u00e1): "forward" \u2014 lit. "in front, ahead." \u03b5\u03bc\u03c0\u03c1\u03cc\u03c2 (empr\u00f3s) = to the front.','middle','Lx')
    g += hr(470)

    g += sh(478,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g += t(240,488,'Arabic: 1.9B speakers, official in 22 countries. Right-to-left abjad. See plates 13A\u201313C for full grammar.','middle','Ls')
    g += t(240,497,'Greek: ~13M speakers (Greece + Cyprus). Left-to-right alphabet. Ancestor of Latin and Cyrillic.','middle','Ls')
    g += t(240,506,'Both languages shaped science, mathematics, and philosophy. Arabic preserved Greek texts 700\u20131300 CE.','middle','Ls')
    g += t(240,515,'Geographic link: Mediterranean. Cairo to Athens ~2,000 km; to Crete ~1,400 km (within 500mi radius).','middle','Lx')

    g += footer('13','ARABIC','GREEK','D','Text')
    return g + close_svg()


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    plates = {
        'plate13a_arabic_greek_script_alt.svg':    build_13a_alt(),
        'plate13b_arabic_greek_phonology_alt.svg': build_13b_alt(),
        'plate13c_arabic_greek_grammar_alt.svg':   build_13c_alt(),
        'plate13d_arabic_greek_text_alt.svg':      build_13d_alt(),
    }
    for fname, content in plates.items():
        path = OUT / fname
        path.write_text(content, encoding='utf-8')
        print(f'Written: {path}')

if __name__ == '__main__':
    main()
