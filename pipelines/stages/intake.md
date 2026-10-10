# Etapa: intake (sessão principal)

Transforma o TOC aprovado em ficha técnica executável. É a única etapa que lê o `toc.md` inteiro.

1. Leia `books/<slug>/toc.md` e `book.yaml`. Se `toc.md` estiver vazio, bloqueie pedindo o TOC.
2. Preencha `book.yaml`:
   - `title`, `subtitle`, `author`, `imprint`, `imprint_name`, `type`, `language`, `positioning`, `reader`, `primary_keyword` (só se já validado; senão deixe vazio: o listing faz a pesquisa), `target_pages` (a faixa de páginas do TOC, ex.: "96-104").
   - `bonus`: se o TOC promete bônus gratuito, `name` e `items` (os nomes exatos de cada item, que serão os mesmos na página do livro, no PDF e no e-mail). Sem bônus: deixe `{}` (a etapa `bonus` é pulada).
   - `trim`, `bleed`, `paper`, `large_print` conforme `rules/formats/<tipo>.md` e `rules/imprints.md`; deixe vazio para usar o padrão do tipo.
   - `front` / `back`: páginas de abertura e fechamento (ver formato). Arquivos `content/_<nome>.md` serão escritos na etapa `matter`.
   - `units`: uma entrada por capítulo, seção de puzzles, mês etc., **na ordem do livro**. Campos: `id` curto (`ch01`, `ws-60s`), `kind`, `title` (exatamente o do TOC), `brief` (propósito + conteúdo-chave do TOC em 1 a 3 linhas), `target_words` (prosa; varie de verdade conforme o peso do tema), `raw` (a linha "Raw material" do TOC, quando houver).
3. Rode `./st plan <slug>` para gerar as tarefas.
4. Verifique pendências e registre em `questions.md` (formato e linguagem do `_protocol.md`):
   - Unidades de prosa com `[DANILO: needs input]` no Raw material: pergunta **BLOQUEANTE** por unidade, pedindo o material específico (5 a 10 itens concretos: histórias, números, opiniões). Não bloqueie o intake por isso; bloqueie as unidades quando chegarem (a própria etapa unit faz isso).
   - Imagens necessárias (livro infantil, capa, banners): peça cada uma pelo que ela mostra e pelo tamanho mínimo em pixels (300 DPI no tamanho impresso). O nome do arquivo que você vai gravar fica em `reviews/decisoes.md`; o Danilo só manda a imagem no chat ou na pasta do livro no OneDrive.
   - Qualquer conflito com `rules/global.md`.
5. Crie o **style sheet** em `books/<slug>/notes.md`, no topo, com: voz (1 parágrafo), grafias e termos fixos, formato de números e datas, como o leitor é tratado (you/we), nomes de personagens ilustrativos aprovados, e o que o livro NÃO faz.
6. Atualize o Notion se o conector estiver disponível: no banco "📖 Livros", status "05 - Em Produção" (crie a página se não existir). Se não houver conector, pule sem registrar erro.

Feche a etapa como `done` mesmo com perguntas BLOQUEANTES de unidades específicas. Só bloqueie o intake se faltar o próprio TOC ou se o TOC tiver conflito que impeça começar.
