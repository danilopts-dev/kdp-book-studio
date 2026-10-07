// Tema visual do livro (P&B). Inserido pelo build logo depois de `#show: book.with(...)` e aplicado com `#show: theme`.
// Define também os helpers _wk-* usados pelas unidades (antes ficavam inline em wk01.typ).

#let ink = luma(20)
#let mid = luma(105)
#let soft = luma(195)
#let tint = luma(242)
#let tint2 = luma(226)
#let display = ("Barlow", "Bahnschrift", "Verdana")
#let body-font = ("Atkinson Hyperlegible", "Verdana")

#let _week-label = state("week-label", "")
#let _plain(c) = if type(c) == str { c } else if c.func() == smartquote { if c.double { "\"" } else { "’" } } else if c.has("text") { c.text } else if c.has("children") { c.children.map(_plain).join() } else if c.has("body") { _plain(c.body) } else if c == [ ] { " " } else { "" }
#let _kicker(body, size: 8pt) = text(font: display, size: size, tracking: 0.18em, fill: mid, weight: "bold", upper(body))

#let theme(body) = {
  set page(
    margin: (inside: 0.75in, outside: 0.6in, top: 0.65in, bottom: 0.75in),
    header: none,
    footer: context {
      let p = here().page()
      if _numbered.get() and not _is-blank(p) {
        let n = counter(page).get().first()
        let num = box(width: 0.3in, height: 0.3in, radius: 50%, fill: ink,
          align(center + horizon, text(fill: white, size: 8.5pt, weight: "bold", font: display, str(n))))
        let tag = _kicker(_week-label.get(), size: 7.5pt)
        if calc.even(n) { grid(columns: (auto, 1fr), gutter: 10pt, align: horizon, num, tag) }
        else { grid(columns: (1fr, auto), gutter: 10pt, align: (right + horizon, horizon), tag, num) }
      }
    },
  )
  set text(font: body-font, size: 11pt, fill: ink)
  set par(leading: 0.68em, spacing: 1.05em, justify: false, first-line-indent: 0em)
  set strong(delta: 300)

  // Aberturas: "Week N — Título" ganha o bloco numérico; "Part 3 — Título", "Introduction — Título" etc. ganham kicker.
  show heading.where(level: 1): it => {
    let t = _plain(it.body)
    let m = t.match(regex("^Week (\d+) — (.+)$"))
    let parts = t.split(" — ")
    let (num, kick, title) = if m != none { (m.captures.at(0), none, m.captures.at(1)) }
      else if parts.len() > 1 { (none, parts.at(0), parts.slice(1).join(" — ")) }
      else { (none, none, t) }
    pagebreak(weak: true)  // metadata depois da quebra: dentro de page() (matter) não gera página em branco
    [#metadata("end") <chap-end>]
    _week-label.update(if num != none { "Week " + num + " · " + title } else if kick != none { kick } else { title })
    set par(leading: 0.45em)
    block(width: 100%, below: 0.26in, if num != none {
      grid(columns: (auto, 1fr), column-gutter: 0.22in, align: bottom,
        box(fill: ink, radius: 10pt, inset: (x: 16pt, top: 9pt, bottom: 11pt), {
          set par(leading: 0.15em)
          text(fill: white, font: display, size: 9pt, tracking: 0.3em, weight: "bold")[WEEK]
          linebreak()
          text(fill: white, font: display, size: 58pt, weight: "bold", if num.len() == 1 { "0" + num } else { num })
        }),
        {
          _kicker(if num == "0" [Before you start · No daily tasks] else [15 minutes a day · 7 days], size: 9pt)
          v(1pt)
          text(font: display, size: 30pt, weight: "bold", title)
          v(3pt)
          line(length: 100%, stroke: 2.5pt + ink)
        },
      )
    } else {
      v(0.15in)
      if kick != none { box(fill: ink, radius: 6pt, inset: (x: 10pt, y: 6pt),
        text(fill: white, font: display, size: 10pt, tracking: 0.25em, weight: "bold", upper(kick))); v(0.06in) }
      text(font: display, size: 32pt, weight: "bold", title)
      v(3pt)
      line(length: 100%, stroke: 2.5pt + ink)
    })
  }

  show heading.where(level: 2): it => block(above: 0.28in, below: 0.15in, sticky: true, {
    set par(leading: 0.5em)
    context { let lbl = _week-label.get(); if lbl != "" { _kicker(lbl); v(-3pt) } }
    text(font: display, size: 20pt, weight: "bold", it.body)
    v(-5pt)
    box(width: 0.7in, height: 4pt, fill: ink, radius: 2pt)
  })
  show heading.where(level: 3): it => block(above: 0.2in, below: 0.1in, sticky: true,
    text(font: display, size: 14pt, weight: "bold", it.body))

  body
}

