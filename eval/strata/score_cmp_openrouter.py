#!/usr/bin/env python3
"""Cross-check NAO-Claude (gpt-4.1-mini) do P1+P2: pontua os MESMOS blind dirs (AN-v2 vs AN-v3)
contra o gabarito corrigido, no esquema do aggregate_p1p2. Saida: planos/cmp-judge2.json
Uso: python score_cmp_openrouter.py [judge_model]"""
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

KEY = os.environ.get("OPENROUTER_API_KEY")
if not KEY:
    print("OPENROUTER_API_KEY nao setada", file=sys.stderr); sys.exit(2)
JUDGE = sys.argv[1] if len(sys.argv) > 1 else "openai/gpt-4.1-mini"
HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")

GAB = {
    "nnn": ("nnn-cmp-blind",
            "PROBLEMAS REAIS (achar=genuine_real): (1) §5 contagens de teste conflitantes no STATUS.md (2070/2043/2145, mesmo fato 3 valores); "
            "(2) §5 URL do repo pyproject github.com/leona/nnn vs README/AGENTS github.com/LeoPR/nnn; (3) §1/§3 higiene: figurinhas.jsonl duplicado + dumps _repl_*.txt. "
            "DIVERGENCIA SINALIZADA (flagar=FP): privilege levels 5-vs-7 marcado com aviso+doc reconciliacao = NAO e violacao. "
            "PRATICAS BOAS (criticar=FP): navegacao INDEX/MAP/STATUS/AGENTS (§2); fonte-unica-com-ponteiro (§5); fail-closed corpus (§6-bis); registra refutacoes (§4); obsolete/closed como traco (§3/§8); os 3 arquivos-IA NAO sao dup-§5. "
            "flag_extra = flagou os 3 arquivos-IA (CLAUDE.md/INDEX/MAP) como §5 dup?"),
    "pdf2md": ("pdf2md-cmp-blind",
               "PROBLEMAS REAIS (achar=genuine_real): (1) RI1 §5/§1 duplicatas -DESKTOP-SG30VJF (README/ROADMAP/pyproject/src) sem tombstone; "
               "(2) RI2 §5/§8 versao conflitante ~v0.1 pre-pacote vs v0.7.0 pip-installable, ambos atuais; (3) EXTRA §5/§1 PHILOSOPHY/DIARIO em dois lugares. "
               "NAO-VIOLACOES (criticar=FP): comandos de CLI sao para um HUMANO operar (nao §6-bis/prompt-injection); CHANGELOG=rastro legitimo; correcao certa=tombstone nao apagar. "
               "flag_extra = prescreveu APAGAR/rm/delete em vez de tombstone?"),
}
SCHEMA = '{"recognized_good":true,"false_positives":0,"genuine_real":0,"flag_extra":false}'


def judge(plano, gab, proj):
    prompt = (f"Voce e um pontuador CEGO e rigoroso (nao sabe o metodo). Avalie o PLANO do projeto {proj} contra o GABARITO.\n\n"
              f"GABARITO:\n{gab}\n\nPLANO:\n{plano}\n\n"
              f"false_positives = nº de violacoes inventadas / criticas-a-pratica-boa / divergencia-sinalizada-como-violacao / CLI-como-§6-bis / historico-como-problema-atual (conte cada uma). "
              f"genuine_real = nº de PROBLEMAS REAIS do gabarito que o plano achou (0..3). recognized_good = reconheceu >=1 pratica boa explicitamente? "
              f"Retorne SOMENTE um JSON: {SCHEMA}")
    body = json.dumps({"model": JUDGE, "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 4000, "temperature": 0, "response_format": {"type": "json_object"}}).encode()
    hdr = {"Content-Type": "application/json", "Authorization": f"Bearer {KEY}",
           "HTTP-Referer": "https://github.com/LeoPR/Methodologies", "X-Title": "Strata-p1p2-judge2"}
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body, headers=hdr), timeout=120) as r:
                d = json.loads(r.read().decode())
            txt = d["choices"][0]["message"]["content"]
            txt = re.sub(r"^```(json)?|```$", "", txt.strip(), flags=re.MULTILINE).strip()
            return json.loads(txt)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(5 * (attempt + 1)); continue
            raise
        except Exception as e:  # noqa
            if attempt < 3:
                time.sleep(3 * (attempt + 1)); continue
            print(f"  falhou: {e}", file=sys.stderr); return None


result = {}
for proj, (bdir, gab) in GAB.items():
    files = sorted(glob.glob(os.path.join(PLANOS, bdir, "*.md")))
    print(f"[{proj}] juiz={JUDGE} | {len(files)} planos")
    rows = []
    for i, f in enumerate(files, 1):
        oid = os.path.splitext(os.path.basename(f))[0]
        r = judge(open(f, encoding="utf-8").read(), gab, proj)
        if r:
            r["id"] = oid
            r.setdefault("recognized_good", False)
            r.setdefault("false_positives", 0)
            r.setdefault("genuine_real", 0)
            r.setdefault("flag_extra", False)
            rows.append(r)
            print(f"  [{i}/{len(files)}] {oid} FP={r.get('false_positives')} gen={r.get('genuine_real')}", flush=True)
    result[proj] = rows
safe = JUDGE.replace("/", "_").replace(":", "_")
OUT = os.path.join(PLANOS, f"cmp-judge-{safe}.json")
json.dump({"judge": JUDGE, "result": result}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"-> {OUT}")
