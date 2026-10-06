= Night 3 — One Little Jar of Oil

#story[
  After the Maccabees cleaned the Temple, they wanted to light the menorah again. That meant finding pure olive oil, oil sealed by the High Priest so no one could doubt it. Judah's men searched everywhere among the wreckage. They found only one small jar with its seal still whole, and it held barely enough oil for a single day.

  Making more oil the proper way would take eight days from start to finish. Should they wait in the dark for it? Or light what little they had and hope?

  They chose to light it. The story says the flame from that one small jar didn't go out after a single day. It kept burning, night after night, until new oil was finally ready on the eighth day.

  That's why Hanukkah lasts eight nights: one jar, one day of oil, and eight days of light.
]

#art("30.png", w: 6.5in, below: 0.04in)

#whats-a("miracle")[A miracle is a wonder nobody saw coming. The Talmud, a great book of Jewish teaching, tells of one small jar of oil that burned for eight days. Jewish families have retold that story for centuries.]

#pagebreak()

#activity(1, "Symbol Sudoku (4x4)")[Fill the grid so every row, column, and small box has all four symbols: jar, candle, dreidel, and star.]

#symbol-key(("noite3_sym_jar.png", "Jar"), ("noite3_sym_candle.png", "Candle"), ("noite3_sym_dreidel.png", "Dreidel"), ("noite3_sym_star.png", "Star"))

#puzzle("noite3_sudoku4x4_recorte.png", w: 6.3in)

#pagebreak()

#activity(1, "Which Jar Is Different?")[These eight oil jars look the same. Look closely. Circle the one jar that is different.]

#v(1fr)
#block(width: 100%, stroke: 1.4pt + ink, radius: 8pt, inset: 8pt,
  align(center, image(_pz + "noite3_jarro_diferente_recorte.png", width: 100%)))
#v(1.4fr)

#pagebreak()

#activity(1, "Follow the Oil")[Help the oil find its way! Start at the jar and trace the one path through the maze to the menorah.]

#v(0.1in)
#align(center, maze-ends("extra_n3_labirinto_oleo", w: 5.2in, side: 1.0in))

#pagebreak()

#activity(2, "Symbol Sudoku (6x6)")[Fill the grid so every row, column, and box has all six symbols, each one only once.]

#symbol-key(("noite3_sym_jar.png", "Jar"), ("noite3_sym_candle.png", "Candle"), ("noite3_sym_dreidel.png", "Dreidel"), ("noite3_sym_star.png", "Star"), ("noite3_sym_hanukkiah.png", "Hanukkiah"), ("noite3_sym_coin.png", "Gelt coin"))

#puzzle("noite3_sudoku6x6_recorte.png", w: 6.4in)

#pagebreak()

#activity(2, "Which Jar Is the Pure One?")[Pretend you're one of Judah's searchers. Use the three clues to find the pure jar.]

#art("31.png", w: 6.4in, below: 0.1in)

#block(width: 100%, above: 0.1in, below: 0.1in, breakable: false, {
  set par(leading: 0.6em, spacing: 0.6em)
  text(font: display, weight: "bold", size: 12pt, tracking: 0.06em)[JAR A, JAR B, JAR C, JAR D.]
  v(0.04in)
  set text(size: 14pt)
  enum(tight: false, spacing: 0.12in,
    [The pure jar's seal is not broken.],
    [The pure jar was found standing up, not knocked over.],
    [The pure jar has the High Priest's own stamp pressed into the seal.])
})

#let _hd(t) = text(font: display, size: 12pt, weight: "bold", tracking: 0.04em, upper(t))
#block(width: 100%, breakable: false,
  table(columns: (0.7fr, 0.9fr, 1.3fr, 1.5fr, 0.8fr, 0.8fr, 0.8fr), stroke: 1.2pt + ink,
    inset: (x: 7pt, y: 12pt), align: center + horizon, fill: (_, y) => if y == 0 { tint } else { none },
    _hd[], _hd[Seal], _hd[Found], _hd[Stamp], _hd[Clue 1], _hd[Clue 2], _hd[Clue 3],
    text(weight: "bold", size: 13.5pt)[Jar A], [broken], [standing up], [none], [], [], [],
    text(weight: "bold", size: 13.5pt)[Jar B], [intact], [knocked over], [none], [], [], [],
    text(weight: "bold", size: 13.5pt)[Jar C], [intact], [standing up], [High Priest's stamp], [], [], [],
    text(weight: "bold", size: 13.5pt)[Jar D], [broken], [knocked over], [none], [], [], []))

#v(0.08in)
#text(size: 12.5pt)[Use the table to cross off jars that don't match each clue. Only one jar is left at the end.]
#v(0.08in)
#grid(columns: (1fr, auto), align: horizon, column-gutter: 12pt,
  text(size: 12pt, fill: mid)[Clue 2 is made up just for this puzzle.],
  block(stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt, y: 9pt),
    text(font: display, weight: "bold", size: 13pt, tracking: 0.04em)[THE PURE JAR IS JAR #box(width: 0.6in, stroke: (bottom: 1.4pt + ink), [])]))

#pagebreak()

#activity(2, "Oil Math")[Solve each problem. Remember: one jar holds oil for 1 day, and Hanukkah lasts 8 days.]

#let _om = json(_pz + "extra_n3_oilmath.json").problems
#v(0.05in)
#for p in _om {
  block(width: 100%, breakable: false, above: 0.14in, below: 0.14in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 18pt, y: 20pt), {
    grid(columns: (0.62in, 1fr), column-gutter: 0.12in, align: top,
      box(width: 0.46in, height: 0.46in, radius: 50%, fill: ink, align(center + horizon, text(fill: white, font: display, weight: "bold", size: 16pt, str(p.id)))),
      {
        text(size: 16.5pt, p.text)
        v(0.3in)
        align(right, text(font: display, weight: "bold", size: 14pt, tracking: 0.05em)[ANSWER: #box(width: 1.1in, stroke: (bottom: 1.6pt + ink), []) #text(size: 13pt, weight: "regular", tracking: 0em, fill: mid, p.unit)])
      })
  })
}

#pagebreak()

#before-candles[
  #subhead[Guess How Long It Burns]
  Before you light tonight's candles, everyone guesses how many minutes they'll burn. Write down your guess. Light the candles, then check a clock when the last one goes out. Closest guess gets a tracker mark. Most marks by Night 8 wins bragging rights.
]

#v(1fr)
#art("32.png", below: 0.04in)
#v(0.35in)
#let _field(label) = block(width: 100%, breakable: false, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 16pt, y: 20pt), {
  set text(font: display, weight: "bold", size: 15pt, tracking: 0.04em)
  label
  v(0.3in)
  [#box(width: 1.7in, stroke: (bottom: 1.4pt + ink), []) minutes]
})
#grid(columns: (1fr, 1fr), column-gutter: 0.3in, _field[MY GUESS:], _field[ACTUAL TIME:])
#v(1fr)
