from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from ..database import db
from ..utils.ai_analyzer import analyzer

router = APIRouter(prefix="/api", tags=["feedback"])

class FeedbackRequest(BaseModel):
    submission_id: str

@router.post("/feedback")
async def get_ai_feedback(request: FeedbackRequest) -> Dict:
    submission = db.get_submission_by_id(request.submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    existing_feedback = db.get_feedback_by_submission_id(request.submission_id)
    if existing_feedback:
        return {
            "success": True,
            "feedback": existing_feedback["analysis"]
        }

    challenge = db.get_challenge_by_id(submission["challenge_id"])
    challenge_title = challenge["title"] if challenge else ""

    analysis = analyzer.analyze_code(
        code=submission["code"],
        language=submission["language"],
        challenge_title=challenge_title
    )

    feedback = db.create_feedback(
        submission_id=request.submission_id,
        analysis=analysis
    )

    db.update_submission_status(request.submission_id, "analyzed")

    return {
        "success": True,
        "feedback": analysis
    }

@router.get("/feedback/{submission_id}")
async def get_feedback_by_id(submission_id: str) -> Dict:
    feedback = db.get_feedback_by_submission_id(submission_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback
