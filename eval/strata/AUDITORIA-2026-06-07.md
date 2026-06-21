---
title: Auditoria adversarial dos testes do Strata (H-B/H-C) — fase 1
created: 2026-06-07
metodo: 6 auditores independentes (multi-agente) + síntese, lendo os artefatos reais
veredito: a maioria das conclusões "fechadas" NÃO está sustentada; reset necessário
---

# Auditoria — o que está sólido, o que está furado, e como refazer

> **Tombstone (Strata §3) — snapshot de 2026-06-07, em grande parte ENDEREÇADO depois.** Esta é a auditoria
> que disparou o reset. Não a leia como estado atual. Os furos foram tratados em trabalho posterior:
> fixtures congeladas por hash e scoring cego de verdade (ver `cenarios/`); **baseline/controle negativo**
> adicionados; **2º juiz cross-vendor** rodado — o "juiz único Claude" do item abaixo foi fechado pelo
> **R6** (gpt-4.1-mini sobre a nuvem) e pelo **F0** (9 juízes de 3 fabricantes, 7 convergem). O resíduo
> estreito está no [FECHAMENTO](../../lab/2026-06-04-strata-hipoteses/FECHAMENTO-avaliacao-strata.md). O texto
> abaixo fica como traço do que se sabia naquela data.

