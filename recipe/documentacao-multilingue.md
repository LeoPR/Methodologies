---
title: Documentação multilíngue — fonte canônica + tradução rastreável
status: portável (piloto aplicado neste repo; pronto para reuso)
created: 2026-06-30
updated: 2026-07-23
---

# Documentação multilíngue — fonte canônica + tradução rastreável

Método portável para ter o README e os documentos de entrada em mais de uma língua,
com **uma fonte canônica** e **traduções que não apodrecem em silêncio**.

Este guia se basta sozinho: dá para copiá-lo para outro projeto e uma IA o aplica.
O *porquê* completo, com as fontes primárias, está no [ADR-008](../decisions/ADR-008-documentacao-multilingue-fonte-canonica.md).

## Quando usar

Quando os documentos de entrada de um projeto (o README e os poucos docs que o leitor abre primeiro)
precisam existir em duas línguas, e você quer saber sempre qual é a fonte e se a tradução está atual.

**Não** vale traduzir tudo: só a **entrada** e o **produto**. Os documentos de pesquisa ficam numa língua,
com uma nota. Traduzir tudo, com um mantenedor só, é a divergência que este método existe para evitar.

## As quatro regras

**1. O nome diz a fonte.**
O arquivo **sem sufixo é o canônico** (`README.md`), na língua principal (aqui, inglês).
A tradução é derivada, com sufixo de idioma [BCP 47](https://www.w3.org/International/articles/language-tags/): `README.pt-BR.md`.
Arquivos que a plataforma reconhece pelo nome exato (LICENSE, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, AGENTS, templates de issue)
**mantêm o nome canônico**; a tradução é um arquivo-irmão sufixado, nunca um rename. O texto da LICENSE não se traduz.

**2. A marcação de idioma é um cólofon.**
No topo de cada arquivo, um comentário HTML (que não renderiza na página). Na fonte:

```markdown
<!-- l10n: doc_id=<slug-estável> · lang=en · canonical -->
```

Na tradução:

```markdown
<!-- l10n: doc_id=<mesmo-slug> · lang=pt-BR · source_lang=en · translation_of=README.md -->
```

O `doc_id` é o mesmo nas duas versões: é a identidade compartilhada que liga as línguas, independente do nome do arquivo.

**3. O frescor mora no histórico do git.**
A régua de "esta tradução está atual?" é a **data do último commit de cada arquivo**, não uma data escrita à mão.
Editar fonte e tradução no mesmo commit = em sincronia. Mexer só na fonte = a tradução está desatualizada.
Não invente um carimbo de data manual: o git já sabe a verdade.

**4. O topo tem um seletor recíproco.**
A primeira linha visível de cada arquivo lista as línguas, com o nome de cada uma **no próprio idioma** (autônimo), com links relativos:

```markdown
**English** · [Português](README.pt-BR.md)
```
```markdown
[English](README.md) · **Português**
```

Não use bandeiras: bandeira é país, não idioma.

**O que traduzir:** só a prosa. Nunca código, caminhos, nomes de arquivo, chaves de configuração, nem o texto da LICENSE.

## Como aplicar — por uma IA

Num chat novo com o projeto aberto, cole:

```text
Organize os documentos de entrada deste projeto (o README e os poucos docs que o
leitor abre primeiro) em inglês e português, por este método:
- README.md (sem sufixo) = inglês, canônico; a tradução vira README.pt-BR.md.
- No topo de cada arquivo, um comentário HTML l10n com: doc_id (o mesmo nas duas
  versões), lang, source_lang e translation_of na tradução, canonical na fonte.
- Primeira linha visível: seletor de idioma recíproco, com o nome de cada língua no
  próprio idioma (English / Português), sem bandeiras.
- Traduza só a prosa; nunca código, caminhos, nomes de arquivo, ou o texto da LICENSE.
- Não invente carimbo de data: a régua de frescor é o histórico do git.
- Arquivos de nome padrão (LICENSE, CONTRIBUTING, SECURITY, AGENTS) mantêm o nome
  canônico; a tradução é um arquivo-irmão sufixado.
Faça o par do README primeiro. Depois liste que outros docs de entrada valem traduzir,
e deixe os de pesquisa numa língua só, com uma nota.
```

## Como aplicar — por um humano

1. Escolha a língua canônica; deixe-a no arquivo sem sufixo. As traduções recebem sufixo BCP 47.
2. Ponha o cólofon l10n no topo de cada arquivo (o mesmo `doc_id` nas versões da mesma obra).
3. Abra cada arquivo com o seletor recíproco (autônimos).
4. Entre fonte e tradução no **mesmo commit**, para nascerem em sincronia; depois, deixe o git medir o frescor.
5. Traduza a entrada e o produto; deixe o resto na língua-fonte, com uma nota.

## Por que assim (o mínimo, para não desfazer)

- **Fonte única:** uma língua é a voz canônica; a tradução é derivada, nunca uma segunda verdade.
- **Traço honesto:** o `translation_of` mais a régua do git tornam a tradução desatualizada um estado *legível*,
  em vez de um texto que mente sobre o próprio frescor.
- **Só o BCP 47 é padrão duro.** "Qual é canônico" e "está atualizado" são prática de comunidade,
  com lastro em precedentes fortes (Debian, GNU, biblioteconomia IFLA LRM). O ADR-008 traça cada um.

## Portabilidade

Este arquivo viaja sozinho: copie-o para outro projeto e aplique. Se um dia ele mesmo precisar de tradução,
aplica-se a si próprio.

## Aplicação neste repositório (plano EN/PT-BR)

Objetivo editorial deste repo:

- `README.md` (raiz) em **inglês** como canônico.
- Versão em português no par `README.pt-BR.md`.
- Demais documentos de entrada/produto em pares `*.en.md` e `*.pt-BR.md`, sem renomear o canônico.

Estado atual e fila recomendada (superfície primeiro):

| Documento de superfície | Estado bilíngue | Próxima ação |
|---|---|---|
| `README.md` | ✅ par pronto (`README.pt-BR.md`) | manter sincronizado por commit |
| `recipe/knowledge-architecture.md` | ✅ par pronto (`knowledge-architecture.en.md`) | manter sincronizado por commit |
| `recipe/README.md` | ❌ sem par | criar `recipe/README.en.md` ou migrar canônico para inglês e criar `recipe/README.pt-BR.md` |
| `MAP.md` | ❌ sem par | criar `MAP.en.md` |
| `STATUS.md` | ❌ sem par | criar `STATUS.en.md` (resumo operacional; histórico pode ficar em PT-BR) |
| `recipe/o-que-voce-ganha.md` | ❌ sem par | criar `recipe/o-que-voce-ganha.en.md` |

Critério de priorização:

1. Entrada de navegação (`README`, `MAP`, `STATUS`).
2. Produto e adoção (`recipe/README`, `recipe/o-que-voce-ganha`, `knowledge-architecture`).
3. Pesquisa (`lab/`) fica monolíngue com nota, salvo necessidade específica.

## Técnica escolhida para manter sincronizado

Padrão adotado: **fonte canônica + espelho rastreável em commit único**.

Como operar em cada alteração de conteúdo:

1. Editar primeiro o arquivo canônico (sem sufixo).
2. Atualizar a tradução no mesmo ciclo de trabalho.
3. Commitar os dois juntos.
4. Se a tradução não ficar pronta, adicionar aviso explícito no topo da tradução e abrir item de pendência.

Checklist de sincronização por par:

- `doc_id` igual nas duas línguas.
- `translation_of` apontando para o canônico correto.
- seletor de idioma recíproco no topo dos dois arquivos.
- links internos revisados após rename de pasta/arquivo.

Esta técnica foi escolhida por ser independente de fornecedor/modelo de IA e por manter
o histórico do git como fonte objetiva de frescor.
