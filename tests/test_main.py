from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "The AI partners are currently reviewing local laws."}

def test_draft_contract():
    response = client.post("/api/v1/draft/contract", json={
        "contract_type": "NDA", 
        "parties": ["Acme Corp", "Beta Inc"], 
        "jurisdiction": "Delaware"
    })
    assert response.status_code == 200
    assert "document" in response.json()
