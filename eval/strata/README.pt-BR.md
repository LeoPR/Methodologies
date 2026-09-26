---
title: 'eval/strata: harness de prova do Strata (pipeline VIVO)'
created: 2026-06-05
updated: 2026-09-26
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

- `core/`: `hb_runner.py` (base) + `providers.py` (nuvem direta e `ollama` local, pelo mesmo caminho
  para local e nuvem serem comparáveis; chaves `.<prov>-key` na raiz)
- `runners/`: `hb_f3/f4/f5/f6/genre/temporal/m0/staged/agent`, `probe_l1.py`
- `verify/`: `verify_f4.py` → `score_f3.py` → `verify_agent.py` + `calc_stats.py` (grafo junto)
- `judges/`: juízes cross-vendor (`judge_f3/f4/s04/f4_ablation/openrouter`, `score_cmp_openrouter`);
  `bench_juiz.py` escolhe juiz por acerto × custo × latência, com portão de virada (o veredito tem de
  mudar quando só a autorização muda) e portão marcador (alegação falsa que o juiz carimbador confirma)
- `aggregate/`: `aggregate_*` + `compare_judges*` · `gen/`: digests, charts, forms, `hash_fixture.py`,
  `build_nc_repo.py` (controle negativo em escala de repositório: planta 5 defeitos L0 + 1 item
  negativo numa cópia deste repo; gabarito e primeiro resultado em `nc-manifest.json`)
- `ops/`: `run_*.sh` (matrizes prontas); `bank_run.py` (banco de capacidades por modelo: conserto →
  armadilha → abstenção, para no conserto; erro de provedor é INFRA, nunca "não atende") ·
  `legacy/`: `hb_l2_*` (defaults quebrados, registro)
- `aggregate/aggregate_bank.py` (tabela do banco por rota) · `verify/score_f5.py` (pontuador F5, gate
  GOLD; `cenarios/f5-recente` = afirmações cuja verdade mudou em 2024-2026, para medir busca na web)
- `runners/hb_f4.py --reasoning off|low|medium|high` (eixo de raciocínio explícito; o cabeçalho
  registra o nível, o custo real do provedor e os tokens de raciocínio)
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
| `runners/hb_f4.py` | execução M4: conserta sem destruir? (STRATA vs `--baseline`) | `cenarios/f4-{dup,trap,clean,clean-v2}` | `f4-manifests/*.json` + `verify/verify_f4.py` |
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

**"Local" é questão de pesos, não de onde roda.** A capacidade de um modelo se mede na nuvem, nos
mesmos pesos (barato, rápido); a máquina local mede só viabilidade (cabe? a que velocidade?) e é a
contra-prova numa ponte de 1–2 células rodadas nos dois lados nas mesmas condições (inclusive o nível
de raciocínio). Sem hospedagem na nuvem, um resultado local vale só para aquela quantização. Decisão
do dono de 2026-08-02 (`../../lab/2026-08-02-reteste-L0-fechado/PLANO.md` §3-bis); encaixe por placa
em `../../lab/2026-06-04-economia-ia-tokens/instrumento/STAGE5.md`.

**A temperatura não é uniforme entre modelos: declare.** Os runners pedem `temperature=0.3` a
todo modelo. Alguns não aceitam o parâmetro (linhas de raciocínio como `gpt-5`, `gpt-5-mini`,
`gpt-5.6-*`, `claude-sonnet-5`, `claude-fable-5`); o OpenRouter o descarta em silêncio e eles
rodam no default do fabricante. O cabeçalho do plano não registra a temperatura efetiva. As
comparações entre modelos misturam, portanto, dois regimes; pela ADR-006 o default de cada modelo
é o seu regime de uso, então é fator a declarar, não erro a corrigir varrendo. Confira um modelo
pelo `supported_parameters` em `https://openrouter.ai/api/v1/models` (a lista muda; a de cima foi
lida em 2026-09-26, e o estado de agosto não é recuperável).

**Antes de uma série nova num fixture:** confira que o fixture não afirma o veredito do gabarito
(ver "Sem atalho" em [`cenarios/README.md`](cenarios/README.md)) e conte o poder: célula presa no
piso, no teto ou em "indeterminado" não carrega informação sobre o efeito.

## Reproduzir um resultado (ex.: §5-fix, o caso sólido)
```bash
export OPENROUTER_API_KEY=$(tr -d ' \r\n' < eval/strata/.openrouter-key)   # chave NUNCA versionada
cd eval/strata
python verify/verify_f4.py --selftest                                     # GOLD-gate (tem que passar 100%)
python runners/hb_f4.py --models google/gemini-2.5-flash --target cenarios/f4-dup --label f4-dup-strata --runs 2
python runners/hb_f4.py --models google/gemini-2.5-flash --target cenarios/f4-dup --label f4-dup-base --runs 2 --baseline

# A/B de VERSAO do metodo (--strata aponta um doc alternativo; o SHA do TEXTO injetado vai
# p/ o header do plano como method_sha, entao as duas metades ficam distinguiveis no traco).
python runners/hb_f4.py --models gpt-oss-120b --provider cerebras --target cenarios/f4-clean-v2 \
  --label s9-v121 --runs 3 --strata /caminho/knowledge-architecture-v1.2.1.pt-BR.md
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
