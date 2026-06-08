---
title: P4 — capacidade por secao x modelo (visualizacao)
created: 2026-06-08
---

```
# Capacidade por SECAO x MODELO — arm 'cloud-an' (sintetico, % de runs que ACHARAM, N=3)

secao\modelo             anthropic_clau deepseek_deeps google_gemini- meta-llama_lla meta-llama_lla openai_gpt-4.1 qwen_qwen-2.5-   MEDIA
P1 §5 fonte-unica                   100            100            100            100            100            100            100   100%
P2 §3/§8 datas/historia              33              0            100              0             67             33              0    33%
P3 §2 navegacao                     100            100            100              0              0            100             33    62%
P4 §3 traco/superficie              100            100            100            100            100            100            100   100%
P5 §4 honestidade                    67            100            100            100            100            100             67    90%
P6 §6 sem-fonte                     100            100            100            100             67            100             67    90%
P7 §6-bis fail-open                 100            100            100             67            100            100             67    90%

# Suficiencia por MODELO (det_found medio no arm, /7)
  anthropic_clau   6.0/7
  deepseek_deeps   6.0/7
  google_gemini-   7.0/7
  meta-llama_lla   4.67/7
  meta-llama_lla   5.33/7
  openai_gpt-4.1   6.33/7
  qwen_qwen-2.5-   4.33/7

NOTA: so a camada L0 (principios §1..§10) foi exercitada; L1 (padroes) e L2 (ferramentas)
NAO foram testadas. E e' o MELHOR caso (sintetico, denso); em projeto REAL todos alucinam (ver R8).
```
