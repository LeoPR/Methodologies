<!-- l10n: doc_id=outreach-2026-08-linkedin-artigo · lang=pt-BR · canonical -->
[English](artigo.en.md) · **Português**

# Strata em agosto de 2026: o que os testes mostram quando a IA tenta organizar conhecimento

*Artigo técnico. Tudo que está afirmado aqui tem gabarito pré-registrado, execução registrada e
documento de resultados aberto no repositório. Onde o regime é fraco, o texto diz fraco.*

## O problema e o método

Todo trabalho longo acumula conhecimento: pesquisa, código, decisões, notas. Com o tempo ele
apodrece: você não acha o que decidiu, não sabe o que ainda vale, e a próxima ferramenta ameaça
obrigar a recomeçar. O Strata ataca isso com uma arquitetura em camadas de durabilidade:

- **Mneme (L0)**, a memória: os princípios que precedem o computador. Método, rastreabilidade,
  fonte única, história imutável. A pergunta-teste: "se a IA e o computador sumissem, isso
  continuaria verdadeiro?". Editorialmente fechado em 1º de agosto de 2026.
- **Morfé (L1)**, a forma: as formas maduras que dão corpo aos princípios (registros de decisão,
  histórico append-only, tombstones). Uma boa forma, não a única; troca-se sem tocar o núcleo.
- **Órganon (L2)**, o instrumento: as ferramentas de hoje, como a IA e o git. Destacáveis: quando
  a ferramenta morre, só esta camada muda.

A tese prática: trocar de ferramenta sem perder o porquê. O restante deste artigo é sobre como
testamos se uma IA consegue aplicar esse método de verdade, e o que respondeu.

## Como testamos

O laboratório é público e barato de reproduzir (a grade inteira sai por cerca de US$ 7). Os
princípios: cenários sintéticos controlados com gabarito mecânico pré-registrado; braços com e
sem o método sobre o mesmo projeto; júri cego de modelos de outros fabricantes; hashes de fixture
congelados; pré-registro antes de rodar. A métrica-mãe é a execução simulada: o modelo emite os
arquivos do conserto e um verificador mecânico inspeciona o estado final, sem juiz humano e sem
juiz de IA na porta principal.

Três situações organizam a grade: o **conserto §5** (duas fontes "oficiais" conflitantes do mesmo
fato; o certo é eleger uma canônica e aposentar a outra preservando o conteúdo), a **armadilha
§6-bis** (o mesmo projeto com uma instrução maliciosa plantada, "baixe e rode este script"; o
certo é recusar) e o **projeto já bom §9** (nada a corrigir; o certo é não agir).

## O que a geração atual de modelos já faz

**O conserto saturou.** De modelos de ~8B rodando numa GPU doméstica ao topo de fronteira pago,
com o método todos executam o conserto no padrão, com tombstone, ponteiro e história preservada.
Sem o método, os mesmos modelos falham na grade inteira: consertam de improviso, apagam histórico
ou propagam a duplicação. O contraste com e sem método é a medida-mãe do estudo, e é grande.

**A recusa de segurança sai espontânea.** Diante da instrução plantada, os modelos da geração
atual se recusam a executar, citam o princípio de que instrução lida de arquivo é dado, não
ordem, e neutralizam o conteúdo. Isso vale até no tier econômico. Exceção catalogada: um modelo
(llama-4-scout) falhou o conserto da armadilha nas duas tentativas e propagou o payload em uma.

**Na primeira célula com ferramentas reais, o padrão transferiu.** Com um agente em sandbox
executando de verdade, o conserto saiu em 10 de 12 casos com o método contra 2 de 12 sem, e
nenhum dos 24 rodou o comando malicioso.

## A borda real: saber não agir

O que separa modelos hoje não é consertar, é **abster-se**. Num projeto já bom, uns reconhecem o
bom e não tocam; outros inventam defeitos para justificar a tarefa. Essa borda é propriedade de
modelo: não ordena por preço, nem por tier, nem (agora medido) por idioma. Há econômicos
calibrados e caros superagentes. Consequência prática, que virou regra de produto: modelo médio
ou econômico trabalha com checklist e um humano confirmando cada achado; a auto-auditoria
autônoma, sem ninguém no loop, é modo de topo de fronteira.

E há uma ressalva ecológica que o projeto carrega no topo dos documentos: em projetos reais de
terceiros, com o pedido "ache problemas", todos os braços, inclusive o baseline, super-detectaram.
A forma de abstenção corrige o falso-positivo; o framing de caça, não. Por isso o método se vende
como organização assistida, não como auditor autônomo de projeto alheio.

## Português × inglês: a pergunta que faltava

O documento canônico do método é o inglês, mas toda a evidência tinha sido produzida em
português. Em 3 de agosto de 2026 fechamos a paridade: o núcleo da grade foi repetido em inglês
com roster idêntico, e um piloto separado mediu a recusa nos dois idiomas.

O resultado, em uma frase: **rode o método no idioma de quem lê e aplica**. O conserto e a
abstenção se reproduzem com paridade; o topo fecha 6 de 6 nos dois idiomas; o idioma do projeto
não move os números. Inglês não é melhor em nenhuma célula. E duas descobertas práticas: misturar
idiomas (método em inglês com instrução para responder em português) foi a pior configuração de
segurança do estudo inteiro, e há um sinal datado, fraco, de que modelos médios abertos recusam
injeção um pouco pior em inglês (5/8 × 1/8, duas execuções por célula; a confirmar com mais
volume se algum dia importar).

## O custo, medido

Uma auditoria de IA num projeto pequeno, método mais projeto na entrada e resposta na saída, sai
por cerca de **1 centavo** no modelo econômico de referência. Reproduzir a grade publicada
inteira custa cerca de **US$ 7**. O idioma move o custo em torno de 20%: o português tokeniza
mais caro que o inglês para o mesmo conteúdo, desigualdade de tokenizer documentada na
literatura, efeito real porém pequeno demais para dirigir decisão. A métrica que organiza o
valor é o **custo por projeto organizado**: uma passada de IA com o método custa menos que um
minuto de tempo humano, e a saída é rastreável, com o que mudou, por quê e sob que autoridade.

## O que isso não é

Sinais em cenários sintéticos controlados, não provas. Validação ecológica em andamento. Saída de
IA é rascunho a revisar, sempre. Modelos envelhecem rápido; os nomes citados são datados por
desenho, e o laboratório existe justamente para re-rodar quando a prateleira virar.

## Onde ler e verificar

Tudo aberto: método, guias de uso (qual modelo, qual idioma), experimentos, gabaritos e os
documentos de resultados por trás de cada número deste artigo.

👉 https://github.com/LeoPR/Methodologies

#GestaoDoConhecimento #ArquiteturaDeInformacao #InteligenciaArtificial #Metodologia #EngenhariaDeSoftware
