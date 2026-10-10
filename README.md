# KDP Book Studio

Produção de livros da Read Publishing Co com Claude Code, do **TOC aprovado** até os arquivos de upload no KDP:
miolo em PDF print-ready, capa (guia de medidas ou capa completa), listing, A+ e revisões em cada etapa.
Conceito e TOC continuam na rotina `kdp-concept-toc`, com o Danilo.

## Como usar (guia do Danilo)

Você conversa com o Claude em português; ele cuida da parte técnica e só te chama quando precisa de você.

| Você quer | Diga |
|---|---|
| Começar um livro | `/novo-livro` e cole o TOC aprovado. Ele só pergunta o nome da pasta no OneDrive. |
| Ir aos poucos | `/proximo` (1 etapa) ou `/proximo 3` (3 etapas) |
| Fazer tudo de uma vez | `/tudo` (ou `/tudo até a revisão`) |
| Refazer algo | `/etapa capítulo 3 mais curto`, `/etapa listing`, `/etapa bônus` |
| Ver como está | `/status` |

Com mais de um livro em andamento, diga qual por qualquer pedaço do título: `/proximo hanukkah`.

**Quando ele precisa de você**, a pergunta vem pronta para responder (com opções e a recomendação dele). Responda no chat. Ele anota as decisões que tomou sozinho para você conferir no fim, sem parar o trabalho.

**Material seu** (histórias, imagens, links): mande no chat ou deixe na pasta do livro no OneDrive.

**O que você recebe**, na pasta `Entrega` do livro no OneDrive:
- o miolo e a capa em PDF, prontos para o KDP;
- o PDF do bônus;
- `listing.md`: keywords (com pesquisa de buscas reais da Amazon), títulos, subtítulos, categorias, descrição, A+ e termos para o Amazon Ads;
- `bonus-brevo.md`: textos do formulário do bônus;
- `READY.md`: o passo a passo do upload no KDP, campo a campo.

**Bônus no Brevo**: o Claude faz o PDF, os textos, cria o e-mail no Brevo (já ativo, com o link certo) e te manda um teste. Você faz duas coisas: copia o link do PDF no OneDrive e monta o formulário no Brevo duplicando o do último livro (o Brevo não deixa criar formulários por fora). Com o link do formulário, ele gera o QR e coloca no livro.

## Etapas de cada livro

Plano do livro (TOC → ficha técnica) → capítulos/seções (cada um escrito, checado e revisado) → páginas de abertura e fechamento → **bônus** (em paralelo: PDF, e-mail no Brevo, QR) → montagem do PDF → revisão final → página da Amazon (keywords, títulos, descrição, A+) → capa → entrega (READY.md).

Depois do primeiro capítulo pronto, o Claude projeta o total de páginas e avisa logo se vai ficar fora do previsto no TOC.

## Comandos internos (referência técnica)

```
./st list | status <livro> | next <livro> --runnable | mark <livro> <tarefa> <status>
./st build | preview | check [--pdf] | voice | cover | gen
./st estimate <livro>                      # projeção de páginas
./st keywords <livro> "semente" ...         # autocomplete de Livros da Amazon.com -> listing/keywords-research.md
./st bonus <livro> [--preview]              # bonus/*.typ -> build/<livro>-bonus.pdf
./st qr <livro> <url> | --placeholder       # inputs/bonus-qr.png (2 in a 600 DPI)
./st link | publish <livro>                 # OneDrive
```
Tipos: `prose`, `activity`, `calendar`, `planner`, `children`. Um livro pode misturar unidades. A raiz do OneDrive fica em `local.yaml` (fora do git), com uma linha: `onedrive_root: 'C:\Users\<você>\OneDrive\Amazon KDP'`.

## O que é código e o que é Claude

Código (não gasta tokens), em `studio/` com o comando `./st`:
- layout do miolo em Typst (`studio/render/lib.typ`): trim, margens do KDP por nº de páginas, sangria, cabeçalhos, fólios, sumário;
- caça-palavras e sudoku (gerados e validados; o sudoku sempre com solução única), answer keys;
- QR do bônus, PDF do bônus, projeção de páginas, pesquisa de keywords no autocomplete da Amazon;
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
