// Printable Declutter Kit — bônus do livro (US Letter, P&B, imprimir em casa).
// Visual alinhado ao theme.typ do miolo, mas independente (não usa lib.typ).
// Páginas: 1 como usar | 2 fluxograma | 3-14 checklists por cômodo (reset mensal) | 15 tracker de 12 semanas.

#let ink = luma(20)
#let mid = luma(105)
#let soft = luma(195)
#let tint = luma(242)
#let tint2 = luma(226)
#let display = ("Barlow", "Verdana")
#let body-font = ("Atkinson Hyperlegible", "Verdana")
#let rule = 0.7pt + luma(150)

#set page(paper: "us-letter", margin: (x: 0.7in, top: 0.6in, bottom: 0.65in),
  footer: context {
    set text(font: display, size: 7.5pt, fill: mid, weight: "bold", tracking: 0.14em)
    grid(columns: (1fr, auto), upper[Printable Declutter Kit · Emily P. Harper], counter(page).display())
  })
#set text(font: body-font, size: 11pt, fill: ink)
#set par(leading: 0.62em, spacing: 1em)
#set strong(delta: 300)

#let kicker(body, size: 8pt) = text(font: display, size: size, tracking: 0.18em, fill: mid, weight: "bold", upper(body))
#let pill-title(kick, title) = {
  box(fill: ink, radius: 6pt, inset: (x: 10pt, y: 5pt),
    text(fill: white, font: display, size: 9pt, tracking: 0.25em, weight: "bold", upper(kick)))
  v(0.06in)
  text(font: display, size: 30pt, weight: "bold", title)
  v(2pt)
  line(length: 100%, stroke: 2.5pt + ink)
}
#let cbox(s: 0.95em) = box(width: s, height: s, stroke: 1.1pt + ink, radius: 2.5pt, fill: white, baseline: 0.15em)
#let blank(w) = box(width: w, height: 0.2in, stroke: (bottom: rule))
#let field(label, above: 0.18in) = block(above: above, width: 100%,
  [#label #box(width: 1fr, height: 0.2in, stroke: (bottom: rule))])
#let lines(n, gap: 0.3in) = stack(spacing: gap, ..range(n).map(_ => line(length: 100%, stroke: 0.6pt + soft)))
#let checklist(title, items, above: 0.14in, gap: 0.58em) = block(width: 100%, above: above, fill: tint, radius: 9pt, inset: (x: 14pt, y: 11pt), {
  if title != none { text(font: display, size: 13pt, weight: "bold", title); v(0.02in) }
  for it in items {
    block(above: gap, grid(columns: (auto, 1fr), column-gutter: 8pt, align: horizon, cbox(s: 0.9em), it))
  }
})

// ---------- Página 1: como usar ----------
#pill-title("Free bonus", "Your Printable Declutter Kit")
#v(0.2in)
This kit goes with *The 12-Week Decluttering Workbook*. These are the pages that work better printed on their own: taped to a door, stuck on the fridge or clipped to a clipboard while your hands are full. Print as many copies as you need. Regular letter-size paper and a black-and-white printer are enough.

#v(0.15in)
#let how(n, name, body) = block(width: 100%, above: 0.12in, breakable: false, stroke: 0.8pt + ink, radius: 9pt, inset: 12pt,
  grid(columns: (0.42in, 1fr), column-gutter: 10pt, align: top,
    box(width: 0.36in, height: 0.36in, radius: 50%, fill: ink, align(center + horizon, text(fill: white, font: display, weight: "bold", size: 14pt, str(n)))),
    [#text(font: display, weight: "bold", size: 14pt, name) \ #body]))
#how(1, "Keep / Donate / Sell / Toss flowchart", [Page 2. The tie-breaker from Week 0 on a single page. Tape a copy inside the closet door, the garage door or wherever you work, and print one for everyone who is helping.])
#how(2, "Room checklists", [Pages 3 to 14. One page for each of the 12 rooms, so every monthly 15-minute reset starts with a clean copy. Set a timer, work down the page and check the boxes. Print the page for the room you are resetting, and file it or toss it when you are done.])
#how(3, "12-week fridge tracker", [Page 15. Check off each week as you finish it, where the whole house can see it.])

#v(0.25in)
#block(width: 100%, fill: tint, radius: 9pt, inset: 14pt)[
  #text(font: display, weight: "bold", size: 14pt)[Three habits that make the kit work] #v(0.04in)
  - *Ask the same question every time.* "If this were gone tomorrow, would I go out and buy it again?"
  - *Keep the boxes labeled.* Four boxes or bags: Keep, Donate, Sell, Toss.
  - *Stop when the timer rings.* Fifteen minutes counts as a full day.
]

#v(0.25in)
#align(center, text(size: 0.9em, fill: mid)[Printing tip: choose "Actual size" or "100%" in the print dialog, not "Fit to page."])

// ---------- Página 2: fluxograma ----------
#pagebreak()
#pill-title("Tie-breaker", "Keep, Donate, Sell or Toss?")
#v(0.1in)
Pick up one item and answer the questions in order. There is no "maybe" box.

#let step(n, body) = block(width: 100%, fill: ink, radius: 12pt, inset: (x: 14pt, y: 8pt), breakable: false,
  grid(columns: (0.42in, 1fr), column-gutter: 10pt, align: horizon,
    box(width: 0.36in, height: 0.36in, radius: 50%, fill: white, align(center + horizon, text(fill: ink, font: display, weight: "bold", size: 14pt, str(n)))),
    text(fill: white, size: 12.5pt, weight: "bold", body)))
