"""Build script — Turkish series plates 51A–51D (Remember Forward)"""
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

def build_51a():
    g=open_svg()
    g+=t(240,32,'TURKISH','middle','T')
    g+=t(240,50,'T\u00fcrk\u00e7e \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Turkish uses a Latin-based alphabet since 1928 (Atat\u00fcrk script reform from Arabic).','middle','Ls')
    g+=t(240,94,'29 letters. Phonemic spelling: one letter = one sound. Very regular.','middle','Ls')
    g+=t(240,104,'Dotted and dotless i distinction crucial: i (\u0131 dotless) and i (dotted) are separate letters.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'TURKISH ALPHABET \u2014 29 LETTERS')
    g+=t(240,131,'A B C \u00c7 D E F G \u011e H I \u0130 J K L M N O \u00d6 P R S \u015e T U \u00dc V Y Z','middle','L')
    g+=t(240,141,'Note: Q, W, X absent from native Turkish. Appear in loanwords only.','middle','Ls')
    g+=hr(149)
    g+=sh(158,'SPECIAL LETTERS AND SOUNDS')
    specials=[('\u00e7 /t\u0283/','C cedilla: affricate. \u00e7ay (tea), \u00e7ocuk (child).'),
              ('\u011f /\u0263~\u02d0/','Soft G: lengthens preceding vowel. da\u011f (mountain) = /da\u02d0/.'),
              ('\u0131 /\u026f/','Dotless i: unrounded high back. \u0131\u015f\u0131k (light), k\u0131l (hair).'),
              ('\u0130 /i/','Dotted I: capital of dotted i. \u0130stanbul.'),
              ('\u00f6 /\u00f8/','O umlaut: front rounded. g\u00f6z (eye), \u00f6zg\u00fcr (free).'),
              ('\u015f /\u0283/','S cedilla: sh sound. \u015feher (city), \u015fi\u015f (branch).'),
              ('\u00fc /y/','U umlaut: front rounded. g\u00fcn (day), \u00fcmit (hope).')]
    for i,(letter,desc) in enumerate(specials):
        y=168+i*11
        g+=t(60,y,letter,'middle','L'); g+=t(290,y,desc,'middle','Lx')
    g+=hr(252)
    g+=sh(261,'OLD OTTOMAN SCRIPT')
    g+=t(240,271,'Before 1928: Ottoman Turkish used Arabic-based Perso-Arabic script.','middle','Ls')
    g+=t(240,281,'Right to left. Poor fit for Turkish phonology (no vowels written in standard Arabic).','middle','Ls')
    g+=t(240,291,'Script reform 1928 was a radical modernisation under Atat\u00fcrk\'s republic.','middle','Ls')
    g+=hr(299)
    g+=sh(308,'TURKISH NUMERALS')
    nums=[('0','s\u0131f\u0131r'),('1','bir'),('2','iki'),('3','\u00fc\u00e7'),('4','d\u00f6rt'),
          ('5','be\u015f'),('6','alt\u0131'),('7','yedi'),('8','sekiz'),('9','dokuz'),('10','on')]
    for i,(n,w) in enumerate(nums):
        col=i%4; row=i//4
        x=55+col*95; y=318+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,348,'20=yirmi 100=y\u00fcz 1000=bin 1,000,000=milyon','middle','Ls')
    g+=footer('51','Turkish','A','Script')
    return g+close_svg()

