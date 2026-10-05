"""
montar_gabaritos_key.py
Gera os recortes *_key.png usados em content/answer-key.typ e confere, por codigo,
cada gabarito contra o puzzle impresso e contra o JSON. Nao sobrescreve nada:
todas as saidas tem sufixo _key. Uso (a partir da raiz do estudio):

    python books/hanukkah-8-nights/legacy/scripts/montar_gabaritos_key.py

Conversoes para miolo P&B: amarelo (destaque do caca-palavras) -> cinza claro;
vermelho (caminho do labirinto / contorno do ligar-pontos) -> cinza escuro mais grosso.
"""
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[2]
PZ = ROOT / "inputs" / "puzzle-assets"
CT = ROOT / "content"
ok_all = True


def check(cond, msg):
    global ok_all
    print(("  ok   " if cond else "  FALHA ") + msg)
    if not cond:
        ok_all = False


def load(name, mode="RGB"):
    return Image.open(PZ / name).convert(mode)


def arr(im):
    return np.array(im)


def to_gray_key(im, yellow_to=205, red_to=95, dilate_red=0):
    """RGB -> L. Amarelo (255,235,150) vira cinza claro; vermelho (200,30,30) vira cinza escuro (dilatado)."""
    a = arr(im.convert("RGB")).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    yellow = (abs(r - 255) < 12) & (abs(g - 235) < 14) & (abs(b - 150) < 30)
    red = (abs(r - 200) < 40) & (g < 90) & (b < 90)
    gray = np.array(im.convert("L")).astype(np.uint8)
    out = gray.copy()
    out[yellow] = yellow_to
    redm = red
    if dilate_red:
        redm = ndimage.binary_dilation(red, iterations=dilate_red)
        # nao pintar por cima de preto (paredes/pontos)
        redm &= gray > 60
    out[redm] = red_to
    return Image.fromarray(out), yellow, red


def crop(im, ox, oy, w, h):
    return im.crop((ox, oy, ox + w, oy + h))


def bbox_nonwhite(a, thr=240):
    m = a < thr
    ys = np.where(m.any(1))[0]
    xs = np.where(m.any(0))[0]
    return xs[0], ys[0], xs[-1] + 1, ys[-1] + 1


def offset_of_recorte(orig_name, rec_name):
    O = arr(load(orig_name, "L"))
    R = arr(load(rec_name, "L"))
    bo, br = bbox_nonwhite(O), bbox_nonwhite(R)
    ox, oy = bo[0] - br[0], bo[1] - br[1]
    sub = O[oy:oy + R.shape[0], ox:ox + R.shape[1]]
    same = sub.shape == R.shape and int(np.abs(sub.astype(int) - R.astype(int)).sum()) == 0
    return ox, oy, R.shape[1], R.shape[0], same


def printed_words(typ, fn):
    src = (CT / typ).read_text(encoding="utf-8")
    ms = re.findall(r"#word-list\(([^)]*)\)", src)
    words = []
    for m in ms:
        words.append(re.findall(r'"([A-Z]+)"', m))
    return words


# ------------------------------------------------------------------ caca-palavras
def wordsearch(orig, rec, gab, jsonf, n, typ, which):
    print(f"[caca-palavras] {gab}")
    ox, oy, w, h, same = offset_of_recorte(orig, rec)
    check(same, f"recorte impresso {rec} = recorte exato de {orig} (offset {ox},{oy})")
    G = load(gab)
    gray, yellow, _ = to_gray_key(G)
    # gabarito sem destaque == puzzle original?
    O = arr(load(orig, "L")).astype(int)
    Gnoy = arr(G.convert("L")).astype(int).copy()
    Gnoy[yellow] = 255
    # o PNG de gabarito pinta o fundo amarelo; letras e linhas devem coincidir (tolerancia ao anti-alias na borda)
    diff = np.abs(Gnoy - O) > 100
    check(diff.sum() < 0.002 * diff.size, f"gabarito sem destaque coincide com o puzzle original ({int(diff.sum())} px de diferenca)")
    out = crop(gray, ox, oy, w, h)
    out.save(PZ / (gab.replace("_gabarito.png", "_gabarito_key.png")))
    # celulas destacadas == posicoes do JSON
    d = json.load(open(PZ / jsonf, encoding="utf-8"))
    grade = d["grade"]
    N = len(grade)
    check(N == n, f"grade {N}x{N}")
    bx0, by0, bx1, by1 = bbox_nonwhite(O.astype(np.uint8))
    cell = (bx1 - bx0) / N
    hl = set()
    for r in range(N):
        for c in range(N):
            cx, cy = int(bx0 + (c + .5) * cell), int(by0 + (r + .5) * cell)
            patch = yellow[cy - int(cell * .4):cy + int(cell * .4), cx - int(cell * .4):cx + int(cell * .4)]
            if patch.mean() > 0.5:
                hl.add((r, c))
    pos = set()
    for wd, cells in d["gabarito_posicoes"].items():
        spelled = "".join(grade[r][c] for r, c in cells)
        check(spelled == wd, f"{wd}: letras nas posicoes do JSON soletram a palavra")
        pos |= {(r, c) for r, c in cells}
    check(hl == pos, f"celulas destacadas na imagem ({len(hl)}) == uniao das posicoes do JSON ({len(pos)})")
    pw = printed_words(typ, None)[which]
    check(sorted(pw) == sorted(d["palavras"]), "lista impressa no livro == palavras do JSON")
    check(set(d["gabarito_posicoes"].keys()) == set(d["palavras"]), "todas as palavras da lista tem posicao no gabarito")
    # a grade impressa = grade do JSON (letras do JSON x grade impressa: confere por pixel, ja acima)


