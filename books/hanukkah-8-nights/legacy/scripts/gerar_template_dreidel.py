"""
gerar_template_dreidel.py
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

OUT_PNG = "/mnt/user-data/outputs/puzzle-assets/noite5_template_dreidel.png"
OUT_JSON = "/mnt/user-data/outputs/puzzle-assets/noite5_template_dreidel_gabarito.json"

# Letras hebraicas das 4 faces, na ordem tradicional (fora de Israel).
LETRAS = ["נ", "ג", "ה", "ש"]  # Nun, Gimel, Hei, Shin
NOMES = ["Nun", "Gimel", "Hei", "Shin"]
SIGNIFICADOS = ["Nes (a miracle)", "Gadol (great)", "Haya (happened)", "Sham (there)"]

S = 1.6  # lado de cada face quadrada
TAB = 0.35  # profundidade das abas de cola


def face_quadrada(ax, x0, y0, letra_idx):
    quad = Polygon(
        [(x0, y0), (x0 + S, y0), (x0 + S, y0 + S), (x0, y0 + S)],
        closed=True, fill=False, edgecolor="black", linewidth=1.6,
    )
    ax.add_patch(quad)
    ax.text(
        x0 + S / 2, y0 + S / 2, LETRAS[letra_idx],
        ha="center", va="center", fontsize=34, fontweight="bold",
    )
    ax.text(
        x0 + S / 2, y0 + 0.14, NOMES[letra_idx],
        ha="center", va="center", fontsize=7.5, style="italic",
    )


def aba_cola(ax, pontos):
    tab = Polygon(pontos, closed=True, fill=False, edgecolor="gray",
                   linewidth=1.0, linestyle=(0, (4, 3)))
    ax.add_patch(tab)


def main():
    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.set_xlim(-1.0, 4 * S + 1.0)
    ax.set_ylim(-1.4, S + 1.6)
    ax.set_aspect("equal")
    ax.axis("off")

    # 4 faces laterais em faixa horizontal
    for i in range(4):
        x0 = i * S
        face_quadrada(ax, x0, 0, i)

    # Aba de cola na borda esquerda da primeira face (para fechar o "tubo")
    x0 = 0
    aba_cola(ax, [(x0, 0), (x0 - TAB, TAB), (x0 - TAB, S - TAB), (x0, S)])

    # Aba de cola na borda direita da ultima face
    x0 = 4 * S
    aba_cola(ax, [(x0, 0), (x0 + TAB, TAB), (x0 + TAB, S - TAB), (x0, S)])

    # Aba de topo: triangulo saindo do topo da 1a face, para formar a ponta do dreidel (sevivon)
    x0 = 0
    topo = Polygon(
        [(x0, S), (x0 + S, S), (x0 + S / 2, S + 0.9)],
        closed=True, fill=False, edgecolor="gray", linewidth=1.0,
        linestyle=(0, (4, 3)),
    )
    ax.add_patch(topo)
    ax.text(x0 + S / 2, S + 0.35, "fold up\n(handle)", ha="center", va="center",
            fontsize=6.5, color="gray")

    # Aba de base: trapezio saindo da base da 2a face, para fechar o fundo (ponta do peao)
    x0 = 1 * S
    base = Polygon(
        [(x0, 0), (x0 + S, 0), (x0 + S * 0.75, -0.9), (x0 + S * 0.25, -0.9)],
        closed=True, fill=False, edgecolor="gray", linewidth=1.0,
        linestyle=(0, (4, 3)),
    )
    ax.add_patch(base)
    ax.text(x0 + S / 2, -0.45, "fold down\n(point)", ha="center", va="center",
            fontsize=6.5, color="gray")

    ax.text(
        4 * S / 2, S + 1.35,
        "DESIGN A DREIDEL — cut along the solid lines, fold along the dashed lines,\n"
        "glue the gray tabs, color each face, then spin!",
        ha="center", va="center", fontsize=9,
    )

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=200, bbox_inches="tight")
    plt.close(fig)

    gabarito = {
        "faces": [
            {"posicao": i, "letra_hebraica": LETRAS[i], "nome": NOMES[i],
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
