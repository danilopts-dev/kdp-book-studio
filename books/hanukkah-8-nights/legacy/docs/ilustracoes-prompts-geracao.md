# Prompts de geração: ilustrações do livro de Hanucá
## 8 Nights of Hanukkah Activity Book · Jonah Feldman

Este arquivo só serve para gerar as imagens. O histórico, os erros anteriores e as decisões continuam em `lista-ilustracoes-livro-completo.md`. **Não anexe aquele arquivo no chat de geração.**

---

## 1. Como usar

1. Abra um **chat normal** no ChatGPT, fora do Projeto e sem ser no modo Work. O raciocínio em "Alta" já basta.
2. Anexe as imagens de referência: `1.1.png` e `2.1.png`. Quando a 1.4 for aprovada, anexe também, porque é a referência das cenas modernas.
3. Cole a **mensagem de abertura** (seção 2) e espere a resposta "Ready".
4. Cole **um prompt por mensagem**, na ordem da fila (seção 4). Mande o próximo só depois de aprovar a imagem anterior.
5. Se só um detalhe sair errado, **não gere de novo**. Use a correção por edição que está embaixo de cada prompt ("Se errar"), que pede para mudar apenas aquele ponto e manter o resto.
6. Depois de umas 8 a 10 imagens, abra um chat novo, anexe as mesmas referências e cole outra vez a mensagem de abertura. Chat comprido também acumula contexto e o estilo começa a variar.
7. **Proporção:** o gerador costuma entregar só 1:1, 3:2 ou 2:3. Nas faixas panorâmicas o prompt pede para manter tudo o que importa na faixa central, para você recortar no Canva sem cortar nada.

---

## 2. Mensagem de abertura (colar uma vez por chat, junto com as 3 referências)

```
I'm going to ask you for illustrations for a children's Hanukkah activity book (ages 6-10), one image per message.

The three attached images are approved. They set the style for every image in this chat: black-and-white coloring-book line art, bold uniform black outlines, pure white background, no shading, no gray, no solid black areas, no text, no border. Friendly storybook characters with slightly larger heads and simple expressive faces. Ancient characters wear simple tunics, sashes and cloth headbands, and the men have short hair. Modern characters wear casual clothes. Never add Christmas elements.

Don't generate anything now. Just reply "Ready".
```

---

## 3. Status

| Ilustração | Situação |
|---|---|
| 1.1, 1.2, 1.3, 2.1, 2.4, 3.1, 3.3, 4.1 | Arquivo já existe em `ilustracoes/` |
| 1.4 | **Não aprovada.** A hanukiá tem 4 suportes de um lado e 5 do outro. Primeira da fila |
| 2.4 | Existe, mas ainda falta o revisor religioso confirmar 7 braços x 8+1 |
| 5.3 (template do dreidel) | **Não gerar.** Já sai por código (`puzzle-assets/noite5_template_dreidel.png`) |
| 3.2 antiga (ícones do sudoku) | **Não gerar.** Superada, saiu por código |
| Todas as outras | Fila abaixo |

---

## 4. Fila de geração

### 2.2 / 2.3: Templo bagunçado (base do jogo dos erros)
Uso: duplicar no Canva e apagar os objetos 1 a 5 (jogo fácil) ou 1 a 10 (jogo difícil) da cópia de baixo. Recorte final: 7.4 x 3.0 in.
```
Same style as the reference images. Wide landscape.

The inside of the ancient Temple hall in Jerusalem, straight-on view, no people. Plain floor, plain back wall with a few big stone blocks, one intact column at each end, an arched doorway in the center.

Ten messy objects, each drawn once and standing alone with white space around it, not touching anything else: 1 broken clay jar, 2 cobweb in the upper-right corner, 3 wooden table on its side, 4 torn curtain on the back wall, 5 small heap of dust, 6 fallen stone column drum, 7 torn banner hanging crooked, 8 bench with a broken leg, 9 knocked-over candle stand, 10 tipped-over wooden bucket.

Nothing else: no extra rubble or debris, no statues or figures.
```
**Se errar:** "Edit this image: remove [objeto extra]. Keep everything else exactly the same." / "Edit this image: add [objeto que faltou] in the empty space at [posição], not touching anything. Keep everything else the same."

---

