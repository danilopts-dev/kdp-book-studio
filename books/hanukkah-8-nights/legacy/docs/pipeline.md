# PIPELINE DE PRODUÇÃO
## 8 Nights of Hanukkah Activity Book (título de trabalho) · Jonah Feldman

Criado em 21/09/2026. Adapta a lógica do pipeline do livro 12 (`70 Reasons to Celebrate Turning 70`) e do pipeline automatizado do livro 11 (`Trivia for Seniors`, seção de puzzle com gabarito), ao contexto deste livro: activity book infantil (6 a 10 anos) organizado pelas 8 noites de Hanucá, com puzzle gerado por código e texto curto.

Esta é a primeira parada do projeto, pedida no `prompt-de-abertura.md`: pipeline e réguas antes de qualquer conteúdo.

---

# 1. O QUE MUDA EM RELAÇÃO AO PIPELINE DO LIVRO 12

## 1.1 A mudança estrutural central: puzzle é código, não prosa

O livro 12 é prosa original em blocos de texto (SCENE/ELEMENT/TURN). O livro 11 tinha puzzle, mas descontinuou o papel de agente Puzzle e passou a gerá-los por script fora do pipeline de agentes.

**Este livro é majoritariamente puzzle**, com texto curto (Tonight's Story, caixa "What's a...?", Before the Candles) em volta. Isso muda o centro de gravidade do pipeline:

- Não existe Checador Factual (como no 12, sem mudança: a história de Hanucá é recontada como tradição, não como fato a verificar com fonte externa; ver seção 6 sobre revisão religiosa, que é um mecanismo diferente).
- **Existe um papel novo que nenhum dos dois pipelines anteriores tinha desse jeito: o Gerador de Puzzle, que é código, não agente.** Cada tipo de puzzle (caça-palavras, sudoku de símbolos, labirinto, jogo dos erros, ligar pontos, sequência para numerar, Mad Libs) tem um script Python que gera o puzzle **e** o gabarito no mesmo processo, porque só assim gabarito e puzzle nascem consistentes por construção. Nenhum puzzle é desenhado ou resolvido por agente lendo o layout; agente nenhum "resolve" um sudoku de cabeça para conferir.
- Cada script de puzzle tem um verificador embutido, rodado antes de qualquer coisa seguir para o Revisor: solução única (sudoku, jogo de lógica), palavras realmente presentes e encontráveis sem sobreposição inválida (caça-palavras), caminho único da entrada à saída sem ambiguidade (labirinto), contagem correta e verificável (sequência, "quantas velas"), Mad Libs com todos os slots de gramática coerentes. Isso generaliza a lógica de `pipeline-automatizado.md` do livro 11 (que só cobria caça-palavras e cruzadinha) para os sete tipos de puzzle deste livro.
- O texto curto ao redor do puzzle (Tonight's Story, caixa "What's a...?", Before the Candles) segue o modelo de Gerador + Revisor dos livros 11 e 12, mas com réguas próprias de voz infantil (ver `reguas-operacionais.md`).

**Consequência prática:** duas linhas de produção por noite, não uma. Linha A (texto) é agente. Linha B (puzzle) é script. Elas se encontram na diagramação.

## 1.2 As correções A1–A8 do livro 12, herdadas e adaptadas

| # | Correção (livro 12) | Aplicação neste livro |
|---|---|---|
| A1 | Gerador não lê `aprovado/` | Aplicada, para a Linha A (texto). O Gerador de texto de cada noite lê réguas operacionais, o bloco do TOC referente àquela noite, `usados.md` (piadas/charadas/termos já usados) e **uma** noite padrão-ouro aprovada. Não lê noites já aprovadas inteiras. Para a Linha B (puzzle), a correção não se aplica da mesma forma: o script não "lê" nada em sentido de contexto de agente, ele recebe parâmetros (lista de palavras, tamanho de grade, dificuldade) e roda. |
| A2 | Script determinístico antes do Revisor | Aplicada, e reforçada: aqui **todo** puzzle passa por verificador de código antes de qualquer revisor humano ou agente ver o arquivo, não só a parte contável do texto. `scripts/conformidade_texto.py` cobre a Linha A (contagem de palavras, travessão longo, palavras banidas, zero Natal, hebraico sinalizado). `scripts/verificar_puzzle.py` cobre a Linha B, com um verificador específico por tipo de puzzle. |
| A3 | Correção é chamada estreita | Aplicada. Ver seção 5. Na Linha B, "correção" quase sempre é reparametrizar e rodar o script de novo, não editar o puzzle manualmente. |
| A4 | Dono único do ledger, e tarde | Aplicada. O Gerador de texto escreve só em `noites/`. Só o Revisor escreve em `usados.md` e só quando aprova o lote. Os scripts de puzzle escrevem em `puzzles/` e no próprio `gabarito/` (gerado junto, nunca à parte). |
| A5 | Ordem do contexto: estável antes de volátil | Aplicada. Réguas, TOC e padrão-ouro não mudam. `usados.md` muda a cada noite e vem depois. A instrução da noite vem por último. |
| A6 | Cache de fontes | Não se aplica a fato externo (como no 12). **Adaptada para um uso novo aqui:** cache de piadas/charadas já descartadas por repetir estrutura, para não gerar a mesma piada reformulada em noites diferentes. Vive em `usados.md`, seção de humor. |
| A7 | Réguas com teto | Aplicada. `reguas-operacionais.md`, teto de 200 linhas, é o único bloco de estilo que entra em sessão de geração de texto. |
| A8 | Log fora do contexto de produção | Aplicada. `relatorio-decisoes.md` e o log de correções do Revisor nunca são lidos pelo Gerador; só pelo Passe Final e pelo Danilo. |

**Consequência para o gargalo de tokens (a razão de ser das correções A1-A8):** no livro 12 a alavanca era quanto contexto o Gerador arrastava por lote de prosa. Aqui a alavanca principal nem é essa: **é quanto do trabalho fica na Linha B, que é gratuita em tokens (script) em vez de na Linha A**. Cada puzzle que sai como agente escrevendo grade célula por célula (em vez de script gerando e verificando) é o equivalente do 12 a reabrir `aprovado/` inteiro: caro, redundante, e ainda assim capaz de errar. Regra fixa deste pipeline: **nenhum puzzle é gerado por agente escrevendo o conteúdo final da grade.** O agente só decide parâmetros de conteúdo (quais palavras, qual tema, qual nível de dificuldade); o script decide layout, posição e gabarito.

---

# 2. PAPÉIS E MODELOS

| Papel | Modelo | Por quê |
|---|---|---|
| **Orquestrador** | Sonnet | Segue o roteiro por noite, chama os scripts, atualiza `proximos-passos.md`, decide quando escalar. |
| **Gerador de texto (Linha A)** | **Opus** | Tonight's Story, caixa "What's a...?" e Before the Candles carregam a voz do livro inteiro para uma criança de 6 a 10 anos; é onde a diferenciação de nível ★/★★ e o humor limpo têm que soar certo desde a primeira noite. Frequência baixa (uma chamada por noite, 8 no total, mais front/back matter). |
| **Gerador de parâmetros de puzzle** | Sonnet | Decide o conteúdo do puzzle (quais 10 palavras no caça-palavras da Noite 1, qual tema no sudoku de símbolos, qual rota faz sentido no labirinto) a partir do TOC e da história da noite. Não desenha a grade; entrega os parâmetros ao script. |
| **Script de puzzle (Linha B)** | nenhum | Gera o puzzle e o gabarito juntos, e roda o verificador próprio do tipo. Custo zero, determinístico, sem erro de contagem ou de sobreposição. |
| **Script de conformidade de texto** | nenhum | Roda o checklist contável da Linha A (contagem, palavras banidas, travessão longo, Natal, hebraico) antes do Revisor. |
| **Revisor** | Sonnet, **Opus na Noite 1 (piloto)** | Recebe os relatórios dos dois scripts prontos e julga só o que exige leitura humana de sentido: tom, humor, se a diferenciação ★/★★ está clara, se a caixa "What's a...?" explica bem. Na Noite 1 sobe para Opus porque o padrão-ouro que sair dali governa as outras sete noites. |
| **Passe Final** | **Opus** | Chamada única, depois da Noite 8, antes da diagramação completa. Mede deriva de voz e de dificuldade entre a Noite 1 e a Noite 8, e verifica a curva de humor/tema do livro inteiro. |
| **Editorial review** | skill `kdp-editorial-review` | Sobre o PDF diagramado, na etapa 4 do prompt de abertura. Corrigir antes de mostrar ao Danilo. |

---

# 3. CONTRATO DE LEITURA POR PAPEL

| Papel | Lê | Escreve |
|---|---|---|
| **Orquestrador** | `proximos-passos.md`, relatórios dos scripts | `proximos-passos.md` |
| **Gerador de texto** | `reguas-operacionais.md`, o bloco da noite em `toc/`, `usados.md`, **uma** noite em `padrao-ouro/` | `noites/[N]/texto.md` |
| **Gerador de parâmetros de puzzle** | o bloco da noite em `toc/`, `usados.md` (temas/palavras já usados), a especificação de parâmetros de cada script em `scripts/README.md` | `noites/[N]/parametros-puzzle.json` (ou similar) |
| **Scripts (puzzle e conformidade)** | tudo, sem restrição (custo zero) | `puzzles/`, `gabarito/`, relatório em stdout |
| **Revisor** | os dois relatórios de script, `reguas-operacionais.md`, `noites/[N]/texto.md`, os puzzles e gabaritos gerados, o padrão-ouro | `usados.md`, `aprovado/`, log de decisões |
| **Passe Final** | o miolo inteiro montado, `reguas-operacionais.md`, o log de decisões inteiro | relatório |

**Nunca, exceto o Passe Final:** ler `aprovado/` inteiro ou o log de decisões inteiro.

---

# 4. ORDEM DE PRODUÇÃO

Diferente do livro 12 (que ia do centro para as pontas), aqui a ordem segue o próprio TOC, noite 1 a 8, porque **a Noite 1 é o piloto que o Danilo aprova antes do lote** (etapa 2 do prompt de abertura), e as noites não têm um "extremo temático" a fixar como no 12: cada noite é independente por desenho do livro.

| Etapa | Conteúdo | Observação |
|---|---|---|
| **P0** | Noite 1 completa: texto + puzzles + gabarito + diagramação em PDF com espaços de ilustração dimensionados e rotulados, mais a lista de ilustrações do livro inteiro com prompts para Google Flow | **Piloto.** Único gate humano obrigatório antes do lote. Revisor em Opus. |
| L1–L7 | Noites 2 a 8, em lote, sem chamar o Danilo | Só depois do piloto aprovado. Cada noite segue o mesmo par Gerador de texto + Gerador de parâmetros de puzzle + scripts + Revisor. |
| L8 | Front matter (título, copyright, How This Book Works) | Depende das decisões da Noite 1 sobre nível e mini-guia de acendimento (item [REVISAR]). |
| L9 | Back matter (After Hanukkah: My Hanukkah Memory Page, próximo livro da série) | |
| L10 | Answer Key (~8 págs) | Gerada automaticamente a partir de `gabarito/`, um script monta a seção, não se redigita nada à mão. |
| L11 | Bonus: 8 Nights Family Pack | Marcado como temporário no TOC; revisar depois que o miolo estiver pronto, conforme o próprio TOC pede. |

Teto de 1 noite por lote de geração de texto (diferente do teto de 6 entradas do livro 12): cada noite já é uma unidade editorial completa (história + 2 níveis + puzzle + Before the Candles), então gerar mais de uma por vez não economiza chamada, só aumenta o risco de a Noite N+1 herdar um erro da Noite N sem passar pelo Revisor no meio.

**Total estimado: 1 Gerador de texto (Opus) + 1 Revisor (Opus) no piloto; 7 Geradores de texto (Opus) + 7 Revisores (Sonnet) no lote; N chamadas de Gerador de parâmetros de puzzle (Sonnet, uma por puzzle, cerca de 3 a 4 por noite); scripts sem custo de modelo; 1 Passe Final (Opus).**

---

# 5. ESCALONAMENTO E CORREÇÃO

## 5.1 A regra

Cada handoff pode devolver o material para correção **uma vez**. Se a segunda passagem falhar no mesmo ponto, o agente para e escreve para o Danilo em vez de tentar de novo. Mesma lógica dos livros 11 e 12: sem esse teto, um agente preso numa régua ambígua reescreve indefinidamente e cada volta consome tokens sem aproximar de solução.

## 5.2 A chamada de correção é estreita

Para a Linha A (texto): a correção recebe só o texto que falhou, o achado específico do relatório do script ou do Revisor, e as linhas de `usados.md` relevantes ao achado. Não recebe réguas inteiras, TOC inteiro, nem outras noites.

Para a Linha B (puzzle): a correção quase sempre é reparametrizar e rodar o script de novo (outro conjunto de palavras, outra semente de geração do labirinto), não editar a grade manualmente. Se o script falhar repetidamente com um parâmetro específico (por exemplo, 10 palavras que não cabem numa grade 10x10 sem sobreposição inválida), o achado é "o parâmetro está inviável", e volta para o Gerador de parâmetros de puzzle, não para o script.

## 5.3 Quando o pipeline chama o Danilo

Exatamente como listado no `prompt-de-abertura.md`:
- Aprovar pipeline e réguas (esta etapa).
- Aprovar o piloto da Noite 1 (visual, nível de dificuldade, voz).
- Receber a lista de ilustrações do livro inteiro, junto com o piloto.
- Decisão de conteúdo religioso que não esteja no TOC (diferente dos itens [REVISAR] já previstos no TOC, que vão para `revisao-religiosa.md` e não exigem parar o pipeline, só entram na lista que o revisor humano local confere).
- Qualquer coisa que mude a especificação (páginas, trim, gutter) ou o preço.
- Bloqueio que sobrevive a uma correção, em qualquer linha.

Fora disso, o pipeline corrige a si mesmo e segue, registrando em `relatorio-decisoes.md`.

---

# 6. OS TRÊS DOCUMENTOS DE ACOMPANHAMENTO

Mantidos pelo Orquestrador/Revisor durante toda a produção, conforme pedido no `prompt-de-abertura.md`:

## 6.1 `relatorio-decisoes.md`

Toda decisão tomada sem aprovação do Danilo, uma linha por decisão: o que foi decidido, por quê, em que noite ou etapa. Exemplos previsíveis já neste início: estilo de ilustração (o TOC deixa em aberto, "proponha no piloto"), escolha de layout de sequência de acendimento, número exato de piadas por noite dentro da faixa aceitável.

## 6.2 `hebraico-para-revisao.md`

Toda página que tiver letra ou palavra em hebraico entra aqui, com o número da noite/página, o texto em hebraico, a transliteração e a tradução usadas. Pelo TOC, isso inclui pelo menos: a bênção da Noite 1 (transliteração e inglês, e o Shehecheyanu), o cartão de bênçãos do Bonus Family Pack, e qualquer rótulo em hebraico nas ilustrações da hanukiá/menorá. Atualizado pelo Revisor a cada noite aprovada, nunca reescrito do zero.

## 6.3 `revisao-religiosa.md`

Todo item marcado [REVISAR] no TOC v2 entra aqui, com a melhor versão proposta pelo pipeline e a fonte usada, para o revisor humano local decidir. Extraído do TOC v2 nesta etapa, a lista de partida é:

| # | Item [REVISAR] | Onde no TOC |
|---|---|---|
| 1 | Mini-guia de acendimento (onde colocar as velas, ordem de acender, o shamash) | Front matter, How This Book Works |
| 2 | O Shehecheyanu, que só se diz na 1ª noite | Noite 1, Before the Candles |
| 3 | Menorá (7 braços, do Templo) x hanukiá (8 + shamash), quadro da diferença | Noite 2, atividade ★★ |
| 4 | Conta de 44 velas em 8 noites (com o shamash) | Noite 4, atividade ★★ |
| 5 | A letra Pei em Israel (variante do dreidel) | Noite 5, atividade ★ |
| 6 | Cartão de bênçãos de Hanucá (hebraico, transliteração, inglês) | Bonus, 8 Nights Family Pack |

Essa lista é o ponto de partida da etapa 1 (pipeline/réguas); cresce se novos pontos ambíguos aparecerem durante a geração das noites 2 a 8, e o Revisor tem instrução de adicionar, nunca de decidir sozinho um ponto religioso não coberto pelo TOC.

---

# 7. ESTRUTURA DE PASTAS

```
13 - Hanukkah 8 Nights Activity Book - 6-10 years/
├── prompt-de-abertura.md
├── toc/
│   └── 2026-09-21 - Hanukkah 8 Nights activity book (Jonah Feldman) - v2.md
├── pipeline.md
├── reguas-operacionais.md
├── padrao-ouro/
│   └── noite-01.md                  (só depois do piloto aprovado)
├── usados.md                        (piadas/charadas usadas, temas de puzzle usados, termos já explicados na caixa "What's a...?")
├── noites/
│   ├── noite-01/
│   │   ├── texto.md                 (Tonight's Story, What's a...?, Before the Candles, os dois níveis)
│   │   └── parametros-puzzle.json   (um por puzzle da noite)
│   ├── noite-02/
│   └── ... noite-08/
├── puzzles/
│   └── noite-01/                    (arquivo de puzzle gerado por script, um por atividade)
├── gabarito/
│   └── noite-01/                    (gabarito gerado pelo mesmo script que gerou o puzzle)
├── scripts/
│   ├── README.md
│   ├── conformidade_texto.py
│   ├── gerar_labirinto.py
│   ├── gerar_caca_palavras.py
│   ├── gerar_sudoku_simbolos.py
│   ├── gerar_ligar_pontos.py
│   ├── gerar_jogo_dos_erros.py      (gera a lista de diferenças e o gabarito numerado; a arte em si é ilustração do Danilo)
│   ├── gerar_mad_libs.py
│   ├── verificar_puzzle.py          (verificador único, despacha por tipo)
│   └── montar_answer_key.py
├── ilustracoes/
│   └── lista-ilustracoes.md         (o que cada imagem mostra, tamanho, proporção, prompt Google Flow)
├── manuscrito/
│   └── miolo.txt                    (montado a partir de noites/ + front/back matter, na ordem do livro)
├── diagramacao/
│   ├── diagramacao.md               (especificação de diagramação, feita no piloto)
│   └── relatorio-diagramacao.md
├── relatorio-decisoes.md
├── hebraico-para-revisao.md
├── revisao-religiosa.md
└── proximos-passos.md
```

---

# 8. ESPECIFICAÇÃO TÉCNICA

| Item | Valor | Observação |
|---|---|---|
| Trim | 8.5 x 11 in | conforme TOC e prompt de abertura |
| Miolo | preto e branco, papel branco | |
| Capa | colorida, fosca | conforme TOC |
| Páginas | 96 a 108 | teto 108 (faixa de custo fixo da KDP, conforme TOC) |
| Gutter (margem interna) | **0.65 in**, não 0.5 in | o livro 12 teve o gutter de 0.5 in (mínimo exato da faixa KDP) rejeitado pela KDP; este livro já parte de 0.65 in para não repetir o problema. Confirmar contra a tabela oficial de gutter por número de páginas da KDP no momento da diagramação, porque a faixa de páginas (96-108) pode exigir gutter ainda maior dependendo da contagem final. |
| Margem externa | folgada (a definir na diagramação, seguindo o mesmo raciocínio do livro 12: recomendação KDP mínima é referência, não meta) | |
| Fólio | sempre na mesma altura, página a página | mesma trava do livro 12 (`diagramacao.md`, seção 4): fólio é elemento posicionado, não parte do fluxo de texto |
| Idioma | inglês americano | |
| Estilo de ilustração | não definido | proposto no piloto (etapa P0), aprovado pelo Danilo junto com o piloto |
| Meta de lançamento | até 12/10/2026 | Hanucá 2026: 4 a 12/dez |

---

# 9. DEPOIS DO PASSE FINAL

1. `python3 scripts/montar_answer_key.py` monta a seção de gabaritos a partir de `gabarito/`, organizada por noite e nível.
2. Diagramação completa do miolo, seguindo `diagramacao/diagramacao.md` (produzida a partir do piloto).
3. Skill `kdp-editorial-review` sobre o PDF final. Corrigir o que ela achar antes de mostrar ao Danilo (regra do prompt de abertura).
4. Skill `kdp-listing-copy` para título, subtítulo, keywords, descrição e A+, só depois do PDF aprovado.
5. Capa e ilustrações finais entram quando o Danilo mandar (as ilustrações são dele; o pipeline só reserva e rotula o espaço).
