from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_grant_under_threshold():
    response = client.post("/validate-grant/", json={"organization_name": "Test NGO", "requested_amount": 10000, "project_summary": "Clean water"})
    assert response.status_code == 200
    assert response.json()["status"] == "APPROVED"

def test_grant_over_threshold():
    response = client.post("/validate-grant/", json={"organization_name": "Big Foundation", "requested_amount": 60000, "project_summary": "AI Research"})
    assert response.status_code == 200
    assert response.json()["status"] == "FLAGGED FOR REVIEW"