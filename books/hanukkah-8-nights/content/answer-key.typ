= Answer Key

// Gabaritos conferidos por código contra o puzzle impresso e contra os JSON: legacy/scripts/montar_gabaritos_key.py
// (gera os recortes inputs/puzzle-assets/*_gabarito_key.png; nada em inputs/ foi sobrescrito).
// Títulos "Night N · ★ Título" = título impresso na noite. Atividades sem resposta única não entram.

#let _ans-size = 13pt
#let _erros = json(_pz + "noite2_erros_gabarito.json").objetos
#let _erros-list(ids) = ak-list(size: 12pt, ..ids.map(i => {
  let o = _erros.find(o => o.id == i).nome
  (str(i), upper(o.first()) + o.slice(1))
}))

// ================================================================ NIGHT 1
#ak-night(1, "Judah Says No")

#ak-grid(
  ak-card(1, 1, "Escape to the Hills", ak-maze("labirinto_facil")),
  ak-card(1, 1, "Word Hunt: Night 1", ak-img("cacapalavras_noite1_gabarito_key.png")),
  ak-card(1, 2, "Back to Modiin (The Hard Way)", ak-maze("labirinto_medio")),
)

#pagebreak()

// ================================================================ NIGHT 2
#ak-night(2, "The Temple Is a Mess")

#ak-grid(
  ak-card(2, 1, "Spot the 5 Differences", {
    ak-img("noite2_erros5_gabarito_key.png", frame: true)
    v(0.08in)
    _erros-list(range(1, 6))
  }),
  ak-card(2, 1, "Connect the Dots: The Hanukkiah", align(center, ak-img("noite2_ligar_pontos_hanukia_gabarito_key.png", w: 100%))),
  ak-card(2, 2, "Spot the 10 Differences", {
    ak-img("noite2_erros10_gabarito_key.png", frame: true)
    v(0.08in)
    _erros-list(range(1, 11))
  }),
  ak-card(2, 2, "Connect the Dots: The Temple Menorah", align(center, ak-img("noite2_ligar_pontos_menora_gabarito_key.png", w: 88%))),
)

#v(0.2in)
#ak-card(2, 0, "Family Riddle", tall: false)[#text(size: 14pt)[A menorah, or its Hanukkah cousin, the hanukkiah.]]

#pagebreak()

// ================================================================ NIGHT 3
#ak-night(3, "One Little Jar of Oil")

#ak-grid(
  ak-card(3, 1, "Symbol Sudoku (4x4)", ak-img("noite3_sudoku4x4_gabarito_key.png")),
  ak-card(3, 1, "Which Jar Is Different?", {
    ak-img("noite3_jarro_diferente_gabarito_key.png", frame: true)
    v(0.1in)
    text(size: _ans-size)[The circled jar has dots instead of stripes.]
  }),
  ak-card(3, 2, "Symbol Sudoku (6x6)", ak-img("noite3_sudoku6x6_gabarito_key.png")),
  ak-card(3, 2, "Which Jar Is the Pure One?", {
    ak-big[Jar C]
    v(0.1in)
    text(size: 14pt)[Its seal is intact, it was found standing up, and it has the High Priest's stamp. Only Jar C matches all three clues.]
  }),
)

#pagebreak()

// ================================================================ NIGHT 4
#ak-night(4, "Light It Right")

