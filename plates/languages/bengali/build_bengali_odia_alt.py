#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Bengali / Odia alt plates 16A–16D for Remember Forward.
Secondary: Odia (Oḍiā) — ~40M speakers in Odisha, ~300mi from Dhaka/Kolkata.
Both Brahmi-descended abugidas. Bengali = U+0980–09FF. Odia = U+0B00–0B7F.
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
        '  .Lb{font-size:12px} .Lbs{font-size:9px}\n'
        '  .Lo{font-size:12px} .Los{font-size:9px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic} .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')
def close_svg(): return '</svg>\n'
def t(x,y,s,a='middle',c='L'): return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'
def hr(y,x1=20,x2=460,sw=0.3): return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y,txt): return t(240,y,f'\u2014 {txt} \u2014','middle','H')
def div(y,lbl):
    return (hr(y,sw=1.5)+f'<rect x="20" y="{y+3}" width="440" height="14" fill="black"/>\n'
        +f'<text x="240" y="{y+13}" text-anchor="middle" class="Hb" fill="white">{esc(lbl)}</text>\n'+hr(y+17,sw=0.3))
def foot(num,l1,l2,let,desc):
    return (hr(625)+t(240,620,f'PLATE {num}{let} ALT \u00b7 {l1}/{l2} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        +hr(633)+t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        +t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))

BN='16'; L1='BENGALI'; L2='ODIA'

def build_16a_alt():
    g=open_svg()
    g+=t(240,30,'BENGALI + ODIA \u2014 SCRIPT \u00b7 WRITING SYSTEMS','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 16A \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'BENGALI \u2014 BANGLA SCRIPT \u00b7 ABUGIDA \u00b7 LEFT TO RIGHT')
    g+=t(240,73,'Bengali (Bangla) script: derived from Brahmi via Eastern Nagari. ~50 letters. Each consonant carries inherent /\u0254/ vowel.','middle','Ls')
    g+=t(240,82,'Vowel signs (matra) modify the inherent vowel. Consonant clusters join into conjuncts.','middle','Lx')
    g+=hr(89)
    g+=sh(97,'BENGALI VOWELS \u2014 INDEPENDENT FORMS')
    vowels_bn=[('\u0985','a'),('\u0986','\u0101'),('\u0987','i'),('\u0988','\u012b'),('\u0989','u'),('\u098a','\u016b'),
               ('\u098b','\u1e5b'),('\u098f','e'),('\u0990','ai'),('\u0993','o'),('\u0994','au')]
    xs=list(range(28,470,40))
    for i,(g_,tr) in enumerate(vowels_bn):
        x=xs[i] if i<len(xs) else 28+i*40
        g+=t(x,107,g_,'middle','Lb'); g+=t(x,118,tr,'middle','Lx')
    g+=hr(125)
    g+=sh(133,'BENGALI CONSONANTS \u2014 FIRST TWO ROWS (ka-varga + ca-varga)')
    row1=[('\u0995','ka'),('\u0996','kha'),('\u0997','ga'),('\u0998','gha'),('\u0999','nga')]
    row2=[('\u099a','ca'),('\u099b','cha'),('\u099c','ja'),('\u099d','jha'),('\u099e','nya')]
    for row,y0 in [(row1,143),(row2,157)]:
        for i,(g_,tr) in enumerate(row):
            x=60+i*80
            g+=t(x,y0,g_,'middle','Lb'); g+=t(x,y0+9,tr,'middle','Lx')
    g+=hr(175)
    g+=sh(183,'SELECTED CONSONANTS \u2014 DENTALS \u00b7 LABIALS \u00b7 SONORANTS')
    more=[('\u09a4','ta'),('\u09a6','da'),('\u09a8','na'),('\u09aa','pa'),('\u09ac','ba'),
          ('\u09ae','ma'),('\u09af','ya'),('\u09b0','ra'),('\u09b2','la'),('\u09b8','sa'),('\u09b9','ha')]
    for i,(g_,tr) in enumerate(more):
        x=28+i*40
        g+=t(x,193,g_,'middle','Lb'); g+=t(x,203,tr,'middle','Lx')
    g+=hr(210)
    g+=sh(218,'SCRIPT NOTES')
    g+=t(240,228,'Script also used for Assamese and several other northeast Indian languages.','middle','Ls')
    g+=t(240,237,'Conjuncts: \u0995\u09cd\u09b7 (kṣa), \u099c\u09cd\u099e (jña) \u2014 joined consonants common in Sanskritic words.','middle','Lx')
    g+=t(240,246,'~230M speakers worldwide (Bangladesh + West Bengal + diaspora). Official script of Bangladesh.','middle','Lx')
    g+=div(257,'ODIA (\u0b13\u0b21\u0b3c\u0b3f\u0b06) \u00b7 SCRIPT \u00b7 ABUGIDA \u00b7 LEFT TO RIGHT')
    g+=t(240,288,'Odia script: also Brahmi-derived, ~11th century. Distinctive rounded letter-tops (influence of palm-leaf manuscripts).','middle','Ls')
    g+=t(240,297,'Same abugida logic as Bengali: consonant + inherent /a/ vowel, modified by matra signs.','middle','Lx')
    g+=t(240,306,'~40M speakers in Odisha state. Classical language status in India (2014). One of 22 Scheduled Languages.','middle','Lx')
    g+=hr(313)
    g+=sh(321,'ODIA VOWELS \u2014 INDEPENDENT FORMS')
    vowels_or=[('\u0b05','a'),('\u0b06','\u0101'),('\u0b07','i'),('\u0b08','\u012b'),('\u0b09','u'),('\u0b0a','\u016b'),
               ('\u0b0f','e'),('\u0b10','ai'),('\u0b13','o'),('\u0b14','au')]
    for i,(g_,tr) in enumerate(vowels_or):
        x=36+i*45
        g+=t(x,331,g_,'middle','Lo'); g+=t(x,342,tr,'middle','Lx')
    g+=hr(349)
    g+=sh(357,'ODIA CONSONANTS \u2014 FIRST TWO ROWS')
    row1o=[('\u0b15','ka'),('\u0b16','kha'),('\u0b17','ga'),('\u0b18','gha'),('\u0b19','nga')]
    row2o=[('\u0b1a','ca'),('\u0b1b','cha'),('\u0b1c','ja'),('\u0b1d','jha'),('\u0b1e','nya')]
    for row,y0 in [(row1o,367),(row2o,381)]:
        for i,(g_,tr) in enumerate(row):
            x=60+i*80
            g+=t(x,y0,g_,'middle','Lo'); g+=t(x,y0+9,tr,'middle','Lx')
    g+=hr(399)
    g+=sh(407,'SCRIPT BRIDGE \u2014 SAME WORDS, BENGALI VS. ODIA')
    bridge=[('\u099c\u09b2','\u0b1c\u0b33','jala','water'),('\u0986\u0997\u09c1\u09a8','\u0b06\u0b17','āgun/āga','fire'),
            ('\u09ae\u09be\u099f\u09bf','\u0b2e\u0b3e\u0b1f\u0b3f','māṭi','earth'),('\u09ae\u09be\u09a8\u09c1\u09b7','\u0b2e\u0b23\u0b3f\u0b37','mānuṣ','person'),
            ('\u099a\u09be\u0981\u09a6','\u0b1a\u0b3e\u0b02\u0b26','cā̃d','moon')]
    for lbl,x in zip(['Bengali','Odia','Translit.','English'],[80,200,320,410]):
        g+=t(x,417,lbl,'middle','Lx')
    g+=hr(421,sw=0.2)
    for i,(bn,or_,tr,en) in enumerate(bridge):
        y=430+i*12
        g+=t(80,y,bn,'middle','Lbs'); g+=t(200,y,or_,'middle','Los'); g+=t(320,y,tr,'middle','Lx'); g+=t(410,y,en,'middle','Lx')
    g+=foot(BN,L1,L2,'A','Script')
    return g+close_svg()

def build_16b_alt():
    g=open_svg()
    g+=t(240,30,'BENGALI + ODIA \u2014 PHONOLOGY \u00b7 SOUND SYSTEMS','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 16B \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'BENGALI \u2014 VOWEL SYSTEM')
    g+=t(240,73,'7 oral vowels: /a \u0254 e \u025b i o u/. /a/ and /\u0254/ both written \u0985 contextually.','middle','Ls')
    g+=t(240,82,'Distinctive: /\u0254/ (open-mid back rounded) \u2014 English "awe". /e/ and /o/ are monophthongs (not diphthongs).','middle','Lx')
    g+=hr(89)
    g+=sh(97,'BENGALI \u2014 CONSONANTS: 4 STOP SERIES')
    g+=t(240,107,'Bengali preserves the full Indo-Aryan 4-way stop contrast: voiceless, aspirated, voiced, voiced-aspirated.','middle','Ls')
    stops=[('ka/kha/ga/gha','velar stops','k k\u02b0 g g\u02b0'),('ca/cha/ja/jha','palatal affricate','t\u0283 t\u0283\u02b0 d\u0292 d\u0292\u02b0'),
           ('ṭa/ṭha/ḍa/ḍha','retroflex stops','\u0288 \u0288\u02b0 \u0256 \u0256\u02b0'),('ta/tha/da/dha','dental stops','t\u032a t\u032a\u02b0 d\u032a d\u032a\u02b0'),
           ('pa/pha/ba/bha','bilabial stops','p p\u02b0 b b\u02b0')]
    for i,(ltr,place,ipa) in enumerate(stops):
        y=116+i*10
        g+=t(100,y,ltr,'middle','Lx'); g+=t(220,y,place,'middle','Lx'); g+=t(360,y,ipa,'middle','Lx')
    g+=hr(170)
    g+=sh(178,'BENGALI \u2014 NASALS \u00b7 RETROFLEXES \u00b7 SIBILANTS')
    g+=t(240,188,'5 nasal stops: /\u014b n\u0272 \u0273 n m/ \u2014 ñ and ṇ rare in modern speech, merged to /n/.','middle','Ls')
    g+=t(240,197,'Retroflexes \u1e6d \u1e0d distinctive in formal register. 3 sibilants: /\u0255 \u0282 s/ written \u09b6 \u09b7 \u09b8.','middle','Lx')
    g+=t(240,206,'No tonal distinctions. Stress: generally on first syllable. Vowel length not phonemic in modern Bengali.','middle','Lx')
    g+=div(217,'ODIA (\u0b13\u0b21\u0b3c\u0b3f\u0b06) \u00b7 PHONOLOGY')
    g+=t(240,249,'Odia phonology closely parallels Bengali. Same 4-way stop system. Both derived from Magadhi Prakrit.','middle','Ls')
    g+=hr(256)
    g+=sh(264,'ODIA \u2014 VOWEL SYSTEM')
    g+=t(240,274,'6 oral vowels: /a \u0101 i \u012b u \u016b e o/. Odia retains length distinction in /a\u0101/ /i\u012b/ /u\u016b/ more clearly than Bengali.','middle','Ls')
    g+=t(240,283,'Odia /a/ is a central open vowel; /\u0101/ is longer. Less merger than Bengali.','middle','Lx')
    g+=hr(290)
    g+=sh(298,'ODIA \u2014 DISTINCT FEATURES FROM BENGALI')
    diffs=[('Retroflex lateral','\u0b33 /\u026d/ (Odia \u1e37a)','Bengali lacks this phoneme'),
           ('Retroflex nasal','\u0b23 /\u0273/ more preserved in Odia','Bengali merged to /n/ in speech'),
           ('Inherent vowel','/a/ in Odia (shorter, more central)','Bengali uses /\u0254/'),
           ('Sibilant merger','Odia: 3 sibilants \u0b36 \u0b37 \u0b38 distinct in writing','Speech: often merged to /s/'),
           ('Stress','Penultimate in Odia, somewhat variable','Bengali: generally first syllable')]
    for i,(feat,or_,bn) in enumerate(diffs):
        y=307+i*18
        g+=t(60,y,feat,'start','Lx'); g+=t(60,y+9,f'Odia: {or_}','start','Lx'); g+=t(320,y+9,f'Beng: {bn}','start','Lx')
    g+=hr(402)
    g+=sh(410,'SHARED FEATURES \u2014 INDO-ARYAN HERITAGE')
    g+=t(240,420,'Both: 4-way stop series, aspirated consonants, retroflexes, SOV word order, postpositions.','middle','Ls')
    g+=t(240,429,'Both descended from Magadhi Prakrit (eastern Middle Indo-Aryan), diverging ~10th\u201312th century CE.','middle','Lx')
    g+=t(240,438,'Major shared vocabulary (Sanskrit loans): \u099c\u09b2/\u0b1c\u0b33 (water), \u09ae\u09be\u09a8\u09c1\u09b7/\u0b2e\u09be\u09a8\u09c1\u09b7 (human), \u09ad\u09c2\u09ae\u09bf/\u0b2d\u09c2\u09ae\u09bf (earth).','middle','Lx')
    g+=foot(BN,L1,L2,'B','Phonology')
    return g+close_svg()

def build_16c_alt():
    g=open_svg()
    g+=t(240,30,'BENGALI + ODIA \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 16C \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'BENGALI \u2014 SOV \u00b7 POSTPOSITIONS \u00b7 ASPECT-HEAVY VERB SYSTEM')
    g+=t(240,73,'Bengali is SOV. Postpositions follow their noun: ghor-e (house-in = in the house).','middle','Ls')
    g+=t(240,82,'Verb agrees with person/formality, not gender. Three registers: formal, neutral, intimate.','middle','Lx')
    g+=t(240,91,'Aspect: Bengali emphasizes perfect/imperfect aspect more than tense. "I have eaten" vs. "I am eating."','middle','Lx')
    g+=hr(99)
    g+=sh(107,'BENGALI CORE VOCABULARY \u2014 20 WORDS')
    bn_v=[('\u099c\u09b2','jal','water'),('\u0986\u0997\u09c1\u09a8','\u0101gun','fire'),('\u09ae\u09be\u099f\u09bf','m\u0101ṭi','earth'),('\u09ae\u09be\u09a8\u09c1\u09b7','m\u0101nuṣ','person'),
          ('\u099a\u09be\u0981\u09a6','c\u0101\u0302d','moon'),('\u09b8\u09c2\u09b0\u09cd\u09af','s\u016brya','sun'),('\u09b9\u09cd\u09af\u09be\u0981','hy\u0101\u0302','yes'),('\u09a8\u09be','n\u0101','no'),
          ('\u0986\u09ae\u09bf','\u0101mi','I'),('\u09a4\u09c1\u09ae\u09bf','tumi','you'),('\u09ad\u09be\u09b2\u09cb\u09ac\u09be\u09b8\u09be','bh\u0101lob\u0101s\u0101','love'),
          ('\u09b8\u09cd\u09ac\u09be\u09a7\u09c0\u09a8\u09a4\u09be','sv\u0101dh\u012bnat\u0101','freedom'),('\u09ad\u09ac\u09bf\u09b7\u09cd\u09af\u09ce','bhaviṣyat','future'),
          ('\u09aa\u09c3\u09a5\u09bf\u09ac\u09c0','pṛthiv\u012b','world'),('\u09ad\u09be\u09b2\u09cb','bh\u0101lo','good'),('\u09ae\u09c3\u09a4\u09cd\u09af\u09c1','mṛtyu','death'),
          ('\u099c\u09c0\u09ac\u09a8','j\u012bvan','life'),('\u09a7\u09a8\u09cd\u09af\u09ac\u09be\u09a6','dhanyav\u0101d','thanks'),('\u0995\u0996\u09a8','kakhan','when'),('\u0995\u09cb\u09a5\u09be\u09af\u09bc','kothai','where')]
    for i,(sc,tr,en) in enumerate(bn_v):
        col=i//10; row=i%10; y=116+row*10; x0=20+col*240
        g+=t(x0+5,y,sc,'start','Lbs'); g+=t(x0+65,y,tr,'start','Lx'); g+=t(x0+130,y,en,'start','Lx')
    g+=hr(222)
    g+=div(230,'ODIA (\u0b13\u0b21\u0b3c\u0b3f\u0b06) \u00b7 GRAMMAR \u00b7 VOCABULARY')
    g+=t(240,262,'Odia is also SOV. Postpositions. Verb-final. Very similar structural grammar to Bengali.','middle','Ls')
    g+=t(240,271,'Three grammatical numbers: singular, plural, honorific-plural. Second person honorific widespread.','middle','Lx')
    g+=hr(278)
    g+=sh(286,'ODIA CORE VOCABULARY \u2014 20 WORDS')
    or_v=[('\u0b1c\u0b33','jaḷa','water'),('\u0b06\u0b17','\u0101ga','fire'),('\u0b2e\u0b3e\u0b1f\u0b3f','m\u0101ṭi','earth'),('\u0b2e\u0b23\u0b3f\u0b37','maṇiṣa','person'),
          ('\u0b1a\u0b3e\u0b02\u0b26','c\u0101\u0302da','moon'),('\u0b38\u0b42\u0b30\u0b4d\u0b5f','s\u016brya','sun'),('\u0b39\u0b01','h\u0101\u0302','yes'),('\u0b28\u0b3e','n\u0101','no'),
          ('\u0b2e\u0b41\u0b01','mu\u0302','I'),('\u0b24\u0b41','tu','you (inf.)'),('\u0b2d\u0b3e\u0b32\u0b2a\u0b3e\u0b07\u0b2c\u0b3e','bh\u0101lap\u0101ib\u0101','love'),
          ('\u0b38\u0b4d\u0b2c\u0b3e\u0b27\u0b40\u0b28\u0b24\u0b3e','sv\u0101dh\u012bnat\u0101','freedom'),('\u0b2d\u0b2c\u0b3f\u0b37\u0b4d\u0b5f\u0b24','bhaviṣyata','future'),
          ('\u0b2a\u0b43\u0b25\u0b3f\u0b2c\u0b40','pṛthiv\u012b','world'),('\u0b2d\u0b32\u0b3e','bhal\u0101','good'),('\u0b2e\u0b43\u0b24\u0b4d\u0b5f\u0b41','mṛtyu','death'),
          ('\u0b1c\u0b40\u0b2c\u0b28','j\u012bvana','life'),('\u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26','dhanyav\u0101da','thanks'),('\u0b15\u0b3e\u0b39\u0b3f\u0b01','k\u0101hi\u0302','when'),('\u0b15\u0b41\u0b06','ku\u0101','where')]
    for i,(sc,tr,en) in enumerate(or_v):
        col=i//10; row=i%10; y=295+row*10; x0=20+col*240
        g+=t(x0+5,y,sc,'start','Los'); g+=t(x0+65,y,tr,'start','Lx'); g+=t(x0+130,y,en,'start','Lx')
    g+=foot(BN,L1,L2,'C','Grammar')
    return g+close_svg()

def build_16d_alt():
    g=open_svg()
    g+=t(240,30,'BENGALI + ODIA \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 16D \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'BENGALI \u2014 PASSAGE 1 \u00b7 TAGORE')
    g+=t(240,74,'\u0986\u09ae\u09be\u09b0 \u09b8\u09cb\u09a8\u09be\u09b0 \u09ac\u09be\u0982\u09b2\u09be, \u0986\u09ae\u09bf \u09a4\u09cb\u09ae\u09be\u09df \u09ad\u09be\u09b2\u09cb\u09ac\u09be\u09b8\u09bf','middle','Lb')
    g+=t(240,86,'\u0100m\u0101r son\u0101r B\u0101\u1e45gl\u0101, \u0101mi tom\u0101y bh\u0101lob\u0101si.','middle','Lx')
    g+=t(240,95,'"My golden Bengal, I love you." \u2014 Rabindranath Tagore. Now the national anthem of Bangladesh.','middle','Ls')
    g+=hr(103)
    g+=sh(111,'BENGALI \u2014 PASSAGE 2 \u00b7 PROVERB')
    g+=t(240,122,'\u09b8\u09be\u09b0 \u09b8\u09be\u09b0 \u0995\u09a5\u09be, \u09a8\u09be \u09b9\u09df \u09ae\u09bf\u09a5\u09cd\u09af\u09be \u09b8\u09be\u09a7\u09a8\u09be\u0964','middle','Lbs')
    g+=t(240,132,'Truth is truth, do not pursue falsehood. \u2014 Bengali proverb.','middle','Ls')
    g+=hr(140)
    g+=sh(148,'BENGALI \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g+=t(240,160,'\u098f\u099f\u09bf \u0986\u09aa\u09a8\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u09ac\u09bf\u09a8\u09be\u09ae\u09c2\u09b2\u09cd\u09af\u09c7 \u09a4\u09c8\u09b0\u09bf \u09b9\u09af\u09bc\u09c7\u099b\u09bf\u09b2\u0964','middle','Lb')
    g+=t(240,172,'\u09af\u09be\u09b0\u09be \u09b8\u09be\u09ae\u09a8\u09c7\u09b0 \u0995\u09a5\u09be \u09ae\u09a8\u09c7 \u09b0\u09c7\u0996\u09c7\u099b\u09bf\u09b2, \u09a4\u09be\u09a6\u09c7\u09b0 \u09a6\u09cd\u09ac\u09be\u09b0\u09be\u0964','middle','Lb')
    g+=t(240,183,'\u0100pn\u0101r janya bin\u0101m\u016blye tairi hayechila. Y\u0101r\u0101 s\u0101maner kath\u0101 mane rekhechila, t\u0101der dv\u0101r\u0101.','middle','Lx')
    g+=t(240,192,'"Made for you, freely. By those who remembered what lies ahead."','middle','Ls')
    g+=hr(200)
    g+=sh(208,'LANGUAGE NOTE \u2014 "FORWARD" IN BENGALI')
    g+=t(240,218,'\u09b8\u09be\u09ae\u09a8\u09c7 (s\u0101mane): "ahead / forward" \u2014 lit. "in front." Opposite: \u09aa\u09c7\u099b\u09a8\u09c7 (pechane) = behind.','middle','Ls')
    g+=t(240,227,'\u09ad\u09ac\u09bf\u09b7\u09cd\u09af\u09ce (bhaviṣyat): "future" \u2014 Sanskrit root bh\u016b (to be) + future suffix. "That which will be."','middle','Lx')
    g+=div(238,'ODIA (\u0b13\u0b21\u0b3c\u0b3f\u0b06) \u00b7 RUNNING TEXT \u00b7 PASSAGES')
    g+=sh(270,'ODIA \u2014 PASSAGE 1 \u00b7 PROVERB')
    g+=t(240,281,'\u0b06\u0b0f\u0b38\u0b4d\u0b2e\u0b3e\u0b30\u0b47 \u0b2d\u0b42\u0b2e\u0b3f \u0b2e\u0b3e','middle','Lo')
    g+=t(240,293,'\u0100es\'m\u0101re bh\u016bmi m\u0101.','middle','Lx')
    g+=t(240,302,'"This earth is our mother." \u2014 Odia proverb. Reverence for land central to Odisha culture.','middle','Ls')
    g+=hr(310)
    g+=sh(318,'ODIA \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g+=t(240,330,'\u0b0f\u0b39\u0b3e \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15 \u0b2a\u0b3e\u0b07\u0b01 \u0b2c\u0b3f\u0b28\u0b3e\u0b2e\u0b42\u0b32\u0b4d\u0b5f\u0b30\u0b47 \u0b24\u0b3f\u0b06\u0b30\u0b3f \u0b39\u0b4b\u0b07\u0b1b\u0b3f\u0964','middle','Lo')
    g+=t(240,342,'\u0b2f\u0b3f\u0b0f\u0b2e\u0b3e\u0b28\u0b47 \u0b2d\u0b2c\u0b3f\u0b37\u0b4d\u0b5f\u0b24 \u0b2e\u0b28\u0b47 \u0b30\u0b16\u0b3f\u0b25\u0b3f\u0b32\u0b47, \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b19\u0b4d\u0b15 \u0b26\u0b4d\u0b35\u0b3e\u0b30\u0b3e\u0964','middle','Los')
    g+=t(240,353,'\u0100paṇa\u1e45ka p\u0101i\u0302 bin\u0101m\u016blyare ti\u0101ri hoichi. Yiem\u0101ne bhaviṣyata mane rakhi\u1e6dhile, sem\u0101na\u1e45ka dv\u0101r\u0101.','middle','Lx')
    g+=t(240,362,'"Made for you, freely. By those who remembered the future."','middle','Ls')
    g+=hr(370)
    g+=sh(378,'LANGUAGE NOTE \u2014 "FUTURE" IN ODIA')
    g+=t(240,388,'\u0b06\u0b17\u0b15\u0b41 (\u0101gaku): "forward / ahead" \u2014 lit. "toward the front." \u0b06\u0b17 (āga) = front/fire. Same root!','middle','Ls')
    g+=t(240,397,'\u0b2d\u0b2c\u0b3f\u0b37\u0b4d\u0b5f\u0b24 (bhaviṣyata): "future" \u2014 same Sanskrit root as Bengali bhaviṣyat. Pan-Indic term.','middle','Lx')
    g+=t(240,406,'Odia classical literature (Panchasakha movement, 15th\u201316th c.) predates modern prose tradition.','middle','Lx')
    g+=hr(414)
    g+=sh(422,'DECODING NOTE')
    g+=t(240,432,'Bengali: ~230M speakers. Largest language in Bangladesh; 2nd largest in India. Official in West Bengal.','middle','Ls')
    g+=t(240,441,'Odia: ~40M speakers. Classical language of India. Script distinct from Bengali despite shared ancestry.','middle','Ls')
    g+=t(240,450,'Geographic link: Kolkata (Bengali center) to Bhubaneswar (Odia center) \u2248 440km \u2014 within 500mi.','middle','Lx')
    g+=foot(BN,L1,L2,'D','Text')
    return g+close_svg()

def main():
    plates={'plate16a_bengali_odia_script_alt.svg':build_16a_alt(),
            'plate16b_bengali_odia_phonology_alt.svg':build_16b_alt(),
            'plate16c_bengali_odia_grammar_alt.svg':build_16c_alt(),
            'plate16d_bengali_odia_text_alt.svg':build_16d_alt()}
    for fn,content in plates.items():
        p=OUT/fn; p.write_text(content,encoding='utf-8'); print(f'Written: {p}')
if __name__=='__main__': main()
