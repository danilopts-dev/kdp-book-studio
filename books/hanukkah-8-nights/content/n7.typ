= Night 7 — Give Some Light Away

#story[
  During Hanukkah, many families give children gelt, coins to spend, save, or share. But gelt has always carried a second job, too.

  Many families teach a simple rule with the gelt: some coins are just for fun, and some go into the tzedakah box, to help people who need it. A little of each night's gelt goes toward someone else, not just yourself.

  This isn't just a Hanukkah idea. Giving to help others is one of the oldest values in Jewish life, practiced all year long. Hanukkah just gives kids a fun, hands-on way to try it: real coins, a real box, a real choice about what to do with what you have.

  Tonight, before you spin another dreidel, set a few coins aside. Watch the tzedakah box get a little heavier.
]

#art("71.png", w: 7.2in, below: 0.04in)

#pagebreak()

#activity(1, "Count the Gelt")[Count the coins in each group. Each full row has 10 coins. Write the total on the line, then add the two groups together.]

#let _coin(d) = box(width: d, height: d, radius: 50%, stroke: 1.8pt + ink, inset: 0pt,
  align(center + horizon, text(font: display, weight: "bold", size: d * 0.55)[\$]))
#let _rows(n, per, d, gap) = grid(columns: (d,) * per, column-gutter: gap, row-gutter: gap, ..range(n).map(_ => _coin(d)))
#let _blank = box(width: 1.2in, height: 0.34in, stroke: (bottom: 1.6pt + ink), [])
#let _group(label, n) = block(width: 100%, breakable: false, above: 0.0in, below: 0.14in,
  stroke: 1.4pt + ink, radius: 10pt, inset: (x: 18pt, y: 12pt), {
    text(font: display, weight: "bold", size: 19pt, tracking: 0.03em)[#label: #h(6pt) #_blank #h(4pt) #text(size: 14pt, weight: "regular", tracking: 0em)[coins]]
    v(0.1in)
    align(center, _rows(n, 10, 0.36in, 0.08in))
  })

#v(0.08in)
#_group("Group A", 17)
#_group("Group B", 26)
#block(width: 100%, breakable: false, above: 0.0in, below: 0.14in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 18pt, y: 12pt),
  text(font: display, weight: "bold", size: 17pt, tracking: 0.03em)[GROUP A + GROUP B TOGETHER: #h(6pt) #box(width: 0.9in, height: 0.3in, stroke: (bottom: 1.6pt + ink), []) #text(size: 13pt, weight: "regular", tracking: 0em)[coins]])

#v(0.02in)
#whats-a("tzedakah", a: false)[Tzedakah means giving to help people in need, like sharing money or food. It comes from the Hebrew word for justice, because helping is simply the right thing to do. Many families keep a tzedakah box at home.]
#art("72.png", w: 2.7in, below: 0.0in)

#pagebreak()

#activity(1, "Bring the Gelt to the Tzedakah Box")[Help the gelt find its way through the maze to the tzedakah box.]

#v(1.2in)
#align(center, maze-ends("noite7_labirinto_tzedaka", icon-in: "73_gelt.png", icon-out: "73_box.png"))

#pagebreak()

// ---- Expansão (2026-10-06): as duas páginas novas entram ANTES do Coupon Book (paridade da página de recorte)
#activity(1, "Which Pile Has More?")[Count the coins in each pile and write the number under it. Circle the bigger pile, then figure out how many more coins it has.]

#let _pl = json(_pz + "extra_n7_v3.json").piles
#let _coin(d) = box(width: d, height: d, radius: 50%, stroke: 1.6pt + ink, inset: 0pt,
  align(center + horizon, text(font: display, weight: "bold", size: d * 0.55)[\$]))
#let _pile(n) = grid(columns: (0.23in,) * 5, column-gutter: 0.035in, row-gutter: 0.035in, ..range(n).map(_ => _coin(0.23in)))
#let _cnt = box(width: 0.7in, height: 0.3in, stroke: (bottom: 1.6pt + ink), [])
// cada pilha numa caixinha própria, com espaço entre as duas (antes pareciam uma coisa só)
#let _pbox(n) = block(width: 100%, breakable: false, stroke: 1pt + ink, radius: 6pt, inset: (x: 5pt, y: 7pt),
  align(center, stack(spacing: 0.24in, box(height: 1.1in, align(bottom + center, _pile(n))), [\= #_cnt])))

#v(0.06in)
#grid(columns: (1fr, 1fr), column-gutter: 0.2in, row-gutter: 0.2in,
  .._pl.map(p => block(width: 100%, breakable: false, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 9pt, y: 10pt), {
    box(width: 0.36in, height: 0.36in, radius: 50%, fill: ink,
      align(center + horizon, text(fill: white, font: display, weight: "bold", size: 14pt, str(p.n))))
    v(0.06in)
    grid(columns: (1fr, 1fr), column-gutter: 0.3in, _pbox(p.left), _pbox(p.right))
    v(0.12in)
    align(center, text(size: 14pt)[Bigger pile: #box(width: 0.5in, stroke: (bottom: 1.6pt + ink), []) more coins])
  })))

#pagebreak()

#activity(2, "Who Gets What?")[Four kids each did a different kind act. Use the clues to find who did what. Mark ✓ or X in the grid.]

#let _lg = json(_pz + "extra_n7_pilhas_logica.json").who_gets_what
#let _acts = ("hug", "dishes", "story", "toys")

#v(0.06in)
#stack(dir: ttb, spacing: 0.1in, .._lg.clues.enumerate().map(((i, c)) => block(width: 100%, breakable: false,
  grid(columns: (0.4in, 1fr), column-gutter: 12pt, align: horizon,
    box(width: 0.4in, height: 0.4in, radius: 50%, fill: ink,
      align(center + horizon, text(fill: white, font: display, weight: "bold", size: 16pt, str(i + 1)))),
    text(size: 15.5pt, c)))))

