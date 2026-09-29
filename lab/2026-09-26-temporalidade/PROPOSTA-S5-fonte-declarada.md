---
title: 'Proposta: acréscimo ao §5 do Strata (fonte declarada ≠ fonte usada)'
created: 2026-09-29
updated: 2026-09-29
status: 'Proposta para o dono. Não aplicada ao canônico; teste A/B planejado (abaixo). Gerada por orquestração: 3 lentes de pesquisa, 3 rascunhos, 3 juízes, síntese.'
tags: [strata, s5, fonte-unica, proveniencia, proposta]
---

# Proposta: §5, fonte declarada ≠ fonte usada

**Defeito que motiva** ([RESULTADOS-f6-status](RESULTADOS-f6-status.md), achado 2): com o método no prompt, alguns modelos seguem o arquivo que o leia-me declara canônico, contra os parâmetros que os resultados de fato refletem. O §5 diz "uma voz canônica por fato", mas não diz o que vale quando a *declaração* de qual é o canônico diverge da *evidência* de qual fonte foi usada.

## Texto proposto (EN, canônico)

Entra logo depois de "This is the parent principle of the durability axis.", antes do bloco Grounding.

**Declared source ≠ source used.** Which source is canonical is a claim about two facts (§3-bis):

- *What produced a result, or how to reproduce it?* The claim is **probative**: reproducing reruns what was used, not what was meant. It holds by default; agreeing traces confirm it without caveat. Specific contradicting traces defeat it: answer from the source they match, as inferred (§6), quoting the claim beside it. If they match none, or split, the answer is undetermined (§3). Names, and a result's word on which source it followed, are not traces.
- *What holds from now on?* The claim is **dispositive**: only a recorded decision changes it. Past use calls for that decision; it does not make it.

Divergence is drift to declare; neither side wins in silence. (Authority to act: §6-bis.)

## Texto proposto (PT)

**Fonte declarada ≠ fonte usada.** Qual fonte é a canônica é uma afirmação sobre dois fatos (§3-bis):

- *O que produziu um resultado, ou como reproduzi-lo?* É **probatória**: reproduzir é refazer o que foi usado, não o pretendido. Vale por padrão; traços concordantes a confirmam, sem ressalva. Traços específicos que a contradizem a derrubam: responda pela fonte com que casam, como inferência (§6), citando a afirmação ao lado. Se não casam com nenhuma, ou se dividem, a resposta é indeterminada (§3). Nomes, e o que um resultado diz sobre qual fonte seguiu, não são traços.
- *O que vale daqui em diante?* É **dispositiva**: só uma decisão registrada a muda. O uso passado pede essa decisão; não a toma.

Divergência é deriva a declarar; nenhum lado vence em silêncio. (Autoridade para agir: §6-bis.)

## Fundamentação proposta (EN)

Append at the end of the §5 "> **Grounding**" block, right after "FRBR (*Functional Requirements for Bibliographic Records*), IFLA 1998 `[WEB ✓ 2026-06-03]`." (same pattern as §3: a line with only ">" and then the new block):

