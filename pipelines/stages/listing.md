# Etapa: listing

Chame o subagente `listing-writer` com slug. Ele segue `rules/skills/kdp-listing-copy.md` e grava:
- `listing/listing.md`: 3 títulos, 3 subtítulos (com justificativa de 1 linha), 7 keywords, descrição em HTML, plano de A+.
- `listing/aplus-prompts.md`: prompts do Google Flow (só depois de o plano de A+ existir), com o checklist de anexos.
Sem keyword primária validada: usa a do TOC e registra ASSUMIDA ("validar no Publisher Rocket"). Título/subtítulo: recomenda a opção 1 e registra ASSUMIDA; o Danilo escolhe no final.
`done` quando os dois arquivos existirem e a auditoria do human-voice tiver rodado.
