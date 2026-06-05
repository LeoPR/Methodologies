#!/usr/bin/env python3
"""
detect_env.py — protótipo detect-and-recommend (rascunho da recipe de ambiente IA).

Detecta o ambiente do dev (GPU, Ollama, Copilot, Anthropic, sync, permissão de
instalar), classifica num arquétipo, e emite DUAS saídas:
  1) HUMANO  — "você parece <arquétipo>": LIGAR AGORA / CONSIDERAR / BLOQUEADO (+por quê)
  2) MÁQUINA — environment-profile.yaml + routing_rules (para o agente de IA ler e rotear)

Invariantes (do confronto, workflow wdoc3jreq):
  - NUNCA recomenda um movimento cuja PRÉ-CONDIÇÃO a máquina viola.
  - Distingue bloqueio FÍSICO (sem GPU → evolua HW) de POLICY (DLP/sem-admin → escale ao IT).
  - Read-only: não instala nada; a própria detecção não deve violar policy.
  - Os números (16k, 8GB) são PARÂMETROS, não constantes — re-medir no HW real é o certo.

Uso:
  python detect_env.py                         # detecta esta máquina
  python detect_env.py --goal economia         # fixa a prioridade
  python detect_env.py --simulate perfil.json  # teoriza outro ambiente (sem detectar)
  python detect_env.py --emit-profile          # grava .ai/environment-profile.yaml
"""
from __future__ import annotations
import argparse, json, os, platform, shutil, socket, subprocess, sys, urllib.request

# Console Windows e cp1252 e nao imprime Unicode (->, ↳, ⚠). Ferramenta portavel
# forca UTF-8 por conta propria (licao de campo: cc-stats e este script bateram nisso).
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ----------------------------------------------------------------------------- detecção
def _run(cmd, timeout=6):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout.strip()
    except Exception:
        return ""

def detect_gpu():
    out = _run(["nvidia-smi", "--query-gpu=name,memory.total,memory.free",
                "--format=csv,noheader,nounits"])
    if not out:
        return {"present": False, "bucket": "none", "name": None, "vram_total_gb": 0, "vram_free_gb": 0}
    name, total, free = [x.strip() for x in out.splitlines()[0].split(",")[:3]]
    tot, fr = int(float(total)), int(float(free))
    gb = tot / 1024
    bucket = "16-24gb" if gb >= 15 else ("8-12gb_wddm" if gb >= 7.5 else "lt8gb")
    return {"present": True, "bucket": bucket, "name": name,
            "vram_total_gb": round(gb, 1), "vram_free_gb": round(fr / 1024, 1)}

def detect_ollama():
    try:
        with urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=2) as r:
            tags = json.loads(r.read().decode())
        models = [m.get("name") for m in tags.get("models", [])]
        return {"running": True, "models": models}
    except Exception:
        return {"running": False, "models": []}

def detect_copilot():
    ext = os.path.join(os.path.expanduser("~"), ".vscode", "extensions")
    found = []
    if os.path.isdir(ext):
        for d in os.listdir(ext):
            dl = d.lower()
            if "copilot" in dl or "windows-ai-studio" in dl or "continue" in dl:
                found.append(d)
    has_copilot = any("copilot" in f.lower() for f in found)
    has_continue = any("continue" in f.lower() for f in found)
    return {"extension_present": has_copilot, "continue_present": has_continue,
            "plan": "unknown", "relevant_ext": found}  # tier do plano não é detectável offline

def detect_anthropic():
    key = bool(os.environ.get("ANTHROPIC_API_KEY"))
    base = os.environ.get("ANTHROPIC_BASE_URL", "")
    claude_dir = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    cc = os.path.isdir(claude_dir)
    # regime: base_url local => não é API metada; key sem base => api_usd; .claude sem key => possivel Max
    if base and "11434" in base:
        regime = "ollama_local_backend"
    elif key:
        regime = "api_usd"
    elif cc:
        regime = "claude_max_or_subscription"
    else:
        regime = "none"
    return {"api_key": key, "base_url": base, "claude_code": cc, "regime": regime}

