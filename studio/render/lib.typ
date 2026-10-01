// Biblioteca de layout de miolo KDP. Usada pelo main.typ que o build gera.
// Não editar por livro: ajustes por livro vão em book.yaml (style:).

#let _numbered = state("numbered", false)
#let _cfg = state("cfg", (:))

// Página em branco antes de um capítulo (gerada por pagebreak(to: "odd")) não leva cabeçalho/fólio.
#let _is-blank(p) = {
  let ends = query(<chap-end>)
  let hs = query(heading.where(level: 1))
  let n = calc.min(ends.len(), hs.len())
  range(n).any(i => ends.at(i).location().page() < p and p < hs.at(i).location().page())
}
#let _is-opener(p) = query(heading.where(level: 1)).any(h => h.location().page() == p)

#let book(
  page-w: 6in, page-h: 9in, bleed: 0in,
  inside: 0.5in, outside: 0.5in, top: 0.7in, bottom: 0.7in,
  body-font: ("Libertinus Serif",), heading-font: ("Libertinus Serif",),
  size: 11pt, leading: 0.65em, justify: true, indent: true, lang: "en",
  title: "", running-heads: true, folios: true, chapter-start: "odd", heading-scale: 1.9,
  body,
) = {
  set document(title: title)
  set text(font: body-font, size: size, lang: lang, hyphenate: justify)
  set par(
    justify: justify, leading: leading,
    first-line-indent: if indent { 1.2em } else { 0em },
    spacing: if indent { leading } else { leading * 1.8 },
  )
  set page(
    width: page-w, height: page-h, binding: left,
    margin: (inside: inside, outside: outside + bleed, top: top + bleed, bottom: bottom + bleed),
    header: context {
      let p = here().page()
      if running-heads and _numbered.get() and not _is-opener(p) and not _is-blank(p) {
        set text(size: size * 0.8, style: "italic")
        if calc.even(p) {
          align(left, title)
        } else {
          let hs = query(heading.where(level: 1)).filter(h => h.location().page() <= p)
          if hs.len() > 0 { align(right, hs.last().body) }
        }
      }
    },
    footer: context {
      let p = here().page()
      if folios and _numbered.get() and not _is-blank(p) {
        set text(size: size * 0.85)
        align(center, counter(page).display("1"))
      }
    },
  )
  _cfg.update((chapter-start: chapter-start, size: size))

  show heading.where(level: 1): it => {
    [#metadata("end") <chap-end>]
    pagebreak(weak: true, to: if chapter-start == "odd" { "odd" } else { none })
    v(0.9in)
    set par(justify: false, first-line-indent: 0em)
    block(width: 100%, below: 0.5in, text(font: heading-font, size: size * heading-scale, weight: "bold", it.body))
  }
  show heading.where(level: 2): it => {
    set par(first-line-indent: 0em)
    block(above: 1.4em, below: 0.8em, sticky: true, text(font: heading-font, size: size * 1.3, weight: "bold", it.body))
  }
  show heading.where(level: 3): it => block(above: 1.2em, below: 0.6em, sticky: true,
    text(font: heading-font, size: size * 1.1, weight: "bold", it.body))
  show quote.where(block: true): it => pad(left: 1.5em, right: 1.5em, text(style: "italic", it.body))
  body
}

// ---------------------------------------------------------------- front/back matter
#let title-page(title, subtitle: none, author: none, imprint: none) = {
  page(header: none, footer: none)[
    #set par(justify: false, first-line-indent: 0em)
    #v(1.6in)
    #align(center, text(size: 2.2em, weight: "bold", title))
    #if subtitle != none { v(0.25in); align(center, text(size: 1.2em, subtitle)) }
    #v(1fr)
    #if author != none { align(center, text(size: 1.1em, author)) }
    #if imprint != none { v(0.15in); align(center, text(size: 0.9em, imprint)) }
    #v(0.4in)
  ]
}

#let plain-page(body) = page(header: none, footer: none, body)

