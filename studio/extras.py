"""Comandos de apoio: QR do bônus, PDF do bônus, projeção de páginas e pesquisa de keywords.

Tudo determinístico (zero tokens). Chamados pela CLI em __main__.py.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

from .book import ROOT, Book

QR_FILE = "bonus-qr.png"        # em inputs/; a página do bônus usa ![](bonus-qr.png "1.6in")
QR_URL_FILE = "bonus-qr.url"    # em inputs/; URL que o QR abre ("PLACEHOLDER" = provisório)


# --- QR do bônus ----------------------------------------------------------------
def qr_status(book: Book) -> str:
    """'real', 'placeholder' ou 'missing'."""
    png, url = book.path("inputs", QR_FILE), book.path("inputs", QR_URL_FILE)
    if not png.exists():
        return "missing"
    if not url.exists() or url.read_text(encoding="utf-8").strip() in ("", "PLACEHOLDER"):
        return "placeholder"
    return "real"


def make_qr(book: Book, url: str | None) -> str:
    """Gera inputs/bonus-qr.png pronto para impressão (2 in a 600 DPI, preto no branco).
    Sem URL: quadrado provisório "QR CODE" do mesmo tamanho, para o livro montar antes do formulário existir."""
    from PIL import Image, ImageDraw, ImageFont

    out = book.path("inputs", QR_FILE)
    out.parent.mkdir(parents=True, exist_ok=True)
    size = 1200
    if url:
        import segno
        qr = segno.make(url, error="m")
        modules = qr.symbol_size(scale=1, border=4)[0]
        scale = -(-size // modules)               # módulos inteiros, sem reamostrar
        px = modules * scale
        tmp = book.build_dir / "qr-tmp.png"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        qr.save(str(tmp), scale=scale, border=4, dark="black", light="white")
        Image.open(tmp).convert("L").save(out, dpi=(px / 2, px / 2))   # 2 in impresso
        tmp.unlink()
        book.path("inputs", QR_URL_FILE).write_text(url.strip() + "\n", encoding="utf-8")
        return f"QR real gerado ({px}px, {px // 2} DPI a 2 in) -> {url}"
    im = Image.new("L", (size, size), 255)
    d = ImageDraw.Draw(im)
    d.rectangle([20, 20, size - 20, size - 20], outline=120, width=12)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 110)
    except OSError:
        try:
            font = ImageFont.truetype("arialbd.ttf", 110)
        except OSError:
            font = ImageFont.load_default(size=110)
    d.text((size / 2, size / 2), "QR CODE", fill=120, anchor="mm", font=font)
    im.save(out, dpi=(600, 600))
    book.path("inputs", QR_URL_FILE).write_text("PLACEHOLDER\n", encoding="utf-8")
    return "QR provisório gerado (troque pelo real com: ./st qr <livro> <url-do-formulário>)"


# --- PDF do bônus -----------------------------------------------------------------
def build_bonus(book: Book, preview: bool = False) -> dict:
    """Compila bonus/*.typ (um PDF por arquivo) em build/<slug>-bonus[-nome].pdf."""
    from pypdf import PdfReader

    from .render import typst_compat as typst

    srcs = sorted(book.path("bonus").glob("*.typ"))
    if not srcs:
        sys.exit("Sem bonus/*.typ neste livro.")
    fonts = [str(ROOT / "fonts")] if (ROOT / "fonts").exists() else []
    book.build_dir.mkdir(parents=True, exist_ok=True)
    out = {}
    for src in srcs:
        suffix = "" if src.stem in ("bonus", "main") or len(srcs) == 1 else f"-{src.stem}"
        pdf = book.build_dir / f"{book.slug}-bonus{suffix}.pdf"
        typst.compile(str(src), output=str(pdf), root=str(ROOT), font_paths=fonts)
        out[pdf.name] = len(PdfReader(str(pdf)).pages)
        if preview:
            pdir = book.build_dir / "preview"
            pdir.mkdir(exist_ok=True)
            for old in pdir.glob("*.png"):
                old.unlink()
            imgs = typst.compile(str(src), format="png", ppi=45, root=str(ROOT), font_paths=fonts)
            for i, img in enumerate([imgs] if isinstance(imgs, bytes) else imgs, 1):
                (pdir / f"p{i:03d}.png").write_bytes(img)
            sheet = book.build_dir / f"sheet-bonus{suffix}.png"
            subprocess.run([sys.executable, str(ROOT / "scripts" / "contact_sheet.py"), str(pdir), str(sheet), "4"],
                           check=True, capture_output=True)
    return out


# --- Projeção de páginas ------------------------------------------------------------
def _target(meta: dict) -> tuple[int, int] | None:
    t = meta.get("target_pages")
    if not t:
        return None
    nums = [int(x) for x in re.findall(r"\d+", str(t))]
    return (nums[0], nums[-1]) if nums else None


def estimate_pages(book: Book) -> dict:
    """Monta o miolo com o que existe e projeta o total quando todas as unidades estiverem prontas."""
    from .render.build import build

    class _Empty(Book):
        @property
        def units(self):
            return []

    base = build(_Empty(book.slug))["pages"]          # só abertura/fechamento
    now = build(book)["pages"]                        # com as unidades que já existem (deixa o PDF certo)
    units = book.units
    ready = [u for u in units if book.unit_file(u).exists()]
    if not ready:
        return {"pages_now": now, "estimate": None, "msg": "Nenhuma unidade pronta ainda."}
    per_unit = (now - base) / len(ready)
    est = round(base + per_unit * len(units))
    tgt = _target(book.meta)
    r = {"pages_now": now, "units_ready": len(ready), "units_total": len(units),
         "estimate": est, "target": f"{tgt[0]}-{tgt[1]}" if tgt else None}
    if tgt:
        lo, hi = tgt
        if est < lo * 0.85:
            r["alert"] = f"Projeção de ~{est} páginas, abaixo do previsto no TOC ({lo}-{hi}). Avisar o Danilo agora."
        elif est > hi * 1.15:
            r["alert"] = f"Projeção de ~{est} páginas, acima do previsto no TOC ({lo}-{hi}). Avisar o Danilo agora."
    return r


# --- Pesquisa de keywords (autocomplete da Amazon) ----------------------------------
AC_URL = ("https://completion.amazon.com/api/2017/suggestions?limit=11&prefix={q}"
          "&suggestion-type=KEYWORD&page-type=Search&lop=en_US&site-variant=desktop"
          "&client-info=amazon-search-ui&mid=ATVPDKIKX0DER&alias=stripbooks")


def _suggest(prefix: str) -> list[str]:
    req = urllib.request.Request(AC_URL.format(q=urllib.parse.quote(prefix)),
                                 headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urllib.request.urlopen(req, timeout=10) as r:
        data = json.loads(r.read().decode("utf-8"))
    return [s["value"].strip().lower() for s in data.get("suggestions", []) if s.get("value")]


def keyword_research(book: Book, seeds: list[str]) -> tuple[Path, str]:
    """Expande cada termo-semente com o autocomplete de Livros da Amazon.com (o que os compradores
    realmente digitam). Para cada semente: a semente sozinha, semente + a..z e 'for' + público.
    Grava listing/keywords-research.md. Sem rede (ex.: nuvem): grava o aviso e segue."""
    out = book.path("listing", "keywords-research.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    seeds = [s.strip().lower() for s in seeds if s.strip()]
    hits: Counter = Counter()
    first_seen: dict[str, str] = {}
    try:
        _suggest(seeds[0])
    except Exception as e:  # noqa: BLE001
        msg = (f"Sem acesso ao autocomplete da Amazon daqui ({type(e).__name__}). "
               "Rode `./st keywords` na máquina local; até lá o listing usa as sementes do TOC "
               "e marca as keywords como 'ideia (não confirmada)'.")
        out.write_text(f"# Pesquisa de keywords\n\n{msg}\n\nSementes: {', '.join(seeds)}\n", encoding="utf-8")
        return out, msg
    for seed in seeds:
        prefixes = [seed] + [f"{seed} {c}" for c in "abcdefghijklmnopqrstuvwxyz"] + [f"{seed} for "]
        for p in prefixes:
            try:
                for s in _suggest(p):
                    hits[s] += 1
                    first_seen.setdefault(s, seed)
            except Exception:  # noqa: BLE001
                pass
            time.sleep(0.15)
    rows = sorted(hits.items(), key=lambda kv: (-kv[1], kv[0]))
    L = [f"# Pesquisa de keywords ({date.today().isoformat()})", "",
         "Fonte: autocomplete de Livros da Amazon.com. Tudo aqui é busca real de comprador; a coluna "
         "'vezes' conta em quantas expansões o termo apareceu (proxy de força, não é volume de busca).", "",
         f"Sementes: {', '.join(seeds)}", "", "| # | termo | vezes | semente |", "|---|---|---|---|"]
    L += [f"| {i} | {k} | {n} | {first_seen[k]} |" for i, (k, n) in enumerate(rows, 1)]
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    return out, f"{len(rows)} termos reais da Amazon"