### 3.0: Abertura da Noite 3, a jarra encontrada
Recorte final: 7.35 x 2.1 in (panorama).
```
Same style as the reference images. Wide landscape; keep all people and key objects in the middle band so I can crop it into a long banner.

Inside the damaged Temple: broken columns and fallen stone blocks. Judah Maccabee and three companions (four men in total) kneel and stand around a pile of rubble, amazed and hopeful. Judah holds up one small clay oil jar closed with a round wax seal, with a few short lines around it showing a glow. On the right, on a stone block, an unlit seven-branched menorah.

Must: only ONE jar in the whole picture. The menorah has seven branches. No soldiers, no weapons.
```
**Se errar:** "Edit this image: remove every jar except the one in Judah's hands. Keep everything else the same." / "Edit this image: make the menorah on the right have exactly seven branches. Keep everything else the same."

---

### 3.2: Família com a hanukiá e o relógio ("Guess How Long It Burns")
Recorte final: 7.35 x 2.6 in.
```
Same style as the reference images, same kind of modern family as in the living-room reference. Wide landscape; keep everything important in the middle band.

A family of four sitting together at a table near a hanukkiah on the third night of Hanukkah. One child points at a simple round wall clock, the others watch the candles, playful and warm.

Must: on the hanukkiah, three candles on the right end plus the taller middle one are lit; the other holders are empty. Night sky, if visible, stays white.
```
**Se errar:** "Edit this image: the hanukkiah should have only three candles on the far right plus the tall center candle, all lit, and the other holders empty. Keep everything else the same."

---

### 4.2: Sequência dos 4 passos (gerar 4 imagens separadas)
Gerar cada quadro sozinho em 1:1. Os números e a montagem da faixa (7.4 x 1.6 in) ficam no Canva, não na imagem. Ainda depende do revisor religioso.

**4.2a**
```
Same style as the reference images. Square image. Close-up of two hands placing an unlit candle into a hanukkiah. Only hands and the hanukkiah, no faces, plain white background, no numbers.
```
**4.2b**
```
Same style as the reference images. Square image. Close-up of two hands holding an open blank card in front of a hanukkiah with unlit candles. The card is empty, with no letters. No faces, plain white background, no numbers.
```
**4.2c**
```
Same style as the reference images. Square image. Close-up of a hand holding a lit candle and touching its flame to one candle on a hanukkiah. No faces, plain white background, no numbers.
```
**4.2d**
```
Same style as the reference images. Square image. Close-up of a hand putting a lit candle back into the taller center holder of a hanukkiah. No faces, plain white background, no numbers.
```

---

### 4.3: Hanukiá vazia para a criança desenhar
Recorte final: 7.4 x 8.0 in. Melhor editar a `1.2.png` para manter a mesma hanukiá: anexe a 1.2 no chat e cole:
```
Edit the attached hanukkiah: remove all the candles so every holder is empty, and make the hanukkiah larger, centered on a square page with plenty of white space around it. Keep the same shape, style and line weight.
```

---

### 5.1: Crianças da época jogando dreidel
Recorte final: 7.4 x 2.6 in.
```
Same style as the reference images, ancient setting like the historical references. Wide landscape; keep everything important in the middle band.

Four children in simple ancient clothes sit in a circle on the floor of a simple stone room, spinning a dreidel and laughing. A small pile of nuts between them. An open scroll lies nearby, as if they had just been studying. In the background, a smiling adult stands by the doorway, keeping watch.

Must: the dreidel has no letters on it. Light, cheerful mood, no soldiers.
```

---

### 5.2: Dreidel grande para colorir
Recorte final: 4 x 4 in. As letras hebraicas **não** vêm do gerador (ele erra a grafia). Coloque no Canva as mesmas letras usadas no template por código, depois da revisão religiosa.
```
Same style as the reference images. Square image. One large dreidel (four-sided spinning top) centered, turned so two faces are visible, with a short handle on top and a pointed tip at the bottom. The faces are completely blank, with no letters or symbols. Plain white background.
```

---

### 6.1: Cozinha, família fazendo latkes
Recorte final: 7.4 x 2.6 in.
```
Same style as the reference images, modern family like the living-room reference. Wide landscape; keep everything important in the middle band.

A cozy kitchen. One parent and two children cook together: a frying pan with round potato pancakes (latkes), a bowl of grated potato on the counter, and a plate of round jelly doughnuts nearby. Happy and warm.
```

