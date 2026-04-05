"""Build script — Tok Pisin series plates 45A–45D (Remember Forward)"""
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

def build_45a():
    g=open_svg()
    g+=t(240,32,'TOK PISIN','middle','T')
    g+=t(240,50,'Script, Origins & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WHAT IS TOK PISIN?')
    g+=t(240,84,'Tok Pisin is an English-based creole language. Official language of Papua New Guinea.','middle','Ls')
    g+=t(240,94,'Developed from 19th-century Pacific pidgin English. Now a native language for 4+ million.','middle','Ls')
    g+=t(240,104,'Name: "Tok" = talk/language (from English), "Pisin" = pidgin (from English pidgin/pigeon).','middle','Ls')
    g+=hr(112)
    g+=sh(121,'WRITING SYSTEM')
    g+=t(240,131,'Tok Pisin uses the Latin alphabet (24 letters; no q, x in native words).','middle','Ls')
    g+=t(240,141,'Standardised orthography since ~1970s. Phonemic spelling (sounds = letters).','middle','Ls')
    g+=t(240,151,'Words usually spelled as pronounced, unlike English.','middle','Ls')
    g+=hr(159)
    g+=sh(168,'ALPHABET AND PHONEMIC SPELLING')
    g+=t(240,178,'A B D E F G H I J K L M N O P R S T U V W Y (24 letters + digraphs)','middle','Ls')
    g+=t(240,188,'Key digraphs: NG /\u014b/, NG- (velar nasal onset), AI /ai/, AU /au/, OI /oi/.','middle','Ls')
    g+=t(240,198,'English "th" = "t" in Tok Pisin: think = tingting. "sh" = "s": ship = sip.','middle','Ls')
    g+=hr(206)
    g+=sh(215,'ENGLISH SOURCE WORDS AND TRANSFORMATIONS')
    examples=[('man','man (person/man)'),('meri','Mary / woman (from English "Mary")'),
              ('pikinini','child (from Portuguese pequenino)'),('gras','grass / hair / fur'),
              ('han','hand / arm'),('lek','leg / foot'),('ai','eye'),
              ('bel','belly / stomach / feelings'),('het','head'),('pes','face'),
              ('haus','house'),('wara','water'),('paia','fire'),('graun','ground/earth'),
              ('gutpela','good (good+fellow)'),('bikpela','big (big+fellow)'),
              ('liklik','small (little+little, reduplication)'),('lapun','old (laplap+un)'),
              ('nau','now'),('baimbai / bai','future marker (by and by)')]
    for i,(tp,gloss) in enumerate(examples):
        col=i%2; row=i//2
        x=80+col*200; y=225+row*10
        g+=t(x,y,f'{tp} = {gloss}','middle','Lx')
    g+=hr(340)
    g+=sh(349,'LANGUAGE SOURCES')
    g+=t(240,359,'~80% English-derived vocabulary (colonial + labor contact language).','middle','Ls')
    g+=t(240,369,'~10% Tolai and Austronesian substrate: -im (transitive suffix from Tolai), -pela (fellow).','middle','Ls')
    g+=t(240,379,'~5% German (colonial era PNG was German New Guinea): maus (mouth, from Ger. Mund).','middle','Ls')
    g+=t(240,389,'Malay, Portuguese: pikinini (small child), susu (breast/milk).','middle','Ls')
    g+=hr(397)
    g+=sh(406,'NUMERALS')
    nums=[('0','siro'),('1','wan'),('2','tu'),('3','tri'),('4','foa'),
          ('5','faiv'),('6','sikis'),('7','seven'),('8','et'),('9','nain'),('10','ten')]
    for i,(n,w) in enumerate(nums):
        col=i%4; row=i//4
        x=55+col*95; y=416+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,446,'100 = wan handet · 1000 = wan tausen · 1,000,000 = wan milion','middle','Ls')
    g+=footer('45','Tok Pisin','A','Script')
    return g+close_svg()

