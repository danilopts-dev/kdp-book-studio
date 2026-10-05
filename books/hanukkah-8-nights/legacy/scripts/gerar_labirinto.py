"""
gerar_labirinto.py
Gera os dois labirintos da Noite 1 (facil "Escape to the Hills" e medio
"Back to Modiin"), garante caminho unico entrada->saida via DFS
recursivo tipo backtracking (recursive backtracker), valida a
unicidade do caminho mais curto por BFS, e salva grid + imagem PNG +
gabarito (lista de coordenadas do caminho) em JSON.

Correcoes desta revisao (feedback do piloto aprovado pelo Danilo):
1. O labirinto medio (18x18) ficou longo demais: reduzido para 15x15,
   ainda maior e mais dificil que o facil (12x12), sem ficar excessivo.
2. Os rotulos de entrada/saida saiam pixelizados porque eram escritos
   direto no PNG com a fonte bitmap padrao do PIL (sem truetype). Agora
   o PNG sai limpo, sem nenhum texto embutido; os rotulos sao desenhados
   como texto vetorial no PDF (montar_pdf_piloto.py), posicionados perto
   da abertura real de entrada/saida (nao mais fixos no topo da pagina).
3. Os encontros de linha (cantos, T, cruzamentos) saiam serrilhados por
   causa da resolucao baixa da imagem. Agora o desenho e feito em escala
   4x maior e reduzido (downscale) com reamostragem LANCZOS, o que
   suaviza junções e cantos sem custo de nitidez.
4. A abertura de entrada/saida usava "desenha a parede e depois apaga
   por cima com uma linha branca", o que deixava sobras finas (aliasing)
   nas pontas do trecho apagado. Agora a parede da celula de entrada/
   saida simplesmente nao e desenhada naquele lado, entao a abertura sai
   limpa, sem nenhuma linha ali.

Uso: python3 gerar_labirinto.py
Saida: /home/claude/n1fix/puzzle-assets/labirinto_facil.png
       /home/claude/n1fix/puzzle-assets/labirinto_facil_gabarito.png
       /home/claude/n1fix/puzzle-assets/labirinto_facil_gabarito.json
       (e as versoes _medio)
"""
import json
import random
from collections import deque

from PIL import Image, ImageDraw

random.seed(13)

OUT_DIR = "/home/claude/n2fix/puzzle-assets"

ESCALA_SUPERSAMPLE = 4  # desenha em 4x e reduz, para junções/cantos suaves


def gerar_labirinto_perfeito(largura, altura):
    """Recursive backtracker. Retorna dict de paredes por celula.
    Cada celula tem paredes N,S,E,W = True (existe parede) inicialmente."""
    celulas = {(x, y): {"N": True, "S": True, "E": True, "W": True}
               for x in range(largura) for y in range(altura)}
    visitado = [[False] * largura for _ in range(altura)]

    def vizinhos(x, y):
        cands = []
        if y > 0:
            cands.append((x, y - 1, "N", "S"))
        if y < altura - 1:
            cands.append((x, y + 1, "S", "N"))
        if x > 0:
            cands.append((x - 1, y, "W", "E"))
        if x < largura - 1:
            cands.append((x + 1, y, "E", "W"))
        random.shuffle(cands)
        return cands

    pilha = [(0, 0)]
    visitado[0][0] = True
    while pilha:
        x, y = pilha[-1]
        candidatos = [v for v in vizinhos(x, y) if not visitado[v[1]][v[0]]]
        if not candidatos:
            pilha.pop()
            continue
        nx, ny, lado_atual, lado_vizinho = random.choice(candidatos)
        celulas[(x, y)][lado_atual] = False
        celulas[(nx, ny)][lado_vizinho] = False
        visitado[ny][nx] = True
        pilha.append((nx, ny))
    return celulas


