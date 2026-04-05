#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Spanish plate series 26A–26D for Remember Forward."""

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

def build_26a():
    g = open_svg()
    g += t(240,32,'SPANISH — SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g += t(240,50,'SERIES 26A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'THE SPANISH ALPHABET — 27 LETTERS')
    g += t(240,79,'Spanish uses the Latin alphabet with one addition: \u00f1 (e\u00f1e). The alphabet has 27 letters.','middle','L')
    g += t(240,89,'Digraphs ch and ll were treated as single letters 1803\u20132010; now alphabetised as two-letter sequences.','middle','Ls')
    g += t(240,98,'Spanish orthography is highly phonemic \u2014 spelling closely matches pronunciation.','middle','Ls')
    g += hr(106)

    g += sh(115,'THE 27 LETTERS WITH NAMES AND KEY SOUNDS')
    letters = [
        ('A a','a','/a/'),('B b','be','/b/\u2013[v]'),('C c','ce','/k/ or /s/\u2020'),
        ('D d','de','/d/\u2013[\u00f0]'),('E e','e','/e/'),('F f','efe','/f/'),
        ('G g','ge','/\u0261/ or /x/'),('H h','hache','silent'),('I i','i','/i/'),
        ('J j','jota','/x/'),('K k','ka','/k/ loans'),('L l','ele','/l/'),
        ('M m','eme','/m/'),('N n','ene','/n/'),('\u00d1 \u00f1','e\u00f1e','/\u0272/'),
        ('O o','o','/o/'),('P p','pe','/p/'),('Q q','cu','/k/ in qu-'),
        ('R r','erre','/r/ or /\u0279/'),('S s','ese','/s/'),('T t','te','/t/'),
        ('U u','u','/u/'),('V v','uve','/b/\u2013[v]'),('W w','doble uve','loans'),
        ('X x','equis','/ks/ or /s/'),('Y y','ye','/j/ or /i/'),('Z z','zeta','/s/ or /\u03b8/')
    ]
    cols = [(40,130,220),(310,400,460)]
    half = 14
    for i,(ltr,name,ipa) in enumerate(letters):
        if i < half:
            cx = cols[0]
            y = 125 + i*9
        else:
            cx = cols[1]
            y = 125 + (i-half)*9
        g += t(cx[0],y,ltr,'middle','Ls')
        g += t(cx[1],y,name,'middle','Lx')
        g += t(cx[2],y,ipa,'middle','Lx')
    g += t(240,256,'\u2020 C = /k/ before a,o,u; /s/ (Americas) or /\u03b8/ (Castilian Spain) before e,i','middle','Lx')
    g += hr(264)

    g += sh(273,'ACCENT MARKS AND SPECIAL CHARACTERS')
    g += t(240,284,'Acute accent (\u00e1\u00e9\u00ed\u00f3\u00fa): marks stress when it falls outside the default pattern, or disambiguates homophones.','middle','Ls')
    g += t(240,293,'Default stress: penultimate syllable if word ends in vowel/n/s; final syllable otherwise.','middle','Ls')
    g += t(240,302,'Tilde (\u00f1): distinct letter, /\u0272/ palatal nasal \u2014 ma\u00f1ana, se\u00f1or, espa\u00f1ol.','middle','Ls')
    g += t(240,311,'Di\u00e9resis (\u00fc): marks that u is pronounced in g\u00fce/g\u00fci: ping\u00fcino, cig\u00fce\u00f1a.','middle','Ls')
    g += t(240,320,'Inverted punctuation: sentences begin with \u00bf (question) or \u00a1 (exclamation): \u00bfC\u00f3mo est\u00e1s?','middle','Ls')
    g += hr(328)

    g += sh(337,'DIALECTAL VARIATION IN WRITING AND SOUND')
    dialects = [
        ('Castilian Spain','c/z before e,i = /\u03b8/ (thin)','vosotros form used'),
        ('Latin America','c/z before e,i = /s/ (seseo)','vosotros absent; ustedes'),
        ('R\u00edo Plata (Arg/Uru)','seseo + yeismo (/\u0292/ for ll/y)','vos instead of t\u00fa'),
        ('Andean Spanish','vowel reduction; Quechua influence','strong /r/ distinction'),
        ('Caribbean','final /s/ aspirated or deleted','coda consonants weakened'),
    ]
    for i,(dial,phon,gram) in enumerate(dialects):
        y = 347+i*14
        g += t(100,y,dial,'middle','Ls')
        g += t(270,y,phon,'middle','Lx')
        g += t(415,y,gram,'middle','Lx')
    g += hr(423)

    g += sh(432,'SPANISH NUMERALS AND SCRIPT HISTORY')
    g += t(240,443,'Spanish uses standard Western Arabic numerals 0\u20139.','middle','Ls')
    g += t(240,452,'Latin alphabet adopted with Christianisation of Iberia (1st\u20136th c. CE).','middle','Ls')
    g += t(240,461,'Old Spanish (El Cid, ~1140): c, \u00e7, j, x, y used for sounds lost later. Modern orthography stabilised ~1741 (RAE).','middle','Ls')
    g += t(240,470,'Real Academia Espa\u00f1ola (RAE, founded 1713): codifies spelling, grammar, and vocabulary for 20+ countries.','middle','Ls')
    g += t(240,479,'Spanish is written by ~500 million native speakers across 20+ countries on 4 continents.','middle','Ls')
    g += t(240,488,'2nd most spoken native language on Earth after Mandarin Chinese.','middle','Ls')

    g += footer('26','Spanish','A','Script')
    g += close_svg()
    return g

