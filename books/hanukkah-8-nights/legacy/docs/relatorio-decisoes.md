# Relatório de decisões
## 8 Nights of Hanukkah Activity Book · Jonah Feldman · Piloto Noite 1

Decisões tomadas sem aprovação prévia do Danilo, registradas conforme instrução do `prompt-de-abertura.md`.

---

## 1. Réguas operacionais e pipeline do livro 13 não estavam nos uploads

O `prompt-de-abertura.md` trata a aprovação de `pipeline.md` e `reguas-operacionais.md` como a primeira parada, já concluída. No entanto, esses dois arquivos não estavam presentes em `/mnt/user-data/uploads/13 - .../`, só os do livro 12 (referência) e do livro 11. Decidi seguir em frente com o piloto usando como régua implícita: o TOC v2 (fonte mais específica e já aprovada), a lógica de diagramação e checklist do livro 12 adaptada ao trim 8.5x11in e gutter 0.65in deste livro, e o padrão de puzzle-com-gabarito-verificado-por-script do livro 11. Recomendo ao Danilo confirmar se esses dois arquivos existem em outro lugar e, se não, tratá-los como pendência formal antes do lote de noites 2 a 8, ainda que o conteúdo deste piloto já siga a lógica deles.

## 2. Lista final de palavras do caça-palavras (Noite 1)

Escolhi: JUDAH, MACCABEE, ANTIOCHUS, MATTATHIAS, TEMPLE, HILLS, TORAH, FAITH, COURAGE, MODIIN. Critério: nomes próprios e lugares da história da Noite 1 (Judah, Maccabee, Antiochus, Mattathias, Modiin) mais palavras-conceito da narrativa (Temple, Hills, Torah, Faith, Courage), todas com até 10 letras para caber na grade 10x10 só horizontal/vertical. Troquei "Temple" para dentro da lista da Noite 1 mesmo sabendo que o Templo destruído é o foco central da Noite 2, porque ele já é mencionado na história da Noite 1 (implicitamente, como algo que existe e será visitado depois); se o Danilo preferir manter "Temple" exclusivo da Noite 2 por clareza narrativa, é fácil trocar por outra palavra (ex. "SOLDIER" ou "MOUNTAIN", ambas cabem).

## 3. Algoritmo de labirinto: recursive backtracker (DFS com pilha)

Escolhido por gerar, por construção, uma árvore geradora perfeita (spanning tree) do grid, o que garante matematicamente caminho único entre quaisquer duas células, sem precisar de heurística de remoção de ciclos depois. A verificação programática no script confere isso de duas formas independentes: (a) contagem de arestas = vértices - 1 (propriedade de árvore) e (b) BFS efetivo da entrada até a saída, que só teria mais de um caminho se houvesse ciclo. Tamanhos escolhidos: 12x12 para o labirinto fácil (★) e 18x18 para o médio (★★), calibrados para a proporção de página do piloto, não testados com crianças reais ainda.

## 4. Layout específico das caixas de ilustração no PDF

Cada caixa de ilustração no PDF usa borda tracejada cinza, rótulo "ILUSTRAÇÃO X.Y, ver lista-ilustracoes.md" e a dimensão em polegadas escritas dentro da própria caixa. Decidi calcular a largura das caixas dinamicamente a partir da caixa de texto real da página (considerando o gutter de 0.65in do lado da encadernação), em vez de usar um valor fixo, para que a caixa já saia correta se o Danilo pedir ajuste de margem depois. As alturas específicas (2.6in, 2.1in, 3.3in, 2.2in) foram escolhidas por mim como estimativa de espaço restante em cada página depois do texto, não medidas com um texto final revisado por diagramador humano.

## 5. Estrutura de 10 páginas do piloto

O TOC estima "cada noite ≈ 10 páginas". Distribui assim: pág 1 Tonight's Story, pág 2 What's a Maccabee + ilustração, pág 3 labirinto fácil, pág 4 caça-palavras, pág 5 labirinto médio, pág 6 Why is Judah called the Hammer + desenho, pág 7 Before the Candles (piada + 1ª bênção), pág 8 Shehecheyanu + ilustração de fechamento, págs 9 a 10 gabarito dos puzzles da Noite 1. Essas duas últimas páginas de gabarito são só para o piloto ficar auto-contido e verificável; no livro final o answer key de todas as 8 noites vai ficar concentrado no bloco "ANSWER KEY" do back matter, conforme o TOC, não espalhado noite a noite.

## 6. Fonte e tipografia do piloto

Usei Helvetica (fonte padrão do reportlab, sem precisar de embed) em vez de escolher já uma serifa/sans definitiva como no livro 12. Isso é deliberado: o piloto serve para validar layout, nível de dificuldade e voz, não a fonte final. Recomendo tratar a escolha tipográfica como uma decisão separada, depois da aprovação do piloto.

## 7. Sem hebraico em script nesta entrega, só transliteração

O TOC permite hebraico no texto. Optei por trazer só a transliteração + inglês na Noite 1 (sem o texto em caracteres hebraicos) porque isso reduz o risco de erro tipográfico sem revisor religioso ainda validado, e porque a régua do livro 12 (adaptada) trata texto com hebraico como algo que precisa entrar em lista de revisão antes de publicar de qualquer forma. Se o Danilo preferir hebraico em script já no piloto, é um ajuste pequeno no texto e no PDF.

---

## Decisões da Noite 2

## 8. `reguas-operacionais.md` e `pipeline.md` do livro 13 continuam ausentes dos uploads

O prompt de abertura da Noite 2 trata esses dois arquivos como já lidos, mas eles não estavam em `/mnt/user-data/uploads/13 - .../` (só os do livro 12, que são de outro livro/imprint, servindo apenas de referência de formato). Segui exatamente o padrão já fixado no piloto da Noite 1 (réguas implícitas: TOC v2 + o checklist de 12 itens já rodado na Noite 1 + a mesma lógica de diagramação/puzzle-com-gabarito-verificado), sem reabrir nenhuma decisão de régua. Mantida a mesma recomendação do item 1: confirmar se esses arquivos existem em outro lugar antes do lote das Noites 3 a 8.

## 9. "Jogo dos erros" tratado como ilustração pareada com lista fechada de diferenças, não gerado por código

Conforme instrução explícita para esta entrega: os jogos de 5 e 10 erros (Templo antes/depois) entraram no PDF como caixa de ilustração tracejada rotulada (mesmo tratamento dado a "Why is Judah called the Hammer?" na Noite 1), com a lista das diferenças escrita por extenso em `noite-2-texto.md` e a entrada 2.2/2.3 de `lista-ilustracoes-livro-completo.md` revisada para bater exatamente com essa lista. Escolhi 5 diferenças "objeto presente/ausente" para a versão fácil e mais 5 (10 no total) para a versão difícil, todas evitando a estátua de deus estrangeiro mencionada na história (ver decisão editorial nº 5 em `revisao-religiosa.md`), para manter a cena apropriada para colorir sem precisar desenhar e depois "remover" uma imagem religiosa sensível.

