# Perguntas e decisões

Formato: `- [ ] [BLOQUEANTE|ASSUMIDA] (etapa) pergunta — assumido: ...`. Marque [x] quando resolvida.

## Abertas

- [ ] [BLOQUEANTE] (matter) Link/QR do bônus Family Pack: o texto aprovado usa `readpublishingco.com/hanukkah-pack`, que era placeholder. Qual é a URL real (e o QR)?
- [ ] [ASSUMIDA] (unit:n1) Ilustração 1.4 (hanukiá da Noite 1): no `ilustracoes-prompts-geracao.md` de 30/09 estava "não aprovada" (4 suportes de um lado, 5 do outro), mas já existe `14.png` do mesmo dia. Assumido que `14.png` é a versão corrigida; confirmar visualmente.
- [ ] [ASSUMIDA] (unit:n2) Ilustração 2.4 (menorá de 7 braços) existe, mas depende de o revisor religioso confirmar 7 braços x 8+1. Usar `24.png` e revisar depois.
- [ ] [ASSUMIDA] (unit:n8) 81 e 83 saíram do gerador com 1131 px de largura; ampliadas 2x (306 DPI em 7.4in) com traço reforçado. Originais em `inputs/illustrations/_raw/`. As demais artes novas ficam em ~265-355 DPI nas larguras previstas.
- [ ] [ASSUMIDA] (unit:n7) 7.3 (ícones gelt + caixa) e 7.4 (6 ícones dos vales) vieram como uma imagem cada, com os ícones soltos: recortar cada ícone na diagramação (por código ou Canva). A FM.1 (`FM1.png`) também foi gerada; ainda depende da revisão religiosa do mini-guia.
- [ ] [ASSUMIDA] (unit:n5) `noite5_template_dreidel.png` é 1679x938 em RGBA (transparência): converter para fundo branco na diagramação.
- [ ] [ASSUMIDA] (copyright) O texto antigo do copyright dizia "Published by Golden Chapter Press" (resquício do livro 12). Assumido: imprint Jonah Feldman / Read Publishing Co. Confirmar a linha do editor.
- [ ] [ASSUMIDA] (build) Tipografia: Atkinson Hyperlegible 13pt no texto + Barlow nos títulos (já em `fonts/`; a Andika, fonte infantil, não está em `fonts/`). No projeto antigo a fonte ficou para depois do piloto. Gutter 0.65". Tema em `theme.typ`.
- [ ] [ASSUMIDA] (answer-key) Answer key montada a partir dos gabaritos existentes (`*_gabarito.png/.json`), sem regerar puzzles. Os PDFs piloto antigos estão desatualizados (decisão 48) e NÃO foram trazidos.
- [ ] [ASSUMIDA] (matter) Mini-guia de acendimento e cartão de bênçãos (`legacy/manuscript/`) escritos, mas as grafias e o mini-guia ainda dependem do revisor religioso humano antes de publicar (ver `legacy/docs/revisao-religiosa.md`).
- [ ] [ASSUMIDA] (editorial) Meta de publicação original era 12/10/2026 (Hanucá começa em 4/dez). Se mantida, o prazo é curto: ver plano no chat.

- [ ] [ASSUMIDA] (planejamento) Páginas: a Noite 1 diagramada ocupa 6 páginas (o TOC estimava ~10). Se as 8 noites seguirem esse padrão o miolo fica em ~65-75 páginas, abaixo das 96-104 do TOC. Decidir ao fim das noites: aceitar o número menor (menor custo de impressão, preço $9.99 continua viável) ou acrescentar atividades/páginas de colorir/bônus. Não parei a produção por isso.
- [ ] [ASSUMIDA] (matter) Página de título mostra "Jonah Feldman" duas vezes (autor + imprint). Resolver na tarefa `matter`: mostrar o nome uma vez.

## Resolvidas
- [x] [BLOQUEANTE] (unit:n2) Falta a ilustração 2.2/2.3 (Templo bagunçado, base do jogo dos erros): `inputs/illustrations/22.png` — prompt pronto em `legacy/docs/ilustracoes-prompts-geracao.md`; recorte final 7.4x3.0 in. → GERADA em 2026-10-05 via codex com referências 11/21/14 (arquivos em inputs/illustrations/).
- [x] [BLOQUEANTE] (unit:n5) Falta a ilustração 5.2 (dreidel grande em branco, 4x4 in): `inputs/illustrations/52.png`. A 5.1 (`51.png`) existe. → GERADA em 2026-10-05 via codex com referências 11/21/14 (arquivos em inputs/illustrations/).
- [x] [BLOQUEANTE] (unit:n6) Faltam 6.1 (cozinha, 7.4x2.6 in) e 6.2 (travessa latkes x sufganiyot, 5x2.5 in): `61.png`, `62.png`. → GERADA em 2026-10-05 via codex com referências 11/21/14 (arquivos em inputs/illustrations/).
- [x] [BLOQUEANTE] (unit:n7) Faltam 7.1 a 7.5: `71.png` (criança e caixa de tzedaká), `72.png` (mãos), `73.png` (ícones gelt + caixa), `74.png` (6 ícones dos vales), `75.png` (família no jogo). → GERADA em 2026-10-05 via codex com referências 11/21/14 (arquivos em inputs/illustrations/).
- [x] [BLOQUEANTE] (unit:n8) Faltam 8.1 (hanukiá acesa, página inteira 7.4x9.0), 8.2 (família na última noite), 8.3 (moldura do certificado): `81.png`, `82.png`, `83.png`. → GERADA em 2026-10-05 via codex com referências 11/21/14 (arquivos em inputs/illustrations/).
- [x] [ASSUMIDA] (unit:n3) Os PNGs de puzzle da Noite 3 (`noite3_jarro_diferente` 568x308, `noite3_sudoku4x4` 400x400, `noite3_sudoku6x6` 580x580) são de 21/09 e têm resolução baixa demais para imprimir (mesma causa raiz da decisão 50 do labirinto). Assumido: regerar em alta resolução (ou desenhar em Typst) mantendo as mesmas soluções. → RESOLVIDO 2026-10-05: redesenhados em 5x (sudoku 4x4 2000px, 6x6 2900px, jarros 2840px) por `legacy/scripts/rerender_noite3_hires.py`, lendo os JSONs de gabarito: mesmas grades e soluções, unicidade reconferida. A hanukkiah do 6x6 foi redesenhada maior (estava ilegível); o círculo do gabarito dos jarros passou de vermelho para preto (livro P&B).
- [ASSUMIDA] (unit:n1) Os labirintos (`labirinto_facil.png`, `labirinto_medio.png`) não trazem os rótulos MODIIN / THE HILLS na arte (só aberturas: entrada no alto à esquerda, saída embaixo à direita). Assumido: rótulos em texto acima ("START (top left)") e abaixo ("FINISH (bottom right)") via `maze-ends` em theme.typ. No labirinto médio, o texto do manuscrito manda começar nas colinas e voltar a Modiin; a arte tem a mesma entrada/saída, então START = The Hills e FINISH = Modiin. Confirmar no gabarito que o caminho vale nessa direção (é único e reversível).
- [ASSUMIDA] (unit:n1) O manuscrito diz "Look across and up and down" no caça-palavras (sem diagonais) e "find all ten"; mantidos fielmente. O PNG tem margem branca grande, então foi gerado `puzzle-assets/cacapalavras_noite1_grade.png` (recorte do original, sem alterar o conteúdo). A palavra "Hanukkah" na bênção segue o manuscrito.

