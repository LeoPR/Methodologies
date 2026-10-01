---
name: status-methodologies-project
type: status
status: active
created: 2026-06-03
updated: 2026-10-01
---

# STATUS: 2026-09-30

Estado atual, no presente. Estados anteriores estão no histórico do git deste arquivo.
Termos de prova (K, gold mecânico, júri cego, §N): [GLOSSARIO.md](GLOSSARIO.md).

## Strata (produto)

- **Canônico:** L0 fechado; versão no frontmatter de
  [`recipe/knowledge-architecture.en.md`](recipe/knowledge-architecture.en.md). Citações do L0
  conferidas em fonte em 2026-09-26 ([revisão temporal](lab/2026-09-26-revisao-temporal/)).
- **Evidência:** estado consolidado em
  [`OPINIAO-DE-USO.md`](lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) e no hub
  [`ARQUITETURA-E-EVIDENCIAS.md`](lab/2026-06-04-strata-hipoteses/ARQUITETURA-E-EVIDENCIAS.md).
- **Qual modelo usar:** [`recipe/strata-com-ia.*`](recipe/strata-com-ia.pt-BR.md), a partir do
  [banco de modelos 2026-09](lab/2026-09-26-banco-modelos/). Capacidade se mede na nuvem nos mesmos
  pesos; local só viabilidade ([encaixe por placa](lab/2026-06-04-economia-ia-tokens/instrumento/STAGE5.md)).
- **Tempo no Strata (F6-status, 2026-09-29):** com 8 fabricantes, o método atual faz os modelos
  avisarem mais quando a ordem ou a vigência não se resolve (+25 pontos contra "sem método"); o
  parágrafo "Ler o tempo de volta" deu sinal fraco e desigual e entrou no §3 como norma, com o
  resultado declarado ([resultados](lab/2026-09-26-temporalidade/RESULTADOS-f6-status.md)). Achado:
  com o método, alguns modelos seguiam a fonte canônica declarada contra a evidência.
- **§5 "Fonte declarada ≠ fonte usada" (v1.2.8):** testado com 8 fabricantes; o alvo sobe e os
  controles ficam na margem; aviso à toa residual quando há cópia divergente e nada contradiz a
  declaração ([resultados](lab/2026-09-26-temporalidade/RESULTADOS-f6-fonte.md)).
- **Guia de modelos:** custo e tempo em faixas; valores exatos e datados no banco.

## Frentes abertas

- **Temporalidade** (3ª frente, [`lab/2026-09-26-temporalidade/`](lab/2026-09-26-temporalidade/)):
  literatura em 8 mapas, ontologia v0, protótipo de ordenador e a bateria de capacidade v1
  ([resultados](lab/2026-09-26-temporalidade/RESULTADOS-bateria-v1.md), 8 modelos de 6 fabricantes).
  - **Sem ajuda:** a ordem por dependência sai certa em 0,93, mas o passo que falta é notado em 1 de
    92.
  - **Com o protocolo da ontologia:** a lacuna sobe para 0,48 e o intruso para 0,99 (H1 vale no
    modo principal e com orçamento de tokens adequado). Mas o alarme falso nos controles sobe de 0,02 para
    0,21 (H2 violada). O protocolo não vira recomendação.
  - **Próximo, se o dono quiser:** v2 do protocolo (lacuna por incompatibilidade de estado; teto de
    tokens decidido antes).
- **Comporta** (2ª metodologia, [`lab/2026-06-04-economia-ia-tokens/`](lab/2026-06-04-economia-ia-tokens/)):
  estágios 1–5 medidos; não destilado para `recipe/`.

## Aguardam decisão do dono

1. Tirar da superfície o histórico append-only do hub (o git guarda o traço).
2. Publicar nos canais as correções do outreach (fonte: `outreach/2026-09-26-*`).

## Pendências do método (canônico)

- Parte IV (adoção/brownfield) e a varredura de evidência do eixo de segurança (os dois "Open
  items" do canônico).
