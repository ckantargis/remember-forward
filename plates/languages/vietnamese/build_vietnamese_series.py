"""Build script — Vietnamese series plates 38A–38D (Remember Forward)"""
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

# ─── PLATE 38A — SCRIPT ────────────────────────────────────────────────────
def build_38a():
    g=open_svg()
    g+=t(240,32,'VIETNAMESE','middle','T')
    g+=t(240,50,'Script \u2014 Ch\u1eef Qu\u1ed1c Ng\u1eef (National Script)','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Vietnamese uses Ch\u1eef Qu\u1ed1c Ng\u1eef, a Latin-based alphabet with diacritics.','middle','Ls')
    g+=t(240,94,'Developed by Portuguese missionaries (17th c.), standardised in French colonial era.','middle','Ls')
    g+=t(240,104,'Two types of diacritics: (1) letter modifiers (shape), (2) tone marks (pitch).','middle','Ls')
    g+=hr(112)
    g+=sh(121,'MODIFIED LETTERS')
    g+=t(240,131,'Each modifier creates a distinct vowel quality:','middle','Ls')
    mods=[('\u00e2 / A\u0302','/\u0250/ — a with circumflex: \u00e2n (grace), b\u00e2y (seven)'),
          ('\u0103 / A\u0306','/\u00e6/ — a with breve: \u0103n (eat), b\u0103m (press)'),
          ('\u00ea / E\u0302','/e/ — e with circumflex: \u00eam (warm), \u0111\u00eam (night)'),
          ('\u00f4 / O\u0302','/o/ — o with circumflex: \u00f4ng (grandfather), c\u00f4 (aunt)'),
          ('\u01a1 / O+','/\u0259/ — o with horn: \u01a1n (debt), tr\u01a1i (sky)'),
          ('\u01b0 / U+','/\u026f/ — u with horn: \u01b0\u1edbc (wish), \u01b0u (wish for)'),
          ('\u0111 / D-','/d/ — d with stroke: \u0111\u00e2y (here), \u0111\u00f3 (that)')]
    for i,(mod,desc) in enumerate(mods):
        y=141+i*10
        g+=t(80,y,mod,'middle','L'); g+=t(300,y,desc,'middle','Lx')
    g+=hr(218)
    g+=sh(227,'SIX TONES \u2014 DIACRITIC MARKS')
    tones=[('a (no mark)','ngang / flat','mid level: a = ah (interjection)'),
           ('\u00e0 (grave)','huy\u1ec1n / falling','low falling: \u00e0 = but, then'),
           ('\u00e1 (acute)','s\u1eafc / rising','high rising: \u00e1 = ah! (exclamation)'),
           ('\u1ea3 (hook)','h\u1ecfi / dipping','mid dipping-rising: h\u1ecfi = to ask'),
           ('\u00e3 (tilde)','ng\u00e3 / broken','high broken/glottalised: ng\u00e3 = to fall'),
           ('\u1ea1 (dot)','n\u1eb7ng / heavy','low glottalised-falling: n\u1eb7ng = heavy')]
    for i,(mark,name,desc) in enumerate(tones):
        y=237+i*11
        g+=t(60,y,mark,'middle','L'); g+=t(140,y,name,'middle','Ls'); g+=t(330,y,desc,'middle','Lx')
    g+=hr(308)
    g+=sh(317,'ALPHABET \u2014 29 LETTERS')
    letters=['A \u00c2 \u0102 B C D \u0110 E \u00ca G H I K L M N O \u00d4 \u01a0 P Q R S T U \u01af V X Y']
    g+=t(240,327,letters[0],'middle','Ls')
    g+=t(240,337,'Note: F, J, W, Z appear only in loanwords. C=/k/, X=/s/, Y=/j/.','middle','Lx')
    g+=hr(345)
    g+=sh(354,'HISTORICAL SCRIPTS')
    g+=t(240,364,'Ch\u1eef N\u00f4m: logographic script based on Chinese characters, used ~10th-19th century.','middle','Ls')
    g+=t(240,373,'Ch\u1eef H\u00e1n: Classical Chinese used for official/literary writing before French era.','middle','Ls')
    g+=t(240,382,'Ch\u1eef Qu\u1ed1c Ng\u1eef became official in 1910 (French mandate), now universal.','middle','Ls')
    g+=hr(390)
    g+=sh(399,'NUMERALS')
    nums=[('0','kh\u00f4ng'),('1','m\u1ed9t'),('2','hai'),('3','ba'),('4','b\u1ed1n'),
          ('5','n\u0103m'),('6','s\u00e1u'),('7','b\u1ea3y'),('8','t\u00e1m'),('9','ch\u00edn'),('10','m\u01b0\u1eddi')]
    for i,(n,w) in enumerate(nums):
        col=i%4; row=i//4
        x=60+col*95; y=409+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,439,'100 = m\u1ed9t tr\u0103m · 1000 = m\u1ed9t ngh\u00ecn · 1,000,000 = m\u1ed9t tri\u1ec7u','middle','Ls')
    g+=footer('38','Vietnamese','A','Script')
    return g+close_svg()

