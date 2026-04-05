#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build French plate series 28A–28D for Remember Forward."""

from pathlib import Path
OUT = Path(__file__).parent

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def open_svg():
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 680" width="480" height="680">\n'
        '<style>\n'
        '  text { font-family: Georgia, serif; }\n'
        '  .T  { font-size:12px; font-weight:bold; letter-spacing:2px; }\n'
        '  .S  { font-size:7px; letter-spacing:1.5px; }\n'
        '  .H  { font-size:6.5px; font-weight:bold; letter-spacing:2.5px; }\n'
        '  .L  { font-size:7px; }\n'
        '  .Ls { font-size:6px; }\n'
        '  .Lx { font-size:5.5px; }\n'
        '  .M  { font-size:6px; letter-spacing:1px; }\n'
        '  .F  { font-size:7px; font-style:italic; }\n'
        '  .Fb { font-size:7.5px; font-weight:bold; }\n'
        '</style>\n'
        '<rect x="0" y="0" width="480" height="680" fill="white"/>\n'
        '<rect x="6" y="6" width="468" height="668" fill="none" stroke="black" stroke-width="3"/>\n'
        '<rect x="12" y="12" width="456" height="656" fill="none" stroke="black" stroke-width="0.75"/>\n'
    )

def close_svg(): return '</svg>\n'

