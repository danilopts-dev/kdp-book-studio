= Night 1 — Mattathias Says No

#story[
  A long time ago, a king named Antiochus ruled over the land of Judea. He wanted everyone in his kingdom to worship the same way he did. He made laws against Jewish traditions: no more keeping Shabbat, no more celebrating Jewish holidays, and no more following the teachings of the Torah. For the Jewish people, that was impossible to accept.

  In a small town called Modiin lived an old man named Mattathias and his five sons. When the king's soldiers ordered Mattathias to take part in a public ceremony honoring another god, he refused. He and his sons grabbed their tools, left Modiin, and fled into the hills before the king could send more soldiers.

  Up in the hills of Judea, they were cold, they were outnumbered, and they were free. That was where the fight for Hanukkah began, one family, one no, one mountain at a time.
]

#art("11.png", w: 4.1in, below: 0.02in)

#v(0.06in)

#whats-a("Maccabee")[Mattathias's sons and the fighters who joined them were called the Maccabees. Some say the name comes from a Hebrew word for "hammer," because that's exactly how they fought: small, fast, and impossible to ignore.]

#pagebreak()

#activity(1, "Escape to the Hills")[Help Mattathias and his sons escape the soldiers and reach the safety of the hills! Start at the town of Modiin and find your way through the maze to the mountaintop.]

#align(center, maze-ends("labirinto_facil"))

#pagebreak()

#activity(1, "Word Hunt: Night 1")[These names and words are hiding in the grid below. Can you find all ten? Look across and up and down, no sneaky diagonals tonight.]

#puzzle("cacapalavras_noite1_grade.png", w: 5.9in)

#word-list("JUDAH", "MACCABEE", "ANTIOCHUS", "MATTATHIAS", "TEMPLE", "HILLS", "TORAH", "FAITH", "COURAGE", "MODIIN")

#pagebreak()

#activity(1, "Unscramble the Words")[These words from tonight's story and its world are all mixed up. Read the clue, then write the word in the boxes.]

#let _un = json(_pz + "extra_n1_unscramble.json").items
#v(0.04in)
#for (i, it) in _un.enumerate() {
  block(width: 100%, breakable: false, above: 0pt, below: 0pt, stroke: (bottom: 1pt + soft), inset: (top: 0.07in, bottom: 0.06in), {
    grid(columns: (0.62in, 2.5in, 1fr), column-gutter: 0.1in, align: horizon,
      box(width: 0.44in, height: 0.44in, radius: 50%, fill: ink, align(center + horizon, text(fill: white, font: display, weight: "bold", size: 15pt, str(i + 1)))),
      text(font: display, size: 27pt, weight: "bold", tracking: 0.16em, it.scrambled),
      stack(dir: ltr, spacing: 6pt, ..range(it.length).map(_ => box(width: 0.36in, height: 0.44in, stroke: (bottom: 1.8pt + ink)))))
    v(0.07in)
    pad(left: 0.72in, text(size: 13pt, it.clue))
  })
}

#pagebreak()

#activity(2, "Back to Modiin (The Hard Way)")[This trail has more twists. Start where the family hides in the hills and find the one true path back down to warn the next village. Watch out for the dead ends, a soldier could be waiting around any of them!]

#align(center, maze-ends("labirinto_medio"))

#pagebreak()

#activity(2, "Why is Judah called the Hammer?")[Judah, one of Mattathias's sons, led the fighters after his father. People called him Judah Maccabee. One explanation of the name is "the Hammer," because he hit hard and moved fast, and his small army kept winning battles nobody expected them to win.

Finish the drawing below: give Judah his hammer, his shield, and a look on his face that says he is not backing down.]

#draw-box(5.7in, body: image("/books/hanukkah-8-nights/inputs/illustrations_hi/13.png", height: 5.3in))

#pagebreak()

#activity(2, "Crack the Code")[Each number stands for a letter: A is 1, B is 2, and so on. Decode the numbers to read a line from tonight's story.]

#let _cell(l, n) = block(width: 100%, stroke: 1.2pt + ink, inset: (y: 7pt), align(center, stack(spacing: 4pt,
  text(font: display, weight: "bold", size: 21pt, l), text(size: 14pt, fill: mid, str(n)))))
#block(width: 100%, above: 0.22in, below: 0.1in, breakable: false, {
  _kicker(size: 10pt)[The code]
  v(0.06in)
  grid(columns: (1fr,) * 13, column-gutter: 4pt, row-gutter: 7pt,
    ..range(1, 27).map(n => _cell(str.from-unicode(64 + n), n)))
})

#let _cd = json(_pz + "extra_n1_codigo.json").lines
#v(0.3in)
#_kicker(size: 10pt)[The message]
#v(0.18in)
#for line in _cd {
  block(width: 100%, breakable: false, above: 0.04in, below: 0.4in,
    stack(dir: ltr, spacing: 0.36in, ..line.map(word =>
      stack(dir: ltr, spacing: 4pt, ..word.map(n => stack(spacing: 6pt,
        box(width: 0.56in, align(center, text(font: display, weight: "bold", size: 22pt, str(n)))),
        box(width: 0.56in, height: 0.62in, stroke: 1.6pt + ink)))))))
}

#pagebreak()

#before-candles[
  #subhead[Tonight's Joke]
  #joke[Why did Mattathias bring his whole toolbox to Modiin? \ Because when the king's soldiers showed up, he knew exactly how to make a point!]

  #subhead[The Blessings]
  Before you light the candles, say these two blessings together. You'll say them every night of Hanukkah. The first thanks God for the mitzvah, the commandment, of lighting the Hanukkah candles. The second remembers the miracles of long ago.

  #blessing("Baruch atah Adonai, Eloheinu melech ha'olam, asher kid'shanu b'mitzvotav v'tzivanu l'hadlik ner shel Hanukkah.", "Blessed are You, Adonai our God, Ruler of the universe, who made us holy with commandments and commanded us to light the Hanukkah candles.")

  #blessing("Baruch atah Adonai, Eloheinu melech ha'olam, she'asah nisim la'avoteinu bayamim hahem baz'man hazeh.", "Blessed are You, Adonai our God, Ruler of the universe, who worked miracles for our ancestors in those days, at this season.")

  #subhead[The Shehecheyanu: The First Night You Light]
  Tonight only, add a third blessing, the Shehecheyanu. It's said the first time you light Hanukkah candles each year, so light number one gets its own special thank-you.

  #blessing("Baruch atah Adonai, Eloheinu melech ha'olam, shehecheyanu v'kiy'manu v'higiyanu laz'man hazeh.", "Blessed are You, Adonai our God, Ruler of the universe, who has kept us alive, sustained us, and brought us to this season.")
]

#art("14.png", w: 85%)