// ---------- helpers ----------
#let _wk-rule = 0.7pt + luma(150)
#let _wk-box = box(width: 0.95em, height: 0.95em, stroke: 1pt + ink, radius: 2.5pt, baseline: 0.15em)
#let _wk-blank(w) = box(width: w, height: 0.2in, stroke: (bottom: _wk-rule))
#let _wk-field(label, above: 0.3in) = block(above: above, width: 100%,
  [#label #box(width: 1fr, height: 0.2in, stroke: (bottom: _wk-rule))])
#let _wk-date = [#_wk-blank(0.5in) / #_wk-blank(0.5in) / #_wk-blank(0.8in)]
#let _wk-lines(n, gap: 0.36in) = stack(spacing: gap, ..range(n).map(_ => line(length: 100%, stroke: 0.6pt + soft)))
#let _wk-head(body) = body

// Tabela: cabeçalho preto, zebrada, cantos arredondados. head: false = sem faixa preta (tabelas sem cabeçalho).
#let _styled-table(head: true, ..args) = block(radius: 8pt, clip: true, stroke: 0.8pt + ink, {
  show table.cell.where(y: 0): it => if head {
    set text(fill: white, weight: "bold", size: 8pt, font: display, tracking: 0.06em)
    show regex("[a-z]"): l => upper(l)
    it
  } else { it }
  table(
    fill: (_, y) => if head and y == 0 { ink } else if calc.even(y) == head { tint } else { white },
    stroke: (x, y) => (
      top: if y > 0 { 0.5pt + soft } else { none },
      left: if x > 0 { 0.5pt + soft } else { none },
    ),
    ..args.named().pairs().filter(((k, _)) => k != "stroke").to-dict(),
    ..args.pos(),
  )
})

#let _wk-table(widths, heads, rows, extra: 0, y: 10pt) = _styled-table(
  columns: widths,
  inset: (x: 8pt, y: y),
  align: (left + horizon,) + (center + horizon,) * (widths.len() - 1),
  table.header(..heads),
  ..rows.map(r => (text(size: 0.92em, r),) + ([],) * (widths.len() - 1)).flatten(),
  ..range(extra).map(_ => ([],) * widths.len()).flatten(),
)

// 7 tarefas: cartões com número do dia, texto, pílula "15 MIN" e checkbox
#let _wk-daily(tasks) = {
  v(0.02in)
  stack(spacing: 5pt, ..tasks.enumerate().map(((i, t)) => block(
    width: 100%, fill: if calc.even(i) { tint } else { white }, stroke: 0.6pt + tint2, radius: 7pt,
    inset: (x: 10pt, y: 6.5pt),
    grid(columns: (0.34in, 1fr, auto, auto), column-gutter: 10pt, align: horizon,
      box(width: 0.3in, height: 0.3in, radius: 50%, fill: ink,
        align(center + horizon, text(fill: white, font: display, weight: "bold", size: 11pt, str(i + 1)))),
      text(size: 10pt, t),
      box(stroke: 0.7pt + mid, radius: 20pt, inset: (x: 6pt, y: 3pt), text(size: 7pt, fill: mid, font: display, weight: "bold")[15 MIN]),
      box(width: 0.2in, height: 0.2in, stroke: 1.2pt + ink, radius: 3pt),
    ),
  )))
}

#let checklist(title, items, box-size: 0.9em) = block(width: 100%, above: 0.18in, fill: tint, radius: 9pt, inset: (x: 14pt, y: 12pt), {
  set par(first-line-indent: 0em)
  if title != none { text(font: display, size: 14pt, weight: "bold", title); v(0.04in) }
  for it in items {
    block(above: 0.62em, grid(columns: (auto, 1fr), column-gutter: 8pt, align: horizon,
      box(width: box-size, height: box-size, stroke: 1pt + ink, radius: 2.5pt, fill: white), it))
  }
})

// cartão com faixa de título (selo + nome) no topo
#let _card(letter, name, body) = block(width: 100%, breakable: false, above: 0.16in,
  stroke: 0.8pt + ink, radius: 9pt, clip: true, {
    block(width: 100%, fill: ink, inset: (x: 12pt, y: 7pt), below: 0pt,
      grid(columns: (auto, 1fr), column-gutter: 8pt, align: horizon,
        box(width: 0.26in, height: 0.26in, radius: 50%, fill: white,
          align(center + horizon, text(fill: ink, font: display, weight: "bold", size: 10pt, letter))),
        text(fill: white, font: display, weight: "bold", size: 11pt, tracking: 0.14em, upper(name))))
    block(width: 100%, inset: (x: 12pt, top: 10pt, bottom: 12pt), above: 0pt, body)
  })

