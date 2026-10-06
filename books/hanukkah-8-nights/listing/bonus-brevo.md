# Bônus no Brevo: 8 Nights Family Pack (criado em 2026-10-06)

Segue o padrão dos outros livros (formulário de captura + e-mail "Simple confirmation" com o template do bônus). Voz: Jonah Feldman / Read Publishing Co.

## O que existe no Brevo
| Item | Nome | Observação |
|---|---|---|
| Lista | Hanukkah 8 Nights | pasta USA, onde ficam as listas dos outros livros |
| Formulário | Hanukkah 8 Nights | duplicado do "Jewish Calendar" (mesmo design e captcha). Título "Get Your Free 8 Nights Family Pack". Confirmação: Simple confirmation email com o template abaixo |
| Template ATIVO (usado pelo formulário) | Hanukkah 8 Nights - Bonus (ATIVO, trocar o link) | id 22; remetente Read Publishing Co <hello@readpublishingco.com>; assinatura "Jonah Feldman / Read Publishing Co" |
| Template inativo (sobra) | Hanukkah 8 Nights - Bonus | id 21; criado antes de descobrir que o formulário só lista templates ativos; pode apagar |
| QR code | `inputs/bonus-qr.png` (cópia em `listing/bonus-qr.png`) | aponta para a página hospedada do formulário; baixado do Brevo (320 px) e redesenhado na mesma grade de 61 módulos em 2760 px, idêntico ao original |

Texto do e-mail: "Thank you for requesting your free bonus! Your 8 Nights Family Pack is ready. It has a printable blessing card with the Hebrew, the transliteration and the English, the dreidel rules with a score sheet you can use all eight nights, and eight gift tags, one for each night of Hanukkah." + botão "[Download Your Family Pack]" + "Print it on regular letter-size paper. If the link stops working or the file won't open, just reply to this email and we'll send it again." + "Happy Hanukkah, Jonah Feldman, Read Publishing Co". Assunto: "Your Free 8 Nights Family Pack Is Here 🕯️".

## Falta (nesta ordem, antes de o livro ir para o KDP)
1. **PDF do Family Pack: PRONTO** (2026-10-06): `build/hanukkah-8-nights-family-pack.pdf`, 3 páginas Letter (cartão de bênçãos com hebraico e nikud, regras do dreidel + placar das 8 noites, 8 etiquetas de presente). Fonte do arquivo: `bonus/family-pack.typ`; gerar de novo com `.venv/Scripts/python.exe books/hanukkah-8-nights/bonus/build.py`. Falta só pegar o link de compartilhamento do OneDrive: abra `Amazon KDP/13 - .../Entrega/hanukkah-8-nights-family-pack.pdf` (o `./st publish` já copiou), clique com o botão direito > Compartilhar > Copiar link (qualquer pessoa com o link pode ver).
2. **Trocar o link do e-mail:** no Brevo, editar o template id 22 e trocar o link provisório (`https://www.readpublishingco.com`) pelo link do OneDrive do PDF. O MCP do Brevo não edita templates, então é na interface (Templates > Hanukkah 8 Nights - Bonus (ATIVO...) > Editar). Pode renomear tirando "(ATIVO, trocar o link)".
3. **Testar o fluxo de ponta a ponta:** abrir o formulário pelo QR com um e-mail seu, conferir se chega o e-mail e se o link baixa o PDF. Sem esse teste não suba o livro.
4. Opcional: apagar o template id 21 (inativo).

Atenção: a página do formulário já está acessível pelo link/QR. Quem se inscrever antes do passo 2 recebe o e-mail com o link provisório (a home do site), não o PDF.
