// Week 1 — 7 paginas. LAYOUT SEMANAL (wk01-wk12): helpers _wk-* definidos em theme.typ.
//  p1 orientacao (~200 palavras) + "This Week, 15 Minutes a Day" (_wk-daily)
//  p2..p5 folhas do comodo (== titulos, _wk-table, _wk-field, checklist)
//  p6 "Where It's Going This Week" (_wk-where)
//  p7 "Keep / Donate / Sell / Toss Count" (_wk-count) + NOTES + WINS

// Helpers _wk-* agora vivem em books/declutter-12-weeks/theme.typ (tema visual do livro).

= Week 1 — The Bathroom: A Fast First Win

The bathroom is small, it has a door that closes, and almost nothing in it comes with a memory. That makes it a good place to start. Most of what you pick up will have an easy answer: the mascara from two summers ago, the hotel samples, the third bottle of the same shampoo, the cold medicine that expired before the cold did.

You will work one drawer or cabinet a day, so the whole room is done in a week and you never face all of it at once. Empty one space onto the counter, wipe it down and sort every item into the four boxes: Keep, Donate, Sell, Toss. Then put the Keep items back where you can reach them. Most bathroom things end up in Toss. A few, like unopened toiletries and towels in good shape, can go to Donate. Very little here is worth selling, so don't spend your 15 minutes on listings.

Expired medicines and old products need a couple of extra steps. The next pages walk you through them. When the timer rings, stop, even if you are halfway through a shelf, and pick it up again tomorrow. On the last page, write down your counts, however small. That is your first win.

#v(0.05in)
== This Week, 15 Minutes a Day

#_wk-daily((
  [*Counter and sink.* Clear everything off. Wipe the surface. Put back only what you used today.],
  [*Medicine cabinet or shelf.* Check the expiration date on every item and set aside what has expired or what you no longer need.],
  [*Under the sink.* Empty it, wipe it and sort.],
  [*Makeup, skin care and sunscreen.* Sort with the date rules on page 4 of this week.],
  [*Hair and tools.* Brushes, styling tools, hair products and the junk drawer of hair ties.],
  [*Shower, tub and towels.* Bottles, bath mats, towels and washcloths.],
  [*Out the door.* Take out the Toss and Donate boxes, and dispose of medicines (page 5 of this week). Count.],
))

#pagebreak()

== Map Your Bathroom

Every bathroom hides its clutter in different places. Write in each drawer, cabinet and shelf you have, choose a day for it and check the boxes as you go.

#v(0.15in)
#_styled-table(
  columns: (1fr, 3.2em, 4.6em, 4.2em, 5.2em),
  inset: (x: 6pt, y: 11pt),
  align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  table.header(_wk-head[Space], _wk-head[Day], _wk-head[Emptied], _wk-head[Sorted], _wk-head[Back in place]),
  ..(
    [Counter and sink],
    [Medicine cabinet or shelf],
    [Under the sink],
    [Makeup and skin care drawer],
    [Hair and tools drawer],
    [Shower and tub],
    [Towel shelf or linen area],
    [Behind the door or on the toilet tank],
    [],
    [],
    [],
    [],
  ).map(s => (s, [], _wk-box, _wk-box, _wk-box)).flatten(),
)

#v(0.2in)
#_wk-field([*The space I'm dreading most:*], above: 0.1in)
#_wk-field([*What I hope it looks like by Day 7:*])

#pagebreak()

== What the Bathroom Keeps

Count what you have before you decide. Seeing five of the same thing written down makes the decision easier. In the last column, write what you did with the extras.

#v(0.15in)
#_wk-table(
  (1fr, 4em, 4em, 1.6in),
  ([Item], [Found], [Keep], [Extras go to]),
  (
    [Toothbrushes and toothpaste tubes],
    [Bars and bottles of soap],
    [Shampoo and conditioner],
    [Body wash and lotion],
    [Razors and shaving supplies],
    [Hairbrushes and combs],
    [Towels and washcloths],
    [Bath mats],
    [Hotel and sample sizes],
    [First aid supplies],
  ),
  extra: 3, y: 10.5pt,
)

