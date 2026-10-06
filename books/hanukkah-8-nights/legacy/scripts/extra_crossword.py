"""
extra_crossword.py
Gerador de palavras cruzadas (crossword) de verdade, com verificacao independente.
- grade que se cruza (palavras ligadas por cruzamentos), sem palavras acidentais
- numeracao across/down no estilo padrao (leitura esquerda->direita, cima->baixo)
- gabarito e PNG (puzzle sem letras + gabarito com letras em cinza), P&B, >= 2400 px
- JSON com grade, numeracao, pistas e respostas (o Typst le as pistas daqui)

Uso (veja extra_n6.py):
    cw = build_crossword(words_clues, seed_range=range(1, 4000), max_side=13)
    verify_crossword(cw, words_clues)
    render_crossword(cw, ASSETS / "nome")
"""
import json
import random
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from extra_common import FONT_BOLD

DIRS = {"A": (0, 1), "D": (1, 0)}  # across = para a direita, down = para baixo


# ------------------------------------------------------------------ construcao
class _Grid:
    def __init__(self):
        self.cells = {}   # (r, c) -> letra
        self.used = {}    # (r, c) -> conjunto de direcoes ("A", "D") que passam pela celula
        self.placed = []  # {"word", "r", "c", "dir"}

    def can_place(self, word, r, c, d):
        dr, dc = DIRS[d]
        pr, pc = dc, dr  # eixo perpendicular
        if (r - dr, c - dc) in self.cells or (r + dr * len(word), c + dc * len(word)) in self.cells:
            return False
        crossings = 0
        for i, ch in enumerate(word):
            p = (r + dr * i, c + dc * i)
            if p in self.cells:
                if self.cells[p] != ch or d in self.used[p]:
                    return False
                crossings += 1
            else:
                if (p[0] + pr, p[1] + pc) in self.cells or (p[0] - pr, p[1] - pc) in self.cells:
                    return False
        return crossings >= 1

    def place(self, word, r, c, d):
        dr, dc = DIRS[d]
        for i, ch in enumerate(word):
            p = (r + dr * i, c + dc * i)
            self.cells[p] = ch
            self.used.setdefault(p, set()).add(d)
        self.placed.append({"word": word, "r": r, "c": c, "dir": d})

    def bbox(self):
        rs = [p[0] for p in self.cells]
        cs = [p[1] for p in self.cells]
        return min(rs), min(cs), max(rs), max(cs)


def _try(words, seed):
    rng = random.Random(seed)
    order = sorted(words, key=lambda w: (-len(w), rng.random()))
    g = _Grid()
    first = order[0]
    g.place(first, 0, 0, "A")
    rest = order[1:]
    # em cada rodada, escolhe uma palavra ainda nao colocada e a melhor posicao (mais cruzamentos, grade compacta)
    while rest:
        rng.shuffle(rest)
        done = False
        for w in rest:
            cands = []
            for (pr_, pc_), ch in g.cells.items():
                for i, wc in enumerate(w):
                    if wc != ch:
                        continue
                    for d in ("A", "D"):
                        dr, dc = DIRS[d]
                        r, c = pr_ - dr * i, pc_ - dc * i
                        if g.can_place(w, r, c, d):
                            cands.append((r, c, d))
            if not cands:
                continue
            cands = list(dict.fromkeys(cands))
            best, best_key = None, None
            rng.shuffle(cands)
            for (r, c, d) in cands:
                dr, dc = DIRS[d]
                n_cross = sum((r + dr * i, c + dc * i) in g.cells for i in range(len(w)))
                rs = [p[0] for p in g.cells] + [r, r + dr * (len(w) - 1)]
                cs = [p[1] for p in g.cells] + [c, c + dc * (len(w) - 1)]
                h, wd = max(rs) - min(rs) + 1, max(cs) - min(cs) + 1
                key = (max(h, wd), h * wd, -n_cross, rng.random())
                if best_key is None or key < best_key:
                    best, best_key = (r, c, d), key
            g.place(w, *best)
            rest.remove(w)
            done = True
            break
        if not done:
            return None
    return g