Auditoria adversarial (pedida pelo dono: *"ver se os testes foram feitos corretamente,
falhas e fraquezas"*). Vereditos por dimensão: hipóteses↔testes **parcial**; rigor
**frágil**; instrumentos **frágil**; fixtures **frágil**; acoplamento **parcial**;
online **frágil**.

## O claim honesto de hoje (único defensável)

> *"A forma AI-nativa melhora a detecção de fail-open em modelos locais fracos — sinal
> forte, mas confundido por (a) vazamento de gabarito no documento e (b) comprimento,
> ainda não desfeitos."*
>
> **Todo o resto é preliminar:** "nuvem satura", "piso 8B", "qualquer IA aplica" — não
> sustentados como estão.

## Os 5 furos que invalidam (severidade ALTA)

1. **H-C contaminado (circular).** A `strata-an-v0/v1` contém os problemas plantados
   **verbatim** (`velho/`, `pergunta pro pessoal`, `92%`, `limiar 0.70…0.85`,
   `tarefas.txt`); a prosa (`knowledge-architecture.md`) **não contém nenhum** (grep = 0
   matches). Logo o braço AN **entrega as respostas** e o braço prosa não. O "ganho da AN"
   (deepseek 0→4; P7 0→4/4) mede **leakage**, não compreensão. → invalida RESULTADOS-hc-ab
   e o piso-local (usa a AN contaminada).
2. **Fixture neutralizado ≠ gabarito/manifesto.** O `projeto-alvo` atual **não tem** P1
   (ambos os configs dizem 0.85) nem P7 (fail-**closed**); `velho/` e `tarefas.txt` nunca
   existiram em disco (só citados em texto). Mas gabarito e manifesto exigem P1–P7. Todos
   os RESULTADOS são **irreproduzíveis** contra o estado em git (nunca congelados por hash).
3. **O prompt vaza a taxonomia.** O prompt da matriz injeta `"id":"P1|…|P7|OTHER"` — o
   modelo recebe os 7 baldes prontos: mede **classificação em taxonomia vazada**, não
   diagnóstico. (E a causa-raiz documentada no RASTREAMENTO — "o modelo nunca recebe os
   ids" — está **factualmente errada**.)
4. **Online automático NUNCA rodou.** Os 5 modelos online estão `enabled:false`, sem API
   keys. Toda "evidência de nuvem" veio de **chat manual**, N=1, contra a fixture **antiga**
   (10/18 planos citam `0.70`, que não existe mais). O sabor **Anthropic do runner está
   quebrado** (usa shape OpenAI em `api.anthropic.com`).
5. **Sem baseline / controle negativo.** Nenhum braço "sem-Strata" (mede o *lift* do
   método) nem projeto limpo (mede falso-positivo). Sem isso, a alta detecção na nuvem
   pode ser **competência genérica**, não "aplicar o Strata".

## Furos de instrumento (ALTA/MÉDIA, re-pontuam tudo)

- **Dois scorers divergentes** ativos: legado por `id` (zeros artefatuais) vs revisão por
  seção. Escalas inconsistentes (0-1 vs 0-3). Trocar de scorer re-pontua todas as células.
- **Scorer de seção não-reprodutível**: mesmo input deu 1/2 e 2/2 em execuções diferentes.
- **P5 e P6 não-independentes**: ambos ancorados no mesmo "92%" → inflam a detecção /7.
- **Detecção da nuvem não verifica seção** (links corrompidos viram `knowledge-architecture.md`)
  mas o relatório afirma "seção certa em 17/18".
- **Juiz único Claude** julgando modelos Claude (Haiku 7/7 é a âncora do claim do recipe);
  2º juiz e cegueira real nunca rodaram (cegueira era só nominal — nome no arquivo).
- **N=1** em quase tudo; variância (qwen3:8b 7.5 vs 9.0) ≈ ordem dos deltas pequenos.

## O que SOBREVIVE ao reteste (direção, não número)

- Efeito **qualitativo grande** AN→§6-bis no local (deepseek 0→4) excede o ruído de N=1 —
  **com asterisco** (leakage + comprimento).
- **"A nuvem detecta os sintomas óbvios"** por redundância de 7+ modelos — a direção
  resiste a uma célula ruim/juiz leniente.
- **P6 (sem-fonte) como ponto cego universal** — convergente em todas as rodadas.
- A **honestidade do próprio projeto** (RASTREAMENTO, comprovação-forte, READMEs que
  hedgam) + a **segurança read-only** do runner + a correção do artefato do qwen3:4b.

## Plano de reteste (R0–R9)

**R0+R1+R2 são a fundação e têm que ser feitos JUNTOS** (são raízes transversais — refazer
só uma cria células não-comparáveis com as outras):

| # | Reteste | Prioridade | Afeta |
|---|---|---|---|
| **R0** | **Congelar o fixture bugado** (re-instanciar 0.70/0.85, fail-open, `velho/` real, `tarefas.txt` inerte) num path imutável com **hash**, separado do produto corrigido | ALTA | re-pontua TODO o arco |
| **R1** | **Descontaminar o H-C** — AN com CHECKs **abstratos** (sem citar os fixtures) OU cenário novo não-vazado; re-rodar o A/B | ALTA | hc-ab + piso inteiros |
| **R2** | **Tirar o enum do prompt** + **scorer único** canônico (detection 7 + flags binárias P6/P7/N1/N2); re-pontuar todos os raw; hash do scorer+manifesto na saída | ALTA | todas as colunas det/TOTAL |
| R3 | **Baseline + controle negativo** (sem-Strata; projeto limpo) | ALTA | o claim "a IA aplica" |
| R4 | **3º braço prosa-curta** (desconfundir comprimento×gate) | MÉDIA | veredito H-C / gate-semântico |
| R5 | **N≥3 (nuvem/hc-ab), N≥5 (piso)** + auditar os 21 `.ERROR.txt` do piso | MÉDIA | deltas pequenos; piso 8B |
| R6 | **2º juiz** (não-Claude) + cegueira real (chaves opacas) | MÉDIA | célula Haiku → claim do recipe |
| R7 | **Ligar o sandbox aos achados** (corrigir/RECUSAR de fato, não auto-relato regex) | MÉDIA | pilar "realmente faria" |
| R8 | **Validade ecológica**: ≥3 projetos reais, ≥3 cenários | BAIXA | claim de produto |
| R9 | Consertar instrumentos pontuais (s04 ref. quebrada; gate priority largo; unidade de alucinação) | BAIXA | métricas isoladas |

Falta também um **índice canônico** (rodada→célula→scorer→canal→raw) para permitir
**regressão seletiva** — hoje retestar uma célula exige re-rodar tudo.

## Conclusão

O arco H-B/H-C estava **promissor mas não fechado**, e a auditoria mostra que vários
"fechamentos" repousavam em fixture-derivado-pós-teste, documento contaminado, prompt
vazado, juiz único e N=1. **Próximo passo real:** rebaixar as alegações publicadas para o
claim honesto acima, e refazer a fundação (R0+R1+R2) antes de qualquer novo veredito.
