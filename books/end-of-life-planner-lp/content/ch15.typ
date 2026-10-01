#let wlines(n) = for _ in range(n) { box(height: elp-line-h, width: 100%, stroke: (bottom: elp-rule)); linebreak() }

#let prompts(..qs) = block(width: 100%, breakable: false, below: 0.1in,
  text(size: 14pt, fill: luma(80), {
    [Some things you might say:]
    for q in qs.pos() { linebreak(); [– #q] }
  }))

#let letter-head(qs, lines-n) = {
  elp-field("To:")
  v(0.08in)
  prompts(..qs)
  wlines(lines-n)
}

#chapter-opener(4, "A Few Words for the People I Love",
  [This section is optional. Skip it if you'd rather. If you'd like to leave a few words, write as much or as little as you like. Short is fine. You can come back to it and change it any time.])

#letter-head((
  [What is one thing you remember doing together?],
  [What do you want them to do after you are gone, like keep a tradition?],
  [Is there something you never got around to saying?],
), 9)

#pagebreak()
#wlines(18)

#pagebreak()
#letter-head((
  [What do you like best about the way they live?],
  [Is there something you'd like them to take care of, or not worry about?],
), 13)

#pagebreak()
#letter-head((
  [What did they do that you were grateful for?],
  [Is there a place, a meal, or a song that reminds you of them?],
  [Is there something you would like them to do now and then, like visit a place?],
), 13)

#pagebreak()
#elp-heading[What I Want You to Know]
#text(size: 16pt)[This page is for everyone. Say what's on your mind, in plain words.]
#v(0.1in)
#wlines(15)

#pagebreak()
#wlines(18)
