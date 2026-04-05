"""Build script — Tagalog series plates 42A–42D (Remember Forward)"""
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

def build_42a():
    g=open_svg()
    g+=t(240,32,'TAGALOG / FILIPINO','middle','T')
    g+=t(240,50,'Script \u2014 Latin Alphabet + Baybayin','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Modern Filipino uses the Latin alphabet (28 letters + ng, adapted from Spanish era).','middle','Ls')
    g+=t(240,94,'Standard Filipino alphabet (1976, revised 2013): a b k d e g h i l m n ng o p r s t u w y.','middle','Ls')
    g+=t(240,104,'Spanish-derived letters retained for loanwords: c, f, j, q, v, x, z.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'BAYBAYIN \u2014 TRADITIONAL SCRIPT')
    g+=t(240,131,'Baybayin (pre-colonial Tagalog): abugida used before Spanish colonisation (~16th c).','middle','Ls')
    g+=t(240,141,'17 consonants, each with inherent /a/ vowel. Diacritics above/below modify vowel.','middle','Ls')
    g+=t(240,151,'Cross-mark (pamudpod) kills the inherent vowel for final consonants.','middle','Ls')
    g+=t(240,161,'Baybayin revived as cultural symbol; now taught in Philippine schools.','middle','Ls')
    bbayin=[('\u1700','ka /ka/'),('\u1701','ga /\u0261a/'),('\u1702','nga /\u014ba/'),
            ('\u1703','ta /ta/'),('\u1704','da /da/'),('\u1705','na /na/'),
            ('\u1706','pa /pa/'),('\u1707','ba /ba/'),('\u1708','ma /ma/'),
            ('\u1709','ya /ja/'),('\u170a','la /la/'),('\u170b','wa /wa/'),
            ('\u170c','sa /sa/'),('\u170e','ha /ha/'),('\u170f','a /a/')]
    for i,(bb,desc) in enumerate(bbayin):
        col=i%5; row=i//5
        x=50+col*78; y=171+row*14
        g+=t(x,y,bb,'middle','L'); g+=t(x,y+9,desc,'middle','Lx')
    g+=hr(218)
    g+=sh(227,'MODERN FILIPINO ALPHABET')
    letters='A B K D E G H I L M N Ng O P R S T U W Y (+ C F J Q V X Z for loanwords)'
    g+=t(240,237,letters,'middle','Ls')
    g+=t(240,247,'Note: K replaces Spanish C/QU; W and Y are vowels in some contexts.','middle','Ls')
    g+=hr(255)
    g+=sh(264,'DIGRAPH NG')
    g+=t(240,274,'NG /\u014b/: the 19th letter. Counts as single letter in alphabetical order.','middle','Ls')
    g+=t(240,284,'Used as velar nasal onset (ngayon = now) and in final position (buhay = life).','middle','Ls')
    g+=t(240,294,'Ngang (with A inherent in Baybayin) = the Baybayin character for /\u014ba/.','middle','Ls')
    g+=hr(302)
    g+=sh(311,'ACCENT MARKS \u2014 STRESS AND GLOTTAL STOP')
    g+=t(240,321,'Tagalog marks stress and glottal stops with diacritics in formal/educational texts:','middle','Ls')
    g+=t(240,331,'Acute \u00b4 = stress on that vowel: bah\u00e1y (house) vs. b\u00e1hay (dialect variant).','middle','Ls')
    g+=t(240,341,'Circumflex \u02c6 = final stressed vowel + glottal stop: mat\u00e2 (eyes).','middle','Ls')
    g+=t(240,351,'Grave ` = final unstressed vowel + glottal stop: bok\u00e0 (hole).','middle','Ls')
    g+=hr(359)
    g+=sh(368,'NUMERALS')
    nums=[('1','isa'),('2','dalawa'),('3','tatlo'),('4','apat'),('5','lima'),
          ('6','anim'),('7','pito'),('8','walo'),('9','siyam'),('10','sampu')]
    for i,(n,w) in enumerate(nums):
        col=i%5; row=i//5
        x=55+col*78; y=378+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,398,'100 = isang daan · 1000 = isang libo · 1,000,000 = isang milyon','middle','Ls')
    g+=footer('42','Tagalog','A','Script')
    return g+close_svg()

