"""v1.15 step D: group L finds (JS60, Wey 05, Primastar Kombi + van packshots, smart #2)."""
import ast, re
from PIL import Image

# Wey 05 cut-out: composite on white so rembg can drop the opaque ground shadow
src = 'ext/unpacked/v115/L/wey-wey-05-side-mocha26'
im = Image.open(src + '.webp').convert('RGBA')
bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
bg.convert('RGB').save(src + '-white.webp', quality=95)

s = open('build_ext.py').read()

NEW = r'''
 'ligier-js60': {'side': ('v115/L/ligier-js60-side-press89', 'R', False, "Ligier Group press photo 'NOUVELLE-JS60-ULTIMATE-89' (media.ligier.fr, September 2026 shoot of the new JS60 Ultimate in blue, 2560 px): near-true side view in a courtyard, facing left, background removed", 'https://media.ligier.fr/communique-de-presse/nouvelle-ligier-js60-la-ligier-qui-voit-plus-grand/')},
 'wey-wey-05': {'side': ('v115/L/wey-wey-05-side-mocha26-white', 'R', False, "Wey's own cut-out render of the Chinese New Mocha Hi4 (2026 model year, black; wey.com model carousel, 1948 px): true side view facing left, ground shadow removed; the Mocha is the Chinese name of the Wey 05 / Coffee 01 and shares its body shell (4,875 mm against 4,871 mm), but bumpers and wheels of the European car differ - GWM's European sites have no side view of the Wey 05", 'https://www.wey.com/mocca.html')},
 'smart-2': {'side': ('v115/L/smart-2-side-earlyorder', 'R', False, "smart's own early-order banner of the production #2 in red (de.smart.com #2 page, 4096 px original used at 2048 px): near-true side view (slight wide-angle lens) in a red studio set, facing left, background removed", 'https://de.smart.com/de/models/hashtag-two/')},
'''
anchor = "\n 'maxus-t90-ev': {"
assert s.count(anchor) == 1
s = s.replace(anchor, NEW + anchor[1:], 1)

def repl_side(key, new_side):
    global s
    m = re.search(r"^ '%s': \{'side': \(.*?\), 'front'" % re.escape(key), s, re.M)
    assert m, key
    s = s[:m.start()] + " '%s': {'side': %s, 'front'" % (key, new_side) + s[m.end():]

repl_side('nissan-primastar-kombi', """('v115/L/nissan-primastar-kombi-side-eutile', 'R', True, "Nissan's own packshot of the Primastar Kombi L1 (nissan.de vehicle-page asset 'Primastar-combi_de.jpg', 600 px - small): true side view on white, mirrored to face left; replaces the v1.13 dimension drawing", 'https://www.nissan.de/fahrzeuge/neuwagen/primastar/primastar-kombi.html')""")
repl_side('nissan-primastar-van-mid', """('v115/L/bonus-nissan-primastar-van-mid-side-eutile', 'R', True, "Nissan's own packshot of the Primastar panel van L1H1 (nissan.de vehicle-page asset 'Primastar fourgon.jpg', 600 px - small): true side view on white, mirrored to face left; replaces the v1.13 dimension drawing (a 2021 press photo of the van was the alternative)", 'https://www.nissan.de/fahrzeuge/neuwagen/primastar.html')""")

ast.parse(s)
open('build_ext.py', 'w').write(s)
print('build_ext.py patched, syntax OK')
