"""Build script — German series plates 52A–52D (Remember Forward)"""
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

def build_52a():
    g=open_svg()
    g+=t(240,32,'GERMAN','middle','T')
    g+=t(240,50,'Deutsch \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'German uses the Latin alphabet (26 letters) plus 4 special characters: \u00e4, \u00f6, \u00fc, \u00df.','middle','Ls')
    g+=t(240,94,'Highly regular spelling; German is phonemic with few exceptions.','middle','Ls')
    g+=t(240,104,'Capital letters: ALL nouns capitalised in German. Unique among major European languages.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'SPECIAL CHARACTERS')
    specials=[('\u00e4 /\u025b/ or /\u025b\u02d0/','A-umlaut: M\u00e4dchen (girl), S\u00e4ge (saw). Alternate: ae.'),
              ('\u00f6 /\u00f8/ or /\u00f8\u02d0/','O-umlaut: \u00f6ffnen (open), K\u00f6nig (king). Alt: oe.'),
              ('\u00fc /y/ or /y\u02d0/','U-umlaut: \u00fcber (over), M\u00fcnchen. Alt: ue.'),
              ('\u00df /s\u02d0/ or /s/','Sharp S (Eszett): stra\u00dfe (street), wei\u00df (white). Alt: ss.')]
    for i,(letter,desc) in enumerate(specials):
        y=131+i*12
        g+=t(60,y,letter,'middle','L'); g+=t(290,y,desc,'middle','Lx')
    g+=hr(185)
    g+=sh(194,'GOTHIC / FRAKTUR SCRIPT')
    g+=t(240,204,'Historical German: Fraktur (Gothic/Blackletter) script used until ~1940s.','middle','Ls')
    g+=t(240,214,'Nazi Germany abolished Fraktur 1941; modern German uses Latin (Antiqua).','middle','Ls')
    g+=t(240,224,'Fraktur still seen on historic documents, decorative signs, beer labels.','middle','Ls')
    g+=hr(232)
    g+=sh(241,'KEY PRONUNCIATION RULES')
    g+=t(240,251,'CH: /x/ after back vowels (Bach, acht), /\u00e7/ after front vowels (ich, nicht).','middle','Ls')
    g+=t(240,261,'W = /v/: Wasser (water) = /vas\u0259r/. V = /f/: Vater (father) = /fa\u02d0t\u0259r/.','middle','Ls')
    g+=t(240,271,'Z = /ts/: Zeit (time) = /tsa\u026at/. J = /j/: Jahr (year) = /ja\u02d0r/.','middle','Ls')
    g+=t(240,281,'Final devoicing: Tag /ta\u02d0k/, Wald /valt/ (d\u2192t, g\u2192k at word end).','middle','Ls')
    g+=hr(289)
    g+=sh(298,'GERMAN NUMERALS')
    nums=[('0','null'),('1','ein'),('2','zwei'),('3','drei'),('4','vier'),('5','f\u00fcnf'),
          ('6','sechs'),('7','sieben'),('8','acht'),('9','neun'),('10','zehn'),
          ('20','zwanzig'),('100','hundert'),('1000','tausend')]
    for i,(n,w) in enumerate(nums):
        col=i%4; row=i//4
        x=55+col*95; y=308+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,348,'Large numbers: 1,000,000 = eine Million. Compound: siebenundzwanzig = 27 (seven-and-twenty).','middle','Ls')
    g+=footer('52','German','A','Script')
    return g+close_svg()

def build_52b():
    g=open_svg()
    g+=t(240,32,'GERMAN','middle','T')
    g+=t(240,50,'Phonology \u2014 Sounds and Key Contrasts','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    cons=[('p /p/','bilabial'),('b /b/','bilabial vd'),('t /t/','alveolar'),
          ('d /d/','alveolar vd'),('k /k/','velar'),('\u0261 /\u0261/','velar vd'),
          ('f /f/','labiodental'),('v /v/','labiodental vd'),
          ('s /s/','alveolar fric'),('z /z/','alveolar fric vd'),
          ('\u0283 /\u0283/','postalveolar'),('x /x/','velar fric (ch-back)'),
          ('\u00e7 /\u00e7/','palatal fric (ch-front)'),('h /h/','glottal'),
          ('ts /ts/','affricate (z)'),('t\u0283 /t\u0283/','affricate (sch+stop)'),
          ('pf /pf/','labial affricate (Pferd)'),('m /m/','bilabial nasal'),
          ('n /n/','alveolar nasal'),('\u014b /\u014b/','velar nasal (ng)'),
          ('l /l/','lateral'),('r /r~\u0281/','trill or uvular (regional)'),
          ('w/v /v/','=v in German'),('j /j/','palatal approx')]
    for i,(c,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=82+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(232)
    g+=sh(241,'VOWELS \u2014 SHORT, LONG, UMLAUT')
    g+=t(240,251,'German has 15+ vowel distinctions (short/long pairs + umlauts + diphthongs):','middle','Ls')
    vowels=[('a/\u0101 /a/~/a\u02d0/','Mann/Bahn'),('e/\u0113 /\u025b/~/e\u02d0/','Bett/Weg'),
            ('i/\u012b /\u026a/~/i\u02d0/','mit/ihm'),('\u00e4/\u01e3 /\u025b/~/\u025b\u02d0/','H\u00e4nde/sp\u00e4t'),
            ('o/\u014d /\u0254/~/o\u02d0/','Gott/Boot'),('\u00f6/\u01ff /\u0153/~/\u00f8\u02d0/','h\u00f6llen/sch\u00f6n'),
            ('u/\u016b /\u028a/~/u\u02d0/','Mutter/Uhr'),('\u00fc/\u01d6 /\u028f/~/y\u02d0/','m\u00fcssen/f\u00fchl'),
            ('\u0259 /\u0259/','schwa: unstressed syllables')]
    for i,(v,ex) in enumerate(vowels):
        col=i%3; row=i//3
        x=65+col*130; y=261+row*11
        g+=t(x,y,f'{v}: {ex}','middle','Lx')
    g+=hr(325)
    g+=sh(334,'DIPHTHONGS')
    g+=t(240,344,'ei/ai /a\u026a/: Eis (ice), Mai (May). eu/\u00e4u /\u0254\u028a/: neu (new), h\u00e4ufig (frequent).','middle','Ls')
    g+=t(240,354,'au /a\u028a/: Haus (house), Baum (tree).','middle','Ls')
    g+=hr(362)
    g+=sh(371,'FINAL DEVOICING AND AUSLAUTVERH\u00c4RTUNG')
    g+=t(240,381,'All obstruents devoice at word/morpheme end:','middle','Ls')
    g+=t(240,391,'Hund /hUnt/ (dog). Hundes /h\u028and\u0259s/ (dog\'s). D restored before vowel.','middle','Ls')
    g+=footer('52','German','B','Phonology')
    return g+close_svg()

def build_52c():
    g=open_svg()
    g+=t(240,32,'GERMAN','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 V2 AND SOV IN SUBORDINATE CLAUSES')
    g+=t(240,82,'Main clause: V2 (finite verb in 2nd position). Subordinate: verb final (SOV).','middle','Ls')
    g+=t(240,92,'Ich lese das Buch. / Das Buch lese ich. (V2: verb always 2nd)','middle','Ls')
    g+=t(240,102,'Ich wei\u00df, dass er das Buch liest. (subordinate: verb final)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'THREE GENDERS AND FOUR CASES')
    g+=t(240,129,'Three grammatical genders: masculine (der), feminine (die), neuter (das).','middle','Ls')
    g+=t(240,139,'Four cases: Nominative (subject), Accusative (direct object), Dative (indirect object), Genitive (of).','middle','Ls')
    g+=t(240,149,'Articles change by case: der (nom) \u2192 den (acc) \u2192 dem (dat) \u2192 des (gen).','middle','Ls')
    g+=hr(157)
    g+=sh(166,'STRONG VERBS \u2014 ABLAUT')
    verbs=[('fahren (drive)','f\u00e4hrt','fuhr','gefahren'),
           ('sehen (see)','sieht','sah','gesehen'),
           ('geben (give)','gibt','gab','gegeben'),
           ('kommen (come)','kommt','kam','gekommen'),
           ('trinken (drink)','trinkt','trank','getrunken')]
    g+=t(240,176,'Infinitive / 3sg present / simple past / past participle:','middle','Lx')
    for i,(inf,p3,past,pp) in enumerate(verbs):
        y=186+i*10
        g+=t(60,y,inf,'middle','Lx'); g+=t(160,y,p3,'middle','Lx')
        g+=t(240,y,past,'middle','Lx'); g+=t(340,y,pp,'middle','Lx')
    g+=hr(242)
    g+=sh(251,'SEPARABLE VERBS AND PREFIXES')
    g+=t(240,261,'Like Dutch, German has separable verbs: prefix moves to end in main clauses.','middle','Ls')
    g+=t(240,271,'aufmachen (open): Ich mache das Fenster auf. (I open the window.)','middle','Ls')
    g+=t(240,281,'Inseparable prefixes (be-, ver-, zer-, ge-) never separate.','middle','Ls')
    g+=hr(289)
    g+=sh(298,'CORE VOCABULARY')
    vocab=[('hallo / guten Tag','hello'),('danke','thank you'),('ja','yes'),
           ('nein','no'),('entschuldigung','excuse me'),('wie geht es Ihnen?','how are you?'),
           ('gut, danke','fine, thanks'),('ich liebe dich','I love you'),
           ('Wasser','water'),('Feuer','fire'),('Erde','earth'),
           ('Mensch','person'),('Zeit','time'),('Mond','moon'),
           ('Stern','star'),('Herz','heart'),('Liebe','love'),
           ('Freiheit','freedom'),('Erinnerung','memory'),
           ('Zukunft','future'),('Welt','world'),('Leben','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=308+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('52','German','C','Grammar')
    return g+close_svg()

def build_52d():
    g=open_svg()
    g+=t(240,32,'GERMAN','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. SPRICHWORT \u2014 PROVERB')
    g+=t(240,80,'Wer nicht wagt, der nicht gewinnt.','middle','L')
    g+=t(240,90,'wer=who nicht-wagt=does-not-dare der=that-one nicht=not gewinnt=wins','middle','Ls')
    g+=t(240,100,'"Who dares not, wins not." (German proverb; like the Dutch)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. ERINNERUNG \u2014 ON MEMORY')
    g+=t(240,128,'Wer die Vergangenheit nicht kennt, ist verdammt, sie zu wiederholen.','middle','L')
    g+=t(240,138,'wer=who die-Vergangenheit=the-past nicht-kennt=does-not-know','middle','Ls')
    g+=t(240,148,'ist-verdammt=is-condemned sie-zu-wiederholen=to-repeat-it','middle','Ls')
    g+=t(240,158,'"Who does not know the past is condemned to repeat it." (after Santayana, German form)','middle','F')
    g+=hr(167)
    g+=sh(176,'III. WISSEN \u2014 ON KNOWLEDGE')
    g+=t(240,186,'Das Wissen ist die einzige Flamme, die heller wird, wenn man sie teilt.','middle','L')
    g+=t(240,196,'das-Wissen=knowledge ist=is die-einzige=the-only Flamme=flame','middle','Ls')
    g+=t(240,206,'die-heller-wird=that-gets-brighter wenn-man-sie-teilt=when-one-shares-it','middle','Ls')
    g+=t(240,216,'"Knowledge is the only flame that grows brighter when shared."','middle','F')
    g+=hr(225)
    g+=sh(234,'IV. VORW\u00c4RTS \u2014 FORWARD')
    g+=t(240,244,'Wir gehen vorw\u00e4rts, w\u00e4hrend wir an jene denken, die vor uns gingen.','middle','L')
    g+=t(240,254,'vorw\u00e4rts=forward w\u00e4hrend=while an-jene-denken=think-of-those','middle','Ls')
    g+=t(240,264,'die-vor-uns-gingen=who-went-before-us','middle','Ls')
    g+=t(240,274,'"We go forward while thinking of those who went before us."','middle','F')
    g+=hr(283)
    g+=sh(292,'V. BRIDGE PHRASE')
    g+=t(240,305,'Dies wurde f\u00fcr dich gemacht, kostenlos,','middle','L')
    g+=t(240,315,'von Menschen, die vorw\u00e4rts erinnerten.','middle','L')
    g+=t(240,329,'dies=this wurde=was gemacht=made f\u00fcr-dich=for-you kostenlos=free-of-cost','middle','Ls')
    g+=t(240,338,'von=by Menschen=people die=who vorw\u00e4rts=forward erinnerten=remembered','middle','Ls')
    g+=t(240,350,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(361)
    g+=sh(370,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,380,'Vorw\u00e4rts = "forward." Sich erinnern = to remember. "Vorw\u00e4rts erinnern" is coined.','middle','Ls')
    g+=t(240,390,'It means: directing one\'s remembering toward the future rather than backward.','middle','Ls')
    g+=t(240,400,'Kostenlos = free/gratis (Kosten=costs + -los=without).','middle','Ls')
    g+=hr(408)
    g+=sh(417,'LANGUAGE NOTES')
    g+=t(240,427,'German: ~100 million L1 speakers in Germany, Austria, Switzerland, Luxembourg.','middle','Ls')
    g+=t(240,437,'Language family: Indo-European, West Germanic (with English, Dutch, Frisian).','middle','Ls')
    g+=t(240,447,'Gutenberg\'s printing press (1440) standardised German orthography and spread literacy.','middle','Ls')
    g+=t(240,457,'Scientific/philosophical heritage: Kant, Hegel, Marx, Einstein, Freud, Nietzsche.','middle','Ls')
    g+=footer('52','German','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate52a_german_script.svg': build_52a(),
        'plate52b_german_phonology.svg': build_52b(),
        'plate52c_german_grammar.svg': build_52c(),
        'plate52d_german_text.svg': build_52d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
