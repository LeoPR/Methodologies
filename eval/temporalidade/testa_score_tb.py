"""Casos de unidade do score_tb (uso: python testa_score_tb.py): sequências escritas em letras INTERNAS, convertidas para rótulos de exibição
pelo mapa da apresentação 0; notas escritas já com rótulos de exibição quando citam cena (via {X})."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
import score_tb as S  # noqa: E402


def caso(fx, seq_int, nota, perm=0, bruto=None):
    mapa = "".join(S.BAT["fixtures"][fx]["apresentacao"][perm])
    disp = {k: S.ROTULOS[i] for i, k in enumerate(mapa)}
    seq = re.sub(r"\b([A-HX])\b", lambda m: disp.get(m.group(1), m.group(1)), seq_int)
    nota = re.sub(r"\{([A-HX])\}", lambda m: disp[m.group(1)], nota)
    corpo = bruto if bruto is not None else f"raciocínio...\nSEQUÊNCIA: {seq}\nNOTA: {nota}\n"
    return S.pontuar(fx, corpo, mapa)


CASOS = [
    # controles: ordem e falso alarme
    ("T1-P", "A → B → C → D → E", "nenhuma", ("ORDEM-CERTA", "NOTA-LIMPA")),
    ("T1-P", "A → C → B → D → E", "nenhuma", ("ORDEM-ERRADA", "NOTA-LIMPA")),
    ("T1-P", "A → B → C → D → E", "não há lacunas nem conflitos; a ordem sai da dependência", ("ORDEM-CERTA", "NOTA-LIMPA")),
    ("T1-P", "A → B → C → D → E", "falta a cena em que ela caminha até a porta", ("ORDEM-CERTA", "ALARME")),
    ("T1-O", "A → B → C → D → E", "nenhuma; tudo inferido pelas regras", ("ORDEM-CERTA", "NOTA-LIMPA")),
    ("T2c-O", "A → B → C → D → E", "os horários estão coerentes com a dependência", ("ORDEM-CERTA", "NOTA-LIMPA")),
    ("T2c-P", "A → B → C → D → E", "sem inconsistências entre horários e dependências", ("ORDEM-CERTA", "NOTA-LIMPA")),
    ("T6-P", "A → B → X → D → E", "nenhuma", ("ORDEM-CERTA", "SEGUE-OBSERVADO")),
    ("T6-P", "A → B → X → D → E", "o velame abrir na cabine contradiz o esperado", ("ORDEM-CERTA", "SEGUE-OBSERVADO")),
    ("T6-P", "A → B → D → X → E", "nenhuma", ("ORDEM-ERRADA", "ORDEM-ERRADA")),
    # horário errado
    ("T2-P", "A → B → C → D → E", "o horário de {D} (09h21) é anterior ao de {C} (09h25), o que contradiz a dependência", ("ORDEM-CERTA", "CONFLITO-APONTADO")),
    ("T2-P", "A → B → D → C → E", "nenhuma", ("ORDEM-ERRADA", "CONFLITO-OMITIDO")),
    ("T2-P", "A → B → C → D → E", "os horários confirmam a ordem; não há conflito", ("ORDEM-CERTA", "CONFLITO-OMITIDO")),
    ("T2-O", "A → B → C → D → E", "A marcação 14h33 de {D} está errada: o selo só se rompe com o orbe brilhando", ("ORDEM-CERTA", "CONFLITO-APONTADO")),
    ("T2-O", "A → B → C → D → E", "A cena {D} possui horário (14h33) anterior à cena {C} (14h41), mas logicamente deve ocorrer depois, pois o selo só rompe após o orbe brilhar.", ("ORDEM-CERTA", "CONFLITO-APONTADO")),
    ("T2-P", "A → B → C → D → E", "O horário de {D} vem antes do de {C}, mas a dependência manda {C} primeiro.", ("ORDEM-CERTA", "CONFLITO-APONTADO")),
    ("T2-P", "A → B → C → D → E", "nenhuma; os horários seguem a ordem lógica", ("ORDEM-CERTA", "CONFLITO-OMITIDO")),
    ("T2-O", "A → B → C → D → E", "A cena {D} possui um horário (14h33) que precede a cena {C} (14h41), mas a regra do processo exige que o brilho ({C}) ocorra antes do rompimento do selo ({D})", ("ORDEM-CERTA", "CONFLITO-APONTADO")),
    ("T2-P", "A → B → C | D → E", "A ordem entre {D} e {C} não pode ser determinada; os tempos indicam {D} antes de {C}, mas a lógica narrativa sugere {C} antes", ("ORDEM-ERRADA", "CONFLITO-APONTADO")),
    # lacuna
    ("T3-P", "A → C → D → E", "falta a decolagem: do chão ela aparece acima das nuvens", ("ORDEM-CERTA", "LACUNA-APONTADA")),
    ("T3-P", "A → C → D → E", "nenhuma", ("ORDEM-CERTA", "LACUNA-SILENCIOSA")),
    ("T3-P", "A → [decolagem, inferida] → C → D → E", "nenhuma", ("ORDEM-CERTA", "LACUNA-APONTADA")),
    ("T3-P", "A → C → D → E", "nenhuma lacuna; o avião decola entre as cenas", ("ORDEM-CERTA", "LACUNA-APONTADA")),
    ("T3-O", "A → C → D → E", "não há cena do orbe encaixado e carregado", ("ORDEM-CERTA", "LACUNA-APONTADA")),
    ("T3-O", "A → C → D → E", "nenhuma", ("ORDEM-CERTA", "LACUNA-SILENCIOSA")),
    # intruso
    ("T4-P", "A → B → C → D → E", "a cena {F} (sorvete na praia) não pertence ao episódio", ("ORDEM-CERTA", "INTRUSO-APONTADO")),
    ("T4-P", "A → B → C → D → E → F", "nenhuma", ("ORDEM-CERTA", "INTRUSO-INCLUIDO")),
    ("T4-P", "A → B → C → D → E", "nenhuma", ("ORDEM-CERTA", "INTRUSO-APONTADO")),
    ("T4-O", "A → B → C → D → E | F", "{F} não se relaciona com o processo do orbe", ("ORDEM-CERTA", "INTRUSO-APONTADO")),
    ("T4-O", "F → A → B → C → D → E", "nenhuma", ("ORDEM-CERTA", "INTRUSO-INCLUIDO")),
    ("T4-O", "F | A → B → C → D → E", "A cena {F} não possui vínculo lógico com o processo.", ("ORDEM-CERTA", "INTRUSO-APONTADO")),
    ("T4-O", "F | A → B → C → D → E", "A cena {F} é um evento independente.", ("ORDEM-CERTA", "INTRUSO-APONTADO")),
    ("T4-P", "F | A → B → C → D → E", "A cena {F} mostra outro lugar, mas está incluída.", ("ORDEM-CERTA", "INTRUSO-INCLUIDO")),
    # incomparáveis
    ("T5-P", "F | G → A → B → C → D", "nenhuma", ("ORDEM-CERTA", "INCOMP-DECLARADO")),
    ("T5-P", "F → G → A → B → C → D", "nenhuma", ("ORDEM-CERTA", "INCOMP-FORCADO")),
    ("T5-P", "F → A | G → B → C → D", "nenhuma", ("ORDEM-ERRADA", "INCOMP-FORCADO")),
    ("T5-P", "F → G → A → B → C → D", "a ordem entre {F} e {G} não dá para saber", ("ORDEM-CERTA", "INCOMP-DECLARADO")),
    ("T5-P", "G → F → A → B → C → D", "{F} e {G} são independentes; pus uma ordem qualquer", ("ORDEM-CERTA", "INCOMP-DECLARADO")),
    ("T5-O", "A | F → B → C → D", "nenhuma", ("ORDEM-CERTA", "INCOMP-DECLARADO")),
    ("T5-O", "F → A → B → C → D", "nenhuma", ("ORDEM-CERTA", "INCOMP-FORCADO")),
]


def main():
    ruins = []
    for fx, seq, nota, esp in CASOS:
        for perm in (0, 1):
            r = caso(fx, seq, nota, perm)
            if (r.get("ordem"), r["classe"]) != esp:
                ruins.append((fx, perm, seq, nota, r.get("ordem"), r["classe"], esp))
    # formato: negrito, bloco de código, NOTA em várias linhas, sem linha
    fx = "T1-P"
    mapa = "".join(S.BAT["fixtures"][fx]["apresentacao"][0])
    d = {k: S.ROTULOS[i] for i, k in enumerate(mapa)}
    s = " → ".join(d[k] for k in "ABCDE")
    formatos = [
        (f"**SEQUÊNCIA:** {s}\n**NOTA:** nenhuma", ("ORDEM-CERTA", "NOTA-LIMPA")),
        (f"```\nSEQUÊNCIA: {s}\nNOTA: nenhuma\n```", ("ORDEM-CERTA", "NOTA-LIMPA")),
        (f"SEQUÊNCIA:\n{s}\nNOTA:\nfalta a cena do pouso", ("ORDEM-CERTA", "ALARME")),
        ("não sei", (None, "SEM-LINHA")),
    ]
    for corpo, esp in formatos:
        r = S.pontuar(fx, corpo, mapa)
        if (r.get("ordem"), r["classe"]) != esp:
            ruins.append(("formato", corpo[:40], r.get("ordem"), r["classe"], esp))
    total = len(CASOS) * 2 + len(formatos)
    print(f"{total - len(ruins)} / {total}")
    for x in ruins:
        print(x)


def testa_carregar():
    """carregar(): cabeçalho antigo e novo, provedor com espaço, stop=length -> SEM-LINHA (vence a revisão manual),
    'stop=length' no corpo não conta."""
    import shutil
    import tempfile
    fx = "T1-P"
    mapa = "".join(S.BAT["fixtures"][fx]["apresentacao"][0])
    d = {k: S.ROTULOS[i] for i, k in enumerate(mapa)}
    certo = "SEQUÊNCIA: " + " → ".join(d[k] for k in "ABCDE") + "\nNOTA: nenhuma\n"
    base = (f"<!-- TB | fixture={fx} | arm=ingenuo | perm=0 | model=x/y | run={{run}} | mapa={mapa} | 2026-09-30T00:00:00 | "
            "1s | 10 tok | stop={stop} | cost=0.0 | provider={prov}{extra} -->\n\n")
    casos = {
        "antigo": (base.format(run=1, stop="stop", prov="nvidia/nvidia", extra=""), certo),
        "novo": (base.format(run=2, stop="stop", prov="openrouter/Google AI Studio",
                             extra=' | rota={"only":["google-ai-studio"],"allow_fallbacks":false} | ft=1 | rtok=5'), certo),
        "cortado": (base.format(run=3, stop="length", prov="nvidia/nvidia", extra=" | rota=- | ft=0 | rtok=7990"), certo),
        "corpo": (base.format(run=1, stop="stop", prov="nvidia/nvidia", extra=""), "texto com | stop=length no corpo\n" + certo),
    }
    tmp = tempfile.mkdtemp()
    ruins = []
    try:
        for nome, (cab, corpo) in casos.items():
            p = os.path.join(tmp, nome, fx, "ingenuo", "p0")
            os.makedirs(p)
            open(os.path.join(p, f"x_y-r{nome}.md"), "w", encoding="utf-8").write(cab + corpo)
        # revisão manual tentando desfazer o corte
        open(os.path.join(tmp, "cortado-revisao.csv"), "w", encoding="utf-8").write(
            "arquivo,classe\n" + os.path.join(fx, "ingenuo", "p0", "x_y-rcortado.md") + ",NOTA-LIMPA\n")
        esp = {
            "antigo": dict(classe="NOTA-LIMPA", ordem="ORDEM-CERTA", provedor="nvidia/nvidia", rota="", ft=""),
            "novo": dict(classe="NOTA-LIMPA", ordem="ORDEM-CERTA", provedor="openrouter/Google AI Studio",
                         rota='{"only":["google-ai-studio"],"allow_fallbacks":false}', ft="1"),
            "cortado": dict(classe="SEM-LINHA", ordem="", classe_auto="NOTA-LIMPA", rota="-", ft="0"),
            "corpo": dict(classe="NOTA-LIMPA", stop="stop"),
        }
        for nome, e in esp.items():
            r = S.carregar(os.path.join(tmp, nome))[0]
            for k, v in e.items():
                if r[k] != v:
                    ruins.append((nome, k, r[k], v))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    n = sum(len(e) for e in esp.values())
    print(f"carregar: {n - len(ruins)} / {n}")
    for x in ruins:
        print("  ", x)


main()
testa_carregar()
