"""
montar_pdf_piloto.py
Monta o PDF do piloto da Noite 1: 8.5x11in, P&B, gutter 0.65in,
folio na mesma altura em todas as paginas, caixas de ilustracao
tracejadas e rotuladas, puzzles renderizados de verdade a partir dos
PNGs gerados por gerar_labirinto.py e gerar_cacapalavras.py.

Revisao (feedback do piloto): os rotulos de entrada/saida do labirinto
nao vem mais embutidos no PNG (que saiam pixelizados). Agora sao lidos
do gabarito JSON (abertura_entrada/abertura_saida) e desenhados como
texto vetorial do proprio PDF, posicionados ao lado da abertura real do
labirinto (nao mais fixos no topo da pagina, o que fazia o rotulo da
saida aparecer longe da porta de saida de verdade).

Uso: python3 montar_pdf_piloto.py
Saida: /mnt/user-data/outputs/piloto-noite-1.pdf
"""
import json

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, HexColor

PAGE_W, PAGE_H = 8.5 * inch, 11 * inch
GUTTER = 0.65 * inch          # margem interna (encadernacao)
OUTER = 0.5 * inch            # margem externa, folgada
TOP = 0.6 * inch
BOTTOM = 0.65 * inch
FOLIO_Y = 0.35 * inch         # altura fixa do folio em toda pagina

ASSETS = "/mnt/user-data/outputs/puzzle-assets"
OUT_PDF = "/mnt/user-data/outputs/piloto-noite-1.pdf"

GRAY = HexColor("#666666")


def margem_interna(pagina_par):
    """Retorna (esquerda, direita) considerando o gutter do lado da
    encadernacao. Paginas pares (verso): gutter na direita.
    Paginas impares (recto): gutter na esquerda."""
    if pagina_par:
        return OUTER, GUTTER
    return GUTTER, OUTER


def folio(c, numero, pagina_par):
    c.setFont("Helvetica", 9)
    c.setFillColor(GRAY)
    esq, dir_ = margem_interna(pagina_par)
    if pagina_par:
        c.drawString(esq, FOLIO_Y, str(numero))
    else:
        c.drawRightString(PAGE_W - dir_, FOLIO_Y, str(numero))
    c.setFillColor(black)


def running_head(c, texto, pagina_par):
    c.setFont("Helvetica", 7.5)
    c.setFillColor(GRAY)
    esq, dir_ = margem_interna(pagina_par)
    if pagina_par:
        c.drawString(esq, FOLIO_Y, "")  # verso: sem running head, so folio
    else:
        c.drawString(esq, FOLIO_Y, texto.upper())
    c.setFillColor(black)


def caixa_texto(pagina_par):
    esq, dir_ = margem_interna(pagina_par)
    x0 = esq
    x1 = PAGE_W - dir_
    y0 = BOTTOM
    y1 = PAGE_H - TOP
    return x0, y0, x1, y1


def caixa_ilustracao(c, x, y, w, h, rotulo, dimensao_pol):
    c.saveState()
    c.setDash(4, 3)
    c.setLineWidth(1.2)
    c.setStrokeColor(GRAY)
    c.rect(x, y, w, h, stroke=1, fill=0)
    c.setDash()
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Oblique", 9)
    texto1 = rotulo
    texto2 = f'{dimensao_pol}"'
    c.drawCentredString(x + w / 2, y + h / 2 + 6, texto1)
    c.drawCentredString(x + w / 2, y + h / 2 - 8, texto2)
    c.restoreState()


def titulo_pagina(c, texto, x0, y_topo, tamanho=20):
    c.setFont("Helvetica-Bold", tamanho)
    c.drawString(x0, y_topo, texto)
    return y_topo - tamanho * 1.4


def paragrafo(c, texto, x0, x1, y, tamanho=11, entrelinha=15, fonte="Helvetica"):
    from textwrap import wrap
    largura_chars = int((x1 - x0) / (tamanho * 0.52))
    c.setFont(fonte, tamanho)
    linhas = []
    for bloco in texto.split("\n"):
        if bloco.strip() == "":
            linhas.append("")
            continue
        linhas.extend(wrap(bloco, largura_chars) or [""])
    for linha in linhas:
        c.drawString(x0, y, linha)
        y -= entrelinha
    return y


