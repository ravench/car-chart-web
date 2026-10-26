#!/usr/bin/env python3
"""Contact sheet: python3 sheet.py <out.png> <cols> <cellw> <cellh> file1 [file2 ...]  (labels = file basenames)"""
import sys, os
from PIL import Image, ImageDraw
out, cols, cw, ch = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); files = sys.argv[5:]
rows = (len(files) + cols - 1) // cols
sheet = Image.new('RGB', (cols * cw, rows * (ch + 16)), (235, 235, 235)); d = ImageDraw.Draw(sheet)
for k, f in enumerate(files):
    x, y = (k % cols) * cw, (k // cols) * (ch + 16)
    try:
        im = Image.open(f); im.load()
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA'); bg = Image.new('RGB', im.size, (255, 255, 255)); bg.paste(im, mask=im.getchannel('A')); im = bg
        else: im = im.convert('RGB')
        im.thumbnail((cw - 4, ch - 4)); sheet.paste(im, (x + 2 + (cw - 4 - im.width) // 2, y + 2 + (ch - 4 - im.height) // 2))
    except Exception as e: d.text((x + 4, y + 4), 'ERR ' + str(e)[:30], fill=(200, 0, 0))
    d.text((x + 3, y + ch + 2), os.path.basename(f)[:40], fill=(0, 0, 0))
sheet.save(out); print(out, sheet.size)
