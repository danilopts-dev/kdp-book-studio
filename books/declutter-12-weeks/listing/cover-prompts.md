# Prompts de capa (ChatGPT / Flow) — The 12-Week Decluttering Workbook

Todos pedem a arte **sem nenhum texto** (IA erra letras). Título, subtítulo e autora entram depois, em Typst, nas zonas livres.
Formato: retrato 2:3 (1024×1536). A capa frontal final é 8,5 × 11 in (≈ 0,77), então a composição deixa margem de segurança em cima e embaixo para corte.
Salve a escolhida em `inputs/cover-front.png`.

## 1. Quatro caixas (tipográfica)

Flat graphic book cover background, portrait 2:3, no text, no letters, no numbers anywhere. Warm cream paper background (#F4EEE2) with a very subtle paper grain. Upper 45% of the image is left completely empty (clean cream) for a large title. In the lower half, four rounded rectangular label tags arranged in a neat 2x2 grid, each tag blank (no writing), slightly tilted by 1 to 2 degrees like stickers, each with a soft drop shadow: sage green (#8FA98B), dusty blue (#7C9CB5), mustard yellow (#D9A73A), terracotta (#C26B4F). A single sharpened yellow pencil lies diagonally across the bottom edge. Minimal, calm, modern, high contrast so it reads at thumbnail size. No people, no clutter, no photos, no text.

## 2. Casa em corte, cômodo por cômodo (ilustrada)

Flat vector illustration for a book cover, portrait 2:3, no text, no letters, no numbers anywhere. A two-story house seen in front cutaway view, like a dollhouse, with 12 clearly separated rooms (bathroom, entryway, kitchen, living room, bedroom, closet, kids' room, home office, laundry, garage, basement, attic). Each room is a simple solid-color block with at most two objects. The rooms on the top rows are tidy and light with a small check-mark badge (no text); the rooms at the bottom are still full of boxes and piles. Warm neutral palette (cream, soft beige, warm gray) with one coral accent (#E0694F) and one sage green accent (#8FA98B). The top 35% of the image is a solid dark charcoal band (#2B2B2B) left empty for the title. Clean shapes, no gradients, no tiny details, readable at thumbnail size. No people, no text.

## 3. Antes e depois com selo de 15 minutos (aspiracional)

Photorealistic lifestyle photo for a book cover, portrait 2:3, no text, no letters, no numbers, no logos anywhere. One wooden shelving unit in a bright home, split by a clean diagonal line from top-left to bottom-right. Left side: shelves crowded with mismatched boxes, stacked items and baskets, slightly messy but plain and neutral (no readable labels). Right side: the same shelves almost empty, with a few neatly placed items, a plant and lots of white space, soft natural window light. Warm, calm, neutral palette (white, oak, soft gray). A plain white circular badge with a thin black outline sits on the diagonal at the center, completely blank inside (the number will be added later). Leave the top 25% of the image as a clean, soft, uncluttered wall area for the title. Sharp focus, realistic proportions, no distorted objects, no people, no text.

---

# Versão escolhida: conceito 3 (antes e depois), com ajustes — 2026-10-07

Ajustes pedidos pelo Danilo: (1) a diagonal define os lados: abaixo/à esquerda do badge = bagunçado; acima/à direita = arrumado, mas não vazio; (2) capa completa com textos; (3) lado arrumado com sol, lado bagunçado em sombra sutil.
A lombada (0,2747 in) NÃO vai nos prompts: IA não acerta uma faixa tão fina. Ela entra pelo estúdio (`./st cover`), com título e autora. Salvar as artes em `inputs/cover-front.png` e `inputs/cover-back.png`.
Texto gerado por IA pode vir com letra errada: conferir cada palavra; se errar, regenerar ou pedir que o texto seja aplicado pelo estúdio (arte sem texto).

## FRONT (anexar a imagem de referência da estante; retrato 2:3)

Edit the attached reference image into a finished book front cover, portrait 2:3. Keep the same wooden two-bay shelving unit, the same camera angle, the warm wall, the rug, the plants and the thin white diagonal line running from the top-left toward the bottom-right, crossing the center of the shelf, with a round white badge with a thin black outline at the exact center of the diagonal.

The diagonal divides the picture into two zones. LOWER-LEFT of the diagonal (everything on the left side of the badge, including the lower shelves of the right bay that fall below the line): clearly MESSY. Overflowing baskets with fabric spilling out, mismatched boxes with lids off, crooked piles of unsorted papers and magazines, books toppled and stacked at random angles, tangled cables, a bowl crammed with small items, clothes draped over a shelf edge. Everything plain and neutral, no readable labels. This zone sits in soft, subtle shade, cooler and slightly dimmer.
UPPER-RIGHT of the diagonal (everything on the right side of the badge, including the upper shelves of the left bay that fall above the line): clearly TIDY and NOT empty. Shelves are full but orderly: books lined up by height, a few matching baskets neatly placed, a pencil cup, two ceramic vases, a small bowl, trailing pothos and a small plant, with comfortable breathing space between objects. This zone is bathed in warm, golden natural sunlight coming through a window on the right, with soft light patches on the wall and shelves.
Keep the light difference subtle and natural, so it reads as calm, not dramatic.

Add the following text, crisp, perfectly spelled, in a bold modern geometric sans-serif (Barlow style), dark charcoal (#1F1F1F) on the clean wall area above the shelf, centered, in this order:
Title in three stacked lines, very large and bold: "THE 12-WEEK" / "DECLUTTERING" / "WORKBOOK".
Under the title, a short thick rule, then the subtitle in medium weight: "15 Minutes a Day, One Room a Week".
Inside the round badge at the center of the diagonal, in black bold: "15" very large, with "MIN / A DAY" in small caps under it.
At the bottom, over the rug area, on a semi-transparent white band: "EMILY P. HARPER" in bold letter-spaced caps.
No other text anywhere. No logos. Sharp focus, realistic proportions, no distorted objects, no people. Keep every piece of text and the badge inside the central 84% of the image height (top and bottom 8% stay as plain background for trimming).

## BACK (retrato 2:3, combina com a frente)

Book back cover, portrait 2:3, matching the front: warm cream wall background (#F2ECE2) with soft golden sunlight patches falling from the upper right, subtle paper grain, and a thin oak-colored border line inset from the edges. In the bottom 15% show the edge of a light oak shelf with one small green plant and two neatly lined books, softly out of focus, as a quiet footer. No people, no logos.

Add the following text, crisp, perfectly spelled, in Barlow-style bold sans-serif for headings and a clean, highly legible humanist sans-serif (Atkinson Hyperlegible style) for body, dark charcoal (#1F1F1F), left-aligned inside a safe margin of at least 9% on every side:

Headline (bold, large, 3 lines max): "Set a timer for 15 minutes, pick up a pencil, and start with the bathroom."

Body (regular, medium size): "Each day you decide about the things in one small part of one room. Each week you move on to the next room. Twelve weeks later, you have been through the whole house."

A short rule, then four bullet points with small square checkboxes instead of dots (regular, medium size):
"7-day task lists for each of the 12 weeks, 15 minutes a day"
"A weekly count of what you kept, donated, sold and tossed"
"A Sell Tracker and a Donation Log"
"A monthly reset tracker to keep every room clear"

Closing line (bold, medium size): "No organizing system to learn. No containers to buy."

Leave a clean empty white rectangle of 2 x 1.2 inches (about 22% of the page width) in the bottom-right corner for the barcode, with no text or decoration. No other text anywhere.

---

# Frente do zero (sem imagem de referência) — 2026-10-07

```
Create a finished book front cover, portrait 2:3, photorealistic lifestyle photograph with typography. Scene: a wide light-oak bookshelf with two bays and five shelves, filling most of the frame, in a bright, calm living room with a warm off-white wall, a woven jute rug on a light wood floor, a leafy pothos plant trailing from the top shelf and an olive tree in the right corner. Eye-level, straight-on camera.

A single thin white diagonal line runs from the top-left corner area to the bottom-right corner area, crossing the center of the shelves. At the exact center of the diagonal sits a round white badge with a thin black outline. The diagonal divides the photo into two zones:
- LOWER-LEFT of the diagonal (everything on the left of the badge, including the lower shelves of the right bay that fall below the line): clearly MESSY. Overflowing baskets with fabric spilling out, mismatched boxes with the lids off, crooked piles of unsorted papers and magazines, books toppled and stacked at random angles, tangled cables, a bowl crammed with small items, clothes draped over a shelf edge. All neutral, no readable labels. This zone sits in soft, subtle shade, slightly cooler and dimmer.
- UPPER-RIGHT of the diagonal (everything on the right of the badge, including the upper shelves of the left bay that fall above the line): clearly TIDY but NOT empty. Shelves are full and orderly: books lined up by height, a few matching baskets, a pencil cup, ceramic vases, a wooden bowl, small plants, with comfortable space between objects. This zone is bathed in warm golden natural sunlight from a window on the right, with soft light patches on the wall and shelves.
Keep the light difference subtle and natural, so the cover feels calm, not dramatic. Warm neutral palette: cream, oak, soft gray, sage green.

The top 30% of the image is a clean, soft, uncluttered wall area for the title. Add this text, crisp and perfectly spelled, in a bold modern geometric sans-serif (Barlow style), dark charcoal (#1F1F1F), centered:
Title in three stacked lines, very large: "THE 12-WEEK" / "DECLUTTERING" / "WORKBOOK".
Under the title, a short thick rule, then the subtitle in medium weight: "15 Minutes a Day, One Room a Week".
Inside the round badge, in black bold: "15" very large, with "MIN / A DAY" in small caps under it.
At the bottom, over the rug, on a semi-transparent white band: "EMILY P. HARPER" in bold letter-spaced caps.
No other text anywhere. No logos, no people, no watermarks. Sharp focus, realistic proportions, no distorted objects. Keep all text and the badge inside the central 84% of the image height; the top and bottom 8% stay as plain background for trimming.
```

---

# Ajuste 1 da frente (usar na mesma conversa do ChatGPT) — 2026-10-07

```
Keep this exact image: same composition, same camera angle, same diagonal line and badge, same text (title, subtitle, badge text and author, spelled exactly as is), same typography, same rug, same plants, same lighting (shade on the lower-left, warm sunlight on the upper-right). Change only the contents of the shelves:

1) LOWER-LEFT (messy side): reduce the mess by about 40%. It should read as "a bit disorganized", not a hoarder's pile. Fewer items overall: one basket with a blanket spilling out slightly, one leaning stack of books and papers, one open box, a few loose items on the floor. Remove the pile of clothes, the tangled cables and the bowl crammed with small items. Leave some visible empty shelf space so it looks messy but believable.

2) UPPER-RIGHT (tidy side): make it noticeably cleaner and more minimal, about 40% fewer objects, but not empty. Each shelf holds only two or three items with generous space between them: for example one short row of books, one vase, one small plant, one wooden bowl. Keep the framed picture on the top shelf, remove the pencil cup and the extra plants and vases. Lots of calm negative space, oak shelf boards clearly visible.

Do not change anything else. No new text, no new objects outside the shelves.
```
