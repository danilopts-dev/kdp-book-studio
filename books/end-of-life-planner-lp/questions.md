# Perguntas e decisões

Formato: `- [ ] [BLOQUEANTE|ASSUMIDA] (etapa) pergunta — assumido: ...`. Marque [x] quando resolvida.

## Abertas

- [ ] [BLOQUEANTE] (unit:welcome) Material real para o Welcome da Emily — contexto: TOC marca [DANILO: needs input]. Preciso de 5 a 10 itens concretos: (1) por que a Emily fez este livro; (2) uma experiência real de organizar os assuntos de um parente (quem, quando, o que faltou, o que foi difícil achar); (3) um detalhe concreto dessa experiência (uma gaveta, um papel, um telefonema); (4) por que letra grande e espaço importam para ela; (5) o que ela diria para quem tem medo de começar. Pode mandar em tópicos, em português.
- [ ] [BLOQUEANTE] (unit:conclusion) Material para a conclusão — contexto: TOC marca [DANILO: needs input]. Preciso de: (1) recomendação de onde guardar o livro (ou deixamos genérico: lugar seguro e conhecido, não no cofre do banco); (2) a quem avisar que ele existe; (3) a versão de casal está confirmada para ser citada? (sim/não); (4) uma frase de fechamento no tom da Emily, se tiver.
- [ ] [BLOQUEANTE] (matter, ch02, ch04, ch06, ch11, back-page) Links reais e QR codes dos bônus — contexto: o livro aponta para o Bônus 1 (Extra Pages Pack) e Bônus 2 (Four-Weekend Plan + e-mails). Preciso: URL curta de cada bônus (ou uma única landing page) e os PNGs em `inputs/` → `qr-bonus.png` (e `qr-bonus2.png` se for outra URL), quadrado, mínimo 600x600 px (1,5" a 300 DPI), preto sobre branco. As unidades podem ser montadas antes; a página do bônus e o build final esperam isso.
- [ ] [ASSUMIDA] (intake) Título/subtítulo = título de trabalho do TOC ("End of Life Planner, Large Print" / "A Guided Organizer with Room to Write — Fill It In Four Weekends"); o listing refina depois. primary_keyword vazio até o listing (CPC sugerido no TOC: end of life planner, large print).
- [ ] [ASSUMIDA] (intake) Autor = Emily P. Harper; imprint_name vazio para não repetir o nome na folha de rosto; copyright fica em nome do autor. Se o copyright deve sair como "Read Publishing Co", me avise.
- [ ] [ASSUMIDA] (intake) Large print: corpo 16 pt (o engine força), linhas de escrita com 0,4" de altura (acima do mínimo de 0,3" do formato), tabelas com no máximo 3–4 colunas por página em 8.5x11. Isso deve empurrar o total para ~145–150 páginas; aceito dentro da faixa do TOC.
- [ ] [ASSUMIDA] (intake) Ordem: o "Welcome" aparece uma vez só, como primeira unidade depois do front matter (título, copyright, "Where this book is kept", sumário, "What this book is, and what it isn't", "Start here: four weekends", página do bônus). O TOC listava Welcome tanto no front matter quanto como seção própria; tratei como a mesma página.
- [ ] [ASSUMIDA] (intake) Disclaimer jurídico curto vai em "What this book is, and what it isn't" (não é testamento, procuração nem diretiva; não substitui advogado) e é repetido em uma linha nos capítulos 12 e 14, como o TOC pede.
- [ ] [ASSUMIDA] (intake) Planner sem datas. Marcador do fim de semana ("Weekend 1 of 4") na abertura de cada capítulo; aviso "Running out of room?" só nos capítulos 2, 4, 6 e 11.
- [ ] [ASSUMIDA] (unit:ch01) A pasta `fonts/` está vazia; o build usa Verdana no lugar da Atkinson Hyperlegible Next. Sigo montando os capítulos com Verdana (mais larga, então o que cabe nela cabe na Atkinson). Antes do build final, baixe a Atkinson Hyperlegible Next do Google Fonts para `fonts/` (README, passo 3).
- [ ] [ASSUMIDA] (unit:ch04) Médicos, farmácia e hospital aparecem no ch02 (lista de ligações: nome e telefone) e no ch04 (ficha médica detalhada). Mantive os dois porque o TOC pede os dois; se preferir, o ch02 p.4 pode remeter ao ch04.

