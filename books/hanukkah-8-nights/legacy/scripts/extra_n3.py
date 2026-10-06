"""N3: Follow the Oil (labirinto 12x12, JAR -> MENORAH) e Oil Math (4 problemas, respostas calculadas por codigo)."""
import json
import re

from extra_common import ASSETS, MANUSCRIPT, make_maze

make_maze("extra_n3_labirinto_oleo", 12, 12, "JAR", "MENORAH", seed=3103)

# ---------------------------------------------------------------- Oil Math
# Fatos da noite 3: um jarro tinha oleo para 1 dia; o oleo queimou 8 dias; Hanukkah tem 8 dias/noites.
JAR_DAYS = 1
MIRACLE_DAYS = 8

# cada problema: parametros -> texto (impresso) + expressao -> resposta (calculada)
problems = []


def add(pid, params, template, expr, unit):
    text = template.format(**params)
    answer = eval(expr, {}, dict(params))  # contas simples, expr escrita aqui no script
    assert isinstance(answer, int) and answer > 0
    # coerencia texto x conta: todo parametro numerico aparece no enunciado impresso
    for k, v in params.items():
        assert re.search(rf"\b{v}\b", text), f"{pid}: {k}={v} nao aparece no enunciado"
    problems.append({"id": pid, "text": text, "expression": expr, "params": params, "answer": answer, "unit": unit})


add(1, {"jar": JAR_DAYS, "burn": MIRACLE_DAYS},
    "One small jar had oil for {jar} day. The story says it burned for {burn} days. How many extra days of light was that?",
    "burn - jar", "extra days")
add(2, {"burn": MIRACLE_DAYS, "now": 3},
    "It's day {now} of the miracle. The oil must last until day {burn}. How many more days are left?",
    "burn - now", "days left")
add(3, {"burn": MIRACLE_DAYS, "have": 5},
    "Imagine the Maccabees had {have} small jars, and each jar holds oil for 1 day. How many more jars would they need for {burn} days?",
    "burn - have", "more jars")
add(4, {"days": MIRACLE_DAYS, "years": 2},
    "Imagine every jar holds oil for 1 day. Each Hanukkah has {days} days. How many jars would you need for {years} Hanukkahs in a row?",
    "days * years", "jars")

# fatos: 1 jarro = 1 dia; 8 dias; confere contra o manuscrito da noite 3
src = (MANUSCRIPT / "noite-3-texto.md").read_text(encoding="utf-8")
assert "barely enough oil for a single day" in src and "eight days of light" in src and "eighth day" in src
# sem travessao, sem Natal, sem hebraico
for p in problems:
    assert not re.search(r"[–—]", p["text"]) and "christmas" not in p["text"].lower()
    assert len(p["text"].split()) <= 30, p["text"]

out = {"facts": {"jar_days": JAR_DAYS, "miracle_days": MIRACLE_DAYS}, "problems": problems,
       "answers": [p["answer"] for p in problems]}
json.dump(out, open(ASSETS / "extra_n3_oilmath.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
for p in problems:
    print(p["id"], p["text"], "=>", p["answer"])
print("[OK] Oil Math: respostas", out["answers"])
