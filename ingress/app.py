from fastapi import FastAPI
from services.ingress_service import process_message

app = FastAPI()

@app.post("/ingest")
async def ingest(message: dict):
    return await process_message(message)