def _normalize(g):
    r0, c0, r1, c1 = g.bbox()
    cells = {(r - r0, c - c0): ch for (r, c), ch in g.cells.items()}
    placed = [{"word": p["word"], "r": p["r"] - r0, "c": p["c"] - c0, "dir": p["dir"]} for p in g.placed]
    return {"rows": r1 - r0 + 1, "cols": c1 - c0 + 1, "cells": cells, "placed": placed}


def _number(cw):
    """Numeracao padrao: celula inicia across se nao tem letra a esquerda e tem a direita; idem down."""
    cells, rows, cols = cw["cells"], cw["rows"], cw["cols"]
    nums, n = {}, 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in cells:
                continue
            a = (r, c - 1) not in cells and (r, c + 1) in cells
            d = (r - 1, c) not in cells and (r + 1, c) in cells
            if a or d:
                n += 1
                nums[(r, c)] = n
    for p in cw["placed"]:
        p["number"] = nums[(p["r"], p["c"])]
    cw["numbers"] = nums
    return cw


def build_crossword(words, seed_range=range(1, 3000), max_side=13):
    """words: lista de palavras. Devolve a melhor grade (menor lado, depois menor area) com TODAS as palavras ligadas."""
    best, best_key = None, None
    for seed in seed_range:
        g = _try(words, seed)
        if g is None:
            continue
        cw = _normalize(g)
        key = (max(cw["rows"], cw["cols"]), cw["rows"] * cw["cols"], -sum(len(v) for v in g.used.values() if len(v) == 2))
        if best_key is None or key < best_key:
            best, best_key = cw, key
            best["seed"] = seed
    assert best is not None, "nenhuma grade encontrada"
    assert max(best["rows"], best["cols"]) <= max_side, (best["rows"], best["cols"])
    return _number(best)


# ------------------------------------------------------------------ verificacao independente
def verify_crossword(cw, words):
    cells, rows, cols = cw["cells"], cw["rows"], cw["cols"]
    # 1) toda palavra esta na grade, na posicao e direcao declaradas
    assert sorted(p["word"] for p in cw["placed"]) == sorted(words), "palavras faltando ou sobrando"
    for p in cw["placed"]:
        dr, dc = DIRS[p["dir"]]
        for i, ch in enumerate(p["word"]):
            assert cells.get((p["r"] + dr * i, p["c"] + dc * i)) == ch, f"{p['word']} nao cabe"
    # 2) todas as sequencias de 2+ letras (across e down) sao exatamente palavras da lista, na direcao certa
    expected = {(p["r"], p["c"], p["dir"]): p["word"] for p in cw["placed"]}
    found = {}
    for r in range(rows):
        c = 0
        while c < cols:
            if (r, c) in cells:
                c2 = c
                while (r, c2 + 1) in cells:
                    c2 += 1
                if c2 > c:
                    found[(r, c, "A")] = "".join(cells[(r, k)] for k in range(c, c2 + 1))
                c = c2 + 1
            else:
                c += 1
    for c in range(cols):
        r = 0
        while r < rows:
            if (r, c) in cells:
                r2 = r
                while (r2 + 1, c) in cells:
                    r2 += 1
                if r2 > r:
                    found[(r, c, "D")] = "".join(cells[(k, c)] for k in range(r, r2 + 1))
                r = r2 + 1
            else:
                r += 1
    assert found == expected, f"palavra acidental ou faltando: {set(found.items()) ^ set(expected.items())}"
    # 3) toda celula pertence a alguma palavra
    covered = set()
    for p in cw["placed"]:
        dr, dc = DIRS[p["dir"]]
        covered |= {(p["r"] + dr * i, p["c"] + dc * i) for i in range(len(p["word"]))}
    assert covered == set(cells), "celula solta"
    # 4) conectividade: grafo palavras-cruzamentos conexo
    sets = [({(p["r"] + DIRS[p["dir"]][0] * i, p["c"] + DIRS[p["dir"]][1] * i) for i in range(len(p["word"]))}) for p in cw["placed"]]
    seen, todo = {0}, [0]
    while todo:
        i = todo.pop()
        for j in range(len(sets)):
            if j not in seen and sets[i] & sets[j]:
                seen.add(j)
                todo.append(j)
    assert len(seen) == len(sets), "palavras desconectadas"
    # 5) numeracao: sem repeticao, em ordem de leitura, across/down corretos
    nums = cw["numbers"]
    order = sorted(nums, key=lambda p: (p[0], p[1]))
    assert [nums[p] for p in order] == list(range(1, len(order) + 1))
    for p in cw["placed"]:
        assert nums[(p["r"], p["c"])] == p["number"]
    # 6) pelo menos 2 cruzamentos por palavra nao e exigido, mas ninguem fica isolado (item 4)
    return True


