"""Build script — Korean series plates 50A–50D (Remember Forward)"""
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
            '.Lk{font-size:11px;}\n'
            '.Lks{font-size:8px;}\n'
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

def build_50a():
    g=open_svg()
    g+=t(240,32,'KOREAN','middle','T')
    g+=t(240,50,'\ud55c\uad6d\uc5b4 \u2014 Script: Hangeul (\ud55c\uae00)','middle','S')
    g+=hr(60)
    g+=sh(72,'HANGEUL \u2014 THE KOREAN ALPHABET')
    g+=t(240,84,'Hangeul created 1443 CE by King Sejong. One of the few scripts with a known author.','middle','Ls')
    g+=t(240,94,'Featural alphabet: letter shapes encode phonetic features (place/manner of articulation).','middle','Ls')
    g+=t(240,104,'Letters combined into syllable blocks. Each block = one syllable.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'CONSONANTS (JAMO) \u2014 19 LETTERS')
    cons=[('\u3131','g/k /k\u02b0~\u0261/'),('\u3132','kk /k*/ tense'),('\u3134','n /n/'),
          ('\u3137','d/t /t\u02b0~d/'),('\u3138','tt /t*/ tense'),('\u3139','r/l /r~l/'),
          ('\u3141','m /m/'),('\u3142','b/p /p\u02b0~b/'),('\u3143','pp /p*/ tense'),
          ('\u3145','s /s/'),('\u3146','ss /s*/ tense'),('\u3147','\u0294/\u014b'),
          ('\u3148','j /t\u0255\u02b0/'),('\u3149','jj /t\u0255*/ tense'),('\u314a','ch /t\u0255\u02b0\u02b0/'),
          ('\u314b','kh /k\u02b0\u02b0/'),('\u314c','th /t\u02b0\u02b0/'),('\u314d','ph /p\u02b0\u02b0/'),
          ('\u314e','h /h/')]
    for i,(jamo,desc) in enumerate(cons):
        col=i%4; row=i//4
        x=50+col*98; y=131+row*12
        g+=t(x,y,jamo,'middle','Lk'); g+=t(x,y+9,desc,'middle','Lx')
    g+=hr(203)
    g+=sh(212,'VOWELS (JAMO) \u2014 21 LETTERS')
    vowels=[('\u314f','/a/'),('\u3150','/\u00e6/'),('\u3151','/\u028c/'),('\u3152','/\u025b/'),
            ('\u3153','/\u0259/'),('\u3154','/e/'),('\u3155','/je/'),('\u3156','/jo/'),
            ('\u3157','/o/'),('\u3158','/wa/'),('\u3159','/w\u00e6/'),('\u315a','/we/'),
            ('\u315b','/jo/'),('\u315c','/u/'),('\u315d','/w\u0259/'),('\u315e','/we/'),
            ('\u315f','/wi/'),('\u3160','/ju/'),('\u3161','/\u026f/'),('\u3162','/\u026fi/'),('\u3163','/i/')]
    for i,(jamo,ipa) in enumerate(vowels):
        col=i%7; row=i//7
        x=35+col*62; y=222+row*12
        g+=t(x,y,jamo,'middle','Lk'); g+=t(x,y+9,ipa,'middle','Lx')
    g+=hr(265)
    g+=sh(274,'SYLLABLE BLOCK STRUCTURE')
    g+=t(240,284,'Syllables assembled in blocks: Initial consonant (onset) + vowel + optional final consonant (coda).','middle','Ls')
    g+=t(240,294,'Example: \ud55c = \u314e + \u3161 + \u3134 (h + eu + n = han). \uae00 = \u3131 + \u3173 + \u3139 (g + eu + l = geul).','middle','Ls')
    g+=t(240,304,'Vowels written below horizontal consonants, right of vertical consonants.','middle','Ls')
    g+=hr(312)
    g+=sh(321,'KOREAN NUMERALS \u2014 TWO SYSTEMS')
    g+=t(240,331,'Korean has Sino-Korean (Chinese-based) and Native Korean number systems:','middle','Ls')
    g+=t(240,341,'Sino: \uc77c(\u4e00) \uc774(\u4e8c) \uc0bc(\u4e09) \uc0ac(\u56db) \uc624(\u4e94) \uc721(\u516d) \uce60(\u4e03) \ud314(\u516b) \uad6c(\u4e5d) \uc2ed(\u5341)','middle','Lk')
    g+=t(240,354,'Native: \ud558\ub098 \ub458 \uc14b \ub137 \ub2e4\uc12f \uc5ec\uc12f \uc77c\uacf1 \uc5ec\ub35f \uc544\ud649 \uc5f4','middle','Lk')
    g+=t(240,367,'Sino used for dates, money, addresses; Native for counting objects, age (older style).','middle','Ls')
    g+=footer('50','Korean','A','Script')
    return g+close_svg()

def build_50b():
    g=open_svg()
    g+=t(240,32,'KOREAN','middle','T')
    g+=t(240,50,'Phonology \u2014 Three-Way Consonant Contrast','middle','S')
    g+=hr(60)
    g+=sh(72,'THREE-WAY STOP CONTRAST')
    g+=t(240,82,'Korean has a unique 3-way contrast for stops and affricates:','middle','Ls')
    g+=t(240,92,'LENIS (plain): aspirated in onset, voiced between vowels: \u3131 /k\u02b0~\u0261/, \u3137 /t\u02b0~d/, \u3142 /p\u02b0~b/','middle','Ls')
    g+=t(240,102,'ASPIRATED: heavily aspirated: \u314b /k\u02b0\u02b0/, \u314c /t\u02b0\u02b0/, \u314d /p\u02b0\u02b0/','middle','Ls')
    g+=t(240,112,'TENSE (fortis): glottalised, no aspiration: \u3132 /k*/, \u3138 /t*/, \u3143 /p*/','middle','Ls')
    g+=t(240,122,'Example: \ubc14 /pa\u02b0/ (leg) vs. \ud30c /p\u02b0\u02b0a/ (spring) vs. \ube60 /p*a/ (fast).','middle','Ls')
    g+=hr(130)
    g+=sh(139,'CONSONANT INVENTORY')
    cons=[('\u3131 /k\u02b0/','lenis velar'),('\u3132 /k*/','tense velar'),('\u314b /k\u02b0\u02b0/','aspirated velar'),
          ('\u3137 /t\u02b0/','lenis alveolar'),('\u3138 /t*/','tense alveolar'),('\u314c /t\u02b0\u02b0/','aspirated alveolar'),
          ('\u3142 /p\u02b0/','lenis bilabial'),('\u3143 /p*/','tense bilabial'),('\u314d /p\u02b0\u02b0/','aspirated bilabial'),
          ('\u3148 /t\u0255\u02b0/','lenis palatal'),('\u3149 /t\u0255*/','tense palatal'),('\u314a /t\u0255\u02b0\u02b0/','aspirated palatal'),
          ('\u3145 /s/','lenis sibilant'),('\u3146 /s*/','tense sibilant'),('\u314e /h/','glottal'),
          ('\u3134 /n/','alveolar nasal'),('\u3141 /m/','bilabial nasal'),('\u3147 /\u014b/','velar nasal (final)'),
          ('\u3139 /r~l/','flap/lateral')]
    for i,(c,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=149+row*10
        g+=t(x-5,y,c,'middle','Lks'); g+=t(x+30,y,desc,'middle','Lx')
    g+=hr(225)
    g+=sh(234,'VOWEL SYSTEM \u2014 10 BASIC VOWELS')
    vowels=[('/a/','open front'),('/\u00e6/','near-open front'),('/\u0259/','mid central schwa'),
            ('/e/','mid-front'),('/i/','high front'),('/o/','mid-back rounded'),
            ('/u/','high back'),('/\u028c/','mid-back unrounded'),('/\u026f/','high central'),
            ('/\u026fi/','high central + front glide')]
    for i,(v,desc) in enumerate(vowels):
        col=i%2; row=i//2
        x=80+col*200; y=244+row*10
        g+=t(x,y,f'{v}: {desc}','middle','Lx')
    g+=hr(305)
    g+=sh(314,'PHONOLOGICAL PROCESSES')
    g+=t(240,324,'Final consonant neutralisation: 7 allowed finals: -p, -t, -k, -m, -n, -ng, -l.','middle','Ls')
    g+=t(240,334,'Nasalisation: k before n \u2192 ng: \u3131+\u3134 \u2192 ng+n (Korean phonology).','middle','Ls')
    g+=t(240,344,'Tensing: consonant after lenis coda may become tense.','middle','Ls')
    g+=t(240,354,'Aspirate liaison: h + lenis \u2192 aspirated (bidirectional).','middle','Ls')
    g+=footer('50','Korean','B','Phonology')
    return g+close_svg()

def build_50c():
    g=open_svg()
    g+=t(240,32,'KOREAN','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SOV, AGGLUTINATIVE')
    g+=t(240,82,'Korean is SOV. Particles follow nouns; verb always final. Very regular agglutination.','middle','Ls')
    g+=t(240,92,'\ub098\ub294 \ubc25\uc744 \uba39\ub294\ub2e4. I rice eat. (na=I neun=TOP bap=rice eul=OBJ meoknunda=eat)','middle','Ls')
    g+=hr(100)
    g+=sh(109,'CASE PARTICLES')
    particles=[('\uc740/\ub294','-eun/-neun: topic marker'),
               ('\uc774/\uac00','-i/-ga: subject marker'),
               ('\uc744/\ub97c','-eul/-reul: object marker'),
               ('\uc5d0','-e: locative/time marker'),
               ('\uc5d0\uc11c','-eseo: from/at (action)'),
               ('\uc5d0\uac8c','-ege: to (person)'),
               ('\uc73c\ub85c/\ub85c','-euro/-ro: direction/means'),
               ('\uc640/\uacfc','-wa/-gwa: and/with')]
    for i,(p,gloss) in enumerate(particles):
        col=i%2; row=i//2
        x=80+col*200; y=119+row*10
        g+=t(x,y,f'{p} {gloss}','middle','Lx')
    g+=hr(203)
    g+=sh(212,'HONORIFIC SYSTEM')
    g+=t(240,222,'Korean has elaborate speech levels encoding social relationship:','middle','Ls')
    levels=[('\ud574\uc694\uccb4','Haeyoche: polite informal (\uba39\uc5b4\uc694 = eat [polite])'),
            ('\ud569\uc1fc\uccb4','Hapssoche: formal polite (\uba39\uc2b5\ub2c8\ub2e4 = eat [formal])'),
            ('\ud574\uccb4','Haeyche: informal casual (\uba39\uc5b4 = eat [casual to close friend])'),
            ('\ud574\ub77c\uccb4','Haerache: plain (\uba39\ub294\ub2e4 = eat [written/narrative])')]
    for i,(level,desc) in enumerate(levels):
        y=232+i*11
        g+=t(100,y,level,'middle','Ls'); g+=t(300,y,desc,'middle','Lx')
    g+=hr(285)
    g+=sh(294,'CORE VOCABULARY')
    vocab=[('\uc548\ub155\ud558\uc138\uc694','hello'),('\uac10\uc0ac\ud569\ub2c8\ub2e4','thank you'),
           ('\ub124','yes'),('\uc544\ub2c8\uc694','no'),('\uc8c4\uc1a1\ud569\ub2c8\ub2e4','I\'m sorry'),
           ('\uc5b4\ub5bb\uac8c \uc9c0\ub0b4\uc138\uc694?','how are you?'),
           ('\uc798 \uc9c0\ub0b4\uc694','I\'m fine'),('\uc0ac\ub791\ud574\uc694','I love you'),
           ('\ubb3c','water'),('\ubd88','fire'),('\ub545','earth/ground'),
           ('\uc0ac\ub78c','person'),('\uc2dc\uac04','time'),('\ub2ec','moon'),
           ('\ubcc4','star'),('\ub9c8\uc74c','heart/mind'),('\uc0ac\ub791','love'),
           ('\uc790\uc720','freedom'),('\uae30\uc5b5','memory'),
           ('\ubbf8\ub798','future'),('\uc138\uc0c1','world'),('\uc0dd\uba85','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<11 else 1
        y=304+(i if i<11 else i-11)*10
        g+=t(50+col*235,y,w,'middle','Lks'); g+=t(185+col*235,y,e,'middle','Lx')
    g+=footer('50','Korean','C','Grammar')
    return g+close_svg()

def build_50d():
    g=open_svg()
    g+=t(240,32,'KOREAN','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. SOKDAM \u2014 PROVERB')
    g+=t(240,80,'\uc2dc\uc791\uc774 \ubc18\uc774\ub2e4.','middle','Lk')
    g+=t(240,94,'siJak-i = the beginning ban = half ida = is','middle','Ls')
    g+=t(240,104,'"Beginning is half." (Korean proverb: well begun is half done)','middle','F')
    g+=hr(113)
    g+=sh(122,'II. GIEOK \u2014 ON MEMORY')
    g+=t(240,132,'\uacfc\uac70\ub97c \uae30\uc5b5\ud558\ub294 \uc790\uac00 \ubbf8\ub798\ub97c \ub9cc\ub4e0\ub2e4.','middle','Lk')
    g+=t(240,146,'gwageo-reul = past-OBJ gieokha-neun = who-remembers ja = person','middle','Ls')
    g+=t(240,155,'mirae-reul = future-OBJ mandeunda = makes/builds','middle','Ls')
    g+=t(240,165,'"The person who remembers the past builds the future."','middle','F')
    g+=hr(174)
    g+=sh(183,'III. JISIK \u2014 ON KNOWLEDGE')
    g+=t(240,193,'\uae00\uc740 \uc0ac\ub77c\uc9c0\uc9c0 \uc54a\ub294\ub2e4.','middle','Lk')
    g+=t(240,207,'Geur-eun = writing salaJiji = disappears/perish anneunda = does-not','middle','Ls')
    g+=t(240,217,'"Writing does not disappear." (Korean saying on the permanence of recorded knowledge)','middle','F')
    g+=hr(226)
    g+=sh(235,'IV. APURO \u2014 FORWARD')
    g+=t(240,245,'\uc6b0\ub9ac\ub294 \uc55e\uc73c\ub85c \ub098\uc544\uac00\uba74\uc11c \uacfc\uac70\ub97c \uae30\uc5b5\ud55c\ub2e4.','middle','Lk')
    g+=t(240,259,'uri-neun = we ap-euro = forward (toward-front) naagamyeonseo = while-going','middle','Ls')
    g+=t(240,268,'gwageo-reul = past gieokhan-da = remember','middle','Ls')
    g+=t(240,278,'"We go forward while remembering the past." (guiding principle)','middle','F')
    g+=hr(287)
    g+=sh(296,'V. BRIDGE PHRASE')
    g+=t(240,308,'\uc774\uac83\uc740 \ub2f9\uc2e0\uc744 \uc704\ud574, \ub3c8\uc5c6\uc774,','middle','Lk')
    g+=t(240,322,'\uc55e\uc73c\ub85c \uae30\uc5b5\ud55c \uc0ac\ub78c\ub4e4\uc774 \ub9cc\ub4e4\uc5c8\uc2b5\ub2c8\ub2e4.','middle','Lk')
    g+=t(240,338,'igeot-eun = this dangsineul = you(formal)-OBJ wihaeseo = for don-eopssi = without-money','middle','Ls')
    g+=t(240,347,'ap-euro = forward gieokhan = who-remembered saram-deul-i = people-SUB','middle','Ls')
    g+=t(240,356,'mandeur-eoss-seumnida = made (formal polite past)','middle','Ls')
    g+=t(240,368,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(379)
    g+=sh(388,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,398,'\uc55e\uc73c\ub85c (ap-euro) = "toward the front/future." In Korean, the future is "in front" (ap).','middle','Ls')
    g+=t(240,408,'\uae30\uc5b5\ud558\ub2e4 (gieokha-da) = "to remember." \ub3c8\uc5c6\uc774 (don-eopssi) = "without money" = free.','middle','Ls')
    g+=t(240,418,'Formal speech level (-seumnida) used as this is a message of respect across time.','middle','Ls')
    g+=hr(426)
    g+=sh(435,'LANGUAGE NOTES')
    g+=t(240,445,'Korean: ~80 million speakers worldwide (South Korea, North Korea, diaspora).','middle','Ls')
    g+=t(240,455,'Language family: Koreanic (language isolate; only distant Japonic relation debated).','middle','Ls')
    g+=t(240,465,'Hangeul created 1443 CE; one of the most phonologically systematic scripts ever devised.','middle','Ls')
    g+=t(240,475,'Significant Chinese loanword layer (Sino-Korean ~60% of vocabulary).','middle','Ls')
    g+=footer('50','Korean','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate50a_korean_script.svg': build_50a(),
        'plate50b_korean_phonology.svg': build_50b(),
        'plate50c_korean_grammar.svg': build_50c(),
        'plate50d_korean_text.svg': build_50d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
