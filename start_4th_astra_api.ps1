param(
    [string]$BindHost = "127.0.0.1",
    [int]$Port = 8787
)

$ErrorActionPreference = "Stop"
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " SmartDesignerAI-4th (Astra / Opus 5.5 Class Omni-Agent) API" -ForegroundColor Cyan
Write-Host " Model ID : smartdesigner-ai-4th-astra" -ForegroundColor Green
Write-Host " Endpoint : http://${BindHost}:${Port}/v1/chat/completions" -ForegroundColor Green
Write-Host " Audio    : /v1/audio/transcriptions | /v1/audio/speech" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan

python -m src.service.openai_compat --host $BindHost --port $Port
