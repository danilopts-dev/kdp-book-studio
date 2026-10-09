= Night 8 — All Eight Lights

#story[
  On the first night, this book started with Mattathias saying no to a king. Tonight, you're about to light all eight candles, plus the shamash. That's a lot of light for one small jar of oil to promise.

  Hanukkah means "dedication." The word points back to the moment the Maccabees cleaned the Temple and lit it again, dedicating it all over, after it had been taken from them. But the word still does work today. Lighting a full hanukkiah is its own small dedication: to remembering a hard story, to being grateful for what stayed lit, to a family gathered in one room.

  Every family carries something different into these eight nights: courage, cleaning, a jar of oil, a window light, a spinning top, fried food, a coin for someone else. Tonight, look at the whole hanukkiah, glowing all at once. That's eight nights of light, still going.
]

#art("82.png", w: 5.4in, below: 0.04in)

#whats-a("Hanukkah", a: false)[Hanukkah means "dedication." The word remembers when the Maccabees cleaned and relit the Temple, dedicating it again after Antiochus's soldiers had taken it over. Today, many families connect that same word to family, gratitude, and keeping the light going.]

#pagebreak()

#activity(1, "Color the Hanukkiah: All Eight Lights")[Here's the hanukkiah with every candle burning, all eight plus the shamash. Color the whole page any way you like.]

#v(0.05in)
#align(center, image(_ill + "81.png", height: 8.0in, fit: "contain"))

#pagebreak()

#activity(1, "Match the Night")[Draw a line from each night to what that night's story was about.]

#let _mdot = circle(radius: 0.1in, fill: ink, stroke: 1.4pt + ink)
#let _mn = json(_pz + "extra_n8_match.json")
#let _mleft(it) = block(width: 100%, height: 0.98in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 12pt),
  align(left + horizon, stack(dir: ttb, spacing: 5pt,
    text(font: display, weight: "bold", size: 12pt, tracking: 0.14em, [NIGHT #it.night]),
    text(font: display, weight: "bold", size: 16pt, it.title))))
#let _mright(it) = block(width: 100%, height: 0.98in, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 12pt),
  align(left + horizon, text(size: 14pt, it.fact)))

#v(0.15in)
#grid(columns: (2.55in, 0.4in, 1fr, 0.4in, 3.0in), row-gutter: 0.27in, align: horizon,
  .._mn.left.enumerate().map(((i, l)) => (_mleft(l), align(center + horizon, _mdot), [], align(center + horizon, _mdot), _mright(_mn.right.at(i)))).flatten())

#pagebreak()

// ---- Family Hanukkah Quiz (perguntas 1-5 e 6-10; respostas só no answer-key)
#let _q(n, body) = block(width: 100%, breakable: false, above: 0.0in, below: 0.0in,
  grid(columns: (0.42in, 1fr), column-gutter: 16pt, align: top,
    box(width: 0.42in, height: 0.42in, radius: 50%, fill: ink,
      align(center + horizon, text(fill: white, font: display, weight: "bold", size: 17pt, str(n)))),
    {
      text(size: 16pt, body)
      v(0.32in)
      box(width: 100%, stroke: (bottom: 1.6pt + ink), [])
    }))

#activity(2, "Family Hanukkah Quiz")[Answer these questions about the eight nights you just finished. Grown-ups can play too, no peeking at the book!]

#v(0.12in)
#stack(dir: ttb, spacing: 0.3in,
  _q(1, [What was the name of the king who tried to stop Jewish people from keeping their traditions?]),
  _q(2, [What was the name of the old man from Modiin who said no to the king's soldiers?]),
  _q(3, [According to the story, what does "Maccabee" mean?]),
  _q(4, [How many branches does the Temple menorah have?]),
  _q(5, [What's the name of the helper candle that lights all the others?]))

#pagebreak()

#activity(2, "Family Hanukkah Quiz")[]

#v(0.12in)
#stack(dir: ttb, spacing: 0.3in,
  _q(6, [How many candles do you light on Night 4, counting the shamash?]),
  _q(7, [According to the story, how many nights did the little jar of oil burn for?]),
  _q(8, [What does "gelt" mean?]),
  _q(9, [What is a latke made from?]),
  _q(10, [What's tzedakah?]))

#v(0.4in)
#block(width: 100%, stroke: (top: 2.5pt + ink), inset: (top: 0.14in), {
  text(font: display, weight: "bold", size: 15pt, tracking: 0.06em, upper[Family Scoreboard: Grown-Ups vs. Kids])
  v(0.06in)
  text(size: 14pt)[Every correct answer earns one tally mark for that team. Most marks after all ten questions wins.]
  v(0.14in)
  // linha em branco por equipe (como no manuscrito): a criança desenha um tracinho por resposta certa
  for t in ([Grown-Ups], [Kids]) {
    grid(columns: (1.5in, 1fr), align: bottom, column-gutter: 10pt,
      text(font: display, weight: "bold", size: 17pt, t),
      box(width: 100%, height: 0.62in, stroke: (bottom: 1.8pt + ink), []))
    v(0.14in)
  }
})

#pagebreak()

#activity(2, "Night by Night Word Search")[Words from all eight nights are hiding here. Look across, down, and diagonally. No words go backward.]

#puzzle("extra_n8_cacapalavras_noites_grade.png", w: 5.8in)

#word-list("DREIDEL", "SHAMASH", "HANUKKIAH", "MIRACLE", "TZEDAKAH", "WINDOW", "DEDICATION", "GRATITUDE", "SOLDIERS", "NEIGHBORS", "SECRET", "FRIED")

#pagebreak()

// ---- Certificado: moldura 83.png como fundo da página inteira (dentro da área segura), sem folio
#page(footer: none, margin: 0in)[
  #place(center + horizon, image(_ill + "83.png", width: 7.5in))
  #place(center + horizon, dy: 0.55in, block(width: 5.3in, {
    set align(center)
    set par(leading: 0.5em)
    text(font: display, size: 40pt, weight: "bold", tracking: 0.04em, upper[Official Hanukkah Expert])
    v(0.5in)
    text(size: 19pt)[This certifies that]
    v(0.5in)
    box(width: 100%, stroke: (bottom: 1.8pt + ink), [])
    v(0.5in)
    text(size: 19pt)[completed all eight nights of Hanukkah, answered the Family Quiz, and knows a jarful of Hanukkah stories.]
    v(0.7in)
    text(size: 19pt)[Awarded on: #box(width: 2.6in, stroke: (bottom: 1.8pt + ink), [])]
  }))
]

#pagebreak(weak: true)

#before-candles[
  #subhead[Pick Tonight's Joke]
  #text(size: 18pt)[It's the last night. Let one kid in the family pick their favorite joke below, then read it out loud before you light the candles.]
  #v(0.3in)
  #let _j(label, q, a) = block(width: 100%, fill: tint, radius: 12pt, inset: (x: 22pt, y: 20pt), breakable: false, {
    text(font: display, weight: "bold", size: 15pt, tracking: 0.06em, upper[Joke #label])
    v(0.08in)
    text(size: 20pt, q)
    v(0.1in)
    text(size: 20pt, a)
  })
  #stack(dir: ttb, spacing: 0.25in,
    _j("A", [Knock, knock. Who's there? Oil. Oil who?], [Oil light the last candle with you, so open the door!]),
    _j("B", [What did the eighth candle say to the shamash on the last night?], ["Thanks for the light! I've waited all week for my turn."]),
    _j("C", [What do you call the last night of Hanukkah, if you're a candle?], [The wick-end, when all eight burn at once!]))
  #v(0.4in)
  #text(font: display, weight: "bold", size: 22pt, tracking: 0.03em)[Which joke did you pick? #box(width: 2.6in, height: 0.34in, stroke: (bottom: 1.6pt + ink), [])]
]
