# Etapa: bônus (sessão principal)

Produz tudo o que o bônus gratuito precisa: o PDF, os textos do formulário e do e-mail, o e-mail no Brevo e o QR impresso no livro.
Corre em paralelo: enquanto espera o Danilo, o livro segue (montagem, revisão, listing, capa). Só a entrega (`finalize`) espera esta etapa.

Livro sem bônus (`bonus:` vazio no `book.yaml` e nada de bônus no TOC): `./st mark <slug> bonus skipped --note "sem bônus"` e pronto.

A ordem importa. No Hanukkah o e-mail foi criado com link provisório antes do PDF existir: sobrou um template inútil e quem se inscrevesse naquela janela receberia o link errado. Por isso o e-mail só é criado com o link final do PDF.

## Fase 1: PDF e textos (sem o Danilo)

1. **PDF do bônus**: chame o `activity-builder` com slug, a descrição do bônus no TOC e a lista `bonus.items` do `book.yaml`. Ele escreve `bonus/bonus.typ` (um arquivo por bônus, se houver mais de um: `bonus/<nome>.typ`), tamanho Letter, com o tema do livro, e roda `./st bonus <slug> --preview`. Os itens têm exatamente os nomes da página de bônus do livro, na mesma quantidade.
2. **Revisão**: `unit-reviewer` com slug, id `bonus` e a folha `build/sheet-bonus.png` (confere nomes dos itens contra a página do livro, erros, conteúdo sensível).
3. **Textos e e-mail**: chame o `listing-writer` no modo bônus (slug + "só bônus"). Ele grava:
   - `listing/bonus-brevo.md`: textos do formulário (título, chamada, itens, campos, botão, mensagem de sucesso, erro), o e-mail (assunto + 2 alternativas, pré-visualização, corpo) e o passo a passo do formulário para o Danilo, em português simples.
   - `listing/bonus-email.html`: o e-mail pronto, a partir de `templates/brevo/bonus-email.html`, com `{{PDF_LINK}}` ainda sem preencher.
   - Se o TOC prometer sequência de e-mails ou lembrete (ex.: plano de 4 fins de semana): um HTML por e-mail (`listing/bonus-email-2.html`...) e, no `bonus-brevo.md`, o passo a passo da automação no Brevo (gatilho: entrou na lista; esperas; qual e-mail em cada passo).
4. **QR provisório** (para o livro montar antes do formulário existir): `./st qr <slug> --placeholder`. A página do bônus usa `![](bonus-qr.png "1.6in")`.
5. `./st publish <slug> --quiet` (copia o PDF do bônus para a pasta Entrega no OneDrive).
6. Pedido 1 ao Danilo (BLOQUEANTE, em `questions.md`, texto pronto abaixo) e `./st mark <slug> bonus blocked --note "aguarda link do PDF"`.

> **Bônus do livro X: preciso do link do PDF.** O PDF do bônus está na pasta Entrega do livro no OneDrive (`<nome do arquivo>`). Clique com o botão direito > Compartilhar > "Qualquer pessoa com o link pode ver" > Copiar link, e cole aqui no chat. Com o link eu crio o e-mail no Brevo e te mando um teste.

## Fase 2: e-mail no Brevo (Claude faz)

Quando o Danilo mandar o link (passo 0 do protocolo):
1. Troque `{{PDF_LINK}}` em `listing/bonus-email.html` pelo link. Confira que nenhum `{{...}}` sobrou, exceto `{{ contact.FIRSTNAME ... }}`.
2. Crie o template no Brevo com `mcp__Brevo__templates_create_smtp_template`: `templateName` "<Título curto> - Bonus", `subject` recomendado, `sender` `{"id": 1}` (hello@readpublishingco.com; confirme com `mcp__Brevo__senders_get_senders` se falhar), `htmlContent` do arquivo, **`isActive: true`** (o formulário só lista templates ativos). Sequência de e-mails: um template por e-mail, todos ativos.
   - O conector do Brevo não edita templates. Se algo mudar depois, crie um novo e avise o Danilo para trocar no formulário e apagar o antigo.
3. Mande um teste para o e-mail do Danilo com `mcp__Brevo__templates_send_test_template`. Se falhar (contato fora de lista), siga e diga que o teste fica para o fluxo completo.
4. Registre no fim de `listing/bonus-brevo.md` (seção "Registro"): id do template, link do PDF, data.
5. Sem conector do Brevo nesta sessão: entregue o HTML e um passo a passo de 4 linhas para colar no Brevo (Templates > Novo > Colar código), e siga.
6. Pedido 2 ao Danilo (BLOQUEANTE, texto pronto abaixo).

> **Bônus do livro X: falta só o formulário (uns 5 minutos).** Já criei o e-mail no Brevo ("<nome do template>") e te mandei um teste. Agora: Brevo > Contatos > Formulários > duplique o formulário do último livro > troque os textos pelos da seção "Formulário" do arquivo `bonus-brevo.md` (pasta Entrega > listing) > em Confirmação, escolha "E-mail de confirmação simples" com o template "<nome>" > lista "<nome da lista>" (crie na pasta USA se não existir) > Salvar e publicar > copie o link da página do formulário e cole aqui.

## Fase 3: QR e fechamento (Claude faz)

1. `./st qr <slug> <url do formulário>` (QR real, 2 in a 600 DPI).
2. Se o miolo já foi montado: `./st build <slug>` e `./st check <slug> --pdf` (o aviso do QR provisório some). `./st publish <slug> --quiet`.
3. Diga ao Danilo para testar uma vez pelo celular: escanear o QR no PDF, se inscrever, receber o e-mail, baixar o PDF. Sem esse teste o livro não vai para o KDP (fica como item em "Antes de subir" no READY.md).
4. `./st mark <slug> bonus done --note "Brevo template <id>, QR real"`.