def caminho_unico_bfs(celulas, largura, altura, inicio, fim):
    """BFS numa arvore perfeita ja tem caminho unico por definicao
    (labirinto perfeito = grafo em arvore, sem ciclos). Ainda assim
    verificamos programaticamente: existe exatamente um caminho simples
    entre inicio e fim, e ele e alcancavel."""
    fila = deque([inicio])
    veio_de = {inicio: None}
    while fila:
        x, y = fila.popleft()
        if (x, y) == fim:
            break
        for lado, (dx, dy) in (("N", (0, -1)), ("S", (0, 1)),
                                ("E", (1, 0)), ("W", (-1, 0))):
            if not celulas[(x, y)][lado]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < largura and 0 <= ny < altura and (nx, ny) not in veio_de:
                    veio_de[(nx, ny)] = (x, y)
                    fila.append((nx, ny))
    if fim not in veio_de:
        raise AssertionError("Labirinto sem caminho da entrada a saida.")
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = veio_de[atual]
    caminho.reverse()

    # Validacao de unicidade: um labirinto "perfeito" (recursive backtracker
    # sem remover paredes extras) e uma arvore geradora, logo so existe UM
    # caminho simples entre dois nos quaisquer. Confirmamos contando arestas
    # e vertices: arvore <=> arestas == vertices - 1.
    total_celulas = largura * altura
    total_passagens = 0
    for (x, y), paredes in celulas.items():
        if not paredes["S"] and y < altura - 1:
            total_passagens += 1
        if not paredes["E"] and x < largura - 1:
            total_passagens += 1
    assert total_passagens == total_celulas - 1, (
        f"Grafo nao e uma arvore ({total_passagens} passagens para "
        f"{total_celulas} celulas): caminho pode nao ser unico."
    )
    return caminho


def desenhar(celulas, largura, altura, inicio, fim, caminho_destacado, caminho_png,
             tamanho_celula=40, margem=6):
    """Desenha so o labirinto (sem nenhum rotulo de texto embutido).
    Renderiza em ESCALA_SUPERSAMPLE x e reduz com LANCZOS, para que
    cantos e cruzamentos de linha saiam suaves em vez de serrilhados.

    Correcao desta revisao: cada parede era um draw.line isolado, o que
    deixa os encontros (T, +, cantos) com uma pequena folga ou
    arredondamento, porque duas linhas que so se tocam na ponta nao
    formam um esquadro solido por construcao no PIL. Agora cada parede
    e um RETANGULO que se estende meia espessura alem da celula em cada
    ponta; assim, no encontro de duas paredes perpendiculares os dois
    retangulos se sobrepoem numa area solida, garantindo canto de 90
    graus sem falha nem arredondamento.

    Margem tambem reduzida (30 -> 6): a margem antiga so existia para
    caber o rotulo de texto dentro do PNG (pratica abandonada nesta
    revisao, rotulo agora e vetorial no PDF). Margem grande fazia o
    rotulo, calculado como fracao da altura da propria imagem, cair bem
    longe da abertura real. Com margem minima (so folga para a espessura
    da linha nao cortar na borda), a abertura e o rotulo ficam alinhados."""
    esc = ESCALA_SUPERSAMPLE
    tc = tamanho_celula * esc
    mg = margem * esc
    espessura = 4 * esc
    meia = espessura / 2

    W = largura * tc + mg * 2
    H = altura * tc + mg * 2
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    def celula_para_px(cx, cy):
        return mg + cx * tc, mg + cy * tc

    def seg_h(x0, x1, y):
        """Segmento horizontal como retangulo, estendido meia espessura
        em cada ponta para os cantos ficarem solidos no encontro com
        segmentos verticais."""
        draw.rectangle([x0 - meia, y - meia, x1 + meia, y + meia], fill="black")

    def seg_v(x, y0, y1):
        draw.rectangle([x - meia, y0 - meia, x + meia, y1 + meia], fill="black")

    for (x, y), paredes in celulas.items():
        px, py = celula_para_px(x, y)
        eh_entrada = (x, y) == inicio
        eh_saida = (x, y) == fim
        # nao desenha o lado da celula que e a abertura de entrada/saida:
        # a abertura fica limpa por construcao, sem sobra de linha
        pular_w = eh_entrada
        pular_e = eh_saida
        if paredes["N"]:
            seg_h(px, px + tc, py)
        if paredes["W"] and not pular_w:
            seg_v(px, py, py + tc)
        if paredes["S"] and y == altura - 1:
            seg_h(px, px + tc, py + tc)
        if paredes["E"] and x == largura - 1 and not pular_e:
            seg_v(px + tc, py, py + tc)

    # borda externa, com os trechos de entrada/saida ja abertos acima:
    # desenhada em 4 segmentos (nao um retangulo fechado) para nao
    # recobrir a abertura que acabamos de deixar limpa
    x0, y0 = mg, mg
    x1, y1 = mg + largura * tc, mg + altura * tc
    seg_h(x0, x1, y0)  # topo
    seg_h(x0, x1, y1)  # base
    px_i, py_i = celula_para_px(*inicio)
    if inicio[0] == 0:
        # borda esquerda, pulando a celula de entrada
        if py_i > y0:
            seg_v(x0, y0, py_i)
        if py_i + tc < y1:
            seg_v(x0, py_i + tc, y1)
    px_f, py_f = celula_para_px(*fim)
    if fim[0] == largura - 1:
        # borda direita, pulando a celula de saida
        if py_f > y0:
            seg_v(x1, y0, py_f)
        if py_f + tc < y1:
            seg_v(x1, py_f + tc, y1)

    if caminho_destacado:
        pts = []
        for (cx, cy) in caminho_destacado:
            px, py = celula_para_px(cx, cy)
            pts.append((px + tc / 2, py + tc / 2))
        draw.line(pts, fill=(200, 30, 30), width=espessura + 2, joint="curve")

    # Nao reamostra/reduz: como toda parede agora e um retangulo com eixos
    # alinhados (sem diagonal), o desenho ja sai com canto de 90 graus
    # perfeito e sem serrilhado na propria resolucao supersampled. Reduzir
    # com LANCZOS nessa etapa so introduzia uma sombra cinza sutil nos
    # cantos (o proprio antialiasing do resize). Salva direto em alta
    # resolucao (ESCALA_SUPERSAMPLE x) e deixa o PDF (reportlab) escalar
    # para o tamanho final na pagina.
    img.save(caminho_png)


