#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Lingala plate series 33A–33D for Remember Forward."""
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

def build_33a():
    g=open_svg()
    g+=t(240,32,'LINGALA \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g+=t(240,50,'SERIES 33A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'LINGALA \u2014 BANTU LINGUA FRANCA OF THE CONGO RIVER')
    g+=t(240,79,'Lingala is a Bantu language spoken by ~70 million people as L1 or L2.','middle','L')
    g+=t(240,89,'Lingua franca of the Democratic Republic of Congo, Republic of Congo, and the Congo River basin.','middle','Ls')
    g+=t(240,98,'Also spoken in parts of Angola, Central African Republic, and South Sudan.','middle','Ls')
    g+=t(240,107,'Used in the Congolese military, church, and urban centres. One of four national languages of DRC.','middle','Ls')
    g+=hr(115)
    g+=sh(124,'LINGALA ALPHABET \u2014 LATIN-BASED')
    g+=t(240,135,'Lingala uses the Latin alphabet. Since 1976 standardisation, tones are marked with diacritics.','middle','Ls')
    letters=[
        ('A a','/a/','open low'),('B b','/b/','bilabial'),('D d','/d/','alveolar'),
        ('E e','/e/','mid front'),('\u0190 \u0190','/\u025b/','open e: b\u0190t\u0250 (arm)'),
        ('F f','/f/','labiodental'),('G g','/\u0261/','velar'),('I i','/i/','high front'),
        ('K k','/k/','velar'),('L l','/l/','lateral'),('M m','/m/','nasal'),
        ('N n','/n/','nasal'),('Ng ng','/\u014b/','velar nasal'),
        ('Ny ny','/\u0272/','palatal nasal'),('O o','/o/','mid back'),
        ('\u0186 \u0186','/\u0254/','open o: l\u0254k\u0254 (tail)'),
        ('P p','/p/','bilabial'),('S s','/s/','alveolar'),('T t','/t/','alveolar'),
        ('V v','/v/','labiodental'),('W w','/w/','glide'),('Y y','/j/','palatal glide'),
        ('Z z','/z/','alveolar'),
    ]
    for i,(ltr,ipa,note) in enumerate(letters):
        col=0 if i<12 else 1
        y=145+(i if i<12 else i-12)*10
        cx=[30,90,175] if col==0 else [260,315,395]
        g+=t(cx[0],y,ltr,'middle','Lx'); g+=t(cx[1],y,ipa,'middle','Lx'); g+=t(cx[2],y,note,'middle','Lx')
    g+=hr(270)
    g+=sh(279,'TONE SYSTEM \u2014 TWO TONES')
    g+=t(240,290,'Lingala has TWO tones: High (H marked with acute \u00b4) and Low (L unmarked or grave \u0060).','middle','L')
    g+=t(240,300,'Tone is phonemic: mot\u00f3 (head) vs m\u00f4to (person) \u2014 same segments, different tones, different meanings.','middle','Ls')
    g+=t(240,309,'In colloquial urban Lingala, tones are often simplified or not marked in informal writing.','middle','Ls')
    g+=hr(317)
    g+=sh(326,'NOUN CLASS SYSTEM \u2014 BANTU CLASSES')
    g+=t(240,337,'Like all Bantu languages, Lingala has noun classes \u2014 grammatical categories that determine agreement.','middle','L')
    g+=t(240,347,'Each noun belongs to a class with a prefix. Adjectives, verbs, and pronouns agree with the noun class.','middle','Ls')
    classes=[('mo-','Class 1/3 (person sg)','moto (person), mok\u00f3l\u00f3 (elder)'),
             ('ba-','Class 2/4 (person pl)','bato (people), bak\u00f3l\u00f3 (elders)'),
             ('li-','Class 5/6 (things)','lik\u00f3mb\u00f3 (boat), monoko (mouth)'),
             ('e-','Class 7/8 (things, actions)','em\u00f3 (animal), ek\u00f3l\u00f3 (country)'),
             ('n-','Class 9/10 (diverse)','ng\u00e1i (I), nk\u00f3t\u00f3 (body)')]
    for i,(pfx,cls,ex) in enumerate(classes):
        y=357+i*12
        g+=t(55,y,pfx,'middle','Ls'); g+=t(140,y,cls,'middle','Lx'); g+=t(360,y,ex,'middle','Lx')
    g+=footer('33','Lingala','A','Script')
    return g+close_svg()

