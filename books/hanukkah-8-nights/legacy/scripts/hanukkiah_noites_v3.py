"""
hanukkiah_noites_v3.py
Hanukkiahs "da noite n" no MESMO traço da ilustração 12.png (a hanukkiah de copos e braços curvos que já
aparece na Noite 2), em vez das velas de retângulo desenhadas em código (pedido do Danilo, 08/10/2026,
páginas 32 e 36). A base é a 12.png com as 9 velas apagadas e os copos fechados; as velas (e o shamash)
são recortadas da própria 12.png e recolocadas nas posições da noite (a partir da direita), com chama em
gota (contorno + chama interna) desenhada por cima do pavio.

Uso: python hanukkiah_noites_v3.py
Saída (inputs/illustrations/): hk_n{0..8}.png  (n velas acesas + shamash aceso; hk_n0 = só o shamash)
                               hk_empty.png    (copos vazios, shamash presente sem chama)
                               hk_empty0.png   (todos os 9 copos vazios, inclusive o do shamash: para "desenhe as velas")
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ILL = Path(__file__).resolve().parents[2] / "inputs" / "illustrations"
_RAW = Image.open(ILL / "12.png").convert("L").point(lambda v: 255 if v > 205 else v)
PAD = 110                                   # folga em cima para as chamas
W, H = _RAW.size[0], _RAW.size[1] + PAD
SRC = Image.new("L", (W, H), 255)
SRC.paste(_RAW, (0, PAD))
SS = 3

# centros x das 8 velas (esquerda->direita, sem o shamash) e do shamash, medidos na 12.png
CX = [215, 352.5, 488.5, 624.5, 914, 1050.5, 1183.5, 1321.5]
SH = 768.5
HALF = 36          # meia largura de recorte da vela
CANDLE_TOP, CANDLE_CUT = 150 + PAD, 372 + PAD       # faixa de y das velas comuns (acima do aro do copo)
SH_TOP, SH_CUT = 30 + PAD, 300 + PAD                # faixa de y do shamash


def cup_mouth(d, cx, cy_mouth, k=SS):
    """Fecha o copo vazio: boca em elipse dentro do aro (como nos copos vazios da 42b_v2)."""
    lw = 6 * k
    # d.arc([(cx - 58) * k, (cy_mouth - 20) * k, (cx + 58) * k, (cy_mouth + 18) * k], 200, 340, fill=0, width=lw)
    d.ellipse([(cx - 44) * k, (cy_mouth - 10) * k, (cx + 44) * k, (cy_mouth + 12) * k], outline=0, width=lw)


def empty_base(shamash_candle=True):
    a = np.array(SRC)
    if not shamash_candle:  # copo do shamash vazio: apaga a vela alta
        a[40 + PAD:305 + PAD + 1, int(SH - HALF - 8):int(SH + HALF + 9)] = 255
        a[306 + PAD:317 + PAD, int(SH - 30):int(SH + 31)] = 255
    for c in CX:
        a[CANDLE_TOP:CANDLE_CUT + 9, int(c - HALF - 8):int(c + HALF + 9)] = 255
        a[CANDLE_CUT + 1:394 + PAD, int(c - 30):int(c + 31)] = 255
    return Image.fromarray(a).resize((W * SS, H * SS), Image.LANCZOS)


def flame(d, cx, y_wick, h=74, w=46, k=SS):
    """Chama em gota (ponta em cima, base redonda) sentada no pavio: contorno grosso + chama interna."""
    ts = [i / 80 * 2 * math.pi for i in range(81)]
    raw = [math.sin(t) * math.sin(t / 2) for t in ts]
    norm = max(abs(v) for v in raw)

    def gota(hh, ww, y_base):
        return [(cx + ww / 2 * (math.sin(t) * math.sin(t / 2)) / norm, y_base - hh * (1 - math.cos(t)) / 2 * -1 - hh) for t in ts]
    # y = y_base - hh*(1+cos t)/2 -> t=0 topo (ponta), t=pi base redonda em y_base
    def curva(hh, ww, y_base):
        return [(cx + ww / 2 * (math.sin(t) * math.sin(t / 2)) / norm, y_base - hh * (1 + math.cos(t)) / 2) for t in ts]
    outer = curva(h, w, y_wick)
    d.line([(x * k, y * k) for x, y in outer], fill=0, width=6 * k, joint="curve")
    inner = curva(h * 0.5, w * 0.46, y_wick - 5)
    d.line([(x * k, y * k) for x, y in inner], fill=0, width=4 * k, joint="curve")


def render(n, out, shamash_lit=True, flames=True, shamash_candle=True):
    base = empty_base(shamash_candle)
    a = np.array(base)
    srcA = np.array(SRC.resize((W * SS, H * SS), Image.LANCZOS))
    # shamash: sempre presente (vela alta no copo central)
    x0, x1 = int((SH - HALF) * SS), int((SH + HALF) * SS)
    if shamash_lit or n >= 0:
        pass
    # velas comuns: posições a partir da direita (índice 7 = noite 1)
    chosen = list(range(7, 7 - n, -1)) if n > 0 else []
    for i in chosen:
        c = CX[i]
        xa, xb = int((c - HALF - 6) * SS), int((c + HALF + 7) * SS)
        ya, yb = CANDLE_TOP * SS, (CANDLE_CUT + 18) * SS
        a[ya:yb, xa:xb] = np.minimum(a[ya:yb, xa:xb], srcA[ya:yb, xa:xb])
    img = Image.fromarray(a)
    d = ImageDraw.Draw(img)
    if not shamash_candle:
        cup_mouth(d, SH, 306 + PAD)
    for i, c in enumerate(CX):          # copos sem vela: boca aberta
        if i not in chosen:
            cup_mouth(d, c, 386 + PAD)
    # shamash: reaplica a vela alta e o copo original (o copo central não foi apagado)
    if flames:
        for i in chosen:
            flame(d, CX[i], 197 + PAD)
        if shamash_lit:
            flame(d, SH, 64 + PAD)
    img = img.resize((W, H), Image.LANCZOS)
    img.save(out, dpi=(300, 300))


def main():
    for n in range(0, 9):
        render(n, ILL / f"hk_n{n}.png")
    render(0, ILL / "hk_empty.png", shamash_lit=False, flames=False)
    render(0, ILL / "hk_empty0.png", shamash_lit=False, flames=False, shamash_candle=False)
    # corta a margem branca com a MESMA caixa em todas (a n8 é a maior): alinhamento idêntico entre as figuras
    ref = np.array(Image.open(ILL / "hk_n8.png").convert("L")) < 128
    ys, xs = np.where(ref)
    pad = 14
    box = (max(0, xs.min() - pad), max(0, ys.min() - pad), min(W, xs.max() + pad), min(H, ys.max() + pad))
    for f in [f"hk_n{n}.png" for n in range(9)] + ["hk_empty.png", "hk_empty0.png"]:
        Image.open(ILL / f).crop(box).save(ILL / f, dpi=(300, 300))
    print("[OK] hk_n0..hk_n8.png, hk_empty.png; caixa", box)


if __name__ == "__main__":
    main()
