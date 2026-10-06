"""N8: Match the Night (ligar 6 noites ao que aconteceu, gabarito por codigo) e Night by Night Word Search (15x15, diagonais sem reverso)."""
import json
import random
import re

from extra_common import ASSETS, MANUSCRIPT, make_wordsearch, story_words, used_words

# ---------------------------------------------------------------- Match the Night
# (noite, titulo real, fato, frase-chave que o manuscrito da noite sustenta)
MATCH = [
    (1, "Judah Says No", "A man from Modiin said no to the king's soldiers.", ["Modiin", "said no"]),
    (2, "The Temple Is a Mess", "The Maccabees swept and scrubbed the broken Temple.", ["swept the floors", "scrubbed"]),
    (3, "One Little Jar of Oil", "The story says one small jar of oil burned for eight days.", ["one small jar", "eight days"]),
    (4, "Light It Right", "The hanukkiah goes where neighbors can see it.", ["neighbors", "can see it"]),
    (5, "Spin the Dreidel", "The story says kids spun a top to hide their studying.", ["spinning top", "study"]),
    (6, "Everything Fried", "Families eat latkes and sufganiyot, foods fried in oil.", ["latkes", "sufganiyot", "fried in oil"]),
]
titles_real = {}
for n in range(1, 9):
    first = (MANUSCRIPT / f"noite-{n}-texto.md").read_text(encoding="utf-8").splitlines()[0]
    titles_real[n] = first.split(":", 1)[1].strip()
for n, title, fact, keys in MATCH:
    assert titles_real[n] == title, (n, titles_real[n], title)
    txt = (MANUSCRIPT / f"noite-{n}-texto.md").read_text(encoding="utf-8").lower()
    for k in keys:
        assert k.lower() in txt, f"noite {n}: '{k}' nao aparece no texto"
    assert not re.search(r"[–—]", fact) and len(fact.split()) <= 14
# a coluna da direita (fatos) embaralhada, sem nenhum par alinhado (derangement) e sem fato unico em 2 noites
rng = random.Random(8108)
while True:
    order = list(range(6))
    rng.shuffle(order)
    if all(order[i] != i for i in range(6)):
        break
right = [{"pos": i + 1, "fact": MATCH[j][2], "night": MATCH[j][0]} for i, j in enumerate(order)]
assert all(r["night"] != MATCH[i][0] for i, r in enumerate(right)), "par alinhado"
assert len({r["fact"] for r in right}) == 6
answers = [{"night": n, "title": t, "fact_position": next(r["pos"] for r in right if r["night"] == n), "fact": f} for n, t, f, _ in MATCH]
json.dump({"left": [{"night": n, "title": t} for n, t, _, _ in MATCH], "right": right, "answers": answers},
          open(ASSETS / "extra_n8_match.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("[OK] Match: pares (esquerda -> posicao do fato na direita):", [(a["night"], a["fact_position"]) for a in answers])

# ---------------------------------------------------------------- Night by Night Word Search
WORDS = ["DREIDEL", "SHAMASH", "HANUKKIAH", "MIRACLE", "TZEDAKAH", "WINDOW",
         "DEDICATION", "GRATITUDE", "SOLDIERS", "NEIGHBORS", "SECRET", "FRIED"]
night_of = {w: [n for n in range(1, 9) if w in story_words(n)] for w in WORDS}
assert all(night_of[w] for w in WORDS), {w: n for w, n in night_of.items() if not n}
covered = sorted({n for v in night_of.values() for n in v})
assert len(covered) == 8, covered  # as 8 noites aparecem
assert not (used_words() & set(WORDS))
# tambem nao repete as palavras do crossword da N6 nem do labirinto/rotulos novos
cw = set(json.load(open(ASSETS / "extra_n6_palavras_cruzadas_gabarito.json", encoding="utf-8"))["palavras"])
assert not (cw & set(WORDS))
meta = make_wordsearch("extra_n8_cacapalavras_noites", WORDS, 15, "medium", seed=8215)
meta["noites_das_palavras"] = night_of
json.dump(meta, open(ASSETS / "extra_n8_cacapalavras_noites_gabarito.json", "w", encoding="utf-8"), indent=2)
print("noites:", night_of)