# ------------------------------------------------------------------ labirintos
def maze(name):
    print(f"[labirinto] {name}")
    G = load(name + "_gabarito.png")
    O = arr(load(name + ".png", "L")).astype(int)
    gray, _, red = to_gray_key(G, red_to=110, dilate_red=5)
    base = arr(G.convert("L")).astype(int).copy()
    base[red] = 255
    diff = np.abs(base - O) > 100
    check(diff.sum() < 0.0005 * diff.size, f"gabarito sem caminho coincide com o labirinto impresso ({int(diff.sum())} px)")
    gray.save(PZ / (name + "_gabarito_key.png"))
    d = json.load(open(PZ / (name + "_gabarito.json"), encoding="utf-8"))
    ncol, nrow = d["dimensoes"]
    b = bbox_nonwhite(O.astype(np.uint8))
    cw, ch = (b[2] - b[0]) / ncol, (b[3] - b[1]) / nrow
    hit = 0
    for x, y in d["caminho"]:
        cx, cy = int(b[0] + (x + .5) * cw), int(b[1] + (y + .5) * ch)
        hit += int(red[cy - 16:cy + 17, cx - 16:cx + 17].any())
        if not red[cy - 16:cy + 17, cx - 16:cx + 17].any():
            print('     (sem tinta no centro da celula', x, y, ')')
    check(hit == len(d["caminho"]), f"caminho do JSON ({len(d['caminho'])} celulas, {d['passos']} passos): {hit} celulas com tinta vermelha")
    check(d["caminho"][0] == d["inicio"] and d["caminho"][-1] == d["fim"], "caminho vai do inicio ao fim declarados")
    # o caminho nao pode atravessar parede: tinta vermelha nao se sobrepoe a pixels pretos do puzzle
    overlap = int(((O < 60) & red).sum())
    check(overlap < 200, f"tinta do caminho nao cobre paredes ({overlap} px)")
    # celulas consecutivas: passagem aberta (sem parede entre os centros)
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
    check(bad == 0, f"nenhuma parede entre celulas consecutivas do caminho ({bad} violacoes)")


