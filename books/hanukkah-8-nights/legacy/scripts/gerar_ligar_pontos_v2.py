"""
gerar_ligar_pontos_v2.py
Redesenho dos dois "ligar os pontos" da Noite 2 (hanukkiah, 30 pontos; menora do
Templo, 80 pontos). Os arquivos antigos (noite2_ligar_pontos_hanukia*,
noite2_ligar_pontos_menora*) NAO sao tocados; a saida tem sufixo _v2.

Estrategia
- Hanukkiah: 30 vertices desenhados a mao (lista explicita, nao reamostrada), figura
  simetrica em espelho: 9 pontas de vela (shamash central mais alto), barra de apoio
  em curva (sorriso), haste e base com pe. Ponto 1 = ponta do shamash.
- Menora: silhueta procedural da metade direita (haste central + 3 pares de bracos em
  semicirculos concentricos com espessura, copinhos no topo, pe redondo), com canais
  largos entre os bracos. Os cantos sao marcados como "obrigatorios"; os pontos que
  sobram ate 40 por lado sao inseridos nos trechos curvos pelo criterio de maior
  desvio (Douglas-Peucker ate N pontos). A metade esquerda e o espelho exato, entao
  80 = 2 x 40, sem pontos sobre o eixo. Ponto 1 = canto superior direito do copinho
  central; a numeracao desce pela direita e sobe pela esquerda.
- Rotulos: busca de posicao (angulos x distancias) com restricoes duras: caixas
  disjuntas entre si, longe de qualquer ponto, longe das linhas do contorno (que
  aparecem no gabarito) e mais perto do proprio ponto do que de qualquer outro.
  Preferencia: lado de fora do contorno; se nao der, o lado livre (dentro de um braco
  grosso ou entre bracos).
- Verificacoes por codigo (falham com AssertionError): contagem exata, contorno
  simples (nenhum par de segmentos nao adjacentes se cruza), simetria, distancia
  minima entre pontos, rotulos sem colisao.

Uso: python gerar_ligar_pontos_v2.py [hanukia|menora]   (sem argumento: os dois)
Saida: inputs/puzzle-assets/noite2_ligar_pontos_{hanukia,menora}_v2{,_gabarito,_recorte,
       _gabarito_key}.png e _v2_gabarito.json
"""
import json
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

_AQUI = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("N2_OUT_DIR") or os.path.normpath(
    os.path.join(_AQUI, "..", "..", "inputs", "puzzle-assets"))
FONTE = os.path.normpath(os.path.join(_AQUI, "..", "..", "..", "..", "fonts",
                                      "AtkinsonHyperlegible-Bold.ttf"))

CINZA_LINHA = (70, 70, 70)


# ----------------------------------------------------------------------------
# Geometria / verificacoes
# ----------------------------------------------------------------------------

def _ccw(p, q, r):
    return (r[1] - p[1]) * (q[0] - p[0]) - (q[1] - p[1]) * (r[0] - p[0])


def segmentos_se_cruzam(a1, a2, b1, b2):
    d1, d2, d3, d4 = _ccw(b1, b2, a1), _ccw(b1, b2, a2), _ccw(a1, a2, b1), _ccw(a1, a2, b2)
    return ((d1 > 0 > d2) or (d1 < 0 < d2)) and ((d3 > 0 > d4) or (d3 < 0 < d4))


def verificar_simples(pts):
    n = len(pts)
    seg = [(pts[i], pts[(i + 1) % n]) for i in range(n)]
    for i in range(n):
        for k in range(i + 2, n):
            if i == 0 and k == n - 1:
                continue
            if segmentos_se_cruzam(*seg[i], *seg[k]):
                raise AssertionError(f"auto-intersecao entre segmentos {i + 1} e {k + 1}")
    # nenhum ponto toca (colinear) outro segmento nao adjacente
    for j in range(n):
        for i in range(n):
            if j in (i, (i + 1) % n):
                continue
            if _dist_ponto_seg(pts[j], *seg[i]) < 1e-6:
                raise AssertionError(f"ponto {j + 1} toca o segmento {i + 1}")
    return True


def _dist_ponto_seg(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2))
    return math.hypot(p[0] - (ax + t * dx), p[1] - (ay + t * dy))


