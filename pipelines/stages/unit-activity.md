# Etapa: unidade de atividade (wordsearch, sudoku, trivia)

1. Chame o subagente `activity-builder` com: slug, id da unidade. Ele escreve `content/<id>.yaml` (listas de palavras, perguntas com fonte, configuração de sudoku) conforme `rules/formats/activity.md` e roda `./st gen` quando aplicável.
2. `./st check <slug> --unit <id>`. Grids, answer keys e unicidade do sudoku são validados por código. Não revise isso lendo.
3. Chame `unit-reviewer` com slug, id e a saída do check. Foco: adequação ao público (era, dificuldade, nada anacrônico), fatos da trivia, títulos, texto de introdução.
4. Check de novo. Sem 🔴: `done`.
