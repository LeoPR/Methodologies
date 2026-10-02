---
title: 'M2a: custo do uso interativo por rota (perfil real de tokens)'
created: 2026-10-01
updated: 2026-10-01
status: 'Executado em 2026-10-01. Desenho fixado e commitado antes dos números; resultados e leitura abaixo dele.'
instrumento: perfil_interativo.py (lê os transcripts do Claude Code; não faz chamada de API)
precos: precos-2026-10-01.json (fonte primária, datada)
---

# M2a: custo do uso interativo por rota

Parte calculável do M2 do [PLANO-v2](../PLANO-v2.md). Pergunta: com o perfil de tokens do uso real do
dono, quanto custaria o mesmo trabalho em cada rota, e que parte dele caberia numa máquina local?

## Desenho (fixado antes de olhar os números)

### Dados

- **Fonte:** os transcripts locais do Claude Code do dono, em todos os projetos; só metadados (modelo,
  contagem de tokens, nome de ferramenta, caminho do arquivo editado). Nenhum conteúdo sai.
- **Janela fechada:** até 2026-10-01T00:00Z (a sessão de hoje ainda cresce).
- **Dedup** por `message.id`, como no `parse_usage.py`; o modelo `<synthetic>` sai.
- **Cobertura:** a limpeza automática do Claude Code apaga sessões antigas. Setembro de 2026 é o
  mês de referência; os meses anteriores são **piso**, não total.

### Rotas comparadas (preços em `precos-2026-10-01.json`)

- **API da Anthropic**, preço de tabela de cada modelo usado, com o cache separado em escrita de 5 min,
  escrita de 1 h e leitura.
- **Copilot Pro+**: o Copilot cobra cada modelo Claude ao mesmo preço por token (verificado). Ele lista
  uma só taxa de escrita de cache; a escrita de 1 h é cobrada nessa taxa. Custo do plano:
  US$ 39 + o que passar dos US$ 70 inclusos.
- **Claude Max** (5x: US$ 100; 20x: US$ 200): preço fixo. O limite é por janela de 5 horas, não por
  token, então este cálculo **não** diz se o uso cabe no plano; só compara o preço.
- **Contrafactual de modelo mais barato:** o mesmo perfil de tokens aos preços do Sonnet 5.5 e do
  Haiku 4.5. Isso mede só o preço. A capacidade é outra pergunta (D1; banco de modelos).
- **Local (RTX 3060, 12 GB):** custo marginal zero. Mede-se só se o contexto cabe, pelas medições já
  feitas no [STAGE5](STAGE5.md) (qwen3:8b cabe com 32k de contexto; decode de ~57 tok/s). Nada
  é medido de novo (parcimônia).

### Unidade de tarefa e classes (regra mecânica)

- **Turno:** de um pedido humano (registro de usuário que não é resultado de ferramenta, nem meta,
  nem resumo de compactação) até o próximo. Entram as chamadas da linha principal e as dos
  subagentes da mesma sessão com horário dentro do turno.
- **Edição:** chamada de `Edit`, `Write`, `MultiEdit` ou `NotebookEdit`; conta-se o número de arquivos
  distintos.
- **Classes:**
  - **C1 pergunta:** nenhuma edição; até 2 chamadas da linha principal.
  - **C2 investigação ou ação por shell:** nenhuma edição; 3 chamadas ou mais.
  - **C3 edição pontual:** edição em 1 arquivo.
  - **C4 multi-arquivo:** edição em 2 arquivos ou mais.
- **Contexto do turno:** o maior contexto de uma chamada (entrada + leitura de cache + escrita de
  cache).

### Saídas

1. **Por mês:** tokens por campo e custo equivalente em cada rota.
2. **Por classe:** número de turnos; mediana e p90 de chamadas, contexto e saída; custo por turno na
   API; parte com subagente; parte com contexto até 8k e até 32k (cabe no local).
3. **Por modelo:** parte do custo.

### Limites declarados de antemão

- **Perfil do Claude Code, não do Copilot.** O agente do Copilot monta o contexto de outro jeito; o
  número é "quanto este perfil custaria", não "quanto o Copilot cobraria".
- **Edição por shell não é detectada.** Arquivo alterado por `Bash`/`PowerShell` cai em C1/C2. Por
  isso C2 se chama "investigação ou ação por shell".
- **Tokenizador:** os modelos a partir do 4.7 contam cerca de 30% mais tokens para o mesmo texto que
  o Sonnet 4.6 e o Haiku 4.5. O contrafactual não corrige isso.
- **Um usuário só, com um estilo de uso** (sessões longas, muito subagente): o resultado é deste
  perfil, não de "o dev típico".

## Resultados (janela até 2026-10-01T00:00Z)

### Conferência do instrumento

- Os totais de tokens são **idênticos** aos do `parse_usage.py`, que agrega por outro caminho.
- O campo `fallback_credit` (não documentado) veio sempre vazio. Não se tira dele conclusão sobre
  cobrança extra.
- 32.096 chamadas de subagente ficaram **sem turno**, quase todas de uma sessão cujo transcript principal
  foi apagado. Entram nos totais do mês, não nas classes.
