# Prompts do Google Flow: A+ de "8 Nights of Hanukkah Activity Book"

Gerados a partir do plano de A+ em `listing.md` (copy dos 5 módulos). Atualizados em 2026-10-10 para a **capa final** (Canva, 09/10) e o miolo final de 82 páginas. Flow: modo imagem, 16:9, 4 gerações por prompt, modelo Nano Banana 2. Depois, recortar cada escolhida para 970 x 600 px no Canva antes de subir ao KDP (não subir o 16:9 cru).

O que mudou em relação à versão de 07/10: a capa final é uma ilustração pintada (noite azul-marinho com estrelas, hanukkiah dourada com luz de vela, jarro terracota com estampa azul, dreidel de madeira, moedas, ramos de oliveira, mesa de madeira). Os prompts antigos pediam "line art de traço grosso com preenchimento chapado", que brigaria com a capa. Agora todos pedem o estilo e a paleta da capa.

## Regras comuns (valem para os 5 prompts)

- Anexar a capa final em TODOS os prompts: `build/aplus-anexos/capa-frente.png` (frente recortada no corte, 1275 x 1651 px). Gerada de `inputs/cover-final.pdf`.
- Estilo: o da capa. Ilustração pintada, quente, com brilho de vela; fundo azul-marinho noturno com estrelas douradas; dourado, creme, terracota e azul do jarro como paleta; madeira escura. Letras grossas e arredondadas em creme e dourado, como o título da capa. Nada de line art, nada de vetor chapado, nada de foto.
- Zero Natal: nada de árvore, enfeite de bola, meia de lareira, guirlanda, papai noel, rena, boneco de neve, laço ou presente com cara natalina, nem a combinação vermelho e verde como paleta. Os ramos de oliveira da capa podem aparecer (são oliveira, não guirlanda).
- Sem letras hebraicas geradas (a IA erra o desenho das letras). Só o texto em inglês pedido em cada prompt.
- Texto na imagem: só o que cada prompt pede (headline curta e frases curtas). Nada de parágrafos.
- Nada de QR code desenhado: a IA inventa um QR falso. A frase do bônus entra só como texto.
- Hanukkiah correta: 8 braços e 9 velas no total, a vela do meio (shamash) mais alta, como na capa.
- **Margem de segurança (obrigatória, todos os prompts):** o Flow gera 16:9 e o A+ é 970 x 600 (1,62:1), então o corte central tira ~9% da largura. Todo texto, ícone e a capa ficam dentro dos 88% centrais da largura e dos 84% centrais da altura (mín. 6% livre à esquerda e à direita, 8% em cima e embaixo); só fundo, estrelas e brilho vão até a borda. Cada prompt traz o parágrafo "Safe margins" logo depois do Layout.
- Lado do concorrente (banner 2): capa tosca com título diferente do nosso e linhas de texto diferentes das nossas (nunca repetir nem parafrasear os pontos do livro).
- Ter cuidado para não repetir na imagem o texto que já está na capa (título e subtítulo). A capa aparece como objeto, não como fundo de texto.

## Checklist de anexos (caminhos relativos a `books/hanukkah-8-nights/`)

Todos os anexos já estão exportados em `build/aplus-anexos/` (fora do git). Se o miolo ou a capa mudar, reexportar.

| Banner | Anexar |
|---|---|
| 1 Hero | `build/aplus-anexos/capa-frente.png` |
| 2 Comparison & Value | `build/aplus-anexos/capa-frente.png` |
| 3 Inside Pages Preview | `capa-frente.png` + `build/aplus-anexos/p11.png` (Crack the Code, Noite 1), `p23.png` (Shape Sudoku 4x4, Noite 3) e `p48.png` (receita de latke, Noite 6). Conferidas no PDF de 82 páginas em 2026-10-10. Reserva: p54 (Hanukkah Food Crossword, Noite 6) no lugar da p11. Se o Flow distorcer alguma página, rodar de novo só com p23 e p48, ou montar o banner no Canva com as páginas reais. |
| 4 Use Case (as 8 noites) | `capa-frente.png`. Opcional, só se os ícones saírem fracos: anexar também `inputs/illustrations/11.png`, `21.png`, `30.png`, `41.png`, `51.png`, `61.png`, `71.png`, `82.png` e acrescentar ao prompt "use the attached line drawings only as subject reference, redraw each in the cover's painted style". |
| 5 Key Benefits (como funciona) | `capa-frente.png`. Não anexar `bonus-qr.png` (a frase do bônus é só texto). |

