"""
Correct the DESCRIPTION on the already-published Zenodo record and Internet
Archive item, without re-uploading files and without minting a new DOI.

WHY THIS EXISTS
  upload_to_zenodo.py creates a NEW deposition, which mints a NEW DOI. Running
  it to fix a typo would fragment the citation record and leave the wrong text
  standing at 10.5281/zenodo.19545922. Zenodo allows metadata edits on a
  published record that preserve the DOI: edit -> PUT metadata -> publish.

  upload_to_archive.py re-uploads every file and only sets item metadata on the
  first PUT. IA has a metadata-only write API that takes a JSON Patch instead.

WHAT IT CORRECTS (audit 2026-09-01)
  1. "engraved on nickel or stainless steel plates" -> titanium / fired ceramic.
     Substrate was reversed 2026-08-06 and never propagated to either record.
  2. Archive.org still described "46 plates (of a planned 214) as of April 2026".
     The item actually holds 477 plate files: 11 knowledge + 466 language plates
     across 55 series.

  Both records get an explicit dated errata note appended, rather than a silent
  edit — the project's own governance material says to keep the reversals in.

USAGE
  python update_published_metadata.py              # dry run, shows the diff
  python update_published_metadata.py --apply      # writes to both services
  python update_published_metadata.py --apply --only zenodo
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

ZENODO_RECORD = "19545922"
IA_IDENTIFIER = "remember-forward-patient-message-plates"

OPENING = (
    "An open-source system of laser-engraver-ready SVG plate designs for time capsules "
    "intended to preserve human knowledge and language through civilizational disruption. "
    "The Patient Message is designed to be engraved on titanium plates or fired ceramic "
    "tablets, sealed in a durable container, and buried or hidden for discovery by future "
    "people who may have lost context."
)

ERRATUM = (
    "Material note, corrected September 2026: earlier versions of this description "
    "specified nickel or stainless steel. The project substrate is titanium Grade 2, "
    "with fired ceramic as a parallel medium. Nickel was sidelined because its archival "
    "reputation rests on electroforming fidelity at micron scale, which is irrelevant at "
    "this project's 0.1 mm feature size; it also costs about twice titanium per plate and "
    "is vulnerable to sulfide attack in anoxic burial soils. The full correction log is in "
    "the GitHub repository."
)

IA_BODY = (
    "This item contains 477 plate files: 11 knowledge plates covering survival, water, "
    "agriculture, technology, governance, physics, electricity and energy generation; and "
    "466 language plates across 55 language series, including alternate pairings.\n\n"
    "Each language series comprises four plates: A (Script and writing system), "
    "B (Phonology with IPA), C (Grammar and core vocabulary), D (Running text with "
    "interlinear translation and the Bridge Phrase).\n\n"
    "The Bridge Phrase, engraved on every Plate D in every language: \"This was made for "
    "you, freely, by people who remembered forward.\"\n\n"
    "All files are CC BY-SA 4.0. Copy, distribute, engrave, and bury freely. "
    "Project: https://rememberforward.org | GitHub: https://github.com/ckantargis/remember-forward"
)


def load_env():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def req(method, url, token=None, data=None, headers=None, form=False):
    h = dict(headers or {})
    body = None
    if data is not None:
        if form:
            body = urllib.parse.urlencode(data).encode()
            h["Content-Type"] = "application/x-www-form-urlencoded"
        else:
            body = json.dumps(data).encode()
            h["Content-Type"] = "application/json"
    if token:
        h["Authorization"] = f"Bearer {token}"
    h.setdefault("User-Agent", "remember-forward-metadata-update")
    r = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            raw = resp.read().decode("utf-8", "replace")
            return resp.status, (json.loads(raw) if raw.strip().startswith(("{", "[")) else raw)
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        return e.code, raw


# ------------------------------------------------------------------ ZENODO
def zenodo(apply_it):
    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        print("  ZENODO_TOKEN not set — skipping")
        return False
    base = "https://zenodo.org/api"

    status, dep = req("GET", f"{base}/deposit/depositions/{ZENODO_RECORD}", token)
    if status != 200:
        print(f"  ERROR reading deposition: HTTP {status}\n  {str(dep)[:300]}")
        return False
    md = dep["metadata"]
    old = md.get("description", "")

    if "nickel" not in old.lower() and "stainless" not in old.lower():
        print("  already corrected — nothing to do")
        return True

    # keep everything after the opening sentence block, swap the opening, append erratum
    tail = old
    for marker in ("This upload contains", "<p>This upload contains"):
        if marker in tail:
            tail = tail[tail.index(marker):]
            break
    new = f"<p>{OPENING}</p>\n{tail}\n<p><em>{ERRATUM}</em></p>"

    print(f"  DOI            : {dep.get('doi', md.get('doi'))}")
    print(f"  description    : {len(old)} chars -> {len(new)} chars")
    print(f"  'nickel' before: {'nickel' in old.lower()}   after: {'nickel' in new.lower()}")
    if not apply_it:
        print("  [dry run] would: actions/edit -> PUT metadata -> actions/publish (DOI preserved)")
        return True

    s, r = req("POST", f"{base}/deposit/depositions/{ZENODO_RECORD}/actions/edit", token)
    if s not in (200, 201, 400):          # 400 = already in edit state
        print(f"  ERROR opening for edit: HTTP {s}\n  {str(r)[:300]}")
        return False
    md["description"] = new
    s, r = req("PUT", f"{base}/deposit/depositions/{ZENODO_RECORD}", token, {"metadata": md})
    if s != 200:
        print(f"  ERROR writing metadata: HTTP {s}\n  {str(r)[:300]}")
        return False
    s, r = req("POST", f"{base}/deposit/depositions/{ZENODO_RECORD}/actions/publish", token)
    if s not in (200, 202):
        print(f"  ERROR publishing: HTTP {s}\n  {str(r)[:300]}")
        return False
    print(f"  PUBLISHED — DOI unchanged: https://doi.org/10.5281/zenodo.{ZENODO_RECORD}")
    return True


# ------------------------------------------------------------------ ARCHIVE
def archive(apply_it):
    ak, sk = os.environ.get("IA_ACCESS_KEY"), os.environ.get("IA_SECRET_KEY")
    if not (ak and sk):
        print("  IA keys not set — skipping")
        return False

    s, meta = req("GET", f"https://archive.org/metadata/{IA_IDENTIFIER}")
    if s != 200:
        print(f"  ERROR reading item: HTTP {s}")
        return False
    old = meta.get("metadata", {}).get("description", "")
    new = f"{OPENING}\n\n{IA_BODY}\n\n{ERRATUM}"

    print(f"  item           : {IA_IDENTIFIER}")
    print(f"  files          : {len(meta.get('files', []))}")
    print(f"  description    : {len(old)} chars -> {len(new)} chars")
    print(f"  'nickel' before: {'nickel' in old.lower()}   after: {'nickel' in new.lower()}")
    print(f"  '46 plates' before: {'46 plates' in old}   after: {'46 plates' in new}")
    if not apply_it:
        print("  [dry run] would PATCH /metadata/description via the IA metadata write API")
        return True

    patch = [{"op": "replace", "path": "/description", "value": new}]
    s, r = req("POST", f"https://archive.org/metadata/{IA_IDENTIFIER}",
               data={"-target": "metadata", "-patch": json.dumps(patch),
                     "access": ak, "secret": sk}, form=True)
    body = r if isinstance(r, dict) else {}
    ok = s == 200 and body.get("success") is True
    print(f"  HTTP {s} — {'UPDATED' if ok else 'CHECK RESPONSE'}: {str(r)[:200]}")
    return ok


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="actually write (default is dry run)")
    p.add_argument("--only", choices=["zenodo", "archive"])
    a = p.parse_args()
    load_env()

    print("=" * 64)
    print("APPLYING" if a.apply else "DRY RUN — nothing will be written")
    print("=" * 64)
    ok = True
    if a.only in (None, "zenodo"):
        print("\nZENODO")
        ok &= zenodo(a.apply)
    if a.only in (None, "archive"):
        print("\nARCHIVE.ORG")
        ok &= archive(a.apply)
    print()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
