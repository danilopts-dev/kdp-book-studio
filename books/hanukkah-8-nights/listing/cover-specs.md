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

## Capa aprovada (09/10/2026)
- Arte gerada por IA (1086 x 1448 px cada, frente e verso), ampliada para 300 DPI (painéis de 2588 x 3375 px) com nitidez leve; as bordas que faltam para a sangria foram preenchidas por extensão suavizada. Resolução real da arte original: ~133 DPI no tamanho impresso, então a capa sai um pouco macia; se quiser mais nitidez, gerar de novo em tamanho maior ou usar um ampliador por IA e trocar `inputs/cover-front.png` / `cover-back.png` / `cover-spine.png`.
- Lombada 0.1847 in sem texto (degradê feito das bordas da arte). Verso sem espaço reservado para o código de barras (a Amazon coloca o dele; o canto inferior direito é escuro e simples).
- Montagem: `./st cover hanukkah-8-nights` (usa `book.yaml: cover: {spine_text: false}`).
