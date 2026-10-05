= After Hanukkah

// ---- Página 1: My Hanukkah Memory Page
// Enfeite de código: hanukkiah pequena, velas apagadas, só o shamash aceso (sem arte gerada).
#let _mini-hk = {
  let cw = 0.1in
  let candle(h, lit: false) = stack(dir: ttb, spacing: 1pt,
    if lit {
      polygon(fill: none, stroke: 1.4pt + ink, (cw / 2, 0pt), (cw * 0.9, 0.11in), (cw / 2, 0.18in), (cw * 0.1, 0.11in))
    } else { v(0.18in) },
    rect(width: cw, height: h, stroke: 1.4pt + ink, radius: 1.5pt))
  stack(dir: ttb, spacing: 0pt,
    align(bottom, stack(dir: ltr, spacing: 0.07in,
      ..range(4).map(_ => candle(0.36in)), candle(0.55in, lit: true), ..range(4).map(_ => candle(0.36in)))),
    rect(width: 1.6in, height: 0.07in, fill: ink, radius: 2pt))
}
#place(top + right, dy: 0.02in, _mini-hk)

#let _field(label, lines: 1, note: none) = block(width: 100%, breakable: false, above: 0pt, below: 0pt, {
  text(font: display, weight: "bold", size: 17pt, label)
  if note != none { h(8pt); text(size: 13pt, fill: mid, note) }
  for _ in range(lines) {
    v(0.43in)
    box(width: 100%, stroke: (bottom: 1.8pt + ink), [])
  }
})

#v(0.04in)
#text(font: display, weight: "bold", size: 15pt, tracking: 0.06em, upper[My Hanukkah Memory Page])
#v(0.1in)
#text(size: 15pt)[Hanukkah is over for this year, but the memories don't have to be. Fill this page in together before you put the hanukkiah away.]
#v(0.2in)

#block(width: 100%, breakable: false, {
  text(font: display, weight: "bold", size: 17pt)[My favorite night was:]
  h(10pt)
  box(width: 0.9in, height: 0.5in, stroke: 1.8pt + ink, radius: 6pt, [])
  h(10pt)
  text(size: 13pt, fill: mid)[(Write the number, 1 through 8.)]
})
#v(0.32in)
#_field([Why:], lines: 2)
#v(0.2in)
#_field([My favorite gift this year was:], lines: 1)
#v(0.3in)

#block(width: 100%, stroke: (top: 2.5pt + ink), inset: (top: 0.14in), breakable: false, {
  text(font: display, weight: "bold", size: 15pt, tracking: 0.06em, upper[Final dreidel tournament score])
  v(0.05in)
  text(size: 14pt)[Draw one tally mark for every win.]
  v(0.14in)
  for t in ([Me:], [My family:]) {
    grid(columns: (1.6in, 1fr), align: horizon, column-gutter: 8pt,
      text(font: display, weight: "bold", size: 17pt, t),
      stack(dir: ltr, spacing: 0.2in, ..range(5).map(_ => box(width: 0.5in, height: 0.5in, stroke: 1.8pt + ink, radius: 5pt, []))))
    v(0.1in)
  }
})
#v(0.14in)
#_field([One thing I want to try next Hanukkah:], lines: 2)

#pagebreak()

// ---- Página 2: That's a wrap
#v(0.2in)
#align(center, text(font: display, weight: "bold", size: 30pt, tracking: 0.03em, upper[That's a wrap on all eight nights!]))
#v(0.3in)
#block(width: 100%, {
  set par(leading: 0.9em)
  text(size: 17pt)[You made it through Judah's escape, the messy Temple, the jar of oil, the lighting, the dreidel, the fried food, the tzedakah, and the last light. Great job.]
})
#v(0.35in)
#block(width: 100%, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 20pt, y: 16pt), breakable: false, {
  text(font: display, weight: "bold", size: 12pt, tracking: 0.1em, upper[Coming next in the series])
  v(0.05in)
  text(size: 22pt, weight: "bold", font: display)[Seder Night]
  v(0.03in)
  text(size: 16pt)[A night by night activity book for Passover.]
})
#v(0.35in)
#block(width: 100%, fill: tint, radius: 12pt, inset: (x: 22pt, y: 22pt), breakable: false, {
  set par(leading: 0.9em)
  text(size: 16pt)[If you haven't already, grab your free *8 Nights Family Pack*: a printable blessing card, dreidel rules, and gift tags for next year.]
  v(0.1in)
  text(size: 16pt)[Scan the code below.]
})
#v(0.3in)
#align(center, bonus-qr(w: 2.0in))
