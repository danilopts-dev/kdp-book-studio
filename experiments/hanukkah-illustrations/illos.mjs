// Ilustrações do "8 Nights of Hanukkah Activity Book", numeração de
// lista-ilustracoes-livro-completo.md. Cada item: id, w/h em polegadas, svg interno
// em unidades de 1/100 in.
import * as L from './lib.mjs';
const { path, line, rect, circle, ellipse, poly, pline, g, text, hollowText, dashed } = L;

const NUN = 'נ', GIMEL = 'ג', HEI = 'ה', SHIN = 'ש';
const ALL = [true, true, true, true, true, true, true, true];
const NONE = [false, false, false, false, false, false, false, false];

// ---------- Templo para o jogo dos erros ----------
// messy=true: versão "antes". hard=true: 10 diferenças (senão 5).
// Tudo o que não é diferença é desenhado igual nas duas versões.
function temple(messy, hard) {
  const W = 740, H = 280, floor = 232;
  let s = rect(0, 0, W, H, 14);
  // parede do fundo: pedras (idênticas nas duas versões)
  s += line(0, floor, W, floor);
  for (const [y, xs] of [[70, [150, 450]], [120, [110, 520]], [175, [160, 430, 590]]]) {
    for (const x of xs) s += line(x, y, x + 36, y, 'stroke-opacity="1"');
  }
  // chão: linhas de perspectiva
  for (const x of [120, 300, 460, 620]) s += line(x, floor, x + (x - 370) * 0.18, H - 4);
  // colunas
  const column = (x, cracked) => {
    let c = rect(x, 34, 50, floor - 44, 2);
    c += rect(x - 8, 20, 66, 16, 3) + rect(x - 8, floor - 12, 66, 12, 3);
    for (const dx of [14, 25, 36]) c += line(x + dx, 44, x + dx, floor - 20);
    if (cracked) c += pline([[x + 4, 90], [x + 18, 104], [x + 10, 118], [x + 30, 134], [x + 22, 148], [x + 46, 160]]);
    return c;
  };
  s += column(20, false);
  s += column(670, hard && messy);
  // cortina (dif. 4)
  const cx0 = 92, cx1 = 192, ctop = 34, cbot = 158;
  s += line(cx0 - 8, ctop, cx1 + 8, ctop) + L.circle(cx0 - 8, ctop, 5) + L.circle(cx1 + 8, ctop, 5);
  if (messy) {
    s += path(`M${cx0},${ctop} L${cx1},${ctop} L${cx1},${cbot - 30} L${cx1 - 16},${cbot} L${cx1 - 30},${cbot - 24} L${cx1 - 46},${cbot + 4} L${cx1 - 58},${cbot - 40} L${cx1 - 74},${cbot - 6} L${cx0 + 10},${cbot - 18} L${cx0},${cbot}Z`);
  } else {
    s += rect(cx0, ctop, cx1 - cx0, cbot - ctop, 0);
  }
  for (const x of [117, 142, 167]) s += line(x, ctop + 6, x, messy ? cbot - 50 : cbot - 8);
  // janela em arco (base); no difícil, veneziana (dif. 10)
  const wx = 222, ww = 80, wy = 48, wh = 96;
  s += path(`M${wx},${wy + wh} L${wx},${wy + ww / 2} A${ww / 2},${ww / 2} 0 0 1 ${wx + ww},${wy + ww / 2} L${wx + ww},${wy + wh}Z`);
  s += line(wx + ww / 2, wy, wx + ww / 2, wy + wh) + line(wx, wy + 60, wx + ww, wy + 60);
  s += rect(wx - 8, wy + wh, ww + 16, 10, 2);
  if (hard) {
    s += rect(wx - 34, wy + 26, 28, 70, 2) + line(wx - 20, wy + 32, wx - 20, wy + 90);
    if (messy) {
      s += g(rect(0, 0, 28, 70, 2) + line(14, 6, 14, 30) + pline([[4, 30], [12, 38], [8, 48], [22, 56]]), `translate(${wx + ww + 10} ${wy + 26}) rotate(22)`);
    } else {
      s += rect(wx + ww + 6, wy + 26, 28, 70, 2) + line(wx + ww + 20, wy + 32, wx + ww + 20, wy + 90);
    }
  }
  // vassoura encostada (base, igual nas duas)
  s += line(648, 96, 626, floor - 26);
  s += path(`M616,${floor - 30} L636,${floor - 22} L630,${floor} L600,${floor}Z`);
  // teia (dif. 2)
  if (messy) {
    const ox = 670, oy = 36;
    for (const a of [100, 125, 150, 175]) {
      const r = (a * Math.PI) / 180;
      s += line(ox, oy, ox + Math.cos(r) * 60, oy + Math.sin(r) * 60);
    }
    for (const rr of [18, 34, 50]) {
      const pts = [100, 125, 150, 175].map((a) => [ox + Math.cos((a * Math.PI) / 180) * rr, oy + Math.sin((a * Math.PI) / 180) * rr]);
      s += pline(pts);
    }
  }
  // estandarte/pergaminho (dif. 7, só difícil)
  if (hard) {
    if (messy) {
      s += rect(318, floor - 16, 70, 16, 8) + ellipse(318, floor - 8, 6, 8) + ellipse(388, floor - 8, 6, 8);
    } else {
      s += line(330, 40, 376, 40) + L.circle(353, 34, 5);
      s += path(`M334,40 L372,40 L372,122 L353,110 L334,122Z`);
      s += L.sixStar(353, 72, 14);
    }
  }
  // candelabro de uma vela (dif. 9, só difícil)
  if (hard) {
    const stand = rect(-4, 0, 8, 100, 2) + ellipse(0, 100, 20, 6) + ellipse(0, 0, 16, 5) + rect(-6, -26, 12, 26, 2);
    s += messy ? g(stand, `translate(398 ${floor - 22}) rotate(-90)`) : g(stand, `translate(416 ${floor - 106})`);
  }
  // mesa (dif. 3)
  if (messy) {
    s += g(rect(0, 0, 110, 14, 3) + rect(14, 14, 12, 58, 2) + rect(84, 14, 12, 58, 2), `translate(${512} ${floor}) rotate(-90)`);
  } else {
    s += rect(470, 166, 120, 14, 3) + rect(484, 180, 12, floor - 180, 2) + rect(564, 180, 12, floor - 180, 2);
  }
  // banco (dif. 8, só difícil)
  if (hard) {
    if (messy) {
      s += g(rect(0, 0, 90, 12, 3) + rect(8, 12, 10, 26, 2) + rect(72, 12, 10, 10, 2), `translate(96 ${floor - 38}) rotate(-8 45 6)`);
      s += g(rect(0, 0, 10, 24, 2), `translate(160 ${floor - 10}) rotate(80)`);
    } else {
      s += rect(96, floor - 38, 90, 12, 3) + rect(104, floor - 26, 10, 26, 2) + rect(168, floor - 26, 10, 26, 2);
    }
  }
  // jarro (dif. 1)
  if (messy) {
    s += g(L.oilJar(0, 0, 56, false), `translate(246 ${floor - 4}) rotate(78)`);
    s += poly([[276, floor], [290, floor - 12], [298, floor]]) + poly([[300, floor], [306, floor - 8], [314, floor]]);
  } else {
    s += L.oilJar(262, floor, 56, false);
  }
  // monte de poeira (dif. 5)
  if (messy) {
    s += path(`M536,${floor} C546,${floor - 26} 584,${floor - 30} 596,${floor}Z`);
    for (const [x, y] of [[552, floor - 10], [566, floor - 16], [580, floor - 8], [528, floor - 4]]) s += L.dot(x, y, 2.6);
  }
  return s;
}

