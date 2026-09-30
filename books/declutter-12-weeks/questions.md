# Perguntas e decisões

Formato: `- [ ] [BLOQUEANTE|ASSUMIDA] (etapa) pergunta — assumido: ...`. Marque [x] quando resolvida.

## Abertas
- [ ] [ASSUMIDA] (intake) copyright_holder = "Read Publishing LLC" (como no House Cleaning). O House Cleaning diz também "Published by Read KDP, LLC": confirmar qual é o nome jurídico certo.
- [ ] [ASSUMIDA] (intake) Título provisório "Clear the Clutter in 12 Weeks", sem subtítulo; decisão final no listing (evitar "challenge"). Pedido do Danilo.
- [ ] [ASSUMIDA] (matter) Página do bônus (Printable Declutter Kit) com link/QR placeholder, a pedido do Danilo. ATENÇÃO: o check final bloqueia placeholder; precisa do link real antes do build final.
- [ ] [ASSUMIDA] (intake) Livro sem data (undated), semanas 0-12 numeradas; 8,5x11 P&B, alvo 120-140 páginas (preset planner).
- [ ] [ASSUMIDA] (intake) Orientação semanal (150-250 palavras) escrita dentro da unidade typst de cada semana, não como unidade de prosa separada, para economizar tarefas; segue human-voice-writing.
- [ ] [ASSUMIDA] (intake) Referência cruzada ao *House Cleaning Checklist Planner* (título do docx do Drive "03 - House Cleaning Checklist"); visual alinhado pela estrutura do docx (blocos de 15 min, Notes + Wins). Texto integral do livro em inputs/reference/house-cleaning-checklist-planner.md (enviado pelo Danilo).
- [ ] [ASSUMIDA] (intake) Fatos [REVISAR] do TOC verificados pelos agentes da unidade em fonte oficial (FDA, IRS), com URL em notes.md; se não confirmar, vira BLOQUEANTE.
- [ ] [ASSUMIDA] (intake) Copyright com disclaimer curto (informativo, não é conselho fiscal/médico) — criar `_copyright.md` na etapa matter.
- [ ] [ASSUMIDA] (intake) also-by: só o House Cleaning Checklist Planner; próximos livros da série citados de forma genérica (sem títulos).
- [ ] [ASSUMIDA] (unit:intro) Regra de desempate das quatro caixas: "If this were gone tomorrow, would I go out and buy it again?" + valor mínimo de venda definido pelo leitor na Week 0 (Donate abaixo dele). Sem caixa "maybe". wk00 deve incluir o campo do valor.

## Resolvidas
- [ ] [ASSUMIDA] (unit:wk01) Helpers do layout semanal `_wk-*` ficam em content/wk01.typ (inline); sugestão de promover a studio/render/lib.typ. wk01 tem 7 páginas com 6 folhas + Count/Notes/Wins na última. Fatos FDA confirmados só via resultados de busca (fda.gov bloqueado no fetch); validar antes do build final. Regra de cosméticos mantida genérica (sem prazos em meses).

- [ASSUMIDA] wk02: "Plan Your Landing Zone" inclui coluna "Who uses it" para o caso de família (sem nomear pessoas); sem fatos [REVISAR] nesta semana. Sugestão de mail-stop (cancelar correio) só como campo em branco, sem citar serviços.
- [ASSUMIDA] wk03: frase sobre datas de alimentos (USDA) genérica, sem prazos; conferência humana rápida recomendada.

- [ASSUMIDA] wk04: nenhum fato [REVISAR] no TOC; usei só orientação genérica (vidro quebrado embrulhado, "check your local guidelines" para eletrônicos) sem afirmações regulatórias. Cabeçalho de página 1 reduzido (~170 palavras) para caber as 7 tarefas na mesma página.

- [ASSUMIDA] wk05: "Discs, Books and Magazines" e "Media, Cables and Remotes" cobrem mídia/cabos/revistas do TOC; página de acordo familiar = "What Stays in the Living Room". Sem fato externo a verificar (descarte de eletrônicos só "check your local guidelines").

- [ASSUMIDA] wk06: o TOC diz "cômodo que mais afeta o humor e o sono"; omitido da orientação por regra do style sheet (sem claims de saúde). Página "How I Want My Bedroom to Look" cobre o espaço para anotar como o quarto deve ficar.
- ASSUMIDA (wk07): nenhuma nova; usou o layout semanal padrão e _wk-blank para campos em branco em cabeçalhos de tabela.
- ASSUMIDA wk09: linhas de bills/warranties/insurance na tabela de retenção são hábito geral conservador (não regra), sem fonte oficial; revisão humana opcional.
