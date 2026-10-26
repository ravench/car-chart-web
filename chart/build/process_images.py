#!/usr/bin/env python3
"""Resize carsized PNGs to WebP tiles and write the image manifest for gen.py.

Usage: python3 process_images.py <src_dir> <out_dir> [max_width=800] [quality=86]
  <src_dir> holds <id>-side.png / <id>-front.png (and optionally manifest.json from the downloader).
Writes <out_dir>/img/<id>-side.webp, <out_dir>/img/<id>-front.webp and <out_dir>/img_manifest.json:
  {id: {"side": "img/<id>-side.webp", "front": "...", "sw": w, "sh": h, "fw": w, "fh": h}}
Images are trimmed of surrounding white space (carsized renders on white) before resizing, so the
car fills the tile; the trim keeps a 2 % margin.
"""
import sys, os, json, glob
from PIL import Image, ImageChops

src, out = sys.argv[1], sys.argv[2]
MAXW = int(sys.argv[3]) if len(sys.argv) > 3 else 800
Q = int(sys.argv[4]) if len(sys.argv) > 4 else 86
os.makedirs(os.path.join(out, 'img'), exist_ok=True)
manifest = {}

def trim(im):
    """Crop to the non-white (or non-transparent) bounding box with a small margin."""
    if im.mode in ('RGBA', 'LA'):
        alpha = im.getchannel('A')
        bbox = alpha.getbbox()
    else:
        im = im.convert('RGB')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        diff = ImageChops.difference(im, bg).convert('L').point(lambda p: 255 if p > 12 else 0)
        bbox = diff.getbbox()
    if not bbox: return im
    l, t, r, b = bbox
    mx, my = int((r - l) * 0.02) + 2, int((b - t) * 0.02) + 2
    return im.crop((max(0, l - mx), max(0, t - my), min(im.width, r + mx), min(im.height, b + my)))

n = 0
for path in sorted(glob.glob(os.path.join(src, '*.png')) + glob.glob(os.path.join(src, '*.webp'))):
    base = os.path.splitext(os.path.basename(path))[0]
    if base.endswith('-side'): mid, kind = base[:-5], 'side'
    elif base.endswith('-front'): mid, kind = base[:-6], 'front'
    else: continue
    try:
        im = Image.open(path)
        im.load()
        if im.mode == 'P': im = im.convert('RGBA')
        im = trim(im)
        if im.mode == 'RGBA':
            bg = Image.new('RGB', im.size, (255, 255, 255)); bg.paste(im, mask=im.getchannel('A')); im = bg
        else: im = im.convert('RGB')
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        rel = f'img/{mid}-{kind}.webp'
        im.save(os.path.join(out, rel), 'WEBP', quality=Q, method=6)
        e = manifest.setdefault(mid, {})
        e[kind] = rel; e[kind[0] + 'w'] = im.width; e[kind[0] + 'h'] = im.height
        n += 1
    except Exception as ex:
        print('FAILED', path, ex)
json.dump(manifest, open(os.path.join(out, 'img_manifest.json'), 'w'), indent=0)
tot = sum(os.path.getsize(os.path.join(out, 'img', f)) for f in os.listdir(os.path.join(out, 'img')))
print(f'{n} images -> {len(manifest)} models, {tot/1e6:.1f} MB total')
