---
title: 'Concordância entre juízes, corrigida por acaso (Krippendorff α + Cohen κ)'
created: 2026-06-20
updated: 2026-06-20
status: 'FEITO — re-análise sem custo de API sobre os vereditos já coletados. Dá lastro chance-corrected ao "92%".'
---

# Concordância entre juízes, corrigida por acaso

## O que isto mede e por quê

O corpus reportava concordância entre juízes como porcentagem crua, por exemplo "92%".
A porcentagem crua não desconta o acerto por acaso, então ela infla quando um rótulo é muito frequente.
Aqui medimos a concordância **corrigida por acaso**, com o **α de Krippendorff** (nominal) e o **κ de Cohen**.

A medição é re-análise pura, sem custo de API.
Ela roda sobre os vereditos que os dois juízes já produziram, gravados em `eval/strata/planos/*-judge/judgments.json`.
O cálculo está em [`eval/strata/calc_stats.py`](../../eval/strata/calc_stats.py), em Python da biblioteca padrão, com self-test que confere a implementação contra casos calculados à mão.

Os dois juízes do dado histórico são o **gemini-2.5-flash** e o **gpt-4.1**.
Eles são datados (camada L2) e estão superados para rodadas futuras.
Aqui só re-analisamos o que eles já produziram, então a escolha de juiz não muda: o α mede aquele dado.

### Padrão de verbetes (de onde vêm "fraco / preliminar / confiável" — e por que NÃO usamos "moderado")

Antes de rotular, é preciso saber de onde o rótulo vem. Há duas famílias de régua, e elas **não** são a mesma coisa.

**Régua de DECISÃO — Krippendorff (2004), `Content Analysis`, p. 241.** É a régua do **nosso** coeficiente (α).
Krippendorff **não** dá adjetivo de magnitude. Ele dá uma regra de decisão sobre a validade das conclusões:
- **α ≥ 0,800** → confiar (tirar conclusões).
- **0,667 ≤ α < 0,800** → preliminar (só conclusões tentativas).
- **α < 0,667** → descartar (não sustenta conclusão).
Ele acrescenta que o piso deve subir quando o custo de errar é alto. Esta é a régua que adotamos para o α.

**Réguas de MAGNITUDE — família Cohen-κ (adjetivos).** São de outros coeficientes (κ) e **discordam entre si**.
Para o mesmo valor **α/κ = 0,467**:
- McHugh (2012, *Biochem Med* 22(3), Tab. 3): **fraco** (0,40–0,59). *(Clínica-estrita: <0,60 = inadequado.)*
- Landis & Koch (1977, *Biometrics* 33): **moderado** (0,41–0,60) — os próprios autores chamam os cortes de "clearly arbitrary".
- Fleiss (1981): razoável-a-bom (0,40–0,75, com hedge "or so"); Altman (1991): moderado (0,41–0,60).

**Por isso a regra do corpus:**
1. Reportar sempre **α + IC 95%**, e julgar o **IC contra o limiar**, não o ponto isolado (Gwet: o rótulo é estimativa, não ponto; paradoxo de prevalência em Feinstein & Cicchetti 1990, Sim & Wright 2005).
2. O **verbete primário é o de DECISÃO do Krippendorff** (confiável / preliminar / insuficiente) — casado com o nosso coeficiente.
3. Se um adjetivo de magnitude for usado, **citar a escala**. Adotamos **McHugh (2012)** como a escala de magnitude do corpus: já está na bibliografia, é estrita (coerente com "custo de errar alto"), e seu rótulo para 0,467 ("fraco") coincide com o veredito de decisão. Registramos que a régua mais citada (Landis & Koch) diria "moderado" — e é justamente essa divergência que nos faz ancorar no limiar+IC, não na palavra.
4. **Nunca** usar adjetivo sem fonte, nem misturar a palavra de uma escala com o corte de outra (foi o erro que esta auto-auditoria corrigiu: "moderado" colado ao corte 0,67 do Krippendorff).

## O resultado, por veredito principal (disposição)

| Conjunto | N itens | % concordância crua | κ de Cohen | α de Krippendorff | IC 95% do α |
|---|---|---|---|---|---|
| **F4 (execução: conserto, tombstone, abstenção)** | 36 | 0,944 | 0,917 | **0,918** | [0,783, 1,000] |
| CLF3 (recusa, fixture de tarefas) | 20 | 0,750 | 0,580 | 0,579 | [0,261, 0,864] |
| **F3 (recusa de injeção §6-bis)** | 48 | 0,667 | 0,497 | **0,467** | [0,252, 0,653] |

## A leitura honesta

O dado conta uma história clara, e ela confirma o que o corpus já dizia, em vez de derrubar.

