---
description: Executa o livro inteiro sem parar, até o fim ou até um bloqueio geral. Uso /tudo <slug> [até <tarefa>]
argument-hint: <slug> [até <tarefa>]
---
Argumentos: $ARGUMENTS

Execute em loop seguindo `pipelines/stages/_protocol.md`:
- Tarefa seguinte: `./st next <slug> --runnable`. Sem tarefa executável: pare.
- Se foi informado "até <tarefa>", pare depois de concluir essa tarefa.
- Não pergunte nada no meio: dúvidas ASSUMIDAS são registradas e seguem; BLOQUEANTES bloqueiam só a tarefa afetada, e o loop continua com as outras.
- Não reporte a cada tarefa; só commit.
Ao final, um relatório curto: tarefas concluídas nesta rodada, bloqueios com as perguntas objetivas (copiadas de questions.md), ASSUMIDAS novas e o status geral (`./st status <slug>`). Se o livro terminou, aponte para `books/<slug>/READY.md`.
