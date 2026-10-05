"""
montar_pdf_piloto_noite2.py
Monta o PDF do piloto da Noite 2 ("The Temple Is a Mess"): 8.5x11in, P&B,
gutter 0.65in, folio na mesma altura em todas as paginas, caixas de
ilustracao tracejadas e rotuladas. Mesmo padrao visual de montar_pdf_piloto.py
(Noite 1). Todo o texto e lido de manuscrito/noite-2-texto.md (fonte unica),
sem redigitar; so a lista curta de diferencas do gabarito e a tabela vem
daqui e devem bater com o md e com montar_answer_key.py.

Revisao 29/09/2026: jogo dos erros passa a ser UMA imagem-base duplicada no
Canva (objetos apagados na copia de baixo), quadro comparativo e historia
atualizados para o texto revisado de 26/09/2026, puzzles de ligar pontos
com os PNGs atuais.

Uso: python3 montar_pdf_piloto_noite2.py  (le noite-2-texto.md do MD_PATH)
Saida: /mnt/user-data/outputs/piloto-noite-2.pdf
"""
import json
import re
from textwrap import wrap

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

ASSETS = "/tmp/assets"
OUT_PDF = "/mnt/user-data/outputs/piloto-noite-2.pdf"

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



MD_PATH = "noite-2-texto.md"
LINHAS = [l.rstrip("\n") for l in open(MD_PATH, encoding="utf-8")]


def apos(marcador, ate_prefixo=None, n_min=1):
    """Retorna as linhas nao vazias depois da linha que contem `marcador`,
    ate a primeira linha que comece com `ate_prefixo` (ou linha '---'/'*(')."""
    i = next(k for k, l in enumerate(LINHAS) if marcador in l)
    out = []
    for l in LINHAS[i + 1:]:
        if l.startswith("---") or l.startswith("*(") or l.startswith("**(") or l.startswith("###"):
            if out:
                break
            continue
        if l.strip() == "":
            continue
        if ate_prefixo and l.startswith(ate_prefixo):
            break
        out.append(l)
    return out


HISTORIA = "\n\n".join(apos("### Tonight's Story"))
CAIXA_MENORA = apos("**WHAT'S A MENORAH VS. A HANUKKIAH?**")[0]
INSTR_5 = apos("**SPOT THE 5 DIFFERENCES**")[0]
INSTR_10 = apos("**SPOT THE 10 DIFFERENCES**")[0]
INSTR_HANUKIA = apos("**CONNECT THE DOTS: THE HANUKKIAH**")[0]
INSTR_MENORA = apos("**CONNECT THE DOTS: THE TEMPLE MENORAH**")[0]
CHARADA = "\n".join(apos("**FAMILY RIDDLE**"))
RESPOSTA = re.search(r"\*\(Answer: (.*)\)\*", "\n".join(LINHAS)).group(1)
TABELA = []
for l in LINHAS:
    if l.startswith("|") and not l.startswith("|---") and not l.startswith("| |"):
        TABELA.append([c.strip() for c in l.strip("|").split("|")])
CAB_TABELA = [c.strip() for c in next(l for l in LINHAS if l.startswith("| |")).strip("|").split("|")]

