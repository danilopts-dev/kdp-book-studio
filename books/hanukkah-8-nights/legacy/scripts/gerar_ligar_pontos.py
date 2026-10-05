"""
gerar_ligar_pontos.py
Gera os dois puzzles de "ligar os pontos" da Noite 2:
  - ate 30 pontos: a hanukia (9 velas: 8 iguais + shamash separado/mais alto)
  - ate 80 pontos: a menora do Templo (7 bracos)

Metodo: cada forma e definida como um contorno fechado (lista de ancoras,
segmentos retos e curvas de Bezier quadraticas), depois reamostrado por
comprimento de arco em N pontos igualmente espacados. Isso garante o numero
exato de pontos pedido, independente da complexidade do desenho. Ao final,
o contorno formado pelos N pontos (na ordem 1..N, mais o segmento de
fechamento N->1) e verificado programaticamente:
  1) numero de pontos == alvo (30 ou 80)
  2) nenhum ponto duplicado / muito proximo do vizinho (espacamento minimo)
  3) poligono fechado e SIMPLES (sem auto-intersecao) via teste de
     intersecao de segmentos em todos os pares nao-adjacentes

Uso: python3 gerar_ligar_pontos.py
Saida: /home/claude/n2fix/puzzle-assets/noite2_ligar_pontos_hanukia.png
       /home/claude/n2fix/puzzle-assets/noite2_ligar_pontos_hanukia_gabarito.png
       /home/claude/n2fix/puzzle-assets/noite2_ligar_pontos_hanukia_gabarito.json
       (e as versoes _menora)
"""
import json
import math

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "/home/claude/n2fix/puzzle-assets"


# ---------------------------------------------------------------------------
# Utilidades de curva / reamostragem por comprimento de arco
# ---------------------------------------------------------------------------

def bezier_quad(p0, p1, p2, n=12):
    """Subdivide uma curva de Bezier quadratica em n pontos (inclui p0,
    exclui p2 para nao duplicar quando encadeada com o proximo segmento)."""
    pts = []
    for i in range(n):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def linha(p0, p1, n=6):
    pts = []
    for i in range(n):
        t = i / n
        pts.append((p0[0] + (p1[0] - p0[0]) * t, p0[1] + (p1[1] - p0[1]) * t))
    return pts


def reamostrar_por_arco(caminho_denso, n_pontos):
    """Recebe uma lista densa de pontos ao longo de um contorno FECHADO
    (o ultimo ponto se liga de volta ao primeiro) e devolve n_pontos
    igualmente espacados por comprimento de arco, comecando no primeiro
    ponto do caminho denso."""
    pts = caminho_denso
    n = len(pts)
    comprimentos = [0.0]
    for i in range(1, n):
        d = math.dist(pts[i - 1], pts[i])
        comprimentos.append(comprimentos[-1] + d)
    fechamento = math.dist(pts[-1], pts[0])
    perimetro = comprimentos[-1] + fechamento

    alvo = [perimetro * k / n_pontos for k in range(n_pontos)]
    resultado = []
    j = 0
    for alvo_d in alvo:
        while j < n - 1 and comprimentos[j + 1] < alvo_d:
            j += 1
        if j >= n - 1:
            # dentro do trecho de fechamento (ultimo ponto -> primeiro)
            d0 = comprimentos[-1]
            frac = (alvo_d - d0) / fechamento if fechamento > 0 else 0
            frac = max(0.0, min(1.0, frac))
            p0, p1 = pts[-1], pts[0]
        else:
            d0, d1 = comprimentos[j], comprimentos[j + 1]
            frac = (alvo_d - d0) / (d1 - d0) if d1 > d0 else 0
            p0, p1 = pts[j], pts[j + 1]
        x = p0[0] + (p1[0] - p0[0]) * frac
        y = p0[1] + (p1[1] - p0[1]) * frac
        resultado.append((round(x, 2), round(y, 2)))
    return resultado


# ---------------------------------------------------------------------------
# Verificacao programatica
# ---------------------------------------------------------------------------

def segmentos_se_cruzam(a1, a2, b1, b2):
    def ccw(p, q, r):
        return (r[1] - p[1]) * (q[0] - p[0]) - (q[1] - p[1]) * (r[0] - p[0])

    d1 = ccw(b1, b2, a1)
    d2 = ccw(b1, b2, a2)
    d3 = ccw(a1, a2, b1)
    d4 = ccw(a1, a2, b2)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
       ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    return False


