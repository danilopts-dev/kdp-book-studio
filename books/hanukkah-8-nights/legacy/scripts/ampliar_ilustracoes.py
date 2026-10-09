"""
ampliar_ilustracoes.py
Gera inputs/illustrations_hi/ com todas as ilustrações (traço P&B) ampliadas 2x quando têm menos de 2400 px de
largura, em escala de cinza, com fundo branco puro e contraste de traço reforçado (curva de níveis), para que o
miolo atinja 300 DPI efetivos nas larguras impressas (revisão de 09/10/2026: p14 177 DPI, p35 177, p40 146, p32 222).
As originais (inputs/illustrations/) ficam intactas. Observação: a ampliação não cria detalhe novo; ela deixa o
contorno liso e nítido em vez de serrilhado/embaçado.
Uso: python ampliar_ilustracoes.py
"""
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC, DST = ROOT / "inputs" / "illustrations", ROOT / "inputs" / "illustrations_hi"
DST.mkdir(exist_ok=True)


def niveis(a: np.ndarray) -> np.ndarray:
    """Fundo (>= 235) vira branco; traço escuro fica mais firme: [60, 200] -> [0, 255]."""
    x = np.clip((a.astype(np.float32) - 60.0) * (255.0 / 140.0), 0, 255)
    x[a >= 235] = 255
    return x.astype(np.uint8)


for f in sorted(SRC.glob("*.png")):
    im = Image.open(f)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        bg.alpha_composite(im)
        im = bg
    im = im.convert("L")
    if im.width < 2400:
        k = 2 if im.width * 2 <= 4800 else 1
        im = im.resize((im.width * k, im.height * k), Image.LANCZOS)
    out = Image.fromarray(niveis(np.array(im)))
    out.save(DST / f.name, dpi=(300, 300), optimize=True)
print(len(list(DST.glob("*.png"))), "arquivos em", DST)
