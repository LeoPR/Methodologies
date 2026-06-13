---
title: 'RESULTADOS — braço externo (bem-comportado + messy): o falso-positivo é da FORMA; o M0 sub-detecta'
created: 2026-06-13
status: 'bem-comportado + messy fechados (6 repos de TERCEIRO, N=1). Os DOIS modos de falha externamente; messy gênero-confundido. Quebra circularidade.'
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

## Tier messy/baixa-conformidade — o espelho (e o confundidor de gênero)
3 repos externos de baixa conformidade objetiva: `mlscratch` **3/7**, `pytorchgan` **3/7** (científicos —
sem tests/CI/changelog), `ml3months` **1/7** (só README — gênero "lista/notas", não software). M0 × 3 modelos:

| repo (conf.) | gemini | gpt-4.1 | gpt-4o-mini |
|---|---|---|---|
| mlscratch (3/7) | PRECISA-PONTOS | JÁ-BOM | JÁ-BOM |
| pytorchgan (3/7) | JÁ-BOM | JÁ-BOM | JÁ-BOM |
| ml3months (1/7) | JÁ-BOM | JÁ-BOM | JÁ-BOM |

**Leitura (honesta, dois lados):**
- **O M0 tem forte viés de ABSTENÇÃO:** disse JÁ-BOM a quase tudo — inclusive ao repo **1/7**. Combinado com
  o tier bem-comportado (JÁ-BOM nos organizados), isso **replica externamente o achado F1/M0**: a forma de
  abstenção **conserta o falso-positivo MAS super-corrige em SUB-DETECÇÃO**. **Nem o gpt-4.1 discriminou** (só
  o gemini flagou 1 caso) → discriminar é **capacidade**, e aqui ela quase não apareceu.
- **PORÉM, confundidor de GÊNERO (o "decidir bom/ruim é difícil" que você apontou):** baixa-conformidade
  **≠ defeito**. Repo de pesquisa sem CI/CHANGELOG ou uma **lista de links** (ml3months) podem estar
  **genuinamente "já-bons" para o gênero** — §9 não manda exigir tests de uma lista. Então o JÁ-BOM pode ser
  **correto**, não sub-detecção. **Sem gabarito gênero-consciente não dá para cravar** — o score de conformidade
  é gênero-cego. (Liga direto à ideia AulaQuantum/DeepLearning: o gênero muda o gabarito.)
- **Conclusão do espelho:** o braço externo mostra **os dois modos de falha** — *audit over-detecta* (falso-
  positivo) e *M0 sub-detecta* (abstém de quase tudo); a forma move o viés, a capacidade (incompletamente)
  calibra. O tier messy é **inconclusivo sobre sub-detecção** (confundido por gênero), mas **confirma o viés de abstenção do M0**.

## Limites (§6) — não generalizar além disto
- **N=1**/célula, **3 repos**, **1 gênero** (pacote Python PyPI), **só o tier bem-comportado**.
- M0 é o **gate** (veredito JÁ-BOM/PRECISA), **não** a auditoria rica de qualidade (o domínio do R8) — esta,
  externamente, **continua aberta**. Este resultado mostra que o *gate de abstenção* funciona em externo, não
  que a auditoria completa bate a competência pura no real.
- **Pendente:** tier **messy/científico** (o M0 diz **PRECISA** corretamente quando HÁ problema real, num
  externo?) e **caótico** — o teste-espelho que evita "abstém de tudo". Mesmos sinais objetivos para classificar.
