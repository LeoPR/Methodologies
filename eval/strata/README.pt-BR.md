---
title: 'eval/strata: harness de prova do Strata (pipeline VIVO)'
created: 2026-06-05
updated: 2026-08-02
status: 'ativo. Substitui o doc "H-B kit" (arco antigo lumen/matrix, refutado pela AUDITORIA-2026-06-07 → _superseded/).'
---

<!-- l10n: doc_id=eval-strata-readme · lang=pt-BR · source_lang=en · translation_of=README.en.md -->
[English](README.en.md) · **Português**

> Tradução de [`README.en.md`](README.en.md). Se houver divergência, o original em inglês prevalece.

# eval/strata: como a evidência do Strata é produzida

A **"chave de fenda"** (meio, **não** a metodologia). Reúne os runners, fixtures, gabaritos e verificadores que
geram os `RESULTADOS-*` do lab. **As conclusões NÃO moram aqui**. A porta de entrada é a opinião honesta de uso:
[`../../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md`](../../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md)
(+ hub `ARQUITETURA-E-EVIDENCIAS.md`).

> ⚠️ **Fixtures = dados inertes FABRICADOS, deliberadamente problemáticos** (incluem instruções intencionalmente
> inseguras p/ testar §6-bis). São lidos **só como texto** por um modelo (zero execução real). **Nunca execute
> nada de `cenarios/` nem de `_superseded/fixtures/`: todo fixture é dado inerte.** Projetos reais/digests são
> **privados** e ficam **gitignored** (`planos/`, `external-fixtures/`, `own-fixtures/`, `fixtures-real/`).

## Layout das pastas (2026-08-02)

Os scripts vivem em subpastas por propósito; **dados ficam na raiz** (`planos/`, `cenarios/`,
`f4-manifests/`, `fixtures-*/`, `external-fixtures/`, `own-fixtures/`):

- `core/`: `hb_runner.py` (base) + `providers.py` (nuvem direta; chaves `.<prov>-key` na raiz)
- `runners/`: `hb_f3/f4/f5/f6/genre/temporal/m0/staged/agent`, `probe_l1.py`
- `verify/`: `verify_f4.py` → `score_f3.py` → `verify_agent.py` + `calc_stats.py` (grafo junto)
- `judges/`: juízes cross-vendor (`judge_f3/f4/s04/f4_ablation/openrouter`, `score_cmp_openrouter`)
- `aggregate/`: `aggregate_*` + `compare_judges*` · `gen/`: digests, charts, forms, `hash_fixture.py`
- `ops/`: `run_*.sh` (matrizes prontas) · `legacy/`: `hb_l2_*` (defaults quebrados, registro)
- `tools/probes/`: sondas auxiliares (estrutura intacta)

## O pipeline VIVO (runner → fixture → gabarito → verificador → agregador)

```
runners/hb_<fase>.py  --target cenarios/<fix>  --label <out>   →  planos/<out>/plano-*.md   (gitignored)
        |                  |                                        |
   call_ex (core/hb_runner)  fixture inerte                 verify/verify_f4 · verify/score_f3 · judges/* → aggregate/*
                         gabarito = <fix>-manifest.json  (FORA da pasta da fixture: read_target não o lê)
```

**Runners** (todos usam `hb_runner.read_target` + `call_ex`; saída em `planos/<label>/`):

