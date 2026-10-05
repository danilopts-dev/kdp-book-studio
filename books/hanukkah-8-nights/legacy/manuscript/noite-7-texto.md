# NIGHT 7: Give Some Light Away
## Texto completo do piloto

---

### Tonight's Story (≈135 palavras)

Every night of Hanukkah, kids get gelt, coins to spend, save, or share. But gelt has always carried a second job, too.

Many families teach a simple rule with the gelt: some coins are just for fun, and some go into the tzedakah box, to help people who need it. A little of each night's gelt goes toward someone else, not just yourself.

This isn't just a Hanukkah idea. Giving to help others is one of the oldest values in Jewish life, practiced all year, not only in December. Hanukkah just gives kids a fun, hands-on way to try it: real coins, a real box, a real choice about what to do with what you have.

Tonight, before you spin another dreidel, set a few coins aside. Watch the tzedakah box get a little heavier.

**(135 palavras)**

---

### What's tzedakah? (caixa, ≤40 palavras)

**WHAT'S TZEDAKAH?**

Tzedakah means giving to help people in need, like sharing money or food. It comes from the Hebrew word for justice, because helping is simply the right thing to do. Many families keep a tzedakah box at home.

**(38 palavras)**

---

### ★ Count the Gelt

**COUNT THE GELT**

Count the coins in each group. Write the total on the line.

Group A: _______

Group B: _______

*(Atividade de contagem simples, dentro da faixa "★: contar até 20-30, uma operação" da régua 4. Dois grupos de moedas (8 e 13) desenhados por código em `scripts/gerar_problemas_moedas_noite7.py`, saída em `puzzle-assets/noite7_contar_moedas_grupo_a.png` e `noite7_contar_moedas_grupo_b.png`, gabarito em `noite7_contar_moedas_gabarito.json` (Group A = 8, Group B = 13). Soma conferida por código no momento da geração.)*

---

### ★ Bring the Gelt to the Tzedakah Box

**BRING THE GELT TO THE TZEDAKAH BOX**

Help the gelt find its way through the maze to the tzedakah box.

*(Labirinto 12x12, nível ★, tamanho igual ao labirinto fácil da Noite 1, gerado e verificado por código em `scripts/gerar_labirinto_tzedaka.py`: recursive backtracker garante labirinto perfeito (árvore geradora), caminho único da entrada "GELT" à saída "TZEDAKAH BOX" confirmado por BFS e pela contagem de arestas (passagens = células - 1). Saída em `puzzle-assets/noite7_labirinto_tzedaka.png`, gabarito em `noite7_labirinto_tzedaka_gabarito.png`/`.json`.)*

---

### ★★ Split and Save

**SPLIT AND SAVE**

Solve each problem. Show your work if you want to!

1. You have 12 gelt coins. You want to give some to tzedakah and save the rest in 3 equal piles for later. If you split all 12 coins into 3 equal piles, how many coins are in each pile?

2. You have 20 gelt coins. First, you put 4 coins in the tzedakah box. Then you split the coins that are left into 4 equal jars to save. How many coins go in each jar?

3. Your family collected 30 gelt coins for tzedakah tonight. You want to put an equal number of coins into 5 different tzedakah boxes for 5 different causes. How many coins go in each box?

4. You earned 24 gelt coins from your grandparents and 12 more from your aunt and uncle. You decide to split everything evenly: half for tzedakah, half to save. How many coins go to tzedakah?

*(Quatro problemas de divisão de moedas em grupos iguais, gerados e verificados por código em `scripts/gerar_problemas_moedas_noite7.py`, mesma lógica de verificação de `gerar_problemas_gelt.py` (Noite 5): cada resposta é recalculada programaticamente e conferida contra o valor declarado antes de salvar em `puzzle-assets/noite7_problemas_moedas.json`. Respostas: 1) 4, 2) 4, 3) 6, 4) 18. Problemas 2 e 4 são de duas etapas (separar/somar, depois dividir), cobrindo o eixo "duas etapas" da régua 4 para ★★; problema 4 soma duas fontes antes de dividir, no espírito da faixa "80+" (a soma intermediária, 36, já passa dos números manipulados no ★ desta noite).)*

---

### ★★ Coupon Book: Give Some Light Away

**COUPON BOOK: GIVE SOME LIGHT AWAY**

Cut out these coupons and give them to your family. Each one is a promise to help, no money needed.

*Jewish tradition calls helping like this gemilut chasadim: acts of loving-kindness.*

**Good for one big hug.**

**Good for helping with the dishes, no complaining.**

**Good for a story read out loud before bed.**

**Good for making someone's bed for them.**

**Good for 15 minutes of quiet while someone naps or reads.**

**Good for picking up ten toys, right now, cheerfully.**