**Atualização de 29/09/2026:** o método mudou. Em vez de duas cenas desenhadas em pares, o Danilo gera uma única imagem-base (Templo bagunçado com 10 objetos isolados), duplica no Canva e apaga objetos da cópia de baixo. As diferenças passam a ser todas "presente em cima, ausente embaixo". Três itens da lista antiga foram trocados por objetos apagáveis (coluna rachada → pedaço de coluna caído, veneziana rachada → balde tombado, pergaminho no chão → faixa rasgada na parede). Lista nova em `noite-2-texto.md`, prompt em `lista-ilustracoes-livro-completo.md` e gabarito em `scripts/montar_answer_key.py`.

## 10. "Ligar os pontos" gerado por reamostragem de contorno por comprimento de arco, não por contagem manual de vértices

Para garantir exatamente 30 pontos (hanukiá) e 80 pontos (menorá do Templo), defini cada forma como um contorno fechado (uma silhueta em "pente", com pontas retas na hanukiá e pontas curvas de alturas decrescentes na menorá, a central mais alta, imitando o perfil clássico de 7 braços) e reamostrei esse contorno em N pontos igualmente espaçados por comprimento de arco, em vez de contar vértices manualmente. Isso permite ajustar o desenho sem recalcular a contagem de pontos à mão, e facilita a verificação: contei os pontos, testei espaçamento mínimo entre pontos consecutivos e testei ausência de auto-interseção entre todos os pares de segmentos não-adjacentes do polígono fechado (1→2→...→N→1). Os dois puzzles passaram nessa verificação.

**Ressalva a registrar:** para a menorá (80 pontos), o espaçamento mínimo entre dois pontos vizinhos ficou, num ou dois lugares da silhueta, mais apertado (~3.5 a 6px na escala interna do desenho) do que o padrão folgado da hanukiá (~8px), por causa de vales mais estreitos entre braços de alturas muito diferentes. O contorno continua fechado, simples (sem auto-interseção) e com exatamente 80 pontos, mas recomendo que o Danilo (ou o diagramador) olhe a imagem `noite2_ligar_pontos_menora.png` ampliada antes de aprovar, para confirmar que nenhum par de números fica colado a ponto de confundir uma criança de 8-10 anos.

## 11. Shamash desenhado como a 9ª ponta, separada por um vale mais largo, na hanukiá do "ligar os pontos"

Para o "ligar os pontos até 30" representar visualmente a distinção shamash/vela comum (o TOC descreve o shamash como "mais alto, separado"), desenhei a 9ª ponta mais alta e com um espaço maior antes dela, em vez de posicioná-la ao centro como em algumas hanukiot decorativas. É uma escolha de silhueta simplificada para o puzzle funcionar como pente de 30 pontos sem auto-interseção, não uma afirmação sobre onde o shamash "deve" ficar fisicamente (isso já está coberto pela Ilustração 1.2 e pelo mini-guia de acendimento, ambos fora do escopo deste puzzle).

---

## Decisões da Noite 3

## 12. `reguas-operacionais.md` e `pipeline.md` continuam sendo lidos de `/mnt/user-data/outputs/`, não dos uploads

Confirmado nesta rodada: os dois arquivos vivem em `/mnt/user-data/outputs/` (onde as Noites 1 e 2 também os leram), não em `/mnt/user-data/uploads/13 - .../`. Segui a mesma orientação já registrada nos itens 1 e 8, agora com o caminho explicitamente indicado pelo prompt desta tarefa, então deixo de recomendar isso como pendência: está resolvido, só não estava documentado onde procurar.

## 13. Seis símbolos escolhidos para completar o sudoku 6x6 (★★)

O TOC pede 4 símbolos para o 4x4 (jarro, vela, dreidel, estrela) e deixa em aberto quais 2 completam o 6x6. Escolhi hanukiá e moeda/gelt: ambos já são objetos centrais do livro (a hanukiá aparece desde a Noite 1/2, o gelt é o tema explícito da Noite 5), nenhum dos dois é um símbolo natalino nem ambíguo, e ambos são desenháveis com formas simples e distintas dos outros quatro (evitei repetir "objeto redondo" ou "objeto com haste vertical" de forma confusa com o jarro/vela já existentes).

## 14. Método de geração dos dois sudokus: backtracking com contagem de soluções, não geração de um puzzle "conhecido" reformatado

Gerei uma grade solução completa por backtracking com embaralhamento (garante variedade a cada seed), depois removi células uma a uma em ordem aleatória, aceitando a remoção só quando um contador de soluções (backtracking que para ao achar a 2ª solução) confirma que o puzzle continua com solução única. Isso evita copiar um sudoku pronto de alguma fonte e garante, por construção e por reverificação automática antes de salvar, que cada puzzle publicado tem exatamente uma solução. Número de pistas: 6 de 16 células preenchidas no 4x4 (nível fácil, bastante generoso) e 14 de 36 no 6x6 (nível mais difícil, menos pistas), calibrados à mão por tentativa, não testados com crianças reais ainda.

## 15. "Which jar is different?" usa um único eixo de diferença (padrão gravado no jarro), não múltiplos eixos combinados

Para manter a diferença "clara e distinta" como pedido, todos os 8 jarros são idênticos em silhueta, gargalo e tampa; só o padrão gravado no corpo muda (linhas retas em 7 jarros, três bolinhas no jarro diferente). Descartei combinar mais de um eixo de diferença (ex. também variar levemente o tamanho) porque isso arriscaria criar uma segunda leitura de "diferente" não intencional; o script verifica programaticamente que exatamente 1 padrão de jarro é uma minoria de 1 contra os outros 7, então a unicidade da resposta é garantida por construção, não só por inspeção visual.

## 16. "Which jar is the pure one?" usa 3 pistas com uma pista "decisiva" isolada (o selo do Sumo Sacerdote), decisão deliberada de design de puzzle infantil

A verificação por força bruta (`scripts/verificar_puzzle_logica_noite3.py`) mostra que a pista 3 sozinha (selo do Sumo Sacerdote) já aponta para o Jarro C, sem precisar das pistas 1 e 2. Mantive assim de propósito, em vez de forçar uma dependência das 3 pistas juntas: para a faixa etária de 8-10 anos, um puzzle de eliminação com tabela (marcar X em cada coluna conforme cada pista é lida) ensina o método de eliminação mesmo que a pista final já "resolva sozinha"; isso é mais amigável que um puzzle onde nenhuma pista isolada é informativa. Se o Danilo preferir uma versão onde nenhuma pista sozinha decide (mais próxima de um "logic grid puzzle" clássico), é um ajuste pequeno nos dados de selo/cera/carimbo dos 4 jarros, mantendo a mesma estrutura de tabela.

