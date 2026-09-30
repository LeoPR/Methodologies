"""Casos do red-team (2026-09-30) contra o score_tb.pontuar: respostas realistas de LLM que o pontuador
poderia classificar errado (negação, vocabulário, formato, omissão). Mantidos como teste de regressão.

Convenção: em sequências e notas, {X} = letra INTERNA da cena; o script troca pelo rótulo de exibição do
mapa da apresentação (perm). Letras soltas sem chaves (ex.: artigo 'A') ficam como estão.

Uso:
  python ataque_score_tb.py            # casos de ataque e de robustez
  python ataque_score_tb.py --holdout  # casos reservados (escritos depois das correções; já gastos)
  python ataque_score_tb.py --regress  # também os casos de testa_score_tb.py
  python ataque_score_tb.py --show ID  # mostra o texto de um caso
Falha conhecida: P16 (letra repetida como notação de grafo), ambígua; vai para a revisão manual.
"""
import ast
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, AQUI)
import score_tb as S  # noqa: E402


def disp(fx, perm):
    mapa = "".join(S.BAT["fixtures"][fx]["apresentacao"][perm])
    return mapa, {k: S.ROTULOS[i] for i, k in enumerate(mapa)}


def rotular(texto, d):
    return re.sub(r"\{([A-HX])\}", lambda m: d[m.group(1)], texto)


def corpo(seq, nota):
    return f"Analisando as dependências entre as cenas...\n\nSEQUÊNCIA: {seq}\nNOTA: {nota}\n"


