#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Portuguese plate series 27A–27D for Remember Forward."""

from pathlib import Path
OUT = Path(__file__).parent

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n'
        '  text { font-family: Georgia, serif; }\n'
        '  .T  { font-size:12px; font-weight:bold; letter-spacing:2px; }\n'
        '  .S  { font-size:7px; letter-spacing:1.5px; }\n'
        '  .H  { font-size:6.5px; font-weight:bold; letter-spacing:2.5px; }\n'
        '  .L  { font-size:7px; }\n'
        '  .Ls { font-size:6px; }\n'
        '  .Lx { font-size:5.5px; }\n'
        '  .M  { font-size:6px; letter-spacing:1px; }\n'
        '  .F  { font-size:7px; font-style:italic; }\n'
        '  .Fb { font-size:7.5px; font-weight:bold; }\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n'
    )

def close_svg(): return '</svg>\n'

def t(x,y,s,a='middle',c='L',extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{esc(s)}</text>\n'

def hr(y,x1=20,x2=460,sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y,txt):
    return t(240,y,f'\u2014 {txt} \u2014','middle','H')

def footer(num,lang,letter,desc):
    return (hr(625)
        + t(240,620,f'SERIES {num} \u00b7 {lang.upper()} \u00b7 PLATE {letter} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        + hr(633)
        + t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        + t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))

def build_27a():
    g = open_svg()
    g += t(240,32,'PORTUGUESE \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g += t(240,50,'SERIES 27A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'THE PORTUGUESE ALPHABET \u2014 26 LETTERS + DIACRITICS')
    g += t(240,79,'Portuguese uses the standard 26-letter Latin alphabet. Since 2009 reform, k, w, y are official letters.','middle','L')
    g += t(240,89,'Rich diacritic system: acute (\u00e1\u00e9\u00ed\u00f3\u00fa), grave (\u00e0), circumflex (\u00e2\u00ea\u00f4), tilde (\u00e3\u00f5), cedilla (\u00e7).','middle','Ls')
    g += t(240,98,'The nasal vowels (\u00e3, \u00f5, \u00e3o, em, im) are a distinctive feature absent from Spanish.','middle','Ls')
    g += hr(106)

    g += sh(115,'DIACRITICS AND THEIR FUNCTIONS')
    diac=[
        ('\u00e1 \u00e9 \u00ed \u00f3 \u00fa','Acute','Marks stress + open vowel quality'),
        ('\u00e0','Grave','Marks contraction only: a + a = \u00e0 (to the-f)'),
        ('\u00e2 \u00ea \u00f4','Circumflex','Marks stress + close (narrow) vowel quality'),
        ('\u00e3 \u00f5','Tilde','Nasalisation: irm\u00e3 (sister), p\u00f5e (puts)'),
        ('\u00e7','Cedilla','C before a,o,u = /s/: fran\u00e7a, \u00e7\u00e3o'),
    ]
    for i,(char,name,func) in enumerate(diac):
        y=125+i*12
        g += t(55,y,char,'middle','Ls'); g += t(115,y,name,'middle','Lx'); g += t(320,y,func,'middle','Lx')
    g += hr(188)

    g += sh(197,'NASAL VOWELS \u2014 A DEFINING FEATURE')
    g += t(240,208,'Portuguese nasalises vowels before n/m or with tilde. These are separate phonemes, not allophonic.','middle','L')
    nasals=[
        ('\u00e3','[\u0250\u0303]','irm\u00e3 (sister), am\u00e3nh\u00e3 (tomorrow), p\u00e3o (bread)'),
        ('\u00f5','[o\u0303]','p\u00f5e (puts), bot\u00f5es (buttons)'),
        ('em/en','[\u025b\u0303]','tempo (time), dentro (inside)'),
        ('im/in','[\u0268\u0303]','sim (yes), cinco (five)'),
        ('om/on','[o\u0303]','som (sound), onde (where)'),
        ('um/un','[u\u0303]','um (one), mundo (world)'),
        ('\u00e3o','[\u0250\u0303w\u0303]','m\u00e3o (hand), cora\u00e7\u00e3o (heart), n\u00e3o (no)'),
    ]
    for i,(v,ipa,ex) in enumerate(nasals):
        y=218+i*11
        g += t(45,y,v,'middle','Ls'); g += t(100,y,ipa,'middle','Lx'); g += t(310,y,ex,'middle','Lx')
    g += hr(300)

    g += sh(309,'EUROPEAN VS BRAZILIAN PORTUGUESE \u2014 KEY DIFFERENCES')
    g += t(240,320,'Portuguese is spoken by ~250 million people. Brazil alone has ~215 million speakers.','middle','Ls')
    diffs=[
        ('Vowels','EP: unstressed vowels heavily reduced','BP: vowels more open and stable'),
        ('S before C/P/T','EP: /\u0283/ (sh)','BP: /s/'),
        ('te/di','EP: /te/ /di/','BP: /t\u0283i/ /d\u0292i/ (palatalised)'),
        ('Second person','EP: tu + voc\u00ea','BP: voc\u00ea dominant (3rd-person verb)'),
        ('Clitic position','EP: verb-clitic (f\u00e1-lo)','BP: clitic-verb (lo fazer) or drop'),
        ('Vocabulary','quinh\u00e3o, autocarro (EP)','quinho, \u00f4nibus (BP)'),
    ]
    for i,(feat,ep,bp) in enumerate(diffs):
        y=330+i*12
        g += t(70,y,feat,'middle','Lx'); g += t(215,y,ep,'middle','Lx'); g += t(375,y,bp,'middle','Lx')
    g += hr(407)

    g += sh(416,'SCRIPT HISTORY')
    g += t(240,427,'Latin spoken in Iberia after Roman conquest (218 BCE). Vulgar Latin differentiated into Galician-Portuguese by ~9th c.','middle','Ls')
    g += t(240,436,'Oldest document: Noticia de Torto (~1214). First major literature: Cantigas de Santa Maria (13th c.).','middle','Ls')
    g += t(240,445,'15th\u201316th c.: Age of Exploration spreads Portuguese to Brazil, Angola, Mozambique, Goa, Macau, Cape Verde.','middle','Ls')
    g += t(240,454,'Today: official language of 9 countries on 4 continents. 3rd most spoken European language globally.','middle','Ls')

    g += footer('27','Portuguese','A','Script')
    g += close_svg()
    return g

def build_27b():
    g = open_svg()
    g += t(240,32,'PORTUGUESE \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g += t(240,50,'SERIES 27B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'VOWEL SYSTEM \u2014 ORAL AND NASAL')
    g += t(240,79,'Portuguese has 7 oral vowels + 5 nasal vowels \u2014 one of the most complex vowel systems among Romance languages.','middle','L')
    oral=[('/a/','a','open low: p\u00e1 (spade)'),('/\u00e6/ or /\u0250/','a unstressed','reduced in EP: casa [k\u00e6z\u0250]'),
          ('/e/','e close','m\u00eas (month)'),('/\u025b/','e open',('p\u00e9 (foot)')),
          ('/i/','i','vir (come)'),('/o/','o close','av\u00f4 (grandfather)'),
          ('/\u0254/','o open','p\u00f3 (dust)'),('/u/','u','luz (light)')]
    for i,(ipa,ltr,ex) in enumerate(oral):
        y=89+i*11
        g += t(55,y,ipa,'middle','Lx'); g += t(130,y,ltr,'middle','Lx'); g += t(310,y,ex,'middle','Lx')
    g += hr(183)

    g += sh(192,'CONSONANT INVENTORY')
    cons=[
        ('p b','/p b/','bilabial stops','pato, boca'),
        ('t d','/t d/','alveolar stops','EP dental; BP: /t\u0283/ /d\u0292/ before i'),
        ('k g','/k \u0261/','velar stops','casa, gato'),
        ('f v','/f v/','labiodentals','fogo, voz'),
        ('s z','/s z/','alveolar frict.','sol, casa [kaza] (BP) / [kaz\u0250] (EP)'),
        ('\u0283 \u0292','/\u0283 \u0292/','palatal frict.','chave, hoje; EP: s before voiceless C'),
        ('m n','/m n/','nasals','mar, n\u00e3o'),
        ('\u0272','/\u0272/','palatal nasal','ninho (nest), junho (June)'),
        ('l','/l/','lateral','lua; EP: [l]; BP word-final: [w]'),
        ('\u028e','/\u028e/','palatal lateral','filho (son), mulher (woman)'),
        ('r','/\u0279/ or /\u0281/','rhotic','caro (EP tap), carro (EP/BP trill or uvular)'),
        ('\u0281','/\u0281/','uvular (EP initial)','r\u00e1pido, rosa \u2014 EP initial r = uvular'),
    ]
    for i,(ltr,ipa,label,ex) in enumerate(cons):
        y=202+i*12
        g += t(40,y,ltr,'middle','Ls'); g += t(88,y,ipa,'middle','Lx')
        g += t(162,y,label,'middle','Lx'); g += t(355,y,ex,'middle','Lx')
    g += hr(350)

    g += sh(359,'STRESS AND VOWEL REDUCTION')
    g += t(240,370,'Stress: penultimate by default; acute/circumflex marks exceptions. Written accent obligatory when stress deviates.','middle','Ls')
    g += t(240,379,'EP vowel reduction: unstressed /e o a/ reduce heavily toward [\u0259 u \u0250] \u2014 makes EP sound very consonantal.','middle','Ls')
    g += t(240,388,'BP vowel reduction: minimal. Unstressed vowels stay open. BP sounds more "vowel-heavy" than EP.','middle','Ls')
    g += t(240,397,'Example: palavra (word) \u2014 EP [p\u0250l\u02c8v\u0250\u0281\u0250], BP [pa\u02c8lavr\u0250] \u2014 same word, very different realisation.','middle','Ls')
    g += hr(405)

    g += sh(414,'SIBILANT SYSTEM')
    g += t(240,425,'EP: s/z before voiceless C \u2192 [\u0283] (sh); before voiced C \u2192 [\u0292] (zh): Lisboa = Lix-boa','middle','Ls')
    g += t(240,434,'BP: s remains /s/ in most positions \u2014 the EP sibilant rule does not apply.','middle','Ls')
    g += t(240,443,'ch = /\u0283/ in both varieties: chave "key", chocolate.','middle','Ls')
    g += t(240,452,'lh = /\u028e/ (palatal lateral): ilha "island", filho "son".','middle','Ls')
    g += t(240,461,'nh = /\u0272/ (palatal nasal): ninho "nest", caminho "path".','middle','Ls')

    g += footer('27','Portuguese','B','Phonology')
    g += close_svg()
    return g

def build_27c():
    g = open_svg()
    g += t(240,32,'PORTUGUESE \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g += t(240,50,'SERIES 27C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'SVO \u2014 NULL SUBJECT \u2014 TWO GENDERS')
    g += t(240,79,'Portuguese is SVO, null-subject, two genders (M/F). Very similar structure to Spanish.','middle','L')
    g += t(240,89,'Key differences from Spanish: nasal vowels, personal infinitive, future subjunctive, mesoclisis.','middle','Ls')
    g += hr(97)

    g += sh(106,'VERB CONJUGATION \u2014 falar "to speak"')
    pres=[('eu','falo','I speak'),('tu','falas','you (inf)'),('ele/ela','fala','he/she'),
          ('n\u00f3s','falamos','we'),('v\u00f3s','falais','you pl (archaic)'),('eles','falam','they')]
    pret=[('eu','falei','I spoke'),('tu','falaste','you'),('ele/ela','falou','he/she'),
          ('n\u00f3s','fal\u00e1mos','we'),('v\u00f3s','flastes','you pl'),('eles','falaram','they')]
    g += t(105,116,'Present Indicative','middle','Lx'); g += t(355,116,'Preterite','middle','Lx')
    for i,((p1,f1,gl1),(p2,f2,gl2)) in enumerate(zip(pres,pret)):
        y=125+i*11
        g += t(42,y,p1,'middle','Lx'); g += t(110,y,f1,'middle','Ls'); g += t(200,y,gl1,'middle','Lx')
        g += t(275,y,p2,'middle','Lx'); g += t(345,y,f2,'middle','Ls'); g += t(435,y,gl2,'start','Lx')
    g += hr(199)

    g += sh(208,'PERSONAL INFINITIVE \u2014 UNIQUE FEATURE')
    g += t(240,219,'Portuguese is rare in having an INFLECTED infinitive \u2014 it takes subject endings even in the infinitive.','middle','L')
    g += t(240,229,'Standard: "\u00c9 importante trabalhar" (It is important to work \u2014 impersonal)','middle','Ls')
    g += t(240,238,'Personal: "\u00c9 importante trabalharmos" (It is important for us to work \u2014 specified subject)','middle','Ls')
    g += t(240,247,'Forms: trabalhar / trabalhares / trabalhar / trabalharmos / trabalhardes / trabalharem','middle','Lx')
    g += hr(255)

    g += sh(264,'FUTURE SUBJUNCTIVE \u2014 ANOTHER UNIQUE FEATURE')
    g += t(240,275,'Portuguese retains the future subjunctive, lost in Spanish: used in temporal/conditional clauses.','middle','Ls')
    g += t(240,284,'"Quando chegar" = "When (he/she) arrives" (future sub.) \u2014 Spanish uses present sub. here.','middle','Ls')
    g += t(240,293,'"Se voc\u00ea quiser" = "If you want" \u2014 future sub.; Spanish: "Si quieres" (present indicative).','middle','Ls')
    g += hr(301)

    g += sh(310,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[
        ('sim / n\u00e3o','yes / no'),('eu / voc\u00ea','I / you'),('isto / isso','this / that'),
        ('onde','where'),('o que','what'),('quem','who'),('quando','when'),('por qu\u00ea','why'),
        ('\u00e1gua','water'),('fogo','fire'),('terra','earth'),('pessoa','person'),
        ('livro','book'),('tempo','time'),('lua','moon'),('estrela','star'),
        ('cora\u00e7\u00e3o','heart'),('amor','love'),('liberdade','freedom'),
        ('mem\u00f3ria','memory'),('futuro','future'),('mundo','world'),
        ('bom / mau','good / bad'),('tudo','everything'),('vida','life'),
    ]
    for i,(pt,en) in enumerate(vocab):
        col=0 if i<13 else 1
        y=320+(i if i<13 else i-13)*10
        g += t(50+col*230,y,pt,'middle','Ls'); g += t(175+col*230,y,en,'middle','Lx')
    g += hr(453)

    g += sh(462,'SER VS ESTAR AND FICAR')
    g += t(240,473,'Portuguese has three "to be" verbs: ser (identity), estar (state/position), ficar (become/stay).','middle','L')
    g += t(240,483,'Ela \u00e9 professora (She IS a teacher \u2014 ser, identity).','middle','Ls')
    g += t(240,492,'Ela est\u00e1 cansada (She IS tired \u2014 estar, state).','middle','Ls')
    g += t(240,501,'Ela ficou triste (She BECAME sad / She STAYED sad \u2014 ficar, change or continuation of state).','middle','Ls')
    g += t(240,510,'Ficar distinguishes Portuguese from Spanish, which uses quedarse or ponerse for similar meanings.','middle','Ls')

    g += footer('27','Portuguese','C','Grammar')
    g += close_svg()
    return g

def build_27d():
    g = open_svg()
    g += t(240,32,'PORTUGUESE \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g += t(240,50,'SERIES 27D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(67,'PASSAGE 1 \u2014 CAM\u00d5ES, OS LUS\u00cdADAS I.1 (1572)')
    g += t(240,78,'As armas e os bar\u00f5es assinalados,','middle','L')
    g += t(240,88,'The arms  and the barons  distinguished,','middle','Lx')
    g += t(240,97,'Que da Ocidental praia Lusitana,','middle','L')
    g += t(240,107,'Who from-the Western shore  Lusitanian,','middle','Lx')
    g += t(240,116,'"The arms and the distinguished heroes who from the Western Lusitanian shore\u2026" \u2014 Portugal\'s national epic.','middle','Ls')
    g += hr(124)

    g += sh(132,'PASSAGE 2 \u2014 FERNANDO PESSOA, MENSAGEM (1934)')
    g += t(240,143,'Tudo vale a pena','middle','L')
    g += t(240,153,'Everything is-worth the trouble','middle','Lx')
    g += t(240,162,'Se a alma n\u00e3o \u00e9 pequena.','middle','L')
    g += t(240,172,'If  the soul not is small.','middle','Lx')
    g += t(240,181,'"Everything is worth the trouble if the soul is not small." \u2014 Portugal\'s most celebrated modern poet.','middle','Ls')
    g += hr(189)

    g += sh(197,'PASSAGE 3 \u2014 CLARICE LISPECTOR, A PA\u00cdX\u00c3O SEGUNDO G.H. (1964)')
    g += t(240,208,'Eu te pergunto: existe a alegria? e tu me respondes com a exist\u00eancia da alegria.','middle','L')
    g += t(240,218,'I  you ask:   exists the joy?   and you me answer  with the existence  of-the joy.','middle','Lx')
    g += t(240,227,'"I ask you: does joy exist? and you answer me with the existence of joy." \u2014 Brazilian modernist.','middle','Ls')
    g += hr(235)

    g += sh(243,'PASSAGE 4 \u2014 PORTUGUESE PROVERBS')
    g += t(240,254,'Devagar se vai ao longe.','middle','L')
    g += t(240,264,'Slowly oneself goes to far. \u2014 "Slowly but surely."','middle','Lx')
    g += t(240,274,'Quem n\u00e3o arrisca n\u00e3o petisca.','middle','L')
    g += t(240,284,'Who not risks  not tastes. \u2014 "Nothing ventured, nothing gained."','middle','Xp')
    g += hr(292)

    g += sh(300,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240,312,'Esta mensagem foi feita para voc\u00ea, gratuitamente, por pessoas que se lembraram do futuro.','middle','L')
    g += t(240,323,'This message  was made  for  you    freely,         by  people  who  remembered  of-the future.','middle','Lx')
    g += t(240,333,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g += hr(341)

    g += sh(350,'LANGUAGE NOTE \u2014 "FUTURE" IN PORTUGUESE')
    g += t(240,361,'futuro: same Latin root as Spanish/French. Portuguese future tense: falarei, falar\u00e1s, falar\u00e1\u2026','middle','L')
    g += t(240,371,'Unique feature: MESOCLISIS \u2014 object pronouns can be inserted into the future/conditional:','middle','Ls')
    g += t(240,380,'Dar-te-ei (I will give you) = dar + te + ei \u2014 pronoun inserted into the verb form. Now rare in BP.','middle','Ls')
    g += t(240,389,'lembrar-se de: to remember (lit. "to remind oneself of") \u2014 reflexive construction.','middle','Ls')
    g += t(240,398,'gratuitamente: from gratuito \u2014 same Latin root as Spanish/French gratuit/gratuito.','middle','Ls')
    g += hr(406)

    g += sh(415,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g += t(240,426,'Portuguese is spoken by ~250 million people as a native language \u2014 3rd most spoken European language.','middle','Ls')
    g += t(240,435,'Countries: Brazil, Portugal, Angola, Mozambique, Cape Verde, Guinea-Bissau, S\u00e3o Tom\u00e9, East Timor, Macau.','middle','Ls')
    g += t(240,444,'Two major standards: European Portuguese (EP) and Brazilian Portuguese (BP) \u2014 mutually intelligible.','middle','Ls')
    g += t(240,453,'Uses the Latin alphabet with cedilla (\u00e7) and nasal vowel markers (\u00e3 \u00f5). Closely related to Spanish.','middle','Ls')
    g += t(240,462,'Descended from Galician-Portuguese, spoken in northwestern Iberia by ~14th century.','middle','Ls')

    g += footer('27','Portuguese','D','Text')
    g += close_svg()
    return g

def main():
    plates = {
        'plate27a_portuguese_script.svg': build_27a(),
        'plate27b_portuguese_phonology.svg': build_27b(),
        'plate27c_portuguese_grammar.svg': build_27c(),
        'plate27d_portuguese_text.svg': build_27d(),
    }
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8')
        print(f'Written: {OUT/fname}')

if __name__ == '__main__':
    main()
