// Week 3 — 7 paginas. Layout semanal padrao (helpers _wk-* definidos em wk01.typ).

= Week 3 — Kitchen, Part One: Counters, Pantry and Fridge

The kitchen is the room you use the most, so it collects the most. To keep it from feeling like too much, it is split across two weeks. This week covers surfaces and food: counters, pantry, fridge and freezer. Week 4 handles cabinets, gadgets and containers.

The goal is simple: empty counters. Keep out only what you touch every day, like the coffee maker or the dish soap. Everything else needs a home in a cabinet or goes into a box.

Food is a little different. Nobody feels guilty about tossing a stale cracker, but many of us hesitate over food that is still good. Sealed, unexpired food you won't eat can go to Donate. Call your local food bank first and ask what they accept. Open packages and anything past its date go to Toss.

Work one zone a day. Take everything out, wipe the shelf and sort as you put things back.

#v(0.05in)
== This Week, 15 Minutes a Day

#_wk-daily((
  [*Counters, part one.* Clear the main counter. Put back only what you use every day.],
  [*Counters, part two.* Small appliances, the paper pile, the fruit bowl and the corner nobody looks at.],
  [*Pantry, top shelves.* Take everything out. Check the dates. Set aside what has expired.],
  [*Pantry, lower shelves.* Sort, and group duplicates together.],
  [*Fridge.* Shelves, door and drawers. Toss what has expired or gone off.],
  [*Freezer and spices.* Anything with frost, no label or no date goes. Check the spice dates.],
  [*Out the door.* Take out the Toss and Donate boxes, bring the food donation to a drop-off, and count.],
))

#pagebreak()

== Map Your Kitchen Zones

Write in each counter, shelf and storage spot you will sort this week. Choose a day for it and check the boxes as you go.

#v(0.15in)
#_styled-table(
  columns: (1fr, 3.2em, 4.6em, 4.2em, 5.2em),
  inset: (x: 6pt, y: 11pt),
  align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  table.header(_wk-head[Space], _wk-head[Day], _wk-head[Emptied], _wk-head[Sorted], _wk-head[Back in place]),
  ..(
    [Main counter],
    [Other counters and the corner],
    [Pantry, top shelves],
    [Pantry, lower shelves],
    [Refrigerator shelves and door],
    [Refrigerator drawers],
    [Freezer],
    [Spice rack or spice drawer],
    [],
    [],
    [],
    [],
  ).map(s => (s, [], _wk-box, _wk-box, _wk-box)).flatten(),
)

#v(0.2in)
#_wk-field([*The space I'm dreading most:*], above: 0.1in)
#_wk-field([*What I want my counters to look like by Day 7:*])

#pagebreak()

== Clear the Counters

Put everything that lives on your counters in the list below. Then decide if it earns its place there. A good test: did you use it in the last week?

#v(0.15in)
#_wk-table(
  (1fr, 4.4em, 4.4em, 1.7in),
  ([On my counter], [Use daily?], [Stays out], [If not, it goes to]),
  (),
  extra: 12, y: 11pt,
)

#v(0.2in)
#_wk-field([*The one thing I'm surprised was out:*], above: 0.1in)
#block(above: 0.2in)[
  #checklist(none, (
    [Counters are wiped and clear except for my daily items],
    [Mail and loose paper have a spot (paper gets sorted in Week 9)],
    [Everything I use daily has a place to come back to],
  ))
]

#pagebreak()

== Pantry: Check, Count, Combine

Go through each shelf and look at the dates. Most are "best if used by" or "use by" dates, which tell you about quality, not safety. When a date is past, look at the food: if it smells, looks or tastes off, or the package is open and stale, let it go. Write down duplicates so you stop buying a fourth jar of the same thing.

#v(0.15in)
#_wk-table(
  (1fr, 3.8em, 4.2em, 3.8em, 4.4em),
  ([Pantry item], [Found], [Expired], [Keep], [Donate]),
  (
    [Canned vegetables and beans],
    [Soup and broth],
    [Pasta and rice],
    [Cereal and oatmeal],
    [Baking supplies],
    [Sauces and condiments],
    [Snacks],
    [Oils and vinegars],
    [Coffee, tea and drinks],
  ),
  extra: 3, y: 10.5pt,
)

#v(0.2in)
#_wk-field([*Something I have three or more of:*], above: 0.1in)
#_wk-field([*Something I bought and never opened:*])
#v(0.05in)
#text(size: 0.8em, style: "italic")[Apart from infant formula, federal law does not require food makers to put a date on their products, so a date is usually the maker's estimate of quality. For more on food date labels, see the U.S. Department of Agriculture Food Safety and Inspection Service (fsis.usda.gov).]

#pagebreak()

== Fridge, Freezer and the Food Bank

Go shelf by shelf. Toss what is moldy, smells off or is unrecognizable. Whatever is still good but you know you won't eat, such as sealed, unexpired pantry items, can go to a food bank. Fresh and opened food usually can't be donated.

#v(0.1in)
#_wk-table(
  (1fr, 1.7in, 3.6em, 3.6em),
  ([Fridge or freezer item], [Date or how old], [Keep], [Toss]),
  (),
  extra: 8, y: 11pt,
)

#v(0.2in)
*Before you donate food*
#v(0.05in)
#checklist(none, (
  [I called or checked the website of a food bank or pantry near me],
  [I asked what they accept and when they take donations],
  [Everything I'm giving is sealed and within its date],
))
#_wk-field([*Food bank or pantry I'll use:*], above: 0.15in)
#block(above: 0.2in)[*The day I'll drop it off:* #_wk-date]

#pagebreak()

== Where It's Going This Week

Decide where each box is headed while the room is fresh in your mind. A box that has a destination actually leaves the house.

#_wk-where(
  [Sealed, unexpired food for a food bank, plus working dishes and small appliances worth less than your sell threshold. Check what the place accepts before you go.],
  [Small appliances in good shape. Only what is worth at least your sell threshold from Week 0.],
  [Expired and opened food, stale spices, freezer-burned items and broken gadgets. Recycle the packaging you can.],
)

#pagebreak()

#_wk-count()