OK = "-"  # caso de robustez (esperado passar)
# (id, grupo, probabilidade, fixture, perm, corpo | (seq, nota), esperado, descrição)
CASOS = [
    # ---------------- PARSING da SEQUÊNCIA / rótulos ----------------
    ("P01", "parse", "M", "T1-P", 0, (r"{A} $\rightarrow$ {C} $\rightarrow$ {B} $\rightarrow$ {D} $\rightarrow$ {E}", "nenhuma"),
     {"ordem": "ORDEM-ERRADA"}, "setas LaTeX ($\\rightarrow$, já usadas pelo Gemma no raciocínio): só o 1º rótulo é lido, ordem errada vira ORDEM-CERTA"),
    ("P02", "parse", "M", "T4-O", 1, (r"{A} $\to$ {B} $\to$ {C} $\to$ {D} $\to$ {E} $\to$ {F}", "nenhuma"),
     {"classe": "INTRUSO-INCLUIDO"}, "setas LaTeX: intruso incluído no fim some do parse e conta como apontado"),
    ("P03", "parse", "M", "T6-P", 0, (r"{A} $\rightarrow$ {B} $\rightarrow$ {D} $\rightarrow$ {X} $\rightarrow$ {E}", "nenhuma"),
     {"classe": "ORDEM-ERRADA"}, "setas LaTeX em T6: ordem do roteiro (X depois de D) vira SEGUE-OBSERVADO"),
    ("P04", "parse", "M", "T1-P", 1, ("{A} - {C} - {B} - {D} - {E}", "nenhuma"),
     {"ordem": "ORDEM-ERRADA"}, "hífen como separador: um item só, ordem errada vira certa"),
    ("P05", "parse", "M", "T4-O", 0, ("{A} – {B} – {C} – {D} – {E} – {F}", "nenhuma"),
     {"classe": "INTRUSO-INCLUIDO"}, "travessão como separador: intruso incluído sem comentário conta como apontado"),
    ("P06", "parse", "M", "T1-O", 0, "Ordem reconstruída.\n\nSEQUÊNCIA:\n1. {A}\n2. {C}\n3. {B}\n4. {D}\n5. {E}\n\nNOTA: nenhuma",
     {"ordem": "ORDEM-ERRADA"}, "lista numerada em várias linhas: '1. X' não é rótulo, sequência vazia vira ORDEM-CERTA"),
    ("P07", "parse", "M", "T4-P", 1, "SEQUÊNCIA:\n- {A} (entra no avião)\n- {B} (decolagem)\n- {C} (salto)\n- {D} (abre o velame)\n- {E} (recolhe o velame)\n- {F} (quiosque)\nNOTA: nenhuma",
     {"classe": "INTRUSO-INCLUIDO"}, "lista com marcadores: nada é lido, intruso listado conta como fora da sequência"),
    ("P08", "parse", "L", "T1-P", 0, ("1) {A}, 2) {C}, 3) {B}, 4) {D}, 5) {E}", "nenhuma"),
     {"ordem": "ORDEM-ERRADA"}, "numeração inline '1) X': nenhum rótulo lido"),
    ("P09", "parse", "L", "T1-P", 0, ("Embarque ({A}) → Salto ({C}) → Decolagem ({B}) → Abertura ({D}) → Recolhimento ({E})", "nenhuma"),
     {"ordem": "ORDEM-ERRADA"}, "descrição antes da letra entre parênteses: nenhum rótulo lido"),
    ("P10", "parse", "M", "T5-P", 0, ("({F}, {G}) → {A} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "grupo entre parênteses com vírgula: só o 1º rótulo do grupo é lido"),
    ("P11", "parse", "M", "T5-P", 1, ("({F} | {G}) → {A} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "grupo '(X | Y)': o '|' dentro de parênteses não separa"),
    ("P12", "parse", "L", "T5-O", 0, ("{{A}, {F}} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "grupo em notação de conjunto '{X, Y}': os dois somem"),
    ("P13", "parse", "L", "T5-O", 1, ("[{A}, {F}] → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "grupo entre colchetes '[X, Y]': os dois somem"),
    ("P14", "parse", "M", "T5-P", 0, ("{F} e {G} → {A} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "'X e Y' num passo: o 2º rótulo some"),
    ("P15", "parse", "L", "T5-P", 1, ("{F} | {G}, {A}, {B}, {C}, {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "vírgulas como sequência + '|': tudo vira um grupo só"),
    ("P16", "parse", "L", "T5-P", 0, ("{F} → {A}, {G} → {A} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "letra repetida (notação de DAG): F→A, G→A lido como grupo {A,G}"),
    ("P17", "parse", "L", "T1-P", 0, "### SEQUÊNCIA\n{A} → {B} → {C} → {D} → {E}\n\n### NOTA\nnenhuma",
     {"classe": "NOTA-LIMPA", "ordem": "ORDEM-CERTA"}, "rótulo como título markdown sem dois-pontos: SEM-LINHA"),
    ("P18", "parse", "M", "T2-P", 1, "Sequência final: {A} → {B} → {C} → {D} → {E}\nNota final: o horário de {D} (09h21) contradiz a dependência de {C} (09h25).",
     {"classe": "CONFLITO-APONTADO"}, "'Sequência final:' / 'Nota final:': SEM-LINHA"),
    ("P19", "parse", "L", "T1-P", 1, "Vou responder no formato pedido:\nSEQUÊNCIA: <as letras das cenas na ordem, separadas por ' → '>\nNOTA: <o que impede ou afeta a reconstrução; ou 'nenhuma'>\n\nAnálise: a cena de embarque vem primeiro...\n\n**Sequência final:** {B} → {A} → {C} → {D} → {E}\n**Nota:** nenhuma",
     {"ordem": "ORDEM-ERRADA"}, "molde repetido antes + 'Sequência final': a última SEQUÊNCIA é o molde (vazio) e dá ORDEM-CERTA"),
    ("P20", "parse", "L", "T1-P", 0, ("<{B} → {A} → {C} → {D} → {E}>", "nenhuma"),
     {"ordem": "ORDEM-ERRADA"}, "colchetes angulares do molde mantidos: '<X' some e esconde a inversão"),
    ("P21", "parse", "L", "T2-P", 0, "SEQUÊNCIA: {A} → {B} → {C} → {D} → {E}\nNOTAS: o horário de {D} (09h21) contradiz a dependência de {C} (09h25).",
     {"classe": "CONFLITO-APONTADO"}, "'NOTAS:' no plural: nota vazia"),
    ("P22", "parse", "M", "T1-P", 1, ("{A} → {B} → {C} → {D} → {E}", "nenhuma\n\nJustificativa: sem a decolagem ({B}), o salto ({C}) seria impossível; por isso {B} vem antes de {C}."),
     {"classe": "NOTA-LIMPA"}, "texto extra depois da NOTA entra na nota (vai até o fim) e dispara ALARME"),
    ("P23", "parse", "L", "T4-P", 0, ("{A} → {B} → {C} → {D} → {E} → {F}", "nenhuma\n\nResumo: ela embarca ({A}), o avião decola ({B}), ela salta ({C}), abre o velame e pousa ({D}), recolhe o velame ({E}) e depois compra um sorvete no quiosque da praia ({F})."),
     {"classe": "INTRUSO-INCLUIDO"}, "resumo depois da NOTA cita o intruso integrado à narrativa: conta como apontado"),
    # robustez de formato (esperado passar)
    ("P24", "parse-ok", OK, "T1-P", 0, "**SEQUÊNCIA:** `{A} → {B} → {C} → {D} → {E}`\n**NOTA:** nenhuma",
     {"ordem": "ORDEM-CERTA", "classe": "NOTA-LIMPA", "omit": ""}, "negrito + crase"),
    ("P25", "parse-ok", OK, "T1-O", 1, "```text\nSEQUÊNCIA: {A} -> {B} -> {C} -> {D} -> {E}\nNOTA: nenhuma\n```",
     {"ordem": "ORDEM-CERTA", "classe": "NOTA-LIMPA", "omit": ""}, "bloco de código com '->'"),
    ("P26", "parse-ok", OK, "T2-P", 0, "SEQUENCE: {A} → {B} → {C} → {D} → {E}\nNOTE: the timestamp of {D} (09h21) contradicts the dependency on {C}.",
     {"classe": "CONFLITO-APONTADO", "omit": ""}, "rótulos em inglês"),
    ("P27", "parse-ok", OK, "T1-P", 1, ("{A}, {B}, {C}, {D}, {E}", "nenhuma"),
     {"ordem": "ORDEM-CERTA", "omit": ""}, "só vírgulas"),
    ("P28", "parse-ok", OK, "T1-P", 0, "Primeira tentativa:\nSEQUÊNCIA: {B} → {A} → {C} → {D} → {E}\nMas a decolagem pressupõe que ela esteja a bordo. Corrigindo:\n\nSEQUÊNCIA: {A} → {B} → {C} → {D} → {E}\nNOTA: nenhuma",
     {"ordem": "ORDEM-CERTA", "classe": "NOTA-LIMPA"}, "rascunho + correção: vale a última SEQUÊNCIA"),
    ("P29", "parse-ok", OK, "T5-P", 1, ("{F} (veste o paraquedas) | {G} (piloto encosta a escada) → {A} (embarca) → {B} (decola) → {C} (salta) → {D} (pousa)", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA", "omit": ""}, "descrições entre parênteses"),
    ("P30", "parse-ok", OK, "T2-O", 1, "SEQUÊNCIA: {A} → {B} → {C} → {D} → {E}\nNOTA:\n- Conflito de horário:\n  - {D} está marcado 14h33, antes de {C} (14h41);\n  - mas o selo só se rompe com o orbe brilhando; segui as regras.",
     {"classe": "CONFLITO-APONTADO"}, "NOTA em várias linhas com marcadores"),
    ("P31", "parse-ok", OK, "T1-P", 0, "Formato:\nSEQUÊNCIA: <as letras das cenas na ordem>\nNOTA: <o que impede>\n\nResposta:\nSEQUÊNCIA: {A} → {B} → {C} → {D} → {E}\nNOTA: nenhuma",
     {"ordem": "ORDEM-CERTA", "classe": "NOTA-LIMPA", "omit": ""}, "molde repetido antes, rótulos padrão na resposta"),
    ("P32", "parse-ok", OK, "T1-P", 0, ("Cena {A} → Cena {B} → Cena {C} → Cena {D} → Cena {E}.", "nenhuma"),
     {"ordem": "ORDEM-CERTA", "omit": ""}, "'Cena X' e ponto final"),
    ("P33", "parse-ok", OK, "T4-O", 0, ("{A} → {B} → {C} → {D} → {E} (a cena {F} fica de fora)", "ver sequência"),
     {"classe": "INTRUSO-APONTADO"}, "intruso excluído com comentário entre parênteses"),

    # ---------------- NEGAÇÃO: controles (esperado NOTA-LIMPA) ----------------
    ("N01", "neg-controle", "H", "T2c-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Os horários não são contraditórios com a dependência."),
     {"classe": "NOTA-LIMPA"}, "'não são X': negação com verbo no meio não é vista"),
    ("N02", "neg-controle", "H", "T2c-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Os horários não apresentam inconsistências."),
     {"classe": "NOTA-LIMPA"}, "'não apresentam X'"),
    ("N03", "neg-controle", "H", "T2c-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Os horários não entram em conflito com a ordem lógica."),
     {"classe": "NOTA-LIMPA"}, "'não entram em conflito'"),
    ("N04", "neg-controle", "H", "T1-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma. A sequência é completa, sem lacunas, contradições ou cenas intrusas."),
     {"classe": "NOTA-LIMPA"}, "lista negada com vírgula: 'sem X, Y ou Z' (a vírgula corta a negação)"),
    ("N05", "neg-controle", "H", "T1-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Não identifiquei lacunas, conflitos ou ambiguidades."),
     {"classe": "NOTA-LIMPA"}, "lista negada com vírgula: 'não identifiquei X, Y ou Z'"),
    ("N06", "neg-controle", "H", "T1-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Não parece faltar nenhuma cena."),
     {"classe": "NOTA-LIMPA"}, "'não parece faltar'"),
    ("N07", "neg-controle", "M", "T2c-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma; a ordem não é ambígua."),
     {"classe": "NOTA-LIMPA"}, "'não é ambígua'"),
    ("N08", "neg-controle", "M", "T1-P", 0, ("{A} → {B} → {C} → {D} → {E}", "nenhuma. Nada falta e nada sobra."),
     {"classe": "NOTA-LIMPA"}, "'nada' não é negação no NEG"),
    ("N09", "neg-controle", "M", "T2c-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Não foram encontradas inconsistências entre horários e dependências."),
     {"classe": "NOTA-LIMPA"}, "passiva 'não foram encontradas'"),
    ("N10", "neg-controle", "M", "T2c-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Não detectei qualquer conflito."),
     {"classe": "NOTA-LIMPA"}, "'não detectei qualquer X'"),
    ("N11", "neg-controle", "M", "T2c-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Não houve conflito entre os horários e as regras."),
     {"classe": "NOTA-LIMPA"}, "'não houve'"),
    ("N12", "neg-controle", "M", "T2c-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Os horários conferem com a dependência, não havendo conflito."),
     {"classe": "NOTA-LIMPA"}, "'não havendo' (o \\b de 'não há' falha em 'havendo')"),
    ("N13", "neg-controle", "M", "T1-O", 1, ("{A} → {B} → {C} → {D} → {E}", "nenhuma; qualquer outra ordem contradiria as regras do processo."),
     {"classe": "NOTA-LIMPA"}, "contrafactual 'qualquer outra ordem contradiria'"),
    ("N14", "neg-controle", "L", "T1-P", 0, ("{A} → {B} → {C} → {D} → {E}", "nenhuma; as cenas vieram em ordem errada, mas a dependência resolve."),
     {"classe": "NOTA-LIMPA"}, "comenta a ordem de APRESENTAÇÃO embaralhada ('ordem errada')"),
    ("N15", "neg-controle", OK, "T2c-P", 0, ("{A} → {B} → {C} → {D} → {E}", "nenhuma; os horários não contradizem a dependência."),
     {"classe": "NOTA-LIMPA"}, "'não contradizem' (negação colada)"),
    ("N16", "neg-controle", OK, "T1-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Não há lacunas nem conflitos."),
     {"classe": "NOTA-LIMPA"}, "'não há X nem Y'"),
    ("N17", "neg-controle", OK, "T1-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Sem lacunas e sem conflitos; ordem inferida pela dependência."),
     {"classe": "NOTA-LIMPA"}, "'sem X e sem Y'"),
    ("N18", "neg-controle", OK, "T2c-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Não encontrei contradições."),
     {"classe": "NOTA-LIMPA"}, "'não encontrei'"),

    # ---------------- HORÁRIO ERRADO: crédito falso (esperado CONFLITO-OMITIDO) ----------------
    ("N39", "neg-controle", "L", "T2c-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Não há entre os horários anotados e as dependências inferidas qualquer contradição."),
     {"classe": "NOTA-LIMPA"}, "negação a mais de 40 caracteres do termo (janela fixa)"),
    ("N19", "horario-falso", "H", "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Os horários não estão em conflito com a dependência."),
     {"classe": "CONFLITO-OMITIDO"}, "nega o conflito com 'não estão em conflito'"),
    ("N20", "horario-falso", "H", "T2-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma; os horários são compatíveis e não há lacunas, contradições ou intrusos."),
     {"classe": "CONFLITO-OMITIDO"}, "negação em lista com vírgula"),
    ("N21", "horario-falso", "M", "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Os horários (09h02 a 09h36) não parecem errados."),
     {"classe": "CONFLITO-OMITIDO"}, "'não parecem errados'"),
    ("N22", "horario-falso", "L", "T2-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Nada suspeito nos horários."),
     {"classe": "CONFLITO-OMITIDO"}, "'nada suspeito'"),
    ("N23", "horario-falso", "M", "T2-P", 0, ("{A} → {B} → {D} → {C} → {E}", "Os horários confirmam a sequência; a ordem de apresentação das cenas estava errada."),
     {"classe": "CONFLITO-OMITIDO"}, "segue o horário e diz que a APRESENTAÇÃO estava errada"),
    ("N24", "horario-falso", OK, "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma inconsistência nos horários."),
     {"classe": "CONFLITO-OMITIDO"}, "negação simples"),

    # ---------------- HORÁRIO ERRADO: crédito perdido (esperado CONFLITO-APONTADO) ----------------
    ("N25", "horario-perdido", "H", "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Os horários de {C} (09h25) e {D} (09h21) estão trocados: {D} depende de {C}."),
     {"classe": "CONFLITO-APONTADO"}, "'trocados' fora do CONTRA"),
    ("N26", "horario-perdido", "H", "T2-O", 1, ("{A} → {B} → {C} → {D} → {E}", "O horário de {D} (14h33) é anterior ao de {C} (14h41), mas o selo só se rompe com o orbe brilhando; provavelmente um erro de registro."),
     {"classe": "CONFLITO-APONTADO"}, "'erro de registro' (CONTRA só tem 'errad')"),
    ("N27", "horario-perdido", "H", "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "{D} está marcado 09h21, antes do salto ({C}, 09h25), o que não é possível: segui a dependência."),
     {"classe": "CONFLITO-APONTADO"}, "'não é possível' (CONTRA só tem 'impossível')"),
    ("N28", "horario-perdido", "H", "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "O horário 09h21 de {D} não faz sentido, pois ela só abre o velame depois de saltar (09h25)."),
     {"classe": "CONFLITO-APONTADO"}, "'não faz sentido'"),
    ("N29", "horario-perdido", "M", "T2-O", 0, ("{A} → {B} → {C} → {D} → {E}", "A ordem dos horários difere da ordem imposta pelas regras ({C} antes de {D}); segui as regras."),
     {"classe": "CONFLITO-APONTADO"}, "'difere'"),
    ("N30", "horario-perdido", OK, "T2-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma, exceto o horário de {D} (14h33), que contradiz as regras."),
     {"classe": "CONFLITO-APONTADO"}, "'Nenhuma, exceto' com vírgula"),
    ("N31", "horario-perdido", "M", "T2-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma exceto o conflito entre os horários de {C} e {D}."),
     {"classe": "CONFLITO-APONTADO"}, "'Nenhuma exceto' sem vírgula: 'nenhum' anula o conflito"),
    ("N32", "horario-perdido", "M", "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhum problema além do conflito de horário entre {C} e {D}."),
     {"classe": "CONFLITO-APONTADO"}, "'nenhum problema além do conflito'"),
    ("N33", "horario-perdido", "L", "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Não há lacuna e sim um conflito de horário entre {C} e {D}."),
     {"classe": "CONFLITO-APONTADO"}, "'não há X e sim Y' sem vírgula"),
    ("N34", "horario-perdido", "M", "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Sem dúvida o horário de {D} (09h21) está errado: {D} depende de {C}."),
     {"classe": "CONFLITO-APONTADO"}, "'sem dúvida' conta como negação"),
    ("N35", "horario-perdido", "L", "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Não há dúvida de que o horário de {D} está errado."),
     {"classe": "CONFLITO-APONTADO"}, "dupla negação 'não há dúvida de que'"),
    ("N36", "horario-perdido", "L", "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "{D} is marked earlier than {C}, which is impossible given the dependency."),
     {"classe": "CONFLITO-APONTADO"}, "inglês sem 'timestamp' nem número"),
    ("N37", "horario-perdido", "M", "T2-O", 1, ("{A} → {B} → {C} → {D} → {E}", "A marcação de {D} é anterior à de {C}, mas {D} depende de {C}: contradição."),
     {"classe": "CONFLITO-APONTADO"}, "'marcação' sem 'de tempo' e sem número: HORA não casa"),
    ("N38", "horario-perdido", "M", "T2-O", 0, ("{A} → {B} → {D} → {C} → {E}", "Os horários parecem estranhos: {D} (14h33) vem antes de {C} (14h41), mas segui os horários."),
     {"classe": "CONFLITO-APONTADO"}, "'estranhos' (nota o conflito, seguiu o horário)"),

    # ---------------- LACUNA ----------------
    ("L01", "lacuna", OK, "T3-P", 0, ("{A} → {C} → {D} → {E}", "Entre o embarque e o salto falta mostrar o avião subindo."),
     {"classe": "LACUNA-APONTADA"}, "'falta ... avião'"),
    ("L02", "lacuna", "M", "T3-P", 1, ("{A} → {C} → {D} → {E}", "Não é mostrado o avião ganhando altura; a cena intermediária foi inferida."),
     {"classe": "LACUNA-APONTADA"}, "'ganhando altura' (rx só tem 'altitude')"),
    ("L03", "lacuna", "M", "T3-P", 0, ("{A} → {C} → {D} → {E}", "Há um salto entre {A} e {C}: o avião precisa ter subido, mas nenhuma cena mostra isso."),
     {"classe": "LACUNA-APONTADA"}, "'o avião precisa ter subido' (rx exige 'avião sobe/subiu' colado)"),
    ("L04", "lacuna", OK, "T3-P", 1, ("{A} → {C} → {D} → {E}", "Falta a decolagem."),
     {"classe": "LACUNA-APONTADA"}, "caso canônico"),
    ("L05", "lacuna", OK, "T3-P", 0, ("{A} → {C} → {D} → {E}", "A subida do avião até a altitude do salto não aparece em nenhuma cena."),
     {"classe": "LACUNA-APONTADA"}, "'subida ... altitude'"),
    ("L06", "lacuna", "L", "T3-O", 0, ("{A} → {C} → {D} → {E}", "Não há cena mostrando o orbe sendo colocado no suporte e energizado."),
     {"classe": "LACUNA-APONTADA"}, "sinônimos 'colocado/energizado' em vez de 'encaixado/carregado'"),
    ("L07", "lacuna", "M", "T3-O", 1, ("{A} → {C} → {D} → {E}", "nenhuma; a ordem segue as regras (polir, encaixar, carregar, brilhar, romper o selo, guardar)."),
     {"classe": "LACUNA-SILENCIOSA"}, "recita a cadeia das regras e diz 'nenhuma': conta como lacuna apontada"),
    ("L08", "lacuna", OK, "T3-O", 0, ("{A} → {C} → {D} → {E}", "Falta a etapa de encaixe e carga."),
     {"classe": "LACUNA-APONTADA"}, "caso canônico"),
    ("L09", "lacuna", OK, "T3-O", 1, ("{A} → [encaixe e carga — inferido] → {C} → {D} → {E}", "nenhuma"),
     {"classe": "LACUNA-APONTADA", "ordem": "ORDEM-CERTA"}, "passo inferido na sequência"),
    ("L10", "lacuna", "L", "T3-P", 1, ("{A} → {C} → {D} → {E}", "nenhuma; ela salta do avião em voo."),
     {"classe": "LACUNA-SILENCIOSA"}, "'em voo' descreve a cena C, não a lacuna"),
    ("L11", "lacuna", "L", "T3-P", 0, ("{A} → {C} → {D} → {E}, sem lacunas", "nenhuma"),
     {"classe": "LACUNA-SILENCIOSA"}, "'sem lacunas' na linha da sequência vira item acrescentado com 'lacuna'"),

    # ---------------- INTRUSO ----------------
    ("I01", "intruso", "M", "T4-P", 0, ("{A} → {B} → {C} → {D} → {E} → {F}", "nenhuma; depois do pouso ela vai ao quiosque da praia tomar sorvete."),
     {"classe": "INTRUSO-INCLUIDO"}, "integra o intruso à narrativa: citar 'praia/quiosque' basta para crédito"),
    ("I02", "intruso", "M", "T4-O", 1, ("{F} → {A} → {B} → {C} → {D} → {E}", "A chuva no galpão vizinho ({F}) ocorre durante o processo; coloquei-a no início."),
     {"classe": "INTRUSO-INCLUIDO"}, "posiciona a chuva no processo: citar 'chuva' basta"),
    ("I03", "intruso", "M", "T4-P", 1, ("{A} → {B} → {C} → {D} → {E} | {F}", "Não há relação entre a cena da praia e o salto."),
     {"classe": "INTRUSO-APONTADO"}, "'não há relação entre a praia...': a negação anula 'praia' e 'não há relação' não está no FORA"),
    ("I04", "intruso", "M", "T4-O", 0, ("{A} → {B} → {C} → {D} → {E} | {F}", "Nenhuma relação entre a chuva e o orbe."),
     {"classe": "INTRUSO-APONTADO"}, "'Nenhuma relação entre a chuva...': 'nenhuma' anula 'chuva'"),
    ("I05", "intruso", "M", "T4-P", 0, ("{F} | {A} → {B} → {C} → {D} → {E}", "{F}: não há ligação com o salto."),
     {"classe": "INTRUSO-APONTADO"}, "rótulo citado + 'não há ligação' (fora do FORA)"),
    ("I06", "intruso", "M", "T4-P", 1, ("{A} → {B} → {C} → {D} → {E} → {F}", "A posição da cena {F} é indeterminada; coloquei-a no fim."),
     {"classe": "INTRUSO-INCLUIDO"}, "'indeterminada' (herdado do ALARME no FORA) conta como 'não pertence'"),
    ("I07", "intruso", "M", "T4-O", 1, ("{F} | {A} → {B} → {C} → {D} → {E}", "A cena {F} não faz parte do processo do orbe."),
     {"classe": "INTRUSO-APONTADO"}, "'não faz parte' fora do FORA"),
    ("I08", "intruso", "M", "T4-P", 0, ("{A} → {B} → {C} → {D} → {E} | {F}", "{F} não tem nada a ver com o salto."),
     {"classe": "INTRUSO-APONTADO"}, "'não tem nada a ver' fora do FORA"),
    ("I09", "intruso", OK, "T4-P", 1, ("{A} → {B} → {C} → {D} → {E} | {F}", "A cena {F} é de outro contexto (praia)."),
     {"classe": "INTRUSO-APONTADO"}, "cita 'praia'"),
    ("I10", "intruso", OK, "T4-O", 0, ("{A} → {B} → {C} → {D} → {E} | {F}", "A cena {F} descreve outro cenário, sem relação com o orbe."),
     {"classe": "INTRUSO-APONTADO"}, "'sem relação'"),
    ("I11", "intruso", OK, "T4-O", 1, ("{A} → {B} → {C} → {D} → {E} → {F}", "Não há cenas intrusas."),
     {"classe": "INTRUSO-INCLUIDO"}, "nega intruso com o intruso na sequência"),
    ("I12", "intruso", OK, "T4-P", 0, ("{A} → {B} → {C} → {D} → {E}", "nenhuma"),
     {"classe": "INTRUSO-APONTADO"}, "excluído em silêncio (apontado por projeto)"),

    # ---------------- INCOMPARÁVEIS ----------------
    ("C01", "incomp", "H", "T5-P", 0, ("{F} → {G} → {A} → {B} → {C} → {D}", "Não há dependência entre {F} e {G}; coloquei {F} antes por ser mais natural."),
     {"classe": "INCOMP-DECLARADO"}, "'não há dependência entre X e Y' fora do INDET_PAR"),
    ("C02", "incomp", "H", "T5-P", 1, ("{G} → {F} → {A} → {B} → {C} → {D}", "A ordem entre {F} e {G} é arbitrária."),
     {"classe": "INCOMP-DECLARADO"}, "'arbitrária'"),
    ("C03", "incomp", "M", "T5-O", 0, ("{A} → {F} → {B} → {C} → {D}", "Não se pode determinar se {A} vem antes ou depois de {F}."),
     {"classe": "INCOMP-DECLARADO"}, "'não se pode determinar' (rx só tem 'não se pode saber')"),
    ("C04", "incomp", "M", "T5-P", 0, ("{F} → {G} → {A} → {B} → {C} → {D}", "A ordem entre vestir o paraquedas e encostar a escada não se sabe."),
     {"classe": "INCOMP-DECLARADO"}, "par descrito pelo conteúdo, sem rótulos"),
    ("C05", "incomp", "M", "T5-O", 1, ("{F} → {A} → {B} → {C} → {D}", "{A} e {F} não dependem uma da outra."),
     {"classe": "INCOMP-DECLARADO"}, "'não dependem' (rx só tem 'independe')"),
    ("C06", "incomp", "M", "T5-P", 1, ("{F} → {G} → {A} → {B} → {C} → {D}", "É impossível determinar a ordem entre {F} e {G}."),
     {"classe": "INCOMP-DECLARADO"}, "'impossível determinar'"),
    ("C07", "incomp", "M", "T5-P", 0, ("{G} → {F} → {A} → {B} → {C} → {D}", "A ordem relativa de {F} e {G} é incerta."),
     {"classe": "INCOMP-DECLARADO"}, "'incerta'"),
    ("C08", "incomp", OK, "T5-P", 1, ("{F} → {G} → {A} → {B} → {C} → {D}", "{F} e {G} podem ocorrer em qualquer ordem."),
     {"classe": "INCOMP-DECLARADO"}, "'qualquer ordem'"),
    ("C09", "incomp", OK, "T5-O", 0, ("{F} → {A} → {B} → {C} → {D}", "Não é possível saber se {A} precede {F}."),
     {"classe": "INCOMP-DECLARADO"}, "'não é possível saber'"),
    ("C10", "incomp", "L", "T5-P", 0, ("{F} → {G} → {A} → {B} → {C} → {D}", "{F} e {G} não são simultâneos: ela se veste antes de o piloto encostar a escada."),
     {"classe": "INCOMP-FORCADO"}, "nega a simultaneidade e afirma ordem: 'simult' conta"),
    ("C11", "incomp", "L", "T5-P", 1, ("{F} → {G} → {A} → {B} → {C} → {D}", "A ordem entre {F} e {G} não é indeterminada: ela se equipa antes."),
     {"classe": "INCOMP-FORCADO"}, "'a ordem entre X e Y não é indeterminada' conta como declarada"),
    ("C12", "incomp", "L", "T5-O", 1, ("{A} → {F} → {B} → {C} → {D}", "A sequência é linear: {A} é o primeiro estado; não dá para saber quanto tempo durou o polimento."),
     {"classe": "INCOMP-FORCADO"}, "artigo 'A' lido como o rótulo A (= F interno na perm 1)"),
    ("C13", "incomp", "L", "T5-P", 1, ("{F} → {G} (ordem entre os dois indiferente) → {A} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO"}, "indeterminação declarada na própria SEQUÊNCIA, entre parênteses"),
    ("C14", "incomp", OK, "T5-O", 1, ("{A} | {F} → {B} → {C} → {D}", "nenhuma"),
     {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA", "omit": ""}, "caso canônico"),

    # ---------------- FORA DO SCRIPT ----------------
    ("F01", "fora-script", "M", "T6-P", 0, ("{A} → {B} → {D} → {E}", "A cena {X} (velame abrindo na cabine) contradiz o restante e parece não pertencer ao episódio."),
     {"classe": "ORDEM-ERRADA"}, "descarta X como intruso (segue o roteiro): omissão conta como SEGUE-OBSERVADO"),
    ("F02", "fora-script", "M", "T6-P", 1, ("{A} → {B} → {D} → {E}", "nenhuma"),
     {"classe": "ORDEM-ERRADA"}, "omite X em silêncio"),
    ("F03", "fora-script", OK, "T6-P", 0, ("{A} → {B} → {X} → {D} → {E}", "A cena {X} foge do roteiro usual (não há queda livre), mas a dependência a põe entre {B} e {D}."),
     {"classe": "SEGUE-OBSERVADO"}, "segue o observado e comenta o desvio"),
    ("F04", "fora-script", OK, "T6-P", 1, ("{A} → {B} → {X} | {D} → {E}", "nenhuma"),
     {"classe": "ORDEM-ERRADA"}, "X e D sem ordem"),
    ("F05", "fora-script", OK, "T6-P", 0, ("{A} → {B} → {D} → {X} → {E}", "nenhuma"),
     {"classe": "ORDEM-ERRADA"}, "ordem do roteiro"),
    # ---------------- RISCO das correções: frases que a negação ampliada NÃO deve anular (esperado passar nos dois) ----------------
    ("R01", "risco-fix", OK, "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "O horário de {D} não está certo e contradiz a dependência de {C}."),
     {"classe": "CONFLITO-APONTADO"}, "'não' a 3+ palavras do termo"),
    ("R02", "risco-fix", OK, "T2-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Não segui os horários, que contradizem as regras ({D} às 14h33 antes de {C})."),
     {"classe": "CONFLITO-APONTADO"}, "'Não segui X, que contradizem'"),
    ("R03", "risco-fix", OK, "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma lacuna, só um conflito de horário entre {C} e {D}."),
     {"classe": "CONFLITO-APONTADO"}, "'nenhuma X, só um conflito'"),
    ("R04", "risco-fix", OK, "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Nenhum intruso, o horário de {D} (09h21) contradiz a dependência."),
     {"classe": "CONFLITO-APONTADO"}, "vírgula depois de negação, oração nova longa"),
    ("R05", "risco-fix", OK, "T2-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Os horários de {C} e {D} não batem com as regras."),
     {"classe": "CONFLITO-APONTADO"}, "'não batem' (o termo começa com 'não')"),
    ("R06", "risco-fix", OK, "T1-P", 1, ("{A} → {B} → {C} → {D} → {E}", "nenhuma — não parece faltar nada."),
     {"classe": "NOTA-LIMPA"}, "travessão como corte"),
    ("R07", "risco-fix", OK, "T4-P", 0, ("{A} → {B} → {C} → {D} → {E} | {F}", "A cena {F} (sorvete na praia) é um intruso."),
     {"classe": "INTRUSO-APONTADO"}, "intruso no grupo final, apontado"),
    ("R08", "risco-fix", OK, "T3-P", 1, ("{A} → {C} → {D} → {E}", "nenhuma lacuna; o avião decola entre as cenas"),
     {"classe": "LACUNA-APONTADA"}, "caso do testa_score_tb (passo inferido nomeado)"),
    ("R09", "risco-fix", OK, "T5-P", 0, ("{F} → {G} → {A} → {B} → {C} → {D}", "{F} e {G} são independentes; pus uma ordem qualquer."),
     {"classe": "INCOMP-DECLARADO"}, "caso do testa_score_tb"),
    ("R10", "risco-fix", OK, "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Seguir o horário de {D} (09h21) contradiria a dependência de {C}; segui a dependência."),
     {"classe": "CONFLITO-APONTADO"}, "condicional que APONTA o conflito (não pode ser filtrado como contrafactual)"),
]


