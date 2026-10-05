"""
rerender_noite3_hires.py
Redesenha em alta resolução os 3 puzzles da Noite 3 SEM mudar o conteúdo:
lê grade, solução e posição do jarro diferente dos *_gabarito.json já aprovados,
reverifica (solução única, exatamente 1 jarro diferente) e redesenha tudo em escala K.

Os PNGs originais eram 400-580 px (21/09) e pixelavam na impressão (mesma causa da decisão 50).
Uso: python rerender_noite3_hires.py   (a partir de qualquer pasta)
Saída: sobrescreve books/hanukkah-8-nights/inputs/puzzle-assets/noite3_*.png
"""
import importlib.util
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parents[1] / "inputs" / "puzzle-assets"
K = 5  # fator de escala sobre o desenho original

spec = importlib.util.spec_from_file_location("sud", HERE / "gerar_sudoku_simbolos.py")
sud = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sud)  # só para reaproveitar o solver (contar_solucoes, caixas_dims, SIMBOLOS)

INK = (0, 0, 0)


# --------------------------------------------------------------------------- símbolos
def simbolo(draw, nome, cx, cy, tam):
    """Mesmos desenhos do script original; só espessuras de traço e detalhes fixos escalam com K."""
    s = tam / 2
    lw = max(2, int(tam * 0.055))
    thin = max(2, lw - K // 2)

    if nome == "jar":
        cw, ch = s * 1.1, s * 1.0
        draw.ellipse([cx - cw / 2, cy - ch / 2 + s * 0.25, cx + cw / 2, cy + ch / 2 + s * 0.25], outline=INK, width=lw)
        draw.rectangle([cx - s * 0.22, cy - s * 0.85, cx + s * 0.22, cy - s * 0.25], outline=INK, width=lw)
        draw.rectangle([cx - s * 0.34, cy - s * 1.0, cx + s * 0.34, cy - s * 0.82], outline=INK, width=lw)
    elif nome == "candle":
        draw.rectangle([cx - s * 0.22, cy - s * 0.3, cx + s * 0.22, cy + s * 0.95], outline=INK, width=lw)
        draw.line([cx, cy - s * 0.3, cx, cy - s * 0.55], fill=INK, width=lw)
        draw.ellipse([cx - s * 0.2, cy - s * 1.0, cx + s * 0.2, cy - s * 0.5], outline=INK, width=lw)
    elif nome == "dreidel":
        topo_w, base_w, alt = s * 0.9, s * 0.35, s * 1.3
        yt, yb = cy - alt / 2 + s * 0.15, cy + alt / 2 + s * 0.15
        draw.polygon([(cx - topo_w / 2, yt), (cx + topo_w / 2, yt), (cx + base_w / 2, yb), (cx - base_w / 2, yb)],
                     outline=INK, width=lw)
        draw.line([cx, yb, cx, yb + s * 0.25], fill=INK, width=lw)
        draw.line([cx, yt, cx, yt - s * 0.3], fill=INK, width=lw)
        draw.line([cx - s * 0.18, yt - s * 0.3, cx + s * 0.18, yt - s * 0.3], fill=INK, width=lw)
    elif nome == "star":
        r = s * 0.8
        up = [(cx + r * math.cos(-math.pi / 2 + i * 2 * math.pi / 3), cy + r * math.sin(-math.pi / 2 + i * 2 * math.pi / 3)) for i in range(3)]
        dn = [(cx + r * math.cos(math.pi / 2 + i * 2 * math.pi / 3), cy + r * math.sin(math.pi / 2 + i * 2 * math.pi / 3)) for i in range(3)]
        draw.polygon(up, outline=INK, width=lw)
        draw.polygon(dn, outline=INK, width=lw)
    elif nome == "hanukkiah":
        # maior que o original (que ficava minúsculo): base + 9 velas grossas, shamash mais alto, chamas
        bw = s * 1.9
        yb = cy + s * 0.75
        draw.line([cx - bw / 2, yb, cx + bw / 2, yb], fill=INK, width=lw)
        draw.line([cx, yb, cx, yb + s * 0.22], fill=INK, width=lw)
        draw.line([cx - s * 0.35, yb + s * 0.22, cx + s * 0.35, yb + s * 0.22], fill=INK, width=lw)
        for i in range(9):
            hx = cx - bw / 2 + bw * i / 8
            alt = s * 1.05 if i == 4 else s * 0.6
            draw.line([hx, yb, hx, yb - alt], fill=INK, width=lw)
            rr = s * 0.075
            draw.ellipse([hx - rr, yb - alt - 3.2 * rr, hx + rr, yb - alt - 0.4 * rr], outline=INK, width=max(2, K // 2))
    elif nome == "coin":
        draw.ellipse([cx - s * 0.8, cy - s * 0.8, cx + s * 0.8, cy + s * 0.8], outline=INK, width=lw)
        draw.ellipse([cx - s * 0.55, cy - s * 0.55, cx + s * 0.55, cy + s * 0.55], outline=INK, width=thin)
        draw.line([cx - s * 0.25, cy, cx + s * 0.25, cy], fill=INK, width=lw)
    else:
        raise ValueError(nome)


def grade_png(grade, n, caminho):
    br, bc = sud.caixas_dims(n)
    cel, marg = 90 * K, 20 * K
    lado = cel * n
    img = Image.new("RGB", (lado + 2 * marg, lado + 2 * marg), "white")
    d = ImageDraw.Draw(img)
    for r in range(n + 1):
        w = 4 * K if r % br == 0 else 1 * K + 1
        y = marg + r * cel
        d.line([(marg - w // 2, y), (marg + lado + w // 2, y)], fill=INK, width=w)
    for c in range(n + 1):
        w = 4 * K if c % bc == 0 else 1 * K + 1
        x = marg + c * cel
        d.line([(x, marg - w // 2), (x, marg + lado + w // 2)], fill=INK, width=w)
    for r in range(n):
        for c in range(n):
            v = grade[r][c]
            if v:
                simbolo(d, sud.SIMBOLOS[v - 1], marg + c * cel + cel / 2, marg + r * cel + cel / 2, cel * 0.72)
    img.save(caminho, dpi=(300, 300))


# --------------------------------------------------------------------------- jarros
def jarro(draw, cx, cy, tam, padrao, circulado=False):
    s = tam / 2
    lw = max(2, int(tam * 0.05))
    cw, ch = s * 1.3, s * 1.15
    top, bot = cy - ch / 2 + s * 0.3, cy + ch / 2 + s * 0.3
    draw.ellipse([cx - cw / 2, top, cx + cw / 2, bot], outline=INK, width=lw)
    draw.rectangle([cx - s * 0.24, cy - s * 0.95, cx + s * 0.24, top + s * 0.1], outline=INK, width=lw)
    draw.rectangle([cx - s * 0.36, cy - s * 1.1, cx + s * 0.36, cy - s * 0.92], outline=INK, width=lw)
    if padrao == "linhas_retas":
        for i in range(-1, 2):
            x = cx + i * s * 0.28
            draw.line([x, top + s * 0.22, x, bot - s * 0.18], fill=INK, width=max(2, lw - K // 2))
    else:  # bolinhas
        for i in range(-1, 2):
            x, y, r = cx + i * s * 0.3, cy + s * 0.15, s * 0.09
            draw.ellipse([x - r, y - r, x + r, y + r], outline=INK, width=max(2, lw - K // 2))
    if circulado:  # preto: o livro é P&B (o círculo vermelho original saía cinza)
        R = tam * 0.62
        draw.ellipse([cx - R, cy - R, cx + R, cy + R], outline=INK, width=lw + 2 * K)


def jarros_png(info, caminho, revelar):
    L, C, cel, marg = info["linhas"], info["colunas"], 130 * K, 24 * K
    img = Image.new("RGB", (C * cel + 2 * marg, L * cel + 2 * marg), "white")
    d = ImageDraw.Draw(img)
    for i in range(L * C):
        r, c = divmod(i, C)
        padrao = info["padrao_diferente"] if i == info["indice_0_based"] else info["padrao_comum"]
        jarro(d, marg + c * cel + cel / 2, marg + r * cel + cel / 2, cel * 0.8, padrao, revelar and i == info["indice_0_based"])
    img.save(caminho, dpi=(300, 300))


def main():
    for n, nome in ((4, "noite3_sudoku4x4"), (6, "noite3_sudoku6x6")):
        data = json.loads((ASSETS / f"{nome}_gabarito.json").read_text(encoding="utf-8"))
        puzzle, sol = data["puzzle"], data["solucao"]
        assert sud.contar_solucoes(puzzle, n, limite=2) == 1, f"{nome}: solução não é única"
        assert sud.resolver_unico([r[:] for r in puzzle], n) == sol, f"{nome}: solução diverge do gabarito"
        assert sum(1 for r in puzzle for v in r if v) == data["numero_de_pistas"], f"{nome}: nº de pistas"
        grade_png(puzzle, n, ASSETS / f"{nome}.png")
        grade_png(sol, n, ASSETS / f"{nome}_gabarito.png")
        print(f"[OK] {nome}: {n}x{n}, {data['numero_de_pistas']} pistas, solução única reconfirmada")
    info = json.loads((ASSETS / "noite3_jarro_diferente_gabarito.json").read_text(encoding="utf-8"))
    assert info["indice_0_based"] == (info["posicao_linha_coluna_1_based"][0] - 1) * info["colunas"] + info["posicao_linha_coluna_1_based"][1] - 1
    jarros_png(info, ASSETS / "noite3_jarro_diferente.png", False)
    jarros_png(info, ASSETS / "noite3_jarro_diferente_gabarito.png", True)
    print("[OK] noite3_jarro_diferente: 1 jarro diferente na posição", info["posicao_linha_coluna_1_based"])


if __name__ == "__main__":
    main()
