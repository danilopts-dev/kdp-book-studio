# Revisão editorial — 8 Nights of Hanukkah Activity Book

Data: 2026-10-05 · Escopo: fontes (`content/*`, `theme.typ`, `toc.md`, `notes.md`, docs de `legacy/`) + 3 contact sheets (p1-22, p23-44, p45-64) + previews de p47 e p55 (coupon e certificado) + 1 folha de verificação (p33-36, 47-50) depois das correções. Build final: 64 páginas; `./st check --pdf` = 0 achados; `./st voice` = sem apontamentos.

Resumo: 🔴 0 · 🟠 5 achados (2 corrigidos, 3 abertos que dependem do Danilo ou de produção externa) · 🟡 8 achados (2 corrigidos) · 🔵 4.

## 1. Estrutura (TOC aprovado x conteúdo)
Toda atividade do TOC existe, na noite e no nível certos (★/★★ no selo de cada atividade). As duas únicas ordens trocadas são as autorizadas (N5: Design a Dreidel antes de Gelt Math; N7: Coupon Book antes de Split and Save). Caixas "What's a...?" por noite batem com o TOC: Maccabee, menorah vs. hanukkiah, miracle, shamash, gelt (na página do Gelt Math, onde a palavra aparece pela primeira vez), latke + sufganiyah (na página do voto), tzedakah, Hanukkah ("dedication"). Front matter completo (título, copyright, How This Book Works + Lighting the Hanukkiah); back matter completo (After Hanukkah, página final com Seder Night e QR, Answer Key de 6 páginas). Número de páginas (64 x 96-104 do TOC): pergunta já aberta, não tocada. Bônus: o miolo o promete e aponta para o QR; o PDF do bônus não existe (ver 🟠 4).

## 🟠 MAJOR

[🟠] p35 (N5, Gelt Math 3) — Conteúdo · CORRIGIDO
Found: "...Then you spin a Hei and have to put half of your coins back in the pot."
Issue: contradiz a regra do próprio livro (Match: Hei = Half; torneio da p36: "Hei: take half the pot"). A criança que acabou de ler a regra erraria o problema.
Fix aplicado: "Then you give half of your coins to your little cousin." A conta (18 + 14) / 2 = 16 e o answer key não mudam. Alteração de texto aprovado, registrada em questions.md.

[🟠] p49 (N7, Split and Save 1) — Conteúdo · CORRIGIDO
Found: "You want to give some to tzedakah and save the rest in 3 equal piles... If you split all 12 coins into 3 equal piles..."
Issue: o enunciado se contradiz (separa moedas para tzedakah e depois divide todas as 12).
Fix aplicado: "You split all of them into 3 equal piles: one to give to tzedakah, one to save, and one to spend." Resposta continua 4. Alteração registrada em questions.md.

[🟠] p14 e p16 (N2, ligar os pontos 30 e 80) — Puzzle · ABERTO (decisão do Danilo; já estava como ASSUMIDA)
Found: no answer key (p60) e nos PNGs de gabarito, a hanukiá de 30 pontos vira um serrote assimétrico e a menorá de 80 pontos, uma coroa irregular; na p14 os rótulos 13/16, 14/17 e 15/18 ficam colados.
Issue: a instrução promete revelar "something that will light up this whole book" e "the menorah that stood in the Temple"; o resultado não é reconhecível, e é o ★ de uma criança de 6-7 anos. É o ponto mais fraco do miolo.
Fix: pendente. Recomendo autorizar o redesenho em arquivos novos (`*_v2`) com o gerador existente. Linha em questions.md.

[🟠] p58 e front matter (bônus Family Pack e QR) — Back matter · ABERTO (pré-upload)
Found: a página 58 imprime a caixa "QR CODE" temporária (placeholder autorizado pelo Danilo); o PDF do bônus (cartão de bênçãos, regras do dreidel + placar, 8 etiquetas) não foi produzido, só o texto do cartão.
Issue: o livro promete o bônus duas vezes (p4 e p58).
Fix: pendente. Produzir o PDF, gerar `inputs/bonus-qr.png` e trocar `has-bonus-qr` para `true` em `theme.typ`. Linha em questions.md.

[🟠] Hebraico/religioso — Gate pré-upload · ABERTO
Found: todo [REVISAR] do TOC está registrado em `legacy/docs/revisao-religiosa.md` e `hebraico-para-revisao.md` (mini-guia, bênçãos, Shehecheyanu, quadro menorá x hanukiá, conta 44, Pei, cartão do bônus), sem item órfão. Nenhum passou por revisor humano ainda.
Fix: pendente (revisor humano). Linha em questions.md.

## 🟡 MINOR

[🟡] p3 (How This Book Works) — Terminologia · CORRIGIDO
"grown up" / "seven year old" -> "grown-up" / "seven-year-old" (o resto do livro usa "grown-up"; p4 já usava).

[🟡] `legacy/docs/hebraico-para-revisao.md` — Documento desatualizado · CORRIGIDO
A tabela consolidada ainda dizia que a Noite 5 tinha letras em script. Acrescentei nota de atualização: o miolo não tem hebraico em script (conferido por código e nas artes 51, 83, 42b); lista o que o revisor deve olhar.

