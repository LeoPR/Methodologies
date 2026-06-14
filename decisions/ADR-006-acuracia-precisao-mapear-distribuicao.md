---
title: ADR-006 — Medir e reportar ACURÁCIA × PRECISÃO como eixos separados (mapear a distribuição, não caçar a temperatura)
status: aceito
date: 2026-06-14
scope: metodologia de avaliação (eval/) — como reportar resultados de modelos; não é conteúdo de uma metodologia-produto
---

# ADR-006 — Acurácia × precisão: dois eixos, não um número

## Contexto

Ao discutir o P8 ([RESULTADOS-p8](../lab/2026-06-04-strata-hipoteses/RESULTADOS-p8-posicao-saliencia-s9.md)),
o dono levantou que **"um modelo ter conseguido 1× não significa estável"**, e que hiperparâmetros
(a temperatura é só **um exemplo**) e ruído aleatório fazem o modelo dar decisões diferentes para a
mesma tarefa. A pesquisa (2 ciclos) confirmou e refinou:

- **Temperatura mexe na PRECISÃO (estabilidade), não na ACURÁCIA (capacidade).** Na faixa útil (0 a ~1,0)
  a acurácia média de decisão quase não muda (Renze & Guven, 9 modelos, p≈0,40); o que muda é a dispersão.
  A cauda só degrada acima de ~1,2. É **um** hiperparâmetro entre vários (top_p, top_k, penalties, e o
  ruído de batching da própria infra — que torna até `temperature=0` não-determinístico).
- **Os dois eixos são ortogonais (metrologia / viés-variância).** Dá para ser **preciso e errado**:
  temperatura baixa **trava no modo**; se o modo é ruim, fixa-se o erro de forma reprodutível, e a
  estabilidade dá **falsa sensação de confiabilidade**.
- **Capacidade é uma DISTRIBUIÇÃO, não um ponto.** A oscilação bom/ruim é máxima **na fronteira de
  competência** — pode ser um modelo fraco numa tarefa média **ou** um forte no limite dele. Um fraco
  numa tarefa que erra **sempre** tem variância **baixa** (erra de forma confiável). Por isso a regra é
  "**o modelo na sua fronteira oscila**", e o fraco chega à fronteira mais cedo.
- **"Conseguiu 1×" (pass@k) ≠ confiável (pass^k).** Os dois rankings divergem; reportar só o melhor caso
  superestima a competência de uso.

## Decisão

Ao medir um modelo aplicando uma metodologia, **reportar ACURÁCIA e PRECISÃO em colunas separadas** —
nunca colapsar num número só.

1. **Acurácia** = média de acerto vs gabarito (capacidade/viés). **Precisão** = dispersão entre
   repetições (SD/CV) **+ taxa de flip** bom↔ruim (estabilidade/variância).
2. **Sempre publicar k e K.** K pequeno (ex.: 2) é **teto de amostra**, não medida estável.
3. **Cobertura vs confiabilidade:** quando importar, reportar `pass@k` (teto de capacidade, sobe com k)
   vs `pass^k` (confiabilidade, cai com k).
4. **Mapear a distribuição no regime de USO** (mesmos seeds/temp/infra que vão para produção). **Não**
   varrer hiperparâmetros para "achar a melhor temperatura" — isso é afirmação de **capacidade**
   (best-case), não de confiabilidade, e a config ótima não transfere entre tarefas.
5. **Não existe temperatura privilegiada.** Rodar só a 0,3 corre risco de **mode-lock** (estável porque
   travado); rodar só a 1,0 infla a cauda. "0 flips" vindo de temp baixa + K pequeno deve ser marcado
   como **possível mode-lock**; só vira "confiável" se sobreviver a temp mais alta e K maior.
6. **A temperatura/hiperparâmetro é a LENTE da variância (precisão), não a capacidade.** A conclusão é
   sobre o eixo precisão, não sobre o número 0,3 vs 1,0.

## Consequências

- O `hb_runner.py` ganhou um flag **`--temp`** (aditivo, default 0,3 = comportamento histórico) para
  permitir mapear a distribuição variando a temperatura sem mudar o que já roda.
- O **P8 foi corrigido**: o "veredito grosso 0 flips a 0,3" deixa de ser "robusto" e passa a
  "estável-possivelmente-travado"; a detecção de segurança do modelo fraco vira **sinal de fronteira**
  (instável), não "ganho"; o `gpt-4.1 K=2` é marcado como não-atestável.
- Próximas medições "oficiais" reportam os dois eixos; células decisivas (segurança, abstenção) pedem
  K maior (≥10) e o flip-rate explícito.

## Alternativas consideradas

- **Um número (a média):** rejeitado — esconde a diferença entre "3 sempre" e "oscilando 2–4".
- **Rodar numa única temperatura "realista":** rejeitado — não há temp privilegiada; troca um viés por outro.
- **Sweep para achar a melhor temperatura:** rejeitado como método de confiabilidade — é teto de
  capacidade, instável como ranking e não transfere entre tarefas.
