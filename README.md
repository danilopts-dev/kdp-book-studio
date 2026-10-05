# KDP Book Studio

Produção de livros da Read Publishing Co com Claude Code, do **TOC aprovado** até os arquivos de upload no KDP:
miolo em PDF print-ready, capa (guia de medidas ou capa completa), listing, A+ e revisões em cada etapa.
Conceito e TOC continuam na rotina `kdp-concept-toc`, com o Danilo.

## Como usar

```
/novo-livro trivia-70s activity golden-chapter     # cria books/trivia-70s/ e pede o TOC
/proximo trivia-70s                                # faz 1 tarefa e para
/proximo trivia-70s 3                              # faz 3 tarefas e para
/tudo trivia-70s                                   # vai até o fim (ou até um bloqueio geral)
/tudo trivia-70s até unit:ch05                     # vai até o capítulo 5
/etapa trivia-70s unit:ch03 deixe mais curto       # refaz uma tarefa específica
/status                                            # todos os livros
```

Tipos: `prose` (guias, textos), `activity` (caça-palavras, sudoku, trivia), `calendar`, `planner`, `children`.
Um livro pode misturar unidades: capítulos em prosa, seções de puzzles, meses de calendário, páginas de planner, páginas ilustradas.

**Dúvidas**: ficam em `books/<slug>/questions.md`. As BLOQUEANTES param só a tarefa afetada; responda no chat ou marque `[x]` no arquivo com a resposta e rode `/proximo`. As ASSUMIDAS não param nada e aparecem no `READY.md` para você validar no fim.

**Imagens e material seu**: ponha em `books/<slug>/inputs/` (capa: `cover-front.png`, `cover-back.png`; material bruto de capítulo: `inputs/raw/<id-da-unidade>.md`).

**Pasta no OneDrive** (só na máquina local): `./st new ... --onedrive "NN - Título"` (ou `onedrive_folder` no `book.yaml` + `./st link <slug>`) cria o atalho `Estudio` dentro de `Amazon KDP/NN - Título/`. `./st publish <slug>` copia PDFs, listing e READY.md para `Entrega/` (roda no `finalize`). A raiz fica em `local.yaml` (fora do git), com uma linha: `onedrive_root: 'C:\Users\<você>\OneDrive\Amazon KDP'`.

**Resultado**: `books/<slug>/build/<slug>-interior.pdf`, `<slug>-cover.pdf` (ou `-cover-guide.pdf`), `listing/` e `READY.md`.

## Etapas de cada livro

`intake` (TOC → ficha técnica e unidades) → `unit:*` (uma por capítulo/seção, cada uma com redação, checagem por script e revisão de olhos frescos) → `matter` (how-to-use, bônus, pedido de review) → `build` (PDF + checagem KDP) → `editorial` (revisão do livro inteiro + inspeção visual) → `listing` (títulos, keywords, descrição, A+, prompts do Flow) → `cover` (lombada, guia, capa completa) → `finalize` (READY.md, Notion).

## O que é código e o que é Claude

Código (não gasta tokens), em `studio/` com o comando `./st`:
- layout do miolo em Typst (`studio/render/lib.typ`): trim, margens do KDP por nº de páginas, sangria, cabeçalhos, fólios, sumário;
- caça-palavras e sudoku (gerados e validados; o sudoku sempre com solução única), answer keys;
- calendário (feriados dos EUA e datas judaicas por biblioteca);
- checagens: placeholders, páginas, tamanho, fontes embutidas, DPI, métricas de voz, duplicatas;
- cálculo de lombada e capa.

Claude (agentes em `.claude/agents/`): texto, listas de palavras, trivia com fonte, revisões, listing.

## Instalação local (Windows)

1. Instale [Python 3.11+](https://www.python.org/downloads/) (marque "Add to PATH"), [Git](https://git-scm.com/) e o Claude Code.
2. `git clone` deste repositório e abra o Claude Code na pasta. O hook de início roda `scripts/setup.sh` e cria o `.venv` sozinho.
3. Fontes (uma vez): baixe do Google Fonts e copie os `.ttf` para `fonts/`:
   - [Atkinson Hyperlegible Next](https://fonts.google.com/specimen/Atkinson+Hyperlegible+Next) (letra grande / atividades)
   - [Literata](https://fonts.google.com/specimen/Literata) (prosa)
   - [Andika](https://fonts.google.com/specimen/Andika) (infantil)
   Sem elas o engine usa substitutas (Verdana/Arial/Libertinus) e o `./st check --pdf` avisa.
4. Teste: `bash scripts/selftest.sh`.

Na nuvem (claude.ai/code) funciona igual; o hook instala tudo a cada sessão. Lá, dê push ao final e baixe os PDFs pelo chat.

## Economia de tokens

- `/proximo` para ir aos poucos; `/tudo` quando tiver folga no limite semanal.
- O orquestrador não lê os capítulos: trabalha com `./st status` e com os resumos em `notes.md`.
- Revisão visual usa uma única imagem (contact sheet) em baixa resolução.
- `writer` e `listing-writer` usam o modelo da sessão (qualidade do texto); os revisores e o `activity-builder` usam Sonnet (mais barato). Para economizar mais, troque `model:` nos arquivos de `.claude/agents/`.

## Estrutura

```
CLAUDE.md                 regras do orquestrador (modos, dúvidas, revisões, economia)
.claude/commands/         /novo-livro /proximo /tudo /etapa /status
.claude/agents/           writer, unit-reviewer, activity-builder, book-editor, listing-writer
pipelines/pipeline.yaml   etapas e tipos de unidade
pipelines/stages/         instruções de cada etapa
rules/                    regras globais, imprints, formatos e cópias das skills do Cowork
studio/                   engine (Typst, geradores, validadores, CLI)
templates/book/           modelo de pasta de livro
books/                    um diretório por livro (books/_demo* = exemplos e teste do engine)
```