def detect_can_install():
    # CORREÇÃO (bug de campo): admin NÃO é requisito — winget/uv/ollama instalam
    # user-level. Default pode_instalar=True; só travar com SINAIS FORTES de policy
    # corporativa (MDM/DLP + egress externo bloqueado), nunca por "não sou admin".
    admin = None
    try:
        if platform.system() == "Windows":
            import ctypes
            admin = bool(ctypes.windll.shell32.IsUserAnAdmin())
        else:
            admin = (os.geteuid() == 0)
    except Exception:
        admin = None
    can_write_userland = os.access(os.path.expanduser("~"), os.W_OK)
    # egress: testar vários; só "bloqueado-externo" se há internet MAS as APIs caíram
    reach = []
    for host, port in [("api.anthropic.com", 443), ("api.openai.com", 443), ("github.com", 443)]:
        try:
            s = socket.create_connection((host, port), timeout=2); s.close(); reach.append(host)
        except Exception:
            pass
    internet = len(reach) > 0
    egress_blocked_external = internet and not ({"api.anthropic.com", "api.openai.com"} & set(reach))
    # sinais fortes de gestão corporativa (Windows MDM/Intune)
    policy_signals = []
    if platform.system() == "Windows":
        for marker in [os.path.join(os.environ.get("ProgramData", ""), "Microsoft", "DMClient"),
                       os.path.join(os.environ.get("ProgramData", ""), "Microsoft", "Windows Defender Advanced Threat Protection")]:
            if marker and os.path.isdir(marker):
                policy_signals.append(os.path.basename(marker))
    policy_locked = bool(policy_signals) and egress_blocked_external
    return {"admin": admin, "internet": internet, "reachable": reach,
            "egress_blocked_external": egress_blocked_external, "policy_signals": policy_signals,
            "policy_locked": policy_locked,
            "pode_instalar": bool(can_write_userland) and not policy_locked}

def detect_sync():
    cwd = os.getcwd().lower()
    home = os.path.expanduser("~").lower()
    markers = ["onedrive", "dropbox", "google drive", "googledrive"]
    in_sync = any(m in cwd for m in markers) or bool(os.environ.get("OneDrive"))
    # volume não-sync gravável (Windows: existe outro drive? Z:? D:?)
    vol = False
    if platform.system() == "Windows":
        for drv in ["Z:\\", "D:\\", "E:\\"]:
            if os.path.isdir(drv) and os.access(drv, os.W_OK):
                vol = True; break
    else:
        vol = os.access("/tmp", os.W_OK)
    return {"under_sync_folder": in_sync, "vol_nao_sync": vol}

def detect_disk():
    try:
        u = shutil.disk_usage(os.getcwd())
        return {"free_gb": round(u.free / 1e9, 1)}
    except Exception:
        return {"free_gb": None}

def _du_gb(path):
    """Soma tamanho (GB) de um diretorio — best-effort, stat-only."""
    if not path or not os.path.isdir(path):
        return None
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return round(total / 1e9, 2)

def _docker_ollama_store():
    """Acha o bind-mount do /root/.ollama do container ollama (caso real: M:\\ollama\\models)."""
    try:
        fmt = '{{range .Mounts}}{{if eq .Destination "/root/.ollama"}}{{.Source}}{{end}}{{end}}'
        out = subprocess.run(["docker", "inspect", "ollama", "--format", fmt],
                             capture_output=True, text=True, timeout=8).stdout.strip()
        if not out:
            return None
        # normalizar 'M://ollama/models' -> 'M:\ollama\models'
        p = out.replace("//", "\\").replace("/", "\\")
        cand = [out, p, os.path.join(p, "models")]
        for c in cand:
            if os.path.isdir(c):
                return c
        return out
    except Exception:
        return None