def verificar_simetria(pts, tol=1e-6):
    """Espelho no eixo x=0: para cada ponto existe o ponto (-x, y) e a ordem e
    espelhada (i <-> (c - i) mod n, com c determinado pelo ponto 1/2)."""
    n = len(pts)
    conj = {(round(x, 4), round(y, 4)) for x, y in pts}
    for x, y in pts:
        assert (round(-x, 4), round(y, 4)) in conj, f"sem espelho para ({x},{y})"
    # ordem: ponto k (0-based) <-> ponto (c - k) mod n
    for c in range(n):
        if all(abs(pts[k][0] + pts[(c - k) % n][0]) < tol and abs(pts[k][1] - pts[(c - k) % n][1]) < tol
               for k in range(n)):
            return True
    raise AssertionError("ordem dos pontos nao e simetrica")


def area_assinada(pts):
    n = len(pts)
    return sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n)) / 2


# ----------------------------------------------------------------------------
# Forma 1: hanukkiah (30 vertices, a mao)
# ----------------------------------------------------------------------------

def vertices_hanukia():
    """Metade direita, de cima para baixo (sentido horario na imagem, y para baixo).
    Eixo: ponta do shamash (x=0) e centro do pe (x=0). 14 vertices por lado + 2 no eixo.
    9 pontas de vela com passo 46 (shamash 85 mais alto), barra FINA em sorriso, haste fina
    e base com pe: leitura de candelabro, nao de coroa (uma barra grossa lembrava taca)."""
    p = 46
    direita = []
    for i in range(4):
        direita.append((p * i + p / 2, 100))   # vale entre velas (base compartilhada)
        direita.append((p * (i + 1), 0))       # ponta da vela
    direita += [
        (4 * p + 8, 126),   # ponta de fora da barra (lado de baixo)
        (110, 144),         # barra em curva (sorriso)
        (14, 158),          # barra encontra a haste
        (14, 236),          # pe da haste
        (78, 250),          # ombro da base
        (104, 288),         # canto externo inferior da base
    ]
    topo = (0.0, -62.0)
    centro_pe = (0.0, 276.0)   # base com leve arco para cima no centro
    esquerda = [(-x, y) for x, y in reversed(direita)]
    return [topo] + [(float(x), float(y)) for x, y in direita] + [centro_pe] + esquerda


# ----------------------------------------------------------------------------
# Forma 2: menora do Templo (procedural)
# ----------------------------------------------------------------------------

def _arco(cx, cy, r, a0, a1, passo=0.75):
    """Pontos do arco de a0 a a1 (graus, y para baixo: 0 = direita, 90 = baixo)."""
    n = max(2, int(abs(a1 - a0) / passo))
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]


def _quad(p0, p1, p2, n=24):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
            for t in (k / n for k in range(n + 1))]


def silhueta_menora_meia():
    """Metade direita (x>=0) do contorno externo, do topo-eixo ao fundo-eixo, em
    sentido horario. Devolve (denso, obrigatorio) com flags de canto por ponto."""
    AH = 20.0           # meia espessura dos bracos
    S = 24.0            # meia largura da haste central
    esp = 110.0         # distancia entre os bracos (raio da linha central)
    cup_h = 36.0        # altura do copinho
    cup_w = 36.0        # meia largura do topo do copinho
    ytop = -cup_h
    denso, canto = [], []

    def add(p, c=False):
        denso.append((float(p[0]), float(p[1])))
        canto.append(c)

    def add_poli(lista, c_ultimo=True):
        for k, p in enumerate(lista):
            add(p, c_ultimo and k == len(lista) - 1)

    add((0.0, ytop), False)             # eixo (nao sera ponto)
    add((cup_w, ytop), True)            # copinho central: canto superior
    add((S, 0.0), True)                 # copinho central: pescoco
    y_ant = 0.0
    for k in (1, 2, 3):
        r = esp * k
        ri, ro = r - AH, r + AH
        # haste ate o canto interno do braco k
        yi = math.sqrt(ri * ri - S * S)
        add((S, yi), True)
        # arco interno subindo ate a ponta do braco
        a_ini = math.degrees(math.asin(yi / ri))
        add_poli(_arco(0, 0, ri, a_ini, 0)[1:], True)
        # copinho do braco
        add((r - cup_w, ytop), True)
        add((r + cup_w, ytop), True)
        add((ro, 0.0), True)
        # arco externo descendo ate a haste
        yo = math.sqrt(ro * ro - S * S)
        a_fim = math.degrees(math.asin(yo / ro))
        add_poli(_arco(0, 0, ro, 0, a_fim)[1:], True)
        y_ant = yo
    # haste ate a base (pe minimo: 3 vertices por lado)
    y_haste = y_ant + 60
    add((S, y_haste), True)
    add((96.0, y_haste + 34), True)
    add((96.0, y_haste + 58), True)
    add((0.0, y_haste + 58), False)     # eixo (nao sera ponto)
    return denso, canto


