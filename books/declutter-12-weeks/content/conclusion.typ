// Conclusion — 4 paginas: (1) notas dos comodos antes/agora (mesma lista de 12 comodos da Week 0),
// (2) contagem semanal Keep/Donate/Sell/Toss, (3) placar total, (4) fechamento + proximos livros + NOTES/WINS.
// Reusa helpers _wk-* de wk01.typ e a lista _w0-rooms de wk00.typ.

#let _cc-dot(n) = box(width: 1.25em, height: 1.25em, radius: 50%, stroke: 0.6pt + luma(120), baseline: 0.3em,
  align(center + horizon, text(size: 0.72em, str(n))))
#let _cc-rooms = (
  ("Week 1", "Bathroom"),
  ("Week 2", "Entryway and coat closet"),
  ("Week 3", "Kitchen, part one: counters, pantry, fridge"),
  ("Week 4", "Kitchen, part two: cabinets, gadgets, containers"),
  ("Week 5", "Living room"),
  ("Week 6", "Bedroom"),
  ("Week 7", "Closet"),
  ("Week 8", "Kids' rooms and toys (or hobby room)"),
  ("Week 9", "Home office and paper pile"),
  ("Week 10", "Linen closet, laundry, cleaning supplies"),
  ("Week 11", "Garage, basement, attic, storage"),
  ("Week 12", "Sentimental things"),
)

= Conclusion — Your Before and After

You started with a walk through your home and a pencil. Now you can do the same walk again. Go room by room, don't pick anything up, and give each space the same 1 to 5 rating you used in Week 0. Trust your first reaction, as you did then.

Copy your Week 0 ratings from "Rate Your Rooms" into the first column, then write today's number in the second. Take the after photo from the same spot in the doorway as the before photo, and check the box. Some rooms moved a lot, some a little. Both count.

#v(0.05in)
#block(breakable: false, width: 100%)[
  #set text(size: 0.88em)
  #grid(columns: (auto, 1fr), column-gutter: 8pt, row-gutter: 6pt,
    [#_cc-dot(1)], [*Calm.* Easy to use, and everything has a place.],
    [#_cc-dot(3)], [*Crowded.* You can use it, but it takes effort to find or put away things.],
    [#_cc-dot(5)], [*Stuck.* You avoid the room, or it can't be used the way it was meant to be.],
  )
]

#v(0.1in)
#table(
  columns: (0.9in, 1fr, 0.75in, 0.75in, 0.75in),
  stroke: 0.5pt + luma(140),
  inset: (x: 5pt, y: 5.5pt),
  align: (left + horizon, left + horizon, center + horizon, center + horizon, center + horizon),
  table.header(
    _wk-head[Week],
    _wk-head[Room],
    _wk-head[Week 0 rating],
    _wk-head[Rating now],
    _wk-head[After photo],
  ),
  ..for (wk, room) in _cc-rooms {
    (text(size: 0.85em, wk), text(size: 0.85em, room), [], [], _wk-box)
  },
)

#v(0.15in)
#align(right)[
  *Total before:* #_wk-blank(0.6in) / 60 #h(0.2in) *Total now:* #_wk-blank(0.6in) / 60 #h(0.2in) *Change:* #_wk-blank(0.5in)
]

#pagebreak()

== Your Weekly Counts

Copy the totals from the "Keep / Donate / Sell / Toss Count" page at the end of each week. Then add up each column. Items out are the items that left the house: Donate, Sell and Toss.

#v(0.15in)
#table(
  columns: (5.4em, 1fr, 1fr, 1fr, 1fr, 1.2fr),
  stroke: 0.5pt + luma(140),
  inset: (x: 6pt, y: 11pt),
  align: center + horizon,
  table.header([], _wk-head[Keep], _wk-head[Donate], _wk-head[Sell], _wk-head[Toss], _wk-head[Items out]),
  ..range(1, 13).map(w => (align(left, text(size: 0.9em)[Week #w]), [], [], [], [], [])).flatten(),
  table.cell(align: left)[#text(weight: "bold", size: 0.9em)[Total]], [], [], [], [], [],
)

#v(0.2in)
#text(size: 0.95em)[*Items out, all 12 weeks* (Donate + Sell + Toss): #_wk-blank(0.9in)]
#v(0.1in)
#text(size: 0.95em)[*Items kept, all 12 weeks:* #_wk-blank(0.9in)]
#v(0.2in)
#_wk-field([*The week with the biggest number:*], above: 0.1in)

#pagebreak()

== Your Scoreboard

Four numbers sum up the 12 weeks. Take the first three from your counts and from "Part 3 Totals", and work out the fourth below.

#v(0.15in)
#table(
  columns: (1fr, 1.7in),
  stroke: 1pt + luma(100),
  inset: (x: 10pt, y: 19pt),
  align: (left + horizon, center + horizon),
  [*Items out* \ #text(size: 0.85em)[Donate + Sell + Toss, from the weekly counts]], [],
  [*Money earned* \ #text(size: 0.85em)["All sold" from Part 3 Totals]], [\$],
  [*Value donated* \ #text(size: 0.85em)["All donated" from Part 3 Totals]], [\$],
  [*Hours invested* \ #text(size: 0.85em)[Worked out below]], [],
)

#v(0.25in)
=== Work Out Your Hours

Most days you used a single 15-minute block. Count the days you did the work, including the extra blocks, and multiply.

#v(0.1in)
#block[#_wk-blank(0.7in) days #sym.times 15 minutes = #_wk-blank(0.8in) minutes]
#v(0.1in)
#block[#_wk-blank(0.8in) minutes #sym.div 60 = #_wk-blank(0.7in) hours]

#v(0.25in)
#_wk-field([*The number that surprised me:*], above: 0.1in)
#_wk-field([*What I sold that I'm glad I sold:*], above: 0.2in)
#_wk-field([*The donation I'm proudest of:*], above: 0.2in)
#_wk-field([*Who benefited most from it:*], above: 0.2in)

#pagebreak()

== What You Did

You made a few hundred small decisions, 15 minutes at a time. Nobody handed you a finished room. You built these results one drawer and one shelf at a time.

#v(0.1in)
The house will not stay this way on its own, and that is fine. Use the monthly 15-minute reset and one in, one out from Part 4. They take little time, and they keep the work from piling up again.

#v(0.1in)
You can go further whenever you want to. The other books in this series take on a single area in depth: closets, the kitchen, the garage, paperwork and downsizing. If one area stayed hard for you, pick that book next. If you want to keep the house clean now that it's clear, the #emph[House Cleaning Checklist Planner] builds a routine in the same 15-minute blocks.

#v(0.3in)
#checklist("Before I close this book", (
  [I rated all 12 rooms again and took the after photos],
  [I filled in my scoreboard],
  [My Donate and Sell boxes have left the house],
  [My monthly reset day is on my calendar],
))

#v(0.2in)
== NOTES + WINS

#v(-0.2em)
*Notes*
#v(0.05in)
#_wk-lines(5, gap: 0.36in)
#v(0.2in)
*Wins*
#v(0.05in)
#_wk-lines(5, gap: 0.36in)
