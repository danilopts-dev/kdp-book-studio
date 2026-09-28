// node preview.mjs <id> [x y w h] [largura_px] -> out/preview-<id>.png
// Sem recorte: página inteira a 300 DPI (arquivo final) + SVG.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { writeFileSync } from 'node:fs';
import { SCENES } from './scenes.mjs';

const [id, ...rest] = process.argv.slice(2);
const sc = SCENES[id];
if (!sc) throw new Error('cena desconhecida: ' + id);
const W = sc.w * 100, H = sc.h * 100;
const crop = rest.length >= 4 ? rest.slice(0, 4).map(Number) : [0, 0, W, H];
const pxW = Number(rest[4] || (rest.length >= 4 ? 1800 : Math.round(sc.w * 300)));
const pxH = Math.round((pxW * crop[3]) / crop[2]);
const body = sc.svg();
const doc = (w, h, vb) => `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${vb.join(' ')}"><rect x="-10000" y="-10000" width="30000" height="30000" fill="#fff"/>${body}</svg>`;
if (rest.length < 4) writeFileSync(new URL(`./out/${id}.svg`, import.meta.url), doc(`${sc.w}in`, `${sc.h}in`, [0, 0, W, H]));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: pxW, height: pxH } });
await page.setContent(`<html><body style="margin:0;filter:grayscale(1)">${doc(pxW, pxH, crop)}</body></html>`);
const name = rest.length >= 4 ? `preview-${id}` : id;
await page.screenshot({ path: new URL(`./out/${name}.png`, import.meta.url).pathname, clip: { x: 0, y: 0, width: pxW, height: pxH } });
await browser.close();
console.log(`out/${name}.png ${pxW}x${pxH}`);
