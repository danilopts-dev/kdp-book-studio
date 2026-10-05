"""Ponte com a pasta do livro no OneDrive (opcional, só na máquina do Danilo).

- `link`: cria o atalho (junction) `Estudio` dentro de `<onedrive_root>/<onedrive_folder>/` apontando para books/<slug>/.
- `publish`: copia os arquivos finais (PDFs, capa, listing, READY.md) para `<pasta>/Entrega/`, que o OneDrive sincroniza.

A raiz fica em `local.yaml` (fora do git): `onedrive_root: C:\\Users\\...\\Amazon KDP`.
A pasta de cada livro fica em `book.yaml`: `onedrive_folder: "13 - Hanukkah 8 Nights Activity Book - 6-10 years"`.
Sem `local.yaml` (ex.: sessão na nuvem), tudo vira no-op com um aviso.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from .book import ROOT, Book

LOCAL = ROOT / "local.yaml"
LINK_NAME = "Estudio"
OUT_NAME = "Entrega"


def _target(book: Book, quiet: bool = False) -> Path | None:
    meta = book.meta
    folder = meta.get("onedrive_folder")
    if not LOCAL.exists():
        if not quiet:
            print("OneDrive: local.yaml ausente (sessão na nuvem?). Nada a fazer.")
        return None
    if not folder:
        if not quiet:
            print(f"OneDrive: defina `onedrive_folder` em books/{book.slug}/book.yaml.")
        return None
    root = (yaml.safe_load(LOCAL.read_text(encoding="utf-8")) or {}).get("onedrive_root")
    if not root:
        if not quiet:
            print("OneDrive: defina `onedrive_root` em local.yaml.")
        return None
    return Path(root) / folder


def link(book: Book) -> None:
    dest = _target(book)
    if dest is None:
        return
    dest.mkdir(parents=True, exist_ok=True)
    lnk = dest / LINK_NAME
    if lnk.exists() or lnk.is_symlink():
        print(f"OneDrive: atalho já existe em {lnk}")
        return
    if sys.platform == "win32":
        r = subprocess.run(["cmd", "/c", "mklink", "/J", str(lnk), str(book.dir)], capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f"Falha ao criar o atalho: {r.stderr.strip() or r.stdout.strip()}")
    else:
        os.symlink(book.dir, lnk, target_is_directory=True)
    print(f"OneDrive: atalho criado {lnk} -> {book.dir}")


def _deliverables(book: Book) -> list[tuple[Path, str]]:
    """(origem, caminho relativo dentro de Entrega/)."""
    items: list[tuple[Path, str]] = []
    for pdf in sorted(book.build_dir.glob("*.pdf")):
        items.append((pdf, pdf.name))
    ready = book.path("READY.md")
    if ready.exists():
        items.append((ready, ready.name))
    lst = book.path("listing")
    if lst.exists():
        for f in sorted(lst.rglob("*")):
            if f.is_file() and f.name != ".gitkeep":
                items.append((f, str(Path("listing") / f.relative_to(lst))))
    return items


def publish(book: Book, quiet: bool = False) -> None:
    dest = _target(book, quiet)
    if dest is None:
        return
    out = dest / OUT_NAME
    items = _deliverables(book)
    if not items:
        if not quiet:
            print("OneDrive: ainda não há PDFs, listing nem READY.md para entregar.")
        return
    for src, rel in items:
        dst = out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime or src.stat().st_size != dst.stat().st_size:
            shutil.copy2(src, dst)
    print(f"OneDrive: {len(items)} arquivo(s) em {out}")