# ------------------------------------------------------------------ ligar pontos
def dots(name, n_expected):
    print(f"[ligar-pontos] {name}")
    ox, oy, w, h, same = offset_of_recorte(name + ".png", name + "_recorte.png")
    check(same, f"recorte impresso = recorte exato do PNG original (offset {ox},{oy})")
    G = load(name + "_gabarito.png")
    gray, _, red = to_gray_key(G, red_to=95, dilate_red=2)
    O = arr(load(name + ".png", "L"))
    Ga = arr(G.convert("L"))
    # pontos pretos do gabarito (sem a linha vermelha) devem existir no original
    blk = (Ga < 60)
    check(float(((O < 120) & blk).sum()) / max(1, blk.sum()) > 0.98, "pontos pretos do gabarito aparecem no puzzle original")
    lab, n = ndimage.label(ndimage.binary_opening(blk, iterations=3))
    idx = range(1, n + 1)
    sizes = np.array(ndimage.sum(blk, lab, idx))
    cents = np.array(ndimage.center_of_mass(blk, lab, idx))  # (y, x)
    med = np.median(sizes)
    big = [i for i in range(n) if sizes[i] > 0.5 * med]
    # pontos muito proximos se fundem num componente (ex.: 32/40 e 34/38 da menora): conta pela area
    count = int(sum(max(1, round(sizes[i] / med)) for i in big))
    check(count == n_expected, f"{count} pontos pretos no gabarito por area ({len(big)} componentes; esperado {n_expected})")
    d0 = json.load(open(PZ / (name + "_gabarito.json"), encoding="utf-8"))
    P = np.array(d0["pontos_em_ordem"])  # (x, y)
    C = cents[big][:, ::-1]  # (x, y)
    s_x = (C[:, 0].max() - C[:, 0].min()) / (P[:, 0].max() - P[:, 0].min())
    s_y = (C[:, 1].max() - C[:, 1].min()) / (P[:, 1].max() - P[:, 1].min())
    ox0 = C[:, 0].min() - s_x * P[:, 0].min()
    oy0 = C[:, 1].min() - s_y * P[:, 1].min()
    miss = 0
    for x, y in P:
        px, py = int(round(s_x * x + ox0)), int(round(s_y * y + oy0))
        if not blk[py - 3:py + 4, px - 3:px + 4].any():
            miss += 1
    check(abs(s_x - s_y) < 0.02 and miss == 0, f"cada um dos {len(P)} pontos do JSON cai sobre um ponto preto do gabarito (escala {s_x:.2f}/{s_y:.2f}; fora: {miss})")
    d = json.load(open(PZ / (name + "_gabarito.json"), encoding="utf-8"))
    check(d["n_pontos"] == n_expected and d.get("fechado") and d.get("verificado_poligono_simples"), "JSON: n_pontos, contorno fechado, poligono simples")
    crop(gray, ox, oy, w, h).save(PZ / (name + "_gabarito_key.png"))


# ------------------------------------------------------------------ erros
def numbered(path_in, ids, boxes, path_out, depois):
    G = load(path_in, "L")
    D = arr(load(depois, "L")).astype(int)
    Ga = arr(G).astype(int)
    diff = np.abs(Ga - D) > 100
    # toda diferenca entre gabarito e "depois" impresso deve estar na borda (tracejado) de alguma caixa do JSON
    strips = np.zeros_like(diff)
    m = 8
    for i in ids:
        x, y, w, h = boxes[i]
        outer = np.zeros_like(diff)
        outer[max(0, y - m):y + h + m, max(0, x - m):x + w + m] = True
        inner = np.zeros_like(diff)
        inner[y + m:y + h - m, x + m:x + w - m] = True
        strips |= outer & ~inner
    check(not (diff & ~strips).any(), f"{path_in}: so ha tracejado (borda das {len(ids)} caixas do JSON); resto identico ao 'depois' impresso ({int((diff & ~strips).sum())} px fora)")
    # cada caixa do JSON tem tracejado de fato desenhado
    for i in ids:
        x, y, w, h = boxes[i]
        top = diff[y - 4:y + 5, x:x + w].any() or diff[y + h - 4:y + h + 5, x:x + w].any()
        check(top, f"caixa {i} do JSON esta desenhada no gabarito") if False else None
        if not top:
            check(False, f"caixa {i} do JSON nao aparece desenhada em {path_in}")
    im = G.convert("RGB")
    dr = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 84)
    except Exception:
        font = ImageFont.load_default()
    for i in ids:
        x, y, w, h = boxes[i]
        r = 54
        cx, cy = x + w / 2, y + h / 2
        # onde nao for empurrar o circulo para fora da imagem
        cy = min(max(cy, r + 4), G.size[1] - r - 4)
        dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")
        t = str(i)
        tw = dr.textlength(t, font=font)
        dr.text((cx - tw / 2, cy - 50), t, fill="white", font=font)
    im.convert("L").save(PZ / path_out)


def erros():
    print("[erros] noite 2")
    d = json.load(open(PZ / "noite2_erros_gabarito.json", encoding="utf-8"))
    boxes = {o["id"]: o["caixa"] for o in d["objetos"]}
    check(d["estrela_1_ids"] == [1, 2, 3, 4, 5] and d["estrela_2_ids"] == list(range(1, 11)), "JSON: 5 diferencas (nivel 1) e 10 (nivel 2)")
    numbered("noite2_erros5_gabarito.png", d["estrela_1_ids"], boxes, "noite2_erros5_gabarito_key.png", "noite2_erros5_depois.png")
    numbered("noite2_erros10_gabarito.png", d["estrela_2_ids"], boxes, "noite2_erros10_gabarito_key.png", "noite2_erros10_depois.png")
    # a imagem "antes" impressa deve ter o objeto onde o JSON diz (tinta em cada caixa)
    A = arr(load("noite2_erros5_antes.png", "L"))
    for o in d["objetos"]:
        x, y, w, h = o["caixa"]
        check((A[y:y + h, x:x + w] < 128).mean() > 0.01, f"objeto {o['id']} ({o['nome']}) tem tinta no 'antes'")


