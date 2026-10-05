"""
gerar_sudoku_simbolos.py
Gera os dois sudokus com simbolos da Noite 3:
  - 4x4 (2x2 caixas): jarro, vela, dreidel, estrela (nivel una-estrela)
  - 6x6 (2x3 caixas): os 4 anteriores + hanukia, moeda/gelt (nivel duas-estrelas)

Metodo:
  1. Gera uma grade solucao completa valida por backtracking com
     embaralhamento (garante variedade a cada seed).
  2. Remove celulas uma a uma (ordem embaralhada); so aceita a remocao
     se a grade resultante ainda tiver solucao UNICA, verificada por um
     solver que conta solucoes por backtracking e para assim que
     encontra a segunda (retorna 0, 1 ou 2+).
  3. Desenha puzzle (com celulas vazias) e gabarito (grade completa)
     como PNG, cada simbolo desenhado por forma geometrica simples e
     distinta (sem arte fina).
  4. Verificacao final antes de salvar: confirma que (a) a grade solucao
     e valida (linhas/colunas/caixas sem repeticao), (b) o puzzle salvo
     tem exatamente o numero de pistas esperado, (c) resolver o puzzle
     salvo bate exatamente com o gabarito salvo, (d) solucao e unica.

Uso: python3 gerar_sudoku_simbolos.py
Saida: /mnt/user-data/outputs/puzzle-assets/noite3_sudoku4x4.png
       /mnt/user-data/outputs/puzzle-assets/noite3_sudoku4x4_gabarito.png
       /mnt/user-data/outputs/puzzle-assets/noite3_sudoku4x4_gabarito.json
       (e as versoes 6x6)
"""
import json
import random

from PIL import Image, ImageDraw

random.seed(13)

OUT_DIR = "/mnt/user-data/outputs/puzzle-assets"

# Simbolos, na ordem 1..N. 4x4 usa os 4 primeiros; 6x6 usa todos os 6.
SIMBOLOS = ["jar", "candle", "dreidel", "star", "hanukkiah", "coin"]


# ---------------------------------------------------------------------------
# Geracao de grade solucao completa (backtracking com embaralhamento)
# ---------------------------------------------------------------------------

def caixas_dims(n):
    """Retorna (altura_caixa, largura_caixa) para o tamanho de grade n."""
    if n == 4:
        return 2, 2
    if n == 6:
        return 2, 3
    raise ValueError("tamanho nao suportado")


