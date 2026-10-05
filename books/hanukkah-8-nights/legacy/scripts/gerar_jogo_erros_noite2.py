#!/usr/bin/env python3
"""Jogo dos erros da Noite 2 (Templo bagunçado, antes e depois), gerado por código.

Entrada : inputs/illustrations/22.png  (1969x799, line art P&B, 10 objetos isolados)
Saídas  : inputs/puzzle-assets/
            noite2_erros5_antes.png   / noite2_erros5_depois.png    (★: objetos 1 a 5 apagados)
            noite2_erros10_antes.png  / noite2_erros10_depois.png   (★★: objetos 1 a 10 apagados)
            noite2_erros_gabarito.json
            noite2_erros5_gabarito.png / noite2_erros10_gabarito.png (depois + retângulos tracejados pretos)

Como apaga: cada objeto tem uma máscara calculada a partir dos próprios traços (nunca um retângulo
cego): componentes conectados (jarro, poeira, banco, vela, balde), região fechada por preenchimento
(mesa, cortina, tambor, estandarte) ou polígono (teia, que encosta na coluna). A máscara é pintada de
branco exato (255). Onde o objeto escondia a linha do chão ou o tijolo da parede, a linha é refeita
("ponte" horizontal entre as pontas que sobraram). Objetos que NÃO são apagados numa versão têm os
traços protegidos (mesa e vela se encostam, por exemplo).

Verificações no fim (o script aborta se falhar):
  - cada diferença do gabarito realmente difere (pixels diferentes dentro da caixa);
  - fora da união das caixas apagadas as imagens são idênticas (diff = 0);
  - objetos mantidos ficam idênticos aos do "antes".
Só usa numpy + PIL (scipy/opencv são bloqueados neste Windows pela política de apps).
"""
import json
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "inputs" / "illustrations" / "22.png"
OUT = ROOT / "inputs" / "puzzle-assets"

DARK = 160  # abaixo disto = traço

# id, nome (para o gabarito), tipo de máscara, caixa de busca (x0, y0, x1, y1), ponte horizontal?
OBJECTS = [
    (1, "broken clay jar", "comp", (42, 494, 324, 711), False),
    (2, "cobweb in the upper right corner", "web", (1655, 0, 1832, 172), False),
    (3, "wooden table lying on its side", "flood", (432, 374, 808, 670), True),
    (4, "torn curtain on the wall", "flood", (280, 12, 652, 422), True),
    (5, "pile of dust on the floor", "comp", (826, 572, 1096, 692), False),
    (6, "fallen stone column drum", "flood", (1080, 404, 1466, 616), True),
    (7, "torn banner hanging crooked", "flood", (1320, 12, 1614, 416), True),
    (8, "wooden bench with a broken leg", "comp", (1553, 472, 1943, 692), False),
    (9, "candle stand knocked over", "comp", (447, 634, 723, 784), False),
    (10, "tipped-over wooden bucket", "comp", (1265, 610, 1521, 781), False),
]
STAR1 = [1, 2, 3, 4, 5]
STAR2 = list(range(1, 11))


def dilate(mask, r):
    """Dilatação por MaxFilter do PIL (mask booleana)."""
    if r <= 0:
        return mask.copy()
    im = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2 * r + 1))
    return np.asarray(im) > 0


def label_components(dark):
    """Rotula componentes 8-conectados. Retorna (labels, {id: (x0,y0,x1,y1)})."""
    h, w = dark.shape
    lab = np.zeros((h, w), np.int32)
    boxes = {}
    n = 0
    for y, x in zip(*np.nonzero(dark)):
        if lab[y, x]:
            continue
        n += 1
        q = deque([(y, x)])
        lab[y, x] = n
        x0 = x1 = x
        y0 = y1 = y
        while q:
            cy, cx = q.popleft()
            x0, x1, y0, y1 = min(x0, cx), max(x1, cx), min(y0, cy), max(y1, cy)
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < h and 0 <= nx < w and dark[ny, nx] and not lab[ny, nx]:
                        lab[ny, nx] = n
                        q.append((ny, nx))
        boxes[n] = (x0, y0, x1, y1)
    return lab, boxes


