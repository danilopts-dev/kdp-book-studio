"""N6: Latke Maze (12x12, POTATO -> PLATE) e Hanukkah Food Crossword (palavras cruzadas geradas e verificadas)."""
from extra_common import ASSETS, story_words, used_words, make_maze
from extra_crossword import build_crossword, verify_crossword, render_crossword, save_json, check_clues

make_maze("extra_n6_labirinto_latke", 12, 12, "POTATO", "PLATE", seed=6106)

# ---------------------------------------------------------------- crossword
CLUES = {
    "APPLESAUCE": "Sweet, smooth latke topping made from a fruit that grows on trees.",
    "BIMUELOS": "Little puffs of fried dough that many Sephardic families make (see the story).",
    "PANCAKE": "Flat and round, like a latke made of potato.",
    "HONEY": "Sticky, golden sweetness made by bees.",
    "SUGAR": "Sweet white powder dusted on sufganiyot.",
    "FLOUR": "Powder made from ground wheat. The latke recipe needs some.",
    "STOVE": "Where a grown-up heats the oil and the pan.",
    "BOWL": "Round dish for mixing the grated potato and onion.",
    "TOWEL": "Clean cloth for squeezing extra liquid out of the potatoes.",
    "SALT": "A little of this white seasoning goes into the latke mix.",
    "EGG": "Crack one open and add it to the latke mix.",
    "CREAM": "Sour ___: a tangy white topping for latkes.",
}
WORDS = list(CLUES)

# palavras do tema da noite 6 (texto + receita) e fora de todos os outros puzzles
sw = story_words(6)
assert all(w in sw for w in WORDS), [w for w in WORDS if w not in sw]
AVOID = {"KITCHEN", "POTATO", "GOLDEN", "SPOON", "ONION", "PLATE", "LATKE", "PAN", "OIL", "FRY", "SUFGANIYAH", "DOUGHNUT",
         "TRADITION", "GRIDDLE", "PLATTER", "CRISPY", "SIZZLE", "FAMILY", "JELLY", "GRATER"}
assert not (AVOID & set(WORDS))
assert not (used_words(exclude="extra_n6_palavras_cruzadas") & set(WORDS))
assert 10 <= len(WORDS) <= 12 and all(len(w) >= 3 for w in WORDS)
check_clues({k: v for k, v in CLUES.items()})

cw = build_crossword(WORDS, seed_range=range(1, 4001), max_side=13)
verify_crossword(cw, WORDS)
W, H = render_crossword(cw, ASSETS / "extra_n6_palavras_cruzadas")
out = save_json(cw, CLUES, ASSETS / "extra_n6_palavras_cruzadas")
print(f"[OK] crossword {cw['rows']}x{cw['cols']} seed {cw['seed']}, {len(WORDS)} palavras, PNG {W}x{H}")
for p in out["across"]:
    print("A", p["n"], p["answer"], "|", p["clue"])
for p in out["down"]:
    print("D", p["n"], p["answer"], "|", p["clue"])
print("\n".join(out["grade"]))