#let _wk-where(donate-hint, sell-hint, toss-hint) = {
  _card("D", "Donate", {
    text(size: 10pt, fill: luma(60), donate-hint)
    _wk-field([*Where it's going:*], above: 0.2in)
    block(above: 0.2in)[*The day I'll drop it off:* #_wk-date]
    v(0.12in); _wk-lines(2, gap: 0.34in)
  })
  _card("S", "Sell", {
    text(size: 10pt, fill: luma(60), sell-hint)
    _wk-field([*Where I'll list it:*], above: 0.2in)
    v(0.12in); _wk-lines(3, gap: 0.34in)
  })
  _card("T", "Toss", {
    text(size: 10pt, fill: luma(60), toss-hint)
    _wk-field([*What needs special handling:*], above: 0.2in)
    v(0.12in); _wk-lines(3, gap: 0.34in)
  })
}

#let _notes-wins(height: 2.4in, lines: 5) = grid(columns: (1fr, 1fr), column-gutter: 0.2in,
  block(width: 100%, height: height, stroke: 0.8pt + ink, radius: 9pt, inset: 12pt, {
    _kicker([Notes], size: 10pt)
    v(0.05in); _wk-lines(lines, gap: 0.34in)
  }),
  block(width: 100%, height: height, fill: tint, radius: 9pt, inset: 12pt, {
    _kicker([Wins], size: 10pt)
    v(0.05in); _wk-lines(lines, gap: 0.34in)
  }),
)

#let _wk-count() = {
  [== Keep / Donate / Sell / Toss Count]
  [Each day, write how many items went into each box. Then add up the week.]
  v(0.08in)
  _styled-table(
    columns: (5em, 1fr, 1fr, 1fr, 1fr),
    inset: (x: 6pt, y: 10.5pt),
    align: center + horizon,
    table.header([], [Keep], [Donate], [Sell], [Toss]),
    ..range(1, 8).map(d => (align(left, text(size: 0.9em, weight: "bold")[Day #d]), [], [], [], [])).flatten(),
    table.cell(align: left, fill: tint2)[#text(weight: "bold", size: 0.9em)[TOTAL]],
    ..range(4).map(_ => table.cell(fill: tint2)[]),
  )
  v(0.14in)
  grid(columns: (1fr, 1fr), column-gutter: 0.2in, row-gutter: 0.12in,
    [*Estimated value of Sell items:* \$ #box(width: 1fr, height: 0.2in, stroke: (bottom: _wk-rule))],
    [*Value of Donate items:* \$ #box(width: 1fr, height: 0.2in, stroke: (bottom: _wk-rule))],
    [*Minutes this week:* #box(width: 1fr, height: 0.2in, stroke: (bottom: _wk-rule))],
    [*Items out (Donate + Sell + Toss):* #box(width: 1fr, height: 0.2in, stroke: (bottom: _wk-rule))],
  )
  v(0.2in)
  _notes-wins()
}

// ---------- folha de rosto e sumário (sobrepõem os do lib.typ) ----------
#let title-page(title, subtitle: none, author: none, imprint: none) = page(header: none, footer: none, {
  v(1.5in)
  box(fill: ink, radius: 6pt, inset: (x: 10pt, y: 6pt),
    text(fill: white, font: display, size: 10pt, tracking: 0.25em, weight: "bold")[CLEAR THE CLUTTER · ROOM BY ROOM])
  v(0.2in)
  set par(leading: 0.4em)
  text(font: display, size: 46pt, weight: "bold", title)
  v(0.1in)
  line(length: 100%, stroke: 3pt + ink)
  if subtitle != none { v(0.15in); text(size: 15pt, subtitle) }
  v(1fr)
  if author != none { text(font: display, size: 16pt, weight: "bold", author) }
  v(0.6in)
})

#let toc(title: "Contents") = page(header: none, footer: none, {
  v(0.3in)
  text(font: display, size: 32pt, weight: "bold", title)
  v(-0.1in)
  line(length: 100%, stroke: 2.5pt + ink)
  v(0.2in)
  show outline.entry: it => {
    let t = _plain(it.element.body)
    let m = t.match(regex("^Week (\d+) — (.+)$"))
    let parts = t.split(" — ")
    let (k, rest) = if m != none { ("Week " + m.captures.at(0), m.captures.at(1)) }
      else if parts.len() > 1 { (parts.at(0), parts.slice(1).join(" — ")) } else { ("", t) }
    block(width: 100%, above: 0pt, below: 0pt, inset: (y: 4pt), stroke: (bottom: 0.5pt + soft),
      link(it.element.location(), grid(
      columns: (1.15in, 1fr, auto), column-gutter: 10pt, align: (left + horizon, left + horizon, right + horizon),
      _kicker(k, size: 9pt),
      text(size: 12.5pt, rest),
      box(width: 0.42in, height: 0.27in, radius: 50%, fill: if k.starts-with("Week") { tint } else { ink },
        align(center + horizon, text(font: display, weight: "bold", size: 11pt,
          fill: if k.starts-with("Week") { ink } else { white }, it.page()))),
    )))
  }
  outline(title: none, depth: 1)
})

// back matter: página normal do tema (com fólio), sem o page() do lib, que gerava página em branco antes de cada seção
#let plain-page(body) = { pagebreak(weak: true); body }

// página de copyright: letra pequena, centralizada na vertical (o lib.typ empurra tudo para o pé da página)
#let copyright-page(body) = page(header: none, footer: none, {
  set par(justify: false, first-line-indent: 0em, spacing: 1.1em, leading: 0.6em)
  set text(size: 8pt, fill: luma(50))
  v(1fr)
  block(width: 100%, inset: (x: 0.6in), body)
  v(1.2fr)
})