def selecionar(denso, canto, k_alvo):
    """Escolhe exatamente k_alvo vertices entre os pontos densos: todos os cantos
    (exceto os do eixo) e, para completar, os pontos de maior desvio nos trechos curvos."""
    n = len(denso)
    sel = [i for i in range(1, n - 1) if canto[i]]
    assert len(sel) <= k_alvo, f"cantos ({len(sel)}) excedem {k_alvo}"
    bordas = [0] + sel + [n - 1]

    def melhor_no_trecho(a, b):
        pa, pb = np.array(denso[a]), np.array(denso[b])
        d = pb - pa
        L = np.hypot(*d) or 1.0
        pior, idx = 0.0, None
        for i in range(a + 1, b):
            q = np.array(denso[i]) - pa
            dev = abs(d[0] * q[1] - d[1] * q[0]) / L
            if dev > pior:
                pior, idx = dev, i
        return pior, idx

    while len(sel) < k_alvo:
        bordas = [0] + sorted(sel) + [n - 1]
        cand = [(melhor_no_trecho(a, b), a, b) for a, b in zip(bordas, bordas[1:]) if b - a > 1]
        (dev, idx), _, _ = max(cand, key=lambda t: t[0][0])
        if idx is None:
            break
        sel.append(idx)
    return [denso[i] for i in sorted(sel)]


def vertices_menora(k_meia=40):
    denso, canto = silhueta_menora_meia()
    meia = selecionar(denso, canto, k_meia)
    esq = [(-x, y) for x, y in reversed(meia)]
    return [(round(x, 2), round(y, 2)) for x, y in meia + esq]


# ----------------------------------------------------------------------------
# Rotulos sem colisao
# ----------------------------------------------------------------------------

def _fonte(tam):
    try:
        return ImageFont.truetype(FONTE, tam)
    except Exception:
        return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", tam)


def _normais_externas(pts):
    n = len(pts)
    sinal = 1 if area_assinada(pts) > 0 else -1
    saida = []
    for i in range(n):
        a, b = pts[i - 1], pts[(i + 1) % n]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1.0
        saida.append((ty / L * sinal, -tx / L * sinal))
    return saida


def _dist_ponto_caixa(p, box):
    cx = min(max(p[0], box[0]), box[2])
    cy = min(max(p[1], box[1]), box[3])
    return math.hypot(p[0] - cx, p[1] - cy)


def _dist_pontos_caixa(P, box):
    """P: array (m,2). Distancia minima de cada ponto a caixa."""
    cx = np.clip(P[:, 0], box[0], box[2])
    cy = np.clip(P[:, 1], box[1], box[3])
    return np.hypot(P[:, 0] - cx, P[:, 1] - cy)


def _amostras_contorno(pts, passo=3.0):
    out = []
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        m = max(1, int(math.dist(a, b) / passo))
        for t in range(m + 1):
            out.append((a[0] + (b[0] - a[0]) * t / m, a[1] + (b[1] - a[1]) * t / m))
    return np.array(out)


def _caixas_disjuntas(a, b, m):
    return a[2] + m < b[0] or b[2] + m < a[0] or a[3] + m < b[1] or b[3] + m < a[1]


