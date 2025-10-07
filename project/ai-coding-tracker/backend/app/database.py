from typing import List, Dict, Optional
from datetime import datetime
import uuid

class Database:
    def __init__(self):
        self.challenges: List[Dict] = [
            {
                "id": str(uuid.uuid4()),
                "title": "Two Sum",
                "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution.",
                "difficulty": "easy",
                "test_cases": [
                    {"input": "[2,7,11,15], 9", "output": "[0,1]"},
                    {"input": "[3,2,4], 6", "output": "[1,2]"}
                ],
                "created_at": datetime.utcnow().isoformat()
            },
            {
                "id": str(uuid.uuid4()),
                "title": "Reverse String",
                "description": "Write a function that reverses a string. The input string is given as an array of characters.",
                "difficulty": "easy",
                "test_cases": [
                    {"input": "hello", "output": "olleh"},
                    {"input": "world", "output": "dlrow"}
                ],
                "created_at": datetime.utcnow().isoformat()
            },
            {
                "id": str(uuid.uuid4()),
                "title": "Palindrome Check",
                "description": "Given a string s, return true if it is a palindrome, otherwise return false. A palindrome is a string that reads the same forward and backward.",
                "difficulty": "easy",
                "test_cases": [
                    {"input": "racecar", "output": "true"},
                    {"input": "hello", "output": "false"}
                ],
                "created_at": datetime.utcnow().isoformat()
            },
            {
                "id": str(uuid.uuid4()),
                "title": "FizzBuzz",
                "description": "Write a function that returns an array of strings from 1 to n. For multiples of 3, add 'Fizz', for multiples of 5, add 'Buzz', and for multiples of both add 'FizzBuzz'.",
                "difficulty": "easy",
                "test_cases": [
                    {"input": "15", "output": "['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz']"}
                ],
                "created_at": datetime.utcnow().isoformat()
            }
        ]
        self.submissions: List[Dict] = []
        self.feedback: List[Dict] = []

    def get_all_challenges(self) -> List[Dict]:
        return self.challenges

    def get_challenge_by_id(self, challenge_id: str) -> Optional[Dict]:
        for challenge in self.challenges:
            if challenge["id"] == challenge_id:
                return challenge
        return None

    def create_submission(self, challenge_id: str, code: str, language: str) -> Dict:
        submission = {
            "id": str(uuid.uuid4()),
            "challenge_id": challenge_id,
            "code": code,
            "language": language,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }
        self.submissions.append(submission)
        return submission

    def get_submission_by_id(self, submission_id: str) -> Optional[Dict]:
        for submission in self.submissions:
            if submission["id"] == submission_id:
                return submission
        return None

    def update_submission_status(self, submission_id: str, status: str):
        for submission in self.submissions:
            if submission["id"] == submission_id:
                submission["status"] = status
                break

    def create_feedback(self, submission_id: str, analysis: Dict) -> Dict:
        feedback_entry = {
            "id": str(uuid.uuid4()),
            "submission_id": submission_id,
            "analysis": analysis,
            "created_at": datetime.utcnow().isoformat()
        }
        self.feedback.append(feedback_entry)
        return feedback_entry

    def get_feedback_by_submission_id(self, submission_id: str) -> Optional[Dict]:
        for feedback_entry in self.feedback:
            if feedback_entry["submission_id"] == submission_id:
                return feedback_entry
        return None

    def get_recent_submissions(self, limit: int = 10) -> List[Dict]:
        return sorted(self.submissions, key=lambda x: x["created_at"], reverse=True)[:limit]

db = Database()
