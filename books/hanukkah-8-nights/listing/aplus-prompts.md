# Prompts do Google Flow: A+ de "8 Nights of Hanukkah Activity Book"

Gerados a partir do plano de A+ em `listing.md` (copy dos 5 módulos). Flow: modo imagem, 16:9, 4 gerações por prompt, modelo Nano Banana 2. Depois, recortar cada escolhida para 970 x 600 px no Canva antes de subir ao KDP (não subir o 16:9 cru).

## Regras comuns (valem para os 5 prompts)

- Anexar a capa em TODOS os prompts. A capa final ainda não existe como arquivo (tarefa `cover` do pipeline). Gerar a capa antes de rodar o Flow.
- Estilo: line art storybook, traço grosso e uniforme, rostos simples e expressivos, sem sombreado. As artes anexadas do miolo servem de referência de traço; as cores de preenchimento vêm da capa.
- Zero Natal: nada de árvore, enfeite de bola, meia de lareira, guirlanda, papai noel, rena, boneco de neve, laço ou presente com cara natalina, nem a combinação vermelho e verde como paleta.
- Sem letras hebraicas geradas (a IA erra o desenho das letras). Só o texto em inglês pedido em cada prompt.
- Texto na imagem: só o que cada prompt pede (headline curta e frases curtas). Nada de parágrafos.

## Checklist de anexos (caminhos relativos a `books/hanukkah-8-nights/`)

| Banner | Anexar |
|---|---|
| 1 Hero | Capa final + `inputs/illustrations/12.png` (hanukkiah, referência de traço e do objeto central) |
| 2 Comparison & Value | Capa final |
| 3 Inside Pages Preview | Capa final + 2 páginas reais do miolo: p23 (Symbol Sudoku 4x4, Noite 3) e p48 (receita de latke, Noite 6). Exportar de `build/hanukkah-8-nights-interior.pdf` com `./st preview hanukkah-8-nights "19,38"` ou em PNG a ~150 ppi. Reexportar se o miolo mudar. |
| 4 Use Case (as 8 noites) | Capa final + referências de traço, uma por noite: `11.png` (N1), `21.png` (N2), `30.png` (N3), `41.png` (N4), `51.png` (N5), `61.png` (N6), `71.png` (N7), `82.png` (N8). Se o Flow limitar o número de anexos, usar `11.png`, `30.png`, `51.png`, `61.png` e `82.png`. |
| 5 Key Benefits (como funciona) | Capa final + `inputs/illustrations/32.png` (família com o relógio, Noite 3) |

Artes reais disponíveis em `inputs/illustrations/` (para trocas ou reforço de referência): `11.png`, `12.png`, `13.png`, `14.png`, `21.png`, `22.png`, `24.png`, `24_menorah.png`, `30.png`, `31.png`, `32.png`, `33.png`, `41.png`, `42a.png`, `42b.png`, `42c.png`, `42d.png`, `43.png`, `51.png`, `52.png`, `61.png`, `62.png`, `71.png`, `72.png`, `73.png`, `73_box.png`, `73_gelt.png`, `74.png`, `74_book.png`, `74_broom.png`, `74_die.png`, `74_die_fix.png`, `74_heart.png`, `74_plate.png`, `74_sun.png`, `75.png`, `81.png`, `82.png`, `83.png`, `FM1.png`.
Evitar como referência: `14.png` (versão ainda a confirmar visualmente, ver questions.md) e a página de ligar os pontos da Noite 2 (p14 e p16, ponto fraco já registrado na revisão editorial; não usar no Inside Pages).

---

## Banner 1: Hero

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Hero

Visual style: Match the exact color palette, typography, and illustration style of the attached book cover. Keep the design clean and consistent with the cover's mood: warm and welcoming, with a light storybook feel. Draw the background elements in thick, uniform-weight line art like the attached hanukkiah illustration, with simple flat color fills taken from the cover. No shading, no gradients, no photorealism.

Layout: 16:9 landscape banner. The book cover is large and prominent on the left third of the frame, slightly angled. On the right, a themed background with an eight-branch hanukkiah (nine candle holders in total, with the center one raised) with lit candles, a dreidel, and a few gold coins, all in line art. Leave clear negative space on the right so the text stays legible.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "One Book for All Eight Nights of Hanukkah"
Supporting phrases: "A short story" | "Two levels" | "A game before the candles"

Audience: parents and grandparents shopping for a Hanukkah activity for kids ages 6 to 10. The mood should feel authentic and warm, not cartoonish or generic stock-like.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 2: Comparison & Value

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Comparison & Value

Visual style: Match the exact color palette, typography, and illustration style of the attached book cover. Keep the design clean and consistent with the cover's mood: warm and welcoming, with a light storybook feel. Thick, uniform line art with flat color fills, no shading.

Layout: 16:9 landscape banner, split composition. Left half: the attached book cover shown upright, in full color, with four check marks (drawn in the cover's accent color) beside four short lines. Right half: a generic, unbranded, plain gray activity book with no cover art and its four lines greyed out and marked with empty circles. Never use a real competitor's branding or cover. Leave clear negative space so the text stays legible.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "Made for the Whole Table"
Left lines: "Two levels on every night" | "Words explained, no experience needed" | "Every night stands alone" | "Answer key included"
Right label: "A typical activity book"

Audience: parents and grandparents comparing activity books for kids ages 6 to 10. The mood should feel honest and friendly, not aggressive.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 3: Inside Pages Preview

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Inside Pages Preview

Visual style: Match the exact color palette, typography, and illustration style of the attached book cover. Keep the design clean and consistent with the cover's mood: warm and welcoming, with a light storybook feel.

Layout: 16:9 landscape banner. Show the two attached interior pages (the symbol sudoku page and the latke recipe page) side by side, slightly tilted, as if lying on a light wooden table, with a small pencil beside them. Use only the attached pages exactly as they are. Do not invent, redraw, or change any content on the pages, and do not add extra pages. Leave clear negative space on one side so the headline stays legible.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "Real Pages, Ready for Pencils"
Supporting phrases: "Symbol sudoku" | "A latke recipe to make with a grown-up" | "A dreidel to cut out"

Audience: parents and grandparents who want to see what the kids will actually be doing. The mood should feel trustworthy and practical.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 4: Use Case & Versatility (as 8 noites)

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Use Case & Versatility (one vignette per night)

Visual style: Match the exact color palette, typography, and illustration style of the attached book cover and the attached line-art illustrations: thick, uniform outlines, simple expressive faces, flat color fills from the cover, no shading. Warm and welcoming.

Layout: 16:9 landscape banner. A tidy row of eight small square vignettes in two rows of four, each with a bold numeral from 1 to 8 in the corner. Each vignette is a simple line-art icon for that night's theme, in this order: 1 a young man standing firm on a mountain path; 2 a messy old temple room with a fallen broom; 3 a single small oil jar; 4 a hanukkiah in a window; 5 a spinning dreidel; 6 a pan of latkes; 7 a coin dropping into a tzedakah box; 8 a hanukkiah with every candle lit. Keep each icon simple and readable at small size. Leave clear negative space at the top for the headline.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "Eight Nights, Eight Themes"
The numerals 1 to 8, one per vignette, and no other text.

Audience: parents and grandparents who want to see how the book is organized, and that they can start on any night.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Banner 5: Key Benefits & Features (como funciona)

```
Create a professional Amazon A+ content marketing banner for a children's holiday activity book titled "8 Nights of Hanukkah Activity Book".

Banner purpose: Key Benefits & Features

Visual style: Match the exact color palette, typography, and illustration style of the attached book cover and the attached family illustration: thick, uniform outlines, simple expressive faces, flat color fills from the cover, no shading. Warm and welcoming.

Layout: 16:9 landscape banner. Three icon-style callouts in a row, each paired with one short phrase underneath: (1) an open book, (2) one star and two stars side by side, (3) a lit candle next to a small clock. Leave clear negative space so the text stays legible.

Text to render exactly as written (do not paraphrase, do not add any other text):
Headline: "How Each Night Works"
Supporting phrases: "Read tonight's short story" | "Pick your level, one star or two" | "Play before you light the candles"

Audience: parents and grandparents who want an easy evening routine with the kids. The mood should feel calm and friendly.

Do not add any logos, watermarks, Hebrew letters, or extra text beyond what is specified above. Do not include evergreen trees, baubles, stockings, wreaths, snowmen, reindeer, or a red-and-green color scheme.
```

## Antes de gerar (pendências)

1. Capa final em arquivo (anexo obrigatório de todos os prompts).
2. Exportar as páginas p23 e p48 do miolo para o banner 3 (e conferir de novo se o miolo mudar de página).
3. Bônus: o módulo 5 não menciona o Family Pack. Só acrescentar "free printable bonus" quando o QR real e o PDF do bônus existirem.
4. Conferir o hebraico: nenhum banner leva letras hebraicas; se o Flow gerar alguma, descartar a variação.
