#!/usr/bin/env python3
"""Unpack records transferred as link nodes in read_page output files.
Node form:  link "@@ <name> <b64len> <fnv8> <meta...>" [ref_N] href="data:,<base64url>"
Usage: python3 -I unpack_links.py OUTDIR file1 [file2 ...]
Writes OUTDIR/<name>.webp|.json|.bin and OUTDIR/<name>.meta.json; prints a report and the names that failed."""
import sys, re, json, os, base64
def fnv(s):
    h = 0x811c9dc5
    for ch in s:
        h ^= ord(ch); h = (h * 0x01000193) & 0xffffffff
    return f'{h:08x}'
outdir = sys.argv[1]; os.makedirs(outdir, exist_ok=True)
ok = bad = 0; names = []; badn = []
pat = re.compile(r'^\s*link "@@ ([^" ]+) (\d+) ([0-9a-f]{8})([^"]*)" \[ref_\d+\] href="data:,([A-Za-z0-9_-]*)"', re.M)
for fn in sys.argv[2:]:
    raw = open(fn, encoding='utf-8').read()
    try:
        arr = json.loads(raw); txt = ''.join(x.get('text', '') for x in arr)
    except Exception:
        txt = raw
    end = re.search(r'generic "@@END (\d+)"', txt)
    recs = pat.findall(txt)
    if not end: print(f'{fn}: WARNING no @@END marker (truncated?) — {len(recs)} link records found')
    elif int(end.group(1)) != len(recs): print(f'{fn}: WARNING header says {end.group(1)} records, found {len(recs)}')
    for name, blen, h, meta, b64 in recs:
        if len(b64) != int(blen) or fnv(b64) != h:
            bad += 1; badn.append(name); print(f'BAD {name}: len {len(b64)} vs {blen}, hash {fnv(b64)} vs {h}'); continue
        data = base64.urlsafe_b64decode(b64 + '=' * (-len(b64) % 4))
        if data[:4] == b'RIFF': ext = '.webp'
        elif data[:1] in (b'{', b'['): ext = '.json'
        else: ext = '.bin'
        open(os.path.join(outdir, name + ext), 'wb').write(data)
        json.dump({'name': name, 'meta': meta.split(), 'bytes': len(data)}, open(os.path.join(outdir, name + '.meta.json'), 'w'))
        ok += 1; names.append(name)
print(f'{ok} records ok, {bad} bad -> {outdir}')
print('OK:', ' '.join(names))
if badn: print('BAD:', ' '.join(badn))
