"""
montar_answer_key.py
Monta a secao "Answer Key" do livro inteiro (8 noites), 8.5x11in, P&B,
gutter 0.65in, folio na mesma altura em todas as paginas, seguindo o
mesmo padrao visual de montar_pdf_piloto.py (Noite 1).

Nao redigita nenhuma resposta a mao: todo numero/resposta usado aqui vem
de um arquivo ja verificado por script (puzzle-assets/*_gabarito.json,
*_problemas*.json) ou do proprio manuscrito ja aprovado (noite-N-texto.md),
que por sua vez ja tem cada resposta conferida por
scripts/verificar_quiz_noite8.py, scripts/verificar_conta_velas_noite4.py
e scripts/verificar_puzzle_logica_noite3.py.

Uso: python3 montar_answer_key.py
Saida: /mnt/user-data/outputs/answer-key.pdf
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, HexColor
from textwrap import wrap

PAGE_W, PAGE_H = 8.5 * inch, 11 * inch
GUTTER = 0.65 * inch
OUTER = 0.5 * inch
TOP = 0.6 * inch
BOTTOM = 0.65 * inch
FOLIO_Y = 0.35 * inch

ASSETS = "/tmp/assets"
OUT_PDF = "/mnt/user-data/outputs/answer-key.pdf"

GRAY = HexColor("#666666")
RH = "Answer Key"


def margem_interna(pagina_par):
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
    if not pagina_par:
        c.drawString(esq, FOLIO_Y, texto.upper())
    c.setFillColor(black)


def caixa_texto(pagina_par):
    esq, dir_ = margem_interna(pagina_par)
    return esq, BOTTOM, PAGE_W - dir_, PAGE_H - TOP


def nova_pagina(c, numero, pagina_par):
    if numero > 1:
        c.showPage()
    folio(c, numero, pagina_par)
    if not pagina_par:
        running_head(c, RH, pagina_par)
    return caixa_texto(pagina_par)


def titulo_pagina(c, texto, x0, y_topo, tamanho=18):
    c.setFont("Helvetica-Bold", tamanho)
    c.drawString(x0, y_topo, texto)
    return y_topo - tamanho * 1.4


def subtitulo(c, texto, x0, y, tamanho=11.5):
    c.setFont("Helvetica-Bold", tamanho)
    c.drawString(x0, y, texto)
    return y - tamanho * 1.5


def paragrafo(c, texto, x0, x1, y, tamanho=10.5, entrelinha=14, fonte="Helvetica"):
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


def imagem_centralizada(c, caminho, x0, x1, y_topo, lado_maximo):
    largura = min(x1 - x0, lado_maximo)
    x = x0 + (x1 - x0 - largura) / 2
    y = y_topo - largura
    c.drawImage(caminho, x, y, width=largura, height=largura, preserveAspectRatio=True)
    return y


def main():
    c = canvas.Canvas(OUT_PDF, pagesize=(PAGE_W, PAGE_H))
    pagina = 1

    # ---------- INTRO ----------
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "ANSWER KEY", x0, y1 - 10, 24)
    y -= 6
    y = paragrafo(c,
        "Answers for every puzzle in this book, night by night. Grown-ups: "
        "feel free to check the kids' work here, or just to double-check "
        "your own dreidel math.",
        x0, x1, y, tamanho=11, entrelinha=15)
    pagina += 1

    # ---------- NIGHT 1 ----------
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 1: Judah Says No", x0, y1 - 10, 16)
    metade = (x1 - x0 - 20) / 2
    y2 = subtitulo(c, "Escape to the Hills", x0, y)
    imagem_centralizada(c, f"{ASSETS}/labirinto_facil_gabarito.png", x0, x0 + metade, y2, 200)
    subtitulo(c, "Back to Modiin", x0 + metade + 20, y)
    imagem_centralizada(c, f"{ASSETS}/labirinto_medio_gabarito.png",
                         x0 + metade + 20, x1, y2, 200)
    pagina += 1

    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 1: Word Hunt", x0, y1 - 10, 16)
    imagem_centralizada(c, f"{ASSETS}/cacapalavras_noite1_gabarito.png", x0, x1, y - 4, 320)
    pagina += 1

    # ---------- NIGHT 2 ----------
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 2: The Temple Is a Mess", x0, y1 - 10, 15)
    y = subtitulo(c, "Spot the 5 / 10 Differences", y=y, x0=x0)
    y = paragrafo(c, "Each item below is in the top picture and missing from the bottom picture.",
                  x0, x1, y, tamanho=9.5, entrelinha=13)
    diffs = [
        "1. Broken jar on the floor.",
        "2. Cobweb in the upper corner.",
        "3. Table lying on its side.",
        "4. Torn curtain on the wall.",
        "5. Pile of dust on the floor.",
        "6. Fallen column drum on the floor. (10 only)",
        "7. Torn banner hanging crooked on the wall. (10 only)",
        "8. Bench with a snapped leg. (10 only)",
        "9. Candle stand knocked over. (10 only)",
        "10. Tipped-over bucket. (10 only)",
    ]
    for linha in diffs:
        y = paragrafo(c, linha, x0, x1, y, tamanho=9.5, entrelinha=13)
    pagina += 1

    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 2: Connect the Dots", x0, y1 - 10, 16)
    metade = (x1 - x0 - 20) / 2
    y2 = subtitulo(c, "The Hanukkiah (1-30)", x0, y)
    imagem_centralizada(c, f"{ASSETS}/noite2_ligar_pontos_hanukia_gabarito.png",
                         x0, x0 + metade, y2, 220)
    subtitulo(c, "The Temple Menorah (1-80)", x0 + metade + 20, y)
    imagem_centralizada(c, f"{ASSETS}/noite2_ligar_pontos_menora_gabarito.png",
                         x0 + metade + 20, x1, y2, 220)
    pagina += 1

    # ---------- NIGHT 3 ----------
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 3: One Little Jar of Oil", x0, y1 - 10, 15)
    metade = (x1 - x0 - 20) / 2
    y2 = subtitulo(c, "Symbol Sudoku (4x4)", x0, y)
    imagem_centralizada(c, f"{ASSETS}/noite3_sudoku4x4_gabarito.png", x0, x0 + metade, y2, 190)
    subtitulo(c, "Symbol Sudoku (6x6)", x0 + metade + 20, y)
    imagem_centralizada(c, f"{ASSETS}/noite3_sudoku6x6_gabarito.png",
                         x0 + metade + 20, x1, y2, 190)
    pagina += 1

    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 3, continued", x0, y1 - 10, 16)
    y = subtitulo(c, "Which Jar Is Different?", x0, y)
    imagem_centralizada(c, f"{ASSETS}/noite3_jarro_diferente_gabarito.png", x0, x1, y, 200)
    y -= 210
    y = subtitulo(c, "Which Jar Is the Pure One?", x0, y)
    y = paragrafo(c,
        "Answer: Jar C. It is the only jar with an intact seal, found "
        "standing up, and stamped with the High Priest's own mark.",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    pagina += 1

    # ---------- NIGHT 4 ----------
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 4: Light It Right", x0, y1 - 10, 16)
    y = subtitulo(c, "Number the Steps", x0, y)
    y = paragrafo(c,
        "Correct order: 2, 4, 1, 3\n"
        "(1) Place tonight's candles. (2) Say the blessings. "
        "(3) Use the lit shamash to light the candles. (4) Put the "
        "shamash back.",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 10
    y = subtitulo(c, "How Many Candles Tonight?", x0, y)
    y = paragrafo(c, "4 candles + 1 shamash = 5 candles lit tonight.",
                  x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 10
    y = subtitulo(c, "How Many Candles in All Eight Nights?", x0, y)
    y = paragrafo(c,
        "Grand total: 44 candles (36 Hanukkah candles, 1 + 2 + ... + 8, "
        "plus 1 shamash lit every night, 8 in all). Verified by "
        "scripts/verificar_conta_velas_noite4.py.",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    pagina += 1

    # ---------- NIGHT 5 ----------
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 5: Spin the Dreidel", x0, y1 - 10, 16)
    y = subtitulo(c, "Match the Letter to Its Meaning", x0, y)
    y = paragrafo(c,
        "Nun = Nothing   |   Gimel = Everything   |   Hei = Half   |   "
        "Shin = Put one in",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 10
    y = subtitulo(c, "Gelt Math", x0, y)
    y = paragrafo(c,
        "1. 12 + 9 = 21     2. 24 / 4 = 6     "
        "3. (18 + 14) / 2 = 16     4. 15 + 22 + 18 + 27 = 82",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 10
    y = subtitulo(c, "Design a Dreidel", x0, y)
    y = paragrafo(c,
        "No single answer, this is a cut-and-fold project. Check that "
        "all four letters ended up on a face after folding: Nun, Gimel, "
        "Hei, Shin (or Pei, for the Israel version).",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    pagina += 1

    # ---------- NIGHT 6 ----------
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 6: Everything Fried", x0, y1 - 10, 16)
    y = subtitulo(c, "Kitchen Word Search", x0, y)
    imagem_centralizada(c, f"{ASSETS}/noite6_cacapalavras_cozinha_gabarito.png", x0, x1, y, 260)
    pagina += 1

    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 6, continued", x0, y1 - 10, 16)
    y = subtitulo(c, "Big Kitchen Word Search", x0, y)
    imagem_centralizada(c, f"{ASSETS}/noite6_cacapalavras_14x14_gabarito.png", x0, x1, y, 300)
    y -= 310
    y = paragrafo(c,
        "The Great Latke Disaster and Latkes or Sufganiyot? A Family Vote "
        "have no fixed answer key: the story depends on the words your "
        "family picks, and the vote depends on your family's taste.",
        x0, x1, y, tamanho=9.5, entrelinha=13, fonte="Helvetica-Oblique")
    pagina += 1

    # ---------- NIGHT 7 ----------
    par = True
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 7: Give Some Light Away", x0, y1 - 10, 15)
    y = subtitulo(c, "Count the Gelt", x0, y)
    y = paragrafo(c, "Group A: 8 coins     Group B: 13 coins",
                  x0, x1, y, tamanho=10.5, entrelinha=14)
    y -= 10
    y = subtitulo(c, "Bring the Gelt to the Tzedakah Box", x0, y)
    imagem_centralizada(c, f"{ASSETS}/noite7_labirinto_tzedaka_gabarito.png", x0, x1, y, 200)
    y -= 210
    y = subtitulo(c, "Split and Save", x0, y)
    y = paragrafo(c,
        "1. 12 / 3 = 4     2. (20 - 4) / 4 = 4     "
        "3. 30 / 5 = 6     4. (24 + 12) / 2 = 18",
        x0, x1, y, tamanho=10.5, entrelinha=14)
    pagina += 1

    # ---------- NIGHT 8 ----------
    par = False
    x0, y0, x1, y1 = nova_pagina(c, pagina, par)
    y = titulo_pagina(c, "Night 8: All Eight Lights", x0, y1 - 10, 16)
    y = subtitulo(c, "Family Hanukkah Quiz", x0, y)
    quiz = [
        "1. Antiochus", "2. Mattathias", "3. Hammer",
        "4. Seven (7)", "5. The shamash", "6. Five (5)",
        "7. Eight (8)", "8. Money (in Yiddish)",
        "9. Grated potato", "10. Giving to help people in need",
    ]
    for linha in quiz:
        y = paragrafo(c, linha, x0, x1, y, tamanho=10, entrelinha=13.5)
    y -= 6
    y = paragrafo(c,
        "Every answer is checked word for word against the story it "
        "came from by scripts/verificar_quiz_noite8.py.",
        x0, x1, y, tamanho=9, entrelinha=12, fonte="Helvetica-Oblique")

    c.save()
    print(f"[OK] PDF gerado: {OUT_PDF}, {pagina} paginas.")


if __name__ == "__main__":
    main()