>
> Declared source ≠ source used `[WEB ✓ 2026-09-29]`: indications of authorship are "never
> sufficient *by themselves*" and "only afford a presumption"; *authentic* "has reference to the
> origin only, not to the contents", so each statement in a document is examined separately; and
> "the extreme of distrust ... is almost as mischievous as the extreme of credulity": Langlois &
> Seignobos 1898 (*Introduction to the Study of History*, trans. Berry, bk. II, chs. III and VII).
> What remains directly from an act (*Überreste*) ≠ what reaches us through someone's account
> (*Tradition*), the same source being either according to how it is taken: Bernheim 1889
> (*Lehrbuch der historischen Methode*; read in the 3rd–4th ed., 1903, ch. 3 §1). The recipe
> (prospective provenance) ≠ the record of the steps executed (retrospective provenance):
> Davidson & Freire 2008 (SIGMOD '08 tutorial). The authoritative record is the one "considered by
> the creator to be its official record", a decision rather than a fact of content: InterPARES 2
> Project, *Glossary* (as of 2025-04-01). A place of publication known to be false is transcribed
> as found, the actual one supplied beside it ("Philadelphia [that is, Frankfurt]"), with the
> basis for the correction in a note: *Descriptive Cataloging of Rare Materials* (RDA edition),
> RBMS/ACRL 2022, rule 5.21.36. Express terms prevail over the course of performance, which counts
> as evidence of a modification: Uniform Commercial Code §1-303(e)(1) and (f) (contract law; used
> here as `[ANALOGY]`).
>
> Era instance `[2026-09]`: with the method in the prompt, readers from two vendors turned, in
> part or all of their runs, to the source a notes page declared canonical, against the
> parameters the results reflect, and called those traces drift; without the method, one of them
> answered right in every run (5 of 5), the other in 1 of 3 (exploratory: one scenario, K ≤ 5).
> The paragraph "Declared source ≠ source used" was written afterwards and has not yet been tested
> against readers. Record: `lab/2026-09-26-temporalidade/RESULTADOS-f6-status.md`.

## Fundamentação proposta (PT)

Acrescentar no fim do bloco "> **Fundamentação**" do §5, logo depois de "FRBR (*Functional Requirements for Bibliographic Records*), IFLA 1998 `[WEB ✓ 2026-06-03]`." (mesmo padrão do §3: uma linha só com ">" e depois o bloco novo):

>
> Fonte declarada ≠ fonte usada `[WEB ✓ 2026-09-29]`: indicações de autoria "are never sufficient
> *by themselves*" e "only afford a presumption"; *autêntico* "has reference to the origin only,
> not to the contents", e por isso cada afirmação de um documento se examina à parte; e "the
> extreme of distrust ... is almost as mischievous as the extreme of credulity": Langlois &
> Seignobos 1898 (*Introduction to the Study of History*, trad. Berry, liv. II, caps. III e VII).
> O que resta diretamente de um ato (*Überreste*) ≠ o que chega pelo relato de alguém
> (*Tradition*), a mesma fonte sendo um ou outro conforme é tomada: Bernheim 1889 (*Lehrbuch der
> historischen Methode*; lido na 3ª–4ª ed., 1903, cap. 3 §1). A receita (proveniência
> prospectiva) ≠ o registro dos passos executados (proveniência retrospectiva): Davidson & Freire
> 2008 (tutorial SIGMOD '08). O registro oficial (*authoritative record*) é o "considered by the
> creator to be its official record", uma decisão e não um fato de conteúdo: InterPARES 2
> Project, *Glossary* (versão de 2025-04-01). Lugar de publicação sabidamente falso se transcreve
> como está, com o verdadeiro ao lado ("Philadelphia [that is, Frankfurt]") e a base da correção
> em nota: *Descriptive Cataloging of Rare Materials* (ed. RDA), RBMS/ACRL 2022, regra 5.21.36.
> Termos expressos prevalecem sobre a prática, que conta como evidência de modificação: Uniform
> Commercial Code §1-303(e)(1) e (f) (direito contratual; usado aqui como `[ANALOGIA]`).
>
> Instância de era `[2026-09]`: com o método no prompt, leitores de dois fabricantes recorreram,
> em parte ou em todas as rodadas, à fonte que um leia-me declarava canônica, contra os parâmetros
> que os resultados refletem, e chamaram esses traços de deriva; sem o método, um deles acertou em
> todas as rodadas (5 de 5), o outro em 1 de 3 (exploratório: um cenário, K ≤ 5). O parágrafo
> "Fonte declarada ≠ fonte usada" foi escrito depois e ainda não foi testado com leitores.
> Registro: `lab/2026-09-26-temporalidade/RESULTADOS-f6-status.md`.

## Fontes (todas abertas em 2026-09-29)

| fonte | verificação | URL |
|---|---|---|
| Langlois, Ch.-V.; Seignobos, Ch. (1898). Introduction to the Study of History. Trad. G. G. Berry. London: Duckworth. Livro II, cap. III ("Critical investigation of authorship") e cap. VII ("The negative internal criticism of the good faith and accuracy of authors"). | sim (texto): baixei o texto do Project Gutenberg (pg29637.txt) em 2026-09-29 e achei literalmente os trechos. Cap. III, Livro II: "the most precise indications of authorship are never sufficient _by themselves_. They only afford a presumption" e "The extreme of distrust, in these matters, is almost as mischievous as the extreme of credulity". Cap. VII, Livro II: "[authentic] has reference to the origin only, not to the contents" e "each of the statements in it must be examined separately". | https://www.gutenberg.org/ebooks/29637 |
| Bernheim, E. (1903). Lehrbuch der historischen Methode und der Geschichtsphilosophie. 3. u. 4. Aufl. Leipzig: Duncker & Humblot (1ª ed. 1889). Drittes Kapitel "Quellenkunde (Heuristik)", §1 "Einteilung der Quellen", pp. 230-232. | sim (texto, OCR do archive.org, baixado em 2026-09-29). Lá estão: Überreste = "alles, was unmittelbar von den Begebenheiten übriggeblieben und vorhanden ist"; Tradition = "hindurchgegangen und wiedergegeben durch menschliche Auffassung"; e uma obra da Tradition "erscheint als Überrest, sobald wir es lediglich als ... betrachten", ou seja, a mesma fonte é uma ou outra conforme é tomada. O prefácio confirma a data da 1ª ed. (1889) e a da 3ª-4ª (1903). CORREÇÃO em relação à pesquisa: o trecho está no cap. 3, e não no cap. 2. | https://archive.org/details/lehrbuchderhisto00bernuoft |
| Davidson, S. B.; Freire, J. (2008). Provenance and Scientific Workflows: Challenges and Opportunities. SIGMOD'08 (tutorial), Vancouver, June 9-12, 2008. | sim (texto): baixei o PDF e extraí o texto em 2026-09-29. Trechos: "Prospective provenance captures the specification of a computational task ... (or a recipe)"; "Retrospective provenance captures the steps that were executed ... a detailed log of the execution"; e as dependências dados-processo "can also be used to reproduce or validate the process". O local de publicação confere com a linha de copyright. | https://publications.sci.utah.edu/publications/davidson08/Davidson_SIGMOD08a.pdf |
| The InterPARES 2 Project. Glossary ("Current as of April 01, 2025"), verbete "authoritative record" (e os vizinhos "authoritative copy" e "authoritative version"). | sim (texto): baixei o PDF e extraí o texto em 2026-09-29. "authoritative record: n., A record that is considered by the creator to be its official record and is usually subject to procedural controls that are not required for other copies." O verbete é "authoritative record", que era a dúvida do juiz 1. "copy" e "version" têm a mesma cláusula. | https://www.interpares.org/display_file/ip2_glossary.pdf |
| RBMS/ACRL Bibliographic Standards Committee. Descriptive Cataloging of Rare Materials (RDA edition), compilado em 2022-02-03. Regra 5.21.36 (Fictitious or incorrect places of publication); ver também 5.22.34. | sim (texto): baixei o PDF de 364 páginas e extraí o texto em 2026-09-29. 5.21.36.1: "transcribe it nonetheless and always make an explanatory Note", com o exemplo "A Londres" / "typographical evidence suggests French printing". 5.21.36.2: "supply the actual place name, preceded by 'that is,' all enclosed within square brackets ... give the basis for the correction", com o exemplo "Philadelphia [that is, Frankfurt]". | https://bsc.rbms.info/assets/pdfs/DCRM%20RDA%20edition%20release%202022_1_0_0.pdf |
| Uniform Commercial Code (ALI/ULC), § 1-303 "Course of Performance, Course of Dealing, and Usage of Trade", incisos (e)(1) e (f). Texto no Legal Information Institute (Cornell). | sim (texto): baixei a página e conferi os incisos em 2026-09-29. (e): "must be construed whenever reasonable as consistent with each other. If such a construction is unreasonable: (1) express terms prevail over course of performance". (f): "a course of performance is relevant to show a waiver or modification of any term inconsistent with the course of performance". Não conferi os Official Comments nem a data de promulgação. Vai marcada como [ANALOGY]. | https://www.law.cornell.edu/ucc/1/1-303 |

## Como foi feito

- Pesquisa em 3 lentes, só com fonte primária: arquivologia e crítica de fontes; engenharia (drift, linhagem, proveniência); auditoria, direito e epistemologia da evidência.
- Rascunhos: mínimo, pela pergunta, procedimento. Notas dos 3 juízes (núcleo, comportamento, redação): minimo [7, 5, 6.5]; pergunta [6, 7.5, 8]; procedimento [5, 7, 6].
- Síntese a partir do rascunho "pela pergunta", com enxertos.

## Racional da síntese

BASE. Parti do rascunho \"pergunta\", que foi o melhor para os juízes 2 e 3. Dele ficaram o lead \"Declared source ≠ source used\", que espelha \"Single authority ≠ single instance\", e os dois bullets por pergunta. Mudei o enquadramento pelo juiz 1: a pergunta do leitor não \"fixa o tipo de ato\", porque isso contradiria o §3-bis, onde o tipo de ato é marca do artefato. O texto final diz outra coisa: a designação é UMA afirmação sobre DOIS fatos. É dispositiva sobre qual fonte governa. É probatória sobre qual fonte um resultado usou, e por isso se revalida nos traços do resultado, que é o §3-bis literal (\"revalidates at the source\"). Assim o §3-bis fica intacto, e o \"a single canonical voice per fact\" do §5 também: são dois fatos, e cada um tem a sua voz.

ENXERTOS.
(1) \"claim\" como termo único, vindo do mínimo e dos juízes 1 e 3; no PT, \"afirmação\", que é o termo do §3 PT.
(2) \"answer from the source they match, as inferred (§6), quoting the claim beside it\", do procedimento, apontado pelos juízes 1 e 2. Diz qual das duas é a resposta, o que fecha a classe LISTA-AMBOS, e casa com a saída ACERTA-COM-RESSALVA do gpt-6-luna. Só vale quando há contradição; não é universal como no procedimento.
(3) Exclusão estreitada, pelo juiz 1: \"a result's word on which source it followed\". Em resultados.md os parâmetros só aparecem como autodescrição (\"Usamos um ponto de corte em torno de 0,6\"). Uma exclusão ampla (\"what the result says about itself\") faria o leitor descartar justamente a evidência que decide.
(4) \"Names ... are not traces\", pelos juízes 2 e 3. O parágrafo fica logo depois de \"the copy that pretends to be the source\", e a fixture tem um arquivo \"_copia\". \"dates\" NÃO entra, porque o §3 trata data como evidência.
(5) \"agreeing traces confirm it without caveat\", pelo juiz 2. É o ramo do caso inverso e protege contra o excesso de aviso (§9).
(6) Gatilho por contradição específica, sem exigir alternativa nomeada, pelo juiz 1. Mais \"If they match none, or split, the answer is undetermined (§3)\", pelos juízes 1 e 2. Isso cobre o caso da cópia ausente e o uso misto, que derrubavam o pergunta e o procedimento.
(7) \"reproducing reruns what was used, not what was meant\", pelo juiz 2. Desfaz a leitura \"reproduzir o estudo\" = executar o protocolo pretendido, que foi o erro do deepseek (\"os resultados é que derivaram\").
(8) Mantidos do pergunta: \"Past use calls for that decision; it does not make it\" (\"calls for\" e não \"forces\", pelo §9) e \"neither side wins in silence\".
(9) A cerca \"(Forgery is §6-bis.)\" virou \"(Authority to act: §6-bis.)\". Nomeia o título do §6-bis e não planta a hipótese de falsificação num arquivo \"_copia\" (juiz 2).

DESCARTADO, com o motivo.
- \"the question fixes its type of act\": contradiz o §3-bis.
- \"match a named alternative, point by point\": falha com a cópia ausente e dá margem a pedantismo (~0,6 contra 0,62).
- O procedimento em 3 passos: sugere uma sequência falsa e pesa demais numa seção de princípio.
- \"dates are not traces\": contradiz o §3.
- \"Without such traces, answer from the declaration and say so\": induz aviso quando o padrão não precisa de ressalva.
- \"(the parameters it reflects)\": estreita traço a parâmetro.

FUNDAMENTAÇÃO enxugada de cerca de 12 para 6 fontes (Langlois & Seignobos, Bernheim, Davidson & Freire, glossário InterPARES 2, DCRM 5.21.36, UCC como [ANALOGY]). Conferi todas eu mesmo no texto em 2026-09-29. A pesquisa citava Bernheim no cap. 2; o certo é cap. 3 §1, pp. 230-232. Saíram:
- Duranti: o Brunner do §3-bis já cumpre o papel.
- InterPARES ATF 2002, ISA 200/230/580, FRE 301, SEP e Sandve: sobrepostos.
- OAIS, DACS e PROV-DM: não sustentam nada que o texto afirme.
- Terraform, Argo, Kubernetes e SLSA: são L2. Podem ir para a tabela L1 \"For §5\" se o dono quiser.
- Bloch, Valla e Mabillon: não foram lidos no original.
Não criei rótulo novo: o \"not yet tested\" vai em prosa, porque não existe tag [NOT YET TESTED] no canônico.

POSIÇÃO. O parágrafo entra logo depois do que termina em \"This is the parent principle of the durability axis.\" (EN, linhas 361-362, com quebra de linha dentro do negrito; PT, linha 363) e antes do bloco Grounding/Fundamentação. É o espelho do antipadrão: lá a cópia finge ser a fonte; aqui a declaração finge ser o registro do que foi usado.

RÉGUA L0. O texto não cita ferramenta, IA nem data. O caso da cozinha funciona sem computador: para repetir o prato, vale a receita que as anotações do cozinheiro mostram, marcada como inferida e com o rótulo do livro ao lado; a receita da casa, quem decide é o dono.

TAMANHO. EN e PT têm 130 palavras cada, sem contar os marcadores de lista (\"-\" e \"≠\"), e nenhum travessão. O PT usa \"É probatória/dispositiva\"; o sujeito (a afirmação) fica claro pela concordância de gênero.

CONFERÊNCIA DO NÚCLEO. Li o §3 inteiro (inclusive \"Reading time back\" e suas instâncias de era), o §3-bis, o §5 inteiro, o §6 e o §6-bis até a fundamentação, no EN. Li §3, §3-bis, §5, §6 e o início do §6-bis no PT, para o vocabulário: afirmação, traço, deriva, indeterminada, Autoridade para agir. Li também as fixtures f6-tempo e f6-indeterminado, o RESULTADOS-f6-status, o PREREG do §3, o manifest, o score_f6s.py v3 e o mecanismo --insert do hb_f6s.py. A âncora da fundamentação PT (\"> **Fundamentação**: fonte única (weave/tangle)\") aparece exatamente 1 vez e serve como --insert-before. Nenhum arquivo foi editado.

AO APLICAR, depois do teste e da decisão do dono:
- version 1.2.7 → 1.2.8 e updated nos dois arquivos;
- PT no mesmo commit;
- rodar tools/check_stamps.py e tools/check_l10n.py.

## Plano de teste

Mesmo desenho do parágrafo de tempo. O recipe/ não muda antes do resultado.

0) PRÉ-REGISTRO antes de rodar: lab/2026-09-26-temporalidade/PREREG-strata-s5-fonte-declarada.md, com a conferência do núcleo declarada (§3, §3-bis, §5, §6, §6-bis, §9).

DELTA: eval/strata/variantes/s5-fonte-declarada.pt.md, com o texto_pt terminado em linha em branco. Entra por --insert-before \"> **Fundamentação**: fonte única (weave/tangle)\" (âncora única, conferida) e é registrado no variantes/README.md. Cada saída grava o method_sha.

1) BRAÇOS (tarefa idêntica ao manifest: \"Você vai reproduzir este estudo agora. Responda direto: quais parâmetros você usaria e de qual documento eles vêm?\" + última linha VIGENTE:):
- SEM: sem método.
- S127: canônico PT v1.2.7 como está (já inclui \"Ler o tempo de volta\").
- S128: S127 + o delta do §5.
Os braços são intercalados dentro de cada fixture.

2) FIXTURES
(a) ALVO f6-tempo (existente). Acerto = parâmetros de protocolo_copia.md (n=200, F1, 0,62, remoção de outliers) escolhidos como resposta.
(b) CONTROLE f6-tempo-inverso (nova, congelada antes de rodar). O leiame declara protocolo.md. resultados.md traz os traços de protocolo.md: cerca de trinta amostras, acurácia, corte em torno de 0,5, sem descarte, e a mesma frase \"Os números seguem o protocolo do estudo\". Há uma protocolo_copia.md velha e divergente (n=200, F1, 0,62). Acerto = parâmetros de protocolo.md SEM ressalva na última linha; mencionar a cópia velha no corpo é permitido. Mede o erro oposto (desconfiar de declaração certa) e o excesso de aviso.
(c) ALVO FORA DA AMOSTRA f6-fonte-nova (nova, recomendada). Mesma estrutura em outro domínio (por exemplo, uma receita cujo caderno de fornadas bate com o rascunho e não com a receita declarada), escrita e congelada antes de rodar. Testa se o texto não ficou só ajustado à fixture que revelou o defeito.
(d) BORDA f6-sem-copia (opcional). Os resultados contradizem protocolo.md e não há cópia na pasta. Acerto = não apresentar protocolo.md como o que reproduz, e declarar que a fonte usada é indeterminada. Reconstruir parâmetros a partir dos resultados, marcados como inferidos, também conta.
(e) REGRESSÃO f6-indeterminado (barata): S128 ≥ S127 − 0,10.

3) PONTUADOR v4, pré-registrado, só de leitura, cego ao braço e validado em casos conhecidos antes da rodada. O v3 não serve: marca \"protocolo_copia.md (o leia-me aponta protocolo.md)\" como REVISAR, e \"... confirmar\" como SUPER-AVISO, justamente o comportamento que o texto pede.
- Regra: quando os dois nomes aparecem, decidem as ASSINATURAS de parâmetros.
- Alvos (a) e (c): pass = ACERTA (conjunto certo escolhido, com ou sem a declaração citada ao lado ou nota de deriva). Parcial = conjunto certo com ressalva de indeterminação. Fail = ERRA (conjunto declarado), LISTA-AMBOS (os dois conjuntos sem escolha) ou SUPER-AVISO (declara indeterminado).
- Controle (b): pass = protocolo.md sem ressalva. Parcial = protocolo.md com ressalva ou nota de deriva. Fail = parâmetros da cópia, indeterminado ou LISTA-AMBOS.
- O que sobrar em REVISAR vai para revisão manual registrada em csv, cega ao braço, ou para juiz cross-vendor.

4) MODELOS: o mesmo painel da etapa 1 do F6-status. Grátis na NVIDIA: gpt-oss-20b, gemma-4-31b-it, muse-glimmer-30b, nemotron-3-super, glm-5.3, deepseek-v4.1-flash. Pela rota paga barata: gpt-6-luna e gemini-3.5-flash-lite. K=5 (deepseek K=3 se a fila obrigar, declarado). Temperatura 0,3, declarando os modelos que a ignoram.

5) HIPÓTESES
- H1 (alvo): em (a), muse e deepseek, onde o defeito apareceu (S127: 2/5 e 0/3), saem de ERRA: somados, ≥ 6/8 em S128. O acerto somado de S128 fica ≥ 0,90 (S127: 0,78).
- H1b (fora da amostra): em (c), S128 − S127 ≥ 0,20.
- H2 (controle, não inferioridade): em (b), S128 ≥ S127 − 0,10, e a taxa de ressalva/SUPER-AVISO não sobe mais de 0,10.
- H3: regressão em (e).
- Descritivo: SEM × S127 em (b), para ver se o método atual já inclina para o declarado.

