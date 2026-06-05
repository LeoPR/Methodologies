#!/usr/bin/env python3
"""
parse_usage.py — instrumento de medição do Estágio 1 (plano-experimental.md, A1).

Lê os transcripts JSONL do Claude Code (~/.claude/projects/**/*.jsonl) READ-ONLY
e agrega os 6 campos canônicos de token por (sessão, modelo), com:

  - DEDUP por message.id (== requestId): a mesma resposta da API aparece em
    várias linhas (streaming/relog); contar por linha infla ~4-7x. Verificado
    no schema real (2026-06-04): 1472 linhas-com-usage / 327 message.id distintos.
  - Modelo '<synthetic>' EXCLUÍDO do custo (não é resposta real de API), contado à parte.
  - Modelo desconhecido (ex.: backend local via ANTHROPIC_BASE_URL) -> custo NULL, não 0.
  - Sidechain (subagentes, path contém '/subagents/') separado do main por flag.
  - Custo USD é PROXY (tabela datada abaixo), NÃO faturado: o ambiente é Claude Max
    (quota por janela), mas o JSONL grava service_tier 'standard'. Use como métrica
    comparável entre condições, nunca como valor contábil.

NÃO faz nenhuma chamada de API. Custo de execução = zero (só leitura de disco).

Uso:
    python parse_usage.py --out baseline_metrics.csv
    python parse_usage.py --validate <arquivo.jsonl>   # dump dedup p/ conferência manual
"""
from __future__ import annotations
import argparse
import csv
import glob
import json
import os
import sys
from collections import defaultdict

# ---------------------------------------------------------------------------
# Tabela de preços — PROXY. Confirme antes de tratar como contábil.
# Fonte: pública Anthropic API (USD por 1M tokens). Data desta tabela: 2026-06-04.
# cache_read = 0.1x input; cache_write_5m = 1.25x input; cache_write_1h = 2x input.
# ATENÇÃO: preços de Opus 4.8 precisam de confirmação do dono (síntese do lab citou
#   $5/$25; fontes mais antigas citam $15/$75 p/ Opus). Edite aqui e re-rode.
# ---------------------------------------------------------------------------
PRICE_TABLE_DATE = "2026-06-04"
PRICE_TABLE_NOTE = "PROXY API-standard, NAO faturado (ambiente Max=quota). Confirmar Opus 4.8."
# prefixo-normalizado -> (in, out) por MTok
PRICES = {
    "claude-opus-4":   (5.00, 25.00),   # CONFIRMAR: síntese lab cita 5/25; verificar
    "claude-sonnet-4": (3.00, 15.00),
    "claude-haiku-4":  (1.00,  5.00),
    "claude-opus-3":   (15.00, 75.00),
    "claude-sonnet-3": (3.00, 15.00),
    "claude-haiku-3":  (0.80,  4.00),
}


def price_for(model: str):
    """Retorna (in,out) por MTok para o modelo, ou None se desconhecido."""
    if not model or model == "<synthetic>":
        return None
    for prefix, pr in PRICES.items():
        if model.startswith(prefix):
            return pr
    return None  # desconhecido -> custo NULL (não 0)


def est_cost_usd(u: dict, model: str):
    """Custo proxy em USD. None se modelo desconhecido/sintético."""
    pr = price_for(model)
    if pr is None:
        return None
    p_in, p_out = pr
    p_read = p_in * 0.1
    cc = u.get("cache_creation") or {}
    w5 = cc.get("ephemeral_5m_input_tokens", 0) or 0
    w1 = cc.get("ephemeral_1h_input_tokens", 0) or 0
    # fallback: se o split não bate, usa cache_creation_input_tokens como 5m
    cc_total = u.get("cache_creation_input_tokens", 0) or 0
    if (w5 + w1) == 0 and cc_total:
        w5 = cc_total
    cost = (
        (u.get("input_tokens", 0) or 0) * p_in
        + (u.get("output_tokens", 0) or 0) * p_out
        + (u.get("cache_read_input_tokens", 0) or 0) * p_read
        + w5 * (p_in * 1.25)
        + w1 * (p_in * 2.0)
    ) / 1_000_000
    return round(cost, 6)


def default_base() -> str:
    return os.path.join(
        os.path.expanduser("~"),
        ".claude", "projects",
        "c--Users-leona-OneDrive-Documents-Projects-Acad-micos-Methodologies",
    )