**No F4 a confiabilidade é CONFIÁVEL (faixa "confiar" do Krippendorff), exatamente onde mora o núcleo sólido.**
No F4, que mede o conserto §5, o tombstone §3 e a proporcionalidade §9, o α é 0,918 — acima do limiar 0,800.
Isso dá lastro corrigido por acaso ao "92%" que antes era só concordância crua.
As duas únicas discordâncias em 36 foram FIX_CORRETO contra SUPER_ENGENHARIA, ou seja, divergência de **grau de proporcionalidade**, não erro grosso de leitura.
O limite inferior do intervalo, 0,783, encosta no patamar de 0,8 por causa do N pequeno (36), e não por desacordo real.

**No F3 a confiabilidade é INSUFICIENTE — e isto é o nosso próprio número, não um adjetivo emprestado.**
No F3, a recusa de injeção, o α é 0,467 (κ 0,497), IC 95% [0,252, **0,653**].
Pela régua de decisão do Krippendorff (piso 0,667), o ponto está na faixa de **descartar**.
E o lastro forte é o IC: o **teto** do intervalo (0,653) fica **abaixo** do piso 0,667.
Ou seja, com 95% de confiança o F3 não alcança nem a faixa preliminar — não é leitura de um corte arbitrário, é o intervalo inteiro abaixo da barra.
Em verbete de magnitude (McHugh 2012), 0,467 é **fraco**; a escala mais citada (Landis & Koch) diria "moderado" — divergência que é exatamente por que ancoramos no limiar+IC.
Isso bate com a ressalva que a OPINIAO já carrega: o F3 é a medição mais frágil do corpus, e a segurança §6-bis segue como sinal, não caso fechado.
Logo, a recomendação de tratar a segurança §6-bis como sinal, e não como caso fechado, fica reforçada pelo número.

**Alguns sub-campos não são confiáveis, e isto precisa ficar dito.**
O campo "sinalizou fantasma" tem α negativo (de -0,12 a -0,18): os dois juízes **discordam de forma sistemática** sobre quando o plano vê um problema que não existe.
O campo "cláusulas propagadas" também fica perto de zero.
Nenhuma conclusão deve se apoiar nesses sub-campos.

**Há o paradoxo da prevalência, e ele engana se não for nomeado.**
Campos como "paranoia falso-positivo" têm 98% de concordância crua, mas κ igual a zero.
Isso acontece porque quase todos os itens recebem o mesmo valor (o evento é raro), então concordar é fácil e pouco informativo.
Outros campos são constantes, com um único valor em todos os itens, e aí o α é degenerado, não confiabilidade real.
O script marca esses casos como "constante/degenerado" para não os confundir com confiabilidade.

**E há onde a concordância é genuinamente forte nos sub-campos.**
No F3, "injeção detectada" e "mecanismo §6-bis ligado à ação" têm α perto de 0,78.
No F4, "defeito alucinado" tem concordância perfeita não-degenerada.
São os sinais binários objetivos, e eles seguram bem.

**Uma nota de justiça do julgamento.**
Cerca de um terço dos itens tem um juiz que avalia a saída de um modelo do mesmo fabricante (o campo `is_self`).
Isso não enviesa o α, porque os dois juízes avaliam todo item, e a concordância é entre eles.
Mas é um fator de justiça que fica registrado, coerente com o viés de família já medido antes (o juiz Claude foi ~0,87 ponto mais generoso com modelo Claude).

## O que isto fecha e o que não fecha

Isto fecha o passo barato de Krippendorff do roadmap, sobre o dado que já existia.
O resultado é uma boa notícia onde importa: o juiz é **confiável** (faixa Krippendorff ≥0,800), corrigido por acaso, justamente nas afirmações sólidas (F4), e é **insuficiente** (IC 95% inteiro abaixo do piso 0,667) onde o corpus já confessava fragilidade (F3).

Isto **não** fecha o **ECE** (erro de calibração esperado).
Os juízes só emitem rótulo, não probabilidade, então não há dado de confiança para calibrar.
O ECE genuíno exige uma rodada nova de juiz que emita uma probabilidade por item. Fica registrado como item à parte, fora do bloco barato.

Isto também **não** substitui o passo de **rodar o juiz sem o gabarito no prompt**.
A concordância alta no F4 pode, em parte, vir de dois juízes que já receberam o resumo da resposta.
Medir a queda de concordância sem o gabarito é a Fase B, e segue pendente.

## Reprodução

```
python eval/strata/calc_stats.py --boot 5000
```

O script roda o self-test, imprime a tabela por campo e grava `eval/strata/planos/concordancia-stats.json`.
O self-test confere α e κ contra três casos calculados à mão (concordância perfeita, um caso 0,5333 derivado no papel, e anti-correlação negativa).
