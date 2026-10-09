"""
sudoku_formas_v3.py
Redesenho dos dois sudokus da Noite 3 (pedido do Danilo, 08/10/2026): os símbolos antigos (jarro, vela,
dreidel, hanukkiah, moeda) eram difíceis de a criança desenhar. Agora são formas simples de desenhar à mão:
  4x4: círculo, quadrado, triângulo, estrela
  6x6: + coração, + (mais)
O CONTEÚDO não muda: lê grade, solução e pistas dos *_gabarito.json já aprovados (solução única reconfirmada
por backtracking), só troca o desenho. Os PNG antigos ficam intactos; as saídas têm sufixo _v3.

Saídas em inputs/puzzle-assets/:
  noite3_sudoku{4x4,6x6}_v3_recorte.png        puzzle impresso (margem branca já cortada)
  noite3_sudoku{4x4,6x6}_v3_gabarito_key.png   solução completa (para o answer key)
  noite3_sym3_{circle,square,triangle,star,heart,plus}.png   legenda dos sudokus (symbol-key)
Uso: python sudoku_formas_v3.py
"""
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parents[1] / "inputs" / "puzzle-assets"

CEL = 540       # px por célula (4x4 -> ~2200 px; 349 DPI a 6.3 in)
FORMAS = ["circle", "square", "triangle", "star", "heart", "plus"]  # ordem 1..N dos JSON


def _pts(nome):
    """Contorno de cada forma em coordenadas unitárias (centro 0,0; raio ~1; y para cima)."""
    if nome == "square":
        a = 0.88
        return [(-a, -a), (a, -a), (a, a), (-a, a)]
    if nome == "triangle":
        r = 1.15
        return [(r * math.cos(math.pi / 2 + i * 2 * math.pi / 3), r * math.sin(math.pi / 2 + i * 2 * math.pi / 3) - 0.14) for i in range(3)]
    if nome == "star":
        R, r = 1.14, 0.47
        return [((R if i % 2 == 0 else r) * math.cos(math.pi / 2 + i * math.pi / 5),
                 (R if i % 2 == 0 else r) * math.sin(math.pi / 2 + i * math.pi / 5) - 0.06) for i in range(10)]
    if nome == "heart":
        out = []
        for i in range(160):
            t = 2 * math.pi * i / 160
            out.append((16 * math.sin(t) ** 3 / 16 * 1.02,
                        (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) / 16 * 1.02 + 0.06))
        return out
    raise ValueError(nome)


def forma(ax, nome, cx, cy, s, lw):
    """Desenha a forma no eixo matplotlib (cx, cy, raio s em unidades da grade; lw em pontos)."""
    kw = dict(color="black", linewidth=lw, solid_joinstyle="round", solid_capstyle="round")
    if nome == "circle":
        ax.add_patch(mpatches.Circle((cx, cy), s * 0.96, fill=False, edgecolor="black", linewidth=lw))
    elif nome == "plus":
        a = s * 0.98
        ax.plot([cx - a, cx + a], [cy, cy], **kw)
        ax.plot([cx, cx], [cy - a, cy + a], **kw)
    else:
        pts = _pts(nome)
        xs = [cx + x * s for x, _ in pts] + [cx + pts[0][0] * s]
        ys = [cy + y * s for _, y in pts] + [cy + pts[0][1] * s]
        ax.plot(xs, ys, **kw)


def _fig(w_units, h_units, px_per_unit):
    fig = plt.figure(figsize=(w_units * px_per_unit / 300, h_units * px_per_unit / 300), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w_units)
    ax.set_ylim(h_units, 0)  # y para baixo (linhas da grade); formas usam y para cima -> invertido abaixo
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def caixas(n):
    return (2, 2) if n == 4 else (2, 3)