def iter_usage_records(base: str, until=None, since=None, exclude_session=None):
    """Gera (message_id, session_id, model, usage, is_sidechain, file_rel) por linha
    de assistant com usage. Conta parse-fails.

    Filtros de JANELA FECHADA (p/ snapshot reproduzível, A3):
      until/since: ISO timestamp (string) — compara com d['timestamp'] lexicograficamente
                   (ISO-8601 UTC ordena como string). Registro sem timestamp é incluído.
      exclude_session: sessionId a excluir (ex.: a sessão ativa, que ainda cresce).
    """
    parse_fails = 0
    total_lines = 0
    for path in glob.glob(os.path.join(base, "**", "*.jsonl"), recursive=True):
        rel = os.path.relpath(path, base)
        is_side = ("subagents" + os.sep) in (rel + os.sep) or "/subagents/" in rel.replace(os.sep, "/")
        try:
            fh = open(path, encoding="utf-8")
        except OSError:
            parse_fails += 1
            continue
        with fh:
            for ln in fh:
                ln = ln.strip()
                if not ln:
                    continue
                total_lines += 1
                try:
                    d = json.loads(ln)
                except json.JSONDecodeError:
                    parse_fails += 1
                    continue
                msg = d.get("message")
                if not isinstance(msg, dict):
                    continue
                u = msg.get("usage")
                if not isinstance(u, dict) or msg.get("role") != "assistant":
                    continue
                mid = msg.get("id")
                if not mid:
                    continue
                sid = d.get("sessionId", "?")
                if exclude_session and sid == exclude_session:
                    continue
                ts = d.get("timestamp")
                if ts is not None:
                    if until and ts >= until:
                        continue
                    if since and ts < since:
                        continue
                model = msg.get("model", "?")
                yield mid, sid, model, u, is_side, rel
    iter_usage_records.parse_fails = parse_fails
    iter_usage_records.total_lines = total_lines


def aggregate(base: str, include_sidechain: bool, until=None, since=None, exclude_session=None):
    """Dedup por message.id, agrega por (session, model, is_sidechain)."""
    seen = {}  # message_id -> True
    agg = defaultdict(lambda: dict(
        input_tokens=0, output_tokens=0, cache_creation_input_tokens=0,
        cache_read_input_tokens=0, est_cost_usd=0.0, n_messages=0, cost_is_null=False,
    ))
    synthetic = 0
    for mid, sid, model, u, is_side, rel in iter_usage_records(
            base, until=until, since=since, exclude_session=exclude_session):
        if is_side and not include_sidechain:
            # ainda dedup global, mas não agrega
            seen.setdefault(mid, True)
            continue
        if mid in seen:
            continue  # DEDUP
        seen[mid] = True
        if model == "<synthetic>":
            synthetic += 1
            continue
        key = (sid, model, is_side)
        row = agg[key]
        row["input_tokens"] += u.get("input_tokens", 0) or 0
        row["output_tokens"] += u.get("output_tokens", 0) or 0
        row["cache_creation_input_tokens"] += u.get("cache_creation_input_tokens", 0) or 0
        row["cache_read_input_tokens"] += u.get("cache_read_input_tokens", 0) or 0
        row["n_messages"] += 1
        c = est_cost_usd(u, model)
        if c is None:
            row["cost_is_null"] = True
        else:
            row["est_cost_usd"] += c
    return agg, synthetic, len(seen)


def write_csv(agg, out_path):
    cols = ["session_id", "model", "is_sidechain", "n_messages",
            "input_tokens", "output_tokens", "cache_creation_input_tokens",
            "cache_read_input_tokens", "est_cost_usd", "price_table_date"]
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for (sid, model, is_side), r in sorted(agg.items()):
            cost = "NULL" if r["cost_is_null"] else round(r["est_cost_usd"], 4)
            w.writerow([sid, model, is_side, r["n_messages"],
                        r["input_tokens"], r["output_tokens"],
                        r["cache_creation_input_tokens"], r["cache_read_input_tokens"],
                        cost, PRICE_TABLE_DATE])


