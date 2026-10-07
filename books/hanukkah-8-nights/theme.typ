// Tema do livro "8 Nights of Hanukkah Activity Book" (P&B, 8.5x11, crianças 6-10).
// Inserido pelo build logo depois de `#show: book.with(...)` e aplicado com `#show: theme`.
// Os componentes abaixo ficam disponíveis para todas as unidades (content/n1.typ ... n8.typ, after.typ, answer-key.typ).
//
// Uso numa noite (nesta ordem; cada noite começa em página nova):
//   = Night 1 — Judah Says No                     (abertura: selo NIGHT + título)
//   #story[...parágrafos...]                      (Tonight's Story)
//   #art("11.png")                                (ilustração de inputs/illustrations/)
//   #whats-a("Maccabee")[...]                     (caixa What's a...?)
//   #activity(1, "Escape to the Hills")[instrução] + #puzzle("labirinto_facil.png")
//   #activity(2, "...")[instrução]
//   #before-candles[...]                          (faixa Before the Candles)

#let ink = luma(15)
#let mid = luma(90)
#let soft = luma(190)
#let tint = luma(244)
#let display = ("Barlow", "Bahnschrift", "Verdana")
#let body-font = ("Atkinson Hyperlegible", "Verdana")
#let heb-font = ("Times New Roman", "Arial")  // só letras isoladas do dreidel (N5); decisão 06/10/2026
#let _ill = "/books/hanukkah-8-nights/inputs/illustrations/"
#let _pz = "/books/hanukkah-8-nights/inputs/puzzle-assets/"

#let _night-label = state("night-label", "")
#let _plain(c) = if type(c) == str { c } else if c.func() == smartquote { if c.double { "\"" } else { "’" } } else if c.has("text") { c.text } else if c.has("children") { c.children.map(_plain).join() } else if c.has("body") { _plain(c.body) } else if c == [ ] { " " } else { "" }
#let _kicker(body, size: 9pt) = text(font: display, size: size, tracking: 0.16em, fill: mid, weight: "bold", upper(body))

#let theme(body) = {
  set page(
    margin: (inside: 0.65in, outside: 0.6in, top: 0.6in, bottom: 0.75in),
    header: none,
    footer: context {
      let p = here().page()
      if _numbered.get() and not _is-blank(p) {
        let n = counter(page).get().first()
        let num = box(width: 0.32in, height: 0.32in, radius: 50%, fill: ink,
          align(center + horizon, text(fill: white, size: 9pt, weight: "bold", font: display, str(n))))
        let tag = _kicker(_night-label.get(), size: 8pt)
        if calc.even(n) { grid(columns: (auto, 1fr), gutter: 10pt, align: horizon, num, tag) }
        else { grid(columns: (1fr, auto), gutter: 10pt, align: (right + horizon, horizon), tag, num) }
      }
    },
  )
  set text(font: body-font, size: 13pt, fill: ink)
  set par(leading: 0.7em, spacing: 1em, justify: false, first-line-indent: 0em)
  set strong(delta: 300)

  // Abertura de noite: "Night 3 — One Little Jar of Oil" => selo NIGHT 3 + título. Outros h1 => só título.
  show heading.where(level: 1): it => {
    let t = _plain(it.body)
    let m = t.match(regex("^Night (\d+) — (.+)$"))
    pagebreak(weak: true)
    [#metadata("end") <chap-end>]
    let (num, title) = if m != none { (m.captures.at(0), m.captures.at(1)) } else { (none, t) }
    _night-label.update(if num != none { "Night " + num + " · " + title } else { title })
    set par(leading: 0.4em)
    block(width: 100%, below: 0.22in, if num != none {
      grid(columns: (auto, 1fr), column-gutter: 0.22in, align: horizon,
        box(fill: ink, radius: 12pt, inset: (x: 16pt, top: 9pt, bottom: 11pt), {
          set par(leading: 0.15em)
          align(center, {
            text(fill: white, font: display, size: 10pt, tracking: 0.3em, weight: "bold")[NIGHT]
            linebreak()
            text(fill: white, font: display, size: 54pt, weight: "bold", num)
          })
        }),
        text(font: display, size: 32pt, weight: "bold", title))
    } else {
      text(font: display, size: 30pt, weight: "bold", title)
    })
  }
  body
}

// ---------------------------------------------------------------- componentes
// Tonight's Story: kicker + texto um pouco maior.
#let story(body) = {
  _kicker[Tonight's Story]
  v(0.1in)
  block(width: 100%, {
    set par(leading: 0.9em, spacing: 1.45em)
    text(size: 15pt, body)
  })
  v(0.14in)
}

