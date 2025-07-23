#!/bin/bash
set -e

export PYTHONPATH=/app  # Make sure all folders (services, adapters, analysis) are importable

echo "Starting Analysis Worker..."
python analysis/app.py &

echo "Starting FastAPI Server..."
exec uvicorn app:app --host 0.0.0.0 --port 8000
