#!/usr/bin/env python3
"""Build the web release of the Identical Car Chart for a WordPress blog.

Usage:  python3 build_release.py [CHART_DIR] [--base-url URL] [--poster PDF] [--out DIR]

CHART_DIR defaults to ../chart (git repository layout) or else the newest ../chart-vX.Y folder (project
folder layout). The poster defaults to ../poster/ or ../poster-a0/identical-car-chart-A0.pdf. The version
is read from the chart header ("Version 1.17"). Output goes to ./out/<version>/ (or --out):
  folder/              upload the contents of this folder to the web root (index.html, img/, fonts/, .htaccess)
  car-chart-<v>.zip    the same files zipped, at the top level of the archive (no parent folder)
  single/car-chart.html  one file with every picture, front view and font inlined (~30 MB)
  wordpress-embed.html   Custom HTML block for a full-screen WordPress page
  page-car-chart.php     optional page template (alternative to the block)

The chart itself is not changed: only the document skeleton, fonts, and (single file) asset
references are rewritten. Fonts are fetched once from Google Fonts into ./fonts-cache/ (Barlow
and Barlow Condensed, SIL Open Font License) so the published page makes no third-party requests.
"""
import base64, json, re, shutil, sys, urllib.request, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # carchart/
GF_URL = ('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700'
          '&family=Barlow:wght@400;500;600;700&display=swap')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
SUBSETS = ('latin', 'latin-ext')
POSTER = 'identical-car-chart-A0.pdf'
TITLE = 'Identical Car Chart'
DESC = ('Which cars are quasi the same vehicle under different badges: every brand on the European market, '
        'grouped by owner, with each model placed by vehicle class and shared-platform twins framed in colour.')


def default_chart():
    if (ROOT / 'chart' / 'index.html').exists():  # git repository layout
        return ROOT / 'chart'
    def key(p):
        return tuple(int(x) for x in re.findall(r'\d+', p.name.split('chart-v', 1)[1]))
    dirs = [p for p in ROOT.glob('chart-v*') if (p / 'index.html').exists()]
    return max(dirs, key=key)


def default_poster():
    for p in (ROOT / 'poster' / POSTER, ROOT / 'poster-a0' / POSTER):
        if p.exists():
            return p
    return ROOT / 'poster-a0' / POSTER  # missing: the release is built without the poster


def chart_version(src, html):
    m = re.search(r'Version <b>([\d.]+[a-z]?)</b>', html)
    if m:
        return 'v' + m.group(1)
    m = re.search(r'v\d+(\.\d+)*[a-z]?$', src.name)
    return m.group(0) if m else src.name


def opt(args, name, default=None):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return default


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def fonts():
    """Return list of (family, weight, subset, unicode_range, local_path), downloading once."""
    cache = HERE / 'fonts-cache'
    cache.mkdir(exist_ok=True)
    css_path = cache / 'google.css'
    if not css_path.exists():
        css_path.write_bytes(get(GF_URL))
    css = css_path.read_text()
    out = []
    for subset, body in re.findall(r'/\* ([\w-]+) \*/\s*@font-face\s*\{(.*?)\}', css, re.S):
        if subset not in SUBSETS:
            continue
        fam = re.search(r"font-family:\s*'([^']+)'", body).group(1)
        wt = re.search(r'font-weight:\s*(\d+)', body).group(1)
        url = re.search(r'url\((https://[^)]+\.woff2)\)', body).group(1)
        ur = re.search(r'unicode-range:\s*([^;]+);', body).group(1).strip()
        name = f"{fam.lower().replace(' ', '-')}-{wt}-{subset}.woff2"
        p = cache / name
        if not p.exists():
            p.write_bytes(get(url))
        out.append((fam, wt, subset, ur, p))
    assert len(out) == 14, f'expected 14 font files, got {len(out)}'
    return out


