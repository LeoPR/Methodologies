---
title: Estilo de redação dos documentos
status: active
created: 2026-06-20
updated: 2026-06-20
---

# Estilo de redação dos documentos

Simples não é pobre.
Simples é escrever de forma completa, com frases inteiras, e deixar a página visualmente agradável.

Vale para todo documento que uma pessoa lê: README, guias, opinião de uso, status.

## De onde vem este estilo

Este estilo segue a **Linguagem Simples** (em inglês, *Plain Language*).
É o movimento de comunicação clara para quem lê, hoje com norma técnica própria.

A Linguagem Simples dá a base: escreva para o seu leitor, em palavra comum, com voz ativa.
A tradição brasileira de redação acrescenta a amarração: clareza, concisão, coesão e coerência.
A escola de **escrita escaneável** acrescenta o formato: uma ideia por bloco, página que se varre com os olhos.

As fontes que ancoram cada peça:

- **ISO 24495-1:2023, *Plain Language — Part 1*** (ISO, 2023). A norma internacional. O texto deve ser relevante, encontrável, compreensível e acionável para quem lê.
- **Federal Plain Language Guidelines** (PLAIN, 2011) e o **Plain Writing Act of 2010** (EUA). A fonte canônica dos princípios: escreva para o público, voz ativa, palavra comum, frase curta, fale com "você".
- **Manual de Redação da Presidência da República** (Casa Civil, 2ª ed., 2002; atributos da 3ª ed., 2018). Define que conciso é dizer o máximo com o mínimo de palavras, cortando palavra inútil, nunca o pensamento. Define a coesão como o entrelaçamento entre frases e parágrafos.
- **Manual de linguagem simples** (gov.br, 2023) e a apostila de **Linguagem Simples no Setor Público** (ENAP, com Heloisa Fischer, 2021). A versão brasileira e oficial do movimento.
- **How Users Read on the Web** (Jakob Nielsen, NN/g, 1997) e **Letting Go of the Words** (Ginny Redish, 2012). A pessoa varre a página antes de ler. Por isso, uma ideia por bloco e listas.

## Os passos

1. Escreva para quem lê, na palavra comum.
   Pense em quem abre o documento e no que essa pessoa precisa saber.
   Use o termo técnico só quando ele é mesmo necessário, e explique quando ele aparece.

2. Prefira a voz ativa e fale com "você".
   Deixe claro quem faz o quê.
   A frase ativa é mais direta do que a passiva.

3. Escreva a frase inteira, com artigo e conectivo.
   Prefira "Esta é a forma de usar com a IA" a "uso com a IA (a forma)".
   A frase curta ainda é uma oração completa, com sujeito e verbo, não um fragmento.

4. Use conectivos de verdade para ligar as ideias.
   São eles: porque, então, mas, quando, para que, já que, ou seja.
   O conectivo é o que torna visível a relação entre uma ideia e a próxima.
   Por isso ele não é palavra inútil, e fica.

5. Seja conciso: corte o que não informa.
   Tire a redundância, o jargão e a palavra vazia.
   Mas preserve o artigo e o conectivo, porque eles dão a coesão.
   Conciso é economia de palavra, não economia de pensamento.

6. Para separar ideias do mesmo assunto, quebre a linha.
   Mantenha uma ideia por linha, mesmo dentro do parágrafo.
   A quebra de linha é mais econômica e mais consistente, e deixa a página fácil de varrer.
   Mas a quebra é para ideias **separadas**, não para cada cláusula de um mesmo argumento.
   Uma cadeia de raciocínio (A, logo B, logo C) lê-se melhor amarrada por conectivos do que picada em frases soltas, ainda mais quando o raciocínio é difícil.
   Avalie se a quebra ajuda; não a aplique de forma mecânica. Na dúvida, vale a orientação clássica de clareza.

   O mesmo vale para o travessão. A pergunta não é "tem travessão?", e sim "ele é mesmo necessário?".
   Muitas vezes a ordem narrativa (passo 7) dispensa o travessão; mas, para um aparte curto e genuíno, ele ainda é a ferramenta certa.

7. Comece pelo mais importante.
   Diga primeiro a conclusão, depois os detalhes.
   Em documento longo, resuma no início.

8. Use parêntese só para o que é mesmo acessório.
   Por exemplo: uma fonte, um número, um exemplo curto.
   Não repita entre parênteses o que a frase já disse.

9. Escreva pelo que a coisa é, não pelo que ela não é.
   Nomeie o que foi usado: "usamos o juiz Gemini e o GPT", e não "um juiz não-Claude".
   Só negue quando o texto já desenvolveu o contraste.
   Negar algo que o texto não introduziu é anti-informação, e o leitor não tem como verificar.
   É o mesmo da §3 do Strata: a superfície de leitura tem que se bastar sozinha.

## Antes e depois

- "Como usar com IA (a receita)"
  vira "Como usar com a IA".

- "Funciona até com IA econômica — a forma é a alavanca."
  vira "Funciona até com a IA econômica, porque a forma é a alavanca."

- "só o topo, ou um humano no loop — nisso não supera"
  vira "Sozinho, ele não supera a competência pura. Para isso, use o topo, ou fique no loop."

- "um 2º juiz não-Claude (gpt-4.1-mini)"
  vira "um 2º juiz, o gpt-4.1-mini".

## Por que isto importa

A língua existe para comunicar.
Quanto mais claro o leitor capta, mais correta foi a comunicação.
Por isso a régua final não é a forma em si, mas se o leitor entendeu.

## Onde isto não se aplica

O traço, ou seja, o histórico, pode ser cronológico por natureza.
Tabelas e o frontmatter podem ser mais densos, porque ali a forma é de dado, não de prosa.

O produto [`recipe/knowledge-architecture.md`](recipe/knowledge-architecture.md) é um caso à parte.
A redação dele é híbrida: uma pessoa precisa conseguir ler e entender, e ao mesmo tempo ele tem que ser eficiente para uma IA entender e aplicar.
Ali o leitor-alvo é a IA, então a densidade serve à aplicação, não ao conforto de leitura humana.
As orientações acima valem para os documentos que uma pessoa lê (README, guias, opinião de uso, status), não para o arquivo do produto.
