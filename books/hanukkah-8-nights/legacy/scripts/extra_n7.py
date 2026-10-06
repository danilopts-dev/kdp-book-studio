"""N7: Which Pile Has More? (6 pares de pilhas, desenhadas em Typst a partir do JSON) e Who Gets What? (logica, solucao unica por forca bruta).
Os dois ficam em inputs/puzzle-assets/extra_n7_*.json; o Typst le os dados dali. Nenhuma resposta e escrita a mao na pagina."""
import itertools
import json
import random
import re

from extra_common import ASSETS, MANUSCRIPT

# ---------------------------------------------------------------- Which Pile Has More?
# (esquerda, direita); posicao da maior alterna D, E, D, E, D, E; diferenca >= 2; no maximo 9 moedas por pilha (cabe na caixa)
PILES = [(5, 7), (9, 6), (4, 8), (8, 6), (3, 6), (7, 4)]
pairs = []
for i, (a, b) in enumerate(PILES, 1):
    assert abs(a - b) >= 2 and 1 <= min(a, b) and max(a, b) <= 9
    pairs.append({"n": i, "left": a, "right": b, "more": "left" if a > b else "right", "difference": abs(a - b)})
sides = [p["more"] for p in pairs]
assert all(sides[i] != sides[i + 1] for i in range(5)) and sides.count("left") == 3  # alternada, 3 de cada lado
assert len({p["left"] + p["right"] for p in pairs}) >= 5  # totais variados (nao da para acertar so pela soma)

# ---------------------------------------------------------------- Who Gets What?
KIDS = ["Ben", "Mia", "Sam", "Zoe"]
# 4 dos 6 vales do Coupon Book da N7 (abraco, louca, historia, cama, silencio, brinquedos); icones 74_*.png do mesmo livro
ACTS = {
    "hug": {"icon": "74_heart.png", "label": "Big Hug", "inf": "give the hug", "past": "gave the hug"},
    "dishes": {"icon": "74_plate.png", "label": "Dishes", "inf": "help with the dishes", "past": "helped with the dishes"},
    "story": {"icon": "74_book.png", "label": "Story", "inf": "read the story", "past": "read the story"},
    "toys": {"icon": "74_die_fix.png", "label": "Toys", "inf": "put the toys away", "past": "put the toys away"},
}
coupon_txt = (MANUSCRIPT / "noite-7-texto.md").read_text(encoding="utf-8")
src = open(ASSETS.parent.parent / "content" / "n7.typ", encoding="utf-8").read()
for key in ("a story read out loud", "helping with the dishes", "picking up ten toys", "one big hug"):
    assert key in src, key  # os 4 gestos existem no Coupon Book

# solucao gerada por codigo (seed fixa)
rng = random.Random(7107)
perm = list(ACTS)
rng.shuffle(perm)
SOLUTION = dict(zip(KIDS, perm))
PERMS = [dict(zip(KIDS, p)) for p in itertools.permutations(ACTS)]


def clue(kind, *args):
    """(texto impresso, predicado). O texto e gerado da MESMA tupla que o predicado, para nunca divergirem."""
    if kind == "not":
        k, a = args
        return f"{k} did not {ACTS[a]['inf']}.", lambda s: s[k] != a
    if kind == "not2":
        k, a, b = args
        return f"{k} did not {ACTS[a]['inf']} or {ACTS[b]['inf']}.", lambda s: s[k] not in (a, b)
    if kind == "neither":
        k1, k2, a = args
        return f"Neither {k1} nor {k2} {ACTS[a]['past']}.", lambda s: s[k1] != a and s[k2] != a
    if kind == "pos":
        k, a = args
        return f"{k} {ACTS[a]['past']}.", lambda s: s[k] == a
    raise ValueError(kind)


# pistas escolhidas em cima da solucao gerada (ordem impressa = ordem desta lista)
CLUES = [
    ("not", "Zoe", "story"),
    ("not", "Sam", "story"),
    ("neither", "Sam", "Zoe", "toys"),
    ("not", "Zoe", "dishes"),
    ("not2", "Mia", "dishes", "story"),
]
built = [clue(*c) for c in CLUES]
n_sol = lambda cs: [p for p in PERMS if all(f(p) for _, f in cs)]
assert all(f(SOLUTION) for _, f in built), "pista falsa para a solucao"
sols = n_sol(built)
assert sols == [SOLUTION], f"{len(sols)} solucoes"
redundant = [built[i][0] for i in range(len(built)) if len(n_sol(built[:i] + built[i + 1:])) == 1]
assert not redundant, f"pistas redundantes: {redundant}"
assert 4 <= len(built) <= 5
for t, _ in built:
    assert not re.search(r"[–—]", t) and len(t.split()) <= 14

out = {
    "piles": {"pairs": pairs, "answers": [("left" if p["more"] == "left" else "right") for p in pairs],
              "verificacao": "diferenca >= 2, maior alterna D/E, <= 9 moedas por pilha"},
    "who_gets_what": {"kids": KIDS, "acts": ACTS, "clues": [t for t, _ in built], "clue_tuples": [list(c) for c in CLUES],
                      "solution": SOLUTION, "n_solutions_bruteforce": len(sols), "permutations_checked": len(PERMS),
                      "redundant_clues": redundant},
}
json.dump(out, open(ASSETS / "extra_n7_pilhas_logica.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("[OK] Piles:", [(p["left"], p["right"], p["more"]) for p in pairs])
print("[OK] Logica: solucao", SOLUTION, "| 1 solucao em", len(PERMS), "permutacoes | nenhuma pista redundante")
for t, _ in built:
    print("  -", t)
