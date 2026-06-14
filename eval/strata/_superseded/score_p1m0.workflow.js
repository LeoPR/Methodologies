export const meta = {
  name: 'score-p1m0',
  description: 'Pontua cego M0 (abstencao) vs audit: veredito + nº acoes + falso-positivo, 3 projetos',
  phases: [{ title: 'nnn' }, { title: 'pdf2md' }, { title: 'fg2p' }],
}
const BASE = 'c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/eval/strata/planos'
const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['id', 'verdict', 'action_count', 'false_positives', 'genuine_real', 'recognized_good', 'notes'],
  properties: {
    id: { type: 'string' },
    verdict: { type: 'string', enum: ['JA-BOM', 'PRECISA-PONTOS', 'PRECISA-MUITO', 'unclear'], description: 'o veredito que o plano expressa (no audit, INFIRA do tom: poucos/nenhum problema=JA-BOM; muitos=PRECISA-MUITO)' },
    action_count: { type: 'integer', description: 'nº de acoes/problemas que o plano recomenda atacar' },
    false_positives: { type: 'integer', description: 'nº de violacoes inventadas / criticas-a-pratica-boa / sinalizado-tratado-como-violacao / historico-como-atual' },
    genuine_real: { type: 'integer', description: 'nº de PROBLEMAS REAIS do gabarito que o plano achou' },
    recognized_good: { type: 'boolean', description: 'reconheceu >=1 pratica boa explicitamente?' },
    notes: { type: 'string' },
  },
}
const GAB = {
  nnn: `# NNN — VEREDITO-VERDADE: JA-BOM (exemplar; o certo e' abster-se / acao minima).
PROBLEMAS REAIS (achar=genuine, mas sao SUTIS e poucos): §5 contagens de teste 2070/2043/2145 no STATUS.md; §5 URL repo leona/nnn vs LeoPR/nnn; §1/§3 figurinhas.jsonl dup + _repl_*.txt.
PRATICAS BOAS (criticar=FALSO-POSITIVO): navegacao INDEX/MAP/STATUS/AGENTS; fonte-unica-com-ponteiro; fail-closed corpus; registra refutacoes; obsolete/closed como traco; os 3 arquivos-IA NAO sao dup. Privilege 5vs7 e' SINALIZADO (flagar=FP).
ERRO-ALVO: veredito PRECISA-MUITO ou muitas acoes aqui = SUPER-APLICACAO (a falha que M0 quer evitar). JA-BOM com 0-2 acoes = correto.`,
  pdf2md: `# pdf2md — VEREDITO-VERDADE: PRECISA-PONTOS (ha problemas reais claros, mas poucos).
PROBLEMAS REAIS (genuine): RI1 duplicatas -DESKTOP-SG30VJF (§5/§1); RI2 versao ~v0.1 vs v0.7.0 (§5/§8); EXTRA PHILOSOPHY/DIARIO em dois lugares.
NAO-VIOLACOES (criticar=FP): CLI dos READMEs e' para humano (nao §6-bis); CHANGELOG=rastro; correcao=tombstone nao apagar.
ERRO-ALVO: JA-BOM aqui = sub-deteccao (perdeu os reais). PRECISA-MUITO com invencao = super-aplicacao.`,
  fg2p: `# FG2P — VEREDITO-VERDADE: PRECISA (projeto antigo/messy, mas tem docs de entrada).
PROBLEMAS REAIS (genuine): §1/§3 backups/ misturado sem tipagem (.docx + modelos + protected); §3 conf/*legacy*.json sem tombstone; §2 sem indice/mapa unico.
NAO-VIOLACOES (criticar=FP): requirements.txt + requirements_inference_only = split intencional (nao §5); CHANGELOG/ROADMAP=rastro; README-head e' recorte (nao criticar tamanho).
ERRO-ALVO: JA-BOM aqui = sub-deteccao. PRECISA com inventar muito = ruido.`,
}
function grp(proj, dir, ids, phaseTitle) {
  return parallel(ids.map((id) => () =>
    agent(`Juiz rigoroso e CEGO (nao sabe a forma que gerou o plano). Leia \`${BASE}/${dir}/${id}.md\` (Read).\n\nGABARITO (${proj}):\n${GAB[proj]}\n\nExtraia o veredito (ou infira no audit), conte as acoes, e os falso-positivos (criticar pratica boa / inventar / sinalizado-como-violacao / historico-como-atual). id="${id}". So o schema.`,
      { label: `${proj}:${id}`, phase: phaseTitle, schema: SCHEMA })))
}
const ids = (p, n) => Array.from({ length: 16 }, (_, i) => p + String(i + 1).padStart(2, '0'))
phase('nnn')
const nnn = await grp('nnn', 'p1-nnn-blind', ids('K'), 'nnn')
phase('pdf2md')
const pdf2md = await grp('pdf2md', 'p1-pdf2md-blind', ids('L'), 'pdf2md')
phase('fg2p')
const fg2p = await grp('fg2p', 'p1-fg2p-blind', ids('M'), 'fg2p')
return { nnn: nnn.filter(Boolean), pdf2md: pdf2md.filter(Boolean), fg2p: fg2p.filter(Boolean) }
