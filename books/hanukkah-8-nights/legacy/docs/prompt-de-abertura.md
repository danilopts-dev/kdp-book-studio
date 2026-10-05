Vamos produzir o livro 13, "8 Nights of Hanukkah Activity Book" (título de trabalho), selo Jonah Feldman / Read Publishing Co. Pasta: `13 - Hanukkah 8 Nights Activity Book - 6-10 years`.

## Leia antes de começar
Deste livro:
- `toc/...- v2.md` (TOC aprovado, com especificação e regras do livro inteiro). O v1 é só histórico.
- `analise-concorrentes.md` (o porquê de cada regra) e `concorrentes/` só se precisar de detalhe.

O pipeline que usamos antes, para replicar a lógica e não a letra:
- Livro 12 (`12 - 70 Reasons to Celebrate Turning 70`): `pipeline.md` (inclui na seção 1.2 as correções A1–A8 herdadas da análise do pipeline de trivia: consumo de tokens era o gargalo), `instrucoes-do-projeto.md`, `reguas-operacionais.md`, `scripts/` (conformidade por script antes do revisor), `diagramacao.md` e `diagramacao/relatorio-diagramacao.md`.
- Livro 11 (`11 - Trivia for Seniors`): `pipeline-automatizado.md`, `gabarito-e-fontes.md`, `editorial-review-passos-2-3.md` e `diagramacao/` (é o precedente de puzzle com gabarito: caça-palavras e cruzadinha).

## O que fazer primeiro
1. Monte um `pipeline.md` para este livro adaptando o do 12. Diferenças que precisam estar lá: aqui o conteúdo é puzzle + texto curto infantil, então todo puzzle é gerado por código com gabarito gerado pelo mesmo código e verificado por script (solução única no sudoku, palavras realmente presentes no caça-palavras, labirinto com saída). Crie as pastas que o pipeline precisar.
2. Monte as réguas do livro (voz para 6–10 anos em inglês americano, humor limpo, zero Natal, caixa "What's a...?", níveis ★/★★) com teto de tamanho, como no 12.
3. Me mostre o `pipeline.md` e as réguas antes de gerar conteúdo. Essa é a primeira parada.

## Depois
4. Piloto: Noite 1 completa, texto + puzzles + diagramação em PDF, com espaços de ilustração dimensionados e rotulados. Segunda parada: eu aprovo visual, nível de dificuldade e voz.
5. Junto com o piloto, me entregue a lista de ilustrações do livro inteiro (o que cada imagem mostra, tamanho, proporção) com prompts prontos para o Google Flow em line art P&B para colorir. As ilustrações são minhas; você encaixa quando eu mandar.
6. Aprovado o piloto: noites 2 a 8, front/back matter e answer key em lote, sem me chamar.
7. Diagramação completa, depois a skill kdp-editorial-review sobre o PDF. Corrija o que ela achar antes de me mostrar.

## Especificação
- 8.5 x 11 in, miolo P&B em papel branco, 96–104 páginas (teto 108)
- Gutter 0.65 in (a KDP rejeitou o 12 com o gutter no mínimo exato de 0.5 in), margem externa folgada, fólio sempre na mesma altura
- Inglês americano
- Estilo de ilustração: ainda não definido; proponha no piloto
- Meta: publicado até 12/10/2026

## Regras de operação
- Gere o máximo sozinho. Revise o próprio trabalho numa etapa separada da geração, como no 12.
- Só me chame para: aprovar pipeline e réguas; aprovar o piloto; receber ilustrações; decisão de conteúdo religioso que não esteja no TOC; qualquer coisa que mude a especificação ou o preço.
- Todo o resto você decide e registra num `relatorio-decisoes.md` o que decidiu sem minha aprovação.
- Mantenha uma lista `hebraico-para-revisao.md` com toda página que tiver letra ou palavra em hebraico, para o revisor humano.
- Tudo marcado [REVISAR] no TOC entra num `revisao-religiosa.md` com a sua melhor versão e a fonte.
- Levante problemas com embasamento e discorde quando tiver razão. Não use travessão longo em nada.
