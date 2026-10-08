= Night 4 — Light It Right

#story[
  Hanukkah has a rule that's easy to love: the hanukkiah goes where people outside can see it. In a window facing the street, or right by the front door.

  There's a reason for that. The whole point of the miracle is to share it, not keep it tucked away. Long ago, families lit their candles where neighbors walking by could catch the glow and know something good was happening inside. It was a quiet way of saying, "Look, the light won."

  Some families still place their hanukkiah in a window every night. Others light it near the door instead, depending on where they live and what feels safest. Either way, the idea stays the same: light isn't meant to hide.

  So tonight, before you light anything, pick a spot where the candles can be seen. That's not just decoration. That's the whole tradition, glowing in one small window.
]

#art("41.png", w: 6.6in, below: 0.02in)

#whats-a("shamash")[The shamash is the "helper" candle. It lights all the others, one by one, but it doesn't count as one of the eight. Most hanukkiahs set it higher or off to the side, so it's easy to spot.]

#pagebreak()

#activity(1, "Number the Steps: Lighting the Hanukkiah")[These steps are out of order. Write 1, 2, 3, and 4 next to each one, in the order you'd really do them.]

#let _step(img, label) = block(width: 100%, breakable: false, {
  align(center, block(width: 2.95in, stroke: 1.4pt + ink, radius: 8pt, clip: true,
    image(_ill + img, width: 100%)))
  v(0.08in)
  grid(columns: (auto, 1fr), column-gutter: 12pt, align: horizon,
    circle(radius: 0.27in, stroke: 1.6pt + ink),
    text(size: 14pt, label))
})