function spotTheDifference(hard) {
  const top = g(temple(true, hard), 'translate(0 0)');
  const bot = g(temple(false, hard), 'translate(0 320)');
  return top + bot;
}

// ---------- Casa vista de fora à noite ----------
function houseScene() {
  const W = 740, H = 260, gy = 214;
  let s = '';
  s += path(`M218,52 A26,26 0 1 0 250,20 A21,21 0 1 1 218,52Z`);
  for (const [x, y, r] of [[40, 30, 6], [130, 20, 5], [300, 18, 5], [520, 30, 7], [640, 16, 5], [700, 52, 6], [420, 14, 5]]) s += L.sparkle(x, y, r * 1.6);
  s += line(0, gy, W, gy) + line(0, gy + 18, W, gy + 18);
  for (let x = 20; x < W; x += 80) s += line(x, gy + 18, x - 12, H - 6);
  const house = (x, w, h, roofH, windows, door) => {
    let o = poly([[x - 10, gy - h], [x + w / 2, gy - h - roofH], [x + w + 10, gy - h]]);
    o += rect(x, gy - h, w, h, 0);
    for (const [wx, wy, ww, wh] of windows) o += rect(x + wx, gy - h + wy, ww, wh, 2) + line(x + wx + ww / 2, gy - h + wy, x + wx + ww / 2, gy - h + wy + wh) + line(x + wx, gy - h + wy + wh / 2, x + wx + ww, gy - h + wy + wh / 2);
    if (door) o += rect(x + door, gy - 64, 38, 64, 3) + L.dot(x + door + 30, gy - 32);
    return o;
  };
  s += house(26, 170, 110, 56, [[18, 24, 44, 36], [106, 24, 44, 36]], 66);
  s += house(544, 170, 104, 52, [[20, 22, 42, 36], [108, 22, 42, 36]], 66);
  // casa do centro com janela grande e hanukiá voltada para a rua
  const cx = 252, cw = 236, ch = 140;
  s += poly([[cx - 12, gy - ch], [cx + cw / 2, gy - ch - 60], [cx + cw + 12, gy - ch]]);
  s += rect(cx, gy - ch, cw, ch, 0);
  s += rect(cx + 20, gy - 66, 40, 66, 3) + L.dot(cx + 52, gy - 33);
  const wx = cx + 78, wy = gy - ch + 22, ww = 140, wh = 92;
  s += rect(wx, wy, ww, wh, 3);
  s += path(`M${wx + 4},${wy + 4} Q${wx + 22},${wy + 40} ${wx + 10},${wy + wh - 4} L${wx + 4},${wy + wh - 4}Z`);
  s += path(`M${wx + ww - 4},${wy + 4} Q${wx + ww - 22},${wy + 40} ${wx + ww - 10},${wy + wh - 4} L${wx + ww - 4},${wy + wh - 4}Z`);
  s += L.hanukkiah({ cx: wx + ww / 2, baseY: wy + wh - 6, W: 104, candles: ALL, lit: ALL, shamashLit: true }).svg;
  s += rect(wx - 8, wy + wh, ww + 16, 8, 2);
  // poste de luz
  s += rect(228, gy - 120, 8, 120, 2) + path(`M218,${gy - 120} L246,${gy - 120} L240,${gy - 140} L224,${gy - 140}Z`);
  s += rect(518, gy - 36, 6, 36, 1) + rect(506, gy - 50, 30, 16, 3);
  return s;
}

