// Week 2 — 7 paginas. Reusa helpers _wk-* definidos em wk01.typ (wk01 vem antes).

= Week 2 — The Entryway and Coat Closet

The entryway is the first thing you see when you come home and the last thing you pass on the way out. It is also where everything lands: coats, shoes, bags, keys, mail, the umbrella you used once. Because it is small and busy, clutter builds up here faster than almost anywhere else.

This week you will work through it one layer at a time: the coat closet first, then shoes, bags, small accessories and finally keys and mail. Take everything out of one space, put it on the floor or a table and sort it into the four boxes: Keep, Donate, Sell, Toss. Coats are a good one to watch. A coat nobody has worn in two winters is taking up room that a coat you wear needs.

The last step is the one that keeps the entryway clear. By Day 6 you will set up a landing zone: one spot for everything that comes into the house, so it stops spreading to the counter and the stairs. The pages ahead help you plan it. When the timer rings, stop and pick it up tomorrow.

#v(0.05in)
== This Week, 15 Minutes a Day

#_wk-daily((
  [*Coat closet, coats.* Take out every coat and jacket. Try on the ones you doubt. Sort.],
  [*Shoes.* Gather every pair from the entry, closet and doorway. Keep the pairs you wear. Sort the rest.],
  [*Bags, backpacks and totes.* Empty each one as you go. Keep only what you carry.],
  [*Hats, gloves, scarves and umbrellas.* Match up pairs. A single glove goes to Toss.],
  [*Keys and mail.* Sort the mail pile, then the key hooks, bowls and drawers.],
  [*Landing zone.* Choose the spot and set it up with the plan on page 5 of this week.],
  [*Out the door.* Take out the Toss and Donate boxes, and list anything for Sell. Count.],
))

#pagebreak()

== Map Your Entryway

Write in each space where things pile up by the door, choose a day for it and check the boxes as you go.

#v(0.15in)
#table(
  columns: (1fr, 3.2em, 4.6em, 4.2em, 5.2em),
  stroke: 0.5pt + luma(140),
  inset: (x: 6pt, y: 11pt),
  align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  table.header(_wk-head[Space], _wk-head[Day], _wk-head[Emptied], _wk-head[Sorted], _wk-head[Back in place]),
  ..(
    [Coat closet],
    [Shoe rack or floor by the door],
    [Hooks and pegs],
    [Bench or console table],
    [Bag and backpack spot],
    [Key hooks, bowls and trays],
    [Mail pile and paper spot],
    [Drawer or basket by the door],
    [],
    [],
    [],
    [],
  ).map(s => (s, [], _wk-box, _wk-box, _wk-box)).flatten(),
)

#v(0.2in)
#_wk-field([*The spot that collects the most stuff:*], above: 0.1in)
#_wk-field([*What I want the doorway to feel like on Day 7:*])

#pagebreak()

== Coats, Shoes and Bags

Write down what you have before you decide. Count one by one, then keep what you wear in a normal week. Seeing ten jackets on paper makes it easier to let a few go. In the last column, write where the extras are headed.

#v(0.15in)
#_wk-table(
  (1fr, 4em, 4em, 1.6in),
  ([Item], [Found], [Keep], [Extras go to]),
  (
    [Winter coats],
    [Light jackets and rain jackets],
    [Shoes I wear every week],
    [Boots],
    [Sandals and flip-flops],
    [Shoes that hurt or don't fit],
    [Handbags and purses],
    [Backpacks and tote bags],
    [Gym and travel bags],
    [Hats, gloves and scarves],
    [Umbrellas],
  ),
  extra: 3, y: 9.5pt,
)

#v(0.2in)
#_wk-field([*A coat or pair of shoes I kept for "someday":*], above: 0.1in)

#pagebreak()

== Keys, Mail and Paper

Keys and mail are small, but they are the reason a doorway never looks clear. Sort the pile once, then decide where each kind of thing will go from now on.

#v(0.15in)
#_wk-table(
  (1fr, 3.6em, 3.6em, 3.6em, 3.6em),
  ([What I found], [Keep], [Donate], [Sell], [Toss]),
  (
    [Keys I can't match to a lock],
    [Spare keys with no label],
    [Loose change and receipts],
    [Junk mail and flyers],
    [Catalogs and magazines],
    [Coupons and cards that have expired],
    [Bills and important papers],
    [Sunglasses, chargers, odds and ends],
  ),
  extra: 3, y: 10pt,
)

#v(0.2in)
#_wk-field([*Mail that needs an answer goes here:*], above: 0.1in)
#_wk-field([*Mail I can stop receiving (write what to cancel):*])
#_wk-field([*The day I'll sort mail every week:*])

#pagebreak()

== Plan Your Landing Zone

A landing zone is one place for everything that comes into your home: keys, mail, bags and the things you need when you leave. The goal is simple. If it comes in through the door, it has a spot by the door, and nothing else comes further in without a reason.

#v(0.1in)
#_wk-table(
  (1.5in, 1fr, 1fr),
  ([What lands here], [Where it goes], [Who uses it]),
  (
    [Keys],
    [Mail],
    [Bags and backpacks],
    [Everyday shoes],
    [Coats worn this week],
    [Outgoing items (returns, donations)],
  ),
  extra: 2, y: 11pt,
)

#v(0.15in)
#_wk-field([*The spot I picked for my landing zone:*], above: 0.1in)
#_wk-field([*Something that will stay out of the entry:*])

#v(0.2in)
#checklist(none, (
  [Every member of the household knows where their things go],
  [Keys have one hook, bowl or tray],
  [The mail has a place, and I picked a day to sort it],
  [The floor by the door is clear],
))

#pagebreak()

== Where It's Going This Week

Decide where each box is headed while the room is fresh in your mind. A box that has a destination actually leaves the house.

#_wk-where(
  [Coats, boots and bags in good shape, and pairs of gloves. Check what the place accepts before you go.],
  [Coats, bags and shoes worth at least your sell threshold from Week 0. Photograph them in daylight.],
  [Worn-out shoes, single gloves, broken umbrellas, expired coupons and junk mail. Recycle paper and what you can.],
)

#pagebreak()

#_wk-count()
