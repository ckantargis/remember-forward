"""Build script — Thai series plates 39A–39D (Remember Forward)"""
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
            '.Lt{font-size:11px;}\n'
            '.Lts{font-size:8px;}\n'
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

# ─── PLATE 39A — SCRIPT ────────────────────────────────────────────────────
def build_39a():
    g=open_svg()
    g+=t(240,32,'THAI','middle','T')
    g+=t(240,50,'\u0e20\u0e32\u0e29\u0e32\u0e44\u0e17\u0e22 \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM \u2014 ABUGIDA')
    g+=t(240,82,'Thai script is an abugida: consonants carry an inherent vowel /\u0254/. Written left to right.','middle','Ls')
    g+=t(240,92,'Derived from Khmer script, which descended from South Indian Brahmic scripts (~13th c).','middle','Ls')
    g+=t(240,102,'No spaces between words; sentence boundaries marked by spaces.','middle','Ls')
    g+=hr(110)
    g+=sh(119,'CONSONANT CLASSES \u2014 THREE CLASSES')
    g+=t(240,129,'Each consonant belongs to one of three classes that determine tone calculation.','middle','Ls')
    g+=t(240,139,'High class (11): \u0e02 \u0e03 \u0e09 \u0e10 \u0e11 \u0e12 \u0e13 \u0e14 \u0e2b \u0e1f \u0e2a','middle','Lt')
    g+=t(240,152,'Mid class (9): \u0e01 \u0e08 \u0e14 \u0e15 \u0e1a \u0e1b \u0e2d \u0e2e \u0e2f','middle','Lt')
    g+=t(240,165,'Low class (24): \u0e07 \u0e0a \u0e0b \u0e0d \u0e10 \u0e11 \u0e12 \u0e13 \u0e19 \u0e1e \u0e1f \u0e1d \u0e1e \u0e20 \u0e21 \u0e22 \u0e23 \u0e25 \u0e27 \u0e2c \u0e2e \u0e2d \u0e2a \u0e2e','middle','Lt')
    g+=hr(178)
    g+=sh(187,'SELECTED CONSONANTS WITH RTGS ROMANISATION')
    cons=[('\u0e01','k','/k/'),('\u0e02','\u1e35h','/k\u02b0/'),('\u0e04','kh','/k\u02b0/'),
          ('\u0e07','ng','/\u014b/'),('\u0e08','ch','/t\u0255/'),('\u0e0a','ch','/t\u0255/'),
          ('\u0e0d','y','/j/'),('\u0e15','t','/t/'),('\u0e16','th','/t\u02b0/'),
          ('\u0e19','n','/n/'),('\u0e1a','b','/b/'),('\u0e1b','p','/p/'),
          ('\u0e1e','ph','/p\u02b0/'),('\u0e21','m','/m/'),('\u0e22','y','/j/'),
          ('\u0e23','r','/r/'),('\u0e25','l','/l/'),('\u0e27','w','/w/'),
          ('\u0e2a','s','/s/'),('\u0e2b','h','/h/'),('\u0e2d','\u2014','(silent/\u0254/ onset)')]
    for i,(thai,rtgs,ipa) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=197+row*11
        g+=t(x-10,y,thai,'middle','Lts'); g+=t(x+15,y,f'{rtgs} {ipa}','middle','Lx')
    g+=hr(290)
    g+=sh(299,'VOWEL DIACRITICS')
    g+=t(240,309,'Thai vowels are written as diacritics around the base consonant.','middle','Ls')
    g+=t(240,319,'C = consonant placeholder. Vowel position: above, below, before, after, or surrounding.','middle','Ls')
    vowels=[('\u0e41C','ae /\u00e6/'),('C\u0e32','aa /a\u02d0/'),('C\u0e34','i /i/'),
            ('C\u0e35','ii /i\u02d0/'),('C\u0e36','ue /\u026f/'),('\u0e40C','e /e/'),
            ('\u0e40C\u0e35\u0e22','ia /i\u0259/'),('C\u0e27','ua /u\u0259/'),('C\u0e38','u /u/')]
    for i,(v,desc) in enumerate(vowels):
        col=i%3; row=i//3
        x=65+col*130; y=329+row*11
        g+=t(x,y,f'{v} = {desc}','middle','Ls')
    g+=hr(377)
    g+=sh(386,'TONE MARKS')
    g+=t(240,396,'Thai has 4 tone marks + unmarked, combined with consonant class to produce 5 tones.','middle','Ls')
    tmarks=[('\u0e48','mai ek (low/falling marker)'),('\u0e49','mai tho (falling/high marker)'),
            ('\u0e4a','mai tri (high marker)'),('\u0e4b','mai jattawa (rising marker)')]
    for i,(m,desc) in enumerate(tmarks):
        y=406+i*10
        g+=t(120,y,m,'middle','Lt'); g+=t(290,y,desc,'middle','Ls')
    g+=hr(450)
    g+=sh(459,'THAI NUMERALS')
    g+=t(240,469,'\u0e50\u0e51\u0e52\u0e53\u0e54\u0e55\u0e56\u0e57\u0e58\u0e59  (0-9)','middle','Lt')
    g+=t(240,482,'Thai numerals are still used alongside Arabic numerals.','middle','Ls')
    g+=footer('39','Thai','A','Script')
    return g+close_svg()

