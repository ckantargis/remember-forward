"""Build script — Zulu series plates 37A–37D (Remember Forward)"""
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

# ─── PLATE 37A — SCRIPT ────────────────────────────────────────────────────
def build_37a():
    g=open_svg()
    g+=t(240,32,'ZULU','middle','T')
    g+=t(240,50,'Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Zulu uses the Latin alphabet. Standard orthography developed in 19th century','middle','Ls')
    g+=t(240,93,'by missionaries; codified in modern form during the 20th century.','middle','Ls')
    g+=t(240,102,'26 standard letters plus digraphs. Tone is not marked in standard writing.','middle','Ls')
    g+=hr(110)
    g+=sh(119,'ZULU ALPHABET AND DIGRAPHS')
    letters=[('A a','/a/'),('B b','/b/'),('C c','/\u01c2/ dental click'),
             ('D d','/d/'),('E e','/\u025b/'),('F f','/f/'),('G g','/\u0261/'),
             ('H h','/h/'),('I i','/i/'),('J j','/d\u0292/'),('K k','/k/'),
             ('L l','/l/'),('M m','/m/'),('N n','/n/'),('O o','/\u0254/'),
             ('P p','/p/'),('Q q','/\u0285/ palato-alveolar click'),('R r','/r/'),
             ('S s','/s/'),('T t','/t/'),('U u','/u/'),('V v','/v/'),
             ('W w','/w/'),('X x','/\u01a1/ lateral click'),('Y y','/j/'),('Z z','/z/'),
             ('sh','/\u0283/'),('ng','/\u014b/'),('ny','/\u0272/'),
             ('dl','/\u026c/'),('hl','/\u026c/ voiceless lateral')]
    for i,(letter,ipa) in enumerate(letters):
        col=i%4; row=i//4
        x=60+col*95; y=129+row*10
        g+=t(x,y,f'{letter} {ipa}','middle','Lx')
    g+=hr(225)
    g+=sh(234,'CLICK CONSONANTS — DEFINING FEATURE')
    g+=t(240,244,'Zulu has 3 click types inherited from Khoisan neighbours (contact languages).','middle','Ls')
    g+=t(240,253,'C /\u01c2/ DENTAL CLICK: tongue tip against upper teeth, pulled back sharply.','middle','Ls')
    g+=t(240,262,'    Like the English "tsk tsk" disapproval click.','middle','Ls')
    g+=t(240,271,'Q /\u0285/ PALATO-ALVEOLAR CLICK: tongue body against hard palate.','middle','Ls')
    g+=t(240,280,'    Produces a loud "pop." Hard palate click.','middle','Ls')
    g+=t(240,289,'X /\u01a1/ LATERAL CLICK: sides of tongue against upper molars.','middle','Ls')
    g+=t(240,298,'    Like the horse-urging click made by riders.','middle','Ls')
    g+=t(240,307,'Each click has voiced (gc-, nc-, gc-), aspirated (ch-, qh-, xh-) and nasal variants.','middle','Ls')
    g+=hr(315)
    g+=sh(324,'PREFIXED CLICK VARIANTS')
    clicks=[('c','basic dental'),('gc','voiced dental'),('ch','aspirated dental'),('nc','nasal dental'),
            ('ngc','nasalised voiced dental'),('q','palato-alveolar'),('gq','voiced palato'),
            ('qh','aspirated palato'),('nq','nasal palato'),('x','lateral'),
            ('gx','voiced lateral'),('xh','aspirated lateral'),('nx','nasal lateral')]
    for i,(c,desc) in enumerate(clicks):
        col=i%3; row=i//3
        x=80+col*130; y=334+row*10
        g+=t(x,y,f'{c}: {desc}','middle','Lx')
    g+=hr(385)
    g+=sh(394,'NUMERALS')
    nums=[('1','kunye'),('2','kubili'),('3','kuthathu'),('4','kune'),('5','kuhlanu'),
          ('6','isithupha'),('7','isikhombisa'),('8','isishiyagalombili'),
          ('9','isishiyagalolunye'),('10','ishumi')]
    for i,(n,w) in enumerate(nums):
        col=i%2; row=i//2
        x=100+col*200; y=404+row*10
        g+=t(x,y,f'{n} = {w}','middle','Lx')
    g+=t(240,460,'20 = amashumi amabili · 100 = ikhulu · 1000 = inkulungwane','middle','Ls')
    g+=footer('37','Zulu','A','Script')
    return g+close_svg()

