= Night 7 — Give Some Light Away

#story[
  Every night of Hanukkah, kids get gelt, coins to spend, save, or share. But gelt has always carried a second job, too.

  Many families teach a simple rule with the gelt: some coins are just for fun, and some go into the tzedakah box, to help people who need it. A little of each night's gelt goes toward someone else, not just yourself.

  This isn't just a Hanukkah idea. Giving to help others is one of the oldest values in Jewish life, practiced all year, not only in December. Hanukkah just gives kids a fun, hands-on way to try it: real coins, a real box, a real choice about what to do with what you have.

  Tonight, before you spin another dreidel, set a few coins aside. Watch the tzedakah box get a little heavier.
]

#art("71.png", w: 7.2in, below: 0.04in)

#pagebreak()

#activity(1, "Count the Gelt")[Count the coins in each group. Write the total on the line.]

#let _blank = box(width: 1.5in, height: 0.34in, stroke: (bottom: 1.6pt + ink), [])
#let _group(label, file) = block(width: 100%, breakable: false, above: 0.0in, below: 0.16in,
  stroke: 1.4pt + ink, radius: 10pt, inset: (x: 18pt, y: 14pt), {
    text(font: display, weight: "bold", size: 20pt, tracking: 0.03em)[#label: #h(6pt) #_blank]
    v(0.1in)
    align(center, image(_pz + file, width: 6.4in))
  })

#v(0.1in)
#_group("Group A", "noite7_contar_moedas_grupo_a_recorte.png")
#_group("Group B", "noite7_contar_moedas_grupo_b_recorte.png")

#v(0.02in)
#whats-a("tzedakah", a: false)[Tzedakah means giving to help people in need, like sharing money or food. It comes from the Hebrew word for justice, because helping is simply the right thing to do. Many families keep a tzedakah box at home.]
#art("72.png", w: 4.7in, below: 0.0in)

#pagebreak()

#activity(1, "Bring the Gelt to the Tzedakah Box")[Help the gelt find its way through the maze to the tzedakah box.]

#v(1.2in)
#align(center, maze-ends("noite7_labirinto_tzedaka", icon-in: "73_gelt.png", icon-out: "73_box.png"))

#pagebreak()

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
      v(0.5in)
      box(width: 2.2in, stroke: (bottom: 1.6pt + ink), [])
    }))

#v(0.05in)
#stack(dir: ttb, spacing: 0.16in,
  _prob(1, [You have 12 gelt coins. You split all of them into 3 equal piles: one to give to tzedakah, one to save, and one to spend. How many coins are in each pile?]),
  _prob(2, [You have 20 gelt coins. First, you put 4 coins in the tzedakah box. Then you split the coins that are left into 4 equal jars to save. How many coins go in each jar?]),
  _prob(3, [Your family collected 30 gelt coins for tzedakah tonight. You want to put an equal number of coins into 5 different tzedakah boxes for 5 different causes. How many coins go in each box?]),
  _prob(4, [You earned 24 gelt coins from your grandparents and 12 more from your aunt and uncle. You decide to split everything evenly: half for tzedakah, half to save. How many coins go to tzedakah?]))

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