class Scene:
    def __init__(self):
        raw = np.asarray(Image.open(SRC).convert("L")).copy()
        # limpeza de fundo (vale para o "antes" e o "depois"): o PNG de origem tem ruído JPEG de
        # 229-254 no fundo; tudo >= 235 vira branco exato para que o apagado não deixe "fantasmas".
        raw[raw >= 235] = 255
        self.img = raw
        self.h, self.w = self.img.shape
        self.dark = self.img < DARK
        self.lab, self.cbox = label_components(self.dark)
        self.masks = {}
        for oid, name, kind, box, bridge in OBJECTS:
            self.masks[oid] = self._mask(kind, box)

    # -------------------------------------------------------------- máscaras
    def _box_mask(self, box):
        m = np.zeros((self.h, self.w), bool)
        x0, y0, x1, y1 = box
        m[y0:y1, x0:x1] = True
        return m

    def _mask(self, kind, box):
        x0, y0, x1, y1 = box
        if kind == "comp":
            m = np.zeros((self.h, self.w), bool)
            for cid, (cx0, cy0, cx1, cy1) in self.cbox.items():
                if cx0 >= x0 and cy0 >= y0 and cx1 < x1 and cy1 < y1:
                    m |= self.lab == cid
            return dilate(m, 4)
        if kind == "web":
            return self._web(box)
        return self._flood(box)

    def _flood(self, box):
        """Traços de um objeto fechado: regiões brancas inacessíveis desde a borda da caixa
        (interior) + traços escuros a até 7 px delas (contorno). Traços de componentes de
        outros objetos (vela sob a mesa, pontas da cortina sobre a mesa) ficam de fora."""
        x0, y0, x1, y1 = box
        sub = self.dark[y0:y1, x0:x1].copy()
        # componentes inteiramente de outro objeto, dentro desta caixa, não contam
        for oid, name, kind, b in [(o[0], o[1], o[2], o[3]) for o in OBJECTS]:
            if kind == "comp" and self._overlap(b, box):
                for cid, (cx0, cy0, cx1, cy1) in self.cbox.items():
                    if cx0 >= b[0] and cy0 >= b[1] and cx1 < b[2] and cy1 < b[3]:
                        sub &= ~(self.lab[y0:y1, x0:x1] == cid)
        # pontas da cortina que invadem a caixa da mesa e vice-versa: componente "cortina" fica fora
        h, w = sub.shape
        reach = np.zeros((h, w), bool)
        q = deque()
        for x in range(w):
            for y in (0, h - 1):
                if not sub[y, x] and not reach[y, x]:
                    reach[y, x] = True
                    q.append((y, x))
        for y in range(h):
            for x in (0, w - 1):
                if not sub[y, x] and not reach[y, x]:
                    reach[y, x] = True
                    q.append((y, x))
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and not sub[ny, nx] and not reach[ny, nx]:
                    reach[ny, nx] = True
                    q.append((ny, nx))
        interior = ~sub & ~reach
        # descarta interiores minúsculos (ruído) e os que não têm contorno próprio
        full = np.zeros((self.h, self.w), bool)
        near = dilate(np.pad(interior, ((y0, self.h - y1), (x0, self.w - x1))), 7)
        full = (near & self.dark) | np.pad(interior, ((y0, self.h - y1), (x0, self.w - x1)))
        # só dentro da caixa e fora dos componentes de outros objetos
        boxm = self._box_mask(box)
        full &= boxm
        for oid, name, kind, b, br in OBJECTS:
            if kind == "comp" and self._overlap(b, box):
                for cid, (cx0, cy0, cx1, cy1) in self.cbox.items():
                    if cx0 >= b[0] and cy0 >= b[1] and cx1 < b[2] and cy1 < b[3]:
                        full &= ~(self.lab == cid)
        return dilate(full, 3) & boxm & ~self._others_comp(box)

    def _others_comp(self, box):
        m = np.zeros((self.h, self.w), bool)
        for oid, name, kind, b, br in OBJECTS:
            if kind == "comp" and self._overlap(b, box):
                for cid, (cx0, cy0, cx1, cy1) in self.cbox.items():
                    if cx0 >= b[0] and cy0 >= b[1] and cx1 < b[2] and cy1 < b[3]:
                        m |= dilate(self.lab == cid, 2)
        return m

    @staticmethod
    def _overlap(a, b):
        return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])

    def _web(self, box):
        """Teia: traços à esquerda da borda da coluna (a coluna fica intacta)."""
        x0, y0, x1, y1 = box
        ys = np.arange(self.h)[:, None]
        xs = np.arange(self.w)[None, :]
        edge = np.where(ys < 29, 1789,
               np.where(ys < 53, 1806 + (ys - 29) * 13 / 24,
               np.where(ys < 73, 1816, 1822)))
        left = (xs < edge) & self._box_mask(box)
        m = dilate((self.img < 215) & left, 2) & left
        return m

    # -------------------------------------------------------------- composição
    def render(self, erase_ids):
        img = self.img.copy()
        erase = np.zeros((self.h, self.w), bool)
        protect = np.zeros((self.h, self.w), bool)
        for oid, name, kind, box, bridge in OBJECTS:
            if oid in erase_ids:
                erase |= self.masks[oid]
            else:
                protect |= dilate(self.masks[oid] & self.dark, 5)
                # mesmo sem estar apagado, o objeto mantém os próprios traços
        # sobras: peças de traço isoladas dentro da caixa de um objeto apagado (pontas da cortina etc.)
        for oid, name, kind, box, bridge in OBJECTS:
            if oid not in erase_ids:
                continue
            x0, y0, x1, y1 = box
            left = self.dark[y0:y1, x0:x1] & ~erase[y0:y1, x0:x1] & ~protect[y0:y1, x0:x1]
            lab, boxes = label_components(left)
            h, w = left.shape
            for cid, (a, b, c, d) in boxes.items():
                area = int((lab == cid).sum())
                if a > 0 and b > 0 and c < w - 1 and d < h - 1 and area < 600:
                    piece = np.zeros((self.h, self.w), bool)
                    piece[y0:y1, x0:x1] = lab == cid
                    erase |= dilate(piece, 4)
        # halo/ruído claro (160-234) em volta do que foi apagado também sai
        light = (self.img < 235) & ~self.dark
        erase |= light & dilate(erase, 10)
        # manchinhas claras soltas dentro da caixa (longe de qualquer traço que fica)
        keep_dark = dilate(self.dark & ~erase, 4)
        for oid, name, kind, box, bridge in OBJECTS:
            if oid in erase_ids:
                x0, y0, x1, y1 = box
                erase[y0:y1, x0:x1] |= (light & ~keep_dark)[y0:y1, x0:x1]
        erase &= ~protect
        img[erase] = 255
        # pontes horizontais (linha do chão / tijolos escondidos pelo objeto)
        for oid, name, kind, box, bridge in OBJECTS:
            if oid not in erase_ids or not bridge:
                continue
            x0, y0, x1, y1 = box
            for y in range(y0, y1):
                row = erase[y]
                x = x0
                while x < x1:
                    if row[x]:
                        a = x
                        while x < x1 and row[x]:
                            x += 1
                        b = x - 1
                        lv = int(self.img[y, a - 1]) if a >= 1 else 255
                        rv = int(self.img[y, b + 1]) if b + 1 < self.w else 255
                        lok = lv < 215 and not erase[y, a - 1]
                        rok = rv < 215 and not erase[y, b + 1]
                        if lok and rok:
                            img[y, a:b + 1] = min(lv, rv)
                        elif (lok or rok) and (b - a + 1) >= 20:
                            # só um lado tem linha: se o outro lado retoma a mesma linha logo adiante
                            # (até 60 px), a linha escondida atrás do objeto é refeita até lá
                            if lok:
                                for r in range(b + 1, min(self.w, b + 71)):
                                    if self.img[y, r] < 215 and not erase[y, r]:
                                        img[y, a:r] = lv
                                        break
                            else:
                                for r in range(a - 1, max(0, a - 71), -1):
                                    if self.img[y, r] < 215 and not erase[y, r]:
                                        img[y, r + 1:b + 1] = rv
                                        break
                    else:
                        x += 1
        return img


