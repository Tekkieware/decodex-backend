from pydantic import BaseModel

class AnalysisResult(BaseModel):
    user_id: str
    passed: bool
    errors: list[str]
