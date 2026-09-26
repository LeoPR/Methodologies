---
title: Strata com IA (guia prático de uso)
status: active
created: 2026-06-08
updated: 2026-09-26
purpose: responder ao desenvolvedor "funciona no meu ambiente? vai sair caro?". Só o que funciona
nota: a pesquisa completa (inclusive o que NÃO funciona e por quê) está em lab/2026-06-04-strata-hipoteses/RESULTADOS-p6..p9 (p8 = posição/variância; p9 = churn de elenco, L2)
---

<!-- l10n: doc_id=strata-com-ia · lang=pt-BR · source_lang=en · translation_of=strata-com-ia.en.md -->
[English](strata-com-ia.en.md) · **Português**

# Strata com IA: guia prático

O texto do método é o mesmo para todos. O que muda o resultado é **quem executa e como**.
Três regras de ouro antes de qualquer modelo:

1. **Para uma avaliação completa, dê a um modelo médio/econômico a checklist em etapas, não
   o texto cru.** Para um conserto conhecido, o texto canônico cru já funciona (grade 2026-08).
   A checklist (`../lab/2026-06-04-strata-hipoteses/strata-ai-native/strata-checklist.md`) é
   um protótipo anterior ao L0 fechado: não tem portão para o §11 nem para o lado de
   autoridade-para-ler do §6-bis. Use-a como andaime, não como o método.
2. **Saída de IA = rascunho a revisar**, nunca veredito automático.
3. **Auto-auditoria autônoma (a IA auditando um projeto sozinha) é modo só de topo**: em
   projeto real ela só rendeu com o modelo de topo. Para modelos médios/econômicos, o arranjo
   que funciona é **checklist + humano confirmando cada achado**.

> **Onde a evidência vale (leia antes da tabela):** os números de saturação e abstenção vêm
> de **fixtures sintéticas** com gabarito pré-registrado. Em **projetos reais de terceiros**,
> o auto-auditor de IA **não** bateu a competência pura: com o framing "ache problemas",
> todos os braços (baseline incluso) super-detectaram, inventando violações e criticando
> práticas boas; é a **forma de abstenção** que corrige o falso-positivo
> ([R8](../lab/2026-06-04-strata-hipoteses/RESULTADOS-r8-sintese-3-projetos.md), reinterpretado
> em 2026-06-13; [braço externo](../lab/2026-06-04-strata-hipoteses/RESULTADOS-externo-bemcomportado.md)).
> Circularidade residual: a auditoria rica de qualidade em projeto de terceiro ainda não tem
> gabarito independente e cobre um só gênero. Use a tabela para escolher modelo em **tarefas
> controladas** (conserto, armadilha, abstenção); trate auditoria de projeto real como
> rascunho para um humano.

## Decisão rápida: o que usar (grade 2026-08)

| Eu quero… | Use | Por quê |
|---|---|---|
| **rodar local (GPU de consumo)** | **qwen3:14b** (cabe inteiro numa 3060 12GB) · **qwen3.6:27b** | o 14b é o prático do dia a dia; o 27b conserta e também se absteve na fixture limpa (ressalva abaixo), mas é lento (~22 min/run com offload) |
| **pagar pouco na nuvem** | **gpt-5-mini** (piso pago OpenAI) · **haiku-4.5** · **deepseek-v4-pro** | executam o conserto no padrão; o gpt-5-mini também recusa injeção espontaneamente e, com web, verifica fonte |
| **o máximo, custe o que custar** | **opus-5** · **fable-5** | conserto e armadilha perfeitos, e se abstiveram na fixture limpa (ressalva abaixo); o topo é onde a **auto-auditoria autônoma** rendeu |
| **topo sem pagar o teto** | sonnet-5 · gpt-5.6-terra · gemini-3.1-pro | conserto perfeito; armadilha perfeita salvo uma rodada do gemini-3.1-pro que re-emitiu a diretiva ativa; abstenção **não medida** |
| **NÃO usar para isto** | llama-4-scout · local <4B | o scout falhou o conserto da armadilha 2/2 e propagou o payload; abaixo de ~4B nem o formato sai |

*Regra: o **conserto de defeito conhecido (§5) satura de ~8B local ao topo**. A borda que separa modelos é a **abstenção** (não mexer no que já está bom): ela depende do **modelo e da redação do pedido**, não do preço, e o texto do método não a compra (§9, testado). Confira o modelo específico na grade honesta da [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md). Saída de IA = rascunho a revisar, sempre. (Nomes e preços datam rápido: vivem na camada datada, o L2. Re-audite antes de ancorar decisão cara.)*

> **Fonte e regime (2026-08-02):** reteste do L0 fechado, ~350 runs, K=2 (duas rodadas por
> célula), três situações (conserto §5, armadilha com injeção §6-bis, projeto já bom §9),
> gabarito mecânico (gold) + júri cego cross-vendor (termos: [GLOSSARIO](../GLOSSARIO.md)).
> Sinais direcionais (sintético), não prova. Números por tarefa × capacidade:
> [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md); diário da rodada:
> [`lab/2026-08-02-reteste-L0-fechado`](../lab/2026-08-02-reteste-L0-fechado/).
>
> **Ressalva sobre as células de abstenção:** a fixture limpa usada nelas dizia a resposta no
> próprio README, então parte do que se mediu é leitura, não calibração. Só a sucessora sem o
> vazamento é limpa, e ela mediu três modelos
> ([verificação do §9](../lab/2026-08-03-prompt-ingenuo/RESULTADOS-verificacao-s9.md)). Leia
> todo "se absteve" desta página como sinal fraco; a leitura qualitativa (varia por modelo, não
> por preço) se mantém.