def detect_storage():
    """Volumes (free por volume) + localizacao de TODOS os stores de modelo + duplicacao.
    Cobre o caso real: Ollama em Docker bind-mount, com ~/.ollama default VAZIO."""
    home = os.path.expanduser("~")
    # volumes
    vols = []
    if platform.system() == "Windows":
        import string
        for L in string.ascii_uppercase:
            root = f"{L}:\\"
            if os.path.exists(root):
                try:
                    u = shutil.disk_usage(root)
                    vols.append({"vol": f"{L}:", "free_gb": round(u.free / 1e9), "total_gb": round(u.total / 1e9)})
                except Exception:
                    pass
    else:
        try:
            u = shutil.disk_usage("/")
            vols.append({"vol": "/", "free_gb": round(u.free / 1e9), "total_gb": round(u.total / 1e9)})
        except Exception:
            pass
    # stores (nome, path, formato)
    candidates = [
        ("ollama-default", os.path.join(home, ".ollama", "models"), "gguf"),
        ("ollama-env", os.environ.get("OLLAMA_MODELS"), "gguf"),
        ("ollama-docker", _docker_ollama_store(), "gguf"),
        ("lmstudio", os.path.join(home, ".lmstudio", "models"), "gguf"),
        ("lmstudio-cache", os.path.join(home, ".cache", "lm-studio", "models"), "gguf"),
        ("foundry-aitk", os.path.join(home, ".aitk", "models"), "onnx"),
        ("foundry-cache", os.path.join(home, ".foundry", "cache", "models"), "onnx"),
        ("gpt4all", os.path.join(home, ".cache", "gpt4all"), "gguf"),
    ]
    stores = []
    for name, path, fmt in candidates:
        if path and os.path.isdir(path):
            gb = _du_gb(path)
            if gb and gb > 0.05:
                stores.append({"name": name, "path": path, "format": fmt, "gb": gb})
    total_model_gb = round(sum(s["gb"] for s in stores), 1)
    # duplicacao (heuristica): >1 store GGUF com conteudo = evitavel; GGUF + ONNX = estrutural
    gguf = [s for s in stores if s["format"] == "gguf" and s["gb"] > 0.5]
    onnx = [s for s in stores if s["format"] == "onnx" and s["gb"] > 0.5]
    dup = []
    if len(gguf) > 1:
        dup.append({"kind": "evitavel", "msg": f"{len(gguf)} stores GGUF — consolidar em 1 (symlink/escolher engine)"})
    if gguf and onnx:
        dup.append({"kind": "estrutural", "msg": "GGUF + ONNX coexistem — mesmo modelo nos dois = 100% duplicado (formatos não compartilháveis)"})
    # reclaimable do docker
    reclaimable_gb = None
    try:
        out = subprocess.run(["docker", "system", "df", "--format", "{{.Reclaimable}}"],
                             capture_output=True, text=True, timeout=8).stdout
        import re
        gbs = [float(x) for x in re.findall(r"([\d.]+)GB", out)]
        if gbs:
            reclaimable_gb = round(sum(gbs), 1)
    except Exception:
        pass
    return {"volumes": vols, "stores": stores, "total_model_gb": total_model_gb,
            "duplication": dup, "reclaimable_gb": reclaimable_gb}

def detect_all():
    return {
        "os": platform.system(), "os_release": platform.release(),
        "wddm": platform.system() == "Windows",
        "gpu": detect_gpu(), "ollama": detect_ollama(), "copilot": detect_copilot(),
        "anthropic": detect_anthropic(), "install": detect_can_install(),
        "sync": detect_sync(), "disk": detect_disk(), "storage": detect_storage(),
    }

# ----------------------------------------------------------------------------- modelos com tool_use (allowlist empírica — STAGE3)
TOOLUSE_PASS = ["llama3.1:8b", "qwen3:14b"]
TOOLUSE_FAIL = ["qwen2.5-coder:7b"]

# ----------------------------------------------------------------------------- movimentos (pré-condições data-driven; do confronto)
def gpu_local_viable(e):
    return e["gpu"]["present"] and e["gpu"]["bucket"] in ("8-12gb_wddm", "16-24gb") and e["install"]["pode_instalar"]

def has_tooluse_model(e):
    return any(m in e["ollama"]["models"] for m in TOOLUSE_PASS)

def _store_on_system_drive(e):
    st = e.get("storage", {})
    sys_pref = "C:" if platform.system() == "Windows" else "/"
    return any(str(s.get("path", "")).startswith(sys_pref) and s.get("gb", 0) > 1 for s in st.get("stores", []))

def _has_bigger_volume(e):
    vols = e.get("storage", {}).get("volumes", [])
    return any(v.get("vol") not in ("C:", "/") and (v.get("free_gb") or 0) > 100 for v in vols)

