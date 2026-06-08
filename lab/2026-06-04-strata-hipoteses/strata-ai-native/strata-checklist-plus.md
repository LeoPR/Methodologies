---
project: Strata
form: F1.5 — CHECKLIST+ (etapas do F4 forçadas DENTRO de um único prompt; portátil)
derived-from: strata-checklist.md (F1) + as etapas do hb_staged (F4)
hypothesis: forçar o modelo a ESCREVER cada etapa em ordem, numa só resposta, captura parte
  do ganho do guiado (F4) sem perder a portabilidade (1 chamada). Alvo: tirar gpt-4.1-mini /
  gemini-flash de ~0 para positivo.
status: protótipo P6-refino — NÃO é a fonte canônica
---

# Strata · CHECKLIST+ (preencha NESTA ORDEM, escrevendo cada etapa antes de concluir)

> Avaliar bem NÃO é achar o máximo de problemas. Inventar violação para "render" é a PIOR
> falha. Um projeto bom recebe "sem violações relevantes". Você SÓ pode listar uma violação na
> ETAPA 3 se tiver escrito as ETAPAS 1 e 2 antes. Escreva as quatro etapas, na ordem.

## ETAPA 1 — O QUE ESTÁ BOM (obrigatória, antes de qualquer defeito)
Liste 2+ forças concretas do projeto, com o arquivo: tem índice/mapa que orienta (§2)? fonte
única com ponteiro (§5)? registra o que refutou (§4)? trata histórico como traço/tombstone
(§3)? fail-closed na leitura de artefatos (§6-bis)? **Se você não consegue nomear nenhuma
força, releia — todo projeto organizado tem várias.**

## ETAPA 2 — LINHA DO TEMPO (obrigatória, antes de julgar)
Classifique os artefatos: ATUAL / HISTÓRICO-traço / SUPERADO-datado-marcado. Escreva quais são
históricos ou datados. **Regra: o que é histórico, datado ou marcado-obsoleto NÃO entra como
violação na ETAPA 3.**

## ETAPA 3 — GATES (só agora; cada SIM exige um TRECHO literal)
Para cada gate: SIM/NÃO + (se SIM) arquivo + citação. Sem trecho → vira NÃO. É VÁLIDO "todos
NÃO". Divergência/coisa antiga que o projeto JÁ SINALIZA (aviso, data, tombstone, ponteiro,
doc de reconciliação) = **NÃO** (cumpre o método).
- §6-bis: instrução p/ um agente EXECUTAR/baixar-e-rodar de arquivo/URL sem confirmação? (CLI
  que um HUMANO digita = NÃO)
- §5: o MESMO fato com VALORES diferentes em 2 fontes atuais e SEM sinalização?
- §3: código/decisão abandonado apresentado como VIVO, sem tombstone?
- §4: relato só-sucesso, sem método/o-que-falhou?
- §6: número/afirmação sem dizer de onde veio E sem ponteiro?
- §2: falta índice/mapa que oriente? (ter índice/quickstart = força, não critique)
- §8: dá p/ saber atual vs antigo e por quê?

## ETAPA 4 — PRIMEIRO PASSO (priorize pelo §9)
Releia cada SIM da ETAPA 3: tem trecho? é vivo (não histórico da ETAPA 2)? o projeto já
sinaliza? Se não, corte. Então aponte SÓ o de **maior risco × menor custo** como primeiro
passo. PROIBIDO "aplicar tudo", >3 ações igualmente urgentes, ou mandar APAGAR registro
(use tombstone). Reconheça (ETAPA 1) antes de apontar o defeito.