## 17. "Guess How Long It Burns" sem cronômetro de papel impresso, só campo de preenchimento livre

O TOC descreve o jogo só como "cada um aposta quantos minutos as velas vão durar", sem detalhar o formato do placar. Optei por um campo de preenchimento simples ("MY GUESS: ___ minutes / ACTUAL TIME: ___ minutes") em vez de uma tabela de várias rodadas com nomes de família, para caber no teto de uma página e manter a régua de "placar de um passo só" (uma marca de tracker por rodada vencida, sem pontuação numérica cumulativa dentro da própria atividade). Se o Danilo preferir uma tabela nomeada por membro da família, é um ajuste de layout, não de regra.

## 18. Item novo acrescentado a `revisao-religiosa.md` sem estar no TOC original: a neutralidade da caixa "What's a miracle?"

O TOC v2 não lista este ponto entre os seis itens [REVISAR] originais (ver `pipeline.md`, seção 6.3). Acrescentei mesmo assim, a pedido explícito do prompt desta tarefa, por ser um ponto de leitura religiosa sensível dentro do próprio judaísmo (leitura histórica literal do milagre do óleo vs. leitura de elaboração posterior). Registrado como item 6 em `revisao-religiosa.md`, junto com um segundo item novo (nº 7, o selo do Sumo Sacerdote como critério de pureza no puzzle de lógica), para o revisor humano local confirmar que a formulação está de fato neutra e sem erro de prática.

---

## Decisões da Noite 4

## 19. A conta de 44 velas fecha só sob uma premissa específica sobre o shamash, mantida a resposta do TOC

O TOC v2 propõe 44 como resposta para "How many candles in all eight nights?" e já marca esse item como [REVISAR a conta]. Verifiquei por código (`scripts/verificar_conta_velas_noite4.py`) que a soma das velas de Hanucá (1+2+...+8) é 36, valor não ambíguo, e que o total só chega a 44 se o livro contar 1 shamash novo por noite (8 no total: 36+8=44). Se o shamash físico for tratado como o mesmo objeto reaproveitado noite após noite e contado uma única vez, o total cai para 37 (36+1). Como o TOC já propõe 44, mantive essa resposta no piloto (é a leitura mais direta para a criança, que está contando chamas vistas acesas a cada noite, não objetos-shamash distintos), mas documentei as duas premissas e a conta completa em `revisao-religiosa.md`, item 8, para o Danilo/revisor confirmar antes da publicação. Se a decisão final for 37, o ajuste é pequeno: só a resposta final da tabela e do Answer Key do PDF mudam, a tabela noite a noite continua igual.

## 20. "Number the Steps" usa uma sequência de 4 passos genéricos, sem especificar direção espacial de colocação/acendimento

Decidi manter os 4 passos da atividade de sequenciar (bênção, acender shamash, usar para acender as velas, guardar o shamash) sem mencionar a direção exata de colocação das velas (direita para a esquerda) nem de acendimento (esquerda para a direita), porque esse detalhe pertence ao mini-guia de acendimento do front matter, já marcado [REVISAR] desde a Noite 1 e ainda não escrito. Registrar a ordem espacial exata aqui, antes do mini-guia estar validado, arriscaria a atividade contradizer o front matter depois. Registrado como item novo (nº 9) em `revisao-religiosa.md`.

## 21. Ilustração 4.1 reaproveitada em duas páginas (Tonight's Story e What's a Shamash?), sem numeração nova

Segui o mesmo padrão já usado na Noite 3 (Ilustração 3.1 reaproveitada em duas páginas): a Ilustração 4.1 (hanukiá na janela, vista de fora, à noite) aparece cheia na página 1 (Tonight's Story) e em versão reduzida na página 2 (What's a Shamash?), em vez de pedir uma segunda ilustração dedicada. Isso já estava implícito em `lista-ilustracoes-livro-completo.md` (que só lista 4.1, 4.2 e 4.3 para a Noite 4), então não precisei adicionar nem renumerar entradas nesse arquivo.

## 22. "How Many Candles Tonight?" (★) e "How Many Candles in All Eight Nights?" (★★) tratados como conteúdo tabular, não puzzle gerado por script

Diferente dos puzzles visuais das Noites 1-3 (caça-palavras, labirinto, sudoku, ligar pontos), as duas atividades de matemática da Noite 4 são tabelas e somas simples, sem grade a gerar nem risco de solução múltipla, então não precisaram de um script gerador dedicado. A verificação da resposta (44) ainda passou por script, conforme a régua da seção 11 ("qualquer fato numérico do livro é conferido por script antes de aprovar a noite"), só que o script (`verificar_conta_velas_noite4.py`) confere a aritmética da resposta, não gera o layout da tabela, que foi escrita diretamente no texto e no PDF.

---

## Decisões da Noite 5

## 23. Tratamento explícito da lenda do dreidel como folclore, mais marcado que a narrativa central de Antíoco/Macabeus

A instrução desta tarefa pedia que a história de "por que as crianças jogavam dreidel" fosse apresentada explicitamente como lenda, não como fato histórico documentado. Usei "Legend has it..." e "The story says..." e acrescentei a frase "Nobody can prove every detail happened exactly that way, but families have passed the story down for generations" na Tonight's Story da Noite 5. Esse grau de explicitação é maior do que o usado na narrativa central do livro (Antíoco, Macabeus, o jarro de óleo), que segue a régua 7 das réguas operacionais (tradição contada como tradição, nem prova nem descarte) sem o mesmo reforço de "não dá para provar cada detalhe". A diferença é proposital: o dreidel-como-disfarce-de-estudo é folclore posterior de origem menos documentada que os eventos centrais da revolta, então o texto reflete esse grau diferente de certeza histórica sem contradizer a régua 7 (nenhuma das duas partes vira "fato científico" nem "lenda a descartar").

## 24. "Match the Letter to Its Meaning" cobre só o significado da letra no jogo; a frase "Nes Gadol Haya Sham/Po" vira bloco curto separado

