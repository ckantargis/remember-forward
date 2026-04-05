"""Build script — Burmese series plates 40A–40D (Remember Forward)"""
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
            '.Lb{font-size:11px;}\n'
            '.Lbs{font-size:8px;}\n'
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

# ─── PLATE 40A — SCRIPT ────────────────────────────────────────────────────
def build_40a():
    g=open_svg()
    g+=t(240,32,'BURMESE','middle','T')
    g+=t(240,50,'\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c \u2014 Script (Abugida)','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM \u2014 ABUGIDA')
    g+=t(240,82,'Burmese script: abugida derived from Mon script, which came from South Indian Brahmic.','middle','Ls')
    g+=t(240,92,'Distinctive rounded letters developed due to palm-leaf writing (curved strokes avoid tearing).','middle','Ls')
    g+=t(240,102,'Written left to right. Consonants carry inherent vowel /a/; diacritics modify vowels.','middle','Ls')
    g+=hr(110)
    g+=sh(119,'CONSONANT TABLE \u2014 33 LETTERS')
    g+=t(240,129,'Burmese has 33 consonants arranged in traditional Sanskrit-derived order:','middle','Ls')
    cons=[('\u1000 ka','\u1001 hka','\u1002 ga','\u1003 gha','\u1004 nga'),
          ('\u1005 ca','\u1006 hca','\u1007 ja','\u1008 jha','\u1009 nya'),
          ('\u100a nnya','\u100b ta','\u100c hta','\u100d da','\u100e dha'),
          ('\u100f na','\u1010 ta','\u1011 hta','\u1012 da','\u1013 dha'),
          ('\u1014 na','\u1015 pa','\u1016 hpa','\u1017 ba','\u1018 bha'),
          ('\u1019 ma','\u101a ya','\u101b ra','\u101c la','\u101d wa'),
          ('\u101e sa','\u101f ha','\u1020 la','\u1021 a','')]
    for row_i,row in enumerate(cons):
        y=139+row_i*12
        for col_i,c in enumerate(row):
            if c:
                parts=c.split(' ',1)
                x=40+col_i*82
                g+=t(x,y,parts[0],'middle','Lb')
                if len(parts)>1: g+=t(x,y+8,parts[1],'middle','Lx')
    g+=hr(228)
    g+=sh(237,'VOWEL DIACRITICS')
    g+=t(240,247,'C = consonant. Vowels written as diacritics above, below, or surrounding:','middle','Ls')
    vowels=[('\u1000\u102b','kaa /k\u0251\u02d0/'),('\u1000\u102c','kaa2 /k\u0251/'),
            ('\u1000\u102d','ki /ki/'),('\u1000\u102e','kii /ki\u02d0/'),
            ('\u1000\u102f','ku /ku/'),('\u1000\u1030','kuu /ku\u02d0/'),
            ('\u1000\u1031','ke /k\u025b/'),('\u1000\u1031\u102c','kae /k\u025b\u02d0/'),
            ('\u1000\u1031\u102b','ko /ko/')]
    for i,(v,desc) in enumerate(vowels):
        col=i%3; row=i//3
        x=65+col*130; y=257+row*11
        g+=t(x,y,f'{v} = {desc}','middle','Lb')
    g+=hr(305)
    g+=sh(314,'THREE TONES \u2014 MARKED BY DIACRITICS')
    tones=[('Level (low short)','no mark: \u1000\u102c ka','short, modal voice'),
           ('Heavy (low long)','colon mark \u1031\u102c: \u1000\u102c\u1038 kaa','long, creaky voice'),
           ('Creaky (high short)','\u102d above: \u1000\u102d\u1037 kai\'','short, creaky+glottal stop')]
    for i,(name,mark,desc) in enumerate(tones):
        y=324+i*11
        g+=t(90,y,name,'middle','Ls'); g+=t(230,y,mark,'middle','Lbs'); g+=t(380,y,desc,'middle','Lx')
    g+=hr(365)
    g+=sh(374,'BURMESE NUMERALS')
    g+=t(240,384,'\u1040\u1041\u1042\u1043\u1044\u1045\u1046\u1047\u1048\u1049  (0\u20139)','middle','Lb')
    g+=t(240,398,'Burmese numerals based on same Brahmi origin as Arabic numerals.','middle','Ls')
    g+=t(240,408,'10 = \u1041\u1040  100 = \u1041\u1000\u1014\u103a  1000 = \u1041\u101e\u1031\u102c','middle','Ls')
    g+=footer('40','Burmese','A','Script')
    return g+close_svg()