Evitar como referência: `inputs/illustrations/14.png` (versão ainda a confirmar visualmente, ver questions.md) e a página de ligar os pontos da Noite 2 (p16 e p19, ponto fraco já registrado na revisão editorial; não usar no Inside Pages nem citar ligar os pontos nos textos).

---

## Banner 1: Hero

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Hero

Visual style: Match the exact color palette, lettering style, and illustration style of the attached book cover: a rich, warm, painted storybook illustration with a deep midnight-blue starry night sky, glowing gold, soft candlelight, terracotta and blue accents, and dark polished wood. Bold rounded cream-and-gold lettering like the cover title. Clean, welcoming, not photographic, not flat vector, not line art.

Layout: 16:9 landscape banner. The attached book cover is large and prominent on the left third of the frame, slightly angled, with a soft shadow. The right two thirds continue the cover's night scene: a starry navy sky, soft silhouettes of a small hillside town, an eight-branch hanukkiah (nine candle holders in total, with the center one raised) with lit candles, a wooden dreidel, and a few gold coins on a dark wooden table. Keep the right side calm, with a clear dark area at the upper right so the text stays legible.

Safe margins (mandatory): the banner will be center-cropped from 16:9 to a 970 x 600 px module, so keep every piece of text, every icon, and the book cover fully inside the central 88% of the frame width and the central 84% of the frame height. Nothing important may touch, approach, or be cut by the edges: leave at least 6% empty on the left and right, and 8% on the top and bottom. Only the background, stars, and glow may extend to the edges.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "One Book for All Eight Nights of Hanukkah"
Supporting phrases: "More than 80 pages" | "Two levels" | "A game before the candles"

Audience: parents and grandparents shopping for a Hanukkah activity for kids ages 6 to 10. The mood should feel authentic and warm, not cartoonish or generic stock-like.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not draw a second copy of the cover title. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 2: Comparison & Value

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Comparison & Value

Visual style: Match the exact color palette, lettering style, and illustration style of the attached book cover: deep midnight blue, glowing gold, warm cream, soft candlelight, painted storybook feel. Clean and organized, welcoming, not photographic.

Layout: 16:9 landscape banner on a deep navy background with a few small gold stars, split composition. Left half: the attached book cover shown upright, in full color, with four gold check marks beside four short lines of cream text. Right half: a generic, basic, low-effort activity book with a crude, amateur cover: a flat pale-blue background, one clumsy clip-art dreidel and a few mismatched stars scattered randomly, a plain default-font title "Fun Puzzles for Kids" in dull black letters, no polish, no glow, no depth, like a cheap template. The cover has no author name, logo, or brand. Beside it, four different short lines in greyed-out text, each marked with an empty circle. These four lines must not repeat, copy, or paraphrase the left-side lines. Never use a real competitor's branding or cover. Leave clear negative space so the text stays legible.

Safe margins (mandatory): the banner will be center-cropped from 16:9 to a 970 x 600 px module, so keep every piece of text, every icon, and the book cover fully inside the central 88% of the frame width and the central 84% of the frame height. Nothing important may touch, approach, or be cut by the edges: leave at least 6% empty on the left and right, and 8% on the top and bottom. Only the background, stars, and glow may extend to the edges.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "Made for the Whole Table"
Left lines: "Two levels on every night" | "Words explained, no experience needed" | "Every night stands alone" | "Full answer key and a free printable bonus"
Right label: "A typical activity book"
Right lines (greyed out): "One level for all ages" | "Hard words left unexplained" | "Hard to start mid-book" | "Little more than puzzles"
Text on the generic cover (only this): "Fun Puzzles for Kids"

Audience: parents and grandparents comparing activity books for kids ages 6 to 10. The mood should feel honest and friendly, not aggressive.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 3: Inside Pages Preview

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Inside Pages Preview

Visual style: Match the exact color palette, lettering style, and illustration style of the attached book cover: deep midnight-blue starry background, warm gold light, cream lettering, a painted storybook feel. Clean and trustworthy.

Layout: 16:9 landscape banner. Show the three attached interior pages (the secret code page, the shape sudoku page, and the latke recipe page) side by side, slightly overlapping and tilted, as if lying on a warm dark wooden table under soft candle glow, with a yellow pencil beside them and a small gold coin or two. The background behind the table is the same starry navy night as the cover. Use only the attached pages exactly as they are. Do not invent, redraw, or change any content on the pages, and do not add extra pages. Leave clear negative space on one side so the headline stays legible.

