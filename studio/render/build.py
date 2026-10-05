"""Monta o main.typ a partir do book.yaml + content/ e compila o PDF do miolo."""
from __future__ import annotations

import json
from pathlib import Path

import typst
import yaml

from .. import kdp
from ..book import ROOT, Book
from ..generators import calendar as cal
from ..generators import sudoku, wordsearch
from .markdown import convert, inline

FONTS_DIR = ROOT / "fonts"

SERIF = ["Literata", "Source Serif 4", "Libertinus Serif"]
SANS = ["Atkinson Hyperlegible Next", "Atkinson Hyperlegible", "Verdana", "Arial", "DejaVu Sans"]

# Presets por tipo; imprint e book.yaml (style:) sobrescrevem nessa ordem.
PRESETS = {
    "prose": dict(trim="6x9", size=11.5, leading=0.7, justify=True, indent=True, body_font=SERIF,
                  heading_font=SERIF, chapter_start="odd", running_heads=True, top=0.75, bottom=0.75,
                  outside=0.6, inside=None),
    "activity": dict(trim="8.5x11", size=16, leading=0.8, justify=False, indent=False, body_font=SANS,
                     heading_font=SANS, chapter_start="any", running_heads=False, top=0.6, bottom=0.6,
                     outside=0.5, inside=None),
    "calendar": dict(trim="8.5x11", size=12, leading=0.7, justify=False, indent=False, body_font=SANS,
                     heading_font=SANS, chapter_start="any", running_heads=False, top=0.5, bottom=0.5,
                     outside=0.5, inside=None),
    "planner": dict(trim="8.5x11", size=12, leading=0.7, justify=False, indent=False, body_font=SANS,
                    heading_font=SANS, chapter_start="any", running_heads=False, top=0.5, bottom=0.5,
                    outside=0.5, inside=None),
    "children": dict(trim="8.5x8.5", size=18, leading=0.8, justify=False, indent=False,
                     body_font=["Andika"] + SANS, heading_font=["Andika"] + SANS, chapter_start="any",
                     running_heads=False, folios=False, top=0.6, bottom=0.6, outside=0.6, inside=None,
                     bleed=True),
}
IMPRINTS = {
    # Golden Chapter: sempre letra grande (público 65+)
    "golden-chapter": dict(size_min=16, body_font=SANS, heading_font=SANS, justify=False, indent=False),
}


def resolve_style(meta: dict, est_pages: int = 150) -> dict:
    st = dict(PRESETS[meta.get("type", "prose")])
    imp = IMPRINTS.get(meta.get("imprint", ""), {})
    size_min = imp.get("size_min")
    st.update({k: v for k, v in imp.items() if k != "size_min"})
    if meta.get("large_print"):
        size_min = max(size_min or 0, 16)
    st.update(meta.get("style") or {})
    for k in ("trim", "bleed"):
        if meta.get(k) is not None:
            st[k] = meta[k]
    if size_min and st["size"] < size_min:
        st["size"] = size_min
    st.setdefault("bleed", False)
    st.setdefault("folios", True)
    if not st.get("inside"):
        st["inside"] = max(kdp.gutter_for_pages(est_pages) + 0.125, 0.5)
    min_out = kdp.MIN_OUTSIDE_MARGIN_BLEED if st["bleed"] else kdp.MIN_OUTSIDE_MARGIN_NO_BLEED
    st["outside"] = max(st["outside"], min_out)
    return st


def _fonts(lst) -> str:
    return "(" + ", ".join(json.dumps(f) for f in lst) + ",)"


def _s(x) -> str:
    return json.dumps(x, ensure_ascii=False)


def _ensure_generated(book: Book, unit: dict) -> dict:
    """Gera grids/puzzles que faltam e grava de volta no YAML (determinístico por seed)."""
    f = book.unit_file(unit)
    data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    kind = unit["kind"]
    changed = False
    base = int(data.get("seed", sum(map(ord, unit["id"]))))
    if kind == "wordsearch":
        for i, p in enumerate(data.get("puzzles", [])):
            if "grid" not in p:
                g = wordsearch.generate(p["words"], size=p.get("size", data.get("size", 15)),
                                        level=p.get("level", data.get("level", "easy")), seed=base + i)
                p.update(grid=g["grid"], placements=g["placements"], size=g["size"], level=g["level"])
                changed = True
    elif kind == "sudoku":
        puzzles = data.setdefault("puzzles", [])
        while len(puzzles) < int(data.get("count", 0)):
            i = len(puzzles)
            g = sudoku.generate(level=data.get("level", "easy"), seed=base + i)
            puzzles.append({"title": f"{data.get('title_prefix', 'Sudoku')} {i + 1}", **g})
            changed = True
    if changed:
        f.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    return data


def _md_file(book: Book, name: str) -> Path:
    return book.path("content", name)


def _matter(book: Book, name: str, fn: str = "plain-page") -> list[str]:
    f = _md_file(book, f"_{name}.md")
    if not f.exists():
        return [f'// matter "{name}" ausente: content/_{name}.md']
    body = convert(f.read_text(encoding="utf-8"), image_root=f"/books/{book.slug}/inputs")
    if fn == "section":
        return [body, ""]
    return [f"#{fn}[", body, "]", ""]