// Ilustração da pasta inputs/illustrations. `w` largura (padrão: coluna inteira); `h` limita a altura.
#let art(file, w: 100%, h: auto, below: 0.12in) = block(width: 100%, above: 0.1in, below: below,
  align(center, image(_ill + file, width: w, height: h, fit: "contain")))

// Imagem de puzzle/gabarito de inputs/puzzle-assets.
#let puzzle(file, w: 4.8in, h: auto) = align(center, image(_pz + file, width: w, height: h, fit: "contain"))

// Caixa "What's a...?"
// `a: false` para termos sem artigo (ex.: "What's gelt?").
#let whats-a(term, body, a: true) = block(width: 100%, above: 0.12in, below: 0.12in, breakable: false,
  stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt, y: 11pt), {
    text(font: display, weight: "bold", size: 12pt, tracking: 0.06em, upper([What's #if a [a ]#term?]))
    v(0.03in)
    text(size: 12.5pt, body)
  })

// Selo de nível: nivel 1 = ★ Warm-up, nivel 2 = ★★ Challenge
#let level-tag(level) = box(stroke: 1.4pt + ink, radius: 20pt, inset: (x: 10pt, y: 3.5pt), baseline: 3pt,
  text(font: display, size: 10.5pt, weight: "bold", tracking: 0.08em,
    if level == 1 [★ #h(2pt) WARM-UP] else [★★ #h(2pt) CHALLENGE]))

// Cabeçalho de atividade (título + instrução curta). O corpo da atividade (puzzle, arte) vem depois.
#let activity(level, title, instruction) = block(width: 100%, above: 0.18in, below: 0.1in, breakable: false, {
  level-tag(level)
  v(0.05in)
  text(font: display, size: 22pt, weight: "bold", upper(title))
  v(0.02in)
  text(size: 13pt, instruction)
})

// Caixa para a criança desenhar/escrever (altura em polegadas ou length).
// `body` opcional: conteúdo já desenhado dentro da caixa (ex.: arte-base para a criança completar).
#let draw-box(h, label: none, body: none) = block(width: 100%, height: h, stroke: (paint: ink, thickness: 1.6pt, dash: "dashed"),
  radius: 8pt, inset: 10pt, {
    if body != none { align(center + horizon, body) }
    else if label != none { align(top + left, text(size: 12pt, fill: mid, label)) }
  })

// Lista de palavras do caça-palavras em colunas, letra grande.
#let word-list(cols: 3, ..words) = block(width: 100%, above: 0.16in, breakable: false,
  stroke: 1.4pt + ink, radius: 8pt, inset: (x: 16pt, y: 12pt), {
    _kicker(size: 10pt)[Word list]
    v(0.06in)
    grid(columns: (1fr,) * cols, row-gutter: 0.1in,
      ..words.pos().map(w => text(font: display, size: 16pt, weight: "bold", tracking: 0.08em, w)))
  })

// Rótulos de entrada/saída acima e abaixo de um labirinto.
// Labirinto com rótulos NA abertura: lê rotulos e posição da entrada (esquerda) e da saída (direita) do <name>_gabarito.json.
// Ex.: #align(center, maze-ends("labirinto_facil")). O PNG é quadrado e sem texto.
// Opcional: `icon-in` / `icon-out` (arquivos de inputs/illustrations) desenham um ícone sob o rótulo de entrada
// e sobre o rótulo de saída, dentro da margem lateral (`icon-w` de largura).
#let maze-ends(name, w: 4.95in, side: 1.15in, icon-in: none, icon-out: none, icon-w: 0.9in) = {
  let d = json(_pz + name + "_gabarito.json")
  let lab(t) = text(font: display, size: 10.5pt, weight: "bold", tracking: 0.03em, upper(t))
  let yi = d.abertura_entrada.y_rel * w
  let yo = d.abertura_saida.y_rel * w
  box(width: w + 2 * side, height: w, {
    place(left + top, dx: side, image(_pz + name + ".png", width: w))
    place(left + top, dy: yi - 0.1in, box(width: side - 0.07in, align(right, lab(d.rotulo_inicio + " →"))))
    place(left + top, dx: side + w + 0.07in, dy: yo - 0.1in, box(width: side - 0.07in, align(left, lab("→ " + d.rotulo_fim))))
    if icon-in != none {
      place(left + top, dx: side - 0.07in - icon-w, dy: yi + 0.3in, image(_ill + icon-in, width: icon-w))
    }
    if icon-out != none {
      place(left + top, dx: side + w + 0.07in, dy: yo - 0.1in - 0.15in - icon-w * 0.8, image(_ill + icon-out, width: icon-w))
    }
  })
}

// Before the Candles
#let before-candles(body) = {
  v(0.1in)
  block(width: 100%, stroke: (top: 2.5pt + ink), inset: (top: 0.12in), {
    _kicker(size: 10pt)[Before the Candles]
    v(0.05in)
    body
  })
}
#let subhead(t) = block(above: 0.26in, below: 0.1in, sticky: true, text(font: display, size: 13pt, weight: "bold", tracking: 0.08em, upper(t)))
#let joke(body) = block(width: 100%, fill: tint, radius: 8pt, inset: 12pt, text(size: 14pt, body))

// Bênção: transliteração em itálico + tradução em inglês
#let blessing(translit, english) = block(width: 100%, above: 0.12in, below: 0.16in, breakable: false,
  stroke: (left: 3pt + ink), inset: (left: 12pt, y: 4pt), {
    text(style: "italic", size: 13pt, translit)
    v(0.05in)
    text(size: 12.5pt, fill: mid, english)
  })

// Placar de um passo só: uma linha por jogador com N círculos
#let scoreboard(..names, circles: 10, label-w: 1.4in, r: 0.13in, size: 13pt) = block(width: 100%, above: 0.1in, below: 0.1in, breakable: false, {
  for n in names.pos() {
    grid(columns: (label-w, 1fr), align: horizon, row-gutter: 0.1in,
      text(font: display, weight: "bold", size: size, n),
      stack(dir: ltr, spacing: 8pt, ..range(circles).map(_ => circle(radius: r, stroke: 1.4pt + ink))))
    v(0.08in)
  }
})

// Jogo dos erros: "antes" em cima, "depois" embaixo (imagens de inputs/puzzle-assets, mesma proporção),
// rótulos BEFORE / AFTER e caixinha com N círculos para a criança marcar as diferenças achadas.
#let spot-diff(before, after, n, w: 100%) = {
  let lab(t) = block(above: 0.08in, below: 0.05in, sticky: true, _kicker(size: 11pt, t))
  let pic(f) = block(width: w, stroke: 1.4pt + ink, radius: 4pt, clip: true, image(_pz + f, width: 100%))
  lab[Before]
  pic(before)
  lab[After]
  pic(after)
  v(0.1in)
  block(width: 100%, breakable: false, stroke: 1.6pt + ink, radius: 10pt, inset: (x: 14pt, y: 9pt),
    grid(columns: (auto, 1fr), column-gutter: 14pt, align: horizon,
      text(font: display, weight: "bold", size: 13pt, tracking: 0.04em, upper[Differences found:]),
      stack(dir: ltr, spacing: 12pt, ..range(n).map(_ => circle(radius: 0.15in, stroke: 1.4pt + ink)))))
}

// Quadro comparativo simples: cabeçalho + linhas (cada linha = array de conteúdos), 1ª coluna em negrito.
#let compare-table(head, ..rows) = block(width: 100%, above: 0.1in, breakable: false,
  table(columns: (0.8fr, 1.1fr, 1.3fr), stroke: 1.2pt + ink, inset: (x: 9pt, y: 7pt), align: left + horizon,
    fill: (_, y) => if y == 0 { tint } else { none },
    ..head.map(h => text(font: display, size: 11pt, weight: "bold", tracking: 0.04em, upper(h))),
    ..rows.pos().flatten().enumerate().map(((i, c)) => if calc.rem(i, 3) == 0 { text(weight: "bold", size: 12.5pt, c) } else { text(size: 12.5pt, c) })))

// Legenda de símbolos de um sudoku: itens (arquivo-em-puzzle-assets, rótulo). Cada símbolo em caixa de altura fixa + rótulo.
#let symbol-key(..items) = block(width: 100%, above: 0.1in, below: 0.14in, breakable: false,
  stroke: 1.4pt + ink, radius: 8pt, inset: (x: 14pt, y: 10pt), {
    _kicker(size: 10pt)[Symbol key]
    v(0.06in)
    grid(columns: (1fr,) * items.pos().len(), column-gutter: 8pt, align: center + top,
      ..items.pos().map(((f, l)) => stack(spacing: 6pt,
        box(height: 0.62in, width: 100%, align(center + horizon, image(_pz + f, height: 100%, fit: "contain"))),
        text(font: display, size: 12pt, weight: "bold", tracking: 0.03em, upper(l)))))
  })

