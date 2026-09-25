# Protocolo de execução de uma tarefa

Usado por `/proximo`, `/tudo` e `/etapa`. Quem executa é a sessão principal (orquestrador).

0. **Destravar respostas** (uma vez por comando): se o Danilo respondeu alguma pergunta BLOQUEANTE, seja na conversa ou marcando `[x]` com a resposta em `questions.md`, mova-a para "Resolvidas" com a resposta. Se o material veio na conversa, grave-o em `inputs/raw/<id>.md`. Depois rode `./st mark <slug> <tarefa> pending` para cada tarefa destravada.
1. **Pegar a tarefa**: `./st next <slug> --runnable` (ou a tarefa indicada em `/etapa`). Se vier `"id": null`, pare e informe o motivo (concluído, ou os bloqueios listados em `blocked`, com as perguntas).
2. **Contexto mínimo**: leia só o necessário para a etapa (o arquivo de `instructions`); o resto fica com os subagentes.
3. `./st mark <slug> <tarefa> in_progress`
4. **Executar** seguindo o arquivo em `instructions` da tarefa (`pipelines/stages/...`). Ele diz quais subagentes chamar e quais scripts rodar.
   - Ao chamar subagente, use o `subagent_type` indicado e passe só: slug, id da tarefa/unidade, caminho das instruções e o que a etapa pede. Nada de colar conteúdo.
   - Rode subagentes em primeiro plano (a próxima ação depende do resultado).
5. **Fechar**:
   - Sucesso sem 🔴: `./st mark <slug> <tarefa> done --note "<resumo de até 12 palavras>"`.
   - Bloqueio: registre em `questions.md` (`- [ ] [BLOQUEANTE] (<tarefa>) <pergunta objetiva> — contexto: <1 linha>`) e rode `./st mark <slug> <tarefa> blocked --note "<motivo curto>"`.
   - Suposições: registre como `- [ ] [ASSUMIDA] (<tarefa>) <o que decidiu e por quê>`. Não param nada.
6. **Commit**: `git add books/<slug> && git commit -qm "<slug>: <tarefa>"`.
7. **Reportar ao Danilo** em até 3 linhas: o que foi feito, perguntas novas (se houver) e quantas tarefas faltam.

Em `/tudo`, volte ao passo 1 depois do passo 6 e reporte só no final (ou num bloqueio geral). Se o contexto da sessão estiver ficando grande, não releia arquivos já processados: confie em `./st status` e `notes.md`.
