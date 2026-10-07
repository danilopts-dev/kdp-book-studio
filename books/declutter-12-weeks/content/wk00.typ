// Week 0 — 5 paginas: (1) orientacao, (2) notas dos comodos, (3) data/horario/valor minimo + regra das quatro caixas,
// (4) o que ter a mao, (5) anotacoes + conferencia. Lista de comodos = mesma da Conclusion (Week 1-12).

#let _w0-rule = _wk-rule
#let _w0-field(label, above: 0.32in) = block(above: above, width: 100%,
  [#label #box(width: 1fr, height: 0.2in, stroke: (bottom: _w0-rule))])
#let _w0-blank(w) = box(width: w, height: 0.2in, stroke: (bottom: _w0-rule))
#let _w0-lines(n, gap: 0.36in) = stack(spacing: gap, ..range(n).map(_ => line(length: 100%, stroke: 0.5pt + luma(160))))
#let _w0-dot(n) = box(width: 1.25em, height: 1.25em, radius: 50%, stroke: _w0-rule, baseline: 0.3em,
  align(center + horizon, text(size: 0.72em, str(n))))
#let _w0-box = _wk-box
#let _w0-rooms = (
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

= Week 0 — Walk Through Your Home Before You Touch Anything

Before you open a single drawer, take one slow walk through your home with this book and a pencil. Go room by room and don't pick anything up. You are looking at each space the way a visitor would, and giving it an honest number from 1 to 5. This book follows a typical home layout. Yours may differ, with more bedrooms, no garage or a shared space, so use the closest week for each space and adapt the pages to fit your home.

Those numbers matter more than they seem to right now. In Week 12 you will rate the same rooms again, and the gap between the two sets of scores is your proof that 12 weeks of 15-minute blocks did something, which is easy to forget in the middle of a messy Tuesday. Take a photo of each room from the doorway too. Nobody has to see them but you.

After the walk, make three practical choices: the day you start, the 15 minutes you will protect each day, and the dollar amount below which an item goes to Donate instead of Sell. Pick a time that already exists in your day, such as right after the morning coffee or while dinner is in the oven. A slot that depends on having a free moment rarely survives the first busy week.

Last, gather what you need from around the house. Nothing on the list costs money, and if you don't have something, skip it and use what you do have.

#v(0.3in)
#block(stroke: 1pt + luma(120), inset: 14pt, radius: 4pt, width: 100%, breakable: false)[
  #text(weight: "bold")[Week 0 has no daily tasks. Four things to finish, in one or two sittings:]
  #v(0.2em)
  #set enum(spacing: 0.8em)
  + Rate all 12 rooms and take the before photos.
  + Write down your start date and your 15-minute slot.
  + Set your sell threshold.
  + Gather the bags, boxes and labels.
]

#pagebreak()

== Rate Your Rooms

Walk through each space and circle one number. Use 2 or 4 if the room falls between two descriptions. Trust your first reaction. Check the box once you have taken the before photo from the doorway, and remember where you stood so you can take the after photo from the same spot in Week 12.

