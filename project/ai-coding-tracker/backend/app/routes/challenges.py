from fastapi import APIRouter, HTTPException
from typing import List, Dict
from ..database import db

router = APIRouter(prefix="/api", tags=["challenges"])

@router.get("/problems")
async def get_challenges() -> List[Dict]:
    return db.get_all_challenges()

@router.get("/problems/{challenge_id}")
async def get_challenge(challenge_id: str) -> Dict:
    challenge = db.get_challenge_by_id(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge
