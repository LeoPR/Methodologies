---
title: Fechamento da avaliação do Strata — honestidade, gaps e convergência ao ideal
status: 'aberto — auditoria adversarial de 5 dimensões; a tese é direção forte, não prova'
created: 2026-06-20
updated: 2026-06-20
---

# Fechamento da avaliação do Strata

## O que este documento é

Este é o fechamento honesto da avaliação do Strata.
Cinco dimensões foram auditadas de forma adversarial: o harness, os juízes, as fixtures, as métricas e as próprias afirmações.
As cinco chegaram ao mesmo nível: DIRECIONAL.

Aqui, fechado não quer dizer provado.
Fechado quer dizer direção forte, com os gaps mapeados e nomeados.
A tese tem evidência consistente que aponta para um lado, mas ainda não tem o poder estatístico, nem a quebra de circularidade, que a transformariam em prova.

## O veredito em uma frase

A avaliação foi parcialmente honesta, e isso é um elogio qualificado.
A honestidade da confissão é quase exemplar, porque o corpus carrega no topo o que não sabe.
A honestidade do desenho ainda é direcional, porque sobrou um over-claim de número (já corrigido) e dois confounds principais seguem declarados sem serem reduzidos: a circularidade e o completion-only.

## O que está sólido

Há um núcleo pequeno e firme, e ele está corretamente restrito na entrega.

O conserto de defeito conhecido é sólido.
Diante de uma informação que virou duas (§5) ou de algo antigo a aposentar (§3), o método leva a IA a consertar sempre do mesmo jeito, rastreável, preservando o histórico.
Esse caso é sólido porque ancora em ação de arquivo objetiva, passa o GOLD-gate em 100%, e o ganho cai justamente no degrau fraco, como a teoria previa.
Vale até no modelo econômico.

O limite-mãe é declarado com rigor raro.
O harness mede texto, não um agente agindo com ferramentas reais.
Isso aparece em muitos documentos, não está enterrado, e a arquitetura honra a afirmação, porque o modelo só emite texto e um sandbox externo grava, com risco zero ao alvo.

A autocorreção é real.
O arco que derivou foi caçado e marcado como superado.
A revisão retroativa rebaixou a tese-mãe a direção, transformou a temporalidade em não-achado, e subiu o R8 (o método piora no real) ao topo da opinião.

## O que é só sinal

Quase tudo que fala do mundo real é sinal, não prova, e a OPINIAO já diz isso.

A conclusão ecológica repousa sobre uma base fina.
São N=1 em cada célula que importa, com framing único que já prima abstenção, digest curado pelo dono e família circular.
Não existe uma única célula ecológica que combine, de uma vez, projeto externo, N maior ou igual a 5, juiz não-Claude, gabarito independente e dois framings.

A convergência dos juízes é mais frágil do que parece.
Os prompts dos juízes entregam o resumo do gabarito, então a concordância de 92% e 56% mede dois juízes que já sabem a resposta concordando, e não julgamento cego.
E os números-headline saem de poucas observações.

## Os gaps que carregam quase tudo

Dois confounds principais estão declarados, mas não foram reduzidos, e o ideal exige reduzir, não só confessar.

A circularidade não foi quebrada de verdade.
O projeto, o gabarito e o método são da mesma família.
O ataque externo ainda é fraco, porque tem um fixture só, o juiz dessa rodada recente foi Claude, e os dois modelos pegaram a mesma inconsistência.

O completion-only não foi superado em nenhuma célula.
Como o produto-alvo é um agente com ferramentas, a transferência das conclusões para o uso real é não-testada.
Esse é o maior gap de validade externa.

Os juízes foram cross-vendor, e não Claude sozinho.
O F0 usou 9 juízes de 3 fabricantes, dos quais 7 convergiram.
O R6 trouxe um 2º juiz não-Claude (gpt-4.1-mini), que fechou o caveat de juiz único nas conclusões da nuvem, incluindo o reteste-limpo.
O F4 teve 92% de concordância entre 2 juízes não-Claude, além da conferência mecânica objetiva da abstenção §9.
O resíduo é estreito: as rodadas ecológicas mais recentes deste ciclo (projetos próprios, fg2p, deepseek) foram pontuadas por juiz Claude, e ainda não foram re-pontuadas cross-vendor.

