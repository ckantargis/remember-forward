"""
Push corrected documents to the existing Internet Archive item, and remove
superseded ones.

upload_to_archive.py re-uploads the whole plate set and only writes item
metadata on the first PUT. This does neither: it touches only the named files.

    python sync_archive_files.py            # dry run
    python sync_archive_files.py --apply

DELETES ARE IRREVERSIBLE. Nothing is removed without --apply, and every removal
must be listed explicitly in DELETE below.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

IDENTIFIER = "remember-forward-patient-message-plates"
HERE = os.path.dirname(os.path.abspath(__file__))

# local path (relative to repo root)  ->  remote path in the IA item
UPLOAD = [
    ("containers/gd_09_flyer_hdpe.docx",   "containers/gd_09_flyer_hdpe.docx"),
    ("containers/gd_09_flyer_hdpe.pdf",    "containers/gd_09_flyer_hdpe.pdf"),
    ("containers/gd_15_tiere_granite.docx", "containers/gd_15_tiere_granite.docx"),
    ("containers/gd_15_tiere_granite.pdf",  "containers/gd_15_tiere_granite.pdf"),
    ("containers/ERRATA.md",               "containers/ERRATA.md"),
    ("AUDIT_2026-09-01.md",                "AUDIT_2026-09-01.md"),
]

# Superseded by the reissue of 2026-09-01. gd_15 keeps its filename and is
# overwritten above, so only the PVC flyer needs removing.
DELETE = [
    "containers/gd_09_flyer_pvc.docx",
    "containers/gd_09_flyer_pvc.pdf",
]

CTYPE = {
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pdf": "application/pdf",
    ".md": "text/markdown",
}


def load_env():
    p = os.path.join(HERE, ".env")
    if not os.path.exists(p):
        return
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def live_files():
    req = urllib.request.Request(f"https://archive.org/metadata/{IDENTIFIER}",
                                 headers={"User-Agent": "rf-sync"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return {f["name"]: f for f in json.load(r).get("files", [])}


def send(method, remote, ak, sk, body=None, ctype=None, extra=None):
    url = f"https://s3.us.archive.org/{IDENTIFIER}/{urllib.parse.quote(remote)}"
    h = {"Authorization": f"LOW {ak}:{sk}",
         "x-archive-keep-old-version": "0",
         "x-archive-queue-derive": "0",
         "User-Agent": "rf-sync"}
    if ctype:
        h["Content-Type"] = ctype
    h.update(extra or {})
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.status, r.read()[:200].decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:400].decode("utf-8", "replace")


def main():
    import urllib.parse  # noqa: F401  (used in send via module scope)
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    load_env()
    ak, sk = os.environ.get("IA_ACCESS_KEY"), os.environ.get("IA_SECRET_KEY")
    if not (ak and sk):
        print("IA_ACCESS_KEY / IA_SECRET_KEY not set")
        return 1

    live = live_files()
    print("=" * 66)
    print("APPLYING" if a.apply else "DRY RUN — nothing will be written or deleted")
    print("=" * 66)

    print("\nUPLOAD")
    for local, remote in UPLOAD:
        lp = os.path.join(HERE, local)
        if not os.path.exists(lp):
            print(f"  MISSING LOCAL FILE: {local}")
            return 1
        size = os.path.getsize(lp)
        state = "replace" if remote in live else "new"
        print(f"  [{state:>7}] {remote}  ({size:,} B)")
        if a.apply:
            body = open(lp, "rb").read()
            ext = os.path.splitext(local)[1]
            st, msg = send("PUT", remote, ak, sk, body, CTYPE.get(ext, "application/octet-stream"))
            print(f"            HTTP {st} {'OK' if st in (200, 201) else msg}")

    print("\nDELETE  (irreversible)")
    for remote in DELETE:
        if remote not in live:
            print(f"  [ absent] {remote} — already gone")
            continue
        print(f"  [ DELETE] {remote}  ({live[remote].get('size','?')} B)")
        if a.apply:
            st, msg = send("DELETE", remote, ak, sk, extra={"x-archive-cascade-delete": "1"})
            print(f"            HTTP {st} {'OK' if st in (200, 204) else msg}")

    if not a.apply:
        print("\nRe-run with --apply to execute.")
    return 0


if __name__ == "__main__":
    import urllib.parse
    sys.exit(main())
