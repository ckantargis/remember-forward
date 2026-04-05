"""Build script — Quechua series plates 46A–46D (Remember Forward)"""
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

def build_46a():
    g=open_svg()
    g+=t(240,32,'QUECHUA','middle','T')
    g+=t(240,50,'Runasimi \u2014 Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Quechua uses the Latin alphabet. No pre-colonial phonetic script (Inca used quipu).','middle','Ls')
    g+=t(240,94,'Modern standardised orthography (1975, revised 1995): 3 vowels, ~20 consonants.','middle','Ls')
    g+=t(240,104,'Dialects vary; "Quechua" is a dialect continuum of ~8-10 major varieties.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'QUIPU \u2014 KNOTTED RECORDS')
    g+=t(240,131,'Quipu (khipu): knotted string recording system used by Inca Empire for accounting.','middle','Ls')
    g+=t(240,141,'~600 surviving quipus; likely encoded numeric + narrative information.','middle','Ls')
    g+=t(240,151,'NOT a phonetic script but may encode language structure in knot sequences.','middle','Ls')
    g+=t(240,161,'Quipu not yet fully deciphered; represents a non-alphabetic information system.','middle','Ls')
    g+=hr(169)
    g+=sh(178,'ALPHABET \u2014 STANDARD QUECHUA (RUNASIMI)')
    g+=t(240,188,'Vowels: only 3 — a, i, u (no e or o in native words). Spanish loanwords add e/o.','middle','Ls')
    g+=t(240,198,'Standard Quechua uses 3 vowels and ~20 consonants.','middle','Ls')
    cons_text='p  t  ch  k  q  '
    g+=t(240,208,cons_text + 'ph  th  chh  kh  qh','middle','L')
    g+=t(240,218,"p'  t'  ch'  k'  q'  (ejectives)","middle",'L')
    g+=t(240,228,'m  n  ny  ng  s  sh  h  l  ll  r  w  y','middle','L')
    g+=hr(238)
    g+=sh(247,'THREE-WAY CONSONANT CONTRAST')
    g+=t(240,257,'Quechua has a unique 3-way stop contrast (unlike 2-way in most languages):','middle','Ls')
    g+=t(240,267,'PLAIN: p, t, ch, k, q (simple stops)','middle','Ls')
    g+=t(240,277,'ASPIRATED: ph, th, chh, kh, qh (puff of air after release)','middle','Ls')
    g+=t(240,287,"EJECTIVE: p', t', ch', k', q' (glottalic egressive, sharp release)","middle",'Ls')
    g+=t(240,297,"Example: papa (potato) vs. p'apa (peeled) vs. phapa (flat/bland).",'middle','Ls')
    g+=hr(305)
    g+=sh(314,'UVULAR Q AND RETROFLEX LL')
    g+=t(240,324,'Q /q/: uvular stop (back of mouth, beyond velar). ','middle','Ls')
    g+=t(240,334,'    Qh /q\u02b0/ (aspirated), Q\' /q\u02bc/ (ejective). Key distinction from K.','middle','Ls')
    g+=t(240,344,'LL /\u028e/: palatal lateral. Varies by dialect: some dialects = /j/ or /\u029e\u032a/.','middle','Ls')
    g+=t(240,354,'NY /\u0272/: palatal nasal, like Spanish \u00f1.','middle','Ls')
    g+=hr(362)
    g+=sh(371,'QUECHUA NUMERALS')
    nums=[('1','huk'),('2','iskay'),('3','kimsa'),('4','tawa'),('5','pichqa'),
          ('6','suqta'),('7','qanchis'),('8','pusaq'),('9','isqun'),('10','chunka')]
    for i,(n,w) in enumerate(nums):
        col=i%5; row=i//5
        x=55+col*78; y=381+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,401,'20 = iskay chunka · 100 = pachak · 1000 = waranqa · 10000 = chunka waranqa','middle','Ls')
    g+=hr(409)
    g+=sh(418,'SCRIPT HISTORY AND DIALECTS')
    g+=t(240,428,'Quechua spread with the Inca Empire (~1438-1533 CE) from Cuzco, Peru.','middle','Ls')
    g+=t(240,438,'After Spanish conquest, Latin alphabet adopted. Quechua first written ~1560.','middle','Ls')
    g+=t(240,448,'Major varieties: Cuzco-Collao, Ancash, Ayacucho, Ecuadorian (Kichwa), Bolivian.','middle','Ls')
    g+=t(240,458,'~8-10 million speakers in Peru, Bolivia, Ecuador, Colombia, Argentina.','middle','Ls')
    g+=footer('46','Quechua','A','Script')
    return g+close_svg()

