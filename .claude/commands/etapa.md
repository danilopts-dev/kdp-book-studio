---
description: Executa ou refaz uma tarefa específica do livro. Uso /etapa <slug> <tarefa> (ex.: unit:ch03, listing, editorial)
argument-hint: <slug> <tarefa> [instruções extras]
---
Argumentos: $ARGUMENTS

Execute a tarefa indicada seguindo `pipelines/stages/_protocol.md`, mesmo que já esteja `done` (nesse caso é um refazer: aplique as instruções extras do Danilo, se houver, e mantenha o que não foi pedido para mudar). Tarefas que dependem desta (build em diante) voltam para `pending` com `./st mark <slug> <tarefa> pending` quando o refazer alterar conteúdo.
Reporte em até 3 linhas.
