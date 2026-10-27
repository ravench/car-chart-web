const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  const errors = []; page.on('pageerror', e => errors.push(String(e))); page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await page.goto('file://' + process.argv[2] + '/index.html'); await page.waitForTimeout(1500);
  await page.screenshot({ path: 'shots/v14_top.png' });
  const imgStats = await page.evaluate(() => { const ims = [...document.querySelectorAll('.tile img.v-side')]; return { tiles: document.querySelectorAll('.tile').length, withImg: ims.length, loaded: ims.filter(i => i.complete && i.naturalWidth > 0).length, missing: document.querySelectorAll('.tile .img.missing').length, noimg: document.querySelectorAll('.tile .noimg').length }; });
  // detail panel for the Golf
  const clickRes = await page.evaluate(() => { try { document.querySelector('.tile[data-id="volkswagen-golf"]').click(); return 'ok hidden=' + document.getElementById('detail').hidden; } catch (e) { return 'ERR ' + e.stack; } }); console.log('click:', clickRes); await page.waitForTimeout(300);
  if (errors.length) console.log('ERRORS so far:', errors.slice(0, 3).join('\n'));
  const det = await page.evaluate(() => document.getElementById('detail').innerText);
  await page.locator('#detail').screenshot({ path: 'shots/v14_detail_golf.png' });
  await page.evaluate(() => document.querySelector('.tile[data-id="citroen-berlingo"]').click()); await page.waitForTimeout(300);
  const det2 = await page.evaluate(() => document.getElementById('detail').innerText);
  await page.locator('#detail').screenshot({ path: 'shots/v14_detail_berlingo.png' });
  await page.evaluate(() => { document.getElementById('detail').hidden = true; });
  // measurement check section
  const h = page.locator('h2', { hasText: 'Measurement check' }); await h.scrollIntoViewIfNeeded(); await page.waitForTimeout(200);
  const y = await h.evaluate(e => e.getBoundingClientRect().top + window.scrollY);
  await page.evaluate(y => window.scrollTo(0, y - 10), y); await page.waitForTimeout(200);
  await page.screenshot({ path: 'shots/v14_check.png' });
  const mc = await page.evaluate(() => { const h = [...document.querySelectorAll('h2')].find(x => x.textContent.includes('Measurement check')); let t = ''; let n = h.nextElementSibling; while (n && n.tagName !== 'H2') { t += n.innerText + '\n'; n = n.nextElementSibling; } return t; });
  // true scale mode screenshot of the c-suv row
  await page.evaluate(() => { window.scrollTo(0, 0); document.getElementById('true-scale').click(); }); await page.waitForTimeout(500);
  await page.screenshot({ path: 'shots/v14_scale.png' });
  console.log(JSON.stringify({ imgStats, errors: errors.slice(0, 5) }, null, 1));
  console.log('--- GOLF DETAIL ---\n' + det.slice(0, 1500));
  console.log('--- BERLINGO DETAIL ---\n' + det2.slice(0, 1200));
  console.log('--- MEASUREMENT CHECK (first 1800 chars) ---\n' + mc.slice(0, 1800));
  await b.close();
})();