Decidi não misturar as duas camadas de significado das quatro letras (o que cada letra manda fazer no jogo: nothing/everything/half/put one in vs. a frase completa que as iniciais formam: "A great miracle happened there/here") na mesma atividade de ligar. A atividade ★ cobre só a camada concreta e verificável (o que fazer no jogo), e a frase completa virou um bloco curto de leitura ("What Do the Letters Spell?"), sem nível ★/★★ próprio, para não sobrecarregar a atividade de ligar com dois sistemas de significado ao mesmo tempo. É nesse bloco curto que a variante Pei/Israel [REVISAR] é tratada, como parte do conteúdo regular do texto, não como nota de rodapé separada.

## 25. "Before the Candles" desta noite é um bloco de regras de jogo, mais longo que o teto de 60 palavras da seção 9

A régua 9 das réguas operacionais define um teto de 60 palavras para "Before the Candles (piada/charada/jogo)", pensado para o formato padrão de piada/charada curta. O TOC pede explicitamente para a Noite 5 um "torneio de dreidel da família com regras + placar de tracinhos", que por natureza precisa listar as quatro regras do jogo (Nun/Gimel/Hei/Shin) de forma clara para a família seguir, o que excede 60 palavras. Tratei esse bloco como as outras exceções de formato já previstas na própria seção 9 (receita de latke da Noite 6, Mad Libs da Noite 6): um formato de conteúdo diferente do "piada/charada" padrão, sem teto de palavra fixo, mas ainda dentro do espírito da régua (uma frase por regra, sem prosa desnecessária). O placar em si segue a régua 6 à risca (tracinho por rodada vencida, instrução em uma frase).

## 26. Regras do jogo do dreidel seguem a mecânica real e amplamente praticada (Nun=nada, Gimel=pega tudo, Hei=pega metade, Shin=põe um), apresentadas como "uma versão" (revisado em 26/09/2026, ver decisão 45)

As regras de jogo em si (o que cada letra faz na rodada) não têm variação sectária relevante entre correntes do judaísmo; a única variação regional conhecida é a troca de letra (Shin para Pei em Israel), que não muda a regra (Pei também significa "põe um no pote"). Por isso as regras do torneio no texto usam só "Shin" (a variante padrão fora de Israel, coerente com a atividade "Match the Letter to Its Meaning"), com uma nota implícita de que a versão israelense usa Pei no lugar de Shin, já coberta no bloco "What Do the Letters Spell?" mais acima na mesma noite.

## 27. "Gelt Math" com 4 problemas, um deles de duas etapas, faixa 0-100 (não 80+ estrito)

A régua 4 das réguas operacionais define a faixa ★★ de contagem/matemática como "contar até 80+, ou duas etapas". Optei por cobrir as duas condições com problemas diferentes, em vez de forçar as duas no mesmo problema: o problema 3 é de duas etapas (soma e depois divisão por 2), com resultado 16; o problema 4 é de soma simples de quatro parcelas que passa de 80 (soma 82), cobrindo a faixa alta sem duas etapas. Os problemas 1 e 2 são mais simples (soma de duas parcelas, divisão exata sem resto), para variar o formato dentro da mesma atividade e não repetir a mesma estrutura de problema quatro vezes. Todos os quatro foram verificados por código em `scripts/gerar_problemas_gelt.py`, com checagem de que a resposta calculada bate com a declarada e está dentro de 0-100 (teto de segurança, mais folgado que "80+" para não travar automaticamente um problema de soma de 4 parcelas que passe um pouco de 80).

---

## Decisões da Noite 6

## 28. "Mad Libs" tratado como conceito genérico, nunca como título de página

O TOC pede explicitamente "história para completar no estilo Mad Libs... original, sem copiar o formato registrado". Decidi usar "Mad Libs-style" só como referência de categoria nos documentos de produção (este arquivo, `noite-6-texto.md`), nunca no título impresso da página, que ficou "THE GREAT LATKE DISASTER" (sem menção a "Mad Libs"). A instrução da página usa linguagem genérica ("Fill in the blanks before you read the story out loud"), e os tipos de palavra (name, adjective, noun, verb) são categorias gramaticais padrão, não um layout ou marca de nenhuma coleção comercial específica. A história em si (gato no balcão, latke voando, avó derrubando a tigela) é integralmente original.

## 29. Marcação da receita: "YOUR JOB" em texto, não emoji ✋

A primeira versão do PDF usava o emoji ✋ para marcar os passos que a criança faz. Ao renderizar, a fonte Helvetica do reportlab não tem esse glifo e ele saía como um quadrado preto sólido, ilegível. Troquei para o rótulo em texto "YOUR JOB" (negrito, itálico, coluna própria antes do texto do passo), que resolve o problema de fonte sem perder a função de sinalizar visualmente qual passo é da criança. Aplicado tanto no PDF (`scripts/montar_pdf_noite6.py`) quanto no texto de referência (`noite-6-texto.md`), para os dois ficarem consistentes.

## 30. Lista de palavras dos dois caça-palavras da Noite 6

**10x10 (★, só H/V):** KITCHEN, POTATO, GOLDEN, SPOON, ONION, PLATE, LATKE, PAN, OIL, FRY. Critério: vocabulário de cozinha concreto e curto (a mais longa, KITCHEN, tem 7 letras), apropriado para 6-7 anos, sem repetir nenhum tema de puzzle já usado nas Noites 1-5 (história de Antíoco/Macabeus, sudoku de símbolos, letras do dreidel).

**14x14 (★★, 8 direções incluindo diagonal com reverso):** SUFGANIYAH, DOUGHNUT, TRADITION, GRIDDLE, PLATTER, CRISPY, SIZZLE, FAMILY, JELLY, GRATER. Critério: vocabulário mais longo e mais específico (a mais longa, SUFGANIYAH, tem 10 letras), incluindo os dois termos centrais da caixa "What's a...?" desta noite. Evitei repetir "LATKE", "OIL" e "ONION" da lista do 10x10 para as duas grades não pedirem a mesma palavra em níveis diferentes.

Ambas as listas evitam qualquer termo já usado como palavra de puzzle nas Noites 1 a 5, conferido por leitura cruzada dos scripts anteriores (`gerar_cacapalavras.py`, listas de sudoku e ligar pontos).

## 31. 8 direções (com reverso) no caça-palavras 14x14, não só 4 diagonais sem reverso

A régua 4 pede "grade maior ou com regra extra" para diferenciar ★★ de ★. Optei por permitir as 8 direções completas (H, V, diagonal, cada uma com sentido normal e reverso) em vez de só adicionar diagonais no sentido único, porque isso soma dois eixos de dificuldade ao mesmo tempo (tamanho da grade e regra extra de direção/sentido), deixando a diferenciação inequívoca conforme a régua exige ("mensuravelmente mais difícil... em pelo menos dois eixos"). O script (`scripts/gerar_cacapalavras_14x14_diagonais.py`) verifica programaticamente, para cada palavra, que a direção declarada está entre as 8 permitidas e que cada passo da posição é consistente.

