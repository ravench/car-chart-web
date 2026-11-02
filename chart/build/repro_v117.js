const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + process.argv[2], { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForTimeout(1500);
  const info = await p.evaluate(() => {
    const rows = [...document.querySelectorAll('input[data-row]')].map(i => [i.dataset.row, i.closest('label').textContent.trim()]);
    const pts = [...document.querySelectorAll('input[data-pt]')].map(i => [i.dataset.pt, i.closest('label').textContent.trim()]);
    return { rows, pts };
  });
  console.log(JSON.stringify(info));
  // smallest three classes = first three row chips; hybrid powertrains = every pt chip whose key or label contains 'hybrid' / 'hev'
  const res = await p.evaluate(() => {
    const rI = [...document.querySelectorAll('input[data-row]')], pI = [...document.querySelectorAll('input[data-pt]')];
    rI.forEach((i, k) => { i.checked = k < 3; });
    pI.forEach(i => { const l = (i.dataset.pt + ' ' + i.closest('label').textContent).toLowerCase(); i.checked = /hybrid|hev/.test(l); });
    rI[0].dispatchEvent(new Event('change', { bubbles: true }));
    const bh = [...document.querySelectorAll('.bhdr:not(.hide)')];
    const tiles = [...document.querySelectorAll('.tile')];
    const out = bh.map(h => { const vt = tiles.filter(t => t.dataset.brand === h.dataset.brand && !t.classList.contains('hide')); return [h.dataset.brand, vt.length, vt.map(t => t.dataset.id + '@' + t.dataset.row + ' pt=' + t.dataset.pt).join('; ')]; });
    const ptSel = pI.filter(i => i.checked).map(i => i.dataset.pt);
    const rowsSel = rI.filter(i => i.checked).map(i => i.dataset.row);
    return { ptSel, rowsSel, cols: out };
  });
  console.log(JSON.stringify(res, null, 1));
  console.log('pageerrors', errs);
  await b.close();
})();
