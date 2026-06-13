---
title: 'RESULTADOS — braço externo (tier bem-comportado): o falso-positivo é da FORMA, não do projeto-próprio'
created: 2026-06-13
status: 'tier bem-comportado fechado (3 repos de TERCEIRO, N=1). Messy/caótico pendentes. SINAL forte, quebra circularidade.'
---

# Braço externo — quebrar a circularidade do "projeto próprio"

Quase todo o "real" testado era projeto **do próprio autor** (circularidade — o maior confundidor da
consolidação). Aqui: **3 repos open-source de TERCEIROS**, classificados por **sinais de conformidade
objetivos** (não julgamento subjetivo): tomli **6/7**, slugify **5/7**, humanize **4/7** — todos
objetivamente organizados (README/pkg-meta/CI/tests). **M0** (abstenção-primeiro) vs **AUDIT** (controle
"ache problemas") × gemini-2.5-flash / gpt-4.1 / gpt-4o-mini. **N=1**. (Digests gitignored — repo de
terceiro é local/privado; só agregado aqui.)

## Resultado
- **M0 (abstenção-primeiro): JÁ-BOM em 9/9** (3 repos × 3 modelos) — todos reconhecem o projeto externo
  organizado como **"já bom, ação mínima"**. A forma de abstenção **abstém certo, externamente**.
- **AUDIT (ache-problemas): ~10-25 "issues"** flagados nos **mesmos** repos limpos — over-detecção
  (falso-positivo) quando primado a achar problema. *(Contagem crua de regex — direção, não número exato.)*

## Leitura — refina o R8 (importante)
O R8 (projetos do dono) mostrou over-detecção/falso-positivo do auto-auditor. O braço externo **refina**:
o falso-positivo é **FRAMING-dependente, não inerente nem circular**. A **forma de abstenção (M0) corrige**
o viés — e isso **vale em projeto de TERCEIRO**, confirmando *"a forma corrige o viés"* (F1/M0) **sem
circularidade**. O framing "ache-problemas" (audit) **ainda** over-detecta.

## Limites (§6) — não generalizar além disto
- **N=1**/célula, **3 repos**, **1 gênero** (pacote Python PyPI), **só o tier bem-comportado**.
- M0 é o **gate** (veredito JÁ-BOM/PRECISA), **não** a auditoria rica de qualidade (o domínio do R8) — esta,
  externamente, **continua aberta**. Este resultado mostra que o *gate de abstenção* funciona em externo, não
  que a auditoria completa bate a competência pura no real.
- **Pendente:** tier **messy/científico** (o M0 diz **PRECISA** corretamente quando HÁ problema real, num
  externo?) e **caótico** — o teste-espelho que evita "abstém de tudo". Mesmos sinais objetivos para classificar.