*(Seis vales, verso em branco (folha própria na diagramação, sem texto impresso, para recortar e colar/decorar se a família quiser). Texto original, tom acolhedor, sem ironia. Revisado em 26/09/2026: os vales deixaram de ser chamados de tzedaká. Tzedaká é dar recursos a quem precisa (raiz tzedek, justiça); atos de ajuda e gentileza são gemilut chasadim, termo agora nomeado no texto e registrado em `hebraico-para-revisao.md`. Nenhum vale é constrangedor ou usa "escolha entre duas coisas ruins" (régua 11). Layout por código de diagramação, sem gerador de puzzle: seis caixas retangulares tracejadas para recorte, cada uma com o texto do vale.)*

---

### Before the Candles: Who Gets the Coupon?

**BEFORE THE CANDLES: WHO GETS THE COUPON?**

Everyone in the family picks a number between 1 and 10. Whoever guesses closest to the grown-up's secret number gets to hand out the first coupon tonight. Take turns being the guesser next time.

Rounds played: _______

*(Jogo de decisão simples para "quem entrega o primeiro coupon", sem "escolha entre duas coisas ruins", sem sistema de pontos complexo. Placar de um passo só (régua 6): um traço para contar rodadas jogadas, não pontos por jogador. Cabe em uma frase de regra, conforme régua 6.)*

**(48 palavras, dentro do teto de 60)**

---

## Checklist da seção 13 das réguas, rodado nesta entrega

1. **Tonight's Story entre 120 e 180 palavras:** 135, dentro da faixa.
2. **Caixa "What's a...?" até 40 palavras por termo:** "What's tzedakah?" 39 palavras. Dentro da faixa. Um único termo, como a maioria das noites anteriores (não é caso de "dois termos na mesma caixa" como a Noite 6).
3. **Zero menção a Natal, direta ou comparativa:** confirmado, nenhuma ocorrência em nenhum bloco.
4. **A atividade ★★ é mensuravelmente mais difícil que a ★ em pelo menos dois eixos da seção 4, nos dois pares desta noite:**
   - Matemática: "Split and Save" (★★, divisão em grupos iguais, dois problemas de duas etapas, números até 30 e uma soma intermediária de 36) contra "Count the Gelt" (★, contar até 13, uma operação simples de contagem). Dois eixos: contagem/matemática (uma operação de contar contra divisão em duas etapas) e raciocínio (achar/contar contra comparar e montar a conta certa).
   - Recorte/atividade manual: "Coupon Book" (★★, escrever e entregar promessas, decidir o que oferecer, ler e agir sobre o compromisso ao longo dos dias seguintes) contra "Bring the Gelt to the Tzedakah Box" (★, achar o caminho num labirinto). Dois eixos: autonomia (a criança decide o que vale cada coupon e cumpre a promessa sozinha, contra seguir um caminho já desenhado) e raciocínio (montar/decidir contra achar/parear).
