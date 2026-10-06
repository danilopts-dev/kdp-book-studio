"""N4: dados e respostas de 'Draw the Candles' (Noites 2, 4, 6) e 'Which Night Is It?' (4 hanukkiahs).
As duas atividades sao desenhadas em Typst (componente hanukkiah-draw do theme.typ); este script fixa os dados,
calcula as respostas e verifica as regras: shamash sempre aceso e fora da contagem das noites."""
import json

from extra_common import ASSETS

# posicoes 0..8, a 4 e o shamash; as velas da noite n entram da direita para a esquerda (como no Family Pack)
ORDER = [8, 7, 6, 5, 3, 2, 1, 0]


def positions(n):
    assert 1 <= n <= 8
    return ORDER[:n]


DRAW = [2, 4, 6]
WHICH = [5, 2, 7, 3]  # fora de ordem de proposito

for n in DRAW + WHICH:
    pos = positions(n)
    assert 4 not in pos and len(pos) == n          # o shamash (posicao 4) nunca conta como noite
    assert len(set(pos)) == n and max(pos) <= 8
draw = [{"night": n, "hanukkah_candles": n, "shamash": 1, "positions_lit": positions(n)} for n in DRAW]
which = [{"night": n, "hanukkah_candles_shown": len(positions(n)), "shamash_shown_lit": True, "positions_lit": positions(n)}
         for n in WHICH]
total_hanukkah = sum(len(positions(n)) for n in WHICH)
assert total_hanukkah == sum(WHICH) == 17
out = {
    "draw_the_candles": {"nights": DRAW, "items": draw,
                         "answer": "Night 2 = 2 candles + shamash; Night 4 = 4 + shamash; Night 6 = 6 + shamash"},
    "which_night": {"items": which, "answers_by_picture": WHICH, "total_hanukkah_candles": total_hanukkah,
                    "total_with_shamash_counted": total_hanukkah + len(WHICH),
                    "note": "pergunta impressa: velas de Hanukkah (sem os shamashes) nas 4 figuras = 17"},
}
json.dump(out, open(ASSETS / "extra_n4_hanukkiahs.json", "w", encoding="utf-8"), indent=2)
print("[OK] N4: noites desenhar", DRAW, "| quais noites", WHICH, "| total sem shamash", total_hanukkah)
