"""Build script — Sinhala series plates 44A–44D (Remember Forward)"""
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
            '.Lsi{font-size:11px;}\n'
            '.Lsis{font-size:8px;}\n'
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

def build_44a():
    g=open_svg()
    g+=t(240,32,'SINHALA','middle','T')
    g+=t(240,50,'\u0dc3\u0dd2\u0d82\u0dc4\u0dbd \u2014 Script (Abugida)','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM \u2014 ABUGIDA')
    g+=t(240,84,'Sinhala script: abugida derived from Brahmi via Old Sinhala (3rd century BCE).','middle','Ls')
    g+=t(240,94,'Distinctive rounded letters. Written left to right. 54 letters total.','middle','Ls')
    g+=t(240,104,'Consonants carry inherent vowel /a/. Diacritics modify or cancel the vowel.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'INDEPENDENT VOWEL LETTERS')
    vowels=[('\u0d85','a'),('\u0d86','aa'),('\u0d87','ae'),('\u0d88','aae'),
            ('\u0d89','i'),('\u0d8a','ii'),('\u0d8b','u'),('\u0d8c','uu'),
            ('\u0d8f','e'),('\u0d91','ee'),('\u0d94','o'),('\u0d96','oo')]
    for i,(s,desc) in enumerate(vowels):
        col=i%6; row=i//6
        x=45+col*68; y=131+row*14
        g+=t(x,y,s,'middle','Lsi'); g+=t(x,y+9,desc,'middle','Lx')
    g+=hr(167)
    g+=sh(176,'SELECTED CONSONANTS')
    cons=[('\u0d9a','ka'),('\u0d9c','ga'),('\u0da0','ca'),('\u0da2','ja'),
          ('\u0da7','ta'),('\u0da9','da'),('\u0daf','na'),('\u0db4','pa'),
          ('\u0db6','ba'),('\u0db8','ma'),('\u0dba','ya'),('\u0dbb','ra'),
          ('\u0dbd','la'),('\u0dc0','va'),('\u0dc3','sa'),('\u0dc4','ha'),
          ('\u0dc5','la(2)'),('\u0dc6','fa')]
    for i,(s,desc) in enumerate(cons):
        col=i%6; row=i//6
        x=45+col*68; y=186+row*14
        g+=t(x,y,s,'middle','Lsi'); g+=t(x,y+9,desc,'middle','Lx')
    g+=hr(255)
    g+=sh(264,'VOWEL DIACRITICS')
    g+=t(240,274,'Vowel diacritics (pilla) are written around the base consonant:','middle','Ls')
    diacritics=[('\u0d9a\u0dcf','ka + aa = kaa'),('\u0d9a\u0dd2','ka + i = ki'),
                ('\u0d9a\u0dd4','ka + u = ku'),('\u0d9a\u0dda','ka + ee = kee'),
                ('\u0d9a\u0dda','ka + oo variant'),('\u0d9a\u0ddf','ka + o = ko')]
    for i,(d,desc) in enumerate(diacritics):
        col=i%3; row=i//3
        x=65+col*130; y=284+row*11
        g+=t(x,y,f'{d} = {desc}','middle','Lsis')
    g+=hr(322)
    g+=sh(331,'SINHALA NUMERALS')
    g+=t(240,341,'\u0de6\u0de7\u0de8\u0de9\u0dea\u0deb\u0dec\u0ded\u0dee\u0def  (0\u20139)','middle','Lsi')
    g+=t(240,355,'Sinhala numerals used in traditional contexts; Arabic numerals in modern use.','middle','Ls')
    g+=hr(363)
    g+=sh(372,'SCRIPT HISTORY')
    g+=t(240,382,'Sinhala script: descended from Brahmi (Ashokan inscriptions ~3rd c BCE).','middle','Ls')
    g+=t(240,392,'Oldest surviving Sinhala inscriptions: ~3rd century BCE, in caves of Sri Lanka.','middle','Ls')
    g+=t(240,402,'Rounded letterforms developed through palm-leaf manuscripts (avoid leaf tearing).','middle','Ls')
    g+=t(240,412,'Sinhala script used for both Sinhala and Pali (Buddhist canonical language).','middle','Ls')
    g+=hr(420)
    g+=sh(429,'DIGLOSSIC REGISTERS')
    g+=t(240,439,'Written (Literary) Sinhala vs. Spoken (Colloquial) Sinhala differ significantly.','middle','Ls')
    g+=t(240,449,'Literary: \u0db8\u0dd0\u0db8\u0dcf \u0d9c\u0dba\u0dcf (mama gaya = I went). Spoken: \u0db8\u0db8 \u0d9c\u0dd2\u0dba\u0dcf (mama giya).','middle','Ls')
    g+=t(240,459,'Grammar, pronouns, and verb forms all differ between registers.','middle','Ls')
    g+=footer('44','Sinhala','A','Script')
    return g+close_svg()

def build_44b():
    g=open_svg()
    g+=t(240,32,'SINHALA','middle','T')
    g+=t(240,50,'Phonology \u2014 Sounds and Contrast System','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    g+=t(240,82,'Sinhala has ~34 consonants including prenasalised and aspiration distinctions.','middle','Ls')
    cons=[('p /p/','bilabial'),('b /b/','bilabial vd'),('ph /p\u02b0/','aspirated bilabial'),
          ('t /t/','dental'),('d /d/','dental vd'),('th /t\u02b0/','aspirated dental'),
          ('\u0288 /t\u0323/','retroflex vl'),('\u0256 /d\u0323/','retroflex vd'),
          ('k /k/','velar'),('g /\u0261/','velar vd'),('kh /k\u02b0/','aspirated velar'),
          ('c /t\u0255/','palatal affricate'),('j /d\u0292/','palatal affricate vd'),
          ('m /m/','bilabial nasal'),('n /n/','dental nasal'),
          ('\u0273 /n\u0331/','retroflex nasal'),('\u0272 /\u0272/','palatal nasal'),
          ('\u014b /\u014b/','velar nasal'),('l /l/','lateral'),
          ('r /r/','trill'),('v /v/','labiodental'),('s /s/','alveolar'),
          ('h /h/','glottal')]
    for i,(c,desc) in enumerate(cons):
        col=i%3; row=i//3
        x=65+col*130; y=92+row*10
        g+=t(x,y,f'{c} {desc}','middle','Lx')
    g+=hr(258)
    g+=sh(267,'VOWEL SYSTEM \u2014 SHORT AND LONG')
    g+=t(240,277,'Sinhala has contrastive vowel length (short vs. long pairs):','middle','Ls')
    vowels=[('a /a/ vs aa /a\u02d0/','open central: ata (eight) vs aata (eight [formal])'),
            ('i /i/ vs ii /i\u02d0/','high front: ithin (from here) vs iitin'),
            ('u /u/ vs uu /u\u02d0/','high back: uda (up) vs uuda (plough)'),
            ('e /e/ vs ee /e\u02d0/','mid-front: ela (it went) vs eela (arrow)'),
            ('o /o/ vs oo /o\u02d0/','mid-back: oda (bed) vs ooda (boat)')]
    for i,(v,desc) in enumerate(vowels):
        y=287+i*11
        g+=t(120,y,v,'middle','Ls'); g+=t(340,y,desc,'middle','Lx')
    g+=hr(355)
    g+=sh(364,'PRENASALISED STOPS')
    g+=t(240,374,'Sinhala has phonemic prenasalised stops: /\u1e47d/ /\u1e47b/ /\u1e45\u0261/ etc.','middle','Ls')
    g+=t(240,384,'anda (cry) vs. ada (today). Prenasalised = nasal+stop as single phoneme.','middle','Ls')
    g+=hr(392)
    g+=sh(401,'STRESS AND SYLLABLE STRUCTURE')
    g+=t(240,411,'Stress: generally on the first syllable of a root. Not phonemic.','middle','Ls')
    g+=t(240,421,'Syllable structure: (C)(C)V(V)(C)(C). Allows complex clusters.','middle','Ls')
    g+=t(240,431,'Sinhala underwent significant changes isolating it from other Indo-Aryan languages.','middle','Ls')
    g+=footer('44','Sinhala','B','Phonology')
    return g+close_svg()

def build_44c():
    g=open_svg()
    g+=t(240,32,'SINHALA','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE \u2014 SOV')
    g+=t(240,82,'Sinhala is Subject-Object-Verb (SOV). Verb is always final.','middle','Ls')
    g+=t(240,92,'Mama bata kanna. I rice eat. (mama=I bata=rice kanna=eat-INF)','middle','Ls')
    g+=t(240,102,'Colloquial: Mama bat kanna. (shorter form, vowel reduction)','middle','Ls')
    g+=hr(110)
    g+=sh(119,'CASE SYSTEM')
    g+=t(240,129,'Sinhala has 7 cases marked by suffixes on nouns:','middle','Ls')
    cases=[('Nominative','-\u00f8 / -a','subject: minisa (the man)'),
           ('Accusative','-va / -ta','object: minisata (to the man)'),
           ('Dative','-ta / -ge','for/to: minisage (man\'s)'),
           ('Genitive','-ge / -lagin','of: minisalagin (from the man)'),
           ('Ablative','-lagin','from: lamaya lagin (from the child)'),
           ('Instrumental','-gen','by/with: minisagen (by the man)'),
           ('Locative','-ee / -hi','at/in: gamahe (in the village)')]
    for i,(case,suffix,ex) in enumerate(cases):
        y=139+i*11
        g+=t(90,y,case,'middle','Ls'); g+=t(170,y,suffix,'middle','Ls'); g+=t(340,y,ex,'middle','Lx')
    g+=hr(225)
    g+=sh(234,'VERB SYSTEM')
    g+=t(240,244,'Verbs agree with subject in person, number, and gender.','middle','Ls')
    verbs=[('kanna','eat (infinitive)'),('kamin inne','is eating (progressive)'),
           ('kae-va','ate (past)'),('kanava','eats (present habitual)'),
           ('kamin yavi','will be eating'),('nokana','does not eat (negative)')]
    for i,(form,gloss) in enumerate(verbs):
        y=254+i*10
        g+=t(120,y,form,'middle','L'); g+=t(310,y,gloss,'middle','Ls')
    g+=hr(325)
    g+=sh(334,'CORE VOCABULARY')
    vocab=[('\u0d85\u0dba\u0dd2\u0dba\u0dca\u0db6\u0dbd','hello (\u0d85\u0dba\u0dd2\u0dba\u0dca\u0db6\u0dbd)'),
           ('\u0dc3\u0dca\u0dad\u0dd4\u0dad\u0dd2\u0dba\u0dd2','thank you'),
           ('\u0d94\u0d85 \u0dbd\u0dda','yes'),('\u0db1\u0dda','no'),
           ('\u0d9a\u0db1\u0ddd \u0d9a\u0dbb\u0dba\u0dd2','excuse me'),
           ('oya kohomada?','how are you?'),('mama honda tama','I am fine'),
           ('mama oyata adare karanava','I love you'),
           ('vatura','water'),('gini','fire'),('bhumi','earth'),
           ('minisa','person'),('kaalaya','time'),('sandha','moon'),
           ('taruva','star'),('hitha','heart'),('adara','love'),
           ('nidahas','freedom'),('smarana','memory'),
           ('anagatha','future'),('lokaya','world'),('jiwithe','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<12 else 1
        y=344+(i if i<12 else i-12)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('44','Sinhala','C','Grammar')
    return g+close_svg()

def build_44d():
    g=open_svg()
    g+=t(240,32,'SINHALA','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. WACHANA \u2014 PROVERB')
    g+=t(240,80,'\u0d9c\u0dd9\u0daf\u0dbb \u0d9c\u0dc3\u0dca\u0dc3\u0dd9\u0db1\u0dca \u0db4\u0dd9\u0db1\u0dd9\u0db1\u0dca\u0db1\u0da7 \u0d91\u0dba\u0dca \u0dba\u0dcf\u0dba\u0dd2.','middle','Lsi')
    g+=t(240,94,'gedara gassenin penennaata ey yayi = home from-outside trying-to-see only go','middle','Ls')
    g+=t(240,104,'"[Do not try to] understand your own home only from the outside." (Sinhala proverb on wisdom)','middle','F')
    g+=hr(113)
    g+=sh(122,'II. SMARANA \u2014 ON MEMORY')
    g+=t(240,132,'\u0d8a\u0dad\u0da7 \u0d9c\u0dd2\u0dba \u0d89\u0dad\u0dd2\u0dc4\u0dcf\u0dc3\u0dba \u0db4\u0dd2\u0dbd\u0dd2\u0d9a\u0dda \u0d9a\u0dbb\u0db1\u0dca\u0db1\u0da7 \u0d86\u0d9a\u0dcf\u0dbb\u0dba\u0dca','middle','Lsi')
    g+=t(240,146,'iyata giya ithihasaya pililikee karannaata aakaara = those who-went history to-reflect way','middle','Ls')
    g+=t(240,156,'"The way to illuminate history is to reflect on those who have gone before us."','middle','F')
    g+=hr(165)
    g+=sh(174,'III. JNANA \u2014 ON KNOWLEDGE')
    g+=t(240,184,'\u0d9c\u0dd2\u0dba\u0dcf\u0dc0\u0dd3\u0db1\u0dca \u0d9a\u0d9c\u0dd9\u0db1\u0dca \u0dc4\u0dd0\u0dba\u0dd2\u0dba\u0dcf\u0db8 \u0dbd\u0dca\u0dbd\u0dcf\u0da8\u0dca\u0dba\u0dd9\u0db1\u0dca','middle','Lsi')
    g+=t(240,198,'giyavin kagen haeyiyaa llaadyen = from those-who-went lighting burning = light taken from past','middle','Ls')
    g+=t(240,208,'"The light is taken from those who have gone before." (Sinhala saying on inherited wisdom)','middle','F')
    g+=hr(217)
    g+=sh(226,'IV. ANUWA \u2014 FORWARD')
    g+=t(240,236,'\u0d86\u0db4\u0dd2 \u0d89\u0daf\u0dd2\u0dbb\u0dd2\u0dba\u0da7 \u0dba\u0db1\u0dca\u0db1\u0da7 \u0d8a\u0dad\u0da7 \u0d9c\u0dd2\u0dba\u0dc0\u0dd4\u0db1\u0dca \u0dc3\u0dca\u0db8\u0dbb\u0db1 \u0d9a\u0dbb\u0db1\u0dcf','middle','Lsi')
    g+=t(240,250,'aapit idiriyata yannata iitaata giyavun smarana karana','middle','Ls')
    g+=t(240,260,'"While moving forward together, remembering those who went ahead." (guiding concept)','middle','F')
    g+=hr(269)
    g+=sh(278,'V. BRIDGE PHRASE')
    g+=t(240,290,'\u0db8\u0db8 \u0db8\u0dd3\u0dba \u0d89\u0daf\u0dd2\u0dbb\u0dd2\u0dba\u0da7 \u0d9a\u0dba\u0dcf \u0d9a\u0dbb\u0db1\u0dca\u0dbd\u0da7 \u0dc3\u0dca\u0db8\u0dbb\u0db1 \u0d9a\u0dbb\u0db1 \u0d9c\u0dbc\u0dba\u0db1\u0dca\u0da7','middle','Lsi')
    g+=t(240,304,'\u0db8\u0dd3\u0dba \u0d92\u0db6\u0da7 \u0db1\u0dd2\u0dbb\u0dcd\u0db8\u0dda\u0dc5\u0dd2\u0dba \u0d9a\u0dbb\u0dda\u0dc5\u0dd2.','middle','Lsi')
    g+=t(240,320,'mama mee idiiriyata kaya karanlaata smarana kara giyanta','middle','Ls')
    g+=t(240,329,'mee oba ata nirmela kereeli = this for-you freely was-made','middle','Ls')
    g+=t(240,341,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(352)
    g+=sh(361,'BRIDGE PHRASE \u2014 NOTES')
    g+=t(240,371,'Idiriya (\u0d89\u0daf\u0dd2\u0dbb\u0dd2\u0dba) = forward/front/ahead. Nirmela = free of charge/pure/free.','middle','Ls')
    g+=t(240,381,'Sinhala SOV structure places the main verb at the end: subject + object + verb.','middle','Ls')
    g+=t(240,391,'The forward-memory concept in Sinhala connects to Buddhist concept of karmic continuity.','middle','Ls')
    g+=hr(399)
    g+=sh(408,'LANGUAGE NOTES')
    g+=t(240,418,'Sinhala: ~17 million L1 speakers; official language of Sri Lanka.','middle','Ls')
    g+=t(240,428,'Language family: Indo-European, Indo-Aryan, insular branch (isolated from mainland).','middle','Ls')
    g+=t(240,438,'Settled in Sri Lanka ~5th century BCE from northern India. Rich Pali Buddhist tradition.','middle','Ls')
    g+=t(240,448,'Sinhala diverged significantly from other Indo-Aryan languages due to island isolation.','middle','Ls')
    g+=footer('44','Sinhala','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate44a_sinhala_script.svg': build_44a(),
        'plate44b_sinhala_phonology.svg': build_44b(),
        'plate44c_sinhala_grammar.svg': build_44c(),
        'plate44d_sinhala_text.svg': build_44d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
