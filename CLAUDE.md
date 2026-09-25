# KDP Book Studio — Read Publishing Co

Estúdio de produção de livros KDP: do **TOC aprovado** até miolo print-ready, capa (guia/wrap), listing e revisões.
Conceito, posicionamento e TOC NÃO acontecem aqui; são decididos pelo Danilo na rotina `kdp-concept-toc`.
Aqui o TOC é entrada fixa: não mude estrutura, promessa ou posicionamento sem perguntar.

Fale com o Danilo em português, direto e curto. O livro sai no idioma do `book.yaml` (padrão: inglês americano nativo).

## Como o trabalho roda

- Cada livro vive em `books/<slug>/`: `book.yaml` (ficha técnica + unidades), `toc.md`, `content/`, `inputs/` (imagens e material do Danilo), `notes.md` (resumos de continuidade), `questions.md`, `reviews/`, `listing/`, `build/` (PDFs, fora do git).
- O pipeline é `pipelines/pipeline.yaml`. `state.json` guarda o status de cada tarefa. **Nunca edite state.json à mão**; use a CLI.
- CLI determinística (zero tokens): `./st <comando>`. Ver `./st -h`. Principais: `status`, `next [--runnable]`, `mark`, `build`, `preview <páginas>`, `check [--unit] [--pdf]`, `voice [--unit]`, `gen`, `cover`.
- O protocolo de execução de tarefa está em `pipelines/stages/_protocol.md`. As instruções de cada etapa estão em `pipelines/stages/`.

## Dois modos de trabalho

- `/proximo <slug> [n]` — executa a próxima tarefa (ou as próximas n) e **para**. Para ir aos poucos e controlar o consumo semanal.
- `/tudo <slug> [até <tarefa>]` — executa em sequência até o fim, até um bloqueio que impeça o resto, ou até a tarefa indicada.
- `/etapa <slug> <tarefa>` — executa ou refaz uma tarefa específica (ex.: `unit:ch03`, `listing`).
- `/novo-livro <slug> <tipo>` — cria a pasta do livro; em seguida o Danilo cola o TOC em `toc.md`.
- `/status [slug]` — situação do livro (ou de todos).

## Dúvidas: quando parar e quando seguir

Registre toda dúvida em `books/<slug>/questions.md`, em uma de duas categorias:

- **BLOQUEANTE** — marca a tarefa como `blocked` e pergunta ao Danilo. Só nestes casos:
  - falta matéria-prima real para texto em prosa (as linhas "Raw material" do TOC marcadas `[DANILO: needs input]`) e o capítulo depende dela;
  - uma decisão que mudaria título, promessa, posicionamento, estrutura do TOC ou público;
  - imagem necessária que não está em `inputs/`;
  - fato central que não dá para verificar (trivia, datas, citações);
  - conflito com as regras (ex.: o TOC pede claim médico).
- **ASSUMIDA** — decida pelo padrão mais conservador, registre o que assumiu e siga. Exemplos: títulos de puzzles, ordem interna de uma seção, escolher a opção 1 de título/subtítulo, tamanho de grid dentro do padrão do formato.

Em `/tudo`, um bloqueio numa unidade não para as outras unidades independentes (`./st next --runnable` já pula as bloqueadas). Build, revisão final, listing e capa esperam tudo estar resolvido.

## Revisões (sempre rodam, nos dois modos)

1. **Por unidade**: checagem por script (`./st check --unit`, `./st voice --unit`) e em seguida o subagente `unit-reviewer` (olhos frescos), que corrige direto no arquivo. A unidade só fica `done` sem nenhum 🔴.
2. **Livro inteiro**: build e checagem do PDF (`./st check --pdf`), depois o `book-editor` faz a revisão editorial completa (checklists do `kdp-editorial-review`) e a inspeção visual por amostragem (contact sheet).
3. **Listing**: o `listing-writer` faz a auditoria do `human-voice-writing` antes de entregar.

Nenhum livro é dado como pronto com 🔴 aberto. 🟠 é corrigido quando a correção cabe na etapa; senão vira pergunta.

## Economia de tokens (obrigatório)

- O orquestrador (sessão principal) **não lê** capítulos nem YAMLs de conteúdo. Lê só `./st next`, `./st status`, os resumos dos subagentes e `notes.md` quando precisar.
- Subagentes recebem **caminhos**, não conteúdo colado. Cada um lê só o que a etapa pede.
- Continuidade entre capítulos vem de `notes.md` (3 a 5 linhas por unidade), nunca da releitura dos capítulos anteriores.
- Script antes de LLM: tudo o que dá para contar ou validar em código (grids, sudoku, datas, placeholders, fontes, páginas, DPI, métricas de voz) é validado por `./st`, não por leitura.
- Inspeção visual: uma única contact sheet (`./st preview <slug> "<páginas>"`), em ppi baixo, com páginas amostradas. Nunca abrir o PDF inteiro.
- Retorno dos subagentes: no máximo 8 linhas. Relatórios longos vão para `reviews/`.
- Em `/proximo`, ao terminar, informe em uma linha quantas tarefas faltam.

## Regras de conteúdo

Leia conforme a etapa (os subagentes já sabem quais):
- `rules/global.md` — regras de todos os livros (KDP, fatos, claims, placeholders, imagens).
- `rules/imprints.md` — voz e público por imprint.
- `rules/formats/<tipo>.md` — produção e checklist por formato.
- `rules/skills/` — cópias das skills do Cowork (`human-voice-writing`, `kdp-editorial-review`, `kdp-listing-copy`). Se o Danilo atualizar uma skill no Cowork, atualize a cópia aqui.

## Git

- Commit ao fim de cada tarefa concluída: `git add books/<slug> && git commit -m "<slug>: <tarefa>"`. `build/` fica fora do git.
- Na nuvem, dê push ao fim da sessão (o container é descartado).
