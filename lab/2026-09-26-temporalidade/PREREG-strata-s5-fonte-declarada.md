---
title: 'Pré-registro: o acréscimo "Fonte declarada ≠ fonte usada" (Strata §5) faz o leitor seguir a evidência de uso sem desconfiar de declaração certa?'
created: 2026-09-29
updated: 2026-09-29
status: 'Pré-registrado antes de qualquer rodada. Fixtures congeladas por hash; pontuador v4.1 depois do red-team (seção 8).'
tags: [strata, s5, pre-registro, a-b, f6-fonte]
---

# Pré-registro: "Fonte declarada ≠ fonte usada" (Strata §5)

## 1. Pergunta

O acréscimo ao §5 ([proposta](PROPOSTA-S5-fonte-declarada.md)) faz o leitor, ao reproduzir um
resultado, usar a fonte que os traços mostram que foi usada, e não a que um leia-me declara, **sem**
passar a desconfiar de uma declaração que os traços confirmam ou que nada contradiz?

Conferência do núcleo (2026-09-29): §3 (inclusive "Ler o tempo de volta", v1.2.7), §3-bis
(probatório × dispositivo), §5 inteiro, §6, início do §6-bis, §9 (avisar à toa é excesso).

## 2. Braços

| braço | prompt |
|---|---|
| SEM | documentos + tarefa, sem metodologia |
| S127 | canônico PT v1.2.7 + documentos + tarefa |
| S128 | idem, com o delta `eval/strata/variantes/s5-fonte-declarada.pt.md` inserido no §5 (antes de `> **Fundamentação**: fonte única (weave/tangle)`) em tempo de execução |

O `recipe/` não muda antes do resultado. Cada saída registra o `method_sha`.

## 3. Fixtures e gabarito (`eval/strata/f6-status-manifest.json`, família "fonte")

Tarefa: reproduzir; as duas últimas linhas são `PARÂMETROS:` e `ORIGEM:`. A escolha do leitor sai
da **assinatura dos valores** em PARÂMETROS; citação ou negação da outra fonte não conta como
escolha; os nomes em ORIGEM só desempatam quando não há valores. Fixtures congeladas por
`.fixture-hash`.

| chave | papel | situação | acerto | parcial | falha |
|---|---|---|---|---|---|
| `f6-tempo-s5` (pasta `f6-tempo`) | alvo | leia-me declara `protocolo.md`; resultados têm os traços da cópia | parâmetros da cópia (citar a declaração ao lado é permitido) | cópia + "indeterminado" | declarada; os dois sem escolha; só "indeterminado" |
| `f6-fonte-nova` | alvo fora da amostra (padaria) | leia-me declara `receita.md`; o registro tem os traços de `receita_teste.md` | parâmetros do teste | idem | idem |
| `f6-tempo-inverso` | controle | leia-me declara `protocolo.md`; resultados têm os traços dele; cópia divergente, não usada, sem data | parâmetros de `protocolo.md` sem ressalva sobre a escolha | com ressalva sobre a escolha | cópia; os dois; só "indeterminado" |
| `f6-tempo-sem-traco` | controle ("vale por padrão") | leia-me declara `protocolo.md`; resultados não discriminam | idem | idem | idem |
| `f6-fonte-nova-inverso` | controle fora da amostra | leia-me declara `receita.md`; o registro tem os traços dela | parâmetros de `receita.md` sem ressalva | idem | idem |
| `f6-sem-copia` | borda | resultados contradizem `protocolo.md`; não há outro protocolo | "indeterminado" ou reconstrução pelos resultados | declarada com ressalva; os dois | declarada sem ressalva |
| `f6-indeterminado` | regressão | como no teste do §3 (tarefa VIGENTE) | | | |

Nota sobre o controle: uma nota sobre a cópia não usada não é ressalva sobre a escolha.

Pontuador: `eval/strata/verify/score_f6s.py` v4.1. Sem as duas linhas: fora do denominador. Valor
que não casa, ou atribuição a arquivo inexistente: REVISAR, revisão manual cega ao braço,
registrada em `planos/<rodada>-revisao.csv` e transcrita no RESULTADOS.

## 4. Hipóteses

- **H1 (alvo):** em `f6-tempo-s5`, acerto S128 > S127; em especial, muse e deepseek (onde o defeito
  apareceu) saem de ERRA.
