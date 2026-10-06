# Perguntas e decisões — The 12-Week Decluttering Workbook

Formato: `- [ ] [BLOQUEANTE|ASSUMIDA] (etapa) pergunta — contexto`. Marque [x] quando resolvida e anote a resposta.
BLOQUEANTE impede a etapa indicada. ASSUMIDA já foi decidida pelo padrão mais conservador e só precisa da sua confirmação (ou correção).

## Abertas — precisam de você

- [ ] [BLOQUEANTE p/ cover e listing] (cover) **Arte da capa.** Pendente, a pedido do Danilo (2026-10-05). O estúdio gera o guia de capa (medidas e lombada pelas 122 páginas); a arte é do Danilo, em `inputs/cover-front.png` (e `cover-back.png`, opcional). Destrava o PDF da capa e os prompts do Google Flow para o A+.

## Em produção (fora do livro)

- [ ] (bônus) **Printable Declutter Kit — subir no Brevo.** PDF criado em 2026-10-06 (`bonus/printable-declutter-kit.pdf`, 15 págs, US Letter, P&B; fonte editável `bonus/kit.typ`). Tem os 3 itens prometidos: fluxograma Keep / Donate / Sell / Toss (p. 2), checklists dos 12 cômodos para o reset mensal (p. 3-14) e tracker de 12 semanas para a geladeira (p. 15), mais uma página de como usar. Falta só você anexar o PDF na automação do Brevo e testar o QR.

## Resolvidas
- [x] (listing) **Keywords.** Danilo não usa Publisher Rocket; ficam as 7 keywords definidas no listing (2026-10-05).
- [x] (unit:wk01, wk03) **Fatos FDA e USDA.** Conferidos em 2026-10-05 contra as páginas oficiais enviadas pelo Danilo (cópias em `inputs/reference/sources/`). Corrigido: (1) ordem da FDA para remédios agora é take-back → flush list → lixo (antes o lixo vinha antes da flush list); (2) protetor solar: removida a exceção de "estável por 3 anos" e a regra de "3 anos após a compra", que não constam da fonte; fica só "é regulado como medicamento e precisa ter validade impressa"; (3) take-back: só farmácia e delegacia, busca por CEP no site da DEA e envelope pré-pago pelos Correios (removidos hospitais, clínicas e o Take Back Day); (4) cosméticos: removido o "open-jar symbol", incluído o rímel de 2 a 4 meses; (5) wk03: datas de comida indicam qualidade, não segurança; descartar pelo estado do alimento, não só pela data.
- [x] (unit:wk09) **Linhas de hábito na tabela de documentos** (contas, garantias, apólices como "general habit, not a rule"): aprovadas como estão (2026-10-05).
- [x] (unit:intro, wk00) **Método de desempate:** a pergunta "If this were gone tomorrow, would I go out and buy it again?" e o valor mínimo de venda definido na Week 0 foram aprovados (2026-10-05).
- [x] (intake, matter) **Livro irmão.** São duas edições com o mesmo título principal: "House Cleaning Checklist Planner: Weekly & Monthly Cleaning Checklists, Home Routines, and Declutter Tools to Keep Your Home Organized" (P&B, ASIN B0G4FBVC3X) e "House Cleaning Checklist Planner: Full Color Weekly and Monthly Cleaning Checklists, Home Routines, and Declutter Tools to Keep Your Home Organized" (colorida, ASIN B0GTRDW4RQ). O miolo cita o título principal; o Final Words diz que existe nas duas edições.
- [x] (conclusion, matter) **Série.** Dizer só que outros livros da Emily virão, sem temas nem títulos (o próximo é o End of Life Planner, fora do tema casa). Conclusion e Final Words ajustados (2026-10-05).

- [x] (intake, listing) **Título e subtítulo.** Aprovados em 2026-09-30: "The 12-Week Decluttering Workbook" / "15 Minutes a Day, One Room a Week: Keep, Donate, Sell or Toss Your Way Through the Whole House, No Storage Bins Required". Keyword primária no book.yaml: decluttering workbook.
- [x] (intake) **Nome jurídico no copyright:** Read Publishing LLC (confirmado pelo Danilo).
- [x] (intake) **Livro sem data (undated).** Confirmado em 2026-10-04. Semanas numeradas de 0 a 12, datas em branco para o leitor preencher; a página de copyright diz que o livro pode ser começado em qualquer semana do ano.
- [x] (matter) **Link do bônus.** Decidido em 2026-10-04: só o QR code (inputs/bonus-qr.png), sem link em texto, porque o link do Brevo é longo. A página diz "scan the code below with your phone's camera".
- [x] (matter) **Fim do livro.** Decidido em 2026-10-04: as páginas "A Small Favor" e "Also by" viraram uma só, "Final Words", com o pedido de review, o contato hello@readpublishingco.com e o link https://www.readpublishingco.com/#emily para os outros títulos da autora.
- [x] (matter) **Página de copyright.** Ajustada em 2026-10-04: letra pequena, centralizada na vertical, com mais conteúdo (título e subtítulo, editora, site e e-mail, primeira edição, fontes do miolo, aviso legal ampliado).
- [x] (listing) **Prompts do Google Flow** só depois da arte da capa e da aprovação do plano de A+ (incorporado à pendência da capa acima).

## Decisões técnicas registradas (não precisam de resposta)

- Visual do miolo: tema único em `theme.typ` (aprovado pelo Danilo em 2026-10-01), fontes Atkinson Hyperlegible e Barlow (OFL) em `fonts/`.
- Orientação semanal (150–250 palavras) escrita dentro da unidade de cada semana, não como capítulo separado.
- Layout semanal fixo de 7 páginas: orientação + 7 tarefas, 4 folhas do cômodo, "Where It's Going This Week", "Keep / Donate / Sell / Toss Count" com Notes e Wins.
- Fatos do TOC marcados [REVISAR] verificados em fonte oficial, com URL em notes.md.
- wk02: "Plan Your Landing Zone" tem coluna "Who uses it" para famílias, sem nomes.
- wk04 e wk05: descarte de eletrônicos e baterias só como "check your local guidelines", sem regra específica.
- wk06: o TOC fala em humor e sono; omitido por regra do style sheet (sem claims de saúde).
- wk08: duas trilhas na mesma semana (crianças ou hobby); a frase sobre crianças brincarem mais com menos brinquedos foi suavizada para "Many parents find…".
- part3: Sell Tracker e Donation Log com 5 páginas cada e uma página "Part 3 Totals" que alimenta o placar da Conclusion.
- part4: tracker do reset mensal em 2 páginas (meses 1–6 e 7–12), com os 12 cômodos da Week 0.
- Conclusion: "Items out" = Donate + Sell + Toss; horas = dias trabalhados × 15 minutos.
