= Night 5 — Spin the Dreidel

#story[
  Long ago, studying the Torah was against the law. Soldiers patrolled the streets, and Jewish children had to study in secret, in small rooms or basements, always ready to hide.

  Legend has it they found a clever trick. They kept a small spinning top nearby, called a dreidel. The moment soldiers came close, they'd shut their books and start spinning the top instead, laughing like it was just a game. "We're only playing," they'd say. The soldiers would walk right past.

  The story says that's how the dreidel became part of Hanukkah: a game born from hiding something precious in plain sight. Nobody can prove every detail happened exactly that way, but families have passed the story down for generations, spinning right along with it.

  Tonight, when you spin your own dreidel, you're playing a game with a story tucked inside it.
]

#v(0.1in)
#art("51.png", w: 7.2in)

#pagebreak()

#activity(1, "Match the Letter to Its Meaning")[A dreidel has four Hebrew letters, one on each side. Draw a line from each letter to what it tells you to do in the game.]

#let _dot = circle(radius: 0.1in, fill: ink, stroke: 1.4pt + ink)
#let _mbox(t) = block(width: 100%, height: 1.0in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt),
  align(center + horizon, text(font: display, weight: "bold", size: 24pt, tracking: 0.03em, t)))
#let _heb = ("Nun": "נ", "Gimel": "ג", "Hei": "ה", "Shin": "ש")
#let _lbox(n) = block(width: 100%, height: 1.0in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt),
  align(center + horizon, stack(dir: ttb, spacing: 7pt,
    text(font: heb-font, size: 38pt, lang: "he", top-edge: "bounds", bottom-edge: "bounds")[#_heb.at(n)],
    text(font: display, weight: "bold", size: 13pt, tracking: 0.04em, n))))
#let _mrow(l, r) = (_lbox(l), align(center + horizon, _dot), [], align(center + horizon, _dot), _mbox(r))
#let _hl(g) = text(font: heb-font, size: 1.3em, lang: "he")[#g]

#v(0.2in)
#grid(columns: (2.2in, 0.4in, 1fr, 0.4in, 2.2in), row-gutter: 0.34in,
  .._mrow("Nun")[Everything],
  .._mrow("Gimel")[Put one in],
  .._mrow("Hei")[Nothing],
  .._mrow("Shin")[Half])

#v(0.45in)
#block(width: 100%, fill: tint, radius: 12pt, inset: (x: 20pt, y: 16pt), breakable: false, {
  text(font: display, weight: "bold", size: 12.5pt, tracking: 0.06em, upper[What do the letters spell?])
  v(0.04in)
  text(size: 14pt)[Put the four letters together (Nun #_hl[נ], Gimel #_hl[ג], Hei #_hl[ה], Shin #_hl[ש]) and they stand for a whole sentence: *Nes Gadol Haya Sham,* "A great miracle happened there." In Israel, dreidels swap the Shin for a *Pei* (#_hl[פ]), so the sentence becomes *Nes Gadol Haya Po,* "A great miracle happened here," because that's where it happened. Same story, two dreidels.]
})

#pagebreak()

#activity(1, "Color the Dreidel")[Here's a big dreidel, just the outline. Color in each side and the whole spinning top however you like.]

#v(0.1in)
#draw-box(7.55in, body: image(_ill + "52.png", width: 7.0in, height: 7.2in, fit: "contain"))

#pagebreak()

// ---- Expansão (2026-10-06): as duas páginas novas entram ANTES de Design a Dreidel (paridade da página de recorte)
#activity(1, "Dreidel Tally Chart")[Spin your dreidel 20 times. After each spin, make one tally mark under the letter it shows. Then see which letter won!]

#let _tl(n) = block(width: 100%, height: 1.55in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 6pt),
  align(center + horizon, stack(dir: ttb, spacing: 9pt,
    text(font: heb-font, size: 56pt, lang: "he", top-edge: "bounds", bottom-edge: "bounds")[#_heb.at(n)],
    text(font: display, weight: "bold", size: 15pt, tracking: 0.04em, n))))
#let _tbox = block(width: 100%, height: 3.3in, stroke: 1.6pt + ink, radius: 10pt, [])

#v(0.08in)
#block(width: 100%, breakable: false, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 14pt, y: 10pt), {
  text(font: display, weight: "bold", size: 12pt, tracking: 0.08em)[SPINS: CROSS OFF ONE CIRCLE EACH TIME]
  v(0.08in)
  for _ in range(2) {
    grid(columns: (1fr,) * 10, row-gutter: 0.1in, align: center,
      ..range(10).map(_ => circle(radius: 0.15in, stroke: 1.4pt + ink)))
    v(0.1in)
  }
})

#v(0.14in)
#grid(columns: (1fr,) * 4, column-gutter: 0.16in, row-gutter: 0.1in,
  .._heb.keys().map(n => _tl(n)),
  .._heb.keys().map(_ => _tbox))

