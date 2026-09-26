---
name: revisao-superficie-strata
type: registro
status: em andamento (commits 1-5 planejados; ver "Execução")
created: 2026-09-26
updated: 2026-09-26
audience: ai-primary
---

# Revisão de superfície do Strata (2026-09-26)

Pedido do dono: revisar o Strata pela **superfície** (a proposta raiz e o refinamento do L0),
e, antes de mexer, conferir se o que está **feito** bate com o que está **declarado feito**.

## Conferência do núcleo

Antes de propor mudança no produto, o L0 foi relido inteiro na expressão inglesa (as 13 seções,
§1 a §11 mais §3-bis e §6-bis) sob a régua que ele declara para si: "sem produto, sem data" (lead
da Parte I), "se a IA e o computador sumissem, ainda valeria?" (teste do L0), §5 (fonte única) e
§9 (proporção) aplicados ao próprio texto.

## Achados da revisão (antes da auditoria)

Proposta raiz (lead + camadas): sólida. Dois defeitos:

- o "teste" do L1 ("é *uma* boa forma, não a única") é definição, não teste decidível;
- restos de conversa com o dono no núcleo neutro: §3 ("You named this as a central goal") e §7
  ("The 'how to generate' you asked for").

Refinamento (L0 fechado):

- a instância de era do §9 carrega diário de pesquisa (modelos, K, percentuais) dentro do L0;
- o §3-bis declara um defeito do §8 ("a distinction §8 today conflates") que nunca foi corrigido
  nem rastreado;
- o §10 repete por inteiro o argumento "autoridade única ≠ cópia única" do §5;
- caminhos citados nos Groundings inconsistentes (`Strata/lab/...` × `lab/...`).

Superfície:

- `recipe/README` promete "guia completo dentro do arquivo" para brownfield; o canônico declara
  o brownfield lacuna conhecida;
- `recipe/README` repete a mesma ressalva cerca de cinco vezes, com trechos em tom de diário;
- `o-que-voce-ganha` afirma "your affordable AI yields much more with the method", o que o §9
  testado não sustenta para a proporção.

## Auditoria declarado × feito

Registro completo, com destino por achado: [`AUDITORIA-sync.md`](AUDITORIA-sync.md).
Resultado: **não estava sincronizado**. Três blocos:

1. **Wayfinding** (versão, ponteiros, status de registros encerrados): mecânico.
2. **Superfície do produto** (capa, `recipe/README`, `o-que-voce-ganha`, o canônico): onde
   caem as recomendações acima, e mais três achados que as agravam:
   - o texto medido como "v1.2.2" no A/B do §9 não é a v1.2.2 commitada (`method_sha` do braço B
     não bate com nenhum commit; o texto testado não foi retido);
   - o A/B rodou só em PT, embora o portão da PROPOSTA-S9 pedisse PT+EN;
   - o parêntese do §9 ("4 models, K=5") descreve só o braço naive; o braço Strata veio de outra
     grade (7 modelos, K=2), sem pareamento.
3. **Camada de evidência** (OPINIAO-DE-USO, tabela-fonte do hub, propagação do vazamento do
   `f4-clean`, outreach, docs do eval, trabalho não commitado do controle negativo): pede
   **decisão do dono**, porque reescreve o que a evidência diz. Fica listada como pendente.

## Execução

Um commit por etapa, cada um com as guardas (`check_stamps`, `check_l10n`) e par EN/PT no mesmo
commit quando a fonte é multilíngue.

| # | Escopo | Achados |
|---|---|---|
| 1 | wayfinding: versão, ponteiros, status de registros encerrados, inventário | ver coluna destino |
| 2 | superfície: brownfield, "não mexer" na capa, frase do `o-que-voce-ganha` | idem |
| 3 | canônico: §9 enxuto (ponteiro, não diário) + errata do traço do A/B | idem |
| 4 | canônico: §3-bis/§8, §5/§10, persona, teste do L1, caminhos, itens abertos | idem |
| 5 | `recipe/README`: uma ressalva só, sem diário, evidência por ponteiro | idem |
