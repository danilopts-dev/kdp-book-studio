# Bônus no Brevo — Printable Declutter Kit

Textos para a página de captura (formulário) e para o e-mail de entrega. Voz: Emily P. Harper.
Alinhado com `content/_bonus.md` (mesmos 3 itens do kit, mesmos nomes).

---

## 1. Página do formulário (landing page)

**Título da página (aba do navegador):**
Printable Declutter Kit | Emily P. Harper

**Headline:**
Your Printable Declutter Kit

**Subheadline:**
The pages from *The 12-Week Decluttering Workbook* that work better on a wall, ready to print as many times as you need.

**Texto de apoio:**
You bought the workbook, so this part is on me. Leave your email below and I'll send you the PDF right away. Print it at home on regular letter-size paper.

**O que vem no kit:**
- **Keep / Donate / Sell / Toss flowchart.** The tie-breaker from Week 0 on one page, for the inside of a closet door.
- **Room checklists.** A clean copy for each monthly 15-minute reset, so you never write over last month's marks.
- **12-week fridge tracker.** Check off each week as you finish it, where the whole house can see it.

**Campos do formulário:**
- First name (opcional) — placeholder: `Your first name`
- Email (obrigatório) — placeholder: `you@example.com`

**Checkbox de consentimento (obrigatório, desmarcado por padrão):**
☐ Yes, send me the Printable Declutter Kit and occasional emails from Emily P. Harper with decluttering tips and new books. I can unsubscribe at any time.

**Texto do botão:**
Send Me the Kit

**Nota abaixo do botão (privacidade):**
No spam. You'll get the kit, a few useful emails, and an unsubscribe link in every one of them.
[link: Privacy Policy]

**Mensagem de sucesso (depois do envio):**
Check your inbox. The kit is on its way to the address you entered. If it isn't there in a few minutes, look in your spam or promotions folder and move it to your main inbox so the next emails find you.

**Mensagem de sucesso, se usar double opt-in:**
Almost there. I just sent you a short email with a button to confirm your address. Click it and the kit arrives right after.

**Mensagem de erro (e-mail inválido):**
That email address doesn't look quite right. Could you check it and try again?

---

## 2. E-mail de confirmação (só se usar double opt-in)

**Subject:** Please confirm your email to get the kit
**Preview text:** One click and your Printable Declutter Kit is on its way.

**Corpo:**
Hi {{contact.FIRSTNAME | default: "there"}},

Thanks for asking for the Printable Declutter Kit. Before I send it, please confirm this is the right address:

[Botão: Confirm My Email]

If you didn't sign up, you can ignore this message and you won't hear from me again.

Emily

---

## 3. E-mail de entrega do bônus

**Subject (recomendado):** Your Printable Declutter Kit is here
**Subject (alternativas):**
- Your declutter kit (print it before Week 1)
- The pages to tape inside your closet door

**Preview text:** Flowchart, room checklists and the 12-week fridge tracker, ready to print.

**Remetente:** Emily P. Harper

**Corpo:**

Hi {{contact.FIRSTNAME | default: "there"}},

Here's your Printable Declutter Kit:

[Botão: Download the Kit (PDF)]

Before you start Week 1, print one copy of the flowchart and tape it somewhere you'll see it with full hands, like the inside of a closet door or the side of the fridge. Most of the time you won't need it. It's there for the sweater you've been holding for five minutes without deciding.

Put the fridge tracker up on day one. Checking off a whole week where everyone in the house can see it tends to keep you going on the days you would rather skip.

Keep the room checklists in a folder. You'll want a fresh copy for each monthly 15-minute reset in Keep It Clear, once the 12 weeks are done.

One small thing: if you haven't done Week 0 yet, start there, with a pencil. You don't have to touch anything on the first walk through.

Talk soon,
Emily

P.S. If the link stops working or the file won't open, just reply to this email and I'll send it again.

---

## Notas para configurar no Brevo

- O PDF do kit ainda não existe. Ele precisa ser criado antes de o fluxo ir ao ar (flowchart, checklists por cômodo, tracker de 12 semanas), no mesmo visual do miolo.
- Rodapé do e-mail: o Brevo inclui o link de descadastro, mas o endereço físico do remetente (exigência do CAN-SPAM nos EUA) precisa estar preenchido nas configurações da conta.
- Política de privacidade: o link abaixo do botão precisa apontar para uma página real (pode ser no readpublishingco.com).
- O e-mail de boas-vindas fala em "a few useful emails". Se não houver sequência planejada, troque por "an occasional email when there's a new book".
- Depois de publicar a página, mande o link final para trocar o placeholder em `content/_bonus.md` e gerar o QR code.
