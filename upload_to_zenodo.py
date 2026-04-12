#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upload Remember Forward plate series to Zenodo.

SETUP (one time):
  1. Go to https://zenodo.org/account/settings/applications/tokens/new/
  2. Create a token with scope: deposit:actions, deposit:write
  3. Set environment variable:
       set ZENODO_TOKEN=your_token_here
     Or edit the line below marked EDIT THIS.

THEN RUN:
  python upload_to_zenodo.py

To use the SANDBOX (test, no real DOI):
  python upload_to_zenodo.py --sandbox

The script creates a new Zenodo deposition, uploads all SVG plates as a
single ZIP archive, and submits for publication. On success it prints the DOI
and the Zenodo URL.
"""

import os
import sys
import json
import time
import zipfile
import argparse
import urllib.request
import urllib.error
import urllib.parse
import io

# ─── CREDENTIALS ─────────────────────────────────────────────────────────────
# Edit this line, OR set environment variable ZENODO_TOKEN
TOKEN = os.environ.get('ZENODO_TOKEN', 'EDIT_THIS_your_zenodo_token')

# ─── ENDPOINTS ───────────────────────────────────────────────────────────────
PROD_URL    = 'https://zenodo.org/api'
SANDBOX_URL = 'https://sandbox.zenodo.org/api'

# ─── METADATA ─────────────────────────────────────────────────────────────────
METADATA = {
    'title': 'Remember Forward — The Patient Message: Complete Plate Series (April 2026)',
    'upload_type': 'dataset',
    'description': (
        '<p>An open-source system of laser-engraver-ready SVG plate designs '
        'for time capsules intended to preserve human knowledge and language '
        'through civilizational disruption. The Patient Message is designed to be '
        'engraved on nickel or stainless steel plates, sealed in a durable container, '
        'and buried or hidden for discovery by future people who may have lost context.</p>'
        '<p>This upload contains the complete plate series as of April 2026: '
        '11 knowledge plates (survival, water, agriculture, technology, governance, '
        'physics, electricity, energy generation); '
        '232 main language plates across 58 language series spanning all major world '
        'language families (Indo-European, Semitic, Dravidian, Sino-Tibetan, Austronesian, '
        'Niger-Congo, Afroasiatic, sign languages, and more); '
        'and 232 alternate draft plates pairing each language with a geographically '
        'nearby secondary language to show structural contrast between neighboring traditions.</p>'
        '<p>Each language series comprises four plates: '
        'A (Script and writing system), B (Phonology with IPA), '
        'C (Grammar and core vocabulary), '
        'D (Running text with interlinear translation and the Bridge Phrase).</p>'
        '<p>The Bridge Phrase — engraved on every Plate D in every language:<br>'
        '<em>"This was made for you, freely, by people who remembered forward."</em></p>'
        '<p>All files are CC BY-SA 4.0. Copy, distribute, engrave, and bury freely.<br>'
        'Project: https://rememberforward.org | '
        'GitHub: https://github.com/ckantargis/remember-forward</p>'
    ),
    'access_right': 'open',
    'license': 'CC-BY-SA-4.0',
    'creators': [
        {'name': 'Remember Forward', 'affiliation': 'Remember Forward LLC (pending)'},
    ],
    'keywords': [
        'time capsule', 'knowledge preservation', 'language preservation',
        'civilizational continuity', 'SVG', 'laser engraving', 'open source',
        'writing systems', 'interlinear translation', 'IPA', 'sign languages',
        'post-catastrophe', 'multilingual',
    ],
    'notes': (
        'This archive is also mirrored on the Internet Archive at '
        'https://archive.org/details/remember-forward-patient-message-plates'
    ),
    'related_identifiers': [
        {
            'identifier': 'https://github.com/ckantargis/remember-forward',
            'relation': 'isSupplementTo',
            'scheme': 'url',
        }
    ],
}

BASE = os.path.dirname(os.path.abspath(__file__))


# ─── FILE COLLECTION ──────────────────────────────────────────────────────────

def collect_files():
    """Return list of (local_abs_path, path_in_zip) tuples."""
    files = []

    kdir = os.path.join(BASE, 'plates', 'knowledge')
    if os.path.isdir(kdir):
        for fname in sorted(os.listdir(kdir)):
            if fname.endswith('.svg'):
                files.append((os.path.join(kdir, fname), f'plates/knowledge/{fname}'))

    ldir = os.path.join(BASE, 'plates', 'languages')
    if os.path.isdir(ldir):
        for lang in sorted(os.listdir(ldir)):
            lang_path = os.path.join(ldir, lang)
            if not os.path.isdir(lang_path):
                continue
            for fname in sorted(os.listdir(lang_path)):
                if fname.endswith('.svg'):
                    files.append((os.path.join(lang_path, fname),
                                  f'plates/languages/{lang}/{fname}'))

    return files


def build_zip(files):
    """Build an in-memory ZIP of all SVG files."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        for local_path, zip_path in files:
            zf.write(local_path, zip_path)
    buf.seek(0)
    return buf.read()