[🟡] Humor (N1, N4, N6, N8) — Estrutura repetida · ABERTO (texto aprovado)
5 das 7 piadas são "Why did X...? Because..." (N1, N4, N6, N8-A, N8-C); 3 giram em torno da hanukkiah em festa/família (N4 "invited to every party", N8-A "throw a party", N8-C "whole family") e "light up" aparece em N4, N8-B e N8-C. Limpas e acolhedoras, mas se repetem. Recomendação em questions.md (trocar N8-A e variar N4).

[🟡] p10, p29, p43, p56 (Before the Candles) — Tamanho de texto das piadas
Corpo da piada varia de 14pt (N1, componente `joke`) a 26pt (N4), conforme o espaço da página. Aceitável; só uniformizaria se sobrar tempo.

[🟡] Placares — Estilo
N3 "tracker mark" (sem campo), N5 círculos, N6 "tally line" (linhas), N8 e After "tally mark" (linha em branco / 5 caixinhas). Todos de um passo só, como manda a regra 3; o estilo varia. Não alterado.

[🟡] p7 (N1 Word Hunt) — Instrução
"Look across and up and down" sugere ler de baixo para cima; as palavras só vão da esquerda para a direita e de cima para baixo (N6 diz "across or down"). Texto aprovado, mantido.

[🟡] p1-2 (copyright) — Redação
"The activities and puzzle pages in the Answer Key are intended for personal, non-commercial use." sugere que o Answer Key tem páginas de puzzle. Sugestão em questions.md.

[🟡] p44 (N7 story) — Generalização
"Every night of Hanukkah, kids get gelt" e "not only in December" generalizam (nem toda família dá gelt toda noite; a data da festa varia entre novembro e dezembro). Texto aprovado; sugestão: "Many families give gelt..." e "all year long". Não alterado.

[🟡] p51 (N8) — Repetição
A história e a caixa "What's Hanukkah?" explicam "dedication" quase com as mesmas palavras na mesma página. Texto aprovado, mantido.

## 🔵 RECOMENDAÇÕES
- Padrão de fecho das histórias: quase toda história termina numa frase-resumo arrumada (N1 "one family, one no, one mountain at a time"; N3 "one jar, one day of oil, and eight days of light"; N4 "That's not just decoration. That's the whole tradition..."; N8 "That's eight nights of light, still going"), com "not just X" em N4 e N7. É uma assinatura coerente, mas lida de uma vez parece fórmula. Variar 1 ou 2 fechamentos na próxima edição.
- Páginas com bastante branco, todas intencionais ou de espaço de escrita: p3, p17 (caixa "My guess" de 3.4in), p20, p23, p29, p36, p43, p50.
- Artes 42b/42d (8 velas) e 42c (3 velas) na Noite 4 (que conta 4 + shamash): já em questions.md.
- Página final anuncia "Seder Night" como próximo livro; manter só se a série for confirmada.

## 2. Consistência entre as 8 noites (conferido por código e nas folhas)
Padrão de abertura (selo NIGHT + título), selo ★/★★ em todas as atividades, rótulos "Tonight's Story" e "Before the Candles", corpo (13pt instruções, 15pt história), respostas em linha em branco ou círculos, folio no mesmo lugar (espelhado par/ímpar, mesma altura) em todas as páginas numeradas. Grafias fixas íntegras (nenhum Chanukah, hanukiah, menora, shamesh, dreidl etc.); "Modiin" sempre assim. Travessão longo e meia-risca: zero em corpo de texto (só o do título "Night N — ..." do tema). Zero Natal. Zero letra hebraica em script. Placeholders: nenhum no texto.

## 3. Impressão
Noite 1 em p5; template do dreidel (N5) em p33 (ímpar) com verso p34 em branco sem folio; frente do Coupon Book (N7) em p47 (ímpar) com verso p48 sem folio e mesma grade (conferida a simetria duplex: 0,65in x 0,6in de margem espelham); certificado em p55 sem folio e com moldura dentro da área segura; nada cortado; nada encostado na margem. 64 páginas mantidas depois das correções. `./st check --pdf`: 0 achados (DPI, fontes, margens).

## 4. Answer key (amostra visual p59-64)
Seis páginas, por noite e nível, títulos iguais aos do corpo, cobre todas as atividades de resposta única (N1 3, N2 5, N3 4, N4 3, N5 2, N6 3, N7 3, N8 quiz). Gelt Math 2 ("3 cousins") e 3 (nova redação) batem com 6 e 16. Count the Gelt conferido contra a arte (8 e 13).

## Alterações de texto (todas registradas em questions.md)
1. `content/n5.typ`, Gelt Math 3: "Then you spin a Hei and have to put half of your coins back in the pot." -> "Then you give half of your coins to your little cousin."
2. `content/n7.typ`, Split and Save 1: nova redação (acima).
3. `content/_how-to-use.md`: hífens em "grown-up" e "seven-year-old".
