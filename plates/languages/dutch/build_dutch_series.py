"""Build script — Dutch series plates 49A–49D (Remember Forward)"""
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

def build_49a():
    g=open_svg()
    g+=t(240,32,'DUTCH','middle','T')
    g+=t(240,50,'Nederlands \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Dutch uses the Latin alphabet (26 letters). Spelling is largely phonemic.','middle','Ls')
    g+=t(240,94,'More regular than English; fewer silent letters. IJ (/\u025b\u026a/) is sometimes counted as 27th letter.','middle','Ls')
    g+=t(240,104,'Long vowels: doubled in closed syllables (aa, ee, oo, uu) or single in open syllables.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'ALPHABET')
    g+=t(240,131,'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z','middle','L')
    g+=t(240,141,'Special: IJ (ligature), sometimes written as \u0132\u0133. Treated as one letter alphabetically.','middle','Ls')
    g+=hr(149)
    g+=sh(158,'VOWEL SPELLING RULES')
    g+=t(240,168,'Dutch vowel length is predictable from spelling:','middle','Ls')
    rules=[('Open syllable: single vowel = long','ba-ker /ba\u02d0k\u0259r/, le-ven /le\u02d0v\u0259(n)/'),
           ('Closed syllable: double vowel = long','baal /ba\u02d0l/, been /be\u02d0n/, boot /bo\u02d0t/'),
           ('Closed syllable: single vowel = short','bal /b\u0251l/, bed /b\u025bt/, bot /b\u0254t/'),
           ('OE = /u\u02d0/: "boek" (book) /bu\u02d0k/','not a double vowel, special digraph'),
           ('IJ/EI = /\u025b\u026a/: "mijn" (my) /m\u025b\u026a(n)/','same sound, two spellings'),
           ('UI = /\u0153y/: "huis" (house) /h\u0153ys/','front rounded diphthong')]
    for i,(rule,ex) in enumerate(rules):
        y=178+i*11
        g+=t(150,y,rule,'middle','Ls'); g+=t(370,y,ex,'middle','Lx')
    g+=hr(250)
    g+=sh(259,'G AND CH \u2014 VELAR FRICATIVES')
    g+=t(240,269,'Dutch G /\u0263/ or /x/: velar fricative. The distinctive "guttural G."','middle','Ls')
    g+=t(240,279,'Northern NL: voiced /\u0263/: "goed" /\u0263ut/. Southern NL/Belgium: voiceless /x/.','middle','Ls')
    g+=t(240,289,'CH /x/: voiceless velar fricative: "licht" (light) /l\u026ax t/, "acht" /\u0251xt/.','middle','Ls')
    g+=t(240,299,'SCH = /sx/: "school" /sxo\u02d0l/, "schrijven" (write) /sxr\u025b\u026av\u0259(n)/.','middle','Ls')
    g+=hr(307)
    g+=sh(316,'DUTCH NUMERALS')
    nums=[('0','nul'),('1','een'),('2','twee'),('3','drie'),('4','vier'),('5','vijf'),
          ('6','zes'),('7','zeven'),('8','acht'),('9','negen'),('10','tien'),
          ('20','twintig'),('100','honderd'),('1000','duizend')]
    for i,(n,w) in enumerate(nums):
        col=i%4; row=i//4
        x=55+col*95; y=326+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=hr(376)
    g+=sh(385,'SCRIPT HISTORY')
    g+=t(240,395,'Dutch: standard language since ~16th century (Statenbijbel 1637 standardised spelling).','middle','Ls')
    g+=t(240,405,'Latin alphabet adopted with Christianity (~8th century in Low Countries).','middle','Ls')
    g+=t(240,415,'Dutch spelling reform 1947/1954/1995/2005: simplified some older spellings.','middle','Ls')
    g+=t(240,425,'Afrikaans (S. Africa, Suriname) is a simplified daughter language of Dutch.','middle','Ls')
    g+=footer('49','Dutch','A','Script')
    return g+close_svg()

def build_49b():
    g=open_svg()
    g+=t(240,32,'DUTCH','middle','T')
    g+=t(240,50,'Phonology \u2014 Guttural G, Vowels, Diphthongs','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    cons=[('p /p/','bilabial stop'),('b /b/','bilabial stop vd'),
          ('t /t/','alveolar stop'),('d /d/','alveolar stop vd'),
          ('k /k/','velar stop'),('\u0261 /\u0261/','velar stop vd (before vowels only)'),
          ('f /f/','labiodental'),('v /v/','labiodental vd'),
          ('s /s/','alveolar fric'),('z /z/','alveolar fric vd'),
          ('\u0283 /\u0283/','postalveolar fric'),('\u0292 /\u0292/','postalveolar vd'),
          ('x /x/','velar fricative vl (ch, g south)'),('\u0263 /\u0263/','velar fricative vd (g north)'),
          ('h /h/','glottal'),('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),
          ('\u014b /\u014b/','velar nasal (ng)'),('l /l/','lateral'),
          ('r /r/','trill/uvular (varies by region)'),('w /\u03b2/','bilabial approx (between v/w)'),('j /j/','palatal')]
    for i,(c,desc) in enumerate(cons):
        col=i%2; row=i//2
        x=80+col*200; y=82+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(225)
    g+=sh(234,'VOWEL SYSTEM')
    vowels=[('a /\u0251/ (short)','bal (ball), man (man)'),('\u0101 /a\u02d0/ (long)','baal (bale), maan (moon)'),
            ('e /\u025b/ (short)','bed (bed), net (net)'),('\u0113 /e\u02d0/ (long)','been (leg/bone)'),
            ('\u0259 /\u0259/ (schwa)','de (the), unstressed syllables'),
            ('i /\u026a/ (short)','bit (bite)'),('\u012b /i\u02d0/ (long)','niet (not)'),
            ('o /\u0254/ (short)','bot (bone)'),('\u014d /o\u02d0/ (long)','boom (tree)'),
            ('u /\u028a/ (short)','bus (bus)'),('\u016b /u\u02d0/ (long)','boek (book: oe=/u\u02d0/)'),
            ('\u00f6 /\u00f8\u02d0/ (eu)','deur (door) /d\u00f8\u02d0r/')]
    for i,(v,ex) in enumerate(vowels):
        col=i%2; row=i//2
        x=80+col*200; y=244+row*10
        g+=t(x,y,f'{v}: {ex}','middle','Lx')
    g+=hr(316)
    g+=sh(325,'DIPHTHONGS')
    diph=[('ij/ei /\u025b\u026a/','mijn (my), wijn (wine), ijzer (iron)'),
          ('ui /\u0153y/','huis (house), uit (out), ruim (spacious)'),
          ('ou/au /\u0251\u028a/','oud (old), auto, blauw (blue)')]
    for i,(d,ex) in enumerate(diph):
        y=335+i*11
        g+=t(90,y,d,'middle','Ls'); g+=t(310,y,ex,'middle','Lx')
    g+=hr(375)
    g+=sh(384,'FINAL DEVOICING')
    g+=t(240,394,'Dutch devoices obstruents (stops, fricatives) at word-final position:','middle','Ls')
    g+=t(240,404,'hond (dog) /h\u0254nt/ (not /h\u0254nd/). honden (dogs) /h\u0254nd\u0259n/ (restored in plural).','middle','Ls')
    g+=t(240,414,'bed /b\u025bt/ (not /b\u025bd/). bedden /b\u025bd\u0259n/. Key rule for Dutch learners.','middle','Ls')
    g+=footer('49','Dutch','B','Phonology')
    return g+close_svg()

def build_49c():
    g=open_svg()
    g+=t(240,32,'DUTCH','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 V2 (VERB SECOND)')
    g+=t(240,82,'Dutch is V2: the finite verb always occupies the second position in a main clause.','middle','Ls')
    g+=t(240,92,'Ik lees het boek. I read the book. (standard SVO)','middle','Ls')
    g+=t(240,102,'Gisteren las ik het boek. Yesterday read I the book. (V2: verb stays 2nd)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'NOUN GENDER \u2014 DE / HET')
    g+=t(240,129,'Dutch has 2 grammatical genders: common (de) and neuter (het).','middle','Ls')
    g+=t(240,139,'de words: de man (man), de vrouw (woman), de tafel (table).','middle','Ls')
    g+=t(240,149,'het words: het kind (child), het huis (house), het water (water).','middle','Ls')
    g+=t(240,159,'Gender must be learned for each noun. Affects adjective endings and pronouns.','middle','Ls')
    g+=hr(167)
    g+=sh(176,'VERB CONJUGATION')
    g+=t(240,186,'Weak (regular) verbs: werken (to work): ik werk, jij werkt, hij werkt, wij werken.','middle','Ls')
    g+=t(240,196,'Strong (irregular): rijden (ride): ik rijd, reed, gereden. schrijven: schrijf, schreef, geschreven.','middle','Ls')
    g+=t(240,206,'Perfect tense: hebben/zijn + past participle: ik heb gewerkt / ik ben gegaan.','middle','Ls')
    g+=hr(214)
    g+=sh(223,'SEPARABLE VERBS')
    g+=t(240,233,'Dutch has many separable verbs: prefix separates in main clause.','middle','Ls')
    g+=t(240,243,'opbellen (call up): Ik bel hem op. I call him up. (op goes to end)','middle','Ls')
    g+=t(240,253,'aanzetten (turn on): Hij zet de radio aan. He turns the radio on.','middle','Ls')
    g+=hr(261)
    g+=sh(270,'CORE VOCABULARY')
    vocab=[('hallo / goedendag','hello'),('dank u / bedankt','thank you'),('ja','yes'),
           ('nee','no'),('sorry / pardon','excuse me'),('hoe gaat het?','how are you?'),
           ('goed, dank u','fine, thank you'),('ik hou van jou','I love you'),
           ('water','water'),('vuur','fire'),('aarde','earth'),
           ('persoon / mens','person'),('tijd','time'),('maan','moon'),
           ('ster','star'),('hart','heart'),('liefde','love'),
           ('vrijheid','freedom'),('herinnering','memory'),
           ('toekomst','future'),('wereld','world'),('leven','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=280+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=hr(395)
    g+=sh(404,'DUTCH IN SURINAME AND BEYOND')
    g+=t(240,414,'Dutch is official in Netherlands, Belgium (Flanders), Suriname, Aruba, Cura\u00e7ao, Bonaire.','middle','Ls')
    g+=t(240,424,'Suriname: Dutch co-official with Sranan Tongo (an English creole) and ~20 others.','middle','Ls')
    g+=t(240,434,'Afrikaans (South Africa): descended from 17th-century Dutch settlers; ~7 million speakers.','middle','Ls')
    g+=footer('49','Dutch','C','Grammar')
    return g+close_svg()

def build_49d():
    g=open_svg()
    g+=t(240,32,'DUTCH','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. SPREEKWOORD \u2014 PROVERB')
    g+=t(240,80,'Wie niet waagt, wie niet wint.','middle','L')
    g+=t(240,90,'wie=who niet=not waagt=dares wint=wins','middle','Ls')
    g+=t(240,100,'"Who dares not, wins not." (Dutch proverb on courage and forward action)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. HERINNERING \u2014 ON MEMORY')
    g+=t(240,128,'Wie zijn verleden niet kent, is gedwongen het te herhalen.','middle','L')
    g+=t(240,138,'wie=who zijn=his verleden=past niet-kent=does-not-know','middle','Ls')
    g+=t(240,148,'is-gedwongen=is-forced het-te-herhalen=to-repeat-it','middle','Ls')
    g+=t(240,158,'"Who does not know their past is forced to repeat it." (Dutch version of Santayana)','middle','F')
    g+=hr(167)
    g+=sh(176,'III. KENNIS \u2014 ON KNOWLEDGE')
    g+=t(240,186,'Kennis is de enige rijkdom die groeit als je haar deelt.','middle','L')
    g+=t(240,196,'kennis=knowledge is=is de-enige=the-only rijkdom=wealth die=that groeit=grows','middle','Ls')
    g+=t(240,206,'als=when je=you haar=it deelt=share','middle','Ls')
    g+=t(240,216,'"Knowledge is the only wealth that grows when you share it." (Dutch educational saying)','middle','F')
    g+=hr(225)
    g+=sh(234,'IV. VOORUIT \u2014 FORWARD')
    g+=t(240,244,'Wij gaan vooruit, terwijl wij denken aan hen die ons voorgingen.','middle','L')
    g+=t(240,254,'wij=we gaan=go vooruit=forward terwijl=while wij=we denken-aan=think-of','middle','Ls')
    g+=t(240,264,'hen=them die=who ons=us voorgingen=preceded/went-before','middle','Ls')
    g+=t(240,274,'"We go forward, while thinking of those who preceded us." (guiding principle)','middle','F')
    g+=hr(283)
    g+=sh(292,'V. BRIDGE PHRASE')
    g+=t(240,305,'Dit werd voor jou gemaakt, gratis,','middle','L')
    g+=t(240,315,'door mensen die vooruit herinnerden.','middle','L')
    g+=t(240,329,'dit=this werd=was gemaakt=made voor-jou=for-you gratis=free of charge','middle','Ls')
    g+=t(240,338,'door=by mensen=people die=who vooruit=forward herinnerden=remembered','middle','Ls')
    g+=t(240,350,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(361)
    g+=sh(370,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,380,'Vooruit = "forward / ahead" (voor=before + uit=out). Herinnerden = "remembered" (past).','middle','Ls')
    g+=t(240,390,'"Vooruit herinneren" is a coined phrase: "remember forward." In Dutch, herinneren','middle','Ls')
    g+=t(240,400,'means "to remember" (recall the past); adding vooruit = directing that into the future.','middle','Ls')
    g+=t(240,410,'Gratis = free of charge (from Latin gratis, "for grace/favor").','middle','Ls')
    g+=hr(418)
    g+=sh(427,'LANGUAGE NOTES')
    g+=t(240,437,'Dutch: ~24 million L1 speakers in Netherlands, Belgium (Flanders), Suriname.','middle','Ls')
    g+=t(240,447,'Language family: Indo-European, West Germanic (with English, German, Frisian).','middle','Ls')
    g+=t(240,457,'Dutch was dominant colonial language in South Africa, Indonesia, New York (New Amsterdam).','middle','Ls')
    g+=t(240,467,'Hundreds of English words from Dutch: yacht, easel, landscape, cookie, boss, cruise.','middle','Ls')
    g+=footer('49','Dutch','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate49a_dutch_script.svg': build_49a(),
        'plate49b_dutch_phonology.svg': build_49b(),
        'plate49c_dutch_grammar.svg': build_49c(),
        'plate49d_dutch_text.svg': build_49d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