def _disk_low(e):
    vols = e.get("storage", {}).get("volumes", [])
    sysv = [v for v in vols if v.get("vol") in ("C:", "/")]
    return any((v.get("free_gb") or 999) < 40 for v in sysv)

MOVES = [
    # id, desc, tier, precond(e)->bool, requires(set), teach
    # requires: o que o movimento EXIGE — usado para calcular o motivo do bloqueio
    # DINAMICAMENTE (físico se falta GPU; policy se não pode instalar). Conceito #5.
    ("M1", "Manter contexto enxuto (tirar distratores, nunca o sinal)", "T0", lambda e: True, (),
     "Inclua só o que tem relação causal com a tarefa; corte código morto/histórico solto."),
    ("M2", "Info crítica no início/fim do prompt (lost-in-the-middle)", "T0", lambda e: True, (),
     "Objetivo+pergunta+trechos críticos na 1ª e última posição; boilerplate no miolo."),
    ("M4", "Right-size do raciocínio (thinking on/off por dificuldade)", "T0", lambda e: True, (),
     "Trivial→thinking off; difícil→on. Overthinking dá <2% de ganho a ~20x custo."),
    ("T1-profile", "Perfil de ambiente legível por agente (.ai/environment-profile.yaml)", "T1", lambda e: True, (),
     "Deixe a ferramenta ciente do seu tier/regime: o agente roteia sozinho."),
    ("T1-git", "Git desde o dia 1 + .gitignore básico", "T1", lambda e: True, (),
     "Rede de segurança: tudo reversível. Mata o medo de quebrar."),
    ("M5", "Autocomplete inline ilimitado do Copilot", "T4", lambda e: e["copilot"]["extension_present"], ("copilot",),
     "Inline é multiplier-0 e ilimitado nos planos PAGOS (Free = cota). Não é o chat Sonnet."),
    ("M6", "Chat rotineiro nos modelos multiplier-0 (GPT-4.1/GPT-5-mini)", "T4", lambda e: e["copilot"]["extension_present"], ("copilot",),
     "Explicar/boilerplate/refactor leve sem consumir os 300 req/mês."),
    ("M3", "Reaproveitar prefixo estável via prompt caching", "T4",
     lambda e: e["anthropic"]["regime"] in ("api_usd", "claude_max_or_subscription", "ollama_local_backend"), ("regime",),
     "Conteúdo invariante byte-idêntico no INÍCIO; volátil (ids/timestamps) no FIM."),
    ("M9", "Ollama + qwen2.5-coder:7b para autocomplete local (FIM)", "T4", gpu_local_viable, ("gpu", "install"),
     "Sweet spot medido 7B@≤16k = ~55 t/s, TTFT 68ms. Precisa GPU ≥8GB livre."),
    ("M10", "Continue.dev ligado ao Ollama (autocomplete/chat local)", "T4", gpu_local_viable, ("gpu", "install"),
     "Config pronta em instrumento/continue-config-sugerida.yaml."),
    ("M11", "Claude Code → backend Ollama local (agêntico)", "T4",
     lambda e: gpu_local_viable(e) and has_tooluse_model(e) and e["anthropic"]["claude_code"], ("gpu", "install", "claude_code"),
     "SÓ com modelo tool_use=PASS (llama3.1:8b/qwen3:14b). ~20 t/s = marginal."),
    ("M12", "CLAUDE_CODE_SUBAGENT_MODEL=haiku (subagentes baratos)", "T4",
     lambda e: e["anthropic"]["claude_code"] and e["anthropic"]["regime"] in ("api_usd", "claude_max_or_subscription"), ("claude_code", "regime"),
     "Subagentes em Haiku; main em Sonnet. Só com fan-out real."),
    ("M13", "Pré-filtro de visão local (descreve/OCR antes do cloud)", "T4",
     lambda e: gpu_local_viable(e) and any("vl" in m or "vision" in m for m in e["ollama"]["models"]), ("gpu", "install"),
     "SÓ para OCR/extração; bypass em raciocínio visual fino. (qwen3-vl:8b cabe num 12GB)"),
    ("M14", "Instrumentar tokens (parser JSONL / cc-statistics)", "T4",
     lambda e: e["anthropic"]["regime"] in ("api_usd", "claude_max_or_subscription"), ("regime",),
     "Ver onde o custo vai. Reportar POR REGIME, nunca somar USD+quota+créditos."),
    ("M8", "Centralizar venv/cache fora do sync (junction p/ disco local)", "T4",
     lambda e: e["sync"]["under_sync_folder"] and e["sync"]["vol_nao_sync"] and e["install"]["pode_instalar"], ("install", "sync"),
     "No MESMO passo, adicione .venv/+caches ao .gitignore (senão o git rastreia o link)."),
    ("M15", "Capar contexto local ≤16k (classe 8-12GB WDDM)", "T4",
     lambda e: e["gpu"]["present"] and e["gpu"]["bucket"] == "8-12gb_wddm", ("gpu",),
     "A 32k há penhasco WDDM (~13 t/s). Se GPU ≥16GB: NÃO cape — re-meça o sweet spot."),
    ("M16", "Consolidar em 1 engine GGUF (não manter 2 stores do mesmo peso)", "T4",
     lambda e: len(e.get("storage", {}).get("duplication", [])) > 0, ("disco",),
     "Decida por disco+daemon+formato, não por t/s (single-user ~idêntico). Foundry/ONNX duplica 100%."),
    ("M17", "Redirecionar store p/ volume não-sistema (OLLAMA_MODELS=D:\\...)", "T4",
     lambda e: _store_on_system_drive(e) and _has_bigger_volume(e), ("disco",),
     "Tira os pesos do SSD do sistema. Cuidado: OLLAMA_HOME é ignorado no Windows; use OLLAMA_MODELS. (análogo ao M8)"),
    ("M18", "Higiene de store: remover modelos mortos + docker system prune", "T4",
     lambda e: (e.get("storage", {}).get("reclaimable_gb") or 0) > 3 or _disk_low(e), ("disco",),
     "Só reclaimable (sem perder modelo ativo). Análogo a 'rebaixar a superfície' do §3 do Strata."),
]