def build_33b():
    g=open_svg()
    g+=t(240,32,'LINGALA \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g+=t(240,50,'SERIES 33B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'VOWEL SYSTEM \u2014 7 VOWELS')
    g+=t(240,79,'Lingala has 7 vowel phonemes, including the open-mid vowels /\u025b/ and /\u0254/.','middle','L')
    vowels=[('/i/','i','high front: mib\u00e9 (two)'),
            ('/e/','e','mid front close: bek\u00e0 (goat)'),
            ('/\u025b/','e-open (\u0190)','mid front open: b\u0190t\u0250 (arm)'),
            ('/a/','a','low central: bal\u00e9 (war)'),
            ('/\u0254/','o-open (\u0186)','mid back open: l\u0254k\u0254 (tail)'),
            ('/o/','o','mid back close: mot\u00f3 (head)'),
            ('/u/','u','high back: mok\u00f3l\u00f3 (elder)')]
    for i,(ipa,ltr,ex) in enumerate(vowels):
        y=89+i*12
        g+=t(55,y,ipa,'middle','Lx'); g+=t(110,y,ltr,'middle','Lx'); g+=t(320,y,ex,'middle','Lx')
    g+=hr(183)
    g+=sh(192,'CONSONANT INVENTORY')
    cons=[('p b','bilabial stops','common'),
          ('t d','alveolar stops','dental-alveolar'),
          ('k g','velar stops','common'),
          ('f v','labiodentals','present in urban/adapted words'),
          ('s z','alveolar fricatives','common'),
          ('m n','nasals','bilabial, alveolar'),
          ('ng','/\u014b/','velar nasal: ngai (I)'),
          ('ny','/\u0272/','palatal nasal: nyama (animal/meat)'),
          ('l r','lateral / rhotic','tap in many dialects'),
          ('w y','glides','common')]
    for i,(ltr,ipa,note) in enumerate(cons):
        y=202+i*12
        g+=t(55,y,ltr,'middle','Ls'); g+=t(120,y,ipa,'middle','Lx'); g+=t(310,y,note,'middle','Lx')
    g+=hr(326)
    g+=sh(335,'TONE IN LINGALA')
    g+=t(240,346,'High tone (H): marked with acute accent in formal writing: mot\u00f3 (head).','middle','Ls')
    g+=t(240,355,'Low tone (L): unmarked or marked with grave: m\u00f4to (person).','middle','Ls')
    g+=t(240,364,'Tone affects meaning, grammatical role, and verb tense/aspect distinctions.','middle','Ls')
    pairs=[('mot\u00f3 (H-H)','head'),('m\u00f4to (L-H)','person'),
           ('nal\u00e0 (H-L)','I have (pres)'),('\u00f3kos\u00e9ngeli (verb H)','he should help')]
    for i,(lw,gl) in enumerate(pairs):
        y=374+i*11
        g+=t(120,y,lw,'middle','Ls'); g+=t(330,y,gl,'middle','Lx')
    g+=footer('33','Lingala','B','Phonology')
    return g+close_svg()

