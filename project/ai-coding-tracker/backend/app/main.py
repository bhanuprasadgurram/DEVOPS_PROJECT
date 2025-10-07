from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from .routes import challenges, submissions, ai_feedback

app = FastAPI(title="AI Coding Tracker", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(challenges.router)
app.include_router(submissions.router)
app.include_router(ai_feedback.router)

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(static_path, "index.html"))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "AI Coding Tracker is running"}