// Hanukkiah desenhada em código (P&B, escala por `w`). 9 posições; a central (4) é o shamash.
// Noite n: n velas, a partir da direita (como no Family Pack). `shamash: true` = vela do shamash acesa e mais alta.
// `empty: true` = só a base e os suportes (shamash em pedestal mais alto), para a criança desenhar as velas.
// Geometria igual à do bonus/family-pack.typ (proporções de 2.3in de largura x 0.82in de altura), multiplicada por w/2.3in.
#let hanukkiah-draw(n, w: 2.3in, empty: false, shamash: true) = {
  let k = w / 2.3in
  let order = (8, 7, 6, 5, 3, 2, 1, 0)
  let lit = order.slice(0, n)
  let step = w / 9
  let cw = 0.1in * k
  let ch = 0.3in * k
  let base = 0.64in * k
  let sw = calc.max(1.2pt, 1.2pt * calc.min(k, 1.6))
  let fl(fw, fh) = polygon(fill: white, stroke: sw + ink,
    (0.5 * fw, 0pt), (0.78 * fw, 0.42 * fh), (fw, 0.7 * fh), (0.78 * fw, 0.95 * fh), (0.5 * fw, fh),
    (0.22 * fw, 0.95 * fh), (0pt, 0.7 * fh), (0.22 * fw, 0.42 * fh))
  box(width: w, height: 0.82in * k, {
    place(left + top, dy: base, dx: 0.04 * w, rect(width: 0.92 * w, height: 0.045in * k, fill: ink, radius: 2pt))
    place(left + top, dy: base + 0.045in * k, dx: w / 2 - 0.2in * k, rect(width: 0.4in * k, height: 0.05in * k, fill: ink, radius: 2pt))
    for i in range(9) {
      let x = step * i + step / 2 - cw / 2
      if empty {
        if i == 4 {
          place(left + top, dx: x - cw * 0.25, dy: base - 0.2in * k, rect(width: cw * 1.5, height: 0.2in * k, fill: white, stroke: sw + ink))
        } else {
          place(left + top, dx: x - cw * 0.25, dy: base - 0.07in * k, rect(width: cw * 1.5, height: 0.07in * k, fill: white, stroke: sw + ink))
        }
      } else if i == 4 {
        if shamash {
          place(left + top, dx: x, dy: base - 0.42in * k, rect(width: cw, height: 0.42in * k, fill: white, stroke: 1.1 * sw + ink))
          place(left + top, dx: x - 0.005in * k, dy: base - 0.42in * k - 0.19in * k, fl(0.11in * k, 0.17in * k))
        }
      } else if i in lit {
        place(left + top, dx: x, dy: base - ch, rect(width: cw, height: ch, fill: white, stroke: sw + ink))
        place(left + top, dx: x - 0.005in * k, dy: base - ch - 0.18in * k, fl(0.11in * k, 0.17in * k))
      } else {
        place(left + top, dx: x, dy: base - 0.06in * k, rect(width: cw, height: 0.06in * k, fill: white, stroke: sw + ink))
      }
    }
  })
}

// QR code do bônus (página final). Enquanto não houver arte, mostra a caixa tracejada vazia do mesmo tamanho.
#let has-bonus-qr = true  // QR do formulário Brevo "Hanukkah 8 Nights" (inputs/bonus-qr.png, 06/10/2026)
#let bonus-qr(w: 1.6in) = if has-bonus-qr {
  image("/books/hanukkah-8-nights/inputs/bonus-qr.png", width: w, height: w, fit: "contain")
} else {
  // Rótulo TEMPORÁRIO (some quando has-bonus-qr = true): evita que a caixa vazia pareça falha no PDF de revisão.
  box(width: w, height: w, stroke: (paint: ink, thickness: 1.6pt, dash: "dashed"), radius: 8pt,
    align(center + horizon, text(font: display, weight: "bold", size: 16pt, tracking: 0.06em, upper[QR code])))
}

