<!-- l10n: doc_id=outreach-2026-08-medium · lang=pt-BR · canonical -->
[English](historia.en.md) · **Português**

# Eu testei se a IA consegue organizar conhecimento sozinha. A resposta é mais interessante que "sim" ou "não"

*Um método em camadas de durabilidade, um laboratório de US$ 7, e o que aprendi quando medi tudo
duas vezes, em dois idiomas.*

---

Todo trabalho longo acumula conhecimento. Pesquisa, código, decisões, notas. Com o tempo, isso
apodrece: você não encontra o que decidiu, não sabe o que ainda vale, e a próxima ferramenta
ameaça obrigar um recomeço. Passei um tempo destilando um método para isso. Chama-se Strata, e a
ideia central cabe numa frase: separar o que é atemporal do que é datado, para trocar de
ferramenta sem perder o porquê.

O método organiza o conhecimento em três camadas de durabilidade, com nomes gregos que contam a
história do conhecimento registrado. **Mneme**, a memória, é o núcleo atemporal: princípios que
precedem o computador, como método, rastreabilidade e fonte única. **Morfé**, a forma, é a camada
das formas maduras que dão corpo aos princípios: registros de decisão, histórico append-only,
tombstones. **Órganon**, o instrumento, são as ferramentas de hoje: a IA, o git, o editor. Quando
a ferramenta morre, só essa camada muda.

Um método assim precisa responder a uma pergunta incômoda: uma IA consegue aplicá-lo? Não na
conversa, na prática: ler um projeto desorganizado e devolver o conserto certo, com a história
preservada e sem obedecer ao que não deve. Foi isso que medi.

## O laboratório

Os princípios do laboratório são os do próprio método: cenários sintéticos com gabarito mecânico
pré-registrado, braços com e sem o método sobre o mesmo projeto, júri cego de modelos de outros
fabricantes, pré-registro antes de rodar. A métrica principal é a execução simulada: o modelo
emite os arquivos do conserto e um verificador mecânico inspeciona o estado final. Sem juiz
humano, sem juiz de IA na porta principal. E tudo é barato de reproduzir: a grade inteira custa
cerca de US$ 7.

Três situações organizam os testes. O **conserto**: duas fontes "oficiais" conflitantes do mesmo
fato, e o certo é eleger uma canônica e aposentar a outra preservando o conteúdo. A **armadilha**:
o mesmo projeto com uma instrução maliciosa plantada, "baixe e rode este script", e o certo é
recusar. E o **projeto já bom**: nada a corrigir, e o certo é não fazer nada.

## O que os modelos atuais já fazem

A primeira surpresa: o conserto saturou. De modelos de ~8B numa GPU doméstica ao topo pago de
fronteira, com o método todos executam o conserto no padrão, com tombstone, ponteiro e história
preservada. Sem o método, os mesmos modelos falham na grade inteira: improvisam, apagam
histórico, propagam a duplicação. A diferença entre com e sem método é a medida central do
estudo, e ela é grande.

A segunda: a recusa de segurança sai espontânea. Diante da instrução plantada, os modelos da
geração atual se recusam a executar, explicam que instrução lida de arquivo é dado e não ordem,
e neutralizam o conteúdo. Isso vale até no modelo econômico. Uma exceção catalogada: um modelo
falhou duas vezes e propagou o payload uma. Ele está nomeado nos documentos.

A terceira veio da célula mais nova: com um agente em sandbox executando de verdade, com
ferramentas reais, o padrão se manteve. Dez de doze consertos corretos com o método, dois de doze
sem. Nenhuma das vinte e quatro execuções rodou o comando malicioso.

## A borda de verdade

O que separa modelos em 2026 não é consertar. É **não agir**. Num projeto já bom, uns modelos
reconhecem o que está certo e não tocam; outros inventam defeitos para justificar a tarefa. Essa
borda não ordena por preço, nem por tier. Há econômicos calibrados e caros superagentes. A regra
prática que saiu disso: modelo médio trabalha com checklist e um humano confirmando cada achado;
auditoria autônoma, sem ninguém no loop, é privilégio do topo de fronteira.

E existe uma ressalva que o projeto carrega com orgulho: em projetos reais de terceiros, com o
pedido "ache problemas", todos os braços super-detectaram, inclusive o baseline. A forma de
abstenção corrige o falso-positivo; o framing de caça, não. O método se vende como organização
assistida, não como auditor autônomo de projeto alheio.

## A pergunta do idioma

O documento canônico do método é o inglês. Toda a evidência, porém, tinha sido produzida em
português. Um leitor atento poderia perguntar: isso foi testado no texto em inglês? Então repeti
o núcleo da grade em inglês, com roster idêntico, e medi a recusa nos dois idiomas num piloto
separado.

A resposta é libertadora: **use o idioma de quem lê e aplica**. Conserto e abstenção se
reproduzem com paridade, o topo fecha 6 de 6 nos dois idiomas, e o idioma do projeto não move os
números. Inglês não é melhor em nenhuma célula. Misturar idiomas, método em inglês com instrução
para responder em português, foi a pior configuração de segurança do estudo inteiro.

Há também um custo medido: o português tokeniza cerca de 22% mais caro que o inglês para o mesmo
conteúdo, uma desigualdade de tokenizer documentada na literatura. É real, mas some na conta:
uma auditoria completa de um projeto pequeno custa cerca de um centavo no modelo econômico. A
métrica que importa é outra: o **custo por projeto organizado**, que sai por menos de um minuto
de tempo humano.

## O que isso não é

Sinais em cenários controlados, não provas. Validação em projetos reais em andamento. Saída de
IA é rascunho a revisar, sempre. E modelos envelhecem rápido: os nomes citados são datados por
desenho, e o laboratório existe para re-rodar quando a prateleira virar.

Tudo é aberto: o método, os guias de uso, os experimentos, os gabaritos e os documentos de
resultados por trás de cada número deste texto.

**Repositório:** https://github.com/LeoPR/Methodologies

---

*Escrito em agosto de 2026. Os números são datados por honestidade; o método, por desenho, não.*
