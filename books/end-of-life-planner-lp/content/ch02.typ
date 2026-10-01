#let elp-role-table(roles) = table(
  columns: (2.5in, 2.7in, 1.8in), stroke: 0.7pt + luma(110), inset: (x: 6pt, y: 5pt),
  ..("Who", "Name", "Phone").map(h => table.cell(fill: luma(235), text(size: elp-label-size, weight: "bold", h))),
  ..roles.map(r => (table.cell(align(horizon, text(size: elp-label-size, weight: "bold", r))), table.cell(box(height: 0.55in - 10pt, width: 100%)), table.cell([]))).flatten(),
)

#chapter-opener(1, "Who to Call, and in What Order",
  [Your family should not have to guess who to phone first. List the people below in the order you want them called. Number 1 is the first call.])

#elp-heading[Family]
#elp-table(("Call #", "Name", "Phone", "In Person?"), rows: 6, row-h: 0.55in, first-numbered: true, widths: (0.9in, 2.6in, 2.2in, 1.3in))

#pagebreak()

#elp-heading[Family, Continued]
#elp-table(("Call #", "Name", "Phone", "In Person?"), rows: 9, row-h: 0.55in, start: 7, first-numbered: true, widths: (0.9in, 2.6in, 2.2in, 1.3in))
#elp-gap
#elp-field(lines: 3, hint: [(anyone who should be called by a relative, not by a stranger)])[Notes on Family]

#pagebreak()

#elp-heading[Close Friends]
#elp-table(("Call #", "Name", "Phone", "In Person?"), rows: 9, row-h: 0.55in, start: 16, first-numbered: true, widths: (0.9in, 2.6in, 2.2in, 1.3in))
#elp-gap
#elp-field(lines: 3)[Friends Who Can Help Spread the Word]

#pagebreak()

#elp-heading[My Doctors]
#elp-table(("Doctor", "Specialty", "Phone"), rows: 5, row-h: 0.55in, widths: (2.6in, 2.2in, 2.2in))
#elp-gap
#elp-field(lines: 2)[Pharmacy: Name and Phone]
#elp-gap
#elp-field(lines: 2)[Hospital I Prefer: Name and Phone]
#elp-gap
#elp-field(lines: 2)[Home Care or Hospice Contact (if any)]

#pagebreak()

#elp-heading[Attorney, Accountant, and Advisors]
#elp-role-table((
  "Attorney",
  "Accountant or Tax Preparer",
  "Financial Advisor",
  "Insurance Agent",
  "Bank Contact",
))
#elp-gap
#elp-field(lines: 2, hint: [(do not write account numbers here)])[Anything They Should Know]

#pagebreak()

#elp-heading[Neighbor, Employer, and Community]
#elp-role-table((
  "Neighbor",
  "Neighbor With a Key",
  "Employer or Former Employer",
  "Church, Temple, or Community Group",
  "Clergy or Spiritual Contact",
  "Club, Veterans, or Volunteer Group",
))

#pagebreak()

#elp-heading[Tell Them in Person]
#elp-field(lines: 3, hint: [(people who should hear it face to face, or from a family member)])[These People]
#elp-gap
#elp-heading[A Phone Call Is Fine]
#elp-field(lines: 3)[These People]
#elp-gap
#elp-heading[A Message or Card Is Fine]
#elp-field(lines: 3)[These People]
#elp-gap
#elp-field(lines: 2)[Who Should Make the Calls]

#pagebreak()

#elp-heading[Anyone Else I Want Called]
#elp-table(("Name", "Relationship", "Phone"), rows: 7)
#elp-gap
#elp-field(lines: 2)[Calls to Make for Me (pets, plants, mail)]

#room-notice()
