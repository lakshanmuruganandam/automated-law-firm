from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

def test_draft_contract():
    response = client.post("/api/v1/draft/contract", json={
        "contract_type": "NDA", 
        "parties": ["Acme Corp", "Beta Inc"], 
        "jurisdiction": "Delaware"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "document" in data
    assert "title" in data["document"]
    assert "content" in data["document"]
    assert "risk_score" in data["document"]
