# Revisão editorial final: 8 Nights of Hanukkah Activity Book

Data: 2026-10-07 · Escopo: fontes (`content/*`, `theme.typ`, `book.yaml`, `toc.md`, `notes.md`, `questions.md`, `bonus/family-pack.typ`, JSON dos puzzles novos, listing) + 3 contact sheets (p1-28, p29-56, p57-82) + previews pontuais (p3, 16, 31, 36, 43, 48, 54, 59, 60, 76-81) + extração de texto do PDF para conferir mapa de páginas, grafias, travessões e hebraico.
Build final: 82 páginas (par) · `./st check --pdf`: 0 críticos, 0 major, 1 minor (QR a 251 DPI "em página inteira", mas o QR tem 2760 px e sai a 2.0in = 1380 DPI: sem problema) · `./st voice`: sem apontamentos.

**Resumo: 🔴 0 · 🟠 4 achados (1 corrigido, 3 abertos: 1 decisão do Danilo, 2 gates externos) · 🟡 10 achados (3 corrigidos) · 🔵 5.**
O miolo está sem 🔴. O único 🟠 de conteúdo ainda aberto é o ligar os pontos da Noite 2, que depende da autorização do Danilo (recomendo resolver antes de subir).

## 1. Estrutura (TOC aprovado x conteúdo)
Tudo o que o TOC promete existe, na noite e no nível certos:
- Cada noite tem história + caixa "What's a...?" + atividades ★ e ★★ + Before the Candles. Contagem de atividades por nível: N1 3+3, N2 3+3, N3 3+3, N4 3+3, N5 3+3, N6 3+3 (mais a receita), N7 3+3, N8 2+2 (colorir e Match; quiz em 2 páginas e Word Search) mais o certificado. As noites passaram de 2 para 3 atividades por nível, como o plano de expansão previa.
- Todos os itens citados nominalmente no TOC estão presentes: labirinto fácil e médio, caça-palavras 10x10 (N1), Hammer, 5 e 10 erros, ligar pontos 30 e 80 com quadro menorá x hanukkiah, sudokus 4x4 e 6x6 de símbolos, jarro diferente, jarro puro, "Guess How Long It Burns", Number the Steps, contagem de velas, 44 velas, Design Your Own Hanukkiah, Match the Letter + Pei, colorir dreidel, Gelt Math, Design a Dreidel, torneio + placar, receita de latke (passos da criança marcados), caça-palavras 10x10 e 14x14 com diagonais, voto Latkes x Sufganiyot, Great Latke Disaster, Count the Gelt, labirinto do gelt, Split and Save, Coupon Book, Who Gets the Coupon?, colorir a hanukkiah acesa, Family Quiz com placar, certificado, 3 piadas com escolha, Memory Page, página final (Seder Night + QR), Answer Key, bônus Family Pack (PDF existe, 3 páginas).
- Ordens trocadas, só as autorizadas, só por paridade: N5 (as duas atividades novas e depois Design a Dreidel antes de Gelt Math) e N7 (as duas novas e depois Coupon Book antes de Split and Save). Nenhuma outra ordem foi alterada em relação ao TOC.
- Front matter completo (título, copyright, How This Book Works, Lighting the Hanukkiah). Back matter completo (After Hanukkah, "That's a wrap" com QR, Answer Key de 8 páginas).
- Não há sumário impresso (o TOC é o plano, não uma página do livro). Livros de atividades dessa faixa costumam dispensar; 🔵.

