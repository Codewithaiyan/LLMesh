FROM ollama/ollama:latest

COPY ollama_models /root/.ollama/models
COPY LLMesh/ollama/start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 11434

ENTRYPOINT ["/app/start.sh"]