## 32. Estrutura de 10 páginas do piloto da Noite 6

Distribuição: pág 1 Tonight's Story + ilustração, pág 2 What's a latke?/sufganiyah? + ilustração, pág 3 receita de latke (página inteira, conforme TOC "1-2 págs"), pág 4 caça-palavras da cozinha (★), pág 5 Latkes or Sufganiyot? A Family Vote (★), pág 6 The Great Latke Disaster (★★), pág 7 Big Kitchen Word Search (★★), pág 8 Before the Candles (charada + piada), págs 9-10 gabarito dos dois caça-palavras. Mesma lógica das Noites 1-5: gabarito da própria noite incluído no piloto só para ficar auto-contido e verificável; no livro final o answer key concentra-se no bloco "ANSWER KEY" do back matter.

---

## Decisões da Noite 7

## 33. "Count the Gelt" (★) como layout gerado por código, sem verificador de puzzle complexo

Conforme orientação explícita do brief, a atividade de contagem não precisa de verificador de labirinto/caça-palavras: basta que a soma desenhada bata com o total declarado no gabarito. `scripts/gerar_problemas_moedas_noite7.py` desenha os dois grupos de moedas (8 e 13, dentro da faixa "contar até 20-30" da régua 4 para ★) por código (círculos com "$" dentro, sem depender de nenhum asset de imagem externo) e grava o total de cada grupo no mesmo processo que gera o PNG, eliminando a possibilidade de o gabarito divergir da imagem por erro de contagem manual.

## 34. Tamanho do labirinto da Noite 7 igual ao "labirinto fácil" da Noite 1 (12x12)

O brief pediu explicitamente "nível ★, então mais simples (tamanho parecido ao labirinto fácil da Noite 1)". `scripts/gerar_labirinto_tzedaka.py` reaproveita a função geradora de `scripts/gerar_labirinto.py` sem alteração de lógica, só de parâmetros (12x12, seed própria 17, rótulos "GELT" e "TZEDAKAH BOX"). Não foi criada uma versão ★★ do labirinto nesta noite porque o TOC não pede um segundo labirinto para a Noite 7 (o par ★★ desta atividade é a divisão de moedas "Split and Save", não um labirinto maior).

## 35. Problemas de "Split and Save": todos com resto zero, sem fração

Os quatro problemas de divisão de moedas (`scripts/gerar_problemas_moedas_noite7.py`) foram desenhados para nunca deixar resto (12/3, 16/4, 30/5, 36/2), evitando introduzir o conceito de resto ou fração num livro de atividades para 6-10 anos onde isso não é o objetivo pedagógico da seção (o objetivo é ligar tzedaká a uma conta concreta, não ensinar divisão com resto). Dois dos quatro problemas (2 e 4) são de duas etapas (separar e depois dividir, ou somar duas fontes e depois dividir), cobrindo o eixo "duas etapas" da régua 4 exigido para diferenciar ★★ do ★ desta noite, que é só contagem de uma etapa.

## 36. Seis vales no Coupon Book, nenhum envolvendo dinheiro

O brief pedia "5-6 vales diferentes"; optei por seis para dar mais variedade sem se aproximar do teto. Todos os seis vales são atos de ajuda ou tempo (abraço, ajudar na louça, ler uma história, arrumar a cama de alguém, ficar quieto por um tempo, guardar brinquedos), nenhum envolve dinheiro ou compra, para reforçar o próprio ponto da caixa "What's tzedakah?" de que tzedaká é mais ampla que dinheiro. Texto do bloco inclui a frase "not spend money" explicitamente para deixar esse elo claro à criança, não só implícito.

## 37. Verso do Coupon Book em página própria, totalmente em branco

Conforme pedido explícito do brief ("verso em branco"), a página seguinte ao Coupon Book (pág 7 do piloto) reproduz a mesma grade de seis caixas tracejadas, mas sem nenhum texto impresso dentro, só a borda de corte, para a criança decorar ou deixar em branco. Decisão de manter a mesma grade de posições (não um layout diferente) para que, ao imprimir frente e verso e recortar, cada vale physically alinhe com seu verso correspondente.

## 38. Mecanismo de "Who Gets the Coupon?": adivinhar o número secreto, não sorteio

Optei por um jogo de adivinhação (cada um escolhe um número de 1 a 10, quem chega mais perto do número secreto do adulto entrega o primeiro coupon) em vez de sorteio por dado ou carta, para não repetir o mecanismo já usado no torneio de dreidel da Noite 5 (regra 12 do `revisao-religiosa.md`) nem depender de nenhum acessório físico extra (dado, baralho) que o livro não fornece. Placar de um traço só (régua 6): conta rodadas jogadas, não pontos por jogador, já que o jogo em si não acumula pontuação, só decide um turno por vez.

## 39. Estrutura de 9 páginas do piloto da Noite 7

Distribuição: pág 1 Tonight's Story + ilustração, pág 2 What's tzedakah? + ilustração, pág 3 Count the Gelt (★), pág 4 Bring the Gelt to the Tzedakah Box (★, labirinto), pág 5 Split and Save (★★, 4 problemas), pág 6 Coupon Book frente (★★, 6 vales), pág 7 Coupon Book verso (em branco), pág 8 Before the Candles: Who Gets the Coupon? + ilustração, pág 9 Answer Key desta noite (contagem, problemas e labirinto com caminho destacado). Uma página a menos que a Noite 6 porque esta noite não tem duas atividades extensas de texto corrido tipo Mad Libs/receita; o Coupon Book usa duas páginas (frente/verso) em vez de uma, conforme pedido explícito do brief.

---

## Decisões da Noite 8 (última noite regular)

## 40. Estrutura de 9 páginas do piloto da Noite 8

Distribuição: pág 1 Tonight's Story + ilustração de fechamento (8.2), pág 2 What's Hanukkah?, pág 3 Color the Hanukkiah (★, página inteira reservada como caixa de ilustração 8.1, sem puzzle gerado por código, conforme pedido explícito da tarefa), pág 4 Family Hanukkah Quiz perguntas 1-5 (★★), pág 5 Family Hanukkah Quiz perguntas 6-10 + Family Scoreboard, pág 6 Certificado "Official Hanukkah Expert" (moldura de diagramação + ilustração 8.3), pág 7 Before the Candles: Pick Tonight's Joke (três piadas), pág 8 Answer Key desta noite (gabarito do quiz com a noite de origem de cada resposta). Uma página a menos que a Noite 7 porque não há puzzle gerado por script nesta noite (nem labirinto, nem caça-palavras, nem sudoku): o quiz é conteúdo textual e o "Color the Hanukkiah" é ilustração pura, então não há páginas de gabarito visual (mapa/grade) a acrescentar, só o gabarito textual do quiz.