- **H1b (fora da amostra):** em `f6-fonte-nova`, acerto S128 ≥ S127 + 0,20. **Regra de teto:** se
  S127 ≥ 0,80, H1b fica "sem poder (teto)" e se lê por modelo, não como refutação.
- **H2 (controles, não inferioridade):** em cada controle (`f6-tempo-inverso`, `f6-tempo-sem-traco`,
  `f6-fonte-nova-inverso`), acerto S128 ≥ S127 − 0,10, e a taxa de ressalva (parcial) não sobe mais
  de 0,10. O `f6-tempo-sem-traco` é o que mede o risco principal do texto (desconfiar à toa quando
  nada contradiz a declaração).
- **H3 (regressão):** em `f6-indeterminado`, S128 ≥ S127 − 0,10.
- **Análise por modelo:** acerto conjunto alvo ∧ controle (`f6-tempo-s5` ∧ `f6-tempo-inverso`). No
  alvo, "o mais novo vence" e "siga os traços" apontam para a mesma resposta; só o par separa os dois.
- Descritivo: `f6-sem-copia` (borda) e SEM × S127 em todas.

## 5. Modelos e K

Os 8 do F6-status: pela NVIDIA grátis `openai/gpt-oss-20b`, `google/gemma-4-31b-it`,
`meta/muse-glimmer-30b`, `nvidia/nemotron-3-super-120b-a12b`, `z-ai/glm-5.3`,
`deepseek-ai/deepseek-v4.1-flash` (K = 3, fila lenta); pelo OpenRouter `openai/gpt-6-luna`,
`google/gemini-3.5-flash-lite`. K = 5. Braços intercalados por fixture. Temperatura 0,3 pela NVIDIA;
GPT-6 ignora temperatura. Raciocínio no padrão do modelo.

## 6. Decisão

1. **Controle ferido** (H2 violada em qualquer controle): o texto induz desconfiança; não adotar;
   revisar o texto.
2. **Alvos sobem** (H1, e H1b ou seu teto) **e controles intactos:** adotar no canônico com
   `[TESTED data: ...]`.
3. **Sem movimento, ou só no alvo original** (H1 sem H1b, fora do teto): ajuste à fixture; adotar
   só como norma editorial, por decisão do dono, sem alegação de efeito.
4. **Heterogêneo por fabricante:** relatar por fabricante.

Exploratório: n efetivo agrupado por modelo.

## 7. Relato

Acerto k/K e classe mais comum em colunas separadas (ADR-006); classes parciais à parte; negativo
registrado com o mesmo peso.

## 8. Red-team antes da rodada (2026-09-29)

Orquestração com 14 agentes: 2 resolvedores cegos por fixture (sem gabarito), 1 crítico por fixture
(com gabarito e pontuador), 2 agentes tentando quebrar o pontuador.

- **Fixtures:** os 4 críticos julgaram o gabarito defensável e sem vazamento; os 8 resolvedores
  cegos acertaram. Ajustes feitos: `f6-fonte-nova` com títulos idênticos e mesma ordem de arquivos
  do `f6-tempo` (`receita_teste.md`, `registro.md`); controles novos `f6-tempo-sem-traco` e
  `f6-fonte-nova-inverso`; "cópia velha" trocado por "divergente, não usada, sem data".
- **Pontuador:** o v4 tinha viés contra o braço S128 (citar a declaração ao lado virava LISTA-AMBOS;
  o marcador de inferência virava "indeterminado"; "sem ressalva" contava como ressalva; `2 h`
  casava dentro de `12 h`; "desvio-padrão" casava a assinatura do declarado; lista em várias linhas
  e rótulos em inglês se perdiam). O **v4.1** corrige: extração tolerante (rótulos EN, lista,
  travessão, cabeçalho, par ORIGEM/PARÂMETROS, guarda de cauda), citação e negação fora da contagem,
  corte no primeiro contraste, assinaturas ancoradas, negação de ressalva, nome negado não é escolha.
- **Validação do v4.1:** 139/139 em 5 conjuntos de casos (21 meus, 46 de formato, 44 de semântica,
  18 de controle retido, 10 de extração). As 339 saídas do teste do §3 mantêm a classe (sem
  regressão).
- Registros: `proposta-s5-orquestracao.json` (proposta) e `redteam-s5-fixtures-pontuador.json`
  (resolvedores cegos, críticos e red-team do pontuador). Protótipos e casos de teste ficam fora do repo.
