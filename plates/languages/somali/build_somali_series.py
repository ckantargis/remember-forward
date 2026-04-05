#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Somali plate series 32A–32D for Remember Forward."""
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

def build_32a():
    g=open_svg()
    g+=t(240,32,'SOMALI \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g+=t(240,50,'SERIES 32A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SOMALI \u2014 CUSHITIC \u00b7 ~25 MILLION SPEAKERS')
    g+=t(240,79,'Somali is a Cushitic language (Afroasiatic family) \u2014 related to Oromo, Afar, and distantly to Arabic.','middle','L')
    g+=t(240,89,'Spoken in Somalia, Djibouti, Ethiopia (Ogaden region), Kenya, and diaspora worldwide.','middle','Ls')
    g+=t(240,98,'Official script: Osmanya (traditional) + Latin-based Somali Orthography (official since 1972).','middle','Ls')
    g+=hr(106)
    g+=sh(115,'OFFICIAL SOMALI LATIN ALPHABET \u2014 26 LETTERS')
    g+=t(240,125,'The 1972 standardised Somali orthography uses 26 Latin letters with NO diacritics.','middle','Ls')
    g+=t(240,134,'All sounds represented by plain letters or digraphs. Tones NOT marked in standard orthography.','middle','Ls')
    letters=[
        ('A a','/a\u02d0/','long or short a'),('B b','/b/','bilabial stop'),('C c','/\u02bf/','pharyngeal fricative (NOT /k/)'),
        ('D d','/d/','alveolar stop (retroflex in some dialects)'),('DH dh','/\u0256/','retroflex d'),
        ('E e','/e\u02d0/','mid front'),('F f','/f/','labiodental'),('G g','/\u0261/','velar stop'),
        ('H h','/h/','glottal'),('I i','/i\u02d0/','high front'),('J j','/d\u0292/','affricate'),
        ('K k','/k/','velar stop'),('KH kh','/x/','velar fricative \u2014 like German Bach'),
        ('L l','/l/','lateral'),('M m','/m/','nasal'),('N n','/n/','nasal'),
        ('O o','/o\u02d0/','mid back'),('Q q','/q/','uvular stop \u2014 deeper than k'),
        ('R r','/r/','alveolar trill / flap'),('S s','/s/','alveolar fricative'),
        ('SH sh','/\u0283/','palatal fricative'),('T t','/t/','alveolar stop'),
        ('U u','/u\u02d0/','high back'),('W w','/w/','glide'),('X x','/\u0127/','pharyngeal fricative (like Arabic H)'),
        ('Y y','/j/','palatal glide'),
    ]
    for i,(ltr,ipa,note) in enumerate(letters):
        col=0 if i<14 else 1
        y=144+(i if i<14 else i-14)*10
        cx=[30,90,175] if col==0 else [260,315,395]
        g+=t(cx[0],y,ltr,'middle','Lx'); g+=t(cx[1],y,ipa,'middle','Lx'); g+=t(cx[2],y,note,'middle','Lx')
    g+=hr(291)
    g+=sh(300,'PHARYNGEAL AND UVULAR CONSONANTS')
    g+=t(240,311,'C = /\u02bf/ pharyngeal approximant (voiced). Found in Semitic/Cushitic \u2014 like Arabic \u02beayn.','middle','Ls')
    g+=t(240,320,'X = /\u0127/ pharyngeal fricative (voiceless). Like Arabic H with friction. cayn vs xayn.','middle','Ls')
    g+=t(240,329,'Q = /q/ uvular stop \u2014 further back in the throat than /k/: qof (person), qalbi (heart).','middle','Ls')
    g+=t(240,338,'DH = /\u0256/ retroflex d \u2014 tongue tip curled back: dhul (land), dhowr (several).','middle','Ls')
    g+=hr(346)
    g+=sh(355,'OSMANYA SCRIPT \u2014 TRADITIONAL SOMALI WRITING')
    g+=t(240,366,'Osmanya script: invented 1920s by Osman Yusuf Kenadid. 22 letters, left to right. Unicode block U+10480.','middle','Ls')
    g+=t(240,375,'Used for Somali before 1972 standardisation. Still used in some communities and Unicode (U+10480).','middle','Ls')
    g+=t(240,384,'Other historical scripts: Wadaad (Arabic-based Ajami), Borama, Kaddare \u2014 all pre-1972.','middle','Ls')
    g+=footer('32','Somali','A','Script')
    return g+close_svg()

def build_32b():
    g=open_svg()
    g+=t(240,32,'SOMALI \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g+=t(240,50,'SERIES 32B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'TONE \u2014 PITCH-ACCENT SYSTEM')
    g+=t(240,79,'Somali has a PITCH-ACCENT system: words have a tonal pattern but it is not a full tone language.','middle','L')
    g+=t(240,89,'Two tone levels (High H and Low L). The accent position changes meaning.','middle','Ls')
    g+=t(240,98,'niin (L-H) "date palm" vs niin (H-L) "woman" \u2014 same consonants, different tones, different meanings.','middle','Ls')
    g+=t(240,107,'Tone is not marked in official orthography \u2014 learned from context and oral tradition.','middle','Ls')
    g+=hr(115)
    g+=sh(124,'VOWEL SYSTEM \u2014 5 SHORT + 5 LONG')
    g+=t(240,135,'Vowel length is phonemic: short vs long changes meaning.','middle','L')
    pairs=[('/a/ vs /a\u02d0/','a vs aa','bad (go-past) vs baad (you go)'),
           ('/e/ vs /e\u02d0/','e vs ee','ber (garden, obs.) vs beer (garden)'),
           ('/i/ vs /i\u02d0/','i vs ii','bir (iron) vs biir (grain measure)'),
           ('/o/ vs /o\u02d0/','o vs oo','gob (noble) vs goob (place)'),
           ('/u/ vs /u\u02d0/','u vs uu','bur (flour) vs buur (mountain)')]
    for i,(ipa,boko,ex) in enumerate(pairs):
        y=145+i*12
        g+=t(80,y,ipa,'middle','Lx'); g+=t(180,y,boko,'middle','Lx'); g+=t(360,y,ex,'middle','Lx')
    g+=hr(210)
    g+=sh(219,'CONSONANT INVENTORY \u2014 22 CONSONANTS')
    cons=[('b d g','voiced stops','bilabial, alveolar, velar'),
          ('t k q','voiceless stops','alveolar, velar, uvular'),
          ('dh','/\u0256/ retroflex','tongue tip curled back'),
          ('f s sh kh','fricatives','labio-dental, alveolar, palatal, velar'),
          ('c x','pharyngeals','/\u02bf/ voiced, /\u0127/ voiceless'),
          ('h','/h/','glottal'),
          ("'",'/\u0294/','glottal stop: aa\u2019ad (you)'),
          ('j','/d\u0292/','affricate'),
          ('m n','nasals','bilabial, alveolar'),
          ('l r','lateral / rhotic',''),
          ('w y','glides','labio-velar, palatal')]
    for i,(ltr,ipa,note) in enumerate(cons):
        y=229+i*12
        g+=t(55,y,ltr,'middle','Ls'); g+=t(115,y,ipa,'middle','Lx'); g+=t(310,y,note,'middle','Lx')
    g+=hr(364)
    g+=sh(373,'SYLLABLE STRUCTURE AND GEMINATION')
    g+=t(240,384,'Somali syllables: CV, CVC, CVV (long vowel). Consonant clusters uncommon.','middle','Ls')
    g+=t(240,393,'Geminate (doubled) consonants are phonemic: guri (house) vs gurri (to fold).','middle','Ls')
    g+=t(240,402,'Word structure: typically C-V-(C) with productive suffixation for case, gender, definiteness.','middle','Ls')
    g+=footer('32','Somali','B','Phonology')
    return g+close_svg()

def build_32c():
    g=open_svg()
    g+=t(240,32,'SOMALI \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,50,'SERIES 32C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(68,'SOV \u2014 CASE SYSTEM \u2014 FOCUS MARKING')
    g+=t(240,79,'Somali is SOV with a complex system of case, gender, focus, and definiteness.','middle','L')
    g+=t(240,89,'Two genders: masculine and feminine. Definiteness marked by suffixes: -ka (M def), -ta (F def).','middle','Ls')
    g+=t(240,98,'FOCUS: a critical feature \u2014 subject and object can be marked with focus particles changing emphasis.','middle','Ls')
    g+=hr(106)
    g+=sh(115,'CASES AND DEFINITENESS')
    cases=[('Absolute (indef.)','No suffix','nin (a man), naag (a woman)'),
           ('Nominative (def.)','M: -ku / -ka\u00a0\u00a0 F: -tu / -ta','ninku (the man [subj]), naagtu (the woman)'),
           ('Genitive','M: -ka\u00a0\u00a0 F: -ta','guriga ninka (the man\'s house)'),
           ('Dative','M: -ka\u00a0\u00a0 F: -ta + -nimo','give TO the man'),
           ('Locative','-ka / -ta','in the house: guriga (the house + loc)')]
    for i,(case,form,ex) in enumerate(cases):
        y=125+i*14
        g+=t(85,y,case,'middle','Lx'); g+=t(215,y,form,'middle','Lx'); g+=t(375,y,ex,'middle','Lx')
    g+=hr(198)
    g+=sh(207,'VERB CONJUGATION \u2014 yiri "said"')
    g+=t(240,218,'Somali verbs are highly complex \u2014 they inflect for tense, aspect, mood, person, number, gender, and focus.','middle','Ls')
    conj=[('Aniga','I','waxaan'),('Adiga','you','waxaad'),('Isaga','he','wuxuu'),
          ('Iyada','she','waxay'),('Annaga','we','waxaynu'),('Idinka','you pl','waxaydin'),
          ('Iyaga','they','waxay')]
    g+=t(55,228,'Subject','middle','Lx'); g+=t(130,228,'Pronoun','middle','Lx'); g+=t(240,228,'Focus+aux (present)','middle','Lx')
    for i,(subj,eng,focus) in enumerate(conj):
        y=237+i*11
        g+=t(55,y,subj,'middle','Ls'); g+=t(130,y,eng,'middle','Lx'); g+=t(240,y,focus,'middle','Ls')
    g+=hr(316)
    g+=sh(325,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[('haa / maya','yes / no'),('aniga / adiga','I / you'),
           ('tan / taas','this / that'),('xaggee?','where'),
           ('maxay?','what'),('cidee?','who'),('goorma?','when'),
           ('maxaa yeelay?','why'),('biyo','water'),('dab','fire'),
           ('dhul','land/earth'),('qof','person'),('buug','book'),
           ('waqti','time'),('dayax','moon'),('xiddig','star'),
           ('qalbi','heart'),('jacayl','love'),('xorriyad','freedom'),
           ('xusuus','memory'),('mustaqbal','future'),('adduunyo','world'),
           ('wanaagsan / xun','good / bad'),('wax kasta','everything'),('nolol','life')]
    for i,(so,en) in enumerate(vocab):
        col=0 if i<13 else 1; y=335+(i if i<13 else i-13)*10
        g+=t(50+col*230,y,so,'middle','Ls'); g+=t(175+col*230,y,en,'middle','Lx')
    g+=hr(468)
    g+=sh(477,'FOCUS SYSTEM')
    g+=t(240,488,'Somali distinguishes SUBJECT FOCUS (waa), OBJECT/VERB FOCUS (baa/ayaa), and NON-VERBAL sentences.','middle','Ls')
    g+=t(240,497,'Ninku wuu tegay (the man went \u2014 neutral) vs Ninku buu tegay (the MAN went \u2014 subject focus).','middle','Ls')
    g+=t(240,506,'This is one of the most complex focus systems in any language.','middle','Ls')
    g+=footer('32','Somali','C','Grammar')
    return g+close_svg()

def build_32d():
    g=open_svg()
    g+=t(240,32,'SOMALI \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,50,'SERIES 32D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(58)
    g+=sh(67,'PASSAGE 1 \u2014 SOMALI PROVERB')
    g+=t(240,78,'Aqoon la\'aani waa iftiin la\'aan.','middle','L')
    g+=t(240,88,'Knowledge lacking  is  light   lacking.','middle','Lx')
    g+=t(240,97,'"Lack of knowledge is lack of light." \u2014 On the value of education.','middle','Ls')
    g+=hr(105)
    g+=sh(113,'PASSAGE 2 \u2014 SOMALI PROVERB')
    g+=t(240,124,'Nin baa nin tira, waa ka dheer tahay.','middle','L')
    g+=t(240,134,'Man counts man,  is  him  taller  is.','middle','Lx')
    g+=t(240,143,'"A person is made by other people." \u2014 On the social nature of humanity.','middle','Ls')
    g+=hr(151)
    g+=sh(159,'PASSAGE 3 \u2014 TRADITIONAL SAYING')
    g+=t(240,170,'Guri walaal leh kuma sugo xumaan.','middle','L')
    g+=t(240,180,'Home siblings has  not-waits evil.','middle','Lx')
    g+=t(240,189,'"Evil does not wait in a house with siblings." \u2014 On family protection and unity.','middle','Ls')
    g+=hr(197)
    g+=sh(205,'PASSAGE 4 \u2014 ON MEMORY AND TIME')
    g+=t(240,216,'Waayo\u2019arag waa aqoon.','middle','L')
    g+=t(240,226,'Experience  is  knowledge.','middle','Lx')
    g+=t(240,235,'"Experience is knowledge." \u2014 What is lived and remembered becomes wisdom.','middle','Ls')
    g+=hr(243)
    g+=sh(251,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g+=t(240,263,'Farriintani waxaa loogu talagalay adiga, bilaash ahaan, dadkii xusuustay mustaqbalka.','middle','L')
    g+=t(240,274,'Message-this  was-made-for  you,   free  being,  people-who remembered  future-the.','middle','Lx')
    g+=t(240,284,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g+=hr(292)
    g+=sh(301,'LANGUAGE NOTE \u2014 "FUTURE" IN SOMALI')
    g+=t(240,312,'mustaqbal: "future" \u2014 borrowed from Arabic mustaqbal "what is received / coming toward one".','middle','L')
    g+=t(240,322,'The Arabic root q-b-l means "to face / to receive" \u2014 the future as what approaches and is received.','middle','Ls')
    g+=t(240,331,'xusuus: "memory / remembrance" \u2014 from Arabic dhikr/khuss root via Somali adaptation.','middle','Ls')
    g+=t(240,340,'bilaash: "free / for free" \u2014 borrowed from Arabic bilash "without cost".','middle','Ls')
    g+=t(240,349,'waxaa: focus-auxiliary particle \u2014 signals object/action focus in the sentence structure.','middle','Ls')
    g+=hr(357)
    g+=sh(366,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g+=t(240,377,'Somali is spoken by ~25 million people in Somalia, Djibouti, Ethiopia, and Kenya.','middle','Ls')
    g+=t(240,386,'It is a Cushitic language (Afroasiatic) \u2014 related to Oromo, Afar, and distantly to Arabic.','middle','Ls')
    g+=t(240,395,'Script: standard Latin-based orthography (since 1972). No diacritics \u2014 see Plate 32A for letter values.','middle','Ls')
    g+=t(240,404,'Key sounds not in English: C (/\u02bf/), X (/\u0127/), Q (/q/) \u2014 all produced in the throat.','middle','Ls')
    g+=t(240,413,'Somali has one of the most complex grammatical focus systems of any known language.','middle','Ls')
    g+=footer('32','Somali','D','Text')
    return g+close_svg()

def main():
    plates={'plate32a_somali_script.svg':build_32a(),'plate32b_somali_phonology.svg':build_32b(),
            'plate32c_somali_grammar.svg':build_32c(),'plate32d_somali_text.svg':build_32d()}
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8'); print(f'Written: {OUT/fname}')

if __name__=='__main__': main()