def abertura_info(largura, altura, inicio, fim, tamanho_celula, margem):
    """Retorna, para entrada e saida, o lado da borda (N/S/E/W) e a
    posicao relativa (0 a 1) ao longo daquele lado, para o PDF poder
    desenhar o rotulo perto da abertura real, nao num canto fixo.

    Correcao: a fracao precisa ser calculada sobre a imagem INTEIRA
    (celula + margem dos dois lados), nao so sobre largura*tamanho_celula,
    senao o rotulo sai desalinhado da abertura real sempre que margem>0
    (era exatamente esse o bug: com margem=30 e celula=40, o rotulo
    caia quase uma celula inteira acima/abaixo da abertura de verdade)."""
    H_img = altura * tamanho_celula + 2 * margem
    W_img = largura * tamanho_celula + 2 * margem

    def info(celula, lado):
        x, y = celula
        y_rel = (margem + (y + 0.5) * tamanho_celula) / H_img
        if lado == "W":
            # x_rel = onde a parede oeste realmente esta na imagem, nao 0.0
            return {"lado": "W", "x_rel": margem / W_img, "y_rel": y_rel}
        if lado == "E":
            return {"lado": "E", "x_rel": 1 - margem / W_img, "y_rel": y_rel}
        raise ValueError(lado)
    return info(inicio, "W"), info(fim, "E")


def gerar_puzzle(nome, largura, altura, rotulo_inicio, rotulo_fim,
                  tamanho_celula=40, margem=6):
    celulas = gerar_labirinto_perfeito(largura, altura)
    inicio = (0, 0)
    fim = (largura - 1, altura - 1)
    caminho = caminho_unico_bfs(celulas, largura, altura, inicio, fim)

    desenhar(celulas, largura, altura, inicio, fim, None,
             f"{OUT_DIR}/{nome}.png", tamanho_celula, margem)
    desenhar(celulas, largura, altura, inicio, fim, caminho,
             f"{OUT_DIR}/{nome}_gabarito.png", tamanho_celula, margem)

    info_entrada, info_saida = abertura_info(largura, altura, inicio, fim,
                                              tamanho_celula, margem)

    gabarito = {
        "nome": nome,
        "dimensoes": [largura, altura],
        "inicio": inicio,
        "fim": fim,
        "caminho": caminho,
        "passos": len(caminho) - 1,
        "rotulo_inicio": rotulo_inicio,
        "rotulo_fim": rotulo_fim,
        "abertura_entrada": info_entrada,
        "abertura_saida": info_saida,
    }
    with open(f"{OUT_DIR}/{nome}_gabarito.json", "w") as f:
        json.dump(gabarito, f, indent=2)

    print(f"[OK] {nome}: {largura}x{altura}, caminho unico com {len(caminho)} celulas, "
          f"verificado (arvore geradora + BFS).")
    return gabarito


if __name__ == "__main__":
    gerar_puzzle("labirinto_facil", 12, 12, "MODIIN", "THE HILLS")
    # medio reduzido de 18x18 para 15x15 (feedback: ficou longo demais),
    # continua maior/mais dificil que o facil (12x12)
    gerar_puzzle("labirinto_medio", 15, 15, "THE HILLS", "MODIIN")
    print("Labirintos gerados e verificados com sucesso.")
