# Especificações da capa (calculadas por `./st cover hanukkah-8-nights`, 2026-10-05)

| Item | Valor |
|---|---|
| Trim | 8.5 x 11 in |
| Páginas do miolo | 82 (recalcular se mudar) |
| Papel | P&B, branco |
| Acabamento da capa | colorida, fosca (conforme TOC) |
| Lombada | 0.1847 in |
| Capa completa (com sangria 0.125 in) | 17.4347 x 11.25 in |
| Texto na lombada | permitido (80+ páginas), mas a lombada é fina (0.1847 in): texto pequeno, uma linha (título), sem imprint |
| Guia para Canva/Flow | `build/hanukkah-8-nights-cover-guide.pdf` (corte, lombada, área segura) |

Pendente: arte da capa (frente e verso) em `inputs/cover-front.png` e `inputs/cover-back.png` (mínimo 300 DPI no tamanho impresso). Faixa "Ages 6-10" na frente (o subtítulo recomendado no listing depende disso). Se o miolo ganhar páginas, rodar `./st cover hanukkah-8-nights` de novo: a largura da lombada muda.

## Capa final (09/10/2026): arquivo do Danilo, feito no Canva
- **ATUALIZAÇÃO (09/10/2026): versão final = "Cover v2" com a arte ampliada** (frente e verso em JPEG de 3092 x 3988 px, ~355 DPI no tamanho impresso; mesmo layout, 17.4375 x 11.25 in, 13 MB). A resolução baixa descrita abaixo vale só para a v1.
- **Arquivo final:** `inputs/cover-final.pdf` (cópia em `build/hanukkah-8-nights-cover.pdf` e em `Entrega/`). PDF de página única, 17.4375 x 11.25 in (o gabarito do estúdio é 17.4347; diferença de 0.0028 in), frente e verso como duas imagens JPEG de 1104 x 1424 px (~128 DPI no tamanho impresso), sem fontes (texto na própria arte), lombada sem texto.
- Arte gerada por IA: conceito 1 (hanukkiah acesa, azul-meia-noite e dourado), contracapa no mesmo fundo, sem espaço reservado para o código de barras (a Amazon coloca o dele no canto inferior direito, que é uma área escura e simples).
- Texto a 0.32 in ou mais do corte (frente) e 0.57 in (verso). Resolução baixa para impressão (recomendado 300 DPI): sai levemente macia; se quiser mais nitidez, ampliar as duas imagens e refazer o PDF no Canva.
- A montagem automática do estúdio (que usava `cover-front/back/spine.png`, agora em `inputs/cover-source/estudio/`) ficou como alternativa; o PDF dela está em `build/hanukkah-8-nights-cover-estudio-superado.pdf`.