#let outcome(word, note, filled: false) = block(width: 100%, breakable: false, radius: 12pt,
  stroke: 2pt + ink, fill: if filled { tint2 } else { white }, inset: (x: 12pt, y: 7pt), {
    text(font: display, size: 22pt, weight: "bold", tracking: 0.06em, upper(word))
    v(-0.05in)
    text(size: 10pt, note)
  })
#let arrow(label, dir: "down") = {
  let g = if dir == "down" { sym.arrow.b } else { sym.arrow.r }
  text(font: display, weight: "bold", size: 11pt, tracking: 0.1em)[#upper(label) #g]
}
#let flow-row(q, label, out) = grid(columns: (1fr, 0.95in, 1fr), column-gutter: 0pt, align: horizon,
  q, align(center, arrow(label, dir: "right")), out)
#let down(label: "No") = align(left, pad(left: 0.45in, v(0.02in) + arrow(label) + v(0.02in)))

#v(0.08in)
#block(width: 100%, stroke: 1pt + ink, radius: 20pt, inset: (x: 14pt, y: 8pt), align(center, text(font: display, weight: "bold", size: 13pt, tracking: 0.08em)[PICK UP ONE ITEM]))
#align(center, v(0.04in) + text(size: 14pt, weight: "bold", sym.arrow.b) + v(0.0in))

#flow-row(
  step(1, [Is it broken, expired, stained or missing its parts?]),
  "Yes",
  outcome("Toss", [Recycle what you can.]),
)
#down(label: "No")
#flow-row(
  step(2, [If this were gone tomorrow, would I go out and buy it again?]),
  "Yes",
  outcome("Keep", [Back in the room, in a place where you can find it.], filled: true),
)
#down(label: "No, or \"I'd have to think about it\"")
#flow-row(
  step(3, [Is it worth my sell threshold or more?]),
  "Yes",
  outcome("Sell", [Worth the time to list it and meet a buyer.]),
)
#down(label: "No")
#block(width: 50% - 0.475in, outcome("Donate", [Under your threshold. Out of the house.], filled: true))

#v(0.1in)
#grid(columns: (1fr, 1fr), column-gutter: 0.2in,
  block(width: 100%, stroke: 0.8pt + ink, radius: 9pt, inset: 12pt)[
    #kicker[My sell threshold]
    #v(0.04in)
    #text(font: display, weight: "bold", size: 20pt)[\$ #blank(1.1in)]
  ],
  block(width: 100%, fill: tint, radius: 9pt, inset: 12pt)[
    #kicker[Truly can't decide?]
    #v(0.04in)
    #text(size: 10pt)[Put it in *Keep for now*. You will look at it again at a 15-minute reset.]
  ],
)

