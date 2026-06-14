export const meta = {
  name: 'score-f15',
  description: 'Pontua cego a F1.5 (checklist+) contra o gabarito corrigido',
  phases: [{ title: 'F15' }],
}
const BASE = 'c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/eval/strata/planos'
const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['id', 'recognized_good', 'false_positives', 'genuine_real', 'flag_extra', 'notes'],
  properties: {
    id: { type: 'string' }, recognized_good: { type: 'boolean' },
    false_positives: { type: 'integer', description: 'violacoes inventadas / criticas-ao-bom / sinalizado-como-violacao / CLI-como-§6-bis / historico-como-atual' },
    genuine_real: { type: 'integer', description: 'nº de PROBLEMAS REAIS do gabarito achados' },
    flag_extra: { type: 'boolean' }, notes: { type: 'string' },
  },
}
const GAB_NNN = `# Gabarito NNN
PROBLEMAS REAIS (genuine): (1) §5 contagens de teste conflitantes no STATUS.md 2070/2043/2145 (mesmo fato 3 valores). (2) §5 URL repo pyproject github.com/leona/nnn vs README/AGENTS github.com/LeoPR/nnn. (3) §1/§3 figurinhas.jsonl duplicado + dumps _repl_*.txt.
SINALIZADA (flagar=FP): privilege levels 5vs7 com aviso+doc reconciliacao = cumpre §5.
PRATICAS BOAS (criticar=FP): navegacao INDEX/MAP/STATUS/AGENTS (§2); fonte-unica-com-ponteiro (§5); fail-closed corpus (§6-bis); registra refutacoes (§4); obsolete/closed como traco (§3/§8); os 3 arquivos-IA NAO sao dup-§5.
FP: criticar navegacao/ADRs/arquivos-IA; divergencia sinalizada como violacao; historico/datado como atual; inventar sem trecho. flag_extra=flagou os 3 arquivos-IA como §5 dup?`
const GAB_PDF = `# Gabarito pdf2md
PROBLEMAS REAIS (genuine): (1) RI1 §5/§1 duplicatas -DESKTOP-SG30VJF sem tombstone. (2) RI2 §5/§8 versao ~v0.1 vs v0.7.0 ambos atuais. (3) EXTRA §5/§1 PHILOSOPHY/DIARIO em dois lugares.
NAO-VIOLACOES (criticar=FP): CLI dos READMEs e para HUMANO operar (nao §6-bis); CHANGELOG=rastro legitimo; correcao=tombstone nao apagar.
FP: CLI como §6-bis; historico como atual; prescrever apagar; inventar sem trecho. flag_extra=prescreveu APAGAR em vez de tombstone?`

function grp(dir, ids, gab, proj) {
  return parallel(ids.map((id) => () =>
    agent(`Juiz rigoroso e CEGO. Leia \`${BASE}/${dir}/${id}.md\` (Read).\n\nGABARITO (${proj}):\n${gab}\n\nRIGOR: criticar pratica boa / flagar sinalizado / historico-como-atual / CLI-como-§6-bis / inventar sem trecho = FALSO-POSITIVO. Problema REAL do gabarito achado = genuine_real. id="${id}". So o schema.`,
      { label: `${proj}:${id}`, phase: 'F15', schema: SCHEMA })))
}
const E = Array.from({ length: 6 }, (_, i) => 'E0' + (i + 1))
const F = Array.from({ length: 6 }, (_, i) => 'F0' + (i + 1))
const [nnn, pdf2md] = await Promise.all([
  grp('p6c-f15-nnn-blind', E, GAB_NNN, 'nnn'),
  grp('p6c-f15-pdf2md-blind', F, GAB_PDF, 'pdf2md'),
])
return { nnn: nnn.filter(Boolean), pdf2md: pdf2md.filter(Boolean) }
