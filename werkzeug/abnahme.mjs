// Abnahme: rendert jede Seite bei 375 und 1440 px, prüft Bilder, Konsole, waagerechtes Scrollen, Reduced-Motion.
// Aufruf: node werkzeug/abnahme.mjs [ausgabeordner]
import { pathToFileURL } from 'node:url';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const { Browser } = await import(pathToFileURL('C:/AI-Assistent/.claude/skills/taste-skill/scripts/lib/cdp.mjs').href);
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\//, '')), '..');
const out = path.resolve(process.argv[2] || path.join(root, 'abnahme-2026-11-25'));
fs.mkdirSync(out, { recursive: true });
const types = { '.html': 'text/html; charset=utf-8', '.svg': 'image/svg+xml', '.css': 'text/css', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp' };
const srv = http.createServer((q, r) => {
  let u = decodeURIComponent(q.url.split('?')[0]); if (u.endsWith('/')) u += 'index.html';
  const f = path.join(root, u);
  if (!f.startsWith(root) || !fs.existsSync(f)) { r.writeHead(404); r.end('404'); console.log('404', u); return; }
  r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r);
});
await new Promise(ok => srv.listen(0, '127.0.0.1', ok));
const base = `http://127.0.0.1:${srv.address().port}`;
const pages = ['', 'beispiel-1/', 'beispiel-2/', 'beispiel-3/'];
const names = ['auswahl', 'beispiel-1', 'beispiel-2', 'beispiel-3'];
const b = await Browser.launch({ width: 1440, height: 900 });
const report = [];
for (let i = 0; i < pages.length; i++) {
  for (const [w, h, mobile, tag, reduced] of [[375, 812, true, 'handy', false], [1440, 900, false, 'desktop', false], [1440, 900, false, 'desktop-reduced', true]]) {
    const p = await b.newPage({ width: w, height: h, mobile, reducedMotion: reduced });
    // Windows meldet hier oft "reduzierte Bewegung" schon vom System: ausdrücklich setzen
    await p.send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: reduced ? 'reduce' : 'no-preference' }] });
    const errs = [];
    await p.send('Log.enable');
    b.on(p.sessionId, 'Log.entryAdded', (e) => { if (['error', 'warning'].includes(e.entry.level)) errs.push(e.entry.level + ': ' + e.entry.text + ' ' + (e.entry.url || '')); });
    b.on(p.sessionId, 'Runtime.consoleAPICalled', (e) => { if (['error', 'assert'].includes(e.type)) errs.push('console.' + e.type + ': ' + (e.args || []).map(a => a.value ?? a.description).join(' ')); });
    await p.goto(`${base}/${pages[i]}`, { settleMs: 1800 });
    // durchscrollen, Einblend-Klassen setzen
    await p.eval(async () => {
      const H = document.documentElement.scrollHeight;
      for (let y = 0; y < H; y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
      window.scrollTo(0, 0);
      document.querySelectorAll('[data-r]').forEach(e => e.classList.add('in'));
      await new Promise(r => setTimeout(r, 1300));
    });
    const info = await p.eval(() => {
      const imgs = [...document.images].map(i => ({ src: i.getAttribute('src'), ok: (i.complete && i.naturalWidth > 0) || i.getClientRects().length === 0 }));
      const bad = imgs.filter(i => !i.ok).map(i => i.src);
      const de = document.documentElement;
      const wide = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('nav ul, .tick, .stage, [data-par], .hero, .band, .gal figure, figure'); }).slice(0, 4).map(e => e.tagName + '.' + e.className);
      const running = document.getAnimations().filter(a => a.playState === 'running' && a.effect && a.effect.getComputedTiming().iterations === Infinity).length;
      return { n: imgs.length, bad, scrollW: de.scrollWidth, clientW: de.clientWidth, h: de.scrollHeight, wide, infinite: running, fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family) };
    });
    const f = path.join(out, `${names[i]}-${tag}.png`);
    await p.screenshot({ path: f, format: 'png', fullPage: true });
    report.push({ seite: names[i], ansicht: tag, ...info, horizontal: info.scrollW > info.clientW, konsole: [...errs, ...p.consoleErrors] });
    await p.close();
  }
}
await b.close(); srv.close();
fs.writeFileSync(path.join(out, 'abnahme.json'), JSON.stringify(report, null, 1));
for (const r of report) console.log(r.seite, r.ansicht, 'bilder', r.n, 'kaputt', r.bad.length, 'horizontal', r.horizontal, `${r.scrollW}/${r.clientW}`, 'hoehe', r.h, 'endlos', r.infinite, 'konsole', r.konsole.length, r.konsole.join(' | '), r.wide.join(','));
