"""Build script — Lao series plates 41A–41D (Remember Forward)"""
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
            '.Ll{font-size:11px;}\n'
            '.Lls{font-size:8px;}\n'
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

def build_41a():
    g=open_svg()
    g+=t(240,32,'LAO','middle','T')
    g+=t(240,50,'\u0ea0\u0eb2\u0eaa\u0eb2\u0ea5\u0eb2\u0ea7 \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM \u2014 ABUGIDA')
    g+=t(240,84,'Lao script is an abugida closely related to Thai script. Written left to right.','middle','Ls')
    g+=t(240,94,'Derived from Khmer/Old Khmer via the same Brahmic lineage as Thai (13th century).','middle','Ls')
    g+=t(240,104,'Consonants have inherent vowel /o/; vowel diacritics modify the inherent sound.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'CONSONANTS \u2014 27 LETTERS, 2 CLASSES')
    g+=t(240,131,'Unlike Thai (3 classes), Lao has 2 consonant classes: high and low.','middle','Ls')
    g+=t(240,141,'High class (7): \u0e81 \u0e82 \u0e88 \u0e8a \u0e8d \u0ea1 \u0eaa','middle','Ll')
    g+=t(240,155,'Low class (20): \u0e87 \u0e8a \u0e8d \u0e99 \u0ea1 \u0ea2 \u0ea3 \u0ea5 \u0ea7 \u0eab \u0e9a \u0e9b \u0e9e \u0e9f \u0ea1 \u0e9c \u0e9d \u0e9e \u0e9f \u0ea0','middle','Ll')
    g+=hr(169)
    g+=sh(178,'SELECTED CONSONANTS')
    cons=[('\u0e81','k /k/'),('\u0e82','kh /k\u02b0/'),('\u0e87','ng /\u014b/'),
          ('\u0e88','ch /t\u0255/'),('\u0e8d','ny /\u0272/'),('\u0e99','n /n/'),
          ('\u0ea1','m /m/'),('\u0ea2','y /j/'),('\u0ea3','r /r/ rare'),
          ('\u0ea5','l /l/'),('\u0ea7','w /w/'),('\u0eaa','s /s/'),
          ('\u0eab','h /h/'),('\u0ea0','silent h (class marker)')]
    for i,(lao,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=188+row*12
        g+=t(x-5,y,lao,'middle','Ll'); g+=t(x+20,y+2,desc,'middle','Lx')
    g+=hr(265)
    g+=sh(274,'VOWEL DIACRITICS')
    g+=t(240,284,'C = consonant placeholder. Vowels written around the base consonant.','middle','Ls')
    vowels=[('\u0c81C','\u0ec2C','aa /a\u02d0/'),('\u0ebcC\u0eb4','\u0ec2C','i /i/'),
            ('\u0ec0C','\u0ec2C','e /e/'),('\u0ec2C','','o /o/'),
            ('\u0ec0C\u0eb2','','ua /u\u0259/'),('\u0ebcC\u0eb8','','u /u/')]
    for i,(v1,v2,desc) in enumerate(vowels):
        y=294+i*10
        g+=t(120,y,v1,'middle','Lls'); g+=t(290,y,desc,'middle','Ls')
    g+=hr(360)
    g+=sh(369,'SIX TONES')
    g+=t(240,379,'Lao has 6 tones (some dialects 5). Tone determined by consonant class + tone marks.','middle','Ls')
    tones=[('Low','mid-low level: sa\u014dn\u0101 /33/'),
           ('Mid','mid level: ek /33/ (same as low in some analyses)'),
           ('High','high level: tho /44/'),
           ('Rising','low-rising: tri /13/'),
           ('High falling','high-falling: jattawa /42/'),
           ('Low falling','low-falling: may ek low /21/')]
    for i,(name,desc) in enumerate(tones):
        y=389+i*10
        g+=t(100,y,name,'middle','Ls'); g+=t(300,y,desc,'middle','Lx')
    g+=hr(455)
    g+=sh(464,'LAO NUMERALS')
    g+=t(240,474,'\u0ed0\u0ed1\u0ed2\u0ed3\u0ed4\u0ed5\u0ed6\u0ed7\u0ed8\u0ed9  (0\u20139)','middle','Ll')
    g+=t(240,488,'10 = \u0ed1\u0ed0  100 = \u0eae\u0ec9\u0ead\u0e8d  1000 = \u0e9e\u0eb1\u0e99','middle','Ll')
    g+=footer('41','Lao','A','Script')
    return g+close_svg()

def build_41b():
    g=open_svg()
    g+=t(240,32,'LAO','middle','T')
    g+=t(240,50,'Phonology \u2014 Tones and Sound System','middle','S')
    g+=hr(60)
    g+=sh(72,'SIX-TONE SYSTEM (VIENTIANE DIALECT)')
    g+=t(240,82,'Lao has 6 phonemic tones in the Vientiane (standard) dialect:','middle','Ls')
    tones=[('Low (sam\u0101n)','mid-low 22: no mark, low class'),
           ('Mid (ek)','mid 33: may ek on low class'),
           ('High (tho)','high 44: high class, no mark'),
           ('Rising (tri)','low-rising 13: may ek on high class'),
           ('High falling','high-falling 42: may tho on high class'),
           ('Low falling','low-dipping 21: may tho on low class')]
    for i,(name,desc) in enumerate(tones):
        y=92+i*11
        g+=t(90,y,name,'middle','Ls'); g+=t(310,y,desc,'middle','Lx')
    g+=hr(163)
    g+=sh(172,'CONSONANTS')
    cons=[('k /k/','velar stop vl'),('kh /k\u02b0/','aspirated velar'),
          ('ng /\u014b/','velar nasal'),('ch /t\u0255/','palatal affricate'),
          ('ny /\u0272/','palatal nasal'),('n /n/','alveolar nasal'),
          ('b /b/','bilabial stop'),('p /p/','bilabial stop vl'),
          ('ph /p\u02b0/','aspirated bilabial'),('f /f/','labiodental'),
          ('m /m/','bilabial nasal'),('y /j/','palatal approximant'),
          ('r /r\u0303/','trill (rare in standard)'),('l /l/','lateral'),
          ('w /w/','labio-velar'),('s /s/','alveolar fricative'),('h /h/','glottal')]
    for i,(c,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=182+row*10
        g+=t(x,y,f'{c} {desc}','middle','Lx')
    g+=hr(278)
    g+=sh(287,'VOWELS')
    g+=t(240,297,'Lao has short/long vowel pairs. 9 monophthongs (short+long) + diphthongs.','middle','Ls')
    g+=t(240,307,'/a aa/ /\u026a i\u02d0/ /\u026f u\u02d0 (approx)/ /\u025b e\u02d0/ /\u0254 o\u02d0/ /\u0250 \u0250\u02d0/ + diphthongs /ia ua \u026fa/','middle','Ls')
    g+=hr(315)
    g+=sh(324,'COMPARISON WITH THAI')
    g+=t(240,334,'Lao and Thai are mutually intelligible at high register; closely related.','middle','Ls')
    g+=t(240,344,'Lao has 2 consonant classes (vs Thai\'s 3); some consonant simplifications.','middle','Ls')
    g+=t(240,354,'Spoken Lao: r often merged to l; final -r dropped; ng- onset rare.','middle','Ls')
    g+=t(240,364,'Lao script cannot write all sounds of formal Thai vocabulary.','middle','Ls')
    g+=hr(372)
    g+=sh(381,'PHONOTACTICS')
    g+=t(240,391,'Syllable: (C)(G)V(V)(C). Codas: -k, -t, -p, -m, -n, -ng, -j, -w.','middle','Ls')
    g+=t(240,401,'Onset clusters: only C+w or C+j (written with semi-vowel diacritics).','middle','Ls')
    g+=footer('41','Lao','B','Phonology')
    return g+close_svg()

def build_41c():
    g=open_svg()
    g+=t(240,32,'LAO','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SVO, ISOLATING')
    g+=t(240,82,'Lao is SVO and isolating, like Thai. No inflection; particles carry meaning.','middle','Ls')
    g+=t(240,92,'Khoi kin khao. I eat rice. (khoi=I kin=eat khao=rice)','middle','Ls')
    g+=hr(100)
    g+=sh(109,'PRONOUNS AND POLITENESS')
    pros=[('khoi','I (standard/neutral)'),('khao','he/she/they'),
          ('jao','you (informal)'),('than','you (respectful)'),
          ('phualao','we (incl)'),('phakkhao','they (group)')]
    for i,(p,gloss) in enumerate(pros):
        y=119+i*10
        g+=t(120,y,p,'middle','L'); g+=t(300,y,gloss,'middle','Ls')
    g+=hr(185)
    g+=sh(194,'VERB PARTICLES')
    particles=[('laeo','already/completed'),('si','future'),('yang','still'),
               ('kamlang','progressive'),('ja','will/about to'),('ko','also/then')]
    for i,(p,gloss) in enumerate(particles):
        col=i%2; row=i//2
        x=80+col*200; y=204+row*10
        g+=t(x,y,f'{p} = {gloss}','middle','Lx')
    g+=hr(250)
    g+=sh(259,'CLASSIFIERS')
    classifiers=[('khon','people'),('tua','animals'),('bai','flat things'),
                 ('kan','tools/instruments'),('hon','houses'),('kham','words')]
    for i,(cl,desc) in enumerate(classifiers):
        col=i%2; row=i//2
        x=80+col*200; y=269+row*10
        g+=t(x,y,f'{cl}: {desc}','middle','Lx')
    g+=hr(310)
    g+=sh(319,'CORE VOCABULARY')
    vocab=[('sabaidi','hello / well-being'),('khop jai','thank you'),('muen','yes'),
           ('boh','no/not'),('khothot','excuse me'),('jao sabai di boh?','how are you?'),
           ('khoi sabai di','I am fine'),('khoi hak jao','I love you'),
           ('nam','water'),('fai','fire'),('din','earth'),('khon','person'),
           ('wela','time'),('duan','moon'),('dao','star'),
           ('hua jai','heart'),('khwam hak','love'),('seli phap','freedom'),
           ('khwam jam','memory'),('anakhot','future'),('lok','world'),
           ('chiwitkan','life'),('na','forward / face / front')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=329+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('41','Lao','C','Grammar')
    return g+close_svg()

def build_41d():
    g=open_svg()
    g+=t(240,32,'LAO','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. PHAXITH \u2014 PROVERB')
    g+=t(240,80,'\u0ec4\u0e94\u0ec9\u0ea2\u0eb4\u0e99 \u0ec0\u0e9a\u0eb4\u0ec8\u0e87\u0e94\u0eb5 \u0e9a\u0ecd\u0ec8\u0ec0\u0e95\u0eb1\u0ec9\u0e99\u0e95\u0ebb\u0e9a\u0ec0\u0e87\u0eb4\u0e99','middle','Ll')
    g+=t(240,94,'dai-yin beuang-di boh-tan-top-ngoen = received-hearing good cannot-answer-money','middle','Ls')
    g+=t(240,104,'"Good advice received cannot be repaid with money." (Lao proverb on wisdom)','middle','F')
    g+=hr(113)
    g+=sh(122,'II. KHWAM JAM \u2014 ON MEMORY')
    g+=t(240,132,'\u0e81\u0eb2\u0e99\u0ec4\u0ea7\u0ec9\u0ec3\u0e88 \u0e82\u0ead\u0e87\u0e84\u0ebb\u0e99\u0ec3\u0e99\u0ead\u0e94\u0eb5\u0e95 \u0ec0\u0e9b\u0eb1\u0e99\u0ec2\u0e8a\u0e81\u0e8a\u0eb0\u0e95\u0eb2\u0ec0\u0e94\u0eb5\u0e99\u0e99\u0eb2','middle','Ll')
    g+=t(240,146,'kan-wai-chai khong-khon nai-a-dit pen-chok-cha-ta-doen-na','middle','Ls')
    g+=t(240,156,'"Trusting the people of the past is the good fortune that moves us forward."','middle','F')
    g+=hr(165)
    g+=sh(174,'III. SANYALAK \u2014 ON KNOWLEDGE')
    g+=t(240,184,'\u0e9e\u0eb9\u0ea1\u0eb5\u0e9b\u0eb1\u0e99\u0e8d\u0eb2 \u0e9c\u0eb9\u0ec9\u0e99\u0eb1\u0ec9\u0e99\u0e9a\u0ecd\u0ec8\u0ec0\u0e84\u0e8d\u0ead\u0e94\u0eab\u0ead\u0e81','middle','Ll')
    g+=t(240,198,'phu-mi-panya phunun boh-koei-ot-hok = one-who-has-wisdom that-one never-thirsty','middle','Ls')
    g+=t(240,208,'"One who has wisdom is never thirsty [for understanding]." (Lao educational saying)','middle','F')
    g+=hr(217)
    g+=sh(226,'IV. NA \u2014 FORWARD')
    g+=t(240,236,'\u0eae\u0eb2\u0ec0\u0e94\u0eb5\u0e99\u0e99\u0eb2 \u0ec2\u0e94\u0e8d\u0e88\u0ebb\u0ec8\u0e9a\u0ecd\u0ec8\u0ea5\u0eb7\u0ea1\u0e95\u0ebb\u0e99\u0ec0\u0eab\u0e87\u0ec3\u0e99\u0ead\u0e94\u0eb5\u0e95','middle','Ll')
    g+=t(240,250,'hao-doen-na doi-job-boh-leum ton-heng nai-a-dit','middle','Ls')
    g+=t(240,260,'"We walk forward without forgetting our roots in the past." (guiding principle)','middle','F')
    g+=hr(269)
    g+=sh(278,'V. BRIDGE PHRASE')
    g+=t(240,290,'\u0eaa\u0eb4\u0ec8\u0e87\u0e99\u0eb5\u0ec9\u0ec0\u0e9b\u0eb1\u0e99\u0eaa\u0eb4\u0ec8\u0e87\u0e97\u0eb5\u0ec8\u0e97\u0ecd\u0eaf\u0eaa\u0eb2\u0e87\u0ec3\u0eab\u0ec9\u0ec0\u0e88\u0ebb\u0ec9\u0eaa\u0ebb','middle','Ll')
    g+=t(240,304,'\u0e9a\u0ecd\u0ec8\u0ec0\u0e9e\u0eb5\u0e8d\u0ec3\u0e8a\u0ec9\u0ec0\u0e87\u0eb4\u0e99 \u0ec2\u0e94\u0e8d\u0e9c\u0eb9\u0ec9\u0e84\u0ebb\u0e99\u0e97\u0eb5\u0ec8\u0e88\u0ebb\u0ec8\u0e99\u0eb3\u0ec3\u0e88\u0e99\u0eb2','middle','Ll')
    g+=t(240,320,'sing-ni pen-sing-thi-thao-sang-hai-jao = this-thing is-the-thing-that-they-made-for-you','middle','Ls')
    g+=t(240,329,'boh-phia-chai-ngoen = without-cost (free) doi-phu-khon = by-people','middle','Ls')
    g+=t(240,338,'thi-job-nam-jai-na = who-hold-the-spirit-forward','middle','Ls')
    g+=t(240,350,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(361)
    g+=sh(370,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,380,'Na (\u0edc\u0ec9\u0eb2) = face/front/forward. Nam-jai (\u0e99\u0eb3\u0ec3\u0e88) = "water-heart" = spirit/memory/intention.','middle','Ls')
    g+=t(240,390,'Job-nam-jai-na = "hold the spirit forward" captures deliberate forward memory.','middle','Ls')
    g+=t(240,400,'Boh-phia-chai-ngoen = "not necessary to pay money" = free of charge.','middle','Ls')
    g+=hr(408)
    g+=sh(417,'LANGUAGE NOTES')
    g+=t(240,427,'Lao: ~7 million L1 speakers; official language of Laos.','middle','Ls')
    g+=t(240,437,'Language family: Tai-Kadai (Kra-Dai), same branch as Thai, Shan, Zhuang.','middle','Ls')
    g+=t(240,447,'Spoken across Isan (northeastern Thailand) by ~20 million as a dialect of Lao/Thai.','middle','Ls')
    g+=t(240,457,'Script: closely related to Thai script, both from Khmer/Brahmic origin.','middle','Ls')
    g+=footer('41','Lao','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate41a_lao_script.svg': build_41a(),
        'plate41b_lao_phonology.svg': build_41b(),
        'plate41c_lao_grammar.svg': build_41c(),
        'plate41d_lao_text.svg': build_41d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