def bbox_of_diff(a, b, thr=40):
    d = np.abs(a.astype(int) - b.astype(int)) > thr
    ys, xs = np.nonzero(d)
    if xs.size == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def dashed_rect(draw, box, dash=22, gap=14, width=6):
    x0, y0, x1, y1 = box
    for (ax, ay, bx, by) in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)):
        length = max(abs(bx - ax), abs(by - ay))
        dx, dy = (bx - ax) / length, (by - ay) / length
        t = 0
        while t < length:
            e = min(t + dash, length)
            draw.line((ax + dx * t, ay + dy * t, ax + dx * e, ay + dy * e), fill=0, width=width)
            t += dash + gap


def main():
    sc = Scene()
    orig = sc.img
    OUT.mkdir(parents=True, exist_ok=True)

    antes = Image.fromarray(orig)
    antes.save(OUT / "noite2_erros5_antes.png")
    antes.save(OUT / "noite2_erros10_antes.png")

    dep5 = sc.render(set(STAR1))
    dep10 = sc.render(set(STAR2))
    Image.fromarray(dep5).save(OUT / "noite2_erros5_depois.png")
    Image.fromarray(dep10).save(OUT / "noite2_erros10_depois.png")

    # caixas do gabarito: "tight" = traços originais do objeto (o que a criança deve achar);
    # "regions" = tudo o que muda quando o objeto sai (inclui linha de parede refeita), para a verificação
    tight, regions = {}, {}
    for oid, name, kind, box, bridge in OBJECTS:
        own = sc.masks[oid] & (sc.dark if kind != "web" else (orig < 215))
        ys, xs = np.nonzero(own)
        pad = 8
        tight[oid] = (max(0, int(xs.min()) - pad), max(0, int(ys.min()) - pad),
                      min(sc.w, int(xs.max()) + 1 + pad), min(sc.h, int(ys.max()) + 1 + pad))
        b = bbox_of_diff(orig, sc.render({oid}))
        assert b is not None, f"objeto {oid} não mudou"
        regions[oid] = (max(0, b[0] - 10), max(0, b[1] - 10), min(sc.w, b[2] + 10), min(sc.h, b[3] + 10))
    boxes = tight

    # ---------------- verificações
    report = {}
    for label, dep, ids in (("5", dep5, STAR1), ("10", dep10, STAR2)):
        # 1) cada diferença do gabarito difere de verdade dentro da caixa
        for oid in ids:
            x0, y0, x1, y1 = boxes[oid]
            n = int((np.abs(orig[y0:y1, x0:x1].astype(int) - dep[y0:y1, x0:x1].astype(int)) > 40).sum())
            assert n >= 150, f"jogo {label}: objeto {oid} quase não difere ({n} px)"
            report.setdefault(label, {})[oid] = n
        # 2) fora das caixas dos objetos apagados, nada mudou
        outside = np.ones((sc.h, sc.w), bool)
        for oid in ids:
            x0, y0, x1, y1 = regions[oid]
            outside[y0:y1, x0:x1] = False
        nd = int((orig[outside] != dep[outside]).sum())
        assert nd == 0, f"jogo {label}: {nd} px diferentes fora das caixas: {list(zip(*np.nonzero((orig != dep) & outside)))[:8]}"
        # 3) objetos mantidos intactos (traços do próprio objeto)
        for oid in set(STAR2) - set(ids):
            own = sc.masks[oid] & sc.dark
            assert (orig[own] == dep[own]).all(), f"jogo {label}: objeto mantido {oid} foi alterado"
    # 4) ★ é subconjunto da ★★: as 5 primeiras apagam o mesmo em ambas
    only5 = np.zeros((sc.h, sc.w), bool)
    for oid in STAR1:
        x0, y0, x1, y1 = regions[oid]
        only5[y0:y1, x0:x1] = True
    assert (dep5[only5] == dep10[only5]).sum() > 0.97 * only5.sum()

    # ---------------- gabaritos em PNG (P&B, retângulos tracejados pretos)
    for label, dep, ids in (("5", dep5, STAR1), ("10", dep10, STAR2)):
        g = Image.fromarray(dep).convert("L")
        d = ImageDraw.Draw(g)
        for oid in ids:
            x0, y0, x1, y1 = boxes[oid]
            dashed_rect(d, (x0, y0, x1, y1))
        g.save(OUT / f"noite2_erros{label}_gabarito.png")

    data = {
        "nome": "noite2_erros",
        "imagem_base": "inputs/illustrations/22.png",
        "tamanho_px": [sc.w, sc.h],
        "unidade_caixa": "px relativos à imagem 1969x799: [x, y, largura, altura]; caixa = o objeto, area_alterada = tudo que muda ao apagá-lo (inclui o tijolo de parede que reaparece)",
        "estrela_1_ids": STAR1,
        "estrela_2_ids": STAR2,
        "objetos": [
            {
                "id": oid,
                "nome": name,
                "caixa": [boxes[oid][0], boxes[oid][1], boxes[oid][2] - boxes[oid][0], boxes[oid][3] - boxes[oid][1]],
                "area_alterada": [regions[oid][0], regions[oid][1], regions[oid][2] - regions[oid][0], regions[oid][3] - regions[oid][1]],
                "estrelas": 1 if oid in STAR1 else 2,
                "pixels_diferentes_5": report["5"].get(oid),
                "pixels_diferentes_10": report["10"].get(oid),
            }
            for oid, name, kind, box, bridge in OBJECTS
        ],
        "verificacao": "diff de pixels: cada caixa difere; fora das caixas das diferenças, 0 pixels diferentes",
    }
    (OUT / "noite2_erros_gabarito.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("OK: 10 objetos; verificações passaram.")
    for o in data["objetos"]:
        print(o["id"], o["nome"], o["caixa"], o["pixels_diferentes_10"])


if __name__ == "__main__":
    main()