Safe margins (mandatory): the banner will be center-cropped from 16:9 to a 970 x 600 px module, so keep every piece of text, every icon, and the book cover fully inside the central 88% of the frame width and the central 84% of the frame height. Nothing important may touch, approach, or be cut by the edges: leave at least 6% empty on the left and right, and 8% on the top and bottom. Only the background, stars, and glow may extend to the edges.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "Real Pages, Ready for Pencils"
Supporting phrases: "Shape sudoku" | "A secret code to crack" | "A latke recipe to make with a grown-up"

Audience: parents and grandparents who want to see what the kids will actually be doing. The mood should feel trustworthy and practical.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 4: Use Case & Versatility (as 8 noites)

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Use Case & Versatility (one vignette per night)

Visual style: Match the exact color palette, lettering style, and illustration style of the attached book cover: deep midnight blue, glowing gold, cream, terracotta and soft blue accents, painted storybook feel with a warm glow. Welcoming, clean, not photographic.

Layout: 16:9 landscape banner on a starry navy background. A tidy grid of eight small rounded square tiles in two rows of four, each tile with a thin gold border and a bold gold numeral from 1 to 8 in the corner. Each tile holds one simple, readable painted icon for that night's theme, in this order: 1 a young man standing firm on a mountain path; 2 a messy old temple room with a fallen broom; 3 a single small terracotta oil jar; 4 a hanukkiah in a window; 5 a spinning wooden dreidel; 6 a pan of golden latkes; 7 a coin dropping into a tzedakah box; 8 a hanukkiah with every candle lit. Keep each icon simple and readable at small size. Leave clear negative space at the top for the headline.

Safe margins (mandatory): the banner will be center-cropped from 16:9 to a 970 x 600 px module, so keep every piece of text, every icon, and the book cover fully inside the central 88% of the frame width and the central 84% of the frame height. Nothing important may touch, approach, or be cut by the edges: leave at least 6% empty on the left and right, and 8% on the top and bottom. Only the background, stars, and glow may extend to the edges.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "Eight Nights, Eight Themes"
Supporting phrase: "New puzzles every night"
The numerals 1 to 8, one per tile, and no other text.

Audience: parents and grandparents who want to see how the book is organized, and that they can start on any night.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 5: Key Benefits & Features (como funciona)

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Key Benefits & Features

Visual style: Match the exact color palette, lettering style, and illustration style of the attached book cover: deep midnight-blue starry background, glowing gold, warm cream lettering, soft candlelight, painted storybook feel. Calm and friendly, not photographic.

Layout: 16:9 landscape banner. Three icon-style callouts in a row, each in a round gold-rimmed medallion with one short phrase underneath: (1) an open book, (2) one star and two stars side by side, (3) a lit candle next to a small clock. Below the three callouts, a slim, plain banner strip for one line of text. Do not draw a QR code, a barcode, or any code pattern anywhere. Leave clear negative space so the text stays legible.

Safe margins (mandatory): the banner will be center-cropped from 16:9 to a 970 x 600 px module, so keep every piece of text, every icon, and the book cover fully inside the central 88% of the frame width and the central 84% of the frame height. Nothing important may touch, approach, or be cut by the edges: leave at least 6% empty on the left and right, and 8% on the top and bottom. Only the background, stars, and glow may extend to the edges.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "How Each Night Works"
Supporting phrases: "Read tonight's short story" | "Pick your level, one star or two" | "Play before you light the candles"
Bottom strip: "Scan the code near the end of the book for a free printable bonus"

Audience: parents and grandparents who want an easy evening routine with the kids. The mood should feel calm and friendly.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Antes de subir (conferências)

1. Capa final: resolvido. `build/aplus-anexos/capa-frente.png` já exportada de `inputs/cover-final.pdf`.
2. Páginas p11, p23 e p48 exportadas em `build/aplus-anexos/`. Conferir de novo se o miolo mudar de página (hoje são 82 páginas).
3. Bônus: o banner 5 e o item do banner 2 mencionam o "free printable bonus"; o QR real está no livro (p74) e o formulário e o e-mail foram testados. Se o bônus sair do ar ou mudar, tirar as duas frases.
4. Conferir o hebraico: nenhum banner leva letras hebraicas; se o Flow gerar alguma, descartar a variação. Conferir também que nenhum banner trouxe QR falso, nem uma hanukkiah com número errado de velas.
5. Depois do Flow, recortar cada escolhida para 970 x 600 px no Canva.
