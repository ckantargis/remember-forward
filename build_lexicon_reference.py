"""
Generates lexicon_reference.html - the readable reference for the domain list.
Data comes from plates/lexicon_domains.py so the two never drift.

    python build_lexicon_reference.py
"""
import html
import math
import sys
from collections import Counter

sys.path.insert(0, "plates")
from lexicon_domains import SECTIONS, PLATES  # noqa: E402

E = html.escape
N_PLATES = len(PLATES)
N_WORDS = sum(p[4] for p in PLATES)
N_PHYS = -(-N_PLATES // 2)
AREA = N_PLATES * 120 * 170 / 1e6

# cost, consistent with lexicon_model.xlsx
TI_PANELS = math.ceil(AREA / 0.36)
TI_COST = TI_PANELS * (28 + 300 * 600 * 0.3 / 1000 * 4.51 / 1000 * 40) + TI_PANELS * 250 / 100
CE_TILES = math.ceil(AREA / 0.36)
CE_MAT = (300 * 600 * 6 / 1000 * 2.3 / 1000 * 1.0 + 0.30) * 1.12 + 70 * 0.2 / 30 * 2
CE_COST = CE_TILES * CE_MAT + AREA * 45 + CE_TILES * 150 / 100

GRAMMAR_NOTE = {
    "SCENE": "A place, with people and things in it. Callouts point into the picture.",
    "SEQUENCE": "A process over time. Numbered panels, read in order.",
    "DIAGRAM": "An abstract system drawn as structure.",
    "ARRAY": "Meaning carried by contrast. Paired panels, identical but for one thing.",
    "ANATOMY": "A whole thing dissected and labelled.",
}
TIER_NOTE = {0: "Semantic prime", 1: "Core vocabulary", 2: "Extended"}

CSS = """
:root{
  --ground:#e9eaec; --panel:#f7f8f9; --panel-2:#eff1f3;
  --ink:#14181c; --body:#3f474f; --muted:#6b747d;
  --rule:#ccd1d6; --rule-soft:#dde1e5;
  --accent:#1c5d7d; --accent-soft:#dbe8ef;
  --clay:#9c4f2b; --clay-soft:#f0e2da;
  --shadow:0 1px 2px rgba(20,24,28,.06);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#131619; --panel:#1a1e22; --panel-2:#20252a;
    --ink:#e7eaec; --body:#b3bcc4; --muted:#8b959e;
    --rule:#2e353b; --rule-soft:#252b31;
    --accent:#6fb3d2; --accent-soft:#16303d;
    --clay:#d08758; --clay-soft:#33221a;
    --shadow:0 1px 2px rgba(0,0,0,.4);
  }
}
:root[data-theme="dark"]{
  --ground:#131619; --panel:#1a1e22; --panel-2:#20252a;
  --ink:#e7eaec; --body:#b3bcc4; --muted:#8b959e;
  --rule:#2e353b; --rule-soft:#252b31;
  --accent:#6fb3d2; --accent-soft:#16303d;
  --clay:#d08758; --clay-soft:#33221a;
  --shadow:0 1px 2px rgba(0,0,0,.4);
}
*{box-sizing:border-box}
body{
  background:var(--ground); color:var(--body);
  font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;
  font-size:15px; line-height:1.55; margin:0;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3{font-family:"Zilla Slab",Georgia,serif; color:var(--ink); text-wrap:balance; margin:0}
.mono{font-family:"IBM Plex Mono",ui-monospace,monospace; font-variant-numeric:tabular-nums}

.wrap{max-width:1180px; margin:0 auto; padding:0 24px}

/* ---------- masthead ---------- */
header{border-bottom:1px solid var(--rule); background:var(--panel)}
.mast{display:flex; flex-direction:column; gap:20px; padding:44px 0 32px}
.eyebrow{
  font-family:"IBM Plex Mono",monospace; font-size:11px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--accent);
}
h1{font-size:clamp(30px,4.4vw,46px); line-height:1.08; font-weight:600; letter-spacing:-.01em}
.standfirst{max-width:63ch; font-size:16.5px; color:var(--body)}
.standfirst strong{color:var(--ink); font-weight:600}

.figures{
  display:grid; grid-template-columns:repeat(auto-fit,minmax(132px,1fr));
  gap:1px; background:var(--rule-soft); border:1px solid var(--rule-soft); margin-top:4px;
}
.fig{background:var(--panel); padding:14px 16px}
.fig dt{
  font-family:"IBM Plex Mono",monospace; font-size:10.5px; letter-spacing:.11em;
  text-transform:uppercase; color:var(--muted); margin-bottom:5px;
}
.fig dd{margin:0; font-family:"Zilla Slab",Georgia,serif; font-size:23px; color:var(--ink); font-variant-numeric:tabular-nums}
.fig dd small{font-size:12px; color:var(--muted); font-family:"IBM Plex Sans",sans-serif}

/* ---------- controls ---------- */
.controls{
  position:sticky; top:0; z-index:20; background:var(--ground);
  border-bottom:1px solid var(--rule); padding:11px 0;
}
.ctl-row{display:flex; flex-wrap:wrap; gap:8px; align-items:center}
.ctl-label{
  font-family:"IBM Plex Mono",monospace; font-size:10.5px; letter-spacing:.11em;
  text-transform:uppercase; color:var(--muted); margin-right:2px;
}
button.chip{
  font:inherit; font-size:12.5px; cursor:pointer; padding:4px 11px;
  background:var(--panel); color:var(--body);
  border:1px solid var(--rule); border-radius:2px; transition:.13s;
}
button.chip:hover{border-color:var(--accent); color:var(--ink)}
button.chip[aria-pressed="true"]{background:var(--accent); border-color:var(--accent); color:var(--ground)}
button.chip:focus-visible{outline:2px solid var(--accent); outline-offset:2px}

/* ---------- sections ---------- */
main{padding:8px 0 72px}
.sect{padding-top:38px; scroll-margin-top:60px}
.sect-head{display:flex; align-items:baseline; gap:14px; border-bottom:2px solid var(--ink); padding-bottom:9px; margin-bottom:4px}
.sect-letter{
  font-family:"Zilla Slab",Georgia,serif; font-size:30px; font-weight:600;
  color:var(--accent); line-height:1;
}
.sect-title{font-size:19px; font-weight:600; letter-spacing:.005em}
.sect-count{
  margin-left:auto; font-family:"IBM Plex Mono",monospace; font-size:11.5px;
  color:var(--muted); white-space:nowrap;
}
.sect-blurb{color:var(--muted); font-size:14px; margin:9px 0 18px; max-width:64ch}

.grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(330px,1fr)); gap:14px}

/* ---------- plate card ---------- */
.card{
  background:var(--panel); border:1px solid var(--rule-soft); box-shadow:var(--shadow);
  padding:15px 16px 14px; display:flex; flex-direction:column; gap:9px;
}
.card.dim{display:none}
.card-top{display:flex; align-items:center; gap:9px}
.callout{
  flex:none; width:27px; height:27px; border-radius:50%;
  border:1.5px solid var(--ink); color:var(--ink);
  font-family:"IBM Plex Mono",monospace; font-size:11px; font-weight:500;
  display:grid; place-items:center;
}
.card-id{font-family:"IBM Plex Mono",monospace; font-size:11px; color:var(--muted); letter-spacing:.04em}
.tag{
  margin-left:auto; font-family:"IBM Plex Mono",monospace; font-size:9.5px;
  letter-spacing:.1em; padding:2.5px 7px; border-radius:2px;
  background:var(--accent-soft); color:var(--accent); white-space:nowrap;
}
.card h3{font-size:16.5px; font-weight:600; line-height:1.25}
.depict{font-size:13.5px; line-height:1.5; color:var(--body); margin:0}
.words{display:flex; flex-wrap:wrap; gap:4px; margin-top:1px}
.w{
  font-family:"IBM Plex Mono",monospace; font-size:11px; padding:1.5px 6px;
  background:var(--panel-2); border:1px solid var(--rule-soft); color:var(--muted); border-radius:2px;
}
.meta{
  display:flex; gap:10px; align-items:center; margin-top:auto; padding-top:9px;
  border-top:1px solid var(--rule-soft);
  font-family:"IBM Plex Mono",monospace; font-size:10.5px; color:var(--muted);
}
.note{
  font-size:12.5px; line-height:1.45; color:var(--clay);
  background:var(--clay-soft); border-left:2px solid var(--clay); padding:7px 10px;
}
.note b{font-weight:600}

/* ---------- key ---------- */
.key{margin-top:52px; border-top:2px solid var(--ink); padding-top:26px}
.key h2{font-size:19px; margin-bottom:6px}
.key > p{max-width:64ch; font-size:14px; color:var(--muted); margin:0 0 20px}
.keygrid{display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:1px; background:var(--rule-soft); border:1px solid var(--rule-soft)}
.keyitem{background:var(--panel); padding:13px 15px}
.keyitem dt{font-family:"IBM Plex Mono",monospace; font-size:11px; letter-spacing:.1em; color:var(--accent); margin-bottom:5px}
.keyitem dd{margin:0; font-size:13.5px; color:var(--body)}

footer{border-top:1px solid var(--rule); margin-top:44px; padding:22px 0 40px; color:var(--muted); font-size:12.5px}
footer p{margin:0 0 6px; max-width:70ch}

@media (max-width:640px){
  .mast{padding:32px 0 24px}
  .grid{grid-template-columns:1fr}
  .sect-count{display:none}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = """
(function(){
  var cards=[].slice.call(document.querySelectorAll('.card'));
  var state={grammar:'ALL',tier:'ALL'};
  function apply(){
    cards.forEach(function(c){
      var okG=state.grammar==='ALL'||c.dataset.grammar===state.grammar;
      var okT=state.tier==='ALL'||c.dataset.tier===state.tier;
      c.classList.toggle('dim',!(okG&&okT));
    });
    document.querySelectorAll('.sect').forEach(function(s){
      var vis=s.querySelectorAll('.card:not(.dim)').length;
      s.hidden = vis===0;
      var c=s.querySelector('.sect-count');
      if(c) c.textContent = vis + ' of ' + s.querySelectorAll('.card').length + ' plates';
    });
  }
  document.querySelectorAll('button.chip').forEach(function(b){
    b.addEventListener('click',function(){
      var k=b.dataset.key;
      state[k]=b.dataset.val;
      document.querySelectorAll('button.chip[data-key="'+k+'"]').forEach(function(o){
        o.setAttribute('aria-pressed', String(o===b));
      });
      apply();
    });
  });
  apply();
})();
"""


def build():
    grammars = [g for g, _ in Counter(p[3] for p in PLATES).most_common()]
    out = []
    a = out.append

    a("<title>The Pictorial Lexicon Index</title>")
    a('<link rel="preconnect" href="https://fonts.googleapis.com">')
    a('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&'
      'family=Zilla+Slab:wght@500;600&display=swap">')
    a("<style>%s</style>" % CSS)

    # masthead
    a('<header><div class="wrap"><div class="mast">')
    a('<div class="eyebrow">Remember Forward &middot; content plan</div>')
    a("<h1>The Pictorial Lexicon Index</h1>")
    a('<p class="standfirst">Every word in the lexicon, placed on a plate. '
      'Built on the Oxford&ndash;Duden pictorial model &mdash; 28,000 entries across 384 plates &mdash; '
      'but run deliberately lighter, at about 55 words per plate instead of 73, so that '
      '<strong>every word stays readable by the naked eye</strong>. No magnifier anywhere in this set. '
      'Numbered callouts point into the picture; the words themselves live in a margin strip that can be '
      're-etched per language while the drawing stays untouched.</p>')
    a('<dl class="figures">')
    for label, val, sub in [
        ("Plates", "%d" % N_PLATES, "scene faces"),
        ("Words", "{:,}".format(N_WORDS), "~55 each"),
        ("Two-sided", "%d" % N_PHYS, "120&times;170mm"),
        ("Area", "%.2f" % AREA, "m&sup2; engraved"),
        ("Titanium", "$%d" % round(TI_COST), "per set, PCM"),
        ("Ceramic", "$%d" % round(CE_COST), "per set, decal"),
    ]:
        a('<div class="fig"><dt>%s</dt><dd>%s <small>%s</small></dd></div>' % (label, val, sub))
    a("</dl>")
    a("</div></div></header>")

    # controls
    a('<div class="controls"><div class="wrap"><div class="ctl-row">')
    a('<span class="ctl-label">Grammar</span>')
    a('<button class="chip" data-key="grammar" data-val="ALL" aria-pressed="true">All</button>')
    for g in grammars:
        n = sum(1 for p in PLATES if p[3] == g)
        a('<button class="chip" data-key="grammar" data-val="%s" aria-pressed="false">%s <span class="mono">%d</span></button>'
          % (g, g.title(), n))
    a('<span class="ctl-label" style="margin-left:14px">Tier</span>')
    a('<button class="chip" data-key="tier" data-val="ALL" aria-pressed="true">All</button>')
    for t in (0, 1, 2):
        n = sum(1 for p in PLATES if p[5] == t)
        a('<button class="chip" data-key="tier" data-val="%d" aria-pressed="false">%s <span class="mono">%d</span></button>'
          % (t, E(TIER_NOTE[t]), n))
    a("</div></div></div>")

    a('<main><div class="wrap">')
    idx = 0
    for code, name, blurb in SECTIONS:
        ps = [p for p in PLATES if p[1] == code]
        a('<section class="sect" id="s-%s">' % code)
        a('<div class="sect-head"><span class="sect-letter">%s</span>'
          '<h2 class="sect-title">%s</h2>'
          '<span class="sect-count">%d plates &middot; %d words</span></div>'
          % (code, E(name), len(ps), sum(x[4] for x in ps)))
        a('<p class="sect-blurb">%s</p>' % E(blurb))
        a('<div class="grid">')
        for pid, _s, ptitle, grammar, words, tier, depiction, samples, link in ps:
            idx += 1
            a('<article class="card" data-grammar="%s" data-tier="%d">' % (grammar, tier))
            a('<div class="card-top"><span class="callout mono">%d</span>'
              '<span class="card-id">%s</span>'
              '<span class="tag">%s</span></div>' % (idx, E(pid), grammar))
            a("<h3>%s</h3>" % E(ptitle))
            a('<p class="depict">%s</p>' % E(depiction))
            a('<div class="words">%s</div>'
              % "".join('<span class="w">%s</span>' % E(w) for w in samples))
            if link:
                a('<p class="note">%s</p>' % E(link))
            a('<div class="meta"><span>%d words</span><span>&middot;</span>'
              '<span>Tier %d &mdash; %s</span></div>' % (words, tier, E(TIER_NOTE[tier])))
            a("</article>")
        a("</div></section>")

    # key
    a('<section class="key">')
    a("<h2>Plate grammars</h2>")
    a("<p>Not everything is a scene. The abstract residue &mdash; quantity, logic, judgment, position &mdash; "
      "resists depiction in a setting, so it gets its own forms. Choosing the wrong grammar is the most "
      "likely way one of these plates fails.</p>")
    a('<dl class="keygrid">')
    for g in grammars:
        n = sum(1 for p in PLATES if p[3] == g)
        a('<div class="keyitem"><dt>%s &mdash; %d</dt><dd>%s</dd></div>' % (g, n, E(GRAMMAR_NOTE[g])))
    a("</dl>")
    a("</section>")

    a("<footer>")
    a("<p>Word counts are budgets, not inventories &mdash; the words themselves are not yet written. "
      "Sample callouts on each card show the kind of vocabulary the plate carries and are illustrative only.</p>")
    a("<p>Costs assume a run of 100 and are drawn from the same model as "
      "<span class='mono'>lexicon_model.xlsx</span>. Generated from "
      "<span class='mono'>plates/lexicon_domains.py</span> &mdash; edit the list there, rebuild this page.</p>")
    a("</footer>")
    a("</div></main>")
    a("<script>%s</script>" % JS)

    open("lexicon_reference.html", "w", encoding="utf-8").write("\n".join(out))
    print("wrote lexicon_reference.html — %d plates, %d sections, %s words"
          % (N_PLATES, len(SECTIONS), "{:,}".format(N_WORDS)))
    print("Ti $%.0f/set (%d panels) | Ceramic+decal $%.0f/set" % (TI_COST, TI_PANELS, CE_COST))


if __name__ == "__main__":
    build()
