---
title: ADR-008 — Documentação multilíngue: fonte canônica única + tradução rastreável
status: aceito
date: 2026-06-30
scope: metodologia de documentação do repo (como padronizamos nomes, marcação de idioma e frescor de docs multilíngues, e como o git os organiza); decorre do §3 e do §5 do Strata; reaproveitável em outro projeto
deciders: [Leonardo Marques, Claude Code]
---

# ADR-008 — Documentação multilíngue: fonte canônica única + tradução rastreável

## Contexto

O repositório passou a ter documentos em mais de uma língua (a porta de entrada em inglês e em português).
Sem uma regra única, o multilíngue apodrece de três formas:

- não se sabe **qual versão é a fonte** e qual é a derivada;
- a tradução **envelhece em silêncio**, e o leitor confia num texto que já divergiu do original;
- os nomes de arquivo e os links **divergem** entre línguas e entre projetos.

Precisávamos de um padrão que resolvesse os três, que tivesse lastro em fonte primária (não ad-hoc), e que fosse **reusável** para organizar outro projeto.

## Decisão

Um esquema em quatro peças. (Cada peça verificada contra fonte primária; ver Fundamentação.)

**1. O nome diz a fonte-da-verdade.**
O arquivo **sem sufixo é o canônico, em inglês** (`README.md`). As traduções são derivadas, com sufixo de idioma BCP 47 (`README.pt-BR.md`).
Arquivos que o GitHub reconhece pelo nome exato (LICENSE, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, AGENTS, templates) **mantêm o nome canônico**; a tradução é um arquivo-irmão sufixado, nunca um rename. O texto operativo da LICENSE não se traduz.

**2. A marcação de idioma é um cólofon l10n.**
No topo de cada arquivo, um comentário HTML (que o GitHub não renderiza) carrega a proveniência:
`doc_id` (identidade compartilhada por todas as línguas), `lang` e `source_lang` (BCP 47), `translation_of` (aponta para a fonte) e `canonical` (na fonte).
No README, o comentário substitui o frontmatter YAML, que o GitHub mostraria como uma tabela.

**3. O frescor mora no histórico do git.**
A régua de "esta tradução está atual?" é a **data do último commit de cada arquivo**, não uma data escrita à mão.
Editar fonte e tradução no mesmo commit = em sincronia. Mexer só na fonte = a tradução fica marcada como desatualizada.
Complementos opcionais: um aviso visível ao leitor quando atrasa, e um limiar gradual (tolerar N correções triviais antes de alarmar).

**4. A ligação cruzada é um seletor no topo.**
Cada arquivo abre com um seletor de idioma recíproco, com o nome de cada língua no próprio idioma (autônimo) e links relativos.

**No git:** commits de tradução usam o prefixo `i18n(...)`; o par fonte + tradução entra junto, para nascerem em sincronia.

## Fundamentação

### Padrões e precedentes (L1)
- **standard-readme:** `README.md` reservado ao inglês; traduções `README.<bcp47>.md`.
- **Debian (`translation-check`):** carimba em cada tradução o commit exato do original de onde saiu, e marca a página quando o original avança. É o nosso `source_commit`/régua-git em forma git-nativa.
- **GNU (GNUN):** injeta um aviso ao leitor quando a tradução atrasa, para não servir texto velho como se fosse atual.
- **BCP 47 (IETF/W3C):** o formato da etiqueta de idioma. É a **única peça do desenho com padrão duro**.
- **DataCite 4.6:** vocabulário recíproco real `IsTranslationOf`/`HasTranslation`, e um papel `Translator` que aceita "sistema automatizado" (cobre a tradução por IA).
- **NISO (Version of Record)** e **Chicago Manual of Style** (edição vs. impressão, ~20% de mudança): a fonte é a versão de referência; só mudança substantiva obriga re-traduzir.
- **Folha de rosto / cólofon de editora:** o "traduzido da Nª edição de X" é a forma impressa do nosso cólofon de proveniência.

### Biblioteconomia (L1)
- **IFLA LRM / FRBR:** uma tradução não é uma obra nova — é uma **Expression distinta da mesma Work**. O `doc_id` é a Work: a identidade estável que colige as línguas, independente do nome do arquivo.

### Do próprio Strata (`recipe/knowledge-architecture.md`)
- **§5 (fonte única):** uma língua é a voz canônica; a tradução é materialização derivada, nunca uma segunda verdade.
- **§3 (rastreabilidade):** o `source_commit` e o aviso ao leitor são o **traço honesto** — a tradução desatualizada vira um tombstone legível ("pode divergir"), em vez de mentir sobre o frescor. Medir o frescor pela régua do git é o §8 (história recuperável por estado) servindo à superfície.
- **Camadas L0/L1/L2:** o `doc_id`/Work é **L0** (atemporal); a convenção BCP 47/DataCite é **L1**; o cólofon e o checador git são **L2**, datados e destacáveis. Datamos a ferramenta, não o princípio.

*Limite honesto:* só o BCP 47 é padrão duro. "Qual é canônico" e "está atualizado" são prática de comunidade — até a W3C ITS 2.0, a recomendação mais voltada a tradução, **omite** o frescor de propósito. Preenchemos uma lacuna que os padrões deixam aberta; não reinventamos padrão.

## Como aplicar a outro projeto

1. Escolher a língua canônica e deixá-la no arquivo sem sufixo; as demais recebem sufixo BCP 47.
2. Pôr o cólofon l10n no topo de cada arquivo (o mesmo `doc_id` nas versões da mesma obra).
3. Deixar a régua de frescor no git (comparar a data de commit da fonte com a da tradução); opcionalmente, um checador que injeta o aviso ao leitor.
4. Abrir cada arquivo com o seletor de idioma recíproco (autônimos).
5. Traduzir só a prosa — nunca código, caminhos ou nomes de arquivo. Traduzir o essencial (entrada + produto) e deixar o resto na língua-fonte, com uma nota.

## Consequências

- Com o inglês canônico, a atualização vai primeiro à fonte, e a tradução a segue. Se, na prática, a edição acontecer sempre na outra língua, reavaliar os papéis.
- Escopo deliberado: bilíngue só na **entrada e no produto**; os docs de pesquisa ficam numa língua, com nota. Traduzir tudo, com um mantenedor só, é a divergência que este ADR existe para evitar.
- A tradução por IA é um caso de **registro de uso de IA** (o `Translator` do DataCite = "sistema automatizado").
- **Sinal de troca:** com 2 línguas, o seletor recíproco e o frescor pelo git bastam. A partir de **3 línguas**, a ligação todos-com-todos e o frescor pedem ferramenta (um checador, ou um gerador de site com i18n). Se surgir um padrão oficial de frescor de tradução, migrar para ele — o princípio (fonte única + traço honesto) sobrevive à troca.
