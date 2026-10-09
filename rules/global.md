# Regras globais (todos os livros)

## Leitor em primeiro lugar
O padrão não é "segue o TOC ao pé da letra", é "entrega a melhor experiência para este leitor, dentro do que o TOC promete". Título e subtítulo têm de corresponder ao que o livro entrega.

## Fatos
- Nunca inventar estatística, estudo, citação, fonte, depoimento ou avaliação. Fato sem fonte verificável sai do texto ou vira pergunta.
- Trivia e referências de época: toda afirmação com `source`. Na dúvida, troque a pergunta.
- Datas de calendário só por biblioteca (`holidays`, `pyluach`); nunca de memória.

## Claims
- Sem claim médico: não dizer que o livro trata, previne ou ajuda com demência, Alzheimer, ansiedade clínica ou qualquer doença. Permitido: "keeps the mind active", "brain-engaging", "mind-stimulating".
- Sem promessas de resultado garantido (financeiro, saúde, relacionamento).

## Texto
- Inglês americano nativo (ou o idioma do `book.yaml`), com grafia do mercado (color/colour conforme o mercado).
- `rules/skills/human-voice-writing.md` vale para toda prosa: capítulos, introduções, how-to-use, descrições.
- Personagens ilustrativos: sem nomes-padrão de IA; nomes comuns e datados para a geração do público.
- Nenhum placeholder no arquivo final (`[DANILO: ...]`, TODO, TBD). O script bloqueia.

## KDP (técnico; o engine já aplica, mas não desfaça)
- Mínimo 24 páginas; margem interna conforme o nº de páginas; margem externa ≥ 0,25" (0,375" com sangria).
- Fontes embutidas (o Typst embute sempre); corpo ≥ 7pt; large print ≥ 16pt.
- Imagens ≥ 300 DPI no tamanho impresso. Com imagem até a borda: `bleed: true`.
- Texto na lombada só com 80+ páginas.

## Imagens do Danilo
Ficam em `books/<slug>/inputs/`. Nome descritivo (`cover-front.png`, `p07-garden.png`). Se uma imagem for necessária e não existir, é BLOQUEANTE, com a especificação exata (conteúdo, proporção, pixels mínimos).

- **Margens do KDP (miolo):** nenhum objeto, inclusive número de página e rodapé, a menos de 0.25 in da borda de cima, de baixo e externa; gutter de pelo menos 0.375 in até 150 páginas. O Visualizador do KDP bloqueia com "This object is outside the margins". `./st check --pdf` mede isso (`check_margins`).