def font_css(fl, inline):
    rules = []
    for fam, wt, _, ur, p in fl:
        src = ('data:font/woff2;base64,' + base64.b64encode(p.read_bytes()).decode()) if inline else f'fonts/{p.name}'
        rules.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};font-display:swap;"
                     f"src:url({src}) format('woff2');unicode-range:{ur}}}")
    return '<style>\n' + '\n'.join(rules) + '\n</style>'


def skeleton(html, fl, inline, version):
    # drop artifact-only meta and the Google Fonts links
    html = re.sub(r'<meta name="claude:[^>]*>\n?', '', html)
    html = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\n?', '', html)
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', '', html)
    html = re.sub(r'^<meta charset="utf-8">\n?', '', html)
    html = re.sub(r'^<title>[^<]*</title>\n?', '', html)
    assert 'fonts.googleapis' not in html and '<body' not in html.lower()
    i = html.index('<header class="top">')
    head = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<title>{TITLE}</title>\n<meta name="description" content="{DESC}">\n'
        f'<meta property="og:title" content="{TITLE}">\n<meta property="og:description" content="{DESC}">\n'
        '<meta property="og:type" content="website">\n'
        f'<meta name="generator" content="Identical Car Chart {version} web release">\n'
        + font_css(fl, inline) + '\n'
    )
    return head + html[:i] + '</head>\n<body>\n' + html[i:].rstrip() + '\n</body>\n</html>\n'


def inline_assets(html, src):
    img = src / 'img'
    n = 0

    def rep(m):
        nonlocal n
        p = img / m.group(1)
        n += 1
        return 'src="data:image/webp;base64,' + base64.b64encode(p.read_bytes()).decode() + '"'
    html = re.sub(r'src="img/([^"]+\.webp)"', rep, html)
    fronts = json.loads((img / 'fronts.json').read_text())
    hook = "fetch('img/fronts.json').then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })"
    assert html.count(hook) == 1, 'front-view loader changed; update build_release.py'
    html = html.replace(hook, 'Promise.resolve(JSON.parse(document.getElementById("fronts-data").textContent))')
    blob = json.dumps(fronts, separators=(',', ':'))
    html = html.replace('</body>', f'<script type="application/json" id="fronts-data">{blob}</script>\n</body>', 1)
    # the side-picture fallback loader (img/sides.json, v1.15+) only fires when an <img> fails, which cannot
    # happen once every side picture is inlined, so its URL may stay in the code
    assert 'src="img/' not in html and "'img/" not in html.replace("'img/sides.json'", '')
    return html, n


def embed_snippets(base_url, outdir):
    base_url = base_url.rstrip('/') + '/'
    block = f'''<!-- Identical Car Chart: paste into a "Custom HTML" block on an empty page.
     It covers the whole window (theme header and footer included). Change the src if you upload elsewhere. -->
<style>html,body{{overflow:hidden!important}}#car-chart-frame{{position:fixed;inset:0;z-index:999999;background:#f4f4f1}}
#car-chart-frame iframe{{border:0;width:100%;height:100%;display:block}}
#car-chart-back{{position:fixed;right:12px;top:12px;z-index:1000000;font:600 13px/1 system-ui,sans-serif;padding:8px 12px;border-radius:8px;background:#1f2a44;color:#fff;text-decoration:none;opacity:.85}}
#car-chart-back:hover{{opacity:1}}</style>
<div id="car-chart-frame"><iframe src="{base_url}index.html" title="Identical Car Chart" allow="fullscreen" referrerpolicy="no-referrer"></iframe></div>
<a id="car-chart-back" href="/">&larr; Blog</a>
'''
    (outdir / 'wordpress-embed.html').write_text(block)
    php = f'''<?php
/*
 * Template Name: Car chart (full screen)
 * Drop this file into your (child) theme folder, then pick the template for the page.
 * The page shows only the chart, full screen; the WordPress admin bar and analytics hooks still run.
 */
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
<style>html,body{{margin:0!important;height:100%;overflow:hidden}}
iframe.car-chart{{position:fixed;inset:var(--wp-admin--admin-bar--height,0) 0 0 0;border:0;width:100%;height:calc(100% - var(--wp-admin--admin-bar--height,0px))}}</style>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<iframe class="car-chart" src="{base_url}index.html" title="<?php the_title_attribute(); ?>" allow="fullscreen"></iframe>
<?php wp_footer(); ?>
</body>
</html>
'''
    (outdir / 'page-car-chart.php').write_text(php)


