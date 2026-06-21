---
title: 'Alavancas — coisas notórias que fariam diferença: o que eu resolvo e o que só a massa resolve'
status: 'aberto — anotação viva de alto impacto; revisar a cada ciclo'
created: 2026-06-20
updated: 2026-06-20
---

# Alavancas que fariam diferença

Esta é a anotação das coisas notórias que mudariam o Strata de "direção forte" para algo mais firme.
Estão separadas em dois grupos, como o dono pediu.
O primeiro é o que **eu** (o dono e este trabalho) consigo tentar resolver.
O segundo é o que **só a experiência em massa** consegue dar, porque depende de muitos projetos, muitos modelos ou muita gente.

A regra para mover um item daqui é a mesma do resto: medir, e não só afirmar.

## Grupo 1 — o que eu posso tentar resolver

Estes pedem dado novo ou re-análise, mas estão ao alcance de um esforço focado.

1. **Fechar a circularidade que sobrou.**
   O braço de abstenção já rodou em terceiros.
   Falta levar a auditoria rica de qualidade a projeto de terceiro, com gabarito pré-registrado por quem não escreveu o método, e em mais de um gênero.
   É o item que mais aproxima o "vale em geral".

2. **Cruzar ruído e framing.**
   Rodar o mesmo fixture sob "ache problemas" e sob "abstenção primeiro".
   É o único corte que separa over-detecção de viés do pedido.

3. **Tirar o gabarito do prompt do juiz.**
   Rodar um subconjunto sem o resumo do gabarito.
   Se a concordância de 92% cair, ela vinha da dica, e isso muda como reportamos o juiz.

4. **Medir o que já está coletado.**
   Krippendorff com intervalo de confiança e ECE sobre os vereditos que já existem.
   O kappa entre o juiz e o ouro humano numa amostra.
   Os JSON já estão no repo, então é re-análise barata.

5. **Re-pontuar o que tem correção pendente.**
   O s04 com o bug do ponteiro corrigido.
   As células ecológicas recentes (P10, próprios, fg2p) com um 2º juiz de outro fabricante.

6. **Construir a ponte do texto para o agente.**
   Rodar uma célula-âncora com o modelo chamando de fato uma ferramenta de escrever arquivo.
   Hoje medimos a intenção do plano, não o agente agindo. É o maior buraco de validade externa que está ao meu alcance.

7. **Validar o digest.**
   Rodar digest cru contra digest capado na mesma célula.
   Se o veredito virar, a sub-detecção era artefato do filtro, não do método.

8. **Decompor L1 e L2.**
   Quase toda a detecção medida é L0.
   Pontuar "nomear formalização" (L1) e "ferramentas datadas" (L2) fecharia uma lacuna de cobertura que hoje é só afirmada.

9. **Empacotar para publicação.**
   Tabela-snapshot datada dos modelos, parágrafo de métodos sobre privacidade, e a regra de decisão pré-registrada do braço externo rico.
   Não é medir, é escrever o que já praticamos.

## Grupo 2 — o que só a experiência em massa resolve

Estes não se fecham com mais um experimento meu.
Eles dependem de escala: muitos projetos reais, muitos modelos ao longo do tempo, ou muita gente julgando.
Anoto para reconhecer o limite, e para saber o que pedir a uma comunidade ou a um uso em larga escala.

1. **A transferência para o produto agêntico real.**
   Saber se o ganho do Strata sobrevive dentro de um agente com ferramentas, em muitos projetos de muitos usuários.
   Uma célula-âncora minha indica; só o uso em massa confirma.

2. **O que é "já bom para o gênero".**
   A fronteira entre sub-detecção e "está bom para o tipo de projeto" muda com o gênero.
   Definir isso bem exige um corpus largo de julgamentos humanos sobre muitos tipos de projeto, não o gabarito de uma pessoa.

3. **A calibração da abstenção no mundo real.**
   Onde o modelo deve parar de agir varia com a base de código.
   O limiar honesto só emerge de muitos repositórios reais, não de uma fixture.

4. **O comportamento temporal de cara longa (F6).**
   Como a IA situa o que é antigo, superado, ou histórico ao longo de anos de um projeto.
   Precisa de muitos repositórios com história real e longa.

5. **A persistência da assinatura por tier ao longo do tempo.**
   Os modelos rotacionam (L2), mas a assinatura por tier parece durar.
   Confirmar isso pede cobertura contínua e ampla de modelos, ao estilo de um benchmark de comunidade que não persegue cada release.

6. **A segurança sob ataque real.**
   A recusa fraca cai sob paráfrase.
   Mapear o quão frágil ela é de verdade exige diversidade adversarial que só o red-team em massa produz.

7. **O ouro humano em escala.**
   O que pessoas de fato consideram um defeito, com concordância entre muitos anotadores.
   Sem isso, o juiz se valida contra a leitura de uma pessoa.

8. **As duas hipóteses de redação.**
   Se a disciplina de escrever claro de fato ensina (a camada de ensino L3/L4) precisa de muitos aprendizes.
   Se comprimir o texto deixa mais claro para a IA precisa de muitos modelos e tarefas.
   Ver [IDEIA-camada-ensino-redacao.md](IDEIA-camada-ensino-redacao.md) e [IDEIA-redacao-clara-para-ia.md](IDEIA-redacao-clara-para-ia.md).

## Como usar esta nota

O Grupo 1 alimenta o roadmap do [FECHAMENTO](FECHAMENTO-avaliacao-strata.md) e do [BACKLOG](BACKLOG-fila-geral.md).
O Grupo 2 é a fronteira honesta: o que o Strata só descobre se sair para o mundo.
Reconhecer o Grupo 2 é, em si, parte da honestidade do método, porque nomeia o que um esforço solo não alcança.
