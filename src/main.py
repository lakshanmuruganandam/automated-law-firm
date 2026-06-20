from fastapi import FastAPI
from src.api.router import api_router

app = FastAPI(
    title="Automated Law Firm",
    description="Local Autonomous Agents for Legal Drafting & Case Law Research",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "The AI partners are currently reviewing local laws."}