DIFFS = [
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

RH = "Night 2: The Temple Is a Mess"


def imagem_ajustada(c, caminho, x0, x1, y_topo, altura_max):
    from PIL import Image
    w, h = Image.open(caminho).size
    larg = x1 - x0
    escala = min(larg / w, altura_max / h)
    dw, dh = w * escala, h * escala
    c.drawImage(caminho, x0 + (larg - dw) / 2, y_topo - dh, width=dw, height=dh)
    return y_topo - dh


def jogo_dos_erros(c, x0, x1, y, rotulo_topo, rotulo_base):
    """Duas caixas empilhadas de 7.35 x 3.0 in (a mesma imagem-base duplicada)."""
    h = 3.0 * inch
    caixa_ilustracao(c, x0, y - h, x1 - x0, h, rotulo_topo, f"{(x1 - x0) / inch:.2f} x 3.0")
    y -= h + 10
    caixa_ilustracao(c, x0, y - h, x1 - x0, h, rotulo_base, f"{(x1 - x0) / inch:.2f} x 3.0")
    return y - h


def tabela(c, x0, x1, y):
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x0, y, "How is it different from the hanukkiah?")
    y -= 18
    larg = x1 - x0
    cols = [x0, x0 + larg * 0.22, x0 + larg * 0.60]
    c.setFont("Helvetica-Bold", 9.5)
    for cx, txt in zip(cols[1:], CAB_TABELA[1:]):
        c.drawString(cx, y, txt)
    c.setLineWidth(0.8)
    c.line(x0, y - 4, x1, y - 4)
    y -= 18
    for linha in TABELA:
        topo = y
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(cols[0], y, linha[0])
        c.setFont("Helvetica", 9.5)
        fim = y
        for cx, larg_col, txt in zip(cols[1:], [larg * 0.36, larg * 0.40], linha[1:]):
            yy = topo
            for seg in wrap(txt, int(larg_col / (9.5 * 0.5))):
                c.drawString(cx, yy, seg)
                yy -= 12.5
            fim = min(fim, yy)
        y = fim - 4
        c.setStrokeColor(GRAY)
        c.setLineWidth(0.4)
        c.line(x0, y + 8, x1, y + 8)
        c.setStrokeColor(black)
        y -= 6
    return y


