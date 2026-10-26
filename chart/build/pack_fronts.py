#!/usr/bin/env python3
"""Pack the front views into <out>/img/fronts.json ({id: base64 WebP}) so that they count as one served data file
(artifacts allow at most 511 files per version and serve no raw binary type). The single <id>-front.webp files are kept
out of the publish set in <out>/img_front_src/. Usage: pack_fronts.py <out_dir>"""
import sys, os, json, glob, shutil, base64
out = sys.argv[1]; src = os.path.join(out, 'img'); keep = os.path.join(out, 'img_front_src'); os.makedirs(keep, exist_ok=True)
for f in glob.glob(os.path.join(src, '*-front.webp')):
    shutil.move(f, os.path.join(keep, os.path.basename(f)))
idx = {}; total = 0
for f in sorted(glob.glob(os.path.join(keep, '*-front.webp'))):
    b = open(f, 'rb').read(); total += len(b)
    idx[os.path.basename(f)[:-len('-front.webp')]] = base64.b64encode(b).decode('ascii')
old = os.path.join(src, 'fronts.bin')
if os.path.exists(old): os.remove(old)
json.dump(idx, open(os.path.join(src, 'fronts.json'), 'w'), separators=(',', ':'))
print(f'{len(idx)} front views packed, {total/1e6:.1f} MB raw, {os.path.getsize(os.path.join(src, "fronts.json"))/1e6:.1f} MB json')