def build_46b():
    g=open_svg()
    g+=t(240,32,'QUECHUA','middle','T')
    g+=t(240,50,'Phonology \u2014 Ejectives, Aspirates, Uvulars','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY \u2014 CUZCO QUECHUA')
    g+=t(240,82,'Cuzco Quechua: ~35 consonants with 3-way stop contrast at 5 places of articulation.','middle','Ls')
    stops=[('Place','Plain','Aspirated','Ejective'),
           ('Bilabial','p /p/','ph /p\u02b0/','p\' /p\u02bc/'),
           ('Alveolar','t /t/','th /t\u02b0/','t\' /t\u02bc/'),
           ('Palatal','ch /t\u0255/','chh /t\u0255\u02b0/','ch\' /t\u0255\u02bc/'),
           ('Velar','k /k/','kh /k\u02b0/','k\' /k\u02bc/'),
           ('Uvular','q /q/','qh /q\u02b0/','q\' /q\u02bc/')]
    for i,(place,plain,asp,ej) in enumerate(stops):
        y=92+i*11
        c='Ls' if i>0 else 'Lx'
        g+=t(60,y,place,'middle',c); g+=t(180,y,plain,'middle',c)
        g+=t(290,y,asp,'middle',c); g+=t(400,y,ej,'middle',c)
    g+=hr(163)
    g+=sh(172,'FRICATIVES AND NASALS')
    others=[('s /s/','alveolar fric'),('sh /\u0283/','postalveolar'),('h /h/','glottal'),
            ('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),('ny /\u0272/','palatal nasal'),
            ('ng /\u014b/','velar nasal'),('l /l/','lateral'),('ll /\u028e/','palatal lateral'),
            ('r /r/','trill'),('w /w/','labio-velar'),('y /j/','palatal approx')]
    for i,(c,desc) in enumerate(others):
        col=i%3; row=i//3
        x=65+col*130; y=182+row*10
        g+=t(x,y,f'{c} {desc}','middle','Lx')
    g+=hr(232)
    g+=sh(241,'VOWEL SYSTEM \u2014 3 VOWELS')
    g+=t(240,251,'Native Quechua has only 3 phonemic vowels: /a/, /i/, /u/.','middle','Ls')
    g+=t(240,261,'Adjacent to uvular Q, vowels lower: /i/\u2192[\u025b], /u/\u2192[\u0254], /a/\u2192[a\u02d0].','middle','Ls')
    g+=t(240,271,'Written "e" and "o" appear next to q: qiwa [q\u025bwa] (grass), qucha [q\u0254t\u0255a] (lake).','middle','Ls')
    g+=t(240,281,'Spanish loanwords introduce /e/ and /o/ as distinct phonemes.','middle','Ls')
    g+=hr(289)
    g+=sh(298,'EJECTIVE CONSONANTS \u2014 PHONETIC DETAIL')
    g+=t(240,308,'Ejectives (/p\u02bc/, /t\u02bc/, etc.): produced by closing both glottis and oral stop simultaneously,','middle','Ls')
    g+=t(240,318,'then releasing oral closure first. Creates a sharp, plosive click-like quality.','middle','Ls')
    g+=t(240,328,'Found in Quechua, Aymara, Caucasian languages, some African languages.','middle','Ls')
    g+=t(240,338,'Not in English or European languages; notable learning challenge.','middle','Ls')
    g+=hr(346)
    g+=sh(355,'STRESS AND SYLLABLE STRUCTURE')
    g+=t(240,365,'Stress: penultimate syllable in most words. No tone.','middle','Ls')
    g+=t(240,375,'Syllable: (C)(C)V(C). Consonant clusters rare; V = a, i, or u primarily.','middle','Ls')
    g+=t(240,385,'Vowel length contrastive in some dialects (Ancash Quechua).','middle','Ls')
    g+=footer('46','Quechua','B','Phonology')
    return g+close_svg()

def build_46c():
    g=open_svg()
    g+=t(240,32,'QUECHUA','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SOV, AGGLUTINATIVE')
    g+=t(240,82,'Quechua is SOV and highly agglutinative. Long words are built by chaining suffixes.','middle','Ls')
    g+=t(240,92,'Noqa mikuni. I eat. (noqa=I miku=eat -ni=1sg present)','middle','Ls')
    g+=t(240,102,'Noqa mikhunita munani. I want to eat. (mikhu-ni-ta=eating-OBJ muna-ni=want-1sg)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'CASE SUFFIXES')
    cases=[('-ta','accusative/object: runtuta mikuni (I eat an egg)'),
           ('-man','dative/allative: Limaman rini (I go to Lima)'),
           ('-pi','locative: wasapi (in the house)'),
           ('-manta','ablative: wasaymanta (from the house)'),
           ('-pa / -q','genitive: wasaypa (of the house)'),
           ('-wan','comitative: paywan (with him/her)'),
           ('-kama','terminative: Limaykama (as far as Lima)')]
    for i,(sfx,gloss) in enumerate(cases):
        y=129+i*10
        g+=t(90,y,sfx,'middle','Ls'); g+=t(290,y,gloss,'middle','Lx')
    g+=hr(205)
    g+=sh(214,'VERB MORPHOLOGY')
    g+=t(240,224,'Verb suffixes encode tense, aspect, person, evidentiality, direction:','middle','Ls')
    verbs=[('miku-ni','I eat (present 1sg)'),('miku-nki','you eat (present 2sg)'),
           ('miku-n','he/she eats (present 3sg)'),('miku-rqa-ni','I ate (past 1sg)'),
           ('miku-sqa-ni','I ate (evidential past)'),('miku-nqa-ni','I will eat (future 1sg)'),
           ('miku-sha-ni','I am eating (progressive)'),('mana miku-ni-chu','I don\'t eat (neg)')]
    for i,(form,gloss) in enumerate(verbs):
        y=234+i*10
        g+=t(130,y,form,'middle','L'); g+=t(320,y,gloss,'middle','Ls')
    g+=hr(325)
    g+=sh(334,'EVIDENTIALITY \u2014 UNIQUE FEATURE')
    g+=t(240,344,'Quechua grammatically marks how the speaker knows what they say (evidentiality):','middle','Ls')
    g+=t(240,354,'-mi/-m: direct evidence (I saw it myself)','middle','Ls')
    g+=t(240,364,'-si/-s: reported speech (I heard that...)','middle','Ls')
    g+=t(240,374,'-chi: conjectural (I suppose/infer that...)','middle','Ls')
    g+=t(240,384,'Example: Paymi hamun = He is coming (I see him). Paysi hamun = He is coming (I was told).','middle','Lx')
    g+=hr(392)
    g+=sh(401,'CORE VOCABULARY')
    vocab=[('allianchu?','hello/how are you?'),('allinim','I am fine'),
           ('sulpayki','thank you'),('ari','yes'),('mana','no'),
           ('noqa','I'),('qam','you'),('pay','he/she/it'),
           ('unu / yaku','water'),('nina','fire'),('allpa','earth/soil'),
           ('runa','person/human'),('pacha','time/world/universe'),
           ('killa','moon'),('ch\'aska','star/Venus'),('sunqu','heart'),
           ('munay','love'),('qispiy','freedom'),('yuyay','memory/thought'),
           ('qhipa','behind / future'),('kay pacha','this world'),('kawsay','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<11 else 1
        y=411+(i if i<11 else i-11)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('46','Quechua','C','Grammar')
    return g+close_svg()

def build_46d():
    g=open_svg()
    g+=t(240,32,'QUECHUA','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. RIMAY \u2014 PROVERB')
    g+=t(240,80,'Ama suwa, ama llulla, ama qhilla.','middle','L')
    g+=t(240,90,'ama=do-not suwa=steal llulla=lie qhilla=be-lazy','middle','Ls')
    g+=t(240,100,'"Do not steal, do not lie, do not be lazy." (Inca moral code; Quechua ethical triad)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. YUYAY \u2014 ON MEMORY')
    g+=t(240,128,'Nawpa machulanchis yuyayninta qhawaspa, kay pachapi kawsanchis.','middle','L')
    g+=t(240,138,'nawpa=before machulanchis=our-ancestors yuyayninta=their-memory qhawaspa=looking-at','middle','Ls')
    g+=t(240,148,'kay-pachapi=in-this-world kawsanchis=we-live','middle','Ls')
    g+=t(240,158,'"Looking at the memory of our ancestors, we live in this world."','middle','F')
    g+=hr(167)
    g+=sh(176,'III. YACHAY \u2014 ON KNOWLEDGE')
    g+=t(240,186,'Yachay mana tukukunchu; runakunap sunqunpi kawsan.','middle','L')
    g+=t(240,196,'yachay=knowledge mana=not tukukunchu=ends-not runakunap=of-people sunqunpi=in-their-heart kawsan=lives','middle','Lx')
    g+=t(240,206,'"Knowledge does not end; it lives in the hearts of people."','middle','F')
    g+=hr(215)
    g+=sh(224,'IV. QHIPA \u2014 FORWARD / FUTURE')
    g+=t(240,234,'Qhipaman purishanchis, nawpaq machulanchis yuyayninta apashpa.','middle','L')
    g+=t(240,244,'qhipaman=toward-the-future / ahead purishanchis=we-walk','middle','Ls')
    g+=t(240,254,'nawpaq=our-ancient machulanchis=ancestors yuyayninta=their-memory apashpa=carrying','middle','Ls')
    g+=t(240,264,'"We walk toward the future, carrying the memory of our ancestors."','middle','F')
    g+=hr(273)
    g+=sh(282,'V. BRIDGE PHRASE')
    g+=t(240,294,'Kay imata qampaq ruwarqanchis, mana qullqiyuqta,','middle','L')
    g+=t(240,304,'qhipaman yuyariq runakunam.','middle','L')
    g+=t(240,318,'kay-imata=this-thing qampaq=for-you ruwarqanchis=we-made mana-qullqiyuqta=without-cost','middle','Ls')
    g+=t(240,327,'qhipaman=toward-the-future yuyariq=remembering runakuna-m=people (evidential -m)','middle','Ls')
    g+=t(240,339,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(350)
    g+=sh(359,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,369,'Qhipa = "behind / the future." In Quechua spatial metaphor the PAST is in FRONT','middle','Ls')
    g+=t(240,379,'(you can see it) and the FUTURE is BEHIND (you cannot see it). Qhipaman =','middle','Ls')
    g+=t(240,389,'"toward the future / toward what is behind." This is the reverse of English.','middle','Ls')
    g+=t(240,399,'The suffix -m (evidential) marks "I know this directly." A true patient message.','middle','Ls')
    g+=hr(407)
    g+=sh(416,'LANGUAGE NOTES')
    g+=t(240,426,'Quechua (Runasimi): ~8-10 million speakers in Peru, Bolivia, Ecuador, Colombia.','middle','Ls')
    g+=t(240,436,'Language family: Quechuan (isolate family, not related to other known families).','middle','Ls')
    g+=t(240,446,'Lingua franca of the Inca Empire (~1438-1533). Survives as living language today.','middle','Ls')
    g+=t(240,456,'Words borrowed into English: llama, condor, quinoa, puma, coca, guano.','middle','Ls')
    g+=footer('46','Quechua','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate46a_quechua_script.svg': build_46a(),
        'plate46b_quechua_phonology.svg': build_46b(),
        'plate46c_quechua_grammar.svg': build_46c(),
        'plate46d_quechua_text.svg': build_46d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
