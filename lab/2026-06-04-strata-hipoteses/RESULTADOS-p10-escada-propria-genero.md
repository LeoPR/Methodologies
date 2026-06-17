---
title: 'P10 — escada por vendor (K=5) nos projetos PRÓPRIOS do dono, eixo gênero-consciente/abstenção'
created: 2026-06-16
updated: 2026-06-16
setup: 'hb_genre.py (prompt gênero-consciente: identifica gênero, aplica só o padrão que se aplica, §9), escada de 9 modelos do Copilot × K=5, via OpenRouter. Alvos: digests de organização (gitignored) de own-aulaquantum, own-deeplearning (cadernos de aula) e fg2p (real, PARCIAL). Juiz Claude cego contra gabarito PRÉ-REGISTRADO.'
status: 'SINAL (circular). REFINADO 2026-06-16 (TCF + fg2p COMPLETOS, K=5): over-ação é NOISE-triggered (TCF limpo → escada INTEIRA abstém, incl. barato); SUB-detecção domina no real (fg2p: só 1/9 detecta de verdade); circularidade ATACADA (no real público, quem detecta é o gpt-5.5, NÃO o Opus da casa).'
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
   **GPT-5 mini** (0/5 e 0/5) — a pior calibração. O **GPT-5.5** inverte só num dos cadernos (o que tem
   mais história/anexos acumulados dispara a over-limpeza).
2. **Achado NOVO — veredito ≠ ação.** A separação por tier aparece no **veredito**, não na taxa de armadilha. Até
   **Opus e Gemini 3.1 Pro acertam JÁ-BOM mas caem em N5 5/5** no aulaquantum (mandam **apagar `old/`** = destruir
   tombstone). "Acerta o diagnóstico, mas a primeira ação over-limpa a história." A abstenção do **veredito** não
   garante a abstenção da **ação**. *(Revisão adversarial 2026-06-16: parte desse N5 é **obediência a uma "Lista de
   Lixo" embutida no fixture** que ordena deletar + **remoção CORRETA de PII** — não puro over-action. Fica como
   sinal, não isolado; ver "Completo" abaixo.)*
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
- **fg2p (parcial) e TCF** foram **completados em 2026-06-16** — ver a seção "Completo" abaixo (esta leitura
  parcial do fg2p foi superada pela escada cheia).
- **Juiz único Claude**; K=5 por célula mas **1 família de fixtures** (não há poder estatístico cross-projeto).
- TCF tem digest + gabarito **pré-registrado por hash** ([PRE-REGISTRO-own-tcf.md](PRE-REGISTRO-own-tcf.md));
  roda quando houver crédito (esperado JÁ-BOM).

*Planos brutos: `eval/strata/planos/esc-{aulaquantum,deeplearning,fg2p}/` (digests-fonte gitignored).*

## Completo (2026-06-16) — TCF + fg2p com escada cheia (K=5, 9 modelos)

Com o top-up, fechamos os dois que faltavam. Projetos por **natureza ampla**:
**TCF** = projeto grande de Python, com docs e artigos (público); **fg2p** = biblioteca/pesquisa em código (público).

### TCF (esperado JÁ-BOM — research-software bem-organizado)
**A escada INTEIRA abstém.** 9/9 modelos: **5/5 JÁ-BOM**, **over-ação ~0**, **N1–N8 caíram 0/5 em todos**
(várias runs nomeiam N1–N8 ativamente como "o que NÃO fazer"). Única mancha: gpt-5-mini over 0,2 (1 run inventou
frontmatter). Única ressalva legítima e recorrente: carimbo de data defasado = reparo cosmético de 1 linha
(autorizado pelo gabarito), não over-ação.

### fg2p (esperado PRECISA — projeto real com dívida organizacional)
Problemas reais do gabarito: (a) pasta de backups misturada/sem tipagem; (b) configs legados sem tombstone;
(c) falta de mapa/índice central. **Quase todos sub-detectam:**