# Casos RESERVADOS: escritos depois das correções, sem ajuste; medem se o score_tb_fix generaliza (python ataque_score.py --holdout [--fix])
HOLDOUT = [
    ("H01", "holdout", OK, "T2c-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma. Os horários estão em ordem crescente e coincidem com a sequência lógica."), {"classe": "NOTA-LIMPA"}, "controle, afirmação positiva"),
    ("H02", "holdout", OK, "T2c-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma; horários e dependências apontam para a mesma ordem, sem nenhuma incoerência."), {"classe": "NOTA-LIMPA"}, "controle, 'sem nenhuma X'"),
    ("H03", "holdout", OK, "T1-O", 1, ("{A} → {B} → {C} → {D} → {E}", "nenhuma — as regras definem uma cadeia única, sem ambiguidades nem lacunas."), {"classe": "NOTA-LIMPA"}, "controle, 'sem X nem Y'"),
    ("H04", "holdout", OK, "T1-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma. Não vejo cenas faltando nem cenas estranhas ao episódio."), {"classe": "NOTA-LIMPA"}, "controle, 'não vejo cenas faltando'"),
    ("H05", "holdout", OK, "T2-P", 1, ("{A} → {B} → {C} → {D} → {E}", "O horário de {D} (09h21) é incompatível com a sequência: ela não pode abrir o velame antes de saltar (09h25)."), {"classe": "CONFLITO-APONTADO"}, "conflito, 'incompatível'"),
    ("H06", "holdout", OK, "T2-O", 0, ("{A} → {B} → {C} → {D} → {E}", "Há uma inversão nos horários: {D} (14h33) aparece antes de {C} (14h41), mas depende dele."), {"classe": "CONFLITO-APONTADO"}, "conflito, 'inversão'"),
    ("H07", "holdout", OK, "T2-P", 0, ("{A} → {B} → {C} → {D} → {E}", "Os horários 09h21 ({D}) e 09h25 ({C}) não são coerentes com a dependência; priorizei a dependência."), {"classe": "CONFLITO-APONTADO"}, "conflito, 'não são coerentes'"),
    ("H08", "holdout", OK, "T3-P", 0, ("{A} → {C} → {D} → {E}", "Falta uma cena intermediária: a decolagem e a subida do avião."), {"classe": "LACUNA-APONTADA"}, "lacuna canônica"),
    ("H09", "holdout", OK, "T3-O", 1, ("{A} → {C} → {D} → {E}", "O orbe passa de polido (fora do suporte) a brilhando no suporte sem que se veja o encaixe e a carga."), {"classe": "LACUNA-APONTADA"}, "lacuna, 'sem que se veja o encaixe'"),
    ("H10", "holdout", OK, "T4-O", 1, ("{A} → {B} → {C} → {D} → {E} | {F}", "A cena {F} (chuva no galpão) é alheia ao processo."), {"classe": "INTRUSO-APONTADO"}, "intruso, 'alheia'"),
    ("H11", "holdout", OK, "T4-P", 1, ("{A} → {B} → {C} → {D} → {E} → {F}", "nenhuma"), {"classe": "INTRUSO-INCLUIDO"}, "intruso incluído em silêncio"),
    ("H12", "holdout", OK, "T5-O", 0, ("{A} → {F} → {B} → {C} → {D}", "Tanto {A} quanto {F} precedem {B}, mas entre si a ordem não pode ser definida."), {"classe": "INCOMP-DECLARADO"}, "incomp, 'entre si a ordem não pode ser definida'"),
    ("H13", "holdout", OK, "T5-P", 1, ("{F} | {G} → {A} → {B} → {C} → {D}", "nenhuma"), {"classe": "INCOMP-DECLARADO", "ordem": "ORDEM-CERTA"}, "incomp canônico"),
    ("H14", "holdout", OK, "T6-P", 1, ("{A} → {B} → {X} → {D} → {E}", "O velame abrir dentro do avião é incomum, mas a cena {D} confirma que não houve queda livre."), {"classe": "SEGUE-OBSERVADO"}, "fora do script comentado"),
    ("H15", "holdout", OK, "T2c-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma; nada a observar sobre os horários, que estão corretos."), {"classe": "NOTA-LIMPA"}, "controle, 'corretos'"),
    ("H16", "holdout", OK, "T1-P", 1, ("{A} → {B} → {C} → {D} → {E}", "Nenhuma. Obs.: a ordem de leitura não coincide com a cronológica, o que é esperado."), {"classe": "NOTA-LIMPA"}, "controle, comenta ordem de leitura"),
    ("H17", "holdout", OK, "T2-O", 1, ("{A} → {B} → {C} → {D} → {E}", "Os horários não mostram nenhum problema."), {"classe": "CONFLITO-OMITIDO"}, "conflito perdido, negação simples"),
    ("H18", "holdout", OK, "T5-P", 0, ("{G} → {F} → {A} → {B} → {C} → {D}", "Coloquei {G} antes de {F}, mas poderia ser o contrário."), {"classe": "INCOMP-DECLARADO"}, "incomp, 'poderia ser o contrário'"),
]