#let copyright-page(body) = page(header: none, footer: none)[
  #set par(justify: false, first-line-indent: 0em, spacing: 1em)
  #set text(size: 0.8em)
  #v(1fr)
  #body
]

#let toc(title: "Contents") = {
  page(header: none, footer: none)[
    #set par(first-line-indent: 0em)
    #text(size: 1.6em, weight: "bold", title)
    #v(0.3in)
    #show outline.entry: it => block(above: 0.9em, it)
    #outline(title: none, depth: 1)
  ]
}

#let body-start() = {
  pagebreak(weak: true, to: "odd")
  counter(page).update(1)
  _numbered.update(true)
}

#let scene-break() = align(center, block(above: 1.2em, below: 1.2em, [\* #h(1em) \* #h(1em) \*]))

// ---------------------------------------------------------------- activities
#let _grid-cells(n, cell, fill-fn, letter-size, content-fn) = grid(
  columns: (cell,) * n, rows: (cell,) * n, stroke: 0.5pt + luma(150),
  ..range(n * n).map(i => {
    let r = calc.div-euclid(i, n)
    let c = calc.rem(i, n)
    box(width: cell, height: cell, fill: fill-fn(r, c),
      align(center + horizon, text(size: letter-size, weight: "bold", content-fn(r, c))))
  })
)

#let section-page(title, subtitle: none) = {
  heading(level: 1, title)
  if subtitle != none { text(size: 1.1em, subtitle) }
}

