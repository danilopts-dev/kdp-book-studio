"""
gerar_template_dreidel_latino.py
VARIANTE SEM HEBRAICO (decisao 49): iniciais latinas N, G, H, S no lugar das letras hebraicas, sem titulo na imagem,
fundo branco opaco, 400 dpi, girado 90 graus (retrato) para ocupar a pagina inteira.
(baseado em gerar_template_dreidel.py)

Gera a planificacao (net) de um dreidel de papel para recortar e montar:
4 faces laterais quadradas (uma letra hebraica em cada: Nun, Gimel, Hei,
Shin), abas de cola nas bordas, uma aba de topo (para fechar a ponta) e
uma aba de base. Linhas de dobra tracejadas, linhas de corte solidas.
Verso da pagina fica em branco (o script gera so a frente).

Uso: python3 gerar_template_dreidel.py
Saida: puzzle-assets/noite5_template_dreidel.png
       puzzle-assets/noite5_template_dreidel_gabarito.json (letras/posicoes, para conferencia)
"""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

OUT_PNG = "inputs/puzzle-assets/noite5_template_dreidel_branco.png"
OUT_JSON = "inputs/puzzle-assets/noite5_template_dreidel_branco_gabarito.json"

# Letras hebraicas das 4 faces, na ordem tradicional (fora de Israel).
LETRAS = ["N", "G", "H", "S"]  # iniciais latinas: Nun, Gimel, Hei, Shin
NOMES = ["Nun", "Gimel", "Hei", "Shin"]
SIGNIFICADOS = ["Nes (a miracle)", "Gadol (great)", "Haya (happened)", "Sham (there)"]

S = 1.6  # lado de cada face quadrada
TAB = 0.35  # profundidade das abas de cola


def texto_face(ax, x0, y0, letra_idx):
    ax.text(
        x0 + S / 2, y0 + S / 2, LETRAS[letra_idx],
        ha="center", va="center", fontsize=44, fontweight="bold",
    )
    ax.text(
        x0 + S / 2, y0 + 0.14, NOMES[letra_idx],
        ha="center", va="center", fontsize=10, style="italic",
    )


CORTE = dict(color="black", linewidth=1.8, linestyle="-", solid_capstyle="round")
DOBRA = dict(color="#444444", linewidth=1.4, linestyle=(0, (4, 3)))


def seg(ax, p, q, estilo):
    ax.plot([p[0], q[0]], [p[1], q[1]], **estilo)


def aba(ax, pontos):
    """Aba cinza clara: primeiro lado (pontos[0]->pontos[-1]) e a dobra (tracejada), o resto e corte (solido)."""
    ax.add_patch(Polygon(pontos, closed=True, facecolor="#d9d9d9", edgecolor="none", zorder=0))
    seg(ax, pontos[0], pontos[-1], DOBRA)
    for i in range(len(pontos) - 1):
        seg(ax, pontos[i], pontos[i + 1], CORTE)


def main():
    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.set_xlim(-1.0, 4 * S + 1.0)
    ax.set_ylim(-1.4, S + 1.6)
    ax.set_aspect("equal")
    ax.axis("off")

    W = 4 * S
    # 4 faces laterais em faixa horizontal
    for i in range(4):
        texto_face(ax, i * S, 0, i)

    # Linhas de dobra entre as faces (tracejadas)
    for i in range(1, 4):
        seg(ax, (i * S, 0), (i * S, S), DOBRA)

    # Bordas de cima e de baixo: corte (solido), exceto onde ha aba (dobra tracejada, desenhada pela aba)
    for i in range(4):
        x0 = i * S
        if i != 0:
            seg(ax, (x0, S), (x0 + S, S), CORTE)
        if i != 1:
            seg(ax, (x0, 0), (x0 + S, 0), CORTE)

    # Aba de cola na borda esquerda da primeira face e na borda direita da ultima (fecham o "tubo")
    aba(ax, [(0, S), (-TAB, S - TAB), (-TAB, TAB), (0, 0)])
    aba(ax, [(W, 0), (W + TAB, TAB), (W + TAB, S - TAB), (W, S)])
    # A borda esquerda da face 1 e a direita da face 4 sao as dobras das abas (ja desenhadas); a borda do tubo se fecha ali.

    # Aba de topo: triangulo saindo do topo da 1a face (ponta de cima, "handle")
    aba(ax, [(0, S), (S / 2, S + 0.9), (S, S)])
    ax.text(S / 2, S + 0.3, "fold up\n(handle)", ha="center", va="center", fontsize=9, color="#333333")

    # Aba de base: trapezio saindo da base da 2a face (ponta de baixo, "point")
    aba(ax, [(S, 0), (S + S * 0.25, -0.9), (S + S * 0.75, -0.9), (2 * S, 0)])
    ax.text(S + S / 2, -0.45, "fold down\n(point)", ha="center", va="center", fontsize=9, color="#333333")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=400, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    from PIL import Image
    im = Image.open(OUT_PNG).convert("RGB").rotate(90, expand=True)
    from PIL import ImageChops
    bbox = ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox()
    pad = 40
    im = im.crop((max(bbox[0]-pad,0), max(bbox[1]-pad,0), min(bbox[2]+pad, im.width), min(bbox[3]+pad, im.height)))
    im.save(OUT_PNG)

    gabarito = {
        "faces": [
            {"posicao": i, "inicial_latina": LETRAS[i], "nome": NOMES[i],
             "significado_fora_de_israel": SIGNIFICADOS[i]}
            for i in range(4)
        ],
        "nota_israel": (
            "Em Israel, a face Shin e substituida por Pei (Sham/'there' vira "
            "Po/'here'), porque o milagre aconteceu la. Variante regional, "
            "nao erro; ver revisao-religiosa.md."
        ),
        "verso_em_branco": True,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(gabarito, f, indent=2, ensure_ascii=False)

    print(f"[OK] Template salvo em {OUT_PNG}")
    print(f"[OK] Gabarito salvo em {OUT_JSON}")


if __name__ == "__main__":
    main()
