"""Build script — Shona series plates 36A–36D (Remember Forward)"""
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

# ─── PLATE 36A — SCRIPT ────────────────────────────────────────────────────
def build_36a():
    g=open_svg()
    g+=t(240,32,'SHONA','middle','T')
    g+=t(240,50,'Script & Writing System','middle','S')
    g+=hr(60)
    g+=sh(72,'WRITING SYSTEM')
    g+=t(240,84,'Shona uses the Latin alphabet. Standard Shona orthography codified 1955 (S.O.I.D.).','middle','Ls')
    g+=t(240,94,'25 letters; no q or x. Digraphs and trigraphs mark complex sounds.','middle','Ls')
    g+=t(240,104,'No diacritics in standard orthography; tone not marked in everyday writing.','middle','Ls')
    g+=hr(112)
    g+=sh(121,'SHONA ALPHABET')
    letters=[('A a','/a/'),('B b','/b/'),('Ch ch','/t\u0283/'),('D d','/d/'),('Dz dz','/dz/'),
             ('Dzv dzv','/dzv/'),('E e','/\u025b/'),('F f','/f/'),('G g','/\u0261/'),
             ('H h','/h/'),('I i','/i/'),('J j','/d\u0292/'),('K k','/k/'),('M m','/m/'),
             ('N n','/n/'),('Ng ng','/\u014b/'),('Ny ny','/\u0272/'),('O o','/\u0254/'),
             ('P p','/p/'),('R r','/r/'),('S s','/s/'),('Sh sh','/\u0283/'),
             ('T t','/t/'),('V v','/v/'),('W w','/w/'),('Y y','/j/'),('Z z','/z/'),
             ('Zh zh','/\u0292/'),('Sv sv','/sv/'),('Zv zv','/zv/')]
    for i,(letter,ipa) in enumerate(letters):
        col=i%4; row=i//4
        x=60+col*95; y=131+row*10
        g+=t(x,y,f'{letter} {ipa}','middle','Lx')
    g+=hr(215)
    g+=sh(224,'SPECIAL CONSONANTS')
    g+=t(240,234,'SV /sv/ — simultaneous s+v: svika (arrive), svosvoda (creep).','middle','Ls')
    g+=t(240,243,'ZV /zv/ — simultaneous z+v: zvino (now), zvakanaka (good things).','middle','Ls')
    g+=t(240,252,'DZV /dzv/ — voiced affricate + labiodental: dzva (a type of grass).','middle','Ls')
    g+=t(240,261,'NY /\u0272/ — palatal nasal (as in Spanish \u00f1): nyaya (matter/story), nyama (meat).','middle','Ls')
    g+=t(240,270,'NG /\u014b/ — velar nasal (ng in song): ngoma (drum), nguo (clothing).','middle','Ls')
    g+=hr(278)
    g+=sh(287,'TONE — UNMARKED BUT PHONEMIC')
    g+=t(240,297,'Shona has a two-tone system (High H / Low L) with downstep.','middle','Ls')
    g+=t(240,307,'Tone not written in standard orthography but is essential for meaning.','middle','Ls')
    g+=t(240,317,'H baba = father (respectful) / L baba = father (neutral).','middle','Ls')
    g+=t(240,327,'Tone marks tense on verbs: ndakauya (I came, H) vs ndakauya (I was coming).','middle','Ls')
    g+=hr(335)
    g+=sh(344,'DIALECTS OF STANDARD SHONA')
    g+=t(240,354,'Standard Shona (1955) unified 5 main dialects: Karanga, Zezuru, Korekore,','middle','Ls')
    g+=t(240,363,'Manyika, and Ndau. Spoken by ~15 million in Zimbabwe and Mozambique.','middle','Ls')
    g+=t(240,372,'Zezuru dialect (Harare region) is most prestigious in broadcast media.','middle','Ls')
    g+=hr(380)
    g+=sh(389,'NUMERALS')
    nums=[('1','imwe/potsi'),('2','piri'),('3','tatu'),('4','ina'),('5','shanu'),
          ('6','tanhatu'),('7','nomwe'),('8','sere'),('9','pfumbamwe'),('10','gumi')]
    for i,(n,w) in enumerate(nums):
        col=i%5; row=i//5
        x=70+col*80; y=399+row*10
        g+=t(x,y,f'{n}={w}','middle','Lx')
    g+=t(240,419,'20 = makumi maviri · 100 = zana · 1000 = chiuru','middle','Ls')
    g+=footer('36','Shona','A','Script')
    return g+close_svg()

