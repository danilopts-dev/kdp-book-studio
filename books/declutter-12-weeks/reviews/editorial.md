# Revisão editorial — The 12-Week Decluttering Workbook

Data: 2026-10-06. Método: leitura dos fontes (`content/*`, `book.yaml`, `toc.md`, `notes.md`, `questions.md`), contact sheet (15 páginas + 5 extras: 7, 8, 119, 120, 121). PDF 122 páginas, 8,5 x 11, P&B. `./st check --pdf`: 0 críticos, 0 major, 1 minor. `./st voice`: intro OK.

Resumo: 🔴 0 | 🟠 2 (corrigidos) | 🟡 6 (4 corrigidos, 2 pendentes) | 🔵 3

## 1. Estrutura

TOC aprovado × units × títulos nos arquivos: coincidem (Intro, Weeks 0-12, Part 3, Part 4, Conclusion; todos os `=` batem com `book.yaml`). Conteúdo de cada item "Key content" do TOC está presente (checado semana a semana). Front matter: título, copyright, contents. Back matter: Printable Declutter Kit, Final Words. Folios e TOC do PDF conferem (Intro 1, Week 0 em 4, Week 1 em 9, Part 3 em 93, Part 4 em 107, Conclusion em 113, Kit em 117, Final Words em 118). Página em branco p.4 é o verso antes da abertura da Introduction (esperado).

Referências "page N of this week" verificadas contra o layout fixo de 7 páginas em wk01-wk12.

## 2. Achados

### 🟠 MAJOR
- **wk07, orientação e Day 3** — Texto mandava o leitor para "page 3" (que é o Reverse-Hanger Test) para roupas que não servem, e dizia "Pages 3 and 4 give each group its own space". Os três grupos difíceis (não serve, "when I lose weight", roupas de festa) estão só na página 4. Correção feita: "Page 4 gives each group its own space" e Day 3 "page 4". `notes.md` ajustado.
- **wk12, Day 3** — "Kids' drawings and school work. Fill in page 3" apontava para a tabela de histórias; a tabela de desenhos e trabalhos escolares está na página 4. Correção feita: page 4.

### 🟡 MINOR
- **wk09, checklist de papel** — "Anything with an account number, Social Security number or birth date goes in the shred bag" contradizia o item seguinte (certidões e escrituras ficam em papel). Corrigido: "...that I don't need to keep...".
- **wk06** — "décor" (com acento) × "decor" em wk05 e wk08. Padronizado "decor".
- **`_bonus.md`** — "the sheets I wanted taped up where I could see them while I worked" inventava experiência pessoal da autora (regra: sem histórias pessoais inventadas). Reescrito em segunda pessoa.
- **wk07, wk08, wk09 (claims soltos)** — "easiest things to sell", "the most sellable thing in your house", "a child who helped choose usually lets the toy go", "Paper is what stalls most people". Suavizados para "some of the easiest...", "often", "stalls a lot of people". Mantida a coerência com o style sheet (sem promessas).
- **Repetição do refrão do timer** — "When the timer rings, stop..." aparece em wk01, wk02, wk05, wk11 e três vezes em wk12 (orientação, mapa e fecha). Variei wk02 e removi o de wk05. Pendente (opcional): wk12 repete duas vezes em duas páginas, o que combina com o tom da semana; deixei.
- **`notes.md`** — o bloco "Fatos wk01 (FDA)" ainda trazia as regras antigas (exceção dos 3 anos do protetor, DEA Take Back Day, hospital), que foram corrigidas em 2026-10-05. Marcado como superado para não induzir agentes futuros.
- **Pendente 🟡** — wk03 checklist diz "paper gets sorted in Week 9", mas a Week 2 já tem a página Keys, Mail and Paper. Não é erro (a Week 9 trata da pilha de papel), só confirma o encadeamento; deixei.

### 🔵 RECOMMENDATION
- **"Where It's Going This Week" é praticamente idêntica em 9 das 12 semanas** ("Decide where each box is headed while the room is fresh in your mind. A box that has a destination actually leaves the house.") e "Check what the place accepts before you go" em 6 delas. Faz sentido como seção fixa, mas variar a segunda frase em 3 ou 4 semanas tiraria a sensação de molde. Não alterei: a seção é fixa por layout.
- **Aberturas de orientação com tríade de exemplos** (wk05 "The remote that belongs to no one, the stack of magazines..., the drawer of cables...", wk06 "The nightstand drawer..., the box..., the chair...", wk10 "Nobody plans..."). O recurso funciona, mas aparece três vezes seguidas; considerar mudar uma abertura em uma próxima edição.
- **Bônus** — a página do Kit promete 3 itens que ainda não existem como PDF (pendência conhecida, em `questions.md`). O QR está a 218 DPI (aviso minor do check); legível e suficiente na largura usada, mas conferir o QR impresso se a página for refeita.

## 3. Conteúdo

- **Coerência entre capítulos:** nomes fixos consistentes (Keep / Donate / Sell / Toss, sell threshold, landing zone, reverse-hanger test, Sell Tracker, Donation Log, one in one out, 15-minute reset, *House Cleaning Checklist Planner*). A lista de 12 cômodos é idêntica em Week 0, Part 4 e Conclusion. Pontes cumpridas: sell threshold da Week 0 → semanas e Part 3; "Keep for now" da intro/wk12 → página "Revisit Keep for now" da Part 4; Sell Tracker e Donation Log de wk07/wk11/wk12 → Part 3; Part 3 Totals → Scoreboard da Conclusion.
- **Promessa do subtítulo:** 15 minutos por dia (7 tarefas diárias por semana), um cômodo por semana, quatro caixas, "No Storage Bins Required" (nenhuma semana manda comprar caixas ou organizadores; wk00 e wk08 dizem explicitamente que não é preciso comprar).
- **Claims e fatos:** FDA, USDA/FSIS e IRS com fonte no corpo da página e cópias em `inputs/reference/sources/`; sem claim de saúde; sem marcas. Form 8283 ($500), reconhecimento ($250), 3/6/7 anos e "good used condition" conferem com `notes.md`. wk09: o prazo geral de "3 years from the date you filed" é simplificação do IRS (3 anos da declaração, ou 2 anos do pagamento do imposto, o que vier depois). Aceitável porque o texto traz "check with a tax professional" e a fonte.
- **Tom (Emily P. Harper):** prático, calmo, sem culpa nem sermão. Sem "transform", "life-changing". Um tique recorrente nas orientações é a frase-fecho aforística curta ("Trust is worth more than space.", "That is your first win."); aceitável, não passa de 4 ou 5 no livro.
- **Voz (human-voice-writing):** sem travessões no corpo (só nos títulos do TOC); pontuação variada; poucas listas de três (intro e orientações). Pontos de atenção já mencionados em 🔵.

## 4. Formato (contact sheet)

Aberturas de capítulo (intro, Week 0, Final Words, Kit) limpas, com respiro; título e folios consistentes (número em círculo, nome da seção no rodapé). Tabelas e grids (Map Your..., Count, Sell Tracker, Part 3 Totals, Monthly Reset, Weekly Counts) com linhas ≥ 0,3", cabeçalho preto legível e nada cortado. Copyright em letra pequena centralizada, como decidido. Página de abertura da Part 4 e das demais não amostradas, mas o check do PDF não acusou problema de fonte, margem ou DPI. Sem answer key (formato planner). Contents completo com folios.

## 5. Pendências que dependem do Danilo (já conhecidas)

Arte da capa e criação do PDF do Printable Declutter Kit. Nenhuma pergunta nova.