def valido(grade, n, br, bc, linha, col, valor):
    for c in range(n):
        if grade[linha][c] == valor:
            return False
    for r in range(n):
        if grade[r][col] == valor:
            return False
    r0 = (linha // br) * br
    c0 = (col // bc) * bc
    for r in range(r0, r0 + br):
        for c in range(c0, c0 + bc):
            if grade[r][c] == valor:
                return False
    return True


def gerar_solucao_completa(n):
    br, bc = caixas_dims(n)
    grade = [[0] * n for _ in range(n)]

    def preencher(pos=0):
        if pos == n * n:
            return True
        r, c = divmod(pos, n)
        valores = list(range(1, n + 1))
        random.shuffle(valores)
        for v in valores:
            if valido(grade, n, br, bc, r, c, v):
                grade[r][c] = v
                if preencher(pos + 1):
                    return True
                grade[r][c] = 0
        return False

    ok = preencher()
    assert ok, "falha ao gerar grade solucao"
    return grade


# ---------------------------------------------------------------------------
# Contador de solucoes (para checar unicidade ao remover celulas)
# ---------------------------------------------------------------------------

def contar_solucoes(grade_puzzle, n, limite=2):
    br, bc = caixas_dims(n)
    grade = [linha[:] for linha in grade_puzzle]
    vazios = [(r, c) for r in range(n) for c in range(n) if grade[r][c] == 0]
    contagem = [0]

    def resolver(idx=0):
        if contagem[0] >= limite:
            return
        if idx == len(vazios):
            contagem[0] += 1
            return
        r, c = vazios[idx]
        for v in range(1, n + 1):
            if contagem[0] >= limite:
                return
            if valido(grade, n, br, bc, r, c, v):
                grade[r][c] = v
                resolver(idx + 1)
                grade[r][c] = 0

    resolver()
    return contagem[0]


def resolver_unico(grade_puzzle, n):
    """Resolve um puzzle que ja se sabe ter solucao unica e devolve a grade
    completa (usado so na verificacao final, nao na geracao)."""
    br, bc = caixas_dims(n)
    grade = [linha[:] for linha in grade_puzzle]
    vazios = [(r, c) for r in range(n) for c in range(n) if grade[r][c] == 0]

    def resolver(idx=0):
        if idx == len(vazios):
            return True
        r, c = vazios[idx]
        for v in range(1, n + 1):
            if valido(grade, n, br, bc, r, c, v):
                grade[r][c] = v
                if resolver(idx + 1):
                    return True
                grade[r][c] = 0
        return False

    resolver()
    return grade


# ---------------------------------------------------------------------------
# Remocao de celulas mantendo solucao unica
# ---------------------------------------------------------------------------

def gerar_puzzle(n, min_pistas):
    solucao = gerar_solucao_completa(n)
    puzzle = [linha[:] for linha in solucao]
    posicoes = [(r, c) for r in range(n) for c in range(n)]
    random.shuffle(posicoes)
    pistas = n * n
    for (r, c) in posicoes:
        if pistas <= min_pistas:
            break
        valor_salvo = puzzle[r][c]
        puzzle[r][c] = 0
        if contar_solucoes(puzzle, n, limite=2) == 1:
            pistas -= 1
        else:
            puzzle[r][c] = valor_salvo
    return solucao, puzzle, pistas


# ---------------------------------------------------------------------------
# Desenho dos simbolos (formas geometricas simples e distintas)
# ---------------------------------------------------------------------------

def desenhar_simbolo(draw, nome, cx, cy, tam):
    """Desenha um simbolo centrado em (cx, cy), dentro de uma caixa
    aproximada de lado 'tam'. Preto sobre branco, so linhas e formas
    simples (nao e arte fina, e reconhecivel e distinto)."""
    s = tam / 2
    cor = (20, 20, 20)
    lw = max(2, int(tam * 0.05))

    if nome == "jar":
        # jarro: corpo oval + gargalo + tampa
        corpo_w, corpo_h = s * 1.1, s * 1.0
        draw.ellipse([cx - corpo_w / 2, cy - corpo_h / 2 + s * 0.25,
                      cx + corpo_w / 2, cy + corpo_h / 2 + s * 0.25],
                     outline=cor, width=lw)
        draw.rectangle([cx - s * 0.22, cy - s * 0.85, cx + s * 0.22, cy - s * 0.25],
                        outline=cor, width=lw)
        draw.rectangle([cx - s * 0.34, cy - s * 1.0, cx + s * 0.34, cy - s * 0.82],
                        outline=cor, width=lw)

    elif nome == "candle":
        # vela: corpo retangular + chama (triangulo/oval)
        draw.rectangle([cx - s * 0.22, cy - s * 0.3, cx + s * 0.22, cy + s * 0.95],
                        outline=cor, width=lw)
        draw.line([cx, cy - s * 0.3, cx, cy - s * 0.55], fill=cor, width=lw)
        draw.ellipse([cx - s * 0.2, cy - s * 1.0, cx + s * 0.2, cy - s * 0.5],
                      outline=cor, width=lw)

    elif nome == "dreidel":
        # dreidel: corpo trapezoidal + ponta + haste no topo
        topo_w, base_w, alt = s * 0.9, s * 0.35, s * 1.3
        y_topo = cy - alt / 2 + s * 0.15
        y_base = cy + alt / 2 + s * 0.15
        draw.polygon([
            (cx - topo_w / 2, y_topo), (cx + topo_w / 2, y_topo),
            (cx + base_w / 2, y_base), (cx - base_w / 2, y_base),
        ], outline=cor, width=lw)
        draw.line([cx, y_base, cx, y_base + s * 0.25], fill=cor, width=lw)
        draw.line([cx, y_topo, cx, y_topo - s * 0.3], fill=cor, width=lw)
        draw.line([cx - s * 0.18, y_topo - s * 0.3, cx + s * 0.18, y_topo - s * 0.3],
                   fill=cor, width=lw)

    elif nome == "star":
        # estrela de 6 pontas (Estrela de David), duas triangulos sobrepostos
        r = s * 0.8
        import math
        pts_up, pts_down = [], []
        for i in range(3):
            ang = -math.pi / 2 + i * (2 * math.pi / 3)
            pts_up.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        for i in range(3):
            ang = math.pi / 2 + i * (2 * math.pi / 3)
            pts_down.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        draw.polygon(pts_up, outline=cor, width=lw)
        draw.polygon(pts_down, outline=cor, width=lw)

    elif nome == "hanukkiah":
        # hanukia: base + 9 hastes curtas (estilizado, so a silhueta)
        base_w = s * 1.5
        draw.line([cx - base_w / 2, cy + s * 0.7, cx + base_w / 2, cy + s * 0.7],
                   fill=cor, width=lw)
        n_hastes = 9
        for i in range(n_hastes):
            hx = cx - base_w / 2 + base_w * i / (n_hastes - 1)
            alt = s * 0.55 if i == n_hastes // 2 else s * 0.4
            draw.line([hx, cy + s * 0.7, hx, cy + s * 0.7 - alt], fill=cor, width=max(2, lw - 1))
            draw.ellipse([hx - 2, cy + s * 0.7 - alt - 4, hx + 2, cy + s * 0.7 - alt + 4],
                         outline=cor, width=1)

    elif nome == "coin":
        # moeda / gelt: circulo duplo com uma marca simples no meio
        draw.ellipse([cx - s * 0.8, cy - s * 0.8, cx + s * 0.8, cy + s * 0.8],
                     outline=cor, width=lw)
        draw.ellipse([cx - s * 0.55, cy - s * 0.55, cx + s * 0.55, cy + s * 0.55],
                     outline=cor, width=max(1, lw - 1))
        draw.line([cx - s * 0.25, cy, cx + s * 0.25, cy], fill=cor, width=lw)

    else:
        raise ValueError(f"simbolo desconhecido: {nome}")


# ---------------------------------------------------------------------------
# Renderizacao da grade (puzzle ou gabarito) em PNG
# ---------------------------------------------------------------------------

def desenhar_grade(grade, n, caminho, celula_px=90, mostrar_todos=True, mascara=None):
    br, bc = caixas_dims(n)
    margem = 20
    lado = celula_px * n
    img = Image.new("RGB", (lado + margem * 2, lado + margem * 2), "white")
    draw = ImageDraw.Draw(img)

    for r in range(n + 1):
        largura = 4 if r % br == 0 else 1
        y = margem + r * celula_px
        draw.line([(margem, y), (margem + lado, y)], fill=(0, 0, 0), width=largura)
    for c in range(n + 1):
        largura = 4 if c % bc == 0 else 1
        x = margem + c * celula_px
        draw.line([(x, margem), (x, margem + lado)], fill=(0, 0, 0), width=largura)

    for r in range(n):
        for c in range(n):
            valor = grade[r][c]
            if valor == 0:
                continue
            if not mostrar_todos and mascara is not None and mascara[r][c] == 0:
                continue
            cx = margem + c * celula_px + celula_px / 2
            cy = margem + r * celula_px + celula_px / 2
            desenhar_simbolo(draw, SIMBOLOS[valor - 1], cx, cy, celula_px * 0.72)

    img.save(caminho)


# ---------------------------------------------------------------------------
# Verificacao final (nao confia so na geracao, reconfere tudo)
# ---------------------------------------------------------------------------

def verificar_grade_valida(grade, n):
    br, bc = caixas_dims(n)
    for r in range(n):
        if sorted(grade[r]) != list(range(1, n + 1)):
            return False
    for c in range(n):
        col = [grade[r][c] for r in range(n)]
        if sorted(col) != list(range(1, n + 1)):
            return False
    for r0 in range(0, n, br):
        for c0 in range(0, n, bc):
            vals = [grade[r][c] for r in range(r0, r0 + br) for c in range(c0, c0 + bc)]
            if sorted(vals) != list(range(1, n + 1)):
                return False
    return True


def processar(n, min_pistas, nome_base):
    solucao, puzzle, pistas = gerar_puzzle(n, min_pistas)

    assert verificar_grade_valida(solucao, n), f"{nome_base}: solucao invalida"
    assert contar_solucoes(puzzle, n, limite=2) == 1, f"{nome_base}: puzzle nao tem solucao unica"
    resolvido = resolver_unico([linha[:] for linha in puzzle], n)
    assert resolvido == solucao, f"{nome_base}: solver nao reproduz o gabarito"

    mascara = [[1 if puzzle[r][c] != 0 else 0 for c in range(n)] for r in range(n)]

    caminho_puzzle = f"{OUT_DIR}/{nome_base}.png"
    caminho_gabarito_png = f"{OUT_DIR}/{nome_base}_gabarito.png"
    caminho_gabarito_json = f"{OUT_DIR}/{nome_base}_gabarito.json"

    desenhar_grade(puzzle, n, caminho_puzzle, mostrar_todos=True)
    desenhar_grade(solucao, n, caminho_gabarito_png, mostrar_todos=True)

    with open(caminho_gabarito_json, "w") as f:
        json.dump({
            "tamanho": n,
            "simbolos_em_ordem_1_a_n": SIMBOLOS[:n],
            "puzzle": puzzle,
            "solucao": solucao,
            "numero_de_pistas": pistas,
        }, f, indent=2)

    print(f"[OK] {nome_base}: grade {n}x{n}, {pistas} pistas dadas, "
          f"solucao unica confirmada.")


def main():
    # 4x4: nivel una-estrela, 4 simbolos, pistas generosas (mais faceis).
    processar(4, min_pistas=6, nome_base="noite3_sudoku4x4")
    # 6x6: nivel duas-estrelas, 6 simbolos, menos pistas (mais dificil).
    processar(6, min_pistas=14, nome_base="noite3_sudoku6x6")


if __name__ == "__main__":
    main()