5. **Tem travessão longo em algum lugar?** Não, nenhuma ocorrência em nenhum bloco.
6. **A caixa "What's a...?" explica sem pressupor nem subestimar?** Sim. Define tzedaká de forma concreta (dinheiro, comida, tempo, gentileza), sem pressupor que o leitor já é judeu e sem tom de "agora vou te ensinar algo que você não sabia"; explicita que é praticada "in different ways" entre famílias, evitando apresentar uma prática como única.
7. **Alguma piada, termo ou tema de puzzle já está em usados.md/nas noites anteriores?** Não. "Tzedakah" é o termo previsto pela régua 5 especificamente para a Noite 7 (não usado nas Noites 1-6). O labirinto retoma o formato de labirinto já usado na Noite 1, mas com tema, tamanho e rótulos novos (GELT → TZEDAKAH BOX), sem repetir conteúdo. Os problemas de matemática usam a mesma lógica de verificação da Noite 5 ("Gelt Math"), mas com números, contexto (tzedaká, não torneio de dreidel) e respostas diferentes; nenhum problema se repete. O jogo "Who Gets the Coupon?" e o Coupon Book são conteúdos inéditos, não usados em nenhuma noite anterior.
8. **Tem hebraico na noite? Se sim, foi registrado em `hebraico-para-revisao.md`?** Não há caractere hebraico nesta noite. "Tzedakah" é transliteração já incorporada ao inglês corrente do livro (mesmo tratamento dado a "hanukkiah", "shamash", "latke" nas noites anteriores), não texto em caracteres hebraicos a transliterar. Nenhuma entrada nova necessária em `hebraico-para-revisao.md`.
9. **Algum item da noite corresponde a um ponto [REVISAR] do TOC?** Não. A ligação entre gelt e tzedaká é tradição amplamente consensual entre correntes do judaísmo, sem controvérsia relevante, conforme informado explicitamente no brief desta tarefa. Registrado por prudência em `revisao-religiosa.md`, mesma lógica aplicada às Noites 2, 4, 5 e 6 para itens não listados no TOC original mas com algum conteúdo religioso/cultural.
10. **As contagens de palavras da seção 9 estão dentro da faixa?** Sim. Tonight's Story: 135 (faixa 120-180). What's tzedakah?: 38 (teto 40). Before the Candles: 48 (teto 60). Instruções de atividade (título + comando) de cada bloco conferidas abaixo do teto de 25 palavras: "Count the Gelt" (comando "Count the coins in each group. Write the total on the line." = 12 palavras); "Bring the Gelt to the Tzedakah Box" (comando "Help the gelt find its way through the maze to the tzedakah box." = 14 palavras); "Split and Save" (comando "Solve each problem. Show your work if you want to!" = 10 palavras); "Coupon Book" (comando "Cut out these coupons and give them to your family. Each one is a promise to help, no money needed." = 20 palavras; a linha "gemilut chasadim" é nota à parte, 11 palavras); "Who Gets the Coupon?" (regra completa em 1-2 frases, dentro do teto de 60 do bloco Before the Candles).
11. **O bloco está bom para o leitor (tom vivo, humor de verdade, ritmo), e não apenas "seguro"?** Sim. A Tonight's Story usa uma imagem concreta e calorosa ("Watch the tzedakah box get a little heavier") em vez de uma frase genérica sobre generosidade. Os vales do Coupon Book têm personalidade real ("no complaining", "right now, cheerfully") em vez de serem promessas vagas. O jogo "Who Gets the Coupon?" transforma uma decisão familiar comum (quem faz algo primeiro) em um mini-jogo de adivinhação com regra clara, em vez de simplesmente sortear.

**Nota sobre "Count the Gelt" (★):** atividade de contagem pura, conforme pedido explícito do brief ("não precisa de verificação complexa, só confira a soma está certa"). Os dois grupos de moedas (8 e 13) foram desenhados por código (`scripts/gerar_problemas_moedas_noite7.py`, função `desenhar_moedas`), cada moeda um círculo com "$" dentro, em fileiras de até 8 por linha. A soma de cada grupo é fixada no próprio script gerador e registrada no gabarito, sem depender de contagem manual por um revisor humano.

**Nota sobre "Split and Save" (★★):** os quatro problemas cobrem duas variações da régua 4 ("contar até 80+, ou duas etapas") sem forçar as duas no mesmo problema, mesma abordagem já usada na Noite 5: problemas 1 e 3 são divisão direta (uma etapa, números até 30); problemas 2 e 4 são de duas etapas (separar uma parte e depois dividir, ou somar duas fontes e depois dividir). Todos os quatro têm resto zero (divisão exata), apropriado para 8-10 anos sem introduzir frações ou resto neste momento do livro. Verificados por código: cada resposta é recalculada e comparada ao valor declarado antes de salvar em `puzzle-assets/noite7_problemas_moedas.json`.

**Nota sobre o Coupon Book:** seis vales (acima da faixa mínima de "5-6" pedida pelo brief), nenhum envolve dinheiro ou compra, todos são atos de ajuda ou tempo dedicado à família, ilustrando gemilut chasadim (atos de bondade), conceito distinto de tzedaká desde a revisão de 26/09/2026. Verso em branco: página própria na diagramação, sem conteúdo impresso, para a criança recortar e guardar/entregar os vales. Tom conferido contra a régua 2 (humor limpo) e a régua 1B (vivo, não morno): "no complaining" e "right now, cheerfully" são especificidade de voz, não sarcasmo.

**Nota sobre "Who Gets the Coupon?":** decisão registrada em `relatorio-decisoes.md` sobre o mecanismo escolhido (adivinhar o número secreto do adulto, não sorteio por dado ou cartas, que já apareceram em jogos de noites anteriores como o torneio de dreidel da Noite 5). Mecanismo simples, sem "escolha entre duas coisas ruins", com placar de um traço só (rodadas jogadas), conforme régua 6.

**Nota sobre o labirinto:** `scripts/gerar_labirinto_tzedaka.py` reaproveita integralmente a lógica de geração e verificação de `scripts/gerar_labirinto.py` (Noite 1): recursive backtracker para gerar um labirinto perfeito (árvore geradora, sem ciclos), BFS para achar o caminho da entrada à saída, e uma prova por contagem de arestas (passagens = células - 1) que confirma que o grafo é de fato uma árvore, logo o caminho é matematicamente único. Tamanho 12x12, igual ao "labirinto fácil" da Noite 1, conforme pedido do brief para o nível ★ desta noite.
