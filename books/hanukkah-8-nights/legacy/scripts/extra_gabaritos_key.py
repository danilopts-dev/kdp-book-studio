"""
extra_gabaritos_key.py
Gera os recortes *_key.png (reduzidos, escala de cinza) dos gabaritos das atividades NOVAS da expansao
e confere, por codigo, cada resposta do answer-key contra o puzzle impresso e contra os JSON.
Nao sobrescreve nada (saidas com sufixo _key). Uso (raiz do estudio):

    python books/hanukkah-8-nights/legacy/scripts/extra_gabaritos_key.py
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
PZ = ROOT / "inputs" / "puzzle-assets"
MAXPX = 1800
ok_all = True


def check(cond, msg):
    global ok_all
    print(("  ok   " if cond else "  FALHA ") + msg)
    if not cond:
        ok_all = False


def J(name):
    return json.load(open(PZ / name, encoding="utf-8"))


def L(name):
    return np.array(Image.open(PZ / name).convert("L")).astype(int)


def bbox(a, thr=240):
    m = a < thr
    ys, xs = np.where(m.any(1))[0], np.where(m.any(0))[0]
    return xs[0], ys[0], xs[-1] + 1, ys[-1] + 1


def save_key(src, dst):
    im = Image.open(PZ / src).convert("L")
    s = MAXPX / max(im.size)
    if s < 1:
        im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
    im.save(PZ / dst, optimize=True)
    print(f"  -> {dst} {im.size}")


# ---------------------------------------------------------------- labirintos
def maze(name):
    print(f"[labirinto] {name}")
    O = L(name + ".png")
    G = L(name + "_gabarito.png")
    d = J(name + "_gabarito.json")
    check(O.shape == G.shape, "gabarito e puzzle impresso com o mesmo tamanho")
    ink = (G > 100) & (G < 200)  # cinza do caminho (128)
    base = G.copy()
    base[ink] = 255
    diff = (np.abs(base - O) > 100).sum()
    check(diff < 0.0005 * O.size, f"gabarito sem o cinza coincide com o labirinto impresso ({int(diff)} px)")
    nx, ny = d["dimensoes"]
    b = bbox(O.astype(np.uint8))
    cw, ch = (b[2] - b[0]) / nx, (b[3] - b[1]) / ny
    hit = 0
    for x, y in d["caminho"]:
        cx, cy = int(b[0] + (x + .5) * cw), int(b[1] + (y + .5) * ch)
        hit += int(ink[cy - 12:cy + 13, cx - 12:cx + 13].any())
    check(hit == len(d["caminho"]), f"{hit}/{len(d['caminho'])} celulas do caminho do JSON tem tinta cinza")
    check(d["caminho"][0] == d["inicio"] and d["caminho"][-1] == d["fim"], "caminho vai do inicio ao fim")
    bad = 0
    for (x0, y0), (x1, y1) in zip(d["caminho"], d["caminho"][1:]):
        assert abs(x0 - x1) + abs(y0 - y1) == 1
        ax, ay = b[0] + (x0 + .5) * cw, b[1] + (y0 + .5) * ch
        bx, by = b[0] + (x1 + .5) * cw, b[1] + (y1 + .5) * ch
        for t in np.linspace(0, 1, 25):
            px, py = int(ax + (bx - ax) * t), int(ay + (by - ay) * t)
            if O[py - 2:py + 3, px - 2:px + 3].min() < 60:
                bad += 1
                break
    check(bad == 0, f"nenhuma parede entre celulas consecutivas do caminho ({bad})")
    # celulas com tinta == celulas do caminho
    cells = set()
    for y in range(ny):
        for x in range(nx):
            cx, cy = int(b[0] + (x + .5) * cw), int(b[1] + (y + .5) * ch)
            if ink[cy - 12:cy + 13, cx - 12:cx + 13].any():
                cells.add((x, y))
    check(cells == {tuple(c) for c in d["caminho"]}, "celulas com tinta == celulas do caminho do JSON")
    save_key(name + "_gabarito.png", name + "_gabarito_key.png")
    return d["rotulo_inicio"], d["rotulo_fim"]


# ---------------------------------------------------------------- caca-palavras
DIRS = {"E": (0, 1), "S": (1, 0), "SE": (1, 1), "NE": (-1, 1)}


def wordsearch(grade_png, gab_png, jsonf, n):
    print(f"[caca-palavras] {gab_png}")
    O = L(grade_png)
    G = L(gab_png)
    d = J(jsonf)
    grade = d["grade"]
    check(len(grade) == n and all(len(r) == n for r in grade), f"grade {n}x{n}")
    check(O.shape == G.shape, "gabarito e grade impressa com o mesmo tamanho")
    hl = (G > 150) & (G < 215)  # cinza do destaque (176)
    base = G.copy()
    base[hl] = 255
    diff = (np.abs(base - O) > 100).sum()
    check(diff < 0.002 * O.size, f"gabarito sem o destaque coincide com a grade impressa ({int(diff)} px)")
    pos = set()
    for wd, cells in d["gabarito_posicoes"].items():
        spelled = "".join(grade[r][c] for r, c in cells)
        dr, dc = DIRS[d["direcoes"][wd]]
        r0, c0 = cells[0]
        straight = all(tuple(cells[i]) == (r0 + dr * i, c0 + dc * i) for i in range(len(cells)))
        check(spelled == wd and straight, f"{wd}: soletra nas posicoes do JSON ({d['direcoes'][wd]})")
        pos |= {tuple(c) for c in cells}
    check(set(d["gabarito_posicoes"]) == set(d["palavras"]), "todas as palavras da lista tem posicao")
    b = bbox(O.astype(np.uint8))
    cell = (b[2] - b[0]) / n
    got = set()
    for r in range(n):
        for c in range(n):
            cx, cy = int(b[0] + (c + .5) * cell), int(b[1] + (r + .5) * cell)
            # amostra o canto da celula (fora da letra): cinza do destaque
            ox, oy = int(b[0] + (c + .1) * cell), int(b[1] + (r + .1) * cell)
            if hl[oy - 3:oy + 4, ox - 3:ox + 4].mean() > .5:
                got.add((r, c))
    check(got == pos, f"celulas destacadas na imagem ({len(got)}) == uniao das posicoes do JSON ({len(pos)})")
    save_key(gab_png, gab_png.replace("_gabarito.png", "_gabarito_key.png"))


# ---------------------------------------------------------------- palavras cruzadas
def crossword():
    print("[palavras cruzadas] N6")
    d = J("extra_n6_palavras_cruzadas_gabarito.json")
    g = d["grade"]
    R, C = d["linhas"], d["colunas"]
    for it in d["across"]:
        s = "".join(g[it["r"]][it["c"] + i] for i in range(len(it["answer"])))
        check(s == it["answer"], f"across {it['n']} {it['answer']} soletra na grade")
    for it in d["down"]:
        s = "".join(g[it["r"] + i][it["c"]] for i in range(len(it["answer"])))
        check(s == it["answer"], f"down {it['n']} {it['answer']} soletra na grade")
    O = L("extra_n6_palavras_cruzadas_grade.png")
    G = L("extra_n6_palavras_cruzadas_gabarito.png")
    check(O.shape == G.shape, "gabarito e grade impressa com o mesmo tamanho")
    b = bbox(O.astype(np.uint8))
    cw, ch = (b[2] - b[0]) / C, (b[3] - b[1]) / R
    mism = 0
    for r in range(R):
        for c in range(C):
            cx, cy = int(b[0] + (c + .5) * cw), int(b[1] + (r + .85) * ch)
            filled = g[r][c] != "."
            gray_ans = 150 < G[cy - 4:cy + 5, cx - 4:cx + 5].mean() < 215  # fundo cinza do gabarito
            white_ans = O[cy - 4:cy + 5, cx - 4:cx + 5].mean() > 235
            if filled != gray_ans:
                mism += 1
            if filled and not white_ans:
                mism += 1
    check(mism == 0, f"celulas preenchidas (cinza no gabarito, branco no puzzle) == grade do JSON ({mism} divergencias)")
    # cada sequencia de 2+ letras e palavra da lista
    words = set(d["palavras"])
    seqs = []
    for r in range(R):
        seqs += ["".join(g[r]).split(".")]
    for c in range(C):
        seqs += ["".join(g[r][c] for r in range(R)).split(".")]
    runs = [s for row in seqs for s in row if len(s) >= 2]
    check(all(s in words for s in runs) and len(runs) == len(words), f"{len(runs)} sequencias de 2+ letras, todas na lista")
    save_key("extra_n6_palavras_cruzadas_gabarito.png", "extra_n6_palavras_cruzadas_gabarito_key.png")


# ---------------------------------------------------------------- respostas em texto
def textos():
    print("[texto] N1")
    un = J("extra_n1_unscramble.json")["items"]
    check(all(sorted(i["answer"]) == sorted(i["scrambled"]) and i["answer"] != i["scrambled"] and len(i["answer"]) == i["length"] for i in un), "8 palavras: embaralhada = anagrama da resposta")
    # anagramas alternativos que tambem sao pistas validas nao sao checaveis sem dicionario: revisao da pista no notes.md
    cd = J("extra_n1_codigo.json")
    dec = " / ".join(" ".join("".join(chr(64 + n) for n in w) for w in line) for line in cd["lines"])
    print("   ", dec)
    check(" ".join(" ".join("".join(chr(64 + n) for n in w) for w in line) for line in cd["lines"]) == cd["phrase"], "codigo decodifica a frase do JSON")
    print("[texto] N3")
    om = J("extra_n3_oilmath.json")
    f = {1: lambda p: p["burn"] - p["jar"], 2: lambda p: p["burn"] - p["now"], 3: lambda p: p["burn"] - p["have"], 4: lambda p: p["days"] * p["years"]}
    check(all(f[p["id"]](p["params"]) == p["answer"] for p in om["problems"]) and om["answers"] == [7, 5, 3, 16], "Oil Math: 4 contas recalculadas = 7, 5, 3, 16")
    print("[texto] N4")
    h = J("extra_n4_hanukkiahs.json")
    check([i["hanukkah_candles"] for i in h["draw_the_candles"]["items"]] == [2, 4, 6] and all(len(i["positions_lit"]) == i["night"] for i in h["draw_the_candles"]["items"]), "Draw the Candles: 2, 4, 6 + shamash")
    wn = h["which_night"]
    check([len(i["positions_lit"]) for i in wn["items"]] == [i["night"] for i in wn["items"]] == [5, 2, 7, 3] and sum(i["night"] for i in wn["items"]) == 17, "Which Night: 5, 2, 7, 3; total 17")
    print("[texto] N5")
    pt = J("extra_n5_padroes.json")["patterns"]
    sh = [p["shown"] for p in pt]
    check(sh[0] + ["H"] == (["N", "G", "H"] * 3)[:9], "padrao 1 (ciclo N G H): Hei")
    check(sh[1] + ["N"] == (["S", "S", "N"] * 3)[:9], "padrao 2 (ciclo S S N): Nun")
    seq = []
    for k, ch in enumerate(["G", "H", "S", "N"], 1):
        pass
    # blocos 1,2,3 e a 3a Nun: G, HH, SSS, NNN... mostrado ate NN
    seq = ["G"] + ["H"] * 2 + ["S"] * 3 + ["N"] * 3
    check(sh[2] == seq[:8] and seq[8 - 1 + 1 - 1] == "N" and pt[2]["answer"] == "N", "padrao 3 (blocos 1,2,3,...): proxima = Nun")
    bounce = ["circle", "square", "triangle", "diamond", "triangle", "square", "circle", "square", "triangle"]
    check(sh[3] + ["triangle"] == bounce, "padrao 4 (vai e volta): triangulo")
    check(sh[4] + ["square"] == ["circle", "circle", "square", "square", "triangle", "triangle", "circle", "circle", "square", "square"][:10], "padrao 5 (cada forma 2x): quadrado")
    check(all(b - a == 4 for a, b in zip(sh[5], sh[5][1:])) and sh[5][-1] + 4 == 24, "padrao 6 (+4): 24")
    print("[texto] N7")
    pl = J("extra_n7_pilhas_logica.json")
    check(all((p["right"] > p["left"]) == (p["more"] == "right") and p["left"] != p["right"] for p in pl["piles"]["pairs"]) and pl["piles"]["answers"] == ["right", "left", "right", "left", "right", "left"], "6 pares: maior pilha recalculada")
    lg = pl["who_gets_what"]
    kids, acts = lg["kids"], list(lg["acts"])
    sols = []
    for perm in itertools.permutations(acts):
        a = dict(zip(kids, perm))
        ok = True
        for t in lg["clue_tuples"]:
            if t[0] == "not":
                ok &= a[t[1]] != t[2]
            elif t[0] == "neither":
                ok &= a[t[1]] != t[3] and a[t[2]] != t[3]
            elif t[0] == "not2":
                ok &= a[t[1]] not in (t[2], t[3])
        if ok:
            sols.append(a)
    check(len(sols) == 1 and sols[0] == lg["solution"], f"Who Gets What: {len(sols)} solucao por forca bruta = {sols[0] if sols else None}")
    print("[texto] N8")
    mt = J("extra_n8_match.json")
    right = {r["pos"]: r for r in mt["right"]}
    check(all(right[a["fact_position"]]["night"] == a["night"] and right[a["fact_position"]]["fact"] == a["fact"] and mt["left"][a["night"] - 1]["title"] == a["title"] for a in mt["answers"]), "Match the Night: pares conferem com o JSON impresso")


if __name__ == "__main__":
    maze("extra_n2_labirinto_limpeza")
    maze("extra_n3_labirinto_oleo")
    maze("extra_n6_labirinto_latke")
    wordsearch("extra_n2_cacapalavras_templo_grade.png", "extra_n2_cacapalavras_templo_gabarito.png", "extra_n2_cacapalavras_templo_gabarito.json", 14)
    wordsearch("extra_n8_cacapalavras_noites_grade.png", "extra_n8_cacapalavras_noites_gabarito.png", "extra_n8_cacapalavras_noites_gabarito.json", 15)
    crossword()
    textos()
    print("\nTUDO OK" if ok_all else "\nHA FALHAS")
    sys.exit(0 if ok_all else 1)