# ─── PLATE 37B — PHONOLOGY ─────────────────────────────────────────────────
def build_37b():
    g=open_svg()
    g+=t(240,32,'ZULU','middle','T')
    g+=t(240,50,'Phonology & Sound System','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    g+=t(240,82,'Zulu has ~50+ consonants when click variants are included.','middle','Ls')
    g+=t(240,91,'Core non-click consonants shown; click series add ~15 more segments.','middle','Ls')
    cons=[('p','/p/ bilabial stop vl'),('b','/b/ bilabial stop vd'),
          ('t','/t/ alveolar stop vl'),('d','/d/ alveolar stop vd'),
          ('k','/k/ velar stop vl'),('g','/\u0261/ velar stop vd'),
          ('ph','/p\u02b0/ aspirated bilabial'),('th','/t\u02b0/ aspirated alveolar'),
          ('kh','/k\u02b0/ aspirated velar'),('f','/f/ labiodental'),('v','/v/ labiodental vd'),
          ('s','/s/ alveolar fricative'),('z','/z/ alveolar fricative vd'),
          ('sh','/\u0283/ postalveolar'),('hl','/\u026c/ lateral fricative vl'),
          ('dl','/\u026c/ lateral fricative vd'),('h','/h/ glottal'),
          ('m','/m/ bilabial nasal'),('n','/n/ alveolar nasal'),
          ('ng','/\u014b/ velar nasal'),('ny','/\u0272/ palatal nasal'),
          ('l','/l/ lateral'),('r','/r/ trill'),('w','/w/ labio-velar'),('y','/j/ palatal')]
    for i,(c,desc) in enumerate(cons):
        col=0 if i<13 else 1
        y=101+(i if i<13 else i-13)*11
        g+=t(60+col*220,y,c,'middle','Ls'); g+=t(140+col*220,y,desc,'middle','Lx')
    g+=hr(252)
    g+=sh(261,'VOWEL SYSTEM — 5 VOWELS')
    vowels=[('a','/a/','open central: amanzi (water)'),('e','/\u025b/','mid-front: ikhaya (home)'),
            ('i','/i/','high front: izinto (things)'),('o','/\u0254/','mid-back: umuntu (person)'),
            ('u','/u/','high back: ubuntu (humanity)')]
    for i,(v,ipa,ex) in enumerate(vowels):
        y=271+i*11
        g+=t(50,y,v,'middle','L'); g+=t(110,y,ipa,'middle','Ls'); g+=t(310,y,ex,'middle','Lx')
    g+=hr(330)
    g+=sh(339,'TONE SYSTEM')
    g+=t(240,349,'Zulu has two tones: High (H) and Low (L). Tone is phonemic.','middle','Ls')
    g+=t(240,359,'Tone not written in standard orthography; context and knowledge required.','middle','Ls')
    g+=t(240,369,'ukufa (L L L) = to die / ukufa (H L L) = to arrive at.','middle','Ls')
    g+=t(240,379,'Downstep (!H) occurs after a low tone: hi!H sequences.','middle','Ls')
    g+=hr(387)
    g+=sh(396,'CLICK PHONOLOGY IN CONTEXT')
    g+=t(240,406,'Clicks in Zulu are full consonants, inherited ~1,000+ years ago from contact with','middle','Ls')
    g+=t(240,416,'Khoisan speakers. They occur in native vocabulary and borrowed words.','middle','Ls')
    g+=t(240,426,'ucingo (dental nc-) = telephone. ukucula (dental c-) = to sing.','middle','Ls')
    g+=t(240,436,'Clicks combine with tone, nasality, aspiration = large segment inventory.','middle','Ls')
    g+=hr(444)
    g+=sh(453,'ASPIRATION AND VOICED/VOICELESS PAIRS')
    g+=t(240,463,'Zulu distinguishes plain, aspirated, and voiced stops: p/ph/b, t/th/d, k/kh/g.','middle','Ls')
    g+=t(240,473,'Aspirated stops: phuza (drink), thanda (love), khuluma (speak).','middle','Ls')
    g+=t(240,483,'HL /\u026c/ voiceless lateral fricative: hlala (sit/stay), hlobo (type/season).','middle','Ls')
    g+=footer('37','Zulu','B','Phonology')
    return g+close_svg()

# ─── PLATE 37C — GRAMMAR ───────────────────────────────────────────────────
def build_37c():
    g=open_svg()
    g+=t(240,32,'ZULU','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE — SVO + AGGLUTINATION')
    g+=t(240,82,'Zulu is Subject-Verb-Object. Extensive agglutination on verbs.','middle','Ls')
    g+=t(240,92,'Umuntu udla ukudla. umuntu=person u-dla=3SG.eat ukudla=food = "The person eats food."','middle','Ls')
    g+=hr(100)
    g+=sh(109,'NOUN CLASS SYSTEM — 17 CLASSES')
    g+=t(240,119,'All Zulu nouns belong to a class marked by prefix. Agreement spreads to verbs, adjectives.','middle','Ls')
    classes=[('umu-/aba-','Class 1/2: persons — umuntu (person) / abantu (people)'),
             ('umu-/imi-','Class 3/4: trees — umuthi (medicine/tree) / imithi'),
             ('ili-/ama-','Class 5/6: general — ilanga (sun/day) / amalanga'),
             ('isi-/izi-','Class 7/8: things — isifundo (lesson) / izifundo'),
             ('in-/izin-','Class 9/10: animals/things — inkosi (chief) / izinkosi'),
             ('u-/izin-','Class 11/10: abstract — ubuntu (humanity)'),
             ('ubu-/—','Class 14: abstract mass — ubukhosi (royalty)'),
             ('uku-/—','Class 15: verbal nouns — ukuthanda (to love)')]
    for i,(prefix,example) in enumerate(classes):
        y=129+i*11
        g+=t(90,y,prefix,'middle','Ls'); g+=t(320,y,example,'middle','Lx')
    g+=hr(225)
    g+=sh(234,'VERB MORPHOLOGY')
    g+=t(240,244,'Template: Subject concord + Tense/Aspect + Object concord + Root + Extension + Final.','middle','Ls')
    verbs=[('ngiyathanda','I love (ngi-ya-thanda)'),('uthanda','he/she loves (u-thanda)'),
           ('ngathanda','I loved (past)'),('ngizothanda','I will love (ngi-zo-thanda)'),
           ('ngiyamthanda','I love him/her (obj concord -m-)'),
           ('angithandi','I don\'t love (a-ngi-thandi, negative final -i)'),
           ('thanda!','love! (imperative)'),('ngithande','let me love (subjunctive)')]
    for i,(form,gloss) in enumerate(verbs):
        y=254+i*10
        g+=t(140,y,form,'middle','L'); g+=t(330,y,gloss,'middle','Ls')
    g+=hr(342)
    g+=sh(351,'UBUNTU — KEY CULTURAL CONCEPT')
    g+=t(240,361,'"Umuntu ngumuntu ngabantu" — A person is a person through other people.','middle','Ls')
    g+=t(240,371,'Ubuntu = humanity/humanness: the philosophy that identity is relational.','middle','Ls')
    g+=t(240,381,'Central to Zulu (and broader Nguni/Bantu) ethics and community life.','middle','Ls')
    g+=hr(389)
    g+=sh(398,'CORE VOCABULARY')
    vocab=[('sawubona','hello (I see you)'),('siyabonga','thank you'),('yebo','yes'),
           ('cha','no'),('ngicela','please'),('unjani?','how are you?'),
           ('ngiyaphila','I am well'),('ngiyakuthanda','I love you'),
           ('igama lami','my name is...'),('amanzi','water'),('umlilo','fire'),
           ('umhlaba','earth/world'),('umuntu','person'),('isikhathi','time'),
           ('inyanga','moon'),('inkanyezi','star'),('inhliziyo','heart'),
           ('uthando','love'),('inkululeko','freedom'),('ukukhumbula','to remember'),
           ('kusasa','tomorrow / future'),('ubuntu','humanity / togetherness'),
           ('impilo','life'),('amandla','power/strength'),('isizwe','nation/people')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<13 else 1
        y=408+(i if i<13 else i-13)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('37','Zulu','C','Grammar')
    return g+close_svg()

# ─── PLATE 37D — RUNNING TEXT ──────────────────────────────────────────────
def build_37d():
    g=open_svg()
    g+=t(240,32,'ZULU','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. UBUNTU — FOUNDATIONAL PHILOSOPHY')
    g+=t(240,80,'Umuntu ngumuntu ngabantu.','middle','L')
    g+=t(240,90,'umuntu=person ngu=is umuntu=person nga=through abantu=people','middle','Ls')
    g+=t(240,100,'"A person is a person through other people." (Nguni ubuntu proverb)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. UKUKHUMBULA — ON REMEMBERING')
    g+=t(240,128,'Ukukhumbula abadlule kuyisikhungo sokuqhubeka phambili.','middle','L')
    g+=t(240,138,'ukukhumbula=to-remember abadlule=those-who-passed kuyisikhungo=is-the-anchor','middle','Ls')
    g+=t(240,147,'sokuqhubeka=of-going-forward phambili=ahead','middle','Ls')
    g+=t(240,157,'"Remembering those who have passed is the anchor of moving forward." (Zulu saying)','middle','F')
    g+=hr(166)
    g+=sh(175,'III. ULWAZI — ON KNOWLEDGE')
    g+=t(240,185,'Ulwazi alupheleli mntwini munye; ludluliselwa kwabalandela.','middle','L')
    g+=t(240,195,'ulwazi=knowledge alupheleli=does-not-end-with mntwini-munye=one-person','middle','Ls')
    g+=t(240,205,'ludluliselwa=is-passed-on kwabalandela=to-those-who-follow','middle','Ls')
    g+=t(240,215,'"Knowledge does not end with one person; it is passed on to those who follow."','middle','F')
    g+=hr(224)
    g+=sh(233,'IV. PHAMBILI — FORWARD')
    g+=t(240,243,'Siyahamba phambili sikhumbula izinyanya.','middle','L')
    g+=t(240,253,'siyahamba=we-walk phambili=forward sikhumbula=we-remember izinyanya=ancestors','middle','Ls')
    g+=t(240,263,'"We walk forward remembering the ancestors." (ancestral continuity)','middle','F')
    g+=hr(272)
    g+=sh(281,'V. BRIDGE PHRASE')
    g+=t(240,294,'Lesi sinto senziwa ngawe, mahhala, ngabantu abakhumbula phambili.','middle','L')
    g+=t(240,308,'lesi-sinto=this-thing senziwa=was-made ngawe=for-you mahhala=freely (without cost)','middle','Ls')
    g+=t(240,317,'ngabantu=by-people abakhumbula=who-remember phambili=forward / ahead','middle','Ls')
    g+=t(240,329,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(340)
    g+=sh(349,'BRIDGE PHRASE — NOTES')
    g+=t(240,359,'Phambili (from Proto-Bantu *-pamba) = "forward / ahead / in front."','middle','Ls')
    g+=t(240,369,'Abakhumbula phambili = "those who remember forward" — honouring ancestors','middle','Ls')
    g+=t(240,379,'while facing forward. In Zulu thought the future is built on ancestral memory.','middle','Ls')
    g+=t(240,389,'Mahhala = free/gratis (from Afrikaans/Dutch gratis, via South African contact).','middle','Ls')
    g+=t(240,399,'Sawubona (I see you) / Siyabona (we see you) — greeting acknowledges personhood.','middle','Ls')
    g+=hr(407)
    g+=sh(416,'LANGUAGE NOTES')
    g+=t(240,426,'Zulu: ~13 million L1 speakers; South Africa\'s most widely spoken home language.','middle','Ls')
    g+=t(240,436,'Language family: Bantu, Nguni branch (with Xhosa, Swati, Ndebele).','middle','Ls')
    g+=t(240,446,'Click consonants absorbed from contact with Khoisan peoples over millennia.','middle','Ls')
    g+=t(240,456,'Official language of South Africa; also spoken in Lesotho, Swaziland, Zimbabwe.','middle','Ls')
    g+=footer('37','Zulu','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate37a_zulu_script.svg': build_37a(),
        'plate37b_zulu_phonology.svg': build_37b(),
        'plate37c_zulu_grammar.svg': build_37c(),
        'plate37d_zulu_text.svg': build_37d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
