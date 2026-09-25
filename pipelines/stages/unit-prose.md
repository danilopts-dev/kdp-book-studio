# Etapa: unidade de prosa (capítulo, introdução, conclusão)

Orquestrada pela sessão principal. Três passos: redação, checagem por script e revisão de olhos frescos.

1. **Pré-condição**: leia no `book.yaml` só a entrada da unidade. Se `raw` contiver `[DANILO: needs input]` e não houver material em `inputs/raw/<id>.md` nem resposta em `questions.md`, bloqueie a unidade (BLOQUEANTE, pedindo 5 a 10 itens concretos). Exceção: introdução/conclusão que só costuram o livro podem seguir.
2. **Redação**: chame o subagente `writer` com: slug, id da unidade. Ele escreve `content/<id>.md` e acrescenta o resumo em `notes.md`.
3. **Checagem**: `./st check <slug> --unit <id>` e `./st voice <slug> --unit <id>`. Guarde a saída (curta).
4. **Revisão**: chame o subagente `unit-reviewer` com: slug, id, e a saída dos dois scripts colada (é curta). Ele corrige o arquivo direto e devolve os achados restantes.
5. Rode os dois scripts de novo. Se ainda houver 🔴 ou violação de voz, uma segunda rodada do `unit-reviewer`; se persistir, bloqueie com a pergunta objetiva.
6. `done` com nota: nº de palavras + "voz OK".
