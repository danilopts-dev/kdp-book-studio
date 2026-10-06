= Night 6 — Everything Fried

#story[
  Long ago, when the Maccabees found the tiny jar of oil in the Temple, they didn't know if it would even burn all night. The story says it did, and then kept going for eight whole nights, exactly as many as they needed.

  That's why, all these years later, Hanukkah has a tradition that sounds like a dream come true: eat food fried in oil. Lots of it.

  Families make latkes, crispy pancakes made from grated potato and onion, fried in a pan until the edges turn golden brown. Other families make sufganiyot, round jelly doughnuts, deep fried and dusted with sugar. Many Sephardic families fry bimuelos, little puffs of dough dripping with honey. Every family has its favorite, and some make them all.

  Every bite says the same thing the little jar said: oil that should have run out kept going anyway.

  Tonight, the kitchen gets loud, the pan sizzles, and the whole house smells like Hanukkah.
]

#art("61.png", w: 7.2in, below: 0.04in)

#pagebreak()

// ---- Receita
#let _job = box(fill: ink, radius: 6pt, inset: (x: 7pt, y: 3.5pt), baseline: 3pt,
  text(fill: white, font: display, size: 11.5pt, weight: "bold", tracking: 0.08em)[YOUR JOB])
#let _num(n, job) = box(width: 0.42in, height: 0.42in, radius: 50%,
  fill: if job { ink } else { white }, stroke: 1.6pt + ink,
  align(center + horizon, text(fill: if job { white } else { ink }, font: display, weight: "bold", size: 16pt, str(n))))
#let _step(n, job: false, body) = block(width: 100%, breakable: false, above: 0.0in, below: 0.0in,
  fill: if job { tint } else { none }, radius: 8pt, inset: (x: 10pt, y: 8pt),
  grid(columns: (0.42in, 1fr), column-gutter: 14pt, align: horizon,
    _num(n, job),
    {
      set par(leading: 0.62em)
      text(size: 14pt, if job { [#_job #h(4pt) #body] } else { body })
    }))

#block(width: 100%, above: 0.05in, below: 0.1in,
  text(font: display, size: 23pt, weight: "bold", upper[Latke Recipe: Make It With a Grown-Up]))

Makes about 12 latkes. A grown-up handles the grater, the stove, and the hot oil. Look for #_job in bold: that's the part you do.

#block(width: 100%, above: 0.12in, below: 0.16in, breakable: false, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt, y: 11pt), {
  text(font: display, weight: "bold", size: 12pt, tracking: 0.06em)[YOU'LL NEED:]
  v(0.04in)
  text(size: 14pt)[4 medium potatoes · 1 small onion · 1 egg · 3 tablespoons flour or matzo meal · 1 teaspoon salt · oil for frying]
})

#text(font: display, weight: "bold", size: 12pt, tracking: 0.06em)[STEPS:]
#v(0.06in)

#stack(dir: ttb, spacing: 0.1in,
  _step(1, job: true)[*Grate the potatoes and onion* into a big bowl. (Grown-up grates, or watches closely if you help.)],
  _step(2, job: true)[*Squeeze out the extra liquid* from the grated potato and onion, using a clean towel or your hands over the sink.],
  _step(3, job: true)[*Crack the egg* into the bowl with the potato and onion.],
  _step(4, job: true)[*Add the flour and salt,* then mix everything together with a spoon.],
  _step(5)[Grown-up heats oil in a pan on the stove.],
  _step(6, job: true)[*Scoop a small pile of the mixture* and hand it to the grown-up to place gently in the hot pan.],
  _step(7)[Grown-up fries each latke for about 3 minutes per side, until golden brown, then moves it to a plate lined with paper towels.],
  _step(8, job: true)[*Top your latke* with applesauce or sour cream, and dig in!])

