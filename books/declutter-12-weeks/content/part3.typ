// Part 3 — 14 paginas. Reusa helpers _wk-* de wk01.typ.
//  p1 intro | p2 guia onde vender/doar | p3 recibos e Form 8283
//  p4-8 Sell Tracker (5 pgs) | p9-13 Donation Log (5 pgs) | p14 totais

#let _p3-sell-rows = 22
#let _p3-don-rows = 20

#let _p3-sell-page(n) = {
  set par(first-line-indent: 0em)
  if n == 1 {
    [== Sell Tracker]
    v(-0.3em)
    [Log each item the day you list it. Come back to fill in the sold price and the date. Add the sold prices at the bottom of the page, then carry the running total forward.]
    v(0.05in)
  } else {
    text(size: 1.2em, weight: "bold")[Sell Tracker, page #n of 5]
    v(0.1in)
  }
  _wk-table(
    (2.2fr, 1.5fr, 0.9fr, 0.9fr, 1.3fr),
    ([Item], [Where listed], [Asking price], [Sold price], [Date sold]),
    (),
    extra: if n == 1 { _p3-sell-rows - 2 } else { _p3-sell-rows },
    y: 12pt,
  )
  v(0.12in)
  text(size: 0.95em)[*Total sold on this page:* \$ #_wk-blank(0.9in) #h(0.3in) *Running total:* \$ #_wk-blank(0.9in)]
}

#let _p3-don-page(n) = {
  set par(first-line-indent: 0em)
  if n == 1 {
    [== Donation Log]
    v(-0.3em)
    [Log each donation when you drop it off, and ask for a receipt. Write the fair market value, meaning what the item would sell for in its current used condition. Then add up the page.]
    v(0.05in)
  } else {
    text(size: 1.2em, weight: "bold")[Donation Log, page #n of 5]
    v(0.1in)
  }
  _wk-table(
    (2fr, 1fr, 0.95fr, 1.6fr, 0.85fr),
    ([Item], [Condition], [Fair market value], [Organization], [Receipt kept]),
    (),
    extra: if n == 1 { _p3-don-rows - 2 } else { _p3-don-rows },
    y: 12pt,
  )
  v(0.12in)
  text(size: 0.95em)[*Value on this page:* \$ #_wk-blank(0.9in) #h(0.3in) *Running total:* \$ #_wk-blank(0.9in)]
}

= Part 3 — Where It All Went: Selling and Donating

By now you have sorted a whole house into four boxes. This part is where you write down what happened to the Sell and Donate boxes. It takes a few minutes each time, and it pays off in three ways.

#v(0.05in)
- *You see the result.* A running total of money earned and value donated is a plain record of the work you did.
- *You learn what is worth the effort.* Listing takes time. An asking price next to a sold price shows you which items were worth it.
- *You have paperwork when you need it.* If you itemize your donations on your taxes, a written log and your receipts make that much easier.

#v(0.1in)
Every week from Week 1 to Week 12 pointed you here. Anything worth at least your sell threshold from Week 0 goes in the Sell Tracker. Everything that went to a charity goes in the Donation Log. Leftovers from a garage sale move from the Sell Tracker to the Donation Log.

#v(0.1in)
#checklist("Before you start Part 3", (
  [I know my sell threshold from Week 0],
  [I have a folder or envelope for donation receipts],
  [I keep this book near the boxes, with a pencil],
  [I will log items when they leave the house, not weeks later],
))

#v(0.1in)
#_wk-field([*My sell threshold:* \$], above: 0.1in)
#_wk-field([*The day I will sit down to log the Sell box:*], above: 0.15in)
#_wk-field([*Where I keep my donation receipts:*], above: 0.15in)

#pagebreak()

== Where to Sell, Where to Donate

Match the item to the kind of place that handles it well. These are channel types, not recommendations. What is available depends on where you live, so call or check first.

