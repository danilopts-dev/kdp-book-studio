# Etapa: listing (página da Amazon)

Chame o subagente `listing-writer` com slug. Ele segue `rules/skills/kdp-listing-copy.md` e grava:

- `listing/keywords-research.md`: saída de `./st keywords <slug> "<semente 1>" "<semente 2>" ...` (3 a 6 sementes tiradas do TOC: tema + formato, tema + público, tema + presente). São buscas reais de compradores no autocomplete de Livros da Amazon.com. Na nuvem a Amazon costuma bloquear; aí o arquivo diz isso e as keywords saem como "ideia (não confirmada)".
- `listing/listing.md`, nesta ordem:
  1. **Keywords** (primeiro, porque título e subtítulo dependem delas): keyword principal recomendada + 2 alternativas; os 7 campos de keyword do KDP (até 50 caracteres cada, sem repetir palavras do título); 15 a 25 termos para a campanha de lançamento no Amazon Ads; cada termo marcado "busca real" (veio do autocomplete) ou "ideia".
  2. 3 títulos e 3 subtítulos (com justificativa de 1 linha), todos usando a keyword principal.
  3. Categorias orientativas (3 principais + alternativas; o Danilo confirma no seletor do KDP).
  4. Descrição em HTML.
  5. Plano de A+.
- `listing/aplus-prompts.md`: prompts do Google Flow (só depois de o plano de A+ existir), com o checklist de anexos. Todo prompt leva o parágrafo "Safe margins" do template da skill (margem de segurança para o corte 16:9 -> 970 x 600).

Os textos do bônus no Brevo não são desta etapa: ficam na etapa `bonus`.

Keyword principal: se o `book.yaml` já tiver `primary_keyword` validada, use-a. Senão, recomende a partir da pesquisa e registre como "decidi sozinho" ("validar no Publisher Rocket se quiser"). Título/subtítulo: recomenda a opção 1 e registra; o Danilo escolhe no final.
`done` quando os arquivos existirem e a auditoria do human-voice tiver rodado.