#ak-grid(
  ak-card(4, 1, "Number the Steps: Lighting the Hanukkiah", ak-list(size: _ans-size,
    ("1", [Place tonight's candles in the hanukkiah.]),
    ("2", [Say the blessings together.]),
    ("3", [Use the lit shamash to light tonight's candles.]),
    ("4", [Put the shamash back in its own holder.]))),
  ak-card(4, 1, "How Many Candles Tonight?", {
    ak-big[5 candles]
    v(0.08in)
    text(size: 14pt)[4 candles + 1 shamash = 5]
  }),
)

#v(0.2in)
#let _nights = range(1, 9)
#let _th(t) = text(font: display, size: 11.5pt, weight: "bold", tracking: 0.03em, upper(t))
#ak-card(4, 2, "How Many Candles in All Eight Nights?", tall: false, {
  table(columns: (1.75fr,) + (1fr,) * 8, stroke: 1.2pt + ink, inset: (x: 6pt, y: 10pt), align: center + horizon,
    fill: (_, y) => if y == 0 { tint } else { none },
    _th[Night], .._nights.map(n => _th(str(n))),
    text(weight: "bold", size: 12pt)[Hanukkah candles], .._nights.map(n => text(size: 13pt, str(n))),
    text(weight: "bold", size: 12pt)[\+ Shamash], .._nights.map(_ => text(size: 13pt)[1]),
    text(weight: "bold", size: 12pt)[Night's total], .._nights.map(n => text(size: 13pt, weight: "bold", str(n + 1))))
  v(0.1in)
  block(stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt, y: 9pt), breakable: false, {
    text(font: display, weight: "bold", size: 15pt, tracking: 0.04em)[GRAND TOTAL: #str(_nights.map(n => n + 1).sum()) candles]
    h(10pt)
    text(size: 13pt)[(#str(_nights.sum()) Hanukkah candles + #str(_nights.len()) shamash)]
  })
})

// ================================================================ NIGHT 5
#ak-night(5, "Spin the Dreidel")

#ak-grid(
  ak-card(5, 1, "Match the Letter to Its Meaning", ak-list(size: _ans-size,
    ("Nun", [Nothing]),
    ("Gimel", [Everything]),
    ("Hei", [Half]),
    ("Shin", [Put one in]))),
  ak-card(5, 2, "Gelt Math", ak-list(size: _ans-size,
    ("1", [12 + 9 = *21*]),
    ("2", [24 / 4 = *6*]),
    ("3", [(18 + 14) / 2 = *16*]),
    ("4", [15 + 22 + 18 + 27 = *82*]))),
)

#pagebreak()

// ================================================================ NIGHT 6
#ak-night(6, "Everything Fried")

// colunas desiguais: a grade 14x14 precisa de ~3.8in para que as letras fiquem >= 10pt na página
#ak-grid(cols: (3.2in, 1fr),
  ak-card(6, 1, "Kitchen Word Search", ak-img("noite6_cacapalavras_cozinha_gabarito_key.png")),
  ak-card(6, 2, "Big Kitchen Word Search", ak-img("noite6_cacapalavras_14x14_gabarito_key.png")),
)

#v(0.2in)
#ak-card(6, 0, "Latke Riddle", tall: false)[#text(size: 14pt)[A latke!]]

#pagebreak()

// ================================================================ NIGHT 7
#ak-night(7, "Give Some Light Away")

#ak-grid(
  ak-card(7, 1, "Count the Gelt", ak-list(size: _ans-size,
    ("Group A", [*8*]),
    ("Group B", [*13*]))),
  grid.cell(rowspan: 2, ak-card(7, 1, "Bring the Gelt to the Tzedakah Box", ak-maze("noite7_labirinto_tzedaka"))),
  ak-card(7, 2, "Split and Save", ak-list(size: _ans-size,
    ("1", [12 / 3 = *4*]),
    ("2", [(20 - 4) / 4 = *4*]),
    ("3", [30 / 5 = *6*]),
    ("4", [(24 + 12) / 2 = *18*]))),
)

// ================================================================ NIGHT 8
#ak-night(8, "All Eight Lights")

#ak-card(8, 2, "Family Hanukkah Quiz", tall: false, {
  let src(n) = h(6pt) + ak-src[Night #n]
  ak-list(size: 13pt,
    ("1", [Antiochus #src(1)]),
    ("2", [Mattathias #src(1)]),
    ("3", [Hammer #src(1)]),
    ("4", [Seven (7) #src(2)]),
    ("5", [The shamash #src(4)]),
    ("6", [Five (5): 4 candles + the shamash #src(4)]),
    ("7", [Eight (8) #src(3)]),
    ("8", [Money, in Yiddish #src(5)]),
    ("9", [Grated potato, with onion and egg #src(6)]),
    ("10", [Giving to help people in need, like sharing money or food #src(7)]))
})