def block_reason(requires, e):
    """Motivo DINAMICO do bloqueio (físico vs policy vs estado) — conceito #5."""
    pode = e["install"].get("pode_instalar", True)
    gpu_ok = e["gpu"].get("present") and e["gpu"].get("bucket") in ("8-12gb_wddm", "16-24gb")
    if "install" in requires and not pode:
        return "policy", "fora do seu alcance — escale ao IT"
    if "gpu" in requires and not gpu_ok:
        return "physical", "evolua o hardware (GPU/VRAM)"
    if "copilot" in requires and not e["copilot"].get("extension_present"):
        return "policy", "requer Copilot pago detectável (ou habilitar no tenant)"
    if "claude_code" in requires and not e["anthropic"].get("claude_code"):
        return "estado", "requer Claude Code ativo"
    return "estado", "pré-condição de estado não satisfeita"

# ----------------------------------------------------------------------------- classificação
def classify(e):
    if not e["install"]["pode_instalar"]:
        return "A4", "conformidade"  # gate-mestre
    g = e["gpu"]["bucket"]; cop = e["copilot"]["extension_present"]
    if g == "none" or g == "lt8gb":
        return ("A1" if not cop else "A2"), "simplicidade"
    if g == "16-24gb":
        return "A3", "performance"
    if g == "8-12gb_wddm":
        return ("A5" if not cop else "A3"), ("economia" if not cop else "performance")
    return "custom", "simplicidade"

# ----------------------------------------------------------------------------- recomendação
def recommend(e):
    enable, consider, blocked = [], [], []
    for mid, desc, tier, pre, requires, teach in MOVES:
        ok = False
        try:
            ok = bool(pre(e))
        except Exception:
            ok = False
        item = {"id": mid, "desc": desc, "tier": tier, "teach": teach}
        if tier in ("T0", "T1"):
            (enable if tier == "T0" else consider).append(item)
        elif ok:
            enable.append(item)
        else:
            kind, msg = block_reason(requires, e)
            item["block_kind"] = kind
            item["block_msg"] = msg
            blocked.append(item)
    return {"enable_now": enable, "consider": consider, "blocked": blocked}

