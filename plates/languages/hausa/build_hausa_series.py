#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Hausa plate series 29A–29D for Remember Forward."""
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

def build_29a():
    g=open_svg()
    g+=t(240,32,'HAUSA \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g+=t(240,50,'SERIES 29A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'HAUSA \u2014 MOST WIDELY SPOKEN CHADIC LANGUAGE')
    g+=t(240,79,'Hausa is a Chadic language (Afroasiatic family), spoken by 70\u2013100 million people as L1 or L2.','middle','L')
    g+=t(240,89,'Lingua franca across Nigeria, Niger, Ghana, Chad, Cameroon, Sudan, and the Sahel belt.','middle','Ls')
    g+=t(240,98,'Two writing systems: Boko (Latin-based, official) and Ajami (Arabic-based, traditional).','middle','Ls')
    g+=hr(106)
    g+=sh(115,'BOKO ALPHABET \u2014 OFFICIAL LATIN-BASED SCRIPT')
    g+=t(240,125,'23 letters from the Latin alphabet + 3 special letters with hooks: \u0253, \u0257, \u2019y (glottalised).','middle','Ls')
    letters=[
        ('A a','/a/','open low'),('B b','/b/','bilabial stop'),('\u0253 \u0253','/\u0253/','implosive bilabial \u2014 ba\u0253a (door)'),
        ('C c','/t\u0283/','ch sound'),('D d','/d/','alveolar stop'),('\u0257 \u0257','/\u0257/','implosive alveolar \u2014 \u0257an (son)'),
        ('E e','/e/','mid front'),('F f','/\u0278/','bilabial fricative'),('G g','/\u0261/','velar stop'),
        ('H h','/h/','glottal'),('I i','/i/','high front'),('J j','/d\u0292/','voiced affricate'),
        ('K k','/k/','velar stop'),('L l','/l/','lateral'),('M m','/m/','nasal'),
        ('N n','/n/','nasal'),('O o','/o/','mid back'),('R r','/r/','trill / flap'),
        ('S s','/s/','alveolar frict.'),('Sh sh','/\u0283/','palatal frict.'),('T t','/t/','alveolar stop'),
        ('Ts ts','/ts\'/ or /\u02a6/','ejective affricate'),('U u','/u/','high back'),('W w','/w/','labio-velar glide'),
        ('Y y','/j/','palatal glide'),('\u2019y \u2019y','/\u02bfj/','glottalised palatal'),('Z z','/z/','alveolar frict.'),
    ]
    cols=[(35,100,210),(265,330,440)]
    half=14
    for i,(ltr,ipa,note) in enumerate(letters):
        if i<half: cx,y=cols[0],135+i*10
        else: cx,y=cols[1],135+(i-half)*10
        g+=t(cx[0],y,ltr,'middle','Lx'); g+=t(cx[1],y,ipa,'middle','Lx'); g+=t(cx[2],y,note,'middle','Lx')
    g+=hr(282)
    g+=sh(291,'AJAMI \u2014 ARABIC-BASED TRADITIONAL SCRIPT')
    g+=t(240,302,'Ajami (from Arabic \u2018ajam \u2014 non-Arab) uses Arabic letters adapted for Hausa sounds.','middle','Ls')
    g+=t(240,311,'Used before colonialism; still used in religious texts, poetry, and traditional manuscripts.','middle','Ls')
    g+=t(240,320,'Hausa implosives (\u0253 \u0257) often written with dotted Arabic letters not standard in Arabic.','middle','Ls')
    g+=hr(328)
    g+=sh(337,'TONE MARKING')
    g+=t(240,348,'Hausa is a TONAL language with 2 tones: High (H) and Low (L). Falling tone = H+L on one syllable.','middle','L')
    g+=t(240,358,'Tone is not marked in standard Boko writing \u2014 must be learned in context or from dictionaries.','middle','Ls')
    g+=t(240,367,'ba\u0253a (door) H-L | ba\u0253\u00e1 (no) L-H | \u0257an (son) H | \u0257\u00e0n (person of) L','middle','Ls')
    g+=t(240,376,'Tone changes word meaning and grammatical function. Critical for comprehension.','middle','Ls')
    g+=hr(384)
    g+=sh(393,'IMPLOSIVE CONSONANTS \u2014 KEY HAUSA FEATURE')
    g+=t(240,404,'\u0253 and \u0257 are IMPLOSIVE stops: airstream moves inward while voicing occurs. Rare in world languages.','middle','L')
    g+=t(240,414,'\u0253 = voiced bilabial implosive: lips close, glottis descends \u2014 ba\u0253a "door", \u0253awa "sand"','middle','Ls')
    g+=t(240,423,'\u0257 = voiced alveolar implosive: tongue at alveolar ridge, glottis descends \u2014 \u0257an "son"','middle','Ls')
    g+=t(240,432,'Distinguished from plain b/d by direction of airflow: implosives pull air in rather than push out.','middle','Ls')
    g+=footer('29','Hausa','A','Script')
    return g+close_svg()

