# Formato: planners e organizers

Construídos como `kind: typst`, com os blocos `lined-page`, `tracker`, `checklist` e `month-page` de `studio/render/lib.typ`, ou Typst livre para layouts novos.

- Definir no intake: datado ou sem data, início da semana, seções (mensal, semanal, trackers, notas) e contagem de páginas alvo.
- Planner datado: datas por código (`studio/generators/calendar.py`), nunca digitadas.
- Consistência: o mesmo tipo de página usa o mesmo layout do começo ao fim.
- Layout novo e reaproveitável: promover para `lib.typ` (registrar ASSUMIDA).

## Checklist de revisão
- Datas e dias da semana corretos; nenhuma semana faltando ou duplicada.
- Espaço de escrita suficiente (linhas ≥ 0,3" de altura).
- Margem interna respeitada nas páginas espelhadas.