def t(x,y,s,a='middle',c='L',extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="{c}" {extra}>{esc(s)}</text>\n'

def hr(y,x1=20,x2=460,sw=0.3):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black" stroke-width="{sw}"/>\n'

def sh(y,txt):
    return t(240,y,f'\u2014 {txt} \u2014','middle','H')

def footer(num,lang,letter,desc):
    return (hr(625)
        + t(240,620,f'SERIES {num} \u00b7 {lang.upper()} \u00b7 PLATE {letter} \u00b7 {desc.upper()} \u00b7 CC BY-SA 4.0 \u00b7 REMEMBERFORWARD.ORG','middle','M')
        + hr(633)
        + t(240,648,'THIS IS A PATIENT MESSAGE. IT WAS MADE FOR YOU, FREELY, BY PEOPLE WHO REMEMBERED FORWARD.','middle','Fb')
        + t(240,663,'BUY IT \u00b7 BUILD IT \u00b7 BURY IT \u00b7 FOR SOMEONE YOU WILL NEVER MEET','middle','F'))

def build_28a():
    g = open_svg()
    g += t(240,32,'FRENCH \u2014 SCRIPT \u00b7 WRITING SYSTEM','middle','T')
    g += t(240,50,'SERIES 28A OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'THE FRENCH ALPHABET \u2014 26 LETTERS + DIACRITICS')
    g += t(240,79,'French uses the standard 26-letter Latin alphabet. Spelling is historically conservative \u2014 many silent letters.','middle','L')
    g += t(240,89,'French spelling preserves medieval and Latin forms even when the pronunciation has changed drastically.','middle','Ls')
    g += t(240,98,'eau = /o/ \u00b7 oi = /wa/ \u00b7 eau, au, o, \u00f4 all = /o/ \u00b7 silent final consonants common: grand, petit, beaux.','middle','Ls')
    g += hr(106)

    g += sh(115,'DIACRITICS \u2014 FIVE TYPES')
    diac=[
        ('\u00e9','Acute (aigu)','Marks /e/ close: \u00e9t\u00e9, pr\u00e9, b\u00e9b\u00e9'),
        ('\u00e8 \u00ea','Grave / Circumflex','Marks /\u025b/ open: m\u00e8re, f\u00eate, t\u00eate'),
        ('\u00e0 \u00f9','Grave (a/u)','Disambiguates homophones: a (has) vs \u00e0 (to); ou (or) vs o\u00f9 (where)'),
        ('\u00e2 \u00ee \u00f4 \u00fb \u00ea','Circumflex','Marks long/close vowel or lost s: h\u00f4pital < hospitale'),
        ('\u00eb \u00ef \u00fc','Di\u00e9r\u00e8se (trema)','Vowel pronounced separately: Na\u00efl, no\u00ebl, na\u00efve'),
        ('\u00e7','C\u00e9dille','C before a/o/u = /s/: fran\u00e7ais, gar\u00e7on, re\u00e7u'),
    ]
    for i,(ch,name,func) in enumerate(diac):
        y=125+i*12
        g += t(45,y,ch,'middle','Ls'); g += t(130,y,name,'middle','Lx'); g += t(320,y,func,'middle','Lx')
    g += hr(200)

    g += sh(209,'SILENT LETTERS \u2014 A MAJOR FEATURE')
    g += t(240,220,'French has extensive silent letters \u2014 final consonants usually silent unless followed by a vowel (liaison).','middle','L')
    silent=[
        ('grand ami','[g\u0281\u00e3t ami]','final -d silent; liaison: grand_ami = [g\u0281\u00e3t_ami]'),
        ('les enfants','[le z\u00e3f\u00e3]','les = /le/; liaison s: [lez\u00e3f\u00e3]'),
        ('est-il','[\u025bttil]','final -t of est pronounced in inversion'),
        ('beaux','[bo]','final -x silent; eau = /o/'),
        ('psychologie','[psikol\u0254\u0292i]','initial p silent in common speech'),
        ('homme','[\u0254m]','initial h always silent; final -e silent'),
    ]
    for i,(sp,ipa,note) in enumerate(silent):
        y=230+i*12
        g += t(75,y,sp,'middle','Ls'); g += t(175,y,ipa,'middle','Lx'); g += t(355,y,note,'middle','Lx')
    g += hr(306)

    g += sh(315,'LIAISON AND ELISION')
    g += t(240,326,'Liaison: final silent consonant pronounced before a following vowel-initial word.','middle','L')
    g += t(240,336,'les amis [lezami] (the friends) \u00b7 nous avons [nuzav\u0254\u0303] (we have) \u00b7 deux enfants [d\u00f8z\u00e3f\u00e3]','middle','Ls')
    g += t(240,345,'Elision: final vowel of small words dropped before vowel: le + ami = l\'ami \u00b7 de + elle = d\'elle','middle','Ls')
    g += t(240,354,'Required elision: le, la, de, que, ne, se, me, te, ce before vowels or silent h.','middle','Ls')
    g += hr(362)

    g += sh(371,'SCRIPT HISTORY')
    g += t(240,382,'Old French (~9th\u201314th c.): diverged from Vulgar Latin; Serments de Strasbourg (842 CE) first French document.','middle','Ls')
    g += t(240,391,'Middle French (14th\u201317th c.): heavy borrowing from Latin; spelling increasingly conservative vs. pronunciation.','middle','Ls')
    g += t(240,400,'Acad\u00e9mie fran\u00e7aise (founded 1635): codifies French spelling and grammar; issues official dictionary.','middle','Ls')
    g += t(240,409,'French is spoken by ~80 million native speakers; ~275 million total (L1+L2) across 29 countries.','middle','Ls')
    g += t(240,418,'Second most learned language in the world; official language of the UN, EU, African Union, Olympic Committee.','middle','Ls')

    g += footer('28','French','A','Script')
    g += close_svg()
    return g

def build_28b():
    g = open_svg()
    g += t(240,32,'FRENCH \u2014 PHONOLOGY \u00b7 SOUND SYSTEM','middle','T')
    g += t(240,50,'SERIES 28B OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'VOWEL SYSTEM \u2014 12 ORAL + 4 NASAL')
    g += t(240,79,'French has one of the most complex vowel systems of any European language: 12 oral + 4 nasal vowels.','middle','L')
    g += t(240,89,'Front rounded vowels /y \u00f8 \u0153/ are absent from English \u2014 a common learning difficulty.','middle','Ls')
    oral=[
        ('/i/','i','vie (life), midi (noon)'),('/e/','e close','\u00e9t\u00e9, donn\u00e9'),
        ('/\u025b/','e open','m\u00e8re, fen\u00eatre'),('/a/','a front','patte, chat'),
        ('/\u0251/','a back','p\u00e2te (rare)'),('/y/','u','lune, pur \u2014 rounded /i/'),
        ('/\u00f8/','eu close','feu, deux \u2014 rounded /e/'),('/\u0153/','eu open','peur, fleur \u2014 rounded /\u025b/'),
        ('/u/','ou','loup, bout'),('/o/','o close','eau, beau, m\u00f4t'),
        ('/\u0254/','o open','or, botte'),('/\u0259/','schwa','le, me, se (optional)'),
    ]
    for i,(ipa,ltr,ex) in enumerate(oral):
        y=99+i*11
        g += t(50,y,ipa,'middle','Lx'); g += t(105,y,ltr,'middle','Lx'); g += t(310,y,ex,'middle','Lx')
    g += t(240,233,'Nasal: /\u00e3/ an\u00b7 /\u025b\u0303/ in\u00b7 /\u0254\u0303/ on\u00b7 /\u0153\u0303/ un \u2014 bon, bain, blanc, brun','middle','Ls')
    g += hr(241)

    g += sh(250,'CONSONANT INVENTORY')
    cons=[
        ('p b','/p b/','bilabial','pain, beau'),
        ('t d','/t d/','dental','tu, dame'),
        ('k g','/k \u0261/','velar','car, gare'),
        ('f v','/f v/','labiodental','feu, voir'),
        ('s z','/s z/','alveolar','sac, zéro'),
        ('\u0283 \u0292','/\u0283 \u0292/','palatal','chat, jour'),
        ('m n','/m n/','nasals','mer, non'),
        ('\u0272','/\u0272/','palatal nasal','gagner, montagne'),
        ('l','/l/','lateral','lune, sol'),
        ('r','/\u0281/','uvular rhotic','rue, Paris \u2014 NOT a trill'),
        ('j w \u0265','/j w \u0265/','glides','yeux, oui, lui (rounded palatal)'),
    ]
    for i,(ltr,ipa,label,ex) in enumerate(cons):
        y=260+i*12
        g += t(40,y,ltr,'middle','Ls'); g += t(85,y,ipa,'middle','Lx')
        g += t(155,y,label,'middle','Lx'); g += t(350,y,ex,'middle','Lx')
    g += hr(396)

    g += sh(405,'STRESS AND RHYTHM')
    g += t(240,416,'French stress falls on the FINAL syllable of a phonological phrase \u2014 not individual words.','middle','L')
    g += t(240,426,'French is syllable-timed \u2014 each syllable gets roughly equal duration (unlike English stress-timing).','middle','Ls')
    g += t(240,435,'This gives French its characteristic even, flowing rhythm. Word-level stress is weak.','middle','Ls')
    g += t(240,444,'Enchainement: final consonant of one word attaches to initial vowel of next: avec elle = [avekkel].','middle','Ls')
    g += hr(452)

    g += sh(461,'KEY PHONOLOGICAL FEATURES')
    g += t(240,472,'Uvular /\u0281/: French r is produced at the back of the throat \u2014 not a tongue-tip sound. Unique among Romance.','middle','Ls')
    g += t(240,481,'Front rounded vowels: /y \u00f8 \u0153/ \u2014 produced by combining front tongue position with lip rounding.','middle','Ls')
    g += t(240,490,'Schwa /\u0259/: optional in fast speech; e muet "mute e" \u2014 le cheval [l\u0259\u0283val] or [\u0283val].','middle','Ls')
    g += t(240,499,'Nasal vowels: vowel before n/m in same syllable becomes nasal and n/m disappears: bon = /b\u0254\u0303/.','middle','Ls')

    g += footer('28','French','B','Phonology')
    g += close_svg()
    return g

def build_28c():
    g = open_svg()
    g += t(240,32,'FRENCH \u2014 GRAMMAR \u00b7 VOCABULARY','middle','T')
    g += t(240,50,'SERIES 28C OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(68,'SVO \u2014 OBLIGATORY SUBJECT \u2014 TWO GENDERS')
    g += t(240,79,'French is SVO. Unlike Spanish/Italian, subject pronouns are OBLIGATORY \u2014 not null-subject.','middle','L')
    g += t(240,89,'Two genders (M/F): le livre (M), la table (F). Gender must be memorised \u2014 not predictable.','middle','Ls')
    g += t(240,98,'Articles: le/la/les (definite), un/une/des (indefinite). Articles required where English often omits them.','middle','Ls')
    g += hr(106)

    g += sh(115,'VERB CONJUGATION \u2014 parler "to speak"')
    pres=[('je','parle','I speak'),('tu','parles','you (inf)'),('il/elle','parle','he/she'),
          ('nous','parlons','we'),('vous','parlez','you (formal/pl)'),('ils/elles','parlent','they')]
    impar=[('je','parlais','I was speaking'),('tu','parlais','you'),('il/elle','parlait','he/she'),
           ('nous','parlions','we'),('vous','parliez','you'),('ils/elles','parlaient','they')]
    g += t(105,125,'Present','middle','Lx'); g += t(355,125,'Imparfait (past continuous)','middle','Lx')
    for i,((p1,f1,gl1),(p2,f2,gl2)) in enumerate(zip(pres,impar)):
        y=134+i*11
        g += t(42,y,p1,'middle','Lx'); g += t(108,y,f1,'middle','Ls'); g += t(198,y,gl1,'middle','Lx')
        g += t(275,y,p2,'middle','Lx'); g += t(345,y,f2,'middle','Ls'); g += t(435,y,gl2,'start','Lx')
    g += t(240,208,'Pass\u00e9 compos\u00e9 (perfect): avoir/\u00eatre + past participle \u2014 j\'ai parl\u00e9 (I spoke/have spoken)','middle','Ls')
    g += t(240,217,'\u00eatre verbs (motion/state change): je suis all\u00e9(e) (I went) \u2014 participle agrees with subject gender.','middle','Ls')
    g += hr(225)

    g += sh(234,'NEGATION AND QUESTION FORMATION')
    g += t(240,245,'Negation: ne\u2026pas wraps the verb: Je ne parle pas (I do not speak). Spoken French often drops ne: je parle pas.','middle','Ls')
    g += t(240,254,'Other negatives: ne\u2026jamais (never), ne\u2026rien (nothing), ne\u2026plus (no more), ne\u2026personne (no one).','middle','Ls')
    g += t(240,263,'Questions: inversion (Parlez-vous?), est-ce que (Est-ce que vous parlez?), or intonation (Vous parlez?).','middle','Ls')
    g += hr(271)

    g += sh(280,'CORE VOCABULARY \u2014 25 WORDS')
    vocab=[
        ('oui / non','yes / no'),('je / vous','I / you (formal)'),('ceci / cela','this / that'),
        ('o\u00f9','where'),('quoi / qu\'est-ce que','what'),('qui','who'),
        ('quand','when'),('pourquoi','why'),('eau','water'),
        ('feu','fire'),('terre','earth'),('personne','person'),
        ('livre','book'),('temps','time/weather'),('lune','moon'),('étoile','star'),
        ('coeur','heart'),('amour','love'),('libert\u00e9','freedom'),
        ('m\u00e9moire','memory'),('avenir / futur','future'),('monde','world'),
        ('bon / mauvais','good / bad'),('tout','everything'),('vie','life'),
    ]
    for i,(fr,en) in enumerate(vocab):
        col=0 if i<13 else 1
        y=290+(i if i<13 else i-13)*10
        g += t(50+col*230,y,fr,'middle','Ls'); g += t(175+col*230,y,en,'middle','Lx')
    g += hr(423)

    g += sh(432,'SUBJUNCTIVE AND FORMAL REGISTER')
    g += t(240,443,'French subjunctive is still widely used (unlike its decline in Spanish/Italian colloquial speech).','middle','L')
    g += t(240,453,'Required after: vouloir que, il faut que, bien que, pour que, avant que\u2026','middle','Ls')
    g += t(240,462,'Il faut que vous parliez (It is necessary that you speak) \u2014 subj. after il faut que.','middle','Ls')
    g += t(240,471,'Register: tu (familiar) vs vous (formal/plural). Vous for strangers, elders, professionals.','middle','Ls')
    g += t(240,480,'French has three registers: spoken colloquial, standard written, and soutenu (elevated/literary).','middle','Ls')
    g += t(240,489,'Acad\u00e9mie fran\u00e7aise guards vocabulary \u2014 resists English loans (courriel not email, logiciel not software).','middle','Ls')

    g += footer('28','French','C','Grammar')
    g += close_svg()
    return g

def build_28d():
    g = open_svg()
    g += t(240,32,'FRENCH \u2014 RUNNING TEXT \u00b7 PASSAGES','middle','T')
    g += t(240,50,'SERIES 28D OF 60 \u00b7 REMEMBER FORWARD','middle','S')
    g += hr(58)

    g += sh(67,'PASSAGE 1 \u2014 DESCARTES, DISCOURS DE LA M\u00c9THODE (1637)')
    g += t(240,78,'Je pense, donc je suis.','middle','L')
    g += t(240,88,'I  think therefore I  am.','middle','Lx')
    g += t(240,97,'"I think, therefore I am." \u2014 The foundation of modern Western philosophy. First published in French, not Latin.','middle','Ls')
    g += hr(105)

    g += sh(113,'PASSAGE 2 \u2014 VICTOR HUGO, LES MIS\u00c9RABLES (1862)')
    g += t(240,124,'Aimer, c\'est agir.','middle','L')
    g += t(240,134,'To-love  it-is  to-act.','middle','Lx')
    g += t(240,143,'"To love is to act." \u2014 Victor Hugo. One of the most translated novels in history.','middle','Ls')
    g += hr(151)

    g += sh(159,'PASSAGE 3 \u2014 ANTOINE DE SAINT-EXUP\u00c9RY, LE PETIT PRINCE (1943)')
    g += t(240,170,'On ne voit bien qu\'avec le coeur.','middle','L')
    g += t(240,180,'One not sees well only-with the  heart.','middle','Lx')
    g += t(240,189,'L\'essentiel est invisible pour les yeux.','middle','L')
    g += t(240,199,'The-essential is invisible to    the eyes.','middle','Lx')
    g += t(240,208,'"One sees clearly only with the heart. The essential is invisible to the eye."','middle','Ls')
    g += hr(216)

    g += sh(224,'PASSAGE 4 \u2014 FRENCH PROVERBS')
    g += t(240,235,'Mieux vaut tard que jamais.','middle','L')
    g += t(240,245,'Better is-worth late than never. \u2014 "Better late than never."','middle','Lx')
    g += t(240,255,'Petit \u00e0 petit, l\'oiseau fait son nid.','middle','L')
    g += t(240,265,'Little by little the bird  makes its nest. \u2014 Patience builds all things.','middle','Lx')
    g += hr(273)

    g += sh(281,'PASSAGE 5 \u2014 D\u00c9CLARATION DES DROITS DE L\'HOMME (1789)')
    g += t(240,292,'Les hommes naissent et demeurent libres et \u00e9gaux en droits.','middle','L')
    g += t(240,302,'The men    are-born and remain   free  and equal in  rights.','middle','Lx')
    g += t(240,311,'"Men are born and remain free and equal in rights." \u2014 Article 1, Declaration of the Rights of Man.','middle','Ls')
    g += hr(319)

    g += sh(327,'BRIDGE PHRASE \u2014 REMEMBER FORWARD')
    g += t(240,339,'Ce message a \u00e9t\u00e9 fait pour vous, gratuitement, par des personnes qui se sont souvenues de l\'avenir.','middle','L')
    g += t(240,350,'This message has been made for you   freely       by  some people   who  themselves remembered of  the future.','middle','Lx')
    g += t(240,360,'"This message was made for you, freely, by people who remembered the future."','middle','Ls')
    g += hr(368)

    g += sh(377,'LANGUAGE NOTE \u2014 "FUTURE" IN FRENCH')
    g += t(240,388,'avenir (m.): the usual word for "future" \u2014 from \u00e0 + venir "to come toward" \u2014 the future as what comes to us.','middle','L')
    g += t(240,398,'futur (m.): also used, especially for the grammatical tense and abstract sense.','middle','Ls')
    g += t(240,407,'se souvenir de: to remember \u2014 lit. "to come up to oneself again" \u2014 reflexive, memory as self-reunion.','middle','Ls')
    g += t(240,416,'gratuitement: freely \u2014 from gratuit (free of charge), from Latin gratuitus.','middle','Ls')
    g += t(240,425,'The pass\u00e9 compos\u00e9 (se sont souvenues) marks completeness: they DID remember, and it is done.','middle','Ls')
    g += hr(433)

    g += sh(442,'DECODING NOTE \u2014 FOR FUTURE READERS')
    g += t(240,453,'French is spoken by ~80M native speakers; ~275M total across 29 countries on 5 continents.','middle','Ls')
    g += t(240,462,'Official language of: France, Belgium, Switzerland, Canada, and 21 African nations (most of West/Central Africa).','middle','Ls')
    g += t(240,471,'French served as the dominant language of diplomacy, science, and high culture 1650\u20131900 CE.','middle','Ls')
    g += t(240,480,'Many English words derive from French (after 1066 Norman conquest): government, justice, language, people.','middle','Ls')
    g += t(240,489,'Uses the Latin alphabet. Spelling is conservative \u2014 pronounce by rules, not by spelling (see Plate 28A).','middle','Ls')

    g += footer('28','French','D','Text')
    g += close_svg()
    return g

def main():
    plates = {
        'plate28a_french_script.svg': build_28a(),
        'plate28b_french_phonology.svg': build_28b(),
        'plate28c_french_grammar.svg': build_28c(),
        'plate28d_french_text.svg': build_28d(),
    }
    for fname,content in plates.items():
        (OUT/fname).write_text(content,encoding='utf-8')
        print(f'Written: {OUT/fname}')

if __name__ == '__main__':
    main()
