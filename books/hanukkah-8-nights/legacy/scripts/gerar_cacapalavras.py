"""
gerar_cacapalavras.py
Gera o caca-palavras 10x10 da Noite 1, so horizontal e vertical (sem
diagonal, sem reverso, conforme TOC e regua para a faixa 6-7 anos).

Correcao (revisao do piloto, pos-aprovacao do Danilo): a versao anterior
deste script permitia H/V, mas o algoritmo de encaixe (first-fit sobre
lista shuffled) resultou, por azar do seed fixo, em 10 de 10 palavras
saindo horizontais - o que na pratica tornava o puzzle so-horizontal e
facil demais. Este script agora FORCA mistura real: cada palavra tenta
primeiro uma direcao preferida que alterna H/V pela ordem de colocacao,
e so cai para a outra direcao se a preferida nao couber. Ao final, exige
por verificacao programatica pelo menos 3 palavras em cada orientacao
(H e V) antes de aceitar a grade; caso contrario descarta e tenta de novo.

Verifica programaticamente que toda palavra da lista esta de fato na
grade nas posicoes declaradas antes de aceitar o resultado, e salva
grade + imagem + gabarito (posicoes) em JSON e PNG.

Uso: python3 gerar_cacapalavras.py
"""
import json
import random

from PIL import Image, ImageDraw, ImageFont

random.seed(13)

OUT_DIR = "/mnt/user-data/outputs/puzzle-assets"
TAMANHO = 10
MIN_POR_ORIENTACAO = 3  # minimo de palavras H e minimo de palavras V exigido

# Lista ajustada para caber em 10x10 so H/V: a palavra mais longa nao
# pode passar de 10 letras. ANTIOCHUS (9) e MATTATHIAS (10) cabem por
# um triz na horizontal/vertical de uma grade 10x10.
PALAVRAS = ["JUDAH", "MACCABEE", "ANTIOCHUS", "MATTATHIAS", "TEMPLE",
            "HILLS", "TORAH", "FAITH", "COURAGE", "MODIIN"]

HORIZONTAL = (0, 1)
VERTICAL = (1, 0)


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


def gerar_grade(palavras, n, tentativas=5000):
    ordenado = sorted(palavras, key=len, reverse=True)
    for tentativa in range(tentativas):
        grade = grade_vazia(n)
        gabarito = {}
        ok = True
        for i, palavra in enumerate(ordenado):
            # alterna a direcao preferida por posicao na lista, para nao
            # deixar o first-fit decidir tudo por acaso (bug corrigido)
            preferida = HORIZONTAL if i % 2 == 0 else VERTICAL
            outra = VERTICAL if preferida == HORIZONTAL else HORIZONTAL
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

        # exige mistura real de orientacoes antes de aceitar a grade
        n_h = sum(1 for pos in gabarito.values() if pos[1][0] == pos[0][0])
        n_v = sum(1 for pos in gabarito.values() if pos[1][1] == pos[0][1])
        if n_h < MIN_POR_ORIENTACAO or n_v < MIN_POR_ORIENTACAO:
            continue

        # preenche o resto com letras aleatorias
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(n):
            for c in range(n):
                if grade[r][c] == "":
                    grade[r][c] = random.choice(letras)
        return grade, gabarito, n_h, n_v
    raise RuntimeError(
        "Nao foi possivel encaixar todas as palavras com mistura H/V "
        "minima exigida.")


def verificar(grade, gabarito, palavras):
    """Verificacao programatica: confirma que cada palavra da lista
    esta realmente presente na grade nas posicoes declaradas, letra a
    letra, que nenhuma palavra da lista ficou de fora, e que a mistura
    de orientacoes H/V atende ao minimo exigido."""
    assert set(gabarito.keys()) == set(palavras), "Gabarito nao cobre todas as palavras."
    n_h = n_v = 0
    for palavra, posicoes in gabarito.items():
        assert len(posicoes) == len(palavra), f"{palavra}: numero de posicoes nao bate."
        for (r, c), letra_esperada in zip(posicoes, palavra):
            assert grade[r][c] == letra_esperada, (
                f"{palavra}: grade[{r}][{c}]={grade[r][c]!r} != {letra_esperada!r}"
            )
        # confirma direcao estritamente H ou V (sem diagonal)
        r0, c0 = posicoes[0]
        r1, c1 = posicoes[1]
        dr, dc = r1 - r0, c1 - c0
        assert (dr, dc) in [(0, 1), (1, 0)], f"{palavra}: direcao invalida {dr, dc}"
        if (dr, dc) == (0, 1):
            n_h += 1
        else:
            n_v += 1
        for i in range(1, len(posicoes)):
            r, c = posicoes[i]
            assert (r, c) == (r0 + dr * i, c0 + dc * i), f"{palavra}: passo nao consistente."
    assert n_h >= MIN_POR_ORIENTACAO, f"So {n_h} palavras horizontais, minimo {MIN_POR_ORIENTACAO}."
    assert n_v >= MIN_POR_ORIENTACAO, f"So {n_v} palavras verticais, minimo {MIN_POR_ORIENTACAO}."
    print(f"[OK] Verificado: {len(palavras)} palavras presentes na grade, "
          f"todas horizontal ou vertical, sem diagonal. Mistura real: "
          f"{n_h} horizontais / {n_v} verticais.")


ESCALA_RESOLUCAO = 4  # ver nota na docstring de desenhar()


def desenhar(grade, gabarito, destacar, caminho_png, tamanho_celula=48, margem=50):
    """Correcao (pixelizacao reportada no piloto): a imagem antiga tinha
    so 48px por celula e fonte de 26px, resolucao baixa demais para o
    tamanho em que o puzzle e exibido na pagina (ate 340pt, ~1.4x maior
    que a imagem fonte a 300dpi), o que deixava letras e linhas
    borradas/serrilhadas ao ampliar. Agora tudo e desenhado em escala 4x
    (celula, margem, fonte e espessura de linha) e a imagem e salva
    nessa resolucao mais alta, sem reduzir depois: o PDF (reportlab)
    escala para baixo ao encaixar na pagina, o que sempre da resultado
    mais nitido do que escalar uma imagem pequena para cima."""
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

    desenhar(grade, gabarito, destacar=False, caminho_png=f"{OUT_DIR}/cacapalavras_noite1.png")
    desenhar(grade, gabarito, destacar=True, caminho_png=f"{OUT_DIR}/cacapalavras_noite1_gabarito.png")

    saida = {
        "grade": grade,
        "palavras": PALAVRAS,
        "gabarito_posicoes": gabarito,
        "regras": "somente horizontal e vertical, sem reverso, sem diagonal, mistura garantida",
        "n_horizontais": n_h,
        "n_verticais": n_v,
    }
    with open(f"{OUT_DIR}/cacapalavras_noite1_gabarito.json", "w") as f:
        json.dump(saida, f, indent=2)

    print("Caca-palavras gerado, verificado e salvo com sucesso.")
