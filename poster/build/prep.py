import json,sys
from PIL import Image, ImageChops
src=sys.argv[1]
d=json.load(open(src+'/build/data.json'));man=json.load(open(src+'/img_manifest.json'))
out={}
for g in d['twin_groups']:
  for i in g['members']:
    e=man.get(i)
    if not e or 'side' not in e: continue
    im=Image.open(src+'/'+e['side'])
    if im.mode in ('RGBA','LA','P'):
      im=im.convert('RGBA'); bgc=Image.new('RGBA',im.size,(255,255,255,255)); bgc.alpha_composite(im); im=bgc
    im=im.convert('RGB')
    diff=ImageChops.difference(im,Image.new('RGB',im.size,(255,255,255))).convert('L').point(lambda p:255 if p>14 else 0)
    bb=diff.getbbox(); im=im.crop(bb)
    im.save(f'img/{i}.jpg',quality=93,subsampling=0)
    out[i]=im.size
json.dump(out,open('imgsizes.json','w'))
print(len(out))
