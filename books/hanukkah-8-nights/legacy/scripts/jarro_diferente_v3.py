"""
jarro_diferente_v3.py
"Which Jar Is Different?" (Noite 3, ★), versão 3 (pedido do Danilo, 08/10/2026: os jarros de código estavam toscos).
Usa UMA ilustração de jarro gerada (inputs/illustrations/_raw/erros/jarro_base_a.png: jarro com alça à direita,
selo no gargalo e faixa de 4 triângulos) e a repete 12 vezes em 3 linhas x 4 colunas, com uma prateleira sob cada
linha. Todos os jarros são cópias idênticas; só um tem a diferença: UM TRIÂNGULO A MENOS na faixa (3 em vez de 4),
apagado por componente conexo. Verificado por pixel: o jarro diferente é o único que difere da cópia padrão.

Saídas (inputs/puzzle-assets/): noite3_jarros_v3.png (puzzle), noite3_jarros_v3_gabarito_key.png (circulado),
noite3_jarros_v3.json (posição do jarro diferente).
Uso: python jarro_diferente_v3.py
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "inputs" / "illustrations" / "_raw" / "erros" / "jarro_base_a.png"
PZ = ROOT / "inputs" / "puzzle-assets"
COLS, ROWS = 4, 3
ODD = (2, 3)  # (linha, coluna), 1-based
JAR_H = 560   # px de altura de cada jarro no puzzle


def jarro_padrao():
    g = Image.open(RAW).convert("L").point(lambda v: 255 if v > 200 else v)
    a = np.array(g)
    ys, xs = np.where(a < 140)
    pad = 6
    g = g.crop((xs.min() - pad, ys.min() - pad, xs.max() + pad, ys.max() + pad))
    w, h = g.size
    return g.resize((round(w * JAR_H / h), JAR_H), Image.LANCZOS)


def jarro_diferente(base):
    a = np.array(base)
    h, w = a.shape
    # componentes dos triângulos: contornos fechados na faixa decorativa (terço inferior-médio do jarro)
    lab, n = ndimage.label(a < 140)
    achados = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        ys, xs = sl
        cy = (ys.start + ys.stop) / 2 / h
        ww, hh = xs.stop - xs.start, ys.stop - ys.start
        if 0.55 < cy < 0.85 and ww < 0.2 * w and hh < 0.2 * h and ww > 0.05 * w:
            achados.append((xs.start, i))
    assert len(achados) == 4, f"esperava 4 triângulos, achei {len(achados)}"
    achados.sort()
    alvo = achados[3][1]  # triângulo mais à direita
    m = ndimage.binary_dilation(lab == alvo, iterations=4)
    b = a.copy()
    b[m] = 255
    return Image.fromarray(b)


def main():
    padrao = jarro_padrao()
    odd = jarro_diferente(padrao)
    jw, jh = padrao.size
    gx, gy = 70, 60        # espaços entre jarros
    shelf = 26             # espessura da prateleira
    W = COLS * jw + (COLS + 1) * gx
    H = ROWS * (jh + shelf + gy) + gy
    canvas = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(canvas)
    boxes = {}
    for r in range(ROWS):
        y = gy + r * (jh + shelf + gy)
        for c in range(COLS):
            x = gx + c * (jw + gx)
            canvas.paste(odd if (r + 1, c + 1) == ODD else padrao, (x, y))
            boxes[(r + 1, c + 1)] = (x, y, x + jw, y + jh)
        d.rounded_rectangle([gx // 2, y + jh + 4, W - gx // 2, y + jh + 4 + shelf], radius=10, outline=0, width=9)
    canvas.save(PZ / "noite3_jarros_v3.png", dpi=(300, 300))

    # verificação por pixel: só o jarro ODD difere da cópia padrão; os outros 11 são idênticos
    A = np.array(canvas).astype(int)
    ref = np.array(padrao).astype(int)
    difs = []
    for (r, c), (x0, y0, x1, y1) in boxes.items():
        if np.abs(A[y0:y1, x0:x1] - ref).max() > 0:
            difs.append((r, c))
    assert difs == [ODD], f"jarros diferentes encontrados: {difs}"

    key = canvas.convert("RGB")
    kd = ImageDraw.Draw(key)
    x0, y0, x1, y1 = boxes[ODD]
    cx, cy, R = (x0 + x1) / 2, (y0 + y1) / 2, max(jw, jh) * 0.62
    kd.ellipse([cx - R, cy - R, cx + R, cy + R], outline=(0, 0, 0), width=20)
    key.convert("L").save(PZ / "noite3_jarros_v3_gabarito_key.png", dpi=(300, 300))
    (PZ / "noite3_jarros_v3.json").write_text(json.dumps({
        "linhas": ROWS, "colunas": COLS, "posicao_linha_coluna_1_based": list(ODD),
        "diferenca": "o jarro diferente tem 3 triângulos na faixa (os outros 11 têm 4)"}, indent=2), encoding="utf-8")
    print(f"[OK] {COLS * ROWS} jarros, o diferente está em linha {ODD[0]}, coluna {ODD[1]}; imagem {W}x{H}")


if __name__ == "__main__":
    main()