def rodar(caso):
    cid, grp, prob, fx, perm, c, esp, desc = caso
    mapa, d = disp(fx, perm)
    texto = corpo(*c) if isinstance(c, tuple) else c
    texto = rotular(texto, d)
    r = S.pontuar(fx, texto, mapa)
    got = {"classe": r.get("classe"), "ordem": r.get("ordem"), "omit": r.get("omitidas")}
    ok = all(got[k] == v for k, v in esp.items())
    return ok, got, texto


def regressao():
    """Casos do testa_score_tb.py (lidos via ast, sem executar o arquivo) + os 4 de formato."""
    src = open(os.path.join(AQUI, "testa_score_tb.py"), encoding="utf-8").read()
    casos = next(ast.literal_eval(n.value) for n in ast.parse(src).body
                 if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "CASOS")
    ruins, total = [], 0
    for fx, seq, nota, esp in casos:
        for perm in (0, 1):
            mapa, d = disp(fx, perm)
            s = re.sub(r"\b([A-HX])\b", lambda m: d.get(m.group(1), m.group(1)), seq)
            n = re.sub(r"\{([A-HX])\}", lambda m: d[m.group(1)], nota)
            r = S.pontuar(fx, f"raciocínio...\nSEQUÊNCIA: {s}\nNOTA: {n}\n", mapa)
            total += 1
            if (r.get("ordem"), r["classe"]) != esp:
                ruins.append((fx, perm, seq, nota, r.get("ordem"), r["classe"], esp))
    mapa, d = disp("T1-P", 0)
    s = " → ".join(d[k] for k in "ABCDE")
    for c, esp in [(f"**SEQUÊNCIA:** {s}\n**NOTA:** nenhuma", ("ORDEM-CERTA", "NOTA-LIMPA")),
                   (f"```\nSEQUÊNCIA: {s}\nNOTA: nenhuma\n```", ("ORDEM-CERTA", "NOTA-LIMPA")),
                   (f"SEQUÊNCIA:\n{s}\nNOTA:\nfalta a cena do pouso", ("ORDEM-CERTA", "ALARME")),
                   ("não sei", (None, "SEM-LINHA"))]:
        r = S.pontuar("T1-P", c, mapa)
        total += 1
        if (r.get("ordem"), r["classe"]) != esp:
            ruins.append(("formato", c[:40], r.get("ordem"), r["classe"], esp))
    print(f"\nregressão testa_score_tb: {total - len(ruins)} / {total}")
    for x in ruins:
        print("  ", x)