// ---------- Mini-guia de acendimento (FM.1) ----------
// Terceira noite: velas nos 3 suportes da direita. Colocação da direita para a
// esquerda; acendimento da esquerda para a direita, começando pela mais nova.
function lightingGuide() {
  const cx = 450, baseY = 580, W = 470;
  const cand = [false, false, false, false, false, true, true, true];
  const h = L.hanukkiah({ cx, baseY, W, candles: cand, lit: NONE, shamashLit: true });
  let s = h.svg;
  const num = (x, y, n) => circle(x, y, 17) + text(x, y + 7, n, 20);
  // passo 1
  const y1 = 110;
  s += text(20, 60, 'STEP 1: PUT THE CANDLES IN', 22, 'start');
  s += text(20, 88, 'One more each night, from RIGHT to LEFT.', 17, 'start', 'normal');
  s += text(20, 112, 'Tonight is night 3.', 17, 'start', 'normal');
  [7, 6, 5].forEach((i, k) => { s += num(h.xs[i], y1, String(k + 1)); });
  s += L.arrow(h.xs[7] + 6, y1 + 34, h.xs[5] - 16, y1 + 34, 14);
  // passo 2
  const y2 = 230;
  s += text(20, 192, 'STEP 2: LIGHT THEM', 22, 'start');
  s += text(20, 220, 'Use the shamash. Start with the', 17, 'start', 'normal');
  s += text(20, 244, 'newest candle, then go LEFT to RIGHT.', 17, 'start', 'normal');
  [5, 6, 7].forEach((i, k) => { s += num(h.xs[i], y2, String(k + 1)); });
  s += L.arrow(h.xs[5] - 16, y2 + 34, h.xs[7] + 6, y2 + 34, 14);
  for (const i of [5, 6, 7]) s += line(h.xs[i], y2 + 50, h.xs[i], h.candleTop - 14, dashed);
  // shamash
  s += line(h.shX - 16, h.shTop + 44, h.shX - 44, h.shTop + 34);
  s += text(h.shX - 50, h.shTop + 36, 'SHAMASH', 18, 'end');
  s += text(h.shX - 50, h.shTop + 58, '(the helper candle)', 15, 'end', 'normal');
  return s;
}

