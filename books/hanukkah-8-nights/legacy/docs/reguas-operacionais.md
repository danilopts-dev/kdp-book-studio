# RÉGUAS OPERACIONAIS
## 8 Nights of Hanukkah Activity Book (título de trabalho) · Jonah Feldman

**Este é o único bloco de régua que entra em sessão de geração de texto.** Teto declarado: 200 linhas, como no livro 12. O raciocínio e o histórico de decisões vivem em `relatorio-decisoes.md`, que o Gerador nunca lê.

Vale só para a Linha A (texto). A Linha B (puzzle) segue a especificação técnica de cada script, em `scripts/README.md`.

---

## 1. PÚBLICO E VOZ

- Público: 6 a 10 anos, dois níveis dentro dessa faixa (ver seção 4). Inglês americano.
- Narrador conta a história de Hanucá como quem conta para uma criança que está ouvindo pela primeira vez ou pela décima, sem pressupor conhecimento prévio e sem tom de aula.
- Frases curtas. Uma ideia por frase na maior parte do texto; frase mais longa só quando o ritmo pedir, nunca por padrão.
- Segunda e terceira pessoa, conforme o bloco: a história é narrada (terceira pessoa, sobre os Macabeus), as instruções de atividade falam direto com a criança ("Find the words hiding in the grid").
- Contrações obrigatórias no texto corrido (não nos rótulos de atividade). "You'll", "let's", "it's". Texto sem contração soa a manual, não a livro infantil.
- Sem ironia, sem trocadilho que dependa de vocabulário adulto, sem referência cultural que uma criança de 6 anos não tenha.

---

## 2. HUMOR

- **Humor limpo e acolhedor.** Bobo pode (trocadilho, situação exagerada, animal falando). Nojento, escatológico ou "escolha entre duas coisas ruins" (o tipo de piada que força a criança a rir de alguém perdendo), não.
- Piada e charada são originais. Não copiar formato nem texto de fontes existentes (a régua do TOC pede 30 a 40 piadas/charadas originais e limpas, sem copiar de coletâneas comerciais).
- Cada piada/charada nova é conferida contra `usados.md` antes de entrar no livro: nem a piada em si nem a estrutura dela ("Why did the X...?" repetido de forma reconhecível) pode se repetir entre noites.

---

## 3. ZERO NATAL

- Nenhuma menção ao Natal, em nenhuma forma. Isso inclui comparação disfarçada de neutralidade: "not Jewish Christmas", "like Christmas but for Hanukkah" e qualquer construção que use o Natal como referência para explicar Hanucá, mesmo para negá-la. Hanucá se explica por si mesma.
- Nenhum símbolo, cor ou objeto associado a Natal (árvore, meia, Papai Noel) aparece em nenhuma ilustração descrita ou puzzle, mesmo como distrator ou erro de "achar a diferença".

---

## 4. NÍVEIS ★ E ★★

Todo par de atividades de uma noite tem uma versão ★ e uma ★★. Critério objetivo de diferenciação, não é "a mesma atividade só que menor":

| Eixo | ★ (6-7 anos) | ★★ (8-10 anos) |
|---|---|---|
| Leitura exigida | palavras curtas, frase simples na instrução | frase com subordinada, vocabulário mais específico do tema |
| Tamanho do puzzle | grade menor (ex.: caça-palavras 10x10, sudoku 4x4) | grade maior ou com regra extra (ex.: caça-palavras 14x14 com diagonais, sudoku 6x6) |
| Contagem/matemática | contar até 20-30, uma operação | contar até 80+, ou duas etapas (dividir e guardar, problema com gelt) |
| Raciocínio | achar/parear/completar | comparar, deduzir, montar (dobrar e recortar, lógica de eliminação) |
| Autonomia | criança faz sozinha na maior parte | pode envolver decidir, justificar escolha, ou fazer sozinho algo que o ★ faz com ajuda |

Cada atividade nova é conferida contra essa tabela antes de entrar no livro: se uma atividade ★★ não é mensuravelmente mais difícil que a ★ da mesma noite em pelo menos dois desses eixos, ela está errada e volta para reformulação.

Marcação obrigatória no título de cada atividade: ★ ou ★★, visível, conforme regra 1 do TOC.

---

## 5. CAIXA "WHAT'S A...?"

- Uma por noite (às vezes dois termos na mesma caixa, quando o TOC pede, como "menorah vs. hanukkiah").
- 1 a 2 frases. Teto de 40 palavras por termo explicado.
- Não pressupõe que o leitor é judeu ("in Jewish tradition..." é aceitável; "as you know from your family..." não é).
- Não subestima a criança que é: explica o termo mesmo para quem já sabe, sem tom de "agora vou te ensinar algo que você não sabia". Frase neutra, factual, sem elogio nem surpresa fingida.
- Termos previstos pelo TOC, um por noite (conferir contra `usados.md` para não repetir explicação em noites diferentes): Maccabee (N1), menorah/hanukkiah (N2), miracle (N3), shamash (N4), gelt (N5), latke/sufganiyah (N6), tzedakah (N7), Hanukkah/"dedication" (N8).

---

## 6. PLACARES DE UM PASSO SÓ

- Todo placar do livro (torneio de dreidel, quiz da família, "Who Gets the Coupon?") usa tracinho ou círculo por ponto. Uma marca, um ponto, sem sistema de pontuação que precise de explicação (nada de "cada resposta certa vale 2 pontos, bônus de 5 se...").
- Instrução do placar cabe em uma frase.

---

## 7. NEUTRALIDADE ENTRE CORRENTES DO JUDAÍSMO