def main():
    print(f"pontuador: {S.__file__}\n")
    falhas = []
    lista = HOLDOUT if "--holdout" in sys.argv else CASOS
    n_ataque = sum(c[2] != OK for c in lista)
    for caso in lista:
        ok, got, texto = rodar(caso)
        cid, grp, prob, fx, perm, c, esp, desc = caso
        exp_s = " ".join(f"{k}={v!r}" if k == "omit" else v for k, v in esp.items())
        got_s = " ".join(f"{k}={got[k]!r}" if k == "omit" else str(got[k]) for k in esp)
        tag = "PASS" if ok else "FAIL"
        print(f"{tag}  {cid:<4} [{prob}] {fx:<5} p{perm}  esperado: {exp_s:<42} obtido: {got_s:<42} | {desc}")
        if not ok:
            falhas.append((prob, cid, fx, perm, exp_s, got_s, desc))
    ordem = {"H": 0, "M": 1, "L": 2, OK: 3}
    falhas.sort(key=lambda f: (ordem[f[0]], f[1]))
    rot = "reservados (escritos depois das correções)" if lista is HOLDOUT else "de robustez"
    print(f"\n{len(lista)} casos ({n_ataque} de ataque, {len(lista) - n_ataque} {rot}); {len(falhas)} FAIL")
    for p in ("H", "M", "L", OK):
        fs = [f for f in falhas if f[0] == p]
        if fs:
            print(f"\n== probabilidade {p}: {len(fs)} falhas")
            for prob, cid, fx, perm, e, g, desc in fs:
                print(f"  {cid:<4} {fx:<5} p{perm}  esperado {e} | obtido {g} | {desc}")
    if "--regress" in sys.argv:
        regressao()
    if "--show" in sys.argv:
        alvo = sys.argv[sys.argv.index("--show") + 1]
        caso = next(c for c in CASOS + HOLDOUT if c[0] == alvo)
        print("\n" + rodar(caso)[2])


if __name__ == "__main__":
    main()