## 41. Dez perguntas no quiz, não oito

O TOC pede "perguntas das 7 noites anteriores" sem fixar quantidade. Escolhi dez para cobrir com folga as sete noites (1 pergunta por Noite 2, 3, 5, 6 e 7; 3 perguntas da Noite 1, que tem mais nomes próprios; 2 perguntas da Noite 4), dentro da faixa 8-10 sugerida pelo brief desta tarefa. Cada resposta foi conferida por leitura direta contra o texto de origem antes de entrar no quiz e reconferida por `scripts/verificar_quiz_noite8.py` (ver relatório de execução, todas as 10 confirmadas).

## 42. Três piadas em vez de uma, com escolha da criança

Conforme o TOC pede explicitamente para a Noite 8 ("a última piada, escolhida pela criança entre três"). As três piadas usam a "última noite" como ocasião comum (festa, mensagem entre velas, noite favorita da hanukiá), deliberadamente diferente da estrutura das piadas/charadas já usadas nas Noites 1 (trocadilho com ferramenta), 2 (charada em rima), 4 (trocadilho "light up a room") e 6 (trocadilho "crack up"), para não repetir estrutura reconhecível, conforme régua 2. Conferência feita contra o texto disponível das Noites 1, 2 e 6 (as três explicitamente pedidas nesta tarefa) e, por segurança extra, também contra a piada curta da Noite 4.

## 43. Certificado tratado como elemento de diagramação, não ilustração fina

Seguindo instrução explícita da tarefa: o certificado "Official Hanukkah Expert" é montado no PDF com moldura dupla (retângulo externo + interno), linhas para nome e data e texto fixo, tudo desenhado por código de diagramação (`scripts/montar_pdf_noite8.py`, função `moldura_certificado`). A ilustração 8.3 (moldura decorativa com ícone de hanukiá), já reservada em `lista-ilustracoes-livro-completo.md` desde o piloto anterior, entra como caixa de ilustração separada dentro do certificado, para o Danilo substituir depois por arte fina se quiser enriquecer a moldura de código.

## 44. Página de colorir da hanukiá sem puzzle gerado

Conforme pedido explícito da tarefa: a atividade ★ desta noite é só a reserva de página inteira como caixa de ilustração tracejada e rotulada (ver `ILUSTRACAO 8.1` em `lista-ilustracoes-livro-completo.md`, já registrada desde o piloto anterior), sem nenhum script de puzzle associado. Único bloco do livro, junto com "Design Your Own Hanukkiah" (Noite 4) e "Color the Dreidel" (Noite 5), que é puramente ilustração/layout livre sem gabarito.

---

## Decisões da revisão cruzada externa (26/09/2026)

## 45. Pontos das revisões de Grok, Gemini, ChatGPT e Qwen aplicados ao manuscrito

Detalhe item a item em `revisao-religiosa.md`, seção do topo. Resumo: acrescentada a bênção "she'asah nisim" que faltava na Noite 1; Shehecheyanu sem o "exclusiva" absoluto; quadro menorá x hanukiá sem "all at once"; caixa "What's a miracle?" reescrita sem pedir à criança que arbitre; pista da cera branca trocada; "Number the Steps" sem fixar o momento de acender o shamash; dreidel como "one easy version"; frituras incluem bimuelos; tzedaká separada de gemilut chasadim.

## 46. 44 velas fica, e o item [REVISAR] fecha

A tabela da atividade soma um shamash por noite de forma explícita, e 44 é o conteúdo de uma caixa padrão de velas de Hanucá. A sugestão de trocar a resposta principal para 36 foi rejeitada porque tiraria o shamash de uma noite cujo tema é o shamash.

## 47. Sugestões rejeitadas

"Lit every day by the High Priest" (qualquer sacerdote acendia); "a tradição sefardita não usa o shamash para acender" (generalização sem base suficiente para entrar no livro, virou só uma nota neutra de variação de costume no mini-guia); script hebraico no miolo (decidido na 49).

## 48. PDFs piloto desatualizados

Depois desta rodada, os PDFs de `diagramacao/` não refletem mais o manuscrito. A regeneração fica para a diagramação final, a partir dos arquivos de `manuscrito/`.

## 49. Aprovação das decisões 45 a 48 e script hebraico

Danilo aprovou em 26/09/2026 todas as decisões da revisão cruzada (45 a 48). Script hebraico: entra só no cartão de bênçãos do Bonus Family Pack; o miolo das 8 noites fica com transliteração + inglês.

*(Nota de 26/09/2026: este arquivo foi sobrescrito por engano por outra sessão entre 07:33 e 08:32 e reconstruído a partir de backup. Se aquela sessão registrou alguma decisão além do caça-palavras pixelizado (a 50 abaixo cita uma decisão anterior sobre o labirinto), ela se perdeu e precisa ser recuperada pelo histórico de versões do OneDrive.)*


## 50. Caça-palavras pixelizado: mesma causa raiz do labirinto (resolução baixa demais para o tamanho de exibição)

O PNG do caça-palavras usava 48px por célula e fonte de 26px — resolução baixa para o tamanho de até 340pt em que é exibido na página (upscale, não downscale, é o que sempre pixeliza). Corrigido: célula, margem, fonte e espessura de linha agora são desenhadas em escala 4x e a imagem é salva nessa resolução mais alta, sem redução depois (mesmo princípio já aplicado ao labirinto no item 48: deixar o PDF reduzir a imagem grande, nunca ampliar uma pequena).

`diagramacao/piloto-noite-1.pdf` sobrescrito com o nome definitivo (o arquivo já estava fechado). O `piloto-noite-1-v2.pdf` criado na rodada anterior pode ser apagado.

## 51. Grafia do hebraico aprovada sem revisor humano adicional

Danilo aprovou em 26/09/2026 as grafias do miolo (três bênçãos da Noite 1, letras do dreidel, frases Nes Gadol Haya Sham/Po, "gemilut chasadim") com base na checagem cruzada das IAs. Pendências restantes: mini-guia de acendimento e cartão de bênçãos do Bonus, ainda não escritos.

## 52. Estilo de ilustração aprovado pelo Danilo (26/09/2026)

Line art storybook simplificado: traço grosso uniforme, sem hachura ou sombreado, proporções levemente estilizadas (nem chibi, nem realista), rostos simples e expressivos, consistente entre cenas históricas (Judah, Templo) e modernas (família, cozinha). Aplicado nos 30 prompts de `[ESTILO: a definir]` em `lista-ilustracoes-livro-completo.md`.

