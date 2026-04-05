"""Build script — Nahuatl series plates 47A–47D (Remember Forward)"""
from pathlib import Path
OUT = Path(__file__).parent
def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
            '<defs><style>\n'
            'text{font-family:Georgia,serif;}\n'
            '.T{font-size:12px;font-weight:bold;letter-spacing:2px;}\n'
            '.S{font-size:7px;letter-spacing:1.5px;}\n'
            '.H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px;}\n'
            '.L{font-size:7px;}\n'
            '.Ls{font-size:6px;}\n'
            '.Lx{font-size:5.5px;}\n'
            '.M{font-size:6px;}\n'
            '.F{font-size:7px;font-style:italic;}\n'
            '.Fb{font-size:7.5px;font-weight:bold;}\n'
            '</style></defs>\n'
            '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
            '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')
def close_svg(): return '</svg>\n'
def t(x,y,s,a='middle',c='L',extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{esc(s)}</text>\n'
def hr(y,x1=20,x2=460,sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y,txt): return t(240,y,f'— {txt} —','middle','H')
def footer(num,lang,letter,desc):
    g=''
    g+=hr(610)
    g+=t(240,622,f'REMEMBER FORWARD \u2014 PLATE {num}{letter} \u2014 {lang.upper()}: {desc.upper()} \u2014 rememberforward.org \u2014 CC BY-SA 4.0','middle','M')
    g+=hr(633)
    g+=t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
    g+=t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F')
    return g

def build_47a():
    g=open_svg()
    g+=t(240,32,'NAHUATL','middle','T')
    g+=t(240,50,'Nahuatl \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Modern Nahuatl uses the Latin alphabet (adopted post-1521 Spanish conquest).','middle','Ls')
    g+=t(240,94,'Multiple orthographies in use; Classical Nahuatl spelling system shown here.','middle','Ls')
    g+=t(240,104,'Pre-colonial Nahuatl: pictographic/logographic writing (Aztec codices) + phonetic elements.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'PRE-COLONIAL WRITING \u2014 AZTEC PICTOGRAPHY')
    g+=t(240,131,'Aztec writing combined pictograms, logograms, and phonetic complements (rebuses).','middle','Ls')
    g+=t(240,141,'Not a fully phonetic system: partially logographic + phonetic signs for sounds.','middle','Ls')
    g+=t(240,151,'Major codices: Codex Mendoza, Codex Borgia, Tonalamatl (ritual calendar).','middle','Ls')
    g+=t(240,161,'After conquest, missionaries created Latin-based phonetic orthography (~1540s).','middle','Ls')
    g+=hr(169)
    g+=sh(178,'NAHUATL ALPHABET \u2014 CLASSICAL ORTHOGRAPHY')
    g+=t(240,188,'26 letters. Special sounds: tl, tz (affricates), hu/uh (labiovelar /w/), cu/uc (kw).','middle','Ls')
    g+=t(240,198,'Long vowels marked with macron in careful text: \u0101, \u012b, \u014d, \u016b.','middle','Ls')
    letters=['A \u0100  C  CH  CU  E  \u0112  H  HU  I  \u012a  L  M  N  O  \u014c  P  QU  T  TL  TZ  U  \u016a  X  Y  Z']
    g+=t(240,208,letters[0],'middle','Ls')
    g+=hr(216)
    g+=sh(225,'SPECIAL CONSONANTS')
    g+=t(240,235,'TL /t\u026c/: lateral affricate (unique to Nahuatl family). "atl" (water) = /at\u026c/.','middle','Ls')
    g+=t(240,245,'TZ /ts/: alveolar affricate. "tzin" (small/revered) = /tsin/.','middle','Ls')
    g+=t(240,255,'X /\u0283/: postalveolar fricative (like English "sh"). "xochitl" = /\u0283o.t\u0255it\u026c/.','middle','Ls')
    g+=t(240,265,'HU/UH /w/: labiovelar approximant. "huey" (great) = /wej/.','middle','Ls')
    g+=t(240,275,'CU/UC /kw/: labiovelar stop. "cueitl" (skirt) = /kwejt\u026c/.','middle','Ls')
    g+=hr(283)
    g+=sh(292,'LONG VOWELS')
    g+=t(240,302,'Nahuatl distinguishes vowel length: a vs. \u0101, i vs. \u012b, o vs. \u014d, u vs. \u016b.','middle','Ls')
    g+=t(240,312,'In modern texts often unmarked; Classical Nahuatl grammars mark length consistently.','middle','Ls')
    g+=t(240,322,'Tl\u0101tocatl (ruler) vs. tlatocatl (speaker). Meaning changes with length.','middle','Ls')
    g+=hr(330)
    g+=sh(339,'NAHUATL NUMERALS (VIGESIMAL BASE-20)')
    g+=t(240,349,'Nahuatl uses a vigesimal (base-20) counting system:','middle','Ls')
    nums=[('1','ce'),('2','ome'),('3','yei'),('4','nahui'),('5','mahcuilli'),
          ('6','chicuace'),('10','mahtlactli'),('15','caxtoltic'),
          ('20','cempohualli'),('400','centzontli'),('8000','cenxiquipilli')]
    for i,(n,w) in enumerate(nums):
        col=i%3; row=i//3
        x=65+col*130; y=359+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,409,'Base-20 counting: 20=1 score, 400=20x20, 8000=20x20x20 (like some Celtic numerals).','middle','Lx')
    g+=footer('47','Nahuatl','A','Script')
    return g+close_svg()

def build_47b():
    g=open_svg()
    g+=t(240,32,'NAHUATL','middle','T')
    g+=t(240,50,'Phonology \u2014 Sounds and Unique Features','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    cons=[('p /p/','bilabial stop'),('t /t/','alveolar stop'),('k /k/','velar stop'),
          ('kw /kw/','labiovelar stop'),('ts /ts/','alveolar affricate'),
          ('t\u0255 /t\u0255/','palatal affricate'),('t\u026c /t\u026c/','lateral affricate'),
          ('s /s/','alveolar fricative'),('\u0283 /\u0283/','postalveolar'),
          ('l /l/','lateral'),('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),
          ('w /w/','labio-velar approx'),('y /j/','palatal approx'),
          ('h /h/','glottal fric'),('\u0294 /\u0294/','glottal stop')]
    for i,(c,desc) in enumerate(cons):
        col=i%2; row=i//2
        x=80+col*200; y=82+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(175)
    g+=sh(184,'TL \u2014 LATERAL AFFRICATE')
    g+=t(240,194,'TL /t\u026c/: simultaneous alveolar stop + lateral fricative release.','middle','Ls')
    g+=t(240,204,'Unique to Nahuatl and related Uto-Aztecan languages; not found in most world languages.','middle','Ls')
    g+=t(240,214,'Examples: atl (water), tlatoa (speak), tlahtoa (speak carefully), xochitl (flower).','middle','Ls')
    g+=t(240,224,'Word-final tl: released with lateral air on both sides of tongue tip.','middle','Ls')
    g+=hr(232)
    g+=sh(241,'VOWEL SYSTEM \u2014 4 VOWELS + LENGTH')
    vowels=[('a /a/ : \u0101 /a\u02d0/','open central: atl (water), \u0101matl (paper)'),
            ('e /e/ : \u0113 /e\u02d0/','mid-front: te (stone), t\u0113tl (stone)'),
            ('i /i/ : \u012b /i\u02d0/','high front: ichtli (thread)'),
            ('o /o/ : \u014d /o\u02d0/','mid-back: ocelotl (jaguar)')]
    for i,(v,ex) in enumerate(vowels):
        y=251+i*11
        g+=t(120,y,v,'middle','Ls'); g+=t(340,y,ex,'middle','Lx')
    g+=hr(300)
    g+=sh(309,'GLOTTAL STOP')
    g+=t(240,319,'Glottal stop /\u0294/ phonemic in Classical Nahuatl. Often unmarked in modern texts.','middle','Ls')
    g+=t(240,329,'Contrasts: "toca" (to sow) vs. "to\u02bca" (our aunt). Context-critical.','middle','Ls')
    g+=hr(337)
    g+=sh(346,'STRESS')
    g+=t(240,356,'Stress: penultimate syllable in Classical Nahuatl.','middle','Ls')
    g+=t(240,366,'Modern dialects vary; some have shifted stress patterns.','middle','Ls')
    g+=footer('47','Nahuatl','B','Phonology')
    return g+close_svg()

def build_47c():
    g=open_svg()
    g+=t(240,32,'NAHUATL','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SOV, POLYSYNTHETIC')
    g+=t(240,82,'Nahuatl is SOV and polysynthetic: entire sentences can be single words.','middle','Ls')
    g+=t(240,92,'Nicmictia. I kill it. (ni=I c=it mictia=kill/make-die) One verb = full sentence.','middle','Ls')
    g+=t(240,102,'Nimitztlazohtla. I love you. (ni=I mitz=you tlazohtle=love)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'SUBJECT-OBJECT PREFIXES ON VERBS')
    g+=t(240,129,'Verb template: Subject prefix + Object prefix + Root + Tense/Aspect suffix.','middle','Ls')
    subj=[('ni-','I (1sg)'),('ti-','you (2sg) / we (1pl)'),('\u00d8-','he/she/it (3sg)'),
          ('an-','you all (2pl)'),('\u00d8-','they (3pl)')]
    obj=[('nech-','me'),('mitz-','you'),('c-/qu-','him/her/it'),
         ('tech-','us'),('amech-','you all'),('kin-','them')]
    g+=t(150,139,'Subject prefixes:','middle','Ls'); g+=t(350,139,'Object prefixes:','middle','Ls')
    for i,(p,gloss) in enumerate(subj):
        y=149+i*10
        g+=t(100,y,f'{p} {gloss}','middle','Lx')
    for i,(p,gloss) in enumerate(obj):
        y=149+i*10
        g+=t(330,y,f'{p} {gloss}','middle','Lx')
    g+=hr(205)
    g+=sh(214,'VERB MORPHOLOGY')
    verbs=[('ni-tla-cua','I eat something (general)'),('ni-tamalli-cua','I eat tamales'),
           ('ni-tla-cua-ya','I was eating (imperfect)'),('o-ni-tla-cua','I ate (past)'),
           ('ni-tla-cua-z','I will eat'),('ma ni-tla-cua','let me eat (optative)'),
           ('a\u0101mo ni-tla-cua','I don\'t eat (neg: a\u0101mo)')]
    for i,(form,gloss) in enumerate(verbs):
        y=224+i*10
        g+=t(130,y,form,'middle','L'); g+=t(330,y,gloss,'middle','Ls')
    g+=hr(310)
    g+=sh(319,'CORE VOCABULARY')
    vocab=[('n\u0101huatl','Nahuatl language (clear speech)'),('tlazohcamati','thank you'),
           ('quemah','yes'),('a\u0101mo','no/not'),('m\u0101 timoyolcuiti','excuse me'),
           ('quen timoyectia?','how are you?'),('cualli nimoyectia','I am fine'),
           ('nimitztlazohtla','I love you'),('atl','water'),('tletl','fire'),
           ('tlalli','earth'),('tlacatl','person'),('cahuitl','time'),
           ('metztli','moon'),('citlalin','star'),('yollo-tl','heart'),
           ('tlazohtlaliztli','love'),('ixtlamachiliztli','freedom'),
           ('ilnamiqui','to remember'),('moztla','tomorrow / future'),
           ('cemanahuac','the world'),('nemiliztli','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=329+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('47','Nahuatl','C','Grammar')
    return g+close_svg()

def build_47d():
    g=open_svg()
    g+=t(240,32,'NAHUATL','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. HUEHUETLAHTOLLI \u2014 ANCIENT WORD')
    g+=t(240,80,'In ic tiqui\u0101huac, in ic timochihua tlalli ipan titemi.','middle','L')
    g+=t(240,90,'in-ic=so-that tiqui\u0101huac=you-came-out timochihua=you-become tlalli=earth ipan=on titemi=you-walk','middle','Lx')
    g+=t(240,100,'"So that you came out into the world, so that you walk upon the earth." (Huehuetlahtolli birth blessing)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. ILNAMIQUI \u2014 ON MEMORY')
    g+=t(240,128,'In tlahtolli mo-ilnamiqui, ahmo polihua; teyolloh ipan mochi-ua.','middle','L')
    g+=t(240,138,'tlahtolli=word mo-ilnamiqui=is-remembered ahmo=not polihua=is-lost','middle','Ls')
    g+=t(240,148,'teyolloh=in-hearts-of-people ipan=upon mochi-ua=it-is-made','middle','Ls')
    g+=t(240,158,'"The word that is remembered is not lost; it is made upon the hearts of people."','middle','F')
    g+=hr(167)
    g+=sh(176,'III. TOLTECAYOTL \u2014 ON CRAFT AND KNOWLEDGE')
    g+=t(240,186,'In toltecatl, iyolloco quimati, iyollopan quichihua.','middle','L')
    g+=t(240,196,'toltecatl=craftsperson iyolloco=in-their-heart quimati=knows iyollopan=with-their-heart quichihua=does','middle','Lx')
    g+=t(240,206,'"The craftsperson knows in their heart, does it with their heart." (Aztec concept of toltecayotl / mastery)','middle','F')
    g+=hr(215)
    g+=sh(224,'IV. HUITZTLAMPA \u2014 FORWARD')
    g+=t(240,234,'Tihuitzeh huitztlampa, tilnamiquini in tohueyitatahuan.','middle','L')
    g+=t(240,244,'tihuitzeh=we-go huitztlampa=toward-the-south/forward tilnamiquini=while-remembering','middle','Ls')
    g+=t(240,254,'in=our tohueyitatahuan=great-grandfathers/ancestors','middle','Ls')
    g+=t(240,264,'"We go forward, remembering our ancestors." (guiding principle)','middle','F')
    g+=hr(273)
    g+=sh(282,'V. BRIDGE PHRASE')
    g+=t(240,294,'In axcan tlahtoa inin, momac oticchiuhqueh,','middle','L')
    g+=t(240,304,'amo tlamach, in tlahtoa huitztlampa tlalnamiquini.','middle','L')
    g+=t(240,318,'in-axcan=this-now tlahtoa-inin=says-this momac=for-you oticchiuhqueh=we-made-it','middle','Ls')
    g+=t(240,327,'amo-tlamach=without-payment in-tlahtoa=those-who huitztlampa=toward-forward','middle','Ls')
    g+=t(240,336,'tlalnamiquini=are-remembering','middle','Ls')
    g+=t(240,348,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(359)
    g+=sh(368,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,378,'Huitztlampa = "toward the south / toward the direction of the thorn." In Aztec','middle','Ls')
    g+=t(240,388,'cosmology, the future is in the south (the direction toward which one walks ahead).','middle','Ls')
    g+=t(240,398,'Tlalnamiquini = "remembering upon the earth." Amo tlamach = free/without payment.','middle','Ls')
    g+=t(240,408,'Polysynthetic grammar compresses the entire meaning into dense verb complexes.','middle','Ls')
    g+=hr(416)
    g+=sh(425,'LANGUAGE NOTES')
    g+=t(240,435,'Nahuatl: ~1.7 million speakers in Mexico (Puebla, Veracruz, Guerrero, Hidalgo).','middle','Ls')
    g+=t(240,445,'Language family: Uto-Aztecan (also includes Hopi, Comanche, Shoshone, Yaqui).','middle','Ls')
    g+=t(240,455,'Classical Nahuatl: language of the Aztec Triple Alliance (~1428-1521 CE).','middle','Ls')
    g+=t(240,465,'Words in English: chocolate, tomato, avocado, chile, coyote, ocelot, tamale.','middle','Ls')
    g+=footer('47','Nahuatl','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate47a_nahuatl_script.svg': build_47a(),
        'plate47b_nahuatl_phonology.svg': build_47b(),
        'plate47c_nahuatl_grammar.svg': build_47c(),
        'plate47d_nahuatl_text.svg': build_47d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
