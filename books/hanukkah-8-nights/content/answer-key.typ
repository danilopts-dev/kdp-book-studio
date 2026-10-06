= Answer Key

// Gabaritos conferidos por código contra o puzzle impresso e contra os JSON: legacy/scripts/montar_gabaritos_key.py
// (gera os recortes inputs/puzzle-assets/*_gabarito_key.png; nada em inputs/ foi sobrescrito).
// Gabaritos das atividades da expansao: legacy/scripts/extra_gabaritos_key.py (reduz os PNG para *_key.png e confere por codigo;
// as respostas em texto sao lidas dos JSON extra_n*.json, nao digitadas).
// Títulos "Night N · ★ Título" = título impresso na noite. Atividades sem resposta única não entram.

#let _ans-size = 13pt
// Cartoes com titulo de uma linha nao reservam 2 linhas (economiza altura; o corpo nao precisa alinhar com o vizinho)
#let _short = ("Escape to the Hills", "Word Hunt: Night 1", "Clean-Up Maze", "Spot the 10 Differences", "Symbol Sudoku (4x4)",
  "Which Jar Is Different?", "Follow the Oil", "Symbol Sudoku (6x6)", "Which Jar Is the Pure One?", "Oil Math", "Gelt Math",
  "Kitchen Word Search", "Latke Maze", "Count the Gelt", "Which Pile Has More?", "Who Gets What?", "Split and Save",
  "Bring the Gelt to the Tzedakah Box", "Match the Night", "Night by Night Word Search")
#let _ak-card = ak-card
#let ak-card(n, level, title, body, tall: true) = _ak-card(n, level, title, body, tall: tall and title not in _short)
#let _xj(f) = json(_pz + f)
#let _cap(t) = upper(t.first()) + t.slice(1)
#let _erros = json(_pz + "noite2_erros_gabarito.json").objetos
#let _erros-list(ids) = ak-list(size: 12pt, ..ids.map(i => {
  let o = _erros.find(o => o.id == i).nome
  (str(i), upper(o.first()) + o.slice(1))
}))

// ================================================================ NIGHT 1
#ak-night(1, "Judah Says No")

#ak-grid(
  ak-card(1, 1, "Escape to the Hills", ak-maze("labirinto_facil", w: 2.9in)),
  ak-card(1, 1, "Word Hunt: Night 1", ak-img("cacapalavras_noite1_gabarito_key.png", w: 2.9in)),
  ak-card(1, 1, "Unscramble the Words", ak-list(size: _ans-size,
    .._xj("extra_n1_unscramble.json").items.enumerate().map(((i, it)) => (str(i + 1), it.answer)))),
  ak-card(1, 2, "Back to Modiin (The Hard Way)", ak-maze("labirinto_medio", w: 2.9in)),
)

#v(0.2in)
#ak-card(1, 2, "Crack the Code", tall: false, {
  let lines = _xj("extra_n1_codigo.json").lines
  let ls = lines.map(l => l.map(w => w.map(n => str.from-unicode(64 + n)).join()).join(" "))
  text(font: display, size: 14pt, weight: "bold", tracking: 0.04em, ls.slice(0, 2).join("  /  ") + linebreak() + ls.slice(2).join("  /  "))
})


// ================================================================ NIGHT 2
#ak-night(2, "The Temple Is a Mess")

#ak-grid(
  ak-card(2, 1, "Spot the 5 Differences", {
    ak-img("noite2_erros5_gabarito_key.png", frame: true)
    v(0.08in)
    _erros-list(range(1, 6))
  }),
  ak-card(2, 1, "Connect the Dots: The Hanukkiah", align(center, ak-img("noite2_ligar_pontos_hanukia_gabarito_key.png", w: 100%))),
  ak-card(2, 1, "Clean-Up Maze", ak-maze("extra_n2_labirinto_limpeza")),
  ak-card(2, 2, "Spot the 10 Differences", {
    ak-img("noite2_erros10_gabarito_key.png", frame: true)
    v(0.08in)
    _erros-list(range(1, 11))
  }),
)