def build_26b():
    g = open_svg()
    g += t(240,32,'SPANISH — PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g += t(240,50,'SERIES 26B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'VOWEL SYSTEM \u2014 5 PURE VOWELS')
    g += t(240,79,'Spanish has 5 vowel phonemes \u2014 one of the simplest vowel systems among major world languages.','middle','L')
    g += t(240,89,'All vowels are short and pure (no diphthongisation). Consistent across most dialects.','middle','Ls')
    vowels = [
        ('/a/','a','low central','padre, mar, casa'),
        ('/e/','e','mid front','mesa, tres, leche'),
        ('/i/','i','high front','vida, mi, hijo'),
        ('/o/','o','mid back','noche, voz, como'),
        ('/u/','u','high back','luna, luz, uno'),
    ]
    for i,(ipa,ltr,qual,ex) in enumerate(vowels):
        y = 99+i*12
        g += t(50,y,ipa,'middle','Ls')
        g += t(95,y,ltr,'middle','Ls')
        g += t(180,y,qual,'middle','Lx')
        g += t(360,y,ex,'middle','Lx')
    g += t(240,162,'Diphthongs: rising (ia,ie,io,iu,ua,ue,ui,uo) and falling (ai,ei,oi,au,eu,ou) \u2014 two vowels in one syllable.','middle','Ls')
    g += hr(170)

    g += sh(179,'CONSONANT INVENTORY')
    cons = [
        ('p b','/p b/','bilabial stops','B/V identical: both /b/ \u2013 [v] between vowels'),
        ('t d','/t d/','dental stops','D = [\u00f0] between vowels: nada [na\u00f0a]'),
        ('k g','/k \u0261/','velar stops','G = [\u0263] between vowels: lago [la\u0263o]'),
        ('f','/f/','labiodental','fuerza, f\u00e1cil'),
        ('s','/s/','alveolar frict.','always voiceless in most dialects'),
        ('x','/x/','velar frict.','j always = /x/: joven, ojo, rojo'),
        ('\u03b8','/\u03b8/','dental frict.','Castilian c/z: cena, zapato (NOT in Latin Am.)'),
        ('t\u0283','/t\u0283/','affricate','ch: noche, muchacho'),
        ('m n','/m n/','nasals','n = [\u014b] before velars: banco [ba\u014bko]'),
        ('\u0272','/\u0272/','palatal nasal','\u00f1: ma\u00f1ana, espa\u00f1ol'),
        ('l','/l/','lateral','leche, sol'),
        ('\u028e','/\u028e/','palatal lateral','ll (Castilian): llave, calle \u2014 merged with /j/ elsewhere'),
        ('r','/\u0279/','tap','single r between vowels: caro, pero'),
        ('rr','/r/','trill','double r / initial r: perro, rosa'),
        ('j','/j/','palatal glide','ya, yo, hierba'),
    ]
    for i,(ltr,ipa,label,note) in enumerate(cons):
        y = 189+i*12
        g += t(40,y,ltr,'middle','Ls')
        g += t(88,y,ipa,'middle','Lx')
        g += t(165,y,label,'middle','Lx')
        g += t(355,y,note,'middle','Lx')
    g += hr(380)

    g += sh(389,'STRESS RULES')
    g += t(240,400,'1. Words ending in vowel, -n, or -s: stress falls on PENULTIMATE syllable: ca-SA, jo-VEN, ca-SAS.','middle','Ls')
    g += t(240,409,'2. Words ending in any other consonant: stress falls on FINAL syllable: ciu-DAD, ha-BLAR, es-PA\u00d1OL.','middle','Ls')
    g += t(240,418,'3. Written accent overrides both rules: m\u00fasica (stress 1st), caf\u00e9 (stress last despite -e).','middle','Ls')
    g += t(240,427,'4. Monosyllables: no accent unless disambiguation needed: s\u00ed (yes) vs si (if); \u00e9l (he) vs el (the).','middle','Ls')
    g += hr(435)

    g += sh(444,'KEY PHONOLOGICAL PROCESSES')
    g += t(240,455,'Lenition: voiced stops /b d g/ weaken to fricatives [\u03b2 \u00f0 \u0263] between vowels \u2014 a defining Spanish feature.','middle','L')
    g += t(240,465,'Seseo/ceceo/distinc\u00f3n: the s/\u03b8 variation divides Spain from the Americas and reflects 15th-c. colonial settlement.','middle','Ls')
    g += t(240,474,'Yeismo: merger of /\u028e/ (ll) and /j/ (y) \u2014 dominant in Latin America and most of Spain today.','middle','Ls')
    g += t(240,483,'Coda weakening: final and pre-consonantal /s/ aspirated [h] or deleted in Caribbean, Andalusian, and coastal dialects.','middle','Ls')
    g += t(240,492,'Vibrantes: tap /\u0279/ vs trill /r/ distinction is phonemic: pero (but) vs perro (dog).','middle','Ls')

    g += footer('26','Spanish','B','Phonology')
    g += close_svg()
    return g

