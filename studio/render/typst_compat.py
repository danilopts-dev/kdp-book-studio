"""`typst.compile` com fallback para o executável `typst`.

O pacote Python `typst` traz um .pyd sem assinatura digital, que o Smart App Control do Windows 11 bloqueia.
Quando o import falha, usamos o CLI oficial (`winget install Typst.Typst`), com a mesma interface.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

try:  # caminho normal (Linux/macOS/nuvem)
    import typst as _typst
except Exception:  # ImportError, ou DLL bloqueada no Windows
    _typst = None


def _cli() -> str:
    exe = shutil.which("typst")
    if exe:
        return exe
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
    if base.exists():
        for p in base.rglob("typst.exe"):
            return str(p)
    raise RuntimeError(
        "Typst indisponível: o pacote Python não carrega e o executável não foi encontrado. "
        "Instale com `winget install Typst.Typst`."
    )


def compile(input, output=None, format=None, ppi=None, root=None, font_paths=()):
    if _typst is not None:
        kw = dict(output=output, root=root, font_paths=list(font_paths))
        if format:
            kw["format"] = format
        if ppi:
            kw["ppi"] = ppi
        return _typst.compile(input, **kw)

    cmd = [_cli(), "compile", "--root", str(root), "--diagnostic-format", "human"]
    for fp in font_paths:
        cmd += ["--font-path", str(fp)]
    if format == "png":
        with tempfile.TemporaryDirectory() as d:
            cmd += ["--format", "png", "--ppi", str(ppi or 144), str(input), str(Path(d) / "p{0p}.png")]
            _run(cmd)
            return [p.read_bytes() for p in sorted(Path(d).glob("p*.png"))]
    cmd += [str(input), str(output)]
    _run(cmd)
    return None


def _run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"typst falhou:\n{r.stderr.strip() or r.stdout.strip()}")
