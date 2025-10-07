from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from ..database import db

router = APIRouter(prefix="/api", tags=["submissions"])

class SubmissionRequest(BaseModel):
    challenge_id: str
    code: str
    language: str = "python"

@router.post("/submit")
async def submit_code(request: SubmissionRequest) -> Dict:
    challenge = db.get_challenge_by_id(request.challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")

    submission = db.create_submission(
        challenge_id=request.challenge_id,
        code=request.code,
        language=request.language
    )

    return {
        "success": True,
        "submission_id": submission["id"],
        "message": "Code submitted successfully"
    }

@router.get("/submissions/{submission_id}")
async def get_submission(submission_id: str) -> Dict:
    submission = db.get_submission_by_id(submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    return submission

@router.get("/submissions")
async def get_recent_submissions(limit: int = 10) -> List[Dict]:
    return db.get_recent_submissions(limit)
