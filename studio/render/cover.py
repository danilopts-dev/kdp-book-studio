"""Capa: cálculo de lombada, PDF-guia (para Canva/Flow) e montagem da capa completa se houver arte."""
from __future__ import annotations

import json

import typst

from .. import kdp
from ..book import ROOT, Book
from .build import FONTS_DIR, resolve_style


def _find(book: Book, stem: str):
    for ext in (".png", ".jpg", ".jpeg", ".pdf"):
        p = book.path("inputs", stem + ext)
        if p.exists():
            return p
    return None


def build_cover(book: Book, pages: int) -> dict:
    meta = book.meta
    st = resolve_style(meta, pages)
    paper = meta.get("paper", "bw-white")
    c = kdp.cover_size(st["trim"], pages, paper)
    cov = meta.get("cover") or {}
    front, back = _find(book, "cover-front"), _find(book, "cover-back")
    b = kdp.BLEED
    W, H, S, TW = (round(c[k], 4) for k in ("width", "height", "spine", "trim_w"))
    spine_x = round(b + TW, 4)
    front_x = round(spine_x + S, 4)
    rel = lambda p: "/" + p.relative_to(ROOT).as_posix()  # noqa: E731

    guide_lines = f"""
#let g(x0, y0, x1, y1, col) = place(top + left, line(start: (x0 * 1in, y0 * 1in), end: (x1 * 1in, y1 * 1in), stroke: 0.6pt + col))
#g(0, {b}, {W}, {b}, red)
#g(0, {H - b}, {W}, {H - b}, red)
#g({b}, 0, {b}, {H}, red)
#g({W - b}, 0, {W - b}, {H}, red)
#g({spine_x}, 0, {spine_x}, {H}, blue)
#g({front_x}, 0, {front_x}, {H}, blue)
#place(top + left, dx: {b + 0.25}in, dy: {b + 0.25}in, rect(width: {TW - 0.5}in, height: {H - 2 * b - 0.5}in, stroke: (paint: green, dash: "dashed")))
#place(top + left, dx: {front_x + 0.25}in, dy: {b + 0.25}in, rect(width: {TW - 0.5}in, height: {H - 2 * b - 0.5}in, stroke: (paint: green, dash: "dashed")))
"""
    info = (f"Capa completa {W:.4f} x {H:.4f} in  |  lombada {S:.4f} in ({pages} pág., {paper})  |  "
            f"vermelho = corte, azul = lombada, verde = área segura")
    guide = f"""#set page(width: {W}in, height: {H}in, margin: 0in)
#set text(font: "DejaVu Sans", size: 9pt)
#place(top + left, dx: {b}in, dy: {H / 2}in, box(width: {TW}in, align(center, text(size: 20pt, fill: gray)[CONTRACAPA])))
#place(top + left, dx: {front_x}in, dy: {H / 2}in, box(width: {TW}in, align(center, text(size: 20pt, fill: gray)[FRENTE])))
#place(bottom + left, dx: 0.3in, dy: -0.3in, text("{info}"))
{guide_lines}
"""
    out_dir = book.build_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    fonts = [str(FONTS_DIR)] if FONTS_DIR.exists() else []
    gsrc = out_dir / "cover-guide.typ"
    gsrc.write_text(guide, encoding="utf-8")
    gpdf = out_dir / f"{book.slug}-cover-guide.pdf"
    typst.compile(str(gsrc), output=str(gpdf), root=str(ROOT), font_paths=fonts)
    result = {**{k: round(v, 4) if isinstance(v, float) else v for k, v in c.items()},
              "pages": pages, "paper": paper, "guide_pdf": str(gpdf)}

    if front:
        bg = cov.get("background", "#ffffff")
        spine_txt = cov.get("spine_text") or f"{meta.get('title', '')}   {meta.get('imprint_name', '')}"
        spine_font = json.dumps(cov.get("spine_font", st["heading_font"][0]))
        spine_col = cov.get("spine_color", "#000000")
        back_part = (f'#place(top + left, image("{rel(back)}", width: {b + TW}in, height: {H}in, fit: "cover"))'
                     if back else "")
        spine_part = ""
        if c["spine_text_allowed"] and cov.get("spine_text", True) is not False:
            spine_part = (f"#place(top + left, dx: {spine_x}in, dy: 0in, box(width: {S}in, height: {H}in, "
                          f"align(center + horizon, rotate(90deg, reflow: true, text(font: {spine_font}, "
                          f"size: {min(S * 72 * 0.5, 14):.1f}pt, fill: rgb(\"{spine_col}\"), "
                          f"{json.dumps(spine_txt)})))))")
        wrap = f"""#set page(width: {W}in, height: {H}in, margin: 0in, fill: rgb("{bg}"))
{back_part}
#place(top + left, dx: {front_x}in, image("{rel(front)}", width: {TW + b}in, height: {H}in, fit: "cover"))
{spine_part}
"""
        wsrc = out_dir / "cover.typ"
        wsrc.write_text(wrap, encoding="utf-8")
        wpdf = out_dir / f"{book.slug}-cover.pdf"
        typst.compile(str(wsrc), output=str(wpdf), root=str(ROOT), font_paths=fonts)
        result["cover_pdf"] = str(wpdf)
        if not c["spine_text_allowed"]:
            result["note"] = f"Sem texto na lombada: KDP exige {kdp.SPINE_TEXT_MIN_PAGES}+ páginas."
    return result
