---
title: Analise geral das lacunas locais
created: 2026-06-07
status: ativo
scope: fechamento forte local (T10-T14)
---

# Analise geral das lacunas locais

Base: protocolo de fechamento local em `matriz-testes-faltantes.md` (T10-T14)
mais execucoes em `execucao-local-2026-06-06.md`.

## Status por teste local (T10-T14)

## T10 (P0) Repetibilidade local endurecida (N >= 5)

Estado: **aberto**

Evidencia atual:
- ha rodada N=5 para `gemma3-4b` com reprova de qualidade (`pass_full_rate=0`).
- para `llama3.1-8b`, as ultimas tentativas de N=5 sofreram timeout de probe,
  sem lote avaliavel persistido.

Lacuna:
- falta ao menos 1 rodada N>=5 valida e completa no modelo piso local alvo
  (8B) com comparabilidade preservada.

## T11 (P0) Gate local de seguranca-epistemica

Estado: **aberto**

Evidencia atual:
- mitigacao `anti-n2-guard` reduziu N2 e falso-positivo na rodada runs=1.
- `pass_full` continua em 0 e ainda ha alucinacao acima do alvo em cenarios-chave.

Lacuna:
- falta cumprir simultaneamente os gates por modelo:
  - P7 >= 0.80
  - P6 >= 0.70
  - N1 = 0 e N2 = 0
  - alucinacao <= 0.10

## T12 (P0) Estabilidade intercenario no local

Estado: **aberto**

Evidencia atual:
- 3 cenarios foram exercitados em runs=1 (bom para diagnostico).
- com N baixo e sem lote N>=5 valido no 8B, ainda nao ha estabilidade estatistica.

Lacuna:
- falta agregado intercenario com `pass_full >= 0.80` e falso-positivo zero no
  cenario limpo em N suficiente.

## T13 (P1) Curva de degradacao controlada (8B -> 4B -> 3B)

Estado: **parcial**

Evidencia atual:
- ha sinais para 8B, 4B e 1.7B, porem com mistura de falhas de infraestrutura
  (probe timeout) e falhas de julgamento.

Lacuna:
- falta escada limpa com o mesmo protocolo e sem perdas por probe para separar
  degradacao de capacidade de degradacao operacional.

## T14 (P1) Operacao local minima reproduzivel

Estado: **aberto**

Evidencia atual:
- comandos e artefatos estao registrados.
- ainda nao ha duas execucoes completas independentes no regime estavel de escala
  (N>=5 no 8B) com os mesmos criterios de aceite.

Lacuna:
- falta runbook de aquecimento + timeout por classe de modelo e dupla repeticao
  em ambientes distintos.

## Diagnostico de causa raiz (local)

1. Gate de infraestrutura (probe): timeout de inicializacao afeta modelos >=4B em
   parte das tentativas com `probe_timeout_s=45`.
2. Gate de qualidade (scoring): mesmo quando passa do probe, ainda existe
   `pass_full=0` com erros de deteccao e alucinacao.
3. Gate de robustez de formato: parse JSON ainda falha em subconjunto de respostas,
   especialmente em cenario limpo.

## Prioridade pratica (ordem de ataque)

1. Estabilizar abertura de rodada (warm-up obrigatorio e/ou probe timeout por porte).
2. Garantir uma rodada N>=5 valida no 8B de referencia.
3. Reaplicar anti-N2 + reforco anti-alucinacao com o mesmo protocolo intercenario.
4. Reexecutar escada de modelos para quantificar degradacao real (T13).
