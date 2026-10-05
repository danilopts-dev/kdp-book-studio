# Style sheet (migrado do projeto antigo em 2026-10-05)

Regras completas do livro: `legacy/docs/reguas-operacionais.md` (valem aqui; os agentes devem lê-las junto com `rules/`). Decisões já tomadas: `legacy/docs/relatorio-decisoes.md`. Itens religiosos: `legacy/docs/revisao-religiosa.md`. Hebraico: `legacy/docs/hebraico-para-revisao.md`.

- **Voz:** 6 a 10 anos, inglês americano, frases curtas, contrações no texto corrido, humor limpo (bobo pode; nojento ou "escolha entre duas coisas ruins" não). A história é contada como a tradição conta ("The story says..."), sem tratar como fato científico nem como lenda a descartar.
- **Leitor:** a criança (instruções em 2ª pessoa) e o adulto que acende as velas com ela (Before the Candles é em família).
- **Níveis:** ★ (6-7 anos) e ★★ (8-10), marcados no título de cada atividade; ★★ mais difícil que ★ em pelo menos 2 eixos (tabela na seção 4 das réguas).
- **Caixa "What's a...?":** uma por noite, até 40 palavras por termo; não pressupõe nem subestima.
- **Placares:** um tracinho ou círculo por ponto. Nada de regra de pontuação.
- **Tetos:** Tonight's Story 120-180 palavras; instrução de atividade até 25; Before the Candles até 60 (exceções: receita da N6, Mad Libs da N6, torneio da N5).
- **Grafias fixas:** Hanukkah (não Chanukah), hanukkiah, menorah, shamash, dreidel, gelt, latke, sufganiyah (plural sufganiyot), tzedakah, Maccabee, Antiochus, Mattathias, Modiin. Diáspora (Hanucá 2026: 4 a 12/dez).
- **Hebraico:** miolo das 8 noites só com transliteração + inglês; script hebraico só no cartão de bênçãos do bônus (aprovado em 26/09).
- **Ilustração:** line art storybook P&B, traço grosso uniforme, sem sombreado/cinza/preto chapado, sem texto nem moldura, rostos simples e expressivos; homens da época com cabelo curto; sem nenhum elemento natalino. Prompts em `legacy/docs/ilustracoes-prompts-geracao.md`.
- **O livro NÃO faz:** menção a Natal (nem por comparação), travessão longo (— –), hebraico no miolo das noites, personagem-guia recorrente, claim religioso de "o jeito certo".
- **Puzzles:** feitos por script (puzzle e gabarito juntos, verificados). Os PNGs prontos estão em `inputs/puzzle-assets/`; os scripts em `legacy/scripts/`. Não gerar puzzle "à mão".
- **Layout:** 8.5x11, miolo P&B, gutter 0.65", fólio sempre na mesma altura, 96-104 págs (teto 108). Respeitar a caixa de texto: as artes foram dimensionadas para ~7.4" de largura.

# Continuidade

Texto de todas as noites, front matter, mini-guia, cartão de bênçãos e back matter já está **escrito e aprovado** em `legacy/manuscript/`. Falta diagramar no engine do estúdio (as tarefas `unit:*` são de diagramação, não de redação). Temas de puzzle já usados (não repetir): N1 nomes da história; N2 hanukiá/menorá; N3 símbolos jarro/vela/dreidel/estrela/hanukiá/moeda; N4 contagem de velas; N5 letras do dreidel; N6 cozinha e frituras; N7 moedas/tzedaká.