Somam-se a esses os gaps de medida.
Não há correção por acaso (Krippendorff) nem calibração (ECE) em nenhum número.
A temperatura não foi mapeada nos runners que geram o sólido.
E o N fica abaixo de 5 em toda célula.

## A convergência ao ideal

| Dimensão | Nível | Onde está em relação ao ideal |
|---|---|---|
| Harness e regime | DIRECIONAL | O limite text-only é declarado e honrado. Mas mede a temperatura única 0,3, sobre digests não validados, com o fix do reasoner só no F3. Sólido onde ancora em ação de arquivo. |
| Juízes | DIRECIONAL | O argumento e o auto-ceticismo são fortes. Mas o juiz tem o gabarito no prompt, a verdade-base é família única, e Krippendorff/ECE/PoLL estão planejados, não medidos. |
| Fixtures e circularidade | DIRECIONAL | As disciplinas do ideal operam (pré-registro por hash, hash congelado, scoring cego, R8 de primeira classe). Mas a conclusão ecológica é N=1, circular, framing único. |
| Métricas | DIRECIONAL | Separa acurácia de precisão, publica N e K, e autocorrige. Mas não re-mediu o bug do s04, não aplica a régua de precisão ao próprio juiz, e não tem correção por acaso. |
| Afirmações e tese | DIRECIONAL | A revisão retroativa fez autocorreção genuína. Restava um over-claim de número (dizia 9 juízes; o real é 7 de 9), já corrigido. O caveat de "juiz único nas células decisivas" estava latente e desatualizado, porque o R6 já o fechara na nuvem; foi corrigido aqui. |

Nenhuma dimensão está EM-DERIVA, porque o arco que derivou foi tombstoneado.
Nenhuma está CONVERGIDA por inteiro, exceto o núcleo §5-fix e §3-tombstone por execução no sintético.

## O que falta para fechar (priorizado)

Os passos baratos, que convertem sinal em evidência sobre o dado que já existe:

1. **Feito hoje:** corrigir o número dos juízes na OPINIAO (de 9 para 7 de 9) e reaproximar o escopo do F0 da afirmação.
2. Re-pontuar o s04 corrigindo o bug do `docs-reproducao.md`, e re-publicar a contagem de inventados, em vez de afirmar que o ranking não muda.
3. Calcular Krippendorff (com IC) e ECE sobre os vereditos já coletados. Os JSON já existem.
4. Re-pontuar as rodadas ecológicas recentes (R8, P10, próprios, fg2p) com um 2º juiz não-Claude. O reteste e a abstenção §9 já têm cross-vendor (R6, F4); falta só o braço ecológico recente. É re-análise barata sobre dado existente.
5. Rodar um subconjunto de juiz sem o resumo do gabarito no prompt. Se a concordância cair, o 92% vinha da dica.
6. Aplicar o ADR-006 ao próprio juiz: K maior ou igual a 5, temperatura acima de 0, e reportar o flip-rate.

Os passos caros, que pedem dado novo:

7. Cruzar o framing: rodar o mesmo fixture sob "ache problemas" e sob "abstenção-primeiro". É o único corte que desconfunde ruído de framing.
8. Quebrar a circularidade: pelo menos 2 repositórios de terceiros, gabarito pré-registrado por quem não escreveu o método, e juiz não-Claude.
9. Construir a ponte texto para agente: rodar uma célula-âncora com o modelo chamando de fato uma ferramenta de escrita de arquivo.
10. Validar o digest: rodar digest-cru contra digest-capado na mesma célula. Se o veredito virar, a sub-detecção era artefato de filtro.
11. Acrescentar uma segunda família de fixture em pelo menos um eixo, para mover "sólido num ponto" para "sólido".

## A moldura honesta

Fechar a avaliação não é declarar a tese provada.
É declarar que a direção é forte, que os gaps estão mapeados, e que o caminho para a prova está escrito e priorizado.

O método pratica o próprio Strata, porque anota e não reescreve, e porque mantém o traço.
O que falta agora não é mais confissão.
O que falta é executar os passos acima.
Enquanto eles não rodam, a frase certa continua sendo a que o corpus já adotou: tudo aqui é sinal e direção forte, não prova.
