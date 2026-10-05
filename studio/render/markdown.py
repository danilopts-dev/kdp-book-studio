"""Conversor mínimo Markdown -> Typst para o texto dos livros.

Suporta: # / ## / ###, parágrafos, **negrito**, *itálico* / _itálico_, listas (- e 1.),
> citação, ![legenda](imagem), --- (quebra de cena), <!-- pagebreak --> e ____ (linha de escrever).
Qualquer outro caractere especial do Typst é escapado, então o texto sai literal.
"""
from __future__ import annotations

import re

_SPECIAL = re.compile(r"([\\#$@<>\[\]`~/=+])")
_BOLD, _ITAL = "\x01", "\x02"
# 3+ sublinhados = linha de escrever (12+ ocupa o resto da linha). Usado em páginas de preencher do front matter.
_FILL = re.compile(r"_{3,}")
_FILL_TOK = re.compile("\x03(\\d+)\x03")


def _fill(n: int) -> str:
    w = "1fr" if n >= 12 else f"{n * 0.55:.2f}em"
    return f"#box(width: {w}, height: 0.9em, stroke: (bottom: 0.6pt))"


def inline(text: str) -> str:
    text = _FILL.sub(lambda m: "\x03" + str(len(m.group(0))) + "\x03", text)
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: _BOLD + m.group(1) + _BOLD, text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", lambda m: _ITAL + m.group(1) + _ITAL, text)
    text = re.sub(r"(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)", lambda m: _ITAL + m.group(1) + _ITAL, text)
    text = _SPECIAL.sub(r"\\\1", text)
    text = text.replace("*", r"\*").replace("_", r"\_")
    text = text.replace(_BOLD, "*").replace(_ITAL, "_")
    return _FILL_TOK.sub(lambda m: _fill(int(m.group(1))), text)


def _typ_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def convert(md: str, image_root: str = "") -> str:
    out: list[str] = []
    para: list[str] = []
    quote: list[str] = []

    def flush():
        if para:
            out.append(inline(" ".join(para)))
            out.append("")
            para.clear()
        if quote:
            out.append("#quote(block: true)[" + inline(" ".join(quote)) + "]")
            out.append("")
            quote.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush()
            continue
        if s == "<!-- pagebreak -->":
            flush()
            out.append("#pagebreak()")
            continue
        if s.startswith("<!--"):
            continue
        if re.fullmatch(r"(-{3,}|\*{3,})", s):
            flush()
            out.append("#scene-break()")
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            flush()
            out.append("=" * len(m.group(1)) + " " + inline(m.group(2)))
            out.append("")
            continue
        m = re.fullmatch(r'!\[(.*?)\]\((\S+?)(?:\s+"([\d.]+(?:in|cm|mm|pt|%))")?\)', s)
        if m:
            flush()
            cap, src, width = m.groups()  # ![legenda](arquivo.png "1.6in"): largura opcional
            path = src if src.startswith("/") else f"{image_root}/{src}"
            fig = f"#figure(image({_typ_str(path)}, width: {width or '100%'})"
            fig += f", caption: [{inline(cap)}])" if cap else ")"
            out.append(fig)
            out.append("")
            continue
        if s.startswith(">"):
            if para:
                flush()
            quote.append(s.lstrip("> ").strip())
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if m:
            flush()
            indent = "  " * (len(m.group(1)) // 2)
            marker = "-" if m.group(2) in "-*" else "+"
            out.append(f"{indent}{marker} {inline(m.group(3))}")
            continue
        if quote:
            flush()
        para.append(s)
    flush()
    return "\n".join(out)
