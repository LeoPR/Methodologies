---
name: revisao-temporal-strata
type: registro
status: varredura feita 2026-09-26; nada aplicado ao produto ainda (aguarda decisão do dono)
created: 2026-09-26
updated: 2026-09-26
audience: ai-primary
---

# Revisão temporal do Strata (2026-09-26)

Pedido do dono: os testes e as fontes envelhecem. Conferir (1) se surgiram técnicas de avaliação
que mudam como julgamos os testes, (2) se o roster de modelos ainda representa os estratos, (3) se
as formalizações do L1 e as ferramentas do L2 continuam corretas, e (4) se o texto do L0, escrito
por humano, diz o que as fontes citadas dizem.

Método: quatro agentes de pesquisa em paralelo, só leitura (três com busca web; a revisão do L0
foi feita por conhecimento de referência, sem web). Nenhum achado abaixo foi aplicado. Onde a
fonte é secundária ou não foi aberta, está marcado.

## 1. Métodos de avaliação (o que muda no harness)

| Prioridade | Técnica | Fonte | Situação no harness | Recomendação |
|---|---|---|---|---|
| 1 | Auditoria de atalho por fixture ("task validity": resolvível só com a capacidade medida) | ABC, Zhu et al. 2025, arXiv 2507.02825 | ausente; é a classe de erro do vazamento do `f4-clean` | adotar: grep dos termos do gabarito dentro da fixture + célula "sem capacidade" antes de cada série |
| 2 | Erro-padrão clusterizado, comparação pareada, análise de poder | Miller 2024, arXiv 2411.00640 | ausente; runs K do mesmo modelo × fixture são tratadas como independentes | adotar; reavaliar o A/B do §9: com K=3 e 3 modelos, "sem efeito medido" pode ser "sem poder" |
| 3 | Sensibilidade do juiz (o veredito vira quando só o elemento decisivo muda) | Chen et al. 2026, arXiv 2608.24419 | parcial: α alto medido, sensibilidade não | adotar um teste de perturbação pequeno |
| 4 | Calibração juiz × gold com intervalo válido | Lee et al. 2025, arXiv 2511.21140 | gold mecânico existe, mas não calibra o juiz | adotar nas células só com juiz |
| 5 | Canary string em fixtures e gabaritos | prática BIG-bench; arXiv 2510.05244 | ausente; `lab/` e `recipe/` são públicos | adotar (uma linha por arquivo) |
| 6 | Abstenção não resolve com escala; raciocínio abstém menos | AbstentionBench, arXiv 2506.09038 (NeurIPS 2025) | não citado | citar como corroboração externa do §9 |
| 7 | Checklist de validade de construto | Bean et al. 2025, arXiv 2511.04703 | espírito coberto | auditoria única do hub com o checklist |
| nota | Pistas superficiais movem vereditos; CoT do juiz não as revela | arXiv 2509.26072, 2602.07996 | júri já é cego | conferir que o prompt do juiz não leva nome de modelo nem rótulo de braço |
| nota | Injeção adaptativa quebra defesas | arXiv 2503.00061; AgentDojo revisado | trap estático, um ataque | manter "costuma recusar"; não afirmar robustez |

Abstracts abertos só de 2507.02825, 2512.21326, 2511.21140 e 2608.24419; os demais vieram de
resultados de busca. Conferir números antes de citar em produto.

**Efeito no que já foi publicado:** nenhuma conclusão qualitativa cai. Duas ficam mais fracas:
a lista nominal de quem calibra ou superage na abstenção (medida na fixture que vazava) e o
"sem efeito medido" do §9 (pouco poder).

## 2. Roster de modelos (fonte: web; agregadores marcados como secundários)

- **Protocolo:** a Anthropic deprecou `temperature` fora do default a partir do Opus 4.7 e na linha
  Claude 5 (docs de deprecations). `providers.chat()` sempre envia `temperature`, e o `hb_runner` usa
  0.3. **A verificar:** como as células Claude 5 da grade de agosto trataram isso (roteador
  descartou? rodaram em default?). Se as temperaturas diferiram por fabricante, é fator a declarar
  (ADR-006).
- **Novos no topo:** claude-opus-5-5 e claude-fable-5-1 (set/2026); GPT-6 Sol e Luna (22-set-2026,
  VentureBeat); Gemini 3.7/3.8 Flash (agregador). gemini-3.1-pro sumiu do seletor do AI Studio,
  segue na API (instável; agregador).
- **Aposentadorias próximas:** Haiku 4.5 "não antes de 2026-10-15"; snapshot gpt-5-mini-2025-08-07
  desliga em 2026-12-11; gpt-4.1-mini na API não confirmado. deepseek-v3.2 superado pelo V4 Pro 0813.
- **Local:** Qwen3.8-27B (Apache-2.0, ago/2026) supera o qwen3.6 27b/35b na classe 24 GB; Gemma 4
  E4B ausente do roster (deixa o Google fora do estrato local).
