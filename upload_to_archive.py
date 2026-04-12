#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upload Remember Forward plate series to Internet Archive.

SETUP (one time):
  1. Go to https://archive.org/account/s3.php  (log in first)
  2. Click "Generate New Key"
  3. Copy the Access Key and Secret Key
  4. Either set environment variables:
       set IA_ACCESS_KEY=your_access_key_here
       set IA_SECRET_KEY=your_secret_key_here
     Or edit the two lines below marked EDIT THIS.

THEN RUN:
  python upload_to_archive.py

The script will create one Internet Archive item containing all 46 SVG plates,
organized into folders, with full metadata.  On success it prints the item URL.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error

# ─── CREDENTIALS ─────────────────────────────────────────────────────────────
# Edit these two lines, OR set environment variables IA_ACCESS_KEY / IA_SECRET_KEY
ACCESS_KEY = os.environ.get('IA_ACCESS_KEY', 'EDIT_THIS_your_access_key')
SECRET_KEY = os.environ.get('IA_SECRET_KEY', 'EDIT_THIS_your_secret_key')

# ─── ITEM SETTINGS ───────────────────────────────────────────────────────────
IDENTIFIER  = 'remember-forward-patient-message-plates'   # unique IA item ID
ITEM_URL    = f'https://archive.org/details/{IDENTIFIER}'

METADATA = {
    'title':       'Remember Forward — The Patient Message: Plate Series',
    'mediatype':   'data',
    'creator':     'Remember Forward',
    'date':        '2026-04-12',
    'description': (
        'An open-source system of laser-engraver-ready SVG plate designs '
        'for time capsules intended to preserve human knowledge and language '
        'through civilizational disruption. '
        'The Patient Message is designed to be engraved on nickel or stainless '
        'steel plates, sealed in a durable container, and buried or hidden for '
        'discovery by future people who may have lost context. '
        '\n\n'
        'This upload contains the complete plate series as of April 2026: '
        '11 knowledge plates (survival, water, agriculture, technology, governance, '
        'physics, electricity, energy generation, and more); '
        '232 main language plates across 58 language series spanning all major world '
        'language families (Indo-European, Semitic, Dravidian, Sino-Tibetan, Austronesian, '
        'Niger-Congo, Afroasiatic, sign languages, and more); '
        'and 232 alternate draft plates pairing each language with a geographically '
        'nearby secondary language to show structural contrast between neighboring traditions. '
        '\n\n'
        'Languages include: Hebrew (4 registers), Arabic, Tamil, Sanskrit, Bengali, '
        'Mandarin, Japanese, Malay/Indonesian, Swahili, Greek, Latin, Persian, Russian, '
        'Hindi, Yoruba, Igbo, Amharic, Tigrinya, Somali, Hausa, Zulu, Shona, Lingala, '
        'Vietnamese, Thai, Burmese, Khmer, Lao, Javanese, Tagalog, Korean, Turkish, '
        'Urdu, Pashto, Punjabi, Tibetan, Mongolian, Quechua, Nahuatl, Hawaiian, '
        'Tok Pisin, English, Dutch, German, French, Spanish, Portuguese, Italian, '
        'Latin, Greek, ASL, BSL, LSF, CSL, LIBRAS, Egyptian Arabic, Ancient Egyptian, '
        'and more. '
        '\n\n'
        'Each language series comprises four plates: '
        'A (Script and writing system), '
        'B (Phonology with IPA), '
        'C (Grammar and core vocabulary), '
        'D (Running text with interlinear translation and the Bridge Phrase). '
        '\n\n'
        'The Bridge Phrase — engraved on every Plate D in every language: '
        '"This was made for you, freely, by people who remembered forward." '
        '\n\n'
        'All files are CC BY-SA 4.0. Copy, distribute, engrave, and bury freely. '
        'Project: https://rememberforward.org | '
        'GitHub: https://github.com/ckantargis/remember-forward'
    ),
    'subject': [
        'time capsule',
        'knowledge preservation',
        'language preservation',
        'civilizational continuity',
        'SVG',
        'laser engraving',
        'open source',
        'writing systems',
        'interlinear translation',
        'IPA',
        'sign languages',
        'post-catastrophe',
        'multilingual',
        'CC BY-SA',
    ],
    'licenseurl':  'https://creativecommons.org/licenses/by-sa/4.0/',
    'source':      'https://rememberforward.org',
    'language':    'mul',   # mul = multiple languages (ISO 639-2)
}

# ─── FILE MANIFEST ────────────────────────────────────────────────────────────
# (local_path_relative_to_this_script, remote_path_in_IA_item)
BASE = os.path.dirname(os.path.abspath(__file__))