def nova_pagina(c, numero, pagina_par, running_head_texto):
    if numero > 1:
        c.showPage()
    folio(c, numero, pagina_par)
    if not pagina_par:
        running_head(c, running_head_texto, pagina_par)
    return caixa_texto(pagina_par)


def desenhar_labirinto_com_rotulos(c, nome_base, x_centro_area, largura_area, y_topo,
                                    lado_maximo=380, gabarito=False):
    """Desenha o PNG do labirinto (ja limpo, sem texto embutido) e
    escreve os rotulos de entrada/saida como texto vetorial do PDF,
    posicionados junto a abertura real do labirinto (nao mais fixos no
    topo da pagina). nome_base e sempre o nome sem sufixo (ex.:
    "labirinto_facil"); gabarito=True usa a imagem com o caminho
    destacado, mas le o mesmo JSON de referencia."""
    with open(f"{ASSETS}/{nome_base}_gabarito.json") as f:
        info = json.load(f)

    lado = min(largura_area, lado_maximo)
    x_img = x_centro_area + (largura_area - lado) / 2
    y_img = y_topo - lado

    sufixo_png = "_gabarito.png" if gabarito else ".png"
    c.drawImage(f"{ASSETS}/{nome_base}{sufixo_png}", x_img, y_img,
                width=lado, height=lado, preserveAspectRatio=True)

    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(black)

    entrada = info["abertura_entrada"]
    saida = info["abertura_saida"]

    # entrada abre sempre no lado esquerdo (W): rotulo a esquerda da
    # imagem, alinhado a direita, na altura E na posicao x exatas da
    # abertura real (x_rel/y_rel ja incluem a margem interna do PNG,
    # entao a linha conectora encosta exatamente na parede aberta)
    x_entrada = x_img + lado * entrada["x_rel"]
    y_entrada = y_img + lado * (1 - entrada["y_rel"])
    c.drawRightString(x_entrada - 6, y_entrada - 3, info["rotulo_inicio"])
    c.saveState()
    c.setLineWidth(1)
    c.line(x_entrada - 4, y_entrada, x_entrada, y_entrada)
    c.restoreState()

    # saida abre sempre no lado direito (E): rotulo a direita da
    # imagem, alinhado a esquerda, na altura e posicao x exatas da abertura
    x_saida = x_img + lado * saida["x_rel"]
    y_saida = y_img + lado * (1 - saida["y_rel"])
    c.drawString(x_saida + 6, y_saida - 3, info["rotulo_fim"])
    c.saveState()
    c.setLineWidth(1)
    c.line(x_saida, y_saida, x_saida + 4, y_saida)
    c.restoreState()

    return y_img


