# NIGHT 3: One Little Jar of Oil
## Texto completo do piloto

---

### Tonight's Story (≈150 palavras)

After the Maccabees cleaned the Temple, they wanted to light the menorah again. That meant finding pure olive oil, oil sealed by the High Priest so no one could doubt it. Judah's men searched everywhere among the wreckage. They found only one small jar with its seal still whole, and it held barely enough oil for a single day.

Making more oil the proper way would take eight days from start to finish. Should they wait in the dark for it? Or light what little they had and hope?

They chose to light it. The story says the flame from that one small jar didn't go out after a single day. It kept burning, night after night, until new oil was finally ready on the eighth day.

That's why Hanukkah lasts eight nights: one jar, one day of oil, and eight days of light.

**(144 palavras)**

---

### What's a miracle? (caixa, ≤40 palavras)

**WHAT'S A MIRACLE?**

A miracle is a wonder nobody saw coming. The Talmud, a great book of Jewish teaching, tells of one small jar of oil that burned for eight days. Jewish families have retold that story for centuries.

**(36 palavras)**

---

### ★ Sudoku 4x4: Jars, Candles, Dreidels, and Stars

**SYMBOL SUDOKU (4x4)**

Fill the grid so every row, column, and small box has all four symbols: jar, candle, dreidel, and star.

*(Puzzle gerado por `gerar_sudoku_simbolos.py`, grade 4x4 com caixas 2x2, 4 simbolos (jarro, vela, dreidel, estrela), solucao unica verificada por contador de solucoes com backtracking. Ver `noite3_sudoku4x4.png` e gabarito.)*

---

### ★ Which Jar Is Different?

**WHICH JAR IS DIFFERENT?**

These eight oil jars look the same. Look closely. Circle the one jar that is different.

*(Puzzle gerado por `gerar_jarro_diferente.py`, grade 2x4 de jarros desenhados por codigo, todos com o mesmo padrao gravado no corpo exceto um; verificado programaticamente que exatamente 1 jarro difere dos demais. Ver `noite3_jarro_diferente.png` e gabarito.)*

---

### ★★ Sudoku 6x6: Six Hanukkah Symbols

**SYMBOL SUDOKU (6x6)**

Fill the grid so every row, column, and box has all six symbols, each one only once.

*(Puzzle gerado por `gerar_sudoku_simbolos.py`, grade 6x6 com caixas 2x3, 6 simbolos: os 4 do nivel ★ mais hanukiá e moeda/gelt, solucao unica verificada por contador de solucoes com backtracking, mesmo metodo do 4x4, com menos pistas dadas. Ver `noite3_sudoku6x6.png` e gabarito.)*

---

### ★★ Which Jar Is the Pure One?

**WHICH JAR IS THE PURE ONE?**

Pretend you're one of Judah's searchers. Use the three clues to find the pure jar.

**Jar A, Jar B, Jar C, Jar D.**

1. The pure jar's seal is not broken.
2. The pure jar was found standing up, not knocked over.
3. The pure jar has the High Priest's own stamp pressed into the seal.

| | Seal | Found | Stamp |
|---|---|---|---|
| Jar A | broken | standing up | none |
| Jar B | intact | knocked over | none |
| Jar C | intact | standing up | High Priest's stamp |
| Jar D | broken | knocked over | none |

Use the table to cross off jars that don't match each clue. Only one jar is left at the end.

