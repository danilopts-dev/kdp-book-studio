"""Gerador de caça-palavras determinístico (seed fixa = mesmo grid sempre)."""
from __future__ import annotations

import random
import re
import string

DIRECTIONS = {
    "E": (0, 1), "S": (1, 0), "SE": (1, 1), "NE": (-1, 1),
    "W": (0, -1), "N": (-1, 0), "NW": (-1, -1), "SW": (1, -1),
}
LEVELS = {
    "easy": ["E", "S"],
    "medium": ["E", "S", "SE", "NE"],
    "hard": list(DIRECTIONS),
}


def normalize(word: str) -> str:
    """Forma que vai no grid: só letras, maiúsculas (ex.: "Rock 'n' Roll" -> ROCKNROLL)."""
    return re.sub(r"[^A-Z]", "", word.upper())


def _fits(grid, word, r, c, dr, dc):
    n = len(grid)
    for i, ch in enumerate(word):
        rr, cc = r + dr * i, c + dc * i
        if not (0 <= rr < n and 0 <= cc < n):
            return False
        if grid[rr][cc] not in ("", ch):
            return False
    return True


def generate(words: list[str], size: int = 15, level: str = "easy", seed: int = 0,
             attempts: int = 200) -> dict:
    dirs = LEVELS[level]
    clean = [(w, normalize(w)) for w in words]
    too_long = [w for w, n in clean if len(n) > size]
    if too_long:
        raise ValueError(f"Palavras maiores que o grid {size}x{size}: {too_long}")
    rng = random.Random(seed)
    order = sorted(clean, key=lambda x: -len(x[1]))
    for _ in range(attempts):
        grid = [["" for _ in range(size)] for _ in range(size)]
        placements = []
        ok = True
        for display, w in order:
            cands = [(r, c, d) for r in range(size) for c in range(size) for d in dirs
                     if _fits(grid, w, r, c, *DIRECTIONS[d])]
            if not cands:
                ok = False
                break
            # metade das vezes prefere cruzar letras já colocadas (grid mais natural)
            rng.shuffle(cands)
            if rng.random() < 0.5:
                cands.sort(key=lambda x: -sum(
                    grid[x[0] + DIRECTIONS[x[2]][0] * i][x[1] + DIRECTIONS[x[2]][1] * i] != ""
                    for i in range(len(w))))
            r, c, d = cands[0]
            dr, dc = DIRECTIONS[d]
            for i, ch in enumerate(w):
                grid[r + dr * i][c + dc * i] = ch
            placements.append({"word": display, "grid_word": w, "row": r, "col": c, "dir": d})
        if not ok:
            continue
        for r in range(size):
            for c in range(size):
                if not grid[r][c]:
                    grid[r][c] = rng.choice(string.ascii_uppercase)
        rows = ["".join(row) for row in grid]
        if all(count_occurrences(rows, p["grid_word"], list(DIRECTIONS)) == 1 for p in placements):
            placements.sort(key=lambda p: words.index(p["word"]))
            return {"size": size, "level": level, "seed": seed, "grid": rows, "placements": placements}
    raise RuntimeError("Não consegui montar o grid; aumente o tamanho ou reduza as palavras.")


def count_occurrences(rows: list[str], word: str, dirs: list[str]) -> int:
    """Quantas vezes a palavra aparece (conjuntos de células distintos; palíndromos contam 1x)."""
    n = len(rows)
    found = set()
    for r in range(n):
        for c in range(n):
            for d in dirs:
                dr, dc = DIRECTIONS[d]
                if all(0 <= r + dr * i < n and 0 <= c + dc * i < n and rows[r + dr * i][c + dc * i] == ch
                       for i, ch in enumerate(word)):
                    found.add(frozenset((r + dr * i, c + dc * i) for i in range(len(word))))
    return len(found)


def solution_cells(puzzle: dict) -> list[list[int]]:
    cells = set()
    for p in puzzle["placements"]:
        dr, dc = DIRECTIONS[p["dir"]]
        for i in range(len(p["grid_word"])):
            cells.add((p["row"] + dr * i, p["col"] + dc * i))
    return sorted([list(x) for x in cells])