- Nenhum modelo ficou sem preço; 251 respostas sintéticas saíram.

### Por mês (setembro é a referência; os meses anteriores são piso)

Custo do mesmo perfil de tokens, em US$. Claude Max: 100 (5x) ou 200 (20x), fixo.

| mês | API (preço de tabela) | Copilot Pro+ (39 + excedente) | perfil no Sonnet 5.5 | perfil no Haiku 4.5 |
|---|---|---|---|---|
| 2026-05 | 1.420 | 1.231 | 526 | 263 |
| 2026-06 | 1.308 | 1.160 | 497 | 248 |
| 2026-07 | 3.479 | 3.066 | 1.108 | 554 |
| 2026-08 | 5.012 | 4.382 | 1.667 | 834 |
| 2026-09 | 3.694 | 3.229 | 1.471 | 736 |

### Onde o custo está (janela inteira, preço da API)

- **Composição:** leitura de cache 55%; escrita de cache de 1 h 30%; de 5 min 7%; saída 8%; entrada
  sem cache perto de 0%.
- **Modelo:** Opus 5 48%; Opus 4.8 22%; Fable 5 13%; Opus 4.7 9%; Opus 5.5 4%; o resto abaixo de 2% cada.

### Por classe de turno (setembro de 2026)

| classe | turnos | chamadas (mediana / p90) | contexto máx. (mediana / p90) | saída (mediana / p90) | US$ por turno na API (mediana / p90) | parte do custo |
|---|---|---|---|---|---|---|
| C1 pergunta | 162 | 1 / 2 | 630.148 / 868.099 | 443 / 3.700 | 0,20 / 3,01 | 5% |
| C2 investigação ou shell | 193 | 5 / 19 | 469.523 / 929.908 | 6.276 / 19.996 | 1,65 / 7,72 | 20% |
| C3 edição pontual | 104 | 8 / 20 | 574.115 / 931.608 | 11.797 / 24.290 | 3,73 / 9,26 | 17% |
| C4 multi-arquivo | 220 | 14 / 67 | 612.639 / 904.859 | 25.029 / 71.250 | 5,73 / 15,43 | 58% |

A janela inteira tem o mesmo desenho (C4: 69% do custo; mediana de US$ 5,73 por turno). A saída
completa por turno é derivada: o script a regenera fora do repositório.

### Local (RTX 3060)

- **Nenhum turno cabe em 32k.** Das 29.346 chamadas da linha principal, 5 cabem em 32k e nenhuma em 8k.
- *Exploratório, fora do desenho:* a primeira chamada de cada sessão já leva de 25,6k a 61,5k tokens
  (19 sessões; mediana perto de 40k). É o próprio harness (instruções, ferramentas, memória) antes de
  qualquer trabalho.

### Exploratório: o mesmo perfil ao preço do Opus 5.5

Fora do desenho. O Opus 5.5 cobra a leitura de cache a 0,05× a entrada (US$ 0,20 por milhão, contra
US$ 0,50 do Opus 5). Com o perfil inteiro a esse preço, o custo cairia para **51% a 63%** do real,
conforme o mês.

## Leitura (o que isto decide)

1. **No uso agêntico pesado, a assinatura domina.** Em setembro, este perfil custaria US$ 3.694 na API
   e US$ 3.229 no Copilot Pro+, contra US$ 100–200 do Max: de 16 a 37 vezes mais. Quem paga por token
   usa menos, mas, para inverter a ordem, o uso teria de encolher de 16 a 37 vezes. O uso real aconteceu
   sob o Max; se houve cobrança extra, o transcript não registra (o dono confirma).
2. **O Copilot Pro+ não substitui o Max neste perfil.** Os US$ 70 inclusos pagam cerca de uma dúzia de
   turnos multi-arquivo (mediana de US$ 5,73). O valor dele aqui é o autocomplete ilimitado e o chat
   leve. Se o chat do Copilot gasta menos de US$ 15 por mês, vale conferir se o Pro (US$ 10, com o mesmo
   autocomplete ilimitado) basta. O M2b mede esse gasto.
3. **Pagando por token, a alavanca é o contexto acumulado, não a saída.** 92% do custo é cache: cada
   chamada relê centenas de milhares de tokens de sessão longa. Pela composição, a economia de primeira
   ordem é a higiene de sessão (sessão nova por tarefa, compactar cedo). A segunda é o modelo com leitura de
   cache barata. No Max isso não muda o preço; se muda o consumo do limite, não se sabe, porque o
   limite não é publicado em tokens.
4. **A 3060 não serve a este harness.** O Claude Code ocupa de 25k a 61k tokens antes de qualquer
   trabalho (mediana perto de 40k), e o trabalho logo passa dos 32k que cabem com o qwen3:8b: só 5 de
   29.346 chamadas couberam. O papel do local fica no autocomplete
   ([STAGE4](STAGE4.md) C1) e no chat curto via BYOK, de contexto pequeno. O M2b mede se isso resolve.

### Limites desta leitura

- Os do desenho valem todos: perfil do Claude Code, não do Copilot; edição por shell não detectada;
  um usuário só.
- "Cabe no Max" é observação deste uso, não garantia: o limite é por janela e não se publica em tokens.
