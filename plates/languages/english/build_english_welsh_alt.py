#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build English / Welsh alt plates 48A–48D for Remember Forward.
Secondary: Welsh (Cymraeg) — ~800K speakers in Wales, within 500mi of London.
Oldest vernacular literary tradition in Western Europe after Latin/Greek.
"""
from pathlib import Path
OUT = Path(__file__).parent

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def open_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n  text{font-family:Georgia,serif;}\n'
        '  .T{font-size:11px;font-weight:bold;letter-spacing:1.5px}\n'
        '  .S{font-size:6.5px;letter-spacing:1.5px}\n'
        '  .H{font-size:6.5px;font-weight:bold;letter-spacing:2.5px}\n'
        '  .Hb{font-size:7px;font-weight:bold;letter-spacing:2px}\n'
        '  .L{font-size:7px} .Ls{font-size:6px} .Lx{font-size:5.5px}\n'
        '  .M{font-size:6px;letter-spacing:1px}\n'
        '  .F{font-size:7px;font-style:italic} .Fb{font-size:7.5px;font-weight:bold}\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n')
def close_svg(): return '</svg>\n'
def t(x,y,s,a='middle',c='L'): return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}">{esc(s)}</text>\n'
def hr(y,x1=20,x2=460,sw=0.3): return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'
def sh(y,txt): return t(240,y,f'\u2014 {txt} \u2014','middle','H')
def div(y,lbl):
    return (hr(y,sw=1.5)+f'<rect x="20" y="{y+3}" width="440" height="14" fill="black"/>\n'
        +f'<text x="240" y="{y+13}" text-anchor="middle" class="Hb" fill="white">{esc(lbl)}</text>\n'+hr(y+17,sw=0.3))
def foot(num,l1,l2,let,desc):
    return (hr(625)+t(240,620,f'PLATE {num}{let} ALT \u00b7 {l1}/{l2} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        +hr(633)+t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        +t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))

BN='48'; L1='ENGLISH'; L2='WELSH'

def build_48a_alt():
    g=open_svg()
    g+=t(240,30,'ENGLISH + WELSH \u2014 SCRIPT \u00b7 WRITING SYSTEMS','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 48A \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'ENGLISH \u2014 LATIN ALPHABET \u00b7 26 LETTERS \u00b7 IRREGULAR SPELLING')
    g+=t(240,73,'English uses 26 Latin letters but spelling is famously irregular: 44 phonemes mapped to 26 letters + digraphs.','middle','Ls')
    g+=t(240,82,'Historical layers: Old English (Germanic), Norman French, Latin/Greek scientific vocabulary.','middle','Lx')
    g+=t(240,91,'No official governing body. Spelling standardized ~1750 by Dr Johnson\'s Dictionary. American/British variants.','middle','Lx')
    g+=hr(99)
    g+=sh(107,'ENGLISH \u2014 KEY DIGRAPHS AND SOUND-SPELLING MISMATCHES')
    digraphs=[('th','/\u03b8/ or /\u00f0/','voiceless (think) or voiced (the) \u2014 same spelling'),
              ('sh','/\u0283/','always the same sound: ship, rush'),('ch','/t\u0283/ /k/ /\u0283/','church, chorus, chef \u2014 three sounds'),
              ('gh','/f/, silent, /g/','enough, night, ghost \u2014 three behaviors'),('ph','/f/','phone: Greek-origin words'),
              ('ough','/\u0254:/ /u:/ /\u028c/ /\u0251:/ /\u0252f/','through, though, tough, thought, thorough \u2014 5 sounds, 1 spelling'),
              ('wr-','/r/','write, wrong: silent w (Old English)'),('kn-','/n/','know, knight: silent k (Old English)')]
    for i,(dg,ipa,note) in enumerate(digraphs):
        y=116+i*10
        g+=t(55,y,dg,'middle','Ls'); g+=t(110,y,ipa,'middle','Lx'); g+=t(310,y,note,'middle','Lx')
    g+=hr(202)
    g+=sh(210,'ENGLISH ALPHABET \u2014 ORIGIN NOTES')
    g+=t(240,220,'26 letters via Latin \u2192 Old English runes/Latin \u2192 Norman French scribes \u2192 printing press (1476).','middle','Ls')
    g+=t(240,229,'Letters eliminated: thorn \u00de (th), wynn \u01bf (w), eth \u00f0, yogh \u021d \u2014 Old English letters lost after Norman Conquest.','middle','Lx')
    g+=t(240,238,'English: ~1.5 billion speakers worldwide. Most-studied second language in history.','middle','Lx')
    g+=div(249,'WELSH (CYMRAEG) \u00b7 SCRIPT \u00b7 28-LETTER LATIN ALPHABET')
    g+=t(240,281,'Welsh uses Latin script with digraphs counted as single letters. 28 letters total.','middle','Ls')
    g+=t(240,290,'Welsh alphabet: a b c ch d dd e f ff g ng h i j l ll m n o p ph r rh s t th u w y','middle','L')
    g+=t(240,300,'No k, q, v, x, z in Welsh (except loanwords). 8 digraphs: ch dd ff ng ll ph rh th.','middle','Lx')
    g+=hr(307)
    g+=sh(315,'WELSH DIGRAPHS \u2014 THE DISTINCTIVE SOUNDS')
    welsh_dig=[('ll','/\u026c/','voiceless lateral fricative \u2014 no English equivalent. Place tongue for l, breathe out sides.'),
               ('ch','/x/','velar fricative, like Scottish "loch" or German "Bach."'),
               ('dd','/\u00f0/','voiced dental fricative \u2014 like English "the."'),
               ('ff','/f/','like English "f." Single f = /v/ in Welsh.'),
               ('rh','/r\u0325/','voiceless r \u2014 breathed r, like r + h blend.'),
               ('ng','/\u014b/','like English "sing." Can appear word-initially in Welsh.'),
               ('th','/\u03b8/','like English "thin" \u2014 always voiceless in Welsh.'),
               ('ph','/f/','like ff, used in mutations: ei phen (her head).')]
    for i,(dg,ipa,note) in enumerate(welsh_dig):
        y=324+i*10
        g+=t(40,y,dg,'middle','Ls'); g+=t(80,y,ipa,'middle','Lx'); g+=t(290,y,note,'middle','Lx')
    g+=hr(410)
    g+=sh(418,'WELSH CONSONANT MUTATIONS \u2014 KEY FEATURE')
    g+=t(240,428,'Welsh mutates initial consonants based on grammar. 4 mutation types: soft, nasal, aspirate, mixed.','middle','Ls')
    g+=t(240,437,'Soft mutation: p\u2192b\u2192f / t\u2192d\u2192dd / c\u2192g\u2192ng / b\u2192f / d\u2192dd / g\u2192\u2205 (zero!).','middle','Lx')
    g+=t(240,446,'cat (cat) \u2192 fy nghath (my cat) / dy gath (your cat) / ei cath (her cat). Same word, 3 forms.','middle','Lx')
    g+=t(240,455,'Mutations carry grammatical information: possessor gender, preposition type, sentence role.','middle','Lx')
    g+=foot(BN,L1,L2,'A','Script')
    return g+close_svg()

def build_48b_alt():
    g=open_svg()
    g+=t(240,30,'ENGLISH + WELSH \u2014 PHONOLOGY \u00b7 SOUND SYSTEMS','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 48B \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'ENGLISH \u2014 VOWEL SYSTEM (GENERAL AMERICAN)')
    g+=t(240,73,'English has ~14\u201320 vowel phonemes depending on dialect \u2014 one of the largest inventories in Europe.','middle','Ls')
    eng_vowels=[('/i:/','"ee"','feet, sea'),('/\u026a/','"ih"','sit, bit'),('/e/','"eh"','bed, set'),('/\u00e6/','"aa"','cat, bad'),
                ('/\u0251:/','"ah"','father, spa'),('/\u0254:/','"aw"','thought, law'),('/o\u028a/','"oh"','go, boat'),('/u:/','"oo"','food, blue'),
                ('/\u028a/','"uh"','put, book'),('/\u028c/','"uh"','cup, but'),('/\u025c:/','"ur"','bird, her'),('/\u0259/','"uh"','about (schwa)')]
    for i,(ipa,approx,ex) in enumerate(eng_vowels):
        col=i//6; row=i%6; y=82+row*10; x0=20+col*235
        g+=t(x0+10,y,ipa,'start','Lx'); g+=t(x0+70,y,approx,'start','Lx'); g+=t(x0+120,y,ex,'start','Lx')
    g+=hr(147)
    g+=sh(155,'ENGLISH \u2014 CONSONANTS \u00b7 NOTABLE FEATURES')
    g+=t(240,165,'/\u03b8/ and /\u00f0/: dental fricatives unique to English among major world languages.','middle','Ls')
    g+=t(240,174,'/r/ = approximant /\u0279/ in most varieties. /h/ weakening in many dialects. /\u014b/ only medial/final.','middle','Lx')
    g+=t(240,183,'No tonal distinctions. Stress accent: variable, not fixed. Rhythm: stress-timed (not syllable-timed).','middle','Lx')
    g+=div(194,'WELSH (CYMRAEG) \u00b7 PHONOLOGY \u00b7 SOUND SYSTEM')
    g+=t(240,226,'Welsh phonology: notable for voiceless resonants, lateral fricative /\u026c/ (ll), and pitch accent in some dialects.','middle','Ls')
    g+=hr(233)
    g+=sh(241,'WELSH VOWELS \u2014 7 + LENGTH')
    g+=t(240,251,'Vowels: /a e \u025b i o \u028a \u0259/ \u2014 each has short and long form. Length marked with circumflex \u00e2 \u00ea \u00ee \u00f4 \u00fb \u0175 \u0177.','middle','Ls')
    g+=t(240,260,'Long vowels: m\u00e2n (fine) vs. man (place) \u2014 circumflex signals vowel length (to bach = little hat).','middle','Lx')
    g+=t(240,269,'w and y function as vowels: cwm /k\u028am/ (valley), dyn /d\u0268n/ (man), bwrdd /b\u028ard/ (table).','middle','Lx')
    g+=hr(276)
    g+=sh(284,'WELSH \u2014 DISTINCTIVE CONSONANTS')
    w_cons=[('/\u026c/ ll','voiceless lateral fricative \u2014 one of Welsh\u2019s most recognized sounds'),
            ('/r\u0325/ rh','voiceless rhotic \u2014 aspirated r, unique in Celtic languages'),
            ('/x/ ch','velar fricative \u2014 like Scottish "loch"'),
            ('/\u0263/ in dialects','voiced velar fricative in some north Welsh pronunciation'),
            ('/m\u0329 n\u0329/','syllabic nasals in some clusters'),]
    for i,(sym,note) in enumerate(w_cons):
        y=293+i*10
        g+=t(80,y,sym,'middle','Ls'); g+=t(320,y,note,'middle','Lx')
    g+=hr(350)
    g+=sh(358,'STRESS AND TONE')
    g+=t(240,368,'Welsh: stress almost always on penultimate syllable (second-to-last). Very regular.','middle','Ls')
    g+=t(240,377,'North Welsh dialects show some pitch distinctions (not true lexical tone). South Welsh more level.','middle','Lx')
    g+=hr(384)
    g+=sh(392,'COMPARATIVE NOTE')
    g+=t(240,402,'English: stress-timed, large vowel inventory, no mutations, SVO order.','middle','Ls')
    g+=t(240,411,'Welsh: syllable-timed (more regular), pitch-influenced stress, radical mutations, VSO order.','middle','Ls')
    g+=t(240,420,'Both: dental fricatives /\u03b8 \u00f0/, Latin alphabet, no tonal lexical distinctions.','middle','Ls')
    g+=t(240,429,'Shared Celtic substrate words in English: crag, corgi, brock (badger), tor, coomb (valley).','middle','Lx')
    g+=foot(BN,L1,L2,'B','Phonology')
    return g+close_svg()

def build_48c_alt():
    g=open_svg()
    g+=t(240,30,'ENGLISH + WELSH \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 48C \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'ENGLISH \u2014 SVO \u00b7 ANALYTIC \u00b7 MINIMAL INFLECTION')
    g+=t(240,73,'English is highly analytic: word order, not endings, marks grammatical roles. Lost case endings ~1200 CE.','middle','Ls')
    g+=t(240,82,'Verb: only -s for 3rd sg present; -ed for past; -ing for progressive. No gender agreement.','middle','Lx')
    g+=t(240,91,'Articles: the (definite) / a, an (indefinite) \u2014 no grammatical gender.','middle','Lx')
    g+=hr(99)
    g+=sh(107,'ENGLISH CORE VOCABULARY \u2014 20 WORDS')
    en_v=[('water','water'),('fire','fire'),('earth','earth'),('person','person'),('moon','moon'),
          ('sun','sun'),('yes','yes'),('no','no'),('I','I'),('you','you'),
          ('love','love'),('freedom','freedom'),('future','future'),('world','world'),('good','good'),
          ('death','death'),('life','life'),('thank you','thank you'),('when','when'),('where','where')]
    for i,(en,gl) in enumerate(en_v):
        col=i//10; row=i%10; y=116+row*10; x0=30+col*230
        g+=t(x0,y,en,'start','Ls'); g+=t(x0+90,y,gl,'start','Lx')
    g+=hr(222)
    g+=div(230,'WELSH (CYMRAEG) \u00b7 GRAMMAR \u00b7 VOCABULARY')
    g+=t(240,262,'Welsh is VSO (Verb-Subject-Object) \u2014 unusual in Europe. "Mae Sioned yn canu" = Is Sioned singing = Sioned sings.','middle','Ls')
    g+=t(240,271,'Inflected prepositions: unique Celtic feature. "I am" = Mae + subject; prepositions conjugate like verbs.','middle','Lx')
    g+=t(240,280,'"ar" (on): arnaf i (on-me), arnat ti (on-you), arno fe (on-him). Prepositions merge with pronouns.','middle','Lx')
    g+=hr(287)
    g+=sh(295,'WELSH VERB "BOD" (TO BE) \u2014 PRESENT TENSE')
    bod=[('rydw i','I am'),('rwyt ti','you are (inf.)'),('mae e/hi','he/she is'),
         ('rydyn ni','we are'),('rydych chi','you are (formal)'),('maen nhw','they are')]
    for i,(form,gl) in enumerate(bod):
        y=304+i*10
        g+=t(160,y,form,'middle','Ls'); g+=t(330,y,gl,'middle','Lx')
    g+=hr(370)
    g+=sh(378,'WELSH CORE VOCABULARY \u2014 20 WORDS')
    cy_v=[('d\u0175r','d\u016br','water'),('t\u00e2n','t\u0101n','fire'),('daear','daear','earth'),('person','person','person'),('lleuad','lleuad','moon'),
          ('haul','haul','sun'),('ie / oes','ie/oes','yes'),('na / nage','na/nage','no'),('fi','f\u012b','I'),('chi/ti','chi/ti','you'),
          ('cariad','cariad','love'),('rhyddid','rh\u0259\u00f0id','freedom'),('dyfodol','d\u0259vodol','future'),('byd','b\u012bd','world'),('da','d\u0101','good'),
          ('marwolaeth','maru\u0254la\u025b\u03b8','death'),('bywyd','b\u0259uid','life'),('diolch','d\u0131\u0254lx','thanks'),('pryd','pr\u012bd','when'),('lle','hle','where')]
    for i,(cy,pron,en) in enumerate(cy_v):
        col=i//10; row=i%10; y=387+row*10; x0=20+col*240
        g+=t(x0+5,y,cy,'start','Ls'); g+=t(x0+75,y,pron,'start','Lx'); g+=t(x0+140,y,en,'start','Lx')
    g+=foot(BN,L1,L2,'C','Grammar')
    return g+close_svg()

def build_48d_alt():
    g=open_svg()
    g+=t(240,30,'ENGLISH + WELSH \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g+=t(240,46,'ALT DRAFT \u00b7 SERIES 48D \u00b7 REMEMBER FORWARD','middle','S')
    g+=hr(54)
    g+=sh(63,'ENGLISH \u2014 PASSAGE 1 \u00b7 SHAKESPEARE')
    g+=t(240,73,'"What a piece of work is a man! How noble in reason, how infinite in faculty!"','middle','L')
    g+=t(240,83,'\u2014 Hamlet, Act 2 Scene 2. William Shakespeare, ~1600.','middle','Ls')
    g+=hr(91)
    g+=sh(99,'ENGLISH \u2014 PASSAGE 2 \u00b7 PROVERB')
    g+=t(240,109,'"A stitch in time saves nine." \u2014 Early intervention prevents greater effort later.','middle','L')
    g+=t(240,119,'Earliest recorded ~1732. Reflects practical, future-oriented thinking in folk wisdom.','middle','Lx')
    g+=hr(127)
    g+=sh(135,'ENGLISH \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g+=t(240,145,'This was made for you, freely, by people who remembered forward.','middle','L')
    g+=t(240,155,'"Forward" in English: from Old English "foreweard" \u2014 toward what is in front.','middle','Lx')
    g+=t(240,164,'"Future": from Latin futurus \u2014 "about to be." English borrowed it wholesale from Latin.','middle','Lx')
    g+=t(240,173,'English uniquely has both Germanic (forthcoming) and Latin (future) words for what lies ahead.','middle','Lx')
    g+=div(184,'WELSH (CYMRAEG) \u00b7 RUNNING TEXT \u00b7 PASSAGES')
    g+=sh(215,'WELSH \u2014 PASSAGE 1 \u00b7 Y GODODDIN (~600 CE)')
    g+=t(240,225,'"Ef aeth Catraeth, oedd ffraeth ei lu."','middle','L')
    g+=t(240,235,'"He went to Catraeth, spirited was his host."','middle','Ls')
    g+=t(240,244,'\u2014 Y Gododdin, Aneirin, ~600 CE. One of the oldest Welsh poems. Records a battle against Anglo-Saxons.','middle','Lx')
    g+=t(240,253,'This text predates Beowulf and most Old English literature. Welsh literacy is ancient.','middle','Lx')
    g+=hr(261)
    g+=sh(269,'WELSH \u2014 PASSAGE 2 \u00b7 PROVERB')
    g+=t(240,279,'"Heb iaith, heb galon."','middle','L')
    g+=t(240,289,'Without  language,  without  heart.','middle','Lx')
    g+=t(240,298,'"Without language, without a heart." \u2014 Welsh proverb on the identity carried by a language.','middle','Ls')
    g+=hr(306)
    g+=sh(314,'WELSH \u2014 BRIDGE PHRASE \u00b7 REMEMBER FORWARD')
    g+=t(240,324,'Cafodd hwn ei wneud i chi, yn rhad ac am ddim, gan bobl a gofiodd ymlaen.','middle','L')
    g+=t(240,334,'Was-made this its-making to you, for free,   by  people who remembered forward.','middle','Lx')
    g+=t(240,343,'"This was made for you, freely, by people who remembered forward."','middle','Ls')
    g+=hr(351)
    g+=sh(359,'LANGUAGE NOTE \u2014 "FORWARD" IN WELSH')
    g+=t(240,369,'ymlaen: "forward / onward" \u2014 from ym (intensive) + blaen (front/tip/point). Lit. "toward the point."','middle','Ls')
    g+=t(240,378,'blaen: "front, tip, blade" \u2014 the forward-most part. The same root gives "bland" in some branches.','middle','Lx')
    g+=t(240,387,'dyfodol: "future" \u2014 from dyfod (to come) + suffix -ol. Lit. "the coming thing." Future comes to you.','middle','Lx')
    g+=t(240,396,'gofio: "to remember" \u2014 from co (memory) + intensifier. Co\u0300 is the Celtic root for memory across all branches.','middle','Lx')
    g+=hr(404)
    g+=sh(412,'DECODING NOTE')
    g+=t(240,422,'English: ~1.5B speakers. Lingua franca of science, aviation, diplomacy. SVO, Latin alphabet.','middle','Ls')
    g+=t(240,431,'Welsh: ~750K speakers in Wales + diaspora. VSO, Celtic mutations, oldest literary tradition in Britain.','middle','Ls')
    g+=t(240,440,'Welsh survived Roman occupation, Anglo-Saxon migration, Norman conquest, and English suppression.','middle','Ls')
    g+=t(240,449,'The Welsh Language Act (1993) and the Welsh Language Measure (2011) gave Welsh co-official status in Wales.','middle','Lx')
    g+=foot(BN,L1,L2,'D','Text')
    return g+close_svg()

def main():
    plates={'plate48a_english_welsh_script_alt.svg':build_48a_alt(),
            'plate48b_english_welsh_phonology_alt.svg':build_48b_alt(),
            'plate48c_english_welsh_grammar_alt.svg':build_48c_alt(),
            'plate48d_english_welsh_text_alt.svg':build_48d_alt()}
    for fn,content in plates.items():
        p=OUT/fn; p.write_text(content,encoding='utf-8'); print(f'Written: {p}')
if __name__=='__main__': main()