def main():
    args = sys.argv[1:]
    base_url = opt(args, '--base-url', 'https://car-chart.forestraven.net/')
    pdf = Path(opt(args, '--poster', default_poster())).resolve()
    out_opt = opt(args, '--out')
    src = Path(args[0]).resolve() if args else default_chart()
    raw = (src / 'index.html').read_text()
    version = chart_version(src, raw)
    out = Path(out_opt).resolve() if out_opt else HERE / 'out' / version
    if out.exists():
        shutil.rmtree(out)
    (out / 'folder').mkdir(parents=True)
    (out / 'single').mkdir()
    fl = fonts()

    # folder release (with the A0 poster PDF when the poster thread has produced one)
    fdir = out / 'folder'
    page = skeleton(raw, fl, False, version)
    if pdf.exists():
        meta_end = '</div>\n</header>'
        assert page.count(meta_end) == 1, 'header changed; update the poster link insertion'
        link = (f'<span><a href="{POSTER}" download style="text-decoration:underline">'
                f'A0 poster <b>PDF · {pdf.stat().st_size / 1e6:.0f} MB</b></a></span>')
        page = page.replace(meta_end, link + meta_end)
    (fdir / 'index.html').write_text(page)
    if pdf.exists():
        shutil.copy(pdf, fdir / POSTER)
    shutil.copytree(src / 'img', fdir / 'img')
    # Apache: make the page and its data files revalidate on every visit (ETag -> cheap 304), so a new
    # upload shows at once; pictures and fonts keep the server's default caching. Harmless without mod_headers.
    (fdir / '.htaccess').write_text(
        '# Identical Car Chart: always revalidate the page and its data, so new uploads show immediately\n'
        '<IfModule mod_headers.c>\n'
        '  <FilesMatch "^(index\\.html|.+\\.json|.+\\.pdf)$">\n'
        '    Header set Cache-Control "no-cache"\n'
        '  </FilesMatch>\n'
        '</IfModule>\n')
    (fdir / 'fonts').mkdir()
    for *_, p in fl:
        shutil.copy(p, fdir / 'fonts' / p.name)
    (fdir / 'fonts' / 'LICENSE.txt').write_text(
        'Barlow and Barlow Condensed by Jeremy Tribby, SIL Open Font License 1.1 (https://openfontlicense.org).\n')
    zp = out / f'car-chart-{version}.zip'
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(fdir.rglob('*')):
            if f.is_file():
                z.write(f, f.relative_to(fdir))  # files at the top level, no parent folder

    # single-file release
    single, n = inline_assets(skeleton(raw, fl, True, version), src)
    (out / 'single' / 'car-chart.html').write_text(single)

    embed_snippets(base_url, out)
    mb = lambda p: p.stat().st_size / 1e6
    size = sum(f.stat().st_size for f in fdir.rglob('*') if f.is_file()) / 1e6
    print(f'source  {src}  ({version})')
    print(f'poster  {pdf if pdf.exists() else "none (no poster PDF yet)"}')
    print(f'folder  {fdir}  {size:.1f} MB')
    print(f'zip     {zp}  {mb(zp):.1f} MB')
    print(f'single  {out / "single" / "car-chart.html"}  {mb(out / "single" / "car-chart.html"):.1f} MB  ({n} side pictures inlined)')


if __name__ == '__main__':
    main()