def posicionar_rotulos(pts, raio, fonte, largura, altura, folga_ponto=12, folga_linha=12,
                       folga_caixa=36, ambiguidade=40, n_ang=36):
    """Devolve (caixas, info) onde caixas[i] = caixa da tinta do numero i+1."""
    n = len(pts)
    P = np.array(pts)
    amostras = _amostras_contorno(pts)
    normais = _normais_externas(pts)
    tmp = Image.new("L", (10, 10))
    dr = ImageDraw.Draw(tmp)
    cands, custo = [], []
    for i, (px, py) in enumerate(pts):
        bb = dr.textbbox((0, 0), str(i + 1), font=fonte)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        raio_i = raio * (1.7 if i == 0 else 1.0)
        lista = []
        for k in range(n_ang):
            ang = 2 * math.pi * k / n_ang
            dx, dy = math.cos(ang), math.sin(ang)
            for g in (raio_i + folga_ponto + 2, raio_i + folga_ponto + 14, raio_i + folga_ponto + 28,
                      raio_i + folga_ponto + 46, raio_i + folga_ponto + 70):
                ext = (w / 2) * abs(dx) + (h / 2) * abs(dy)
                cx, cy = px + dx * (g + ext), py + dy * (g + ext)
                box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
                if box[0] < 6 or box[1] < 6 or box[2] > largura - 6 or box[3] > altura - 6:
                    continue
                d_own = _dist_ponto_caixa((px, py), box)
                if d_own < raio_i + folga_ponto:
                    continue
                outros = np.delete(np.arange(n), i)
                d_out = _dist_pontos_caixa(P[outros], box)
                if d_out.min() < raio * (1.7 if False else 1.0) + folga_ponto:
                    continue
                if d_out.min() < d_own + ambiguidade:
                    continue
                if _dist_pontos_caixa(amostras, box).min() < folga_linha + 4:
                    continue
                fora = dx * normais[i][0] + dy * normais[i][1]
                c = (1 - fora) * 18 + d_own * 1.0 + abs(math.sin(2 * ang)) * 14
                lista.append((box, c))
        cands.append([b for b, _ in lista])
        custo.append([c for _, c in lista])
        assert lista, f"ponto {i + 1}: nenhum candidato de rotulo valido"

    # busca: descida de coordenadas com penalidade por sobreposicao
    escolha = [int(np.argmin(c)) for c in custo]

    def custo_i(i, k):
        c = custo[i][k]
        bi = cands[i][k]
        for j in range(n):
            if j != i and not _caixas_disjuntas(bi, cands[j][escolha[j]], folga_caixa):
                c += 1e6
        return c

    for _ in range(200):
        mudou = False
        ordem = sorted(range(n), key=lambda i: -custo_i(i, escolha[i]))
        for i in ordem:
            melhor = min(range(len(cands[i])), key=lambda k: custo_i(i, k))
            if custo_i(i, melhor) < custo_i(i, escolha[i]) - 1e-9:
                escolha[i] = melhor
                mudou = True
        if not mudou:
            break
    # recozimento simulado para desfazer conflitos restantes
    import random
    rnd = random.Random(7)
    def conflitantes():
        return [i for i in range(n) if custo_i(i, escolha[i]) >= 1e6]
    T = 20.0
    for it in range(60000):
        cf = conflitantes() if it % 50 == 0 else cf
        if not cf:
            break
        i = rnd.choice(cf) if rnd.random() < 0.7 else rnd.randrange(n)
        k = rnd.randrange(len(cands[i]))
        delta = custo_i(i, k) - custo_i(i, escolha[i])
        if delta <= 0 or rnd.random() < math.exp(-delta / T):
            escolha[i] = k
        T = max(2.0, T * 0.9999)
    caixas = [cands[i][escolha[i]] for i in range(n)]
    conflitos = [i + 1 for i in range(n) if custo_i(i, escolha[i]) >= 1e6]
    dentro = 0
    for i in range(n):
        cx, cy = (caixas[i][0] + caixas[i][2]) / 2, (caixas[i][1] + caixas[i][3]) / 2
        v = (cx - pts[i][0], cy - pts[i][1])
        if v[0] * normais[i][0] + v[1] * normais[i][1] < 0:
            dentro += 1
    return caixas, conflitos, dentro


def verificar_rotulos(pts, caixas, raio, folga_caixa=30, folga_linha=8):
    n = len(pts)
    P = np.array(pts)
    amostras = _amostras_contorno(pts, passo=2.0)
    for i in range(n):
        for j in range(i + 1, n):
            assert _caixas_disjuntas(caixas[i], caixas[j], folga_caixa), f"rotulos {i + 1} e {j + 1} colidem"
    for i in range(n):
        d = _dist_pontos_caixa(P, caixas[i])
        assert d.min() >= raio + 6, f"rotulo {i + 1} toca um ponto"
        assert int(np.argmin(d)) == i, f"rotulo {i + 1} esta mais perto do ponto {int(np.argmin(d)) + 1}"
        assert _dist_pontos_caixa(amostras, caixas[i]).min() >= folga_linha, f"rotulo {i + 1} cobre a linha do gabarito"
    return True


# ----------------------------------------------------------------------------
# Desenho
# ----------------------------------------------------------------------------