#let puzzle-title(title, number: none) = {
  set par(first-line-indent: 0em, justify: false)
  align(center, block(below: 0.25in, text(size: 1.5em, weight: "bold",
    if number != none [#number. #title] else [#title])))
}

#let wordsearch(title, rows, words, number: none, intro: none, word-cols: 3) = {
  pagebreak(weak: true)
  puzzle-title(title, number: number)
  if intro != none { align(center, block(below: 0.2in, text(style: "italic", intro))) }
  layout(sz => {
    let n = rows.len()
    let cell = calc.min(sz.width / n, 0.42in)
    align(center, _grid-cells(n, cell, (r, c) => none, cell * 0.62, (r, c) => rows.at(r).at(c)))
  })
  v(0.25in)
  set par(first-line-indent: 0em, justify: false)
  align(center, grid(columns: word-cols, column-gutter: 0.35in, row-gutter: 0.7em,
    ..words.map(w => text(size: 1em, upper(w)))))
}

#let wordsearch-key(title, rows, cells, number: none) = {
  let n = rows.len()
  let hit = cells.map(x => str(x.at(0)) + "-" + str(x.at(1)))
  block(breakable: false, width: 100%, {
    align(center, text(weight: "bold", size: 0.9em, if number != none [#number. #title] else [#title]))
    v(0.4em)
    layout(sz => {
      let cell = calc.min(sz.width / n, 0.2in)
      align(center, _grid-cells(n, cell,
        (r, c) => if hit.contains(str(r) + "-" + str(c)) { luma(200) } else { none },
        cell * 0.6, (r, c) => rows.at(r).at(c)))
    })
  })
}

#let _sudoku-grid(rows, cell, size, bold-digits: none) = {
  let n = 9
  grid(
    columns: (cell,) * n, rows: (cell,) * n,
    stroke: (x, y) => (
      left: if calc.rem(x, 3) == 0 { 2pt } else { 0.5pt },
      top: if calc.rem(y, 3) == 0 { 2pt } else { 0.5pt },
      right: if x == 8 { 2pt } else { none },
      bottom: if y == 8 { 2pt } else { none },
    ),
    ..range(81).map(i => {
      let r = calc.div-euclid(i, 9)
      let c = calc.rem(i, 9)
      let ch = rows.at(r).at(c)
      let given = bold-digits == none or bold-digits.at(r).at(c) != "."
      align(center + horizon, if ch == "." { [] } else {
        text(size: size, weight: if given { "bold" } else { "regular" },
          fill: if given { black } else { luma(90) }, ch)
      })
    })
  )
}

#let sudoku(title, puzzle, number: none, intro: none) = {
  pagebreak(weak: true)
  puzzle-title(title, number: number)
  if intro != none { align(center, block(below: 0.2in, text(style: "italic", intro))) }
  layout(sz => {
    let cell = calc.min(sz.width / 9, 0.62in)
    align(center, _sudoku-grid(puzzle, cell, cell * 0.6))
  })
}

#let sudoku-key(title, puzzle, solution, number: none) = block(breakable: false, width: 100%, {
  align(center, text(weight: "bold", size: 0.9em, if number != none [#number. #title] else [#title]))
  v(0.4em)
  layout(sz => {
    let cell = calc.min(sz.width / 9, 0.24in)
    align(center, _sudoku-grid(solution, cell, cell * 0.6, bold-digits: puzzle))
  })
})

#let trivia(title, questions, intro: none, start: 1) = {
  heading(level: 1, title)
  if intro != none { block(below: 0.25in, text(style: "italic", intro)) }
  set par(first-line-indent: 0em, justify: false)
  for (i, q) in questions.enumerate() {
    block(breakable: false, above: 1.1em, {
      text(weight: "bold")[#(start + i). #q.q]
      if q.at("options", default: none) != none {
        let letters = "ABCDEFGH"
        for (j, o) in q.options.enumerate() {
          block(above: 0.45em, pad(left: 1.2em)[#letters.at(j)) #o])
        }
      }
    })
  }
}

#let trivia-key(title, questions, start: 1) = {
  set par(first-line-indent: 0em, justify: false)
  heading(level: 2, title)
  for (i, q) in questions.enumerate() {
    let ans = q.answer
    if q.at("options", default: none) != none {
      let idx = q.options.position(o => o == q.answer)
      if idx != none { ans = "ABCDEFGH".at(idx) + ") " + q.answer }
    }
    block(above: 0.6em)[*#(start + i).* #ans#if q.at("fact", default: none) != none [ — #text(style: "italic", q.fact)]]
  }
}

#let answer-keys(title: "Answer Key", body) = {
  heading(level: 1, title)
  body
}

#let key-grid(cols: 2, items) = grid(columns: (1fr,) * cols, column-gutter: 0.3in, row-gutter: 0.3in, ..items)

// ---------------------------------------------------------------- calendar
#let month-page(name, year, weeks, days, weekday-names: ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"),
  note-size: 0.55em) = {
  page(header: none, footer: none)[
    #set par(first-line-indent: 0em, justify: false)
    #align(center, text(size: 2em, weight: "bold")[#name #year])
    #v(0.15in)
    #grid(
      columns: (1fr,) * 7,
      rows: (auto,) + (1fr,) * weeks.len(),
      stroke: 0.6pt + luma(120),
      ..weekday-names.map(d => align(center, pad(y: 4pt, text(weight: "bold", size: 0.9em, d)))),
      ..weeks.flatten().map(dn => {
        if dn == 0 { [] } else {
          let info = days.at(str(dn), default: (:))
          pad(4pt, {
            text(weight: "bold", str(dn))
            if "hebrew" in info { h(1fr); text(size: note-size, info.hebrew) }
            if "notes" in info {
              linebreak()
              text(size: note-size, info.notes.join("\n"))
            }
          })
        }
      })
    )
  ]
}

// ---------------------------------------------------------------- picture books
#let picture-page(img, body: none, mode: "full", text-size: 1.4em) = {
  page(margin: 0in, header: none, footer: none)[
    #if mode == "full" {
      image(img, width: 100%, height: 100%, fit: "cover")
      if body != none {
        place(bottom + center, dy: -0.6in, block(fill: white.transparentize(15%), inset: 14pt, radius: 6pt,
          width: 80%, align(center, text(size: text-size, body))))
      }
    } else {
      let img-h = if mode == "top" { 65% } else { 60% }
      let pic = image(img, width: 100%, height: img-h, fit: "cover")
      let txt = block(width: 100%, height: 100% - img-h, inset: 0.6in,
        align(center + horizon, text(size: text-size, body)))
      if mode == "top" { stack(spacing: 0pt, pic, txt) } else { stack(spacing: 0pt, txt, pic) }
    }
  ]
}

