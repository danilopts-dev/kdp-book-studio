# KDP Book Studio — Read Publishing Co

Estúdio de produção de livros KDP: do **TOC aprovado** até miolo print-ready, capa (guia/wrap), listing e revisões.
Conceito, posicionamento e TOC NÃO acontecem aqui; são decididos pelo Danilo na rotina `kdp-concept-toc`.
Aqui o TOC é entrada fixa: não mude estrutura, promessa ou posicionamento sem perguntar.

Fale com o Danilo em português, direto e curto. O livro sai no idioma do `book.yaml` (padrão: inglês americano nativo).

## Como falar com o Danilo (obrigatório)

O Danilo não é programador. O que é técnico fica com você; para ele vale o livro, as decisões e o que ele precisa fazer.

- **Palavras proibidas nas respostas a ele**: slug, git, commit, push, branch, merge, repositório, state.json, YAML, Typst, script, CLI, `./st`, pipeline, subagente, orquestrador, flag, variável, nomes de arquivo do projeto e caminhos (`books/...`, `inputs/...`, `content/...`), ids de tarefa (`unit:n3`, `matter`), recto/verso, paridade, DPI (diga "resolução" ou "tamanho mínimo em pixels").
- **Como dizer**:
  | Interno | Para o Danilo |
  |---|---|
  | slug / pasta do livro | o título curto ("o livro do Hanukkah") |
  | `unit:ch03`, `unit:n5` | "Capítulo 3", "Noite 5" (o título da unidade) |
  | intake / matter / build | "plano do livro" / "páginas de abertura e fechamento" / "montei o PDF" |
  | editorial / listing / cover / finalize | "revisão final" / "página da Amazon" / "capa" / "entrega" |
  | bonus | "bônus" (PDF, e-mail no Brevo, QR) |
  | BLOQUEANTE / ASSUMIDA | "preciso de você" / "decidi sozinho (confira no fim)" |
  | 🔴 / 🟠 | "erro que impede publicar" / "ajuste importante" |
  | `build/`, `listing/`, `Entrega/` | "na pasta Entrega do livro no OneDrive" (ou "te mandei aqui no chat") |
- **Nunca peça para ele** rodar comando, abrir pasta do projeto ou editar arquivo. Ele manda tudo pelo chat (texto, imagem, link) ou deixa na pasta do livro no OneDrive; você grava onde precisar.
- **Salvar o trabalho** (commit e push) é automático, ao fim de cada tarefa. Nunca mencione nem pergunte.
- **Toda pergunta** diz: o que preciso, por quê (1 linha), opções numeradas com a sua recomendação, e como responder ("responda aqui com 1, 2 ou 3").
- **Formato do relatório** (no fim de `/proximo`, `/tudo`, `/etapa`):
  - **Feito:** o que ficou pronto, em palavras do livro ("Noites 1 a 4 escritas e revisadas").
  - **Preciso de você:** só se houver; cada item pronto para responder.
  - **Próximo:** a próxima etapa pelo nome, e "faltam X etapas".

## Como o trabalho roda

- Cada livro vive em `books/<slug>/`: `book.yaml` (ficha técnica + unidades), `toc.md`, `content/`, `inputs/` (imagens e material do Danilo), `notes.md` (resumos de continuidade), `questions.md` (o que o Danilo lê), `reviews/` (inclui `decisoes.md`, o registro técnico), `bonus/` (fonte do PDF do bônus), `listing/`, `build/` (PDFs, fora do git).
- O pipeline é `pipelines/pipeline.yaml`. `state.json` guarda o status de cada tarefa. **Nunca edite state.json à mão**; use a CLI.
- CLI determinística (zero tokens): `./st <comando>`. Ver `./st -h`. Principais: `status`, `next [--runnable]`, `mark`, `build`, `preview <páginas>`, `check [--unit] [--pdf]`, `voice [--unit]`, `gen`, `cover`, `estimate`, `keywords`, `bonus`, `qr`. Todos aceitam um pedaço do nome ou do título no lugar do slug.
- O protocolo de execução de tarefa está em `pipelines/stages/_protocol.md`. As instruções de cada etapa estão em `pipelines/stages/`.

## Dois modos de trabalho

O livro pode ser indicado por qualquer pedaço do nome ou do título ("hanukkah"); sem indicação, vale o único em andamento.

