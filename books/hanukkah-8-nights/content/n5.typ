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
#activity(1, "Dreidel Tally Chart")[Spin your dreidel 20 times. After each spin, make one tally mark under the letter it shows (if your dreidel has Pei, mark Shin). Then see which letter won!]

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

#activity(2, "Design a Dreidel")[Color the faces, cut along the solid lines, fold along the dashed lines, and glue the gray tabs. Then push a straw or a toothpick through the X and out the point, and give it a spin!]

// Molde em vetor (v2, 09/10/2026, conforme o desenho de correção do Danilo): 4 faces com a letra em pé, 4 triângulos
// que formam a ponta, cada um com uma aba cinza no lado direito para colar no triângulo vizinho; tampa quadrada presa à
// 2a face, 3 abas de cima (faces 1, 3 e 4) e 1 aba lateral. Linhas contínuas = cortar; tracejadas = dobrar (inclusive a
// base de TODAS as abas). O contorno acompanha o chanfro das abas (sem linhas retas sobrando entre elas).
#let _dn(sz: 1.6, t: 0.38, tw: 0.35, h: 1.25) = {
  let s = sz
  let P(x, y) = (x * 1in, y * 1in)
  let pts(a) = a.map(q => P(q.at(0), q.at(1)))
  let ln(x0, y0, x1, y1) = place(top + left, line(start: P(x0, y0), end: P(x1, y1), stroke: (paint: ink, thickness: 1.3pt, dash: "dashed")))
  let gray = luma(215)
  let c = 0.13   // chanfro das abas de cima
  // aba no lado direito do triângulo i: ponto na aresta (fração f do vértice da base até a ponta) e deslocamento e
  let edge(i, f) = (((i + 1) * s) + f * (-0.5 * s), 2 * s + f * h)
  let tab(i) = {
    let h1 = edge(i, 0.28)
    let h2 = edge(i, 0.90)
    (h1, (h1.at(0) + 0.30, h1.at(1) + 0.10), (h2.at(0) + 0.24, h2.at(1) - 0.08), h2)
  }
  let bottom = ()
  for i in (3, 2, 1, 0) {
    bottom += tab(i)
    bottom += (((i + 0.5) * s, 2 * s + h),)
    bottom += ((i * s, 2 * s),)
  }
  let outline = (
    (s, 0), (2 * s, 0), (2 * s, s), (2 * s + c, s - t), (3 * s - c, s - t), (3 * s, s), (3 * s + c, s - t), (4 * s - c, s - t), (4 * s, s),
    (4 * s + tw, s + 0.25), (4 * s + tw, 2 * s - 0.25), (4 * s, 2 * s),
  ) + bottom + (
    (0, s), (c, s - t), (s - c, s - t), (s, s),
  )
  block(width: (4 * s + tw) * 1in, height: (2 * s + h) * 1in, {
    // abas cinza (só preenchimento; o corte vem do contorno e a dobra, das linhas tracejadas)
    for x0 in (0, 2 * s, 3 * s) {
      place(top + left, polygon(fill: gray, stroke: none, ..pts(((x0, s), (x0 + c, s - t), (x0 + s - c, s - t), (x0 + s, s)))))
    }
    place(top + left, polygon(fill: gray, stroke: none, ..pts(((4 * s, s), (4 * s + tw, s + 0.25), (4 * s + tw, 2 * s - 0.25), (4 * s, 2 * s)))))
    for i in range(4) {
      place(top + left, polygon(fill: gray, stroke: none, ..pts(tab(i))))
    }
    // contorno geral (corte)
    place(top + left, polygon(fill: none, stroke: 1.9pt + ink, ..pts(outline)))
    // faces: letra em pé + nome
    for (i, (g, nm)) in (("נ", "Nun"), ("ג", "Gimel"), ("ה", "Hei"), ("ש", "Shin")).enumerate() {
      place(top + left, dx: (i * s) * 1in, dy: s * 1in, box(width: s * 1in, height: s * 1in,
        align(center + horizon, stack(dir: ttb, spacing: 6pt,
          text(font: heb-font, size: 64pt, lang: "he", top-edge: "bounds", bottom-edge: "bounds")[#g],
          text(font: display, weight: "bold", size: 12pt, tracking: 0.05em, upper(nm))))))
    }
    // tampa: X no centro
    place(top + left, dx: s * 1in, dy: 0in, box(width: s * 1in, height: s * 1in,
      align(center + horizon, stack(dir: ttb, spacing: 4pt,
        text(font: display, weight: "bold", size: 40pt)[X],
        text(font: display, size: 8.5pt, tracking: 0.08em)[POKE THE STRAW HERE]))))
    // dobras (tracejadas): entre faces, base das abas e da tampa, base dos triângulos e base das abas dos triângulos
    ln(s, s, s, 2 * s); ln(2 * s, s, 2 * s, 2 * s); ln(3 * s, s, 3 * s, 2 * s); ln(4 * s, s, 4 * s, 2 * s)
    ln(0, s, 4 * s, s); ln(0, 2 * s, 4 * s, 2 * s)
    for i in range(4) {
      let tt = tab(i)
      ln(tt.at(0).at(0), tt.at(0).at(1), tt.at(3).at(0), tt.at(3).at(1))
    }
  })
}

#v(1fr)
#align(center, _dn())
#v(0.15in)
#block(width: 100%, fill: tint, radius: 8pt, inset: (x: 12pt, y: 9pt), text(size: 13pt)[*Tip:* thin paper bends. For a dreidel that really spins, trace this pattern onto cardboard or thick paper (or glue the page onto cardboard first). Fold the four pointy triangles inward and glue each gray tab to the next triangle to close the point.])
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

    If your dreidel has Pei (#_hl[פ]) instead of Shin (#_hl[ש]), follow the same rule: put one in.

    If the pot ever runs out, everyone puts 1 coin back in. Keep spinning until someone wins all the gelt, or until it's time to light the candles, whichever comes first.
  ]
  #v(0.45in)
  #subhead[Scoreboard]
  #text(size: 15pt)[Fill in one circle for every round you win.]
  #v(0.25in)
  #scoreboard([Player: #box(width: 1.1in, stroke: (bottom: 1.4pt + ink), [])], [Player: #box(width: 1.1in, stroke: (bottom: 1.4pt + ink), [])], [Player: #box(width: 1.1in, stroke: (bottom: 1.4pt + ink), [])], label-w: 2.1in)
]
