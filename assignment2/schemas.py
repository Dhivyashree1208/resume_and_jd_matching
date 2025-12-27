from pydantic import BaseModel

class ScreeningRequest(BaseModel):
    resume_text: str
    job_description: str


class ScreeningResponse(BaseModel):
    match_score: float
    decision: str
    reasons: list[str]
    confidence: str