#v(0.16in)
#block(width: 100%, breakable: false, fill: tint, radius: 12pt, inset: (x: 18pt, y: 14pt),
  text(font: display, weight: "bold", size: 19pt, tracking: 0.04em)[WHICH LETTER WON? #h(8pt) #box(width: 2.4in, height: 0.34in, stroke: (bottom: 1.6pt + ink), [])])

#pagebreak()

#activity(2, "What Comes Next? Dreidel Patterns")[Each row follows a pattern. Figure out what comes next, then write or draw it in the empty box.]

#let _pat = json(_pz + "extra_n5_padroes.json").patterns
#let _nm = ("N": "Nun", "G": "Gimel", "H": "Hei", "S": "Shin")
#let _chip(body) = box(width: 0.58in, height: 0.54in, stroke: 1.4pt + ink, radius: 8pt, align(center + horizon, body))
#let _shape(k) = {
  if k == "circle" { circle(radius: 0.2in, fill: ink) }
  else if k == "square" { rect(width: 0.37in, height: 0.37in, fill: ink) }
  else if k == "triangle" { polygon(fill: ink, (0.2in, 0pt), (0.4in, 0.36in), (0pt, 0.36in)) }
  else { polygon(fill: ink, (0.2in, 0pt), (0.4in, 0.2in), (0.2in, 0.4in), (0pt, 0.2in)) }
}
#let _item(x) = {
  if type(x) == int { text(font: display, weight: "bold", size: 20pt, str(x)) }
  else if x in _nm { text(font: display, weight: "bold", size: 12.5pt, _nm.at(x)) }
  else { _shape(x) }
}
#let _blankchip = box(width: 0.58in, height: 0.54in, stroke: (paint: ink, thickness: 1.6pt, dash: "dashed"), radius: 8pt, [])

#v(0.1in)
#for (i, s) in _pat.enumerate() {
  block(width: 100%, breakable: false, above: 0.0in, below: 0.3in, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 12pt, y: 16pt),
    grid(columns: (0.42in, 1fr), column-gutter: 12pt, align: horizon,
      box(width: 0.42in, height: 0.42in, radius: 50%, fill: ink,
        align(center + horizon, text(fill: white, font: display, weight: "bold", size: 17pt, str(i + 1)))),
      stack(dir: ltr, spacing: 4pt, ..s.shown.map(x => _chip(_item(x))), _blankchip)))
}

#pagebreak()

#activity(2, "Design a Dreidel")[Cut along the solid lines, fold along the dashed lines, and glue the gray tabs. Color each face before you fold, it's much easier that way. When it's dry, give it a spin!]

#v(1fr)
#align(center, image(_pz + "noite5_template_dreidel_branco.png", height: 7.8in, fit: "contain"))
#v(1fr)

// Verso em branco de propósito (a criança recorta o template): sem número de página.
#pagebreak()
#page(footer: none)[]

#pagebreak(weak: true)

#activity(2, "Gelt Math")[Solve these gelt problems. Most take two steps, so read carefully.]

#let _prob(n, body) = block(width: 100%, breakable: false, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 18pt, y: 10pt),
  grid(columns: (auto, 1fr), column-gutter: 16pt, align: top,
    box(width: 0.42in, height: 0.42in, radius: 50%, fill: ink,
      align(center + horizon, text(fill: white, font: display, weight: "bold", size: 17pt, str(n)))),
    {
      text(size: 15pt, body)
      v(0.1in)
      align(right, text(font: display, weight: "bold", size: 13pt, tracking: 0.05em)[ANSWER: #box(width: 1.1in, stroke: (bottom: 1.6pt + ink), []) #text(weight: "regular", tracking: 0em)[coins]])
    }))

#v(0.05in)
#stack(dir: ttb, spacing: 0.1in,
  _prob(1, [You win 3 rounds of the dreidel game. Each round, you win 14 gelt coins. How many gelt coins did you win in all?]),
  _prob(2, [You have 72 gelt coins to share equally with your 5 cousins (you get a share too). How many coins does each person get?]),
  _prob(3, [You start the game with 48 gelt coins. You spin a Gimel and win 36 more coins from the pot. Then you give one fourth of all your coins to your little cousin. How many coins do you have left?]),
  _prob(4, [Four cousins count their gelt after the tournament: 38, 47, 29, and 56 coins. They put every coin in the middle and give half of the pile to tzedakah. How many coins go to tzedakah?]))

#v(0.14in)
#whats-a("gelt", a: false)[Gelt means "money" in Yiddish. Today it's usually chocolate coins wrapped in gold foil, given out during Hanukkah. Families use it for games (like the dreidel tournament tonight), for prizes, and sometimes just for a sweet treat after lighting the candles.]

#pagebreak()

#before-candles[
  #subhead[Family Dreidel Tournament]
  #text(size: 16pt)[
    Families play dreidel in lots of different ways. Here's one easy version. Everyone starts with 10 to 15 gelt coins (or nuts, buttons, anything small works) and puts 1 coin in the middle pot to start. Take turns spinning. Here's what each letter means:

    - *Nun:* do nothing. Pass the dreidel to the next player.
    - *Gimel:* take the whole pot! Everyone puts 1 coin back in to start the next round.
    - *Hei:* take half the pot.
    - *Shin:* put 1 coin into the pot.

    If the pot ever runs out, everyone puts 1 coin back in. Keep spinning until someone wins all the gelt, or until it's time to light the candles, whichever comes first.
  ]
  #v(0.45in)
  #subhead[Scoreboard]
  #text(size: 15pt)[Fill in one circle for every round you win.]
  #v(0.25in)
  #scoreboard([Player: #box(width: 1.1in, stroke: (bottom: 1.4pt + ink), [])], [Player: #box(width: 1.1in, stroke: (bottom: 1.4pt + ink), [])], [Player: #box(width: 1.1in, stroke: (bottom: 1.4pt + ink), [])], label-w: 2.1in)
]
