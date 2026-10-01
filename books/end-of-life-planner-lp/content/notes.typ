#let nlines(n) = for _ in range(n) { box(height: elp-line-h, width: 100%, stroke: (bottom: elp-rule)); linebreak() }
#let nhead = block(below: 0.1in, text(size: 14pt, fill: luma(110), tracking: 0.06em, upper[Notes]))

#pagebreak(weak: true)
#set par(first-line-indent: 0em, justify: false)
#{
  show heading.where(level: 1): it => block(above: 0pt, below: 0.15in, width: 100%,
    text(size: 26pt, weight: "bold", it.body))
  heading(level: 1, [Notes])
}
#line(length: 100%, stroke: 1.2pt + black)
#v(0.1in)
#nlines(15)

#for _ in range(7) {
  pagebreak()
  nhead
  nlines(16)
}
