"""
extra_common.py
Funcoes compartilhadas dos puzzles extras (expansao de paginas, 2026-10-06).
- labirinto 12x12 (reusa gerar_labirinto.py), PNG >= 2400 px, gabarito em cinza (P&B), JSON com rotulos
- caca-palavras renderizado em PNG (Atkinson Hyperlegible Bold), gabarito com celulas cinza
Tudo e verificado por codigo antes de salvar.
"""
import json
import random
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent.parent
ASSETS = BOOK / "inputs" / "puzzle-assets"
MANUSCRIPT = BOOK / "legacy" / "manuscript"
ROOT = BOOK.parent.parent
FONT_BOLD = str(ROOT / "fonts" / "AtkinsonHyperlegible-Bold.ttf")
sys.path.insert(0, str(ROOT))  # para importar studio.generators
sys.path.insert(0, str(HERE))

import gerar_labirinto as GL  # noqa: E402
from studio.generators import wordsearch as WS  # noqa: E402

GL.ESCALA_SUPERSAMPLE = 5  # 12 celulas x 40 x 5 = 2400 px + margem


def story_words(night):
    """Palavras (maiusculas) do texto da noite N."""
    txt = (MANUSCRIPT / f"noite-{night}-texto.md").read_text(encoding="utf-8")
    return set(re.findall(r"[A-Za-z]+", txt.upper().replace("'", "")))


def used_words(exclude=None):
    """Todas as palavras de caca-palavras ja usadas no livro (gabarito JSON das outras noites)."""
    used = set()
    for f in ASSETS.glob("*_gabarito.json"):
        if exclude and f.name == f"{exclude}_gabarito.json":
            continue  # nao conta o proprio puzzle (regeracao)
        d = json.load(open(f, encoding="utf-8"))
        for k in ("palavras", "words"):
            if k in d:
                used |= {w.upper() for w in d[k]}
    return used


# ------------------------------------------------------------------ labirinto
def _nbrs(cells, w, h, c):
    x, y = c
    out = []
    for lado, (dx, dy) in (("N", (0, -1)), ("S", (0, 1)), ("E", (1, 0)), ("W", (-1, 0))):
        nx, ny = x + dx, y + dy
        if not cells[(x, y)][lado] and 0 <= nx < w and 0 <= ny < h:
            out.append((nx, ny))
    return out


def _simple_paths(cells, w, h, start, end):
    """Conta TODOS os caminhos simples start->end por DFS (independente do BFS do gerador)."""
    count = 0
    seen = {start}
    stack = [(start, iter(_nbrs(cells, w, h, start)))]
    while stack:
        cur, it = stack[-1]
        if cur == end:
            count += 1
            seen.discard(cur)
            stack.pop()
            continue
        nxt = next(it, None)
        if nxt is None:
            seen.discard(cur)
            stack.pop()
            continue
        if nxt not in seen:
            seen.add(nxt)
            stack.append((nxt, iter(_nbrs(cells, w, h, nxt))))
    return count


def make_maze(name, w, h, label_in, label_out, seed, cell=40, margin=6):
    random.seed(seed)
    cells = GL.gerar_labirinto_perfeito(w, h)
    start, end = (0, 0), (w - 1, h - 1)
    path = GL.caminho_unico_bfs(cells, w, h, start, end)  # arvore geradora + BFS
    # verificacoes independentes
    assert _simple_paths(cells, w, h, start, end) == 1, "mais de um caminho"
    reach = {start}
    todo = [start]
    while todo:
        c = todo.pop()
        for n in _nbrs(cells, w, h, c):
            if n not in reach:
                reach.add(n)
                todo.append(n)
    assert len(reach) == w * h, "celulas inalcancaveis"
    out_png = ASSETS / f"{name}.png"
    GL.desenhar(cells, w, h, start, end, None, str(out_png), cell, margin)
    img = Image.open(out_png).convert("RGB")
    esc = GL.ESCALA_SUPERSAMPLE
    tc, mg = cell * esc, margin * esc
    assert max(img.size) >= 2400, img.size
    # aberturas: parede oeste da entrada e leste da saida brancas
    ye = mg + start[1] * tc + tc // 2
    ys = mg + end[1] * tc + tc // 2
    assert img.getpixel((mg, ye)) == (255, 255, 255), "entrada fechada"
    assert img.getpixel((mg + w * tc, ys)) == (255, 255, 255), "saida fechada"
    # gabarito P&B: caminho em cinza grosso por baixo, paredes pretas por cima
    g = img.copy()
    d = ImageDraw.Draw(g)
    pts = [(mg + x * tc + tc / 2, mg + y * tc + tc / 2) for x, y in path]
    d.line([(mg, pts[0][1])] + pts + [(mg + w * tc, pts[-1][1])],
           fill=(130, 130, 130), width=int(tc * 0.34), joint="curve")
    walls = img.convert("L").point(lambda v: 255 if v < 128 else 0)  # 255 onde ha parede
    g.paste((0, 0, 0), mask=walls)
    g.save(ASSETS / f"{name}_gabarito.png")
    info_in, info_out = GL.abertura_info(w, h, start, end, cell, margin)
    meta = {
        "nome": name, "dimensoes": [w, h], "inicio": list(start), "fim": list(end),
        "caminho": [list(p) for p in path], "passos": len(path) - 1,
        "rotulo_inicio": label_in, "rotulo_fim": label_out,
        "abertura_entrada": info_in, "abertura_saida": info_out,
        "seed": seed,
        "verificado": "arvore geradora + BFS + contagem independente de caminhos simples = 1 + todas as celulas alcancaveis",
    }
    json.dump(meta, open(ASSETS / f"{name}_gabarito.json", "w", encoding="utf-8"), indent=2)
    print(f"[OK] {name}: {w}x{h}, {len(path)} celulas no caminho, PNG {img.size}, caminho unico verificado")
    return meta


