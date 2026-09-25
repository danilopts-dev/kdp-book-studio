# Formato: livros de atividades

Padrões do engine: 8.5x11, sans, 16pt+, um puzzle por página, answer key no fim (2 grids por linha no caça-palavras, 3 no sudoku), abertura de seção em página própria.

## Caça-palavras
- Grid 13x13 a 15x15 em letra grande (o engine limita a célula a 0,42"). Para sêniores: `easy` (→ e ↓) ou `medium` (+ diagonais). `hard` (reverso) só se o TOC pedir.
- 8 a 15 palavras por puzzle, todas do tema, ≥ 3 letras, sem repetir entre puzzles da mesma seção. Frases viram palavra única no grid (`Double Feature` → DOUBLEFEATURE); o nome exibido na lista mantém o espaço.
- Cada puzzle com título temático concreto (ex.: "At the Drive-In", não "Puzzle 7").
- O script garante: toda palavra está no grid exatamente uma vez, na direção permitida.

## Sudoku
- `easy` 40 pistas, `medium` 32, `hard` 27; solução única garantida por código.

## Trivia / memória
- Perguntas curtas, uma ideia por pergunta; múltipla escolha com 3 opções para sêniores (o padrão), resposta distribuída entre A/B/C.
- `fact` opcional (1 frase), que dá o gostinho de nostalgia na answer key.
- Referências só da era declarada; calibrar para o que alguém que viveu a época lembraria.

## Checklist de revisão
- Todo puzzle tem solução e toda solução corresponde a um puzzle (o engine gera juntos; confira títulos).
- Dificuldade consistente dentro da seção; sem saltos.
- Nenhum anacronismo; nada inadequado para o público.
- How-to-use presente e simples.
- Formato ainda sem gerador (palavras cruzadas, labirinto, ligar pontos): criar como `kind: typst` com o conteúdo pronto, ou propor um gerador novo em `studio/generators/` (ASSUMIDA).
