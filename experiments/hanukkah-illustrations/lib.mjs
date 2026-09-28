// Primitivas de line art para colorir. Unidade: 1/100 de polegada.
// Tudo é traço preto uniforme sobre branco, sem sombra: formas com fill branco
// para que sobreposições escondam o que está atrás.

export const SW = 4; // espessura única de traço (0.04 in)
const ST = `stroke="#000" stroke-width="${SW}" stroke-linejoin="round" stroke-linecap="round"`;
const f = (n) => +n.toFixed(2);

export const path = (d, fill = '#fff', extra = '') => `<path d="${d}" fill="${fill}" ${ST} ${extra}/>`;
export const line = (x1, y1, x2, y2, extra = '') =>
  `<line x1="${f(x1)}" y1="${f(y1)}" x2="${f(x2)}" y2="${f(y2)}" ${ST} ${extra}/>`;
export const rect = (x, y, w, h, rx = 0, fill = '#fff', extra = '') =>
  `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" rx="${rx}" fill="${fill}" ${ST} ${extra}/>`;
export const circle = (cx, cy, r, fill = '#fff', extra = '') =>
  `<circle cx="${f(cx)}" cy="${f(cy)}" r="${f(r)}" fill="${fill}" ${ST} ${extra}/>`;
export const ellipse = (cx, cy, rx, ry, fill = '#fff', extra = '') =>
  `<ellipse cx="${f(cx)}" cy="${f(cy)}" rx="${f(rx)}" ry="${f(ry)}" fill="${fill}" ${ST} ${extra}/>`;
export const dot = (cx, cy, r = 3.2) => `<circle cx="${f(cx)}" cy="${f(cy)}" r="${r}" fill="#000"/>`;
export const poly = (pts, fill = '#fff', extra = '') =>
  `<polygon points="${pts.map(([x, y]) => `${f(x)},${f(y)}`).join(' ')}" fill="${fill}" ${ST} ${extra}/>`;
export const pline = (pts, extra = '') =>
  `<polyline points="${pts.map(([x, y]) => `${f(x)},${f(y)}`).join(' ')}" fill="none" ${ST} ${extra}/>`;
export const g = (inner, tf = '') => `<g${tf ? ` transform="${tf}"` : ''}>${inner}</g>`;
export const dashed = `stroke-dasharray="10 8"`;

export const text = (x, y, s, size = 18, anchor = 'middle', weight = 'bold', extra = '') =>
  `<text x="${f(x)}" y="${f(y)}" font-family="DejaVu Sans" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="#000" ${extra}>${s}</text>`;
// Letra vazada (contorno), para a criança colorir.
export const hollowText = (x, y, s, size, anchor = 'middle', tf = '') =>
  `<text x="${f(x)}" y="${f(y)}" font-family="DejaVu Sans" font-size="${size}" font-weight="bold" text-anchor="${anchor}" fill="#fff" stroke="#000" stroke-width="${SW * 0.9}" stroke-linejoin="round" paint-order="stroke"${tf ? ` transform="${tf}"` : ''}>${s}</text>`;

// Tubo contornado: desenha as linhas em preto grosso e depois em branco mais fino.
// Várias linhas passadas juntas se fundem sem costura nas junções.
export function tubes(ds, w) {
  const blk = ds.map((d) => `<path d="${d}" fill="none" stroke="#000" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`).join('');
  const wht = ds.map((d) => `<path d="${d}" fill="none" stroke="#fff" stroke-width="${w - 2 * SW}" stroke-linecap="round" stroke-linejoin="round"/>`).join('');
  return blk + wht;
}

export function arrow(x1, y1, x2, y2, head = 14) {
  const a = Math.atan2(y2 - y1, x2 - x1);
  const p1 = [x2 - head * Math.cos(a - 0.45), y2 - head * Math.sin(a - 0.45)];
  const p2 = [x2 - head * Math.cos(a + 0.45), y2 - head * Math.sin(a + 0.45)];
  return line(x1, y1, x2, y2) + pline([p1, [x2, y2], p2]);
}

