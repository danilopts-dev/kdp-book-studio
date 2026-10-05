"""
gerar_jarro_diferente.py
Gera o puzzle "Which jar is different?" da Noite 3 (nivel uma-estrela):
uma grade de jarros de oleo desenhados por codigo, todos identicos, exceto
um com uma diferenca geometrica clara (o padrao gravado no corpo do jarro).

Verificacao programatica antes de salvar: a grade descreve cada jarro por
uma assinatura (padrao + numero de tracos), e o script confirma que
exatamente 1 jarro tem assinatura diferente dos demais (que sao todos
identicos entre si).

Uso: python3 gerar_jarro_diferente.py
Saida: /mnt/user-data/outputs/puzzle-assets/noite3_jarro_diferente.png
       /mnt/user-data/outputs/puzzle-assets/noite3_jarro_diferente_gabarito.png
       /mnt/user-data/outputs/puzzle-assets/noite3_jarro_diferente_gabarito.json
"""
import json
import random

from PIL import Image, ImageDraw

random.seed(13)

OUT_DIR = "/mnt/user-data/outputs/puzzle-assets"

LINHAS, COLUNAS = 2, 4  # 8 jarros no total
CELULA = 130
MARGEM = 24

PADRAO_COMUM = "linhas_retas"   # padrao de todos os jarros "iguais"
PADRAO_DIFERENTE = "bolinhas"   # padrao do unico jarro diferente


def desenhar_jarro(draw, cx, cy, tam, padrao, circulado=False):
    """Desenha um jarro de oleo: corpo oval, gargalo, tampa, e um padrao
    gravado no corpo (linhas retas ou bolinhas) que e o unico elemento
    que muda entre os jarros."""
    s = tam / 2
    cor = (20, 20, 20)
    lw = max(2, int(tam * 0.045))

    corpo_w, corpo_h = s * 1.3, s * 1.15
    corpo_top = cy - corpo_h / 2 + s * 0.3
    corpo_bottom = cy + corpo_h / 2 + s * 0.3
    draw.ellipse([cx - corpo_w / 2, corpo_top, cx + corpo_w / 2, corpo_bottom],
                 outline=cor, width=lw)

    draw.rectangle([cx - s * 0.24, cy - s * 0.95, cx + s * 0.24, corpo_top + s * 0.1],
                    outline=cor, width=lw)
    draw.rectangle([cx - s * 0.36, cy - s * 1.1, cx + s * 0.36, cy - s * 0.92],
                    outline=cor, width=lw)

    # padrao gravado no corpo (o unico ponto que difere entre os jarros)
    if padrao == "linhas_retas":
        for i in range(-1, 2):
            x = cx + i * s * 0.28
            draw.line([x, corpo_top + s * 0.22, x, corpo_bottom - s * 0.18],
                       fill=cor, width=max(2, lw - 1))
    elif padrao == "bolinhas":
        for i in range(-1, 2):
            x = cx + i * s * 0.3
            y = cy + s * 0.15
            r = s * 0.09
            draw.ellipse([x - r, y - r, x + r, y + r], outline=cor, width=max(2, lw - 1))
    else:
        raise ValueError(f"padrao desconhecido: {padrao}")

    if circulado:
        raio = tam * 0.62
        draw.ellipse([cx - raio, cy - raio, cx + raio, cy + raio],
                     outline=(200, 30, 30), width=4)


def montar_grade():
    total = LINHAS * COLUNAS
    indice_diferente = random.randrange(total)
    grade = []
    for i in range(total):
        grade.append(PADRAO_DIFERENTE if i == indice_diferente else PADRAO_COMUM)
    return grade, indice_diferente


def verificar_exatamente_um_diferente(grade):
    contagem = {}
    for padrao in grade:
        contagem[padrao] = contagem.get(padrao, 0) + 1
    # exatamente um padrao deve ter contagem 1, e os demais devem ser todos
    # do mesmo padrao majoritario
    padroes_unicos = [p for p, n in contagem.items() if n == 1]
    return len(contagem) == 2 and len(padroes_unicos) == 1


def renderizar(grade, indice_diferente, caminho, revelar=False):
    largura = COLUNAS * CELULA + MARGEM * 2
    altura = LINHAS * CELULA + MARGEM * 2
    img = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(img)

    for i, padrao in enumerate(grade):
        r, c = divmod(i, COLUNAS)
        cx = MARGEM + c * CELULA + CELULA / 2
        cy = MARGEM + r * CELULA + CELULA / 2
        circulado = revelar and i == indice_diferente
        desenhar_jarro(draw, cx, cy, CELULA * 0.8, padrao, circulado=circulado)

    img.save(caminho)


def main():
    grade, indice_diferente = montar_grade()
    assert verificar_exatamente_um_diferente(grade), "grade nao tem exatamente 1 jarro diferente"

    caminho_puzzle = f"{OUT_DIR}/noite3_jarro_diferente.png"
    caminho_gabarito_png = f"{OUT_DIR}/noite3_jarro_diferente_gabarito.png"
    caminho_gabarito_json = f"{OUT_DIR}/noite3_jarro_diferente_gabarito.json"

    renderizar(grade, indice_diferente, caminho_puzzle, revelar=False)
    renderizar(grade, indice_diferente, caminho_gabarito_png, revelar=True)

    linha, coluna = divmod(indice_diferente, COLUNAS)
    with open(caminho_gabarito_json, "w") as f:
        json.dump({
            "linhas": LINHAS,
            "colunas": COLUNAS,
            "indice_0_based": indice_diferente,
            "posicao_linha_coluna_1_based": [linha + 1, coluna + 1],
            "padrao_comum": PADRAO_COMUM,
            "padrao_diferente": PADRAO_DIFERENTE,
        }, f, indent=2)

    print(f"[OK] noite3_jarro_diferente: {LINHAS}x{COLUNAS} jarros, "
          f"1 diferente na posicao (linha {linha + 1}, coluna {coluna + 1}), "
          f"verificado.")


if __name__ == "__main__":
    main()