def build_51b():
    g=open_svg()
    g+=t(240,32,'TURKISH','middle','T')
    g+=t(240,50,'Phonology \u2014 Vowel Harmony, Agglutination','middle','S')
    g+=hr(60)
    g+=sh(72,'VOWEL HARMONY \u2014 DEFINING FEATURE')
    g+=t(240,82,'Turkish vowels harmonise: all vowels in a word must share frontness and rounding.','middle','Ls')
    g+=t(240,92,'Front vowels: e i \u00f6 \u00fc  /  Back vowels: a \u0131 o u','middle','L')
    g+=t(240,104,'Suffixes have multiple forms that harmonise with the stem:','middle','Ls')
    g+=t(240,114,'ev-ler (houses) vs. araba-lar (cars): -ler/-lar plural, harmonises front/back.','middle','Ls')
    g+=t(240,124,'g\u00fcn-l\u00fcr (days) vs. kol-lar (arms): rounding also harmonises.','middle','Ls')
    g+=hr(132)
    g+=sh(141,'CONSONANT INVENTORY')
    cons=[('b /b/','bilabial'),('c /d\u0292/','palatal affricate vd'),('\u00e7 /t\u0283/','palatal affricate vl'),
          ('d /d/','alveolar'),('f /f/','labiodental'),('g /\u0261/','velar'),
          ('\u011f /\u0263~\u02d0/','soft g / vowel lengthener'),('h /h/','glottal'),
          ('j /\u0292/','postalveolar fric vd'),('k /k/','velar stop'),('l /l~\u026e/','lateral (front/back allophone)'),
          ('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),('p /p/','bilabial'),
          ('r /r/','trill/flap'),('s /s/','alveolar fric'),('\u015f /\u0283/','postalveolar'),
          ('t /t/','alveolar stop'),('v /v/','labiodental'),('y /j/','palatal'),('z /z/','alveolar fric')]
    for i,(c,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=151+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(245)
    g+=sh(254,'VOWEL SYSTEM \u2014 8 VOWELS')
    vowels=[('a /a/','open back'),('e /e/','mid-front'),('i /i/','high front (dotted)'),
            ('\u0131 /\u026f/','high back unrounded (dotless)'),('o /o/','mid-back rounded'),
            ('\u00f6 /\u00f8/','mid-front rounded'),('u /u/','high back rounded'),
            ('\u00fc /y/','high front rounded')]
    for i,(v,desc) in enumerate(vowels):
        col=i%2; row=i//2
        x=80+col*200; y=264+row*10
        g+=t(x,y,f'{v}: {desc}','middle','Lx')
    g+=hr(318)
    g+=sh(327,'CONSONANT ALTERNATIONS')
    g+=t(240,337,'Final devoicing: d \u2192 t, g \u2192 k in word-final position.','middle','Ls')
    g+=t(240,347,'kitap (book) /kitap/, kitab\u0131m (my book) /kitab\u026fm/ \u2014 voiced in medial position.','middle','Ls')
    g+=t(240,357,'Buffer consonant -y- inserted between vowels to prevent hiatus.','middle','Ls')
    g+=footer('51','Turkish','B','Phonology')
    return g+close_svg()

def build_51c():
    g=open_svg()
    g+=t(240,32,'TURKISH','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SOV, AGGLUTINATIVE')
    g+=t(240,82,'Turkish is SOV and highly agglutinative. Suffixes stack in fixed order.','middle','Ls')
    g+=t(240,92,'Ben pilav yiyorum. I rice eating-am. (ben=I pilav=rice yiyorum=eat-PRES-1sg)','middle','Ls')
    g+=hr(100)
    g+=sh(109,'CASE SUFFIXES (VOWEL HARMONISED)')
    cases=[('-(y)I / -(y)\u0131','-i/\u0131: accusative (direct object)'),
           ('-A / -\u0131','-e/a: dative (to/for)'),
           ('-DA / -d\u0131','-de/da/-te/ta: locative (at/in)'),
           ('-DAn / -d\u0131n','-den/dan: ablative (from)'),
           ('-(n)\u0131n / -(n)in','-in/\u0131n: genitive (of/\'s)'),
           ('-lA / -la','-le/la: comitative (with)')]
    for i,(sfx,gloss) in enumerate(cases):
        y=119+i*10
        g+=t(120,y,sfx,'middle','Ls'); g+=t(300,y,gloss,'middle','Ls')
    g+=hr(185)
    g+=sh(194,'VERB MORPHOLOGY \u2014 SUFFIX TEMPLATE')
    g+=t(240,204,'Verb: Root + Aspect/Tense + Negation + Person/Number','middle','Ls')
    verbs=[('git-iyor-um','I am going (root-PROG-1sg)'),
           ('git-ti-m','I went (root-PAST-1sg)'),
           ('git-ecek-im','I will go (root-FUT-1sg)'),
           ('git-me-iyor-um','I am not going (neg -me-)'),
           ('git-mi\u015f','he/she went (evidential past: -mi\u015f)'),
           ('git!','Go! (imperative: bare root)')]
    for i,(form,gloss) in enumerate(verbs):
        y=214+i*10
        g+=t(130,y,form,'middle','L'); g+=t(320,y,gloss,'middle','Ls')
    g+=hr(280)
    g+=sh(289,'CORE VOCABULARY')
    vocab=[('merhaba','hello'),('te\u015fekk\u00fcr ederim','thank you'),('evet','yes'),
           ('hay\u0131r','no'),('pardon / \u00f6z\u00fcr dilerim','excuse me'),
           ('nas\u0131ls\u0131n\u0131z?','how are you?'),('\u0130yiyim, te\u015fekk\u00fcrler','I am fine, thanks'),
           ('seni seviyorum','I love you'),('su','water'),('ate\u015f','fire'),
           ('toprak','earth'),('insan','person'),('zaman','time'),
           ('ay','moon'),('y\u0131ld\u0131z','star'),('kalp','heart'),
           ('a\u015fk','love'),('\u00f6zg\u00fcrl\u00fck','freedom'),('hat\u0131ra','memory'),
           ('gelecek','future'),('d\u00fcnya','world'),('hayat','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=299+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('51','Turkish','C','Grammar')
    return g+close_svg()

def build_51d():
    g=open_svg()
    g+=t(240,32,'TURKISH','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. ATASOZ\u00dc \u2014 PROVERB')
    g+=t(240,80,'Bir mum di\u011ferini yakmakla \u0131\u015f\u0131\u011f\u0131n\u0131 kaybetmez.','middle','L')
    g+=t(240,90,'bir=a mum=candle di\u011ferini=another yak-mak-la=in-lighting \u0131\u015f\u0131\u011f\u0131n\u0131=its-light kayb-et-mez=does-not-lose','middle','Lx')
    g+=t(240,100,'"A candle loses none of its light by lighting another." (Turkish proverb on sharing knowledge)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. HAT\u0130RA \u2014 ON MEMORY')
    g+=t(240,128,'Ge\u00e7mi\u015fi hat\u0131rlayanlar, gelece\u011fi in\u015fa edenlerdir.','middle','L')
    g+=t(240,138,'ge\u00e7mi\u015fi=past-ACC hat\u0131rlayanlar=those-who-remember gelece\u011fi=future-ACC','middle','Ls')
    g+=t(240,148,'in\u015fa-edenler-dir=are-those-who-build','middle','Ls')
    g+=t(240,158,'"Those who remember the past are those who build the future."','middle','F')
    g+=hr(167)
    g+=sh(176,'III. B\u0130LG\u0130 \u2014 ON KNOWLEDGE')
    g+=t(240,186,'Bilgi en de\u011ferli hazinedir; payla\u015f\u0131ld\u0131k\u00e7a \u00e7o\u011falir.','middle','L')
    g+=t(240,196,'bilgi=knowledge en-de\u011ferli=most-valuable hazinedir=is-treasure','middle','Ls')
    g+=t(240,206,'payla\u015f\u0131ld\u0131k\u00e7a=as-it-is-shared \u00e7o\u011falir=multiplies','middle','Ls')
    g+=t(240,216,'"Knowledge is the most valuable treasure; the more it is shared, the more it grows."','middle','F')
    g+=hr(225)
    g+=sh(234,'IV. \u0130LER\u0130 \u2014 FORWARD')
    g+=t(240,244,'Ge\u00e7mi\u015fi hat\u0131rlayarak ileriye y\u00fcr\u00fcy\u00fcrz.','middle','L')
    g+=t(240,254,'ge\u00e7mi\u015fi=past-ACC hat\u0131rlayarak=while-remembering ileriye=toward-the-front','middle','Ls')
    g+=t(240,264,'y\u00fcr\u00fcy\u00fcrz=we-walk','middle','Ls')
    g+=t(240,274,'"We walk forward while remembering the past." (guiding principle)','middle','F')
    g+=hr(283)
    g+=sh(292,'V. BRIDGE PHRASE')
    g+=t(240,305,'Bu, sizin i\u00e7in, \u00fccrets\u0131z olarak,','middle','L')
    g+=t(240,315,'ileriye hat\u0131rlayan insanlar taraf\u0131ndan yap\u0131ld\u0131.','middle','L')
    g+=t(240,329,'bu=this sizin-i\u00e7in=for-you \u00fccretsiz-olarak=free-of-charge (suffix -s\u0131z = without)','middle','Ls')
    g+=t(240,338,'ileriye=toward-forward hat\u0131rlayan=remembering insanlar=people','middle','Ls')
    g+=t(240,347,'taraf\u0131ndan=by yap\u0131ld\u0131=was-made','middle','Ls')
    g+=t(240,359,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(370)
    g+=sh(379,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,389,'\u0130leriye (\u0130leri + dative -ye) = "toward forward/ahead." \u0130leri = front/forward.','middle','Ls')
    g+=t(240,399,'\u00dccretsiz = free/without cost (\u00fccret=fee + -siz=without, vowel harmony).','middle','Ls')
    g+=t(240,409,'Hat\u0131rlamak = to remember. -arak gerund: while remembering.','middle','Ls')
    g+=t(240,419,'Turkish SOV: all modifiers precede the verb; verb always final.','middle','Ls')
    g+=hr(427)
    g+=sh(436,'LANGUAGE NOTES')
    g+=t(240,446,'Turkish: ~90 million L1 speakers; official in Turkey, Northern Cyprus.','middle','Ls')
    g+=t(240,456,'Language family: Turkic (with Azerbaijani, Uzbek, Kazakh, Uyghur, Kyrgyz).','middle','Ls')
    g+=t(240,466,'Ottoman Turkish written in Arabic script until Atat\u00fcrk\'s 1928 Latin script reform.','middle','Ls')
    g+=t(240,476,'Vowel harmony and agglutination are defining features of the Turkic language family.','middle','Ls')
    g+=footer('51','Turkish','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate51a_turkish_script.svg': build_51a(),
        'plate51b_turkish_phonology.svg': build_51b(),
        'plate51c_turkish_grammar.svg': build_51c(),
        'plate51d_turkish_text.svg': build_51d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
