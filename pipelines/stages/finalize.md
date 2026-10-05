# Etapa: finalize

1. `./st check <slug> --pdf` final. Qualquer 🔴: volte à tarefa responsável (`/etapa`).
2. Escreva `books/<slug>/READY.md` com: arquivos para upload (miolo, capa ou guia), especificações KDP (trim, papel, bleed, páginas), listing recomendado, e a lista de **todas as ASSUMIDAS** para o Danilo validar.
3. `./st publish <slug>`: copia miolo, capa/guia, listing e READY.md para `Entrega/` na pasta do livro no OneDrive (no-op se `local.yaml` não existir).
4. Notion (se disponível): status do livro e nota "Pronto para upload — ver READY.md".
5. Na nuvem: `git push`. Envie os PDFs ao Danilo pelo SendUserFile (miolo + capa/guia) quando a sessão for na nuvem.