def build_33c():
    g=open_svg()
    g+=t(240,32,'LINGALA \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,50,'SERIES 33C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SVO \u2014 BANTU NOUN CLASSES \u2014 TONAL ASPECT')
    g+=t(240,79,'Lingala is SVO. Verb agreement with noun class. Tense/aspect marked by verb prefixes and tone.','middle','L')
    g+=t(240,89,'Subject prefixes agree with noun class: a- (class 1 sg), ba- (class 2 pl), e- (class 7), etc.','middle','Ls')
    g+=hr(97)
    g+=sh(106,'VERB CONJUGATION \u2014 kosala "to do/work"')
    conj=[('Ng\u00e1i','I','nasali','I did'),
          ('Yo','you sg','osali','you did'),
          ('Ye','he/she','asali','he/she did'),
          ('Biso','we','tosali','we did'),
          ('Bino','you pl','bosali','you pl did'),
          ('Bango','they','basali','they did')]
    g+=t(55,116,'Subject','middle','Lx'); g+=t(130,116,'Pronoun','middle','Lx')
    g+=t(260,116,'Past form','middle','Lx'); g+=t(390,116,'Gloss','middle','Lx')
    for i,(subj,eng,past,gl) in enumerate(conj):
        y=125+i*11
        g+=t(55,y,subj,'middle','Lx'); g+=t(130,y,eng,'middle','Lx')
        g+=t(260,y,past,'middle','Ls'); g+=t(390,y,gl,'middle','Lx')
    g+=t(240,197,'Present: na-sala (I work) \u00b7 Future: na-ko-sala (I will work) \u00b7 Neg: na-sala-ki te (I did not work)','middle','Ls')
    g+=hr(205)
    g+=sh(214,'NOUN AGREEMENT')
    g+=t(240,225,'All adjectives, demonstratives, and verbs agree with the noun class prefix.','middle','Ls')
    g+=t(240,234,'moto mok\u00f3l\u00f3 (1 elder person) \u00b7 bato bak\u00f3l\u00f3 (2/pl elder people) \u00b7 class changes prefix throughout.','middle','Ls')
    g+=hr(242)
    g+=sh(251,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[('ey\u00f3 / t\u00e9','yes / no'),('ng\u00e1i / yo','I / you'),
           ('oyo / wana','this / that'),('wapi?','where'),
           ('nini?','what'),('nani?','who'),('ntango nini?','when'),
           ('pona nini?','why'),('mai','water'),
           ('moto (fire)','fire'),('mab\u00e9l\u00e9 ya mw\u00e1si','earth/ground'),
           ('moto (person)','person'),('buku','book'),
           ('ntango','time'),('ngond\u00e9','moon'),('ny\u00f3t\u00e9','star'),
           ('mot\u00f3 ya pem\u00f3','heart/mind'),('bolingo','love'),
           ('bonsomi','freedom'),('makanisi','memory/thought'),
           ('lobi / mike\u00f3','tomorrow / future'),('d\u00fanya','world'),
           ('mal\u00e0mu / mab\u00e9','good / bad'),('nyonso','everything'),('bomoi','life')]
    for i,(li,en) in enumerate(vocab):
        col=0 if i<13 else 1; y=261+(i if i<13 else i-13)*10
        g+=t(50+col*230,y,li,'middle','Ls'); g+=t(185+col*230,y,en,'middle','Lx')
    g+=hr(398)
    g+=sh(407,'URBAN LINGALA')
    g+=t(240,418,'Urban Kinshasa/Brazzaville Lingala has absorbed many French words: fol\u00f3 (floor), tabl\u00f3 (table).','middle','Ls')
    g+=t(240,427,'Also creative coinages: kobeta n\u00f3t\u00e0 (to take notes, lit. "to hit notes"), mwa\u00eds\u00e9 (baby, from French moi aussi).','middle','Ls')
    g+=t(240,436,'Lingala is the language of Congolese rumba music (soukous) \u2014 hugely influential across Africa.','middle','Ls')
    g+=footer('33','Lingala','C','Grammar')
    return g+close_svg()

def build_33d():
    g=open_svg()
    g+=t(240,32,'LINGALA \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,50,'SERIES 33D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(67,'PASSAGE 1 \u2014 CONGOLESE PROVERB')
    g+=t(240,78,'Libanga moko etongi ndako te.','middle','L')
    g+=t(240,88,'Stone   one   builds  house  not.','middle','Lx')
    g+=t(240,97,'"One stone does not build a house." \u2014 Communal effort is required for any great work.','middle','Ls')
    g+=hr(105)
    g+=sh(113,'PASSAGE 2 \u2014 CONGOLESE PROVERB')
    g+=t(240,124,'Moto azali moto na nzela ya bato banz\u00f3.','middle','L')
    g+=t(240,134,'Person is   person on  path  of  people other.','middle','Lx')
    g+=t(240,143,'"A person is a person through other people." \u2014 Parallels Ubuntu philosophy.','middle','Ls')
    g+=hr(151)
    g+=sh(159,'PASSAGE 3 \u2014 LINGALA SONG (SOUKOUS TRADITION)')
    g+=t(240,170,'Nakobundisa bolingo na ngai,','middle','L')
    g+=t(240,180,'I-will-give   love   of  me,','middle','Lx')
    g+=t(240,189,'pona yo, pona biso nyonso.','middle','L')
    g+=t(240,199,'for  you  for  us   all.','middle','Lx')
    g+=t(240,208,'"I will give my love, for you, for all of us." \u2014 from the tradition of Congolese rumba.','middle','Ls')
    g+=hr(216)
    g+=sh(224,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g+=t(240,236,'Sango oyo esalami pona yo, na ofele, na bato oyo bakanisaki lobi.','middle','L')
    g+=t(240,247,'Message this  made    for  you  for free  by  people who  thought-of  tomorrow/future.','middle','Lx')
    g+=t(240,257,'"This message was made for you, freely, by people who thought of the future."','middle','Ls')
    g+=hr(265)
    g+=sh(274,'LANGUAGE NOTE \u2014 "FUTURE" IN LINGALA')
    g+=t(240,285,'lobi: "tomorrow" \u2014 also used for "future" in everyday speech.','middle','L')
    g+=t(240,295,'mike\u00f3: "ahead / in front / future" \u2014 from the spatial concept of forward direction.','middle','Ls')
    g+=t(240,304,'makanisi: "thoughts / memory / remembrance" \u2014 from kokanisa (to think, to recall).','middle','Ls')
    g+=t(240,313,'ofele: "free / for free" \u2014 from French "au f\u00e9le" / "gratis". Common in urban Lingala.','middle','Ls')
    g+=hr(321)
    g+=sh(330,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g+=t(240,341,'Lingala is spoken by ~70 million people (L1+L2) primarily in DRC and Republic of Congo.','middle','Ls')
    g+=t(240,350,'It is a Bantu language \u2014 related to Swahili, Zulu, Yoruba (distant), and hundreds of other African languages.','middle','Ls')
    g+=t(240,359,'Script: Latin-based, left to right. Tones marked with accents in formal writing (see Plate 33A).','middle','Ls')
    g+=t(240,368,'Lingala is the language of Congolese soukous and rumba \u2014 one of the most influential music traditions in Africa.','middle','Ls')
    g+=footer('33','Lingala','D','Text')
    return g+close_svg()

def main():
    plates={'plate33a_lingala_script.svg':build_33a(),'plate33b_lingala_phonology.svg':build_33b(),
            'plate33c_lingala_grammar.svg':build_33c(),'plate33d_lingala_text.svg':build_33d()}
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8'); print(f'Written: {OUT/fname}')

if __name__=='__main__': main()
