#!/bin/bash

# Start Ollama server in background
ollama serve &

# Wait for it to be ready
echo "Waiting for Ollama to start..."
sleep 5

# Pull Mistral model
echo "Pulling Mistral model..."
ollama pull mistral

# Keep container running
wait