// ---------- Planificação do dreidel (5.3) ----------
// 4 faces com as letras, tampa com abas, 4 triângulos da ponta com abas.
function dreidelNet() {
  const a = 116, x0 = 64, y0 = 200;
  const letters = [NUN, GIMEL, HEI, SHIN];
  let s = '';
  const tab = (p1, p2, depth = 20, away = [x0 + 2 * a, y0 + a / 2]) => {
    // aba trapezoidal no segmento p1->p2, apontando para longe de `away`
    const dx = p2[0] - p1[0], dy = p2[1] - p1[1], len = Math.hypot(dx, dy);
    let nx = dy / len, ny = -dx / len;
    const mx = (p1[0] + p2[0]) / 2 - away[0], my = (p1[1] + p2[1]) / 2 - away[1];
    if (nx * mx + ny * my < 0) { nx = -nx; ny = -ny; }
    const ux = dx / len, uy = dy / len;
    const q1 = [p1[0] + nx * depth + ux * depth * 0.8, p1[1] + ny * depth + uy * depth * 0.8];
    const q2 = [p2[0] + nx * depth - ux * depth * 0.8, p2[1] + ny * depth - uy * depth * 0.8];
    return poly([p1, q1, q2, p2]);
  };
  // abas primeiro (ficam atrás)
  const tip = (i) => [x0 + i * a + a / 2, y0 + a + a * 0.9];
  for (let i = 0; i < 4; i++) s += tab([x0 + (i + 1) * a, y0 + a], tip(i), 18, [x0 + i * a + a / 2, y0 + a + 30]);
  s += tab([x0 + 4 * a, y0 + a], [x0 + 4 * a, y0], 26);
  s += tab([x0, y0 - a], [x0, y0], 22, [x0 + a / 2, y0 - a / 2]);
  s += tab([x0 + a, y0], [x0 + a, y0 - a], 22, [x0 + a / 2, y0 - a / 2]);
  s += tab([x0 + a, y0 - a], [x0, y0 - a], 22, [x0 + a / 2, y0 - a / 2]);
  for (let i = 0; i < 4; i++) {
    const x = x0 + i * a;
    s += rect(x, y0, a, a, 0);
    s += hollowText(x + a / 2, y0 + a / 2 + 32, letters[i], 90);
    s += poly([[x, y0 + a], [x + a, y0 + a], tip(i)]);
  }
  s += rect(x0, y0 - a, a, a, 0);
  s += circle(x0 + a / 2, y0 - a / 2, 11);
  s += text(x0 + a + 40, y0 - a / 2 - 8, 'Poke a pencil through', 15, 'start', 'normal');
  s += text(x0 + a + 40, y0 - a / 2 + 14, 'this circle for the handle.', 15, 'start', 'normal');
  // dobras tracejadas por cima
  for (let i = 1; i < 4; i++) s += line(x0 + i * a, y0, x0 + i * a, y0 + a, dashed);
  s += line(x0, y0 + a, x0 + 4 * a, y0 + a, dashed) + line(x0, y0, x0 + a, y0, dashed);
  // legenda
  s += line(64, 560, 130, 560) + text(140, 566, 'cut', 17, 'start', 'normal');
  s += line(230, 560, 296, 560, dashed) + text(306, 566, 'fold', 17, 'start', 'normal');
  s += rect(390, 548, 34, 24, 3) + text(434, 566, 'glue tab', 17, 'start', 'normal');
  return s;
}

