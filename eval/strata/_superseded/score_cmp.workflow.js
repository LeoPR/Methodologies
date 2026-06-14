export const meta = {
  name: 'score-cmp-anv2-anv3',
  description: 'Pontua cego planos AN-v2 vs AN-v3 contra o gabarito corrigido (P1+P2)',
  phases: [{ title: 'NNN' }, { title: 'pdf2md' }],
}
const BASE = 'c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/eval/strata/planos'
const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['id', 'recognized_good', 'false_positives', 'genuine_real', 'flag_extra', 'notes'],
  properties: {
    id: { type: 'string' },
    recognized_good: { type: 'boolean', description: 'reconheceu >=1 pratica boa/nao-violacao explicitamente?' },
    false_positives: { type: 'integer', description: 'nº de violacoes inventadas / criticas-ao-bom / sinalizado-tratado-como-violacao / CLI-como-§6-bis' },
    genuine_real: { type: 'integer', description: 'nº de PROBLEMAS REAIS do gabarito que o plano achou (0..3+)' },
    flag_extra: { type: 'boolean', description: 'nnn: flagou os 3 arquivos-IA como §5 dup? | pdf2md: prescreveu APAGAR (rm/delete) em vez de tombstone?' },
    notes: { type: 'string' },
  },
}
const GAB_NNN = `# Gabarito NNN — base-de-verdade CORRIGIDA
PROBLEMAS REAIS (achar = GENUINO): (1) §5 contagens de teste conflitantes no STATUS.md: 2070 (Stage1), 2043 (Stage0), 2145 (Metricas 2026-05-31) — 3 valores do mesmo fato sem marcacao de qual vale AGORA. (2) §5 URL do repo: pyproject diz github.com/leona/nnn vs README/AGENTS github.com/LeoPR/nnn. (3) §1/§3 higiene leve: figurinhas.jsonl duplicado (raiz+examples/), dumps _repl_*.txt sem tipo.
DIVERGENCIA SINALIZADA (flagar como violacao = FALSO-POSITIVO): Privilege levels (5 vs 7) marcado com aviso 'diverge' + doc de reconciliacao = cumpre §5; reconhecer=ok, chamar de violacao=FP.
PRATICAS BOAS (reconhecer=bom; criticar=FP): §2 navegacao rica (INDEX/MAP/STATUS/AGENTS); §5 fonte-unica-com-ponteiro (delegam o numero ao STATUS via pytest); §6-bis fail-closed na leitura do corpus; §4 registra o que REFUTOU; §3/§8 obsolete/ closed/ como traco nao-apagavel; os 3 arquivos-IA (CLAUDE.md->AGENTS, INDEX, MAP) NAO sao dup-§5.
FALSO-POSITIVOS: criticar navegacao/ADRs/arquivos-IA; chamar a divergencia sinalizada de violacao; marcar historico/datado como problema ATUAL; inventar sem trecho.
flag_extra(nnn) = flagou os 3 arquivos-IA como §5 dup?`
const GAB_PDF = `# Gabarito pdf2md — base-de-verdade
PROBLEMAS REAIS (achar=GENUINO): (1) RI1 §5/§1 duplicatas -DESKTOP-SG30VJF (README, ROADMAP, pyproject, src/*-DESKTOP-SG30VJF.py) coexistindo sem tombstone. (2) RI2 §5/§8 versao conflitante: um conjunto diz ~v0.1 pre-pacote (CLI roadmap, nao pip-installable), o -DESKTOP diz v0.7.0 CLI estavel pip-installable — dois estados se dizendo atuais. (3) EXTRA §5/§1 PHILOSOPHY/DIARIO em dois lugares (docs/PHILOSOPHY.md vs docs/explanation/philosophy.md; DIARIO.md vs docs/explanation/diario.md), ambos vivos/linkados.
PRATICAS BOAS / NAO-VIOLACOES (criticar=FP): comandos de CLI nos READMEs sao para um HUMANO operar (pdf2md convert, venv) — NAO auto-execucao por agente; flaga-los como §6-bis/prompt-injection=FP. CHANGELOG ate 0.7.0 = rastro legitimo. A correcao certa das duplicatas e TOMBSTONE, nao rm/apagar.
FALSO-POSITIVOS: flagar a CLI como §6-bis; marcar historico/changelog como problema atual; prescrever apagar (em vez de tombstone); inventar sem trecho.
flag_extra(pdf2md) = prescreveu APAGAR/rm/delete em vez de tombstone?`

function scoreProj(proj, dir, ids, gab, phaseTitle) {
  return parallel(ids.map((id) => () =>
    agent(
      `Voce e' um juiz rigoroso e CEGO (nao sabe qual metodo gerou o plano). Leia o arquivo \`${dir}/${id}.md\` (use a ferramenta Read com esse caminho absoluto).\n\n` +
      `GABARITO (base-de-verdade do projeto ${proj}):\n${gab}\n\n` +
      `Pontue o plano contra o gabarito. RIGOR: criticar pratica boa, flagar divergencia SINALIZADA, marcar historico/datado como problema atual, flagar CLI-humana como §6-bis, ou inventar sem trecho = FALSO-POSITIVO (conte cada um). Achar um problema REAL do gabarito (com referencia plausivel ao arquivo/trecho) = genuine_real. ` +
      `Use id="${id}". Responda SO o schema.`,
      { label: `${proj}:${id}`, phase: phaseTitle, schema: SCHEMA }
    )
  ))
}

phase('NNN')
const NIDS = Array.from({ length: 16 }, (_, i) => 'N' + String(i + 1).padStart(2, '0'))
const RIDS = Array.from({ length: 16 }, (_, i) => 'R' + String(i + 1).padStart(2, '0'))
const nnn = await scoreProj('nnn', `${BASE}/nnn-cmp-blind`, NIDS, GAB_NNN, 'NNN')
phase('pdf2md')
const pdf = await scoreProj('pdf2md', `${BASE}/pdf2md-cmp-blind`, RIDS, GAB_PDF, 'pdf2md')
return { nnn: nnn.filter(Boolean), pdf2md: pdf.filter(Boolean) }