- **Reteste mínimo proposto:** ~480 runs de candidatos, com âncoras idênticas a agosto (qwen3 8b,
  deepseek-v4-pro no mesmo snapshot, opus-5) para separar deriva do modelo de deriva do instrumento:
  conserto (gold mecânico, ~180), recusa PT+EN (~150), abstenção em 2 redações (~150), **na
  `f4-clean-v2`, não na fixture que vazava**. Antes de trocar juízes, bench de concordância dos
  juízes novos sobre saídas já julgadas.

## 3. L1 / L2 (fonte: web)

Mudanças necessárias no canônico:

- **OAIS: erro factual.** Vale ISO 14721:2025 / CCSDS 650.0-M-3 (dez/2024), não a edição de 2012. O
  carimbo `[WEB ✓ 2026-08-01]` deixou passar.
- **C2PA:** spec na 2.4 (abr/2026); ISO 22144 em DIS por fontes secundárias (iso.org bloqueou a
  consulta: estágio não verificado na primária).
- **OTel GenAI:** segue Development; desde a v1.42.0 vive num repositório próprio.
- **EU AI Act:** acrescentar as Guidelines finais do Art. 50 (20-jul-2026); conferir no EUR-Lex o
  prazo de 2-dez-2026 do Art. 50(2).

Sem mudança: MCP 2026-07-28, AGENTS.md (AAIF), Agent Skills, RiC-CM 1.0, MADR 4.0, Conventional
Commits 1.0, NIST SP 800-207. Não verificados nesta rodada (sem sinal de mudança, sem confirmação):
SemVer, CITATION.cff, FAIR4RS, BagIt, RFC 2119/8174/5280, SP 800-162. Não recarimbar estes como
verificados.

Candidato novo no L1: nenhum maduro. O concept paper do NIST NCCoE sobre identidade e autorização
de agentes de IA (fev/2026) cabe, no máximo, no sinal de troca da linha RBAC/ABAC.

## 4. L0: teoria × texto (sem web; conferir na fonte antes de editar)

Nenhum achado muda princípio. São citações e atribuições:

| Onde | O texto diz | A fonte diz | Certeza |
|---|---|---|---|
| §6-bis | Saltzer & Schroeder 1975, *CACM* 17(7) | *Proc. IEEE* 63(9):1278–1308 | alta |
| §4, §8 | Claerbout & Karrenbach "coins the term" | popularizam *reproducible research* no sentido computacional | alta |
| §3-bis | cláusula dispositiva aberta por `notum sit`/`sciatis` | isso é a *notificatio*; a *dispositio* usa *do/concedo/trado*; Austin/Searle são paralelo, não genealogia | alta / média |
| §6-bis | EO 8381 funda need-to-know | EO 8381 cria níveis de classificação; need-to-know vem da prática da guerra, codificada depois | média-alta |
| §6 | NULL de Codd 1970 | NULL em Codd 1975/1979; ausência tipada (A-/I-marks) em 1990 | alta |
| §6 | Rubin 1976 com MCAR/MAR/MNAR | MNAR é Little & Rubin 1987; Rubin trata de mecanismo, não de ausência confirmada | média-alta |
| §11 | literary warrant: Svenonius 2000 | cunhado por Hulme 1911; Svenonius sistematiza | alta |
| §5 | Weyuker "generaliza para toda verificação formal" | extrapolação sem suporte na fonte | média |
| §3 | Bjork & Bjork para decaimento de superfície | teoria de memória humana: falta `[ANALOGY]` | alta |
| §6-bis | Polybius VI.34: senha e contrassenha por canal separado | distribuição e devolução da tábua da senha (VI.34–36) | média |
| §6 | Sackett 1996: hierarquia de evidência | Canadian Task Force 1979 propõe a hierarquia | média |
| §7 | Lachmann, método estemático | atribuição em parte mítica (Timpanaro 1963) | média |
| §11 | gênero e diferença: *Categories* | sobretudo *Topics*; árvore de Porfírio | média |

Conferidos e corretos: a maioria das demais (Dijkstra, Parnas, Pirolli & Card, Buneman, Rochkind,
Schellenberg, Snodgrass, Nosek, Cook & Campbell, Knuth, FRBR, Kerckhoffs, Shannon, Bell-LaPadula,
Brewer-Nash, LOCKSS, Kuny, Ranganathan, Bowker & Star). Nenhuma contradição interna de substância.

## Próximos passos propostos (em ordem de custo × valor)

1. **Verificar na web** os itens de certeza alta da seção 4 e as mudanças da seção 3; depois
   corrigir o canônico EN+PT num commit (v1.2.5), com reconferência do L0.
2. **Auditoria de atalho** em todas as fixtures (grep do gabarito): barato, fecha a classe do
   `f4-clean`.
3. **Recalcular o A/B do §9** com teste pareado e poder declarado, sem rodar nada novo.
4. **Esclarecer a temperatura** das células Claude 5 na grade de agosto.
5. **Reteste mínimo** (seção 2) na `f4-clean-v2`, com âncoras. Custa inferência: decisão do dono.
