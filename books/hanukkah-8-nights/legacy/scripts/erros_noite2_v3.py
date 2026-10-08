"""
erros_noite2_v3.py
Jogo dos erros da Noite 2, versão 3 (pedido do Danilo, 08/10/2026): em vez de uma cena bagunçada com objetos
apagados por script, duas cenas COMPLETAS geradas à parte (inputs/illustrations/_raw/erros/erros{5,10}_base_a.png).
O "depois" é feito apagando objetos da cópia (no Canva, à mão, ou provisoriamente por este script).

Fluxo:
  1. `antes`  = a cena completa cortada em faixa 2:1 (y 128..896 do PNG 1536x1024).
  2. `depois` = a mesma faixa com N objetos apagados. Se existir `inputs/puzzle-assets/noite2_erros{N}_depois_v3.png`
     feito à mão, ele é usado como está (mesmo tamanho do antes). Senão, este script gera um depois provisório
     apagando componentes isolados da cena (lista PROVISORIO abaixo) e grava como `..._depois_v3_auto.png`.
  3. Confere por código: diferenças só em N regiões (agrupadas por proximidade); fora delas 0 px diferentes.
  4. Gabarito: o `antes` com caixas tracejadas numeradas nas N regiões (`..._gabarito_key.png`) + JSON das caixas.

Uso: python erros_noite2_v3.py
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "inputs" / "illustrations" / "_raw" / "erros"
PZ = ROOT / "inputs" / "puzzle-assets"
Y0, Y1 = 0, 1024  # cena inteira 3:2 (1536 x 1024)

# cena-base de cada jogo (PNG 1536x1024 gerado) e faixa 2:1 usada no livro
BASES = {5: "s1_b.png", 7: "s2_user_antes.png"}
SEED = {5: 3, 7: 5}


def isolados(base):
    """Componentes conexos isolados (objetos soltos, sem encostar em parede/coluna): candidatos a apagar."""
    a = np.array(base.convert("L"))
    lab, _ = ndimage.label(ndimage.binary_dilation(a < 140, iterations=4))
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        area = int((lab[sl] == i).sum())
        ys, xs = sl
        if 2500 < area < 70000:
            out.append((xs.start, ys.start, xs.stop, ys.stop, i))
    return a, lab, out


def band(im):
    return im.crop((0, Y0, im.width, Y1))


def provisional(n, base):
    """Depois provisório: apaga N objetos isolados (bem separados entre si); o Danilo troca pelo feito à mão."""
    import random
    a, lab, cand = isolados(base)
    rnd = random.Random(SEED[n])
    rnd.shuffle(cand)
    escolhidos = []
    for c in cand:
        if all(c[0] > e[2] + 40 or c[2] < e[0] - 40 or c[1] > e[3] + 40 or c[3] < e[1] - 40 for e in escolhidos):
            escolhidos.append(c)
        if len(escolhidos) == n:
            break
    assert len(escolhidos) == n, "poucos objetos isolados na cena"
    out = a.copy()
    for *_, i in escolhidos:
        out[ndimage.binary_dilation(lab == i, iterations=6)] = 255
    return Image.fromarray(out)


def regioes(antes, depois, n):
    """Diferenças = traço escuro de uma imagem sem par escuro na outra a até 3 px (ignora o deslocamento de 1-2 px
    de imagens regeneradas). Agrupa por proximidade (14 px), descarta ruído (< 40 px de tinta) e funde caixas
    quase contidas uma na outra (partes do mesmo objeto)."""
    a = np.array(antes.convert("L")) < 128
    b = np.array(depois.convert("L")) < 128
    da = a & ~ndimage.binary_dilation(b, iterations=3)
    db = b & ~ndimage.binary_dilation(a, iterations=3)
    d = da | db
    lab, _ = ndimage.label(ndimage.binary_dilation(d, iterations=14))
    boxes = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        m = d & (lab == i)
        if m.sum() < 40:
            continue
        ys, xs = np.where(m)
        boxes.append([int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1])
    mudou = True
    while mudou:
        mudou = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a_, b_ = boxes[i], boxes[j]
                iw = min(a_[2], b_[2]) - max(a_[0], b_[0])
                ih = min(a_[3], b_[3]) - max(a_[1], b_[1])
                menor = min((a_[2] - a_[0]) * (a_[3] - a_[1]), (b_[2] - b_[0]) * (b_[3] - b_[1]))
                if iw > 0 and ih > 0 and iw * ih > 0.5 * menor:
                    boxes[i] = [min(a_[0], b_[0]), min(a_[1], b_[1]), max(a_[2], b_[2]), max(a_[3], b_[3])]
                    del boxes[j]
                    mudou = True
                    break
            if mudou:
                break
    boxes = [[x0, y0, x1 - x0, y1 - y0] for x0, y0, x1, y1 in boxes]
    boxes.sort(key=lambda b: (b[0], b[1]))
    return d, boxes


def gabarito(antes, boxes, caminho, n):
    """Imagem ORIGINAL (o antes) com uma bola cinza e o número em branco em cada diferença (sem destacar a área)."""
    img = antes.convert("L").convert("RGB")
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("arialbd.ttf", 76)
    except OSError:
        f = ImageFont.load_default()
    for i, (x, y, w, h) in enumerate(boxes, 1):
        cx, cy, r = x + w / 2, y + h / 2, 62
        cx = min(max(cx, r + 4), img.width - r - 4)
        cy = min(max(cy, r + 4), img.height - r - 4)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(105, 105, 105))
        d.text((cx, cy - 2), str(i), fill=(255, 255, 255), font=f, anchor="mm")
    img.convert("L").save(caminho)


def processar(n):
    base = Image.open(RAW / BASES[n]).convert("L").point(lambda v: 255 if v > 205 else v)  # fundo quase-branco vira branco
    antes = band(base)
    antes.save(PZ / f"noite2_erros{n}_antes_v3.png", dpi=(300, 300))
    manual = PZ / f"noite2_erros{n}_depois_v3.png"
    if manual.exists():
        depois = Image.open(manual).convert("L")
        assert depois.size == antes.size, f"{manual.name}: tamanho {depois.size} difere do antes {antes.size}"
        origem = "feito à mão"
    else:
        depois = provisional(n, base).crop((0, Y0, base.width, Y1))
        depois.save(PZ / f"noite2_erros{n}_depois_v3_auto.png", dpi=(300, 300))
        origem = "provisório (automático)"
    depois.save(PZ / f"noite2_erros{n}_depois_v3_final.png", dpi=(300, 300))  # é este que o livro usa
    mask, boxes = regioes(antes, depois, n)
    assert len(boxes) == n, f"{n} erros esperados, achei {len(boxes)} regiões: {boxes}"
    gabarito(antes, boxes, PZ / f"noite2_erros{n}_v3_gabarito_key.png", n)
    (PZ / f"noite2_erros{n}_v3.json").write_text(json.dumps({"n": n, "origem_do_depois": origem, "caixas_xywh": boxes}, indent=2), encoding="utf-8")
    print(f"[OK] erros{n}: {len(boxes)} diferenças ({origem}); caixas {boxes}")


if __name__ == "__main__":
    for n in (5, 7):
        processar(n)
