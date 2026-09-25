# Etapa: unidade de calendário

1. Chame `activity-builder` com slug e id. Ele escreve `content/<id>.yaml` (ano, início da semana, feriados EUA, datas judaicas, meses, nomes dos dias) conforme `rules/formats/calendar.md`.
2. Datas, dias da semana, feriados e datas judaicas vêm de biblioteca (`holidays`, `pyluach`). O modelo **nunca** digita datas de memória.
3. `./st preview <slug> "<páginas do calendário>"` (gera `build/sheet.png`). O `unit-reviewer` confere visualmente um mês e compara 3 datas-chave com a fonte (ex.: Rosh Hashaná, Thanksgiving, Pessach) consultando o JSON em `build/data/<id>.json`.
4. Sem 🔴: `done`.
