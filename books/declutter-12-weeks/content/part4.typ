// Part 4 — 6 paginas. Reusa helpers _wk-* de wk01.typ.
//  p1 intro | p2-3 tracker mensal (meses 1-6, 7-12) | p4 Keep for now | p5 one in, one out | p6 handoff

#let _p4-rooms = (
  [Bathroom],
  [Entryway and coat closet],
  [Kitchen part one: counters, pantry, fridge],
  [Kitchen part two: cabinets, gadgets, containers],
  [Living room],
  [Bedroom],
  [Closet],
  [Kids' rooms and toys (or hobby room)],
  [Home office and paper pile],
  [Linen closet, laundry, cleaning supplies],
  [Garage, basement, attic, storage],
  [Sentimental things],
)

#let _p4-reset-page(first, last) = {
  set par(first-line-indent: 0em)
  if first == 1 {
    [== Monthly 15-Minute Reset Tracker]
    v(-0.3em)
    [Once a month, set a timer for 15 minutes in one room. Put back what drifted, move anything new into Keep, Donate, Sell or Toss, and check the box. Months are undated, so start at Month 1 whenever you finish this book.]
    v(0.1in)
  } else {
    text(size: 1.2em, weight: "bold")[Monthly 15-Minute Reset Tracker, continued]
    v(0.1in)
  }
  let cols = last - first + 1
  _styled-table(
    columns: (2.6fr,) + (0.6fr,) * cols,
    inset: (x: 5pt, y: 14pt),
    align: (left + horizon,) + (center + horizon,) * cols,
    table.header([#_wk-head[Room]], ..range(first, last + 1).map(m => _wk-head[Month #m])),
    ..for r in _p4-rooms {
      (text(size: 0.88em, r), ..range(cols).map(_ => align(center, _wk-box)))
    },
  )
  v(0.12in)
  if first == 1 {
    text(size: 0.95em)[*My reset day each month:* #_wk-blank(1.8in)]
  } else {
    text(size: 0.95em)[*Resets done in all 12 months:* #_wk-blank(0.6in) #h(0.2in) / 144]
  }
}

= Part 4 — Keep It Clear

#v(0.3in)
You did the hard part. Every room has been sorted, and the boxes have left the house. Now comes the part that keeps it that way.

#v(0.05in)
Houses slide back slowly. A few bags land by the door, a drawer fills up, a counter collects mail. None of it feels like much on the day, and it adds up. Part 4 gives you three small habits to stop that.

#v(0.1in)
- *The monthly 15-minute reset.* One 15-minute block per room, once a month, tracked on the next two pages.
- *A second look at "Keep for now."* Anything you were unsure about in Weeks 1 to 12 gets a fresh decision at a reset.
- *One in, one out.* When something new comes into the house, something of the same kind goes out.

#v(0.1in)
You do not need a new system. You already know how to make a decision in 15 minutes. This part only asks you to keep doing it, a little at a time.

#v(0.1in)
#checklist("Before you start Part 4", (
  [All 12 weeks are done, or I have decided which ones to skip],
  [I know which day of the month works for my reset],
  [I have a pencil and a timer],
  [The Keep / Donate / Sell / Toss boxes are still where I left them, or I know where they are going],
))

#v(0.1in)
#_wk-field([*Today's date:* #_wk-date], above: 0.1in)
#_wk-field([*The room I will reset first:*], above: 0.15in)
#_wk-field([*The day of the month I will reset:*], above: 0.15in)
#_wk-field([*Why I want to keep my house clear:*], above: 0.15in)
#_wk-lines(2, gap: 0.36in)

#pagebreak()

#_p4-reset-page(1, 6)

#pagebreak()

#_p4-reset-page(7, 12)

#pagebreak()

== Revisit "Keep for now"

Some things were not a clear yes or no. The rule was simple: when you truly could not decide, it stayed in Keep for now, and you would look again at a 15-minute reset. This is that page.

#v(0.1in)
Ask the same question you asked in Week 0: *If this were gone tomorrow, would I go out and buy it again?* If yes, it stays in Keep and goes back to its place. If no, it goes to Donate, Sell or Toss, using your sell threshold.

#v(0.12in)
#_wk-table(
  (2fr, 1.1fr, 0.6fr, 0.6fr, 0.6fr, 0.6fr),
  ([Item I kept for now], [Room], [Keep], [Donate], [Sell], [Toss]),
  (),
  extra: 14,
  y: 12pt,
)

#v(0.15in)
#checklist(none, (
  [I asked the question for every item on this list],
  [Anything that changed to Donate, Sell or Toss went into the right box],
  [Sell items were added to the Sell Tracker, Donate items to the Donation Log],
))

#v(0.1in)
#_wk-field([*Next time I will look at this page again:* #_wk-date], above: 0.1in)

#pagebreak()

== One In, One Out

The rule is short. When something new comes into the house, something of the same kind goes out. A new pair of shoes means one old pair leaves. A new mug means one mug goes. A new book means one book goes.

#v(0.1in)
Out means it leaves the house. It goes into Donate, Sell or Toss. It does not go into a bag in the closet.

#v(0.1in)
- *Same kind.* Swap like for like, so a jacket replaces a jacket.
- *Same week.* Do it within a week, before the new item settles in.
- *Gifts count.* You can say thank you and still let something else go.
- *Small things are your call.* Decide ahead of time whether pens and greeting cards count, and stick to it.

#v(0.12in)
#text(size: 1.1em, weight: "bold")[One In, One Out Log]
#v(0.05in)
#_wk-table(
  (1.6fr, 1.6fr, 1fr, 0.8fr),
  ([What came in], [What went out], [Where it went], [Done]),
  (),
  extra: 15,
  y: 12pt,
)

#pagebreak()

== What Comes Next

Your house is clear, and you have a way to keep it that way. The next step is to keep it clean. That is where the #emph[House Cleaning Checklist Planner] picks up.

#v(0.1in)
Decluttering and cleaning work together. Clear surfaces are much quicker to wipe. Because you made a place for what you kept, the #emph[House Cleaning Checklist Planner] routine can move room by room in 15-minute blocks, without stopping to move piles.

#v(0.1in)
Use this table to plan where the routine starts. Pick a day and a time for each room, and check it off once the room is in your routine.

#v(0.1in)
#_styled-table(
  columns: (2.6fr, 1fr, 1fr, 0.6fr),
  inset: (x: 6pt, y: 6pt),
  align: (left + horizon, center + horizon, center + horizon, center + horizon),
  table.header(_wk-head[Room], _wk-head[Day], _wk-head[Time], _wk-head[Set]),
  .._p4-rooms.map(r => (text(size: 0.88em, r), [], [], align(center, _wk-box))).flatten(),
)

#v(0.02in)
#checklist("Before I pick up the routine", (
  [My surfaces are clear and everything has a place],
  [My cleaning supplies are gathered from Week 10],
  [I picked a day for my monthly 15-minute reset],
  [I know my one in, one out rule],
))

#_wk-field([*The day I will start my cleaning routine:* #_wk-date], above: 0.1in)
#_wk-field([*My reset day each month:*], above: 0.15in)
#_wk-field([*One room I want to keep clear above all:*], above: 0.15in)
