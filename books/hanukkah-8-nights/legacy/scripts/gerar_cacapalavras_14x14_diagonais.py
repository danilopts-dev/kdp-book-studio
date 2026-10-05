"""
gerar_cacapalavras_14x14_diagonais.py
Gera o caca-palavras 14x14 da Noite 6 (nivel Star-Star), com palavras
de cozinha/Hanuca mais desafiadoras e permitindo as 8 direcoes
(horizontal, vertical e diagonal, com reverso), regra extra que torna
esta atividade mensuravelmente mais dificil que o caca-palavras 10x10
so H/V da mesma noite (grade maior + regra extra, conforme regua 4).

Verifica programaticamente que toda palavra esta de fato na grade nas
posicoes declaradas, em qualquer uma das 8 direcoes, antes de aceitar
o resultado.

Uso: python3 gerar_cacapalavras_14x14_diagonais.py
"""
import json
import random

from PIL import Image, ImageDraw, ImageFont

random.seed(1214)

OUT_DIR = "/home/claude/n2fix/puzzle-assets"
TAMANHO = 14

# Vocabulario mais amplo e mais dificil de cozinha/Hanuca (a mais
# longa, SUFGANIYAH, tem 10 letras, cabe com folga em 14x14).
PALAVRAS = ["SUFGANIYAH", "DOUGHNUT", "TRADITION", "GRIDDLE",
            "PLATTER", "CRISPY", "SIZZLE", "FAMILY", "JELLY", "GRATER"]

DIRECOES_8 = [(0, 1), (1, 0), (0, -1), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


def grade_vazia(n):
    return [["" for _ in range(n)] for _ in range(n)]


def cabe(grade, palavra, linha, col, dr, dc):
    n = len(grade)
    for i, letra in enumerate(palavra):
        r, c = linha + dr * i, col + dc * i
        if not (0 <= r < n and 0 <= c < n):
            return False
        atual = grade[r][c]
        if atual != "" and atual != letra:
            return False
    return True


def colocar(grade, palavra, linha, col, dr, dc):
    posicoes = []
    for i, letra in enumerate(palavra):
        r, c = linha + dr * i, col + dc * i
        grade[r][c] = letra
        posicoes.append([r, c])
    return posicoes


def gerar_grade(palavras, n, tentativas=3000):
    for _ in range(tentativas):
        grade = grade_vazia(n)
        gabarito = {}
        ordenado = sorted(palavras, key=len, reverse=True)
        ok = True
        for palavra in ordenado:
            colocado = False
            candidatos = [(r, c, dr, dc)
                          for dr, dc in DIRECOES_8
                          for r in range(n) for c in range(n)]
            random.shuffle(candidatos)
            for r, c, dr, dc in candidatos:
                if cabe(grade, palavra, r, c, dr, dc):
                    gabarito[palavra] = colocar(grade, palavra, r, c, dr, dc)
                    colocado = True
                    break
            if not colocado:
                ok = False
                break
        if ok:
            letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for r in range(n):
                for c in range(n):
                    if grade[r][c] == "":
                        grade[r][c] = random.choice(letras)
            return grade, gabarito
    raise RuntimeError("Nao foi possivel encaixar todas as palavras.")


def verificar(grade, gabarito, palavras):
    assert set(gabarito.keys()) == set(palavras), "Gabarito nao cobre todas as palavras."
    for palavra, posicoes in gabarito.items():
        assert len(posicoes) == len(palavra), f"{palavra}: numero de posicoes nao bate."
        for (r, c), letra_esperada in zip(posicoes, palavra):
            assert grade[r][c] == letra_esperada, (
                f"{palavra}: grade[{r}][{c}]={grade[r][c]!r} != {letra_esperada!r}"
            )
        r0, c0 = posicoes[0]
        r1, c1 = posicoes[1]
        dr, dc = r1 - r0, c1 - c0
        assert (dr, dc) in DIRECOES_8, f"{palavra}: direcao invalida {dr, dc}"
        for i in range(1, len(posicoes)):
            r, c = posicoes[i]
            assert (r, c) == (r0 + dr * i, c0 + dc * i), f"{palavra}: passo nao consistente."
    print(f"[OK] Verificado: {len(palavras)} palavras presentes na grade 14x14, "
          f"horizontal, vertical ou diagonal, com reverso permitido.")


ESCALA_RESOLUCAO = 4  # mesma correcao de resolucao aplicada em gerar_cacapalavras.py


def desenhar(grade, gabarito, destacar, caminho_png, tamanho_celula=36, margem=46):
    esc = ESCALA_RESOLUCAO
    tamanho_celula *= esc
    margem *= esc
    espessura_linha = 2 * esc

    n = len(grade)
    W = n * tamanho_celula + margem * 2
    H = n * tamanho_celula + margem * 2
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    try:
        fonte = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 19 * esc)
    except OSError:
        fonte = ImageFont.load_default()

    if destacar:
        for palavra, posicoes in gabarito.items():
            for (r, c) in posicoes:
                x0 = margem + c * tamanho_celula
                y0 = margem + r * tamanho_celula
                draw.rectangle([x0, y0, x0 + tamanho_celula, y0 + tamanho_celula],
                                fill=(255, 235, 150))

    for r in range(n + 1):
        y = margem + r * tamanho_celula
        draw.line([(margem, y), (margem + n * tamanho_celula, y)], fill="black", width=espessura_linha)
    for c in range(n + 1):
        x = margem + c * tamanho_celula
        draw.line([(x, margem), (x, margem + n * tamanho_celula)], fill="black", width=espessura_linha)

    for r in range(n):
        for c in range(n):
            letra = grade[r][c]
            x = margem + c * tamanho_celula + tamanho_celula / 2
            y = margem + r * tamanho_celula + tamanho_celula / 2
            bbox = draw.textbbox((0, 0), letra, font=fonte)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw.text((x - tw / 2, y - th / 2 - bbox[1]), letra, fill="black", font=fonte)

    img.save(caminho_png)


if __name__ == "__main__":
    grade, gabarito = gerar_grade(PALAVRAS, TAMANHO)
    verificar(grade, gabarito, PALAVRAS)

    desenhar(grade, gabarito, destacar=False, caminho_png=f"{OUT_DIR}/noite6_cacapalavras_14x14.png")
    desenhar(grade, gabarito, destacar=True, caminho_png=f"{OUT_DIR}/noite6_cacapalavras_14x14_gabarito.png")

    saida = {
        "grade": grade,
        "palavras": PALAVRAS,
        "gabarito_posicoes": gabarito,
        "regras": "horizontal, vertical ou diagonal, com reverso permitido (8 direcoes)",
    }
    with open(f"{OUT_DIR}/noite6_cacapalavras_14x14_gabarito.json", "w") as f:
        json.dump(saida, f, indent=2)

    print("Caca-palavras 14x14 com diagonais gerado, verificado e salvo com sucesso.")
