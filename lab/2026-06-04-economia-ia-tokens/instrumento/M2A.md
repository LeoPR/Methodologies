---
title: 'M2a: custo do uso interativo por rota (perfil real de tokens)'
created: 2026-10-01
updated: 2026-10-01
status: 'Desenho fixado antes de olhar os números (2026-10-01). Resultados abaixo do desenho.'
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
