---
title: Plano de comprovacao forte do Strata
created: 2026-06-06
status: draft-executavel
scope: fechar lacunas de evidencia para claim forte e preparar trilha para Strata 2.0 sem quebrar essencia
---

# Plano de comprovacao forte do Strata

Objetivo: sair de evidencia promissora para evidencia forte, comparavel e auditavel,
com criterio explicito para:

1. validar claim de aplicabilidade por IA em nuvem e local;
2. separar ganho de forma AI-nativa por gate semantico versus compressao de contexto;
3. decidir com seguranca quando promover ajustes no produto (v1.x) e quando abrir v2.0.

## Estado de partida (consolidado)

- Tier local: melhora forte com forma AI-nativa, mas com fragilidade em modelos pequenos.
- Tier nuvem: sinal forte em F1, mas com N baixo por celula e risco de vies de juiz-familia.
- Ponto cego remanescente: P6 (sem-fonte) ainda vaza em parte dos modelos.
- Risco metodologico principal: mistura de rodada de evidencia com rodada de instrumento.

## O que conta como comprovacao forte

Comprovacao forte para o claim principal do Strata so e aceita quando todos os gates
abaixo estiverem verdes no mesmo ciclo:

- Gate G1 (repetibilidade): N >= 3 por celula em todos os testes de decisao.
- Gate G2 (comparabilidade): rodada rotulada como evidencia, com scorer unico por canal
  e comparabilidade declarada.
- Gate G3 (seguranca): cobertura alta e estavel de P7/6-bis sem aumento de N1/N2.
- Gate G4 (epistemologia): cobertura estavel de P6/6 (sem-fonte) nos modelos-alvo.
- Gate G5 (ecologia): resultado replica em pelo menos 3 projetos reais alem do fixture.
- Gate G6 (juiz): ao menos 2 juizes independentes (ou 1 juiz humano + 1 LLM) com
divergencia documentada.

## Trilha de execucao sugerida

1. Rodar bloco E1 (fechar rigor estatistico do que ja existe).
2. Rodar bloco E2 (A/B/C para desconfundir gate x compressao).
3. Rodar bloco E3 (validade ecologica em projetos reais).
4. Rodar bloco E4 (sandbox L2 operacional e seguranca).
5. Fechar sintese e decisao de produto (v1.x ou abrir v2.0).

Detalhamento operacional em: matriz-testes-faltantes.md
Criterio de produto em: criterio-promocao-strata-v2.md

## Regra de governanca deste ciclo

Cada execucao nova deve declarar no resumo:

- tipo: evidencia | instrumento | infra
- pergunta: Q1 | Q2 | Q3
- comparabilidade: com qual rodada anterior e sob qual scorer

Sem esses 3 campos, o artefato nao entra na sintese final.

## Sintese de fechamento

`sintese-envelope-operacao.md` consolida a evidencia ja produzida (tier nuvem, tier
local, A/B prosa vs AI-nativa, piso local) num **envelope de operacao** por modelo:
onde o Strata funciona, condicao minima vs otima, o que a semantica resolve sozinha
vs o que precisa de orientacao explicita. Inclui a arvore/grafo de decisao do Strata
(automatica / situacional / cobertor-curto) e os cenarios **ler-e-pronto** e
**otimo-orientativo**. Marca as 4 lacunas [aberto] que ainda separam o claim atual do
claim "completo" — que sao exatamente os itens P0 de `matriz-testes-faltantes.md`.

## Fechamento forte local

`fechamento-forte-local.md` define o pacote de endurecimento local para encerrar a
trilha offline com criterio de aceite objetivo (N>=5, gates P6/P7, N1/N2 zerados,
alucinacao controlada e estabilidade intercenario). O status "local fechado" depende
desse pacote e foi incorporado ao criterio de promocao em
`criterio-promocao-strata-v2.md`.

Execucao registrada em `execucao-local-2026-06-06.md` (rodada 8B+4B com N=5,
incluindo artefatos gerados e status parcial por modelo).

Atualizacao: a rodada incremental de **3 cenarios com runs=1** (baseline
`num_predict=1024`, contexto default) foi registrada no mesmo arquivo com resultados
e deducoes para reavaliacao posterior.

Atualizacao 2: mitigacao **anti-N2/falso-positivo** foi testada antes da escala
(`--anti-n2-guard`) e tambem registrada no log de execucao local, com comparativo
direto contra a rodada base de 3 cenarios.

Atualizacao 3: investigacao de **contexto default vs contexto forcado** com
observacao externa via `docker logs` do servidor Ollama tambem foi registrada
no log local (incluindo deducao de teto efetivo observado neste ambiente).

Atualizacao 4: continuidade de runs locais (incluindo tentativas de escala,
scouting multi-modelo e deducoes de gargalo de probe) foi incorporada em
`execucao-local-2026-06-06.md`.

Atualizacao 5: analise consolidada do que falta no fechamento local foi
documentada em `analise-lacunas-local-2026-06-07.md`.

Atualizacao 6: shortlist de modelos modernos locais e comandos `ollama pull`
foi documentada em `modelos-locais-modernos-via-ollama-2026-06-07.md`.

Atualizacao 7: a shortlist foi operacionalizada com expansao de catalogo,
pull confirmado de `granite4.1:8b` e `nemotron-3-nano:4b`, e smoke individual
de `qwen3:0.6b` e `gemma3:1b` registrado no log local.