// ---------- Cupons (7.4) ----------
function coupons() {
  const icons = [
    (x, y) => L.heart(x, y + 4, 44),
    (x, y) => line(x + 16, y - 26, x - 6, y + 10) + path(`M${x - 18},${y + 4} L${x + 4},${y + 16} L${x - 4},${y + 30} L${x - 30},${y + 18}Z`) + line(x - 22, y + 14, x - 12, y + 28),
    (x, y) => path(`M${x},${y - 14} Q${x - 18},${y - 24} ${x - 34},${y - 18} L${x - 34},${y + 20} Q${x - 18},${y + 14} ${x},${y + 24} Q${x + 18},${y + 14} ${x + 34},${y + 20} L${x + 34},${y - 18} Q${x + 18},${y - 24} ${x},${y - 14}Z`) + line(x, y - 14, x, y + 24),
    (x, y) => circle(x, y, 28) + circle(x, y, 18) + line(x - 38, y - 18, x - 38, y + 22) + line(x + 38, y - 18, x + 38, y + 22),
    (x, y) => L.dreidel(x, y - 10, 34, [SHIN, NUN]),
    (x, y) => L.sparkle(x, y, 30),
  ];
  let s = '';
  const cw = 350, chh = 180;
  for (let i = 0; i < 6; i++) {
    const x = 10 + (i % 2) * (cw + 20), y = 10 + Math.floor(i / 2) * (chh + 20);
    s += rect(x, y, cw, chh, 10, 'none', dashed);
    s += circle(x + 62, y + chh / 2, 46) + icons[i](x + 62, y + chh / 2);
    s += text(x + 124, y + 42, 'THIS COUPON IS GOOD FOR:', 13, 'start');
    s += line(x + 124, y + 82, x + cw - 18, y + 82) + line(x + 124, y + 116, x + cw - 18, y + 116);
    s += text(x + 124, y + 156, 'FROM:', 13, 'start') + line(x + 176, y + 158, x + cw - 18, y + 158);
  }
  return s;
}

// ---------- Moldura do labirinto (7.3) ----------
function mazeFrame() {
  let s = L.frameBorder(550, 550, 6, 10);
  s += rect(80, 80, 390, 390, 4, 'none', dashed);
  s += L.coin(56, 56, 34) + text(140, 58, 'START', 16);
  s += L.tzedakahBox(488, 530, 60) + text(400, 506, 'FINISH', 16);
  for (const [x, y] of [[275, 30], [520, 275], [30, 275], [275, 522]]) s += L.sixStar(x, y, 12);
  return s;
}