# ----------------------------------------------------------------------------- saídas
def render_human(e, arch, goal, recs):
    L = []
    g = e["gpu"]
    L.append(f"# Ambiente detectado → arquétipo {arch} · prioridade {goal}")
    L.append(f"OS={e.get('os','?')} {e.get('os_release','')} (WDDM={e.get('wddm')}) | GPU={g.get('name') or 'nenhuma'} "
             f"{g['vram_total_gb']}GB (livre {g['vram_free_gb']}GB, bucket {g['bucket']})")
    L.append(f"Ollama={'rodando, '+str(len(e['ollama']['models']))+' modelos' if e['ollama']['running'] else 'ausente'} | "
             f"Copilot ext={e['copilot']['extension_present']} | Anthropic regime={e['anthropic']['regime']} | "
             f"pode_instalar={e['install']['pode_instalar']} | sob_sync={e['sync']['under_sync_folder']}")
    L.append("")
    L.append("## LIGAR AGORA (T0 universal + T4 com pré-condição satisfeita)")
    for m in recs["enable_now"]:
        L.append(f"  [{m['tier']}] {m['id']:11} {m['desc']}")
        L.append(f"               ↳ {m['teach']}")
    L.append("\n## CONSIDERAR (T1 — baixo risco, você talvez não sabia)")
    for m in recs["consider"]:
        L.append(f"  [{m['tier']}] {m['id']:11} {m['desc']}")
    L.append("\n## BLOQUEADO AQUI (com a causa)")
    for m in recs["blocked"]:
        tag = "FÍSICO" if m["block_kind"] == "physical" else "POLICY" if m["block_kind"] == "policy" else "ESTADO"
        L.append(f"  [{tag}] {m['id']:11} {m['desc']} — {m['block_msg']}")
    # disco / stores de modelo
    st = e.get("storage", {})
    if st.get("stores") or st.get("volumes"):
        L.append("\n## DISCO E STORES DE MODELO")
        vols = ", ".join(f"{v['vol']} {v['free_gb']}GB livre" for v in st.get("volumes", []))
        L.append(f"  Volumes: {vols}")
        for s in st.get("stores", []):
            L.append(f"  store {s['name']} ({s['format']}): {s['gb']}GB em {s['path']}")
        if st.get("total_model_gb"):
            L.append(f"  TOTAL em modelos: {st['total_model_gb']}GB"
                     + (f" | reclaimable: {st['reclaimable_gb']}GB" if st.get("reclaimable_gb") else ""))
        for d in st.get("duplication", []):
            L.append(f"  ⚠ duplicação {d['kind']}: {d['msg']}")
    # armadilhas ativas
    L.append("\n## ARMADILHAS ATIVAS")
    L.append("  ⚠ Claude Sonnet no Copilot NÃO é grátis: 1x multiplier, consome a quota de 300 req/mês.")
    if e["sync"]["under_sync_folder"]:
        L.append("  ⚠ Projeto sob pasta sincronizada — venv/caches travam o sync; veja M8 (com .gitignore).")
    if g["bucket"] == "8-12gb_wddm":
        L.append("  ⚠ A 32k de contexto o decode despenca (penhasco WDDM). Fique ≤16k OU quiesça apps de fundo.")
    if g["bucket"] == "16-24gb":
        L.append("  ⚠ GPU ≥16GB: NÃO cape em 16k — re-meça o sweet spot (sobe p/ 32k+). Os números são parâmetros.")
    return "\n".join(L)

