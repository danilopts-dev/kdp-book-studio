# Etapa: build (sessão principal, só scripts)

1. `./st build <slug>` — gera `build/<slug>-interior.pdf` (2 passadas: a margem interna se ajusta ao nº de páginas).
2. `./st check <slug> --pdf` — páginas mínimas/máximas, tamanho de página, fontes embutidas, fonte preferida usada, corpo mínimo, DPI das imagens.
3. Trate os achados que são de engenharia (fonte faltando em `fonts/`, trim errado, páginas < 24) aqui mesmo. Páginas < 24 ou muito acima do planejado: BLOQUEANTE com proposta (ex.: +N puzzles, páginas de notas).
4. Sem 🔴: `./st publish <slug> --quiet` (copia o PDF para `Entrega/` no OneDrive) e `done` com nota "<n> páginas".
