# Etapa: revisão editorial do livro inteiro

1. `./st preview <slug> "1-6,<2 aberturas de capítulo>,<2 páginas de atividade>,<answer key>,last"`.
2. Chame o subagente `book-editor` com slug. Ele:
   - roda a revisão completa de `rules/skills/kdp-editorial-review.md` (TOC × conteúdo, consistência, voz, formato) lendo os arquivos-fonte (MD/YAML), não o PDF;
   - inspeciona `build/sheet.png` (layout, fontes, respiros, grids, cabeçalhos);
   - corrige 🔴/🟠 direto nos arquivos-fonte e grava o relatório em `reviews/editorial.md`.
3. Se houve correção: `./st build <slug>` e `./st check <slug> --pdf` de novo.
4. Sem 🔴: `done`. 🟠 que exigem decisão viram perguntas.