# ------------------------------------------------------------------ sudoku / jarro
def sudoku(name, n, bh, bw):
    print(f"[sudoku] {name}")
    d = json.load(open(PZ / (name + "_gabarito.json"), encoding="utf-8"))
    sol, pz = d["solucao"], d["puzzle"]
    check(all(sorted(r) == list(range(1, n + 1)) for r in sol), "linhas validas")
    check(all(sorted(sol[r][c] for r in range(n)) == list(range(1, n + 1)) for c in range(n)), "colunas validas")
    boxes_ok = True
    for r0 in range(0, n, bh):
        for c0 in range(0, n, bw):
            vals = sorted(sol[r][c] for r in range(r0, r0 + bh) for c in range(c0, c0 + bw))
            boxes_ok &= vals == list(range(1, n + 1))
    check(boxes_ok, "caixas validas")
    check(all(pz[r][c] in (0, sol[r][c]) for r in range(n) for c in range(n)), "pistas do puzzle coincidem com a solucao")
    ox, oy, w, h, same = offset_of_recorte(name + ".png", name + "_recorte.png")
    check(same, f"recorte impresso = recorte exato do PNG original (offset {ox},{oy})")
    O = arr(load(name + ".png", "L")).astype(int)
    G = arr(load(name + "_gabarito.png", "L")).astype(int)
    b = bbox_nonwhite(O.astype(np.uint8))
    cw = (b[2] - b[0]) / n
    m = int(cw * 0.12)

    def cell(A, r, c):
        return A[int(b[1] + r * cw) + m:int(b[1] + (r + 1) * cw) - m, int(b[0] + c * cw) + m:int(b[0] + (c + 1) * cw) - m]

    # celulas de pista: gabarito == puzzle; celulas vazias: puzzle vazio e gabarito com simbolo
    clues_same = all(np.abs(cell(G, r, c) - cell(O, r, c)).mean() < 2 for r in range(n) for c in range(n) if pz[r][c])
    check(clues_same, "celulas de pista identicas no puzzle impresso e no gabarito")
    empties_blank = all((cell(O, r, c) < 128).mean() < 0.003 for r in range(n) for c in range(n) if not pz[r][c])
    check(empties_blank, "celulas vazias do puzzle impresso estao em branco")
    # simbolo de cada celula do gabarito == simbolo de referencia (celula de pista com o mesmo numero)
    ref = {}
    for r in range(n):
        for c in range(n):
            if pz[r][c]:
                ref.setdefault(pz[r][c], cell(G, r, c))
    check(set(ref) == set(range(1, n + 1)), "todos os simbolos aparecem entre as pistas (referencia para conferir a imagem)")
    def norm(a):
        # recorta ao retangulo da tinta e normaliza para 96x96 (independe de deslocamento/centralizacao)
        m = a < 128
        ys, xs = np.where(m)
        sub = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.uint8)
        return np.array(Image.fromarray(sub).resize((96, 96), Image.LANCZOS)).astype(float)

    def dist(a, b2):
        return float(np.abs(norm(a) - norm(b2)).mean())
    bad, margins = [], []
    for r in range(n):
        for c in range(n):
            sc = {k: dist(cell(G, r, c), v) for k, v in ref.items()}
            best = min(sc, key=sc.get)
            others = min(v for k, v in sc.items() if k != best)
            if best != sol[r][c] or others - sc[best] < 5:
                print('     debug', (r + 1, c + 1), 'esperado', sol[r][c], {k: round(v, 1) for k, v in sc.items()})
            margins.append(others - sc[best])
            if best != sol[r][c]:
                bad.append((r + 1, c + 1))
    check(min(margins) > 5, f"o teste distingue os simbolos (menor margem de diferenca media entre o melhor e o segundo simbolo: {min(margins):.1f})")
    check(not bad, f"simbolo desenhado em cada celula do gabarito == simbolo do JSON (divergentes: {bad})")
    crop(load(name + "_gabarito.png"), ox, oy, w, h).convert("L").save(PZ / (name + "_gabarito_key.png"))


