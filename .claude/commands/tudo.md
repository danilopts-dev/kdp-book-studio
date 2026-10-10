---
description: Faz o livro inteiro sem parar, até o fim ou até precisar do Danilo. Uso /tudo [livro] [até <etapa>]
argument-hint: [livro] [até <etapa>]
---
Argumentos: $ARGUMENTS

Livro: qualquer pedaço do nome ou do título serve; sem livro, use o único em andamento (se houver mais de um, pergunte qual).

Execute em loop seguindo `pipelines/stages/_protocol.md`:
- Tarefa seguinte: `./st next <livro> --runnable`. Sem tarefa executável: pare.
- Se foi informado "até <etapa>" (ex.: "até a revisão", "até o capítulo 5"), pare depois de concluir essa tarefa.
- Não pergunte nada no meio: decisões menores você toma e registra; o que precisa do Danilo trava só a tarefa afetada, e o loop segue com as outras. O bônus corre em paralelo e não segura o resto.
- Não reporte a cada tarefa; só salve (commit e push silenciosos).
Ao final, um relatório no formato de CLAUDE.md: o que ficou pronto nesta rodada, o que preciso do Danilo (perguntas copiadas de "Preciso de você", prontas para responder) e quantas etapas faltam. Se o livro terminou, diga que o passo a passo do upload está no READY.md da pasta Entrega e envie os PDFs.