# ------------------------------------------------------------------ pistas
def check_clues(clues):
    """clues: {PALAVRA: texto}. Nenhuma pista contem alguma das respostas (nem como pedaco), sem travessao."""
    for w, t in clues.items():
        low = t.lower()
        for a in clues:
            assert a.lower() not in low, f"pista de {w} entrega {a}: {t}"
        assert not re.search(r"[–—]", t), f"travessao em {w}"
        assert len(t.split()) <= 14, f"pista longa em {w}: {t}"


# ------------------------------------------------------------------ PNG
def render_crossword(cw, base, margin=14, line=8):
    rows, cols, cells, nums = cw["rows"], cw["cols"], cw["cells"], cw["numbers"]
    cell = -(-(2440 - 2 * margin) // max(rows, cols))  # lado maior >= 2440 px
    W, H = cols * cell + 2 * margin, rows * cell + 2 * margin
    assert max(W, H) >= 2400, (W, H)
    f_let = ImageFont.truetype(FONT_BOLD, int(cell * 0.56))
    f_num = ImageFont.truetype(FONT_BOLD, int(cell * 0.32))

    def draw(show_letters):
        img = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(img)
        for (r, c), ch in cells.items():
            x0, y0 = margin + c * cell, margin + r * cell
            d.rectangle([x0, y0, x0 + cell, y0 + cell], fill=(205, 205, 205) if show_letters else "white")
        for (r, c), ch in cells.items():
            x0, y0 = margin + c * cell, margin + r * cell
            d.rectangle([x0, y0, x0 + cell, y0 + cell], outline="black", width=line)
        for (r, c), ch in cells.items():
            x0, y0 = margin + c * cell, margin + r * cell
            if (r, c) in nums:
                d.text((x0 + line + 7, y0 + line + 2), str(nums[(r, c)]), fill="black", font=f_num)
            if show_letters:
                bb = d.textbbox((0, 0), ch, font=f_let)
                d.text((x0 + cell / 2 - (bb[0] + bb[2]) / 2, y0 + cell * 0.57 - (bb[1] + bb[3]) / 2), ch, fill="black", font=f_let)
        return img

    base = Path(base)
    draw(False).save(f"{base}_grade.png")
    draw(True).save(f"{base}_gabarito.png")
    return W, H


def save_json(cw, clues, base, extra=None):
    across = sorted([p for p in cw["placed"] if p["dir"] == "A"], key=lambda p: p["number"])
    down = sorted([p for p in cw["placed"] if p["dir"] == "D"], key=lambda p: p["number"])
    out = {
        "linhas": cw["rows"], "colunas": cw["cols"], "seed": cw["seed"],
        "grade": ["".join(cw["cells"].get((r, c), ".") for c in range(cw["cols"])) for r in range(cw["rows"])],
        "across": [{"n": p["number"], "answer": p["word"], "clue": clues[p["word"]], "r": p["r"], "c": p["c"]} for p in across],
        "down": [{"n": p["number"], "answer": p["word"], "clue": clues[p["word"]], "r": p["r"], "c": p["c"]} for p in down],
        "palavras": [p["word"] for p in cw["placed"]],
        "verificado": "toda palavra cabe; todas as sequencias de 2+ letras (across e down) sao palavras da lista; todas conectadas; numeracao em ordem de leitura",
    }
    if extra:
        out.update(extra)
    json.dump(out, open(f"{base}_gabarito.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    return out
