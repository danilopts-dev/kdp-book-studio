# Perguntas e decisões

Formato: `- [ ] [BLOQUEANTE|ASSUMIDA] (etapa) pergunta — assumido: ...`. Marque [x] quando resolvida.

## Abertas
- [ ] [BLOQUEANTE p/ finalize] (matter) Link/QR real do Printable Declutter Kit — placeholder [DANILO: bonus link + QR code] em _bonus.md, a pedido do Danilo
- [ ] [ASSUMIDA] (matter) Página do bônus (Printable Declutter Kit) com link/QR placeholder, a pedido do Danilo. ATENÇÃO: o check final bloqueia placeholder; precisa do link real antes do build final.
- [ ] [ASSUMIDA] (intake) Livro sem data (undated), semanas 0-12 numeradas; 8,5x11 P&B, alvo 120-140 páginas (preset planner).
- [ ] [ASSUMIDA] (intake) Orientação semanal (150-250 palavras) escrita dentro da unidade typst de cada semana, não como unidade de prosa separada, para economizar tarefas; segue human-voice-writing.
- [ ] [ASSUMIDA] (intake) Referência cruzada ao *House Cleaning Checklist Planner* (título do docx do Drive "03 - House Cleaning Checklist"); visual alinhado pela estrutura do docx (blocos de 15 min, Notes + Wins). Texto integral do livro em inputs/reference/house-cleaning-checklist-planner.md (enviado pelo Danilo).
- [ ] [ASSUMIDA] (intake) Fatos [REVISAR] do TOC verificados pelos agentes da unidade em fonte oficial (FDA, IRS), com URL em notes.md; se não confirmar, vira BLOQUEANTE.
- [ ] [ASSUMIDA] (intake) Copyright com disclaimer curto (informativo, não é conselho fiscal/médico) — criar `_copyright.md` na etapa matter.
- [ ] [ASSUMIDA] (intake) also-by: só o House Cleaning Checklist Planner; próximos livros da série citados de forma genérica (sem títulos).
- [ ] [ASSUMIDA] (unit:intro) Regra de desempate das quatro caixas: "If this were gone tomorrow, would I go out and buy it again?" + valor mínimo de venda definido pelo leitor na Week 0 (Donate abaixo dele). Sem caixa "maybe". wk00 deve incluir o campo do valor.
- [ ] [ASSUMIDA] (listing) Keyword primária "decluttering workbook" (SERP ~$61k/mês, workbooks KDP guiados $540-1.700/mês), secundária "room by room declutter"; base: análise de 2026-09-21 no Drive (SellerSprite, sem volume de busca). Validar no Publisher Rocket.
- [ ] [ASSUMIDA] (listing) Prompts do Google Flow (aplus-prompts.md) só depois da arte da capa e da aprovação do plano de A+.

## Resolvidas
- [x] [ASSUMIDA] (intake) Título provisório "Clear the Clutter in 12 Weeks", sem subtítulo; decisão final no listing (evitar "challenge"). Pedido do Danilo. — Danilo aprovou (2026-09-30): "The 12-Week Decluttering Workbook" / "15 Minutes a Day, One Room a Week: Keep, Donate, Sell or Toss Your Way Through the Whole House, No Storage Bins Required".
- [x] [ASSUMIDA] (listing) Recomendado título opção 1 "The 12-Week Decluttering Workbook" + subtítulo opção 1. Se aprovado, atualizar title/subtitle/primary_keyword no book.yaml (folha de rosto) e na capa. Danilo escolhe. — Danilo aprovou (2026-09-30): "The 12-Week Decluttering Workbook" / "15 Minutes a Day, One Room a Week: Keep, Donate, Sell or Toss Your Way Through the Whole House, No Storage Bins Required".
- [x] [ASSUMIDA] (intake) copyright_holder = "Read Publishing LLC" — Danilo confirmou: Read Publishing LLC
- [ ] [ASSUMIDA] (unit:wk01) Helpers do layout semanal `_wk-*` ficam em content/wk01.typ (inline); sugestão de promover a studio/render/lib.typ. wk01 tem 7 páginas com 6 folhas + Count/Notes/Wins na última. Fatos FDA confirmados só via resultados de busca (fda.gov bloqueado no fetch); validar antes do build final. Regra de cosméticos mantida genérica (sem prazos em meses).

- [ASSUMIDA] wk02: "Plan Your Landing Zone" inclui coluna "Who uses it" para o caso de família (sem nomear pessoas); sem fatos [REVISAR] nesta semana. Sugestão de mail-stop (cancelar correio) só como campo em branco, sem citar serviços.
- [ASSUMIDA] wk03: frase sobre datas de alimentos (USDA) genérica, sem prazos; conferência humana rápida recomendada.

- [ASSUMIDA] wk04: nenhum fato [REVISAR] no TOC; usei só orientação genérica (vidro quebrado embrulhado, "check your local guidelines" para eletrônicos) sem afirmações regulatórias. Cabeçalho de página 1 reduzido (~170 palavras) para caber as 7 tarefas na mesma página.

- [ASSUMIDA] wk05: "Discs, Books and Magazines" e "Media, Cables and Remotes" cobrem mídia/cabos/revistas do TOC; página de acordo familiar = "What Stays in the Living Room". Sem fato externo a verificar (descarte de eletrônicos só "check your local guidelines").

- [ASSUMIDA] wk06: o TOC diz "cômodo que mais afeta o humor e o sono"; omitido da orientação por regra do style sheet (sem claims de saúde). Página "How I Want My Bedroom to Look" cobre o espaço para anotar como o quarto deve ficar.
- ASSUMIDA (wk07): nenhuma nova; usou o layout semanal padrão e _wk-blank para campos em branco em cabeçalhos de tabela.
- ASSUMIDA wk09: linhas de bills/warranties/insurance na tabela de retenção são hábito geral conservador (não regra), sem fonte oficial; revisão humana opcional.

- [ASSUMIDA] part3: Sell Tracker e Donation Log com 5 páginas cada (22 e 20 linhas de ~0,33"), página final "Part 3 Totals" que alimenta a Conclusion; continuações sem heading para não inflar o sumário. Linhas ampliadas pelo orquestrador após a contact sheet (antes ~0,25").
- [ASSUMIDA] part4: tracker mensal dividido em 2 páginas (Month 1-6, 7-12) com 12 cômodos de Week 0; p6 tem tabela própria de planejamento da rotina (dia/hora por cômodo) em vez de descrever o conteúdo do outro livro.
- ASSUMIDA conclusion: "Items out" = Donate + Sell + Toss (Keep não conta como saída); horas = dias trabalhados × 15 min; placar sem linha separada para Keep.