- A história de Hanucá é contada como a tradição conta: nem como fato científico a provar, nem como lenda a descartar. "The story says..." ou equivalente, sem "cientistas descobriram" nem "é claro que isso não aconteceu de verdade".
- Nenhuma prática, costume ou pronúncia é apresentada como "a certa" quando correntes diferentes do judaísmo fazem diferente (exemplo already sinalizado no TOC: a letra Pei do dreidel em Israel, variante regional, não erro a corrigir).
- Onde o TOC já marcou [REVISAR] por causa disso (ver `pipeline.md`, seção 6.3), o texto gerado propõe a versão mais neutra possível e registra em `revisao-religiosa.md`; não decide sozinho qual corrente prevalece.

---

## 8. HEBRAICO

- Permitido no texto e nas ilustrações, conforme o TOC.
- Toda página que tiver hebraico (letra ou palavra) entra em `hebraico-para-revisao.md` no momento em que o Revisor aprova a noite, com o texto, a transliteração e a tradução usados. Isso não bloqueia a aprovação da noite; é revisão em paralelo, antes da publicação.
- Transliteração sempre acompanha o hebraico quando o contexto é uma bênção ou palavra que a criança vai tentar ler em voz alta (ex.: a bênção da Noite 1).

---

## 9. TETO DE TAMANHO POR SEÇÃO

| Bloco | Teto |
|---|---|
| Tonight's Story | 120 a 180 palavras |
| Caixa "What's a...?" | 40 palavras por termo |
| Instrução de atividade (título + comando) | 25 palavras |
| Before the Candles (piada/charada/jogo) | 60 palavras |
| Receita de latke (Noite 6, exceção de formato) | até 250 palavras no total, passos numerados |
| Mad Libs "The Great Latke Disaster" (Noite 6, ★★) | 150 a 220 palavras de história-base, original, sem copiar o formato registrado de coleções comerciais de Mad Libs |

Fora da faixa é achado do script de conformidade de texto (`scripts/conformidade_texto.py`), bloqueio automático antes do Revisor.

---

## 10. PROIBIÇÕES DE LINGUAGEM

**Travessão longo proibido em todo o livro e em toda resposta gerada neste projeto.** Nem em, nem –. Usar ponto, vírgula, dois-pontos ou parênteses. Regra do Danilo, vale para prosa do livro e para qualquer documento de produção.

- Sem gíria adulta, sarcasmo, ou humor que dependa de "entender a referência".
- Sem frase negativa dupla ("not unlike", "isn't uncommon") na voz infantil: direto, positivo, concreto.
- Evitar abrir frase com "And" ou "But" em excesso (aceitável ocasionalmente no registro infantil, mas não em mais de uma frase por bloco).
- Nada de instrução de atividade em forma de pergunta retórica ("Can you find all the words?" é aceitável como abertura de instrução; "Wouldn't it be fun to...?" não).

---

## 11. PROIBIÇÕES DE CONTEÚDO

- Zero Natal, em qualquer forma (ver seção 3).
- Zero conteúdo assustador, violento ou triste de verdade: a perseguição de Antíoco e a fuga para as montanhas (Noite 1) são contadas como aventura e coragem, não como ameaça de medo. Sem descrição de violência.
- Zero "escolha entre duas coisas ruins" como mecânica de piada ou jogo (regra 4 do TOC).
- Zero afirmação de corrente religiosa como única correta (ver seção 7).
- Zero fato inventado sobre a história em si: os eventos centrais (Antíoco, a proibição, Mattathias, Judah, o Templo, o jarro de óleo) seguem a tradição tal como contada nas fontes já levantadas em `analise-concorrentes.md`; o que pode ser inventado é o tom e o detalhe de cor (uma frase de diálogo, uma descrição sensorial), nunca um evento que a tradição não sustenta.
- A conta de 44 velas (Noite 4) e qualquer outro número factual do livro é conferida por script antes de aprovar a noite, não só por leitura humana.

---

## 12. ANTI-REPETIÇÃO

Antes de escrever, o Gerador lê `usados.md` e não repete:
- Piada, charada ou estrutura de piada já usada em outra noite (seção 2).
- Termo já explicado na caixa "What's a...?" (seção 5), a não ser que o TOC peça reexplicar por design (ex.: menorah vs. hanukkiah retoma o shamash já visto na Noite 1, mas com foco novo).
- Tema ou conjunto de palavras já usado em puzzle de outra noite (conferido pelo Gerador de parâmetros de puzzle contra `usados.md`, não pelo Gerador de texto).
- Abertura de frase idêntica entre a Tonight's Story de noites diferentes.

---

## 13. TESTE FINAL POR NOITE (rodar antes de entregar)

1. Alguma frase menciona Natal, direta ou por comparação? Se sim, sai.
2. A atividade ★★ é mensuravelmente mais difícil que a ★ em pelo menos dois eixos da seção 4?
3. Tem travessão longo em algum lugar? Se sim, sai.
4. A caixa "What's a...?" explica sem pressupor nem subestimar?
5. Alguma piada, termo ou tema de puzzle já está em `usados.md`?
6. Tem hebraico na noite? Se sim, foi registrado em `hebraico-para-revisao.md`?
7. Algum item da noite corresponde a um ponto [REVISAR] do TOC? Se sim, foi registrado em `revisao-religiosa.md` com a melhor versão proposta e a fonte?
8. As contagens de palavras da seção 9 estão dentro da faixa?

Se qualquer resposta reprovar, corrigir antes de entregar. Não entregar com ressalva.
