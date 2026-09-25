"""Checagens determinísticas (sem LLM). Severidade no padrão do kdp-editorial-review.

🔴 CRITICAL bloqueia a publicação; 🟠 MAJOR deve ser corrigido; 🟡 MINOR / 🔵 RECOMMENDATION informativos.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import yaml

from .. import kdp
from ..book import Book
from ..generators import sudoku, wordsearch

CRIT, MAJ, MIN, REC = "🔴 CRITICAL", "🟠 MAJOR", "🟡 MINOR", "🔵 RECOMMENDATION"
PLACEHOLDER = re.compile(r"\[DANILO[^\]]*\]|\bTODO\b|\bTBD\b|lorem ipsum|INSERT HERE|\bXXX\b|\{\{.*?\}\}", re.I)


def _f(sev, where, msg):
    return {"sev": sev, "where": where, "msg": msg}


def check_content(book: Book, unit_id: str | None = None) -> list[dict]:
    out = []
    meta = book.meta
    units = [u for u in book.units if unit_id in (None, u["id"])]
    if not units:
        out.append(_f(CRIT, "book.yaml", "Nenhuma unidade definida (units:)." if unit_id is None
                      else f"Unidade '{unit_id}' não existe."))
    ids = [u["id"] for u in book.units]
    for dup in [k for k, v in Counter(ids).items() if v > 1]:
        out.append(_f(CRIT, "book.yaml", f"id de unidade duplicado: {dup}"))
    seen_paras: dict[str, str] = {}
    for u in units:
        f = book.unit_file(u)
        where = f"content/{f.name}"
        if not f.exists() or not f.read_text(encoding="utf-8").strip():
            out.append(_f(CRIT, where, "Unidade sem conteúdo."))
            continue
        txt = f.read_text(encoding="utf-8")
        for m in PLACEHOLDER.finditer(txt):
            out.append(_f(CRIT, where, f"Placeholder/pendência no texto: {m.group(0)[:80]}"))
        kind = u.get("kind", "prose")
        if kind == "prose":
            words = len(re.findall(r"\b\w+\b", txt))
            tgt = u.get("target_words")
            if tgt and not (0.6 * tgt <= words <= 1.5 * tgt):
                out.append(_f(MIN, where, f"{words} palavras; alvo {tgt} (fora de ±40/50%)."))
            for para in [p.strip() for p in txt.split("\n\n") if len(p.strip()) > 80]:
                key = re.sub(r"\W+", " ", para.lower())
                if key in seen_paras:
                    out.append(_f(MAJ, where, f"Parágrafo repetido (também em {seen_paras[key]}): {para[:60]}…"))
                seen_paras[key] = where
        else:
            try:
                data = yaml.safe_load(txt) or {}
            except yaml.YAMLError as e:
                out.append(_f(CRIT, where, f"YAML inválido: {e}"))
                continue
            out += _check_activity(kind, data, where, meta)
    for item in meta.get("front", []) + meta.get("back", []):
        if item not in ("title", "copyright", "toc", "answers") and not book.path("content", f"_{item}.md").exists():
            out.append(_f(CRIT, f"content/_{item}.md", f"Seção '{item}' listada em front/back mas o arquivo não existe."))
    return out


def _check_activity(kind: str, data: dict, where: str, meta: dict) -> list[dict]:
    out = []
    if kind == "wordsearch":
        titles = Counter(p.get("title") for p in data.get("puzzles", []))
        for t, n in titles.items():
            if n > 1:
                out.append(_f(MAJ, where, f"Título de puzzle repetido: {t}"))
        for i, p in enumerate(data.get("puzzles", []), 1):
            w = f"{where} #{i} {p.get('title', '')}"
            words = p.get("words", [])
            norm = [wordsearch.normalize(x) for x in words]
            for dup in [k for k, v in Counter(norm).items() if v > 1]:
                out.append(_f(CRIT, w, f"Palavra duplicada na lista: {dup}"))
            if any(len(x) < 3 for x in norm):
                out.append(_f(MIN, w, "Palavras com menos de 3 letras."))
            if "grid" not in p:
                continue  # ainda não gerado; o build gera
            rows = p["grid"]
            if len(set(map(len, rows))) != 1 or len(rows) != len(rows[0]):
                out.append(_f(CRIT, w, "Grid não é quadrado."))
            dirs = wordsearch.LEVELS[p.get("level", "easy")]
            for word, gw in zip(words, norm):
                n = wordsearch.count_occurrences(rows, gw, list(wordsearch.DIRECTIONS))
                if n == 0:
                    out.append(_f(CRIT, w, f"Palavra da lista não está no grid: {word}"))
                elif n > 1:
                    out.append(_f(MAJ, w, f"Palavra aparece {n}x no grid (ambíguo): {word}"))
                elif wordsearch.count_occurrences(rows, gw, dirs) == 0:
                    out.append(_f(CRIT, w, f"'{word}' só aparece numa direção fora do nível '{p.get('level')}'."))
    elif kind == "sudoku":
        for i, p in enumerate(data.get("puzzles", []), 1):
            w = f"{where} #{i}"
            if not sudoku.is_valid_solution(p["solution"]):
                out.append(_f(CRIT, w, "Solução inválida."))
            if any(a != "." and a != b for pr, sr in zip(p["puzzle"], p["solution"]) for a, b in zip(pr, sr)):
                out.append(_f(CRIT, w, "Puzzle não bate com a solução (answer key errada)."))
            if sudoku.count_solutions(sudoku.parse(p["puzzle"])) != 1:
                out.append(_f(CRIT, w, "Sudoku sem solução única."))
    elif kind == "trivia":
        qs = data.get("questions", [])
        if not qs:
            out.append(_f(CRIT, where, "Sem perguntas."))
        seen = Counter(re.sub(r"\W+", " ", q.get("q", "").lower()).strip() for q in qs)
        for q, n in seen.items():
            if n > 1:
                out.append(_f(CRIT, where, f"Pergunta repetida: {q[:60]}"))
        pos = Counter()
        for i, q in enumerate(qs, 1):
            if not q.get("answer"):
                out.append(_f(CRIT, where, f"Pergunta {i} sem resposta."))
            opts = q.get("options")
            if opts:
                if q.get("answer") not in opts:
                    out.append(_f(CRIT, where, f"Pergunta {i}: resposta não está entre as opções."))
                else:
                    pos[opts.index(q["answer"])] += 1
                if len(set(opts)) != len(opts):
                    out.append(_f(MAJ, where, f"Pergunta {i}: opções duplicadas."))
            if not q.get("source") and meta.get("require_sources", True):
                out.append(_f(MIN, where, f"Pergunta {i} sem 'source' (fato não verificado)."))
        if pos and len(qs) >= 8 and max(pos.values()) > 0.45 * sum(pos.values()):
            out.append(_f(MAJ, where, f"Respostas concentradas numa mesma letra: {dict(pos)}"))
    return out


def check_pdf(book: Book) -> list[dict]:
    from pypdf import PdfReader

    out = []
    pdf = book.build_dir / f"{book.slug}-interior.pdf"
    if not pdf.exists():
        return [_f(CRIT, "build", "PDF não gerado. Rode `python -m studio build`.")]
    from ..render.build import resolve_style
    r = PdfReader(str(pdf))
    n = len(r.pages)
    st = resolve_style(book.meta, n)
    w, h = kdp.page_size(st["trim"], st["bleed"])
    if n < kdp.MIN_PAGES:
        out.append(_f(CRIT, "PDF", f"{n} páginas; mínimo KDP é {kdp.MIN_PAGES}."))
    if n > kdp.MAX_PAGES:
        out.append(_f(CRIT, "PDF", f"{n} páginas; acima do máximo KDP."))
    if n % 2:
        out.append(_f(REC, "PDF", f"{n} páginas (ímpar); o KDP adiciona uma página em branco no fim."))
    for i, p in enumerate(r.pages, 1):
        pw, ph = float(p.mediabox.width) / 72, float(p.mediabox.height) / 72
        if abs(pw - w) > 0.01 or abs(ph - h) > 0.01:
            out.append(_f(CRIT, f"p.{i}", f"Tamanho {pw:.3f}x{ph:.3f}in; esperado {w:.3f}x{h:.3f}in."))
            break
    fonts, unembedded = set(), set()
    for p in r.pages:
        res = p.get("/Resources") or {}
        for fobj in (res.get("/Font") or {}).values():
            fo = fobj.get_object()
            name = str(fo.get("/BaseFont", "?")).split("+")[-1]
            fonts.add(name)
            desc = fo.get("/FontDescriptor")
            if desc is None and "/DescendantFonts" in fo:
                desc = fo["/DescendantFonts"][0].get_object().get("/FontDescriptor")
            desc = desc.get_object() if desc is not None else {}
            if not any(k in desc for k in ("/FontFile", "/FontFile2", "/FontFile3")):
                unembedded.add(name)
    if unembedded:
        out.append(_f(CRIT, "PDF", f"Fontes não embutidas: {sorted(unembedded)}"))
    wanted = st["body_font"][0]
    if not any(wanted.replace(" ", "") in f for f in fonts):
        out.append(_f(MAJ, "PDF", f"Fonte preferida '{wanted}' não foi usada (fallback: {sorted(fonts)}). "
                                  "Coloque o .ttf em fonts/ ou ajuste style.body_font."))
    if st["size"] < kdp.MIN_FONT_PT:
        out.append(_f(CRIT, "estilo", f"Corpo {st['size']}pt abaixo do mínimo KDP."))
    if book.meta.get("large_print") and st["size"] < 16:
        out.append(_f(CRIT, "estilo", "Livro 'large print' com corpo abaixo de 16pt."))
    out += check_images(book, st)
    return out


def check_images(book: Book, st: dict) -> list[dict]:
    out = []
    inputs = book.path("inputs")
    if not inputs.exists():
        return out
    try:
        from PIL import Image
    except ImportError:
        return [_f(MIN, "imagens", "Pillow não instalado; DPI não verificado.")]
    tw, th = kdp.page_size(st["trim"], st["bleed"])
    for img in sorted(inputs.glob("*")):
        if img.suffix.lower() not in (".png", ".jpg", ".jpeg", ".tif", ".tiff"):
            continue
        with Image.open(img) as im:
            px_w, px_h = im.size
        dpi_full = min(px_w / tw, px_h / th)
        dpi_text = px_w / (tw - st["inside"] - st["outside"])
        if dpi_full < kdp.MIN_IMAGE_DPI and dpi_text < kdp.MIN_IMAGE_DPI:
            out.append(_f(MAJ, f"inputs/{img.name}", f"{px_w}x{px_h}px: ~{dpi_text:.0f} DPI na largura do texto "
                                                     f"(mínimo {kdp.MIN_IMAGE_DPI})."))
        elif dpi_full < kdp.MIN_IMAGE_DPI:
            out.append(_f(MIN, f"inputs/{img.name}", f"OK para largura do texto, mas só {dpi_full:.0f} DPI em página inteira."))
    return out


def report(findings: list[dict], title: str) -> str:
    order = [CRIT, MAJ, MIN, REC]
    lines = [f"# {title}", ""]
    if not findings:
        return "\n".join(lines + ["Nenhum problema encontrado.", ""])
    for sev in order:
        items = [f for f in findings if f["sev"] == sev]
        if items:
            lines.append(f"## {sev} ({len(items)})")
            lines += [f"- **{f['where']}** — {f['msg']}" for f in items]
            lines.append("")
    return "\n".join(lines)


def write_report(book: Book, findings: list[dict], name: str, title: str) -> Path:
    d = book.path("reviews")
    d.mkdir(exist_ok=True)
    p = d / name
    p.write_text(report(findings, title), encoding="utf-8")
    return p
