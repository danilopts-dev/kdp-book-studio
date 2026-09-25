# Etapa: unidade livre em Typst (planners, organizers, trackers, formatos novos)

1. Chame `activity-builder` com slug e id. Ele escreve `content/<id>.typ` usando os blocos de `studio/render/lib.typ` (`lined-page`, `tracker`, `checklist`, `month-page`...) ou Typst puro, conforme `rules/formats/planner.md`. Imagens com caminho absoluto `/books/<slug>/inputs/...`.
2. `./st preview <slug> "<páginas>"` (gera `build/sheet.png`). Se o layout for novo, o `unit-reviewer` inspeciona a folha.
3. Se o formato novo for reaproveitável, proponha (ASSUMIDA) promover o bloco para `lib.typ`.
4. Sem 🔴: `done`.
