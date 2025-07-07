from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from services.ingress_service import process_message, listen_to_results
from adapters.websocket_adapter import WebSocketAdapter
from fastapi.middleware.cors import CORSMiddleware

import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Shared WebSocket adapter
websocket_adapter = WebSocketAdapter()


@app.on_event("startup")
async def startup_event():
    # Start the listener to broadcast analysis results via WebSocket
    asyncio.create_task(listen_to_results(websocket_adapter))


@app.post("/analyze")
async def analyze(request: Request):
    try:
        payload = await request.json()

        result = await process_message(payload)

        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result["detail"])

        return JSONResponse(content=result, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.websocket("/a/{analysis_id}")
async def websocket_endpoint(websocket: WebSocket, analysis_id: str):
    await websocket_adapter.connect(websocket, analysis_id)
    try:
        while True:
            # Keep connection alive, can handle pings or client messages if needed
            await websocket.receive_text()
    except WebSocketDisconnect:
        websocket_adapter.disconnect(websocket, analysis_id)