def validate(path: str):
    """Dump dedup de UM arquivo p/ conferência manual linha-a-linha (GATE-1)."""
    per_id = defaultdict(list)
    lines = 0
    with open(path, encoding="utf-8") as fh:
        for i, ln in enumerate(fh, 1):
            ln = ln.strip()
            if not ln:
                continue
            lines += 1
            try:
                d = json.loads(ln)
            except json.JSONDecodeError:
                continue
            msg = d.get("message") or {}
            u = msg.get("usage")
            if isinstance(u, dict) and msg.get("role") == "assistant" and msg.get("id"):
                per_id[msg["id"]].append((i, u.get("output_tokens", 0), msg.get("model")))
    print(f"arquivo: {os.path.basename(path)}")
    print(f"linhas totais: {lines}")
    print(f"linhas-com-usage: {sum(len(v) for v in per_id.values())}")
    print(f"message.id distintos (após dedup): {len(per_id)}")
    dup = {k: v for k, v in per_id.items() if len(v) > 1}
    print(f"ids que aparecem em >1 linha: {len(dup)}")
    if dup:
        k = next(iter(dup))
        print(f"  exemplo id {k[:24]}...: {len(dup[k])} linhas, "
              f"output_tokens nelas = {sorted(set(x[1] for x in dup[k]))} "
              f"(idênticos => dedup correta)")
    tot_dedup = sum(v[0][1] for v in per_id.values())  # 1 por id
    tot_naive = sum(x[1] for v in per_id.values() for x in v)
    print(f"output_tokens DEDUP (1/id): {tot_dedup}")
    print(f"output_tokens NAIVE (por linha): {tot_naive}")
    print(f"fator de inflação evitado: {round(tot_naive/max(1,tot_dedup),2)}x")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Parser de usage do Claude Code (read-only).")
    ap.add_argument("--base", default=default_base(), help="dir base dos JSONL")
    ap.add_argument("--out", default="baseline_metrics.csv", help="CSV de saída")
    ap.add_argument("--include-sidechain", action="store_true",
                    help="incluir subagentes (default: separa/exclui da agregação)")
    ap.add_argument("--validate", metavar="JSONL", help="dump dedup de um arquivo p/ conferência")
    ap.add_argument("--until", metavar="ISO", help="janela fechada: só registros com timestamp < ISO")
    ap.add_argument("--since", metavar="ISO", help="janela fechada: só registros com timestamp >= ISO")
    ap.add_argument("--exclude-session", metavar="SID",
                    help="excluir uma sessão (ex.: a ativa, que ainda cresce) — p/ snapshot reproduzível")
    ap.add_argument("--snapshot", action="store_true",
                    help="modo A3: congela a janela e imprime SHA256 do CSV (hash em memória)")
    args = ap.parse_args(argv)

    if args.validate:
        validate(args.validate)
        return 0

    if not os.path.isdir(args.base):
        print(f"ERRO: base não existe: {args.base}", file=sys.stderr)
        return 2

    agg, synthetic, n_ids = aggregate(
        args.base, args.include_sidechain,
        until=args.until, since=args.since, exclude_session=args.exclude_session)
    write_csv(agg, args.out)

    tot_in = sum(r["input_tokens"] for r in agg.values())
    tot_out = sum(r["output_tokens"] for r in agg.values())
    tot_cr = sum(r["cache_read_input_tokens"] for r in agg.values())
    tot_cc = sum(r["cache_creation_input_tokens"] for r in agg.values())
    tot_cost = sum(r["est_cost_usd"] for r in agg.values() if not r["cost_is_null"])
    has_null = any(r["cost_is_null"] for r in agg.values())

    print(f"== parse_usage.py | base: ...{os.sep}{os.path.basename(args.base)}")
    print(f"linhas lidas: {iter_usage_records.total_lines} | parse-fails: {iter_usage_records.parse_fails}")
    print(f"message.id distintos (dedup global): {n_ids} | sintéticos excluídos: {synthetic}")
    print(f"grupos (sessão x modelo x sidechain): {len(agg)}")
    print(f"TOTAIS (dedup): input={tot_in:,} output={tot_out:,} "
          f"cache_read={tot_cr:,} cache_creation={tot_cc:,}")
    print(f"custo proxy USD: ${tot_cost:,.2f}  [{PRICE_TABLE_NOTE}]"
          + ("  (alguns grupos com custo NULL: modelo desconhecido)" if has_null else ""))
    print(f"CSV: {os.path.abspath(args.out)}")

    if args.snapshot:
        import hashlib
        with open(args.out, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        win = []
        if args.since: win.append(f"since={args.since}")
        if args.until: win.append(f"until={args.until}")
        if args.exclude_session: win.append(f"exclude_session={args.exclude_session}")
        print("-- SNAPSHOT A3 --")
        print(f"janela: {', '.join(win) if win else 'TODA (não fechada — não reproduzível!)'}")
        print(f"SHA256({os.path.basename(args.out)}) = {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
