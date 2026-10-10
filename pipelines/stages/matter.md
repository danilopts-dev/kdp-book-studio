# Etapa: front/back matter

Chame o subagente `writer` com slug e a lista `front`/`back` do `book.yaml`. Ele escreve cada `content/_<nome>.md` que não seja automático (`title`, `copyright`, `toc` e `answers` são gerados pelo build). Itens comuns:
- `how-to-use` (atividades/planners): curto, prático, letra grande.
- `dedication` (opcional, só se o Danilo fornecer).
- `bonus`: página que entrega o bônus definido no TOC, com os itens de `bonus.items` e o QR como imagem: `![](bonus-qr.png "1.6in")`. Só QR, sem URL impressa. Se o QR ainda não existir, rode `./st qr <slug> --placeholder` e siga: o QR real entra na etapa `bonus`. Nunca bloqueie por falta de link.
- `review`: pedido de avaliação honesto, 3 a 5 frases, sem pressão, na voz do imprint.
- `about` / `also-by`: outros títulos do imprint (fonte: Notion "📖 Livros"; sem fonte, registre como "decidi sozinho").
Copyright: só crie `_copyright.md` se o padrão automático não servir (ex.: disclaimer médico/geral necessário).
Depois: `./st check <slug>` (vale para arquivos listados que faltam). Sem 🔴: `done`.
