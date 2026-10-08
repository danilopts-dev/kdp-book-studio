# Etapa: listing

Chame o subagente `listing-writer` com slug. Ele segue `rules/skills/kdp-listing-copy.md` e grava:
- `listing/listing.md`: 3 títulos, 3 subtítulos (com justificativa de 1 linha), 7 keywords, descrição em HTML, plano de A+.
- `listing/aplus-prompts.md`: prompts do Google Flow (só depois de o plano de A+ existir), com o checklist de anexos.
- `listing/bonus-brevo.md` (se o livro promete bônus): textos do formulário (incluindo a mensagem de sucesso), e-mail de confirmação (double opt-in, se houver) e e-mail de entrega, no modelo da skill ("Bonus Capture Texts").
Sem keyword primária validada: usa a do TOC e registra ASSUMIDA ("validar no Publisher Rocket"). Título/subtítulo: recomenda a opção 1 e registra ASSUMIDA; o Danilo escolhe no final.
`done` quando os arquivos existirem (o do bônus só se o livro tiver bônus) e a auditoria do human-voice tiver rodado.
