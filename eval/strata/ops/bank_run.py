#!/usr/bin/env python3
"""bank_run.py — banco de capacidades de modelos para o Strata (conserto / armadilha / abstencao).

Roda o nucleo F4 por modelo, pontua com o verificador MECANICO (verify_f4, gate GOLD) e grava um
resumo por celula. Regra de parada: o conserto (§5) vem primeiro; se o modelo nao passa em pelo
menos 2 de K, as outras celulas nao rodam ("nao atende": nao se gasta medicao com quem nao faz o
basico). Custo e tempo vem dos cabecalhos dos planos (custo real devolvido pelo provedor).

Celulas: fix = f4-dup (PASS), trap = f4-trap (PASS, payload local), abst = f4-clean-v2
(ABSTENCAO_CORRETA; a f4-clean original vazava a resposta).

Uso:
  python ops/bank_run.py --provider nvidia --models moonshotai/kimi-k3 z-ai/glm-5.3 --k 3
  python ops/bank_run.py --provider openrouter --models openai/gpt-6-luna --reasoning off
Saida bruta: planos/<tag>/ (gitignored); resumo: planos/<tag>/summary.jsonl
"""
import argparse
import json
import os
import re
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
CELLS = {
    "fix": ("cenarios/f4-dup", "f4-manifests/f4-dup.json", "PASS"),
    "trap": ("cenarios/f4-trap", "f4-manifests/f4-trap.json", "PASS"),
    "abst": ("cenarios/f4-clean-v2", "f4-manifests/f4-clean-v2.json", "ABSTENCAO_CORRETA"),
}
HDR = re.compile(r"<!--(.*?)-->", re.DOTALL)


def header_meta(path):
    txt = open(path, encoding="utf-8", errors="replace").read(1500)
    m = HDR.search(txt)
    out = {}
    if not m:
        return out
    for part in m.group(1).split("|"):
        part = part.strip()
        if part.endswith("s") and part[:-1].isdigit():
            out["secs"] = int(part[:-1])
        elif part.endswith(" tok") and part.split()[0].isdigit():
            out["tok"] = int(part.split()[0])
        elif "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def run_cell(a, model, cell):
    target, manifest, ok_verdict = CELLS[cell]
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", model)
    label = f"{a.tag}/{cell}-{a.provider}-{safe}-r{a.reasoning}"
    outdir = os.path.join(HERE, "planos", label)
    cmd = [PY, os.path.join(HERE, "runners", "hb_f4.py"), "--provider", a.provider,
           "--models", model, "--target", os.path.join(HERE, target), "--label", label,
           "--runs", str(a.k), "--num-ctx", str(a.num_ctx), "--num-predict", str(a.num_predict),
           "--reasoning", a.reasoning]
    env = dict(os.environ, PYTHONUTF8="1")
    subprocess.run(cmd, cwd=HERE, env=env, check=False)
    subprocess.run([PY, os.path.join(HERE, "verify", "verify_f4.py"), "--indir", outdir,
                    "--fixture", os.path.join(HERE, target), "--manifest", os.path.join(HERE, manifest)],
                   cwd=HERE, env=env, check=False, capture_output=True)
    scores_p = os.path.join(outdir, "f4-mech-scores.json")
    scores = json.load(open(scores_p, encoding="utf-8")) if os.path.exists(scores_p) else []
    verdicts = {}
    for s in scores:
        verdicts[s["verdict"]] = verdicts.get(s["verdict"], 0) + 1
    errors = len([f for f in os.listdir(outdir) if f.endswith(".ERROR.txt")]) if os.path.isdir(outdir) else a.k
    metas = [header_meta(os.path.join(outdir, s["file"])) for s in scores]
    costs = [float(m["cost"]) for m in metas if m.get("cost") not in (None, "None", "")]
    secs = [m["secs"] for m in metas if "secs" in m]
    rtok = [int(m["rtok"]) for m in metas if str(m.get("rtok", "")).isdigit()]
    row = {"model": model, "provider": a.provider, "cell": cell, "reasoning": a.reasoning, "k": a.k,
           "ok": verdicts.get(ok_verdict, 0), "verdicts": verdicts, "errors": errors,
           "cost_total": round(sum(costs), 5) if costs else None,
           "secs_median": statistics.median(secs) if secs else None,
           "rtok_median": statistics.median(rtok) if rtok else None,
           "served_by": sorted({m.get("provider", "") for m in metas})}
    with open(os.path.join(HERE, "planos", a.tag, "summary.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"## {model} [{a.provider}, reasoning={a.reasoning}] {cell}: {row['ok']}/{a.k} "
          f"{verdicts} err={errors} cost={row['cost_total']} secs~{row['secs_median']}", flush=True)
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True, choices=["openrouter", "cerebras", "groq", "nvidia", "ollama"])
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--cells", nargs="+", default=["fix", "trap", "abst"], choices=list(CELLS))
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--reasoning", default="default", choices=["default", "off", "low", "medium", "high"])
    ap.add_argument("--tag", default="bank26")
    ap.add_argument("--num-ctx", type=int, default=20480)
    ap.add_argument("--num-predict", type=int, default=12000)
    ap.add_argument("--no-stop", action="store_true", help="roda todas as celulas mesmo se o conserto falhar")
    a = ap.parse_args()
    os.makedirs(os.path.join(HERE, "planos", a.tag), exist_ok=True)
    need = (a.k // 2) + 1  # maioria de K (2 de 3)
    for m in a.models:
        fix_ok, infra = None, False
        for cell in a.cells:
            # erro de provedor (402/429/timeout) nao e medida de capacidade: para o modelo, mas
            # registra como infra, nunca como "nao atende"
            reason = ("infra_error" if infra else
                      "fix_below_majority" if (cell != "fix" and fix_ok is not None and fix_ok < need
                                               and not a.no_stop) else None)
            if reason:
                print(f"## {m}: {cell} PULADA ({reason})", flush=True)
                with open(os.path.join(HERE, "planos", a.tag, "summary.jsonl"), "a", encoding="utf-8") as f:
                    f.write(json.dumps({"model": m, "provider": a.provider, "cell": cell,
                                        "reasoning": a.reasoning, "skipped": reason}) + "\n")
                continue
            row = run_cell(a, m, cell)
            if row["errors"] >= a.k:
                infra = True
            elif cell == "fix":
                # maioria sobre as runs PONTUAVEIS; erro de provedor nao conta como falha
                fix_ok = row["ok"] if (a.k - row["errors"]) >= need else None
                if fix_ok is None:
                    infra = True


if __name__ == "__main__":
    main()
