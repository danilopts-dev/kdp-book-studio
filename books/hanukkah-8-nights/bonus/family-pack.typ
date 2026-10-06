// 8 Nights Family Pack: PDF gratuito do bônus (Letter, 3 páginas, para imprimir em casa).
// Textos: legacy/manuscript/bonus-cartao-bencaos.md (cartão, hebraico com nikud) e noite-5-texto.md (regras do dreidel).
// Compilar: python bonus/build.py  ->  build/hanukkah-8-nights-family-pack.pdf

#let ink = luma(15)
#let mid = luma(90)
#let soft = luma(200)
#let tint = luma(244)
#let display = ("Barlow", "Bahnschrift", "Verdana")
#let body-font = ("Atkinson Hyperlegible", "Verdana")
#let heb-font = ("Times New Roman", "Arial")
#let ill = "/books/hanukkah-8-nights/inputs/illustrations/"

#set document(title: "8 Nights Family Pack", author: "Jonah Feldman")
#set text(font: body-font, size: 12.5pt, fill: ink, lang: "en")
#set par(leading: 0.7em, spacing: 1em, justify: false)
#set page(
  width: 8.5in, height: 11in,
  margin: (x: 0.8in, top: 0.6in, bottom: 0.85in),
  footer: align(center, text(font: display, size: 8.5pt, tracking: 0.14em, fill: mid)[8 NIGHTS FAMILY PACK #h(6pt) · #h(6pt) JONAH FELDMAN #h(6pt) · #h(6pt) READ PUBLISHING CO]),
)

#let kicker(t) = text(font: display, size: 9.5pt, tracking: 0.16em, weight: "bold", fill: mid, upper(t))
#let page-title(t) = text(font: display, size: 30pt, weight: "bold", upper(t))

// ------------------------------------------------------------------ página 1: cartão de bênçãos
#let blessing(num, label, when, heb, tr, en) = block(width: 100%, breakable: false, above: 0.15in, below: 0pt, {
  text(font: display, weight: "bold", size: 12.5pt, tracking: 0.05em)[#num. #upper(label)]
  h(8pt)
  text(style: "italic", fill: mid, size: 11.5pt)[(#when)]
  v(5pt)
  block(width: 100%, {
    set text(dir: rtl, lang: "he", font: heb-font, size: 17.5pt)
    set par(leading: 0.8em)
    heb
  })
  v(5pt)
  text(style: "italic", size: 11.5pt, tr)
  v(3pt)
  text(size: 11.5pt, fill: mid, en)
})

#align(center)[
  #kicker[Free printable bonus]
  #v(0.05in)
  #page-title[Hanukkah Blessings]
  #v(0.04in)
  #image(ill + "33_clean.png", width: 1.05in)
]
#v(0.04in)
#align(center, block(width: 5.6in, text(size: 13pt)[Say the first two blessings every night, before you light the candles. On the first night you light, add the third one.]))

#line(length: 100%, stroke: 1.2pt + ink)

#blessing(1, "For lighting the Hanukkah candles", "every night",
  [בָּרוּךְ אַתָּה יְיָ אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, אֲשֶׁר קִדְּשָׁנוּ בְּמִצְוֹתָיו, וְצִוָּנוּ לְהַדְלִיק נֵר שֶׁל חֲנֻכָּה.],
  [Baruch atah Adonai, Eloheinu melech ha'olam, asher kid'shanu b'mitzvotav v'tzivanu l'hadlik ner shel Hanukkah.],
  [Blessed are You, our God, Ruler of the universe, who made us holy with commandments and commanded us to light the Hanukkah candles.])

#blessing(2, "For the miracles", "every night",
  [בָּרוּךְ אַתָּה יְיָ אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, שֶׁעָשָׂה נִסִּים לַאֲבוֹתֵינוּ בַּיָּמִים הָהֵם בַּזְּמַן הַזֶּה.],
  [Baruch atah Adonai, Eloheinu melech ha'olam, she'asah nisim la'avoteinu bayamim hahem baz'man hazeh.],
  [Blessed are You, our God, Ruler of the universe, who worked miracles for our ancestors in those days, at this season.])

#blessing(3, "Shehecheyanu", "the first night you light",
  [בָּרוּךְ אַתָּה יְיָ אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, שֶׁהֶחֱיָנוּ וְקִיְּמָנוּ וְהִגִּיעָנוּ לַזְּמַן הַזֶּה.],
  [Baruch atah Adonai, Eloheinu melech ha'olam, shehecheyanu v'kiy'manu v'higianu laz'man hazeh.],
  [Blessed are You, our God, Ruler of the universe, who has kept us alive, sustained us, and brought us to this season.])

#v(0.14in)
#line(length: 100%, stroke: 1.2pt + ink)
#v(0.04in)
#align(center)[
  #text(style: "italic", size: 12pt)[Light the candles from left to right, newest candle first. Happy Hanukkah!] \
  #text(style: "italic", size: 10.5pt, fill: mid)[This card contains Hebrew blessings with God's name. Please keep it in a respectful place.]
]

// ------------------------------------------------------------------ página 2: regras do dreidel + placar
#pagebreak()

