#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Yoruba plate series 30A–30D for Remember Forward."""
from pathlib import Path
OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text { font-family: Georgia, serif; }\n'
        '  .T{font-size:12px;font-weight:bold;letter-spacing:2px}\n'
        '  .S{font-size:7px;letter-spacing:1.5px}\n'
        '  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}\n'
        '  .L{font-size:7px} .Ls{font-size:6px} .Lx{font-size:5.5px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic}\n'
        '  .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')
def close_svg(): return '</svg>\n'
def t(x,y,s,a='middle',c='L',extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{esc(s)}</text>\n'
def hr(y,x1=20,x2=460,sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y,txt): return t(240,y,f'\u2014 {txt} \u2014','middle','H')
def footer(num,lang,letter,desc):
    return (hr(625)+t(240,620,f'SERIES {num} \u00b7 {lang.upper()} \u00b7 PLATE {letter} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        +hr(633)+t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        +t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))

def build_30a():
    g=open_svg()
    g+=t(240,32,'YORUBA \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g+=t(240,50,'SERIES 30A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'YORUBA \u2014 NIGER-CONGO \u00b7 ~45 MILLION SPEAKERS')
    g+=t(240,79,'Yoruba is a Niger-Congo (Volta-Niger branch) language spoken in Nigeria, Benin, and Togo.','middle','L')
    g+=t(240,89,'One of the three major languages of Nigeria alongside Hausa and Igbo.','middle','Ls')
    g+=t(240,98,'Also the liturgical language of the Candomble and Lucumi/Santeria traditions of the Americas.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'THE YORUBA ALPHABET \u2014 25 LETTERS')
    g+=t(240,125,'Standard Yoruba uses 25 Latin letters. Three additional vowels: e-dot (\u1eb9), o-dot (\u1ecdot), s-dot (\u1e63).','middle','Ls')
    letters=[
        ('A a','/a/','open low'),('B b','/b/','bilabial'),('D d','/d/','alveolar'),
        ('E e','/e/','mid front close'),('\u1eb9 \u1eb9','/\u025b/','mid front open: \u1eb9y\u1eb9 (language)'),
        ('F f','/f/','labiodental'),('G g','/\u0261/','velar'),('Gb gb','/\u0261\u0253/','labial-velar stop (unique!)'),
        ('H h','/h/','glottal'),('I i','/i/','high front'),('J j','/d\u0292/','affricate'),
        ('K k','/k/','velar'),('L l','/l/','lateral'),('M m','/m/','nasal'),
        ('N n','/n/','nasal'),('O o','/o/','mid back close'),('\u1ecd \u1ecd','/\u0254/','mid back open: \u1ecd\u0300run (heaven)'),
        ('P p','/k\u0253/','labial-velar ejective (unique!)'),('R r','/r/','alveolar tap'),
        ('S s','/s/','alveolar'),('\u1e63 \u1e63','/\u0283/','palatal frict.: \u1e63\u1eb9 (money)'),
        ('T t','/t/','alveolar'),('U u','/u/','high back'),('W w','/w/','glide'),('Y y','/j/','glide'),
    ]
    for i,(ltr,ipa,note) in enumerate(letters):
        col=0 if i<13 else 1
        y=135+(i if i<13 else i-13)*10
        cx=[35,100,200] if col==0 else [255,320,420]
        g+=t(cx[0],y,ltr,'middle','Lx'); g+=t(cx[1],y,ipa,'middle','Lx'); g+=t(cx[2],y,note,'middle','Lx')
    g+=hr(272)
    g+=sh(281,'THREE-TONE SYSTEM \u2014 HIGH, MID, LOW')
    g+=t(240,292,'Yoruba has THREE tones: High (\u00b4), Mid (unmarked), Low (\u0060). Tone is phonemic.','middle','L')
    g+=t(240,302,'High: \u00e0r\u00e1 (thunder) \u00b7 Mid: ara (body) \u00b7 Low: \u00e0r\u00e0 (saw/tool)','middle','Ls')
    g+=t(240,311,'Tones are marked with diacritics in standard orthography: acute=H, grave=L, unmarked=M.','middle','Ls')
    g+=t(240,320,'Tonal downstep: a sequence of highs may step down in pitch through a phrase.','middle','Ls')
    g+=hr(328)
    g+=sh(337,'UNIQUE CONSONANTS: GB AND KP')
    g+=t(240,348,'gb = /\u0261\u0253/ labial-velar: lips and back of tongue close SIMULTANEOUSLY. Not found in European languages.','middle','L')
    g+=t(240,358,'kp = /k\u0253/ or /p\u0294/: similar simultaneous closure, voiceless. Also in Igbo, Ewe, and other Niger-Congo languages.','middle','Ls')
    g+=t(240,367,'These sounds exist in ~30% of Niger-Congo languages and are essentially absent outside Africa.','middle','Ls')
    g+=footer('30','Yoruba','A','Script')
    return g+close_svg()

def build_30b():
    g=open_svg()
    g+=t(240,32,'YORUBA \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g+=t(240,50,'SERIES 30B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'THREE-TONE SYSTEM \u2014 PHONEMIC TONES')
    g+=t(240,79,'Yoruba tone is critical: the same string of consonants and vowels has different meanings by tone alone.','middle','L')
    examples=[
        ('aw\u00f3','(H-H)','hand-washing basin'),
        ('\u00e0w\u00f2','(L-H)','ashes'),
        ('aw\u00f2','(M-H)','colour / image'),
        ('\u1ecd\u0300m\u00f3','(L-H)','child'),
        ('\u1ecd\u0301m\u00f3','(H-H)','plant (young)'),
        ('\u1ecd m\u1ecd','(L-M)','face that'),
    ]
    for i,(word,tone,gloss) in enumerate(examples):
        y=89+i*12
        g+=t(80,y,word,'middle','Ls'); g+=t(155,y,tone,'middle','Lx'); g+=t(330,y,gloss,'middle','Lx')
    g+=hr(165)
    g+=sh(174,'VOWELS \u2014 7 ORAL + 5 NASAL')
    g+=t(240,185,'Yoruba has 7 oral vowels and 5 nasal vowels. Nasal vowels are phonemic (contrastive).','middle','L')
    vowels=[('/i/','i','ile (house)'),('/e/','e','eko (food)'),('/\u025b/','e-dot','\u1eb9y\u1eb9 (language)'),
            ('/a/','a','aja (dog)'),('/\u0254/','o-dot','\u1ecd run (heaven)'),('/o/','o','ojo (day)'),('/u/','u','unu (mouth)')]
    nasal=[('/\u0129/','in','it\u0303\u1eb9\u0301l\u1eb9\u0301 (darkness)'),('/\u1ebd/','en','...'),
           ('/\u025b\u0303/','en-dot','...'),('/\u00f5/','on','...'),('/\u1ecd\u0303/','on-dot','...')]
    g+=t(100,195,'Oral','middle','Lx'); g+=t(340,195,'Nasal','middle','Lx')
    for i,(ipa,ltr,ex) in enumerate(vowels):
        y=204+i*11
        g+=t(55,y,ipa,'middle','Lx'); g+=t(105,y,ltr,'middle','Lx'); g+=t(195,y,ex,'middle','Lx')
    for i,(ipa,ltr,ex) in enumerate(nasal):
        y=204+i*11
        g+=t(285,y,ipa,'middle','Lx'); g+=t(340,y,ltr,'middle','Lx')
    g+=hr(286)
    g+=sh(295,'CONSONANT HIGHLIGHTS')
    g+=t(240,306,'Yoruba has 18 consonants. Key features: labial-velar stops gb/kp and syllabic nasals.','middle','L')
    g+=t(240,316,'Syllabic nasals: m and n can form complete syllables: m\u0300b\u00ed (a name), n\u00edp\u00e1 (there is a broom).','middle','Ls')
    g+=t(240,325,'The syllabic nasal carries its own tone: m\u0300 (L) vs m\u0301 (H).','middle','Ls')
    g+=t(240,334,'No consonant clusters: every consonant is followed by a vowel (strict CV syllable structure).','middle','Ls')
    g+=hr(342)
    g+=sh(351,'DOWNSTEP AND DOWNDRIFT')
    g+=t(240,362,'Downstep: a High tone after a floating Low tone is lower than a previous High \u2014 marked with \u02c0.','middle','Ls')
    g+=t(240,371,'Downdrift: High tones gradually lower across an utterance with intervening Low tones.','middle','Ls')
    g+=t(240,380,'This means identical tonal patterns at the start and end of a long sentence may be at very different pitches.','middle','Ls')
    g+=footer('30','Yoruba','B','Phonology')
    return g+close_svg()

def build_30c():
    g=open_svg()
    g+=t(240,32,'YORUBA \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,50,'SERIES 30C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SVO \u2014 ISOLATING LANGUAGE \u2014 NO INFLECTION')
    g+=t(240,79,'Yoruba is an ISOLATING language: no inflectional suffixes. Grammatical meaning conveyed by particles and order.','middle','L')
    g+=t(240,89,'No case endings, no verb conjugation for agreement. Tense/aspect marked by pre-verbal particles.','middle','Ls')
    g+=t(240,98,'Mo fe lati lo. (I want to go.) \u2014 Mo=I, fe=want, lati=to, lo=go. No inflection at all.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'TENSE-ASPECT-MOOD PARTICLES')
    tams=[('(none)','Simple present / habitual','Mo joko. (I sit / I sit habitually.)'),
          ('\u0301n','Progressive (present cont.)','Mo \u0301n joko. (I am sitting.)'),
          ('ti','Perfect (completed)','Mo ti joko. (I have sat.)'),
          ('yoo / ma\u00e1','Future / habitual future','Mo yoo joko. (I will sit.)'),
          ('\u0301f\u0101','Past habitual','Mo \u0301f\u0101 joko. (I used to sit.)')]
    for i,(part,func,ex) in enumerate(tams):
        y=125+i*14
        g+=t(55,y,part,'middle','Ls'); g+=t(165,y,func,'middle','Lx'); g+=t(360,y,ex,'middle','Lx')
    g+=hr(198)
    g+=sh(207,'SERIAL VERB CONSTRUCTIONS')
    g+=t(240,218,'Yoruba uses SERIAL VERBS: multiple verbs in sequence share one subject with no conjunction.','middle','L')
    g+=t(240,228,'Mo m\u00fa omi mu. (I took water drank.) = "I drank water."','middle','Ls')
    g+=t(240,237,'O w\u00e0 w\u1ecd. (He came saw.) = "He came and looked / He came to see."','middle','Ls')
    g+=t(240,246,'This is a defining feature of Niger-Congo languages \u2014 absent from Indo-European.','middle','Ls')
    g+=hr(254)
    g+=sh(263,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[('b\u1eb9\u0301\u1eb9\u0300 / r\u00e0r\u00e0','yes / no'),('mi / \u0254 / \u0113yin','I / he-she / you pl'),
           ('y\u00ed / \u0300y\u0300en','this / that'),('\u00edbo?','where'),
           ('k\u00ed n\u00ed?','what'),('ta l\u00f3?','who'),('\u00edg\u00bat\u00ed?','when'),
           ('p\u00e0t\u00e0k\u00ed?','why'),('\u0254mi','water'),('\u1ecdr\u1ecdl\u1ecd','fire'),
           ('\u00e0gb\u00e0l\u1eb9','earth/soil'),('eni','person'),('iwe','book'),
           ('ak\u00f3k\u00f3','time'),('\u1cd5\u0300\u0254sc\u00f2','moon'),('ish\u1eb9\u0301','star'),
           ('\u1ecdr\u00f2kan','heart'),('if\u1eb9\u0301','love'),('ominira','freedom'),
           ('\u00ecranti','memory'),('\u1ed3j\u1ecd\u0301\u00e0','future'),('ay\u00e9','world/life'),
           ('dara / b\u00e0j\u00e9','good / bad'),('gbogbo','everything'),('ay\u1eb9','life')]
    for i,(y_w,e) in enumerate(vocab):
        col=0 if i<13 else 1
        y=273+(i if i<13 else i-13)*10
        g+=t(50+col*230,y,y_w,'middle','Ls'); g+=t(175+col*230,y,e,'middle','Lx')
    g+=hr(408)
    g+=sh(417,'NOUNS AND PRONOUNS')
    g+=t(240,428,'No grammatical gender. No articles. Definiteness marked by context or demonstratives.','middle','Ls')
    g+=t(240,437,'Pronouns: mo/mi (I/me), o/\u0301 (you sg), \u00f3 (he/she/it), a (we), yin (you pl), w\u1ecdn (they).','middle','Ls')
    g+=t(240,446,'Possessives: noun + pronoun: il\u00e9 mi (my house), il\u00e9 r\u1eb9 (your house), il\u00e9 r\u1eb9\u0300 (his house).','middle','Ls')
    g+=footer('30','Yoruba','C','Grammar')
    return g+close_svg()

def build_30d():
    g=open_svg()
    g+=t(240,32,'YORUBA \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,50,'SERIES 30D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(67,'PASSAGE 1 \u2014 YORUBA PROVERB')
    g+=t(240,78,'Yoruba: Aj\u00e9 l\u1eb9\u0301 \u0300b\u00e0 or\u00ed s\u1eb9\u0301.','middle','L')
    g+=t(240,88,'Wealth comes  head  finds.','middle','Lx')
    g+=t(240,97,'"Wealth comes to the head that seeks it." \u2014 Fortune favours the prepared.','middle','Ls')
    g+=hr(105)
    g+=sh(113,'PASSAGE 2 \u2014 YORUBA PROVERB')
    g+=t(240,124,'Or\u00ed \u0300p\u00e9 l\u00f3 maa n\u0301 gbani j\u1eb9\u0301, k\u00ed \u0300s\u00ed aw\u1ecdn \u00e0gb\u00e0gb\u00e0.','middle','L')
    g+=t(240,134,'Destiny that  will save-one  not are  elders.','middle','Lx')
    g+=t(240,143,'"It is one\'s destiny that saves, not the elders." \u2014 Personal fate and responsibility.','middle','Ls')
    g+=hr(151)
    g+=sh(159,'PASSAGE 3 \u2014 ON THE NATURE OF MEMORY')
    g+=t(240,170,'\u00ccr\u00e0nti \u0300n\u00ed k\u00ed a m\u1ecd d\u00e0 s\u1eb9\u0301h\u00ecn, k\u00ed a s\u00ec t\u1ecds\u00ed\u0332w\u1ecdl\u1eb9\u0301.','middle','L')
    g+=t(240,180,'Memory says that we look back,  that we face forward.','middle','Lx')
    g+=t(240,189,'"Memory asks us to look back so that we may face forward."','middle','Ls')
    g+=hr(197)
    g+=sh(205,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g+=t(240,217,'\u1ecdr\u1ecd\u0300 y\u00ed ni a \u015e\u1eb9\u0301 f\u00fan \u0254, l\u00f3fo, nip\u1eb9\u0301 aw\u1ecdn eni t\u00ed w\u1ecdn r\u00e0nti \u1ed3j\u1ecd\u0301\u00e0.','middle','L')
    g+=t(240,228,'Message this it was made for you freely  by   people   who   they remembered future.','middle','Lx')
    g+=t(240,238,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g+=hr(246)
    g+=sh(255,'LANGUAGE NOTE \u2014 "FUTURE" IN YORUBA')
    g+=t(240,266,'\u1ed3j\u1ecd\u0301\u00e0 = "future" \u2014 literally "day coming" or "coming day". The future as an approaching moment.','middle','L')
    g+=t(240,276,'r\u00e0nti = "to remember" \u2014 \u00ecr\u00e0nti = "memory / remembrance" (noun from verb).','middle','Ls')
    g+=t(240,285,'l\u00f3fo = "freely / free of charge" \u2014 from \u00f3fo (free, no cost, without loss).','middle','Ls')
    g+=t(240,294,'Tone note: \u1ecdr\u1ecd\u0300 (message) is L-L; \u1ed3j\u1ecd\u0301\u00e0 (future) is H-H-L \u2014 tone carries meaning.','middle','Ls')
    g+=hr(302)
    g+=sh(311,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g+=t(240,322,'Yoruba is spoken by ~45 million people in Nigeria, Benin, and Togo. One of Africa\'s major literary languages.','middle','Ls')
    g+=t(240,331,'It spread to the Americas through the slave trade: Candomble, Lucumi, and Santeria preserve Yoruba liturgy.','middle','Ls')
    g+=t(240,340,'Three tones (H/M/L) are marked in standard writing with acute, grave, and no accent.','middle','Ls')
    g+=t(240,349,'Consult Plate 30A for the alphabet including dotted letters (\u1eb9, \u1ecd, \u1e63) and the unique gb/kp sounds.','middle','Ls')
    g+=footer('30','Yoruba','D','Text')
    return g+close_svg()

def main():
    plates={'plate30a_yoruba_script.svg':build_30a(),'plate30b_yoruba_phonology.svg':build_30b(),
            'plate30c_yoruba_grammar.svg':build_30c(),'plate30d_yoruba_text.svg':build_30d()}
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8'); print(f'Written: {OUT/fname}')

if __name__=='__main__': main()
