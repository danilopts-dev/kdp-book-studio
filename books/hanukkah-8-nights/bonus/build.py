"""Compila o PDF do bônus (8 Nights Family Pack) para books/hanukkah-8-nights/build/.

Uso (na raiz do repositório): .venv/Scripts/python.exe books/hanukkah-8-nights/bonus/build.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from studio.render import typst_compat  # noqa: E402

BOOK = ROOT / "books" / "hanukkah-8-nights"
out = BOOK / "build" / "hanukkah-8-nights-family-pack.pdf"
out.parent.mkdir(exist_ok=True)
typst_compat.compile(str(BOOK / "bonus" / "family-pack.typ"), output=str(out), root=str(ROOT),
                     font_paths=[str(ROOT / "fonts")])
print(out)