## 2. Consistência (8 noites; 16 atividades novas x antigas)
- Padrão visual: selo NIGHT + título, selo ★ WARM-UP / ★★ CHALLENGE em toda atividade, instruções a 13pt, blocos de resposta com bordas de 1.4-1.6pt, números em círculo preto. As páginas novas seguem o mesmo padrão (círculos numerados, caixas arredondadas, linhas de resposta). Nada destoa.
- Instruções das 16 atividades novas: todas dentro do teto de 25 palavras (as que passam de 25 são as antigas aprovadas).
- Grafias fixas (conferidas no texto extraído do PDF): Hanukkah, hanukkiah, menorah, shamash, dreidel, gelt, latke, sufganiyah/sufganiyot, tzedakah, Maccabee, Antiochus, Mattathias, Modiin, doughnut: sem nenhuma variante (zero Chanukah, hanukiah, menora, dreidl, shamesh). "grown-up" com hífen em todo o livro (a única "grownup" que o extrator mostra é a quebra de linha "grown-/up's" na p48).
- Travessão longo e meia-risca: zero em corpo de texto, no PDF e nas fontes; só o "—" do título "Night N — ..." (tema). Zero Natal (miolo, JSON dos puzzles, listing).
- Hebraico em script: só as letras נ ג ה ש (e פ) na N5: p39 (Match + caixa "What do the letters spell?"), p41 (Tally Chart) e o molde do dreidel p43 (imagem, letras corretas conferidas girando o PNG). Nenhuma outra página.
- Puzzles novos conferidos à mão contra os JSON (além do que o código já verificou): Who Gets What? (Ben=Story, Mia=Toys, Sam=Dishes, Zoe=Big Hug satisfaz as 5 pistas e é único por dedução), padrões N5, Oil Math, Which Night Is It? (5, 2, 7, 3 = 17), cruzadas, sudoku 4x4, Unscramble (pistas excluem o anagrama alternativo STOOL).
- Humor: nenhuma piada nova na expansão. A repetição já registrada continua (ver 🟡 4).
- Respostas do quiz da N8 conferidas contra as noites (Antiochus, Mattathias, hammer, 7, shamash, 5, 8, "money" em iídiche, batata ralada, tzedakah).

## 3. Impressão
- Total 82 (par). Noite 1 em p5. Molde do dreidel p43 (ímpar) com verso em branco p44 sem folio; Coupon Book p61 (ímpar) com verso p62 sem folio e com a mesma grade espelhada (a grade ocupa a caixa de texto inteira, 7.25in, nos dois lados: conferido). Certificado p71 sem folio, moldura dentro da área segura (0.5in), acima do mínimo da KDP e da margem do tema.
- Fólio na mesma altura em todas as páginas numeradas (conferido nas 3 folhas), espelhado par/ímpar; as páginas sem fólio são só as de front matter (p1-4), as duas em branco e o certificado. O fólio impresso começa em 1 na p5 (offset de 4, paridade mantida).
- Margens: nada perto das margens; gutter 0.65in; `check --pdf` sem achados de margem, DPI ou fonte.
- Imagens: nítidas nas folhas e nas ampliações. Nenhuma página quase vazia sem motivo (as de bastante branco são as de escrita/desenho: p21, p29, p37, p64, p72).
- Answer key: legível (letras das grades >= 9pt; imagens com cinza escuro, bom para P&B) e completo para todas as atividades de resposta única: os 16 puzzles novos que têm resposta única entram (N5 Tally Chart está fora de propósito: sem resposta única). Ordem e títulos iguais aos do corpo.
- Lista across/down da cruzada da N6 (topo da p81): avaliei e **não mexi**. O cartão se chama "Night 6 · ★★ Hanukkah Food Crossword: Across and Down", então se acha sozinho, e a própria grade em cinza da p80 já mostra todas as palavras soletradas. Juntar a lista à grade empurraria o cartão para outra página e mudaria a contagem. 🔵 se quiser: na próxima edição, colocar a lista ao lado da grade.

## 4. Promessas do front matter e do how-to-use
- Dois níveis ★/★★, "uma noite por vez", "começar em qualquer noite", mini-guia de acendimento, bênçãos na Noite 1, Family Pack (cartão de bênçãos, regras do dreidel, etiquetas "Night 1-8"): tudo existe. O PDF do bônus tem exatamente esses 3 itens.
- "20 to 30 minutes" por noite: **deixou de ser plausível** (ver 🟠 2): corrigido.

