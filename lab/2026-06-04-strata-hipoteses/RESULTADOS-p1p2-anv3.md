---
title: P1+P2 — AN-v3 (forma anti-falso-positivo + etapas) — orientar o modelo médio
created: 2026-06-08
setup: AN-v3 × 4 médios (gpt-4.1-mini, gemini-2.5-flash, deepseek-v3, haiku) × NNN+pdf2md × N=2 · pontuação CEGA (juiz Claude, 32 agentes) contra gabarito CORRIGIDO (inclui os §5 que o Opus achou no P0) · comparado aos MESMOS 4 modelos do R8 (AN-v2)
status: a forma AJUDA (menos falso-positivo, melhor sinal-ruído), mas NÃO instala a discernância do Opus — desloca o erro, não fecha o gap de capacidade
---

# P1+P2 — a forma+etapas faz o médio se comportar como o Opus? Em parte.

Pergunta: as 6 condutas que fizeram o Opus acertar (P0), embutidas como **forma anti-falso-
positivo + processo em etapas** (AN-v3), fazem um modelo **médio** parar de alucinar e achar
o real? Testado nos mesmos 4 médios e 2 projetos do R8 — só a forma muda (AN-v2 → AN-v3).

## Os números (juiz Claude cego, gabarito corrigido)

| projeto | forma | FALSO-POS | genuíno | reconh.bom | net (gen−FP) |
|---|---|---|---|---|---|
| **NNN** (exemplar) | AN-v2 | 4.25 | 0.00 | 0.25 | −4.25 |
| | **AN-v3** | **2.88** | 0.12 | **0.62** | **−2.76** |
| **pdf2md** (reais) | AN-v2 | 1.88 | 1.50 | 0.75 | −0.38 |
| | **AN-v3** | **0.38** | 0.88 | 0.62 | **+0.50** |

- **Falso-positivo CAI** nos dois (NNN −1.38; pdf2md −1.50, quase a zero) e **reconhecer-o-bom
  SOBE** no NNN (0.25→0.62). Os gates "é válido não achar nada / reconheça o bom 1º / situe no
  tempo" **funcionam** — o §9 que o R8 mostrou violado passa a ser respeitado.
- **Sinal-ruído (genuíno − falso-positivo) melhora nos dois** — e no pdf2md fica **positivo**
  (+0.50 vs −0.38): mais real que ruído pela primeira vez.

## O trade-off (o achado honesto) — é por MODELO

| modelo | NNN FP v2→v3 | pdf2md (FP/gen) v2→v3 | leitura |
|---|---|---|---|
| **gemini-2.5-flash** | 7.0 → **2.5** | (1.0/2.0) → (0.0/**0.5**) | forma derruba o ruído, mas o cala: perde os reais |
| **gpt-4.1-mini** | 0.5 → 0.5 | (3.0/0.5) → (**0.0/0.0**) | zera o ruído mas fica **mudo** (diz "tudo ok") |
| **deepseek-v3** | 5.0 → 4.0 | (2.5/1.5) → (**1.0/2.0**) | **melhora nos dois eixos** (o único) |
| **claude-3.5-haiku** | 4.5 → **4.5** | (1.0/2.0) → (0.5/1.0) | **ignora** a forma no NNN |

**A forma troca super-crítica por silêncio em alguns modelos** (gemini, gpt-4.1-mini ficam
mudos e perdem os `-DESKTOP`/versão reais); **haiku nem registra** a forma; **só o deepseek**
ganhou discernância (menos ruído E mais real). Ou seja: a AN-v3 **desloca o erro de
over-flag para under-flag**, em vez de instalar a **discernância** do Opus (achar o §5 sutil
mantendo a calma). Essa discernância é **capacidade**, não some por instrução.

## Veredito

1. **Orientar a IA é uma alavanca REAL.** A forma+etapas mede melhor sinal-ruído que a v2 nos
   dois projetos (NNN net −4.25→−2.76; pdf2md −0.38→**+0.50**). Para modelo médio, **AN-v3 > AN-v2**.
2. **Mas não fecha o gap de capacidade.** Nenhum médio virou Opus (que no P0 achou o real **e**
   reconheceu o bom **e** não alucinou — os três juntos). Os médios só conseguem dois de três,
   e qual par depende do modelo.
3. **Implicação de produto:** auto-auditor confiável = **modelo de topo** (P0) **ou humano-no-
   loop**. Para médios, use a AN-v3 (menos ruído) **esperando sub-detecção** — bom como filtro
   de "o que claramente está mal", ruim como rede fina.
4. **Próximo (P6):** o scatterplot dos eixos de borda vai mapear ONDE cada família quebra —
   e o deepseek (que respondeu à forma) merece um olhar à parte.

## Caveats
- N=2 por célula; 2 projetos; juiz Claude (cross-check não-Claude: ver abaixo).
- "genuine_real" é exigente (problemas sutis); FP conta cada crítica-ao-bom/invenção.
- Gabarito corrigido pós-P0 (mais rigoroso que o do R8) — re-pontua AN-v2 e AN-v3 na mesma régua.

## Robustez (2º juiz, não-Claude — gpt-4.1-mini)

O 2º juiz é **sistematicamente leniente com falso-positivo**: vê FP ~1.1 no NNN onde o juiz
Claude vê ~4.25. Ele **não reconhece quando um plano critica uma prática boa** — falta-lhe a
mesma discernância que o experimento mede. (Meta-achado: detectar falso-positivo **exige**
capacidade; um juiz fraco não consegue — espelha o resultado dos auditores.)

Mesmo assim, ele **confirma a direção qualitativa**:
- **reconhecer-o-bom SOBE** com a AN-v3 no NNN (0.50 → 0.62) — concorda com o juiz Claude.
- **haiku é o outlier** resistente à forma: o ÚNICO com FP alto para os dois juízes (5.0→4.5).
- **genuíno NÃO sobe** (fica igual ou cai levemente) — concorda: a forma não instala detecção.

O que ele **não consegue** confirmar é a **magnitude** da queda de falso-positivo (porque mal
detecta FP). Logo: a **direção** do veredito é robusta a 2 juízes; a **magnitude** do ganho
anti-FP depende do juiz mais discernente (Claude). Conclusão inalterada: **a forma ajuda
(menos ruído, mais reconhecimento do bom), mas não fecha o gap de capacidade.**