#v(0.14in)
#block(width: 100%, stroke: (left: 3pt + ink), inset: (left: 12pt, y: 4pt),
  text(size: 13pt)[Steps marked #_job are yours to do. The stove and the hot oil are always a grown-up's job.])

#pagebreak()

#activity(1, "Kitchen Word Search")[Find these kitchen words hiding in the grid. They go across or down.]

#puzzle("noite6_cacapalavras_cozinha_grade.png", w: 6.4in)

#word-list("KITCHEN", "POTATO", "GOLDEN", "SPOON", "ONION", "PLATE", "LATKE", "PAN", "OIL", "FRY")

#pagebreak()

#activity(1, "Latkes or Sufganiyot? A Family Vote")[Ask everyone in your family which one they like best. Mark one tally line for every vote.]

#v(0.1in)
#art("62.png", w: 5.2in, below: 0.12in)

#whats-a("latke")[A latke is a crispy pancake made from grated potato, onion, and egg, fried in oil until golden brown. Families often top it with applesauce or sour cream. Latkes are a Hanukkah favorite because they're fried, just like the oil in the story.]

#whats-a("sufganiyah")[A sufganiyah is a round doughnut, deep fried and filled with jelly, then dusted with powdered sugar. "Sufganiyot" is the plural. Like the latke, it's fried in oil, which is exactly why it belongs on the Hanukkah table.]

#v(0.1in)

#let _vote(label) = block(width: 100%, breakable: false, above: 0.0in, below: 0.12in,
  grid(columns: (2.3in, 1fr), align: bottom, column-gutter: 8pt,
    text(font: display, weight: "bold", size: 18pt, tracking: 0.03em, [#label:]),
    box(width: 100%, height: 0.68in, stroke: (bottom: 1.6pt + ink), [])))

#_vote[Latkes]
#_vote[Sufganiyot]
#_vote[Both, always]

#pagebreak()

#activity(1, "Latke Maze")[The potato is ready for the pan! Start at the potato and find the one path through the maze to the plate.]

#v(0.1in)
#align(center, maze-ends("extra_n6_labirinto_latke", w: 5.2in, side: 1.0in))

#pagebreak()

#activity(2, "The Great Latke Disaster")[Fill in the blanks before you read the story out loud. Ask family members for a word each, without telling them the story first, it's funnier that way.]

#let _n = state("blank-n", 0)
#let _b(label) = {
  _n.update(n => n + 1)
  context {
    let n = _n.get()
    h(2pt)
    box({
      box(width: 0.24in, height: 12pt, outset: (y: 2.6pt), radius: 50%, fill: ink, baseline: 2pt,
        align(center + horizon, text(fill: white, font: display, weight: "bold", size: 12pt, str(n))))
      h(3pt)
      box(width: 1.1in, height: 12pt, stroke: (bottom: 1.5pt + ink), baseline: 2pt, [])
      h(3pt)
      text(size: 12pt, fill: mid)[(#label)]
    })
    h(2pt)
  }
}

#v(0.1in)
#block(width: 100%, stroke: 1.4pt + ink, radius: 10pt, inset: (x: 16pt, y: 16pt), {
  set par(leading: 1.2em, spacing: 1.5em)
  set text(size: 15.5pt)
  [#_b[name] was in charge of the latkes this year, and it was going to be the best Hanukkah ever. The kitchen smelled like #_b[adjective] oil, and the pan was #_b[adjective] hot.

  "Watch this," said #_b[name], flipping a latke high into the air. It spun once, twice, and landed right on top of the #_b[noun, plural]. The whole family started to #_b[verb].

  Just then, the cat jumped onto the counter and started #_b[verb ending in -ing] at the applesauce. Grandma grabbed a #_b[noun] to shoo it away, and somehow knocked over the entire bowl of grated #_b[noun, plural].

  For a moment, nobody said a word. Then #_b[name] started laughing so hard that everyone else did too. They ate the latkes anyway, sat on the floor to eat them, and agreed it was the most #_b[adjective] Hanukkah dinner they'd ever had.]
})

#pagebreak()

#activity(2, "Big Kitchen Word Search")[This one's tougher: the words can go across, down, or diagonally, in any direction.]

#puzzle("noite6_cacapalavras_14x14_grade.png", w: 6.0in)

#word-list("SUFGANIYAH", "DOUGHNUT", "TRADITION", "GRIDDLE", "PLATTER", "CRISPY", "SIZZLE", "FAMILY", "JELLY", "GRATER")

#pagebreak()

#activity(2, "Hanukkah Food Crossword")[Use the clues to fill in the grid. Words go across and down. The small numbers show where each word starts.]

#let _cw = json(_pz + "extra_n6_palavras_cruzadas_gabarito.json")
#let _cl(it) = grid(columns: (0.38in, 1fr), column-gutter: 4pt, align: top,
  text(font: display, weight: "bold", size: 13pt, [#it.n.]),
  text(size: 12.5pt, it.clue))

#v(0.02in)
#puzzle("extra_n6_palavras_cruzadas_grade.png", w: auto, h: 4.55in)
#v(0.08in)
#grid(columns: (1fr, 1fr), column-gutter: 0.25in, align: top,
  {
    text(font: display, weight: "bold", size: 12pt, tracking: 0.1em)[ACROSS]
    v(0.05in)
    stack(dir: ttb, spacing: 0.09in,.._cw.across.map(_cl))
  },
  {
    text(font: display, weight: "bold", size: 12pt, tracking: 0.1em)[DOWN]
    v(0.05in)
    stack(dir: ttb, spacing: 0.09in, .._cw.down.map(_cl))
  })

#pagebreak()

#before-candles[
  #subhead[Latke Riddle]
  #block(width: 100%, fill: tint, radius: 12pt, inset: 22pt, text(size: 20pt)[I start as a potato, I get grated and fried, and I end up golden on a plate by your side. What am I?])
  #v(0.2in)
  #draw-box(1.5in, label: [My guess:])
  #v(0.2in)
  #subhead[Latke Joke]
  #block(width: 100%, fill: tint, radius: 12pt, inset: 26pt, text(size: 22pt)[Why did the latke stop telling jokes?])
  #v(0.2in)
  #block(width: 100%, fill: tint, radius: 12pt, inset: 26pt, text(size: 22pt)[It was afraid it would crack up in the pan!])
]
