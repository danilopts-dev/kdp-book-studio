"""
gerar_cacapalavras_cozinha.py
Gera o caca-palavras 10x10 da Noite 6 (cozinha, tema latke), so
horizontal e vertical (sem diagonal, sem reverso), mesma logica de
gerar_cacapalavras.py (Noite 1), adaptada para a lista de palavras
desta noite. Verifica programaticamente que toda palavra esta de fato
na grade nas posicoes declaradas antes de aceitar o resultado.

Uso: python3 gerar_cacapalavras_cozinha.py
"""
import json
import random

from PIL import Image, ImageDraw, ImageFont

random.seed(613)

OUT_DIR = "/home/claude/n2fix/puzzle-assets"
TAMANHO = 10

# Palavras de cozinha ligadas ao latke, cabem em 10x10 so H/V (a mais
# longa, KITCHEN, tem 7 letras).
PALAVRAS = ["KITCHEN", "POTATO", "GOLDEN", "SPOON", "ONION",
            "PLATE", "LATKE", "PAN", "OIL", "FRY"]


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


MIN_POR_ORIENTACAO = 3  # mesma correcao aplicada em gerar_cacapalavras.py (Noite 1):
                        # forca mistura real H/V em vez de deixar o first-fit decidir


def gerar_grade(palavras, n, tentativas=5000):
    direcoes = [(0, 1), (1, 0)]  # horizontal, vertical (sem diagonal, sem reverso)
    ordenado = sorted(palavras, key=len, reverse=True)
    for _ in range(tentativas):
        grade = grade_vazia(n)
        gabarito = {}
        ok = True
        for i, palavra in enumerate(ordenado):
            preferida = direcoes[i % 2]
            outra = direcoes[(i + 1) % 2]
            colocado = False
            for dr, dc in (preferida, outra):
                candidatos = [(r, c) for r in range(n) for c in range(n)]
                random.shuffle(candidatos)
                for r, c in candidatos:
                    if cabe(grade, palavra, r, c, dr, dc):
                        gabarito[palavra] = colocar(grade, palavra, r, c, dr, dc)
                        colocado = True
                        break
                if colocado:
                    break
            if not colocado:
                ok = False
                break
        if not ok:
            continue
        n_h = sum(1 for pos in gabarito.values() if pos[1][0] == pos[0][0])
        n_v = sum(1 for pos in gabarito.values() if pos[1][1] == pos[0][1])
        if n_h < MIN_POR_ORIENTACAO or n_v < MIN_POR_ORIENTACAO:
            continue
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(n):
            for c in range(n):
                if grade[r][c] == "":
                    grade[r][c] = random.choice(letras)
        return grade, gabarito, n_h, n_v
    raise RuntimeError("Nao foi possivel encaixar todas as palavras com mistura H/V minima.")


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
        assert (dr, dc) in [(0, 1), (1, 0)], f"{palavra}: direcao invalida {dr, dc}"
        for i in range(1, len(posicoes)):
            r, c = posicoes[i]
            assert (r, c) == (r0 + dr * i, c0 + dc * i), f"{palavra}: passo nao consistente."
    print(f"[OK] Verificado: {len(palavras)} palavras presentes na grade, "
          f"todas horizontal ou vertical, sem diagonal.")


ESCALA_RESOLUCAO = 4  # mesma correcao de resolucao aplicada em gerar_cacapalavras.py


def desenhar(grade, gabarito, destacar, caminho_png, tamanho_celula=48, margem=50):
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
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26 * esc)
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
    grade, gabarito, n_h, n_v = gerar_grade(PALAVRAS, TAMANHO)
    verificar(grade, gabarito, PALAVRAS)
    print(f"[OK] Mistura real: {n_h} horizontais / {n_v} verticais.")

    desenhar(grade, gabarito, destacar=False, caminho_png=f"{OUT_DIR}/noite6_cacapalavras_cozinha.png")
    desenhar(grade, gabarito, destacar=True, caminho_png=f"{OUT_DIR}/noite6_cacapalavras_cozinha_gabarito.png")

    saida = {
        "grade": grade,
        "palavras": PALAVRAS,
        "gabarito_posicoes": gabarito,
        "regras": "somente horizontal e vertical, sem reverso, sem diagonal",
    }
    with open(f"{OUT_DIR}/noite6_cacapalavras_cozinha_gabarito.json", "w") as f:
        json.dump(saida, f, indent=2)

    print("Caca-palavras da cozinha (10x10) gerado, verificado e salvo com sucesso.")