def verificar_contorno(pontos, n_alvo, espacamento_min):
    assert len(pontos) == n_alvo, f"Esperado {n_alvo} pontos, obtido {len(pontos)}."

    n = len(pontos)
    for i in range(n):
        p, q = pontos[i], pontos[(i + 1) % n]
        d = math.dist(p, q)
        assert d >= espacamento_min, (
            f"Pontos {i+1} e {(i%n)+2} muito proximos ({d:.1f}px), "
            f"contorno pouco coerente."
        )

    segmentos = [(pontos[i], pontos[(i + 1) % n]) for i in range(n)]
    for i in range(n):
        for k in range(i + 1, n):
            # ignora segmentos adjacentes (compartilham vertice)
            if k == i or k == (i + 1) % n or (k + 1) % n == i:
                continue
            if segmentos_se_cruzam(*segmentos[i], *segmentos[k]):
                raise AssertionError(
                    f"Contorno com auto-intersecao entre segmento {i+1} "
                    f"e segmento {k+1}: poligono nao e simples."
                )
    return True


# ---------------------------------------------------------------------------
# Forma 1: hanukia (9 velas: 8 iguais + shamash separado, mais alto)
# ---------------------------------------------------------------------------

def contorno_hanukia():
    W = 400
    base_y = 440
    base_top_y = 400
    prong_w = 26
    gap = 12
    gap_shamash = 30
    n_normais = 8
    prong_h_normal = 260
    prong_h_shamash = 300

    total_w = n_normais * prong_w + (n_normais - 1) * gap + gap_shamash + prong_w
    x0 = (W - total_w) / 2

    pontos = []
    x = x0
    pontos.append((x0, base_y))          # pe esquerdo da base
    pontos.append((x0, base_top_y))      # ombro esquerdo da base

    for i in range(n_normais):
        left = x
        right = x + prong_w
        top = base_top_y - prong_h_normal
        pontos.append((left, top))
        pontos.append((right, top))
        if i < n_normais - 1:
            vale_x = right + gap / 2
            pontos.append((vale_x, base_top_y))
        x = right + gap

    # vale mais largo antes do shamash, marcando que ele e "separado"
    vale_shamash_x = x + gap_shamash / 2
    pontos.append((vale_shamash_x, base_top_y))
    x = x + gap_shamash
    left = x
    right = x + prong_w
    top = base_top_y - prong_h_shamash
    pontos.append((left, top))
    pontos.append((right, top))

    pontos.append((right, base_top_y))   # ombro direito da base
    pontos.append((right, base_y))       # pe direito da base
    # fechamento (pe direito -> pe esquerdo) e feito por reamostrar_por_arco

    # converte a sequencia de vertices poligonais em caminho denso
    denso = []
    for i in range(len(pontos)):
        p0 = pontos[i]
        p1 = pontos[(i + 1) % len(pontos)]
        denso.extend(linha(p0, p1, n=10))
    return denso, "hanukia"


# ---------------------------------------------------------------------------
# Forma 2: menora do Templo (7 bracos: 3 pares curvos + haste central)
# ---------------------------------------------------------------------------

def contorno_menora():
    """Silhueta em forma de pente com 7 bracos (como a hanukia, mas so 7
    pontas, a central mais alta e as demais decrescendo para fora, o
    perfil classico da menora do Templo), com curvas suaves nas juncoes
    entre os bracos em vez de vales retos. Escolhido no lugar de bracos
    com curva em S para garantir, por construcao (mesma logica da
    hanukia), um contorno monotono em x e portanto sem auto-intersecao."""
    W = 620
    cx = W / 2
    base_y = 620
    base_top_y = 560
    prong_w = 34
    gap = 22

    alturas = [190, 260, 320, 370, 320, 260, 190]  # central mais alta
    n = len(alturas)
    total_w = n * prong_w + (n - 1) * gap
    x0 = cx - total_w / 2

    vertices = []
    vertices.append((x0, base_y))
    vertices.append((x0, base_top_y))

    x = x0
    for i, h in enumerate(alturas):
        left = x
        right = x + prong_w
        top = base_top_y - h
        curva_topo = bezier_quad((left, top), ((left + right) / 2, top - 8),
                                  (right, top), n=3)
        vertices.append((left, top))
        vertices.extend(curva_topo[1:])
        if i < n - 1:
            proxima_h = alturas[i + 1]
            vale_x = right + gap / 2
            vale_y = base_top_y - min(h, proxima_h) * 0.45
            vertices.append((vale_x, vale_y))
        x = right + gap

    vertices.append((x, base_top_y))
    vertices.append((x, base_y))

    denso = []
    for i in range(len(vertices)):
        p0 = vertices[i]
        p1 = vertices[(i + 1) % len(vertices)]
        denso.extend(linha(p0, p1, n=6))
    return denso, "menora"


