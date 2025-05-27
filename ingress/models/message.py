from pydantic import BaseModel

class Message(BaseModel):
    code: str
    language: str
    user_id: str