#v(0.05in)
#grid(columns: (1fr, 1fr), column-gutter: 0.3in, row-gutter: 0.22in,
  _step("42b_v2.png", [Say the blessings together.]),
  _step("42d_v2.png", [Put the shamash back in its own holder.]),
  _step("42a_v2.png", [Place tonight's candles in the hanukkiah.]),
  _step("42c_v2.png", [Use the lit shamash to light tonight's candles.]))

#pagebreak()

#activity(1, "How Many Candles Tonight?")[It's the 6th night. Look at the hanukkiah, then fill in the blanks.]

#let _ln(w: 0.7in) = box(width: w, stroke: (bottom: 1.6pt + ink), [])
#let _q(i, body) = block(width: 100%, breakable: false, above: 0.17in, below: 0.17in,
  grid(columns: (0.5in, 1fr), column-gutter: 0.1in, align: horizon,
    box(width: 0.4in, height: 0.4in, radius: 50%, fill: ink, align(center + horizon, text(fill: white, font: display, weight: "bold", size: 14pt, str(i)))),
    text(size: 16.5pt, body)))

#align(center, image(_ill + "hk_n6.png", width: 5.6in))
#v(0.1in)
#_q(1)[Count the Hanukkah candles (not the shamash): #_ln()]
#_q(2)[Now add the shamash: #_ln(w: 0.5in) + 1 = #_ln(w: 0.5in) candles lit tonight]
#_q(3)[8 holders for candles. Empty tonight: 8 − #_ln(w: 0.5in) = #_ln(w: 0.5in)]
#_q(4)[Tomorrow: 1 more candle, plus the shamash. Candles lit: #_ln(w: 0.5in)]

#pagebreak()

#activity(1, "Draw the Candles")[Draw the right number of candles for Night 2, Night 4, and Night 6, starting from the right. Don't forget the shamash!]

#v(0.1in)
#for n in json(_pz + "extra_n4_hanukkiahs.json").draw_the_candles.nights {
  block(width: 100%, breakable: false, above: 0.1in, below: 0.2in, {
    grid(columns: (1fr, auto), align: bottom,
      text(font: display, weight: "bold", size: 20pt, tracking: 0.08em)[NIGHT #n],
      text(size: 14pt)[I drew #box(width: 0.5in, stroke: (bottom: 1.4pt + ink), []) candles.])
    v(0.04in)
    align(center, hanukkiah-draw(n, w: 5.9in, empty: true))
  })
}

#pagebreak()

#activity(2, "How Many Candles in All Eight Nights?")[Every night, you light one more candle than the night before, plus the shamash. Add them up, night by night, to find the grand total for the whole holiday.]

#let _hd(t) = text(font: display, size: 12.5pt, weight: "bold", tracking: 0.04em, upper(t))
#let _num(t) = text(size: 17pt, t)
#block(width: 100%, above: 0.1in, breakable: false,
  table(columns: (0.7fr, 1.4fr, 1fr, 1.2fr), stroke: 1.4pt + ink,
    inset: (x: 8pt, y: 0.27in), align: center + horizon, fill: (_, y) => if y == 0 { tint } else { none },
    _hd[Night], _hd[Hanukkah candles], _hd[\+ Shamash], _hd[Night's total],
    ..range(1, 9).map(n => (text(weight: "bold", size: 17pt, str(n)), _num(str(n)), _num[1], [])).flatten()))

#v(0.18in)
#text(size: 14pt)[Add up the "Night's total" column for all eight nights.]
#v(0.12in)
#block(stroke: 1.6pt + ink, radius: 10pt, inset: (x: 16pt, y: 12pt), breakable: false,
  text(font: display, weight: "bold", size: 17pt, tracking: 0.04em)[GRAND TOTAL: #box(width: 1in, stroke: (bottom: 1.4pt + ink), []) candles])
#v(0.12in)
#text(size: 13pt)[Fun fact: that's why a box of Hanukkah candles usually holds exactly that many!]

#pagebreak()

#activity(2, "Design Your Own Hanukkiah")[Here's a blank hanukkiah, just the shape. Draw in the candles, the shamash, and any pattern or color you want. Make it yours.]

#v(0.1in)
#draw-box(7.55in, body: image(_ill + "43.png", width: 7.1in, height: 7.3in, fit: "contain"))

#pagebreak()

#activity(2, "Which Night Is It?")[Count the Hanukkah candles on each hanukkiah to find the night. The shamash doesn't count! Then answer the four questions below.]

#let _wn = json(_pz + "extra_n4_v3.json").which_night
#v(0.05in)
#grid(columns: (1fr, 1fr), column-gutter: 0.25in, row-gutter: 0.12in,
  ..range(4).map(i => block(width: 100%, breakable: false, {
    align(center, image(_ill + "hk_n" + str(_wn.items.at(i).night) + ".png", width: 3.0in))
    v(0.02in)
    align(center, block(stroke: 1.4pt + ink, radius: 8pt, inset: (x: 12pt, y: 7pt),
      text(font: display, weight: "bold", size: 15pt, tracking: 0.05em)[PICTURE #str(i + 1): NIGHT #box(width: 0.5in, stroke: (bottom: 1.6pt + ink), [])]))
  })))

#let _ln2(w: 0.55in) = box(width: w, stroke: (bottom: 1.6pt + ink), [])
#let _q2(i, body) = block(width: 100%, breakable: false, above: 0.07in, below: 0.07in,
  grid(columns: (0.45in, 1fr), column-gutter: 0.08in, align: horizon,
    box(width: 0.36in, height: 0.36in, radius: 50%, fill: ink, align(center + horizon, text(fill: white, font: display, weight: "bold", size: 13pt, str(i)))),
    text(size: 14.5pt, body)))
#v(0.1in)
#_q2(1)[Hanukkah candles in all four pictures (no shamash): #_ln2()]
#_q2(2)[Add the 4 shamash candles too. How many flames in all? #_ln2()]
#_q2(3)[Which picture has twice as many candles as Night 3? Picture #_ln2(w: 0.4in)]
#_q2(4)[Fullest picture minus emptiest picture: #_ln2() candles]

#pagebreak()

#before-candles[
  #subhead[The Hanukkiah's Joke]
  #v(0.9in)
  #block(width: 100%, fill: tint, radius: 12pt, inset: 36pt, text(size: 26pt)[Which candle on the hanukkiah is the best helper in the whole house?])
  #v(0.8in)
  #block(width: 100%, fill: tint, radius: 12pt, inset: 36pt, text(size: 26pt)[The shamash! It's always ready to lend a hand, or a flame, to every other candle.])
]
