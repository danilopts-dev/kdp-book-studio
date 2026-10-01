#chapter-opener(3, "My Pets: Who Takes Them and How",
  [Pets cannot ask for help, and someone must know what they need on the first day. Use one page for each pet, up to three. Name the person who will take each one, and ask that person before you write it down.])

#elp-heading[Right Now, Who Looks After My Pets If I Cannot?]
#elp-field(lines: 2, hint: [(a neighbor, a relative, a friend)])[Name and Phone]
#elp-gap
#elp-field(lines: 2, hint: [(a drawer, a folder, the vet's office)])[Where My Pets' Papers and Records Are]
#elp-gap
#elp-field(lines: 2, hint: [(a kennel, a sitter, a rescue group)])[Anyone Else Who Cares for Them]
#elp-gap
#elp-field(lines: 2)[Notes for Whoever Steps In First]

#pagebreak()

#let pet-page(n) = [
  #elp-heading[Pet #n of 3]
  #elp-field[Name]
  #elp-gap
  #elp-field-row("Kind and Breed", "Age")
  #elp-gap
  #elp-field-row("Veterinarian", "Phone")
  #elp-gap
  #elp-field(lines: 2, hint: [(brand, amount, times of day)])[Food and Feeding]
  #elp-gap
  #elp-field(lines: 2, hint: [(name, dose, times)])[Medicines and When They Are Given]
  #elp-gap
  #elp-field(lines: 2, hint: [(fears, favorite spot, walks, quirks)])[Habits and Things to Know]
  #elp-gap
  #elp-field[Who Takes This Pet]
  #elp-gap
  #elp-field(hint: [(Yes / Not yet asked)])[Have They Agreed?]
  #elp-gap
  #elp-field(hint: [(name and phone)])[Plan B If That Person Cannot]
]

#pet-page(1)
#pagebreak()
#pet-page(2)
#pagebreak()
#pet-page(3)
