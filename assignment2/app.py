from fastapi import FastAPI
from assignment2.schemas import ScreeningRequest, ScreeningResponse
from assignment2.decision_logic import get_decision
from assignment1.scoring import calculate_match_score

app = FastAPI(
    title="AI Resume Screening Service",
    description="Screens resumes against job descriptions using explainable NLP",
    version="1.0"
)


@app.post("/screen", response_model=ScreeningResponse)
def screen_candidate(data: ScreeningRequest):

    # Edge case: empty or very short resume
    if len(data.resume_text.strip()) < 50:
        return ScreeningResponse(
            match_score=0.0,
            decision="Reject",
            reasons=["Resume too short"],
            confidence="Low"
        )

    score, _, _, matched_skills = calculate_match_score(
        data.resume_text,
        data.job_description
    )

    decision, confidence = get_decision(score)

    return ScreeningResponse(
        match_score=score,
        decision=decision,
        reasons=matched_skills,
        confidence=confidence
    )