# ------------------------------------------------------------------ caca-palavras
def render_grid(rows, cells_hl, path_png, cell=176, margin=10, line=6):
    n = len(rows)
    W = n * cell + 2 * margin
    img = Image.new("RGB", (W, W), "white")
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_BOLD, int(cell * 0.56))
    for (r, c) in cells_hl:
        x0, y0 = margin + c * cell, margin + r * cell
        d.rectangle([x0, y0, x0 + cell, y0 + cell], fill=(190, 190, 190))
    for i in range(n + 1):
        p = margin + i * cell
        d.rectangle([margin - line // 2, p - line // 2, margin + n * cell + line // 2, p + line // 2], fill="black")
        d.rectangle([p - line // 2, margin - line // 2, p + line // 2, margin + n * cell + line // 2], fill="black")
    for r in range(n):
        for c in range(n):
            ch = rows[r][c]
            cx, cy = margin + c * cell + cell / 2, margin + r * cell + cell / 2
            bb = d.textbbox((0, 0), ch, font=font)
            d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), ch, fill="black", font=font)
    assert W >= 2400, W
    img.save(path_png)
    return W


BAD = ["ASS", "SEX", "DAMN", "HELL", "CRAP", "PEE", "POO", "BUTT", "SHIT", "FUCK", "DICK", "TIT", "HATE",
       "KILL", "XMAS", "TREE", "SANTA", "NOEL", "CROSS", "JESUS", "CHRIST", "BUM", "WAR", "GUN", "BOMB", "DEAD",
       "NAZI", "PIG", "CRY", "SIN", "IDOL"]


def fill_has_bad_word(rows, placed_cells):
    """True se uma palavra feia/inadequada aparece (4 direcoes de leitura) usando celulas de enchimento."""
    n = len(rows)
    for r in range(n):
        for c in range(n):
            for dr, dc in ((0, 1), (1, 0), (1, 1), (-1, 1)):
                for ln in range(3, 7):
                    cs = [(r + dr * i, c + dc * i) for i in range(ln)]
                    if not all(0 <= a < n and 0 <= b < n for a, b in cs):
                        break
                    if "".join(rows[a][b] for a, b in cs) in BAD and not all(x in placed_cells for x in cs):
                        return True
    return False


def make_wordsearch(name, words, size, level, seed):
    assert 10 <= len(words) <= 14
    assert all(len(w) >= 3 for w in words)
    dup = used_words(exclude=name) & set(words)
    assert not dup, f"palavras ja usadas em outros puzzles: {dup}"
    for tentativa in range(200):  # troca a seed ate o enchimento nao formar palavra inadequada
        puz = WS.generate(words, size=size, level=level, seed=seed + tentativa)
        placed = {tuple(c) for c in WS.solution_cells(puz)}
        if not fill_has_bad_word(puz["grid"], placed):
            seed = seed + tentativa
            break
    else:
        raise RuntimeError("sem grade limpa")
    rows = puz["grid"]
    dirs = WS.LEVELS[level]
    # verificacao independente: cada palavra aparece exatamente 1 vez em TODAS as 8 direcoes
    # (logo nunca de tras para frente) e a posicao declarada esta na grade
    for p in puz["placements"]:
        assert WS.count_occurrences(rows, p["grid_word"], list(WS.DIRECTIONS)) == 1
        dr, dc = WS.DIRECTIONS[p["dir"]]
        assert p["dir"] in dirs
        for i, ch in enumerate(p["grid_word"]):
            assert rows[p["row"] + dr * i][p["col"] + dc * i] == ch
    cells = {tuple(c) for c in WS.solution_cells(puz)}
    W = render_grid(rows, set(), ASSETS / f"{name}_grade.png")
    render_grid(rows, cells, ASSETS / f"{name}_gabarito.png")
    meta = {"grade": [list(r) for r in rows], "palavras": words,
            "regras": f"{level}: {', '.join(dirs)} (sem reverso)",
            "gabarito_posicoes": {p["word"]: [[p["row"] + WS.DIRECTIONS[p["dir"]][0] * i,
                                               p["col"] + WS.DIRECTIONS[p["dir"]][1] * i]
                                              for i in range(len(p["grid_word"]))] for p in puz["placements"]},
            "direcoes": {p["word"]: p["dir"] for p in puz["placements"]}, "seed": seed}
    json.dump(meta, open(ASSETS / f"{name}_gabarito.json", "w", encoding="utf-8"), indent=2)
    print(f"[OK] {name}: {size}x{size} {level}, {len(words)} palavras unicas, PNG {W}px")
    return meta
