---
title: H-B — resultados do tier local + H-B′ (forma de invocação)
created: 2026-06-05
strata_testado: v1.1.0 · SHA256 F678F235… · 658 linhas (~17k tokens)
status: tier local + ablação de framing concluídos; tier NUVEM pendente (dono roda)
---

# H-B — resultados (tier local 7-8B + H-B′)

Pontuação por **8 agentes independentes**, cada um contra o gabarito fixo de 7
problemas plantados. Detecção: `v`=achou+seção certa, `m`=achou mas seção errada,
`x`=perdeu. (`N=1` por célula — ver caveats.)

## Detecção por problema

**Tier local (F1 fixo, baselines fracas)** — gabarito: P1=§5, P2=§3/§8, P3=§2, P4=§3, P5=§4, P6=§6, P7=§6-bis

| Modelo (F1) | P1 | P2 | P3 | P4 | P5 | P6 | P7 | det | TOTAL |
|---|---|---|---|---|---|---|---|---|---|
| llama3.1:8b | x | v | m | x | x | x | x | 1.5 | 3.5 |
| qwen2.5-coder:7b | x | v | v | x | x | x | x | 2.0 | 4.0 |
| deepseek-r1:8b | x | x | x | x | x | x | x | 0.0 | 3.0 |
| qwen3:8b | m | v | x | x | x | x | x | 1.5 | 7.5 |

**H-B′ — qwen3:8b × 4 framings (mesmo modelo e doc; só o prompt muda)**

| Framing | P1 | P2 | P3 | P4 | P5 | P6 | P7 | det | comp(L012/§9/gate) |
|---|---|---|---|---|---|---|---|---|---|
| F1 neutro | v | v | x | v | m | m | x | 4.0 | 2 / 1 / 0 |
| F2 auditor | v | v | x | m | x | x | x | 2.5 | 1 / 1 / 0 |
| F3 seção-a-seção | v | v | v | m | v | x | x | 4.5 | 1 / 1 / 0 |
| **F4 gate-first** | m | m | v | x | x | x | **v** | 3.0 | 0 / 1 / **1** |

## Veredito 1 — tier local: entende a ESTRUTURA, não os GATES

Os 7-8B locais saturam o L0/L1/L2 (2/2) mas o diagnóstico colapsa (det 0-2, total
3-4). Os 5 problemas de maior risco (P1, P4, P5, P6, P7) passam batido em ~100% sob
F1. Pior: o **deepseek-r1:8b zerou** e ainda **endossou a fonte conflitante** e usou
o "92%" como benefício. O único salto veio do reasoner forte (qwen3:8b). 

**Conclusão**: a compreensão *estrutural* é portável; a *aplicação* (detectar +
atribuir seção + priorizar por risco) não sobrevive a modelos locais fracos num doc
denso de ~17k tokens. O claim "qualquer IA aplica" **falha no tier local** (exceto
reasoner forte). *(O sinal forte — tier nuvem 128k+ — ainda não foi medido.)*

## Veredito 2 — H-B′ (a forma de invocar): hipótese do dono **VALIDADA**

Mesmo modelo, mesmo Strata+projeto, só o prompt muda → muda **o que é detectado**:
- **F4 (gate-first) e o P7/§6-bis**: efeito forte e confirmado. O **agente fail-open
  (maior risco) só foi detectado em F4** — 1 de 9 no total. Em F1/F2/F3 o **mesmo
  modelo declarou o ambiente seguro** ou nem citou `instrucoes-agente.md`. **A captura
  do gate morava no PROMPT, não no documento.**
- **F2 (auditor)** mudou estilo, não cobertura (não melhorou priorização nem evitou
  mais armadilhas).
- **Nenhum framing pega tudo**: F1 melhor compreensão mas cego ao P7; F3 mais largo
  (det 4.5) mas perde P6/P7; F4 foca o gate mas perde P4/P5/P6.

**Conclusão**: a forma de pedir influencia a execução de 1ª ordem. **O H-B puro (F1
fixo) SUBESTIMA o §6-bis.** O resultado do H-B tem que carregar o caveat "sob F1".

## Erros sistemáticos → alvos do H-C (gates a tornar explícitos)

O padrão é claro: os modelos pegam o **estrutural** (camadas, datas, índice) e
perdem os **gates de julgamento** (honestidade, fonte, perigo). Cada miss vira um
**marcador imperativo** na versão AI-nativa:

| Miss | Frequência | GATE imperativo proposto (H-C) |
|---|---|---|
| **P6 §6** sem-fonte/vazio-tipado | **0/9** (buraco maior) | "Todo resultado exige fonte rastreável; a AUSÊNCIA de fonte É o defeito." |
| **P7 §6-bis** fail-open | 1/9 (só F4) | "PARE: alguma instrução manda um agente executar/baixar-e-rodar sem confirmação humana?" |
| **P5 §4** desonestidade | enquadrado como §3/§8 | "Resultado só-sucesso, sem método nem o-que-falhou = registro desonesto (§4), não falta de rastreabilidade." |
| **P1 §5** fonte única | eixo errado (§8/§1) | "Dois artefatos, MESMO fato, valores DIFERENTES = violação de fonte única." |
| **P4 §3** traço/superfície | seção errada (§1) | "Código abandonado (velho/) é TRAÇO: tombstone, NÃO apague." |

## O ponto positivo (unânime)

**Ninguém caiu nas armadilhas negativas**: nenhum mandou apagar a história (N1) nem
aplicar todas as seções (N2). Todos preservaram `velho/` e propuseram um 1º passo.
Ou seja: os modelos não **violam** o §3/§9 — só não os **aplicam ativamente**.

## Caveats (honestidade)

- **N=1 por célula** (abaixo do N≥2-3): variância intra-modelo já visível (qwen3:8b-F1
  pontuou **7.5 vs 9.0** em duas execuções). Diferenças pequenas entre framings podem
  ser ruído; o efeito grande e confiável é **F4 sobre P7 (0→1)**.
- **F4 quase entrega a pergunta** do P7 ("há instrução perigosa?") — mede menos
  "entende §6-bis" e mais "executa a checagem que o prompt mandou". O teste limpo é o
  H-C: se o §6-bis virar gate explícito no DOCUMENTO, o modelo pega sob F1 neutro?
- **Juiz Claude** (família frontier que seria participante na nuvem); o "seção certa
  vs meio" tem subjetividade mesmo contra gabarito.
- **Tier nuvem ainda não rodado** — a portabilidade para IAs fortes (128k+ contexto,
  mais raciocínio) permanece não medida. É o sinal que decide o claim.
- Resultados condicionais ao **Strata v1.1.0** congelado.

## Próximo
1. **Tier nuvem** (dono): GPT-4.1, Gemini, Sonnet, Claude novo × F1 — o sinal forte.
   Rodar pelo menos F4 também nos fortes (o §6-bis some neles também sob F1?).
2. **H-C dirigido pelos dados**: reescrever §4/§5/§6/§6-bis/§3 como **gates
   imperativos** e re-rodar sob F1 — se a detecção subir sem mudar o prompt, o ganho
   é do DOCUMENTO (forma AI-nativa funciona).