# ─── PLATE 38B — PHONOLOGY ─────────────────────────────────────────────────
def build_38b():
    g=open_svg()
    g+=t(240,32,'VIETNAMESE','middle','T')
    g+=t(240,50,'Phonology \u2014 Six Tones and Consonant System','middle','S')
    g+=hr(60)
    g+=sh(72,'SIX-TONE SYSTEM')
    g+=t(240,82,'Vietnamese (Hanoi dialect) has 6 phonemic tones. Each tone has distinct pitch + contour.','middle','Ls')
    tones=[('Ngang','mid level 33','ma = ghost'),
           ('Huy\u1ec1n','low falling 21','m\u00e0 = but'),
           ('S\u1eafc','high rising 35','m\u00e1 = cheek'),
           ('H\u1ecfi','dipping-rising 312','m\u1ea3 = grave/tomb'),
           ('Ng\u00e3','high broken 35+glottal','m\u00e3 = horse [north dialect]'),
           ('N\u1eb7ng','low glottalised 21+constriction','m\u1ea1 = rice seedling')]
    for i,(name,contour,ex) in enumerate(tones):
        y=92+i*11
        g+=t(80,y,name,'middle','Ls'); g+=t(200,y,contour,'middle','Lx'); g+=t(360,y,ex,'middle','Lx')
    g+=hr(165)
    g+=sh(174,'INITIAL CONSONANTS')
    inits=[('b','/b/'),('c/k/q','/k/'),('ch','/c/ palatal'),('d/gi','/z/ north /j/ south'),
           ('\u0111','/d/ north /j/ south'),('g/gh','/\u0263/'),('h','/h/'),('kh','/x/'),
           ('l','/l/'),('m','/m/'),('n','/n/'),('ng/ngh','/\u014b/'),('nh','/\u0272/'),
           ('p','/p/ rare'),('ph','/f/'),('r','/r/ north /z/ south'),
           ('s','/s/ north /\u0283/ south'),('t','/t/'),('th','/t\u02b0/'),
           ('tr','/t\u0283/ north /t\u0283/ south'),('v','/v/ north /j/ south'),
           ('x','/s/ north /s/ south'),('x','/s/'),('gi','/z/ north /j/ south')]
    for i,(c,ipa) in enumerate(inits):
        col=i%3; row=i//3
        x=65+col*130; y=184+row*10
        g+=t(x,y,f'{c} {ipa}','middle','Lx')
    g+=hr(278)
    g+=sh(287,'FINAL CONSONANTS AND CODAS')
    g+=t(240,297,'Vietnamese allows only limited codas: -c/-ch, -m, -n, -ng/-nh, -p, -t.','middle','Ls')
    g+=t(240,307,'No consonant clusters in onset or coda; syllable structure: (C)(G)V(C)(T).','middle','Ls')
    g+=t(240,317,'Final -c and -ch are unreleased stops (no audible burst).','middle','Ls')
    g+=hr(325)
    g+=sh(334,'VOWEL SYSTEM')
    g+=t(240,344,'14 monophthongs + triphthongs; vowel length not phonemic (tone-conditioned).','middle','Ls')
    vowels=[('a /a/','open front'),('\u0103 /\u00e6/','near-open front'),('\u00e2 /\u0250/','open central'),
            ('e /\u025b/','mid-front'),('\u00ea /e/','close-mid front'),('i /i/','high front'),
            ('o /\u0254/','mid-back'),('\u00f4 /o/','close-mid back'),('\u01a1 /\u0259/','mid central'),
            ('u /u/','high back'),('\u01b0 /\u026f/','high central'),('y /i/','=i in diphthong')]
    for i,(v,desc) in enumerate(vowels):
        col=i%3; row=i//3
        x=65+col*130; y=354+row*10
        g+=t(x,y,f'{v} {desc}','middle','Lx')
    g+=hr(402)
    g+=sh(411,'NORTH vs. SOUTH DIALECT DIFFERENCES')
    g+=t(240,421,'Hanoi (north): 6 tones; d=\u0256, gi=z, s=s, x=s, r=r.','middle','Ls')
    g+=t(240,431,'Saigon/HCMC (south): 5 tones (ng\u00e3=h\u1ecfi merged); d=j, gi=j, s=\u0283, r=z.','middle','Ls')
    g+=t(240,441,'Standard orthography represents Hanoi pronunciation.','middle','Ls')
    g+=footer('38','Vietnamese','B','Phonology')
    return g+close_svg()

