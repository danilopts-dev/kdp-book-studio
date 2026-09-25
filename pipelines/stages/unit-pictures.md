# Etapa: unidade ilustrada (livro infantil, páginas com imagem)

1. Confira se as imagens listadas para a unidade estão em `inputs/`. Faltando: BLOQUEANTE listando os arquivos (nome, cena, proporção, mín. 300 DPI no tamanho final com sangria).
2. Chame `writer` para o texto das páginas em `content/<id>.yaml` (`pages: [{image, text, mode: full|top|bottom}]`), seguindo `rules/formats/children.md`.
3. `./st check <slug> --unit <id>` e `./st preview <slug> "<páginas>"` (gera `build/sheet.png`); o `unit-reviewer` confere texto × imagem, legibilidade sobre a arte e área segura.
4. Sem 🔴: `done`.
