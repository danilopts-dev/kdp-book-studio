"""
gerar_problemas_gelt.py
Gera e verifica por codigo os problemas de matematica com gelt da Noite 5
(atividade ★★ "Gelt Math"). Aritmetica simples (soma, divisao em grupos
iguais com resto), dentro da faixa "contar ate 80+, ou duas etapas" da
regra 4 das reguas operacionais, adequada a 8-10 anos.

Uso: python3 gerar_problemas_gelt.py
Saida: puzzle-assets/noite5_problemas_gelt.json (problemas + respostas)
"""
import json

OUT = "/mnt/user-data/outputs/puzzle-assets/noite5_problemas_gelt.json"


def problema_1():
    # Soma simples de duas maos de gelt
    a, b = 12, 9
    resposta = a + b
    return {
        "id": "gelt_1",
        "enunciado": f"You win {a} gelt coins in the first round and {b} more in the second round. How many gelt coins do you have now?",
        "operacao": f"{a} + {b}",
        "resposta": resposta,
    }


def problema_2():
    # Divisao em grupos iguais, sem resto
    total, grupos = 24, 4
    resposta = total // grupos
    assert total % grupos == 0
    return {
        "id": "gelt_2",
        "enunciado": f"You have {total} gelt coins to share equally with {grupos} cousins (you get a share too). How many coins does each person get?",
        "operacao": f"{total} / {grupos}",
        "resposta": resposta,
    }


def problema_3():
    # Duas etapas: ganhar e depois perder metade (Hei) para o pote
    inicio, ganho = 18, 14
    subtotal = inicio + ganho
    perdido = subtotal // 2
    resposta = subtotal - perdido
    assert subtotal % 2 == 0
    return {
        "id": "gelt_3",
        "enunciado": (
            f"You start the dreidel game with {inicio} gelt coins. You spin a Gimel and win "
            f"{ganho} more coins from the pot. Then you spin a Hei and have to put half of your "
            f"coins back in the pot. How many coins do you have left?"
        ),
        "operacao": f"({inicio} + {ganho}) / 2",
        "resposta": resposta,
        "duas_etapas": True,
    }


def problema_4():
    # Soma de mais de dois numeros, faixa 80+
    moedas = [15, 22, 18, 27]
    resposta = sum(moedas)
    return {
        "id": "gelt_4",
        "enunciado": (
            "Four cousins count their gelt after the tournament: "
            f"{moedas[0]}, {moedas[1]}, {moedas[2]}, and {moedas[3]} coins. "
            "How many gelt coins did the whole family win tonight?"
        ),
        "operacao": " + ".join(str(m) for m in moedas),
        "resposta": resposta,
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


def main():
    problemas = [problema_1(), problema_2(), problema_3(), problema_4()]
    erros = verificar(problemas)
    if erros:
        raise SystemExit(f"[FALHA] Verificacao encontrou erros: {erros}")
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(problemas, f, indent=2, ensure_ascii=False)
    print(f"[OK] {len(problemas)} problemas gerados e verificados. Salvo em {OUT}")
    for p in problemas:
        print(f"  {p['id']}: {p['operacao']} = {p['resposta']}")


if __name__ == "__main__":
    main()