## 🔴 CRITICAL
Nenhum.

## 🟠 MAJOR

[🟠] p16 e p19 (N2, ligar os pontos 30 e 80); gabaritos p76 e p77 — Puzzle · RESOLVIDO em 07/10/2026 com os assets `_v2` (conferir as páginas no próximo build)
Found: ao ligar, a hanukkiah de 30 pontos vira um serrote e a menorá de 80 pontos vira algo parecido com uma mão; na p16 os rótulos 13/16, 14/17 e 15/18 continuam colados. A instrução da p16 promete "something that will light up this whole book"; a da p19, "the menorah that stood in the Temple".
Issue: a promessa do TOC não se cumpre e a página ★ é para a criança de 6-7 anos. É a página mais fraca do livro e a que um comprador percebe.
Fix: pendente, pois exige redesenhar assets aprovados (autorização). Recomendação detalhada em `questions.md` ("Revisão editorial final"): versões `_v2` em arquivos novos, hanukkiah com vértices reais e shamash central, menorá com braços curvos, rótulos pelo `posicionar_rotulos`. Trocar o `puzzle(...)` em `content/n2.typ` e as duas imagens do `answer-key.typ`. Mesma contagem de páginas.

[🟠] p3 (How This Book Works) e listing — Promessa · CORRIGIDO
Found: "Most nights take about 20 to 30 minutes from start to finish." (e "Plan on 20 to 30 minutes a night" na descrição).
Issue: o TOC pensava em 3-4 atividades por nível; com a expansão são 6 por noite (e na N6 há ainda a receita). Quem fizer todas as páginas leva bem mais; o comprador lê isso como promessa não cumprida.
Fix aplicado: "Most nights take about 20 to 30 minutes for the story and a few puzzles. You never have to do every page, so pick the ones that look fun and come back to the rest any time." Descrição do listing: "...for the story and a few puzzles; there is no need to do every page." Sem mudança de paginação (p3 tinha branco de sobra). Registrado em `questions.md` e na decisão 54 de `legacy/docs/relatorio-decisoes.md`.

[🟠] Hebraico/religioso — Gate pré-upload · ABERTO (externo)
Found: nenhum item [REVISAR] passou por revisor humano (mini-guia, 3 bênçãos com "Adonai", Shehecheyanu com "v'higiyanu", quadro menorá x hanukkiah, 44 velas, letras do dreidel e Pei, cartão do bônus com nikud). As alterações da revisão religiosa estão aplicadas e batem entre miolo e bônus (as transliterações das 3 bênçãos são idênticas nas duas peças).
Fix: pendente (revisor humano). Não é decisão minha.

[🟠] Bônus: fluxo de entrega — Back matter · ABERTO (externo, pré-upload)
Found: QR real no livro (p74) e PDF do Family Pack prontos; falta, segundo `READY.md`, pegar o link do OneDrive, trocar o link provisório do template id 22 no Brevo e testar o fluxo de ponta a ponta.
Issue: o livro promete o bônus em dois lugares (p4 e p74). Se o e-mail não entregar o PDF, o comprador fica sem.
Fix: pendente (passos em `listing/bonus-brevo.md`).

## 🟡 MINOR

