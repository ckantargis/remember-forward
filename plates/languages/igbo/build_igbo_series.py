"""Build script — Igbo series plates 35A–35D (Remember Forward)"""
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

# ─── PLATE 35A — SCRIPT ────────────────────────────────────────────────────
def build_35a():
    g=open_svg()
    g+=t(240,32,'IGBO','middle','T')
    g+=t(240,50,'Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Igbo uses the Latin alphabet, standardised in the 1961 Onwu orthography.','middle','L')
    g+=t(240,94,'28 letters (a b ch d e f g gb gh gw h i \u1ecb j k kp kw l m n\u1ecb n o \u1ecd p r s sh t u \u1ee5 w y z).','middle','Ls')
    g+=t(240,104,'Diacritics mark tone (acute = high, grave = low) and distinguish vowels with dot-below.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'VOWEL SYSTEM — 8 ORAL VOWELS')
    vowels=[('a','/a/','arm'),('e','/e/','bed'),('\u1ecb','/\u1ecb/','Igbo vowel, between e and i'),
            ('i','/i/','see'),('o','/o/','ore'),('\u1ecd','/\u0254/','open-o, pot'),
            ('u','/u/','moon'),('\u1ee5','/\u1ee5/','Igbo vowel, between u and o')]
    for i,(letter,ipa,note) in enumerate(vowels):
        y=131+i*10
        g+=t(60,y,letter,'middle','L'); g+=t(130,y,ipa,'middle','Ls'); g+=t(310,y,note,'middle','Lx')
    g+=hr(215)
    g+=sh(224,'IGBO ALPHABET — ONWU ORTHOGRAPHY (1961)')
    letters=[('A a','a'),('B b','b'),('CH ch','ch'),('D d','d'),('E e','e'),
             ('F f','f'),('G g','g'),('GB gb','gb'),('GH gh','gh'),('GW gw','gw'),
             ('H h','h'),('I i','i'),('\u1eca \u1ecb','\u1ecb'),('J j','j'),('K k','k'),
             ('KP kp','kp'),('KW kw','kw'),('L l','l'),('M m','m'),('N n','n'),
             ('N\u1eca N\u1ecb','n\u1ecb'),('O o','o'),('\u1ecc \u1ecd','\u1ecd'),('P p','p'),('R r','r'),
             ('S s','s'),('SH sh','sh'),('T t','t'),('U u','u'),('\u1ee4 \u1ee5','\u1ee5'),
             ('W w','w'),('Y y','y'),('Z z','z')]
    for i,(letter,note) in enumerate(letters):
        col=i%4; row=i//4
        x=60+col*100; y=234+row*10
        g+=t(x,y,f'{letter}','middle','Ls')
    g+=hr(330)
    g+=sh(339,'DIGRAPHS AND SPECIAL FEATURES')
    g+=t(240,349,'GB /\u0261b/ — simultaneous velar+bilabial: gbara (filled), gbe (hit).','middle','Ls')
    g+=t(240,358,'KP /kp/ — simultaneous velar+bilabial (voiceless): kpoo (knock), kpa (carry).','middle','Ls')
    g+=t(240,367,'GH /\u0263/ — voiced velar fricative: ghara (do not), ngha (grinding).','middle','Ls')
    g+=t(240,376,'SH /\u0283/ — as in English: shiri (bird), sha (share out).','middle','Ls')
    g+=t(240,385,'N\u1eca /\u014b/ — velar nasal (ng in song): n\u1ecba (eat), n\u1ecbe (carry).','middle','Ls')
    g+=hr(393)
    g+=sh(402,'TONE MARKING')
    g+=t(240,412,'High tone: acute accent — \u00e1 \u00e9 \u00ed \u00f3 \u00fa (e.g., \u00e1 = yes, \u00f3bi = heart).','middle','Ls')
    g+=t(240,421,'Low tone: grave accent — \u00e0 \u00e8 \u00ec \u00f2 \u00f9 (e.g., \u00e0 = then, that).','middle','Ls')
    g+=t(240,430,'Mid/unmarked: no diacritic in many texts (tone is predictable in context).','middle','Ls')
    g+=t(240,439,'Down-step (!) marks a high tone that is lower than the preceding high.','middle','Ls')
    g+=hr(447)
    g+=sh(456,'HISTORICAL SCRIPT')
    g+=t(240,466,'Nsibidi: indigenous ideographic system used by Ekpe secret society.','middle','Ls')
    g+=t(240,475,'Nsibidi not standardised for everyday Igbo; used for ritual/legal texts.','middle','Ls')
    g+=t(240,484,'Modern Igbo literacy uses Latin-based Onwu orthography exclusively.','middle','Ls')
    g+=hr(492)
    g+=sh(501,'IGBO NUMERALS')
    nums=[('1','otu'),('2','abuo'),('3','ato'),('4','ano'),('5','ise'),
          ('6','isii'),('7','asaa'),('8','asato'),('9','toolu'),('10','iri')]
    for i,(n,w) in enumerate(nums):
        col=i%5; row=i//5
        x=70+col*80; y=511+row*10
        g+=t(x,y,f'{n} = {w}','middle','Lx')
    g+=t(240,531,'20 = iri abuo · 100 = otu narị · 1000 = otu puku','middle','Ls')
    g+=footer('35','Igbo','A','Script')
    return g+close_svg()

# ─── PLATE 35B — PHONOLOGY ─────────────────────────────────────────────────
def build_35b():
    g=open_svg()
    g+=t(240,32,'IGBO','middle','T')
    g+=t(240,50,'Phonology & Sound System','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    g+=t(240,82,'Igbo has ~28 consonants including labial-velar stops, nasals, and fricatives.','middle','Ls')
    cons=[('p','bilabial stop vl'),('b','bilabial stop vd'),('t','alveolar stop vl'),
          ('d','alveolar stop vd'),('k','velar stop vl'),('g','velar stop vd'),
          ('kp','/kp/ labial-velar vl'),('gb','/\u0261b/ labial-velar vd'),
          ('f','labiodental fricative'),('v','labiodental fricative vd'),
          ('s','alveolar fricative'),('z','alveolar fricative vd'),
          ('sh','/\u0283/ postalveolar'),('gh','/\u0263/ velar fricative'),
          ('h','glottal fricative'),('ch','/t\u0283/ affricate'),
          ('j','/d\u0292/ affricate'),('m','bilabial nasal'),
          ('n','alveolar nasal'),('n\u1ecb','/\u014b/ velar nasal'),
          ('l','lateral'),('r','flap /\u027e/'),('w','labio-velar approx'),('y','/j/ palatal approx')]
    for i,(c,desc) in enumerate(cons):
        col=0 if i<12 else 1
        y=92+(i if i<12 else i-12)*10
        g+=t(50+col*230,y,c,'middle','Ls'); g+=t(175+col*230,y,desc,'middle','Lx')
    g+=hr(338)
    g+=sh(347,'TONE SYSTEM — 2 OR 3 LEVELS')
    g+=t(240,357,'Igbo is a tonal language. Tone is phonemic (distinguishes meaning).','middle','Ls')
    g+=t(240,367,'High (H): \u00e1k\u01ce \u2014 chin. Low (L): \u00e0k\u01ce \u2014 door.','middle','Ls')
    g+=t(240,377,'Down-step: sequence HH in context of a preceding L lowers the second H.','middle','Ls')
    g+=t(240,387,'Tone sandhi: Low+High across word boundary may merge or shift.','middle','Ls')
    g+=t(240,397,'Verb tone patterns signal tense/aspect: \u1ecd b\u00e1 (present perfect) vs. \u1ecd b\u00e0 (stative).','middle','Ls')
    g+=hr(405)
    g+=sh(414,'VOWEL HARMONY — ATR SYSTEM')
    g+=t(240,424,'Igbo has Advanced Tongue Root (ATR) vowel harmony.','middle','Ls')
    g+=t(240,434,'+ATR set: i e u o a — tongue root pushed forward, more open pharynx.','middle','Ls')
    g+=t(240,444,'-ATR set: \u1ecb \u1ecd \u1ee5 \u2014 three vowels with dot-below.','middle','Ls')
    g+=t(240,454,'Within a word, vowels generally agree in ATR value (some exceptions).','middle','Ls')
    g+=t(240,464,'Function words may not trigger harmony; certain affixes are transparent.','middle','Ls')
    g+=hr(472)
    g+=sh(481,'LABIAL-VELAR STOPS — KEY FEATURE')
    g+=t(240,491,'GB /\u0261b/: voiced. Both lips close AND back of tongue touches velum simultaneously.','middle','Ls')
    g+=t(240,501,'KP /kp/: voiceless version. Two closures released simultaneously, not sequentially.','middle','Ls')
    g+=t(240,511,'Found across West/Central Africa (Yoruba gb/kp, Igbo gb/kp, Ewe gb/kp).','middle','Ls')
    g+=t(240,521,'English speakers often hear these as two-consonant clusters — they are single stops.','middle','Ls')
    g+=hr(529)
    g+=sh(538,'SYLLABLE STRUCTURE')
    g+=t(240,548,'Igbo syllables: V, CV, CVN (N = syllabic nasal). No complex clusters.','middle','Ls')
    g+=t(240,558,'Syllabic nasals carry tone: M!, N! (low-tone syllabic nasal + downstep).','middle','Ls')
    g+=t(240,568,'Open syllables preferred; word-final consonants rare (except nasals).','middle','Ls')
    g+=footer('35','Igbo','B','Phonology')
    return g+close_svg()

# ─── PLATE 35C — GRAMMAR ───────────────────────────────────────────────────
def build_35c():
    g=open_svg()
    g+=t(240,32,'IGBO','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE — SVO')
    g+=t(240,82,'Igbo is Subject-Verb-Object (SVO): Emeka ri-ara ji (Emeka ate yam).','middle','Ls')
    g+=t(240,92,'Verbs are central; they carry tense, aspect, and negation morphology.','middle','Ls')
    g+=t(240,102,'Subject pronouns are obligatory: m (I), i/\u1ecb (you), \u1ecd (he/she/it), any\u1ecb (we), unu (y\'all), ha (they).','middle','Ls')
    g+=hr(110)
    g+=sh(119,'VERB SYSTEM')
    g+=t(240,129,'Igbo verbs use a root + tonal pattern to signal tense/aspect.','middle','Ls')
    verbs=[('root','ri','eat'),('past imperfective','na-ar\u1ecb','was eating'),
           ('past perfective','rir\u1ecb','ate (completed)'),('present hab','na-ar\u1ecb','eats (habitually)'),
           ('future','g\u1ecb ar\u1ecb','will eat'),('stative','er-iri','have eaten'),
           ('negative','anagh\u1ecb ar\u1ecb','does not eat'),('imperative','r\u1ecb!','eat!')]
    for i,(label,form,gloss) in enumerate(verbs):
        y=139+i*10
        g+=t(90,y,label,'middle','Lx'); g+=t(230,y,form,'middle','Ls'); g+=t(370,y,gloss,'middle','Lx')
    g+=hr(225)
    g+=sh(234,'SUBJECT PRONOUNS')
    pros=[('m / m\u1ee5','I / me (emphatic: m\u1ee5)'),('\u1ecb / g\u1ecb','you (subject / emphatic)'),
          ('\u1ecd','he/she/it (3rd sg)'),('any\u1ecb','we (inclusive)'),
          ('unu','you (plural)'),('ha','they / them')]
    for i,(p,gloss) in enumerate(pros):
        y=244+i*10
        g+=t(120,y,p,'middle','L'); g+=t(310,y,gloss,'middle','Ls')
    g+=hr(310)
    g+=sh(319,'NOUN CLASSES — GENDER BY PREFIX')
    g+=t(240,329,'No grammatical gender; nouns modified by adjectives that follow: \u1ecd j\u1ecb \u1ecd b\u1ecd (the white yam).','middle','Ls')
    g+=t(240,339,'Plurals often formed by tone change or N- prefix: \u1ecd ch\u1ec7 \u2192 \u1ecd ch\u1ec7 (tree \u2192 trees by context).','middle','Ls')
    g+=t(240,349,'Classifiers used with numerals: otu oche (one chair), ise oche (five chairs).','middle','Ls')
    g+=hr(357)
    g+=sh(366,'CORE VOCABULARY')
    vocab=[('\u1ecd b\u00ed\u00e0r\u00e0','welcome'),('d\u1ecbm\u1eb9','thank you'),('\u00edc\u1eb9','yes'),
           ('m\u1ecdch\u1ecb\u0301kw\u1ee5','no'),('b\u00edko','please'),('\u1ecd d\u1ecb\u0301','good morning'),
           ('nd\u1eebu\u1ecb?','how are you?'),('a d\u1ecb m','I am fine'),
           ('a f\u1ecd\u1ee5 m g\u1ecb','I love you'),('\u1ec5\u1ec9 k\u1ecb?','what is your name?'),
           ('\u1eccch\u1ecb m b\u1ecdch\u1ecb','my name is...'),('\u1ecd b\u00e1','come'),
           ('\u1ecd ga','go'),('r\u1ecb','eat'),('\u1ecb nu n\u1ecbm','drink water'),
           ('ulo','house'),('oji','kola nut'),('ji','yam'),
           ('mmiri','water'),('oku','fire'),('ana','earth/ground'),
           ('mmad\u1ee5','person'),('oge','time'),('onwa','moon'),
           ('kpakpando','star'),('ob\u1ecb','heart'),('ihunanya','love'),
           ('ononihu','freedom'),('echeta','remember/memory'),
           ('\u1ecd z\u1ecd\u1ecd','tomorrow / future'),('elu-ala','the world')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<16 else 1
        y=376+(i if i<16 else i-16)*10
        g+=t(50+col*230,y,w,'middle','Ls'); g+=t(175+col*230,y,e,'middle','Lx')
    g+=footer('35','Igbo','C','Grammar')
    return g+close_svg()

# ─── PLATE 35D — RUNNING TEXT ──────────────────────────────────────────────
def build_35d():
    g=open_svg()
    g+=t(240,32,'IGBO','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. IG\u1ee4EKELE — GREETING / PROVERB')
    g+=t(240,80,'Onye wetara oji wetara ndu.','middle','L')
    g+=t(240,90,'onye=who wetara=brought oji=kola-nut wetara=brought ndu=life','middle','Ls')
    g+=t(240,100,'"The one who brings kola nut brings life." (Igbo ceremonial greeting proverb)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. AJA — ON MEMORY AND ANCESTORS')
    g+=t(240,128,'A na-echeta nd\u1ecb nna-ochie eme ka eze ha ndu na-aga n\'iru.','middle','L')
    g+=t(240,138,'a-na-echeta=one-remembers nd\u1ecb=those nna-ochie=ancestors','middle','Ls')
    g+=t(240,147,'eme=makes eze=their ka=so-that ha=them ndu=life na-aga=goes n\'iru=forward','middle','Ls')
    g+=t(240,157,'"Remembering the ancestors makes their life go forward." (traditional concept)','middle','F')
    g+=hr(166)
    g+=sh(175,'III. IHEM\u1eCaCHACHA — ON KNOWLEDGE')
    g+=t(240,185,'Ihe onye m\u1ecd t\u1ecb, onye ibe ya mara ya, mara ya rue na nna-ochie.','middle','Ls')
    g+=t(240,195,'ihe=thing onye=a-person m\u1ecd-t\u1ecb=knows onye-ibe=another ya=it mara=knows','middle','Ls')
    g+=t(240,205,'rue=reaches na=to nna-ochie=ancestors','middle','Ls')
    g+=t(240,215,'"What one person knows, let another know it, let it reach the ancestors." (knowledge proverb)','middle','F')
    g+=hr(224)
    g+=sh(233,'IV. ELU IHU — FORWARD MOTION')
    g+=t(240,243,'Anyị na-aga n\'iru ma anyị na-eche nd\u1ecb nd\u1ecb gara aga.','middle','L')
    g+=t(240,253,'anyị=we na-aga=go n\'iru=forward ma=while na-eche=think-of nd\u1ecb=those','middle','Ls')
    g+=t(240,263,'nd\u1ecb=people gara=went aga=ahead/forward','middle','Ls')
    g+=t(240,273,'"We go forward while thinking of those who went ahead." (guiding principle)','middle','F')
    g+=hr(282)
    g+=sh(291,'V. BRIDGE PHRASE')
    g+=t(240,304,'A kere ihe a m\u1eedzi m\u1eedzi maka g\u1ecb, n\'an\u1ecb\u1ecb, site n\'aka nd\u1ecb','middle','L')
    g+=t(240,314,'na-echeta n\'iru.','middle','L')
    g+=t(240,328,'a-kere=was-made ihe-a=this-thing m\u1eedzi-m\u1eedzi=freely maka=for g\u1ecb=you','middle','Ls')
    g+=t(240,337,'n\'an\u1ecb\u1ecb=truly site-n\'aka=from-the-hands nd\u1ecb=those na-echeta=who-remember','middle','Ls')
    g+=t(240,346,'n\'iru=forward (lit: who-face-forward)','middle','Ls')
    g+=t(240,358,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(370)
    g+=sh(379,'BRIDGE PHRASE — NOTES')
    g+=t(240,389,'N\'iru (n\'ir\u00f9) literally means "in front / forward / facing ahead."','middle','Ls')
    g+=t(240,399,'The phrase na-echeta n\'iru means "remember(s) forward" — facing ahead while','middle','Ls')
    g+=t(240,409,'honoring the past. This captures the Igbo cosmological sense that the living','middle','Ls')
    g+=t(240,419,'walk forward into the future while the ancestors walk behind, guiding them.','middle','Ls')
    g+=t(240,429,'Meedzi meedzi = completely freely / without cost (reduplication for emphasis).','middle','Ls')
    g+=hr(437)
    g+=sh(446,'LANGUAGE NOTES')
    g+=t(240,456,'Igbo: ~44 million speakers in southeastern Nigeria (Enugu, Anambra, Imo, Abia states).','middle','Ls')
    g+=t(240,466,'Language family: Niger-Congo, Volta-Niger branch. Closely related to Ika, Ekpeye.','middle','Ls')
    g+=t(240,476,'Dialects: Central Igbo (Owerri-Onitsha basis of Standard Igbo), Inland, Delta.','middle','Ls')
    g+=t(240,486,'Literary tradition since 19th century; Chinua Achebe wrote in English about Igbo life.','middle','Ls')
    g+=footer('35','Igbo','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate35a_igbo_script.svg': build_35a(),
        'plate35b_igbo_phonology.svg': build_35b(),
        'plate35c_igbo_grammar.svg': build_35c(),
        'plate35d_igbo_text.svg': build_35d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
