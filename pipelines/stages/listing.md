# Etapa: listing

Chame o subagente `listing-writer` com slug. Ele segue `rules/skills/kdp-listing-copy.md` e grava:
- `listing/listing.md`: 3 títulos, 3 subtítulos (com justificativa de 1 linha), 7 keywords, categorias orientativas (3 principais + alternativas; o Danilo confirma no seletor do KDP), descrição em HTML, plano de A+.
- `listing/aplus-prompts.md`: prompts do Google Flow (só depois de o plano de A+ existir), com o checklist de anexos. Todo prompt leva o parágrafo "Safe margins" do template da skill (margem de segurança para o corte 16:9 -> 970 x 600).
- `listing/bonus-brevo.md` (se o livro promete bônus): textos do formulário (incluindo a mensagem de sucesso) e o e-mail de confirmação simples (que é o de entrega; nunca double opt-in), no modelo da skill ("Bonus Capture Texts").
Sem keyword primária validada: usa a do TOC e registra ASSUMIDA ("validar no Publisher Rocket"). Título/subtítulo: recomenda a opção 1 e registra ASSUMIDA; o Danilo escolhe no final.
`done` quando os arquivos existirem (o do bônus só se o livro tiver bônus) e a auditoria do human-voice tiver rodado.
