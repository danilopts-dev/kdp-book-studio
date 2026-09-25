"""Gerador de sudoku 9x9 com solução única garantida."""
from __future__ import annotations

import random

CLUES = {"easy": 40, "medium": 32, "hard": 27}


def _candidates(g, r, c):
    used = set(g[r]) | {g[i][c] for i in range(9)}
    br, bc = 3 * (r // 3), 3 * (c // 3)
    used |= {g[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}
    return [n for n in range(1, 10) if n not in used]


def count_solutions(g, limit=2):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                total = 0
                for n in _candidates(g, r, c):
                    g[r][c] = n
                    total += count_solutions(g, limit - total)
                    g[r][c] = 0
                    if total >= limit:
                        return total
                return total
    return 1


def _fill(g, rng):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                cands = _candidates(g, r, c)
                rng.shuffle(cands)
                for n in cands:
                    g[r][c] = n
                    if _fill(g, rng):
                        return True
                g[r][c] = 0
                return False
    return True


def generate(level: str = "easy", seed: int = 0) -> dict:
    rng = random.Random(seed)
    sol = [[0] * 9 for _ in range(9)]
    _fill(sol, rng)
    puzzle = [row[:] for row in sol]
    cells = [(r, c) for r in range(9) for c in range(9)]
    rng.shuffle(cells)
    target = CLUES[level]
    filled = 81
    for r, c in cells:
        if filled <= target:
            break
        keep = puzzle[r][c]
        puzzle[r][c] = 0
        if count_solutions([row[:] for row in puzzle]) != 1:
            puzzle[r][c] = keep
        else:
            filled -= 1
    return {
        "level": level,
        "seed": seed,
        "clues": filled,
        "puzzle": ["".join(str(n) if n else "." for n in row) for row in puzzle],
        "solution": ["".join(map(str, row)) for row in sol],
    }


def parse(rows: list[str]) -> list[list[int]]:
    return [[0 if ch == "." else int(ch) for ch in row] for row in rows]


def is_valid_solution(rows: list[str]) -> bool:
    g = parse(rows)
    full = set(range(1, 10))
    for i in range(9):
        if set(g[i]) != full or {g[r][i] for r in range(9)} != full:
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            if {g[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)} != full:
                return False
    return True