#v(0.2in)
#table(columns: (1.3in, 1.45in, 1.45in, 1.45in, 1.45in), rows: (1.3in, 0.95in, 0.95in, 0.95in, 0.95in),
  stroke: 1.5pt + ink, align: center + horizon, inset: 6pt,
  [],
  .._acts.map(a => stack(dir: ttb, spacing: 4pt,
    image(_ill + _lg.acts.at(a).icon, width: 0.7in, height: 0.7in, fit: "contain"),
    text(font: display, weight: "bold", size: 12pt, tracking: 0.04em, upper(_lg.acts.at(a).label)))),
  .._lg.kids.map(k => (text(font: display, weight: "bold", size: 17pt, k), [], [], [], [])).flatten())

// ---- Coupon Book (frente e verso com a MESMA grade; a grade fica em posição fixa para alinhar no duplex)
#let _cw = 3.5in
#let _ch = 2.2in
#let _cdash = (paint: ink, thickness: 1.6pt, dash: "dashed")
#let _coupon-grid(cells) = place(top + left, dy: 2.7in,
  grid(columns: (_cw, _cw), column-gutter: 0.25in, row-gutter: 0.1in, ..cells))
#let _coupon(icon, text-body) = block(width: _cw, height: _ch, stroke: _cdash, radius: 10pt, inset: (x: 14pt, y: 10pt),
  grid(columns: (1.15in, 1fr), column-gutter: 12pt, align: horizon,
    align(center + horizon, image(_ill + icon, width: 1.1in, height: 1.3in, fit: "contain")),
    text(font: display, weight: "bold", size: 15.5pt, text-body)))
#let _coupon-blank = block(width: _cw, height: _ch, stroke: _cdash, radius: 10pt, [])

#activity(2, "Coupon Book: Give Some Light Away")[Cut out these coupons and give them to your family. Each one is a promise to help, no money needed.]

#text(size: 13pt, style: "italic")[Jewish tradition calls helping like this gemilut chasadim: acts of loving-kindness.]

#_coupon-grid((
  _coupon("74_heart.png")[Good for one big hug.],
  _coupon("74_plate.png")[Good for helping with the dishes, no complaining.],
  _coupon("74_book.png")[Good for a story read out loud before bed.],
  _coupon("74_broom.png")[Good for making someone's bed for them.],
  _coupon("74_sun.png")[Good for 15 minutes of quiet while someone naps or reads.],
  _coupon("74_die_fix.png")[Good for picking up ten toys, right now, cheerfully.],
))

// Verso em branco de propósito (mesma grade, sem texto): sem número de página.
#pagebreak()
#page(footer: none)[
  #_coupon-grid(range(6).map(_ => _coupon-blank))
]

#pagebreak(weak: true)

#activity(2, "Split and Save")[Solve each problem. Show your work if you want to!]

#let _prob(n, body) = block(width: 100%, breakable: false, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 18pt, y: 13pt),
  grid(columns: (auto, 1fr), column-gutter: 16pt, align: top,
    box(width: 0.42in, height: 0.42in, radius: 50%, fill: ink,
      align(center + horizon, text(fill: white, font: display, weight: "bold", size: 17pt, str(n)))),
    {
      text(size: 15.5pt, body)
      v(0.42in)
      box(width: 2.2in, stroke: (bottom: 1.6pt + ink), [])
    }))

#v(0.05in)
#stack(dir: ttb, spacing: 0.16in,
  _prob(1, [You have 48 gelt coins. You split all of them into 4 equal piles: one to give to tzedakah, one to save, one to spend, and one to share with your sibling. How many coins are in each pile?]),
  _prob(2, [You have 85 gelt coins. First, you put 25 coins in the tzedakah box. Then you split the coins that are left into 4 equal jars to save. How many coins go in each jar?]),
  _prob(3, [Your family collected 96 gelt coins for tzedakah tonight. You want to put an equal number of coins into 6 different tzedakah boxes for 6 different causes. How many coins go in each box?]),
  _prob(4, [You earned 38 gelt coins from your grandparents and 46 more from your aunt and uncle. You give half of everything to tzedakah. Then you split the rest equally into 3 jars to save. How many coins go in each jar?]))

#pagebreak(weak: true)

#before-candles[
  #subhead[Who Gets the Coupon?]
  #v(0.1in)
  #text(size: 20pt)[Everyone in the family picks a number between 1 and 10. Whoever guesses closest to the grown-up's secret number gets to hand out the first coupon tonight. Take turns being the guesser next time.]
  #v(0.7in)
  #text(font: display, weight: "bold", size: 24pt, tracking: 0.03em)[Rounds played: #box(width: 1.6in, height: 0.34in, stroke: (bottom: 1.6pt + ink), [])]
  #v(0.9in)
  #art("75.png", w: 7.2in)
]