| modelo | fg2p (esperado PRECISA) |
|---|---|
| **GPT-5.5** | **0 JÁ-BOM / 5 PRECISA · recall real ~2/3 · 0 FP proibido** ← único que detecta |
| gpt-5-mini | 3 PRECISA/2 JÁ-BOM, mas **recall 0/3** (certo pelo motivo errado) |
| Opus 4.8 | 5/5 JÁ-BOM (sub-detecção); over 3,0 (infla com nº inconsistente) |
| Sonnet 4.6 | 5/5 JÁ-BOM, recall ~0/3 (inventa lacuna de pesquisa) |
| Haiku 4.5 | 5/5 JÁ-BOM, recall 0/3, **alucina arquivos inexistentes** (over 2,6) |
| Gemini 3.1 Pro | 5/5 JÁ-BOM, vê backups mas trata como cosmético |
| Gemini 3 Flash | 5/5 JÁ-BOM, recall raso |
| DeepSeek V4 Pro | 5/5 JÁ-BOM, **R4/R5 defendem o backups** (anti-recall) |
| DeepSeek V4 Flash | 4/5 JÁ-BOM, recall ~nulo |

### Achados que isto refina (DIRECIONAIS — revisados contra exagero, 2026-06-16)

> **Confound transversal (atinge os 4):** o framing gênero-consciente (`hb_genre.py`) **já prima abstenção**
> ("§9 não exija o que não se aplica" + "apenas as poucas lacunas"). O limpo (TCF) e o over-ação do corpus
> anterior **não** foram medidos sob o mesmo prompt (aquele era "ache problemas"). Então **ruído está confundido
> com framing**, e "JÁ-BOM" pode ser leniência-de-prompt. Tudo abaixo é **direcional**, N=1 fixture/projeto, 1
> juiz (Claude), TCF circular (do dono). *(Revisão adversarial: 4 críticos rebaixaram os 4 achados de causais p/ direcionais.)*

1. **Over-ação parece modulada por ruído/legibilidade — NÃO isolada de capacidade.** No TCF limpo a escada
   inteira deu JÁ-BOM (over ~0), incl. barato — *consistente* com "menos ruído → menos over-ação". Mas **não é
   causal**: sob o MESMO framing, no caderno aulaquantum o GPT-5-mini **inverteu** para PRECISA e até o Opus caiu
   em N5 — capacidade reaparece. Falta rodar TCF sob "ache problemas" para isolar.
2. **Sobre a over-LIMPEZA (apagar história):** não apareceu no TCF, apareceu no caderno — mas o desenho **não
   isola a legibilidade** como causa. O caderno **embute uma "Lista de Lixo" que ORDENA deletar** (o Opus cita
   isso como justificativa = obedeceu um gatilho do próprio fixture) e parte do "apagar" é **remoção CORRETA de
   PII** (não over-ação). Sinal fraco; falta um fixture par-a-par variando só a legibilidade.
3. **No real, a falha pende para SUB-detecção:** 8/9 deram JÁ-BOM no fg2p (recall ~0/3); só o **GPT-5.5**
   detectou (PRECISA, recall ~2/3). **Parte é leniência do prompt** (o mesmo que abstém no TCF), não disposição
   inerente — prova: sob o MESMO framing o GPT-5.5 detecta, logo **capacidade diferencia e o framing INFLA** (não
   fabrica). A direção replica o R8; a magnitude (8/9) e "falha dominante" são de 1 fixture/1 juiz/1 prompt.
4. **Circularidade: enfraquecida, NÃO atacada de forma decisiva.** No fg2p (público), o GPT-5.5 acertou PRECISA e
   o Opus (da casa) deu JÁ-BOM — sinal de que o discernimento no real não é exclusivo da família. Mas: (a) ambos
   pegaram a MESMA inconsistência de versão — a diferença é **uma casa de limiar**, não cego×detecta; (b) 1
   fixture (noutras células o OpenAI foi o pior e o Opus abstém certo); (c) **o juiz é Claude** (a circularidade
   muda de lado); (d) gabarito é do dono. Atacar de verdade = terceiros múltiplos + gabarito independente + juiz não-Claude.

**Defesa parcial:** o TCF tem **pré-registro por hash** do gabarito antes de rodar — mitiga ajuste pós-hoc, mas
não a circularidade nem o digest **auto-sinalizante** (modelos chegam a parafrasear os rótulos N1–N8 do gabarito).

**Caveats:** K=5, 1 juiz (Claude), 1 fixture por projeto; **framing único pró-abstenção** (não cruzado com "ache
problemas"); TCF circular; fg2p e TCF públicos. **Sinais direcionais, não prova.** Saldo após o run ~US$4,7 (~US$5,1 este run).
