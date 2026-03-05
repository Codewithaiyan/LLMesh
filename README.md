# LLMesh 🔗

Distributed LLM inference platform with intelligent load balancing, autoscaling, and real-time observability on Kubernetes.

## Architecture
- **Ollama + phi3** — lightweight LLM inference backend
- **FastAPI Router** — round-robin load balancing across Ollama pods
- **Kubernetes (Minikube)** — orchestration with HPA autoscaling
- **Prometheus + Grafana** — real-time observability dashboard

## Stack
Docker · Kubernetes · Minikube · FastAPI · Ollama · Prometheus · Grafana · Helm

## Features
- ✅ Round-robin load balancing across multiple inference pods
- ✅ Prometheus metrics (request count, latency, per-pod tracking)
- ✅ Live Grafana dashboard
- ✅ Horizontal Pod Autoscaler (HPA)
- ✅ Model baked into Docker image for offline deployment

## Quick Start
```bash
minikube start --cpus=4 --memory=10240
eval $(minikube docker-env)
kubectl apply -f k8s/
```

## Results
- Average inference latency: ~1.6 seconds
- Round-robin proved across 2 pods
- Live metrics visible in Grafana
