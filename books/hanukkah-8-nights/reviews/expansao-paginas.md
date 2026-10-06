# Expansão de páginas: +2 por noite (aprovada pelo Danilo em 2026-10-06)

Objetivo: o miolo vai de 64 para ~82 páginas (16 páginas novas nas noites + ~2 no answer key). Cada noite ganha **1 página ★ e 1 página ★★** (1 atividade por página). Preenche o que o TOC já prometia (3-4 atividades por nível por noite). **Não muda estrutura, promessa nem texto aprovado das atividades existentes.**

## Regras (valem para todas as atividades novas)
- Uma atividade por página, título concreto, selo de nível pelo componente `activity(1|2, "Título")[instrução]` do `theme.typ`. Instrução de até 25 palavras, inglês americano simples (★ 6-7 anos, ★★ 8-10; ver `legacy/docs/reguas-operacionais.md`, seções 1, 4, 9, 10, 11).
- Zero Natal. Nenhuma letra hebraica em script (exceção única já aprovada: as letras נ ג ה ש e פ na N5, exatamente como no exercício "Match the Letter"). Sem travessão longo (— ou –) no corpo. Humor limpo. Nada de fato que as noites (`legacy/manuscript/noite-N-texto.md` e `content/nN.typ`) não sustentem.
- **Todo puzzle é gerado por script e verificado por código** (solução única, palavras presentes na grade, caminho único do labirinto, cifra que decodifica, lógica com 1 solução, contas conferidas). Nenhum puzzle é escrito "à mão" por agente. Scripts novos em `legacy/scripts/extra_*.py`; assets em `inputs/puzzle-assets/extra_nN_*` (puzzle PNG + gabarito PNG + JSON), P&B, fundo branco puro, mínimo 2400 px no lado maior, traço grosso (legível impresso). Fonte nas imagens: `fonts/AtkinsonHyperlegible-Bold.ttf` (PIL). Atividades desenhadas em Typst (velas, moedas, tabelas) não precisam de PNG, mas os dados e as respostas vão para o JSON/`notes.md`.
- **Não repetir** palavras de puzzle de outras noites: confira `inputs/puzzle-assets/*_gabarito.json`, `notes.md` (temas já usados) e os `content/*.typ`. Caça-palavras/crossword: palavras de 3+ letras, todas do tema da noite, 10-14 por puzzle.
- Labirinto: reutilizar `legacy/scripts/gerar_labirinto.py` (veja `gerar_labirinto_tzedaka.py`: gera o PNG e o `_gabarito.json` com `rotulo_inicio`, `rotulo_fim`, `abertura_entrada`, `abertura_saida`) e o componente `maze-ends("<nome-sem-extensão>")` (rótulos NA abertura). Seed própria por labirinto, tamanho 12x12 (★).
- Caça-palavras: `studio/generators/wordsearch.py` (níveis easy = →↓; medium = + diagonais) e renderizar em PNG no estilo de `cacapalavras_noite1_grade.png`, com gabarito destacado em cinza (livro P&B, nada de vermelho).
- **Inserção na noite**: a nova ★ vai depois da última atividade ★ existente; a nova ★★ depois da última ★★ e antes do Before the Candles. **Exceção N5 e N7** (páginas de recorte com verso em branco que dependem de paridade): inserir as DUAS páginas novas imediatamente ANTES da primeira página de recorte (N5: antes de "Design a Dreidel"; N7: antes do Coupon Book), na ordem nova ★, nova ★★. Como cada noite ganha exatamente 2 páginas, a paridade de todas as páginas de recorte se mantém. Confira no PDF.
- Cada atividade nova: 1 página, respiro como nas existentes, texto ≥ 12pt, nada cortado, nada pixelado. Não alterar páginas existentes além de inserir as novas.
- Registrar em `notes.md` (3 linhas por noite): páginas novas, assets, componentes, e as **respostas** de cada atividade (o answer-key as lê dali). Registrar suposições em `questions.md` (ASSUMIDA).
- Não sobrescrever arquivos aprovados em `inputs/`. Não fazer commit nem mexer em `state.json`.

## O que entra em cada noite
| Noite | ★ nova | ★★ nova |
|---|---|---|
| N1 Judah Says No | **Unscramble the Words**: 8 palavras da história (fora do caça-palavras da N1) embaralhadas, com pista curta cada; resposta por linha | **Crack the Code**: cifra letra-número (A=1...Z=26), tabela da cifra + mensagem numérica que decodifica uma frase da própria história (ex.: "ONE FAMILY ONE NO") |
| N2 The Temple Is a Mess | **Clean-Up Maze**: labirinto 12x12, entrada BROOM, saída TEMPLE DOOR | **Temple Word Search**: 14x14 com diagonais (sem reverso), 12 palavras da limpeza do Templo (não "TEMPLE", usada na N1) |
| N3 One Little Jar of Oil | **Follow the Oil**: labirinto 12x12, entrada JAR, saída MENORAH | **Oil Math**: 4 problemas de conta ligados a 1 jarro e 8 dias (conferidos por código; respostas fora da página) |
| N4 Light It Right | **Draw the Candles**: 3 hanukkiahs vazias (Noites 2, 4 e 6) para a criança desenhar as velas certas; lembrar do shamash | **Which Night Is It?**: 4 hanukkiahs desenhadas em Typst com velas acesas; a criança escreve a noite (o shamash não conta) e responde quantas velas ao todo |
| N5 Spin the Dreidel | **Dreidel Tally Chart**: "gire 20 vezes e marque um tracinho por letra", 4 colunas (letra hebraica grande + nome, como no Match), pergunta "qual letra ganhou?" | **What Comes Next? Dreidel Patterns**: 6 sequências com padrão (letras/formas), resposta única verificada por código |
| N6 Everything Fried | **Latke Maze**: 12x12, entrada POTATO, saída PLATE | **Hanukkah Food Crossword**: palavras cruzadas geradas por código (novo gerador), 10-12 palavras de comidas e cozinha da N6 (sem repetir as do caça-palavras da noite), pistas curtas |
| N7 Give Some Light Away | **Which Pile Has More?**: 6 pares de pilhas de moedas desenhadas por código, circular a maior (diferença ≥ 2) | **Who Gets What?**: lógica com 4 crianças e 4 gestos de bondade, 4-5 pistas, grade para marcar, solução única por força bruta |
| N8 All Eight Lights | **Match the Night**: ligar 6 noites ao que aconteceu nelas (fatos conferidos contra os manuscritos) | **Night by Night Word Search**: 15x15 com diagonais, 12 palavras das 8 noites, sem repetir palavras de outros puzzles |

## Respostas (preencher conforme cada noite for feita)
