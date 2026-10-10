---
description: Cria um livro novo a partir do TOC aprovado. Uso /novo-livro (e cole o TOC), ou /novo-livro <título> [tipo] [imprint]
argument-hint: [título] [tipo] [imprint]
---
Argumentos: $ARGUMENTS

O Danilo não precisa saber nomes de pasta nem tipos técnicos. Deduza do TOC o que der:
- **Apelido da pasta**: você cria, curto, em minúsculas e com hífens, a partir do título (ex.: "8 Nights of Hanukkah Activity Book" → `hanukkah-8-nights`). Não pergunte e não mostre ao Danilo.
- **Tipo**: `prose` (guias, textos), `activity` (puzzles, atividades), `calendar`, `planner` (organizers, trackers), `children` (livro ilustrado). Deduza do TOC; só pergunte se for ambíguo, com as opções em português.
- **Imprint**: golden-chapter, silvia-press, emily-harper, jonah-feldman. Deduza do TOC/público; pergunte só se não der.
- **Pasta no OneDrive**: pergunte o nome ("NN - Título", ex.: "16 - Passover Activity Book") se ele não disse.

1. Sem TOC na conversa: peça que cole o TOC aprovado (ou diga onde está no Notion) e pare.
2. `./st new <apelido> --type <tipo> --imprint <imprint> --onedrive "<pasta>"` (o `--onedrive` cria o atalho do estúdio dentro da pasta do livro).
3. Grave o TOC em `books/<apelido>/toc.md` e execute a tarefa `intake` seguindo `pipelines/stages/_protocol.md`.
4. Reporte em até 5 linhas, no formato de CLAUDE.md: quantos capítulos/seções o livro terá, se tem bônus, o que preciso dele (se algo) e como seguir ("é só dizer /proximo ou /tudo").