def jarro():
    print("[jarro diferente]")
    d = json.load(open(PZ / "noite3_jarro_diferente_gabarito.json", encoding="utf-8"))
    G = load("noite3_jarro_diferente_gabarito.png", "L")
    O = arr(load("noite3_jarro_diferente.png", "L")).astype(int)
    Ga = arr(G).astype(int)
    diff = np.abs(Ga - O) > 100
    ys, xs = np.where(diff)
    cx, cy = xs.mean(), ys.mean()
    colw = O.shape[1] / d["colunas"]
    roww = O.shape[0] / d["linhas"]
    col, row = int(cx // colw) + 1, int(cy // roww) + 1
    check([row, col] == d["posicao_linha_coluna_1_based"], f"circulo do gabarito esta no jarro (linha,coluna) = ({row},{col}) do JSON")
    b = bbox_nonwhite(Ga.astype(np.uint8))
    pad = 40
    box = (max(0, b[0] - pad), max(0, b[1] - pad), min(G.size[0], b[2] + pad), min(G.size[1], b[3] + pad))
    G.crop(box).save(PZ / "noite3_jarro_diferente_gabarito_key.png")
    print("  recorte do gabarito:", box)


# ------------------------------------------------------------------ moedas
def moedas():
    print("[count the gelt]")
    d = json.load(open(PZ / "noite7_contar_moedas_gabarito.json", encoding="utf-8"))
    tot = {g["id"]: g["total"] for g in d["grupos"]}
    for gid, f in (("grupo_a", "noite7_contar_moedas_grupo_a_recorte.png"), ("grupo_b", "noite7_contar_moedas_grupo_b_recorte.png")):
        a = arr(load(f, "L")) < 128
        # cada moeda e um anel: preenche os furos e conta os componentes de tamanho razoavel
        filled = ndimage.binary_fill_holes(ndimage.binary_closing(a, iterations=2))
        lab, n = ndimage.label(filled)
        sizes = ndimage.sum(filled, lab, range(1, n + 1))
        coins = int((sizes > 0.5 * np.median(sizes)).sum())
        check(coins == tot[gid], f"{gid}: {coins} moedas na imagem impressa == total do JSON ({tot[gid]})")


def contas():
    print("[contas dos enunciados impressos]")
    n5 = json.load(open(PZ / "noite5_problemas_gelt.json", encoding="utf-8"))
    n7 = json.load(open(PZ / "noite7_problemas_moedas.json", encoding="utf-8"))
    for p in n5 + n7:
        v = eval(p["operacao"].replace("/", "//") if False else p["operacao"])
        check(abs(v - p["resposta"]) < 1e-9, f"{p['id']}: {p['operacao']} = {v}")
    check(sum(n + 1 for n in range(1, 9)) == 44 and sum(range(1, 9)) == 36, "N4: (1+...+8) + 8 shamash = 36 + 8 = 44")
    # operacoes impressas no n5.typ
    src = (CT / "n5.typ").read_text(encoding="utf-8")
    for op in ("12 + 9", "24 / 4", "(18 + 14) / 2", "15 + 22 + 18 + 27"):
        check(op in src, f"n5.typ imprime a operacao '{op}'")


def main():
    wordsearch("cacapalavras_noite1.png", "cacapalavras_noite1_grade.png", "cacapalavras_noite1_gabarito.png",
               "cacapalavras_noite1_gabarito.json", 10, "n1.typ", 0)
    wordsearch("noite6_cacapalavras_cozinha.png", "noite6_cacapalavras_cozinha_grade.png",
               "noite6_cacapalavras_cozinha_gabarito.png", "noite6_cacapalavras_cozinha_gabarito.json", 10, "n6.typ", 0)
    wordsearch("noite6_cacapalavras_14x14.png", "noite6_cacapalavras_14x14_grade.png",
               "noite6_cacapalavras_14x14_gabarito.png", "noite6_cacapalavras_14x14_gabarito.json", 14, "n6.typ", 1)
    for m in ("labirinto_facil", "labirinto_medio", "noite7_labirinto_tzedaka"):
        maze(m)
    dots("noite2_ligar_pontos_hanukia", 30)
    dots("noite2_ligar_pontos_menora", 80)
    erros()
    sudoku("noite3_sudoku4x4", 4, 2, 2)
    sudoku("noite3_sudoku6x6", 6, 2, 3)
    jarro()
    moedas()
    contas()
    print("\nTUDO OK" if ok_all else "\nHA FALHAS")
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