def build_29b():
    g=open_svg()
    g+=t(240,32,'HAUSA \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g+=t(240,50,'SERIES 29B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'TWO-TONE SYSTEM \u2014 HIGH AND LOW')
    g+=t(240,79,'Hausa has two level tones (High and Low) plus a falling tone (H\u2192L on one mora).','middle','L')
    g+=t(240,89,'Tone is phonemic: identical segmental strings differ only in tone pattern.','middle','Ls')
    pairs=[('mai','owner (H)','m\u00e0i','stomach (L)'),
           ('k\u0101ya','loads (HL)','k\u00e0ya','thorns (LH)'),
           ('g\u012bda','house (HL)','g\u00ecda','(verb: go home) (LH)')]
    for i,(h1,g1,h2,g2) in enumerate(pairs):
        y=99+i*12
        g+=t(80,y,h1,'middle','Ls'); g+=t(155,y,g1,'middle','Lx')
        g+=t(285,y,h2,'middle','Ls'); g+=t(385,y,g2,'middle','Lx')
    g+=hr(138)
    g+=sh(147,'VOWEL SYSTEM \u2014 5 SHORT + 5 LONG')
    g+=t(240,158,'Vowel length is phonemic in Hausa \u2014 like tone, it changes meaning.','middle','L')
    vowels=[('/a/ vs /a\u02d0/','a vs aa','karA (pull) vs kaara (make a road)'),
            ('/e/ vs /e\u02d0/','e vs ee','mee (what) vs meehe (whatchamacallit)'),
            ('/i/ vs /i\u02d0/','i vs ii','cikin (inside) vs ciikii (belly full)'),
            ('/o/ vs /o\u02d0/','o vs oo','gona (farm) vs goona (farm-emph)'),
            ('/u/ vs /u\u02d0/','u vs uu','muta (people) vs muuta (die-pl)')]
    for i,(ipa,boko,ex) in enumerate(vowels):
        y=168+i*12
        g+=t(80,y,ipa,'middle','Lx'); g+=t(175,y,boko,'middle','Lx'); g+=t(355,y,ex,'middle','Lx')
    g+=t(240,233,'Diphthongs: ai /ai\u0306/ and au /au\u0306/ are common in Hausa.','middle','Ls')
    g+=hr(241)
    g+=sh(250,'CONSONANT INVENTORY')
    cons=[('p b \u0253','/p b \u0253/','labials \u2014 \u0253 is implosive'),
          ('t d \u0257','/t d \u0257/','alveolars \u2014 \u0257 is implosive'),
          ('k g','/k \u0261/','velars'),
          ('k\u02bc','/k\'/ ejective','glottalised velar: k\u02bca\u0253\u00e0 (shoe)'),
          ('ts','/ts\u02bc/ ejective','glottalised affricate \u2014 distinctive'),
          ('c','/t\u0283/','palatal affricate: cikin'),
          ('j','/d\u0292/','voiced affricate'),
          ('f s z sh','/\u0278 s z \u0283/','fricatives'),
          ('r','/r/','trill (word initial) / flap (medial)'),
          ('l m n','/l m n/','lateral and nasals'),
          ('w y \u2019y','/w j \u02bfj/','glides \u2014 \u2019y is glottalised'),
          ('\u02be','/\u02be/','glottal stop: ya\u02bein (eye)')]
    for i,(ltr,ipa,note) in enumerate(cons):
        y=260+i*11
        g+=t(50,y,ltr,'middle','Ls'); g+=t(115,y,ipa,'middle','Lx'); g+=t(330,y,note,'middle','Lx')
    g+=hr(396)
    g+=sh(405,'SYLLABLE STRUCTURE AND PROSODY')
    g+=t(240,416,'Hausa syllables: CV or CVC. No complex clusters. Words tend to be disyllabic.','middle','Ls')
    g+=t(240,425,'Long vowels count as two morae: CVV = heavy syllable; affects tone and grammar.','middle','Ls')
    g+=t(240,434,'Word-final position: often determines tone pattern of entire word (WF tone).','middle','Ls')
    g+=footer('29','Hausa','B','Phonology')
    return g+close_svg()