// Gerador determinístico (mulberry32), nunca Math.random.
export function rng(seed) {
  return () => {
    seed |= 0; seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// Contorno irregular fechado e suave (latke, pedra, poeira).
export function blob(cx, cy, rx, ry, seed, wobble = 0.12, n = 14) {
  const r = rng(seed);
  const pts = [];
  for (let i = 0; i < n; i++) {
    const a = (i / n) * Math.PI * 2;
    const k = 1 + (r() - 0.5) * 2 * wobble;
    pts.push([cx + Math.cos(a) * rx * k, cy + Math.sin(a) * ry * k]);
  }
  let d = '';
  for (let i = 0; i < n; i++) {
    const p0 = pts[(i - 1 + n) % n], p1 = pts[i], p2 = pts[(i + 1) % n], p3 = pts[(i + 2) % n];
    if (i === 0) d += `M${f(p1[0])},${f(p1[1])}`;
    const c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
    const c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
    d += `C${f(c1[0])},${f(c1[1])} ${f(c2[0])},${f(c2[1])} ${f(p2[0])},${f(p2[1])}`;
  }
  return d + 'Z';
}

// ---------- Objetos do livro ----------

export function flame(cx, baseY, h) {
  const w = h * 0.36;
  const outer = `M${cx},${baseY} C${cx - w * 1.1},${baseY - h * 0.25} ${cx - w * 0.5},${baseY - h * 0.7} ${cx},${baseY - h} C${cx + w * 0.5},${baseY - h * 0.7} ${cx + w * 1.1},${baseY - h * 0.25} ${cx},${baseY}Z`;
  const ih = h * 0.5, iw = w * 0.5, iy = baseY - h * 0.08;
  const inner = `M${cx},${iy} C${cx - iw * 1.1},${iy - ih * 0.25} ${cx - iw * 0.5},${iy - ih * 0.7} ${cx},${iy - ih} C${cx + iw * 0.5},${iy - ih * 0.7} ${cx + iw * 1.1},${iy - ih * 0.25} ${cx},${iy}Z`;
  return path(outer) + path(inner);
}

export function candle(cx, bottomY, w, h, lit) {
  let s = rect(cx - w / 2, bottomY - h, w, h, 2);
  s += line(cx, bottomY - h, cx, bottomY - h - w * 0.35);
  if (lit) s += flame(cx, bottomY - h - w * 0.2, w * 2.1);
  return s;
}

// Hanukiá: 8 suportes iguais em linha + shamash mais alto e destacado no centro.
// candles/lit: arrays de 8 booleanos, da esquerda para a direita.
export function hanukkiah({ cx, baseY, W, candles = [], lit = [], shamashCandle = true, shamashLit = false }) {
  const barY = baseY - 0.4 * W;
  const barH = 0.038 * W;
  const tube = 0.04 * W;
  const d = 0.098 * W;
  const xs = [];
  for (let i = 0; i < 4; i++) xs.push(cx - 0.46 * W + i * d);
  for (let i = 0; i < 4; i++) xs.push(cx + 0.46 * W - (3 - i) * d);
  const shY = barY - 0.15 * W;
  let s = '';
  // braços decorativos + haste (tubos contornados)
  const armY = barY + barH;
  const arms = [
    `M${cx},${baseY - 0.07 * W} L${cx},${shY}`,
    `M${cx},${barY + 0.2 * W} C${cx - 0.12 * W},${barY + 0.2 * W} ${cx - 0.38 * W},${armY + 0.1 * W} ${cx - 0.42 * W},${armY}`,
    `M${cx},${barY + 0.2 * W} C${cx + 0.12 * W},${barY + 0.2 * W} ${cx + 0.38 * W},${armY + 0.1 * W} ${cx + 0.42 * W},${armY}`,
  ];
  s += tubes(arms, tube);
  // base
  s += path(`M${cx - 0.2 * W},${baseY} L${cx + 0.2 * W},${baseY} L${cx + 0.1 * W},${baseY - 0.07 * W} L${cx - 0.1 * W},${baseY - 0.07 * W}Z`);
  s += rect(cx - 0.23 * W, baseY - 0.012 * W, 0.46 * W, 0.03 * W, 4);
  // barra
  s += rect(cx - 0.5 * W, barY, W, barH, barH / 2);
  // copos
  const cupW = 0.062 * W, cupH = 0.036 * W;
  const cup = (x, y) => path(`M${x - cupW / 2},${y - cupH} L${x + cupW / 2},${y - cupH} L${x + cupW * 0.32},${y} L${x - cupW * 0.32},${y}Z`);
  const cw = 0.032 * W, ch = 0.13 * W;
  xs.forEach((x, i) => {
    s += cup(x, barY);
    if (candles[i]) s += candle(x, barY - cupH, cw, ch, lit[i]);
  });
  // shamash
  s += rect(cx - 0.045 * W, shY - 0.01 * W, 0.09 * W, 0.022 * W, 4);
  s += cup(cx, shY - 0.01 * W);
  if (shamashCandle) s += candle(cx, shY - 0.01 * W - cupH, cw, ch, shamashLit);
  return { svg: s, xs, barY, cupTop: barY - cupH, candleTop: barY - cupH - ch, shX: cx, shTop: shY - 0.01 * W - cupH - ch };
}

// Menorá do Templo: 7 braços, sem shamash separado.
export function menorah7({ cx, baseY, W, lit = false }) {
  const topY = baseY - 0.72 * W;
  const tube = 0.042 * W;
  const ds = [`M${cx},${baseY - 0.08 * W} L${cx},${topY}`];
  for (let k = 1; k <= 3; k++) {
    const r = (k * W) / 6.4;
    ds.push(`M${cx - r},${topY} A${r},${r} 0 0 0 ${cx + r},${topY}`);
  }
  let s = tubes(ds, tube);
  s += path(`M${cx - 0.22 * W},${baseY} L${cx + 0.22 * W},${baseY} L${cx + 0.12 * W},${baseY - 0.05 * W} L${cx + 0.04 * W},${baseY - 0.1 * W} L${cx - 0.04 * W},${baseY - 0.1 * W} L${cx - 0.12 * W},${baseY - 0.05 * W}Z`);
  const cupW = 0.07 * W, cupH = 0.045 * W;
  for (let k = -3; k <= 3; k++) {
    const x = cx + (k * W) / 6.4;
    s += path(`M${x - cupW / 2},${topY - cupH} L${x + cupW / 2},${topY - cupH} L${x + cupW * 0.3},${topY + 2} L${x - cupW * 0.3},${topY + 2}Z`);
    if (lit) s += flame(x, topY - cupH - 2, 0.09 * W);
  }
  return s;
}

// Pião (dreidel) visto de quina: duas faces com letras.
export function dreidel(cx, y0, s, letters = ['נ', 'ג']) {
  const w = 0.55 * s, sl = 0.15 * s, fh = 0.75 * s;
  let o = '';
  // tampa
  o += poly([[cx - w, y0 + 0.1 * s], [cx, y0 + 0.1 * s - sl], [cx + w, y0 + 0.1 * s], [cx, y0 + 0.1 * s + sl]]);
  o += ellipse(cx, y0 + 0.1 * s, 0.1 * s, 0.05 * s);
  o += rect(cx - 0.08 * s, y0 - 0.38 * s, 0.16 * s, 0.46 * s, 0.08 * s);
  // faces
  const tl = [cx - w, y0 + 0.1 * s], tm = [cx, y0 + 0.1 * s + sl], tr = [cx + w, y0 + 0.1 * s];
  o += poly([tl, tm, [tm[0], tm[1] + fh], [tl[0], tl[1] + fh]]);
  o += poly([tm, tr, [tr[0], tr[1] + fh], [tm[0], tm[1] + fh]]);
  // ponta
  const tip = [cx, y0 + 0.1 * s + fh + 0.55 * s];
  o += poly([[tl[0], tl[1] + fh], [tm[0], tm[1] + fh], tip]);
  o += poly([[tm[0], tm[1] + fh], [tr[0], tr[1] + fh], tip]);
  // letras (inclinadas junto com cada face)
  const ang = (Math.atan2(sl, w) * 180) / Math.PI;
  const fs = 0.5 * s;
  const lcx = cx - w / 2, lcy = y0 + 0.1 * s + sl / 2 + fh / 2 + fs * 0.35;
  o += hollowText(0, 0, letters[0], fs, 'middle', `translate(${lcx} ${lcy}) skewY(${ang})`);
  const rcx = cx + w / 2;
  o += hollowText(0, 0, letters[1], fs, 'middle', `translate(${rcx} ${lcy}) skewY(${-ang})`);
  return o;
}

export function sixStar(cx, cy, r, fill = '#fff') {
  const tri = (rot) => poly([0, 1, 2].map((i) => {
    const a = rot + (i * 2 * Math.PI) / 3;
    return [cx + r * Math.sin(a), cy - r * Math.cos(a)];
  }), fill);
  return tri(0) + tri(Math.PI);
}

export function sparkle(cx, cy, r) {
  const k = r * 0.28;
  return path(`M${cx},${cy - r} Q${cx + k},${cy - k} ${cx + r},${cy} Q${cx + k},${cy + k} ${cx},${cy + r} Q${cx - k},${cy + k} ${cx - r},${cy} Q${cx - k},${cy - k} ${cx},${cy - r}Z`);
}

export function coin(cx, cy, r) {
  return circle(cx, cy, r) + circle(cx, cy, r * 0.78) + sixStar(cx, cy, r * 0.45);
}

export function heart(cx, cy, s) {
  return path(`M${cx},${cy + s * 0.45} C${cx - s * 0.9},${cy - s * 0.1} ${cx - s * 0.45},${cy - s * 0.75} ${cx},${cy - s * 0.3} C${cx + s * 0.45},${cy - s * 0.75} ${cx + s * 0.9},${cy - s * 0.1} ${cx},${cy + s * 0.45}Z`);
}

export function tzedakahBox(cx, bottomY, w) {
  const h = w * 0.72, d = w * 0.22;
  let s = '';
  s += poly([[cx - w / 2, bottomY - h], [cx - w / 2 + d, bottomY - h - d * 0.6], [cx + w / 2 + d, bottomY - h - d * 0.6], [cx + w / 2, bottomY - h]]);
  s += poly([[cx + w / 2, bottomY - h], [cx + w / 2 + d, bottomY - h - d * 0.6], [cx + w / 2 + d, bottomY - d * 0.6], [cx + w / 2, bottomY]]);
  s += rect(cx - w / 2, bottomY - h, w, h, 3);
  s += rect(cx - w * 0.2 + d / 2, bottomY - h - d * 0.36, w * 0.4, d * 0.14, 3, '#000');
  s += heart(cx, bottomY - h * 0.5, w * 0.34);
  return s;
}

export function oilJar(cx, bottomY, h, sealed = true) {
  const w = h * 0.62;
  const d = `M${cx - w * 0.18},${bottomY - h * 0.82} C${cx - w * 0.2},${bottomY - h * 0.7} ${cx - w * 0.55},${bottomY - h * 0.62} ${cx - w * 0.55},${bottomY - h * 0.35} C${cx - w * 0.55},${bottomY - h * 0.1} ${cx - w * 0.3},${bottomY} ${cx},${bottomY} C${cx + w * 0.3},${bottomY} ${cx + w * 0.55},${bottomY - h * 0.1} ${cx + w * 0.55},${bottomY - h * 0.35} C${cx + w * 0.55},${bottomY - h * 0.62} ${cx + w * 0.2},${bottomY - h * 0.7} ${cx + w * 0.18},${bottomY - h * 0.82}Z`;
  let s = path(d);
  s += rect(cx - w * 0.26, bottomY - h * 0.9, w * 0.52, h * 0.09, 4);
  if (sealed) s += ellipse(cx, bottomY - h * 0.95, w * 0.22, h * 0.06) + ellipse(cx, bottomY - h * 0.95, w * 0.11, h * 0.03);
  s += path(`M${cx - w * 0.5},${bottomY - h * 0.42} Q${cx},${bottomY - h * 0.36} ${cx + w * 0.5},${bottomY - h * 0.42}`, 'none');
  return s;
}

export function latke(cx, cy, rx, seed) {
  const r = rng(seed);
  let s = path(blob(cx, cy, rx, rx * 0.3, seed, 0.08, 16));
  for (let i = 0; i < 3; i++) {
    const x = cx + (r() - 0.5) * rx * 1.1, y = cy + (r() - 0.5) * rx * 0.2;
    s += path(`M${x - rx * 0.12},${y} q${rx * 0.12},${-rx * 0.06} ${rx * 0.24},0`, 'none');
  }
  return s;
}

export function sufganiyah(cx, cy, r, seed) {
  const q = rng(seed);
  let s = path(blob(cx, cy, r, r * 0.78, seed, 0.04, 12));
  s += path(blob(cx + r * 0.1, cy - r * 0.42, r * 0.28, r * 0.16, seed + 7, 0.15, 8));
  for (let i = 0; i < 5; i++) {
    const a = q() * Math.PI * 2, d = r * (0.25 + q() * 0.4);
    s += `<circle cx="${(cx + Math.cos(a) * d).toFixed(1)}" cy="${(cy + 0.1 * r + Math.sin(a) * d * 0.6).toFixed(1)}" r="2.6" fill="#000"/>`;
  }
  return s;
}

export function frameBorder(W, H, inset = 14, gap = 10) {
  return rect(inset, inset, W - 2 * inset, H - 2 * inset, 18, 'none') +
    rect(inset + gap, inset + gap, W - 2 * (inset + gap), H - 2 * (inset + gap), 12, 'none');
}

// ---------- Pessoas (meio corpo, atrás de mesa/parapeito) ----------
// r = raio da cabeça. hair: short | long | curly | kippah | bun | ponytail
// hands: lista de [x, y] absolutos para as mãos (0, 1 ou 2).
export function person({ x, neckY, r, hair = 'short', hands = [], smile = 1, shirt = 'plain', face = 0 }) {
  let s = '';
  const hy = neckY - r * 1.02;
  const sh = r * 1.35;
  // cabelo de trás
  if (hair === 'long') s += path(`M${x - r * 1.05},${hy} C${x - r * 1.25},${hy + r * 1.6} ${x - r * 1.1},${neckY + r * 0.9} ${x - r * 0.6},${neckY + r * 0.9} L${x + r * 0.6},${neckY + r * 0.9} C${x + r * 1.1},${neckY + r * 0.9} ${x + r * 1.25},${hy + r * 1.6} ${x + r * 1.05},${hy}Z`);
  if (hair === 'ponytail') s += path(blob(x + r * 1.05, hy + r * 0.25, r * 0.35, r * 0.6, 3, 0.06, 10));
  if (hair === 'bun') s += circle(x, hy - r * 1.05, r * 0.42);
  // tronco
  s += path(`M${x - sh},${neckY + r * 0.35} Q${x - sh},${neckY} ${x - r * 0.4},${neckY} L${x + r * 0.4},${neckY} Q${x + sh},${neckY} ${x + sh},${neckY + r * 0.35} L${x + sh * 1.02},${neckY + r * 4} L${x - sh * 1.02},${neckY + r * 4}Z`);
  s += path(`M${x - r * 0.4},${neckY} L${x},${neckY + r * 0.5} L${x + r * 0.4},${neckY}`, 'none');
  if (shirt === 'stripes') for (const k of [1.3, 2.1, 2.9]) s += line(x - sh, neckY + r * k, x + sh, neckY + r * k);
  if (shirt === 'star') s += sixStar(x, neckY + r * 1.6, r * 0.45);
  // pescoço, orelhas, cabeça
  s += rect(x - r * 0.25, neckY - r * 0.25, r * 0.5, r * 0.35, 0);
  s += circle(x - r * 0.98, hy + r * 0.1, r * 0.2) + circle(x + r * 0.98, hy + r * 0.1, r * 0.2);
  s += circle(x, hy, r);
  // cabelo da frente
  const top = `M${x - r * 1.0},${hy + r * 0.05} C${x - r * 1.05},${hy - r * 1.2} ${x + r * 1.05},${hy - r * 1.2} ${x + r * 1.0},${hy + r * 0.05}`;
  if (hair === 'short') s += path(`${top} C${x + r * 0.7},${hy - r * 0.45} ${x - r * 0.2},${hy - r * 0.55} ${x - r * 1.0},${hy + r * 0.05}Z`);
  if (hair === 'long' || hair === 'ponytail' || hair === 'bun') s += path(`${top} C${x + r * 0.5},${hy - r * 0.5} ${x - r * 0.5},${hy - r * 0.5} ${x - r * 1.0},${hy + r * 0.05}Z`);
  if (hair === 'curly') s += path(blob(x, hy - r * 0.55, r * 1.08, r * 0.62, 9, 0.12, 12));
  if (hair === 'kippah') {
    s += path(`${top} C${x + r * 0.7},${hy - r * 0.45} ${x - r * 0.2},${hy - r * 0.55} ${x - r * 1.0},${hy + r * 0.05}Z`);
    s += path(`M${x - r * 0.5},${hy - r * 0.78} Q${x},${hy - r * 1.25} ${x + r * 0.5},${hy - r * 0.78} Q${x},${hy - r * 0.9} ${x - r * 0.5},${hy - r * 0.78}Z`);
  }
  // rosto
  const fx = x + face * r * 0.25;
  s += dot(fx - r * 0.34, hy + r * 0.05, r * 0.09) + dot(fx + r * 0.34, hy + r * 0.05, r * 0.09);
  s += path(`M${fx - r * 0.3},${hy + r * 0.38} Q${fx},${hy + r * (0.38 + 0.3 * smile)} ${fx + r * 0.3},${hy + r * 0.38}`, 'none');
  // braços
  const shoulders = [[x - sh * 0.9, neckY + r * 0.45], [x + sh * 0.9, neckY + r * 0.45]];
  hands.forEach(([tx, ty]) => {
    const [sx, sy] = tx < x ? shoulders[0] : shoulders[1];
    const ex = (sx + tx) / 2 + (tx < x ? -1 : 1) * r * 0.2, ey = Math.max(sy, ty) + r * 0.6;
    s += tubes([`M${sx},${sy} Q${ex},${ey} ${tx},${ty}`], r * 0.62);
    s += circle(tx, ty, r * 0.3);
  });
  return s;
}
