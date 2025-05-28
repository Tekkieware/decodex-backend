from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

from services.ingress_service import process_message

app = FastAPI()


class IngestRequest(BaseModel):
    """
    Schema for incoming ingestion requests.
    """
    code: str = Field(..., description="The source code to be analyzed")
    language: str = Field(..., description="Programming language of the code")
    user_id: str = Field(..., description="Unique identifier of the user")

    # Optional: You can add more field constraints or supported languages if needed
    # language: Literal["python", "javascript", "java", "c++"]


@app.post("/ingest", summary="Ingest a new code message")
async def ingest(message: IngestRequest):
    """
    Ingest an incoming code message and publish it to the Redis channel.

    Args:
        message (IngestRequest): Validated code message from the client.

    Returns:
        dict: Status message indicating success or failure.
    """
    try:
        # Convert validated Pydantic model to dictionary for processing
        result = await process_message(message.dict())
        return result
    except Exception as e:
        # If something unexpected happens, raise a 500 error
        raise HTTPException(status_code=500, detail=str(e))