// ---------- Certificado (8.3) ----------
function certificate() {
  let s = L.frameBorder(740, 900, 14, 12);
  s += '<rect x="262" y="0" width="216" height="150" fill="#fff"/>';
  s += L.hanukkiah({ cx: 370, baseY: 130, W: 180, candles: ALL, lit: ALL, shamashLit: true }).svg;
  for (const [x, y] of [[62, 62], [678, 62], [62, 838], [678, 838]]) s += circle(x, y, 30) + L.sixStar(x, y, 18);
  for (let y = 150; y <= 760; y += 76) s += L.sparkle(44, y, 11) + L.sparkle(696, y, 11);
  return s;
}

// ---------- Página grande para colorir (8.1) ----------
function allEightLights() {
  let s = L.frameBorder(740, 900, 10, 12);
  s += L.hanukkiah({ cx: 370, baseY: 700, W: 600, candles: ALL, lit: ALL, shamashLit: true }).svg;
  s += L.dreidel(150, 740, 70, [GIMEL, HEI]) + L.dreidel(600, 740, 70, [SHIN, NUN]);
  for (const [x, y, r] of [[300, 800, 26], [360, 818, 26], [420, 800, 26], [470, 826, 22], [250, 826, 22]]) s += L.coin(x, y, r);
  for (const [x, y, r] of [[110, 120, 18], [630, 110, 20], [200, 200, 12], [540, 190, 12], [370, 70, 14], [90, 420, 12], [650, 420, 12]]) s += L.sparkle(x, y, r);
  return s;
}

// ---------- Travessa latkes x sufganiyot (6.2) ----------
function platter() {
  let s = ellipse(250, 150, 238, 92) + ellipse(250, 150, 212, 74);
  s += line(250, 80, 250, 222, dashed);
  [[140, 186, 70, 11], [132, 160, 66, 12], [146, 134, 62, 13], [138, 110, 56, 14]].forEach(([x, y, r, sd]) => { s += L.latke(x, y, r, sd); });
  [[310, 176, 36, 21], [380, 180, 36, 22], [345, 132, 36, 23], [412, 140, 30, 24]].forEach(([x, y, r, sd]) => { s += L.sufganiyah(x, y, r, sd); });
  return s;
}

// ---------- Menorá x hanukiá (2.4) ----------
function compare() {
  let s = '';
  s += rect(50, 8, 260, 40, 10, 'none') + rect(430, 8, 260, 40, 10, 'none');
  s += L.menorah7({ cx: 180, baseY: 292, W: 290 });
  s += L.hanukkiah({ cx: 560, baseY: 292, W: 320, candles: ALL, lit: NONE }).svg;
  s += line(370, 30, 370, 280, dashed);
  return s;
}


// ---------- Teste figurativo: família acendendo na janela (1.4) ----------
function familyWindow() {
  const W = 740, H = 220;
  let s = '';
  // janela ao fundo com céu noturno
  const wx = 230, wy = 8, ww = 280, wh = 150;
  s += rect(wx, wy, ww, wh, 4);
  s += line(wx + ww / 2, wy, wx + ww / 2, wy + wh * 0.55);
  s += path(`M${wx + 40},${wy + 44} A18,18 0 1 0 ${wx + 64},${wy + 18} A14,14 0 1 1 ${wx + 40},${wy + 44}Z`);
  for (const [x, y] of [[wx + 110, 26], [wx + 200, 40], [wx + 240, 20], [wx + 160, 60]]) s += L.sparkle(x, y, 8);
  // cortinas
  s += path(`M${wx - 30},0 L${wx + 10},0 Q${wx + 24},${wh * 0.6} ${wx + 4},${wh + 8} L${wx - 30},${wh + 8}Z`);
  s += path(`M${wx + ww + 30},0 L${wx + ww - 10},0 Q${wx + ww - 24},${wh * 0.6} ${wx + ww - 4},${wh + 8} L${wx + ww + 30},${wh + 8}Z`);
  // parapeito + hanukiá (1ª noite: 1 vela à direita; shamash na mão do pai)
  s += rect(wx - 40, wy + wh, ww + 80, 12, 3);
  const h = L.hanukkiah({ cx: wx + ww / 2 + 10, baseY: wy + wh, W: 170, candles: [0, 0, 0, 0, 0, 0, 0, 1], lit: NONE, shamashCandle: false });
  s += h.svg;
  // pessoas
  const tx = h.xs[7], ty = h.candleTop - 8;
  s += L.person({ x: 150, neckY: 92, r: 26, hair: 'kippah', hands: [[tx - 26, ty + 14]], face: 0.6 });
  s += L.candle(tx - 22, ty + 6, 6, 30, true);
  s += L.person({ x: 600, neckY: 94, r: 25, hair: 'long', hands: [[548, 150]], face: -0.4 });
  s += L.person({ x: 250, neckY: 150, r: 21, hair: 'curly', shirt: 'stripes', face: 0.5 });
  s += L.person({ x: 480, neckY: 146, r: 22, hair: 'ponytail', shirt: 'star', face: -0.5 });
  // mesa em primeiro plano esconde a cintura
  s += rect(-10, 196, W + 20, 40, 0);
  return s;
}

