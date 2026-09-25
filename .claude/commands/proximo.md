---
description: Executa a próxima tarefa do livro (ou as próximas N) e para. Uso /proximo <slug> [N]
argument-hint: <slug> [N]
---
Argumentos: $ARGUMENTS (sem slug e com um só livro em books/ sem "_" no início, use esse livro; se houver vários, pergunte qual.)

Execute N tarefas (padrão 1) seguindo `pipelines/stages/_protocol.md`, usando `./st next <slug> --runnable` a cada uma. Pare depois da N-ésima, ou antes se não houver tarefa executável.
Ao final, reporte em até 3 linhas: o que foi feito, perguntas novas e "faltam X tarefas" (de `./st status <slug>`).
