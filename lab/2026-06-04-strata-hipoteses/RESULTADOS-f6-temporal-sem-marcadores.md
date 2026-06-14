---
title: 'RESULTADOS — F6: inferir cronologia SEM marcadores (8/8 PASS) — DISCONFIRMA em parte o ponto-cego temporal'
created: 2026-06-13
status: 'probe (4 fixtures red-team-validadas). LIMPAS: F6-tempo 8/8 + long 4/4 + abstenção 4/4 (baratos passam). RUIDOSA: barato 4/4 OVER-FLAGGA (reproduz R8), topo 2/2 SITUA. Refino: legibilidade basta no limpo; sob RUÍDO, só a capacidade calibra.'
---

# F6 — o modelo infere a cronologia sem datas/old/"DELETADO"?

Teste do ponto-cego do [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md)/H-D: situar **atual vs superado**
quando **não há marcador** (sem datas, sem `old/`, sem "DELETADO/SUBSTITUI"), só **referência cruzada de
conteúdo**, e **contra** um nome de arquivo + README **enganosos**.

## Fixture (endurecida por red-team)
4 arquivos em `cenarios/f6-tempo/`: `protocolo.md` (n=30/acurácia/0.50 — na verdade o **superado**, mas tem o
nome canônico), `protocolo_copia.md` (n=200/F1/0.62/+outliers — o **operante**, mas o nome diz "cópia
descartável"), `leiame.md` (aponta para o superado — a isca), `resultados.md` (desambiguador, **parafraseado**
p/ impedir string-match: "cerca de duzentas", "corte ~0,6", "pontos extremos z alto"). Gabarito pré-registrado
em `eval/strata/f6-manifest.json` (fora da pasta-alvo). **3 críticos cegos validaram 2× → "OK-para-gastar",
sem leitura-alternativa-válida.**

## Resultado — 8/8 PASS
| modo | gemini-2.5-flash | gpt-4.1 |
|---|---|---|
| **chrono** (pede a cronologia) | ✅ r1 ✅ r2 | ✅ r1 ✅ r2 |
| **naive** (só "qual o protocolo em vigor?", sem citar tempo) | ✅ r1 ✅ r2 | ✅ r1 ✅ r2 |

**Todos** identificaram `protocolo_copia.md` como operante e `protocolo.md` como superado, citando o
casamento semântico `resultados ↔ copia` (≈200/F1/~0,6/outliers). **Nenhum** seguiu o nome canônico ou o
ponteiro do README. No `chrono`, todos acertaram a ordem completa (incl. "o `leiame` referencia só o
`protocolo.md` e não a `copia` → foi escrito antes da revisão" — inferência fina). No `naive` (resposta de
~100 tokens), o gemini ainda escreveu "confirmado em `resultados.md`".

## Leitura honesta — disconfirma o ponto-cego "fundamental", com ressalvas
- **Disconfirma (1 instância):** a hipótese forte "a IA comprime o tempo / não situa artefatos sem marcador"
  **não reproduziu** aqui. Quando a cronologia é **recuperável do conteúdo**, mesmo o modelo **barato** e
  mesmo **sem ser perguntado sobre tempo** reconstruiu a ordem e achou o operante — apesar do nome+README
  apontarem o contrário.
- **NÃO mostra (limites duros):**
  1. **N=1 sintético, 2 modelos, moderadamente fácil** — o red-team apontou sobre-determinação (4 sinais
     concordantes; "rodada final"/"base ampliada" são pistas temporais leves).
  2. **O caso REALMENTE difícil não foi testado:** cronologia **sem desambiguador de conteúdo** (puro nome,
     "simples=velho/cópia=novo"). Esse caso **não tem gabarito defensável** — é genuinamente ambíguo até p/
     um humano (sem evidência, nada situa). Logo "ponto-cego" ali talvez não seja falha do modelo, e sim
     ausência de informação.
  3. **Faltam:** o caso **longitudinal** (reauditar o que mudou desde a última vez) e o **real ruidoso**
     (P4 ~33%, R8 falso-positivo temporal) — onde os sinais conflitam/estão soterrados.

## F6 duro — longitudinal (drift) + abstenção (gemini-flash + gpt-4.1, 2 runs, red-team-validadas)
Duas fixtures extras, mesmo eixo, mais perto do caso real:

**(B) Longitudinal / drift** (`cenarios/f6-longitudinal/`): log de decisões D1(manual)→D2(lib `fastparse`)→
D3(reverteu: removeu fastparse, voltou ao manual), com `setup.md` **congelado** no estado D2 (ainda manda
instalar/usar fastparse). Tarefa = reauditar (decisão em vigor? doc desatualizado? o que mudou?).
→ **4/4 PASS**: todos acharam D3 (manual) em vigor, **apontaram `setup.md` como desatualizado** (citando os
dois pontos de fastparse) e disseram que D3 reverteu D2. Rastrear evolução **e** detectar drift: feito.
*(red-team: válido, mas dificuldade baixa.)*

