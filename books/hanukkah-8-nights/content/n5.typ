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

#activity(1, "Match the Letter to Its Meaning")[A dreidel has four Hebrew letters, one on each side. Draw a line from each letter to what it stands for.]

#let _dot = circle(radius: 0.1in, fill: ink, stroke: 1.4pt + ink)
#let _mbox(t) = block(width: 100%, height: 1.0in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt),
  align(center + horizon, text(font: display, weight: "bold", size: 24pt, tracking: 0.03em, t)))
#let _mrow(l, r) = (_mbox(l), align(center + horizon, _dot), [], align(center + horizon, _dot), _mbox(r))

#v(0.2in)
#grid(columns: (2.2in, 0.4in, 1fr, 0.4in, 2.2in), row-gutter: 0.34in,
  .._mrow[Nun][Everything],
  .._mrow[Gimel][Put one in],
  .._mrow[Hei][Nothing],
  .._mrow[Shin][Half])

#v(0.45in)
#block(width: 100%, fill: tint, radius: 12pt, inset: (x: 20pt, y: 16pt), breakable: false, {
  text(font: display, weight: "bold", size: 12.5pt, tracking: 0.06em, upper[What do the letters spell?])
  v(0.04in)
  text(size: 14pt)[Put the four letters together (Nun, Gimel, Hei, Shin) and they stand for a whole sentence: *Nes Gadol Haya Sham,* "A great miracle happened there." In Israel, dreidels swap the Shin for a *Pei,* so the sentence becomes *Nes Gadol Haya Po,* "A great miracle happened here," because that's where it happened. Same story, two dreidels.]
})

#pagebreak()

#activity(1, "Color the Dreidel")[Here's a big dreidel, just the outline. Color in each side and the whole spinning top however you like.]

#v(0.1in)
#draw-box(7.55in, body: image(_ill + "52.png", width: 7.0in, height: 7.2in, fit: "contain"))

#pagebreak()

#activity(2, "Design a Dreidel")[Cut along the solid lines, fold along the dashed lines, and glue the gray tabs. Color each face before you fold, it's much easier that way. When it's dry, give it a spin!]

#v(1fr)
#align(center, image(_pz + "noite5_template_dreidel_branco.png", height: 7.8in, fit: "contain"))
#v(1fr)

// Verso em branco de propósito (a criança recorta o template): sem número de página.
#pagebreak()
#page(footer: none)[]

#pagebreak(weak: true)

#activity(2, "Gelt Math")[Solve these gelt problems. Some take two steps, so read carefully before you add.]

#let _prob(n, body, op) = block(width: 100%, breakable: false, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 18pt, y: 12pt),
  grid(columns: (auto, 1fr), column-gutter: 16pt, align: top,
    box(width: 0.42in, height: 0.42in, radius: 50%, fill: ink,
      align(center + horizon, text(fill: white, font: display, weight: "bold", size: 17pt, str(n)))),
    {
      text(size: 15.5pt, body)
      v(0.12in)
      text(size: 20pt)[#op \= #box(width: 1.3in, stroke: (bottom: 1.6pt + ink), [])]
    }))

#v(0.05in)
#stack(dir: ttb, spacing: 0.14in,
  _prob(1, [You win 12 gelt coins in the first round and 9 more in the second round. How many gelt coins do you have now?], [12 + 9]),
  _prob(2, [You have 24 gelt coins to share equally with 3 cousins (you get a share too). How many coins does each person get?], [24 / 4]),
  _prob(3, [You start the game with 18 gelt coins. You spin a Gimel and win 14 more coins from the pot. Then you spin a Hei and have to put half of your coins back in the pot. How many coins do you have left?], [(18 + 14) / 2]),
  _prob(4, [Four cousins count their gelt after the tournament: 15, 22, 18, and 27 coins. How many gelt coins did the whole family win tonight?], [15 + 22 + 18 + 27]))

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
