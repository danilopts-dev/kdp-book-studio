"""
gerar_problemas_moedas_noite7.py
Gera os dois conteudos de matematica com moedas da Noite 7:

1. ★ "Count the Gelt" — atividade simples de contagem: desenha N moedas
   (circulos com $ dentro, estilo gelt) em fileiras, a crianca escreve o
   total. Layout gerado por codigo (PNG), soma conferida por codigo.
2. ★★ "Split and Save" — 4 problemas de dividir moedas em grupos iguais
   (tzedakah + guardar em potes), mesma logica de verificacao de
   gerar_problemas_gelt.py (Noite 5): cada resposta e recalculada e
   conferida contra o valor declarado antes de salvar.

Uso: python3 gerar_problemas_moedas_noite7.py
Saida: puzzle-assets/noite7_contar_moedas.png
       puzzle-assets/noite7_contar_moedas_gabarito.json
       puzzle-assets/noite7_problemas_moedas.json
"""
import json

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "/home/claude/n2fix/puzzle-assets"


def _fonte(tamanho):
    try:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", tamanho)
    except OSError:
        return ImageFont.load_default()


# ---------------------------------------------------------------------
# 1. ★ Count the Gelt (contagem simples, desenho gerado por codigo)
# ---------------------------------------------------------------------

ESCALA_RESOLUCAO = 3  # mesma correcao de resolucao do resto do piloto: o
                       # "$" usava draw.text sem fonte explicita (fonte
                       # bitmap padrao do PIL, minuscula e pixelizada) -
                       # corrigido para fonte truetype em escala maior


def desenhar_moedas(n_moedas, por_fileira, caminho_png, raio=26, espaco=18, margem=30):
    esc = ESCALA_RESOLUCAO
    raio *= esc
    espaco *= esc
    margem *= esc
    fonte = _fonte(int(22 * esc))

    fileiras = (n_moedas + por_fileira - 1) // por_fileira
    W = por_fileira * (raio * 2 + espaco) + margem * 2
    H = fileiras * (raio * 2 + espaco) + margem * 2
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    for i in range(n_moedas):
        linha = i // por_fileira
        col = i % por_fileira
        cx = margem + col * (raio * 2 + espaco) + raio
        cy = margem + linha * (raio * 2 + espaco) + raio
        draw.ellipse([cx - raio, cy - raio, cx + raio, cy + raio],
                     outline="black", width=3 * esc)
        # simbolo "$" centralizado com fonte truetype (antes usava a
        # fonte bitmap padrao do PIL, que saia pixelizada ao ampliar)
        bbox = draw.textbbox((0, 0), "$", font=fonte)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text((cx - tw / 2, cy - th / 2 - bbox[1]), "$", fill="black", font=fonte)

    img.save(caminho_png)
    return W, H


def gerar_contagem():
    """Duas linhas de contagem na mesma pagina: 8 moedas e 13 moedas,
    dentro da faixa '★: contar ate 20-30, uma operacao' da regra 4."""
    grupos = [
        {"id": "grupo_a", "quantidade": 8, "por_fileira": 8},
        {"id": "grupo_b", "quantidade": 13, "por_fileira": 8},
    ]
    for g in grupos:
        caminho = f"{OUT_DIR}/noite7_contar_moedas_{g['id']}.png"
        desenhar_moedas(g["quantidade"], g["por_fileira"], caminho)
        g["arquivo"] = caminho

    gabarito = {
        "atividade": "Count the Gelt (★)",
        "grupos": [{"id": g["id"], "total": g["quantidade"]} for g in grupos],
    }
    with open(f"{OUT_DIR}/noite7_contar_moedas_gabarito.json", "w") as f:
        json.dump(gabarito, f, indent=2)

    print("[OK] Count the Gelt: 2 grupos de moedas desenhados "
          f"({', '.join(str(g['quantidade']) for g in grupos)} moedas), "
          "gabarito salvo.")
    return gabarito