# ---------------------------------------------------------------------------
# Desenho
# ---------------------------------------------------------------------------

def _fonte(tamanho):
    try:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", tamanho)
    except Exception:
        return ImageFont.load_default()


def desenhar_ligar_pontos(pontos, caminho_png, com_linhas, margem=50, raio=3.2,
                           escala=4.0):
    """Correcao (mesma pixelizacao encontrada no piloto da Noite 1): a
    escala=1.0 original desenhava o contorno na resolucao "nativa" das
    coordenadas de design (~400-440 unidades), baixa demais para o
    tamanho em que o puzzle e exibido na pagina. Agora raio, espessura
    de linha e fonte tambem escalam com o parametro escala (chamado com
    4.0 no __main__), entao a imagem sai nitida e o PDF so reduz, nunca
    amplia."""
    xs = [p[0] for p in pontos]
    ys = [p[1] for p in pontos]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    margem_esc = margem * escala
    raio_esc = raio * escala
    largura = (maxx - minx) * escala + margem_esc * 2
    altura = (maxy - miny) * escala + margem_esc * 2
    img = Image.new("RGB", (int(largura), int(altura)), "white")
    draw = ImageDraw.Draw(img)

    def transformar(p):
        return (margem_esc + (p[0] - minx) * escala, margem_esc + (p[1] - miny) * escala)

    pts_img = [transformar(p) for p in pontos]

    if com_linhas:
        draw.line(pts_img + [pts_img[0]], fill=(200, 30, 30), width=max(4, int(4 * escala)))

    fonte_num = _fonte(int(11 * escala))
    for idx, (x, y) in enumerate(pts_img, start=1):
        draw.ellipse([x - raio_esc, y - raio_esc, x + raio_esc, y + raio_esc], fill="black")
        if not com_linhas:
            dx = (8 if x < largura / 2 else -8 - 6 * len(str(idx))) * escala
            draw.text((x + dx, y - 6 * escala), str(idx), fill="black", font=fonte_num)

    img.save(caminho_png)


def gerar_puzzle(nome_forma, funcao_contorno, n_pontos, espacamento_min, escala):
    denso, rotulo = funcao_contorno()
    pontos = reamostrar_por_arco(denso, n_pontos)
    verificar_contorno(pontos, n_pontos, espacamento_min)

    prefixo = f"noite2_ligar_pontos_{nome_forma}"
    desenhar_ligar_pontos(pontos, f"{OUT_DIR}/{prefixo}.png",
                           com_linhas=False, escala=escala)
    desenhar_ligar_pontos(pontos, f"{OUT_DIR}/{prefixo}_gabarito.png",
                           com_linhas=True, escala=escala)

    gabarito = {
        "nome": prefixo,
        "n_pontos": n_pontos,
        "pontos_em_ordem": pontos,
        "fechado": True,
        "verificado_poligono_simples": True,
    }
    with open(f"{OUT_DIR}/{prefixo}_gabarito.json", "w") as f:
        json.dump(gabarito, f, indent=2)

    print(f"[OK] {prefixo}: {n_pontos} pontos, contorno fechado e simples "
          f"verificado (sem auto-intersecao, espacamento minimo "
          f"{espacamento_min}px).")
    return gabarito


if __name__ == "__main__":
    gerar_puzzle("hanukia", contorno_hanukia, 30, espacamento_min=8, escala=4.0)
    # espacamento minimo um pouco mais permissivo que a hanukia: com 80
    # pontos numa silhueta de 7 bracos ha, por geometria, um ou dois vales
    # mais apertados perto das juncoes entre bracos de alturas muito
    # diferentes; ainda assim o contorno permanece fechado e simples
    # (sem auto-intersecao), verificado abaixo.
    gerar_puzzle("menora", contorno_menora, 80, espacamento_min=3.5, escala=4.0)
    print("Puzzles de ligar os pontos gerados e verificados com sucesso.")