def collect_files():
    """Return list of (local_abs_path, remote_path) tuples."""
    files = []

    # Knowledge plates
    kdir = os.path.join(BASE, 'plates', 'knowledge')
    for fname in sorted(os.listdir(kdir)):
        if fname.endswith('.svg'):
            files.append((os.path.join(kdir, fname), f'plates/knowledge/{fname}'))

    # Language plates
    ldir = os.path.join(BASE, 'plates', 'languages')
    for lang in sorted(os.listdir(ldir)):
        lang_path = os.path.join(ldir, lang)
        if not os.path.isdir(lang_path):
            continue
        for fname in sorted(os.listdir(lang_path)):
            if fname.endswith('.svg'):
                files.append((os.path.join(lang_path, fname), f'plates/languages/{lang}/{fname}'))

    return files


# ─── UPLOAD ───────────────────────────────────────────────────────────────────

def build_headers(remote_path, is_first, access_key, secret_key, metadata):
    """Build HTTP headers for a single IA S3 PUT request."""
    headers = {
        'Authorization':        f'LOW {access_key}:{secret_key}',
        'Content-Type':         'image/svg+xml',
        'x-amz-auto-make-bucket': '1',
        'x-archive-queue-derive': '0',   # skip derive job (no need for SVG)
        'x-archive-keep-old-version': '0',
    }

    # Only set item-level metadata on the first file upload
    if is_first:
        # Single-value fields
        single_fields = ['title', 'mediatype', 'creator', 'date', 'description',
                         'licenseurl', 'source', 'language']
        for field in single_fields:
            if field in metadata:
                # IA uses 'x-archive-meta-FIELD' for single values
                # Values must be ASCII-safe in headers; encode non-ASCII
                val = metadata[field]
                try:
                    val.encode('ascii')
                    headers[f'x-archive-meta-{field}'] = val
                except (UnicodeEncodeError, AttributeError):
                    # Use uri encoding for non-ASCII
                    import urllib.parse
                    headers[f'x-archive-meta-{field}'] = 'uri(' + urllib.parse.quote(val, safe='') + ')'

        # Multi-value subject tags
        for i, subj in enumerate(metadata.get('subject', [])):
            headers[f'x-archive-meta{str(i).zfill(2)}-subject'] = subj

    return headers


def upload_file(identifier, remote_path, local_path, access_key, secret_key,
                metadata, is_first):
    url = f'https://s3.us.archive.org/{identifier}/{remote_path}'
    headers = build_headers(remote_path, is_first, access_key, secret_key, metadata)

    with open(local_path, 'rb') as f:
        data = f.read()

    headers['Content-Length'] = str(len(data))

    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, resp.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')
    except urllib.error.URLError as e:
        return 0, str(e)


def check_credentials(access_key, secret_key):
    if 'EDIT_THIS' in access_key or 'EDIT_THIS' in secret_key:
        print()
        print('ERROR: Credentials not set.')
        print()
        print('  1. Go to https://archive.org/account/s3.php')
        print('  2. Generate a key pair')
        print('  3. Either set environment variables:')
        print('       set IA_ACCESS_KEY=your_key_here')
        print('       set IA_SECRET_KEY=your_secret_here')
        print('     Or edit the ACCESS_KEY / SECRET_KEY lines in this script.')
        print()
        sys.exit(1)


def main():
    check_credentials(ACCESS_KEY, SECRET_KEY)

    files = collect_files()
    if not files:
        print('ERROR: No SVG files found. Run this from the remember-forward folder.')
        sys.exit(1)

    print(f'Remember Forward — Internet Archive Upload')
    print(f'Item identifier : {IDENTIFIER}')
    print(f'Files to upload : {len(files)}')
    print(f'Item URL (live after ~5 min): {ITEM_URL}')
    print()

    ok = 0
    fail = 0
    for i, (local_path, remote_path) in enumerate(files):
        is_first = (i == 0)
        fname = os.path.basename(local_path)
        size_kb = os.path.getsize(local_path) // 1024
        print(f'  [{i+1:02d}/{len(files)}] {remote_path} ({size_kb} KB) ... ', end='', flush=True)

        status, body = upload_file(
            IDENTIFIER, remote_path, local_path,
            ACCESS_KEY, SECRET_KEY, METADATA, is_first
        )

        if status in (200, 201, 204):
            print('OK')
            ok += 1
        else:
            print(f'FAILED (HTTP {status})')
            if body:
                # Print first 200 chars of error body
                print(f'    {body[:200]}')
            fail += 1

        # Brief pause to avoid hammering IA's servers
        if not is_first:
            time.sleep(0.5)

    print()
    print(f'Done. {ok} uploaded, {fail} failed.')
    if ok > 0:
        print()
        print(f'Your item will be live within a few minutes at:')
        print(f'  {ITEM_URL}')
        print()
        print(f'The permanent URL (for citations and prior art) is:')
        print(f'  https://archive.org/details/{IDENTIFIER}')
    if fail > 0:
        print()
        print('To retry failed files, simply run the script again.')
        print('IA S3 uploads are idempotent — re-uploading is safe.')


if __name__ == '__main__':
    main()
