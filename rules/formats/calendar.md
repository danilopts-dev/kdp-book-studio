# Formato: calendários

Padrões do engine: 8.5x11, um mês por página, grade de 7 colunas, notas por dia (feriados, festas, parashá), data hebraica opcional.

- Mercado EUA: semana começa no domingo. Outros mercados: confirmar no intake.
- Feriados EUA via `holidays`; datas judaicas, festas, jejuns e parashá via `pyluach` (diáspora por padrão).
- Ano de validade: calendário 2027 publicado até ~agosto de 2026 para pegar a temporada; confirmar no intake.
- Páginas extras comuns: visão anual, datas importantes, notas (use `kind: typst`).

## Checklist de revisão
- 12 meses completos; dia da semana do dia 1 conferido em 3 meses; Rosh Hashaná, Yom Kipur, Pessach e Chanucá conferidos no JSON em `build/data/`.
- Transliteração consistente com o style sheet.
- Nenhuma nota cortada na célula (inspeção visual).
