---
description: Faz ou refaz uma etapa específica do livro. Uso /etapa [livro] <etapa> [o que mudar] (ex.: "capítulo 3 mais curto", "listing", "bônus")
argument-hint: [livro] <etapa> [o que mudar]
---
Argumentos: $ARGUMENTS

O Danilo pode chamar a etapa pelo nome comum ("capítulo 3", "noite 5", "listing", "capa", "bônus", "revisão"). Ache a tarefa correspondente em `./st status <livro>` (os nomes legíveis aparecem ali, com o id entre colchetes). Se ficar ambíguo, pergunte citando as opções pelo nome.

Execute a tarefa seguindo `pipelines/stages/_protocol.md`, mesmo que já esteja pronta (nesse caso é um refazer: aplique o que o Danilo pediu e mantenha o resto). Se o refazer mudar conteúdo do miolo, as etapas que dependem dele (montagem do PDF em diante) voltam para `pending` com `./st mark`.
Reporte em até 3 linhas, no formato de CLAUDE.md.