#v(0.2in)
// coluna direita mais larga: a grade 14x14 precisa de >= 3.7in para letras >= 9pt
#ak-grid(cols: (1fr, 3.8in),
  ak-card(2, 2, "Connect the Dots: The Temple Menorah", align(center, ak-img("noite2_ligar_pontos_menora_gabarito_key.png", w: 88%))),
  ak-card(2, 2, "Temple Word Search", ak-img("extra_n2_cacapalavras_templo_gabarito_key.png")),
)

#v(0.2in)
#ak-card(2, 0, "Family Riddle", tall: false)[#text(size: 14pt)[A menorah, or its Hanukkah cousin, the hanukkiah.]]


// ================================================================ NIGHT 3
#ak-night(3, "One Little Jar of Oil")

#ak-grid(
  ak-card(3, 1, "Symbol Sudoku (4x4)", ak-img("noite3_sudoku4x4_gabarito_key.png")),
  ak-card(3, 1, "Which Jar Is Different?", {
    ak-img("noite3_jarro_diferente_gabarito_key.png", frame: true)
    v(0.1in)
    text(size: _ans-size)[The circled jar has dots instead of stripes.]
  }),
  ak-card(3, 1, "Follow the Oil", ak-maze("extra_n3_labirinto_oleo")),
  ak-card(3, 2, "Symbol Sudoku (6x6)", ak-img("noite3_sudoku6x6_gabarito_key.png")),
  ak-card(3, 2, "Which Jar Is the Pure One?", {
    ak-big[Jar C]
    v(0.1in)
    text(size: 14pt)[Its seal is intact, it was found standing up, and it has the High Priest's stamp. Only Jar C matches all three clues.]
  }),
  ak-card(3, 2, "Oil Math", ak-list(size: _ans-size,
    .._xj("extra_n3_oilmath.json").problems.map(p => (str(p.id), [*#p.answer* #p.unit])))),
)


// ================================================================ NIGHT 4
#ak-night(4, "Light It Right")

#ak-grid(
  ak-card(4, 1, "Number the Steps: Lighting the Hanukkiah", ak-list(size: _ans-size,
    ("1", [Place tonight's candles in the hanukkiah.]),
    ("2", [Say the blessings together.]),
    ("3", [Use the lit shamash to light tonight's candles.]),
    ("4", [Put the shamash back in its own holder.]))),
  {
    ak-card(4, 1, "How Many Candles Tonight?", {
      ak-big[5 candles]
      v(0.08in)
      text(size: 14pt)[4 candles + 1 shamash = 5]
    })
    v(0.2in)
    ak-card(4, 1, "Draw the Candles", tall: false, ak-list(size: _ans-size,
      .._xj("extra_n4_hanukkiahs.json").draw_the_candles.items.map(i => ("Night " + str(i.night), [#i.hanukkah_candles candles + shamash]))))
  },
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

#v(0.2in)
#{
  let wn = _xj("extra_n4_hanukkiahs.json").which_night
  ak-card(4, 2, "Which Night Is It?", tall: false, {
    ak-list(size: _ans-size,
      ..wn.items.zip(("Top", "2nd", "3rd", "Bottom")).map(((it, l)) => (l, [Night *#it.night*])))
    v(0.1in)
    text(size: _ans-size)[Hanukkah candles in all four pictures: *#wn.total_hanukkah_candles* (the shamash is not counted).]
  })
}

// ================================================================ NIGHT 5
#ak-night(5, "Spin the Dreidel")

#ak-grid(
  ak-card(5, 1, "Match the Letter to Its Meaning", ak-list(size: _ans-size,
    ("Nun", [Nothing]),
    ("Gimel", [Everything]),
    ("Hei", [Half]),
    ("Shin", [Put one in]))),
  ak-card(5, 2, "What Comes Next? Dreidel Patterns", ak-list(size: _ans-size,
    .._xj("extra_n5_padroes.json").answers_text.enumerate().map(((i, a)) => (str(i + 1), [*#_cap(a)*])))),
  ak-card(5, 2, "Gelt Math", ak-list(size: _ans-size,
    ("1", [12 + 9 = *21*]),
    ("2", [24 / 4 = *6*]),
    ("3", [(18 + 14) / 2 = *16*]),
    ("4", [15 + 22 + 18 + 27 = *82*]))),
)


// ================================================================ NIGHT 6
#ak-night(6, "Everything Fried")

// colunas desiguais: as grades de letras precisam de >= 3.2in (10x10) e >= 3.8in (14x14) para letras >= 10pt na pagina
#ak-grid(cols: (3.2in, 1fr),
  ak-card(6, 1, "Kitchen Word Search", ak-img("noite6_cacapalavras_cozinha_gabarito_key.png")),
  ak-card(6, 1, "Latke Maze", ak-maze("extra_n6_labirinto_latke", w: 3.0in)),
)
#v(0.2in)
#ak-grid(cols: (1fr, 3.2in),
  ak-card(6, 2, "Big Kitchen Word Search", ak-img("noite6_cacapalavras_14x14_gabarito_key.png")),
  ak-card(6, 2, "Hanukkah Food Crossword", {
    ak-img("extra_n6_palavras_cruzadas_gabarito_key.png")
  }),
)

#v(0.2in)
#ak-card(6, 2, "Hanukkah Food Crossword: Across and Down", tall: false, {
  let cw = _xj("extra_n6_palavras_cruzadas_gabarito.json")
  grid(columns: (1fr, 1fr), column-gutter: 0.25in, align: top,
    ak-list(size: 12pt, ..cw.across.map(it => (str(it.n), it.answer))),
    ak-list(size: 12pt, ..cw.down.map(it => (str(it.n), it.answer))))
})

#v(0.2in)
#ak-card(6, 0, "Latke Riddle", tall: false)[#text(size: 14pt)[A latke!]]


// ================================================================ NIGHT 7
#ak-night(7, "Give Some Light Away")

#{
  let pl = _xj("extra_n7_pilhas_logica.json")
  let lg = pl.who_gets_what
  ak-grid(
    {
      ak-card(7, 1, "Count the Gelt", ak-list(size: _ans-size,
        ("Group A", [*8*]),
        ("Group B", [*13*])))
      v(0.2in)
      ak-card(7, 1, "Which Pile Has More?", ak-list(size: _ans-size,
        ..pl.piles.pairs.map(p => ("Pair " + str(p.n), [*#_cap(p.more)* pile (#p.left vs #p.right)]))))
      v(0.2in)
      ak-card(7, 2, "Who Gets What?", ak-list(size: _ans-size,
        ..lg.kids.map(k => (k, [*#lg.acts.at(lg.solution.at(k)).label*]))))
      v(0.2in)
      ak-card(7, 2, "Split and Save", ak-list(size: _ans-size,
        ("1", [12 / 3 = *4*]),
        ("2", [(20 - 4) / 4 = *4*]),
        ("3", [30 / 5 = *6*]),
        ("4", [(24 + 12) / 2 = *18*])))
    },
    ak-card(7, 1, "Bring the Gelt to the Tzedakah Box", ak-maze("noite7_labirinto_tzedaka")),
  )
}


// ================================================================ NIGHT 8
#ak-night(8, "All Eight Lights")

#{
  let src(n) = h(6pt) + ak-src[Night #n]
  let mt = _xj("extra_n8_match.json")
  ak-grid(cols: (1fr, 3.8in),
    {
      ak-card(8, 1, "Match the Night", ak-list(size: 12pt,
        ..mt.answers.map(a => ("Night " + str(a.night), [#a.fact]))))
      v(0.2in)
      ak-card(8, 2, "Family Hanukkah Quiz", tall: false, {
        ak-list(size: 12pt,
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
    },
    ak-card(8, 2, "Night by Night Word Search", ak-img("extra_n8_cacapalavras_noites_gabarito_key.png")),
  )
}