# ---------------------------------------------------------------------
# 2. ★★ Split and Save (divisao em grupos iguais, verificado por codigo)
# ---------------------------------------------------------------------

def problema_1():
    # Divisao simples em grupos iguais, sem resto.
    total, grupos = 12, 3
    resposta = total // grupos
    assert total % grupos == 0
    return {
        "id": "moedas_1",
        "enunciado": (
            f"You have {total} gelt coins. You want to give some to "
            f"tzedakah and save the rest in {grupos} equal piles for "
            f"later. If you split all {total} coins into {grupos} "
            f"equal piles, how many coins are in each pile?"
        ),
        "operacao": f"{total} / {grupos}",
        "resposta": resposta,
    }


def problema_2():
    # Duas etapas: separar uma parte para tzedaka primeiro, depois
    # dividir o resto em grupos iguais.
    total, tzedakah, grupos = 20, 4, 4
    resto = total - tzedakah
    resposta = resto // grupos
    assert resto % grupos == 0
    return {
        "id": "moedas_2",
        "enunciado": (
            f"You have {total} gelt coins. First, you put {tzedakah} "
            f"coins in the tzedakah box. Then you split the coins "
            f"that are left into {grupos} equal jars to save. How "
            f"many coins go in each jar?"
        ),
        "operacao": f"({total} - {tzedakah}) / {grupos}",
        "resposta": resposta,
        "duas_etapas": True,
    }


def problema_3():
    # Divisao com numero maior, ainda sem resto.
    total, grupos = 30, 5
    resposta = total // grupos
    assert total % grupos == 0
    return {
        "id": "moedas_3",
        "enunciado": (
            f"Your family collected {total} gelt coins for tzedakah "
            f"tonight. You want to put an equal number of coins into "
            f"{grupos} different tzedakah boxes for {grupos} "
            f"different causes. How many coins go in each box?"
        ),
        "operacao": f"{total} / {grupos}",
        "resposta": resposta,
    }


def problema_4():
    # Duas etapas com numero na faixa alta (80+): somar duas fontes de
    # moedas, depois dividir em grupos iguais.
    a, b, grupos = 24, 12, 2
    subtotal = a + b
    resposta = subtotal // grupos
    assert subtotal % grupos == 0
    return {
        "id": "moedas_4",
        "enunciado": (
            f"You earned {a} gelt coins from your grandparents and "
            f"{b} more from your aunt and uncle. You decide to split "
            f"everything evenly: half for tzedakah, half to save. "
            f"How many coins go to tzedakah?"
        ),
        "operacao": f"({a} + {b}) / {grupos}",
        "resposta": resposta,
        "duas_etapas": True,
    }


def verificar(problemas):
    erros = []
    for p in problemas:
        try:
            valor = eval(p["operacao"].replace("/", "//"))
        except Exception as e:
            erros.append((p["id"], f"erro ao avaliar: {e}"))
            continue
        if valor != p["resposta"]:
            erros.append((p["id"], f"esperado {p['resposta']}, calculado {valor}"))
        if not (0 <= p["resposta"] <= 100):
            erros.append((p["id"], f"resposta fora da faixa 0-100: {p['resposta']}"))
    return erros


def gerar_divisao():
    problemas = [problema_1(), problema_2(), problema_3(), problema_4()]
    erros = verificar(problemas)
    if erros:
        raise SystemExit(f"[FALHA] Verificacao encontrou erros: {erros}")
    with open(f"{OUT_DIR}/noite7_problemas_moedas.json", "w", encoding="utf-8") as f:
        json.dump(problemas, f, indent=2, ensure_ascii=False)
    print(f"[OK] {len(problemas)} problemas de 'Split and Save' gerados e verificados.")
    for p in problemas:
        print(f"  {p['id']}: {p['operacao']} = {p['resposta']}")
    return problemas


def main():
    gerar_contagem()
    gerar_divisao()


if __name__ == "__main__":
    main()
