"""N2: Clean-Up Maze (12x12, BROOM -> TEMPLE DOOR) e Temple Word Search (14x14, diagonais, sem reverso)."""
from extra_common import make_maze, make_wordsearch, story_words

# --- labirinto
make_maze("extra_n2_labirinto_limpeza", 12, 12, "BROOM", "TEMPLE DOOR", seed=2102)

# --- caca-palavras: palavras da limpeza do Templo (historia da N2 + objetos da cena)
PALAVRAS = ["ALTAR", "COBWEBS", "SCRUBBED", "JERUSALEM", "FLOORS", "BROKEN",
            "SWEPT", "CLEAN", "DUST", "PIECES", "SLEEVES", "BROOM"]
sw = story_words(2)
# todas do texto da noite 2, exceto BROOM (ferramenta de limpeza, ja o rotulo aprovado do labirinto)
faltam = [w for w in PALAVRAS if w not in sw and w != "BROOM"]
assert not faltam, f"fora do texto da N2: {faltam}"
assert "TEMPLE" not in PALAVRAS
make_wordsearch("extra_n2_cacapalavras_templo", PALAVRAS, 14, "medium", seed=2214)