// ---------- Páginas 3-14: checklists por cômodo ----------
// (semana, cômodo, tarefas do reset). Cômodos idênticos aos do livro (Week 0, Part 4).
#let rooms = (
  ("Week 1", "Bathroom", (
    [Counter and sink are clear. Only what I used today is out],
    [Medicine cabinet or shelf: anything expired or no longer needed is out],
    [Under the sink is tidy and nothing leaks or has spilled],
    [Makeup, skin care and sunscreen: expired items are in Toss],
    [Hair products, brushes and tools: only what I use is left],
    [Towels and toiletries: extras and duplicates are in Donate or Toss],
  )),
  ("Week 2", "Entryway and coat closet", (
    [Coats and jackets: only the ones in season and in use are here],
    [Shoes by the door: every pair is one I wear],
    [Bags, backpacks and totes are emptied of old receipts and papers],
    [Hats, gloves, scarves and umbrellas are paired up],
    [Keys and mail are sorted. The landing zone is clear],
    [Anything that drifted in and does not belong here is back in its room],
  )),
  ("Week 3", "Kitchen, part one: counters, pantry, fridge", (
    [Counters are clear except for what I use every day],
    [Pantry shelves: expired or stale food is in Toss],
    [Duplicates are combined. Sealed, in-date extras can go to the food bank],
    [Fridge shelves and door are wiped. Old leftovers and condiments are out],
    [Freezer and spices are checked],
    [Everything left has a home I can find without moving something else],
  )),
  ("Week 4", "Kitchen, part two: cabinets, gadgets, containers", (
    [Dishes and glasses: chipped or unused ones are out],
    [Pots, pans and bakeware: only what I used in the last year],
    [Utensil and gadget drawers: duplicates and never-used gadgets are out],
    [Small appliances: anything I don't use is in Donate or Sell],
    [Containers and lids: every lid has its container and every container its lid],
    [Party and serving pieces are sorted, and the rest has a clear spot],
  )),
  ("Week 5", "Living room", (
    [Media area: only what still works and gets used],
    [Cables, chargers and remotes each match a device I own],
    [Movies, music and games nobody plays are in Donate or Sell],
    [Magazines, books and papers: the current ones stay, the rest go],
    [Coffee table, side tables and drawers are clear],
    [Blankets, pillows and decor: only what I like and use],
  )),
  ("Week 6", "Bedroom", (
    [Nightstands hold only what I use at night],
    [Under the bed is clear, or holds only what I chose to put there],
    [The clothes chair is empty],
    [Dresser top and windowsill are clear of dishes, receipts and loose change],
    [Floor and corners: baskets, shoes and books are put away],
    [Anything that landed here and belongs elsewhere is back in its room],
  )),
  ("Week 7", "Closet", (
    [Hangers: I checked what I wore since the last reset],
    [Shirts, pants, skirts and dresses: pieces that don't fit are out],
    [Jackets and sweaters: I kept what I reached for],
    [Shoes and accessories are paired and in good shape],
    [Party clothes and the "not sure" bag have been decided],
    [Sell items are in the Sell Tracker. Donate items are by the door],
  )),
  ("Week 8", "Kids' rooms and toys (or hobby room)", (
    [Toys: broken pieces and puzzles with missing parts are out],
    [Toys and supplies outgrown or no longer used are in the Donate box],
    [Books and games: only what gets used is on the shelf],
    [Art, crafts and school papers: I kept the best and recycled the rest],
    [Closet and drawers hold only clothes that fit],
    [Hobby room: supplies I won't use are in Donate or Sell],
  )),
  ("Week 9", "Home office and paper pile", (
    [Inbox pile is sorted: file, act on or recycle],
    [Desk surface and drawers are clear],
    [Papers to shred are in the shred bin],
    [Paper to scan is scanned and sorted],
    [Cables, pens and supplies: only what works is kept],
    [Filing system is current and I can find any document in a minute],
  )),
  ("Week 10", "Linen closet, laundry, cleaning supplies", (
    [Sheets and towels: I kept the sets I use and tossed the worn ones],
    [Blankets and pillows: extras are in Donate],
    [Laundry area is clear of lone socks, lint and empty bottles],
    [Cleaning supplies: duplicates and unused products are out],
    [Leftover products that need special handling are set aside for disposal],
    [Everything that stayed is where I can reach it],
  )),
  ("Week 11", "Garage, basement, attic, storage", (
    [Floor space is clear. Nothing blocks the door or the stairs],
    [Boxes: I opened one pile and decided on every item in it],
    [Tools and equipment: only what I use stays],
    [Sports gear and seasonal items are sorted and in the right place],
    [Items for the garage sale are together and priced],
    [Toss and Donate boxes left the house this month],
  )),
  ("Week 12", "Sentimental things", (
    [I looked at one box or bag, with the timer on],
    [I kept the memory in a way I can enjoy it, not just in a box],
    [Photos and letters: I sorted a small batch],
    [Things that belong to other people are returned or set aside for them],
    [Keepsakes I'm unsure about are in Keep for now],
    [What I kept has a clear, safe spot],
  )),
)

#for (wk, room, tasks) in rooms {
  pagebreak()
  kicker(wk + " · Monthly 15-minute reset")
  v(0.04in)
  text(font: display, size: 26pt, weight: "bold", room)
  v(2pt)
  line(length: 100%, stroke: 2.5pt + ink)

  block(above: 0.16in)[*Date:* #blank(0.6in) / #blank(0.6in) / #blank(0.9in) #h(0.3in) *Timer set for 15 minutes:* #cbox()]
  checklist("This room", tasks, above: 0.2in, gap: 0.95em)
  checklist("Every reset", (
    [Put back what drifted. Anything new went into Keep, Donate, Sell or Toss],
    [I looked at anything in Keep for now and asked: would I buy it again?],
    [Donate and Toss boxes are by the door. Sell items are listed or in the Sell Tracker],
    [One in, one out: anything new that came into this room replaced something],
  ), gap: 0.95em)

  v(0.2in)
  text(font: display, weight: "bold", size: 13pt)[Count]
  v(0.04in)
  block(radius: 8pt, clip: true, stroke: 0.8pt + ink, table(
    columns: (1fr, 1fr, 1fr, 1fr), inset: (x: 8pt, y: 8pt), align: center + horizon,
    fill: (_, y) => if y == 0 { ink } else { white },
    stroke: (x, y) => (left: if x > 0 { 0.5pt + soft } else { none }),
    table.header(..([Keep], [Donate], [Sell], [Toss]).map(t => text(fill: white, font: display, weight: "bold", size: 9pt, tracking: 0.1em, upper(t)))),
    [#v(0.3in)], [], [], [],
  ))

  v(0.15in)
  grid(columns: (1fr, 1fr), column-gutter: 0.2in,
    block(width: 100%, height: 1.55in, stroke: 0.8pt + ink, radius: 9pt, inset: 10pt, {
      kicker([Notes], size: 9pt); v(0.03in); lines(4, gap: 0.27in)
    }),
    block(width: 100%, height: 1.55in, fill: tint, radius: 9pt, inset: 10pt, {
      kicker([Wins], size: 9pt); v(0.03in); lines(4, gap: 0.27in)
    }),
  )
}

// ---------- Página 15: tracker de 12 semanas (geladeira) ----------
#pagebreak()
#pill-title("Fridge door", "My 12-Week Decluttering Tracker")
#v(0.12in)
#grid(columns: (1fr, 1fr), column-gutter: 0.3in,
  [*My name:* #box(width: 1fr, height: 0.2in, stroke: (bottom: rule))],
  [*Start date:* #blank(0.5in) / #blank(0.5in) / #blank(0.7in)],
)
#v(0.12in)
Check the box when the week is done. Write in the date and how many items left the house.

#v(0.08in)
#let weeks = (
  ("0", "Walk through and rate your rooms"),
  ("1", "Bathroom"),
  ("2", "Entryway and coat closet"),
  ("3", "Kitchen, part one"),
  ("4", "Kitchen, part two"),
  ("5", "Living room"),
  ("6", "Bedroom"),
  ("7", "Closet"),
  ("8", "Kids' rooms or hobby room"),
  ("9", "Home office and paper"),
  ("10", "Linen, laundry, cleaning supplies"),
  ("11", "Garage, basement, attic"),
  ("12", "Sentimental things"),
)
#block(radius: 10pt, clip: true, stroke: 1pt + ink, table(
  columns: (0.65in, 1fr, 0.6in, 1.05in, 0.95in),
  inset: (x: 7pt, y: 9.5pt),
  align: (center + horizon, left + horizon, center + horizon, center + horizon, center + horizon),
  fill: (_, y) => if y == 0 { ink } else if calc.even(y) { tint } else { white },
  stroke: (x, y) => (top: if y > 0 { 0.5pt + soft } else { none }, left: if x > 0 { 0.5pt + soft } else { none }),
  table.header(..([Week], [Room], [Done], [Date finished], [Items out]).map(t =>
    text(fill: white, font: display, weight: "bold", size: 8.5pt, tracking: 0.08em, upper(t)))),
  ..for (n, r) in weeks {
    (text(font: display, weight: "bold", size: 14pt, n), text(size: 11pt, r), cbox(s: 1.15em), [], [])
  },
))

#v(0.15in)
#align(center, block(width: 100%, stroke: 2pt + ink, radius: 10pt, inset: (x: 14pt, y: 11pt),
  text(font: display, weight: "bold", size: 15pt, tracking: 0.04em)[ALL 12 WEEKS DONE ON  #box(width: 1.1in, height: 0.22in, stroke: (bottom: rule)) / #box(width: 0.5in, height: 0.22in, stroke: (bottom: rule)) / #box(width: 0.7in, height: 0.22in, stroke: (bottom: rule))]))
