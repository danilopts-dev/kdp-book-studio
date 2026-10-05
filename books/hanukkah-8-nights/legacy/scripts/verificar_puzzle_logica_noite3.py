"""
verificar_puzzle_logica_noite3.py
Verifica por forca bruta que as 3 pistas textuais de "Which jar is the pure
one?" (Noite 3, nivel duas-estrelas) levam a exatamente UMA solucao valida
entre os 4 jarros (A, B, C, D).

Testa todas as combinacoes possiveis (forca bruta sobre os 4 jarros) contra
cada pista isoladamente e contra as 3 combinadas, para confirmar que:
  1) nenhuma pista isolada ja da a resposta sozinha de forma trivial demais
     (ou, se der, documenta isso);
  2) as 3 pistas combinadas eliminam todos os jarros exceto 1.

Uso: python3 verificar_puzzle_logica_noite3.py
"""

JARROS = ["A", "B", "C", "D"]

SELO = {"A": "broken", "B": "intact", "C": "intact", "D": "broken"}
POSICAO = {"A": "standing", "B": "knocked_over", "C": "standing", "D": "knocked_over"}  # pista 2 revisada em 26/09/2026 (antes: cor da cera)
SELO_SUMO_SACERDOTE = {"A": "none", "B": "none", "C": "kohen_gadol", "D": "none"}

PISTA_1 = lambda j: SELO[j] == "intact"
PISTA_2 = lambda j: POSICAO[j] == "standing"
PISTA_3 = lambda j: SELO_SUMO_SACERDOTE[j] == "kohen_gadol"


def aplicar(pistas):
    candidatos = JARROS[:]
    for pista in pistas:
        candidatos = [j for j in candidatos if pista(j)]
    return candidatos


def main():
    isolada_1 = aplicar([PISTA_1])
    isolada_2 = aplicar([PISTA_2])
    isolada_3 = aplicar([PISTA_3])
    combinada = aplicar([PISTA_1, PISTA_2, PISTA_3])

    print("Pista 1 isolada (selo intacto):", isolada_1)
    print("Pista 2 isolada (encontrado em pe):", isolada_2)
    print("Pista 3 isolada (selo do Sumo Sacerdote):", isolada_3)
    print("As 3 pistas combinadas:", combinada)

    assert len(combinada) == 1, "as pistas nao levam a uma solucao unica"
    print(f"[OK] Solucao unica confirmada por forca bruta: Jarro {combinada[0]}.")


if __name__ == "__main__":
    main()
