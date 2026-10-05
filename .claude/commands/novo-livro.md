---
description: Cria um livro novo a partir do TOC aprovado. Uso /novo-livro <slug> <prose|activity|calendar|planner|children> [imprint]
argument-hint: <slug> <tipo> [imprint]
---
Argumentos: $ARGUMENTS

1. Rode `./st new <slug> --type <tipo>` (com `--imprint <imprint>` se informado; com `--onedrive "NN - Título"` se o Danilo informar a pasta do livro no OneDrive: cria o atalho `Estudio` lá dentro; imprints: golden-chapter, silvia-press, emily-harper, jonah-feldman).
2. Se o Danilo colou o TOC nesta conversa, grave-o em `books/<slug>/toc.md`. Se não, peça que cole (ou informe o caminho/página do Notion onde está) e pare.
3. Com o TOC gravado, execute a tarefa `intake` seguindo `pipelines/stages/_protocol.md`.
4. Reporte em até 5 linhas: unidades criadas, perguntas BLOQUEANTES (se houver) e o próximo comando sugerido (`/proximo <slug>` ou `/tudo <slug>`).
