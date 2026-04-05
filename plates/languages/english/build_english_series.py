"""Build script — English series plates 48A–48D (Remember Forward)"""
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

def build_48a():
    g=open_svg()
    g+=t(240,32,'ENGLISH','middle','T')
    g+=t(240,50,'Script \u2014 Latin Alphabet & Orthography','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'English uses the Latin alphabet (26 letters). No diacritics in native words.','middle','Ls')
    g+=t(240,94,'Orthography is highly irregular: historical spellings preserved despite sound changes.','middle','Ls')
    g+=t(240,104,'"though" /\u00f0o\u028a/, "through" /\u03b8ru\u02d0/, "cough" /k\u0254f/, "rough" /r\u028cf/ \u2014 same -ough, 4 sounds.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'ALPHABET')
    g+=t(240,131,'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z','middle','L')
    g+=t(240,141,'Upper and lower case. Pronounced very differently from Latin or Spanish values.','middle','Ls')
    g+=hr(149)
    g+=sh(158,'SPELLING IRREGULARITIES \u2014 KEY PATTERNS')
    irr=[('silent letters','"knight" /na\u026at/, "write" /ra\u026at/, "gnome" /no\u028am/'),
         ('-tion suffix','/\u0283\u0259n/: "nation", "station", "fiction"'),
         ('c = /k/ or /s/','"cat" /k\u00e6t/ vs "cent" /s\u025bnt/ (before e/i/y)'),
         ('gh = /f/ or silent','"rough" /r\u028cf/, "night" /na\u026at/ (no sound)'),
         ('ea = multiple sounds','"bread" /\u025b/, "bead" /i\u02d0/, "great" /e\u026a/'),
         ('-ed past tense','/t/ "walked", /d/ "lived", /\u026ad/ "wanted"'),
         ('double consonants','often signal short vowel: "bitter" vs "biter"')]
    for i,(pattern,ex) in enumerate(irr):
        y=168+i*11
        g+=t(100,y,pattern,'middle','Ls'); g+=t(310,y,ex,'middle','Lx')
    g+=hr(253)
    g+=sh(262,'IPA FOR ENGLISH \u2014 RECEIVED PRONUNCIATION')
    g+=t(240,272,'English has ~44 phonemes (RP) but only 26 letters. IPA bridging essential.','middle','Ls')
    g+=t(240,282,'Vowels: /i\u02d0 \u026a e \u00e6 \u0251\u02d0 \u0254\u02d0 \u028a u\u02d0 \u028c \u0259 \u025c\u02d0 e\u026a \u0259\u028a a\u026a \u0254\u026a \u026a\u0259 e\u0259 \u028a\u0259/','middle','Ls')
    g+=t(240,292,'Consonants: /p b t d k \u0261 t\u0283 d\u0292 f v \u03b8 \u00f0 s z \u0283 \u0292 m n \u014b l r w j h/','middle','Ls')
    g+=hr(300)
    g+=sh(309,'SCRIPT HISTORY')
    g+=t(240,319,'Old English (450-1100 CE): runic alphabet (futhorc) + Latin alphabet with thorn (\u00fe), eth (\u00f0), wynn.','middle','Ls')
    g+=t(240,329,'Middle English (1100-1500): Norman French influence; many French spellings adopted.','middle','Ls')
    g+=t(240,339,'Modern English (~1500+): printing press standardised spelling; Great Vowel Shift changed pronunciation.','middle','Ls')
    g+=t(240,349,'Result: spelling frozen in 1500s, pronunciation continued shifting \u2014 creating irregularities.','middle','Ls')
    g+=hr(357)
    g+=sh(366,'ENGLISH NUMERALS AND COUNTING')
    nums=[('1','one'),('2','two'),('3','three'),('4','four'),('5','five'),
          ('6','six'),('7','seven'),('8','eight'),('9','nine'),('10','ten'),
          ('11','eleven'),('12','twelve'),('13','thirteen'),('20','twenty'),('100','hundred')]
    for i,(n,w) in enumerate(nums):
        col=i%5; row=i//5
        x=50+col*76; y=376+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,406,'1000 = thousand · 1,000,000 = million · 1,000,000,000 = billion','middle','Ls')
    g+=footer('48','English','A','Script')
    return g+close_svg()

def build_48b():
    g=open_svg()
    g+=t(240,32,'ENGLISH','middle','T')
    g+=t(240,50,'Phonology \u2014 44 Phonemes, Stress, Intonation','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY \u2014 24 CONSONANTS')
    cons=[('p /p/','bilabial stop vl: pin'),('b /b/','bilabial stop vd: bin'),
          ('t /t/','alveolar stop vl: tin'),('d /d/','alveolar stop vd: din'),
          ('k /k/','velar stop vl: kin'),('\u0261 /\u0261/','velar stop vd: give'),
          ('t\u0283 /t\u0283/','postalveolar affricate: chin'),('d\u0292 /d\u0292/','postalveolar aff vd: gin'),
          ('f /f/','labiodental: fin'),('v /v/','labiodental vd: vine'),
          ('\u03b8 /\u03b8/','dental fricative: thin'),('\u00f0 /\u00f0/','dental fricative vd: this'),
          ('s /s/','alveolar fric: sin'),('z /z/','alveolar fric vd: zip'),
          ('\u0283 /\u0283/','postalveolar: shin'),('\u0292 /\u0292/','postalveolar vd: measure'),
          ('h /h/','glottal: hat'),('m /m/','bilabial nasal: man'),
          ('n /n/','alveolar nasal: nun'),('\u014b /\u014b/','velar nasal: sing'),
          ('l /l/','lateral: lip'),('r /r/','approximant: run'),
          ('w /w/','labio-velar: win'),('j /j/','palatal: yes')]
    for i,(c,desc) in enumerate(cons):
        col=i%2; row=i//2
        x=80+col*200; y=82+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(212)
    g+=sh(221,'VOWEL SYSTEM \u2014 20 VOWELS (RP)')
    g+=t(240,231,'English has one of the largest vowel inventories of major world languages.','middle','Ls')
    short=[('i /\u026a/','kit'),('e /e/','dress'),('\u00e6 /\u00e6/','trap'),('\u0254 /\u0254/','lot'),
           ('\u028c /\u028c/','strut'),('\u028a /\u028a/','foot'),('\u0259 /\u0259/','comma')]
    long=[('i\u02d0 /i\u02d0/','fleece'),('u\u02d0 /u\u02d0/','goose'),('\u0251\u02d0 /\u0251\u02d0/','palm'),
          ('\u0254\u02d0 /\u0254\u02d0/','thought'),('\u025c\u02d0 /\u025c\u02d0/','nurse')]
    diph=[('e\u026a /e\u026a/','face'),('\u0259\u028a /\u0259\u028a/','goat'),('a\u026a /a\u026a/','price'),
          ('\u0254\u026a /\u0254\u026a/','choice'),('a\u028a /a\u028a/','mouth'),
          ('\u026a\u0259 /\u026a\u0259/','near'),('e\u0259 /e\u0259/','square'),('\u028a\u0259 /\u028a\u0259/','cure')]
    g+=t(240,241,'Short:','middle','Lx')
    for i,(v,kw) in enumerate(short):
        x=30+i*62; g+=t(x,251,f'{v}','middle','Lx'); g+=t(x,260,kw,'middle','Lx')
    g+=t(240,271,'Long:','middle','Lx')
    for i,(v,kw) in enumerate(long):
        x=50+i*80; g+=t(x,281,f'{v}','middle','Lx'); g+=t(x,290,kw,'middle','Lx')
    g+=t(240,300,'Diphthongs:','middle','Lx')
    for i,(v,kw) in enumerate(diph):
        x=30+i*55; g+=t(x,310,f'{v}','middle','Lx'); g+=t(x,319,kw,'middle','Lx')
    g+=hr(328)
    g+=sh(337,'STRESS \u2014 PHONEMIC AND UNPREDICTABLE')
    g+=t(240,347,'English stress is unpredictable: must be learned for each word.','middle','Ls')
    g+=t(240,357,'"REcord" (noun) vs. "reCORD" (verb). "PERmit" vs. "perMIT."','middle','Ls')
    g+=t(240,367,'Unstressed vowels reduce to /\u0259/ (schwa): "the", "a", unstressed syllables.','middle','Ls')
    g+=hr(375)
    g+=sh(384,'TH-SOUNDS \u2014 UNIQUE TO ENGLISH')
    g+=t(240,394,'English /\u03b8/ and /\u00f0/ are rare cross-linguistically. Most L2 speakers replace with t/d or s/z.','middle','Ls')
    g+=t(240,404,'/\u03b8/ voiceless: think, three, both, tooth, health, cloth.','middle','Ls')
    g+=t(240,414,'/\u00f0/ voiced: this, that, the, though, breathe, father.','middle','Ls')
    g+=footer('48','English','B','Phonology')
    return g+close_svg()

def build_48c():
    g=open_svg()
    g+=t(240,32,'ENGLISH','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SVO, ANALYTIC')
    g+=t(240,82,'English is SVO and analytic (little inflection; function words carry grammar).','middle','Ls')
    g+=t(240,92,'Compared to Latin or Russian, English has minimal case endings and verb conjugations.','middle','Ls')
    g+=hr(100)
    g+=sh(109,'VERB TENSE SYSTEM')
    g+=t(240,119,'English has 12 main tenses/aspects (simple, perfect, continuous, perfect-continuous x 3 times):','middle','Ls')
    tenses=[('Simple present','I write / she writes'),('Present cont.','I am writing'),
            ('Present perfect','I have written'),('Pres. perf. cont.','I have been writing'),
            ('Simple past','I wrote'),('Past cont.','I was writing'),
            ('Past perfect','I had written'),('Past perf. cont.','I had been writing'),
            ('Simple future','I will write'),('Future cont.','I will be writing'),
            ('Future perfect','I will have written'),('Fut. perf. cont.','I will have been writing')]
    for i,(tense,ex) in enumerate(tenses):
        col=i%2; row=i//2
        x=80+col*200; y=129+row*10
        g+=t(x,y,f'{tense}: {ex}','middle','Lx')
    g+=hr(203)
    g+=sh(212,'IRREGULAR VERBS \u2014 STRONG VERBS')
    g+=t(240,222,'English has ~200 irregular verbs from Old English strong conjugation:','middle','Ls')
    irregulars=[('be','was/were','been'),('go','went','gone'),('have','had','had'),
                ('do','did','done'),('say','said','said'),('make','made','made'),
                ('come','came','come'),('see','saw','seen'),('know','knew','known'),
                ('give','gave','given'),('get','got','got/gotten'),('take','took','taken')]
    for i,(inf,past,pp) in enumerate(irregulars):
        col=i%3; row=i//3
        x=65+col*130; y=232+row*10
        g+=t(x,y,f'{inf}/{past}/{pp}','middle','Lx')
    g+=hr(290)
    g+=sh(299,'ARTICLES \u2014 DEFINITE AND INDEFINITE')
    g+=t(240,309,'"The" (definite): specific known item. "A/an" (indefinite): any one item.','middle','Ls')
    g+=t(240,319,'No articles in many languages (Mandarin, Russian, Latin, Swahili).','middle','Ls')
    g+=t(240,329,'"A/an": use "an" before vowel sounds: "an hour" (/\u02c8a\u028a\u0259r/).','middle','Ls')
    g+=hr(337)
    g+=sh(346,'CORE VOCABULARY')
    vocab=[('hello / hi','greeting'),('thank you','gratitude'),('yes','affirmation'),
           ('no','negation'),('please','polite request'),('how are you?','greeting query'),
           ('I am fine','standard reply'),('I love you','affection'),
           ('water','liquid H2O'),('fire','combustion'),('earth','soil/ground'),
           ('person','human being'),('time','duration'),('moon','Earth\'s satellite'),
           ('star','celestial body'),('heart','organ/emotion'),('love','deep affection'),
           ('freedom','liberty'),('memory','stored experience'),
           ('future','time ahead'),('world','Earth/all'),('life','being alive')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=356+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('48','English','C','Grammar')
    return g+close_svg()

def build_48d():
    g=open_svg()
    g+=t(240,32,'ENGLISH','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. PROVERB \u2014 KNOWLEDGE AND TIME')
    g+=t(240,80,'Knowledge is the one flame that grows brighter when shared.','middle','L')
    g+=t(240,90,'knowledge = that which is known, accumulated experience and understanding','middle','Ls')
    g+=t(240,100,'flame = metaphor for living transmission: unlike fire, knowledge is not diminished by sharing','middle','Lx')
    g+=t(240,110,'"Knowledge is the one flame that grows brighter when shared." (project proverb)','middle','F')
    g+=hr(119)
    g+=sh(128,'II. ON MEMORY')
    g+=t(240,138,'The dead are only truly gone when the last person who remembers them is gone.','middle','Ls')
    g+=t(240,148,'This is why we write. This is why we bury what we know.','middle','Ls')
    g+=t(240,158,'We make memory patient. We teach it to wait for the right reader.','middle','Ls')
    g+=t(240,168,'"Make memory patient. Teach it to wait." (Remember Forward, Founder\'s Letter)','middle','F')
    g+=hr(177)
    g+=sh(186,'III. ON KNOWLEDGE')
    g+=t(240,196,'In the beginning was the word. And the word was written down.','middle','L')
    g+=t(240,206,'And the writing was copied, and buried, and found again.','middle','L')
    g+=t(240,216,'And the one who found it learned what the one who wrote it knew.','middle','L')
    g+=t(240,226,'And the chain held. (project text on written knowledge)','middle','F')
    g+=hr(235)
    g+=sh(244,'IV. FORWARD')
    g+=t(240,254,'We are not the last. There will be those who come after.','middle','L')
    g+=t(240,264,'What we know, they could know. What we learned, they could learn.','middle','L')
    g+=t(240,274,'If we remember forward. (project text)','middle','F')
    g+=hr(283)
    g+=sh(292,'V. BRIDGE PHRASE')
    g+=t(240,307,'This was made for you, freely, by people who remembered forward.','middle','L')
    g+=t(240,321,'this = the plate you hold was = past tense passive','middle','Ls')
    g+=t(240,330,'made for you = created as a gift freely = without cost, no strings attached','middle','Ls')
    g+=t(240,339,'by people = by human beings who remembered forward = who directed their memory ahead','middle','Ls')
    g+=t(240,351,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(362)
    g+=sh(371,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,381,'"Forward" in English means both "ahead in space" and "ahead in time."','middle','Ls')
    g+=t(240,391,'"Remembered forward" is not standard English \u2014 it is coined by this project.','middle','Ls')
    g+=t(240,401,'It means: held the past in mind while directing one\'s attention toward the future.','middle','Ls')
    g+=t(240,411,'The phrase is the thesis of the entire project, stated in the language of its origin.','middle','Ls')
    g+=hr(419)
    g+=sh(428,'LANGUAGE NOTES')
    g+=t(240,438,'English: ~380 million L1 speakers; ~1.5 billion total speakers worldwide.','middle','Ls')
    g+=t(240,448,'Language family: Indo-European, West Germanic (with German, Dutch, Frisian).','middle','Ls')
    g+=t(240,458,'Massive lexical borrowing: Norman French, Latin, Greek, Norse, hundreds of others.','middle','Ls')
    g+=t(240,468,'Current global lingua franca for science, aviation, diplomacy, and the internet.','middle','Ls')
    g+=footer('48','English','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate48a_english_script.svg': build_48a(),
        'plate48b_english_phonology.svg': build_48b(),
        'plate48c_english_grammar.svg': build_48c(),
        'plate48d_english_text.svg': build_48d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