def render_profile(e, arch, goal):
    g = e["gpu"]
    local_viable = gpu_local_viable(e)
    tooluse = [m for m in e["ollama"]["models"] if m in TOOLUSE_PASS]
    lines = [
        "# .ai/environment-profile.yaml — gerado por detect_env.py (re-meça os números no SEU HW)",
        "profile:",
        f"  archetype: {arch}",
        f"  primary_goal: {goal}",
        f"  os: {e['os'].lower()}{'-wddm' if e['wddm'] else ''}",
        f"  gpu_bucket: {g['bucket']}",
        f"  vram_free_gb: {g['vram_free_gb']}",
        f"  local_inference_viable: {str(local_viable).lower()}",
        f"  ollama_running: {str(e['ollama']['running']).lower()}",
        f"  copilot_present: {str(e['copilot']['extension_present']).lower()}",
        f"  anthropic_regime: {e['anthropic']['regime']}",
        f"  pode_instalar: {str(e['install']['pode_instalar']).lower()}",
        f"  under_sync_folder: {str(e['sync']['under_sync_folder']).lower()}",
        f"  agent_tool_use_models: [{', '.join(tooluse) if tooluse else ''}]   # allowlist PASS (STAGE3)",
        f"  max_context_local: {16384 if g['bucket']=='8-12gb_wddm' else ('REMEDIR' if g['bucket']=='16-24gb' else 'n/a')}",
        "  cost_regimes_active:   # SEPARADOS — nunca somar",
        f"    credits_copilot: {str(e['copilot']['extension_present']).lower()}",
        f"    quota_max_5h: {str(e['anthropic']['regime']=='claude_max_or_subscription').lower()}",
        f"    usd_metered: {str(e['anthropic']['regime']=='api_usd').lower()}",
        "  human_gates: [revisar_antes_de_aceitar]",
        "",
        "routing_rules:   # o agente lê e obedece, em ordem",
        "  - SEMPRE: aplicar M1,M2,M4 + universais (output 2-6x input; K-quants; prefill/decode)",
        "  - autocomplete: copilot_inline se pago; senão FIM local (qwen2.5-coder:7b <= max_context_local) se viável",
        "  - chat_rotineiro: gpt-4.1/gpt-5-mini (multiplier-0); NUNCA assumir Sonnet gratis",
        "  - agentico_local: SO modelo de agent_tool_use_models; NUNCA qwen2.5-coder:7b (tool_use FAIL)",
        "  - hard/multi-arquivo: cloud frontier (cascata verificada se local); right-size por primary_goal",
        "  - NEVER: somar regimes de custo; localhost:11434 em corporativo; multiplier-0 em tarefa critica",
    ]
    return "\n".join(lines)

# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Detect-and-recommend de ambiente IA (read-only).")
    ap.add_argument("--goal", choices=["simplicidade", "economia", "performance", "qualidade", "conformidade"])
    ap.add_argument("--simulate", metavar="JSON", help="perfil de ambiente sintético (não detecta)")
    ap.add_argument("--emit-profile", action="store_true", help="grava .ai/environment-profile.yaml")
    ap.add_argument("--json", action="store_true", help="imprime o ambiente detectado como JSON")
    a = ap.parse_args()

    if a.simulate:
        with open(a.simulate, encoding="utf-8") as fh:
            e = json.load(fh)
        # preencher chaves faltantes com defaults seguros
        e.setdefault("os", "Windows"); e.setdefault("wddm", True); e.setdefault("os_release", "?")
        for k, dv in [("gpu", {"present": False, "bucket": "none", "name": None, "vram_total_gb": 0, "vram_free_gb": 0}),
                      ("ollama", {"running": False, "models": []}), ("copilot", {"extension_present": False, "continue_present": False}),
                      ("anthropic", {"regime": "none", "claude_code": False}), ("install", {"pode_instalar": True}),
                      ("sync", {"under_sync_folder": False, "vol_nao_sync": True}), ("disk", {"free_gb": None}),
                      ("storage", {"volumes": [], "stores": [], "total_model_gb": 0, "duplication": [], "reclaimable_gb": None})]:
            e.setdefault(k, dv)
    else:
        e = detect_all()

    if a.json:
        print(json.dumps(e, indent=2, ensure_ascii=False)); return

    arch, goal_guess = classify(e)
    goal = a.goal or goal_guess
    recs = recommend(e)
    print(render_human(e, arch, goal, recs))
    print("\n" + "=" * 60 + "\n# environment-profile.yaml (saída-máquina)\n")
    profile = render_profile(e, arch, goal)
    print(profile)
    if a.emit_profile:
        os.makedirs(".ai", exist_ok=True)
        with open(os.path.join(".ai", "environment-profile.yaml"), "w", encoding="utf-8") as fh:
            fh.write(profile + "\n")
        print("\n[gravado] .ai/environment-profile.yaml")


if __name__ == "__main__":
    main()
