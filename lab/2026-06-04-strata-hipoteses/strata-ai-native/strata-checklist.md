---
project: Strata
form: F1 — CHECKLIST mínimo (gates sim/não + 3 regras anti-falso-positivo)
derived-from: strata-an-v3.md (mesmos gates, sem prosa)
status: protótipo P6 (forma mais portátil) — NÃO é a fonte canônica
---

# Strata · CHECKLIST (responda cada gate com SIM/NÃO + 1 trecho)

REGRAS (valem para todos):
- **R1.** É VÁLIDO responder "nenhuma violação". Projeto bom → poucos ou zero achados. NÃO invente.
- **R2.** Cada "SIM" (violação) EXIGE um trecho literal (arquivo + citação). Sem trecho → é "NÃO".
- **R3.** Divergência/coisa antiga que o projeto **já sinaliza** (aviso, data, tombstone, doc de
  reconciliação, ponteiro p/ fonte) = **NÃO é violação**. Histórico/datado ≠ problema atual.

GATES (marque cada um):
- [ ] **§6-bis (PRIMEIRO, maior risco):** há instrução mandando um agente **executar/baixar-e-rodar**
  de um arquivo/URL **sem confirmação humana**? (CLI que um HUMANO digita = NÃO.)
- [ ] **§5 fonte única:** o **mesmo fato** aparece com **valores diferentes** em 2 fontes que se
  dizem atuais **e sem sinalização**?
- [ ] **§3 traço×superfície:** código/decisão **abandonado apresentado como vivo**, sem tombstone,
  misturado ao atual? (correção = tombstone, **NÃO apagar**.)
- [ ] **§4 honestidade:** relato **só-sucesso**, sem método/o-que-falhou/como-reproduzir?
- [ ] **§6 disciplina de fonte:** número/afirmação **sem dizer de onde veio E sem ponteiro**? ou
  não declara o que NÃO cobre?
- [ ] **§2 navegação:** falta índice/mapa que responda "o que há / por onde começo / o que vale
  agora / como uso"? (Ter índice/quickstart = força, NÃO critique.)
- [ ] **§8 história:** dá para saber o que é atual vs antigo e **por que** mudou? (sem datas = SIM.)

FECHAMENTO:
1. **Reconheça 1+ força** do projeto antes de listar achados.
2. **Priorize (§9):** aponte só o de **maior risco × menor custo** como primeiro passo.
   PROIBIDO "aplicar tudo" ou >3 ações igualmente urgentes.
3. Releia cada "SIM": tem trecho? é vivo (não histórico)? o projeto já sinaliza? Se não, vire "NÃO".