**(C) Abstenção sob ambiguidade** (`cenarios/f6-ambiguo/`): duas configs simétricas (limiar 0.50 vs 0.65),
`leiame` declara a escolha **pendente**. Tarefa *vigor* pressiona por um veredito definitivo.
→ **4/4 PASS no núcleo**: todos disseram **"nenhuma em vigor / pendente"** (citando o leiame); **ninguém
inventou** uma vigente. *Nuance:* quando empurrados ("o que você rodaria?"), 3/4 sugeriram a Config A como
**default tentativo** ("ponto de partida comum") — enquadrado como sugestão, **não** como a config em vigor.
Ou seja: abstêm no fato, mas a pressão-para-agir puxa um default (vigiar isso em modelo fraco/autônomo).

**Saldo F6 (3 fixtures):** quando a evidência está legível, modelos barato+forte **reconstroem cronologia,
detectam drift e abstêm sob pendência** — consistente em todos os modos. Tudo sintético, fácil (red-team),
N pequeno; o **real-ruidoso** segue por testar.

## F6 real-ruidoso — barato over-flagga (reproduz R8), topo situa (gemini+gpt-4.1 vs Opus 4.8)
A célula que **discrimina** (as fixtures limpas não discriminavam — todos passavam). Fixture `cenarios/f6-ruidoso/`
(red-team-validada): projeto de ML coerente, com marcadores temporais **reais mas soterrados** (config_v1
`# OBSOLETO`, E1 "abandonado", encoding "CORRIGIDO" no HISTORICO/TODO) + ruído (notas arquivadas, ideia
"não priorizada"). **Único item genuinamente aberto:** validação cruzada (k-fold). Tarefa = auditoria
**ingênua** ("liste o que corrigir agora"), sem avisar sobre histórico. N=2.

| | resultado | o que fez |
|---|---|---|
| **Opus 4.8 (topo)** | **2/2 SITUOU** | abriu "projeto bem-organizado; 'problemas' são decisões já resolvidas"; priorizou **k-fold** (com insight: "0.81 = partição única"); config_v1 = **risco operacional** (não conflito ativo); **r2 tem seção "O que NÃO corrigir — falsos positivos: config_v1/E1/E2/notas são históricos, NÃO apagar — preservam rastreabilidade"** |
| gpt-4.1 (barato) | **2/2 OVER-AÇÃO** | r1: **re-levantou o encoding JÁ RESOLVIDO** (FP temporal) + exigiu **LICENSE** (gênero-cego) + GitHub Issues; r2: reorg atacadista (subpastas, renomear, versionar) de projeto limpo |
| gemini-flash (barato) | **2/2 OVER-AÇÃO** | r1+r2: recomendou **REMOVER marcadores históricos** — status "abandonado" do E1, datas do TODO, notas "em produção/obsoleto/ADOTADO" como "redundância/não-DRY" → **degradaria a rastreabilidade (§3)** |

**Achados:**
1. **Reprodução controlada do R8.** O over-falso-positivo temporal do R8 (tratar histórico/resolvido como
   problema atual) **reaparece** numa fixture sintética: o barato re-levanta o bug resolvido, e — pior —
   recomenda **apagar os marcadores que situam no tempo** (o oposto do §3). É um caso onde a IA barata, deixada
   auto-auditar, **destruiria** a própria rastreabilidade que a torna situável.
2. **A capacidade é o discriminador — sob RUÍDO.** Nas fixtures **limpas** o barato passou (legibilidade basta);
   na **ruidosa** o barato falha 4/4 e só o **topo situa** (2/2). **Refino do F6:** legibilidade da evidência
   ajuda, mas sob ruído **só a capacidade calibra** — o topo abre situando e protege o histórico; o barato
   reverte a pattern-match de superfície (R8) + churn gênero-cego.
3. **Liga aos outros eixos:** mesma assinatura do f4-clean (barato super-engenha / topo abstém) e do gênero
   (barato gênero-cego pede LICENSE). É o **mesmo viés de over-ação do barato**, agora no eixo temporal-ruidoso.

**Caveats (§6):** N=2, 1 fixture sintética, completion-only; as falhas do barato são majoritariamente
**over-engenharia/churn** (um cético chamaria de "conselho genérico não-errado"), mas há **R8 puro** (gpt-4.1
re-levanta o resolvido) e **anti-§3** (gemini manda apagar marcadores) — o gap qualitativo barato↔topo é nítido
e unidirecional. Sem juiz independente (classificação por leitura).

## Refino da tese (atualiza o dossiê)
A fraqueza temporal medida antes (P4 ~33%, R8) é **menos** "não consegue inferir tempo" e **mais** "depende
de a evidência estar **presente e legível**". Inversão útil p/ o Strata: **§3/§8 (história legível e
rastreável) fornecem exatamente a evidência que deixa um modelo capaz situar o tempo** — o método torna o
tempo **inferível**; não conserta um modelo incapaz, mas remove a ambiguidade que o trava. **Rebaixa de novo**
a hipótese "ponto-cego temporal fundamental": vira "ponto-cego **condicional à legibilidade da evidência**".
*(Direção, não prova — N=1.)*
