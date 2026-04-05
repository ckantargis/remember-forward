#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Amharic plate series 31A–31D for Remember Forward."""
from pathlib import Path
OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text { font-family: Georgia, serif; }\n'
        '  .T{font-size:12px;font-weight:bold;letter-spacing:2px}\n'
        '  .S{font-size:7px;letter-spacing:1.5px}\n'
        '  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}\n'
        '  .L{font-size:7px} .Ls{font-size:6px} .Lx{font-size:5.5px}\n'
        '  .La{font-size:11px} .Las{font-size:9px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')
def close_svg(): return '</svg>\n'
def t(x,y,s,a='middle',c='L',extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{esc(s)}</text>\n'
def hr(y,x1=20,x2=460,sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y,txt): return t(240,y,f'\u2014 {txt} \u2014','middle','H')
def footer(num,lang,letter,desc):
    return (hr(625)+t(240,620,f'SERIES {num} \u00b7 {lang.upper()} \u00b7 PLATE {letter} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        +hr(633)+t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        +t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))

def build_31a():
    g=open_svg()
    g+=t(240,32,'AMHARIC \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g+=t(240,50,'SERIES 31A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'ETHIOPIC SCRIPT (FIDEL) \u2014 AN ABUGIDA')
    g+=t(240,79,'Amharic is written in the Ethiopic script (Fidel \u1348\u12f0\u120d), an abugida: each symbol = consonant + vowel.','middle','L')
    g+=t(240,89,'Each consonant has 7 forms (orders), one for each vowel. Base form includes inherent /\u0259/ vowel.','middle','Ls')
    g+=t(240,98,'~234 syllable signs in full Amharic fidel. Left to right, top to bottom.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'SAMPLE FIDEL \u2014 CONSONANT ha IN ALL 7 VOWEL ORDERS')
    g+=t(240,126,'Each row shows one consonant across all 7 vowels: \u0259 u i a e (none) o','middle','Lx')
    rows=[
        ('\u1200','\u1201','\u1202','\u1203','\u1204','\u1205','\u1206','h\u2026'),
        ('\u1208','\u1209','\u120a','\u120b','\u120c','\u120d','\u120e','l\u2026'),
        ('\u1210','\u1211','\u1212','\u1213','\u1214','\u1215','\u1216','H\u2026'),
        ('\u1218','\u1219','\u121a','\u121b','\u121c','\u121d','\u121e','m\u2026'),
        ('\u1230','\u1231','\u1232','\u1233','\u1234','\u1235','\u1236','s\u2026'),
        ('\u1238','\u1239','\u123a','\u123b','\u123c','\u123d','\u123e','sh\u2026'),
        ('\u1240','\u1241','\u1242','\u1243','\u1244','\u1245','\u1246','q\u2026'),
    ]
    vowel_hdrs=['\u0259','u','i','a','e','-','o','C']
    col_xs=[32,78,118,158,198,238,278,322]
    for ci,vh in enumerate(vowel_hdrs):
        g+=t(col_xs[ci],136,vh,'middle','Lx')
    for ri,row in enumerate(rows):
        y=146+ri*14
        for ci,ch in enumerate(row):
            g+=t(col_xs[ci],y,ch,'middle','La' if ci<7 else 'Lx')
    g+=hr(248)
    g+=sh(257,'THE 7 VOWEL ORDERS')
    orders=[('1st / \u1308\u12d3\u12ed','\u0259','like "about" \u2014 base form'),
            ('2nd / \u12ab\u12d3\u12ed','u','like "boot"'),
            ('3rd / \u1233\u120d\u1235\u12d3\u12ed','i','like "see"'),
            ('4th / \u122b\u12d3\u12ed','a','like "father"'),
            ('5th / \u1213\u121d\u1235\u12d3\u12ed','e','like "bed"'),
            ('6th / \u1233\u12f5\u1235\u12d3\u12ed','(none)','consonant only / short \u0259'),
            ('7th / \u1230\u12d3\u12ed','o','like "go"')]
    for i,(order,vowel,desc) in enumerate(orders):
        y=267+i*11
        g+=t(100,y,order,'middle','Lx'); g+=t(200,y,vowel,'middle','Lx'); g+=t(350,y,desc,'middle','Lx')
    g+=hr(346)
    g+=sh(355,'SCRIPT HISTORY')
    g+=t(240,366,'Ethiopic script descended from South Arabian (Sabaean) script via ancient Ge\'ez (~4th c. CE).','middle','Ls')
    g+=t(240,375,'Ge\'ez (Classical Ethiopic): liturgical language of the Ethiopian Orthodox Church; used in manuscripts.','middle','Ls')
    g+=t(240,384,'Amharic adopted Fidel from Ge\'ez ~13th\u201314th c., adding new letters for Amharic-specific sounds.','middle','Ls')
    g+=t(240,393,'Ethiopia was never fully colonised \u2014 Ethiopic script was never replaced by Latin.','middle','Ls')
    g+=t(240,402,'Modern Amharic: official language of Ethiopia (~35M native speakers, ~100M L1+L2).','middle','Ls')
    g+=t(240,411,'Fidel is also used for Tigrinya, Ge\'ez, and Tigre languages.','middle','Ls')
    g+=footer('31','Amharic','A','Script')
    return g+close_svg()

def build_31b():
    g=open_svg()
    g+=t(240,32,'AMHARIC \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g+=t(240,50,'SERIES 31B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SEMITIC PHONOLOGY \u2014 EJECTIVES AND PHARYNGEALS')
    g+=t(240,79,'Amharic is a Semitic language (with Ethiopian Cushitic influence). Notable for ejective and pharyngeal consonants.','middle','L')
    g+=t(240,89,'Ejectives: produced with glottalic airstream \u2014 simultaneous glottal and oral closure, then burst.','middle','Ls')
    g+=hr(97)
    g+=sh(106,'VOWEL SYSTEM \u2014 7 VOWELS')
    vowels=[('/\u0259/','1st order','central mid: like English "about" \u2014 most common vowel'),
            ('/u/','2nd order','high back rounded: like "boot"'),
            ('/i/','3rd order','high front: like "see"'),
            ('/a/','4th order','low central: like "father"'),
            ('/e/','5th order','mid front: like "bed"'),
            ('/\u0268/','6th order','high central: "pure" consonant-adjacent schwa'),
            ('/o/','7th order','mid back rounded: like "go"')]
    for i,(ipa,order,desc) in enumerate(vowels):
        y=116+i*12
        g+=t(55,y,ipa,'middle','Lx'); g+=t(130,y,order,'middle','Lx'); g+=t(330,y,desc,'middle','Lx')
    g+=hr(204)
    g+=sh(213,'CONSONANT INVENTORY \u2014 EJECTIVES AND PHARYNGEALS')
    cons=[('p b','plain bilabial stops','/p/ rare; /b/ common'),
          ("p'",'/p\u02bc/ ejective','glottalic burst: rare in Amharic'),
          ('t d','alveolar stops','dental-alveolar'),
          ("t'",'/t\u02bc/ ejective','\u1273 \u2014 frequent in Amharic'),
          ('k g','velar stops','common'),
          ("k'",'/k\u02bc/ ejective','\u12ab \u2014 very common: k\'al (word)'),
          ('ts dz','affricates','alveolar'),
          ("ts'",'/ts\u02bc/ ejective','\u1338 \u2014 common'),
          ('ch j','palatal affricate','/t\u0283/ /d\u0292/'),
          ("ch'",'/t\u0283\u02bc/ ejective','\u127d \u2014 ejective palatal'),
          ('f s z sh','fricatives','labiodental, alveolar, palatal'),
          ('\u02bf \u02be','/\u02bf \u02be/','pharyngeal fricatives \u2014 Semitic heritage'),
          ('h H','glottal / pharyngeal','two distinct h sounds'),
          ('m n','nasals','bilabial, alveolar'),
          ('l r','lateral / rhotic',''),
          ('w y','glides','')]
    for i,(ltr,ipa,note) in enumerate(cons):
        y=223+i*11
        g+=t(50,y,ltr,'middle','Lx'); g+=t(130,y,ipa,'middle','Lx'); g+=t(330,y,note,'middle','Lx')
    g+=hr(402)
    g+=sh(411,'GEMINATION \u2014 CONSONANT LENGTH IS PHONEMIC')
    g+=t(240,422,'Amharic distinguishes single and geminate (doubled) consonants: a key Semitic feature.','middle','L')
    g+=t(240,432,'\u1270\u1263\u1260 (tebabe) "wrapped" vs \u1270\u1263\u1263\u1260 (tebabbet) "wrapped intensely" \u2014 the double b changes meaning.','middle','Ls')
    g+=t(240,441,'Gemination in Amharic also marks verb-object agreement: y\u0259-s\u0259ma (he hears) vs y\u0259-ss\u0259m\u0259\u02be (he listens).','middle','Ls')
    g+=footer('31','Amharic','B','Phonology')
    return g+close_svg()

def build_31c():
    g=open_svg()
    g+=t(240,32,'AMHARIC \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,50,'SERIES 31C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SOV \u2014 VERB-FINAL \u2014 SEMITIC ROOTS')
    g+=t(240,79,'Amharic is SOV (verb-final), like most Semitic languages. Extensive use of prefixes and suffixes.','middle','L')
    g+=t(240,89,'Semitic root system: 3-consonant roots carry core meaning; vowel patterns and affixes create related words.','middle','Ls')
    g+=t(240,98,'Root s-b-r = "break": s\u0259bb\u0259r\u0259 (he broke), t\u0259s\u0259bb\u0259r\u0259 (it broke), as\u0259bb\u0259r\u0259 (he broke it [causative]).','middle','Ls')
    g+=hr(106)
    g+=sh(115,'VERB CONJUGATION \u2014 n\u0259gg\u0259r\u0259 "spoke / said"')
    conj=[('(\u0300n\u0259gg\u0259r-ku)','1sg','I spoke'),('(\u0300n\u0259gg\u0259r-k)','2sg M','you-m spoke'),
          ('(\u0300n\u0259gg\u0259r-sh)','2sg F','you-f spoke'),('\u0300n\u0259gg\u0259r\u0259','3sg M','he spoke'),
          ('\u0300n\u0259gg\u0259r-\u0259tch','3sg F','she spoke'),('\u0300n\u0259gg\u0259rn\u0259','1pl','we spoke'),
          ('\u0300n\u0259gg\u0259r-\u0259chu','2pl','you pl spoke'),('\u0300n\u0259gg\u0259ru','3pl','they spoke')]
    g+=t(70,125,'Form','middle','Lx'); g+=t(175,125,'Person','middle','Lx'); g+=t(300,125,'Gloss','middle','Lx')
    for i,(form,pers,gl) in enumerate(conj):
        y=134+i*11
        g+=t(70,y,form,'middle','Ls'); g+=t(175,y,pers,'middle','Lx'); g+=t(300,y,gl,'middle','Lx')
    g+=hr(226)
    g+=sh(235,'DEFINITE ARTICLE AND CASE')
    g+=t(240,246,'Definite article: suffix -u (M) or -wa (F) added to noun: b\u0259t (house) \u2192 b\u0259t-u (the house).','middle','Ls')
    g+=t(240,255,'Accusative (object): suffix -\u0259n: b\u0259t-\u0259n (the house, as object).','middle','Ls')
    g+=t(240,264,'Genitive: y\u0259- prefix: y\u0259-b\u0259t b\u0259r (the door of the house).','middle','Ls')
    g+=hr(272)
    g+=sh(281,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[('\u12a3\u12cd\u1295\u1275 / \u12a0\u12ed\u12f0\u120d\u121d','\u0259wunt / ayd\u0259l\u0259m','yes / no'),
           ('\u12a5\u1294 / \u12a0\u1295\u1270','\u0259n\u0259 / ant\u0259','I / you (m)'),
           ('\u12ed\u1205 / \u12eb','\u0259yih / \u0259ya','this / that'),
           ('\u12e8\u1275','\u0259yet','where'),('\u121d\u1295','\u0259mn','what'),
           ('\u121b\u1295','\u0259man','who'),('\u1218\u127d','\u0259m\u0259tch','when'),
           ('\u120d\u121d\u1295','\u0259l\u0259m\u0259n','why'),('\u12cd\u203b','\u0259w\u0259ha','water'),
           ('\u12d5\u1265','\u0259ts\'at','fire'),('\u121d\u12f5\u122d','\u0259m\u0259dr','earth'),
           ('\u1230\u12c8','\u0259s\u0259w','person'),('\u121d\u1352','\u0259m\u0259ts\u02bc\u0268af','book'),
           ('\u130d\u12dc','\u0259g\u0268z\u0259','time'),('\u12c8\u122d\u1215','\u0259w\u0259rh','moon'),
           ('\u12b0\u12ad\u12d3\u1275','\u0259wk\'iat','star'),('\u1209\u1265','\u0259lib','heart'),
           ('\u134d\u1240\u122d','\u0259f\u0268q\u0259r','love'),('\u1270\u1235\u134b','\u0259t\u0259sf\u0268a','freedom'),
           ('\u12a5\u1293\u1235\u1273\u1233','memory (thought)','thought/memory'),
           ('\u12c8\u12f0\u12d3\u12ed\u1275','\u0259w\u0259d\u0259ayt','future'),
           ('\u12d3\u1208\u121d','\u0259al\u0259m','world'),('\u1240\u1293 / \u1218\u132d','\u0259q\u0259na / m\u0259t\u0283\u0259','good / bad'),
           ('\u1201\u1209\u121d','everything','everything'),('\u12d8\u1218\u1295','\u0259\u0259men','life')]
    for i,(am,tr,en) in enumerate(vocab):
        col=0 if i<13 else 1; y=291+(i if i<13 else i-13)*10
        g+=t(30+col*235,y,am,'middle','Las'); g+=t(115+col*235,y,tr,'middle','Lx'); g+=t(215+col*235,y,en,'middle','Lx')
    g+=hr(426)
    g+=sh(435,'COMPOUND VERBS AND AUXILIARY')
    g+=t(240,446,'Amharic uses "light verb" constructions: noun + a\u0259l\u0259 (said/did) for complex meanings.','middle','Ls')
    g+=t(240,455,'t\u0259s\u0259fa (hope) + a\u0259l\u0259 = "hoped" \u00b7 fiq\u0259r (love) + a\u0259l\u0259 = "loved"','middle','Ls')
    g+=footer('31','Amharic','C','Grammar')
    return g+close_svg()

def build_31d():
    g=open_svg()
    g+=t(240,32,'AMHARIC \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,50,'SERIES 31D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(67,'PASSAGE 1 \u2014 ETHIOPIAN PROVERB')
    g+=t(240,79,'\u12a0\u1218\u1233 \u1208\u12ab\u12d5\u1299 \u12eb\u1235\u1233\u1323\u120d።','middle','La')
    g+=t(240,92,'\u0259m\u0259sa l\u0259k\'aN\u0259tu yas\u0259sat\u0259al.','middle','Lx')
    g+=t(240,101,'The fish because-of-its-mouth is-caught.','middle','Lx')
    g+=t(240,110,'"A fish is caught because of its mouth." \u2014 Be careful what you say.','middle','Ls')
    g+=hr(118)
    g+=sh(126,'PASSAGE 2 \u2014 ETHIOPIAN PROVERB')
    g+=t(240,138,'\u12a5\u12f5\u121e\u12cd\u1295 \u12ea\u1270\u1293\u1308\u12cd\u1275 \u12a5\u1295\u12aa\u12f5\u121d \u1270\u1293\u1308\u12ad \u1218\u12d8\u1218\u12f5 \u12ad\u127d\u120d።','middle','Las')
    g+=t(240,151,'\u0259nd\u0259mow\u0259n\u0259 y\u0259tt\u0259nag\u0259wat \u0259nk\u0259d\u0259m t\u0259nag\u0259k m\u0259z\u0259m\u0259d k\u0259ts\'il.','middle','Lx')
    g+=t(240,160,'Before speaking what you will say, think whether it is useful.','middle','Lx')
    g+=t(240,169,'"Before speaking, think whether what you will say is useful."','middle','Ls')
    g+=hr(177)
    g+=sh(185,'PASSAGE 3 \u2014 MOTTO OF ETHIOPIA')
    g+=t(240,197,'\u12a2\u1275\u12ee\u1335\u12eb \u1208\u12a0\u1208\u121d','middle','La')
    g+=t(240,210,'Ityopy\'a l\u0259al\u0259m','middle','Lx')
    g+=t(240,219,'"Ethiopia forever" \u2014 Traditional patriotic expression.','middle','Ls')
    g+=hr(227)
    g+=sh(235,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g+=t(240,247,'\u12ed\u1205 \u12e8\u1270\u1233\u1290\u12cd \u1218\u120d\u12a5\u12ad\u1275 \u1208\u12a5\u1228\u1235\u12ce \u1260\u1290\u1333 \u1270\u12f8\u129d\u1290\u12cd\u1290\u1275 ።','middle','Las')
    g+=t(240,260,'Y\u0259h y\u0259t\u0259saN\u0259w\u0259 m\u0259l\u0259\u0259kt l\u0259\u0259r\u0259swo b\u0259n\u0259ts\'ina t\u0259z\u0259\u0268w\u0259n\u0259w\u0259nt.','middle','Lx')
    g+=t(240,270,'This message  made   for-you freely   who-remembered  future.','middle','Lx')
    g+=t(240,280,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g+=hr(288)
    g+=sh(297,'LANGUAGE NOTE \u2014 "FUTURE" IN AMHARIC')
    g+=t(240,308,'\u12c8\u12f0\u12d3\u12ed\u1275 (w\u0259d\u0259ayt): "future" \u2014 lit. "the ahead / the forward direction". From w\u0259d (toward) + ayt (direction).','middle','L')
    g+=t(240,318,'Amharic has no simple future tense \u2014 uses imperfective + auxiliary y\u0259h\u0259onal (it will be) for future.','middle','Ls')
    g+=t(240,327,'t\u0259z\u0259\u0268w\u0259n\u0259w\u0259nt: "memory / remembrance" \u2014 from root z-w-n "to remember; to be mindful".','middle','Ls')
    g+=t(240,336,'b\u0259n\u0259ts\'ina: "freely / for free" \u2014 from n\u0259ts\u02bc (free / freedom) \u2014 same root as freedom.','middle','Ls')
    g+=hr(344)
    g+=sh(353,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g+=t(240,364,'Amharic is the official language of Ethiopia (~35M native speakers, 100M+ L1+L2).','middle','Ls')
    g+=t(240,373,'Written in the Ethiopic (Fidel) script \u2014 an abugida where each symbol = consonant + vowel order.','middle','Ls')
    g+=t(240,382,'Consult Plate 31A for the full syllabary table and 7 vowel orders.','middle','Ls')
    g+=t(240,391,'Amharic is a Semitic language \u2014 related to Arabic, Hebrew, and Tigrinya.','middle','Ls')
    g+=t(240,400,'Ethiopia has one of the oldest continuous writing traditions in Africa, dating to the 4th century CE.','middle','Ls')
    g+=footer('31','Amharic','D','Text')
    return g+close_svg()

def main():
    plates={'plate31a_amharic_script.svg':build_31a(),'plate31b_amharic_phonology.svg':build_31b(),
            'plate31c_amharic_grammar.svg':build_31c(),'plate31d_amharic_text.svg':build_31d()}
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8'); print(f'Written: {OUT/fname}')

if __name__=='__main__': main()
