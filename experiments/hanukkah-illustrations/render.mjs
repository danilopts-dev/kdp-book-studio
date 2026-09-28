// node render.mjs [ids...]  -> out/<id>.svg, out/<id>.png (300 DPI) e out/contact.png
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { writeFileSync, mkdirSync } from 'node:fs';
import { ILLOS } from './illos.mjs';

const DPI = 300;
const only = process.argv.slice(2);
const list = only.length ? ILLOS.filter((i) => only.includes(i.id)) : ILLOS;
mkdirSync(new URL('./out/', import.meta.url), { recursive: true });

const svgDoc = (it, pxW, pxH) =>
  `<svg xmlns="http://www.w3.org/2000/svg" width="${pxW}" height="${pxH}" viewBox="0 0 ${it.w * 100} ${it.h * 100}">` +
  `<rect width="100%" height="100%" fill="#fff"/>${it.svg()}</svg>`;

const browser = await chromium.launch();
const page = await browser.newPage();
for (const it of list) {
  const pxW = Math.round(it.w * DPI), pxH = Math.round(it.h * DPI);
  const svg = svgDoc(it, pxW, pxH);
  writeFileSync(new URL(`./out/${it.id}.svg`, import.meta.url), svgDoc(it, `${it.w}in`, `${it.h}in`));
  await page.setViewportSize({ width: pxW, height: pxH });
  await page.setContent(`<html><body style="margin:0;filter:grayscale(1)">${svg}</body></html>`);
  await page.screenshot({ path: new URL(`./out/${it.id}.png`, import.meta.url).pathname, clip: { x: 0, y: 0, width: pxW, height: pxH } });
  console.log('ok', it.id, `${pxW}x${pxH}`);
}

// contact sheet em baixa resolução
const cells = list.map((it) => `<figure><div class="box">${svgDoc(it, '100%', '100%')}</div><figcaption>${it.id} · ${it.title}</figcaption></figure>`).join('');
await page.setViewportSize({ width: 1600, height: 800 });
await page.setContent(`<html><head><style>
body{filter:grayscale(1);margin:0;padding:16px;font:14px sans-serif;background:#ddd;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
figure{margin:0;background:#fff;padding:8px}.box{height:300px;display:flex;align-items:center;justify-content:center}
.box svg{max-width:100%;max-height:100%;width:auto;height:auto}figcaption{margin-top:6px}</style></head><body>${cells}</body></html>`);
await page.screenshot({ path: new URL('./out/contact.png', import.meta.url).pathname, fullPage: true });
await browser.close();
