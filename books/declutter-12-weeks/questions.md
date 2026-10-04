# Perguntas e decisões — The 12-Week Decluttering Workbook

Formato: `- [ ] [BLOQUEANTE|ASSUMIDA] (etapa) pergunta — contexto`. Marque [x] quando resolvida e anote a resposta.
BLOQUEANTE impede a etapa indicada. ASSUMIDA já foi decidida pelo padrão mais conservador e só precisa da sua confirmação (ou correção).

## Abertas — precisam de você

- [ ] [BLOQUEANTE p/ cover e listing] (cover) **Arte da capa.** O estúdio gera o guia de capa (medidas, lombada pelas 122 páginas, área segura), mas a arte da frente e do verso é sua. Coloque em `inputs/cover-front.png` (e `inputs/cover-back.png`, se tiver). Sem ela não sai o PDF da capa nem os prompts do Google Flow para o A+, que usam a capa como referência em todas as imagens.

- [ ] [ASSUMIDA] (listing) **Confirmar a keyword "decluttering workbook" no Publisher Rocket.** Ela foi escolhida com base na receita da SERP (análise de 21/09 no Drive, SellerSprite): cerca de $61k/mês, com workbooks guiados KDP vendendo $540–1.700/mês. A análise não traz volume de busca. Se o Rocket mostrar volume baixo para esse termo, o título aprovado ainda funciona, mas as 7 keywords do backend podem precisar de ajuste.

- [ ] [ASSUMIDA] (unit:wk01, wk03) **Conferir três fatos de saúde/alimentos.** Foram confirmados só por resultados de busca, porque o fetch direto no site oficial foi bloqueado. Basta abrir as páginas e conferir se o texto do livro bate:
  - wk01, descarte de remédios (programas de take-back; lixo comum misturado com borra de café ou areia de gato; a "flush list" só para os remédios listados): https://www.fda.gov/drugs/safe-disposal-medicines/disposal-unused-medicines-what-you-should-know
  - wk01, protetor solar tem data de validade obrigatória, exceto se estável por 3 anos; cosméticos não têm validade exigida por lei nos EUA: https://www.fda.gov/cosmetics/cosmetics-labeling/shelf-life-and-expiration-dating-cosmetics
  - wk03, datas em alimentos são estimativa de qualidade e não são exigidas por lei federal, exceto em fórmula infantil: https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/food-product-dating
  (Os fatos do IRS na wk09 e na Part 3 foram conferidos direto no irs.gov e não precisam de revisão.)

- [ ] [ASSUMIDA] (unit:wk09) **Prazos que não são do IRS na tabela de documentos.** A tabela "How Long to Keep Your Papers" mistura regras oficiais do IRS (marcadas "IRS: …") com hábitos comuns para contas, garantias e apólices (marcados "general habit, not a rule"). Confirmar se você quer manter essas linhas de hábito ou deixar só o que é regra oficial.

- [ ] [ASSUMIDA] (unit:intro, wk00) **Método de desempate.** O livro inteiro usa duas regras que não estavam no TOC e foram criadas na introdução: (1) a pergunta "If this were gone tomorrow, would I go out and buy it again?" (sim = Keep; não = sai); (2) um valor mínimo de venda que o leitor define na Week 0 (abaixo dele, Donate; igual ou acima, Sell). Não existe caixa "maybe": na dúvida, o item fica como "Keep for now" e é revisto no reset mensal da Part 4. Confirmar que esse é o método que você quer como marca do livro.

- [ ] [ASSUMIDA] (matter) **Conteúdo do Printable Declutter Kit.** A página do bônus e os textos do Brevo prometem 3 itens: o flowchart Keep / Donate / Sell / Toss, checklists por cômodo para reimprimir a cada reset e um tracker de 12 semanas para a geladeira. O PDF do kit no OneDrive está protegido por senha e não deu para conferir. Confirmar que ele tem exatamente esses 3 itens (ou me dizer o que tem, que eu ajusto o texto).

- [ ] [ASSUMIDA] (intake, matter) **Referências ao livro irmão.** O livro cita o *House Cleaning Checklist Planner* (na wk10, na Part 4, na Conclusion e no Final Words) com esse título exato. Confirmar se é o título como aparece na Amazon.

- [ ] [ASSUMIDA] (conclusion, matter) **Promessa de série.** A Conclusion diz que há outros livros a caminho, cada um sobre uma parte da casa (closets, cozinha, garagem, papelada, downsizing), sem citar títulos. Se a série não for sair, troco por uma frase que não prometa lançamentos.

## Resolvidas

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
