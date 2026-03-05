from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import httpx
import time
import itertools
import os

app = FastAPI(title="LLMesh Router")

# ─── Ollama pod URLs (loaded from env) ───────────────────────────────────────
OLLAMA_PODS = os.getenv("OLLAMA_PODS", "http://localhost:11434").split(",")
pod_cycle = itertools.cycle(OLLAMA_PODS)  # round-robin iterator

# ─── Prometheus Metrics ───────────────────────────────────────────────────────
REQUEST_COUNT = Counter(
    "llmesh_requests_total",
    "Total inference requests",
    ["pod", "status"]
)

REQUEST_LATENCY = Histogram(
    "llmesh_request_duration_seconds",
    "Inference request latency",
    ["pod"],
    buckets=[0.5, 1, 2, 5, 10, 20, 30, 60]
)

# ─── Routes ──────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "ok", "pods": OLLAMA_PODS}

@app.post("/generate")
async def generate(payload: dict):
    pod = next(pod_cycle)  # pick next pod in rotation
    start = time.time()

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{pod}/api/generate",
                json=payload
            )
        duration = time.time() - start

        REQUEST_COUNT.labels(pod=pod, status="success").inc()
        REQUEST_LATENCY.labels(pod=pod).observe(duration)

        return {
            "pod": pod,
            "duration_seconds": round(duration, 3),
            "response": response.json()
        }

    except Exception as e:
        duration = time.time() - start
        REQUEST_COUNT.labels(pod=pod, status="error").inc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