## Resolvidas
- [ ] [ASSUMIDA] (unit:ch01) Layout do sistema visual: abertura compacta (marcador "WEEKEND N OF 4" em caixa alta 14 pt, título 26 pt, intro 16 pt, régua), sem página ímpar forçada nem v(0.9in) do engine, para caber em 2 págs; subtítulos de bloco 18 pt; rótulos de campo 14 pt; tabelas com cabeçalho cinza e linhas de 0,4". Blocos promovidos para lib.typ com prefixo `elp-`.
- ch02 (ASSUMIDA): numeração de chamadas contínua 1-24 entre páginas via novo parâmetro start em elp-table; página 8 só com room-notice (fim de capítulo, conforme bonus_notice).

- ASSUMIDA (ch03): `elp-role-table` promovido de ch02.typ para studio/render/lib.typ (agora com headers/widths/row-h); definição local removida do ch02.
- ASSUMIDA (ch03): inclui páginas de seguros, dinheiro/impostos e funeral além da lista do brief, para fechar 6 págs; só locais, sem números.

- ch04 ASSUMIDA: 12 páginas distribuídas como em notes.md; tabelas de remédios com 3 páginas de 12 linhas + 1 de uso eventual/suplementos; room-notice na última página junto do registro de mudanças. "Hospital I Do Not Want" incluído como opcional.

- ASSUMIDA (ch05): religião/fé incluída como campo opcional ("if any"); certidão de nascimento e passaporte não repetidos, apenas remetidos ao ch03; SS card só "where kept".

- ch06 ASSUMIDA: 16 págs distribuídas como em notes.md; inclui o telefone público do Social Security (1-800-772-1213) e "who I believe is named" em retirement (sem afirmar regra); linhas 0,6". Sem blocos novos.

- ch07 ASSUMIDA: dois telefones oficiais incluídos (Medicare 1-800-633-4227; VA 1-800-827-1000). Se preferir nenhum telefone, remover as duas linhas finais das págs. 3 e 7.
- ch07 ASSUMIDA: "Medicare Advantage / Medigap / Part D" citados só como exemplos de rótulo, sem explicação ou conselho.

- ch08 ASSUMIDA: sem blocos novos; local dos returns só remete a ch03 p.18; "Date of My Last Return" como campo de data; 6 págs exatas.
- ch09 ASSUMIDA: pagina de chaves/alarme sem códigos; utilities em 2 tabelas de 5 linhas (genéricas, sem empresas pré-preenchidas); 'Seasonal Routines' em campos por estação.

- ASSUMIDA (ch10): 4 págs = P1 abertura + campos gerais de cuidado imediato; P2-4 um pet por página. Macro `pet-page` fica no ch10.typ, não em lib.typ.
- ASSUMIDA (ch11): 10 págs; sem coluna de senha; rótulos genéricos (Keep/Memorialize/Close, Legacy Contact) sem procedimentos de empresas; bancos remetem ao ch06; sem blocos novos.
- ch12 (assumida): p.1 aviso de 'não é documento legal' fica na abertura; nenhuma opção médica pré-redigida, só perguntas abertas.

- ASSUMIDA (ch13): caixas de marcar via macro local `choice` no ch13.typ (não promovido ao lib.typ); sem room-notice (alvo de 8 págs); "Who Should Be Told First" fica na p.8 como lista de avisos.

- ASSUMIDA (ch13): ch12 nao usa caixas de marcar (so dica de texto "Yes, No, or Still Deciding"), entao nao ha conflito visual; macros opt/choice ficam locais ao ch13. Se ch14+ precisar de caixas, promover a lib.typ.

- ASSUMIDA (ch14): `opt`/`choice` promovidos do ch13 para lib.typ. Tabela de itens com 37 linhas no total (5+8+8+8) e 1" de altura para a coluna "Why". Página extra "Things I Have Already Promised or Given" e campos de "se duas pessoas querem a mesma coisa" (sem prometer evitar conflito). Nota legal só na P1.

- ASSUMIDA (ch15): distribuição das 6 págs = opener+carta 1 / carta 1 cont. / carta 2 / carta 3 / What I Want You to Know / continuação. Cartas sem nome pré-preenchido ("To:" em branco); perguntas de apoio sob "Some things you might say:" (14 pt cinza). Macros locais ao ch15 (não promovidas ao lib.typ).

- ASSUMIDA (ch16): criado `plan-notice()` no lib.typ ("Want a reminder?"), variante do room-notice sem URL/QR. Texto de ch16 usa os rótulos "Review Date (MM/DD/YYYY)" e datas MM/DD/YYYY nas tabelas. Checklist agrupado por tema (não por capítulo numerado) para caber em 2 páginas.
