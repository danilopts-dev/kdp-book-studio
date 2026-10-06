"""N5: Dreidel Tally Chart (pagina em Typst, sem resposta unica) e What Comes Next? Dreidel Patterns (6 sequencias, resposta unica verificada).

Verificacao de unicidade: uma BIBLIOTECA de regras (periodica, blocos que crescem, vai e volta, aritmetica, geometrica, 2a diferenca constante).
Cada regra que e consistente com o trecho mostrado preve o proximo item; a resposta so e aceita se TODAS as regras
consistentes preveem o mesmo item (e pelo menos uma e consistente). Nenhuma sequencia e escrita sem passar por isso.
"""
import json

from extra_common import ASSETS


# ---------------------------------------------------------------- biblioteca de regras: cada uma devolve a previsao ou None
def r_periodic(seq):
    """Periodo p (1 <= p <= len-2): seq[i] == seq[i-p]. Preve seq[len-p]. Devolve o conjunto de previsoes (uma por p consistente)."""
    out = set()
    n = len(seq)
    for p in range(1, n - 1):
        if all(seq[i] == seq[i - p] for i in range(p, n)):
            out.add(seq[n - p])
    return out


def r_grow(seq):
    """Blocos que crescem: 1, 2, 3, ... repeticoes de cada item, e os itens seguem o ciclo visto (letra nova a cada bloco)."""
    runs = []
    for x in seq:
        if runs and runs[-1][0] == x:
            runs[-1][1] += 1
        else:
            runs.append([x, 1])
    k = len(runs)
    if k < 3 or any(runs[i][1] != i + 1 for i in range(k - 1)):
        return set()
    last_item, last_len = runs[-1]
    if last_len > k:
        return set()
    items = [r[0] for r in runs]
    # ciclo das letras: o primeiro item que repete marca o periodo; se nao repetiu, o ciclo e todo o visto
    cycle = items
    for p in range(1, k):
        if all(items[i] == items[i % p] for i in range(k)):
            cycle = items[:p]
            break
    if last_len < k:
        return {last_item}          # bloco k ainda nao chegou ao tamanho k
    return {cycle[k % len(cycle)]}  # bloco completo: vem o proximo item do ciclo


def r_bounce(seq):
    """Vai e volta sobre uma lista de itens distintos (A B C D C B A B ...). Tamanho da lista = numero de itens distintos."""
    items = list(dict.fromkeys(seq))
    m = len(items)
    if m < 3 or len(seq) <= m:   # sem volta visivel, nao ha como saber que vai voltar
        return set()
    path = list(range(m)) + list(range(m - 2, 0, -1))  # 0..m-1..1
    n = len(seq)
    for start in range(len(path)):
        if all(seq[i] == items[path[(start + i) % len(path)]] for i in range(n)):
            return {items[path[(start + n) % len(path)]]}
    return set()


def r_arith(seq):
    if len(seq) < 4 or not all(isinstance(x, int) for x in seq):
        return set()
    d = seq[1] - seq[0]
    return {seq[-1] + d} if all(seq[i + 1] - seq[i] == d for i in range(len(seq) - 1)) else set()


def r_geom(seq):
    if len(seq) < 4 or not all(isinstance(x, int) and x != 0 for x in seq):
        return set()
    if all(seq[i + 1] * seq[0] == seq[i] * seq[1] for i in range(len(seq) - 1)) and (seq[1] * seq[-1]) % seq[0] == 0:
        return {seq[-1] * seq[1] // seq[0]}
    return set()


def r_diff2(seq):
    if len(seq) < 5 or not all(isinstance(x, int) for x in seq):
        return set()
    d1 = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
    return {seq[-1] + d1[-1] + d2[0]} if len(set(d2)) == 1 else set()


RULES = {"periodic": r_periodic, "grow": r_grow, "bounce": r_bounce, "arith": r_arith, "geom": r_geom, "diff2": r_diff2}


def predictions(seq):
    return {name: f(seq) for name, f in RULES.items() if f(seq)}


# ---------------------------------------------------------------- as 6 sequencias
# itens: nomes das letras do dreidel (so transliteracao), formas (circle square triangle diamond) e numeros
NAMES = {"N": "Nun", "G": "Gimel", "H": "Hei", "S": "Shin"}
SEQS = [
    {"kind": "letters", "shown": ["N", "G", "H", "N", "G", "H", "N", "G"], "answer": "H", "rule": "ciclo de 3 (Nun, Gimel, Hei)"},
    {"kind": "letters", "shown": ["S", "S", "N", "S", "S", "N", "S", "S"], "answer": "N", "rule": "ciclo de 3 (Shin, Shin, Nun)"},
    {"kind": "letters", "shown": ["G", "H", "H", "S", "S", "S", "N", "N"], "answer": "N", "rule": "blocos que crescem 1, 2, 3, 4 (o bloco da Nun ainda esta no 2, falta a 3a Nun)"},
    {"kind": "shapes", "shown": ["circle", "square", "triangle", "diamond", "triangle", "square", "circle", "square"], "answer": "triangle", "rule": "vai e volta sobre 4 formas"},
    {"kind": "shapes", "shown": ["circle", "circle", "square", "square", "triangle", "triangle", "circle", "circle", "square"], "answer": "square", "rule": "cada forma duas vezes, ciclo de 3 formas"},
    {"kind": "numbers", "shown": [4, 8, 12, 16, 20], "answer": 24, "rule": "soma 4 a cada passo (gelt no pote)"},
]
for i, s in enumerate(SEQS, 1):
    pred = predictions(s["shown"])
    assert pred, f"seq {i}: nenhuma regra da biblioteca explica a sequencia"
    allp = set().union(*pred.values())
    assert allp == {s["answer"]}, f"seq {i}: previsoes ambiguas {pred}"
    assert 5 <= len(s["shown"]) <= 9
    if s["kind"] == "letters":
        assert set(s["shown"] + [s["answer"]]) <= set(NAMES)
    s["rules_that_fit"] = sorted(pred)
    print(i, s["kind"], s["shown"], "=>", s["answer"], "| regras:", s["rules_that_fit"])

# a regra que explica cada sequencia e a intencional (guarda contra "acertou por acaso")
INTENDED = ["periodic", "periodic", "grow", "bounce", "periodic", "arith"]
for s, want in zip(SEQS, INTENDED):
    assert want in s["rules_that_fit"], (s["shown"], want)

# Tally chart: 4 letras, 20 giradas; nao tem resposta unica (depende da crianca)
TALLY = {"letters": [{"name": NAMES[k], "letter_script": s} for k, s in zip("NGHS", "נגהש")], "spins": 20,
         "answer": "sem resposta unica (depende das giradas)"}
assert [t["name"] for t in TALLY["letters"]] == ["Nun", "Gimel", "Hei", "Shin"]

out = {"patterns": SEQS, "answers": [s["answer"] for s in SEQS], "answers_text": [NAMES.get(s["answer"], str(s["answer"])) for s in SEQS],
       "tally_chart": TALLY}
json.dump(out, open(ASSETS / "extra_n5_padroes.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("[OK] N5: 6 sequencias com resposta unica; respostas:", out["answers_text"])
