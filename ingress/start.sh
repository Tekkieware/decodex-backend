
set -e

echo "Starting Analysis Worker..."
python -m analysis.worker &

echo "Starting FastAPI Server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
