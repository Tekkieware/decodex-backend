from fastapi import WebSocket
from typing import Dict, List


class WebSocketAdapter:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, analysis_id: str):
        await websocket.accept()
        self.active_connections.setdefault(analysis_id, []).append(websocket)

    def disconnect(self, websocket: WebSocket, analysis_id: str):
        if analysis_id in self.active_connections:
            self.active_connections[analysis_id].remove(websocket)
            if not self.active_connections[analysis_id]:
                del self.active_connections[analysis_id]

    async def send_to_analysis(self, analysis_id: str, message: str):
        if analysis_id in self.active_connections:
            for connection in self.active_connections[analysis_id]:
                await connection.send_text(message)