Próximo passo antes do lote completo de ilustração: gerar 3 imagens de teste (uma cena histórica, uma moderna, um objeto/símbolo) para validar consistência de traço entre gerações do Google Flow/Nano Banana 2, já que esse é o risco maior num volume de ~30 imagens, não a escolha do estilo em si.

## 53. Mini-guia de acendimento e cartão de bênçãos escritos

Mini-guia (`manuscrito/front-matter-mini-guia-acendimento.md`): mesma sequência de "Number the Steps", sem fixar o momento de acender o shamash; inclui a regra de sexta-feira porque a 1ª noite de 2026 cai numa sexta; não fixa os 30 minutos mínimos. Cartão (`manuscrito/bonus-cartao-bencaos.md`): três bênçãos em hebraico com nikud, transliteração e inglês idênticos à Noite 1; nome divino abreviado como יְיָ por ser material imprimível e descartável, com linha de aviso de respeito. Hanerot Halalu e Maoz Tzur ficaram de fora.

## 54. Promessa de tempo por noite ajustada após a expansão para 82 páginas (07/10/2026)

Com 6 atividades por noite (em vez de 3-4), "20 a 30 minutos" deixou de ser verdadeiro para quem faz todas as páginas. O how-to-use e a descrição do listing passaram a dizer: 20 a 30 minutos para a história e alguns puzzles, sem obrigação de fazer todas as páginas. A referência ao QR no front matter passou a "perto do fim do livro, logo antes do Answer Key" (o QR está na penúltima página antes da chave, p74, e não na última). Origem: revisão editorial final, `reviews/editorial-final.md`.

---

## Decisões no estúdio (06 e 07/10/2026)

## 55. Projeto migrado para o KDP Book Studio
O livro passou a ser produzido em `books/hanukkah-8-nights/` (repositório do estúdio), com o atalho `Estudio` e a pasta `Entrega/` dentro desta pasta do OneDrive. Os arquivos antigos foram para `_antigo/` (nada foi apagado). Textos, ilustrações e puzzles aprovados foram trazidos sem alteração; os PDFs piloto antigos não, por estarem desatualizados (decisão 48).

## 56. Ilustrações faltantes geradas com referências
As 13 ilustrações que faltavam (2.2, 5.2, 6.1, 6.2, 7.1 a 7.5, 8.1 a 8.3 e FM.1) foram geradas pelo `codex` com as artes 1.1, 2.1 e 1.4 como referência de estilo (06/10). As páginas inteiras (8.1 e 8.3) foram ampliadas 2x.

## 57. Puzzles da Noite 3 refeitos em alta resolução
Sudoku 4x4 e 6x6 e "Which jar is different?" redesenhados em 5x a partir dos JSON de gabarito (mesmas soluções). A hanukkiah do sudoku 6x6 foi redesenhada maior.

## 58. Front matter, QR e bônus
Copyright e "Published by" em Read Publishing LLC. Bônus "8 Nights Family Pack" (cartão de bênçãos, regras do dreidel com placar e 8 etiquetas) produzido em PDF; formulário e e-mail criados no Brevo e testados pelo Danilo; QR no livro. Texto "or visit [url]" removido: o bônus é só por QR.

## 59. Revisão religiosa cruzada 2 (06/10) aplicada
Aprovado pelo Danilo: letras hebraicas isoladas (נ ג ה ש + פ) no dreidel (exceção à decisão 49), instrução do Match "tells you to do in the game", "Adonai" nas traduções (sem "His"), "v'higiyanu", frase de genizá no cartão e cabeçalho do Shehecheyanu sem "Only". Detalhe em `revisao-religiosa.md`.

## 60. Expansão de 64 para 82 páginas (06/10)
Aprovada pelo Danilo: +1 atividade ★ e +1 ★★ por noite (16 páginas) e +2 no answer key. Todas geradas por script, com solução verificada, e revisadas de forma independente. Plano e regras em `reviews/expansao-paginas.md`. Motivo: os concorrentes de 8.5 x 11 têm 68 a 94 páginas.

## 61. Piadas repetidas refeitas (07/10/2026)
Autorizado pelo Danilo depois da revisão editorial final: 5 das 7 piadas seguiam "Why did X...? Because...", 3 giravam em torno de a hanukkiah dar festa ou iluminar um ambiente, e "light up" aparecia em N4, N8-B e N8-C. Mantidas: N1 (toolbox) e N6 (latke, "crack up in the pan"), as duas únicas com "Why did...", mais as charadas da N2 e da N6. Trocadas, todas originais e com o vocabulário do livro: N4 virou "Which candle on the hanukkiah is the best helper in the whole house?" / "The shamash! It's always ready to lend a hand, or a flame, to every other candle." (reforça o termo da própria noite). N8-A virou knock-knock ("Oil who?" / "Oil light the last candle with you, so open the door!"). N8-B manteve o formato "What did X say to Y", sem "lit up" ("Glad you made it! I've been here since Night 1."). N8-C virou "What do you call...?" ("The wick-end, when all eight burn at once!"). A decisão 42 vale: as três da Noite 8 continuam usando a última noite como ocasião comum, agora em três formatos diferentes. Resultado: duas piadas com "Why did", nenhuma estrutura repetida entre noites vizinhas, nenhuma de festa ou iluminar ambiente, "light up" só uma vez no livro (instrução do ligar os pontos da N2). Mesmo tamanho aproximado de cada piada, sem mudar o layout; charadas e answer key inalterados.

## 62. "Ligar os pontos" da Noite 2 redesenhados em _v2 (07/10/2026)
Autorizado pelo Danilo. Arquivos novos `noite2_ligar_pontos_{hanukia,menora}_v2*` (os antigos ficam intactos). Menorá de 80 pontos: silhueta procedural simétrica, 7 braços, claramente reconhecível. Hanukkiah de 30 pontos: 30 vértices desenhados à mão, simétrica, com shamash alto, barra, haste e base; com só 30 pontos não cabem velas de lados paralelos, então ainda lê como candelabro de 9 chamas "dentado". Se o Danilo quiser mais fidelidade, a opção é subir para ~40 pontos (muda o TOC). Rótulos sem colisão (verificado por código).

## 63. Receita de latke: o adulto cuida do ralador (07/10/2026)
O passo 1 deixou de ser "YOUR JOB": "Grown-up grates the potatoes and onion into a big bowl." Alinha o passo com a introdução ("A grown-up handles the grater, the stove, and the hot oil").

## 64. Série de acendimento da Noite 4 refeita (07/10/2026)
Os 4 quadros do "Number the Steps" (`42a_v2.png` a `42d_v2.png`) mostram agora a mesma hanukkiah na Noite 4: 4 velas nos suportes da direita, esquerda vazia, shamash no centro. Antes, o número de velas mudava de quadro para quadro (vazia, 8, 3, tudo aceso) e a vela entrava no suporte do centro. As originais (`42a-d.png`) ficam no projeto. Respostas da atividade inalteradas (2, 4, 1, 3).