#v(0.1in)
#block(breakable: false, width: 100%)[
  #set text(size: 0.92em)
  #grid(columns: (auto, 1fr), column-gutter: 8pt, row-gutter: 6pt,
    [#_w0-dot(1)], [*Calm.* Easy to use, and everything has a place.],
    [#_w0-dot(3)], [*Crowded.* You can use it, but it takes effort to find or put away things.],
    [#_w0-dot(5)], [*Stuck.* You avoid the room, or it can't be used the way it was meant to be.],
  )
]

#v(0.15in)
#_styled-table(
  columns: (0.85in, 1fr, 1.95in, 0.85in),
  inset: (x: 6pt, y: 9pt),
  align: (left + horizon, left + horizon, center + horizon, center + horizon),
  table.header(
    text(size: 0.8em, weight: "bold")[Week],
    text(size: 0.8em, weight: "bold")[Room],
    text(size: 0.8em, weight: "bold")[Rating (1 to 5)],
    text(size: 0.8em, weight: "bold")[Before photo],
  ),
  ..for (wk, room) in _w0-rooms {
    (
      text(size: 0.9em, wk),
      text(size: 0.9em, room),
      [#_w0-dot(1) #h(2pt) #_w0-dot(2) #h(2pt) #_w0-dot(3) #h(2pt) #_w0-dot(4) #h(2pt) #_w0-dot(5)],
      _w0-box,
    )
  },
)

#v(0.1in)
#align(right, [*Add up your 12 ratings:* #box(width: 0.7in, height: 0.9em, stroke: (bottom: _w0-rule)) / 60])

#pagebreak()

== Pick Your Start Date and Your 15 Minutes

Tie the 15 minutes to something you already do, like the morning coffee, school drop-off or dinner cleanup.

#block(above: 0.3in)[*Start date:* #_w0-blank(0.6in) / #_w0-blank(0.6in) / #_w0-blank(0.9in)]
#_w0-field([*My daily 15-minute slot:*])
#_w0-field([*I will do it right after:*])
#_w0-field([*Backup time if that falls through:*])
#_w0-field([*Who will help or cheer me on:*])

#v(0.25in)
#block(stroke: 1.5pt, inset: 16pt, radius: 4pt, width: 100%, breakable: false)[
  #text(size: 1.5em, weight: "bold")[My sell threshold: \$ #_w0-blank(1.3in)]
  #v(0.5em)
  Items worth less than this go to Donate, not Sell. Items worth this much or more are worth the time it takes to list them and meet a buyer. Some people pick \$20, others \$50 or more. You can change it later, but set it now so you aren't debating every object.
]

#v(0.1in)
== When You Can't Decide

Go through these steps, in order, for every item you pick up. There is no "maybe" box.

#v(0.3em)
#_styled-table(head: false,
  columns: (2.2em, 1.2fr, 1fr),
  inset: (x: 7pt, y: 8pt),
  align: (center + horizon, left + horizon, left + horizon),
  [*1*], [Is it broken, expired, stained or missing its parts?], [*Toss* it. Recycle what you can.],
  [*2*], [If this were gone tomorrow, would I go out and buy it again?], [*Yes:* Keep. It goes back in the room, in a place where you can find it.],
  [*3*], [If the answer is no, or "I'd have to think about it": is it worth my sell threshold or more?], [*Yes:* Sell. *No:* Donate.],
)

#pagebreak()

== What to Have on Hand

Collect these before Week 1. Everything here is something most homes already have. Don't buy anything new for this book.

#v(0.15in)
#checklist(none, (
  [Four boxes or heavy-duty trash bags, one each for Keep, Donate, Sell and Toss],
  [Tape and a marker to label each one],
  [A pencil or pen that lives with this book],
  [A timer (the one on your phone works) set to 15 minutes],
  [Extra trash bags and a recycling bin nearby],
  [A rag or paper towels for wiping shelves as you empty them],
  [A phone or camera for before photos],
  [A few sticky notes for things you need to look up, like what something might sell for],
))

#v(0.3in)
== Where the Boxes Will Live

Pick spots now so you aren't deciding while you're holding a stack of towels.

#_w0-field([*The Keep box waits here between sessions:*])
#_w0-field([*The Donate box lives by (the door, the car, the garage):*])
#_w0-field([*Sell items wait here until I list them:*])
#_w0-field([*The day I take the Donate box out of the house:*])

#pagebreak()

== First Walk-Through Notes

#_w0-field([*The room I'm dreading most:*], above: 0.2in)
#_w0-field([*The room I expect to be easiest:*])
#_w0-field([*What I want from these 12 weeks:*])
#v(0.1in)
#_w0-lines(2)

#v(0.25in)
== NOTES + WINS

#_w0-lines(6)

#v(0.3in)
== Week 0 Is Done When

#checklist(none, (
  [All 12 rooms are rated and I added up the total],
  [The before photos are taken],
  [My start date and 15-minute slot are written down],
  [My sell threshold is set],
  [My supplies are gathered and the boxes have a home],
))
