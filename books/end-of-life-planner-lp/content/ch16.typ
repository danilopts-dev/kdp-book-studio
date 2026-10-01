#let item(t) = block(above: 0pt, below: 0.27in, [#opt(t) #h(0.12in) #t])
#let grp(t, ..items) = {
  block(above: 0.12in, below: 0.08in, sticky: true, text(size: 16pt, weight: "bold", fill: luma(40), t))
  for i in items.pos() { item(i) }
}

#chapter-opener(4, "Keeping This Book Up to Date",
  [Once a year, set aside an hour with this book. Check each part below, fix what changed, and write it in the change log. Pick a date you will remember, like a birthday or New Year's Day.])

#elp-field-row("Review Date (MM/DD/YYYY)", "Done By")
#v(0.04in)
#text(size: 16pt, weight: "bold")[Yearly Review Checklist]

#grp([People and Health (Weekends 1 and 2)],
  [Phone numbers, addresses, and emails are still right],
  [Call These People First: the right people, in the right order],
  [Medicines, doses, and doctors are current],
  [Allergies and health conditions are up to date],
  [New births, marriages, or deaths in the family are added])
#grp([Papers and Money],
  [Legal papers are where I wrote that they are],
  [New papers are added to Where My Important Papers Are],
  [Bank, retirement, and credit card accounts are current],
  [Insurance companies and beneficiaries are still right],
  [Home, vehicles, and tax records are updated])

#pagebreak()

#grp([Home and Pets (Weekend 3)],
  [Utilities, keys, and alarm information are current],
  [People I Trust are still the right people],
  [Pet care and the people who will take over are current],
  [Where my passwords are written down is still true])
#grp([My Wishes (Weekend 4)],
  [Health care and end-of-life wishes still say what I want],
  [The person who speaks for me knows and agrees],
  [Funeral and service wishes are current],
  [My belongings list and who should get each item are current],
  [Letters are updated, or left as they are])
#grp([This Book Itself],
  [My family knows where this book is kept],
  [Everyone who has a copy has the newest pages],
  [The change log on the next page is filled in])
#elp-gap
#elp-field(lines: 3, hint: [(things to do before next year)])[Notes From This Review]
#plan-notice()

#pagebreak()

#elp-heading[Change Log]
Write down each change when you make it. Then your family can tell which pages are newest.
#v(0.08in)
#elp-table(("Date", "What I Changed", "Chapter"), rows: 13, row-h: 0.55in, widths: (1.9in, 3.8in, 1.3in))
#elp-gap
#text(size: 14pt, fill: luma(80))[Write the date as MM/DD/YYYY, for example 01/15/2027.]

#pagebreak()

#elp-heading[Who Has a Copy or Knows Where This Book Is]
Each time you give someone a copy, or tell them where the book is, write it here.
#v(0.08in)
#elp-table(("Name", "Copy or Told Where?", "Phone", "Date"), rows: 7, row-h: 0.6in, widths: (2.2in, 2.0in, 1.7in, 1.1in))
#elp-gap
#elp-field(lines: 1)[Where I Keep the Original]
#elp-gap
#elp-field(lines: 1)[Who Can Open That Place]
#elp-gap
#elp-field(lines: 2, hint: [(for example, if someone moves or you replace pages)])[When I Will Tell Everyone About Changes]
