const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'domcontentloaded' }); await p.waitForTimeout(800);
  for (const id of ['ligier-js60', 'casalini-650', 'aixam-city', 'chatenet-ch46']) {
    await p.click(`.tile[data-id="${id}"]`); await p.waitForTimeout(200);
    const txt = await p.evaluate(() => document.getElementById('detail').innerText);
    const m = txt.split('\n').filter(l => /drive|Drive/.test(l)).slice(0, 3);
    console.log(id, '=>', m.join(' | ').slice(0, 420));
  }
  const chips = await p.evaluate(() => [...document.querySelectorAll('input[data-drive]')].map(i => i.dataset.drive + ':' + i.closest('label').textContent.trim()));
  console.log('drive chips', chips);
  await b.close();
})();
