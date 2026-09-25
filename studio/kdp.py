"""Especificações técnicas do KDP (paperback). Fonte: KDP Help Center — Print Options / Cover Calculator.

Tudo em polegadas. Conferir de tempos em tempos se a Amazon mudou alguma regra.
"""

BLEED = 0.125  # por lado (topo, base e borda externa); a borda interna não tem sangria

TRIM_SIZES = {
    "5x8": (5.0, 8.0),
    "5.5x8.5": (5.5, 8.5),
    "6x9": (6.0, 9.0),
    "7x10": (7.0, 10.0),
    "8x10": (8.0, 10.0),
    "8.25x11": (8.25, 11.0),
    "8.5x8.5": (8.5, 8.5),
    "8.5x11": (8.5, 11.0),
}

# Espessura por página (spine) por tipo de papel/impressão
PAPER_THICKNESS = {
    "bw-white": 0.002252,
    "bw-cream": 0.0025,
    "color-standard": 0.002252,
    "color-premium": 0.002347,
}

MIN_PAGES = 24
MAX_PAGES = 828  # varia por trim/papel; 828 é o teto para B&W na maioria dos tamanhos
SPINE_TEXT_MIN_PAGES = 80  # KDP: texto na lombada só com mais de 79 páginas
MIN_OUTSIDE_MARGIN_NO_BLEED = 0.25
MIN_OUTSIDE_MARGIN_BLEED = 0.375
MIN_FONT_PT = 7
MIN_IMAGE_DPI = 300


def gutter_for_pages(pages: int) -> float:
    """Margem interna mínima exigida pelo KDP conforme o número de páginas."""
    if pages <= 150:
        return 0.375
    if pages <= 300:
        return 0.5
    if pages <= 500:
        return 0.625
    if pages <= 700:
        return 0.75
    return 0.875


def trim(size: str) -> tuple[float, float]:
    if size not in TRIM_SIZES:
        raise ValueError(f"Trim '{size}' não suportado. Opções: {', '.join(TRIM_SIZES)}")
    return TRIM_SIZES[size]


def page_size(size: str, bleed: bool) -> tuple[float, float]:
    w, h = trim(size)
    return (w + BLEED, h + 2 * BLEED) if bleed else (w, h)


def spine_width(pages: int, paper: str) -> float:
    return pages * PAPER_THICKNESS[paper]


def cover_size(size: str, pages: int, paper: str) -> dict:
    """Dimensões da capa completa (contracapa + lombada + frente), com sangria."""
    w, h = trim(size)
    spine = spine_width(pages, paper)
    return {
        "width": BLEED + w + spine + w + BLEED,
        "height": BLEED + h + BLEED,
        "spine": spine,
        "trim_w": w,
        "trim_h": h,
        "spine_text_allowed": pages >= SPINE_TEXT_MIN_PAGES,
    }
