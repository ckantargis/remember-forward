#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Tigrinya plate series 34A–34D for Remember Forward."""
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

def build_34a():
    g=open_svg()
    g+=t(240,32,'TIGRINYA \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g+=t(240,50,'SERIES 34A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'TIGRINYA \u2014 SEMITIC \u00b7 ~10 MILLION SPEAKERS')
    g+=t(240,79,'Tigrinya is a Semitic language (Afroasiatic family), official language of Eritrea, spoken in northern Ethiopia.','middle','L')
    g+=t(240,89,'~7 million speakers in Eritrea; ~3 million in Tigray region of Ethiopia.','middle','Ls')
    g+=t(240,98,'Written in the same Ethiopic (Fidel) script as Amharic. Related to Ge\'ez, Tigre, and Amharic.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'ETHIOPIC SCRIPT (FIDEL) \u2014 SHARED WITH AMHARIC')
    g+=t(240,125,'Same abugida system as Amharic (Plate 31A): each symbol = consonant + vowel order.','middle','Ls')
    g+=t(240,134,'7 vowel orders. Tigrinya uses ~276 syllable signs (more than Amharic due to additional consonants).','middle','Ls')
    rows=[
        ('\u1200','\u1201','\u1202','\u1203','\u1204','\u1205','\u1206','h'),
        ('\u1208','\u1209','\u120a','\u120b','\u120c','\u120d','\u120e','l'),
        ('\u1210','\u1211','\u1212','\u1213','\u1214','\u1215','\u1216','H (pharyngeal)'),
        ('\u1220','\u1221','\u1222','\u1223','\u1224','\u1225','\u1226','S (emphatic)'),
        ('\u1228','\u1229','\u122a','\u122b','\u122c','\u122d','\u122e','r'),
        ('\u1230','\u1231','\u1232','\u1233','\u1234','\u1235','\u1236','s'),
        ('\u1238','\u1239','\u123a','\u123b','\u123c','\u123d','\u123e','sh'),
    ]
    vowel_hdrs=['\u0259','u','i','a','e','-','o','C']
    col_xs=[32,72,108,144,180,216,252,290]
    for ci,vh in enumerate(vowel_hdrs): g+=t(col_xs[ci],144,vh,'middle','Lx')
    for ri,row in enumerate(rows):
        y=153+ri*13
        for ci,ch in enumerate(row):
            g+=t(col_xs[ci],y,ch,'middle','La' if ci<7 else 'Lx')
    g+=hr(250)
    g+=sh(259,'ADDITIONAL TIGRINYA CONSONANTS vs AMHARIC')
    g+=t(240,270,'Tigrinya preserves some Semitic sounds reduced or absent in Amharic.','middle','Ls')
    extras=[('\u1290\u1295\u1295','nn \u2014 geminate nasal common in verb morphology'),
            ('\u12b0\u12b5\u120a','\u0175\u0259l\u0268 \u2014 labialised consonants: t\u02b7, d\u02b7, k\u02b7 (rounded)'),
            ('\u12d0\u12d5\u12d8','/\u02bf\u02be/ \u2014 pharyngeal consonants preserved in Tigrinya'),
            ('\u1345\u1340\u134b','/ts\u02bc q\u02bc f\u02bc/ \u2014 ejective series')]
    for i,(ex,desc) in enumerate(extras):
        y=280+i*13
        g+=t(80,y,ex,'middle','La'); g+=t(310,y,desc,'middle','Lx')
    g+=hr(338)
    g+=sh(347,'SCRIPT HISTORY AND STATUS')
    g+=t(240,358,'Ethiopic script: ~4th century CE, derived from South Arabian (Sabaean) script via ancient Ge\'ez.','middle','Ls')
    g+=t(240,367,'Tigrinya uses the same script as Amharic but is a distinct language with distinct grammar.','middle','Ls')
    g+=t(240,376,'Tigrinya became official language of Eritrea at independence (1993). Equal with Arabic in Eritrean constitution.','middle','Ls')
    g+=t(240,385,'In Ethiopia, Tigrinya is the dominant language of the Tigray regional state.','middle','Ls')
    g+=footer('34','Tigrinya','A','Script')
    return g+close_svg()

def build_34b():
    g=open_svg()
    g+=t(240,32,'TIGRINYA \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g+=t(240,50,'SERIES 34B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SEMITIC PHONOLOGY \u2014 EJECTIVES AND PHARYNGEALS')
    g+=t(240,79,'Tigrinya shares the Semitic ejective and pharyngeal consonant inventory with Amharic and Arabic.','middle','L')
    g+=t(240,89,'Ejectives: t\u02bc k\u02bc ts\u02bc q\u02bc \u2014 produced with glottalic (inward) airstream.','middle','Ls')
    g+=t(240,98,'Pharyngeals: /\u02bf/ (voiced) and /\u0127/ or /H/ (voiceless) \u2014 produced in the pharynx, behind the tongue root.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'VOWEL SYSTEM \u2014 7 VOWELS (SAME AS AMHARIC)')
    vowels=[('/\u0259/','1st','central mid \u2014 most common, like "about"'),
            ('/u/','2nd','high back rounded: like "boot"'),
            ('/i/','3rd','high front: like "see"'),
            ('/a/','4th','low central: like "father"'),
            ('/e/','5th','mid front: like "bed"'),
            ('/\u0268/','6th','high central: short vowel adjacent to consonant'),
            ('/o/','7th','mid back: like "go"')]
    for i,(ipa,order,desc) in enumerate(vowels):
        y=125+i*12
        g+=t(55,y,ipa,'middle','Lx'); g+=t(105,y,order,'middle','Lx'); g+=t(310,y,desc,'middle','Lx')
    g+=hr(213)
    g+=sh(222,'KEY DIFFERENCES FROM AMHARIC PHONOLOGY')
    diffs=[('Pharyngeals','Tigrinya PRESERVES /\u02bf/ and /\u0127/','Amharic has largely merged/lost them'),
           ('Labialisation','t\u02b7 d\u02b7 k\u02b7 series present in Tigrinya','less prominent in Amharic'),
           ('Gemination','Both use consonant length as phonemic','same system, different distributions'),
           ('Ejectives','Both have t\u02bc k\u02bc ts\u02bc q\u02bc','Tigrinya q\u02bc is more common'),
           ('Tones','Neither Tigrinya nor Amharic is tonal','unlike many neighboring Cushitic languages')]
    for i,(feat,tig,amh) in enumerate(diffs):
        y=232+i*14
        g+=t(75,y,feat,'middle','Lx'); g+=t(240,y,tig,'middle','Lx'); g+=t(400,y,amh,'middle','Lx')
    g+=hr(306)
    g+=sh(315,'GEMINATION')
    g+=t(240,326,'Tigrinya has phonemic consonant length (gemination) \u2014 doubled consonants change meaning.','middle','L')
    g+=t(240,336,'t\u0259bel\u0259 "he hit" vs t\u0259bbel\u0259 "he fought" \u2014 double b = intensive/reciprocal meaning.','middle','Ls')
    g+=t(240,345,'In Tigrinya, gemination is used systematically to form verb stems and derivational patterns.','middle','Ls')
    g+=hr(353)
    g+=sh(362,'SYLLABLE STRUCTURE')
    g+=t(240,373,'Tigrinya syllables: CV, CVC, CVCC. Clusters possible in codas.','middle','Ls')
    g+=t(240,382,'Epenthetic \u0259: inserted to break up otherwise illegal consonant clusters.','middle','Ls')
    g+=t(240,391,'Word stress: generally on the penultimate syllable; varies with verb morphology.','middle','Ls')
    g+=footer('34','Tigrinya','B','Phonology')
    return g+close_svg()

def build_34c():
    g=open_svg()
    g+=t(240,32,'TIGRINYA \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,50,'SERIES 34C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SOV \u2014 SEMITIC ROOTS \u2014 TWO GENDERS')
    g+=t(240,79,'Tigrinya is SOV (verb-final). Two genders: masculine and feminine. Verb-final, like Amharic.','middle','L')
    g+=t(240,89,'Semitic 3-consonant root system: same root k-t-b gives k\u0259tab\u0259 (he wrote), k\u0259tib (written), m\u0259ktab (office).','middle','Ls')
    g+=hr(97)
    g+=sh(106,'VERB CONJUGATION \u2014 t\u0259haz\u0259 "to take/hold"')
    conj=[('Ani (I)','1sg','(\u0300t\u0259haz-ku)','I took'),
          ('Ant\u0259 (you m)','2sg M','(\u0300t\u0259haz-k\u0259)','you took'),
          ('Antchi (you f)','2sg F','(\u0300t\u0259haz-ki)','you took'),
          ('Nsu (he)','3sg M','\u0300t\u0259haz\u0259','he took'),
          ('Nsa (she)','3sg F','\u0300t\u0259haz-at','she took'),
          ('Nihna (we)','1pl','\u0300t\u0259haz-na','we took'),
          ('Nkhum (you pl m)','2pl M','\u0300t\u0259haz-kum','you took'),
          ('Nik\u0259n (they)','3pl','\u0300t\u0259haz-u','they took')]
    g+=t(80,116,'Subject','middle','Lx'); g+=t(170,116,'Person','middle','Lx')
    g+=t(270,116,'Past form','middle','Lx'); g+=t(400,116,'Gloss','middle','Lx')
    for i,(subj,pers,form,gl) in enumerate(conj):
        y=125+i*11
        g+=t(80,y,subj,'middle','Lx'); g+=t(170,y,pers,'middle','Lx')
        g+=t(270,y,form,'middle','Las'); g+=t(400,y,gl,'middle','Lx')
    g+=hr(215)
    g+=sh(224,'DEFINITE ARTICLE AND CASE')
    g+=t(240,235,'Definite article: suffix -u (M sg) / -a (F sg) / -om (M pl) / -en (F pl).','middle','Ls')
    g+=t(240,244,'n\u0259br (tiger, indef.) \u2192 n\u0259bru (the tiger, M def.)','middle','Ls')
    g+=t(240,253,'Accusative/object: not morphologically marked, conveyed by SOV word order.','middle','Ls')
    g+=hr(261)
    g+=sh(270,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[('\u12a0\u12af / \u12ed\u12d0\u1295','\u0259aw / yihayn','yes / no'),
           ('\u12a2\u1295\u12eb / \u12d3\u1295\u1270\u12db','\u0259in\u0259ya / ant\u0259z','I / you (m)'),
           ('\u12ad\u12ed / ቲ\u12eb','\u0259k\u0268y / t\u0268ya','this / that'),
           ('\u12d8\u12ed\u1295?','\u0259z\u0268yn','where'),('\u121b\u1295?','man','what'),
           ('\u12d8\u12ed\u1295 ሰብ?','which person','who'),('\u12a2\u1295\u1272\u12eb?','when','when'),
           ('\u1295\u1230\u12ed?','why','why'),('\u121d\u12ed\u1205','\u0259m\u0268yih','water'),
           ('\u131b','\u0259ts\u02bc at','fire'),('\u12d5\u1265\u122a','\u0259br\u0268','earth'),
           ('\u1230\u1265','s\u0259b','person'),('\u121d\u1295\u1350\u134d','m\u0259nt\u0259f','book'),
           ('\u130d\u12dc','\u0259g\u0268z\u0259','time'),('\u12c8\u122d\u1215','w\u0259rh','moon'),
           ('\u12b0\u12ad\u12d5\u1275','wk\u02bcat','star'),('\u1209\u1265','l\u0268b','heart'),
           ('\u134d\u1240\u122d','f\u0268q\u0259r','love'),('\u1215\u122d\u1290\u1275','h\u0268rn\u0259t','freedom'),
           ('\u12d8\u12ab\u122e\u1295','z\u0268karun','memory'),('\u1218\u1340\u12f0\u1218\u1273','m\u0259q\u0259d\u0259m\u0259ta','future'),
           ('\u12d3\u1208\u121d','al\u0259m','world'),('\u1277\u1261 / \u12d8\u12ed\u1295 ዘ\u12ed\u12f0\u1209','\u0175\u0259bu / bad','good / bad'),
           ('\u1200\u1209\u1348 \u130d\u12dc','everything','everything'),('\u121d\u12d8\u1293\u12ee\u1275','m\u0268z\u0259naw\u0268t','life')]
    for i,(tig,tr,en) in enumerate(vocab):
        col=0 if i<13 else 1; y=280+(i if i<13 else i-13)*10
        g+=t(25+col*235,y,tig,'middle','Las'); g+=t(110+col*235,y,tr,'middle','Lx'); g+=t(200+col*235,y,en,'middle','Lx')
    g+=footer('34','Tigrinya','C','Grammar')
    return g+close_svg()

def build_34d():
    g=open_svg()
    g+=t(240,32,'TIGRINYA \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,50,'SERIES 34D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(67,'PASSAGE 1 \u2014 ERITREAN PROVERB')
    g+=t(240,79,'\u12e8\u12d0 \u1259\u1271 \u12c8\u12f0 \u12d9\u1203 \u12ed\u1275\u1296\u1298 \u12a1\u1208\u121d።','middle','La')
    g+=t(240,92,'y\u0259ha q\u0268t\u0268 w\u0259d\u0259 z\u0268h\u0259a y\u0259tn\u0259bib al\u0259m.','middle','Lx')
    g+=t(240,101,'The person who goes toward the light does not stumble.','middle','Lx')
    g+=t(240,110,'"The one who walks toward the light does not stumble."','middle','Ls')
    g+=hr(118)
    g+=sh(126,'PASSAGE 2 \u2014 TIGRINYA PROVERB')
    g+=t(240,138,'\u12d8\u12ed\u1295 \u12d0\u12ed\u1295 \u12a5\u1295\u1270\u12cd \u12aa\u1275\u12ad\u1208\u1270 \u12ab\u12d3\u12ed \u1265\u12d8\u12d3 \u12a3\u1270\u12cb።','middle','Las')
    g+=t(240,151,'That which you do not speak, even the wisest person does not know.','middle','Lx')
    g+=t(240,160,'"What you do not say, even the wise do not know." \u2014 Speak your needs.','middle','Ls')
    g+=hr(168)
    g+=sh(176,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g+=t(240,188,'\u12ed\u1205 \u1218\u1230\u12d8\u1272 \u1308\u12ed\u122d\u1290 \u1265\u1323\u12d8\u12a8\u1275 \u1265\u12c8\u1328 \u12d8\u12e8\u1218\u1340\u12f0\u1218\u1273 \u12d8\u12b0\u12ab\u12f1 ።','middle','Las')
    g+=t(240,201,'Y\u0259h m\u0259s\u0259z\u0259t\u0268 g\u0259yr\u0259n\u0259 b\u0268tat\u0259z\u0259k\u0259t b\u0268w\u0259q\u0268 z\u0259y\u0259m\u0259q\u0259d\u0259m\u0259ta z\u0259w\u0259kad\u0268.','middle','Lx')
    g+=t(240,211,'This message for-you freely by-those who-the-future remembered.','middle','Lx')
    g+=t(240,221,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g+=hr(229)
    g+=sh(238,'LANGUAGE NOTE \u2014 "FUTURE" IN TIGRINYA')
    g+=t(240,249,'\u1218\u1340\u12f0\u1218\u1273 (m\u0259q\u0259d\u0259m\u0259ta): "future / ahead" \u2014 from q\u0259d\u0259m\u0259 (to precede / to go before).','middle','L')
    g+=t(240,259,'Literally "the preceding-ness" \u2014 the future as what stands ahead and goes before us.','middle','Ls')
    g+=t(240,268,'\u12d8\u12b0\u12ab\u12f1 (z\u0259w\u0259kad\u0268): "remembered" \u2014 from root w-k-d / z-k-r (to remember, to be mindful).','middle','Ls')
    g+=t(240,277,'\u1265\u12c8\u1328 (b\u0268w\u0259q\u0268): "freely / for free" \u2014 literally "without price".','middle','Ls')
    g+=hr(285)
    g+=sh(294,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g+=t(240,305,'Tigrinya is the official language of Eritrea and the dominant language of the Tigray region of Ethiopia.','middle','Ls')
    g+=t(240,314,'~10 million speakers total. Written in the Ethiopic (Fidel) script \u2014 same as Amharic (Plate 31A).','middle','Ls')
    g+=t(240,323,'Tigrinya is a Semitic language (Afroasiatic) \u2014 related to Arabic, Amharic, Hebrew, and Ge\'ez.','middle','Ls')
    g+=t(240,332,'Ge\'ez (Classical Ethiopic) is the liturgical ancestor of Tigrinya, still used in church services.','middle','Ls')
    g+=footer('34','Tigrinya','D','Text')
    return g+close_svg()

def main():
    plates={'plate34a_tigrinya_script.svg':build_34a(),'plate34b_tigrinya_phonology.svg':build_34b(),
            'plate34c_tigrinya_grammar.svg':build_34c(),'plate34d_tigrinya_text.svg':build_34d()}
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8'); print(f'Written: {OUT/fname}')

if __name__=='__main__': main()
