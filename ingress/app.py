from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from .services.ingress_service import process_message  

app = FastAPI()


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
