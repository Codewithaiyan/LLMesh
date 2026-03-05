# LLMesh 🔗

Distributed LLM inference platform with intelligent load balancing, autoscaling, and real-time observability on Kubernetes.

## Architecture
- **Ollama** — serves Mistral 7B as inference backend
- **FastAPI Router** — distributes requests across Ollama pods
- **Kubernetes + HPA** — orchestration and autoscaling
- **Prometheus + Grafana** — real-time observability

## Stack
Docker · Kubernetes · Minikube · FastAPI · Ollama · Prometheus · Grafana · k6

## Status
🚧 In Progress
