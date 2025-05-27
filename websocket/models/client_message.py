from pydantic import BaseModel

class ClientMessage(BaseModel):
    user_id: str
    passed: bool
    errors: list[str]