# ─── PLATE 39B — PHONOLOGY ─────────────────────────────────────────────────
def build_39b():
    g=open_svg()
    g+=t(240,32,'THAI','middle','T')
    g+=t(240,50,'Phonology \u2014 Five Tones and Sound System','middle','S')
    g+=hr(60)
    g+=sh(72,'FIVE-TONE SYSTEM')
    g+=t(240,82,'Thai (Bangkok) has 5 phonemic tones. Tone is determined by consonant class + tone marks.','middle','Ls')
    tones=[('Mid (sa\u014dn\u0101)','mid level 33','kao = he/she (mid class, no mark)'),
           ('Low (ek)','low falling 21','k\u00e0o = news/rice (low class, mai ek)'),
           ('Falling (tho)','high falling 51','k\u00e2o = nine (mid class, mai tho)'),
           ('High (tri)','high rising 45','k\u0101o = enter (high class, no mark)'),
           ('Rising (jattawa)','low dipping 213','k\u01ceo = white (mid class, mai jattawa)')]
    for i,(name,contour,ex) in enumerate(tones):
        y=92+i*11
        g+=t(90,y,name,'middle','Ls'); g+=t(210,y,contour,'middle','Lx'); g+=t(370,y,ex,'middle','Lx')
    g+=hr(153)
    g+=sh(162,'CONSONANT INVENTORY')
    g+=t(240,172,'Initial consonants: 21 distinct sounds. Final consonants: 8 allowed (-k, -t, -p, -m, -n, -ng, -j, -w).','middle','Ls')
    cons=[('/p/','bilabial stop'),('/p\u02b0/','aspirated bilabial'),('/b/','bilabial stop vd'),
          ('/t/','alveolar stop'),('/t\u02b0/','aspirated alveolar'),('/d/','alveolar stop vd'),
          ('/k/','velar stop'),('/k\u02b0/','aspirated velar'),('/\u0294/','glottal stop'),
          ('/t\u0255/','palatal affricate'),('/t\u0255\u02b0/','aspirated palatal'),
          ('/f/','labiodental'),('/s/','alveolar fric'),('/h/','glottal'),
          ('/m/','bilabial nasal'),('/n/','alveolar nasal'),('/\u014b/','velar nasal'),
          ('/l/','lateral'),('/r/','trill'),('/w/','labio-velar'),('/j/','palatal')]
    for i,(ipa,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=182+row*10
        g+=t(x,y,f'{ipa} {desc}','middle','Lx')
    g+=hr(275)
    g+=sh(284,'VOWEL SYSTEM \u2014 21 VOWELS (SHORT + LONG)')
    g+=t(240,294,'Thai distinguishes vowel length: short/long pairs. 9 short + 9 long + 3 triphthongs.','middle','Ls')
    g+=t(240,304,'Short: /a \u026a \u026f \u028a \u025b e \u0254 o \u0250/  Long: /a\u02d0 i\u02d0 \u026f\u02d0 u\u02d0 \u025b\u02d0 e\u02d0 \u0254\u02d0 o\u02d0 \u0250\u02d0/','middle','Ls')
    g+=hr(312)
    g+=sh(321,'TONE CALCULATION RULES')
    g+=t(240,331,'Tone depends on: (1) consonant class (high/mid/low), (2) syllable type (live/dead),','middle','Ls')
    g+=t(240,341,'(3) tone mark present. Dead syllable = ends in stop or short vowel.','middle','Ls')
    g+=t(240,351,'Mid class + no mark + live = mid tone. Mid class + no mark + dead = low tone.','middle','Ls')
    g+=t(240,361,'High class consonant raises tones. Low class consonant lowers tones.','middle','Ls')
    g+=hr(369)
    g+=sh(378,'BORROWED SOUNDS')
    g+=t(240,388,'Foreign loanwords may use /v/, /f/ (limited), and complex onsets (kr-, kl-, pr-, pl-, tr-).','middle','Ls')
    g+=t(240,398,'English loanwords common: \u0e2d\u0e34\u0e19\u0e40\u0e15\u0e2d\u0e23\u0e4c (internet), \u0e42\u0e17\u0e23\u0e28\u0e31\u0e1e\u0e17\u0e4c (telephone).','middle','Ls')
    g+=hr(406)
    g+=sh(415,'PHONOTACTICS')
    g+=t(240,425,'No consonant clusters in coda. Onset clusters limited to: stop/nasal + r/l/w.','middle','Ls')
    g+=t(240,435,'Syllable: (C)(C)V(V)(C)(T) — T = tone. CV is minimal syllable.','middle','Ls')
    g+=footer('39','Thai','B','Phonology')
    return g+close_svg()

# ─── PLATE 39C — GRAMMAR ───────────────────────────────────────────────────
def build_39c():
    g=open_svg()
    g+=t(240,32,'THAI','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SVO, ISOLATING')
    g+=t(240,82,'Thai is an isolating language like Vietnamese. No inflection, no case markers.','middle','Ls')
    g+=t(240,92,'Phom kin khao. I eat rice. (phom=I[male] kin=eat khao=rice)','middle','Ls')
    g+=t(240,102,'Politeness particles: phom (I, male), chan/dichon (I, female), khun (you).','middle','Ls')
    g+=hr(110)
    g+=sh(119,'POLITENESS PARTICLES')
    g+=t(240,129,'Sentence-final particles mark politeness and gender:','middle','Ls')
    g+=t(240,139,'kh\u0101p (male speaker) / kha (female speaker) — respectful acknowledgement.','middle','Ls')
    g+=t(240,149,'na — softening/seeking agreement. Si — mild emphasis/suggestion.','middle','Ls')
    g+=hr(157)
    g+=sh(166,'VERB SYSTEM')
    g+=t(240,176,'Verbs uninflected. Tense/aspect by time words and aspect particles:','middle','Ls')
    particles=[('laeo','completed/already'),('ya\u014b','still/continuing'),
               ('ja','will/future intent'),('k\u0113oap','about to'),
               ('tham-mai','why'),('y\u016f','have been doing')]
    for i,(p,gloss) in enumerate(particles):
        y=186+i*10
        g+=t(120,y,p,'middle','Ls'); g+=t(290,y,gloss,'middle','Ls')
    g+=hr(252)
    g+=sh(261,'CLASSIFIERS (LAKSANANAM)')
    g+=t(240,271,'Like Vietnamese and Chinese, Thai requires classifiers with numbers.','middle','Ls')
    classifiers=[('khon','people'),('tua','animals, clothing'),('lam','boats, aircraft'),
                 ('kh\u1ea1n','books'),('bai','flat things, leaves, tickets'),
                 ('an','general small items'),('h\u014dng','rooms'),
                 ('lang','houses/buildings')]
    for i,(cl,desc) in enumerate(classifiers):
        col=i%2; row=i//2
        x=80+col*200; y=281+row*10
        g+=t(x,y,f'{cl}: {desc}','middle','Lx')
    g+=hr(335)
    g+=sh(344,'NEGATION AND QUESTIONS')
    g+=t(240,354,'Negation: mai before verb: mai kin = not eat. mai dai = cannot/did not.','middle','Ls')
    g+=t(240,364,'Yes/no question: add mai at end: kin khao mai? = eat rice? (do you eat?)','middle','Ls')
    g+=t(240,374,'Answer: chai (yes) / mai chai (no).','middle','Ls')
    g+=hr(382)
    g+=sh(391,'CORE VOCABULARY')
    vocab=[('sawasdee','hello/goodbye'),('khop khun','thank you'),('chai','yes'),
           ('mai chai','no'),('khana thoht','excuse me/sorry'),('sabai dee mai?','how are you?'),
           ('sabai dee','I am fine'),('chan rak khun','I love you [female]'),
           ('phom rak khun','I love you [male]'),('nam','water'),('fai','fire'),
           ('din','earth/soil'),('khon','person'),('wela','time'),('duang jan','moon'),
           ('dao','star'),('hua jai','heart'),('khwam rak','love'),
           ('seriphap','freedom'),('khwam jam','memory'),
           ('anakhot','future'),('lok','world'),('chiwit','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=401+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('39','Thai','C','Grammar')
    return g+close_svg()

# ─── PLATE 39D — RUNNING TEXT ──────────────────────────────────────────────
def build_39d():
    g=open_svg()
    g+=t(240,32,'THAI','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. SUPHACIT \u2014 PROVERB')
    g+=t(240,80,'\u0e04\u0e27\u0e32\u0e21\u0e23\u0e39\u0e49\u0e04\u0e37\u0e2d\u0e41\u0e2a\u0e07\u0e2a\u0e27\u0e48\u0e32\u0e07\u0e43\u0e19\u0e04\u0e27\u0e32\u0e21\u0e21\u0e37\u0e14','middle','Lt')
    g+=t(240,94,'khwam-ru = knowledge khu = is saeng-sawang = bright light nai = in khwam-muet = darkness','middle','Ls')
    g+=t(240,104,'"Knowledge is the bright light in the darkness." (Thai educational proverb)','middle','F')
    g+=hr(113)
    g+=sh(122,'II. KHWAM JAM \u2014 ON MEMORY')
    g+=t(240,132,'\u0e08\u0e33\u0e04\u0e19\u0e43\u0e19\u0e2d\u0e14\u0e35\u0e15\u0e04\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e2d\u0e19\u0e32\u0e04\u0e15','middle','Lt')
    g+=t(240,146,'jam = remember khon = people nai = in a-dit = past khu = is kan-sang = the building anakhot = future','middle','Ls')
    g+=t(240,156,'"Remembering the people of the past is building the future." (Thai saying)','middle','F')
    g+=hr(165)
    g+=sh(174,'III. PANYA \u2014 ON WISDOM')
    g+=t(240,184,'\u0e1b\u0e31\u0e0d\u0e0d\u0e32\u0e04\u0e37\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e23\u0e39\u0e49\u0e17\u0e35\u0e48\u0e2a\u0e31\u0e48\u0e07\u0e2a\u0e21\u0e44\u0e27\u0e49\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e16\u0e48\u0e32\u0e22\u0e17\u0e2d\u0e14','middle','Lt')
    g+=t(240,198,'panya = wisdom khu = is khwam-ru = knowledge thi = that sang-som-wai = accumulated phua = for thay-thot = passing-on','middle','Lx')
    g+=t(240,208,'"Wisdom is knowledge accumulated to be passed on." (Thai concept of inherited wisdom)','middle','F')
    g+=hr(217)
    g+=sh(226,'IV. KHANG NA \u2014 FORWARD')
    g+=t(240,236,'\u0e23\u0e30\u0e25\u0e36\u0e01\u0e16\u0e36\u0e07\u0e2d\u0e14\u0e35\u0e15\u0e40\u0e14\u0e34\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e44\u0e1b','middle','Lt')
    g+=t(240,250,'ra-luek = remember thueng = of/about a-dit = past doen = walk na = forward pai = go','middle','Ls')
    g+=t(240,260,'"Remembering the past, [we] walk forward." (guiding principle)','middle','F')
    g+=hr(269)
    g+=sh(278,'V. BRIDGE PHRASE')
    g+=t(240,290,'\u0e2a\u0e34\u0e48\u0e07\u0e19\u0e35\u0e49\u0e16\u0e39\u0e01\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e04\u0e38\u0e13','middle','Lt')
    g+=t(240,304,'\u0e42\u0e14\u0e22\u0e44\u0e21\u0e48\u0e40\u0e2a\u0e35\u0e22\u0e04\u0e48\u0e32\u0e43\u0e0a\u0e48\u0e08\u0e48\u0e32\u0e22','middle','Lt')
    g+=t(240,318,'\u0e42\u0e14\u0e22\u0e1c\u0e39\u0e49\u0e04\u0e19\u0e17\u0e35\u0e48\u0e08\u0e33\u0e44\u0e27\u0e49\u0e01\u0e49\u0e32\u0e27\u0e2b\u0e19\u0e49\u0e32','middle','Lt')
    g+=t(240,335,'sing-ni = this-thing thuuk-sang = was-made khuen-ma = up/for phuea = for khun = you','middle','Ls')
    g+=t(240,344,'doi-mai-sia-kha = without-cost (free of charge)','middle','Ls')
    g+=t(240,353,'doi = by phu-khon = people thi = who jam-wai = remember-and-keep kao-na = forward','middle','Ls')
    g+=t(240,365,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(376)
    g+=sh(385,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,395,'Khao na (\u0e40\u0e02\u0e49\u0e32\u0e2b\u0e19\u0e49\u0e32) = go forward/advance. Na (\u0e2b\u0e19\u0e49\u0e32) = face/front.','middle','Ls')
    g+=t(240,405,'Jam wai = "remember and keep" (preserve in memory). The Thai spatial metaphor','middle','Ls')
    g+=t(240,415,'places the future in front and the past behind, like most world languages.','middle','Ls')
    g+=t(240,425,'Doi mai sia kha = "without expense/cost" — polite formal phrasing.','middle','Ls')
    g+=hr(433)
    g+=sh(442,'LANGUAGE NOTES')
    g+=t(240,452,'Thai: ~60 million L1 speakers; official language of Thailand.','middle','Ls')
    g+=t(240,462,'Language family: Tai-Kadai (Kra-Dai), closely related to Lao, Shan, Zhuang.','middle','Ls')
    g+=t(240,472,'Script derived from Khmer/Old Khmer, in turn from Pallava (South India), ~13th century.','middle','Ls')
    g+=t(240,482,'Extensive Sanskrit/Pali loanwords in formal register; Sino-Thai in everyday speech.','middle','Ls')
    g+=footer('39','Thai','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate39a_thai_script.svg': build_39a(),
        'plate39b_thai_phonology.svg': build_39b(),
        'plate39c_thai_grammar.svg': build_39c(),
        'plate39d_thai_text.svg': build_39d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