# ─── PLATE 40B — PHONOLOGY ─────────────────────────────────────────────────
def build_40b():
    g=open_svg()
    g+=t(240,32,'BURMESE','middle','T')
    g+=t(240,50,'Phonology \u2014 Three Tones and Consonant System','middle','S')
    g+=hr(60)
    g+=sh(72,'THREE-TONE SYSTEM')
    g+=t(240,82,'Burmese has 3 phonemic tones (plus a 4th "checked" syllable type):','middle','Ls')
    tones=[('Level (low)','short, modal voice, mid-low pitch: ma (horse)'),
           ('Heavy (long)','long, modal/creaky voice, falling: maa (come)'),
           ('Creaky (high)','short, creaky voice, high pitch with glottal stop: ma\' (hard)'),
           ('Checked (stop)','short syllable ending in glottal stop or unreleased stop')]
    for i,(name,desc) in enumerate(tones):
        y=92+i*12
        g+=t(100,y,name,'middle','Ls'); g+=t(320,y,desc,'middle','Lx')
    g+=hr(145)
    g+=sh(154,'CONSONANT INVENTORY')
    cons=[('p /p/','bilabial vl'),('ph /p\u02b0/','bilabial asp'),('b /b/','bilabial vd'),
          ('t /t/','alveolar vl'),('th /t\u02b0/','alveolar asp'),('d /d/','alveolar vd'),
          ('s /s/','alveolar fric'),('sh /\u0283/','postalveolar'),
          ('k /k/','velar vl'),('kh /k\u02b0/','velar asp'),('g /\u0261/','velar vd'),
          ('c /t\u0255/','palatal aff'),('m /m/','bilabial nasal'),('n /n/','alveolar nasal'),
          ('ng /\u014b/','velar nasal'),('ny /\u0272/','palatal nasal'),
          ('l /l/','lateral'),('r /j/','palatal glide (modern)'),
          ('w /w/','labio-velar'),('y /j/','palatal'),('h /h/','glottal'),
          ('? /\u0294/','glottal stop')]
    for i,(c,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=164+row*10
        g+=t(x,y,f'{c} {desc}','middle','Lx')
    g+=hr(265)
    g+=sh(274,'CONSONANT MEDIALS')
    g+=t(240,284,'Burmese allows medial consonants (w, y, r, h) before the vowel in a syllable:','middle','Ls')
    g+=t(240,294,'kw- (k+w medial), ky- (k+y medial), khy- (kh+y), my- (m+y), etc.','middle','Ls')
    g+=t(240,304,'Medials affect pronunciation: kya = /t\u0255a/, mya = /mja/.','middle','Ls')
    g+=hr(312)
    g+=sh(321,'VOWEL SYSTEM')
    g+=t(240,331,'Short/long pairs: a/aa, i/ii, u/uu, e/ee, o/oo, plus diphthongs.','middle','Ls')
    g+=t(240,341,'Vowel length + tone together = distinct syllable types.','middle','Ls')
    g+=t(240,351,'Schwa /\u0259/ common in unstressed syllables (often written as -a).','middle','Ls')
    g+=hr(359)
    g+=sh(368,'SANDHI AND SPOKEN BURMESE')
    g+=t(240,378,'Literary Burmese and spoken Burmese differ significantly.','middle','Ls')
    g+=t(240,388,'Spoken: copula "is" = hpyi (written: jaa). Questions use final particles.','middle','Ls')
    g+=t(240,398,'Diglossia: formal/written vs. colloquial/spoken registers differ in vocabulary + structure.','middle','Ls')
    g+=footer('40','Burmese','B','Phonology')
    return g+close_svg()

# ─── PLATE 40C — GRAMMAR ───────────────────────────────────────────────────
def build_40c():
    g=open_svg()
    g+=t(240,32,'BURMESE','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SOV')
    g+=t(240,82,'Burmese is Subject-Object-Verb (SOV) — verb always final.','middle','Ls')
    g+=t(240,92,'Nga htamin sa de. I rice eat. (nga=I htamin=rice sa=eat de=particle)','middle','Ls')
    g+=t(240,102,'Particles follow every major element: subject -ga/-k\u0259, object -go, location -hma.','middle','Ls')
    g+=hr(110)
    g+=sh(119,'CASE PARTICLES')
    particles=[('-ga / -k\u0259','subject/topic marker'),('-go','object/direction marker'),
               ('-hma','locative (at/in/on)'),('-n\u0259','instrumental (by/with)'),
               ('-pei','benefactive (for)'),('-h\u0259','ablative (from)'),
               ('-\u0254\u014b','comitative (with, accompaniment)')]
    for i,(p,gloss) in enumerate(particles):
        y=129+i*10
        g+=t(120,y,p,'middle','Ls'); g+=t(300,y,gloss,'middle','Ls')
    g+=hr(205)
    g+=sh(214,'VERB SYSTEM')
    g+=t(240,224,'Verbs are final; tense/aspect by particles following the verb stem.','middle','Ls')
    verbs=[('sa de','eats (present/habitual, -de = assertion)'),
           ('sa m\u025b','will eat (-m\u025b = future)'),
           ('sa b\u00ed','ate (-bi = past completive)'),
           ('sa \u02a1\u00e6','is eating (-\u02a1\u00e6 = progressive)'),
           ('ma-sa-b\u00fa','did not eat (ma-...b\u00fa = past negative)'),
           ('sa l\u00f3','eat! (imperative)')]
    for i,(form,gloss) in enumerate(verbs):
        y=234+i*10
        g+=t(130,y,form,'middle','Ls'); g+=t(320,y,gloss,'middle','Lx')
    g+=hr(305)
    g+=sh(314,'PRONOUNS')
    pros=[('nga','I (informal)'),('k\u0259ma','I (female formal)'),('kj\u0259ma','I (male formal)'),
          ('n\u00edng','you (informal)'),('shin','you (respectful to monk)'),
          ('thu','he/she'),('doa','we (incl)'),('sh\u0254','they')]
    for i,(p,gloss) in enumerate(pros):
        col=i%2; row=i//2
        x=80+col*200; y=324+row*10
        g+=t(x,y,f'{p} = {gloss}','middle','Lx')
    g+=hr(385)
    g+=sh(394,'CORE VOCABULARY')
    vocab=[('ming-ga-la-ba','hello'),('kyei-zu-tin-ba-de','thank you'),
           ('h\u00f3uq-keh','yes'),('m\u00e0 h\u00f3uq-b\u00fa','no'),
           ('seim-na-ma-shi-b\u00fa','excuse me/sorry'),('nei-k\u00e0uq-l\u00e0?','how are you?'),
           ('k\u0259-m\u0259 nei-k\u00e0uq-d\u00e9','I am fine'),('j\u0259 j\u0259','I love you'),
           ('ye','water'),('m\u00edq','fire'),('m\u0259j\u00e9','earth'),
           ('lu','person'),('aq-j\u00e1','time'),('l\u00e0','moon'),
           ('kj\u00f3 tha\u014b\u014b\u00e9','star'),('h\u014b-th\u00e0','heart'),
           ('ch\u00e6t-th\u00e0','love'),('v\u00edq-th\u00e0','freedom'),
           ('mh\u00e0u-z\u00e0','memory/remember'),('n\u00e4-n\u00e4','future'),
           ('k\u00e0b\u00e0','world'),('a-th\u00e0','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<11 else 1
        y=404+(i if i<11 else i-11)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('40','Burmese','C','Grammar')
    return g+close_svg()

# ─── PLATE 40D — RUNNING TEXT ──────────────────────────────────────────────
def build_40d():
    g=open_svg()
    g+=t(240,32,'BURMESE','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. PYAN YA \u2014 PROVERB')
    g+=t(240,80,'\u1019\u101e\u1010\u102e\u1000\u102c\u1038\u1019\u103e\u102c \u1015\u100a\u100a\u102ac\u1000\u102c \u1010\u101e\u102d\u102f\u1038\u1019\u103e\u102c \u1015\u100a\u100a\u102c\u101e\u1031\u102c\u101c','middle','Lb')
    g+=t(240,95,'mashi-kaa-mha pannya-kaa to-shi-kaa-mha to-shi-kaa tha-le','middle','Ls')
    g+=t(240,105,'"What is not yet known, knowledge will bring; what is already there, wisdom will show."','middle','F')
    g+=hr(114)
    g+=sh(123,'II. HTIDAW \u2014 ON MEMORY')
    g+=t(240,133,'\u101b\u103e\u1031\u102c\u101e\u1030\u1038\u1000\u102d\u102f \u1019\u103e\u1010\u100a\u100a\u102c\u101e\u100a\u1037 \u1021\u1014\u102c\u1001\u102c\u101c\u102c\u1014\u1031\u1037','middle','Lb')
    g+=t(240,148,'yaungo-kyi mhaw-htaung-tha ana-kala la-ne','middle','Ls')
    g+=t(240,158,'"Remembering the past is how the future comes to us." (Burmese proverb on memory)','middle','F')
    g+=hr(167)
    g+=sh(176,'III. THUTEH \u2014 ON KNOWLEDGE')
    g+=t(240,186,'\u1015\u100a\u100a\u102c\u1006\u102c\u101e\u100a\u1037 \u1019\u102e\u1038\u1000\u102d\u102f\u1038 \u1019\u1015\u103c\u102f\u1011\u100f\u102c\u1021\u1036','middle','Lb')
    g+=t(240,201,'pannya-hka-tha myi-kyi-mya ma-pyaw-hpan','middle','Ls')
    g+=t(240,211,'"The flame of wisdom can never be extinguished." (Burmese saying on enduring knowledge)','middle','F')
    g+=hr(220)
    g+=sh(229,'IV. NA-NAING \u2014 FORWARD')
    g+=t(240,239,'\u101b\u103e\u1031\u102c\u101e\u1030\u1038\u1000\u102d\u102f \u101e\u1010\u102d\u1019\u103e\u1010\u102c\u1038 \u1021\u101b\u103e\u1031\u102c\u101e\u102d\u102f\u1038\u1021\u1031\u102c\u1001\u102c\u101e\u100a\u1037','middle','Lb')
    g+=t(240,253,'yaungo-kyi shi-thma-de amyaungo-da-la-tha','middle','Ls')
    g+=t(240,263,'"Moving forward while keeping the past in mind." (guiding concept)','middle','F')
    g+=hr(272)
    g+=sh(281,'V. BRIDGE PHRASE')
    g+=t(240,293,'\u1012\u102e\u1012\u101d\u101c\u102c\u101e\u100a\u1037\u1000\u102d\u102f \u1001\u1004\u102b\u101e\u1030\u1038\u1021\u1010\u103a\u1000\u102c','middle','Lb')
    g+=t(240,308,'\u1005\u101b\u102d\u102f\u1001\u100a\u1038\u1014\u103e\u1004\u1037\u101e\u100a\u1037','middle','Lb')
    g+=t(240,323,'\u1021\u101b\u103e\u1031\u102c\u101e\u102d\u102f\u1038 \u101e\u1010\u102d\u1019\u103e\u1010\u102c\u1038\u101e\u100a\u1037 \u101c\u1030\u101c\u102c\u101e\u100a\u1037\u1000\u101e\u102d\u1037','middle','Lb')
    g+=t(240,340,'di-da-la-tha kyi u-hka-mhu mashi-pya-ta (this-thing for-you free-of-cost was-made)','middle','Ls')
    g+=t(240,349,'amyaungo-da-la-tha shi-thma-de (who-forward remember keeping)','middle','Ls')
    g+=t(240,358,'lu-la-tha doh-a-hyi (by-those-people by)','middle','Ls')
    g+=t(240,370,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(380)
    g+=sh(389,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,399,'A-myaung-go (\u1021\u101b\u103e\u1031\u102c\u101e\u102d\u102f\u1038) = forward / front. In Burmese, the future is "ahead" (a-myaung).','middle','Ls')
    g+=t(240,409,'Mashi-pyaw-ta = free of charge (no-cost-given). SOV order maintained.','middle','Ls')
    g+=t(240,419,'The phrase encodes the project\'s core philosophy across the tonal system.','middle','Ls')
    g+=hr(427)
    g+=sh(436,'LANGUAGE NOTES')
    g+=t(240,446,'Burmese (Myanmar): ~33 million L1 speakers; official language of Myanmar.','middle','Ls')
    g+=t(240,456,'Language family: Sino-Tibetan, Tibeto-Burman branch (Lolo-Burmese group).','middle','Ls')
    g+=t(240,466,'Script: Mon/Brahmi-derived, rounded due to palm-leaf writing tradition.','middle','Ls')
    g+=t(240,476,'Significant diglossia between written (literary) and spoken registers.','middle','Ls')
    g+=footer('40','Burmese','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate40a_burmese_script.svg': build_40a(),
        'plate40b_burmese_phonology.svg': build_40b(),
        'plate40c_burmese_grammar.svg': build_40c(),
        'plate40d_burmese_text.svg': build_40d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