- `/proximo [livro] [n]` — executa a próxima tarefa (ou as próximas n) e **para**. Para ir aos poucos e controlar o consumo semanal.
- `/tudo [livro] [até <etapa>]` — executa em sequência até o fim, até precisar do Danilo em algo que trava o resto, ou até a etapa indicada.
- `/etapa [livro] <etapa> [o que mudar]` — executa ou refaz uma etapa ("capítulo 3", "listing", "bônus").
- `/novo-livro` — o Danilo cola o TOC; você deduz apelido, tipo e imprint e pergunta só a pasta do OneDrive.
- `/status [livro]` — situação do livro (ou de todos) e o que está esperando o Danilo.

## Dúvidas: quando parar e quando seguir

`questions.md` é a lista que o Danilo lê: só o que ele precisa ver, em português simples (formato e regras em `pipelines/stages/_protocol.md`). Decisões técnicas vão para `reviews/decisoes.md`. Duas categorias:

- **BLOQUEANTE** — marca a tarefa como `blocked` e pergunta ao Danilo. Só nestes casos:
  - falta matéria-prima real para texto em prosa (as linhas "Raw material" do TOC marcadas `[DANILO: needs input]`) e o capítulo depende dela;
  - uma decisão que mudaria título, promessa, posicionamento, estrutura do TOC ou público;
  - imagem necessária que não está em `inputs/`;
  - link ou ação no Brevo/OneDrive para o bônus (só a etapa `bonus` fica parada; o resto segue);
  - fato central que não dá para verificar (trivia, datas, citações);
  - conflito com as regras (ex.: o TOC pede claim médico).
- **ASSUMIDA** — decida pelo padrão mais conservador, registre o que assumiu e siga. Exemplos: títulos de puzzles, ordem interna de uma seção, escolher a opção 1 de título/subtítulo, tamanho de grid dentro do padrão do formato.

Em `/tudo`, um bloqueio numa unidade não para as outras unidades independentes (`./st next --runnable` já pula as bloqueadas). Build, revisão final, listing e capa esperam as unidades e o matter; o bônus corre em paralelo e só segura a entrega.

Depois da 1ª unidade pronta, `./st estimate` projeta o total de páginas; se fugir da faixa do TOC, pergunte já (não no fim).

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
- Em `/proximo`, ao terminar, informe em uma linha quantas etapas faltam.

## Regras de conteúdo

Leia conforme a etapa (os subagentes já sabem quais):
- `rules/global.md` — regras de todos os livros (KDP, fatos, claims, placeholders, imagens).
- `rules/imprints.md` — voz e público por imprint.
- `rules/formats/<tipo>.md` — produção e checklist por formato.
- `rules/skills/` — cópias das skills do Cowork (`human-voice-writing`, `kdp-editorial-review`, `kdp-listing-copy`). Se o Danilo atualizar uma skill no Cowork, atualize a cópia aqui.

## Pasta no OneDrive

O Danilo mantém uma pasta por livro em `Amazon KDP/NN - Título/`. Cada livro tem `onedrive_folder` no `book.yaml`; `./st link <slug>` cria o atalho `Estudio` lá dentro e `./st publish <slug>` copia as entregas para `Entrega/`. Ao criar um livro, pergunte o nome da pasta e use `./st new ... --onedrive "NN - Título"`. A raiz fica em `local.yaml` (fora do git; ausente na nuvem, onde o publish é no-op).

## Bônus, Brevo e keywords

- **Bônus** (etapa `bonus`, `pipelines/stages/bonus.md`): você faz o PDF, os textos do formulário, o e-mail (criado direto no Brevo pelo conector, já ativo, com o link final do PDF), o teste para o e-mail do Danilo e o QR impresso no livro (`./st qr`). O Danilo faz só duas coisas: copiar o link do PDF no OneDrive e montar o formulário no Brevo (o Brevo não permite criar formulários pelo conector). Nunca crie o e-mail com link provisório.
- **Keywords** (etapa `listing`): `./st keywords` puxa buscas reais do autocomplete de Livros da Amazon.com; o listing entrega keyword principal, os 7 campos do KDP e os termos de lançamento do Amazon Ads, cada um marcado "busca real" ou "ideia".

## Salvar o trabalho (git)

- Commit ao fim de cada tarefa concluída: `git add books/<slug> && git commit -m "<slug>: <tarefa>"`. `build/` fica fora do git.
- Na nuvem, push logo depois de cada commit (o container é descartado a qualquer momento).
- Tudo isso é silencioso: nunca mencione ao Danilo.