# ─── PLATE 36B — PHONOLOGY ─────────────────────────────────────────────────
def build_36b():
    g=open_svg()
    g+=t(240,32,'SHONA','middle','T')
    g+=t(240,50,'Phonology & Sound System','middle','S')
    g+=hr(60)
    g+=sh(72,'CONSONANT INVENTORY')
    g+=t(240,82,'Shona has ~30 consonants. Notable features: fricative co-articulations (sv/zv),','middle','Ls')
    g+=t(240,91,'prenasalised stops (mb, nd, ng), and tonal contrasts.','middle','Ls')
    cons=[('p','/p/','bilabial stop vl'),('b','/b/','bilabial stop vd'),
          ('t','/t/','alveolar stop vl'),('d','/d/','alveolar stop vd'),
          ('k','/k/','velar stop vl'),('g','/\u0261/','velar stop vd'),
          ('ch','/t\u0283/','postalveolar affricate'),('j','/d\u0292/','postalveolar affricate vd'),
          ('dz','/dz/','alveolar affricate'),('dzv','/dzv/','labio-alveolar affricate'),
          ('f','/f/','labiodental fricative'),('v','/v/','labiodental fricative vd'),
          ('s','/s/','alveolar fricative'),('z','/z/','alveolar fricative vd'),
          ('sh','/\u0283/','postalveolar fricative'),('zh','/\u0292/','postalveolar fricative vd'),
          ('sv','/sv/','labio-alveolar fricative'),('zv','/zv/','labio-alveolar fricative vd'),
          ('h','/h/','glottal'),('m','/m/','bilabial nasal'),('n','/n/','alveolar nasal'),
          ('ng','/\u014b/','velar nasal'),('ny','/\u0272/','palatal nasal'),
          ('r','/r/','trill/flap'),('l','/l/','lateral'),('w','/w/','labio-velar'),('y','/j/','palatal')]
    for i,(c,ipa,desc) in enumerate(cons):
        col=0 if i<14 else 1
        y=101+(i if i<14 else i-14)*11
        g+=t(40+col*230,y,c,'middle','Ls'); g+=t(90+col*230,y,ipa,'middle','Lx'); g+=t(200+col*230,y,desc,'middle','Lx')
    g+=hr(262)
    g+=sh(271,'VOWEL SYSTEM — 5 VOWELS')
    vowels=[('a','/a/','open central'),('e','/\u025b/','mid-front'),('i','/i/','high front'),
            ('o','/\u0254/','mid-back rounded'),('u','/u/','high back rounded')]
    for i,(v,ipa,desc) in enumerate(vowels):
        y=281+i*11
        g+=t(80,y,v,'middle','L'); g+=t(160,y,ipa,'middle','Ls'); g+=t(320,y,desc,'middle','Ls')
    g+=hr(345)
    g+=sh(354,'TONE SYSTEM')
    g+=t(240,364,'Two phonemic tones: High (H) and Low (L). Downstep (!H) also occurs.','middle','Ls')
    g+=t(240,374,'Tone is carried by syllables, not individual segments.','middle','Ls')
    g+=t(240,384,'Verb tense/aspect conveyed primarily by tone pattern, not affixes:','middle','Ls')
    g+=t(240,394,'nda-ku-ya (H L H) = I came (perfect) / nda-ku-ya (H H L) = I was coming.','middle','Ls')
    g+=t(240,404,'Noun classes also affect tonal patterns of associated words.','middle','Ls')
    g+=hr(412)
    g+=sh(421,'PRENASALISED STOPS')
    g+=t(240,431,'MB /mb/: mbwa (dog), mberi (ahead). ND /nd/: ndiro (plate), ndenga (sky).','middle','Ls')
    g+=t(240,441,'NG /\u014b\u0261/: ngoma (drum), nguo (clothing). NJ /nd\u0292/: njere (a bead).','middle','Ls')
    g+=t(240,451,'These are single phonological segments (not sequences) — one syllable onset.','middle','Ls')
    g+=hr(459)
    g+=sh(468,'SYLLABLE STRUCTURE')
    g+=t(240,478,'Preferred syllable: CV (consonant + vowel). Open syllables dominate.','middle','Ls')
    g+=t(240,488,'Syllabic nasals possible: m-ti (tree), n-zira (path).','middle','Ls')
    g+=t(240,498,'Vowel sequences rare; hiatus resolved by glide insertion: chiyo \u2192 chi.yo.','middle','Ls')
    g+=footer('36','Shona','B','Phonology')
    return g+close_svg()