def build_42b():
    g=open_svg()
    g+=t(240,32,'TAGALOG / FILIPINO','middle','T')
    g+=t(240,50,'Phonology \u2014 Sounds and Stress','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    cons=[('p /p/','bilabial stop vl'),('b /b/','bilabial stop vd'),
          ('t /t/','alveolar stop vl'),('d /d/','alveolar stop vd'),
          ('k /k/','velar stop vl'),('g /\u0261/','velar stop vd'),
          ('\u0294 /\u0294/','glottal stop (unmarked in spelling)'),
          ('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),
          ('ng /\u014b/','velar nasal'),('l /l/','lateral'),('r /r/','trill/tap'),
          ('s /s/','alveolar fricative'),('h /h/','glottal fricative'),
          ('w /w/','labio-velar approx'),('y /j/','palatal approx'),
          ('f /f/','labiodental (loanwords)'),('v /v/','labiodental vd (loanwords)')]
    for i,(c,desc) in enumerate(cons):
        col=i%2; row=i//2
        x=80+col*200; y=82+row*10
        g+=t(x,y,f'{c} {desc}','middle','Lx')
    g+=hr(187)
    g+=sh(196,'VOWEL SYSTEM \u2014 5 VOWELS')
    vowels=[('a /a/','open front: bahay (house)'),('e /\u025b/','mid-front: bente (twenty)'),
            ('i /i/','high front: isa (one)'),('o /o/','mid-back: oo (yes)'),
            ('u /u/','high back: uno (one, Spanish loan)')]
    for i,(v,ex) in enumerate(vowels):
        y=206+i*10
        g+=t(80,y,v,'middle','Ls'); g+=t(300,y,ex,'middle','Lx')
    g+=hr(262)
    g+=sh(271,'GLOTTAL STOP \u2014 KEY FEATURE')
    g+=t(240,281,'The glottal stop /\u0294/ is phonemic in Tagalog but not written in modern orthography.','middle','Ls')
    g+=t(240,291,'Word-final glottal stop: mata (eyes) /ma.ta\u0294/ vs. mata (to kill) /ma.ta/.','middle','Ls')
    g+=t(240,301,'Medial glottal: baa /ba\u0294a/ (to brand) vs. baa /ba.a/.','middle','Ls')
    g+=t(240,311,'Learners must acquire glottal placement from context and exposure.','middle','Ls')
    g+=hr(319)
    g+=sh(328,'STRESS SYSTEM')
    g+=t(240,338,'Tagalog has phonemic stress (distinguishes word meaning).','middle','Ls')
    g+=t(240,348,'Default: stress on penultimate (second-to-last) syllable.','middle','Ls')
    g+=t(240,358,'Final stress (mabuting = becoming good) vs. penultimate (mabuting = good [linker]).','middle','Ls')
    g+=t(240,368,'Stress + glottal stop combinations create multiple minimal pairs.','middle','Ls')
    g+=hr(376)
    g+=sh(385,'LOAN PHONOLOGY')
    g+=t(240,395,'Spanish loans retain /f v/ and clusters: flores, crema, presidente.','middle','Ls')
    g+=t(240,405,'English loans common in modern speech: computer, internet, cellphone.','middle','Ls')
    g+=t(240,415,'Tagalog easily adapts foreign words to CV syllable structure.','middle','Ls')
    g+=footer('42','Tagalog','B','Phonology')
    return g+close_svg()

def build_42c():
    g=open_svg()
    g+=t(240,32,'TAGALOG / FILIPINO','middle','T')
    g+=t(240,50,'Grammar \u2014 Focus System & Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 FOCUS SYSTEM (UNIQUE)')
    g+=t(240,82,'Tagalog has a focus/trigger system rather than standard SVO/SOV.','middle','Ls')
    g+=t(240,92,'The focus particle marks which argument is "in focus" (topic/pivot).','middle','Ls')
    g+=t(240,102,'Verb affixes change to show which semantic role is focused.','middle','Ls')
    g+=hr(110)
    g+=sh(119,'FOCUS TYPES')
    focus=[('Actor focus (AF)','-um- / mag-','Bumili siya ng tinapay. HE bought bread.'),
           ('Patient/Object focus (PF)','-in / -hin','Binili niya ang tinapay. BREAD was bought by him.'),
           ('Locative focus (LF)','-an','Binilhan niya ng tinapay ang tindahan. AT the store.'),
           ('Benefactive focus (BF)','-an / i-','Ibinili niya siya ng tinapay. FOR her, he bought bread.')]
    for i,(name,affix,ex) in enumerate(focus):
        y=129+i*14
        g+=t(100,y,name,'middle','Ls'); g+=t(190,y,affix,'middle','Ls'); g+=t(360,y,ex,'middle','Lx')
    g+=hr(195)
    g+=sh(204,'ANG, NG, SA \u2014 CASE MARKERS')
    g+=t(240,214,'Tagalog uses three case markers (not inflections on the noun):','middle','Ls')
    markers=[('ang','nominative / focus / definite: ang bahay (THE house)'),
             ('ng /na\u014b/','genitive/object: ng bahay (of a house)'),
             ('sa','oblique/locative: sa bahay (at/in/to the house)')]
    for i,(m,gloss) in enumerate(markers):
        y=224+i*10
        g+=t(80,y,m,'middle','L'); g+=t(290,y,gloss,'middle','Ls')
    g+=hr(260)
    g+=sh(269,'LINKER \u2014 NA/NG')
    g+=t(240,279,'Linker na (after consonant) / ng (after vowel) connects modifier to head.','middle','Ls')
    g+=t(240,289,'magandang babae = beautiful woman (maganda + ng + babae).','middle','Ls')
    g+=t(240,299,'Linker marks adjectives, relative clauses, and genitive relationships.','middle','Ls')
    g+=hr(307)
    g+=sh(316,'CORE VOCABULARY')
    vocab=[('mabuhay','welcome / long live'),('salamat','thank you'),('oo','yes'),
           ('hindi','no/not'),('paumanhin','excuse me/sorry'),('kamusta ka?','how are you?'),
           ('mabuti naman','I am fine/well'),('mahal kita','I love you'),
           ('tubig','water'),('apoy','fire'),('lupa','earth/land'),
           ('tao','person'),('oras','time'),('buwan','moon'),
           ('bituin','star'),('puso','heart'),('pagmamahal','love'),
           ('kalayaan','freedom'),('alaala','memory/remembrance'),
           ('kinabukasan','future/tomorrow'),('mundo','world'),('buhay','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<11 else 1
        y=326+(i if i<11 else i-11)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('42','Tagalog','C','Grammar')
    return g+close_svg()

def build_42d():
    g=open_svg()
    g+=t(240,32,'TAGALOG / FILIPINO','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. SALAWIKAIN \u2014 PROVERB')
    g+=t(240,80,'Ang hindi marunong lumingon sa pinanggalingan ay hindi makararating sa paroroonan.','middle','Ls')
    g+=t(240,90,'hindi=not marunong=know lumingon=look-back pinanggalingan=origin','middle','Ls')
    g+=t(240,100,'hindi=not makararating=reach paroroonan=destination','middle','Ls')
    g+=t(240,110,'"One who does not look back at where they came from will not reach their destination."','middle','F')
    g+=hr(119)
    g+=sh(128,'II. ALAALA \u2014 ON MEMORY')
    g+=t(240,138,'Ang alaala ng nakaraan ay gabay sa kinabukasan.','middle','L')
    g+=t(240,148,'alaala=memory nakaraan=the-past gabay=guide kinabukasan=future/tomorrow','middle','Ls')
    g+=t(240,158,'"The memory of the past is a guide to the future." (Filipino saying)','middle','F')
    g+=hr(167)
    g+=sh(176,'III. KAALAMAN \u2014 ON KNOWLEDGE')
    g+=t(240,186,'Ang kaalaman ay kayamanan na hindi mananakaw.','middle','L')
    g+=t(240,196,'kaalaman=knowledge kayamanan=wealth hindi=not mananakaw=can-be-stolen','middle','Ls')
    g+=t(240,206,'"Knowledge is wealth that cannot be stolen." (Filipino educational proverb)','middle','F')
    g+=hr(215)
    g+=sh(224,'IV. PASULONG \u2014 FORWARD')
    g+=t(240,234,'Lumalakad tayong pasulong habang inaalala ang mga nauna sa atin.','middle','Ls')
    g+=t(240,244,'lumalakad=walk tayo=we pasulong=forward habang=while inaalala=remembering','middle','Ls')
    g+=t(240,254,'mga=plural-marker nauna=those-who-came-before atin=us','middle','Ls')
    g+=t(240,264,'"We walk forward while remembering those who came before us." (guiding principle)','middle','F')
    g+=hr(273)
    g+=sh(282,'V. BRIDGE PHRASE')
    g+=t(240,294,'Ang bagay na ito ay ginawa para sa iyo, nang libre,','middle','L')
    g+=t(240,304,'ng mga taong nagtatandang pasulong.','middle','L')
    g+=t(240,318,'bagay-na-ito=this-thing ginawa=was-made para-sa-iyo=for-you','middle','Ls')
    g+=t(240,327,'nang-libre=freely (without cost)','middle','Ls')
    g+=t(240,336,'ng-mga-tao=by-people nagtatandang=who-remember pasulong=forward','middle','Ls')
    g+=t(240,348,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(359)
    g+=sh(368,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,378,'Pasulong = "forward / ahead" (from pa- directional + sulong = advance).','middle','Ls')
    g+=t(240,388,'Nagtatandang pasulong = "who remember forward" — the -ng linker attaches pasulong','middle','Ls')
    g+=t(240,398,'to nagtatanda as an adverb of direction. Nang libre = "freely/at no cost."','middle','Ls')
    g+=t(240,408,'Philippine concept of utang na loob (debt of gratitude) inverted: this gift has none.','middle','Ls')
    g+=hr(416)
    g+=sh(425,'LANGUAGE NOTES')
    g+=t(240,435,'Tagalog: ~25 million L1 speakers; basis of Filipino, national language of Philippines.','middle','Ls')
    g+=t(240,445,'Language family: Austronesian, Malayo-Polynesian, Philippine branch.','middle','Ls')
    g+=t(240,455,'Related: Cebuano, Ilocano, Hiligaynon, Malay/Indonesian, Malagasy.','middle','Ls')
    g+=t(240,465,'Spanish influence ~333 years (1565-1898); English since 1898 (US period).','middle','Ls')
    g+=footer('42','Tagalog','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate42a_tagalog_script.svg': build_42a(),
        'plate42b_tagalog_phonology.svg': build_42b(),
        'plate42c_tagalog_grammar.svg': build_42c(),
        'plate42d_tagalog_text.svg': build_42d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
