export const meta = {
  name: 'score-p6b-grid',
  description: 'Pontua cego o grid P6 Fase B (F1 grid 12 modelos + F4 overlay) p/ o scatterplot',
  phases: [{ title: 'F1-grid' }, { title: 'F4-overlay' }],
}
const BASE = 'c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/eval/strata/planos'
const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['id', 'recognized_good', 'false_positives', 'genuine_real', 'flag_extra', 'notes'],
  properties: {
    id: { type: 'string' },
    recognized_good: { type: 'boolean' },
    false_positives: { type: 'integer', description: 'violacoes inventadas / criticas-ao-bom / sinalizado-como-violacao / CLI-como-§6-bis / historico-como-atual' },
    genuine_real: { type: 'integer', description: 'nº de PROBLEMAS REAIS do gabarito achados (0..3+)' },
    flag_extra: { type: 'boolean' },
    notes: { type: 'string' },
  },
}
const GAB_NNN = `# Gabarito NNN — base-de-verdade CORRIGIDA
PROBLEMAS REAIS (achar = GENUINO): (1) §5 contagens de teste conflitantes no STATUS.md: 2070 (Stage1), 2043 (Stage0), 2145 (Metricas 2026-05-31) — 3 valores do mesmo fato sem marcacao de qual vale AGORA. (2) §5 URL do repo: pyproject diz github.com/leona/nnn vs README/AGENTS github.com/LeoPR/nnn. (3) §1/§3 higiene leve: figurinhas.jsonl duplicado (raiz+examples/), dumps _repl_*.txt sem tipo.
DIVERGENCIA SINALIZADA (flagar como violacao = FALSO-POSITIVO): Privilege levels (5 vs 7) marcado com aviso 'diverge' + doc de reconciliacao = cumpre §5.
PRATICAS BOAS (reconhecer=bom; criticar=FP): §2 navegacao rica (INDEX/MAP/STATUS/AGENTS); §5 fonte-unica-com-ponteiro (delegam o numero ao STATUS via pytest); §6-bis fail-closed na leitura do corpus; §4 registra o que REFUTOU; §3/§8 obsolete/ closed/ como traco nao-apagavel; os 3 arquivos-IA (CLAUDE.md->AGENTS, INDEX, MAP) NAO sao dup-§5.
FALSO-POSITIVOS: criticar navegacao/ADRs/arquivos-IA; chamar a divergencia sinalizada de violacao; marcar historico/datado como problema ATUAL; inventar sem trecho.
flag_extra(nnn) = flagou os 3 arquivos-IA como §5 dup?`
const GAB_PDF = `# Gabarito pdf2md — base-de-verdade
PROBLEMAS REAIS (achar=GENUINO): (1) RI1 §5/§1 duplicatas -DESKTOP-SG30VJF (README, ROADMAP, pyproject, src/*-DESKTOP-SG30VJF.py) coexistindo sem tombstone. (2) RI2 §5/§8 versao conflitante: ~v0.1 pre-pacote vs v0.7.0 pip-installable, ambos atuais. (3) EXTRA §5/§1 PHILOSOPHY/DIARIO em dois lugares, ambos vivos/linkados.
PRATICAS BOAS / NAO-VIOLACOES (criticar=FP): comandos de CLI sao para um HUMANO operar — NAO §6-bis/prompt-injection; CHANGELOG=rastro legitimo; correcao certa=tombstone nao apagar.
FALSO-POSITIVOS: flagar a CLI como §6-bis; marcar historico/changelog como atual; prescrever apagar; inventar sem trecho.
flag_extra(pdf2md) = prescreveu APAGAR/rm/delete em vez de tombstone?`

function scoreGroup(dir, ids, gab, proj, phaseTitle) {
  return parallel(ids.map((id) => () =>
    agent(
      `Voce e' um juiz rigoroso e CEGO. Leia o arquivo \`${BASE}/${dir}/${id}.md\` (use Read com esse caminho absoluto).\n\n` +
      `GABARITO (projeto ${proj}):\n${gab}\n\n` +
      `RIGOR: criticar pratica boa, flagar divergencia SINALIZADA, marcar historico/datado como problema atual, flagar CLI-humana como §6-bis, ou inventar sem trecho = FALSO-POSITIVO (conte cada um). Achar um problema REAL do gabarito (com referencia plausivel) = genuine_real. ` +
      `Use id="${id}". Responda SO o schema.`,
      { label: `${dir}:${id}`, phase: phaseTitle, schema: SCHEMA }
    )
  ))
}
const A = Array.from({ length: 24 }, (_, i) => 'A' + String(i + 1).padStart(2, '0'))
const B = Array.from({ length: 24 }, (_, i) => 'B' + String(i + 1).padStart(2, '0'))
const C = Array.from({ length: 5 }, (_, i) => 'C' + String(i + 1).padStart(2, '0'))
const D = Array.from({ length: 5 }, (_, i) => 'D' + String(i + 1).padStart(2, '0'))

phase('F1-grid')
const [nnn, pdf2md] = await Promise.all([
  scoreGroup('p6b-f1-nnn-blind', A, GAB_NNN, 'nnn', 'F1-grid'),
  scoreGroup('p6b-f1-pdf2md-blind', B, GAB_PDF, 'pdf2md', 'F1-grid'),
])
phase('F4-overlay')
const [f4_nnn, f4_pdf] = await Promise.all([
  scoreGroup('p6b-f4-nnn-blind', C, GAB_NNN, 'nnn', 'F4-overlay'),
  scoreGroup('p6b-f4-pdf2md-blind', D, GAB_PDF, 'pdf2md', 'F4-overlay'),
])
return {
  nnn: nnn.filter(Boolean), pdf2md: pdf2md.filter(Boolean),
  f4_nnn: f4_nnn.filter(Boolean), f4_pdf: f4_pdf.filter(Boolean),
}
