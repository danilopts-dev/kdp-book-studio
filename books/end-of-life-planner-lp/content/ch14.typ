#let items-table(rows) = elp-table(("Item", "Where It Is", "Who Should Get It", "Why"),
  rows: rows, row-h: 1.0in, widths: (1.65in, 1.55in, 1.6in, 2.7in))

#chapter-opener(4, "What I'm Leaving and Who Should Have It",
  [List what matters to you, where it is, who should have it, and why. A short reason helps people understand your choice. Start with the things you care about most.])

#block(width: 100%, stroke: 1pt + luma(60), inset: 10pt, radius: 4pt, breakable: false,
  text(size: 14pt)[*Please note:* this list states your wishes. To legally transfer property, you need a will or trust. Ask an attorney if you have questions.])
#v(0.1in)
#items-table(5)

#pagebreak()
#items-table(8)

#pagebreak()
#items-table(8)

#pagebreak()
#items-table(8)

#pagebreak()

#elp-heading[Things I Have Already Promised or Given]
#elp-table(("Item", "Promised To", "When or Where", "Note"),
  rows: 6, row-h: 0.7in, widths: (1.9in, 1.8in, 1.7in, 2.1in))
#elp-gap
#elp-field(lines: 2, hint: [(a name, or "talk it over together")])[If Two People Would Like the Same Thing]
#elp-gap
#elp-field(lines: 2)[Who Can Settle Questions About My Belongings]

#pagebreak()

#elp-heading[What to Donate or Sell]
#elp-table(("Item or Group of Items", "Donate or Sell?", "To Whom or Where", "Note"),
  rows: 7, row-h: 0.7in, widths: (2.2in, 1.5in, 1.9in, 1.9in))
#elp-gap
#elp-field(lines: 2, hint: [(a church, a charity, an estate sale)])[Where I'd Like Things I Don't List to Go]
#elp-gap
#elp-field(lines: 2)[Who Should Handle It]

#pagebreak()

#elp-heading[Things That Look Valuable but Aren't]
Think of items your family might hold onto or worry about, and say what you know.
#v(0.08in)
#elp-field(lines: 5, hint: [(a costume necklace, a copy, a set no one wants)])[What They Are and What You Know About Them]
#elp-gap
#elp-field(lines: 3)[What I'd Like Done With Them]

#pagebreak()

#elp-heading[Things That Don't Look Valuable but Are]
#elp-field(lines: 5, hint: [(old coins, a tool, a signed book, a family recipe box)])[What They Are and Where They Are]
#elp-gap
#elp-field(lines: 2)[Papers That Prove What They Are Worth]
#elp-gap
#elp-field(lines: 2)[Who Can Tell Me or My Family More About Them]
#elp-gap
#elp-field(lines: 2)[Anything Else I Want My Family to Know About My Belongings]
