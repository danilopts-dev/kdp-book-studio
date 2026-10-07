# 8 Nights of Hanukkah Activity Book: READY (atualizado em 2026-10-07)

Estado: **miolo pronto, sem 🔴, 82 páginas** (revisão editorial final em `reviews/editorial-final.md`). O bônus (formulário Brevo, e-mail, QR, PDF) está funcionando. **Faltam: capa (arte), revisor humano (hebraico e mini-guia) e a sua decisão sobre o "ligar os pontos" da Noite 2.**

## Arquivos
| Arquivo | Onde |
|---|---|
| Miolo (PDF, 82 págs) | `build/hanukkah-8-nights-interior.pdf` (cópia em `Entrega/` no OneDrive, via `./st publish`) |
| Bônus gratuito (PDF, 3 págs) | `build/hanukkah-8-nights-family-pack.pdf` (fonte: `bonus/family-pack.typ`; também em `Entrega/`) |
| Guia da capa (corte, lombada, área segura) | `build/hanukkah-8-nights-cover-guide.pdf` |
| Medidas da capa | `listing/cover-specs.md` |
| Listing (títulos, keywords, descrição HTML, A+) | `listing/listing.md`, `listing/aplus-prompts.md` |
| Bônus no Brevo (passo a passo e registros) | `listing/bonus-brevo.md` |
| Para o revisor humano | `reviews/revisor-humano.md` (e `Entrega/Para o revisor/` no OneDrive) |
| Relatórios editoriais | `reviews/editorial.md` (05/10) e `reviews/editorial-final.md` (07/10) |

## Especificações KDP
- Trim 8.5 x 11 in, miolo P&B em papel branco, **82 páginas** (par), sem sangria no miolo, gutter 0.65 in.
- Capa colorida fosca, lombada 0.1847 in (texto na lombada permitido, 80+ páginas, mas é fina: uma linha pequena), capa completa 17.4347 x 11.25 in com sangria.
- Inglês americano. Lançamento previsto $9.99. Hanucá 2026: 4 a 12 de dezembro.
- Listing recomendado (ASSUMIDA, você escolhe): título 1 + subtítulo 1; keyword primária "Hanukkah activity book" (as 7 keywords precisam ser validadas no Publisher Rocket/BookBeam).

## Antes de subir (gates)
1. **Capa:** gerar a arte (frente e verso) a partir do guia, com a faixa "Ages 6-10" na frente. Salvar `inputs/cover-front.png` e `cover-back.png` e rodar `./st cover hanukkah-8-nights`. Depois os 5 banners do A+ (dependem da capa).
2. **Revisor humano (judeu, que leia hebraico):** mandar o pacote `Entrega/Para o revisor/` (2 PDFs, o resumo `revisor-humano.md` e os registros). Aplicar o que ele apontar e reconstruir.
3. ~~Ligar os pontos da Noite 2~~ **Redesenhados em `_v2` (07/10)**: a menorá de 80 pontos ficou claramente uma menorá de 7 braços; a hanukkiah de 30 pontos ficou simétrica, com base e shamash alto, mas ainda um pouco "dentada" (limite dos 30 pontos). Olhe as páginas p16 e p19 e diga se aceita ou se quer subir a hanukkiah para ~40 pontos.
4. **Listing:** validar as keywords e escolher título e subtítulo.
5. **Teste final do bônus** (já testado pelo Danilo em 06/10): rever depois do upload do PDF final, se o PDF do bônus mudar.

## Decisões suas ainda abertas (todas em `questions.md`)
- Hanukkiah de 30 pontos (Noite 2): aceitar o desenho atual ou subir para ~40 pontos (muda o TOC).
- Opcional: galeria de colorir (+4 páginas, total 86; exige gerar 4 ilustrações).

## Já resolvido
- 07/10: receita de latke (adulto ralha), copyright centralizado, piadas variadas (decisão 61), série de acendimento da Noite 4 refeita com a mesma hanukkiah, ligar os pontos em `_v2`, artes 14 e 24 conferidas (ver decisões 62 a 65).
- Expansão de 64 para 82 páginas (06/10), com revisão independente das 16 atividades novas.
- Decisões religiosas pós-revisão cruzada (letras hebraicas no dreidel, "Adonai", "v'higiyanu", instrução do Match, genizá no cartão).
- Bônus: lista e formulário no Brevo, template ativo com o link do OneDrive, QR no livro (última página antes do Answer Key), PDF de 3 páginas.
- Textos aprovados corrigidos por erro de conta/lógica (N5 Gelt Math 2 e 3, N7 Split and Save 1), com as mesmas respostas.
- Paridade das páginas de recorte: molde do dreidel p43 (verso p44) e Coupon Book p61 (verso p62). Se o número de páginas de qualquer noite mudar, reconferir.
- Imprint: copyright e "Published by" em Read Publishing LLC; tipografia Atkinson Hyperlegible 13pt + Barlow.
