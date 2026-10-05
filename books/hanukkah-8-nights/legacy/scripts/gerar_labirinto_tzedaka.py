"""
gerar_labirinto_tzedaka.py
Gera o labirinto da Noite 7 ("Bring the Gelt to the Tzedakah Box"),
nivel ★, mesma logica de gerar_labirinto.py (recursive backtracker +
verificacao de caminho unico por BFS + prova de arvore geradora).
Tamanho parecido com o labirinto facil da Noite 1 (12x12), conforme
pedido pelo brief ("nivel ★, entao mais simples").

Correcao (mesmo bug do labirinto da Noite 1, encontrado no piloto): este
script era uma copia colada de uma versao antiga de gerar_labirinto.py,
com os mesmos tres problemas ja corrigidos la (rotulo pixelizado por
fonte bitmap padrao do PIL, abertura de saida com sobra de linha por
"desenha e apaga por cima", cantos com folga por usar linha em vez de
retangulo). Em vez de colar a correcao de novo (o jeito que esse bug se
duplicou da primeira vez), este script agora IMPORTA as funcoes ja
corrigidas de gerar_labirinto.py, para as duas noites usarem sempre a
mesma logica testada.

Uso: python3 gerar_labirinto_tzedaka.py
Saida: puzzle-assets/noite7_labirinto_tzedaka.png
       puzzle-assets/noite7_labirinto_tzedaka_gabarito.png
       puzzle-assets/noite7_labirinto_tzedaka_gabarito.json
"""
import json
import random

from gerar_labirinto import (
    gerar_labirinto_perfeito,
    caminho_unico_bfs,
    desenhar,
    abertura_info,
    OUT_DIR,
)

# seed propria desta noite (mantida igual a decisao original registrada
# em relatorio-decisoes.md, item 34: seed 17, 12x12)
random.seed(17)


def gerar_puzzle(nome, largura, altura, rotulo_inicio, rotulo_fim):
    celulas = gerar_labirinto_perfeito(largura, altura)
    inicio = (0, 0)
    fim = (largura - 1, altura - 1)
    caminho = caminho_unico_bfs(celulas, largura, altura, inicio, fim)

    desenhar(celulas, largura, altura, inicio, fim, None,
             f"{OUT_DIR}/{nome}.png")
    desenhar(celulas, largura, altura, inicio, fim, caminho,
             f"{OUT_DIR}/{nome}_gabarito.png")

    info_entrada, info_saida = abertura_info(largura, altura, inicio, fim,
                                              tamanho_celula=40, margem=6)

    gabarito = {
        "nome": nome,
        "dimensoes": [largura, altura],
        "inicio": inicio,
        "fim": fim,
        "caminho": caminho,
        "passos": len(caminho) - 1,
        "rotulo_inicio": rotulo_inicio,
        "rotulo_fim": rotulo_fim,
        "abertura_entrada": info_entrada,
        "abertura_saida": info_saida,
    }
    with open(f"{OUT_DIR}/{nome}_gabarito.json", "w") as f:
        json.dump(gabarito, f, indent=2)

    print(f"[OK] {nome}: {largura}x{altura}, caminho unico com {len(caminho)} celulas, "
          f"verificado (arvore geradora + BFS).")
    return gabarito


if __name__ == "__main__":
    # Nivel ★, tamanho parecido ao labirinto facil da Noite 1 (12x12).
    gerar_puzzle("noite7_labirinto_tzedaka", 12, 12, "GELT", "TZEDAKAH BOX")
    print("Labirinto da Noite 7 gerado e verificado com sucesso.")