#grid(columns: (1fr, 1.35in), column-gutter: 0.2in, align: horizon,
  [#kicker[Family game] #v(0.04in) #page-title[Family Dreidel Tournament]],
  align(right, image(ill + "52.png", width: 1.3in)))

#v(0.1in)
Families play dreidel in lots of different ways. Here's one easy version. Everyone starts with 10 to 15 gelt coins (or nuts, buttons, anything small works) and puts 1 coin in the middle pot to start. Take turns spinning. Here's what each letter means:

#block(width: 100%, fill: tint, radius: 8pt, inset: (x: 14pt, y: 10pt), {
  set par(spacing: 0.6em)
  [*Nun:* do nothing. Pass the dreidel to the next player.]
  parbreak()
  [*Gimel:* take the whole pot! Everyone puts 1 coin back in to start the next round.]
  parbreak()
  [*Hei:* take half the pot.]
  parbreak()
  [*Shin:* put 1 coin into the pot.]
})

If the pot ever runs out, everyone puts 1 coin back in. Keep spinning until someone wins all the gelt, or until it's time to light the candles, whichever comes first.

#v(0.08in)
#kicker[Scoreboard]
#v(0.04in)
Mark one tally line for every round you win.
#v(0.06in)

#let name-cell = table.cell(align: bottom + left, text(size: 10pt, fill: mid)[Name:])
#table(
  columns: (1.15in, 1fr, 1fr, 1fr, 1fr),
  rows: (0.42in,) + (0.5in,) * 8,
  stroke: 1.1pt + ink,
  inset: 6pt,
  align: horizon + center,
  table.cell(fill: ink)[#text(fill: white, font: display, weight: "bold", size: 11pt, tracking: 0.08em)[NIGHT]],
  name-cell, name-cell, name-cell, name-cell,
  ..range(1, 9).map(n => (
    table.cell(fill: tint)[#text(font: display, weight: "bold", size: 14pt)[Night #n]],
    [], [], [], [],
  )).flatten(),
)

// ------------------------------------------------------------------ página 3: etiquetas de presente
#pagebreak()

#let flame(fw: 0.11in, fh: 0.17in) = polygon(fill: white, stroke: 1.1pt + ink,
  (0.5 * fw, 0pt), (0.78 * fw, 0.42 * fh), (fw, 0.7 * fh), (0.78 * fw, 0.95 * fh), (0.5 * fw, fh),
  (0.22 * fw, 0.95 * fh), (0pt, 0.7 * fh), (0.22 * fw, 0.42 * fh))

#let hanukkiah(n, w: 2.3in) = {
  // 9 posições (0 a 8); a central (4) é o shamash. Noite n: n velas, começando pela direita.
  let order = (8, 7, 6, 5, 3, 2, 1, 0)
  let lit = order.slice(0, n)
  let step = w / 9
  let cw = 0.1in
  let ch = 0.3in
  let base = 0.64in
  box(width: w, height: 0.82in, {
    // barra de base
    place(left + top, dy: base, dx: 0.04 * w, rect(width: 0.92 * w, height: 0.045in, fill: ink, radius: 2pt))
    place(left + top, dy: base + 0.045in, dx: w / 2 - 0.2in, rect(width: 0.4in, height: 0.05in, fill: ink, radius: 2pt))
    for i in range(9) {
      let x = step * i + step / 2 - cw / 2
      if i == 4 {
        place(left + top, dx: x, dy: base - 0.42in, rect(width: cw, height: 0.42in, fill: white, stroke: 1.3pt + ink))
        place(left + top, dx: x - 0.005in, dy: base - 0.42in - 0.19in, flame())
      } else if i in lit {
        place(left + top, dx: x, dy: base - ch, rect(width: cw, height: ch, fill: white, stroke: 1.2pt + ink))
        place(left + top, dx: x - 0.005in, dy: base - ch - 0.18in, flame())
      } else {
        place(left + top, dx: x, dy: base - 0.06in, rect(width: cw, height: 0.06in, fill: white, stroke: 1.2pt + ink))
      }
    }
  })
}

#let tag(n) = block(width: 3.4in, height: 2.0in, radius: 12pt, stroke: (paint: ink, thickness: 1.3pt, dash: "dashed"), inset: 0.1in, {
  place(left + top, dx: 0.02in, dy: 0.02in, circle(radius: 0.06in, stroke: 1pt + mid))
  align(center, {
    v(0.02in)
    text(font: display, weight: "bold", size: 21pt, tracking: 0.05em)[NIGHT #n]
    v(0.06in)
    hanukkiah(n)
    v(0.06in)
    grid(columns: (auto, 1fr, auto, 1fr), column-gutter: 5pt, align: bottom,
      text(size: 10.5pt, fill: mid)[To:], line(length: 100%, stroke: 0.8pt + ink),
      text(size: 10.5pt, fill: mid)[From:], line(length: 100%, stroke: 0.8pt + ink))
  })
})

#align(center)[
  #kicker[Cut along the dashed lines]
  #v(0.03in)
  #text(font: display, size: 22pt, weight: "bold")[GIFT TAGS, NIGHT 1 TO NIGHT 8]
]
#v(0.12in)
#block(breakable: false, grid(columns: (3.4in, 3.4in), column-gutter: 0.1in, row-gutter: 0.1in, ..range(1, 9).map(tag)))
