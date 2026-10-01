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

**ch02 (Weekend 1, 8 págs, PDF págs. 7-14).** P1-2 Family (tabela com ordem numerada 1-15, coluna "In Person?"), P3 Close Friends (16-24), P4 My Doctors/pharmacy/hospital, P5 Attorney/Accountant/Advisors (campos Phone, sem nº de conta), P6 Neighbor/Employer/Community, P7 Tell Them in Person / Phone / Message, P8 room-notice (sozinho). Sem nomes de exemplo.
lib.typ: `elp-table` ganhou `start:` (numeração contínua entre páginas; padrão 1, retrocompatível).

**ch03 (Weekend 1, 6 págs, PDF págs. 15-20).** Só ONDE ficam os papéis (local, quem tem cópia, data), sem conteúdo/números. P1 Wills and Legal Papers (will, trust, POAs, advance directive, living will), P2 Personal Records, P3 Home and Vehicles, P4 Insurance, Money, and Taxes, P5 Military Service + Safe Deposit Box (campos de local/chave/quem abre/onde o nº está anotado), P6 Home Safe + Papers My Attorney Holds + Missing Papers + Other Hiding Places. Sem room-notice.
lib.typ: `elp-role-table(roles, headers:, widths:, row-h:)` promovido do ch02 (padrão Who/Name/Phone, retrocompatível); ch03 usa headers Document / Where It's Kept / Who Has a Copy / Date.
- ch03 (revisão): p.18 já registra ONDE estão apólices e declarações de imposto; ch07 e ch08 devem remeter a ela ("see Where My Important Papers Are") em vez de repetir o local do papel.

**ch04 (Weekend 1, 12 págs, PDF págs. 21-32; impressas 17-28).** P1 Health Conditions (opener + tabela 4 col), P2 Allergies + blood type/implants/organ donor card, P3-5 Medications Every Day (12 linhas/pág, Medicine / Dose and When / What It Is For / Prescribed By), P6 as-needed + vitamins, P7 My Doctors (10 linhas), P8 Pharmacy/Hospital + onde ficam os cartões de saúde (sem nº), P9 Equipment, P10 Surgeries and Stays, P11 Notes (rotina de remédios, quem ajuda), P12 Medicine changes log + room-notice. Sem conselho médico, sem nomes de exemplo.
Sem blocos novos em lib.typ (só `elp-table` com 0,6" de linha). ch05 deve remeter a ch04 para saúde; ch07 (Medicare) só "see Where My Health Cards Are Kept".

**ch05 (Weekend 2, 5 págs, PDF págs. 33-37; impressas 29-33).** P1 opener + nome legal/outros nomes/nascimento/naturalidade/religião, P2 Pais + Irmãos, P3 Casamentos + Filhos, P4 Netos + Others I Count as Family + Where My ID Is Kept (carteira, SS card "not the number", outros; certidão/passaporte só remetem a "Where My Important Papers Are"), P5 School/Work/Military (discharge papers: onde ficam). Sem nº de documento, sem room-notice, sem blocos novos. ch06+ (Social Security) pode remeter ao cartão em ch05 p.4.

**ch06 (Weekend 2, 16 págs, PDF págs. 38-53; impressas 34-49).** P1 opener + Checking, P2 Savings/CDs, P3 uso das contas (outros na conta, onde ficam extratos, banco, onde logins estão anotados, dinheiro em casa), P4 Investments + advisor, P5 outros bens, P6 Retirement (IRA/401k), P7 Pensions/Annuities, P8 Social Security (card remete a ch05) e outros benefícios, P9-10 cartões de crédito/loja/débito, P11 Loans, P12 Money Owed to Me, P13-14 contas mensais/anuais/assinaturas, P15 pagamentos automáticos, P16 Who Keeps Bills Paid + notes + room-notice. Só "Last 4 (optional)" e onde ficam extratos; sem senhas nem conselho financeiro. Seguros (ch07) e imóveis/veículos/impostos (ch08) não tocados. Sem blocos novos.

**ch07 (Weekend 2, 8 págs, PDF págs. 54-61; impressas 50-57).** P1 opener + Life Insurance (Company/Kind/Beneficiary/Last 4) + quem liga, P2 Other Places Life Insurance May Hide (emprego, sindicato, cartão, hipoteca), P3 Health + Medicare (remete a "Where My Health Cards Are Kept"; 1-800-MEDICARE), P4 Long-Term Care + Annuities (remete a ch06 Pensions and Annuities), P5 Auto, P6 Homeowners/Renters/outros, P7 Veterans (VA 1-800-827-1000; papéis remetem a ch03), P8 Who Will Claim What + outros benefícios + notas. Locais de apólices só remetem a "Where My Important Papers Are". Sem nº completo, sem room-notice, sem blocos novos. ch08 não repete seguros; impostos/imóveis/veículos ficam lá.

**ch08 (Weekend 2, 6 págs, PDF págs. 62-67; impressas 58-63).** P1 opener + My Home (endereço, own/rent, onde fica a escritura, hipoteca, imposto predial), P2 Other Property (tabela + chaves/aluguel), P3 Vehicles (tabela com "Where the Title Is Kept", sem VIN/placa) + chaves, P4 Businesses and Partnerships, P5 Accountant/Tax Preparer, P6 Tax Returns and Records (remete a "Where My Important Papers Are"; quanto tempo guarda, registros antigos, impostos em aberto, notas). Sem nº de documento, sem room-notice, sem blocos novos. Fecha o Weekend 2; ch09 abre o Weekend 3.

**ch09 (Weekend 3, 8 págs, PDF págs. 68-75; impressas 64-71).** P1 opener + Utilities (tabela Service/Company/Autopay, remete a ch06 para autopay) + titular da conta, P2 Phone/Internet/TV/Security + equipamento + onde logins estão anotados, P3 Shutoffs and Breakers (água, gás, disjuntores, outros), P4 Keys (spares, quem tem chave, outras entradas), P5 Alarm and Cameras (só "where the code is written down"), P6 People I Trust (tabela 8 linhas), P7 Mail, Garage and Storage (sem combinações de cadeado), P8 Seasonal Routines + notas. Sem room-notice, sem blocos novos. ch10 (pets) abre em seguida, ainda Weekend 3.

**ch10 (Weekend 3, 4 págs).** P1 opener + quem cuida dos pets agora, onde ficam os papéis, outros cuidadores, notas. PDF págs. 76-79 (impressas 72-75). P2-4 uma página por pet (idêntica): nome, espécie/raça, idade, veterinário/telefone, alimentação, remédios e horários, hábitos, quem assume, "Have They Agreed? (Yes / Not yet asked)", Plan B If That Person Cannot (1 linha). Sem conselho veterinário, sem room-notice. Bloco `pet-page` é local ao ch10 (macro no .typ), não promovido ao lib.typ. ch11 (digital) abre em seguida, ainda Weekend 3.