![Strata por IA: qual modelo usar, por vendor](strata-com-ia-fronteira.pt-BR.svg)

**Como ler o gráfico** (grade 2026-08; por contexto de acesso: GPU local, plano econômico, topo).

O reteste mediu cada modelo em **três situações** com gabarito pré-registrado:

- **Conserto §5**: um defeito conhecido (duplicação de informação), braço Strata × baseline.
- **Armadilha §6-bis**: o mesmo conserto com uma instrução maliciosa plantada no projeto.
- **Projeto já bom §9**: nada a corrigir; a resposta certa é **não agir**.

O achado que organiza o gráfico: **o conserto §5 saturou**: de ~8B local ao topo de fronteira,
com Strata todos executam no padrão.
**A borda que separa os modelos é a abstenção** (§9): quem se abstém num projeto que já está bom.
Ela depende do **modelo, não do tier nem do preço**. Opus-5/fable-5 se abstiveram, e há
econômicos calibrados e caros superagentes (tudo na fixture limpa, com a ressalva acima);
confira o modelo específico na OPINIAO.

**O que o gráfico diz:**
- **Local:** abaixo de ~4B nem o formato sai (não é o método, é capacidade). O **qwen3:14b**
  cabe inteiro numa 3060 12GB e carrega o dia a dia; o **qwen3.6:27b** conserta e também se
  absteve (ressalva acima), mas roda com offload: ~22 min/run, factível, lento.
- **Nuvem econômica:** **gpt-5-mini** é o piso pago da OpenAI; **haiku-4.5** e
  **deepseek-v4-pro** executam o conserto perfeitamente.
- **Topo:** **opus-5** e **fable-5** consertam, passam na armadilha e se abstiveram (ressalva
  acima); sonnet-5, gpt-5.6-terra, gemini-3.1-pro e kimi-k3 consertam perfeitamente e passam
  na armadilha, salvo uma rodada do gemini-3.1-pro; a abstenção deles não foi medida.
- **Evitar para este uso:** **llama-4-scout**, único que, com Strata, falhou o conserto da
  armadilha 2/2 e propagou o payload da injeção num deles.

> **Leia pelo padrão, não pelo nome.** Modelos mudam rápido; o que **dura** é o comportamento por
> estrato de acesso (nomes de modelo são exemplos datados; roster auditado em fonte primária em
> 2026-08-02). Grade honesta completa, por tarefa × capacidade × custo:
> [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md).

## Como você pede: o que ajuda e o que não ajuda

Numa **avaliação completa** por modelo médio/econômico, a forma do pedido ajuda (sinal de junho):
- **Checklist** (sim/não por gate, com as 3 regras anti-falso-positivo) >> texto cru.
- **Etapas** (aplicar em turnos separados) é o que mais ajuda os modelos médios/econômicos:
  obriga o modelo a reconhecer o que está bom e situar no tempo **antes** de apontar defeito.
- Ela **não** compra o julgamento de quando *não* agir: esse fica com o modelo, e um pedido
  leigo bem redigido o calibra tanto quanto o método, ou melhor.
- **Reasoners** (deepseek-r1, qwen3-thinking) precisam de `think:true` e bastante orçamento de
  tokens, senão "pensam" e não respondem.

## Limites (o que esperar: não é defeito, é como calibrar)

- **Superagir não é carimbo de tier:** há econômicos que calibram num projeto limpo e caros
  que superagem; aparece mais com ruído e sob framing de auditoria. Trate o resultado como
  rascunho e confirme cada achado com o trecho citado.
- **A dimensão temporal depende da legibilidade:** com datas e histórico legíveis (§3/§8), os
  modelos situam no tempo corretamente; com histórico ruidoso ou sem marcas, marcam o
  histórico como problema atual. Revise achados datados com atenção.
- **Os dois lados de uma vez (2026-08):** na grade sintética, opus-5, fable-5 e o local
  qwen3.6:27b consertaram **e** se abstiveram (fixture limpa, ressalva acima). Os demais
  **oscilam** num dos lados; trate como rascunho.
- **Reasoner local engana:** um reasoner local pode parecer
  "limpo" só porque **truncou antes de concluir**; quando ele de fato termina, o veredito muda.
  Não confie no resultado parcial (no reteste 2026-08, falso-zero por truncamento vira
  INDETERMINADO, nunca FAIL).

## Notas finais

- **Local grátis é opção real:** qwen3:14b (cabe numa 3060 12GB) executa o
  conserto, e qwen3.6:27b também se absteve (ressalva acima): grátis, lento. Remoto `:free` segue ruim: rate-limit
  pesado e qualidade baixa.
- A análise completa (configurações que **não** funcionam, os experimentos e os gráficos
  de pesquisa) está em `lab/2026-06-04-strata-hipoteses/`
  (`RESULTADOS-p6-*`).