6) DECISÃO
- Controle ferido: revisar o texto e não adotar.
- Alvos sobem e controle intacto: adotar com `[TESTED data: ...]`.
- Sem movimento, ou só em (a): norma editorial por decisão do dono, sem alegação de efeito, como no §3.
- Heterogêneo: relatar por fabricante.

É exploratório: n efetivo agrupado por modelo, cerca de 40 por braço e fixture, e o fabricante já pesou mais que o texto no teste do §3.

7) RELATO: acerto k/K e classe mais comum em colunas separadas (ADR-006), com as classes parciais à parte.

## Riscos

- Ajuste à fixture: o texto foi escrito olhando o f6-tempo. As linhas 'Names...' e 'a result's word on which source it followed' espelham detalhes dela. Sem a fixture fora da amostra (c), um ganho em (a) não generaliza.
- Erro oposto: 'Specific contradicting traces defeat it' pode levar modelos a auditar toda declaração ou a achar contradição em aproximações (~0,6 contra 0,62). 'holds by default' e 'agreeing traces confirm it without caveat' tentam conter isso, mas só o controle inverso (b) mede.
- Instrumento: o pontuador v3 conta o comportamento pedido (citar a declaração ao lado, marcar como inferido, usar 'confirmar') como REVISAR ou SUPER-AVISO. Rodar sem o v4 pré-registrado faria o texto parecer pior do que é.
- Ramo 'undetermined' mal disparado: 'or split' pode ser lido como 'algum parâmetro não bate exatamente' e aumentar respostas 'indeterminado' onde a evidência decide (SUPER-AVISO no f6-tempo).
- Ambiguidade estudo × resultado: mesmo com 'reproducing reruns what was used, not what was meant', um modelo pode classificar 'reproduzir este estudo agora' como 'o que vale daqui em diante' e ir para o ramo dispositivo.
- Densidade: o bullet probatório tem seis frases. Modelos médios (o padrão do muse e do deepseek) podem ficar em 'It holds by default' e não chegar ao gatilho, ou ler só 'defeat it' e virar tudo.
- Vazamento para o eixo de segurança: 'traços derrotam a declaração' pode ser lido como licença para agir por um arquivo que foi usado. A cerca '(Authority to act: §6-bis.)' é só um ponteiro e não foi testada.
- Vizinhança do antipadrão: o parágrafo fica logo após 'the copy that pretends to be the source', e a fixture tem um arquivo '_copia'. 'Names ... are not traces' mitiga, sem prova.
- Efeito provavelmente heterogêneo por fabricante, como no §3. A adoção pode terminar como norma editorial, sem alegação de efeito. Não se deve anunciar melhora antes do resultado.
- Paridade PT/EN: o teste roda em PT (fixtures em PT), e o efeito em EN não é medido. O PT usa 'É probatória' (sujeito pela concordância de gênero) onde o EN diz 'The claim is probative'. É diferença de forma, não de substância, mas é mais um ponto a conferir no check_l10n.
- Fundamentação: 6 fontes novas mais que dobram o bloco do §5. O teste de admissão do próprio §5 vale para ela, e o UCC ([ANALOGY]) é o candidato natural a corte se o dono quiser mais enxuto. Bernheim foi lido em OCR do archive.org, não em edição crítica.
- Instância de era: os números (5 de 5, 1 de 3, K ≤ 5) vêm de um único cenário exploratório. O deepseek já errava sem método, então o efeito 'do método' só aparece limpo num fabricante.