def main():
    c = canvas.Canvas(OUT_PDF, pagesize=(PAGE_W, PAGE_H))
    pagina = 1

    # 1 (recto): Tonight's Story
    x0, y0, x1, y1 = nova_pagina(c, pagina, False, RH)
    y = titulo_pagina(c, "NIGHT 2: The Temple Is a Mess", x0, y1 - 10, 22)
    y -= 6
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x0, y, "Tonight's Story")
    y -= 20
    y = paragrafo(c, HISTORIA, x0, x1, y, tamanho=11.5, entrelinha=16)
    y -= 10
    caixa_ilustracao(c, x0, y - 173, x1 - x0, 173,
                     "ILUSTRACAO 2.1 - aprovada (ilustracoes/2.1.png), recortar para esta faixa",
                     f"{(x1 - x0) / inch:.2f} x 2.4")
    pagina += 1

    # 2 (verso): menorah vs hanukkiah
    x0, y0, x1, y1 = nova_pagina(c, pagina, True, RH)
    y = titulo_pagina(c, "What's a Menorah vs. a Hanukkiah?", x0, y1 - 10, 16)
    c.saveState()
    c.setStrokeColor(GRAY)
    c.setLineWidth(1)
    box_h = 72
    c.rect(x0, y - box_h, x1 - x0, box_h)
    c.restoreState()
    paragrafo(c, CAIXA_MENORA, x0 + 10, x1 - 10, y - 16, tamanho=10.5, entrelinha=14)
    y -= box_h + 30
    caixa_ilustracao(c, x0, y - 216, x1 - x0, 216,
                     "ILUSTRACAO 2.4 - menora (7 braços) x hanukiá (8+1), sem texto na arte [REVISAR]",
                     f"{(x1 - x0) / inch:.2f} x 3.0")
    pagina += 1

    # 3 (recto): 5 erros
    x0, y0, x1, y1 = nova_pagina(c, pagina, False, RH)
    y = titulo_pagina(c, "★ Spot the 5 Differences", x0, y1 - 10, 16)
    y = paragrafo(c, INSTR_5, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 8
    jogo_dos_erros(c, x0, x1, y,
                   "ILUSTRACAO 2.2 - Templo ANTES (imagem-base completa)",
                   "ILUSTRACAO 2.2 - Templo DEPOIS (copia sem os objetos 1 a 5)")
    pagina += 1

    # 4 (verso): ligar pontos hanukia
    x0, y0, x1, y1 = nova_pagina(c, pagina, True, RH)
    y = titulo_pagina(c, "★ Connect the Dots: the Hanukkiah", x0, y1 - 10, 16)
    y = paragrafo(c, INSTR_HANUKIA, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 10
    imagem_ajustada(c, f"{ASSETS}/noite2_ligar_pontos_hanukia.png", x0, x1, y, 480)
    pagina += 1

    # 5 (recto): 10 erros
    x0, y0, x1, y1 = nova_pagina(c, pagina, False, RH)
    y = titulo_pagina(c, "★★ Spot the 10 Differences", x0, y1 - 10, 16)
    y = paragrafo(c, INSTR_10, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 8
    jogo_dos_erros(c, x0, x1, y,
                   "ILUSTRACAO 2.3 - Templo ANTES (mesma imagem-base completa)",
                   "ILUSTRACAO 2.3 - Templo DEPOIS (copia sem os objetos 1 a 10)")
    pagina += 1

    # 6 (verso): ligar pontos menorah + quadro
    x0, y0, x1, y1 = nova_pagina(c, pagina, True, RH)
    y = titulo_pagina(c, "★★ Connect the Dots: the Temple Menorah", x0, y1 - 10, 15)
    y = paragrafo(c, INSTR_MENORA, x0, x1, y - 6, tamanho=10.5, entrelinha=14)
    y -= 6
    y = imagem_ajustada(c, f"{ASSETS}/noite2_ligar_pontos_menora.png", x0, x1, y, 330)
    y -= 26
    y = tabela(c, x0, x1, y)
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(GRAY)
    c.drawString(x0, y - 4, "[REVISAR] quadro comparativo, ver revisao-religiosa.md")
    c.setFillColor(black)
    pagina += 1

    # 7 (recto): Before the Candles
    x0, y0, x1, y1 = nova_pagina(c, pagina, False, RH)
    y = titulo_pagina(c, "Before the Candles", x0, y1 - 10, 18)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x0, y, "Family Riddle")
    y -= 18
    y = paragrafo(c, CHARADA, x0, x1, y, tamanho=11.5, entrelinha=16)
    y -= 8
    y = paragrafo(c, f"(Answer: {RESPOSTA})", x0, x1, y, tamanho=10, entrelinha=14,
                  fonte="Helvetica-Oblique")
    y -= 24
    caixa_ilustracao(c, x0, y - 200, x1 - x0, 200,
                     "ILUSTRACAO 2.1 (reaproveitada) ou nova cena de fechamento",
                     f"{(x1 - x0) / inch:.2f} x 2.8")
    pagina += 1

    # 8 (verso): gabarito
    x0, y0, x1, y1 = nova_pagina(c, pagina, True, RH)
    y = titulo_pagina(c, "Answer Key: Night 2 (pilot)", x0, y1 - 10, 16)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x0, y, "Spot the 5 / 10 Differences")
    y -= 15
    y = paragrafo(c, "Each item below is in the top picture and missing from the bottom picture.",
                  x0, x1, y, tamanho=9.5, entrelinha=13)
    for linha in DIFFS:
        y = paragrafo(c, linha, x0, x1, y, tamanho=9.5, entrelinha=13)
    y -= 12
    metade = (x1 - x0 - 20) / 2
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x0, y, "Connect the Dots: the Hanukkiah")
    c.drawString(x0 + metade + 20, y, "Connect the Dots: the Temple Menorah")
    y -= 8
    imagem_ajustada(c, f"{ASSETS}/noite2_ligar_pontos_hanukia_gabarito.png", x0, x0 + metade, y, 200)
    imagem_ajustada(c, f"{ASSETS}/noite2_ligar_pontos_menora_gabarito.png", x0 + metade + 20, x1, y, 220)
    pagina += 1

    c.save()
    print(f"[OK] PDF gerado: {OUT_PDF}, {pagina - 1} paginas.")


if __name__ == "__main__":
    main()
