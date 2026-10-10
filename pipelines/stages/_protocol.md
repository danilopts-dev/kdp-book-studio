# Protocolo de execução de uma tarefa

Usado por `/proximo`, `/tudo` e `/etapa`. Quem executa é a sessão principal (orquestrador).

0. **Destravar respostas** (uma vez por comando): se o Danilo respondeu alguma pergunta (na conversa ou marcando `[x]` em `questions.md`), mova-a para "Resolvidas" com a resposta em 1 linha. Material que veio na conversa vai para `inputs/raw/<id>.md`; links (PDF do bônus, formulário) vão para o lugar que a etapa indica. Depois `./st mark <slug> <tarefa> pending` em cada tarefa destravada.
1. **Pegar a tarefa**: `./st next <slug> --runnable` (ou a tarefa indicada em `/etapa`). Se vier `"id": null`, pare e informe o motivo (livro pronto, ou o que está esperando o Danilo).
2. **Contexto mínimo**: leia só o arquivo de `instructions` da etapa; o resto fica com os subagentes.
3. `./st mark <slug> <tarefa> in_progress`
4. **Executar** seguindo o arquivo em `instructions` (`pipelines/stages/...`). Ele diz quais subagentes chamar e quais scripts rodar.
   - Ao chamar subagente, use o `subagent_type` indicado e passe só: slug, id da tarefa/unidade, caminho das instruções e o que a etapa pede. Nada de colar conteúdo.
   - Rode subagentes em primeiro plano (a próxima ação depende do resultado).
5. **Projeção de páginas** (só uma vez por livro, logo depois da 1ª unidade concluída, e se o `book.yaml` tiver `target_pages`): `./st estimate <slug>`. Se vier `alert`, pergunte ao Danilo já, com proposta (aceitar menos páginas, acrescentar atividades, páginas de notas). No Hanukkah isso só apareceu no fim (64 páginas contra 96 a 104 do TOC) e custou uma expansão inteira. Não pare a produção por isso: registre com a marca `[PRECISO]`, sem bloquear tarefa.
6. **Fechar**:
   - Sucesso sem erro grave: `./st mark <slug> <tarefa> done --note "<resumo de até 12 palavras>"`.
   - Precisa do Danilo: registre em `questions.md` (formato abaixo) e `./st mark <slug> <tarefa> blocked --note "<motivo curto>"`.
   - Decisão tomada sozinho: registre (formato abaixo). Não para nada.
7. **Salvar**: `git add books/<slug> && git commit -qm "<slug>: <tarefa>"` e, na nuvem, `git push -u origin HEAD` (com até 4 novas tentativas se a rede falhar). Silencioso: nunca mencione isso ao Danilo.
8. **Reportar ao Danilo** no formato de CLAUDE.md ("Como falar com o Danilo").

Em `/tudo`, volte ao passo 1 depois do passo 7 e reporte só no final. Se o contexto da sessão estiver ficando grande, não releia arquivos já processados: confie em `./st status` e `notes.md`.

## Onde registrar dúvidas e decisões

`questions.md` é lido pelo Danilo. Só entra lá o que ele precisa ver, em português simples, sem caminho de arquivo, nome de comando, código ou id de tarefa:

```
## Preciso de você
- [ ] [BLOQUEANTE] **Capítulo 3: falta sua história.** Preciso de 5 a 10 itens concretos (...). Responda aqui no chat, em tópicos.
## Decidi sozinho (confira quando puder)
- [ ] [ASSUMIDA] Noite 5: troquei "4 primos" por "3 primos" porque a conta não fechava; a resposta continua 6.
## Resolvidas
- [x] Link do bônus: recebido em 06/10.
```

Regras:
- Cada item: 1 a 2 linhas. Comece pelo assunto em negrito ("Capa:", "Noite 5:", "Bônus:"). Pergunta com opções numeradas e a sua recomendação, e diga como responder.
- Decisões técnicas que o Danilo não precisa avaliar (fonte, margem, nome de arquivo, bloco reaproveitado no layout, resolução de imagem dentro do padrão, paridade de página) vão para `reviews/decisoes.md`, não para `questions.md`. Na dúvida, pergunte-se: "o Danilo mudaria alguma coisa se lesse isto?". Se não, é `decisoes.md`.
- Resolvido sai de "Preciso de você" na hora e vai para "Resolvidas" com 1 linha. Nada de histórico longo no topo do arquivo.
- Pergunta que precisa do Danilo mas não trava tarefa (projeção de páginas, arte da capa): marca `[PRECISO]`.
- As marcas `[BLOQUEANTE]`, `[PRECISO]` e `[ASSUMIDA]` ficam no arquivo porque o `./st status` conta por elas; na conversa use "preciso de você" e "decidi sozinho".
