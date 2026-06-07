param(
    [string]$PythonExe = ".venv/Scripts/python.exe",
    [string]$Method = "lab/2026-06-04-strata-hipoteses/hb-kit/strata-an-v1.md",
    [string[]]$Scenarios = @("s03-simples", "s01-comum-brownfield", "s04-bem-formatado"),
    [int]$CtxMin = 4096,
    [int]$CtxMax = 12288,
    [int]$Runs = 1,
    [double]$TargetPassRate = 1.0,
    [int]$TimeoutS = 120,
    [string[]]$ModelIds = @(
        "qwen3-1.7b",
        "gemma3-4b",
        "llama3.1-8b",
        "qwen2.5-coder-7b",
        "qwen3-8b"
    ),
    [hashtable]$ModelIdToOllamaName = @{
        "qwen3-1.7b"       = "qwen3:1.7b"
        "gemma3-4b"        = "gemma3:4b"
        "llama3.1-8b"      = "llama3.1:8b"
        "qwen2.5-coder-7b" = "qwen2.5-coder:7b"
        "qwen3-8b"         = "qwen3:8b"
    },
    [switch]$StopAfterEach = $true
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-Warmup {
    param([string]$ModelName)
    Write-Host "WARMUP -> $ModelName"
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    & ollama run $ModelName "ok" | Out-Null
    $sw.Stop()
    Write-Host ("  warmup_ok elapsed={0:n1}s" -f $sw.Elapsed.TotalSeconds)
}

function Invoke-StopModel {
    param([string]$ModelName)
    try {
        & ollama stop $ModelName | Out-Null
        Write-Host "  stopped $ModelName"
    }
    catch {
        Write-Host "  stop_failed ${ModelName}: $($_.Exception.Message)"
    }
}

$pythonPath = Join-Path (Get-Location) $PythonExe
if (-not (Test-Path $pythonPath)) {
    throw "Python nao encontrado em: $pythonPath"
}

foreach ($modelId in $ModelIds) {
    if (-not $ModelIdToOllamaName.ContainsKey($modelId)) {
        throw "ModelId sem mapeamento para nome Ollama: $modelId"
    }

    $modelName = $ModelIdToOllamaName[$modelId]
    Write-Host "`n===== MODEL $modelId ($modelName) ====="

    Invoke-Warmup -ModelName $modelName

    $args = @(
        "lab/2026-06-04-strata-hipoteses/hb-kit/hb_limit_search.py",
        "--method", $Method,
        "--only-model", $modelId,
        "--only-scenario"
    ) + $Scenarios + @(
        "--ctx-min", "$CtxMin",
        "--ctx-max", "$CtxMax",
        "--runs", "$Runs",
        "--target-pass-rate", "$TargetPassRate",
        "--timeout-s", "$TimeoutS"
    )

    Write-Host "RUN -> hb_limit_search ($modelId)"
    & $pythonPath $args

    if ($LASTEXITCODE -ne 0) {
        Write-Host "  run_failed model=$modelId exit=$LASTEXITCODE"
    }
    else {
        Write-Host "  run_ok model=$modelId"
    }

    if ($StopAfterEach) {
        Invoke-StopModel -ModelName $modelName
    }
}

Write-Host "`nSerial limit-search finalizado."