// ---------------------------------------------------------------- answer key (content/answer-key.typ)
// Faixa de noite: selo "NIGHT n" + título da noite + filete.
#let ak-night(n, title) = block(width: 100%, above: 0.2in, below: 0.12in, sticky: true,
  grid(columns: (auto, auto, 1fr), column-gutter: 10pt, align: horizon,
    box(fill: ink, radius: 8pt, inset: (x: 10pt, top: 4.5pt, bottom: 5.5pt),
      text(fill: white, font: display, size: 12pt, weight: "bold", tracking: 0.14em)[NIGHT #n]),
    text(font: display, size: 14pt, weight: "bold", tracking: 0.04em, upper(title)),
    line(length: 100%, stroke: 1.2pt + soft)))

// Cartão de resposta: título "Night N · ★ Título" (level 1 = ★, 2 = ★★, 0 = sem estrela; o título é o mesmo texto impresso na noite)
// + corpo. `tall: true` reserva 2 linhas de título para alinhar os corpos de cartões lado a lado.
#let ak-card(n, level, title, body, tall: true) = block(width: 100%, breakable: false, {
  let stars = ("", "★ ", "★★ ").at(level)
  block(width: 100%, height: if tall { 0.4in } else { auto }, below: 0.06in,
    text(font: display, size: 11.5pt, weight: "bold", tracking: 0.03em, upper("Night " + str(n) + " · " + stars + title)))
  body
})

// Grade de cartões (2 por linha por padrão; 3 para itens pequenos; `cols` também aceita um array de larguras). Use grid.cell(rowspan: 2, ...) quando um cartão alto cobrir duas linhas.
#let ak-grid(cols: 2, ..cells) = grid(columns: if type(cols) == int { (1fr,) * cols } else { cols }, column-gutter: 0.25in, row-gutter: 0.2in,
  align: top + left, ..cells)

// Imagem de gabarito (inputs/puzzle-assets), largura da célula, com filete fino opcional.
#let ak-img(file, frame: false, w: 100%) = block(width: w, stroke: if frame { 1pt + ink } else { none }, radius: 3pt, clip: true,
  image(_pz + file, width: 100%))

// Labirinto resolvido + rótulos (entrada → saída) lidos do <nome>_gabarito.json.
#let ak-maze(name, w: 100%) = {
  let d = json(_pz + name + "_gabarito.json")
  stack(spacing: 5pt, image(_pz + name + "_gabarito_key.png", width: w),
    text(font: display, size: 11pt, weight: "bold", tracking: 0.04em, upper(d.rotulo_inicio + " → " + d.rotulo_fim)))
}

// Resposta grande (ex.: "Jar C").
#let ak-big(t) = text(font: display, size: 20pt, weight: "bold", tracking: 0.03em, t)

// Lista de respostas numeradas: pares (rótulo, conteúdo).
#let ak-list(size: 12.5pt, ..items) = grid(columns: (auto, 1fr), column-gutter: 9pt, row-gutter: 7pt, align: (right + top, left + top),
  ..items.pos().map(((l, b)) => (text(font: display, weight: "bold", size: size, l), text(size: size, b))).flatten())

// Origem da resposta (ex.: "Night 4") em cinza, 11pt.
#let ak-src(t) = text(size: 11pt, fill: mid)[(#t)]

// ---------------------------------------------------------------- front matter (sobrescreve title-page/plain-page do lib.typ)
// Página de título: pedido do texto aprovado, "hanukkiah simples com uma vela acesa abaixo do título" (33.png).
#let title-page(title, subtitle: none, author: none, imprint: none) = {
  page(header: none, footer: none)[
    #set par(justify: false, first-line-indent: 0em)
    #v(1.1in)
    #align(center, text(font: display, size: 44pt, weight: "bold", tracking: 0.01em, title))
    #if subtitle != none { v(0.22in); align(center, text(size: 17pt, fill: mid, subtitle)) }
    #v(0.45in)
    #align(center, image(_ill + "33.png", width: 3.6in))
    #v(1fr)
    #if author != none { align(center, text(font: display, size: 18pt, weight: "bold", tracking: 0.12em, upper(author))) }
    #if imprint != none { v(0.12in); align(center, text(size: 11pt, imprint)) }
    #v(0.45in)
  ]
}

// Páginas de matter em Markdown (how-to-use): mesmo estilo das noites, texto maior, títulos em Barlow.
#let plain-page(body) = page(header: none, footer: none)[
  #set heading(outlined: false)
  #set text(size: 14.5pt)
  #set par(leading: 0.85em, spacing: 1.25em, justify: false, first-line-indent: 0em)
  #show heading.where(level: 1): it => {
    [#metadata("end") <chap-end>]
    set par(justify: false, first-line-indent: 0em)
    block(width: 100%, above: 0pt, below: 0.28in, text(font: display, size: 32pt, weight: "bold", it.body))
  }
  #body
]

// Página de copyright centrada na página (pedido do Danilo, 07/10/2026); sobrescreve o copyright-page do lib.typ.
#let copyright-page(body) = page(header: none, footer: none)[
  #set par(justify: false, first-line-indent: 0em, spacing: 1.1em)
  #set text(size: 11.5pt)
  #align(center + horizon, block(width: 5.6in, body))
]
