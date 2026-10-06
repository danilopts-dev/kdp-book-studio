"""N1: Unscramble the Words (8 palavras da historia, fora do caca-palavras) e Crack the Code (cifra A=1..Z=26).
Gera JSON lido pelo Typst (content/n1.typ). Respostas ficam no JSON e em notes.md."""
import json
import random
import re

from extra_common import ASSETS, MANUSCRIPT, used_words

story = (MANUSCRIPT / "noite-1-texto.md").read_text(encoding="utf-8")
# so o trecho "Tonight's Story" (ate a caixa What's a Maccabee)
tonight = story.split("### Tonight's Story")[1].split("### What's a Maccabee")[0]
tonight_words = set(re.findall(r"[A-Za-z]+", tonight.upper()))

# ---------------------------------------------------------------- Unscramble
ITEMS = [  # (resposta, pista)
    ("KING", "Antiochus was one. He ruled the land of Judea."),
    ("TOWN", "Mattathias lived in Modiin, a small ___."),
    ("TOOLS", "Hammers and saws are ___. The family grabbed theirs."),
    ("SONS", "Mattathias had five of them."),
    ("COLD", "The opposite of hot. Up in the hills, the family was ___."),
    ("FREE", "Not stuck and not trapped. In the hills, the family was ___."),
    ("CANDLES", "The king said no more Shabbat ___."),
    ("HEBREW", "The king said no more speaking this language in the streets."),
]
rng = random.Random(1101)


def scramble(word):
    letters = list(word)
    for _ in range(10000):
        rng.shuffle(letters)
        if all(a != b for a, b in zip(letters, word)):  # nenhuma letra no lugar original
            return "".join(letters)
    raise RuntimeError(word)


used = used_words()
rows = []
for ans, clue in ITEMS:
    assert ans in tonight_words, f"{ans} nao esta na historia da N1"
    assert ans not in used, f"{ans} ja usada em outro puzzle"
    assert "—" not in clue and "–" not in clue
    s = scramble(ans)
    assert s != ans and sorted(s) == sorted(ans)
    rows.append({"answer": ans, "scrambled": s, "clue": clue, "length": len(ans)})
assert len({r["answer"] for r in rows}) == 8 and len({r["scrambled"] for r in rows}) == 8
json.dump({"items": rows}, open(ASSETS / "extra_n1_unscramble.json", "w", encoding="utf-8"), indent=2)
for r in rows:
    print(r["scrambled"], "->", r["answer"])

# ---------------------------------------------------------------- Crack the Code
PHRASE_LINES = ["ONE FAMILY", "ONE NO", "ONE MOUNTAIN", "AT A TIME"]
phrase_plain = " ".join(PHRASE_LINES)
# a frase tem de estar na historia: "one family, one no, one mountain at a time"
norm_story = re.sub(r"[^a-z ]", "", tonight.lower().replace("\n", " "))
norm_story = re.sub(r"\s+", " ", norm_story)
assert phrase_plain.lower() in norm_story, "frase nao esta na historia da N1"


def enc(word):
    return [ord(c) - 64 for c in word]


def dec(nums):
    return "".join(chr(n + 64) for n in nums)


lines = [[enc(w) for w in line.split()] for line in PHRASE_LINES]
# ida e volta
for line_src, line_nums in zip(PHRASE_LINES, lines):
    assert " ".join(dec(w) for w in line_nums) == line_src
    assert all(1 <= n <= 26 for w in line_nums for n in w)
table = {chr(64 + i): i for i in range(1, 27)}
assert all(table[dec([n])] == n for n in range(1, 27))
assert " ".join(" ".join(dec(w) for w in line) for line in lines) == phrase_plain
json.dump({"phrase": phrase_plain, "lines": lines, "source": "Tonight's Story, N1, last paragraph"},
          open(ASSETS / "extra_n1_codigo.json", "w", encoding="utf-8"), indent=2)
print("[OK] cifra:", phrase_plain, lines)