// ---------------------------------------------------------------- planners / organizers
// Unidades kind: typst usam estes blocos (ou Typst livre) em content/<id>.typ.
#let lined-page(title, lines: 22, gap: 0.34in) = page(header: none)[
  #set par(first-line-indent: 0em)
  #if title != none { text(size: 1.4em, weight: "bold", title); v(0.2in) }
  #stack(spacing: gap, ..range(lines).map(_ => line(length: 100%, stroke: 0.5pt + luma(160))))
]

#let tracker(title, rows, cols, row-label-width: 1.6in, header: none) = {
  set par(first-line-indent: 0em)
  if title != none { text(size: 1.3em, weight: "bold", title); v(0.15in) }
  let hdr = if header == none { range(1, cols + 1).map(str) } else { header }
  table(
    columns: (row-label-width,) + (1fr,) * cols,
    stroke: 0.5pt + luma(140),
    inset: 5pt,
    [], ..hdr.map(h => align(center, text(size: 0.75em, weight: "bold", h))),
    ..rows.map(r => (text(size: 0.9em, r),) + ([],) * cols).flatten(),
  )
}

#let checklist(title, items, box-size: 0.9em) = {
  set par(first-line-indent: 0em)
  if title != none { text(size: 1.3em, weight: "bold", title); v(0.1in) }
  for it in items {
    block(above: 0.7em, [#box(width: box-size, height: box-size, stroke: 0.8pt) #h(0.5em) #it])
  }
}

// ---------------------------------------------------------------- elp: organizer em letra grande
// Blocos reutilizáveis dos capítulos do End of Life Planner (e de outros organizers 8.5x11 em letra grande).
// Regras: linhas de escrita 0,4"; texto de rótulo/cabeçalho nunca abaixo de 14pt.
#let elp-line-h = 0.4in
#let elp-label-size = 14pt
#let elp-rule = 0.6pt + luma(110)

// Abertura de capítulo: marcador "Weekend N of 4" + heading nível 1 (entra no sumário) + intro curta.
// Compacto de propósito (o heading padrão do engine ocupa ~1,5"); não força quebra de página para capítulo ímpar.
#let chapter-opener(weekend, title, intro) = {
  [#metadata("end") <chap-end>]
  pagebreak(weak: true)
  set par(first-line-indent: 0em, justify: false)
  block(below: 0.12in, text(size: 14pt, weight: "bold", tracking: 0.06em, fill: luma(70), upper[Weekend #weekend of 4]))
  {
    show heading.where(level: 1): it => block(above: 0pt, below: 0.15in, width: 100%,
      text(size: 26pt, weight: "bold", it.body))
    heading(level: 1, title)
  }
  block(below: 0.2in, text(size: 16pt, intro))
  line(length: 100%, stroke: 1.2pt + black)
  v(0.15in)
}

// Subtítulo de bloco dentro de um capítulo.
#let elp-heading(title) = block(above: 0.28in, below: 0.1in, sticky: true,
  text(size: 18pt, weight: "bold", title))

// Campo de escrita com rótulo. lines: 1 = rótulo e linha na mesma faixa; >1 = rótulo acima e N linhas.
// hint: texto pequeno (>=14pt) depois do rótulo, p.ex. "(optional)".
#let elp-field(label, lines: 1, hint: none) = {
  let lab = text(size: elp-label-size, weight: "bold", label)
  let hnt = if hint == none { [] } else { text(size: elp-label-size, fill: luma(80), [ #hint]) }
  if lines == 1 {
    grid(columns: (auto, 1fr), column-gutter: 8pt, align: bottom,
      box(height: elp-line-h, align(horizon + left, lab + hnt)),
      box(height: elp-line-h, width: 100%, stroke: (bottom: elp-rule)))
  } else {
    block(breakable: false, {
      lab + hnt
      v(0pt)
      for _ in range(lines) { box(height: elp-line-h, width: 100%, stroke: (bottom: elp-rule)); linebreak() }
    })
  }
}

// Vários campos de linha única lado a lado: elp-field-row(("Phone", none), ("Email", none)) ou só rótulos.
#let elp-field-row(..labels) = grid(columns: (1fr,) * labels.pos().len(), column-gutter: 0.3in,
  ..labels.pos().map(l => elp-field(l)))

// Espaçamento padrão entre campos.
#let elp-gap = v(0.08in)

// Tabela de papéis/itens: coluna 1 pré-preenchida (rótulo em negrito), demais colunas vazias.
// Padrão (Who/Name/Phone) usado no ch02; headers/widths/row-h permitem outras formas (ex.: documentos).
#let elp-role-table(roles, headers: ("Who", "Name", "Phone"), widths: (2.5in, 2.7in, 1.8in), row-h: 0.55in) = table(
  columns: widths, stroke: 0.7pt + luma(110), inset: (x: 6pt, y: 5pt),
  ..headers.map(h => table.cell(fill: luma(235), text(size: elp-label-size, weight: "bold", h))),
  ..roles.map(r => (table.cell(align(horizon, text(size: elp-label-size, weight: "bold", r))),
    ..range(headers.len() - 1).map(_ => table.cell(box(height: row-h - 10pt, width: 100%))))).flatten(),
)

// Tabela larga para preencher: headers (3-4 colunas), rows linhas vazias de altura >= 0,4".
// widths: lista de larguras (padrão: colunas iguais). first-numbered: coluna 1 pré-numerada (1., 2., ...).
#let elp-table(headers, rows: 5, widths: none, first-numbered: false, row-h: elp-line-h, start: 1) = {
  let n = headers.len()
  let cols = if widths == none { (1fr,) * n } else { widths }
  table(
    columns: cols, stroke: 0.7pt + luma(110), inset: (x: 6pt, y: 5pt),
    ..headers.map(h => table.cell(fill: luma(235), text(size: elp-label-size, weight: "bold", h))),
    ..range(rows).map(i => range(n).map(j =>
      table.cell(box(height: row-h - 10pt, width: 100%,
        if first-numbered and j == 0 { align(horizon, text(size: 16pt, weight: "bold")[#(i + start).]) } else { [] }
      )))).flatten(),
  )
}

// Caixas de marcar: choice([A], [B]) lista opções verticais com quadrado para marcar (ch12-ch14).
#let opt(label) = box(baseline: 0.04in, stroke: 1pt + black, width: 0.2in, height: 0.2in)
#let choice(..items) = for it in items.pos() [
  #opt(it) #h(0.1in) #it   #v(0.06in)
]

// Aviso "Running out of room?" (capítulos 2, 4, 6, 11). Hoje aponta para a página do bônus no início do livro.
// Quando existir o QR, mude SÓ este bloco (adicionar a imagem ao lado do texto).
#let room-notice() = block(breakable: false, width: 100%, above: 0.25in, stroke: 1pt + luma(60), inset: 12pt, radius: 4pt, {
  set par(first-line-indent: 0em, justify: false)
  text(size: 16pt, weight: "bold")[Running out of room?]
  linebreak()
  text(size: 16pt)[The Extra Pages Pack has more pages just like these. See the Bonus page at the front of this book.]
})

// Aviso do Four-Weekend Plan + lembrete anual por e-mail (bonus 2) no ch16. Mesmo estilo do room-notice.
// Ainda sem URL/QR; quando existirem, mude SÓ este bloco.
#let plan-notice() = block(breakable: false, width: 100%, above: 0.25in, stroke: 1pt + luma(60), inset: 12pt, radius: 4pt, {
  set par(first-line-indent: 0em, justify: false)
  text(size: 16pt, weight: "bold")[Want a reminder?]
  linebreak()
  text(size: 16pt)[The Four-Weekend Plan and a yearly reminder email are free with this book. See the Bonus page at the front of this book.]
})
