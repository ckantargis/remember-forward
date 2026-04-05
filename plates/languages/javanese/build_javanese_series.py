"""Build script — Javanese series plates 43A–43D (Remember Forward)"""
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

def build_43a():
    g=open_svg()
    g+=t(240,32,'JAVANESE','middle','T')
    g+=t(240,50,'Basa Jawa \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEMS')
    g+=t(240,84,'Javanese uses three scripts in different contexts:','middle','Ls')
    g+=t(240,94,'(1) Hanacaraka / Aksara Jawa: traditional Brahmi-derived abugida.','middle','Ls')
    g+=t(240,104,'(2) Latin (Pegon-influenced): used in modern education and daily writing.','middle','Ls')
    g+=t(240,114,'(3) Pegon: Arabic-based script used in Islamic educational contexts.','middle','Ls')
    g+=hr(122)
    g+=sh(131,'HANACARAKA \u2014 JAVANESE SCRIPT')
    g+=t(240,141,'20 base letters (aksara) arranged in 4 rows of 5 (traditional mnemonic order):','middle','Ls')
    g+=t(240,151,'ha na ca ra ka / da ta sa wa la / pa dha ja ya nya / ma ga ba tha nga','middle','L')
    g+=t(240,163,'Each aksara = consonant + inherent vowel /a/. Stack forms modify consonants.','middle','Ls')
    g+=t(240,173,'Javanese script: \ua998\ua9a0\ua9a2\ua9b0\ua9a6 \ua9a7\ua9ab\ua9b8\ua9c0\ua9c2 \ua99e\ua9a8\ua9aa\ua9c4\ua9c6 \ua9b0\ua9b2\ua9b4\ua9b6\ua9b8','middle','L')
    g+=hr(184)
    g+=sh(193,'VOWEL SYSTEM \u2014 LATIN ORTHOGRAPHY')
    g+=t(240,203,'Standard Javanese uses Latin orthography in modern texts. 6 vowels:','middle','Ls')
    vowels=[('a /\u0254/','schwa-like open back: ora (no), apa (what)'),
            ('e /\u025b/ or /\u0259/','context-dependent: elek (bad), mengko (later)'),
            ('i /i/','high front: iki (this), siji (one)'),
            ('o /o/','mid-back: loro (two), roto (all)'),
            ('u /u/','high back: udan (rain), satu (one)'),
            ('\xe9 /e/','close-mid (marked in careful texts)')]
    for i,(v,desc) in enumerate(vowels):
        y=213+i*10
        g+=t(80,y,v,'middle','Ls'); g+=t(290,y,desc,'middle','Lx')
    g+=hr(280)
    g+=sh(289,'SPEECH REGISTERS \u2014 NGOKO, MADYA, KRAMA')
    g+=t(240,299,'Javanese has 3 main speech registers encoding social hierarchy:','middle','Ls')
    regs=[('Ngoko','informal: used with close friends, younger/lower-status. Core vocabulary.'),
          ('Madya','intermediate: polite but not highly formal. Urban/modern register.'),
          ('Krama','formal: used with elders, superiors, strangers. Different vocabulary.'),
          ('Krama Inggil','highest respect: special vocabulary for high-status persons.')]
    for i,(r,desc) in enumerate(regs):
        y=309+i*11
        g+=t(90,y,r,'middle','Ls'); g+=t(310,y,desc,'middle','Lx')
    g+=hr(358)
    g+=sh(367,'REGISTER COMPARISON')
    g+=t(240,377,'Concept       Ngoko          Madya          Krama','middle','Lx')
    g+=t(240,387,'"I"           aku            kula           dalem','middle','Lx')
    g+=t(240,397,'"you"         kowe           sampeyan       panjenengan','middle','Lx')
    g+=t(240,407,'"eat"         mangan         nedha           dhahar','middle','Lx')
    g+=t(240,417,'"sleep"       turu           tilem            sare','middle','Lx')
    g+=t(240,427,'"house"       omah           griya           dalem','middle','Lx')
    g+=hr(435)
    g+=sh(444,'JAVANESE NUMERALS')
    nums=[('1','siji'),('2','loro'),('3','telu'),('4','papat'),('5','lima'),
          ('6','enem'),('7','pitu'),('8','wolu'),('9','songo'),('10','sepuluh')]
    for i,(n,w) in enumerate(nums):
        col=i%5; row=i//5
        x=55+col*78; y=454+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,474,'100 = satus · 1000 = sewu · 1,000,000 = yuta','middle','Ls')
    g+=footer('43','Javanese','A','Script')
    return g+close_svg()