# ─── PLATE 38C — GRAMMAR ───────────────────────────────────────────────────
def build_38c():
    g=open_svg()
    g+=t(240,32,'VIETNAMESE','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE — SVO, ISOLATING')
    g+=t(240,82,'Vietnamese is an isolating (analytic) language: no inflection, no case, no gender.','middle','Ls')
    g+=t(240,92,'Meaning conveyed by word order, particles, and context.','middle','Ls')
    g+=t(240,102,'T\u00f4i \u0103n c\u01a1m. I eat rice. (T\u00f4i=I \u0103n=eat c\u01a1m=cooked-rice)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'PRONOUNS \u2014 SOCIAL REGISTER SYSTEM')
    g+=t(240,129,'Vietnamese pronouns encode social relationship, age, and respect level.','middle','Ls')
    pros=[('t\u00f4i','I (neutral/formal)'),('m\u00ecnh','I/self (intimate)'),
          ('anh','I/you (older male to younger)'),('ch\u1ecb','I/you (older female)'),
          ('em','I/you (younger to older)'),('b\u1ea1n','you (peer/friend)'),
          ('\u00f4ng','he/you (elderly male)'),('b\u00e0','she/you (elderly female)'),
          ('n\u00f3/h\u1eafn','he/she (3rd sg, informal)'),('h\u1ecd','they (3rd pl)'),
          ('ch\u00fang t\u00f4i','we (excl)'),('ch\u00fang ta','we (incl)')]
    for i,(p,gloss) in enumerate(pros):
        col=i%2; row=i//2
        x=80+col*200; y=139+row*10
        g+=t(x,y,f'{p} = {gloss}','middle','Lx')
    g+=hr(210)
    g+=sh(219,'VERB SYSTEM \u2014 PARTICLES AND ASPECT')
    g+=t(240,229,'Verbs are uninflected. Tense/aspect marked by pre-verbal particles:','middle','Ls')
    particles=[('\u0111\u00e3','past (completed)'),('s\u1ebd','future'),('\u0111ang','progressive/ongoing'),
               ('s\u1eafp','imminent future'),('v\u1eeba','just completed'),('\u0111\u01b0\u1ee3c','ability/completion'),
               ('b\u1ecb','passive (negative)'),('\u0111\u01b0\u1ee3c','passive (positive)')]
    for i,(p,gloss) in enumerate(particles):
        col=i%2; row=i//2
        x=80+col*200; y=239+row*10
        g+=t(x,y,f'{p} = {gloss}','middle','Lx')
    g+=hr(305)
    g+=sh(314,'CLASSIFIERS')
    g+=t(240,324,'Classifiers required between numeral and noun: m\u1ed9t c\u00e1i b\u00e0n (one CL.thing table).','middle','Ls')
    classifiers=[('c\u00e1i','inanimate things'),('con','animals, rivers, roads'),
                 ('c\u00e1','fish, some body parts'),('c\u00e2y','trees, sticks, pens'),
                 ('b\u00e0i','papers, lessons, songs'),('qu\u1ea3','round things, fruits'),
                 ('ng\u01b0\u1eddi','people'),('cu\u1ed1n','books, rolls')]
    for i,(cl,desc) in enumerate(classifiers):
        col=i%2; row=i//2
        x=80+col*200; y=334+row*10
        g+=t(x,y,f'{cl}: {desc}','middle','Lx')
    g+=hr(400)
    g+=sh(409,'CORE VOCABULARY')
    vocab=[('xin ch\u00e0o','hello'),('c\u1ea3m \u01a1n','thank you'),('c\u00f3','yes/have'),
           ('kh\u00f4ng','no/not/zero'),('xin l\u1ed7i','sorry/excuse me'),
           ('b\u1ea1n kh\u1ecfe kh\u00f4ng?','how are you?'),('t\u00f4i kh\u1ecfe','I am well'),
           ('t\u00f4i y\u00eau b\u1ea1n','I love you'),('n\u01b0\u1edbc','water'),('l\u1eeda','fire'),
           ('\u0111\u1ea5t','earth/land'),('ng\u01b0\u1eddi','person'),('th\u1eddi gian','time'),
           ('m\u1eb7t tr\u0103ng','moon'),('ng\u00f4i sao','star'),('tr\u00e1i tim','heart'),
           ('t\u00ecnh y\u00eau','love'),('t\u1ef1 do','freedom'),('k\u00fd \u1ee9c','memory'),
           ('t\u01b0\u01a1ng lai','future'),('th\u1ebf gi\u1edbi','world'),('cu\u1ed9c s\u1ed1ng','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<11 else 1
        y=419+(i if i<11 else i-11)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('38','Vietnamese','C','Grammar')
    return g+close_svg()

# ─── PLATE 38D — RUNNING TEXT ──────────────────────────────────────────────
def build_38d():
    g=open_svg()
    g+=t(240,32,'VIETNAMESE','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. T\u1ee4C NG\u1eee \u2014 PROVERB')
    g+=t(240,80,'H\u1ecdc, h\u1ecdc n\u1eefa, h\u1ecdc m\u00e3i.','middle','L')
    g+=t(240,90,'h\u1ecdc=study h\u1ecdc=study n\u1eefa=more h\u1ecdc=study m\u00e3i=always/forever','middle','Ls')
    g+=t(240,100,'"Study, study more, study always." (Ho Chi Minh; continuous learning imperative)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. K\u00dd \u1ee8C V\u00c0 T\u01af\u01a0NG LAI \u2014 MEMORY AND FUTURE')
    g+=t(240,128,'U\u1ed1ng n\u01b0\u1edbc nh\u1edb ngu\u1ed3n.','middle','L')
    g+=t(240,138,'u\u1ed1ng=drink n\u01b0\u1edbc=water nh\u1edb=remember ngu\u1ed3n=source/spring','middle','Ls')
    g+=t(240,148,'"When you drink water, remember its source." (proverb on gratitude and memory)','middle','F')
    g+=hr(157)
    g+=sh(166,'III. TRI TH\u1ee8C \u2014 ON KNOWLEDGE')
    g+=t(240,176,'M\u1ed9t kho b\u00e1u kh\u00f4ng bao gi\u1edd c\u1ea1n ki\u1ec7t l\u00e0 tri th\u1ee9c.','middle','Ls')
    g+=t(240,186,'m\u1ed9t=one kho-b\u00e1u=treasure kh\u00f4ng=not bao-gi\u1edd=ever c\u1ea1n-ki\u1ec7t=exhausted l\u00e0=is tri-th\u1ee9c=knowledge','middle','Lx')
    g+=t(240,196,'"A treasure that never runs out is knowledge." (Vietnamese educational maxim)','middle','F')
    g+=hr(205)
    g+=sh(214,'IV. TI\u1ebeN L\u00caN \u2014 FORWARD')
    g+=t(240,224,'Ch\u00fang ta b\u01b0\u1edbc ti\u1ebfn ph\u00eda tr\u01b0\u1edbc, mang theo k\u00fd \u1ee9c c\u1ee7a nh\u1eefng ng\u01b0\u1eddi \u0111i tr\u01b0\u1edbc.','middle','Ls')
    g+=t(240,234,'b\u01b0\u1edbc-ti\u1ebfn=step-forward ph\u00eda-tr\u01b0\u1edbc=toward-front mang-theo=carry-along','middle','Ls')
    g+=t(240,244,'k\u00fd-\u1ee9c=memory c\u1ee7a=of nh\u1eefng-ng\u01b0\u1eddi=those-people \u0111i-tr\u01b0\u1edbc=went-before','middle','Ls')
    g+=t(240,254,'"We step forward, carrying the memory of those who went before." ','middle','F')
    g+=hr(263)
    g+=sh(272,'V. BRIDGE PHRASE')
    g+=t(240,285,'V\u1eadt n\u00e0y \u0111\u01b0\u1ee3c l\u00e0m ra cho b\u1ea1n, mi\u1ec5n ph\u00ed,','middle','L')
    g+=t(240,295,'b\u1edfi nh\u1eefng ng\u01b0\u1eddi \u0111\u00e3 nh\u1edb v\u1ec1 ph\u00eda tr\u01b0\u1edbc.','middle','L')
    g+=t(240,309,'v\u1eadt-n\u00e0y=this-thing \u0111\u01b0\u1ee3c-l\u00e0m-ra=was-made cho=for b\u1ea1n=you','middle','Ls')
    g+=t(240,318,'mi\u1ec5n-ph\u00ed=free-of-charge b\u1edfi=by nh\u1eefng-ng\u01b0\u1eddi=those-people','middle','Ls')
    g+=t(240,327,'\u0111\u00e3=PAST nh\u1edb=remember v\u1ec1=toward ph\u00eda-tr\u01b0\u1edbc=the-front/forward','middle','Ls')
    g+=t(240,339,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(350)
    g+=sh(359,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,369,'Ph\u00eda tr\u01b0\u1edbc = "the front / ahead / forward." In Vietnamese spatial metaphor,','middle','Ls')
    g+=t(240,379,'the future is ph\u00eda tr\u01b0\u1edbc (in front) and the past is ph\u00eda sau (behind).','middle','Ls')
    g+=t(240,389,'Nh\u1edb v\u1ec1 ph\u00eda tr\u01b0\u1edbc = "remember toward the front" — an unusual collocation','middle','Ls')
    g+=t(240,399,'that captures the spirit of forward-facing memory. Mi\u1ec5n ph\u00ed = free of charge.','middle','Ls')
    g+=hr(407)
    g+=sh(416,'LANGUAGE NOTES')
    g+=t(240,426,'Vietnamese: ~90 million L1 speakers; official language of Vietnam.','middle','Ls')
    g+=t(240,436,'Language family: Austroasiatic, Mon-Khmer branch (Viet-Muong sub-group).','middle','Ls')
    g+=t(240,446,'Heavy Chinese loanword influence (Sino-Vietnamese layer, ~60% of formal vocab).','middle','Ls')
    g+=t(240,456,'Spoken also in overseas communities: USA, France, Australia, Cambodia.','middle','Ls')
    g+=footer('38','Vietnamese','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate38a_vietnamese_script.svg': build_38a(),
        'plate38b_vietnamese_phonology.svg': build_38b(),
        'plate38c_vietnamese_grammar.svg': build_38c(),
        'plate38d_vietnamese_text.svg': build_38d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
