// Motor de desenho para line art de livro de colorir.
// Unidade: 1/100 in. Traço uniforme SW. Cada figura é desenhada em camadas; em cada
// camada, as formas se fundem numa silhueta única (contorno só por fora), e os
// detalhes (dobras, rosto) entram por cima. Camadas seguintes cobrem as anteriores.

export const SW = 3;
const r2 = (n) => Math.round(n * 100) / 100;

// Caneta: curva suave (Catmull-Rom -> Bézier) por pontos [x, y] ou [x, y, 1] (quina).
export function pen(pts, closed = true, t = 1) {
  const n = pts.length;
  if (n < 2) return '';
  const get = (i) => (closed ? pts[((i % n) + n) % n] : pts[Math.max(0, Math.min(n - 1, i))]);
  const corner = (i) => (!closed && (i <= 0 || i >= n - 1)) || get(i)[2] === 1;
  let d = `M${r2(get(0)[0])},${r2(get(0)[1])}`;
  const segs = closed ? n : n - 1;
  for (let i = 0; i < segs; i++) {
    const p0 = get(i - 1), p1 = get(i), p2 = get(i + 1), p3 = get(i + 2);
    const c1 = corner(i)
      ? [p1[0] + (p2[0] - p1[0]) / 3, p1[1] + (p2[1] - p1[1]) / 3]
      : [p1[0] + ((p2[0] - p0[0]) * t) / 6, p1[1] + ((p2[1] - p0[1]) * t) / 6];
    const c2 = corner(i + 1)
      ? [p2[0] - (p2[0] - p1[0]) / 3, p2[1] - (p2[1] - p1[1]) / 3]
      : [p2[0] - ((p3[0] - p1[0]) * t) / 6, p2[1] - ((p3[1] - p1[1]) * t) / 6];
    d += `C${r2(c1[0])},${r2(c1[1])} ${r2(c2[0])},${r2(c2[1])} ${r2(p2[0])},${r2(p2[1])}`;
  }
  return closed ? d + 'Z' : d;
}

export function ellPts(cx, cy, rx, ry, rot = 0, n = 16) {
  const a = (rot * Math.PI) / 180, out = [];
  for (let i = 0; i < n; i++) {
    const t = (i / n) * Math.PI * 2;
    const x = Math.cos(t) * rx, y = Math.sin(t) * ry;
    out.push([cx + x * Math.cos(a) - y * Math.sin(a), cy + x * Math.sin(a) + y * Math.cos(a)]);
  }
  return out;
}

// Membro afunilado entre a e b, com raios ra e rb (pontas arredondadas).
export function capPts(a, b, ra, rb, n = 5) {
  const dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy) || 1;
  const ang = Math.atan2(dy, dx);
  const out = [];
  for (let i = 0; i <= n; i++) {
    const t = ang - Math.PI / 2 + (i / n) * Math.PI;
    out.push([b[0] + Math.cos(t) * rb, b[1] + Math.sin(t) * rb]);
  }
  for (let i = 0; i <= n; i++) {
    const t = ang + Math.PI / 2 + (i / n) * Math.PI;
    out.push([a[0] + Math.cos(t) * ra, a[1] + Math.sin(t) * ra]);
  }
  return out;
}

export class Fig {
  constructor({ x = 0, y = 0, s = 1, flip = false } = {}) {
    Object.assign(this, { x, y, s, flip });
    this.layers = [];
    this.stack = [];
  }
  // Transformação local de grupo: escala/rotação em torno de (ox, oy), depois desloca.
  push({ dx = 0, dy = 0, s = 1, sx = s, sy = s, rot = 0, ox = 0, oy = 0 } = {}) {
    const a = (rot * Math.PI) / 180, c = Math.cos(a), sn = Math.sin(a);
    this.stack.push((p) => {
      const x = (p[0] - ox) * sx, y = (p[1] - oy) * sy;
      return [ox + x * c - y * sn + dx, oy + x * sn + y * c + dy, p[2]];
    });
    return this;
  }
  pop() { this.stack.pop(); return this; }
  L(i) { return (this.layers[i] ||= { fills: [], lines: [], blacks: [], whites: [], his: [] }); }
  m(p) {
    for (let i = this.stack.length - 1; i >= 0; i--) p = this.stack[i](p);
    const X = this.x + (this.flip ? -p[0] : p[0]) * this.s, Y = this.y + p[1] * this.s;
    return p[2] ? [X, Y, p[2]] : [X, Y];
  }
  M(pts) { return pts.map((p) => this.m(p)); }
  shape(i, pts, t) { this.L(i).fills.push(pen(this.M(pts), true, t)); return this; }
  white(i, pts, t) { this.L(i).whites.push(pen(this.M(pts), true, t)); return this; }
  line(i, pts, t) { this.L(i).lines.push(pen(this.M(pts), false, t)); return this; }
  loop(i, pts, t) { this.L(i).lines.push(pen(this.M(pts), true, t)); return this; }
  black(i, pts, t) { this.L(i).blacks.push(pen(this.M(pts), true, t)); return this; }
  hi(i, pts, t) { this.L(i).his.push(pen(this.M(pts), true, t)); return this; }
  ell(i, cx, cy, rx, ry, rot = 0, kind = 'shape') { return this[kind](i, ellPts(cx, cy, rx, ry, rot)); }
  cap(i, a, b, ra, rb = ra) { return this.shape(i, capPts(a, b, ra, rb)); }
  svg() {
    let o = '';
    for (let k = 0; k < this.layers.length; k++) {
      const Lr = this.layers[k];
      if (!Lr) continue;
      const P = (ds) => ds.map((d) => `<path d="${d}"/>`).join('');
      if (Lr.fills.length) {
        o += `<g fill="#000" stroke="#000" stroke-width="${2 * SW}" stroke-linejoin="round">${P(Lr.fills)}</g>`;
        o += `<g fill="#fff">${P(Lr.fills)}</g>`;
      }
      if (Lr.whites.length) o += `<g fill="#fff">${P(Lr.whites)}</g>`;
      if (Lr.lines.length) o += `<g fill="none" stroke="#000" stroke-width="${SW}" stroke-linecap="round" stroke-linejoin="round">${P(Lr.lines)}</g>`;
      if (Lr.blacks.length) o += `<g fill="#000">${P(Lr.blacks)}</g>`;
      if (Lr.his.length) o += `<g fill="#fff">${P(Lr.his)}</g>`;
    }
    return o;
  }
}

// Arco recortado em "nuvem" (cabelo cacheado, copa de árvore, nuvem).
// Ângulos em graus no sistema do SVG (0 = direita, -90 = cima). n calombos.
export function scallopPts(cx, cy, r, a0, a1, n, amp, ry = r) {
  const out = [];
  const R = (k, rr) => {
    const t = ((a0 + (a1 - a0) * k) * Math.PI) / 180;
    return [cx + Math.cos(t) * rr, cy + Math.sin(t) * rr * (ry / r)];
  };
  for (let i = 0; i < n; i++) {
    const k0 = i / n, k1 = (i + 1) / n, km = (k0 + k1) / 2;
    out.push([...R(k0, r), 1]);
    out.push(R(k0 + (k1 - k0) * 0.2, r + amp * 0.75));
    out.push(R(km, r + amp));
    out.push(R(k0 + (k1 - k0) * 0.8, r + amp * 0.75));
  }
  out.push([...R(1, r), 1]);
  return out;
}