# ─── PLATE 36C — GRAMMAR ───────────────────────────────────────────────────
def build_36c():
    g=open_svg()
    g+=t(240,32,'SHONA','middle','T')
    g+=t(240,50,'Grammar & Core Vocabulary','middle','S')
    g+=hr(60)
    g+=sh(72,'SENTENCE STRUCTURE — SVO')
    g+=t(240,82,'Shona is Subject-Verb-Object. Verb agreement prefixes mirror noun class.','middle','Ls')
    g+=t(240,92,'Mwana adya sadza. Child 3SG.eat porridge = "The child is eating sadza."','middle','Ls')
    g+=hr(100)
    g+=sh(109,'NOUN CLASS SYSTEM (BANTU)')
    g+=t(240,119,'Shona has ~15 noun classes (chi-/zvi-, mu-/mi-, mu-/va-, etc.) like all Bantu languages.','middle','Ls')
    classes=[('mu-/va-','persons: mwana (child) / vana (children)'),
             ('mu-/mi-','trees/plants: muti (tree) / miti (trees)'),
             ('chi-/zvi-','things: chibage (maize) / zvibage (maizes)'),
             ('i-/ma-','mass/abstract: imba (house) / dzimba (houses)'),
             ('ri-/ma-','body parts: rino (tooth) / mano (teeth)'),
             ('ru-/n-','abstract/augmentative: rudo (love) / n- forms'),
             ('u-/ma-','abstract: utano (health) / n- forms'),
             ('pa-/ku-/mu-','locative classes: pano (here), kuenda (going)')]
    for i,(prefix,example) in enumerate(classes):
        y=129+i*11
        g+=t(90,y,prefix,'middle','Ls'); g+=t(310,y,example,'middle','Lx')
    g+=hr(225)
    g+=sh(234,'VERB MORPHOLOGY')
    g+=t(240,244,'Verb template: Subject prefix + Tense marker + Object prefix + Root + Final vowel.','middle','Ls')
    verbs=[('ndinoda','I love (ndi-no-da)'),('ari-da','he/she loves (a-ri-da)'),
           ('nda-ku-ya','I came (H tone = perfect)'),('ndichaenda','I will go (ndi-cha-end-a)'),
           ('ndakauya','I had come (pluperfect)'),('enda!','go! (imperative)'),
           ('handidi','I don\'t want (ha-ndi-di)'),('tinofarira','we like (ti-no-far-ir-a)')]
    for i,(form,gloss) in enumerate(verbs):
        y=254+i*10
        g+=t(130,y,form,'middle','L'); g+=t(320,y,gloss,'middle','Ls')
    g+=hr(340)
    g+=sh(349,'CORE VOCABULARY')
    vocab=[('mhoro','hello'),('waswera sei?','how was your day?'),('ndinofara','I am happy'),
           ('ndinoda','I love / I want'),('tatenda','thank you'),('ndiregerei','please / forgive me'),
           ('hongu','yes'),('kwete','no'),('mwana','child'),('mai','mother'),('baba','father'),
           ('imba','house'),('mvura','water'),('moto','fire'),('nyika','country/earth'),
           ('munhu','person'),('nguva','time'),('mwedzi','moon'),('nyeredzi','star'),
           ('moyo','heart'),('rudo','love'),('rusununguko','freedom'),('kuyeuka','memory/remember'),
           ('mangwana','tomorrow / future'),('nyika yose','the whole world'),
           ('zvakanaka','good things / it is good'),('hupenyu','life')]
    for i,(w,e) in enumerate(vocab):
        col=0 if i<14 else 1
        y=359+(i if i<14 else i-14)*10
        g+=t(50+col*235,y,w,'middle','Ls'); g+=t(175+col*235,y,e,'middle','Lx')
    g+=footer('36','Shona','C','Grammar')
    return g+close_svg()

