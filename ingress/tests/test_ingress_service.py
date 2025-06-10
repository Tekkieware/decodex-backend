from services.ingress_service import process_message
import pytest

@pytest.mark.asyncio
async def test_process_message():
    message = {"code": "print('Hello')", "language": "python"}
    response = await process_message(message)
    assert response["status"] == "sent"
