"""v1.15 step C: add SEL entries for the F/J/K/I/G finds, clean soft shadows, flag automoto.it."""
import ast, re, sys
from PIL import Image
import numpy as np

# 1. alpha cleaning of transparent sources with soft ground shadows
for src, thr in [
    ('ext/unpacked/v115/F/xpeng-l03-side-cfg', 160),
    ('ext/unpacked/v115/F/xpeng-g9l-side-cfg', 160),
    ('ext/unpacked/v115/I/mitsubishi-l200-side-clubcab', 170),
]:
    im = Image.open(src + '.webp').convert('RGBA')
    a = np.array(im)
    al = a[:, :, 3]
    print(src, 'pixels dropped', int(((al > 0) & (al < thr)).sum()))
    al[al < thr] = 0
    a[:, :, 3] = al
    Image.fromarray(a).save(src + '-clean.webp', lossless=True)

s = open('build_ext.py').read()
orig = s

NEW = r'''
 'xpeng-l03': {'side': ('v115/F/xpeng-l03-side-cfg-clean', 'a', False, "XPeng's own configurator render (store.xpeng.com/de L03 configurator, exterior view 2 of 3, transparent PNG 2048 px, car about 1640 px): true side view of the European L03 in white with a black roof, facing left; the soft ground shadow in the alpha channel removed", 'https://store.xpeng.com/de/configurator/L03')},
 'xpeng-g9l': {'side': ('v115/F/xpeng-g9l-side-cfg-clean', 'a', False, "XPeng's own configurator render (store.xpeng.com/de G9L configurator, exterior view 2 of 3, transparent PNG 2048 px, car about 1500 px): true side view in silver-white, facing left; soft ground shadow removed", 'https://store.xpeng.com/de/configurator/G9L')},
 'denza-z9-gt': {'side': ('v115/F/denza-z9-gt-side-studio', 'R', False, "Denza's own studio picture from the European Z9 GT page (denza.com/de, 'eu-model-introduction' exterior image 2, 2400 px): near-true side view in teal, facing left; light-grey studio background and floor reflection removed", 'https://www.denza.com/de/z9gt')},
 'denza-d9': {'side': ('v115/F/denza-d9-side', 'R', False, "Denza's own studio picture from the European D9 page (denza.com/de, exterior image 2, 2400 px): side view of the European D9 in dark blue, facing left, studio gradient background removed; the camera sits a few degrees towards the front, so the edge of the grille shows (near-side view)", 'https://www.denza.com/de/d9'), 'front': ('v115/F/denza-d9-front-eu', 'R', False, "Denza's own studio front view from the same European D9 page (exterior image 1), background removed", 'https://www.denza.com/de/d9')},
 'chatenet-ch46': {'side': ('v115/J/chatenet-ch46-side-automoto2019', 'R', False, "third-party catalogue photo (automoto.it CH46 listing of 2019, 2000 px, soft/upscaled): true side view in white with a black roof, facing left, grey studio background removed; the body is the current CH46 shell (Chatenet's own site has only lifestyle and three-quarter pictures) - placeholder until a brand-own side view is found", 'https://www.automoto.it/catalogo/chatenet/ch46')},
 'wey-wey-03': {'side': ('v115/K/wey-wey-03-side-press66', 'R', False, "GWM Germany press photo 'GWM-WEY-03_-66' (presse.gwm-motor.de, June 2024 set, 2560 px, used at 1536 px): true side view of the white Wey 03 on a lake shore, facing left, background removed", 'https://presse.gwm-motor.de/')},
 'mhero-mhero-i': {'side': ('v115/K/mhero-mhero-i-side-zigwheels', 'R', False, "third-party catalogue photo (zigwheels.ae, 'Side View (Left)', 930 px): true side view of a black Mhero I in a dark architectural scene, facing left, background removed; UAE listing of the same body as the European electric car - placeholder until a brand-own side view is found", 'https://www.zigwheels.ae/newcars/Mhero/1')},
 'mitsubishi-l200': {'side': ('v115/I/mitsubishi-l200-side-clubcab-clean', 'a', True, "Mitsubishi Australia's own configurator render of the Triton (= L200, same sixth-generation body) in Impulse Blue (mitsubishi-motors.com.au, transparent PNG 1920 px): true side view, mirrored to face left, soft ground shadow removed; it shows the Club Cab body (shorter cab, longer tub) because no Double Cab pick-up side render was found - the European Double Cab shares the nose, wheelbase and overall length", 'https://www.mitsubishi-motors.com.au/vehicles/triton.html')},
 'iveco-daily': {'side': ('v115/G/iveco-daily-side-edaily-cab', 'R', False, "Iveco UK's own profile render 'eDaily_cab_MY24_profilo_SW_LHD' (iveco.com/uk eDaily page, 1048 px, vehicle about 890 px): near-true side view of the MY24 eDaily single chassis cab with a dropside body, facing left, white background removed; no side view of the Daily van exists on Iveco's sites, so the cab (shared with the diesel Daily) stands in for the family - placeholder", 'https://www.iveco.com/uk/')},
'''
anchor = "\n 'maxus-mifa-7': {"
assert s.count(anchor) == 1
s = s.replace(anchor, NEW + anchor[1:], 1)

# existing entries: replace the side part, keep the front part
def repl_side(key, new_side):
    global s
    m = re.search(r"^ '%s': \{'side': \(.*?\), 'front'" % re.escape(key), s, re.M)
    assert m, key
    s = s[:m.start()] + " '%s': {'side': %s, 'front'" % (key, new_side) + s[m.end():]

repl_side('nissan-townstar-van-small', """('v115/K/nissan-townstar-van-small-side-37afe1', 'R', True, "Nissan Europe press photo from the 2021 Townstar reveal gallery (europe.nissannews.com, photo 6, public 928 px copy, van about 580 px): true side view of the white L1 van in a city scene, background removed, mirrored to face left; small source", 'https://europe.nissannews.com/')""")
repl_side('nissan-primastar-van-mid', """('v115/K/nissan-primastar-van-mid-side-107793', 'R', True, "Nissan Europe press photo from the 2021 Interstar/Primastar/Townstar gallery (europe.nissannews.com, photo 14, public 928 px copy, van about 540 px): true side view of the grey L1H1 van with the 2021 nose in front of a glass building, background removed, mirrored to face left; small source", 'https://europe.nissannews.com/')""")

old_cas = " 'casalini-650': {'front': ("
assert s.count(old_cas) == 1
s = s.replace(old_cas, """ 'casalini-650': {'side': ('v115/J/casalini-650-side-starter-white', 'R', True, "Casalini's own studio photo of the 650 Starter in white (casalini.eu media library, CASALINI-starter-dx.jpg, September 2026, 2048 px): true side view, white background removed, mirrored to face left", 'https://casalini.eu/'), 'front': (""")

old_src = "    if 'carbase' in host:"
assert s.count(old_src) == 1
s = s.replace(old_src, "    if 'automoto.it' in host: return 'automoto.it (third-party catalogue photo)', 'copyright of the manufacturer / automoto.it; third-party placeholder'\n" + old_src)

ast.parse(s)
open('build_ext.py', 'w').write(s)
print('build_ext.py patched, syntax OK')