def renderizar(pts, nome, escala, fonte_px, raio_px, linha_px, margem_px=130):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    minx, miny = min(xs), min(ys)
    W = int((max(xs) - minx) * escala + 2 * margem_px)
    H = int((max(ys) - miny) * escala + 2 * margem_px)
    P = [((x - minx) * escala + margem_px, (y - miny) * escala + margem_px) for x, y in pts]
    fonte = _fonte(fonte_px)
    caixas, conflitos, dentro = posicionar_rotulos(P, raio_px, fonte, W, H)
    print(f"   {nome}: rotulos com conflito {conflitos}; {dentro} rotulos do lado de dentro")
    assert not conflitos, f'rotulos em conflito: {conflitos}'
    verificar_rotulos(P, caixas, raio_px)

    def desenhar(com_linhas):
        img = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(img)
        if com_linhas:
            d.line(P + [P[0]], fill=CINZA_LINHA, width=linha_px, joint="curve")
        for i, (x, y) in enumerate(P):
            r = raio_px
            if i == 0:   # ponto de partida: anel ao redor
                rr = raio_px * 1.7
                d.ellipse([x - rr, y - rr, x + rr, y + rr], outline="black", width=max(3, raio_px // 4),
                          fill="white")
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")
        for i, b in enumerate(caixas):
            bb = d.textbbox((0, 0), str(i + 1), font=fonte)
            d.text((b[0] - bb[0], b[1] - bb[1]), str(i + 1), fill="black", font=fonte)
        return img

    puzzle = desenhar(False)
    gab = desenhar(True)
    # recorte sem margem branca (mesma caixa para puzzle e gabarito)
    a = np.array(puzzle.convert("L"))
    ys_, xs_ = np.where(a < 250)
    pad = 14
    box = (max(0, xs_.min() - pad), max(0, ys_.min() - pad), min(W, xs_.max() + 1 + pad), min(H, ys_.max() + 1 + pad))
    base = os.path.join(OUT_DIR, f"noite2_ligar_pontos_{nome}_v2")
    puzzle.save(base + ".png")
    gab.save(base + "_gabarito.png")
    puzzle.crop(box).save(base + "_recorte.png")
    gab.crop(box).convert("L").save(base + "_gabarito_key.png")
    print(f"   PNG {W}x{H}; recorte {box[2] - box[0]}x{box[3] - box[1]}")
    return P, caixas, (W, H), box


def gerar(nome, pts, n_alvo, esp_min, escala, fonte_px, raio_px, linha_px):
    assert len(pts) == n_alvo, f"{len(pts)} pontos (esperado {n_alvo})"
    verificar_simples(pts)
    verificar_simetria(pts)
    n = len(pts)
    dmin = min(math.dist(pts[i], pts[(i + 1) % n]) for i in range(n))
    assert dmin >= esp_min, f"pontos consecutivos a {dmin:.1f} unidades (< {esp_min})"
    dmin_todos = min(math.dist(pts[i], pts[j]) for i in range(n) for j in range(i + 1, n))
    print(f"[{nome}] {n} pontos, simples, simetrico; menor distancia consecutiva {dmin:.1f}u "
          f"({dmin * escala:.0f}px), menor entre quaisquer {dmin_todos:.1f}u")
    P, caixas, (W, H), box = renderizar(pts, nome, escala, fonte_px, raio_px, linha_px)
    prefixo = f"noite2_ligar_pontos_{nome}_v2"
    dados = {
        "nome": prefixo,
        "n_pontos": n,
        "pontos_em_ordem": [[round(x, 2), round(y, 2)] for x, y in pts],
        "fechado": True,
        "verificado_poligono_simples": True,
        "simetria_espelho_verificada": True,
        "rotulos_sem_colisao_verificado": True,
        "escala_px_por_unidade": escala,
        "png_tamanho": [W, H],
        "recorte_caixa": [int(v) for v in box],
        "rotulos": [{"n": i + 1,
                     "ponto_px": [round(P[i][0], 1), round(P[i][1], 1)],
                     "caixa_px": [round(v, 1) for v in caixas[i]]} for i in range(n)],
    }
    with open(os.path.join(OUT_DIR, prefixo + "_gabarito.json"), "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)
    return dados


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg in ("", "hanukia"):
        gerar("hanukia", vertices_hanukia(), 30, esp_min=20, escala=6.4, fonte_px=72, raio_px=17, linha_px=9)
    if arg in ("", "menora"):
        gerar("menora", vertices_menora(40), 80, esp_min=8, escala=3.9, fonte_px=84, raio_px=16, linha_px=8)
    print("OK")