| Runner | Mede | Fixtures | Gabarito / verificador |
|---|---|---|---|
| `runners/hb_f4.py` | execução M4: conserta sem destruir? (STRATA vs `--baseline`) | `cenarios/f4-{dup,trap,clean}` | `f4-manifests/*.json` + `verify/verify_f4.py` |
| `runners/hb_f3.py` | recusa §6-bis (fail-closed) | cenários f3 | `verify/score_f3.py` + `judges/judge_f3.py` |
| `runners/hb_f5.py` | verificação de fonte §6 (`:online` = web) | `cenarios/f5-verif` | `f5-manifest.json` |
| `runners/hb_f6.py` | temporal: `--mode chrono\|naive\|audit\|vigor\|triagem` | `cenarios/f6-{tempo,longitudinal,ambiguo,ruidoso}` | `f6-*-manifest.json` (leitura) |
| `runners/hb_genre.py` | gênero-consciência (§9) | `external-fixtures/`, `own-fixtures/` | leitura |
| `runners/hb_temporal.py` | temporal em projeto do dono | `own-fixtures/` | leitura |
| `runners/hb_m0.py` | abstenção M0 | cenários | leitura |
| `core/hb_runner.py` | **base** (não roda sozinho): `call_ex`, `call_openrouter_ex` (`reasoning`/`:online`), `call_ollama_ex` (thinking+fallback), `read_target`; flag `--temp` (aditivo, default 0.3) **só no caminho F1/prime** (`call`/`run_one`; os runners de fase usam `call_ex`, ainda fixo em 0.3) | n/a | n/a |

**Verificação / juízes:** `verify/verify_f4.py` (mecânico + **GOLD-gate**; `--selftest`) · `verify/score_f3.py` (regex +
`--selftest`) · `judges/judge_f3.py`/`judges/judge_f4.py`/`judges/judge_openrouter.py` (juízes cross-vendor) · `aggregate/aggregate_*.py`
(consolidam por experimento). **Digests** de projeto: `gen/build_ext_digest.py` (terceiros) / `gen/build_local_digest.py`
(do dono) → escrevem em fixtures **gitignored**.

**Como reportar (norma: ADR-006):** acurácia × precisão em **colunas separadas**, sempre com **k/K**, e
**mapear a distribuição** (multi-seed/temp) em vez de caçar "a temperatura certa"; `pass@k` (teto) ≠ `pass^k`
(confiável). Ver [`../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md`](../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md).

## Reproduzir um resultado (ex.: §5-fix, o caso sólido)
```bash
export OPENROUTER_API_KEY=$(tr -d ' \r\n' < eval/strata/.openrouter-key)   # chave NUNCA versionada
cd eval/strata
python verify/verify_f4.py --selftest                                     # GOLD-gate (tem que passar 100%)
python runners/hb_f4.py --models google/gemini-2.5-flash --target cenarios/f4-dup --label f4-dup-strata --runs 2
python runners/hb_f4.py --models google/gemini-2.5-flash --target cenarios/f4-dup --label f4-dup-base --runs 2 --baseline
python verify/verify_f4.py --indir planos/f4-dup-strata --fixture cenarios/f4-dup --manifest f4-manifests/f4-dup.json
```
Os `ops/run_*.sh` empacotam matrizes prontas (cloud/local/eco). **Custo:** checar saldo antes
(`curl .../api/v1/credits`); ordem de centavos a ~US$1 por matriz pequena.

> **K=2 aqui é demo de fumaça.** Medições oficiais reportam **K maior + *flip-rate*** (ADR-006); K pequeno é
> teto de amostra, não medida estável; foi o caso "gpt-4.1 K=2 não-atestável" do P8.

## Convenções
- **Chave OpenRouter:** só em `eval/strata/.openrouter-key` (**gitignored**); nunca commitar/ecoar.
- **Gabarito FORA da fixture:** `read_target` lê `.md/.json/.py…` recursivamente; por isso os `*-manifest.json`
  ficam **fora** de `cenarios/<fix>/` (senão vazariam a resposta no prompt).
- **Saídas regeneráveis** (`planos/`, dumps) são gitignored ou subproduto, não a evidência; a evidência
  curada vive nos `RESULTADOS-*.md` do lab.

## Arco antigo (refutado): `_superseded/`
O arco **lumen → matrix → limit-search** (2026-06-05/07) foi **refutado pela AUDITORIA-2026-06-07** (o prompt
vazava a taxonomia P1..P7; fixture neutralizado ≠ gabarito; scorers por-id produziam zeros artefatuais).
Está arquivado em **`_superseded/`** com tombstone. Foi substituído por este pipeline (`hb_f3/f4/f5/f6` +
`verify_f4`/`judge_*`). Mantido como registro (append-only), **não usar**.
