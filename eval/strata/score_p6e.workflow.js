export const meta = {
  name: 'score-p6e',
  description: 'Pontua cego a validacao local (deepseek-r1:8b/qwen3-thinking N=3)',
  phases: [{ title: 'nnn' }, { title: 'pdf2md' }],
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
FP: criticar navegacao/ADRs/arquivos-IA; divergencia sinalizada como violacao; historico/datado como atual; inventar sem trecho. flag_extra=flagou os 3 arquivos-IA como §5 dup?
NOTA: alguns planos sao TRACE de raciocinio (reasoner local) — pontue pelo conteudo do diagnostico mesmo que nao formatado.`
const GAB_PDF = `# Gabarito pdf2md
PROBLEMAS REAIS (genuine): (1) RI1 §5/§1 duplicatas -DESKTOP-SG30VJF sem tombstone. (2) RI2 §5/§8 versao ~v0.1 vs v0.7.0 ambos atuais. (3) EXTRA §5/§1 PHILOSOPHY/DIARIO em dois lugares.
NAO-VIOLACOES (criticar=FP): CLI dos READMEs e para HUMANO operar (nao §6-bis); CHANGELOG=rastro legitimo; correcao=tombstone nao apagar.
FP: CLI como §6-bis; historico como atual; prescrever apagar; inventar sem trecho. flag_extra=prescreveu APAGAR em vez de tombstone?
NOTA: alguns planos sao TRACE de raciocinio (reasoner local) — pontue pelo conteudo do diagnostico mesmo que nao formatado.`

function grp(dir, ids, gab, proj, phaseTitle) {
  return parallel(ids.map((id) => () =>
    agent(`Juiz rigoroso e CEGO. Leia \`${BASE}/${dir}/${id}.md\` (Read).\n\nGABARITO (${proj}):\n${gab}\n\nRIGOR: criticar pratica boa / flagar sinalizado / historico-como-atual / CLI-como-§6-bis / inventar sem trecho = FALSO-POSITIVO. Problema REAL do gabarito achado = genuine_real. id="${id}". So o schema.`,
      { label: `${proj}:${id}`, phase: phaseTitle, schema: SCHEMA })))
}
const I = Array.from({ length: 6 }, (_, i) => 'I0' + (i + 1))
const J = Array.from({ length: 6 }, (_, i) => 'J0' + (i + 1))
phase('nnn')
const nnn = await grp('p6e-nnn-blind', I, GAB_NNN, 'nnn', 'nnn')
phase('pdf2md')
const pdf2md = await grp('p6e-pdf2md-blind', J, GAB_PDF, 'pdf2md', 'pdf2md')
return { nnn: nnn.filter(Boolean), pdf2md: pdf2md.filter(Boolean) }