def contar(grade, n, limite=2):
    br, bc = caixas(n)
    g = [r[:] for r in grade]
    vazios = [(r, c) for r in range(n) for c in range(n) if g[r][c] == 0]
    cont = [0]

    def ok(r, c, v):
        if any(g[r][k] == v for k in range(n)) or any(g[k][c] == v for k in range(n)):
            return False
        r0, c0 = r // br * br, c // bc * bc
        return all(g[i][j] != v for i in range(r0, r0 + br) for j in range(c0, c0 + bc))

    def rec(i=0):
        if cont[0] >= limite:
            return
        if i == len(vazios):
            cont[0] += 1
            return
        r, c = vazios[i]
        for v in range(1, n + 1):
            if ok(r, c, v):
                g[r][c] = v
                rec(i + 1)
                g[r][c] = 0
    rec()
    return cont[0]


def grade_img(grade, n, caminho):
    br, bc = caixas(n)
    m = 0.04  # margem em células
    fig, ax = _fig(n + 2 * m, n + 2 * m, CEL)
    for i in range(n + 1):
        lw_r = 3.4 if i % br == 0 else 1.1
        lw_c = 3.4 if i % bc == 0 else 1.1
        ax.plot([m, m + n], [m + i, m + i], color="black", linewidth=lw_r, solid_capstyle="projecting")
        ax.plot([m + i, m + i], [m, m + n], color="black", linewidth=lw_c, solid_capstyle="projecting")
    lw = 5.0 if n == 4 else 4.4
    for r in range(n):
        for c in range(n):
            v = grade[r][c]
            if v:
                # eixo y invertido: converter y "para cima" das formas
                forma_inv(ax, FORMAS[v - 1], m + c + 0.5, m + r + 0.5, 0.31, lw)
    fig.savefig(caminho, dpi=300, facecolor="white")
    plt.close(fig)


def forma_inv(ax, nome, cx, cy, s, lw):
    """Como forma(), mas no eixo com y para baixo (espelha o y dos contornos)."""
    kw = dict(color="black", linewidth=lw, solid_joinstyle="round", solid_capstyle="round")
    if nome == "circle":
        ax.add_patch(mpatches.Circle((cx, cy), s * 0.96, fill=False, edgecolor="black", linewidth=lw))
    elif nome == "plus":
        a = s * 0.98
        ax.plot([cx - a, cx + a], [cy, cy], **kw)
        ax.plot([cx, cx], [cy - a, cy + a], **kw)
    else:
        pts = [(cx + x * s, cy - y * s) for x, y in _pts(nome)]
        ax.add_patch(mpatches.Polygon(pts, closed=True, fill=False, edgecolor="black", linewidth=lw, joinstyle="round"))


def legenda(nome):
    fig, ax = _fig(2.2, 2.2, 240)
    forma_inv(ax, nome, 1.1, 1.1, 0.8, 8.5)
    fig.savefig(ASSETS / f"noite3_sym3_{nome}.png", dpi=300, facecolor="white")
    plt.close(fig)


def main():
    for n, nome in ((4, "noite3_sudoku4x4"), (6, "noite3_sudoku6x6")):
        data = json.loads((ASSETS / f"{nome}_gabarito.json").read_text(encoding="utf-8"))
        puzzle, sol = data["puzzle"], data["solucao"]
        assert contar(puzzle, n) == 1, f"{nome}: solução não é única"
        assert all(sorted(r) == list(range(1, n + 1)) for r in sol)
        assert all(puzzle[r][c] in (0, sol[r][c]) for r in range(n) for c in range(n))
        grade_img(puzzle, n, ASSETS / f"{nome}_v3_recorte.png")
        grade_img(sol, n, ASSETS / f"{nome}_v3_gabarito_key.png")
        print(f"[OK] {nome}: {n}x{n}, {data['numero_de_pistas']} pistas, solução única reconfirmada")
    for f in FORMAS:
        legenda(f)
    print("[OK] legendas das formas")


if __name__ == "__main__":
    main()