1. [🟡] p3 e p4 (how-to-use) — "Scan the code at the end of this book" · CORRIGIDO. O QR está na p74, antes do Answer Key (que vem depois). Agora: "Scan the code near the end of this book, just before the Answer Key".
2. [🟡] `READY.md`, `listing/aplus-prompts.md`, `listing/listing.md` — Referências de página velhas · CORRIGIDO. QR "página 58" -> 74; exportar "19,38" -> "23,48" (as páginas que o próprio texto cita); faixas de páginas da auditoria do listing atualizadas para o miolo de 82 páginas.
3. [🟡] `legacy/docs/relatorio-decisoes.md` — decisão 54 acrescentada (promessa de tempo e QR).
4. [🟡] N4 (p31) e N8 — Artes 42b/42d (8 velas) e 42c (3) no Number the Steps, seguidas de p32 (4 velas), p33 (Night 2, 4, 6) e p36 (Which Night Is It?). ABERTO, já em questions.md; agora pesa mais porque a N4 tem 3 páginas de contagem de velas e as figuras da p31 mostram a hanukkiah cheia. Recomendo regerar 42b/42d com 4 velas.
5. [🟡] N6 receita (p48), passo 1 — "YOUR JOB: Grate the potatoes and onion" × introdução "a grown-up handles the grater". ABERTO (texto aprovado; sugestão em questions.md: tirar a marca do passo 1). Segurança, e é a primeira coisa que a criança lê na lista.
6. [🟡] Humor — 5 das 7 piadas são "Why did X...? Because..." e três giram em torno da hanukkiah em festa/família com "light up" (N4, N8-B, N8-C). ABERTO (em questions.md desde 05/10). Nenhuma piada nova entrou na expansão.
7. [🟡] p2 (copyright) — "The activities and puzzle pages in the Answer Key..." ABERTO (já em questions.md; sugestão de redação pronta).
8. [🟡] p56 (N7 história) — "Every night of Hanukkah, kids get gelt" e "not only in December" generalizam. ABERTO (questions.md).
9. [🟡] p7 (N1 Word Hunt) — "Look across and up and down" sugere ler de baixo para cima; as palavras só vão da esquerda para a direita e de cima para baixo. ABERTO (texto aprovado). Mantido.
10. [🟡] Detalhes de diagramação sem ação: p48 termina com a viúva "up's job." (quebra "grown-/up's"); piadas das Before the Candles entre 14pt (N1) e 26pt (N4); placares em estilos diferentes (círculos, linha, caixinhas), todos de um passo só; N8 repete "dedication" na história e na caixa (p65).

## 🔵 RECOMENDAÇÕES
1. Zero cortado do Atkinson Hyperlegible (2Ø, 3Ø, 1Ø) em todo o texto corrido e nas contas. É desenho da fonte, sem feature para desligar; vale saber que a criança de 6-7 anos vai ver "2Ø gelt coins". Registrado em questions.md.
2. N7 Which Pile Has More?: a maior pilha alterna direita, esquerda, direita, esquerda, direita, esquerda; trocar os lados nos pares 3 e 5 (JSON + answer-key leem do mesmo arquivo) quebra o padrão. Não alterei.
3. Molde do dreidel (p43): só há uma aba triangular (cabo) e uma trapezoidal (ponta); o resultado é um dreidel aberto em cima e embaixo. O texto manda "glue the gray tabs" e "give it a spin". Se a criança não conseguir montar, não é erro de conteúdo, mas vale um teste de montagem em papel antes de subir.
4. Página final p74 anuncia "Seder Night" como próximo livro; manter só se a série estiver confirmada.
5. Lista across/down da cruzada no answer-key: juntar à grade na próxima edição.

## Alterações feitas nesta revisão
1. `content/_how-to-use.md`: tempo por noite ("20 to 30 minutes for the story and a few puzzles... You never have to do every page") e localização do QR ("near the end of this book, just before the Answer Key").
2. `listing/listing.md`: mesma frase de tempo na descrição; faixas de páginas da auditoria atualizadas.
3. `listing/aplus-prompts.md`: comando de exportação "19,38" -> "23,48".
4. `READY.md`: QR na página 74.
5. `legacy/docs/relatorio-decisoes.md`: decisão 54.
6. `questions.md`: seção "Revisão editorial final (2026-10-07)" (dots N2, receita, zero cortado, pilhas, N7).
Nenhum PNG de `inputs/` alterado. Nenhuma mudança de paginação: `./st build` e `./st check --pdf` rodados depois das alterações: 82 páginas, p5 / p43-44 / p61-62 conferidas.