#v(0.2in)
#_wk-field([*Something I own two or more of that I didn't realize:*], above: 0.1in)

#pagebreak()

== Check the Date

Some things have a date on them, and some only have a rule of thumb. Use the table to decide, then log what you find below it.

#v(0.15in)
#_styled-table(
  columns: (1.15in, 1fr, 1.8in),
  inset: (x: 7pt, y: 8pt),
  align: (left + horizon, left + horizon, left + horizon),
  table.header(_wk-head[Item], _wk-head[What to check], _wk-head[Then]),
  [*Medicines* (prescription and over-the-counter)], [The expiration date printed on the label or package.], [Expired or no longer needed: see the disposal page. Unsure? Ask your pharmacist.],
  [*Sunscreen*], [A printed expiration date. U.S. rules require one, unless the product is stable for at least 3 years. No date means treat it as expired 3 years after you bought it.], [Expired or undated and old: Toss. Write the purchase date on new ones with a marker.],
  [*Makeup and skin care*], [No U.S. law requires an expiration date on cosmetics, so look for a date or open-jar symbol on the package. If it smells, looks or feels different than it used to, or you can't remember when you bought it, let it go.], [Toss. Write the open date on new ones with a marker.],
)
#v(0.05in)
#text(size: 0.8em, style: "italic")[This is general information, not medical advice. Sources: U.S. Food and Drug Administration (fda.gov).]

#v(0.2in)
#_wk-table(
  (1fr, 1.6in, 3.6em, 3.6em),
  ([Item I checked], [Date on it (or guess)], [Keep], [Toss]),
  (),
  extra: 8, y: 11pt,
)

#pagebreak()

== Getting Rid of Old Medicines

Don't toss pills in the trash loose, and don't flush them unless the label says to. The U.S. Food and Drug Administration (FDA) recommends these options, starting with take-back.

#v(0.1in)
#block(stroke: 1pt + luma(120), inset: 12pt, radius: 4pt, width: 100%, breakable: false)[
  *1. Use a drug take-back option when you can.* Many pharmacies, hospitals, clinics and police stations accept unused medicines. Some pharmacies sell or give out prepaid mail-back envelopes. The U.S. Drug Enforcement Administration also holds National Prescription Drug Take Back events.
]
#v(0.1in)
#block(stroke: 1pt + luma(120), inset: 12pt, radius: 4pt, width: 100%, breakable: false)[
  *2. If there's no take-back option, most medicines can go in the household trash.* Take the medicine out of its container and mix it with something unappealing, such as used coffee grounds, dirt or cat litter. Seal the mixture in a zip bag, a can or another container that won't leak. Throw it away.
]
#v(0.1in)
#block(stroke: 1pt + luma(120), inset: 12pt, radius: 4pt, width: 100%, breakable: false)[
  *3. A short list of medicines is meant to be flushed.* Check the FDA flush list (on the FDA page named below) or the package directions before you decide. Flush only if the medicine is on that list.
]

#v(0.15in)
Before you recycle or toss an empty bottle, scratch out your name and prescription number on the label.

#v(0.05in)
#text(size: 0.8em, style: "italic")[Source: FDA, "Disposal of Unused Medicines: What You Should Know," fda.gov/drugs/safe-disposal-medicines/disposal-unused-medicines-what-you-should-know. Check that page for the current flush list. This is general information, not medical advice.]

#v(0.15in)
#checklist(none, (
  [I checked the flush list for any medicine I'm getting rid of],
  [I found a take-back location or mail-back option],
  [I removed or covered personal information on the labels],
))
#_wk-field([*Take-back location near me:*], above: 0.2in)
#block(above: 0.2in)[*The day I'll drop it off:* #_wk-date]

#pagebreak()

== Where It's Going This Week

Decide where each box is headed while the room is fresh in your mind. A box that has a destination actually leaves the house.

#_wk-where(
  [Unopened toiletries and towels in good shape. Check what the place accepts before you go.],
  [Only what is worth at least your sell threshold from Week 0. In the bathroom, that is rare.],
  [Expired products, empty bottles, worn towels and anything you can't donate. Recycle what you can.],
)

#pagebreak()

#_wk-count()
