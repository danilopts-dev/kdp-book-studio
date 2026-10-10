# Etapa: entrega (finalize)

1. `./st check <slug> --pdf` final. Qualquer 🔴: volte à tarefa responsável (`/etapa`). O QR do bônus precisa estar real (sem aviso de "provisório").
2. Escreva `books/<slug>/READY.md` para o Danilo, em português simples, sem caminhos do projeto, comandos ou termos técnicos. Os arquivos são citados pelo nome dentro da pasta Entrega do OneDrive. Estrutura fixa:

```
# <Título>: pronto para o KDP (<data>)

## Antes de subir
(só o que ainda falta, numerado; se nada falta: "Nada. Pode subir.")
Ex.: testar o bônus pelo celular (escanear o QR no PDF, se inscrever, baixar o PDF).

## Upload no KDP, campo a campo
- Idioma, título, subtítulo, autor (copiar e colar)
- Descrição: "copie o bloco HTML da seção Descrição do arquivo listing.md"
- 7 keywords (uma por linha, prontas para colar)
- Categorias: as 3 sugestões (confirmar no seletor)
- Faixa de idade / conteúdo adulto, se se aplica
- ISBN, data de publicação, impressão (papel, cor, trim, sangria, acabamento da capa)
- Arquivos: miolo e capa (nome do arquivo na pasta Entrega)
- Uso de IA: o que declarar (texto, imagens, traduções)
- Preço sugerido
- Conferir no Visualizador antes de publicar

## Depois do upload
- A+ (banners: prompts no arquivo aplus-prompts.md)
- Amazon Ads: os termos de lançamento estão no listing.md (seção Keywords)

## Decidi sozinho (confira)
(só as que ainda importam, 1 linha cada; o resto está em decisoes.md)

## Arquivos na pasta Entrega
(tabela: arquivo | o que é)
```

3. `./st publish <slug>`: copia miolo, capa/guia, bônus, listing e READY.md para `Entrega/` na pasta do livro no OneDrive (não faz nada se `local.yaml` não existir).
4. Notion (se disponível): status do livro e nota "Pronto para upload".
5. Na nuvem: envie ao Danilo pelo SendUserFile o miolo, a capa (ou guia) e o PDF do bônus.
