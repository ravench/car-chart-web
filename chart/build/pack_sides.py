#!/usr/bin/env python3
"""Pack side views that are NOT published as single files into <out>/img/sides.json ({id: base64 WebP}).
The chart page loads a packed side view only when img/<id>-side.webp fails to load (onerror -> sideFallback), so a
folder copy with all files never needs the pack, while the published artifact (at most 512 files per version) does.
Usage: pack_sides.py <out_dir> [id ...]   (ids are added to <out>/img/sides_packed.txt and the whole list is packed)"""
import sys, os, json, base64
out = sys.argv[1]; src = os.path.join(out, 'img'); lst = os.path.join(src, 'sides_packed.txt')
ids = [l.strip() for l in open(lst)] if os.path.exists(lst) else []
for i in sys.argv[2:]:
    if i not in ids: ids.append(i)
open(lst, 'w').write('\n'.join(ids) + '\n')
idx = {}; total = 0; missing = []
for i in ids:
    f = os.path.join(src, i + '-side.webp')
    if not os.path.exists(f): missing.append(i); continue
    b = open(f, 'rb').read(); total += len(b); idx[i] = base64.b64encode(b).decode('ascii')
json.dump(idx, open(os.path.join(src, 'sides.json'), 'w'), separators=(',', ':'))
print(f'{len(idx)} side views packed, {total/1e6:.2f} MB raw, {os.path.getsize(os.path.join(src, "sides.json"))/1e6:.2f} MB json; missing: {missing}')
