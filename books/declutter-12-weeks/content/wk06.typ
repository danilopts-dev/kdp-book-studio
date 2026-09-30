= Week 6 — Your Bedroom

The bedroom is the room you see first in the morning and last at night, so what sits in it gets noticed more than you think. The nightstand drawer that holds six pens and no paper, the box pushed under the bed "for now," the chair that has turned into a second closet: none of it was a decision. It just landed.

This week you clear the spots where things pile up. Take them one at a time: the nightstands, the space under the bed, the clothes chair, the dresser top and the floor and corners. Sort every item into the four boxes: Keep, Donate, Sell, Toss. Clothes get their own week, so this week you only deal with the ones sitting out of place. Anything you pull from under the bed that you haven't seen in a year deserves a hard look.

You also get a page to describe how you want the room to look. Write it down before you start, and check it again on Day 7.

#v(0.05in)
== This Week, 15 Minutes a Day

#_wk-daily((
  [*First nightstand.* Empty the top and the drawer. Keep only what you use at night.],
  [*Second nightstand or bedside table.* Same thing. If you have only one, start the dresser top.],
  [*Under the bed.* Pull everything out, look at each item and sort it. Log it on page 3 of this week.],
  [*The clothes chair.* Sort the pile into clean, dirty and "not sure." Use page 4 of this week.],
  [*Dresser top and windowsill.* Trays, jewelry dishes, loose change, receipts and old perfume bottles.],
  [*Floor, corners and walls.* Baskets, shoes, books, décor and anything that landed and stayed.],
  [*Out the door.* Take out the Toss and Donate boxes. Look at page 5 of this week and write down what you see. Count.],
))

#pagebreak()

== Map Your Bedroom

Every bedroom collects things in its own places. Write in yours, choose a day for each and check the boxes as you go.

#v(0.15in)
#table(
  columns: (1fr, 3.2em, 4.6em, 4.2em, 5.2em),
  stroke: 0.5pt + luma(140),
  inset: (x: 6pt, y: 11pt),
  align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  table.header(_wk-head[Space], _wk-head[Day], _wk-head[Emptied], _wk-head[Sorted], _wk-head[Back in place]),
  ..(
    [First nightstand (top and drawer)],
    [Second nightstand or bedside table],
    [Under the bed],
    [The clothes chair],
    [Dresser top],
    [Windowsill or shelf],
    [Floor and corners],
    [Wall hooks and door],
    [],
    [],
    [],
    [],
  ).map(s => (s, [], _wk-box, _wk-box, _wk-box)).flatten(),
)

#v(0.2in)
#_wk-field([*The spot that bothers me most:*], above: 0.1in)
#_wk-field([*Something I've walked around for months:*])

#pagebreak()

== Nightstands and Under the Bed

Put here what you found. The nightstand should hold what you reach for at night and nothing else. Under the bed should hold only things you can name.

#v(0.15in)
#_wk-table(
  (1fr, 4em, 4em, 4em, 4em),
  ([What I found], [Keep], [Donate], [Sell], [Toss]),
  (
    [Nightstand: books and magazines],
    [Nightstand: pens, notepads, coins],
    [Nightstand: cords and chargers I use],
    [Nightstand: lotions, lip balm, loose items],
    [Under the bed: boxes and bins],
    [Under the bed: shoes and bags],
    [Under the bed: bedding and blankets],
    [Under the bed: things I can't name],
  ),
  extra: 4, y: 10.5pt,
)

#v(0.2in)
#_wk-field([*The one thing I'll keep within reach of the bed:*], above: 0.1in)
#_wk-field([*A box I hadn't opened in over a year held:*])

#pagebreak()

== The Clothes Chair

The chair is not the problem. It is where "I'll decide later" piles up. Go through the pile one item at a time and give each piece a home. The full wardrobe decisions wait for Week 7.

#v(0.15in)
#_wk-table(
  (1fr, 3.6em, 3.6em, 1.7in),
  ([Item on the chair], [Clean], [Dirty], [Where it belongs]),
  (
    [Worn once, not dirty enough to wash],
    [Clean clothes never put away],
    [Clothes waiting to be washed],
    [Pajamas and robes],
    [Items to try on before deciding],
    [Things that need mending],
  ),
  extra: 5, y: 10.5pt,
)

#v(0.2in)
#checklist(none, (
  [The chair is empty, or it holds only what I wore today],
  [Dirty clothes are in the hamper or the laundry room],
  [Anything I'm "not sure" about is in a bag marked for Week 7],
))
#_wk-field([*Why things land on the chair:*], above: 0.25in)
#_wk-lines(2, gap: 0.34in)

#pagebreak()

== How I Want My Bedroom to Look

Describe how you want the room to look and feel, then compare it with what you see on Day 7. Write what you would notice when you walk in: what's on the surfaces, what's on the floor, what's in view from the bed.

#v(0.1in)
#block(stroke: 1pt + luma(120), inset: 12pt, radius: 4pt, width: 100%, breakable: false)[
  *Right now I see:*
  #v(0.1in)
  #_wk-lines(4, gap: 0.34in)
]
#v(0.15in)
#block(stroke: 1pt + luma(120), inset: 12pt, radius: 4pt, width: 100%, breakable: false)[
  *I want to see:*
  #v(0.1in)
  #_wk-lines(4, gap: 0.34in)
]

#v(0.15in)
#checklist(none, (
  [The nightstands hold only what I use each night],
  [Nothing is stored under the bed that I can't name],
  [Every surface has at most three things on it],
  [I like what I see from the bed],
))
#_wk-field([*One thing that still needs to move out:*], above: 0.25in)
#_wk-field([*Day 7 date:* #_wk-date], above: 0.15in)

#pagebreak()

== Where It's Going This Week

Decide where each box is headed while the room is fresh in your mind. A box that has a destination actually leaves the house.

#_wk-where(
  [Books, unopened toiletries, bedding and décor in good shape. Check what the place accepts before you go.],
  [Furniture, lamps, frames and anything worth at least your sell threshold from Week 0.],
  [Broken items, dried-out pens, worn pillows, old receipts and anything you can't donate. Recycle what you can.],
)

#pagebreak()

#_wk-count()
