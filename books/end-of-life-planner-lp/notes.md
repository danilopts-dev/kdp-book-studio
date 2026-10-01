# Style sheet — End of Life Planner, Large Print (Emily P. Harper)

**Voz.** Prática, calma e gentil, sem melodrama nem eufemismo pesado. Emily fala como uma vizinha organizada que já passou por isso: frases curtas, verbos concretos, uma instrução por vez. Reconhece que o assunto é pesado em no máximo uma frase e volta ao que fazer. Nada de "journey", "legacy" em tom de cartão, nem humor sobre morte. Textos de abertura de capítulo: 2 a 4 frases, nunca mais que 1/3 de página.

**Termos fixos.** "this book" (nunca "this planner" e "this organizer" alternados); "Weekend 1" a "Weekend 4" (com maiúscula, algarismo); "the four weekends"; "Extra Pages Pack" (bônus 1); "Four-Weekend Plan" (bônus 2); "Running out of room?" (aviso, sempre igual); "power of attorney", "advance directive", "living will", "trust", "safe deposit box", "Social Security", "Medicare". Rótulos de campo em Title Case curto ("Phone", "Where It's Kept", "Who Has a Copy").

**Números e datas.** Datas como "Date: ____ / ____ / ______" (MM/DD/YYYY, padrão EUA). Telefone com espaço livre, sem máscara. Nunca pedir número completo de documento, conta, cartão ou senha: campos são "Last 4 digits (optional)" ou "Where the number is written down".

**Leitor.** Tratado por "you" nos textos de instrução; os campos e títulos de capítulo ficam em primeira pessoa ("My Pets", "Where My Important Papers Are"). Sem "we".

**Nomes ilustrativos.** Nenhum por padrão. Se um exemplo for indispensável: Margaret, Harold, Linda, Robert (geração 60+).

**O que o livro NÃO faz.** Não é documento legal nem modelo de testamento, procuração ou diretiva; não dá conselho jurídico, financeiro ou médico; não pede senhas nem números completos; não faz claim de resultado ("your family will never fight"). Diz onde as coisas estão e o que a pessoa deseja.

**Layout.** 8.5x11, 16 pt, linhas de escrita 0,4", mesmo layout para o mesmo tipo de página do começo ao fim. Cada capítulo abre com o marcador "Weekend N of 4" + título + intro curta. Máximo 2 elementos recorrentes por capítulo.

---
# Continuidade (resumos por unidade)

<!-- Cada unidade concluída adiciona 3-5 linhas: o que cobriu, histórias/dados usados, ganchos para as próximas.
     Os agentes leem ISTO em vez de reler os capítulos anteriores (economia de tokens). -->

**ch01 (Weekend 1, 2 págs).** Página 1: About Me (nome, endereço, telefone/e-mail, nascimento) + tabela "Call These People First" (4 linhas). Página 2: Where This Book Is Kept / Who Has a Copy, Where My Main Documents Are, Allergies, Medications I Must Not Miss (tabela 5 linhas). Sem números de documento/conta; sem nomes de exemplo.
Blocos em lib.typ (reusar nos ch02–16): `chapter-opener(weekend, title, intro)`; `elp-heading(title)`; `elp-field(label, lines: 1, hint: none)` (1 = rótulo+linha inline; >1 = rótulo acima + N linhas de 0,4"); `elp-field-row(..labels)`; `elp-gap`; `elp-table(headers, rows: 5, widths: none, first-numbered: false, row-h: 0.4in)`; `room-notice()` (texto da página do bônus, sem QR/URL; trocar só o bloco depois). Rótulos 14 pt, corpo 16 pt.
Correção de engine: `checks.py` não tenta mais parsear unidades `kind: typst` como YAML.