*(The High Priest's unbroken seal comes from the story. Clue 2 is made up just for this puzzle.)*

*(Instrução de arte: ver ILUSTRAÇÃO 3.1 em `lista-ilustracoes-livro-completo.md`, quatro jarros de perfil simples lado a lado, rotulados A a D, sem revelar a resposta na ilustração; a tabela acima já está no texto para a criança usar como ferramenta de eliminação, não depende de a ilustração mostrar as diferenças. Pista 2 ("standing up") substituiu a antiga "cera branca" em 26/09/2026: cor de cera não tem base na tradição e podia parecer regra de pureza ritual; a nova pista é lógica de cena, sinalizada ao leitor como inventada para o puzzle. Solução verificada por força bruta testando as 4 opções contra as 3 pistas: só o Jarro C satisfaz as três ao mesmo tempo; ver `scripts/verificar_puzzle_logica_noite3.py`.)*

---

### Before the Candles

**GUESS HOW LONG IT BURNS**

Before you light tonight's candles, everyone guesses how many minutes they'll burn. Write down your guess. Light the candles, then check a clock when the last one goes out. Closest guess gets a tracker mark. Most marks by Night 8 wins bragging rights.

**(43 palavras)**

---

## Checklist da seção 13 das réguas, rodado nesta entrega

1. Tonight's Story entre 120 e 180 palavras: 144, dentro da faixa.
2. What's a miracle? até 40 palavras: 36, dentro da faixa.
3. Zero menção a Natal, direta ou comparativa: confirmado, nenhuma ocorrência.
4. A atividade ★★ é mensuravelmente mais difícil que a ★ em pelo menos dois eixos da seção 4: sim, em ambos os pares. Sudoku 6x6 (★★) tem grade maior (36 células vs. 16), mais símbolos a rastrear (6 vs. 4), e menos pistas dadas (14 vs. 6), exigindo mais dedução por casa vazia. "Which jar is the pure one?" (★★) exige ler e cruzar 3 pistas textuais numa tabela de eliminação lógica, contra "Which jar is different?" (★), que é achar visualmente 1 elemento diferente entre 8, sem leitura nem dedução multi-passo.
5. Placar de um passo só: sim, "Guess How Long It Burns" usa uma marca de tracker por vitória de rodada, sem sistema de pontos.
6. Hebraico presente: não há hebraico novo no texto da Noite 3 (nenhuma palavra hebraica é introduzida; "High Priest" e "sealed" são termos em inglês). Nada novo para `hebraico-para-revisao.md` nesta entrega.
7. Tom da história neutro entre correntes, milagre tratado nem como fato científico nem como lenda descartável: confirmado. "The story says..." introduz o milagre do óleo (seção 7 das réguas), e a caixa "What's a miracle?" atribui a história ao Talmud e diz que ela é recontada há séculos, sem pedir à criança que escolha entre leituras. Revisado em 26/09/2026: a versão anterior ("some families read it as history, others as a story carrying deeper truth") saiu porque colocava a criança como árbitra e podia soar, para famílias ortodoxas, como dúvida sobre a tradição.
8. Nenhum fato inventado fora da tradição: confirmado. A tradição do jarro de óleo que durou oito dias é a do Talmud, Shabat 21b (distinta da narrativa dos Livros dos Macabeus, que não menciona esse milagre; ver `analise-concorrentes.md` e nota abaixo). O detalhe do selo do Sumo Sacerdote no puzzle de lógica é consistente com a mesma tradição rabínica (o jarro reconhecido como puro por trazer o selo intacto).
9. Travessão longo: nenhuma ocorrência em nenhum bloco deste arquivo (usar vírgula, ponto, dois-pontos ou parênteses).
10. Voz com vida, não morna: a história usa tensão real de decisão ("Should they wait in the dark for it? Or light what little they had and hope?") em vez de relato passivo, mantendo o registro de aventura sem medo de verdade, e sem forçar uma resposta científica ao milagre.
11. Marcação ★/★★ presente em todo título de atividade: confirmado.
12. Caixa "What's a...?" presente: confirmado, "What's a miracle?", termo previsto pelo TOC para a Noite 3.

**Nota sobre o fato histórico/religioso (conforme pedido explícito desta tarefa):** a história do jarro de óleo que durou 8 dias é tradição rabínica (Talmud, Shabat 21b), não aparece nos Livros dos Macabeus, que registram a purificação do Templo (Noite 2) como um evento militar/histórico sem o milagre do óleo. O texto desta noite segue a régua 7 e conta a tradição do óleo como a tradição conta ("the story says..."), sem afirmar como fato cientificamente provado nem descartar como lenda. A caixa "What's a miracle?" atribui a história ao Talmud sem arbitrar entre leituras (reescrita em 26/09/2026, ver checklist item 7). Este bloco não estava na lista original de itens [REVISAR] do TOC v2 (que cobre outros seis pontos, ver `pipeline.md` seção 6.3), mas por ser um ponto sensível de leitura religiosa dentro do judaísmo, foi acrescentado a `revisao-religiosa.md` nesta entrega, como item novo, para o revisor humano local confirmar que a formulação está adequadamente neutra.

**Nota sobre os puzzles desta noite:** os dois sudokus de símbolos (4x4 e 6x6) e o "which jar is different" são gerados por código, com verificação de solução única e de "exatamente 1 diferente" embutida no próprio script, igual ao tratamento dado aos puzzles gerados por código nas Noites 1 e 2. O "which jar is the pure one?" é puzzle de lógica textual (tipo clue puzzle), verificado por força bruta separadamente (script pequeno, ver acima), e usa espaço de ilustração reservado e rotulado no PDF, tratado como apoio visual, não como arte fina, igual ao padrão de ILUSTRAÇÃO usado nas noites anteriores.
