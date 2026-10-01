#let med-table(rows, first: "Medicine", start: 1) = elp-table((first, "Dose and When", "What It Is For", "Prescribed By"),
  rows: rows, row-h: 0.6in, widths: (2.0in, 1.7in, 1.7in, 1.6in))

#chapter-opener(1, "What a Doctor Needs to Know About Me in an Emergency",
  [Keep this section where a paramedic or a family member can find it fast. Copy from your pill bottles, not from memory. Write only what you already know; this book gives no medical advice.])

#elp-heading[My Health Conditions]
#elp-table(("Condition", "Since (Year)", "Doctor Who Treats It", "Notes"),
  rows: 7, row-h: 0.6in, widths: (2.2in, 1.0in, 1.9in, 1.9in))

#pagebreak()

#elp-heading[My Allergies]
#elp-table(("Allergic To", "What Happens", "Since (Year)"),
  rows: 6, row-h: 0.6in, widths: (2.6in, 3.0in, 1.4in))
#elp-gap
#elp-heading[Other Facts a Doctor Asks First]
#elp-field[Blood Type (if I know it)]
#elp-field(lines: 2, hint: [(pacemaker, joint, stent, and so on)])[Implants or Devices in My Body]
#elp-gap
#elp-field(lines: 2, hint: [(none, or where it is kept)])[Organ Donor Card]

#pagebreak()

#elp-heading[Medications I Take Every Day]
#med-table(12)

#pagebreak()

#elp-heading[Medications I Take Every Day (continued)]
#med-table(12)

#pagebreak()

#elp-heading[Medications I Take Every Day (continued)]
#med-table(12)

#pagebreak()

#elp-heading[Only When I Need Them, and Vitamins]
#elp-table(("Medicine or Supplement", "Dose and When", "What It Is For", "Prescribed By"),
  rows: 10, row-h: 0.6in, widths: (2.0in, 1.7in, 1.7in, 1.6in))

#pagebreak()

#elp-heading[My Doctors]
#elp-table(("Doctor", "Kind of Doctor", "Phone", "Office or Hospital"),
  rows: 10, row-h: 0.6in, widths: (1.9in, 1.6in, 1.6in, 1.9in))

#pagebreak()

#elp-heading[Pharmacy and Hospital]
#elp-field(lines: 2)[Pharmacy: Name and Phone]
#elp-gap
#elp-field[Second Pharmacy or Mail-Order (if any)]
#elp-gap
#elp-field(lines: 2)[Hospital I Prefer: Name and Phone]
#elp-gap
#elp-field(hint: [(if I have a choice)])[Hospital I Do Not Want]
#elp-gap
#elp-heading[Where My Health Cards Are Kept]
#elp-field(hint: [(not the number)])[Medicare Card]
#elp-gap
#elp-field[Supplement or Other Insurance Card]
#elp-gap
#elp-field[Prescription Drug Card]

#pagebreak()

#elp-heading[Medical Equipment and Supplies]
#elp-table(("Item", "Where It Is Kept", "Company or Supplier", "Phone"),
  rows: 8, row-h: 0.6in, widths: (1.9in, 1.7in, 1.9in, 1.5in))
#elp-gap
#elp-field(lines: 2, hint: [(oxygen, CPAP, hearing aids, walker, and so on)])[Anything Someone Must Bring to the Hospital]

#pagebreak()

#elp-heading[Surgeries and Hospital Stays]
#elp-table(("What Happened", "Year", "Hospital", "Doctor"),
  rows: 8, row-h: 0.6in, widths: (2.3in, 0.9in, 1.9in, 1.9in))
#elp-gap
#elp-field(lines: 2)[Anything Else a Doctor Should Know]

#pagebreak()

#elp-heading[Notes for My Doctor or My Family]
#for _ in range(1) [
  #elp-field(lines: 3)[What I Do Each Morning With My Medicines]
  #elp-gap
  #elp-field(lines: 3)[Who Helps Me With My Medicines (if anyone)]
  #elp-gap
  #elp-field(lines: 3)[Hearing, Sight, or Memory Matters Others Should Know]
  #elp-gap
  #elp-field(lines: 3)[Other Notes]
]

#pagebreak()

#elp-heading[When My Medicines Change]
#elp-table(("Date", "Medicine", "What Changed", "Told By"),
  rows: 8, row-h: 0.6in, widths: (1.2in, 2.0in, 2.2in, 1.6in))

#room-notice()
