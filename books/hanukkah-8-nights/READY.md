# 8 Nights of Hanukkah Activity Book — READY (2026-10-05)

Estado: **miolo pronto e sem 🔴**; faltam capa (arte), bônus (PDF + QR) e a revisão religiosa humana antes do upload.

## Arquivos
| Arquivo | Onde |
|---|---|
| Miolo (PDF, 64 págs) | `build/hanukkah-8-nights-interior.pdf` (cópia em `Entrega/` no OneDrive, via `./st publish`) |
| Guia da capa (corte, lombada, área segura) | `build/hanukkah-8-nights-cover-guide.pdf` |
| Medidas da capa | `listing/cover-specs.md` |
| Listing (títulos, keywords, descrição HTML, A+) | `listing/listing.md` |
| Prompts do Google Flow para o A+ | `listing/aplus-prompts.md` |
| Relatório editorial | `reviews/editorial.md` |

## Especificações KDP
- Trim 8.5 x 11 in, miolo P&B em papel branco, 64 páginas, sem sangria no miolo, gutter 0.65 in.
- Capa colorida fosca, lombada 0.1441 in (sem texto na lombada: menos de 80 páginas), capa completa 17.3941 x 11.25 in com sangria.
- Inglês americano. Lançamento previsto $9.99. Hanucá 2026: 4 a 12 de dezembro.
- Listing recomendado (ASSUMIDA, você escolhe): título 1 + subtítulo 1; keyword primária "Hanukkah activity book" (validar no Publisher Rocket/BookBeam).

## Antes de subir (gates)
1. **Capa:** gerar a arte (frente e verso) a partir do guia; faixa "Ages 6-10" na frente. `inputs/cover-front.png`, `cover-back.png`, depois `./st cover hanukkah-8-nights`.
2. **Bônus Family Pack:** produzir o PDF (cartão de bênçãos com `legacy/manuscript/bonus-cartao-bencaos.md`, regras do dreidel + placar, 8 etiquetas), gerar `inputs/bonus-qr.png` com a URL real e trocar `has-bonus-qr` para `true` em `theme.typ`. Hoje a página 58 imprime uma caixa "QR CODE" temporária e a página 4 diz "Scan the code at the end of this book".
3. **Revisor religioso humano:** mini-guia de acendimento, 3 bênçãos da Noite 1, Shehecheyanu, quadro menorá x hanukkiah, letra Pei, cartão com nikud (`legacy/docs/revisao-religiosa.md`, `legacy/docs/hebraico-para-revisao.md`).
4. **Ligar os pontos da Noite 2** (hanukkiah 30 e menorá 80): ao ligar, não formam a figura prometida. Recomendação: autorizar redesenho em arquivos `_v2`. É o ponto mais fraco do miolo.

## Decisões suas (todas as ASSUMIDAS estão em `questions.md`)
- **Páginas:** o miolo tem 64 (o TOC previa 96-104). Aceitar, ou acrescentar atividades?
- **Artes 42b/42c/42d (Noite 4):** mostram 8, 3 e 8 velas; a atividade seguinte conta 4 + shamash. Regerar com 4?
- **Piadas:** 5 das 7 seguem "Why did X...? Because..."; sugestão de trocar a N8-A e variar a N4.
- **Copyright:** a linha "puzzle pages in the Answer Key" soa estranha; sugestão: "The activities in this book are intended for personal, non-commercial use."
- **Texto aprovado alterado por erro de conta/lógica** (conferir): N5 Gelt Math 2 ("3 cousins") e 3 (Hei dá metade ao primo), N7 Split and Save 1 (três pilhas). Respostas iguais.
- **Imprint:** copyright e "Published by" em Read Publishing LLC (padrão do livro de Declutter); `imprint_name` vazio.
- **Tipografia:** Atkinson Hyperlegible 13pt + Barlow (a Andika não está em `fonts/`).
- Ilustração 1.4 (`14.png`) e 2.4 (menorá de 7 braços) assumidas como aprovadas; página 1 do how-to-use com ~40% de branco.
- Paridade das páginas de recorte (N5 dreidel em p33, N7 Coupon Book em p47): se o número de páginas de qualquer noite mudar, reconferir.
