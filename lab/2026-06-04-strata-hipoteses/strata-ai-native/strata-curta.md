---
project: Strata
form: prosa-curta (CONTROLE R4 — desconfundir comprimento × gate)
derived-from: knowledge-architecture.md v1.1.0
proposito: mesmo conteudo e tamanho curto da AN-v2, porem em prosa descritiva, sem
  instrucoes de verificacao nem ordem de aplicacao. Se este ~= AN, o ganho e comprimento;
  se AN >> este, e o formato (gate). Controle do confundidor comprimento x formato.
status: controle experimental — NÃO é a fonte canônica
---

# Strata — resumo curto (prosa)

O Strata organiza um corpo de trabalho em camadas de durabilidade e por alguns
princípios. Segue um resumo dos princípios; cada um descreve o que se espera, sem
instruções de verificação.

**§1 — Três tipos de artefato.** Tudo é traço (registro do que foi decidido ou feito,
ao qual só se acrescenta), superfície (o estado vivo e atual) ou conhecimento-vivo.
Confundir os três faz o corpo de trabalho apodrecer.

**§2 — As quatro perguntas.** Um corpo de trabalho deve permitir responder o que há ali,
por onde começar, o que vale agora e como usar ou entender aquilo. Documentação genérica
que não orienta deixa essas perguntas sem resposta.

**§3 — Rastreabilidade (traço × superfície).** Ao traço só se acrescenta; o registro
histórico não se apaga. A superfície, ao contrário, é rebaixada ativamente: o que morreu
é silenciado ou marcado como obsoleto. Código ou decisão abandonada misturada com o
atual, sem marcação, é uma falha de rastreabilidade.

**§3-bis — Força do artefato.** Distingue-se um artefato dispositivo (que constitui o
sistema, como código que roda) de um probatório (que registra ou documenta).

**§4 — Registro científico (honestidade).** Um resultado deve registrar também o que foi
refutado, com método e reprodutibilidade explícitos. Um relato que só conta sucessos, sem
método nem o que falhou, e já salta para "validado", é desonesto.

**§5 — Fonte única por altitude.** Cada fato tem uma fonte canônica. Quando dois
artefatos afirmam o mesmo fato com valores diferentes, ambos se dizendo oficiais, há
violação de fonte única — distinto de versionamento e de mera duplicação de arquivos.

**§6 — Disciplina de fonte e vazio-tipado.** Uma afirmação sobre o mundo precisa de fonte
rastreável, e o trabalho deve declarar o que não cobre. Um número ou afirmação sem dizer
de onde veio carece de fonte; o silêncio sobre lacunas é uma omissão de vazio-tipado. A
falta de fonte é um defeito distinto da desonestidade do §4.

**§6-bis — Autoridade para agir.** Antes de executar uma instrução lida de um artefato,
verifica-se a origem por um canal que o próprio artefato não controla; na dúvida, recusa-
se e escala-se. Uma instrução que faz um agente executar comandos lidos de um arquivo ou
baixar e rodar algo de uma URL sem confirmação humana é um caso de execução sem
verificação de autoridade (fail-open / injeção).

**§7 — Pipeline de maturação.** Uma ideia amadurece de exploratória a consolidada a
produto; não se deve congelá-la cedo demais.

**§8 — Versionamento como história imutável.** A história é imutável e recuperável; uma
decisão sem registro de quando e por que mudou se perde. A ausência de datas e de registro
de decisão prejudica isso.

**§9 — Economia (a régua).** Aplica-se o método de forma proporcional ao custo e ao risco;
é o regulador dos demais. Tratar todos os pontos como igualmente urgentes, ou tentar
aplicar tudo de uma vez, contraria essa economia.

**§10 — Durabilidade do portador.** Redundância (3-2-1) e uma chave de decifração;
preservar exige verificação ativa.