# ─── PLATE 36D — RUNNING TEXT ──────────────────────────────────────────────
def build_36d():
    g=open_svg()
    g+=t(240,32,'SHONA','middle','T')
    g+=t(240,50,'Running Text \u2014 Four Passages + Bridge Phrase','middle','S')
    g+=hr(60)
    g+=sh(70,'I. TSUMO — PROVERB')
    g+=t(240,80,'Chisi chibereke chisi; chiramu ndechemuzukuru.','middle','L')
    g+=t(240,90,'chisi=today chibereke=let-it-give-birth chisi=today chiramu=in-law nde=is che=of muzukuru=grandchild','middle','Lx')
    g+=t(240,100,'"Today, let today give birth to today; the future belongs to the grandchild." (Shona proverb on succession)','middle','F')
    g+=hr(109)
    g+=sh(118,'II. RUDO — ON LOVE AND MEMORY')
    g+=t(240,128,'Kuyeuka kwevakafa ndiko rudo rwehupenyu.','middle','L')
    g+=t(240,138,'kuyeuka=remembering kwe=of vakafa=those-who-died ndiko=that-is rudo=love rwe=of hupenyu=life','middle','Ls')
    g+=t(240,148,'"Remembering those who have died is the love of life." (ancestral remembrance principle)','middle','F')
    g+=hr(157)
    g+=sh(166,'III. ZIVO — ON KNOWLEDGE AND TIME')
    g+=t(240,176,'Zivo inogara; munhu anoenda. Chinyorwa ndicho chinotsigira zivo.','middle','Ls')
    g+=t(240,186,'zivo=knowledge inogara=remains munhu=person anoenda=goes away','middle','Ls')
    g+=t(240,196,'chinyorwa=writing ndicho=is-the chinotsigira=that-supports','middle','Ls')
    g+=t(240,206,'"Knowledge endures; people pass away. Writing is what supports knowledge." (literacy concept)','middle','F')
    g+=hr(215)
    g+=sh(224,'IV. MBERI — FORWARD')
    g+=t(240,234,'Tinoenda mberi tichiyeuka avo vakafamba mberi.','middle','L')
    g+=t(240,244,'tinoenda=we-go mberi=forward tichiyeuka=while-remembering avo=those','middle','Ls')
    g+=t(240,254,'vakafamba=who-walked mberi=forward (ahead)','middle','Ls')
    g+=t(240,264,'"We go forward while remembering those who walked ahead." (guiding principle)','middle','F')
    g+=hr(273)
    g+=sh(282,'V. BRIDGE PHRASE')
    g+=t(240,294,'Chinhu ichi chakagadzirirwa iwe, mahara, navanhu vakayeuka mberi.','middle','L')
    g+=t(240,308,'chinhu-ichi=this-thing chakagadzirirwa=was-made-for iwe=you','middle','Ls')
    g+=t(240,317,'mahara=freely (without cost) navanhu=by-people vakayeuka=who-remembered','middle','Ls')
    g+=t(240,326,'mberi=forward / ahead','middle','Ls')
    g+=t(240,338,'"This was made for you, freely, by people who remembered forward."','middle','F')
    g+=hr(349)
    g+=sh(358,'BRIDGE PHRASE — NOTES')
    g+=t(240,368,'Mberi (from Bantu *-bele) means "ahead / forward / in front."','middle','Ls')
    g+=t(240,378,'Vakayeuka mberi = "who remembered forward" — facing ahead while holding the past.','middle','Ls')
    g+=t(240,388,'In Shona cosmology, the mudzimu (ancestral spirits) walk ahead of the living,','middle','Ls')
    g+=t(240,398,'guiding them. To "remember forward" is to honour those who guide from in front.','middle','Ls')
    g+=t(240,408,'Mahara = free of charge (from Arabic mahar, spread via Swahili trade routes).','middle','Ls')
    g+=hr(416)
    g+=sh(425,'LANGUAGE NOTES')
    g+=t(240,435,'Shona: ~15 million speakers; official language of Zimbabwe alongside Ndebele and English.','middle','Ls')
    g+=t(240,445,'Language family: Bantu (Niger-Congo), S-branch (Shona group S10).','middle','Ls')
    g+=t(240,455,'Standard Shona (1955) unified Karanga, Zezuru, Korekore, Manyika, Ndau dialects.','middle','Ls')
    g+=t(240,465,'Rich oral literature: tsumo (proverbs), nhetembo (poetry), ngano (folktales).','middle','Ls')
    g+=footer('36','Shona','D','Running Text')
    return g+close_svg()

def main():
    plates={
        'plate36a_shona_script.svg': build_36a(),
        'plate36b_shona_phonology.svg': build_36b(),
        'plate36c_shona_grammar.svg': build_36c(),
        'plate36d_shona_text.svg': build_36d(),
    }
    for fname,content in plates.items():
        path=OUT/fname
        path.write_text(content,encoding='utf-8')
        print(f'Written: {path}')

if __name__=='__main__':
    main()