def build_43b():
    g=open_svg()
    g+=t(240,32,'JAVANESE','middle','T')
    g+=t(240,50,'Phonology \u2014 Sounds and Register Variation','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    cons=[('p /p/','bilabial stop vl'),('b /b/','bilabial stop vd'),
          ('t /t/','alveolar stop'),('d /d/','alveolar stop vd'),
          ('th /t\u032a/','apical dental stop'),('dh /d\u032a/','apical dental vd'),
          ('k /k/','velar stop'),('g /\u0261/','velar stop vd'),
          ('c /t\u0255/','palatal affricate'),('j /d\u0292/','palatal affricate vd'),
          ('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),
          ('ny /\u0272/','palatal nasal'),('ng /\u014b/','velar nasal'),
          ('l /l/','lateral'),('r /r/','trill'),('s /s/','alveolar fricative'),
          ('h /h/','glottal'),('w /w/','labio-velar'),('y /j/','palatal approx')]
    for i,(c,desc) in enumerate(cons):
        col=i%2; row=i//2
        x=80+col*200; y=82+row*10
        g+=t(x,y,f'{c} {desc}','middle','Lx')
    g+=hr(192)
    g+=sh(201,'APICAL VS. LAMINAL DISTINCTION')
    g+=t(240,211,'Javanese (like Sanskrit-derived Indic languages) distinguishes:','middle','Ls')
    g+=t(240,221,'T/D (laminal dental): t (/t\u032a/), d (/d\u032a/) — tongue blade to upper teeth.','middle','Ls')
    g+=t(240,231,'TH/DH (retroflex-like): th (/\u0288/), dh (/\u0256/) — tongue tip curled back.','middle','Ls')
    g+=t(240,241,'In Latin spelling: t = dental, th = retroflex. Contrast: tahu (tofu) vs. thahu (know).','middle','Ls')
    g+=hr(249)
    g+=sh(258,'VOWEL SYSTEM')
    g+=t(240,268,'6 vowels; /a/ (orthographic) = /\u0254/ (open-back) in many environments.','middle','Ls')
    g+=t(240,278,'Vowel /e/ = /\u025b/ in open syllables, /\u0259/ in closed syllables (context-conditioned).','middle','Ls')
    g+=t(240,288,'No tonal system; stress: generally penultimate syllable.','middle','Ls')
    g+=hr(296)
    g+=sh(305,'PHONOLOGICAL REGISTER DIFFERENCES')
    g+=t(240,315,'Krama register uses entirely different roots (not just affixes):','middle','Ls')
    g+=t(240,325,'Ngoko mangan /mang\u0254\u014b/ (eat) vs. Krama dhahar /d\u02b0ahar/ (eat honorific).','middle','Ls')
    g+=t(240,335,'Register shift requires knowing two distinct lexicons simultaneously.','middle','Ls')
    g+=hr(343)
    g+=sh(352,'BORROWED PHONOLOGY')
    g+=t(240,362,'Sanskrit loanwords: guru, karma, dharma, yoga (via Old Javanese).','middle','Ls')
    g+=t(240,372,'Arabic/Islamic loanwords: salam, doa (prayer), kitab (book), waktu (time).','middle','Ls')
    g+=t(240,382,'Dutch and Malay loanwords significant in modern vocabulary.','middle','Ls')
    g+=footer('43','Javanese','B','Phonology')
    return g+close_svg()

def build_43c():
    g=open_svg()
    g+=t(240,32,'JAVANESE','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SVO')
    g+=t(240,82,'Javanese is SVO. Affixes (prefixes, suffixes, circumfixes) on verbs and nouns.','middle','Ls')
    g+=t(240,92,'Aku mangan sega. I eat rice. (Ngoko register)','middle','Ls')
    g+=t(240,102,'Kula nedha sekul. I eat rice. (Krama register \u2014 same meaning, different words)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'VERB MORPHOLOGY')
    g+=t(240,129,'Active voice: N- prefix (nasal) + root: mangan (eat) < N+pangan.','middle','Ls')
    g+=t(240,139,'Passive: di- prefix + root: dipangan (was eaten).','middle','Ls')
    g+=t(240,149,'Ke- + root: kepangan (accidentally eaten).','middle','Ls')
    g+=t(240,159,'Reduplication: turu-turu = keep sleeping / sleep repeatedly.','middle','Ls')
    g+=hr(167)
    g+=sh(176,'AFFIXES')
    affixes=[('N- (active)','nasal assimilation: nulis (write) < N+tulis'),
             ('di- (passive)','ditulis (was written)'),
             ('-ake (causative/benefactive)','nulis-ake (write for someone)'),
             ('-i (local applicative)','nulis-i (write on)'),
             ('ke- (accidental)','kepangan (accidentally eaten)'),
             ('paN- (nominaliser)','panulisan (writing, act of)')]
    for i,(a,desc) in enumerate(affixes):
        y=186+i*10
        g+=t(120,y,a,'middle','Ls'); g+=t(320,y,desc,'middle','Lx')
    g+=hr(252)
    g+=sh(261,'CORE VOCABULARY (NGOKO / KRAMA)')
    vocab=[('aku / kula','I'),('kowe / sampeyan','you'),('dheweke / piyambake','he/she'),
           ('kita / kula panjenengan','we'),('mangan / dhahar','eat'),
           ('turu / sare','sleep'),('lunga / kesah','go'),('teka / rawuh','come'),
           ('omah / griya','house'),('banyu / toya','water'),('geni / latu','fire'),
           ('lemah / siti','earth'),('wong / tiyang','person'),('wektu / wanci','time'),
           ('rembulan / wulan','moon'),('lintang / sato','star'),
           ('ati / manah','heart'),('tresna / sih','love'),
           ('merdeka','freedom'),('eling / emut','remember'),
           ('sesuk / mbenjang','tomorrow / future'),('donya / jagad','world'),
           ('urip / gesang','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=271+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('43','Javanese','C','Grammar')
    return g+close_svg()

def build_43d():
    g=open_svg()
    g+=t(240,32,'JAVANESE','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. PARIBASAN \u2014 PROVERB')
    g+=t(240,80,'Becik ketitik, ala ketara.','middle','L')
    g+=t(240,90,'becik=good ketitik=will-show ala=bad ketara=will-appear','middle','Ls')
    g+=t(240,100,'"Good will show itself; evil will become apparent." (Javanese proverb on truth)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. ELING \u2014 ON MEMORY')
    g+=t(240,128,'Sing eling marang leluhure, dheweke bakal bisa ngerti lakune urip.','middle','L')
    g+=t(240,138,'sing=who eling=remembers marang=toward leluhure=their-ancestors','middle','Ls')
    g+=t(240,148,'dheweke=they bakal=will bisa=be-able ngerti=understand lakune=path urip=life','middle','Ls')
    g+=t(240,158,'"One who remembers their ancestors will be able to understand the path of life."','middle','F')
    g+=hr(167)
    g+=sh(176,'III. KAWRUH \u2014 ON KNOWLEDGE')
    g+=t(240,186,'Ilmu iku kelakone kanthi laku.','middle','L')
    g+=t(240,196,'ilmu=knowledge/science iku=that kelakone=is-accomplished kanthi=through laku=practice/conduct','middle','Ls')
    g+=t(240,206,'"Knowledge is achieved through practice." (Javanese Wulang Reh wisdom)','middle','F')
    g+=hr(215)
    g+=sh(224,'IV. MAJU \u2014 FORWARD')
    g+=t(240,234,'Kita mlaku maju kanthi nggawa eling marang leluhur.','middle','L')
    g+=t(240,244,'kita=we mlaku=walk maju=forward kanthi=with nggawa=carrying','middle','Ls')
    g+=t(240,254,'eling=remembrance marang=toward leluhur=ancestors','middle','Ls')
    g+=t(240,264,'"We walk forward carrying remembrance of the ancestors." (guiding principle)','middle','F')
    g+=hr(273)
    g+=sh(282,'V. BRIDGE PHRASE')
    g+=t(240,294,'Barang iki digawe kanggo kowe, kanthi gratis,','middle','L')
    g+=t(240,304,'dening wong-wong kang eling marang masa ngarep.','middle','L')
    g+=t(240,318,'barang-iki=this-thing digawe=was-made kanggo=for kowe=you','middle','Ls')
    g+=t(240,327,'kanthi-gratis=freely (without cost) dening=by wong-wong=people','middle','Ls')
    g+=t(240,336,'kang=who eling=remember marang=toward masa-ngarep=the-future / forward','middle','Ls')
    g+=t(240,348,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(359)
    g+=sh(368,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,378,'Masa ngarep = "the forward time" = future. Ngarep (Ngoko) = "in front / forward."','middle','Ls')
    g+=t(240,388,'Eling marang masa ngarep = "remember toward the future" \u2014 forward-facing memory.','middle','Ls')
    g+=t(240,398,'Gratis = free of charge (Dutch loanword, via colonial-era Malay).','middle','Ls')
    g+=t(240,408,'Note: Krama equivalent would use "wekdal ngajeng" (formal "forward time").','middle','Ls')
    g+=hr(416)
    g+=sh(425,'LANGUAGE NOTES')
    g+=t(240,435,'Javanese: ~82 million speakers; most-spoken language of Indonesia (Java, Bali, diaspora).','middle','Ls')
    g+=t(240,445,'Language family: Austronesian, Malayo-Polynesian, Javanese-Madurese.','middle','Ls')
    g+=t(240,455,'Rich literary tradition: Kakawin (Sanskrit-Javanese court poetry), Babad (chronicles).','middle','Ls')
    g+=t(240,465,'Speech levels (Ngoko/Madya/Krama) encode one of world\'s most elaborate social registers.','middle','Ls')
    g+=footer('43','Javanese','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate43a_javanese_script.svg': build_43a(),
        'plate43b_javanese_phonology.svg': build_43b(),
        'plate43c_javanese_grammar.svg': build_43c(),
        'plate43d_javanese_text.svg': build_43d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
