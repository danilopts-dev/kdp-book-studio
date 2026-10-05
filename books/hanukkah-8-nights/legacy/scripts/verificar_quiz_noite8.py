"""
verificar_quiz_noite8.py
Confere que cada resposta do "Family Hanukkah Quiz" (Noite 8) de fato
aparece no texto da noite de origem correspondente (noite-N-texto.md),
por checagem de palavra-chave/substring, case-insensitive. Nenhuma
resposta deve depender de fato nao escrito nas Noites 1-7.

Uso: python3 verificar_quiz_noite8.py
Saida: relatorio no stdout, exit code 0 se tudo passar, 1 se alguma
pergunta falhar.
"""
import re
import sys

BASE = "/mnt/user-data/outputs"

# Cada entrada: (numero, pergunta curta, noite de origem, lista de
# palavras-chave que TODAS precisam aparecer no texto da noite de
# origem para a resposta ser considerada confirmada).
QUIZ = [
    (1, "King who tried to stop Jewish traditions", 1, ["antiochus"]),
    (2, "Old man from Modiin who said no", 1, ["mattathias", "modiin"]),
    (3, "What Maccabee means", 1, ["hebrew word for", "hammer"]),
    (4, "Branches on the Temple menorah", 2, ["seven branches"]),
    (5, "Name of the helper candle", 4, ["shamash", "helper"]),
    (6, "Candles lit on Night 4 counting shamash", 4, ["4 candles + 1 shamash"]),
    (7, "Nights the little jar of oil burned", 3, ["eighth day"]),
    (8, "What gelt means", 5, ["gelt means", "money", "yiddish"]),
    (9, "What a latke is made from", 6, ["grated potato"]),
    (10, "What tzedakah is", 7, ["tzedakah means giving to help"]),
]


def carregar_texto(noite):
    caminho = f"{BASE}/noite-{noite}-texto.md"
    with open(caminho, encoding="utf-8") as f:
        return f.read().lower()


def main():
    falhas = []
    print("Verificacao do Family Hanukkah Quiz (Noite 8) contra as fontes originais\n")
    textos_cache = {}
    for num, pergunta, noite, palavras_chave in QUIZ:
        if noite not in textos_cache:
            textos_cache[noite] = carregar_texto(noite)
        texto = textos_cache[noite]
        ok = True
        faltando = []
        for palavra in palavras_chave:
            if palavra.lower() not in texto:
                ok = False
                faltando.append(palavra)
        status = "OK" if ok else "FALHA"
        print(f"[{status}] Q{num} ({pergunta}) -> Night {noite}: chaves {palavras_chave}")
        if not ok:
            falhas.append((num, pergunta, noite, faltando))

    print()
    if falhas:
        print(f"[FALHA GERAL] {len(falhas)} pergunta(s) sem confirmacao no texto de origem:")
        for num, pergunta, noite, faltando in falhas:
            print(f"  Q{num} ({pergunta}), Night {noite}: nao encontrado {faltando}")
        sys.exit(1)
    else:
        print(f"[OK GERAL] Todas as {len(QUIZ)} respostas do quiz foram confirmadas "
              f"por palavra-chave contra o texto da noite de origem correspondente.")
        sys.exit(0)


if __name__ == "__main__":
    main()
