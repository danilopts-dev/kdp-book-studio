"""
verificar_conta_velas_noite4.py
Verifica por codigo a conta usada na atividade Night 4 (Star2):
"How many candles in all eight nights?"

O TOC v2 sinaliza [REVISAR a conta] com a resposta proposta "44 com o shamash".
Este script confere essa soma sob DUAS premissas possiveis (ver
revisao-religiosa.md para a decisao final entre elas):

  Premissa A: 1 shamash NOVO acendido a cada noite (8 shamashim ao total)
    total = soma das velas de Hanuca (1+2+...+8) + 8 shamashim

  Premissa B: o MESMO shamash fisico e reutilizado noite apos noite
    (contado uma unica vez no total de "velas usadas", nao uma vez por noite)
    total = soma das velas de Hanuca (1+2+...+8) + 1 shamash

Uso: python3 verificar_conta_velas_noite4.py
"""


def velas_acesas_por_noite():
    """Numero de velas de Hanuca (sem contar o shamash) acesas
    em cada uma das 8 noites: noite N acende N velas."""
    return list(range(1, 9))


def main():
    velas_por_noite = velas_acesas_por_noite()
    assert velas_por_noite == [1, 2, 3, 4, 5, 6, 7, 8]

    soma_velas_hanuca = sum(velas_por_noite)
    print(f"Velas de Hanuca por noite: {velas_por_noite}")
    print(f"Soma das velas de Hanuca (1+2+...+8) = {soma_velas_hanuca}")

    # Premissa A: 1 shamash novo por noite (8 shamashim no total)
    shamashim_premissa_a = 8
    total_a = soma_velas_hanuca + shamashim_premissa_a
    print()
    print("Premissa A (1 shamash novo a cada noite, 8 no total):")
    print(f"  {soma_velas_hanuca} + {shamashim_premissa_a} = {total_a}")
    assert total_a == 44, f"Premissa A esperava 44, deu {total_a}"

    # Premissa B: o mesmo shamash fisico reutilizado, contado 1 vez
    shamashim_premissa_b = 1
    total_b = soma_velas_hanuca + shamashim_premissa_b
    print()
    print("Premissa B (mesmo shamash fisico reaproveitado, contado 1 vez):")
    print(f"  {soma_velas_hanuca} + {shamashim_premissa_b} = {total_b}")

    # Conferencia independente por soma noite a noite (sem usar a formula
    # fechada n(n+1)/2), para nao confiar so na aritmetica de cabeca.
    total_a_loop = 0
    total_b_loop = 0
    for noite, n_velas in enumerate(velas_por_noite, start=1):
        total_a_loop += n_velas + 1          # +1 shamash novo nesta noite
        if noite == 1:
            total_b_loop += n_velas + 1      # 1a noite acende o shamash tambem
        else:
            total_b_loop += n_velas          # shamash ja contado na noite 1
    print()
    print(f"Conferencia por loop, noite a noite, Premissa A: {total_a_loop}")
    print(f"Conferencia por loop, noite a noite, Premissa B: {total_b_loop}")
    assert total_a_loop == total_a
    assert total_b_loop == total_b

    print()
    print("[OK] Premissa A (a usada no texto do piloto) confere: 44 velas no total.")
    print("[OK] Premissa B (shamash fisico unico reaproveitado) confere: 37 velas no total.")
    print()
    print("O TOC v2 propoe 44 como resposta. Esse numero so fecha sob a")
    print("Premissa A (contar 1 shamash por noite, 8 no total). Registrado")
    print("em revisao-religiosa.md para o Danilo/revisor confirmar qual")
    print("convencao o livro deve adotar antes da publicacao.")


if __name__ == "__main__":
    main()