# ─── ZENODO API HELPERS ───────────────────────────────────────────────────────

def api_request(method, url, token, data=None, content_type='application/json'):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': content_type,
    }
    if data is not None:
        if isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
        headers['Content-Length'] = str(len(data))

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            body = resp.read().decode('utf-8', errors='replace')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {'_raw': body}
    except urllib.error.URLError as e:
        return 0, {'_raw': str(e)}


def create_deposition(base_url, token):
    status, resp = api_request('POST', f'{base_url}/deposit/depositions', token,
                               data={})
    if status not in (200, 201):
        print(f'ERROR creating deposition: HTTP {status}')
        print(json.dumps(resp, indent=2))
        sys.exit(1)
    dep_id = resp['id']
    bucket_url = resp['links']['bucket']
    print(f'  Deposition ID : {dep_id}')
    print(f'  Bucket URL    : {bucket_url}')
    return dep_id, bucket_url


def upload_zip(bucket_url, token, zip_bytes, filename='remember_forward_plates.zip'):
    url = f'{bucket_url}/{filename}'
    print(f'  Uploading {filename} ({len(zip_bytes) // 1024} KB) ...', end='', flush=True)
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/octet-stream',
        'Content-Length': str(len(zip_bytes)),
    }
    req = urllib.request.Request(url, data=zip_bytes, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            print(f' OK ({resp.status})')
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f' FAILED (HTTP {e.code})')
        print(f'  {body[:300]}')
        return False


def set_metadata(base_url, token, dep_id):
    url = f'{base_url}/deposit/depositions/{dep_id}'
    payload = {'metadata': METADATA}
    status, resp = api_request('PUT', url, token, data=payload)
    if status not in (200, 201):
        print(f'ERROR setting metadata: HTTP {status}')
        print(json.dumps(resp, indent=2)[:500])
        sys.exit(1)
    print('  Metadata set.')


def publish_deposition(base_url, token, dep_id):
    url = f'{base_url}/deposit/depositions/{dep_id}/actions/publish'
    status, resp = api_request('POST', url, token)
    if status not in (200, 201, 202):
        print(f'ERROR publishing: HTTP {status}')
        print(json.dumps(resp, indent=2)[:500])
        sys.exit(1)
    doi = resp.get('doi', resp.get('metadata', {}).get('doi', '(pending)'))
    record_url = resp.get('links', {}).get('html', '')
    return doi, record_url


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sandbox', action='store_true',
                        help='Use Zenodo sandbox (test, no real DOI)')
    parser.add_argument('--no-publish', action='store_true',
                        help='Upload and set metadata but do NOT publish (leaves as draft)')
    args = parser.parse_args()

    token = TOKEN
    if 'EDIT_THIS' in token:
        print()
        print('ERROR: Zenodo token not set.')
        print()
        print('  1. Go to https://zenodo.org/account/settings/applications/tokens/new/')
        print('  2. Create a token with scopes: deposit:actions, deposit:write')
        print('  3. Set environment variable:')
        print('       set ZENODO_TOKEN=your_token_here')
        print()
        sys.exit(1)

    base_url = SANDBOX_URL if args.sandbox else PROD_URL
    mode = 'SANDBOX' if args.sandbox else 'PRODUCTION'
    print(f'Remember Forward — Zenodo Upload ({mode})')
    print()

    # Collect files
    files = collect_files()
    main_plates = [f for f in files if '_alt' not in f[1]]
    alt_plates   = [f for f in files if '_alt' in f[1]]
    print(f'  Files to include: {len(files)} ({len(main_plates)} main + {len(alt_plates)} alt)')

    # Build ZIP
    print('  Building ZIP archive...', end='', flush=True)
    zip_bytes = build_zip(files)
    print(f' {len(zip_bytes) // 1024} KB')

    # Create deposition
    print('  Creating Zenodo deposition...')
    dep_id, bucket_url = create_deposition(base_url, token)

    # Upload ZIP
    ok = upload_zip(bucket_url, token, zip_bytes)
    if not ok:
        print('Upload failed. Deposition left as draft.')
        sys.exit(1)

    # Set metadata
    print('  Setting metadata...')
    set_metadata(base_url, token, dep_id)

    if args.no_publish:
        print()
        print(f'Draft saved (not published). Edit at:')
        print(f'  {base_url.replace("/api","")}/deposit/{dep_id}')
        return

    # Publish
    print('  Publishing...')
    doi, record_url = publish_deposition(base_url, token, dep_id)
    print()
    print('SUCCESS')
    print(f'  DOI        : {doi}')
    print(f'  Record URL : {record_url}')
    print()
    print('Add this DOI to CLAUDE.md and prior art submissions.')


if __name__ == '__main__':
    main()
