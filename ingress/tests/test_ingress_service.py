from services.ingress_service import process_message
import pytest

@pytest.mark.asyncio
async def test_process_message():
    message = {"code": "print('Hello')", "language": "python", "user_id": "u1"}
    response = await process_message(message)
    assert response["status"] == "sent"