def build_29c():
    g=open_svg()
    g+=t(240,32,'HAUSA \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,50,'SERIES 29C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SVO \u2014 ASPECT-BASED VERB SYSTEM \u2014 TWO GENDERS')
    g+=t(240,79,'Hausa is SVO with postverbal objects. Two grammatical genders: masculine and feminine.','middle','L')
    g+=t(240,89,'Verbs do not conjugate for tense \u2014 instead, ASPECT is marked by a pronominal aspect complex (PAC).','middle','Ls')
    g+=t(240,98,'The PAC (subject pronoun + aspect marker) precedes the verb and encodes person, number, gender, aspect.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'PRONOMINAL ASPECT COMPLEX \u2014 COMPLETIVE ASPECT')
    pac=[('n\u0101','1sg','I (did)'),('k\u0101','2sg M','you-m (did)'),('k\u012b','2sg F','you-f (did)'),
         ('y\u0101','3sg M','he (did)'),('t\u0101','3sg F','she (did)'),
         ('mun','1pl','we (did)'),('kun','2pl','you pl (did)'),('sun','3pl','they (did)')]
    g+=t(80,125,'PAC','middle','Lx'); g+=t(155,125,'Person','middle','Lx'); g+=t(260,125,'Gloss','middle','Lx')
    g+=t(360,125,'Example: zo (come)','middle','Lx')
    for i,(pac_f,pers,gl) in enumerate(pac):
        y=134+i*11
        g+=t(80,y,pac_f,'middle','Ls'); g+=t(155,y,pers,'middle','Lx'); g+=t(260,y,gl,'middle','Lx')
        g+=t(380,y,pac_f+' zo','middle','Ls')
    g+=hr(225)
    g+=sh(234,'ASPECT SYSTEM')
    aspects=[('Completive','n\u0101/y\u0101\u2026','completed action','y\u0101 ci ya\u2019yi (he has eaten)'),
             ('Continuative','in\u0101/y\u0101 na\u2026','ongoing action','y\u0101 na cin (he is eating)'),
             ('Future/Intentive','\u0253an/z\u0101\u2026','future intention','z\u0101 y\u0101 ci (he will eat)'),
             ('Subjunctive','y\u0101\u2026 (no asp)','wish/command','y\u0101 ci! (let him eat!)')]
    for i,(asp,form,func,ex) in enumerate(aspects):
        y=244+i*13
        g+=t(80,y,asp,'middle','Ls'); g+=t(185,y,form,'middle','Lx')
        g+=t(285,y,func,'middle','Lx'); g+=t(400,y,ex,'middle','Lx')
    g+=hr(298)
    g+=sh(307,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[('i\u0257\u0257\u0101 / a\u02bea','yes / no'),('ni / kai','I / you (m)'),
           ('wannan / wancan','this / that'),('ina?','where'),('me?','what'),
           ('wane?','who'),('yaushe?','when'),('don me?','why'),
           ('ruwa','water'),('wuta','fire'),('k\u0101sa','earth/land'),
           ('mutum','person'),('littafi','book'),('lokaci','time'),
           ('wata','moon'),('tauraro','star'),('zuciya','heart'),
           ('koyayya','love'),('yanci','freedom'),('tunawa','memory'),
           ('gobe','tomorrow / future'),('duniya','world'),
           ('mai kyau / mugu','good / bad'),('duka','everything'),('rai','life')]
    for i,(h,e) in enumerate(vocab):
        col=0 if i<13 else 1
        y=317+(i if i<13 else i-13)*10
        g+=t(50+col*230,y,h,'middle','Ls'); g+=t(175+col*230,y,e,'middle','Lx')
    g+=hr(450)
    g+=sh(459,'GENDER AND PLURALITY')
    g+=t(240,470,'Gender: masculine default; feminine marked by final -aa or -iyaa suffix in many nouns.','middle','Ls')
    g+=t(240,479,'Plural formation is complex and partly irregular \u2014 several plural patterns exist.','middle','Ls')
    g+=t(240,488,'gida (house) \u2192 gidaje (houses) \u00b7 mutum (person) \u2192 mutane (people) \u00b7 k\u012bfi (fish, unchanged)','middle','Ls')
    g+=footer('29','Hausa','C','Grammar')
    return g+close_svg()

def build_29d():
    g=open_svg()
    g+=t(240,32,'HAUSA \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,50,'SERIES 29D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(67,'PASSAGE 1 \u2014 HAUSA PROVERB')
    g+=t(240,78,'Hausa: Hankali ya fi karfi.','middle','L')
    g+=t(240,88,'Wisdom  surpasses strength.','middle','Lx')
    g+=t(240,97,'"Wisdom surpasses strength." \u2014 Intelligence overcomes brute force.','middle','Ls')
    g+=hr(105)
    g+=sh(113,'PASSAGE 2 \u2014 HAUSA PROVERB')
    g+=t(240,124,'Zaman lafiya shi ne dukiya.','middle','L')
    g+=t(240,134,'Living   peace  it  is  wealth.','middle','Lx')
    g+=t(240,143,'"Living in peace is wealth." \u2014 On the value of communal harmony.','middle','Ls')
    g+=hr(151)
    g+=sh(159,'PASSAGE 3 \u2014 TRADITIONAL SAYING')
    g+=t(240,170,'Duk\u0101 abinda Allah ya yi, da \u0006ke\u0007ya.','middle','L')
    g+=t(240,180,'All   things  God    did  with wisdom.','middle','Lx')
    g+=t(240,189,'"All that God has made, He made with wisdom." \u2014 On gratitude and purpose.','middle','Ls')
    g+=hr(197)
    g+=sh(205,'PASSAGE 4 \u2014 ON MEMORY')
    g+=t(240,216,'Tunawa da tarihi shi ne mabudin gobe.','middle','L')
    g+=t(240,226,'Remembering the history it  is  key-of  tomorrow.','middle','Lx')
    g+=t(240,235,'"Remembering history is the key to tomorrow." \u2014 Hausa oral tradition.','middle','Ls')
    g+=hr(243)
    g+=sh(251,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g+=t(240,263,'Wannan sako an yi shi a gare ku, kyauta, daga mutanen da suka tuna da gobe.','middle','L')
    g+=t(240,274,'This    message was made it  for  you  freely  from  people   who  remembered  tomorrow/future.','middle','Lx')
    g+=t(240,284,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g+=hr(292)
    g+=sh(301,'LANGUAGE NOTE \u2014 "FUTURE" IN HAUSA')
    g+=t(240,312,'Hausa: gobe = "tomorrow" \u2014 used colloquially for "the future". Also: nan gaba = "ahead / in the future".','middle','L')
    g+=t(240,322,'tuna = "to remember" \u2014 tuna da = "to remember X". The completive aspect (sun tuna) means "they remembered".','middle','Ls')
    g+=t(240,331,'kyauta = "gift / free of charge" \u2014 kyauta ne! = "it\'s free!" \u2014 from root kya (good).','middle','Ls')
    g+=t(240,340,'Tone note: wannan (THIS) is H-H-L; sako (message) is L-H \u2014 both critical for comprehension.','middle','Ls')
    g+=hr(348)
    g+=sh(357,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g+=t(240,368,'Hausa is spoken by 70\u2013100 million people across Nigeria, Niger, Ghana, Chad, Cameroon, and Sudan.','middle','Ls')
    g+=t(240,377,'It is the dominant trade and lingua franca language of the West African Sahel belt.','middle','Ls')
    g+=t(240,386,'Script: Boko (Latin-based, left to right). Tone is not marked in normal writing \u2014 learned from context.','middle','Ls')
    g+=t(240,395,'Hausa belongs to the Chadic branch of Afroasiatic \u2014 distantly related to Arabic and Amharic.','middle','Ls')
    g+=t(240,404,'The two implosive consonants (\u0253, \u0257) are unique to the Chadic/Niger-Congo region and rare globally.','middle','Ls')
    g+=footer('29','Hausa','D','Text')
    return g+close_svg()

def main():
    plates={'plate29a_hausa_script.svg':build_29a(),'plate29b_hausa_phonology.svg':build_29b(),
            'plate29c_hausa_grammar.svg':build_29c(),'plate29d_hausa_text.svg':build_29d()}
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8'); print(f'Written: {OUT/fname}')

if __name__=='__main__': main()