export const ILLOS = [
  { id: '1-4', title: 'TESTE figurativo: família', w: 7.4, h: 2.2, svg: familyWindow },
  { id: '1-2', title: 'Hanukiá simples', w: 3.0, h: 2.1, svg: () => L.hanukkiah({ cx: 150, baseY: 200, W: 270, candles: ALL, lit: NONE }).svg },
  { id: '2-2', title: 'Jogo dos 5 erros', w: 7.4, h: 6.0, svg: () => spotTheDifference(false) },
  { id: '2-3', title: 'Jogo dos 10 erros', w: 7.4, h: 6.0, svg: () => spotTheDifference(true) },
  { id: '2-4', title: 'Menorá x hanukiá', w: 7.4, h: 3.0, svg: compare },
  { id: '3-1', title: 'Jarro de óleo (objeto)', w: 3.0, h: 3.0, svg: () => L.oilJar(150, 270, 240) + [[40, 40], [260, 60], [60, 250], [250, 240]].map(([x, y]) => L.sparkle(x, y, 14)).join('') },
  { id: '3-3', title: 'Hanukiá, primeira noite', w: 3.0, h: 3.0, svg: () => L.hanukkiah({ cx: 150, baseY: 270, W: 270, candles: [0, 0, 0, 0, 0, 0, 0, 1], lit: [0, 0, 0, 0, 0, 0, 0, 1], shamashLit: true }).svg },
  { id: '4-1', title: 'Hanukiá na janela (rua)', w: 7.4, h: 2.6, svg: houseScene },
  { id: '4-3', title: 'Hanukiá para desenhar', w: 7.4, h: 8.0, svg: () => L.hanukkiah({ cx: 370, baseY: 700, W: 640, candles: NONE, lit: NONE, shamashCandle: false }).svg },
  { id: '5-2', title: 'Dreidel grande', w: 4.0, h: 4.0, svg: () => L.dreidel(200, 110, 180, [NUN, GIMEL]) },
  { id: '5-3', title: 'Dreidel para montar', w: 6.0, h: 6.0, svg: dreidelNet },
  { id: '6-2', title: 'Latkes x sufganiyot', w: 5.0, h: 2.5, svg: platter },
  { id: '7-3', title: 'Moldura do labirinto', w: 5.5, h: 5.5, svg: mazeFrame },
  { id: '7-4', title: 'Cupons', w: 7.4, h: 6.0, svg: coupons },
  { id: '8-1', title: 'Todas as luzes (colorir)', w: 7.4, h: 9.0, svg: allEightLights },
  { id: '8-3', title: 'Certificado', w: 7.4, h: 9.0, svg: certificate },
  { id: 'FM-1', title: 'Mini-guia de acendimento', w: 7.4, h: 6.0, svg: lightingGuide },
];