def main():
    c = canvas.Canvas(OUT_PDF, pagesize=(PAGE_W, PAGE_H))
    pagina = 1
    RH = "Night 1: Judah Says No"

    # PAGINA 1 (recto, impar): Tonight's Story
    par = (pagina % 2 == 0)
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "NIGHT 1: Judah Says No", x0, y1 - 10, 22)
    y -= 6
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x0, y, "Tonight's Story")
    y -= 20
    historia = (
        "A long time ago, a king named Antiochus ruled over the land of Judea. "
        "He wanted everyone in his kingdom to worship the same way he did, and "
        "he made a law: no more Shabbat candles, no more Torah, no more "
        "speaking Hebrew in the streets. For the Jewish people, that was "
        "impossible to accept.\n\n"
        "In a small town called Modiin lived an old man named Mattathias and "
        "his five sons. When the king's soldiers came asking him to break the "
        "law in public, Mattathias said no, and he meant it. He and his sons "
        "grabbed their tools, turned the soldiers away, and ran for the hills "
        "before the king could send more.\n\n"
        "Up in the hills of Judea, they were cold, they were outnumbered, and "
        "they were free. That was where the fight for Hanukkah began, one "
        "family, one no, one mountain at a time."
    )
    y = paragrafo(c, historia, x0, x1, y, tamanho=11.5, entrelinha=16)
    y -= 10
    caixa_ilustracao(c, x0, y - 190, x1 - x0, 190,
                      "ILUSTRACAO 1.1 - ver lista-ilustracoes.md",
                      f'{(x1 - x0) / inch:.2f} x 2.6')
    pagina += 1

    # PAGINA 2 (verso, par): What's a Maccabee + inicio labirinto facil
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "What's a Maccabee?", x0, y1 - 10, 16)
    caixa = (
        "Mattathias's sons and the fighters who joined them were called the "
        "Maccabees. Some say the name comes from a Hebrew word for \"hammer,\" "
        "because that's exactly how they fought: small, fast, and impossible "
        "to ignore."
    )
    c.saveState()
    c.setStrokeColor(GRAY)
    c.setLineWidth(1)
    box_h = 70
    c.rect(x0, y - box_h, x1 - x0, box_h)
    c.restoreState()
    paragrafo(c, caixa, x0 + 10, x1 - 10, y - 16, tamanho=10.5, entrelinha=14)
    y -= box_h + 30

    caixa_ilustracao(c, x0, y - 150, x1 - x0, 150,
                      "ILUSTRACAO 1.2 - hanukkiah simples, ver lista",
                      f'{(x1 - x0) / inch:.2f} x 2.1')
    pagina += 1

    # PAGINA 3 (recto): labirinto facil
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "★ Escape to the Hills", x0, y1 - 10, 16)
    instrucao = ("Help Mattathias and his sons escape the soldiers and reach the "
                 "safety of the hills! Start at MODIIN and find your way through "
                 "the maze to THE HILLS.")
    y = paragrafo(c, instrucao, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 14
    desenhar_labirinto_com_rotulos(c, "labirinto_facil", x0, x1 - x0, y, lado_maximo=380)
    pagina += 1

    # PAGINA 4 (verso): caca-palavras
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "★ Word Hunt: Night 1", x0, y1 - 10, 16)
    instrucao = ("These names and words are hiding in the grid below. Can you "
                 "find all ten? Some go across, some go up and down, no sneaky "
                 "diagonals tonight.")
    y = paragrafo(c, instrucao, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 6
    lista = "JUDAH · MACCABEE · ANTIOCHUS · MATTATHIAS · TEMPLE · HILLS · TORAH · FAITH · COURAGE · MODIIN"
    c.setFont("Helvetica-Oblique", 9.5)
    y = paragrafo(c, lista, x0, x1, y, tamanho=9.5, entrelinha=13, fonte="Helvetica-Oblique")
    y -= 10
    largura_puzzle = min(x1 - x0, 340)
    c.drawImage(f"{ASSETS}/cacapalavras_noite1.png", x0 + (x1 - x0 - largura_puzzle) / 2,
                y - largura_puzzle, width=largura_puzzle, height=largura_puzzle,
                preserveAspectRatio=True)
    pagina += 1

    # PAGINA 5 (recto): labirinto medio
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "★★ Back to Modiin (the hard way)", x0, y1 - 10, 15)
    instrucao = ("This trail has more twists. Start where the family hides in the "
                 "hills and find the one true path back down to warn the next "
                 "village. Watch out for the dead ends!")
    y = paragrafo(c, instrucao, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 14
    desenhar_labirinto_com_rotulos(c, "labirinto_medio", x0, x1 - x0, y, lado_maximo=380)
    pagina += 1

    # PAGINA 6 (verso): Why is Judah called the Hammer + desenho
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "★★ Why Is Judah Called the Hammer?", x0, y1 - 10, 14)
    texto = (
        "Judah, one of Mattathias's sons, led the fighters after his father. "
        "People called him Judah Maccabee, Judah \"the Hammer,\" because he hit "
        "hard and moved fast, and his small army kept winning battles nobody "
        "expected them to win.\n\n"
        "Finish the drawing below: give Judah his hammer, his shield, and a "
        "look on his face that says he is not backing down."
    )
    y = paragrafo(c, texto, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 10
    caixa_ilustracao(c, x0, y - 240, x1 - x0, 240,
                      "ILUSTRACAO 1.3 - Judah, metade a completar",
                      f'{(x1 - x0) / inch:.2f} x 3.3')
    pagina += 1

    # PAGINA 7 (recto): Before the Candles - piada + bencao 1
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "Before the Candles", x0, y1 - 10, 18)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x0, y, "Tonight's Joke")
    y -= 16
    piada = ("Why did Mattathias bring his whole toolbox to Modiin? Because "
              "when the king's soldiers showed up, he knew exactly how to make "
              "a point!")
    y = paragrafo(c, piada, x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 16
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x0, y, "The First Blessing")
    y -= 16
    intro = ("Before you light the candles tonight, say this blessing "
              "together. It thanks God for the mitzvah of lighting the "
              "Hanukkah candles.")
    y = paragrafo(c, intro, x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 8
    c.setFont("Helvetica-Oblique", 10.5)
    y = paragrafo(c,
                  "Baruch atah Adonai, Eloheinu melech ha'olam, asher "
                  "kid'shanu b'mitzvotav v'tzivanu l'hadlik ner shel "
                  "Chanukah.",
                  x0, x1, y, tamanho=10.5, entrelinha=14, fonte="Helvetica-Oblique")
    y -= 4
    y = paragrafo(c,
                  "Blessed are You, our God, Ruler of the universe, who made "
                  "us holy with commandments and commanded us to light the "
                  "Hanukkah candles.",
                  x0, x1, y, tamanho=10, entrelinha=13)
    pagina += 1

    # PAGINA 8 (verso): Shehecheyanu
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "Only on Night 1: the Shehecheyanu", x0, y1 - 10, 15)
    intro = ("Tonight only, add one more blessing, the Shehecheyanu. It's said "
              "the first time you do something in a new year, so light number "
              "one gets its own special thank-you.")
    y = paragrafo(c, intro, x0, x1, y - 4, tamanho=10.5, entrelinha=14)
    y -= 8
    y = paragrafo(c,
                  "Baruch atah Adonai, Eloheinu melech ha'olam, shehecheyanu "
                  "v'kiy'manu v'higianu laz'man hazeh.",
                  x0, x1, y, tamanho=10.5, entrelinha=14, fonte="Helvetica-Oblique")
    y -= 4
    y = paragrafo(c,
                  "Blessed are You, our God, Ruler of the universe, who has "
                  "kept us alive, sustained us, and brought us to this season.",
                  x0, x1, y, tamanho=10, entrelinha=13)
    y -= 20
    caixa_ilustracao(c, x0, y - 160, x1 - x0, 160,
                      "ILUSTRACAO 1.4 - familia acendendo a 1a vela",
                      f'{(x1 - x0) / inch:.2f} x 2.2')
    pagina += 1

    # PAGINAS 9-10: gabaritos deste piloto (labirintos + caca-palavras)
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "Answer Key: Night 1 (pilot)", x0, y1 - 10, 16)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x0, y, "Escape to the Hills")
    y -= 14
    metade = (x1 - x0 - 20) / 2
    y_topo_gabarito = y
    desenhar_labirinto_com_rotulos(c, "labirinto_facil", x0, metade,
                                    y_topo_gabarito, lado_maximo=220, gabarito=True)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x0 + metade + 20, y, "Back to Modiin")
    desenhar_labirinto_com_rotulos(c, "labirinto_medio", x0 + metade + 20, metade,
                                    y_topo_gabarito - 14, lado_maximo=220, gabarito=True)
    pagina += 1

    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par, RH)
    y = titulo_pagina(c, "Answer Key: Word Hunt", x0, y1 - 10, 16)
    largura_puzzle = min(x1 - x0, 340)
    c.drawImage(f"{ASSETS}/cacapalavras_noite1_gabarito.png",
                x0 + (x1 - x0 - largura_puzzle) / 2,
                y - largura_puzzle, width=largura_puzzle, height=largura_puzzle,
                preserveAspectRatio=True)
    pagina += 1

    c.save()
    print(f"[OK] PDF gerado: {OUT_PDF}, {pagina - 1} paginas.")


if __name__ == "__main__":
    main()
