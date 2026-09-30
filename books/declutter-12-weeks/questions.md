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
