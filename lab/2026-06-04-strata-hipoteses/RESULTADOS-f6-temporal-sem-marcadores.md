---
title: 'RESULTADOS — F6: inferir cronologia SEM marcadores (8/8 PASS) — DISCONFIRMA em parte o ponto-cego temporal'
created: 2026-06-13
status: 'probe (3 fixtures sintéticas endurecidas por red-team, 2 modelos baratos). F6-tempo 8/8 + F6-longitudinal 4/4 + F6-abstenção 4/4. Sinal DISCONFIRMADOR do "ponto-cego temporal fundamental".'
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

## Refino da tese (atualiza o dossiê)
A fraqueza temporal medida antes (P4 ~33%, R8) é **menos** "não consegue inferir tempo" e **mais** "depende
de a evidência estar **presente e legível**". Inversão útil p/ o Strata: **§3/§8 (história legível e
rastreável) fornecem exatamente a evidência que deixa um modelo capaz situar o tempo** — o método torna o
tempo **inferível**; não conserta um modelo incapaz, mas remove a ambiguidade que o trava. **Rebaixa de novo**
a hipótese "ponto-cego temporal fundamental": vira "ponto-cego **condicional à legibilidade da evidência**".
*(Direção, não prova — N=1.)*
