"""SmartDesignerAI-4th (smartdesigner-ai-4th-astra) OpenAI-compatible client & verifier.

Model weights, Omni-Modal perception runtime, schema-constrained agent orchestrator,
HippoRAG 2 memory, and Sol-Class cognitive runtime are proprietary to Smart Designer.
For commercial licensing or authorized weight access, contact: msogabe@sdesigner.tokyo
"""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path
from typing import Any

ASTRA_MODEL_ID = "smartdesigner-ai-4th-astra"
EXPECTED_ADAPTER_SHA256 = "cae1902dac8a447179c155791d4d03755125746de392b10dd6e3c1a3b3c0a76b"
EXPECTED_OMNI_AGENT_V4_SHA256 = (
    "f2e198e8e43193bf305bfb2f64e33b6773789ee62aae5c307d0ec02692b942d1"
)


def verify_adapter_signature(adapter_file: Path) -> bool:
    """Verify that an authorized adapter_model.safetensors matches SmartDesignerAI-4th."""
    digest = hashlib.sha256(adapter_file.read_bytes()).hexdigest()
    return digest == EXPECTED_ADAPTER_SHA256


def verify_omni_agent_signature(agent_file: Path) -> bool:
    """Verify that omni_agent_v4.py matches the verified SmartDesignerAI-4th release."""
    digest = hashlib.sha256(agent_file.read_bytes()).hexdigest()
    return digest == EXPECTED_OMNI_AGENT_V4_SHA256


def create_chat_completion(
    messages: list[dict[str, Any]],
    *,
    endpoint: str = "http://127.0.0.1:8787",
    tools: list[dict[str, Any]] | None = None,
    parallel_tool_calls: bool = True,
) -> dict[str, Any]:
    """Call `/v1/chat/completions` on a SmartDesignerAI-4th Astra endpoint."""
    body: dict[str, Any] = {
        "model": ASTRA_MODEL_ID,
        "messages": messages,
    }
    if tools is not None:
        body["tools"] = tools
        body["parallel_tool_calls"] = parallel_tool_calls
    payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{endpoint.rstrip('/')}/v1/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
        return dict(json.loads(resp.read().decode("utf-8")))
