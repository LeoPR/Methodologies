---
title: Protótipo detect-and-recommend — ambiente IA do dev
created: 2026-06-04
status: funcional (rascunho); detecção tem 2 limitações conhecidas
relates: [../arvore-decisao.md, ../mapa-recursos-llm.md]
---

# Protótipo: detect_env.py

Detecta o ambiente do dev, classifica num arquétipo (A1-A6), e emite o que
**LIGAR AGORA / CONSIDERAR / está BLOQUEADO (com a causa)**, mais um
`environment-profile.yaml` legível-por-agente. É o rascunho executável da
árvore de decisão (`../arvore-decisao.md`).

## Uso

```powershell
$py = "..\..\..\.venv\Scripts\python.exe"
& $py detect_env.py                      # detecta esta máquina
& $py detect_env.py --goal economia      # fixa a prioridade (cobertor curto)
& $py detect_env.py --emit-profile       # grava .ai/environment-profile.yaml
& $py detect_env.py --json               # só o ambiente detectado (JSON)
& $py detect_env.py --simulate perfil.json --goal qualidade   # TEORIZA outro ambiente
```

> Nota Windows: o script força UTF-8 por conta própria (o console cp1252 não
> imprime →/⚠/≤). Lição de campo já vista no cc-stats.

## O que detecta (sondas read-only, best-effort)

GPU/VRAM (nvidia-smi → bucket none/<8/8-12-WDDM/16-24) · Ollama (api/tags +
modelos) · Copilot (extensão) · Anthropic (regime: api_usd / claude_max /
ollama_local) · pode_instalar (user-level, NÃO exige admin) · policy_locked
(MDM + egress externo bloqueado) · sync-folder (OneDrive/Dropbox) · disco.

## Validação (3 casos rodados)

| Caso | Classificação | Comportamento correto |
|---|---|---|
| Máquina real (3060, Ollama, OneDrive) | **A5** | locais (M9-M13) LIGAR AGORA; M8 com .gitignore |
| Simulado A1 (sem GPU, Copilot) | A2 | M5 LIGAR; locais bloqueados **FÍSICO** |
| Simulado A4 (RTX 4090, locked) | A4 | locais bloqueados **POLICY** (não físico!) — 4090 ótima, IT bloqueia |

O caso A4 valida o conceito #5 (físico ⊥ policy): mesmo movimento, motivo de
bloqueio **dinâmico** conforme o que falhou (GPU vs permissão).

## Limitações de detecção conhecidas (achadas rodando — honestidade epistêmica)

1. **Tier do plano Copilot não é detectável offline.** O script só vê se a
   extensão existe em `~/.vscode/extensions`; o **perfil do VSCode** pode esconder
   a extensão (na máquina real deu `copilot=False` embora haja Copilot Pro). E o
   entitlement (Free/Pro/Enterprise) não é legível sem autenticar. → tratar como
   entrada manual / re-confirmar.
2. **`pode_instalar` é heurística.** Corrigido o bug grave (exigia admin → todo
   dev não-admin virava "corporativo"). Agora: user-level basta; `policy_locked`
   só com sinais fortes (MDM + egress externo bloqueado). Ainda assim, um falso
   positivo/negativo é possível — o dev confirma.

> Estas limitações são por que os números/flags do protótipo são **defaults a
> sobrescrever**, não verdades. A autoridade vem da execução/medição local
> (lição L3). Próxima iteração: ler entitlement do Copilot, sondar MDM melhor,
> e MEDIR t/s local em vez de assumir o sweet spot.

## Invariantes (do confronto)

- Nunca recomenda movimento cuja pré-condição a máquina viola (assert por Mx).
- Distingue bloqueio FÍSICO (evolua HW) de POLICY (escale ao IT).
- Read-only por default (não instala nada); `--emit-profile` é a única escrita.
- Saída-máquina (`environment-profile.yaml`) mantém os 3 regimes de custo
  SEPARADOS (nunca soma) e carrega a allowlist de tool_use.

## Próximo
- Calibrar detecção (limitações 1-2) e adicionar micro-bench local (medir t/s
  real em vez de assumir). Depois, este protótipo + `../arvore-decisao.md`
  viram a base da recipe portável.