def build_45b():
    g=open_svg()
    g+=t(240,32,'TOK PISIN','middle','T')
    g+=t(240,50,'Phonology \u2014 Creole Sound System','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    g+=t(240,82,'Tok Pisin has a relatively simple consonant system (~18 phonemes).','middle','Ls')
    cons=[('p /p/','bilabial stop'),('b /b/','bilabial stop vd'),
          ('t /t/','alveolar stop'),('d /d/','alveolar stop vd'),
          ('k /k/','velar stop'),('g /\u0261/','velar stop vd'),
          ('f /f/','labiodental'),('v /v/','labiodental vd'),
          ('s /s/','alveolar fricative'),('h /h/','glottal fricative'),
          ('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),
          ('ng /\u014b/','velar nasal'),('l /l/','lateral'),
          ('r /r/','trill or flap'),('w /w/','labio-velar'),('y /j/','palatal')]
    for i,(c,desc) in enumerate(cons):
        col=i%2; row=i//2
        x=80+col*200; y=92+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(187)
    g+=sh(196,'VOWEL SYSTEM \u2014 5 VOWELS')
    vowels=[('a /a/','open central: man (person)'),('e /\u025b/','mid-front: nem (name)'),
            ('i /i/','high front: bikpela (big)'),('o /\u0254/','mid-back: tokples (local language)'),
            ('u /u/','high back: gutpela (good)')]
    for i,(v,ex) in enumerate(vowels):
        y=206+i*10
        g+=t(80,y,v,'middle','Ls'); g+=t(300,y,ex,'middle','Lx')
    g+=hr(262)
    g+=sh(271,'PHONOLOGICAL SIMPLIFICATION FROM ENGLISH')
    g+=t(240,281,'English consonant clusters reduced: "strength" > stren, "scratch" > skraes.','middle','Ls')
    g+=t(240,291,'"th" (/\u03b8\u00f0/) absent: think = tingting, the = de/dispela.','middle','Ls')
    g+=t(240,301,'"sh" (/\u0283/) absent: ship = sip, shoe = su, wash = was.','middle','Ls')
    g+=t(240,311,'Final consonant clusters simplified: "hand" > han, "friend" > pren.','middle','Ls')
    g+=hr(319)
    g+=sh(328,'REDUPLICATION \u2014 PRODUCTIVE PROCESS')
    g+=t(240,338,'Reduplication marks plurality, repetition, or intensification:','middle','Ls')
    g+=t(240,348,'save (know) \u2192 savesave (know well/understand deeply).','middle','Ls')
    g+=t(240,358,'sing (sing) \u2192 singsing (music/traditional dance ceremony).','middle','Ls')
    g+=t(240,368,'gras (grass) \u2192 grasgras (weedy/overgrown).','middle','Ls')
    g+=t(240,378,'tok (speak) \u2192 toktok (conversation/talk/discuss).','middle','Ls')
    g+=hr(386)
    g+=sh(395,'STRESS AND INTONATION')
    g+=t(240,405,'Stress: generally on the penultimate syllable (inherited from English pattern).','middle','Ls')
    g+=t(240,415,'No tonal distinctions. Intonation patterns from Austronesian substrate + English.','middle','Ls')
    g+=footer('45','Tok Pisin','B','Phonology')
    return g+close_svg()

def build_45c():
    g=open_svg()
    g+=t(240,32,'TOK PISIN','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SVO')
    g+=t(240,82,'Tok Pisin is SVO. Very regular structure with few exceptions.','middle','Ls')
    g+=t(240,92,'Mi kaikai rais. I eat rice. (mi=I kaikai=eat rais=rice)','middle','Ls')
    g+=hr(100)
    g+=sh(109,'PRONOUNS')
    pros=[('mi','I'),('yu','you (sg)'),('em','he/she/it'),
          ('yumi (incl)','we (you+me)'),('mipela (excl)','we (not you)'),
          ('yupela','you (pl)'),('ol','they')]
    for i,(p,gloss) in enumerate(pros):
        y=119+i*10
        g+=t(120,y,p,'middle','L'); g+=t(300,y,gloss,'middle','Ls')
    g+=hr(193)
    g+=sh(202,'TRANSITIVE SUFFIX \u2014im')
    g+=t(240,212,'Many verbs require -im suffix for transitive use (from Tolai substrate):','middle','Ls')
    g+=t(240,222,'Lukim (see-it): Mi lukim yu. I see you.','middle','Ls')
    g+=t(240,232,'Helpim (help-it): Helpim mi! Help me!','middle','Ls')
    g+=t(240,242,'Kisim (catch/take-it): Em kisim dispela. He took this.','middle','Ls')
    g+=t(240,252,'Kaikai (eat) stays as kaikai (already transitive from form).','middle','Ls')
    g+=hr(260)
    g+=sh(269,'TENSE / ASPECT MARKERS')
    g+=t(240,279,'Bai (baimbai): future marker. Bai mi go = I will go.','middle','Ls')
    g+=t(240,289,'Pinis: completive aspect. Mi kaikai pinis = I have finished eating.','middle','Ls')
    g+=t(240,299,'Stap: progressive. Em stap slip = He is sleeping.','middle','Ls')
    g+=t(240,309,'Laik: want to / about to. Mi laik go = I want to go / I\'m going to go.','middle','Ls')
    g+=hr(317)
    g+=sh(326,'ADJECTIVE SUFFIX \u2014pela')
    g+=t(240,336,'Adjectives use -pela suffix (from English "fellow"): gutpela (good), bikpela (big).','middle','Ls')
    g+=t(240,346,'Dropped before nouns in some contexts: gut man (a good person, informal).','middle','Ls')
    g+=hr(354)
    g+=sh(363,'CORE VOCABULARY')
    vocab=[('gude','hello/good day'),('tenk yu','thank you'),('yes/ya','yes'),
           ('nogat','no/not'),('sori','sorry/excuse me'),('yu orait?','how are you?'),
           ('mi orait','I am fine'),('mi laikim yu','I love you'),
           ('wara','water'),('paia','fire'),('graun','earth/ground'),
           ('man/meri','person (man/woman)'),('taim','time'),('mun','moon'),
           ('sta','star'),('bel','stomach/feelings/heart'),('lav','love'),
           ('fri / fridom','free / freedom'),('tingting','memory/thought/mind'),
           ('tumora','tomorrow / future'),('graun/wol','world'),('laip','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<11 else 1
        y=373+(i if i<11 else i-11)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('45','Tok Pisin','C','Grammar')
    return g+close_svg()

def build_45d():
    g=open_svg()
    g+=t(240,32,'TOK PISIN','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. TOKTOK \u2014 PROVERB')
    g+=t(240,80,'Gutpela save i stap long bel bilong ol lapun man.','middle','L')
    g+=t(240,90,'gutpela=good save=knowledge i=predicate-marker stap=stay/is long=in bel=belly/inside','middle','Ls')
    g+=t(240,100,'bilong=of ol=plural lapun=old man=people','middle','Ls')
    g+=t(240,110,'"Good knowledge lives inside old people." (PNG proverb on elder wisdom)','middle','F')
    g+=hr(119)
    g+=sh(128,'II. TINGTING \u2014 ON MEMORY')
    g+=t(240,138,'Sapos yu tingim ol manmeri i go pinis, yu stap strong.','middle','L')
    g+=t(240,148,'sapos=if yu=you tingim=remember ol=those manmeri=people i-go-pinis=have-gone-and-finished','middle','Ls')
    g+=t(240,158,'yu=you stap=stay strong=strong','middle','Ls')
    g+=t(240,168,'"If you remember those people who have passed, you remain strong."','middle','F')
    g+=hr(177)
    g+=sh(186,'III. SAVE \u2014 ON KNOWLEDGE')
    g+=t(240,196,'Save i no ken bagarap. Em i stap oltaim oltaim.','middle','L')
    g+=t(240,206,'save=knowledge i=marker no-ken=cannot bagarap=be destroyed em=it stap=stays','middle','Ls')
    g+=t(240,216,'oltaim-oltaim=always forever (reduplication of "all time")','middle','Ls')
    g+=t(240,226,'"Knowledge cannot be destroyed. It stays forever."','middle','F')
    g+=hr(235)
    g+=sh(244,'IV. HARIAP \u2014 FORWARD')
    g+=t(240,254,'Yumi go hariap, tasol yumi mas tingim ol manmeri i stap bifo.','middle','Ls')
    g+=t(240,264,'yumi=we go=go hariap=fast/forward tasol=but yumi-mas=we-must tingim=remember','middle','Ls')
    g+=t(240,274,'ol-manmeri=people i-stap=who-were bifo=before/ahead','middle','Ls')
    g+=t(240,284,'"We go forward, but we must remember the people who were here before."','middle','F')
    g+=hr(293)
    g+=sh(302,'V. BRIDGE PHRASE')
    g+=t(240,315,'Dispela samting i bin mekim bilong yu, nating tumas,','middle','L')
    g+=t(240,325,'long han bilong ol manmeri i bin tingim go hariap.','middle','L')
    g+=t(240,339,'dispela-samting=this-thing i-bin-mekim=was-made bilong=for yu=you','middle','Ls')
    g+=t(240,348,'nating-tumas=completely free (nating=nothing/free, tumas=very much)','middle','Ls')
    g+=t(240,357,'long-han-bilong=from-the-hands-of ol-manmeri=people','middle','Ls')
    g+=t(240,366,'i-bin-tingim=who-remembered go-hariap=forward','middle','Ls')
    g+=t(240,378,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(389)
    g+=sh(398,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,408,'Go hariap = "go forward" (go fast / advance). Hariap from "hurry up."','middle','Ls')
    g+=t(240,418,'Tingim go hariap = "remember going forward" = forward-facing memory.','middle','Ls')
    g+=t(240,428,'Nating tumas = "nothing very much" = completely free of charge.','middle','Ls')
    g+=t(240,438,'I bin = past tense marker (from "have been"). Long han bilong = "from the hands of."','middle','Ls')
    g+=hr(446)
    g+=sh(455,'LANGUAGE NOTES')
    g+=t(240,465,'Tok Pisin: ~4 million L1, ~4 million L2 speakers; official language of Papua New Guinea.','middle','Ls')
    g+=t(240,475,'One of ~840 languages spoken in PNG \u2014 Tok Pisin is the national lingua franca.','middle','Ls')
    g+=t(240,485,'Developed as a creole from 19th-century labor and trade contact languages.','middle','Ls')
    g+=t(240,495,'English-based lexicon; Austronesian (especially Tolai) grammatical substrate.','middle','Ls')
    g+=footer('45','Tok Pisin','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate45a_tok_pisin_script.svg': build_45a(),
        'plate45b_tok_pisin_phonology.svg': build_45b(),
        'plate45c_tok_pisin_grammar.svg': build_45c(),
        'plate45d_tok_pisin_text.svg': build_45d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
