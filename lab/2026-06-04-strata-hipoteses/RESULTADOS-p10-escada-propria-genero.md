---
title: 'P10 — escada por vendor (K=5) nos projetos PRÓPRIOS do dono, eixo gênero-consciente/abstenção'
created: 2026-06-16
updated: 2026-06-16
setup: 'hb_genre.py (prompt gênero-consciente: identifica gênero, aplica só o padrão que se aplica, §9), escada de 9 modelos do Copilot × K=5, via OpenRouter. Alvos: digests de organização (gitignored) de own-aulaquantum, own-deeplearning (cadernos de aula) e fg2p (real, PARCIAL). Juiz Claude cego contra gabarito PRÉ-REGISTRADO.'
status: 'SINAL (circular). A assinatura por tier replica EM PARTE nos projetos reais do dono; achado novo: o VEREDITO abstém mas a AÇÃO over-limpa. fg2p parcial (crédito esgotou). TCF não rodou (crédito).'
---

# P10 — a escada nos projetos do próprio dono (gênero-consciente)

Motivação do dono: "quero dados honestos mesmo que sejam meus projetos". Rodamos a escada de 9 modelos (K=5)
no eixo **gênero-consciente** (o modelo identifica o gênero e aplica só o padrão que se aplica; §9). Nos dois
**cadernos de aula** (aulaquantum, deeplearning) o veredito CORRETO é **JÁ-BOM-PARA-O-GÊNERO** (abster) — a barra
de software (CI/LICENSE/tests) não se aplica. Gabarito pré-registrado: `GABARITO-genero-temporal-own.md`
(armadilhas negativas N1–N5).

> **CIRCULAR (lê com cuidado):** projeto + analista do gabarito + autor do método = mesma família (Leonardo +
> Claude). Mede se o modelo **lê como o autor lê** (reconhece gênero + abstém), **não** se o método é válido nem
> se generaliza. Sinal de consistência interna, não evidência independente.

## Resultado (escada · veredito esperado = JÁ-BOM nos dois cadernos)

| modelo | aulaquantum | deeplearning | fg2p (PARCIAL) |
|---|---|---|---|
| **Opus 4.8** | JÁ-BOM 5/5 · over 1,8 (N5 5/5, N2 3/5) | JÁ-BOM 5/5 · over 0,5 | n=5 JÁ-BOM 5/5 = **sub-detecção** |
| **Sonnet 4.6** | JÁ-BOM 4/5 · over 1,1 (N5 1/5) | JÁ-BOM 5/5 · over 1,0 | n=2 · 0/3 reais |
| **Haiku 4.5** | JÁ-BOM 4/5 · over 1,6 (N5 2/5, N2 1/5) | JÁ-BOM 5/5 · over 1,3 (N1 2/5) | n=2 sub-detecção |
| **Gemini 3.1 Pro** | JÁ-BOM 5/5 · over 1,8 (**N5 5/5**) | JÁ-BOM 4/5 (r5 truncou) · over 0,0 | — |
| **Gemini 3 Flash** | JÁ-BOM 5/5 · over 1,6 (N5 3/5) | JÁ-BOM 5/5 · over 0,0 | n=4 sub-detecção (N5 2/4) |
| **GPT-5.5** | **PRECISA 4/5** (over-age) · over 1,8 (N5 4/5) | JÁ-BOM 4/5 · over 1,2 | — |
| **GPT-5 mini** | **PRECISA 5/5** (over-age) · over 1,6 | **PRECISA 5/5** (over-age) · over 2,0 (**N1 5/5**) | — |
| **DeepSeek V4 Pro** | JÁ-BOM 5/5 · over 1,2 (N5 3/5, N2 2/5) | JÁ-BOM 5/5 · over 0,6 | — |
| **DeepSeek V4 Flash** | JÁ-BOM 3/5 · over 1,4 (N5 3/5) | JÁ-BOM 4/5 · over 0,5 | n=5 sub-detecção |

## Achados

1. **A assinatura "topo abstém / barato over-age" replica EM PARTE.** Topo (Opus, Sonnet) e os fortes
   (DeepSeek-Pro, Gemini-Pro/Flash) **abstêm** (JÁ-BOM). O único que **inverte o veredito nos dois cadernos** é o
   **GPT-5 mini** (0/5 e 0/5) — a pior calibração. O **GPT-5.5** inverte só no aulaquantum (o caderno com `old/`
   + zips + dado pessoal dispara a over-limpeza).
2. **Achado NOVO — veredito ≠ ação.** A separação por tier aparece no **veredito**, não na taxa de armadilha. Até
   **Opus e Gemini 3.1 Pro acertam JÁ-BOM mas caem em N5 5/5** no aulaquantum (mandam **apagar `old/`** = destruir
   tombstone). "Acerta o diagnóstico, mas a primeira ação over-limpa a história." A abstenção do **veredito** não
   garante a abstenção da **ação**.
3. **N5 (apagar tombstone `old/`) é epidemia** no aulaquantum (Gemini-Pro e Opus 5/5; GPT-5.5 4/5; Flash e
   DeepSeek-Pro 3/5). **N1 (dataset DELETADO recriável lido como perda)** só no deeplearning, grave no GPT-5 mini
   (5/5). **N3/N4 quase não caem** — o gênero foi bem lido (todos descartam CI/LICENSE/tests e leem
   `.md→derivado` como fonte/artefato, não duplicação).
4. **Ressalva ao "barato".** O **Haiku** (barato Anthropic) **não inverte** o veredito (só sobe a over-ação) —
   o "barato over-age" não é uniforme; o GPT-5 mini é o caso que de fato falha.

## fg2p (PARCIAL — o eixo se inverte)

fg2p é projeto **real com problemas reais** (3 plantados: backups/ misturado, configs legacy sem tombstone,
falta de mapa central). Só 18/45 rodaram (crédito esgotou; n desigual: Opus/DeepSeek-Flash n=5, Gemini-Flash
n=4, Sonnet/Haiku n=2; faltam Gemini-Pro, GPT-5.5, GPT-5-mini, DeepSeek-Pro).
**Todos sub-detectaram** (deram JÁ-BOM onde o correto é PRECISA) e erraram os 3 reais. **A "virtude de abster"
dos cadernos vira "vício de complacência"** num projeto que de fato precisa. **Conclusão provisória** (cobertura ruim).

## Caveats

- **Circular** (acima) — o limite mais importante.
- **fg2p parcial** + **TCF não rodou** (crédito esgotou em 402 no meio do fg2p; saldo OpenRouter = 0).
- **Juiz único Claude**; K=5 por célula mas **1 família de fixtures** (não há poder estatístico cross-projeto).
- TCF tem digest + gabarito **pré-registrado por hash** ([PRE-REGISTRO-own-tcf.md](PRE-REGISTRO-own-tcf.md));
  roda quando houver crédito (esperado JÁ-BOM).

*Planos brutos: `eval/strata/planos/esc-{aulaquantum,deeplearning,fg2p}/` (digests-fonte gitignored).*