#v(0.1in)
#let _g(a, b, c) = (text(weight: "bold", a), text(size: 0.92em, b), text(size: 0.92em, c))
#table(
  columns: (0.75fr, 1.4fr, 1.4fr),
  stroke: 0.5pt + luma(140),
  inset: (x: 7pt, y: 12pt),
  align: left + horizon,
  table.header(_wk-head[Item type], _wk-head[Where it can sell], _wk-head[Where it can go]),
  .._g([Clothes], [Local consignment shop. Online marketplace or resale app. Garage sale.], [Thrift store. Charity shop. Shelter or clothing closet. Clean, wearable items only.]),
  .._g([Furniture], [Local online listing or community group, buyer picks up. Consignment store. Garage sale.], [Charity that takes furniture. Some will pick up. Ask about size and condition rules first.]),
  .._g([Electronics], [Online marketplace. Local listing. Trade-in program from a manufacturer or store.], [Charities that take working items. Electronics recycling for anything broken or old.]),
  .._g([Books], [Used bookstore. Online marketplace. Garage sale.], [Public library (ask about donation rules). Schools, charity shops, little free libraries.]),
  .._g([Building materials], [Local online listing. Garage sale, for tools and small lots.], [Nonprofit reuse store for building materials. Some take donations from homeowners.]),
)

#v(0.15in)
#text(size: 0.92em)[*Good to know.* Call before you load the car, because donation sites can turn items away. Paint, chemicals, batteries and old electronics may need special handling, so check your local household hazardous waste guidelines. Fees and rules vary. A well-known online marketplace or national thrift chain is an example of a channel type, not a pick.]

#v(0.15in)
#_wk-field([*Where I will sell first:*], above: 0.1in)
#_wk-field([*Where I will donate first:*], above: 0.15in)

#pagebreak()

== Receipts and Form 8283

This page is general information from the IRS, not tax advice. Rules change, and your situation is your own.

#v(0.05in)
- *Keep a receipt for every donation.* Write the date, the organization and a description of what you gave. Drop-off boxes often give no receipt, so make your own note at the time.
- *\$250 or more.* For a contribution of \$250 or more, the IRS requires a written acknowledgment from the charity.
- *Good used condition.* Donated clothing and household items generally need to be in good used condition or better to be deductible.
- *Fair market value.* That means what a buyer would pay for the item in its current condition. The IRS explains how to figure it in Publication 561, Determining the Value of Donated Property.
- *More than \$500 in noncash gifts.* If your deduction for all noncash contributions is more than \$500, you generally file Form 8283 with your return. Items worth more than \$5,000 have extra rules.

#v(0.1in)
#text(size: 0.92em)[Look up the current details at irs.gov: Form 8283 and its instructions, Publication 526 (Charitable Contributions) and Publication 561. Check with a tax professional before you file.]

#v(0.1in)
#checklist("My receipts checklist", (
  [I have a receipt or written note for every donation in the Donation Log],
  [I wrote a description and date on each one],
  [I kept the acknowledgment for any gift of \$250 or more],
  [I added up my noncash donations and compared the total to \$500],
  [I talked to a tax professional if I am not sure],
))

#v(0.1in)
#_wk-field([*Total noncash donations so far:* \$], above: 0.1in)
#_wk-field([*Questions for my tax professional:*], above: 0.15in)
#_wk-lines(2, gap: 0.34in)

#pagebreak()

#for i in range(1, 6) [
  #_p3-sell-page(i)
  #pagebreak()
]

#for i in range(1, 6) [
  #_p3-don-page(i)
  #pagebreak()
]

== Part 3 Totals

Add the page totals from the Sell Tracker and the Donation Log. Carry these numbers to the Conclusion.

#v(0.1in)
#_wk-table(
  (1.4fr, 1fr),
  ([Sell Tracker], [Total sold]),
  ([Page 1], [Page 2], [Page 3], [Page 4], [Page 5]),
  extra: 0, y: 11pt,
)
#v(0.1in)
#text(size: 0.95em)[*All sold:* \$ #_wk-blank(1in) #h(0.3in) *Items sold:* #_wk-blank(0.6in)]

#v(0.25in)
#_wk-table(
  (1.4fr, 1fr),
  ([Donation Log], [Value donated]),
  ([Page 1], [Page 2], [Page 3], [Page 4], [Page 5]),
  extra: 0, y: 11pt,
)
#v(0.1in)
#text(size: 0.95em)[*All donated:* \$ #_wk-blank(1in) #h(0.3in) *Items donated:* #_wk-blank(0.6in)]

#v(0.25in)
#_wk-field([*What sold better than I expected:*], above: 0.1in)
#_wk-field([*Who received my donations:*], above: 0.15in)