---

### 6.2: Travessa latkes x sufganiyot
Recorte final: 5 x 2.5 in.
```
Same style as the reference images. Landscape image. One oval platter seen from slightly above, divided in two: a stack of potato pancakes on the left, a pile of round jelly doughnuts on the right. Nothing else, plain white background.
```

---

### 7.1: Criança e a caixa de tzedaká
Recorte final: 7.4 x 2.3 in.
```
Same style as the reference images, modern child like the living-room reference. Wide landscape; keep everything important in the middle band.

A smiling child drops a coin into a simple rectangular charity box with a slot on top, holding a few more coins in the other hand. The box has no letters or symbols. Simple home background: a shelf and a plant.
```

---

### 7.2: Mãos de criança e de adulto na mesma caixa
Recorte final: 7.4 x 2.5 in. Use a mesma caixa da 7.1 (anexe a 7.1 se ela ficar diferente).
```
Same style as the reference images. Wide landscape. Close-up of two hands, one small child's hand and one adult hand, each dropping a coin into the same simple rectangular charity box with a slot on top. No faces, no letters on the box, plain white background.
```

---

### 7.3: Ícones do labirinto (início e fim)
O labirinto sai por código; a moldura e o posicionamento ficam no Canva. Aqui só os dois ícones.
```
Same style as the reference images. Landscape image. Two separate small icons with lots of white space between them: on the left, a little pile of round gelt coins; on the right, a simple rectangular charity box with a coin slot on top. No letters, no background.
```

---

### 7.4: Ícones dos vales (coupon book)
Os retângulos pontilhados ficam no layout. Aqui só os seis ícones, que você recorta no Canva. Troque a lista se os vales do piloto forem outros.
```
Same style as the reference images. Landscape image. Six small separate icons in two rows of three, evenly spaced with white space around each: a heart, a broom, an open book, a plate and cup, a smiling sun, a board-game die. Simple and bold, no text, no boxes around them.
```

---

### 7.5: Família no jogo "Who Gets the Coupon?"
Recorte final: 7.4 x 2.0 in.
```
Same style as the reference images, modern family like the living-room reference. Wide landscape; keep everything important in the middle band.

A family of four sits on a sofa. One child holds up three fingers to guess a number, while the others smile and wait for their turn. Playful and warm.
```

---

### 8.1: Hanukiá completa acesa (página inteira)
Recorte final: 7.4 x 9.0 in. Editar a `1.2.png`: anexe e cole:
```
Edit the attached hanukkiah: light all nine candles with simple outlined flames, make it larger and centered on a tall portrait page with generous white space around it. Keep the same shape, style and line weight.
```

---

### 8.2: Família reunida na última noite
Recorte final: 7.4 x 3.0 in.
```
Same style as the reference images, same kind of modern family as the living-room reference. Wide landscape; keep everything important in the middle band.

The eighth night of Hanukkah: grandparents, parents and two children gather close around a hanukkiah on a table by the window, all smiling. Warm, celebratory.

Must: all nine candles on the hanukkiah are lit. Night sky stays white with a few outlined stars.
```
**Se errar:** "Edit this image: make all nine candles on the hanukkiah lit, with simple outlined flames. Keep everything else the same."

---

### 8.3: Moldura do certificado
Recorte final: 7.4 x 9.0 in. Aqui a moldura é o próprio objeto, então o "no border" da abertura não vale.
```
Same style as the reference images. Tall portrait page. This time the subject IS a border: a simple decorative certificate frame around the edges, made of small dreidels, coins and stars. A small hanukkiah centered at the top. The middle of the page stays completely empty for text I'll add later. No text, no laurel wreaths.
```

---

### FM.1: Mini-guia de acendimento
As setas e os números **não** vão para o gerador (é aí que ele mais erra). Gere só a hanukiá da terceira noite editando a `1.2.png` e faça as setas no Canva. Ainda depende da revisão religiosa.
```
Edit the attached hanukkiah: keep candles only in the three holders on the far right and in the taller center holder; remove all the other candles so those holders are empty. All candles unlit. Keep the same shape, style and line weight.
```