def assemble(book: Book, est_pages: int = 150) -> tuple[str, dict]:
    meta = book.meta
    st = resolve_style(meta, est_pages)
    w, h = kdp.page_size(st["trim"], st["bleed"])
    bleed = kdp.BLEED if st["bleed"] else 0
    data_dir = book.build_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    rel = lambda p: "/" + p.relative_to(ROOT).as_posix()  # noqa: E731

    L = ['#import "/studio/render/lib.typ": *', ""]
    L.append(
        "#show: book.with("
        f"page-w: {w}in, page-h: {h}in, bleed: {bleed}in, inside: {st['inside']}in, "
        f"outside: {st['outside']}in, top: {st['top']}in, bottom: {st['bottom']}in, "
        f"body-font: {_fonts(st['body_font'])}, heading-font: {_fonts(st['heading_font'])}, "
        f"size: {st['size']}pt, leading: {st['leading']}em, justify: {str(st['justify']).lower()}, "
        f"indent: {str(st['indent']).lower()}, lang: {_s(meta.get('language', 'en-US').split('-')[0])}, "
        f"title: {_s(meta.get('title', ''))}, running-heads: {str(st['running_heads']).lower()}, "
        f"folios: {str(st['folios']).lower()}, chapter-start: {_s(st['chapter_start'])})"
    )
    L.append("")
    theme = book.path("theme.typ")
    if theme.exists():  # tema visual por livro (inline, para enxergar o lib.typ); define `theme` e helpers
        L += [f"// --- {rel(theme)}", theme.read_text(encoding="utf-8"), "#show: theme", ""]

    front = meta.get("front", ["title", "copyright", "toc"])
    back = meta.get("back", ["answers"])
    for item in front:
        if item == "title":
            L.append(f"#title-page({_s(meta.get('title', ''))}, subtitle: {_s(meta.get('subtitle')) if meta.get('subtitle') else 'none'}, "
                     f"author: {_s(meta.get('author')) if meta.get('author') else 'none'}, "
                     f"imprint: {_s(meta.get('imprint_name')) if meta.get('imprint_name') else 'none'})")
        elif item == "copyright":
            f = _md_file(book, "_copyright.md")
            if f.exists():
                txt = convert(f.read_text(encoding="utf-8"))
            else:
                holder = meta.get("copyright_holder") or meta.get("imprint_name") or meta.get("author", "")
                txt = inline(f"Copyright © {meta.get('year', '')} {holder}. All rights reserved.") + \
                    "\n\n" + inline("No part of this book may be reproduced in any form without written "
                                    "permission from the publisher, except for brief quotations in reviews.")
            L += ["#copyright-page[", txt, "]"]
        elif item == "toc":
            L.append(f"#toc(title: {_s(meta.get('toc_title', 'Contents'))})")
        else:
            L += _matter(book, item)
    L += ["", "#body-start()", ""]

    keys: dict[str, list] = {"wordsearch": [], "sudoku": [], "trivia": []}
    n_puzzle = 0
    for u in book.units:
        kind = u.get("kind", "prose")
        f = book.unit_file(u)
        if not f.exists():
            L.append(f"// UNIDADE AUSENTE: {u['id']}")
            continue
        if kind == "typst":
            # inline (não #include) para herdar o import do lib.typ; caminhos de imagem absolutos: /books/<slug>/inputs/...
            L += [f"// --- {rel(f)}", f.read_text(encoding="utf-8"), ""]
            continue
        if kind == "prose":
            md = f.read_text(encoding="utf-8")
            if not md.lstrip().startswith("# "):
                md = f"# {u.get('title', u['id'])}\n\n" + md
            L += [convert(md, image_root=f"/books/{book.slug}/inputs"), ""]
            continue
        data = _ensure_generated(book, u)
        jf = data_dir / f"{u['id']}.json"
        jf.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        var = "d_" + u["id"].replace("-", "_")
        L.append(f'#let {var} = json("{rel(jf)}")')
        title = u.get("title", u["id"])
        if u.get("section_page", kind in ("wordsearch", "sudoku")) and kind in ("wordsearch", "sudoku"):
            sub = f", subtitle: {_s(data['intro'])}" if data.get("intro") else ""
            L.append(f"#section-page({_s(title)}{sub})")
        if kind == "wordsearch":
            for i, p in enumerate(data["puzzles"]):
                n_puzzle += 1
                L.append(f"#wordsearch({var}.puzzles.at({i}).title, {var}.puzzles.at({i}).grid, "
                         f"{var}.puzzles.at({i}).words, number: {n_puzzle}"
                         + (f", intro: {var}.puzzles.at({i}).intro" if p.get("intro") else "") + ")")
                keys["wordsearch"].append((n_puzzle, p["title"], p["grid"], wordsearch.solution_cells(p)))
        elif kind == "sudoku":
            for i, p in enumerate(data["puzzles"]):
                n_puzzle += 1
                L.append(f"#sudoku({var}.puzzles.at({i}).title, {var}.puzzles.at({i}).puzzle, number: {n_puzzle})")
                keys["sudoku"].append((n_puzzle, p["title"], p["puzzle"], p["solution"]))
        elif kind == "trivia":
            intro = f", intro: {var}.intro" if data.get("intro") else ""
            L.append(f"#trivia({_s(title)}, {var}.questions{intro})")
            keys["trivia"].append((title, u["id"], var))
        elif kind == "calendar":
            yr = cal.build_year(int(data["year"]), data.get("week_start", "sunday"),
                                us=data.get("us_holidays", True), jewish=data.get("jewish", False),
                                months=data.get("months"))
            jf.write_text(json.dumps({**data, **yr}, ensure_ascii=False), encoding="utf-8")
            wd = data.get("weekday_names") or (["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
                                               if yr["week_start"] == "sunday"
                                               else ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
            L.append(f"#for m in {var}.months [#month-page(m.name, {var}.year, m.weeks, m.days, "
                     f"weekday-names: {_fonts(wd)})]")
        elif kind == "pictures":
            for i, pg in enumerate(data["pages"]):
                img = pg["image"] if pg["image"].startswith("/") else f"/books/{book.slug}/inputs/{pg['image']}"
                body = f"[{inline(pg['text'])}]" if pg.get("text") else "none"
                L.append(f"#picture-page({_s(img)}, body: {body}, mode: {_s(pg.get('mode', 'full'))})")
        else:
            raise ValueError(f"kind desconhecido: {kind}")
        L.append("")

    for item in back:
        if item == "answers":
            if not any(keys.values()):
                continue
            kf = data_dir / "_keys.json"
            kf.write_text(json.dumps({
                "wordsearch": [dict(n=n, title=t, grid=g, cells=c) for n, t, g, c in keys["wordsearch"]],
                "sudoku": [dict(n=n, title=t, puzzle=p, solution=s) for n, t, p, s in keys["sudoku"]],
            }, ensure_ascii=False), encoding="utf-8")
            L.append(f'#let keys = json("{rel(kf)}")')
            L.append(f"#answer-keys(title: {_s(meta.get('answers_title', 'Answer Key'))})[")
            if keys["wordsearch"]:
                L.append("#key-grid(cols: 2, keys.wordsearch.map(k => wordsearch-key(k.title, k.grid, k.cells, number: k.n)))")
            if keys["sudoku"]:
                L.append("#key-grid(cols: 3, keys.sudoku.map(k => sudoku-key(k.title, k.puzzle, k.solution, number: k.n)))")
            for title, _uid, var in keys["trivia"]:
                L.append(f"#trivia-key({_s(title)}, {var}.questions)")
            L.append("]")
        else:
            L += _matter(book, item)
    return "\n".join(L) + "\n", st


def build(book: Book, preview: str | None = None, ppi: int = 50) -> dict:
    """Compila o miolo. Faz 2 passadas: a 1ª mede o nº de páginas para acertar a margem interna."""
    book.build_dir.mkdir(parents=True, exist_ok=True)
    main = book.build_dir / "main.typ"
    pdf = book.build_dir / f"{book.slug}-interior.pdf"
    fonts = [str(FONTS_DIR)] if FONTS_DIR.exists() else []
    pages = 150
    st: dict = {}
    for _ in range(2):
        src, st = assemble(book, est_pages=pages)
        main.write_text(src, encoding="utf-8")
        typst.compile(str(main), output=str(pdf), root=str(ROOT), font_paths=fonts)
        from pypdf import PdfReader
        new_pages = len(PdfReader(str(pdf)).pages)
        if kdp.gutter_for_pages(new_pages) == kdp.gutter_for_pages(pages):
            pages = new_pages
            break
        pages = new_pages
    out = {"pdf": str(pdf), "pages": pages, "style": st}
    if preview:
        out["previews"] = render_previews(book, main, fonts, preview, ppi)
    return out


def render_previews(book: Book, main: Path, fonts: list[str], spec: str, ppi: int) -> list[str]:
    """PNGs de páginas selecionadas (ex.: "1-4,10,last") para inspeção visual barata."""
    imgs = typst.compile(str(main), format="png", ppi=ppi, root=str(ROOT), font_paths=fonts)
    if isinstance(imgs, bytes):
        imgs = [imgs]
    n = len(imgs)
    wanted: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if part == "last":
            wanted.add(n)
        elif "-" in part:
            a, b = part.split("-")
            wanted.update(range(int(a), min(int(b), n) + 1))
        elif part == "all":
            wanted.update(range(1, n + 1))
        elif part:
            wanted.add(int(part))
    pdir = book.build_dir / "preview"
    pdir.mkdir(exist_ok=True)
    for old in pdir.glob("*.png"):
        old.unlink()
    paths = []
    for i in sorted(wanted):
        if 1 <= i <= n:
            p = pdir / f"p{i:03d}.png"
            p.write_bytes(imgs[i - 1])
            paths.append(str(p))
    return paths