def build_26c():
    g = open_svg()
    g += t(240,32,'SPANISH — GRAMMAR \u00b7 VOCABULARY','middle','T')
    g += t(240,50,'SERIES 26C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'SVO LANGUAGE \u2014 FLEXIBLE ORDER, NULL SUBJECT')
    g += t(240,79,'Spanish is SVO but highly flexible \u2014 any constituent can front for emphasis or topic.','middle','L')
    g += t(240,89,'NULL SUBJECT: subject pronouns optional \u2014 verb ending marks person/number: (yo) hablo = "I speak".','middle','Ls')
    g += t(240,98,'Two genders: masculine (-o) and feminine (-a). Adjectives agree: libro rojo / mesa roja.','middle','Ls')
    g += hr(106)

    g += sh(115,'VERB CONJUGATION \u2014 hablar "to speak" (regular -ar)')
    pres=[('yo','hablo','I speak'),('t\u00fa','hablas','you speak'),('\u00e9l/ella','habla','he/she speaks'),
          ('nosotros','hablamos','we speak'),('vosotros','habl\u00e1is','you pl. (Spain)'),('ellos','hablan','they speak')]
    pret=[('yo','habl\u00e9','I spoke'),('t\u00fa','hablaste','you spoke'),('\u00e9l/ella','habl\u00f3','he/she spoke'),
          ('nosotros','hablamos','we spoke'),('vosotros','hablasteis','you pl.'),('ellos','hablaron','they spoke')]
    g += t(105,125,'Present Indicative','middle','Lx')
    g += t(355,125,'Preterite (simple past)','middle','Lx')
    for i,((p1,f1,gl1),(p2,f2,gl2)) in enumerate(zip(pres,pret)):
        y = 134+i*11
        g += t(45,y,p1,'middle','Lx'); g += t(115,y,f1,'middle','Ls'); g += t(200,y,gl1,'middle','Lx')
        g += t(280,y,p2,'middle','Lx'); g += t(355,y,f2,'middle','Ls'); g += t(440,y,gl2,'start','Lx')
    g += t(240,208,'Subjunctive: hable, hables, hable... \u2014 used for doubt, wishes, emotions, hypotheticals.','middle','Ls')
    g += t(240,217,'Ser vs Estar: both mean "to be" \u2014 ser = permanent identity; estar = state/location/condition.','middle','Ls')
    g += hr(225)

    g += sh(234,'OBJECT PRONOUNS AND REFLEXIVES')
    g += t(240,245,'Direct: me, te, lo/la, nos, os, los/las \u2014 Lo veo "I see him/it"','middle','Ls')
    g += t(240,254,'Indirect: me, te, le, nos, os, les \u2014 Le doy el libro "I give him the book"','middle','Ls')
    g += t(240,263,'Reflexive: me, te, se, nos, os, se \u2014 Se lava "he/she washes (him/herself)"','middle','Ls')
    g += t(240,272,'Clitic climbing: with infinitives \u2014 Quiero verlo OR Lo quiero ver (both = "I want to see it")','middle','Ls')
    g += hr(280)

    g += sh(289,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[
        ('s\u00ed / no','yes / no'),('yo / t\u00fa','I / you'),('esto / eso','this / that'),
        ('\u00bfd\u00f3nde?','where'),('\u00bfqu\u00e9?','what'),('\u00bfqui\u00e9n?','who'),
        ('\u00bfcu\u00e1ndo?','when'),('\u00bfpor qu\u00e9?','why'),('agua','water'),
        ('fuego','fire'),('tierra','earth'),('persona','person'),('libro','book'),
        ('tiempo','time / weather'),('luna','moon'),('estrella','star'),
        ('coraz\u00f3n','heart'),('amor','love'),('libertad','freedom'),
        ('memoria','memory'),('futuro','future'),('mundo','world'),
        ('bueno / malo','good / bad'),('todo','everything'),('vida','life'),
    ]
    for i,(sp,en) in enumerate(vocab):
        col = 0 if i < 13 else 1
        y = 299 + (i if i<13 else i-13)*10
        g += t(50+col*230,y,sp,'middle','Ls'); g += t(175+col*230,y,en,'middle','Lx')
    g += hr(430)

    g += sh(439,'THE TWO "TO BE" VERBS \u2014 SER AND ESTAR')
    ser_ex=[('Mi madre es m\u00e9dica','My mother is a doctor (identity)'),
            ('El cielo es azul','The sky is blue (inherent)'),
            ('La fiesta es en Madrid','The party is in Madrid (event location)')]
    estar_ex=[('Estoy cansado','I am tired (state)'),
              ('El libro est\u00e1 en la mesa','The book is on the table (position)'),
              ('Est\u00e1 muerto','He is dead (resulting state)')]
    g += t(100,449,'SER (permanent / identity)','middle','Lx')
    g += t(360,449,'ESTAR (state / position)','middle','Lx')
    for i,((s,sg),(e,eg)) in enumerate(zip(ser_ex,estar_ex)):
        y = 458+i*14
        g += t(40,y,s,'start','Ls'); g += t(40,y+7,sg,'start','Lx')
        g += t(255,y,e,'start','Ls'); g += t(255,y+7,eg,'start','Lx')
    g += hr(508)

    g += sh(517,'TENSE SYSTEM OVERVIEW')
    g += t(240,528,'Spanish has 14 indicative tenses/moods + 6 subjunctive forms + imperative.','middle','Ls')
    g += t(240,537,'Key distinction: pret\u00e9rito indefinido (completed) vs imperfecto (ongoing/habitual in past).','middle','Ls')
    g += t(240,546,'Habl\u00e9 (I spoke once, done) vs hablaba (I was speaking / I used to speak).','middle','Ls')
    g += t(240,555,'Future can be expressed with ir a + infinitive: voy a hablar "I am going to speak".','middle','Ls')

    g += footer('26','Spanish','C','Grammar')
    g += close_svg()
    return g

def build_26d():
    g = open_svg()
    g += t(240,32,'SPANISH — RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g += t(240,50,'SERIES 26D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(67,'PASSAGE 1 \u2014 CERVANTES, DON QUIJOTE I.1 (1605)')
    g += t(240,78,'En un lugar de la Mancha, de cuyo nombre no quiero acordarme,','middle','L')
    g += t(240,88,'In a  place  of  La Mancha  of whose  name   not I-wish to-remember,','middle','Lx')
    g += t(240,97,'no ha mucho tiempo que viv\u00eda un hidalgo de los de lanza en astillero\u2026','middle','L')
    g += t(240,107,'not long  time   that lived  a  nobleman of those of lance on rack\u2026','middle','Lx')
    g += t(240,116,'"In a village of La Mancha, the name of which I do not wish to recall, there lived not long ago a gentleman\u2026"','middle','Ls')
    g += hr(124)

    g += sh(132,'PASSAGE 2 \u2014 PABLO NERUDA, TONIGHT I CAN WRITE (1924)')
    g += t(240,143,'Puedo escribir los versos m\u00e1s tristes esta noche.','middle','L')
    g += t(240,153,'I-can write   the  verses  most sad    this  night.','middle','Lx')
    g += t(240,162,'La quer\u00ed, y a veces ella tambi\u00e9n me quer\u00eda.','middle','L')
    g += t(240,172,'Her I-loved and sometimes she  also  me loved.','middle','Lx')
    g += t(240,181,'"Tonight I can write the saddest lines. I loved her, and sometimes she loved me too."','middle','Ls')
    g += hr(189)

    g += sh(197,'PASSAGE 3 \u2014 GABRIEL GARC\u00cdA M\u00c1RQUEZ, CIEN A\u00d1OS DE SOLEDAD (1967)')
    g += t(240,208,'Muchos a\u00f1os despu\u00e9s, frente al pelot\u00f3n de fusilamiento,','middle','L')
    g += t(240,218,'Many  years later  facing the  firing squad,','middle','Lx')
    g += t(240,227,'el coronel Aureliano Buend\u00eda hab\u00eda de recordar aquella tarde remota\u2026','middle','L')
    g += t(240,237,'the colonel Aureliano Buend\u00eda was  to remember that  remote  afternoon\u2026','middle','Lx')
    g += t(240,246,'"Many years later, as he faced the firing squad, Colonel Aureliano Buend\u00eda was to remember\u2026"','middle','Ls')
    g += hr(254)

    g += sh(262,'PASSAGE 4 \u2014 SPANISH PROVERBS')
    g += t(240,273,'M\u00e1s vale tarde que nunca.','middle','L')
    g += t(240,283,'More is-worth late than never. \u2014 "Better late than never."','middle','Lx')
    g += t(240,293,'El que no arriesga, no gana.','middle','L')
    g += t(240,303,'He who not risks    not wins. \u2014 "Nothing ventured, nothing gained."','middle','Lx')
    g += hr(311)

    g += sh(319,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240,331,'Este mensaje fue hecho para usted, gratuitamente, por personas que recordaron el futuro.','middle','L')
    g += t(240,342,'This message  was made  for  you    freely,         by  people  who  remembered  the future.','middle','Lx')
    g += t(240,352,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g += hr(360)

    g += sh(369,'LANGUAGE NOTE \u2014 "FUTURE" IN SPANISH')
    g += t(240,380,'futuro (el futuro): from Latin futurum \u2014 same root. Grammatical future tense formed by adding endings to infinitive.','middle','L')
    g += t(240,390,'hablar\u00e9, hablar\u00e1s, hablar\u00e1\u2026 \u2014 The endings derive from Latin habere "to have": habl-ar-he\u0301 = "speak-to-I have".','middle','Ls')
    g += t(240,399,'recordar: to remember \u2014 from Latin re-cord-are "to pass back through the heart" (cor/cordis = heart).','middle','Ls')
    g += t(240,408,'gratuitamente: freely \u2014 from Latin gratuitus "given without return", gratis "by grace".','middle','Ls')
    g += hr(416)

    g += sh(425,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g += t(240,436,'Spanish is spoken by ~500 million native speakers across Spain, all of Latin America except Brazil, the Caribbean,','middle','Ls')
    g += t(240,445,'and large communities in the USA. It is the world\'s 2nd most spoken native language.','middle','Ls')
    g += t(240,454,'It uses the Latin alphabet (same as English) with \u00f1 and optional accent marks. Pronunciation is highly regular.','middle','Ls')
    g += t(240,463,'Spanish is an Indo-European language \u2014 descended from Latin, related to Portuguese, French, Italian, and Romanian.','middle','Ls')
    g += t(240,472,'The passage above from Don Quijote (1605) is widely considered the first modern novel in any language.','middle','Ls')

    g += footer('26','Spanish','D','Text')
    g += close_svg()
    return g

def main():
    plates = {
        'plate26a_spanish_script.svg': build_26a(),
        'plate26b_spanish_phonology.svg': build_26b(),
        'plate26c_spanish_grammar.svg': build_26c(),
        'plate26d_spanish_text.svg': build_26d(),
    }
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8')
        print(f'Written: {OUT/fname}')

if __name__ == '__main__':
    main()