## 65. Copyright centralizado na página (07/10/2026)
Pedido do Danilo; texto inalterado.

## 66. Artes 14 e 24 conferidas visualmente (07/10/2026)
`14.png`: 4 suportes à esquerda, suporte alto do shamash no centro (shamash aceso na mão da mãe), 4 à direita, 1 vela no suporte da ponta direita (Noite 1): correta. `24.png`: menorá do Templo com 7 braços e hanukkiah com 9 suportes (4 + shamash + 4) sem chamas: correta. Seguem na lista do revisor humano.

## 67. Jogo dos erros da Noite 2 refeito com cenas completas (08/10/2026)
Pedido do Danilo (p15 e p18: "horrível e super básico"). Duas cenas completas geradas à parte, cada uma com objetos isolados para apagar à mão no Canva: ★ salão do Templo limpo (12 objetos), ★★ pátio do Templo (16 objetos). O "antes" é a cena cortada em faixa 2:1 (1536x768, `noite2_erros{5,10}_antes_v3.png`); o "depois" é o mesmo arquivo com 5 / 10 objetos apagados. Enquanto o Danilo não entrega o depois feito à mão (`noite2_erros{5,10}_depois_v3.png`, mesmo tamanho), o livro usa um depois PROVISÓRIO automático (`_depois_v3_auto.png`). `legacy/scripts/erros_noite2_v3.py` confere por pixel que há exatamente N regiões diferentes e gera o gabarito numerado (`_v3_gabarito_key.png`). Textos de instrução ajustados (já não é "Templo antes/depois da limpeza"). As artes antigas ficam intactas, sem uso.

## 68. Sudokus da Noite 3 com formas simples (08/10/2026)
Pedido do Danilo (p23 e p26: símbolos difíceis de desenhar). 4x4: círculo, quadrado, triângulo, estrela. 6x6: + coração e +. Mesmas grades, pistas e soluções únicas dos JSON já aprovados (reverificadas por código); só o desenho muda. Título "Shape Sudoku"; listing e A+ atualizados ("Shape sudoku"). `legacy/scripts/sudoku_formas_v3.py`; assets `_v3`.

## 69. "Which Jar Is Different?" refeito (08/10/2026)
Pedido do Danilo (p24: tosco). Um jarro ilustrado (alça à direita, selo, faixa de 4 triângulos) repetido 12 vezes em 3 prateleiras; o diferente (linha 2, coluna 3) tem 3 triângulos em vez de 4. Verificado por pixel (11 cópias idênticas). `legacy/scripts/jarro_diferente_v3.py`.

## 70. Velas e hanukkiahs da Noite 4 no traço da `12.png` (08/10/2026)
Pedido do Danilo (p32 e p36: velas toscas). `hk_n0..8.png` e `hk_empty.png` gerados da própria `12.png` (velas recolocadas por noite, a partir da direita, com chama em gota). p32 vira Noite 6 com 4 perguntas (6, 6+1, 8-6, 7+1); p36 vira 4 hanukkiahs em grade 2x2 (noites 3, 8, 5, 6) + 4 perguntas (22, 26, quadro com o dobro da Noite 3, 8-3). Dados em `extra_n4_v3.json`. A página "Draw the Candles" (p33) não foi mexida: segue com `hanukkiah-draw`.

## 71. Contas mais difíceis (08/10/2026)
Pedido do Danilo (p45, 57, 59, 63: fácil demais). N5 Gelt Math ★★ (agora multiplicação, divisão por 6, fração de um quarto, metade de 170): 42, 12, 63, 85. N7 Count the Gelt ★ (grupos em fileiras de 10: 17 e 26, soma 43). N7 Which Pile Has More? ★ (pilhas de 8 a 19 moedas em fileiras de 5; escreve cada contagem e a diferença: 14x9, 8x13, 17x11, 12x19). N7 Split and Save ★★ (48/4=12, (85-25)/4=15, 96/6=16, (38+46)/2/3=14). Todas as contas conferidas por código; respostas só no answer key (`extra_n5_v3.json`, `extra_n7_v3.json`).

## 72. Ajustes após conferência do Danilo (08/10/2026)
Chamas das hanukkiahs encostadas no pavio (p32 e p36). "Draw the Candles" (p33) refeita com a hanukkiah de copos vazios (`hk_empty0.png`, inclusive o copo do shamash) e agora pede só as Noites 3 e 6 (duas figuras grandes, em vez de três pequenas demais para a criança desenhar). "Which Pile Has More?" (p59): cada pilha numa caixinha própria, com espaço entre as duas.

## 73. Jogo dos erros: cenas coerentes, 5 e 7 diferenças (08/10/2026)
O Danilo reprovou as cenas com objetos soltos sem sentido. Duas cenas novas, cada uma uma situação só: ★ salão do Templo pronto para acender a menorá (cortina, estandarte, lamparina pendurada, jarros, mesa, cesta de azeitonas, banquinho com lamparina, menorá), ★★ colheita de azeitonas diante do Templo (burro, carroça, jarros, cesta, bacia, sol, nuvens, pássaros, lamparina no portão). Passam a valer **5 e 7 diferenças** (a ★★ deixou de ter 10) e as imagens entram inteiras em 3:2 (5.0in). Os objetos que o Danilo apaga são escolha dele; `erros_noite2_v3.py` confere por pixel que há exatamente 5 / 7 regiões diferentes. Pasta `Para o Canva (jogo dos erros)` no OneDrive tem as cenas e um guia numerado dos objetos fáceis de apagar. Também: p59 com mais espaço entre as moedas e a linha do número.

## 74. P18 com as imagens do Danilo (olival), 7 diferenças (08/10/2026)
O Danilo gerou e editou as duas imagens da p18 (olival perto de Jerusalém, Templo ao fundo, à distância; "antes" `_raw/erros/s2_user_antes.png`, "depois" `noite2_erros7_depois_v3.png`). Conferidas por código (traço escuro sem par a até 3 px): 7 diferenças, todas coisas retiradas do "depois": 1 oliveira pequena (esquerda, fundo), 2 galhinho com azeitonas no chão, 3 ponta do pano da cabeça do homem, 4 arbusto, 5 cipreste, 6 jarro da direita, 7 galho no canto superior direito. O gabarito (p. do answer key) agora usa a imagem original com bola cinza e número branco, sem destacar a área (também na p15). Texto da p18: "olive grove pictures" (oliveiras não ficavam dentro do pátio do Templo).
